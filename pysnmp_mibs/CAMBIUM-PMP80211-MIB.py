# SNMP MIB module (CAMBIUM-PMP80211-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-PMP80211-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:46 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

pmpMibTree = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21)
)
if mibBuilder.loadTexts:
    pmpMibTree.setRevisions(
        ("2020-02-13 19:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cambium_ObjectIdentity = ObjectIdentity
cambium = _Cambium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_Cambiumpmp80211SystemTraps_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemTraps = _Cambiumpmp80211SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0)
)
_CambiumPmp80211SystemStatus_ObjectIdentity = ObjectIdentity
cambiumPmp80211SystemStatus = _CambiumPmp80211SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1)
)
_CambiumGeneralStatus_ObjectIdentity = ObjectIdentity
cambiumGeneralStatus = _CambiumGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1)
)


class _CambiumCurrentSWInfo_Type(DisplayString):
    """Custom type cambiumCurrentSWInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumCurrentSWInfo_Type.__name__ = "DisplayString"
_CambiumCurrentSWInfo_Object = MibScalar
cambiumCurrentSWInfo = _CambiumCurrentSWInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 1),
    _CambiumCurrentSWInfo_Type()
)
cambiumCurrentSWInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentSWInfo.setStatus("current")


class _CambiumHWInfo_Type(Integer32):
    """Custom type cambiumHWInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 6),
        ValueRangeConstraint(8, 14),
        ValueRangeConstraint(16, 20),
        ValueRangeConstraint(22, 22),
        ValueRangeConstraint(33, 55),
        ValueRangeConstraint(59, 62),
        ValueRangeConstraint(100, 250),
        ValueRangeConstraint(53264, 53561),
    )


_CambiumHWInfo_Type.__name__ = "Integer32"
_CambiumHWInfo_Object = MibScalar
cambiumHWInfo = _CambiumHWInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 2),
    _CambiumHWInfo_Type()
)
cambiumHWInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumHWInfo.setStatus("current")


class _CambiumDateTime_Type(DisplayString):
    """Custom type cambiumDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumDateTime_Type.__name__ = "DisplayString"
_CambiumDateTime_Object = MibScalar
cambiumDateTime = _CambiumDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 3),
    _CambiumDateTime_Type()
)
cambiumDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDateTime.setStatus("current")


class _CambiumSystemUptime_Type(DisplayString):
    """Custom type cambiumSystemUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumSystemUptime_Type.__name__ = "DisplayString"
_CambiumSystemUptime_Object = MibScalar
cambiumSystemUptime = _CambiumSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 4),
    _CambiumSystemUptime_Type()
)
cambiumSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSystemUptime.setStatus("current")


class _CambiumWirelessMACAddress_Type(DisplayString):
    """Custom type cambiumWirelessMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumWirelessMACAddress_Type.__name__ = "DisplayString"
_CambiumWirelessMACAddress_Object = MibScalar
cambiumWirelessMACAddress = _CambiumWirelessMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 5),
    _CambiumWirelessMACAddress_Type()
)
cambiumWirelessMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWirelessMACAddress.setStatus("current")


class _CambiumDFSStatus_Type(Integer32):
    """Custom type cambiumDFSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CambiumDFSStatus_Type.__name__ = "Integer32"
_CambiumDFSStatus_Object = MibScalar
cambiumDFSStatus = _CambiumDFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 6),
    _CambiumDFSStatus_Type()
)
cambiumDFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFSStatus.setStatus("current")


class _CambiumEffectiveSyncSource_Type(Integer32):
    """Custom type cambiumEffectiveSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_CambiumEffectiveSyncSource_Type.__name__ = "Integer32"
_CambiumEffectiveSyncSource_Object = MibScalar
cambiumEffectiveSyncSource = _CambiumEffectiveSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 7),
    _CambiumEffectiveSyncSource_Type()
)
cambiumEffectiveSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSyncSource.setStatus("current")


class _CambiumEffectiveCountryCode_Type(DisplayString):
    """Custom type cambiumEffectiveCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CambiumEffectiveCountryCode_Type.__name__ = "DisplayString"
_CambiumEffectiveCountryCode_Object = MibScalar
cambiumEffectiveCountryCode = _CambiumEffectiveCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 8),
    _CambiumEffectiveCountryCode_Type()
)
cambiumEffectiveCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveCountryCode.setStatus("current")


class _CambiumEffectiveAntennaGain_Type(Integer32):
    """Custom type cambiumEffectiveAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_CambiumEffectiveAntennaGain_Type.__name__ = "Integer32"
_CambiumEffectiveAntennaGain_Object = MibScalar
cambiumEffectiveAntennaGain = _CambiumEffectiveAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 9),
    _CambiumEffectiveAntennaGain_Type()
)
cambiumEffectiveAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveAntennaGain.setStatus("current")


class _CambiumEffectiveTDDRatio_Type(Integer32):
    """Custom type cambiumEffectiveTDDRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
    )


_CambiumEffectiveTDDRatio_Type.__name__ = "Integer32"
_CambiumEffectiveTDDRatio_Object = MibScalar
cambiumEffectiveTDDRatio = _CambiumEffectiveTDDRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 10),
    _CambiumEffectiveTDDRatio_Type()
)
cambiumEffectiveTDDRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveTDDRatio.setStatus("current")


class _CambiumEffectiveSSID_Type(DisplayString):
    """Custom type cambiumEffectiveSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumEffectiveSSID_Type.__name__ = "DisplayString"
_CambiumEffectiveSSID_Object = MibScalar
cambiumEffectiveSSID = _CambiumEffectiveSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 11),
    _CambiumEffectiveSSID_Type()
)
cambiumEffectiveSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSSID.setStatus("current")


class _CambiumEffectiveAuthenticationType_Type(Integer32):
    """Custom type cambiumEffectiveAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_CambiumEffectiveAuthenticationType_Type.__name__ = "Integer32"
_CambiumEffectiveAuthenticationType_Object = MibScalar
cambiumEffectiveAuthenticationType = _CambiumEffectiveAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 12),
    _CambiumEffectiveAuthenticationType_Type()
)
cambiumEffectiveAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveAuthenticationType.setStatus("current")


class _CambiumEffectiveDeviceName_Type(DisplayString):
    """Custom type cambiumEffectiveDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumEffectiveDeviceName_Type.__name__ = "DisplayString"
_CambiumEffectiveDeviceName_Object = MibScalar
cambiumEffectiveDeviceName = _CambiumEffectiveDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 13),
    _CambiumEffectiveDeviceName_Type()
)
cambiumEffectiveDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceName.setStatus("current")


class _CambiumUbootVersion_Type(DisplayString):
    """Custom type cambiumUbootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumUbootVersion_Type.__name__ = "DisplayString"
_CambiumUbootVersion_Object = MibScalar
cambiumUbootVersion = _CambiumUbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 14),
    _CambiumUbootVersion_Type()
)
cambiumUbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumUbootVersion.setStatus("current")


class _CambiumLANMACAddress_Type(DisplayString):
    """Custom type cambiumLANMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumLANMACAddress_Type.__name__ = "DisplayString"
_CambiumLANMACAddress_Object = MibScalar
cambiumLANMACAddress = _CambiumLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 15),
    _CambiumLANMACAddress_Type()
)
cambiumLANMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANMACAddress.setStatus("current")


class _CambiumCurrentuImageIVersion_Type(DisplayString):
    """Custom type cambiumCurrentuImageIVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CambiumCurrentuImageIVersion_Type.__name__ = "DisplayString"
_CambiumCurrentuImageIVersion_Object = MibScalar
cambiumCurrentuImageIVersion = _CambiumCurrentuImageIVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 16),
    _CambiumCurrentuImageIVersion_Type()
)
cambiumCurrentuImageIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentuImageIVersion.setStatus("current")


class _CambiumCurrentuImageVersion_Type(DisplayString):
    """Custom type cambiumCurrentuImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CambiumCurrentuImageVersion_Type.__name__ = "DisplayString"
_CambiumCurrentuImageVersion_Object = MibScalar
cambiumCurrentuImageVersion = _CambiumCurrentuImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 17),
    _CambiumCurrentuImageVersion_Type()
)
cambiumCurrentuImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentuImageVersion.setStatus("current")
_CambiumDeviceLatitude_Type = DisplayString
_CambiumDeviceLatitude_Object = MibScalar
cambiumDeviceLatitude = _CambiumDeviceLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 18),
    _CambiumDeviceLatitude_Type()
)
cambiumDeviceLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceLatitude.setStatus("current")
_CambiumDeviceLongitude_Type = DisplayString
_CambiumDeviceLongitude_Object = MibScalar
cambiumDeviceLongitude = _CambiumDeviceLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 19),
    _CambiumDeviceLongitude_Type()
)
cambiumDeviceLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceLongitude.setStatus("current")
_SysRebootCounter_Type = Integer32
_SysRebootCounter_Object = MibScalar
sysRebootCounter = _SysRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 20),
    _SysRebootCounter_Type()
)
sysRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRebootCounter.setStatus("current")


class _CambiumDFSStatusStr_Type(DisplayString):
    """Custom type cambiumDFSStatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDFSStatusStr_Type.__name__ = "DisplayString"
_CambiumDFSStatusStr_Object = MibScalar
cambiumDFSStatusStr = _CambiumDFSStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 21),
    _CambiumDFSStatusStr_Type()
)
cambiumDFSStatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFSStatusStr.setStatus("current")


class _CambiumDriverType_Type(Integer32):
    """Custom type cambiumDriverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumDriverType_Type.__name__ = "Integer32"
_CambiumDriverType_Object = MibScalar
cambiumDriverType = _CambiumDriverType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 22),
    _CambiumDriverType_Type()
)
cambiumDriverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDriverType.setStatus("current")


class _CambiumSFPMACAddress_Type(DisplayString):
    """Custom type cambiumSFPMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumSFPMACAddress_Type.__name__ = "DisplayString"
_CambiumSFPMACAddress_Object = MibScalar
cambiumSFPMACAddress = _CambiumSFPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 23),
    _CambiumSFPMACAddress_Type()
)
cambiumSFPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPMACAddress.setStatus("current")
_SysSoftRebootCounter_Type = Integer32
_SysSoftRebootCounter_Object = MibScalar
sysSoftRebootCounter = _SysSoftRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 25),
    _SysSoftRebootCounter_Type()
)
sysSoftRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftRebootCounter.setStatus("current")
_SysHardRebootCounter_Type = Integer32
_SysHardRebootCounter_Object = MibScalar
sysHardRebootCounter = _SysHardRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 26),
    _SysHardRebootCounter_Type()
)
sysHardRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardRebootCounter.setStatus("current")
_SysConfigFlashStatus_Type = Integer32
_SysConfigFlashStatus_Object = MibScalar
sysConfigFlashStatus = _SysConfigFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 27),
    _SysConfigFlashStatus_Type()
)
sysConfigFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigFlashStatus.setStatus("current")
_SysWDTRebootCounter_Type = Integer32
_SysWDTRebootCounter_Object = MibScalar
sysWDTRebootCounter = _SysWDTRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 28),
    _SysWDTRebootCounter_Type()
)
sysWDTRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWDTRebootCounter.setStatus("current")


class _CambiumESN_Type(DisplayString):
    """Custom type cambiumESN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixed_length = 13


_CambiumESN_Type.__name__ = "DisplayString"
_CambiumESN_Object = MibScalar
cambiumESN = _CambiumESN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 30),
    _CambiumESN_Type()
)
cambiumESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumESN.setStatus("current")


class _CambiumEPMPMSN_Type(DisplayString):
    """Custom type cambiumEPMPMSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_CambiumEPMPMSN_Type.__name__ = "DisplayString"
_CambiumEPMPMSN_Object = MibScalar
cambiumEPMPMSN = _CambiumEPMPMSN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 31),
    _CambiumEPMPMSN_Type()
)
cambiumEPMPMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEPMPMSN.setStatus("current")


class _CambiumFactoryReset_Type(Integer32):
    """Custom type cambiumFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumFactoryReset_Type.__name__ = "Integer32"
_CambiumFactoryReset_Object = MibScalar
cambiumFactoryReset = _CambiumFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 32),
    _CambiumFactoryReset_Type()
)
cambiumFactoryReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFactoryReset.setStatus("current")


class _CambiumSubModeType_Type(Integer32):
    """Custom type cambiumSubModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(6, 6),
    )


_CambiumSubModeType_Type.__name__ = "Integer32"
_CambiumSubModeType_Object = MibScalar
cambiumSubModeType = _CambiumSubModeType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 33),
    _CambiumSubModeType_Type()
)
cambiumSubModeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSubModeType.setStatus("current")


class _CambiumDAVersion_Type(DisplayString):
    """Custom type cambiumDAVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_CambiumDAVersion_Type.__name__ = "DisplayString"
_CambiumDAVersion_Object = MibScalar
cambiumDAVersion = _CambiumDAVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 35),
    _CambiumDAVersion_Type()
)
cambiumDAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDAVersion.setStatus("current")


class _EPMP2000PowerSupplyStatus_Type(Integer32):
    """Custom type ePMP2000PowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_EPMP2000PowerSupplyStatus_Type.__name__ = "Integer32"
_EPMP2000PowerSupplyStatus_Object = MibScalar
ePMP2000PowerSupplyStatus = _EPMP2000PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 40),
    _EPMP2000PowerSupplyStatus_Type()
)
ePMP2000PowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000PowerSupplyStatus.setStatus("current")


class _EPMP2000SmartAntennaStatus_Type(Integer32):
    """Custom type ePMP2000SmartAntennaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_EPMP2000SmartAntennaStatus_Type.__name__ = "Integer32"
_EPMP2000SmartAntennaStatus_Object = MibScalar
ePMP2000SmartAntennaStatus = _EPMP2000SmartAntennaStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 41),
    _EPMP2000SmartAntennaStatus_Type()
)
ePMP2000SmartAntennaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000SmartAntennaStatus.setStatus("current")


class _EPMP2000ULAntennaStatus_Type(Integer32):
    """Custom type ePMP2000ULAntennaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_EPMP2000ULAntennaStatus_Type.__name__ = "Integer32"
_EPMP2000ULAntennaStatus_Object = MibScalar
ePMP2000ULAntennaStatus = _EPMP2000ULAntennaStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 42),
    _EPMP2000ULAntennaStatus_Type()
)
ePMP2000ULAntennaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000ULAntennaStatus.setStatus("current")


class _EPMP2000FPGALoadStatus_Type(Integer32):
    """Custom type ePMP2000FPGALoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-31, 1),
    )


_EPMP2000FPGALoadStatus_Type.__name__ = "Integer32"
_EPMP2000FPGALoadStatus_Object = MibScalar
ePMP2000FPGALoadStatus = _EPMP2000FPGALoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 43),
    _EPMP2000FPGALoadStatus_Type()
)
ePMP2000FPGALoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000FPGALoadStatus.setStatus("current")


class _CambiumSTAForceAntennaSelection_Type(Integer32):
    """Custom type cambiumSTAForceAntennaSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumSTAForceAntennaSelection_Type.__name__ = "Integer32"
_CambiumSTAForceAntennaSelection_Object = MibScalar
cambiumSTAForceAntennaSelection = _CambiumSTAForceAntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 44),
    _CambiumSTAForceAntennaSelection_Type()
)
cambiumSTAForceAntennaSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAForceAntennaSelection.setStatus("current")


class _CambiumSTALinktestForceSelection_Type(Integer32):
    """Custom type cambiumSTALinktestForceSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumSTALinktestForceSelection_Type.__name__ = "Integer32"
_CambiumSTALinktestForceSelection_Object = MibScalar
cambiumSTALinktestForceSelection = _CambiumSTALinktestForceSelection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 45),
    _CambiumSTALinktestForceSelection_Type()
)
cambiumSTALinktestForceSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTALinktestForceSelection.setStatus("current")
_CambiumEffectiveNTPServers_Type = IpAddress
_CambiumEffectiveNTPServers_Object = MibScalar
cambiumEffectiveNTPServers = _CambiumEffectiveNTPServers_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 46),
    _CambiumEffectiveNTPServers_Type()
)
cambiumEffectiveNTPServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNTPServers.setStatus("current")


class _CambiumNTPDateState_Type(Integer32):
    """Custom type cambiumNTPDateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumNTPDateState_Type.__name__ = "Integer32"
_CambiumNTPDateState_Object = MibScalar
cambiumNTPDateState = _CambiumNTPDateState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 47),
    _CambiumNTPDateState_Type()
)
cambiumNTPDateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumNTPDateState.setStatus("current")


class _CambiumMCUVersion_Type(DisplayString):
    """Custom type cambiumMCUVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumMCUVersion_Type.__name__ = "DisplayString"
_CambiumMCUVersion_Object = MibScalar
cambiumMCUVersion = _CambiumMCUVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 50),
    _CambiumMCUVersion_Type()
)
cambiumMCUVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMCUVersion.setStatus("current")


class _CambiumWireless2MACAddress_Type(DisplayString):
    """Custom type cambiumWireless2MACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumWireless2MACAddress_Type.__name__ = "DisplayString"
_CambiumWireless2MACAddress_Object = MibScalar
cambiumWireless2MACAddress = _CambiumWireless2MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 51),
    _CambiumWireless2MACAddress_Type()
)
cambiumWireless2MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWireless2MACAddress.setStatus("current")


class _CambiumDFS2Status_Type(Integer32):
    """Custom type cambiumDFS2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CambiumDFS2Status_Type.__name__ = "Integer32"
_CambiumDFS2Status_Object = MibScalar
cambiumDFS2Status = _CambiumDFS2Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 52),
    _CambiumDFS2Status_Type()
)
cambiumDFS2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFS2Status.setStatus("current")


class _CambiumEffectiveSSID2_Type(DisplayString):
    """Custom type cambiumEffectiveSSID2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumEffectiveSSID2_Type.__name__ = "DisplayString"
_CambiumEffectiveSSID2_Object = MibScalar
cambiumEffectiveSSID2 = _CambiumEffectiveSSID2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 53),
    _CambiumEffectiveSSID2_Type()
)
cambiumEffectiveSSID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSSID2.setStatus("current")


class _CambiumDFS2StatusStr_Type(DisplayString):
    """Custom type cambiumDFS2StatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDFS2StatusStr_Type.__name__ = "DisplayString"
_CambiumDFS2StatusStr_Object = MibScalar
cambiumDFS2StatusStr = _CambiumDFS2StatusStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 54),
    _CambiumDFS2StatusStr_Type()
)
cambiumDFS2StatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFS2StatusStr.setStatus("current")


class _CrashReporterKernelDataAvailable_Type(Integer32):
    """Custom type crashReporterKernelDataAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CrashReporterKernelDataAvailable_Type.__name__ = "Integer32"
_CrashReporterKernelDataAvailable_Object = MibScalar
crashReporterKernelDataAvailable = _CrashReporterKernelDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 55),
    _CrashReporterKernelDataAvailable_Type()
)
crashReporterKernelDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crashReporterKernelDataAvailable.setStatus("current")


class _CambiumTR069Status_Type(Integer32):
    """Custom type cambiumTR069Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CambiumTR069Status_Type.__name__ = "Integer32"
_CambiumTR069Status_Object = MibScalar
cambiumTR069Status = _CambiumTR069Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 56),
    _CambiumTR069Status_Type()
)
cambiumTR069Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTR069Status.setStatus("current")


class _CambiumDPIStatus_Type(Integer32):
    """Custom type cambiumDPIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDPIStatus_Type.__name__ = "Integer32"
_CambiumDPIStatus_Object = MibScalar
cambiumDPIStatus = _CambiumDPIStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 57),
    _CambiumDPIStatus_Type()
)
cambiumDPIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDPIStatus.setStatus("current")
_CambiumRFStatus_ObjectIdentity = ObjectIdentity
cambiumRFStatus = _CambiumRFStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2)
)


class _CambiumSTAConnectedRFFrequency_Type(Integer32):
    """Custom type cambiumSTAConnectedRFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2355, 6420),
    )


_CambiumSTAConnectedRFFrequency_Type.__name__ = "Integer32"
_CambiumSTAConnectedRFFrequency_Object = MibScalar
cambiumSTAConnectedRFFrequency = _CambiumSTAConnectedRFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 1),
    _CambiumSTAConnectedRFFrequency_Type()
)
cambiumSTAConnectedRFFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedRFFrequency.setStatus("current")


class _CambiumSTAConnectedRFBandwidth_Type(Integer32):
    """Custom type cambiumSTAConnectedRFBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAConnectedRFBandwidth_Type.__name__ = "Integer32"
_CambiumSTAConnectedRFBandwidth_Object = MibScalar
cambiumSTAConnectedRFBandwidth = _CambiumSTAConnectedRFBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 2),
    _CambiumSTAConnectedRFBandwidth_Type()
)
cambiumSTAConnectedRFBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedRFBandwidth.setStatus("current")
_CambiumSTADLRSSI_Type = Integer32
_CambiumSTADLRSSI_Object = MibScalar
cambiumSTADLRSSI = _CambiumSTADLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 3),
    _CambiumSTADLRSSI_Type()
)
cambiumSTADLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLRSSI.setStatus("current")
_CambiumSTADLCINR_Type = Integer32
_CambiumSTADLCINR_Object = MibScalar
cambiumSTADLCINR = _CambiumSTADLCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 4),
    _CambiumSTADLCINR_Type()
)
cambiumSTADLCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLCINR.setStatus("obsolete")


class _CambiumSTAConductedTXPower_Type(Integer32):
    """Custom type cambiumSTAConductedTXPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 30),
    )


_CambiumSTAConductedTXPower_Type.__name__ = "Integer32"
_CambiumSTAConductedTXPower_Object = MibScalar
cambiumSTAConductedTXPower = _CambiumSTAConductedTXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 5),
    _CambiumSTAConductedTXPower_Type()
)
cambiumSTAConductedTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConductedTXPower.setStatus("current")
_CambiumSTAUplinkMCSMode_Type = Integer32
_CambiumSTAUplinkMCSMode_Object = MibScalar
cambiumSTAUplinkMCSMode = _CambiumSTAUplinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 6),
    _CambiumSTAUplinkMCSMode_Type()
)
cambiumSTAUplinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAUplinkMCSMode.setStatus("current")
_CambiumSTADownlinkMCSMode_Type = Integer32
_CambiumSTADownlinkMCSMode_Object = MibScalar
cambiumSTADownlinkMCSMode = _CambiumSTADownlinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 7),
    _CambiumSTADownlinkMCSMode_Type()
)
cambiumSTADownlinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADownlinkMCSMode.setStatus("current")


class _CambiumSTAConnectedAP_Type(DisplayString):
    """Custom type cambiumSTAConnectedAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumSTAConnectedAP_Type.__name__ = "DisplayString"
_CambiumSTAConnectedAP_Object = MibScalar
cambiumSTAConnectedAP = _CambiumSTAConnectedAP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 8),
    _CambiumSTAConnectedAP_Type()
)
cambiumSTAConnectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedAP.setStatus("current")


class _CambiumSTAPowerControlMode_Type(Integer32):
    """Custom type cambiumSTAPowerControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAPowerControlMode_Type.__name__ = "Integer32"
_CambiumSTAPowerControlMode_Object = MibScalar
cambiumSTAPowerControlMode = _CambiumSTAPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 9),
    _CambiumSTAPowerControlMode_Type()
)
cambiumSTAPowerControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAPowerControlMode.setStatus("current")


class _CambiumAPNumberOfConnectedSTA_Type(Integer32):
    """Custom type cambiumAPNumberOfConnectedSTA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumAPNumberOfConnectedSTA_Type.__name__ = "Integer32"
_CambiumAPNumberOfConnectedSTA_Object = MibScalar
cambiumAPNumberOfConnectedSTA = _CambiumAPNumberOfConnectedSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 10),
    _CambiumAPNumberOfConnectedSTA_Type()
)
cambiumAPNumberOfConnectedSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPNumberOfConnectedSTA.setStatus("current")
_CambiumAPConnectedSTAListTable_Object = MibTable
cambiumAPConnectedSTAListTable = _CambiumAPConnectedSTAListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAListTable.setStatus("obsolete")
_CambiumAPConnectedSTAListEntry_Object = MibTableRow
cambiumAPConnectedSTAListEntry = _CambiumAPConnectedSTAListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1)
)
cambiumAPConnectedSTAListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAListEntry.setStatus("obsolete")


class _ConnectedSTAListMAC_Type(DisplayString):
    """Custom type connectedSTAListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_ConnectedSTAListMAC_Type.__name__ = "DisplayString"
_ConnectedSTAListMAC_Object = MibTableColumn
connectedSTAListMAC = _ConnectedSTAListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 1),
    _ConnectedSTAListMAC_Type()
)
connectedSTAListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMAC.setStatus("obsolete")
_ConnectedSTAListAID_Type = Integer32
_ConnectedSTAListAID_Object = MibTableColumn
connectedSTAListAID = _ConnectedSTAListAID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 2),
    _ConnectedSTAListAID_Type()
)
connectedSTAListAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListAID.setStatus("obsolete")
_ConnectedSTAListChannel_Type = Integer32
_ConnectedSTAListChannel_Object = MibTableColumn
connectedSTAListChannel = _ConnectedSTAListChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 3),
    _ConnectedSTAListChannel_Type()
)
connectedSTAListChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListChannel.setStatus("obsolete")
_ConnectedSTAListULRSSI_Type = Integer32
_ConnectedSTAListULRSSI_Object = MibTableColumn
connectedSTAListULRSSI = _ConnectedSTAListULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 4),
    _ConnectedSTAListULRSSI_Type()
)
connectedSTAListULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULRSSI.setStatus("obsolete")
_ConnectedSTAListDLRSSI_Type = Integer32
_ConnectedSTAListDLRSSI_Object = MibTableColumn
connectedSTAListDLRSSI = _ConnectedSTAListDLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 5),
    _ConnectedSTAListDLRSSI_Type()
)
connectedSTAListDLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLRSSI.setStatus("obsolete")
_ConnectedSTAListULCINR_Type = Integer32
_ConnectedSTAListULCINR_Object = MibTableColumn
connectedSTAListULCINR = _ConnectedSTAListULCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 6),
    _ConnectedSTAListULCINR_Type()
)
connectedSTAListULCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULCINR.setStatus("obsolete")
_ConnectedSTAListDLCINR_Type = Integer32
_ConnectedSTAListDLCINR_Object = MibTableColumn
connectedSTAListDLCINR = _ConnectedSTAListDLCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 7),
    _ConnectedSTAListDLCINR_Type()
)
connectedSTAListDLCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLCINR.setStatus("obsolete")


class _ConnectedSTAListULMCS_Type(Integer32):
    """Custom type connectedSTAListULMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
        ValueRangeConstraint(20, 29),
        ValueRangeConstraint(30, 39),
    )


_ConnectedSTAListULMCS_Type.__name__ = "Integer32"
_ConnectedSTAListULMCS_Object = MibTableColumn
connectedSTAListULMCS = _ConnectedSTAListULMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 8),
    _ConnectedSTAListULMCS_Type()
)
connectedSTAListULMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULMCS.setStatus("obsolete")


class _ConnectedSTAListDLMCS_Type(Integer32):
    """Custom type connectedSTAListDLMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
        ValueRangeConstraint(20, 29),
        ValueRangeConstraint(30, 39),
    )


_ConnectedSTAListDLMCS_Type.__name__ = "Integer32"
_ConnectedSTAListDLMCS_Object = MibTableColumn
connectedSTAListDLMCS = _ConnectedSTAListDLMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 9),
    _ConnectedSTAListDLMCS_Type()
)
connectedSTAListDLMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLMCS.setStatus("obsolete")
_ConnectedSTAListIP_Type = IpAddress
_ConnectedSTAListIP_Object = MibTableColumn
connectedSTAListIP = _ConnectedSTAListIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 10),
    _ConnectedSTAListIP_Type()
)
connectedSTAListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListIP.setStatus("obsolete")
_ConnectedSTAListMirSrc_Type = DisplayString
_ConnectedSTAListMirSrc_Object = MibTableColumn
connectedSTAListMirSrc = _ConnectedSTAListMirSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 12),
    _ConnectedSTAListMirSrc_Type()
)
connectedSTAListMirSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirSrc.setStatus("obsolete")
_ConnectedSTAListMirULRate_Type = DisplayString
_ConnectedSTAListMirULRate_Object = MibTableColumn
connectedSTAListMirULRate = _ConnectedSTAListMirULRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 13),
    _ConnectedSTAListMirULRate_Type()
)
connectedSTAListMirULRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirULRate.setStatus("obsolete")
_ConnectedSTAListMirDLRate_Type = DisplayString
_ConnectedSTAListMirDLRate_Object = MibTableColumn
connectedSTAListMirDLRate = _ConnectedSTAListMirDLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 14),
    _ConnectedSTAListMirDLRate_Type()
)
connectedSTAListMirDLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirDLRate.setStatus("obsolete")
_CambiumSTADistanceKm_Type = DisplayString
_CambiumSTADistanceKm_Object = MibScalar
cambiumSTADistanceKm = _CambiumSTADistanceKm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 12),
    _CambiumSTADistanceKm_Type()
)
cambiumSTADistanceKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADistanceKm.setStatus("current")
_CambiumSTADistanceMil_Type = DisplayString
_CambiumSTADistanceMil_Object = MibScalar
cambiumSTADistanceMil = _CambiumSTADistanceMil_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 13),
    _CambiumSTADistanceMil_Type()
)
cambiumSTADistanceMil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADistanceMil.setStatus("current")


class _CambiumPropagationDelay_Type(Integer32):
    """Custom type cambiumPropagationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 5000000),
    )


_CambiumPropagationDelay_Type.__name__ = "Integer32"
_CambiumPropagationDelay_Object = MibScalar
cambiumPropagationDelay = _CambiumPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 14),
    _CambiumPropagationDelay_Type()
)
cambiumPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumPropagationDelay.setStatus("current")
_CambiumSTAConnectedAPListTable_Object = MibTable
cambiumSTAConnectedAPListTable = _CambiumSTAConnectedAPListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPListTable.setStatus("obsolete")
_CambiumSTAConnectedAPListEntry_Object = MibTableRow
cambiumSTAConnectedAPListEntry = _CambiumSTAConnectedAPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1)
)
cambiumSTAConnectedAPListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "connectedAPListSSID"),
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPListEntry.setStatus("obsolete")
_ConnectedAPListSSID_Type = DisplayString
_ConnectedAPListSSID_Object = MibTableColumn
connectedAPListSSID = _ConnectedAPListSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 1),
    _ConnectedAPListSSID_Type()
)
connectedAPListSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListSSID.setStatus("obsolete")
_ConnectedAPListBSSID_Type = DisplayString
_ConnectedAPListBSSID_Object = MibTableColumn
connectedAPListBSSID = _ConnectedAPListBSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 2),
    _ConnectedAPListBSSID_Type()
)
connectedAPListBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListBSSID.setStatus("obsolete")
_ConnectedAPListChannel_Type = Integer32
_ConnectedAPListChannel_Object = MibTableColumn
connectedAPListChannel = _ConnectedAPListChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 3),
    _ConnectedAPListChannel_Type()
)
connectedAPListChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListChannel.setStatus("obsolete")
_ConnectedAPListFrequency_Type = Integer32
_ConnectedAPListFrequency_Object = MibTableColumn
connectedAPListFrequency = _ConnectedAPListFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 4),
    _ConnectedAPListFrequency_Type()
)
connectedAPListFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListFrequency.setStatus("obsolete")
_ConnectedAPListBandwidth_Type = DisplayString
_ConnectedAPListBandwidth_Object = MibTableColumn
connectedAPListBandwidth = _ConnectedAPListBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 5),
    _ConnectedAPListBandwidth_Type()
)
connectedAPListBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListBandwidth.setStatus("obsolete")
_ConnectedAPListRate_Type = DisplayString
_ConnectedAPListRate_Object = MibTableColumn
connectedAPListRate = _ConnectedAPListRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 6),
    _ConnectedAPListRate_Type()
)
connectedAPListRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRate.setStatus("obsolete")
_ConnectedAPListCINR_Type = Integer32
_ConnectedAPListCINR_Object = MibTableColumn
connectedAPListCINR = _ConnectedAPListCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 7),
    _ConnectedAPListCINR_Type()
)
connectedAPListCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListCINR.setStatus("obsolete")
_ConnectedAPListRSSI_Type = Integer32
_ConnectedAPListRSSI_Object = MibTableColumn
connectedAPListRSSI = _ConnectedAPListRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 8),
    _ConnectedAPListRSSI_Type()
)
connectedAPListRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRSSI.setStatus("obsolete")
_ConnectedAPListNoise_Type = Integer32
_ConnectedAPListNoise_Object = MibTableColumn
connectedAPListNoise = _ConnectedAPListNoise_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 9),
    _ConnectedAPListNoise_Type()
)
connectedAPListNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNoise.setStatus("obsolete")
_ConnectedAPListINT_Type = Integer32
_ConnectedAPListINT_Object = MibTableColumn
connectedAPListINT = _ConnectedAPListINT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 10),
    _ConnectedAPListINT_Type()
)
connectedAPListINT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListINT.setStatus("obsolete")
_ConnectedAPListNEState_Type = Integer32
_ConnectedAPListNEState_Object = MibTableColumn
connectedAPListNEState = _ConnectedAPListNEState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 11),
    _ConnectedAPListNEState_Type()
)
connectedAPListNEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNEState.setStatus("obsolete")
_ConnectedAPListNEAge_Type = DisplayString
_ConnectedAPListNEAge_Object = MibTableColumn
connectedAPListNEAge = _ConnectedAPListNEAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 12),
    _ConnectedAPListNEAge_Type()
)
connectedAPListNEAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNEAge.setStatus("obsolete")
_ConnectedAPListScanAge_Type = DisplayString
_ConnectedAPListScanAge_Object = MibTableColumn
connectedAPListScanAge = _ConnectedAPListScanAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 13),
    _ConnectedAPListScanAge_Type()
)
connectedAPListScanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListScanAge.setStatus("obsolete")
_ConnectedAPListRemainingSTA_Type = Integer32
_ConnectedAPListRemainingSTA_Object = MibTableColumn
connectedAPListRemainingSTA = _ConnectedAPListRemainingSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 14),
    _ConnectedAPListRemainingSTA_Type()
)
connectedAPListRemainingSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRemainingSTA.setStatus("obsolete")
_ConnectedAPListCAPS_Type = DisplayString
_ConnectedAPListCAPS_Object = MibTableColumn
connectedAPListCAPS = _ConnectedAPListCAPS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 15),
    _ConnectedAPListCAPS_Type()
)
connectedAPListCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListCAPS.setStatus("obsolete")
_ConnectedAPAuthMethod_Type = DisplayString
_ConnectedAPAuthMethod_Object = MibTableColumn
connectedAPAuthMethod = _ConnectedAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 16),
    _ConnectedAPAuthMethod_Type()
)
connectedAPAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPAuthMethod.setStatus("obsolete")
_ConnectedAPListMeetNEAttemptCriteria_Type = DisplayString
_ConnectedAPListMeetNEAttemptCriteria_Object = MibTableColumn
connectedAPListMeetNEAttemptCriteria = _ConnectedAPListMeetNEAttemptCriteria_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 17),
    _ConnectedAPListMeetNEAttemptCriteria_Type()
)
connectedAPListMeetNEAttemptCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListMeetNEAttemptCriteria.setStatus("obsolete")


class _WirelessInterfaceConnectionState_Type(Integer32):
    """Custom type wirelessInterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceConnectionState_Type.__name__ = "Integer32"
_WirelessInterfaceConnectionState_Object = MibScalar
wirelessInterfaceConnectionState = _WirelessInterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 16),
    _WirelessInterfaceConnectionState_Type()
)
wirelessInterfaceConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessInterfaceConnectionState.setStatus("current")


class _CambiumSTAPriority_Type(Integer32):
    """Custom type cambiumSTAPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAPriority_Type.__name__ = "Integer32"
_CambiumSTAPriority_Object = MibScalar
cambiumSTAPriority = _CambiumSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 17),
    _CambiumSTAPriority_Type()
)
cambiumSTAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAPriority.setStatus("current")
_CambiumSTADLSNR_Type = Integer32
_CambiumSTADLSNR_Object = MibScalar
cambiumSTADLSNR = _CambiumSTADLSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 18),
    _CambiumSTADLSNR_Type()
)
cambiumSTADLSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLSNR.setStatus("current")


class _CambiumConnectedAPMACAddress_Type(DisplayString):
    """Custom type cambiumConnectedAPMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_CambiumConnectedAPMACAddress_Type.__name__ = "DisplayString"
_CambiumConnectedAPMACAddress_Object = MibScalar
cambiumConnectedAPMACAddress = _CambiumConnectedAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 19),
    _CambiumConnectedAPMACAddress_Type()
)
cambiumConnectedAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumConnectedAPMACAddress.setStatus("current")
_CambiumSTAConnectedAPTable_Object = MibTable
cambiumSTAConnectedAPTable = _CambiumSTAConnectedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPTable.setStatus("current")
_CambiumSTAConnectedAPEntry_Object = MibTableRow
cambiumSTAConnectedAPEntry = _CambiumSTAConnectedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1)
)
cambiumSTAConnectedAPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "connectedAPListSSID"),
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPEntry.setStatus("current")
_ConnectedAPSSID_Type = DisplayString
_ConnectedAPSSID_Object = MibTableColumn
connectedAPSSID = _ConnectedAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 1),
    _ConnectedAPSSID_Type()
)
connectedAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPSSID.setStatus("current")
_ConnectedAPBSSID_Type = DisplayString
_ConnectedAPBSSID_Object = MibTableColumn
connectedAPBSSID = _ConnectedAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 2),
    _ConnectedAPBSSID_Type()
)
connectedAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPBSSID.setStatus("current")
_ConnectedAPChannel_Type = Integer32
_ConnectedAPChannel_Object = MibTableColumn
connectedAPChannel = _ConnectedAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 3),
    _ConnectedAPChannel_Type()
)
connectedAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPChannel.setStatus("current")
_ConnectedAPFrequency_Type = Integer32
_ConnectedAPFrequency_Object = MibTableColumn
connectedAPFrequency = _ConnectedAPFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 4),
    _ConnectedAPFrequency_Type()
)
connectedAPFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPFrequency.setStatus("current")
_ConnectedAPBandwidth_Type = DisplayString
_ConnectedAPBandwidth_Object = MibTableColumn
connectedAPBandwidth = _ConnectedAPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 5),
    _ConnectedAPBandwidth_Type()
)
connectedAPBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPBandwidth.setStatus("current")
_ConnectedAPRate_Type = DisplayString
_ConnectedAPRate_Object = MibTableColumn
connectedAPRate = _ConnectedAPRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 6),
    _ConnectedAPRate_Type()
)
connectedAPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRate.setStatus("current")
_ConnectedAPSNR_Type = Integer32
_ConnectedAPSNR_Object = MibTableColumn
connectedAPSNR = _ConnectedAPSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 7),
    _ConnectedAPSNR_Type()
)
connectedAPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPSNR.setStatus("current")
_ConnectedAPRSSI_Type = Integer32
_ConnectedAPRSSI_Object = MibTableColumn
connectedAPRSSI = _ConnectedAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 8),
    _ConnectedAPRSSI_Type()
)
connectedAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRSSI.setStatus("current")
_ConnectedAPNoise_Type = Integer32
_ConnectedAPNoise_Object = MibTableColumn
connectedAPNoise = _ConnectedAPNoise_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 9),
    _ConnectedAPNoise_Type()
)
connectedAPNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNoise.setStatus("current")
_ConnectedAPINT_Type = Integer32
_ConnectedAPINT_Object = MibTableColumn
connectedAPINT = _ConnectedAPINT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 10),
    _ConnectedAPINT_Type()
)
connectedAPINT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPINT.setStatus("current")
_ConnectedAPNEState_Type = Integer32
_ConnectedAPNEState_Object = MibTableColumn
connectedAPNEState = _ConnectedAPNEState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 11),
    _ConnectedAPNEState_Type()
)
connectedAPNEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNEState.setStatus("current")
_ConnectedAPNEAge_Type = DisplayString
_ConnectedAPNEAge_Object = MibTableColumn
connectedAPNEAge = _ConnectedAPNEAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 12),
    _ConnectedAPNEAge_Type()
)
connectedAPNEAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNEAge.setStatus("current")
_ConnectedAPScanAge_Type = DisplayString
_ConnectedAPScanAge_Object = MibTableColumn
connectedAPScanAge = _ConnectedAPScanAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 13),
    _ConnectedAPScanAge_Type()
)
connectedAPScanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPScanAge.setStatus("current")
_ConnectedAPRemainingSTA_Type = Integer32
_ConnectedAPRemainingSTA_Object = MibTableColumn
connectedAPRemainingSTA = _ConnectedAPRemainingSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 14),
    _ConnectedAPRemainingSTA_Type()
)
connectedAPRemainingSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRemainingSTA.setStatus("current")
_ConnectedAPCAPS_Type = DisplayString
_ConnectedAPCAPS_Object = MibTableColumn
connectedAPCAPS = _ConnectedAPCAPS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 15),
    _ConnectedAPCAPS_Type()
)
connectedAPCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPCAPS.setStatus("current")
_ConnectedAPAuthenticationMethod_Type = DisplayString
_ConnectedAPAuthenticationMethod_Object = MibTableColumn
connectedAPAuthenticationMethod = _ConnectedAPAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 16),
    _ConnectedAPAuthenticationMethod_Type()
)
connectedAPAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPAuthenticationMethod.setStatus("current")
_ConnectedAPMeetNEAttemptCriteria_Type = DisplayString
_ConnectedAPMeetNEAttemptCriteria_Object = MibTableColumn
connectedAPMeetNEAttemptCriteria = _ConnectedAPMeetNEAttemptCriteria_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 17),
    _ConnectedAPMeetNEAttemptCriteria_Type()
)
connectedAPMeetNEAttemptCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPMeetNEAttemptCriteria.setStatus("current")
_ConnectedAPIsViaInterface_Type = Integer32
_ConnectedAPIsViaInterface_Object = MibTableColumn
connectedAPIsViaInterface = _ConnectedAPIsViaInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 18),
    _ConnectedAPIsViaInterface_Type()
)
connectedAPIsViaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPIsViaInterface.setStatus("current")
_ConnectedAPDriverMode_Type = Integer32
_ConnectedAPDriverMode_Object = MibTableColumn
connectedAPDriverMode = _ConnectedAPDriverMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 19),
    _ConnectedAPDriverMode_Type()
)
connectedAPDriverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPDriverMode.setStatus("current")


class _StaTxCapacity_Type(Integer32):
    """Custom type staTxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StaTxCapacity_Type.__name__ = "Integer32"
_StaTxCapacity_Object = MibScalar
staTxCapacity = _StaTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 21),
    _StaTxCapacity_Type()
)
staTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxCapacity.setStatus("current")


class _StaTxQuality_Type(Integer32):
    """Custom type staTxQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StaTxQuality_Type.__name__ = "Integer32"
_StaTxQuality_Object = MibScalar
staTxQuality = _StaTxQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 22),
    _StaTxQuality_Type()
)
staTxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxQuality.setStatus("current")


class _CambiumePMPElevateConnected_Type(Integer32):
    """Custom type cambiumePMPElevateConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumePMPElevateConnected_Type.__name__ = "Integer32"
_CambiumePMPElevateConnected_Object = MibScalar
cambiumePMPElevateConnected = _CambiumePMPElevateConnected_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 23),
    _CambiumePMPElevateConnected_Type()
)
cambiumePMPElevateConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumePMPElevateConnected.setStatus("current")
_CambiumRSSICh0_Type = Integer32
_CambiumRSSICh0_Object = MibScalar
cambiumRSSICh0 = _CambiumRSSICh0_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 24),
    _CambiumRSSICh0_Type()
)
cambiumRSSICh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRSSICh0.setStatus("current")
_CambiumRSSICh1_Type = Integer32
_CambiumRSSICh1_Object = MibScalar
cambiumRSSICh1 = _CambiumRSSICh1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 25),
    _CambiumRSSICh1_Type()
)
cambiumRSSICh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRSSICh1.setStatus("current")
_CambiumAPConnectedSTATable_Object = MibTable
cambiumAPConnectedSTATable = _CambiumAPConnectedSTATable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30)
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTATable.setStatus("current")
_CambiumAPConnectedSTAEntry_Object = MibTableRow
cambiumAPConnectedSTAEntry = _CambiumAPConnectedSTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1)
)
cambiumAPConnectedSTAEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAEntry.setStatus("current")


class _ConnectedSTAMAC_Type(DisplayString):
    """Custom type connectedSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_ConnectedSTAMAC_Type.__name__ = "DisplayString"
_ConnectedSTAMAC_Object = MibTableColumn
connectedSTAMAC = _ConnectedSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 1),
    _ConnectedSTAMAC_Type()
)
connectedSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMAC.setStatus("current")
_ConnectedSTAAID_Type = Integer32
_ConnectedSTAAID_Object = MibTableColumn
connectedSTAAID = _ConnectedSTAAID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 2),
    _ConnectedSTAAID_Type()
)
connectedSTAAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAAID.setStatus("current")
_ConnectedSTAChannel_Type = Integer32
_ConnectedSTAChannel_Object = MibTableColumn
connectedSTAChannel = _ConnectedSTAChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 3),
    _ConnectedSTAChannel_Type()
)
connectedSTAChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAChannel.setStatus("current")
_ConnectedSTAULRSSI_Type = Integer32
_ConnectedSTAULRSSI_Object = MibTableColumn
connectedSTAULRSSI = _ConnectedSTAULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 4),
    _ConnectedSTAULRSSI_Type()
)
connectedSTAULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULRSSI.setStatus("current")
_ConnectedSTADLRSSI_Type = Integer32
_ConnectedSTADLRSSI_Object = MibTableColumn
connectedSTADLRSSI = _ConnectedSTADLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 5),
    _ConnectedSTADLRSSI_Type()
)
connectedSTADLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLRSSI.setStatus("current")
_ConnectedSTAULSNR_Type = Integer32
_ConnectedSTAULSNR_Object = MibTableColumn
connectedSTAULSNR = _ConnectedSTAULSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 6),
    _ConnectedSTAULSNR_Type()
)
connectedSTAULSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULSNR.setStatus("current")
_ConnectedSTADLSNR_Type = Integer32
_ConnectedSTADLSNR_Object = MibTableColumn
connectedSTADLSNR = _ConnectedSTADLSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 7),
    _ConnectedSTADLSNR_Type()
)
connectedSTADLSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLSNR.setStatus("current")
_ConnectedSTAULMCS_Type = Integer32
_ConnectedSTAULMCS_Object = MibTableColumn
connectedSTAULMCS = _ConnectedSTAULMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 8),
    _ConnectedSTAULMCS_Type()
)
connectedSTAULMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULMCS.setStatus("current")
_ConnectedSTADLMCS_Type = Integer32
_ConnectedSTADLMCS_Object = MibTableColumn
connectedSTADLMCS = _ConnectedSTADLMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 9),
    _ConnectedSTADLMCS_Type()
)
connectedSTADLMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLMCS.setStatus("current")
_ConnectedSTAIP_Type = IpAddress
_ConnectedSTAIP_Object = MibTableColumn
connectedSTAIP = _ConnectedSTAIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 10),
    _ConnectedSTAIP_Type()
)
connectedSTAIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAIP.setStatus("current")
_ConnectedSTAPriority_Type = DisplayString
_ConnectedSTAPriority_Object = MibTableColumn
connectedSTAPriority = _ConnectedSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 11),
    _ConnectedSTAPriority_Type()
)
connectedSTAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAPriority.setStatus("current")
_ConnectedSTAMirSrc_Type = DisplayString
_ConnectedSTAMirSrc_Object = MibTableColumn
connectedSTAMirSrc = _ConnectedSTAMirSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 12),
    _ConnectedSTAMirSrc_Type()
)
connectedSTAMirSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirSrc.setStatus("current")
_ConnectedSTAMirULRate_Type = DisplayString
_ConnectedSTAMirULRate_Object = MibTableColumn
connectedSTAMirULRate = _ConnectedSTAMirULRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 13),
    _ConnectedSTAMirULRate_Type()
)
connectedSTAMirULRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirULRate.setStatus("current")
_ConnectedSTAMirDLRate_Type = DisplayString
_ConnectedSTAMirDLRate_Object = MibTableColumn
connectedSTAMirDLRate = _ConnectedSTAMirDLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 14),
    _ConnectedSTAMirDLRate_Type()
)
connectedSTAMirDLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirDLRate.setStatus("current")
_ConnectedSTAClickTHWAddr_Type = DisplayString
_ConnectedSTAClickTHWAddr_Object = MibTableColumn
connectedSTAClickTHWAddr = _ConnectedSTAClickTHWAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 15),
    _ConnectedSTAClickTHWAddr_Type()
)
connectedSTAClickTHWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTHWAddr.setStatus("current")
_ConnectedSTAClickTWebPort_Type = Integer32
_ConnectedSTAClickTWebPort_Object = MibTableColumn
connectedSTAClickTWebPort = _ConnectedSTAClickTWebPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 16),
    _ConnectedSTAClickTWebPort_Type()
)
connectedSTAClickTWebPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTWebPort.setStatus("current")
_ConnectedSTAClickTWebSec_Type = Integer32
_ConnectedSTAClickTWebSec_Object = MibTableColumn
connectedSTAClickTWebSec = _ConnectedSTAClickTWebSec_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 17),
    _ConnectedSTAClickTWebSec_Type()
)
connectedSTAClickTWebSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTWebSec.setStatus("current")
_ConnectedSTAClickTHostName_Type = DisplayString
_ConnectedSTAClickTHostName_Object = MibTableColumn
connectedSTAClickTHostName = _ConnectedSTAClickTHostName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 18),
    _ConnectedSTAClickTHostName_Type()
)
connectedSTAClickTHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTHostName.setStatus("current")


class _ConnectedSTATXCapacity_Type(Integer32):
    """Custom type connectedSTATXCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectedSTATXCapacity_Type.__name__ = "Integer32"
_ConnectedSTATXCapacity_Object = MibTableColumn
connectedSTATXCapacity = _ConnectedSTATXCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 19),
    _ConnectedSTATXCapacity_Type()
)
connectedSTATXCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTATXCapacity.setStatus("current")


class _ConnectedSTATXQuality_Type(Integer32):
    """Custom type connectedSTATXQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectedSTATXQuality_Type.__name__ = "Integer32"
_ConnectedSTATXQuality_Object = MibTableColumn
connectedSTATXQuality = _ConnectedSTATXQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 20),
    _ConnectedSTATXQuality_Type()
)
connectedSTATXQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTATXQuality.setStatus("current")
_ConnectedSTAMcastTotalGroups_Type = Integer32
_ConnectedSTAMcastTotalGroups_Object = MibTableColumn
connectedSTAMcastTotalGroups = _ConnectedSTAMcastTotalGroups_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 21),
    _ConnectedSTAMcastTotalGroups_Type()
)
connectedSTAMcastTotalGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastTotalGroups.setStatus("current")
_ConnectedSTAMcastGRP0_Type = IpAddress
_ConnectedSTAMcastGRP0_Object = MibTableColumn
connectedSTAMcastGRP0 = _ConnectedSTAMcastGRP0_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 22),
    _ConnectedSTAMcastGRP0_Type()
)
connectedSTAMcastGRP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP0.setStatus("current")
_ConnectedSTAMcastGRP1_Type = IpAddress
_ConnectedSTAMcastGRP1_Object = MibTableColumn
connectedSTAMcastGRP1 = _ConnectedSTAMcastGRP1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 23),
    _ConnectedSTAMcastGRP1_Type()
)
connectedSTAMcastGRP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP1.setStatus("current")
_ConnectedSTAMcastGRP2_Type = IpAddress
_ConnectedSTAMcastGRP2_Object = MibTableColumn
connectedSTAMcastGRP2 = _ConnectedSTAMcastGRP2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 24),
    _ConnectedSTAMcastGRP2_Type()
)
connectedSTAMcastGRP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP2.setStatus("current")
_ConnectedSTAMcastGRP3_Type = IpAddress
_ConnectedSTAMcastGRP3_Object = MibTableColumn
connectedSTAMcastGRP3 = _ConnectedSTAMcastGRP3_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 25),
    _ConnectedSTAMcastGRP3_Type()
)
connectedSTAMcastGRP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP3.setStatus("current")
_ConnectedSTAMcastGRP4_Type = IpAddress
_ConnectedSTAMcastGRP4_Object = MibTableColumn
connectedSTAMcastGRP4 = _ConnectedSTAMcastGRP4_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 26),
    _ConnectedSTAMcastGRP4_Type()
)
connectedSTAMcastGRP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP4.setStatus("current")
_ConnectedSTASessionTime_Type = DisplayString
_ConnectedSTASessionTime_Object = MibTableColumn
connectedSTASessionTime = _ConnectedSTASessionTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 27),
    _ConnectedSTASessionTime_Type()
)
connectedSTASessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTASessionTime.setStatus("current")
_ConnectedSTADLRateMbps_Type = DisplayString
_ConnectedSTADLRateMbps_Object = MibTableColumn
connectedSTADLRateMbps = _ConnectedSTADLRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 28),
    _ConnectedSTADLRateMbps_Type()
)
connectedSTADLRateMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLRateMbps.setStatus("current")
_ConnectedSTADistance_Type = Integer32
_ConnectedSTADistance_Object = MibTableColumn
connectedSTADistance = _ConnectedSTADistance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 29),
    _ConnectedSTADistance_Type()
)
connectedSTADistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADistance.setStatus("current")
_ConnectedSTAVerticalAngle_Type = DisplayString
_ConnectedSTAVerticalAngle_Object = MibTableColumn
connectedSTAVerticalAngle = _ConnectedSTAVerticalAngle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 30),
    _ConnectedSTAVerticalAngle_Type()
)
connectedSTAVerticalAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAVerticalAngle.setStatus("current")
_ConnectedSTAHorizontalAngle_Type = DisplayString
_ConnectedSTAHorizontalAngle_Object = MibTableColumn
connectedSTAHorizontalAngle = _ConnectedSTAHorizontalAngle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 31),
    _ConnectedSTAHorizontalAngle_Type()
)
connectedSTAHorizontalAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAHorizontalAngle.setStatus("current")


class _ConnectedSTAIsForcedAngle_Type(Integer32):
    """Custom type connectedSTAIsForcedAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ConnectedSTAIsForcedAngle_Type.__name__ = "Integer32"
_ConnectedSTAIsForcedAngle_Object = MibTableColumn
connectedSTAIsForcedAngle = _ConnectedSTAIsForcedAngle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 32),
    _ConnectedSTAIsForcedAngle_Type()
)
connectedSTAIsForcedAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAIsForcedAngle.setStatus("current")


class _ConnectedSTASKU_Type(Integer32):
    """Custom type connectedSTASKU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConnectedSTASKU_Type.__name__ = "Integer32"
_ConnectedSTASKU_Object = MibTableColumn
connectedSTASKU = _ConnectedSTASKU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 33),
    _ConnectedSTASKU_Type()
)
connectedSTASKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTASKU.setStatus("current")


class _ConnectedSTALinktestForceAllow_Type(Integer32):
    """Custom type connectedSTALinktestForceAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConnectedSTALinktestForceAllow_Type.__name__ = "Integer32"
_ConnectedSTALinktestForceAllow_Object = MibTableColumn
connectedSTALinktestForceAllow = _ConnectedSTALinktestForceAllow_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 34),
    _ConnectedSTALinktestForceAllow_Type()
)
connectedSTALinktestForceAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTALinktestForceAllow.setStatus("current")
_ConnectedSTAIPv6_Type = Ipv6Address
_ConnectedSTAIPv6_Object = MibTableColumn
connectedSTAIPv6 = _ConnectedSTAIPv6_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 35),
    _ConnectedSTAIPv6_Type()
)
connectedSTAIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAIPv6.setStatus("current")


class _ConnectedSTAIsViaInterface_Type(Integer32):
    """Custom type connectedSTAIsViaInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ConnectedSTAIsViaInterface_Type.__name__ = "Integer32"
_ConnectedSTAIsViaInterface_Object = MibTableColumn
connectedSTAIsViaInterface = _ConnectedSTAIsViaInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 36),
    _ConnectedSTAIsViaInterface_Type()
)
connectedSTAIsViaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAIsViaInterface.setStatus("current")


class _ConnectedSTAMUMIMOGain_Type(Integer32):
    """Custom type connectedSTAMUMIMOGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_ConnectedSTAMUMIMOGain_Type.__name__ = "Integer32"
_ConnectedSTAMUMIMOGain_Object = MibTableColumn
connectedSTAMUMIMOGain = _ConnectedSTAMUMIMOGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 37),
    _ConnectedSTAMUMIMOGain_Type()
)
connectedSTAMUMIMOGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMUMIMOGain.setStatus("current")
_ConnectedSTAModelName_Type = DisplayString
_ConnectedSTAModelName_Object = MibTableColumn
connectedSTAModelName = _ConnectedSTAModelName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 38),
    _ConnectedSTAModelName_Type()
)
connectedSTAModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAModelName.setStatus("current")


class _ConnectedSTAMUMIMOAzMetric_Type(Integer32):
    """Custom type connectedSTAMUMIMOAzMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_ConnectedSTAMUMIMOAzMetric_Type.__name__ = "Integer32"
_ConnectedSTAMUMIMOAzMetric_Object = MibTableColumn
connectedSTAMUMIMOAzMetric = _ConnectedSTAMUMIMOAzMetric_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 39),
    _ConnectedSTAMUMIMOAzMetric_Type()
)
connectedSTAMUMIMOAzMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMUMIMOAzMetric.setStatus("current")


class _ConnectedSTAMUMIMOQuality_Type(Integer32):
    """Custom type connectedSTAMUMIMOQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectedSTAMUMIMOQuality_Type.__name__ = "Integer32"
_ConnectedSTAMUMIMOQuality_Object = MibTableColumn
connectedSTAMUMIMOQuality = _ConnectedSTAMUMIMOQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 40),
    _ConnectedSTAMUMIMOQuality_Type()
)
connectedSTAMUMIMOQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMUMIMOQuality.setStatus("current")


class _ConnectedSTAMUMIMORate_Type(Integer32):
    """Custom type connectedSTAMUMIMORate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ConnectedSTAMUMIMORate_Type.__name__ = "Integer32"
_ConnectedSTAMUMIMORate_Object = MibTableColumn
connectedSTAMUMIMORate = _ConnectedSTAMUMIMORate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 41),
    _ConnectedSTAMUMIMORate_Type()
)
connectedSTAMUMIMORate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMUMIMORate.setStatus("current")


class _ConnectedSTAMUMIMOPairs_Type(Integer32):
    """Custom type connectedSTAMUMIMOPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_ConnectedSTAMUMIMOPairs_Type.__name__ = "Integer32"
_ConnectedSTAMUMIMOPairs_Object = MibTableColumn
connectedSTAMUMIMOPairs = _ConnectedSTAMUMIMOPairs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 42),
    _ConnectedSTAMUMIMOPairs_Type()
)
connectedSTAMUMIMOPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMUMIMOPairs.setStatus("current")
_ConnectedSTASoftwareVersion_Type = DisplayString
_ConnectedSTASoftwareVersion_Object = MibTableColumn
connectedSTASoftwareVersion = _ConnectedSTASoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 43),
    _ConnectedSTASoftwareVersion_Type()
)
connectedSTASoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTASoftwareVersion.setStatus("current")
_CambiumAPBridgeTable_Object = MibTable
cambiumAPBridgeTable = _CambiumAPBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40)
)
if mibBuilder.loadTexts:
    cambiumAPBridgeTable.setStatus("current")
_CambiumAPBridgeEntry_Object = MibTableRow
cambiumAPBridgeEntry = _CambiumAPBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1)
)
cambiumAPBridgeEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "camAPBrTabDevMACAddress"),
)
if mibBuilder.loadTexts:
    cambiumAPBridgeEntry.setStatus("current")
_CamAPBrTabBridgeName_Type = DisplayString
_CamAPBrTabBridgeName_Object = MibTableColumn
camAPBrTabBridgeName = _CamAPBrTabBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 1),
    _CamAPBrTabBridgeName_Type()
)
camAPBrTabBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabBridgeName.setStatus("current")
_CamAPBrTabDevMACAddress_Type = DisplayString
_CamAPBrTabDevMACAddress_Object = MibTableColumn
camAPBrTabDevMACAddress = _CamAPBrTabDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 2),
    _CamAPBrTabDevMACAddress_Type()
)
camAPBrTabDevMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabDevMACAddress.setStatus("current")
_CamAPBrTabDevPort_Type = DisplayString
_CamAPBrTabDevPort_Object = MibTableColumn
camAPBrTabDevPort = _CamAPBrTabDevPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 3),
    _CamAPBrTabDevPort_Type()
)
camAPBrTabDevPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabDevPort.setStatus("current")
_CamAPBrTabSTAMACAddress_Type = DisplayString
_CamAPBrTabSTAMACAddress_Object = MibTableColumn
camAPBrTabSTAMACAddress = _CamAPBrTabSTAMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 4),
    _CamAPBrTabSTAMACAddress_Type()
)
camAPBrTabSTAMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabSTAMACAddress.setStatus("current")
_CamAPBrTabAgingTime_Type = Counter32
_CamAPBrTabAgingTime_Object = MibTableColumn
camAPBrTabAgingTime = _CamAPBrTabAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 5),
    _CamAPBrTabAgingTime_Type()
)
camAPBrTabAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabAgingTime.setStatus("current")
_CambiumSTABridgeTable_Object = MibTable
cambiumSTABridgeTable = _CambiumSTABridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50)
)
if mibBuilder.loadTexts:
    cambiumSTABridgeTable.setStatus("current")
_CambiumSTABridgeEntry_Object = MibTableRow
cambiumSTABridgeEntry = _CambiumSTABridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1)
)
cambiumSTABridgeEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "camSTABrTabDevMACAddress"),
)
if mibBuilder.loadTexts:
    cambiumSTABridgeEntry.setStatus("current")
_CamSTABrTabBridgeName_Type = DisplayString
_CamSTABrTabBridgeName_Object = MibTableColumn
camSTABrTabBridgeName = _CamSTABrTabBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 1),
    _CamSTABrTabBridgeName_Type()
)
camSTABrTabBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabBridgeName.setStatus("current")
_CamSTABrTabDevMACAddress_Type = DisplayString
_CamSTABrTabDevMACAddress_Object = MibTableColumn
camSTABrTabDevMACAddress = _CamSTABrTabDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 2),
    _CamSTABrTabDevMACAddress_Type()
)
camSTABrTabDevMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabDevMACAddress.setStatus("current")
_CamSTABrTabDevPort_Type = DisplayString
_CamSTABrTabDevPort_Object = MibTableColumn
camSTABrTabDevPort = _CamSTABrTabDevPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 3),
    _CamSTABrTabDevPort_Type()
)
camSTABrTabDevPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabDevPort.setStatus("current")
_CamSTABrTabAgingTime_Type = Counter32
_CamSTABrTabAgingTime_Object = MibTableColumn
camSTABrTabAgingTime = _CamSTABrTabAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 4),
    _CamSTABrTabAgingTime_Type()
)
camSTABrTabAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabAgingTime.setStatus("current")


class _CambiumSTAMAC_Type(DisplayString):
    """Custom type cambiumSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CambiumSTAMAC_Type.__name__ = "DisplayString"
_CambiumSTAMAC_Object = MibScalar
cambiumSTAMAC = _CambiumSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 60),
    _CambiumSTAMAC_Type()
)
cambiumSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAMAC.setStatus("current")


class _CambiumSTADropReason_Type(DisplayString):
    """Custom type cambiumSTADropReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumSTADropReason_Type.__name__ = "DisplayString"
_CambiumSTADropReason_Object = MibScalar
cambiumSTADropReason = _CambiumSTADropReason_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 61),
    _CambiumSTADropReason_Type()
)
cambiumSTADropReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADropReason.setStatus("current")


class _CambiumNetworkEntryFailureSTAMAC_Type(DisplayString):
    """Custom type cambiumNetworkEntryFailureSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CambiumNetworkEntryFailureSTAMAC_Type.__name__ = "DisplayString"
_CambiumNetworkEntryFailureSTAMAC_Object = MibScalar
cambiumNetworkEntryFailureSTAMAC = _CambiumNetworkEntryFailureSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 62),
    _CambiumNetworkEntryFailureSTAMAC_Type()
)
cambiumNetworkEntryFailureSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumNetworkEntryFailureSTAMAC.setStatus("current")


class _CambiumNetworkEntryFailureReason_Type(DisplayString):
    """Custom type cambiumNetworkEntryFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumNetworkEntryFailureReason_Type.__name__ = "DisplayString"
_CambiumNetworkEntryFailureReason_Object = MibScalar
cambiumNetworkEntryFailureReason = _CambiumNetworkEntryFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 63),
    _CambiumNetworkEntryFailureReason_Type()
)
cambiumNetworkEntryFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumNetworkEntryFailureReason.setStatus("current")
_WirelessLinkDroppedCount_Type = Integer32
_WirelessLinkDroppedCount_Object = MibScalar
wirelessLinkDroppedCount = _WirelessLinkDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 64),
    _WirelessLinkDroppedCount_Type()
)
wirelessLinkDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkDroppedCount.setStatus("current")


class _CambiumMUMIMOGainAggregated_Type(Integer32):
    """Custom type cambiumMUMIMOGainAggregated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CambiumMUMIMOGainAggregated_Type.__name__ = "Integer32"
_CambiumMUMIMOGainAggregated_Object = MibScalar
cambiumMUMIMOGainAggregated = _CambiumMUMIMOGainAggregated_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 65),
    _CambiumMUMIMOGainAggregated_Type()
)
cambiumMUMIMOGainAggregated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMUMIMOGainAggregated.setStatus("current")


class _CambiumSTA2ConnectedRFFrequency_Type(Integer32):
    """Custom type cambiumSTA2ConnectedRFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2355, 6420),
    )


_CambiumSTA2ConnectedRFFrequency_Type.__name__ = "Integer32"
_CambiumSTA2ConnectedRFFrequency_Object = MibScalar
cambiumSTA2ConnectedRFFrequency = _CambiumSTA2ConnectedRFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 101),
    _CambiumSTA2ConnectedRFFrequency_Type()
)
cambiumSTA2ConnectedRFFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2ConnectedRFFrequency.setStatus("current")


class _CambiumSTA2ConnectedRFBandwidth_Type(Integer32):
    """Custom type cambiumSTA2ConnectedRFBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTA2ConnectedRFBandwidth_Type.__name__ = "Integer32"
_CambiumSTA2ConnectedRFBandwidth_Object = MibScalar
cambiumSTA2ConnectedRFBandwidth = _CambiumSTA2ConnectedRFBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 102),
    _CambiumSTA2ConnectedRFBandwidth_Type()
)
cambiumSTA2ConnectedRFBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2ConnectedRFBandwidth.setStatus("current")
_CambiumSTA2DLRSSI_Type = Integer32
_CambiumSTA2DLRSSI_Object = MibScalar
cambiumSTA2DLRSSI = _CambiumSTA2DLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 103),
    _CambiumSTA2DLRSSI_Type()
)
cambiumSTA2DLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2DLRSSI.setStatus("current")


class _CambiumSTA2ConductedTXPower_Type(Integer32):
    """Custom type cambiumSTA2ConductedTXPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 30),
    )


_CambiumSTA2ConductedTXPower_Type.__name__ = "Integer32"
_CambiumSTA2ConductedTXPower_Object = MibScalar
cambiumSTA2ConductedTXPower = _CambiumSTA2ConductedTXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 105),
    _CambiumSTA2ConductedTXPower_Type()
)
cambiumSTA2ConductedTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2ConductedTXPower.setStatus("current")
_CambiumSTA2UplinkMCSMode_Type = Integer32
_CambiumSTA2UplinkMCSMode_Object = MibScalar
cambiumSTA2UplinkMCSMode = _CambiumSTA2UplinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 106),
    _CambiumSTA2UplinkMCSMode_Type()
)
cambiumSTA2UplinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2UplinkMCSMode.setStatus("current")
_CambiumSTA2DownlinkMCSMode_Type = Integer32
_CambiumSTA2DownlinkMCSMode_Object = MibScalar
cambiumSTA2DownlinkMCSMode = _CambiumSTA2DownlinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 107),
    _CambiumSTA2DownlinkMCSMode_Type()
)
cambiumSTA2DownlinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2DownlinkMCSMode.setStatus("current")


class _CambiumSTA2ConnectedAP_Type(DisplayString):
    """Custom type cambiumSTA2ConnectedAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumSTA2ConnectedAP_Type.__name__ = "DisplayString"
_CambiumSTA2ConnectedAP_Object = MibScalar
cambiumSTA2ConnectedAP = _CambiumSTA2ConnectedAP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 108),
    _CambiumSTA2ConnectedAP_Type()
)
cambiumSTA2ConnectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2ConnectedAP.setStatus("current")
_CambiumSTA2DLSNR_Type = Integer32
_CambiumSTA2DLSNR_Object = MibScalar
cambiumSTA2DLSNR = _CambiumSTA2DLSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 118),
    _CambiumSTA2DLSNR_Type()
)
cambiumSTA2DLSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTA2DLSNR.setStatus("current")


class _CambiumConnectedAP2MACAddress_Type(DisplayString):
    """Custom type cambiumConnectedAP2MACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_CambiumConnectedAP2MACAddress_Type.__name__ = "DisplayString"
_CambiumConnectedAP2MACAddress_Object = MibScalar
cambiumConnectedAP2MACAddress = _CambiumConnectedAP2MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 119),
    _CambiumConnectedAP2MACAddress_Type()
)
cambiumConnectedAP2MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumConnectedAP2MACAddress.setStatus("current")


class _Sta2TxCapacity_Type(Integer32):
    """Custom type sta2TxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sta2TxCapacity_Type.__name__ = "Integer32"
_Sta2TxCapacity_Object = MibScalar
sta2TxCapacity = _Sta2TxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 121),
    _Sta2TxCapacity_Type()
)
sta2TxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sta2TxCapacity.setStatus("current")


class _Sta2TxQuality_Type(Integer32):
    """Custom type sta2TxQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sta2TxQuality_Type.__name__ = "Integer32"
_Sta2TxQuality_Object = MibScalar
sta2TxQuality = _Sta2TxQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 122),
    _Sta2TxQuality_Type()
)
sta2TxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sta2TxQuality.setStatus("current")
_CambiumRSSI2Ch0_Type = Integer32
_CambiumRSSI2Ch0_Object = MibScalar
cambiumRSSI2Ch0 = _CambiumRSSI2Ch0_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 124),
    _CambiumRSSI2Ch0_Type()
)
cambiumRSSI2Ch0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRSSI2Ch0.setStatus("current")
_CambiumRSSI2Ch1_Type = Integer32
_CambiumRSSI2Ch1_Object = MibScalar
cambiumRSSI2Ch1 = _CambiumRSSI2Ch1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 125),
    _CambiumRSSI2Ch1_Type()
)
cambiumRSSI2Ch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRSSI2Ch1.setStatus("current")
_CambiumGPSStatus_ObjectIdentity = ObjectIdentity
cambiumGPSStatus = _CambiumGPSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3)
)


class _CambiumGPSCurrentSyncState_Type(Integer32):
    """Custom type cambiumGPSCurrentSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumGPSCurrentSyncState_Type.__name__ = "Integer32"
_CambiumGPSCurrentSyncState_Object = MibScalar
cambiumGPSCurrentSyncState = _CambiumGPSCurrentSyncState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 1),
    _CambiumGPSCurrentSyncState_Type()
)
cambiumGPSCurrentSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSCurrentSyncState.setStatus("current")


class _CambiumGPSLatitude_Type(DisplayString):
    """Custom type cambiumGPSLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSLatitude_Type.__name__ = "DisplayString"
_CambiumGPSLatitude_Object = MibScalar
cambiumGPSLatitude = _CambiumGPSLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 2),
    _CambiumGPSLatitude_Type()
)
cambiumGPSLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSLatitude.setStatus("current")


class _CambiumGPSLongitude_Type(DisplayString):
    """Custom type cambiumGPSLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSLongitude_Type.__name__ = "DisplayString"
_CambiumGPSLongitude_Object = MibScalar
cambiumGPSLongitude = _CambiumGPSLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 3),
    _CambiumGPSLongitude_Type()
)
cambiumGPSLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSLongitude.setStatus("current")


class _CambiumGPSHeight_Type(DisplayString):
    """Custom type cambiumGPSHeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSHeight_Type.__name__ = "DisplayString"
_CambiumGPSHeight_Object = MibScalar
cambiumGPSHeight = _CambiumGPSHeight_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 4),
    _CambiumGPSHeight_Type()
)
cambiumGPSHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSHeight.setStatus("current")


class _CambiumGPSTime_Type(DisplayString):
    """Custom type cambiumGPSTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSTime_Type.__name__ = "DisplayString"
_CambiumGPSTime_Object = MibScalar
cambiumGPSTime = _CambiumGPSTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 5),
    _CambiumGPSTime_Type()
)
cambiumGPSTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSTime.setStatus("current")


class _CambiumGPSNumTrackedSat_Type(Integer32):
    """Custom type cambiumGPSNumTrackedSat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumGPSNumTrackedSat_Type.__name__ = "Integer32"
_CambiumGPSNumTrackedSat_Object = MibScalar
cambiumGPSNumTrackedSat = _CambiumGPSNumTrackedSat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 6),
    _CambiumGPSNumTrackedSat_Type()
)
cambiumGPSNumTrackedSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSNumTrackedSat.setStatus("current")


class _CambiumGPSNumVisibleSat_Type(Integer32):
    """Custom type cambiumGPSNumVisibleSat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumGPSNumVisibleSat_Type.__name__ = "Integer32"
_CambiumGPSNumVisibleSat_Object = MibScalar
cambiumGPSNumVisibleSat = _CambiumGPSNumVisibleSat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 7),
    _CambiumGPSNumVisibleSat_Type()
)
cambiumGPSNumVisibleSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSNumVisibleSat.setStatus("current")
_CambiumGPSSatSNRTable_Object = MibTable
cambiumGPSSatSNRTable = _CambiumGPSSatSNRTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cambiumGPSSatSNRTable.setStatus("current")
_CambiumGPSSatSNREntry_Object = MibTableRow
cambiumGPSSatSNREntry = _CambiumGPSSatSNREntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1)
)
cambiumGPSSatSNREntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "gpsSatelliteId"),
)
if mibBuilder.loadTexts:
    cambiumGPSSatSNREntry.setStatus("current")


class _GpsSatelliteId_Type(Integer32):
    """Custom type gpsSatelliteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GpsSatelliteId_Type.__name__ = "Integer32"
_GpsSatelliteId_Object = MibTableColumn
gpsSatelliteId = _GpsSatelliteId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 1),
    _GpsSatelliteId_Type()
)
gpsSatelliteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatelliteId.setStatus("current")


class _GpsSnrValue_Type(Integer32):
    """Custom type gpsSnrValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GpsSnrValue_Type.__name__ = "Integer32"
_GpsSnrValue_Object = MibTableColumn
gpsSnrValue = _GpsSnrValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 2),
    _GpsSnrValue_Type()
)
gpsSnrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSnrValue.setStatus("current")


class _GpsSatelliteStatus_Type(Integer32):
    """Custom type gpsSatelliteStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_GpsSatelliteStatus_Type.__name__ = "Integer32"
_GpsSatelliteStatus_Object = MibTableColumn
gpsSatelliteStatus = _GpsSatelliteStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 3),
    _GpsSatelliteStatus_Type()
)
gpsSatelliteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatelliteStatus.setStatus("current")


class _CambiumGPSDeviceInfo_Type(DisplayString):
    """Custom type cambiumGPSDeviceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSDeviceInfo_Type.__name__ = "DisplayString"
_CambiumGPSDeviceInfo_Object = MibScalar
cambiumGPSDeviceInfo = _CambiumGPSDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 9),
    _CambiumGPSDeviceInfo_Type()
)
cambiumGPSDeviceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSDeviceInfo.setStatus("current")


class _CambiumGPSFirmwareUpdateStatus_Type(Integer32):
    """Custom type cambiumGPSFirmwareUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumGPSFirmwareUpdateStatus_Type.__name__ = "Integer32"
_CambiumGPSFirmwareUpdateStatus_Object = MibScalar
cambiumGPSFirmwareUpdateStatus = _CambiumGPSFirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 10),
    _CambiumGPSFirmwareUpdateStatus_Type()
)
cambiumGPSFirmwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSFirmwareUpdateStatus.setStatus("current")


class _CambiumGPSAntennaType_Type(DisplayString):
    """Custom type cambiumGPSAntennaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CambiumGPSAntennaType_Type.__name__ = "DisplayString"
_CambiumGPSAntennaType_Object = MibScalar
cambiumGPSAntennaType = _CambiumGPSAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 11),
    _CambiumGPSAntennaType_Type()
)
cambiumGPSAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSAntennaType.setStatus("current")
_TddSyncInternalStateDur_Type = Integer32
_TddSyncInternalStateDur_Object = MibScalar
tddSyncInternalStateDur = _TddSyncInternalStateDur_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 12),
    _TddSyncInternalStateDur_Type()
)
tddSyncInternalStateDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncInternalStateDur.setStatus("current")
_TddSyncExpectedDrift_Type = Integer32
_TddSyncExpectedDrift_Object = MibScalar
tddSyncExpectedDrift = _TddSyncExpectedDrift_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 13),
    _TddSyncExpectedDrift_Type()
)
tddSyncExpectedDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncExpectedDrift.setStatus("current")
_TddSyncExpectedJitter_Type = Integer32
_TddSyncExpectedJitter_Object = MibScalar
tddSyncExpectedJitter = _TddSyncExpectedJitter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 14),
    _TddSyncExpectedJitter_Type()
)
tddSyncExpectedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncExpectedJitter.setStatus("current")
_TddSyncStatTable_Object = MibTable
tddSyncStatTable = _TddSyncStatTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15)
)
if mibBuilder.loadTexts:
    tddSyncStatTable.setStatus("current")
_TddSyncStatEntry_Object = MibTableRow
tddSyncStatEntry = _TddSyncStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1)
)
tddSyncStatEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "tddSyncStatPeriod"),
)
if mibBuilder.loadTexts:
    tddSyncStatEntry.setStatus("current")


class _TddSyncStatPeriod_Type(Integer32):
    """Custom type tddSyncStatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("minutes5", 1),
          ("hours1", 2),
          ("hours24", 3),
          ("alltime", 4))
    )


_TddSyncStatPeriod_Type.__name__ = "Integer32"
_TddSyncStatPeriod_Object = MibTableColumn
tddSyncStatPeriod = _TddSyncStatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 1),
    _TddSyncStatPeriod_Type()
)
tddSyncStatPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncStatPeriod.setStatus("current")
_TddSyncPulseCount_Type = Counter32
_TddSyncPulseCount_Object = MibTableColumn
tddSyncPulseCount = _TddSyncPulseCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 2),
    _TddSyncPulseCount_Type()
)
tddSyncPulseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncPulseCount.setStatus("current")
_TddSyncLostPulseCount_Type = Counter32
_TddSyncLostPulseCount_Object = MibTableColumn
tddSyncLostPulseCount = _TddSyncLostPulseCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 3),
    _TddSyncLostPulseCount_Type()
)
tddSyncLostPulseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncLostPulseCount.setStatus("current")
_TddSyncInvalidPulseCount_Type = Counter32
_TddSyncInvalidPulseCount_Object = MibTableColumn
tddSyncInvalidPulseCount = _TddSyncInvalidPulseCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 4),
    _TddSyncInvalidPulseCount_Type()
)
tddSyncInvalidPulseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncInvalidPulseCount.setStatus("current")
_TddSyncInvPulseDeviationMin_Type = Integer32
_TddSyncInvPulseDeviationMin_Object = MibTableColumn
tddSyncInvPulseDeviationMin = _TddSyncInvPulseDeviationMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 5),
    _TddSyncInvPulseDeviationMin_Type()
)
tddSyncInvPulseDeviationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncInvPulseDeviationMin.setStatus("current")
_TddSyncInvPulseDeviationMax_Type = Integer32
_TddSyncInvPulseDeviationMax_Object = MibTableColumn
tddSyncInvPulseDeviationMax = _TddSyncInvPulseDeviationMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 6),
    _TddSyncInvPulseDeviationMax_Type()
)
tddSyncInvPulseDeviationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncInvPulseDeviationMax.setStatus("current")


class _TddSyncInvPulseDeviationAvgAbs_Type(Integer32):
    """Custom type tddSyncInvPulseDeviationAvgAbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TddSyncInvPulseDeviationAvgAbs_Type.__name__ = "Integer32"
_TddSyncInvPulseDeviationAvgAbs_Object = MibTableColumn
tddSyncInvPulseDeviationAvgAbs = _TddSyncInvPulseDeviationAvgAbs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 7),
    _TddSyncInvPulseDeviationAvgAbs_Type()
)
tddSyncInvPulseDeviationAvgAbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncInvPulseDeviationAvgAbs.setStatus("current")
_TddSyncDriftMin_Type = Integer32
_TddSyncDriftMin_Object = MibTableColumn
tddSyncDriftMin = _TddSyncDriftMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 8),
    _TddSyncDriftMin_Type()
)
tddSyncDriftMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncDriftMin.setStatus("current")
_TddSyncDriftMax_Type = Integer32
_TddSyncDriftMax_Object = MibTableColumn
tddSyncDriftMax = _TddSyncDriftMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 9),
    _TddSyncDriftMax_Type()
)
tddSyncDriftMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncDriftMax.setStatus("current")
_TddSyncDriftAvg_Type = Integer32
_TddSyncDriftAvg_Object = MibTableColumn
tddSyncDriftAvg = _TddSyncDriftAvg_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 10),
    _TddSyncDriftAvg_Type()
)
tddSyncDriftAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncDriftAvg.setStatus("current")
_TddSyncJitterMin_Type = Integer32
_TddSyncJitterMin_Object = MibTableColumn
tddSyncJitterMin = _TddSyncJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 11),
    _TddSyncJitterMin_Type()
)
tddSyncJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncJitterMin.setStatus("current")
_TddSyncJitterMax_Type = Integer32
_TddSyncJitterMax_Object = MibTableColumn
tddSyncJitterMax = _TddSyncJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 12),
    _TddSyncJitterMax_Type()
)
tddSyncJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncJitterMax.setStatus("current")


class _TddSyncJitterAvgAbs_Type(Integer32):
    """Custom type tddSyncJitterAvgAbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TddSyncJitterAvgAbs_Type.__name__ = "Integer32"
_TddSyncJitterAvgAbs_Object = MibTableColumn
tddSyncJitterAvgAbs = _TddSyncJitterAvgAbs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 13),
    _TddSyncJitterAvgAbs_Type()
)
tddSyncJitterAvgAbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncJitterAvgAbs.setStatus("current")
_TddSyncState1Count_Type = Counter32
_TddSyncState1Count_Object = MibTableColumn
tddSyncState1Count = _TddSyncState1Count_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 14),
    _TddSyncState1Count_Type()
)
tddSyncState1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState1Count.setStatus("current")
_TddSyncState1Duration_Type = Counter32
_TddSyncState1Duration_Object = MibTableColumn
tddSyncState1Duration = _TddSyncState1Duration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 15),
    _TddSyncState1Duration_Type()
)
tddSyncState1Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState1Duration.setStatus("current")
_TddSyncState2Count_Type = Counter32
_TddSyncState2Count_Object = MibTableColumn
tddSyncState2Count = _TddSyncState2Count_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 16),
    _TddSyncState2Count_Type()
)
tddSyncState2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState2Count.setStatus("current")
_TddSyncState2Duration_Type = Counter32
_TddSyncState2Duration_Object = MibTableColumn
tddSyncState2Duration = _TddSyncState2Duration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 17),
    _TddSyncState2Duration_Type()
)
tddSyncState2Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState2Duration.setStatus("current")
_TddSyncState3Count_Type = Counter32
_TddSyncState3Count_Object = MibTableColumn
tddSyncState3Count = _TddSyncState3Count_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 18),
    _TddSyncState3Count_Type()
)
tddSyncState3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState3Count.setStatus("current")
_TddSyncState3Duration_Type = Counter32
_TddSyncState3Duration_Object = MibTableColumn
tddSyncState3Duration = _TddSyncState3Duration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 15, 1, 19),
    _TddSyncState3Duration_Type()
)
tddSyncState3Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tddSyncState3Duration.setStatus("current")
_CambiumLinkStatus_ObjectIdentity = ObjectIdentity
cambiumLinkStatus = _CambiumLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4)
)


class _CambiumLANStatus_Type(Integer32):
    """Custom type cambiumLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLANStatus_Type.__name__ = "Integer32"
_CambiumLANStatus_Object = MibScalar
cambiumLANStatus = _CambiumLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 1),
    _CambiumLANStatus_Type()
)
cambiumLANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANStatus.setStatus("current")


class _CambiumWLANStatus_Type(Integer32):
    """Custom type cambiumWLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumWLANStatus_Type.__name__ = "Integer32"
_CambiumWLANStatus_Object = MibScalar
cambiumWLANStatus = _CambiumWLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 2),
    _CambiumWLANStatus_Type()
)
cambiumWLANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWLANStatus.setStatus("current")
_CambiumEffectiveDeviceIPAddress_Type = IpAddress
_CambiumEffectiveDeviceIPAddress_Object = MibScalar
cambiumEffectiveDeviceIPAddress = _CambiumEffectiveDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 3),
    _CambiumEffectiveDeviceIPAddress_Type()
)
cambiumEffectiveDeviceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceIPAddress.setStatus("current")


class _CambiumEffectiveSTANetworkMode_Type(Integer32):
    """Custom type cambiumEffectiveSTANetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_CambiumEffectiveSTANetworkMode_Type.__name__ = "Integer32"
_CambiumEffectiveSTANetworkMode_Object = MibScalar
cambiumEffectiveSTANetworkMode = _CambiumEffectiveSTANetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 4),
    _CambiumEffectiveSTANetworkMode_Type()
)
cambiumEffectiveSTANetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSTANetworkMode.setStatus("current")
_CambiumEffectiveDeviceLANNetMask_Type = IpAddress
_CambiumEffectiveDeviceLANNetMask_Object = MibScalar
cambiumEffectiveDeviceLANNetMask = _CambiumEffectiveDeviceLANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 5),
    _CambiumEffectiveDeviceLANNetMask_Type()
)
cambiumEffectiveDeviceLANNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceLANNetMask.setStatus("current")
_CambiumEffectiveDeviceDefaultGateWay_Type = IpAddress
_CambiumEffectiveDeviceDefaultGateWay_Object = MibScalar
cambiumEffectiveDeviceDefaultGateWay = _CambiumEffectiveDeviceDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 6),
    _CambiumEffectiveDeviceDefaultGateWay_Type()
)
cambiumEffectiveDeviceDefaultGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceDefaultGateWay.setStatus("current")
_CambiumEffectiveDeviceDNSIPAddress_Type = IpAddress
_CambiumEffectiveDeviceDNSIPAddress_Object = MibScalar
cambiumEffectiveDeviceDNSIPAddress = _CambiumEffectiveDeviceDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 7),
    _CambiumEffectiveDeviceDNSIPAddress_Type()
)
cambiumEffectiveDeviceDNSIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceDNSIPAddress.setStatus("current")
_CambiumEffectiveWANIPAddress_Type = IpAddress
_CambiumEffectiveWANIPAddress_Object = MibScalar
cambiumEffectiveWANIPAddress = _CambiumEffectiveWANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 8),
    _CambiumEffectiveWANIPAddress_Type()
)
cambiumEffectiveWANIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveWANIPAddress.setStatus("current")
_CambiumEffectiveDeviceWANNetMask_Type = IpAddress
_CambiumEffectiveDeviceWANNetMask_Object = MibScalar
cambiumEffectiveDeviceWANNetMask = _CambiumEffectiveDeviceWANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 9),
    _CambiumEffectiveDeviceWANNetMask_Type()
)
cambiumEffectiveDeviceWANNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceWANNetMask.setStatus("current")


class _CambiumEffectiveDeviceWANPPPoEStatus_Type(Integer32):
    """Custom type cambiumEffectiveDeviceWANPPPoEStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumEffectiveDeviceWANPPPoEStatus_Type.__name__ = "Integer32"
_CambiumEffectiveDeviceWANPPPoEStatus_Object = MibScalar
cambiumEffectiveDeviceWANPPPoEStatus = _CambiumEffectiveDeviceWANPPPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 10),
    _CambiumEffectiveDeviceWANPPPoEStatus_Type()
)
cambiumEffectiveDeviceWANPPPoEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceWANPPPoEStatus.setStatus("current")


class _CambiumLANModeStatus_Type(Integer32):
    """Custom type cambiumLANModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLANModeStatus_Type.__name__ = "Integer32"
_CambiumLANModeStatus_Object = MibScalar
cambiumLANModeStatus = _CambiumLANModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 11),
    _CambiumLANModeStatus_Type()
)
cambiumLANModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANModeStatus.setStatus("current")


class _CambiumLANSpeedStatus_Type(Integer32):
    """Custom type cambiumLANSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_CambiumLANSpeedStatus_Type.__name__ = "Integer32"
_CambiumLANSpeedStatus_Object = MibScalar
cambiumLANSpeedStatus = _CambiumLANSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 12),
    _CambiumLANSpeedStatus_Type()
)
cambiumLANSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANSpeedStatus.setStatus("current")


class _CambiumDHCPOption82Status_Type(Integer32):
    """Custom type cambiumDHCPOption82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDHCPOption82Status_Type.__name__ = "Integer32"
_CambiumDHCPOption82Status_Object = MibScalar
cambiumDHCPOption82Status = _CambiumDHCPOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 13),
    _CambiumDHCPOption82Status_Type()
)
cambiumDHCPOption82Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption82Status.setStatus("current")


class _CambiumLAN2ModeStatus_Type(Integer32):
    """Custom type cambiumLAN2ModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLAN2ModeStatus_Type.__name__ = "Integer32"
_CambiumLAN2ModeStatus_Object = MibScalar
cambiumLAN2ModeStatus = _CambiumLAN2ModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 14),
    _CambiumLAN2ModeStatus_Type()
)
cambiumLAN2ModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2ModeStatus.setStatus("current")


class _CambiumLAN2SpeedStatus_Type(Integer32):
    """Custom type cambiumLAN2SpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_CambiumLAN2SpeedStatus_Type.__name__ = "Integer32"
_CambiumLAN2SpeedStatus_Object = MibScalar
cambiumLAN2SpeedStatus = _CambiumLAN2SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 15),
    _CambiumLAN2SpeedStatus_Type()
)
cambiumLAN2SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2SpeedStatus.setStatus("current")


class _CambiumLAN2Status_Type(Integer32):
    """Custom type cambiumLAN2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLAN2Status_Type.__name__ = "Integer32"
_CambiumLAN2Status_Object = MibScalar
cambiumLAN2Status = _CambiumLAN2Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 16),
    _CambiumLAN2Status_Type()
)
cambiumLAN2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2Status.setStatus("current")


class _CambiumDHCPOption66Status_Type(Integer32):
    """Custom type cambiumDHCPOption66Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumDHCPOption66Status_Type.__name__ = "Integer32"
_CambiumDHCPOption66Status_Object = MibScalar
cambiumDHCPOption66Status = _CambiumDHCPOption66Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 17),
    _CambiumDHCPOption66Status_Type()
)
cambiumDHCPOption66Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption66Status.setStatus("current")


class _CambiumDHCPOption66URL_Type(DisplayString):
    """Custom type cambiumDHCPOption66URL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDHCPOption66URL_Type.__name__ = "DisplayString"
_CambiumDHCPOption66URL_Object = MibScalar
cambiumDHCPOption66URL = _CambiumDHCPOption66URL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 18),
    _CambiumDHCPOption66URL_Type()
)
cambiumDHCPOption66URL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption66URL.setStatus("current")


class _CambiumDHCPOption66Error_Type(Integer32):
    """Custom type cambiumDHCPOption66Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumDHCPOption66Error_Type.__name__ = "Integer32"
_CambiumDHCPOption66Error_Object = MibScalar
cambiumDHCPOption66Error = _CambiumDHCPOption66Error_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 19),
    _CambiumDHCPOption66Error_Type()
)
cambiumDHCPOption66Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption66Error.setStatus("current")
_CambiumARPTable_Object = MibTable
cambiumARPTable = _CambiumARPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20)
)
if mibBuilder.loadTexts:
    cambiumARPTable.setStatus("current")
_CambiumARPEntry_Object = MibTableRow
cambiumARPEntry = _CambiumARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1)
)
cambiumARPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumARPIndex"),
)
if mibBuilder.loadTexts:
    cambiumARPEntry.setStatus("current")


class _CambiumARPIndex_Type(Integer32):
    """Custom type cambiumARPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CambiumARPIndex_Type.__name__ = "Integer32"
_CambiumARPIndex_Object = MibTableColumn
cambiumARPIndex = _CambiumARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 1),
    _CambiumARPIndex_Type()
)
cambiumARPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPIndex.setStatus("current")


class _CambiumARPMAC_Type(DisplayString):
    """Custom type cambiumARPMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CambiumARPMAC_Type.__name__ = "DisplayString"
_CambiumARPMAC_Object = MibTableColumn
cambiumARPMAC = _CambiumARPMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 2),
    _CambiumARPMAC_Type()
)
cambiumARPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPMAC.setStatus("current")
_CambiumARPIP_Type = IpAddress
_CambiumARPIP_Object = MibTableColumn
cambiumARPIP = _CambiumARPIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 3),
    _CambiumARPIP_Type()
)
cambiumARPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPIP.setStatus("current")


class _CambiumARPInterface_Type(DisplayString):
    """Custom type cambiumARPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_CambiumARPInterface_Type.__name__ = "DisplayString"
_CambiumARPInterface_Object = MibTableColumn
cambiumARPInterface = _CambiumARPInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 4),
    _CambiumARPInterface_Type()
)
cambiumARPInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPInterface.setStatus("current")


class _CambiumDHCPOption43URL_Type(DisplayString):
    """Custom type cambiumDHCPOption43URL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDHCPOption43URL_Type.__name__ = "DisplayString"
_CambiumDHCPOption43URL_Object = MibScalar
cambiumDHCPOption43URL = _CambiumDHCPOption43URL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 21),
    _CambiumDHCPOption43URL_Type()
)
cambiumDHCPOption43URL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption43URL.setStatus("current")


class _CambiumManagementIFStatus_Type(Integer32):
    """Custom type cambiumManagementIFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumManagementIFStatus_Type.__name__ = "Integer32"
_CambiumManagementIFStatus_Object = MibScalar
cambiumManagementIFStatus = _CambiumManagementIFStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 25),
    _CambiumManagementIFStatus_Type()
)
cambiumManagementIFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFStatus.setStatus("current")
_CambiumManagementIFIPAddress_Type = IpAddress
_CambiumManagementIFIPAddress_Object = MibScalar
cambiumManagementIFIPAddress = _CambiumManagementIFIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 26),
    _CambiumManagementIFIPAddress_Type()
)
cambiumManagementIFIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFIPAddress.setStatus("current")
_CambiumManagementIFNetMask_Type = IpAddress
_CambiumManagementIFNetMask_Object = MibScalar
cambiumManagementIFNetMask = _CambiumManagementIFNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 27),
    _CambiumManagementIFNetMask_Type()
)
cambiumManagementIFNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFNetMask.setStatus("current")
_CambiumManagementIFGateway_Type = IpAddress
_CambiumManagementIFGateway_Object = MibScalar
cambiumManagementIFGateway = _CambiumManagementIFGateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 28),
    _CambiumManagementIFGateway_Type()
)
cambiumManagementIFGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFGateway.setStatus("current")


class _CambiumEffectiveNetworkLanMTU_Type(Integer32):
    """Custom type cambiumEffectiveNetworkLanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_CambiumEffectiveNetworkLanMTU_Type.__name__ = "Integer32"
_CambiumEffectiveNetworkLanMTU_Object = MibScalar
cambiumEffectiveNetworkLanMTU = _CambiumEffectiveNetworkLanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 29),
    _CambiumEffectiveNetworkLanMTU_Type()
)
cambiumEffectiveNetworkLanMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNetworkLanMTU.setStatus("current")


class _CambiumEffectiveNetworkBridgeMTU_Type(Integer32):
    """Custom type cambiumEffectiveNetworkBridgeMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_CambiumEffectiveNetworkBridgeMTU_Type.__name__ = "Integer32"
_CambiumEffectiveNetworkBridgeMTU_Object = MibScalar
cambiumEffectiveNetworkBridgeMTU = _CambiumEffectiveNetworkBridgeMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 30),
    _CambiumEffectiveNetworkBridgeMTU_Type()
)
cambiumEffectiveNetworkBridgeMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNetworkBridgeMTU.setStatus("current")
_CambiumStaticRoutesTable_Object = MibTable
cambiumStaticRoutesTable = _CambiumStaticRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31)
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesTable.setStatus("current")
_CambiumStaticRoutesEntry_Object = MibTableRow
cambiumStaticRoutesEntry = _CambiumStaticRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1)
)
cambiumStaticRoutesEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumStaticRoutesIndex"),
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesEntry.setStatus("current")


class _CambiumStaticRoutesIndex_Type(Integer32):
    """Custom type cambiumStaticRoutesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CambiumStaticRoutesIndex_Type.__name__ = "Integer32"
_CambiumStaticRoutesIndex_Object = MibTableColumn
cambiumStaticRoutesIndex = _CambiumStaticRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 1),
    _CambiumStaticRoutesIndex_Type()
)
cambiumStaticRoutesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesIndex.setStatus("current")
_CambiumStaticRoutesDestIP_Type = IpAddress
_CambiumStaticRoutesDestIP_Object = MibTableColumn
cambiumStaticRoutesDestIP = _CambiumStaticRoutesDestIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 2),
    _CambiumStaticRoutesDestIP_Type()
)
cambiumStaticRoutesDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesDestIP.setStatus("current")
_CambiumStaticRoutesGW_Type = IpAddress
_CambiumStaticRoutesGW_Object = MibTableColumn
cambiumStaticRoutesGW = _CambiumStaticRoutesGW_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 3),
    _CambiumStaticRoutesGW_Type()
)
cambiumStaticRoutesGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesGW.setStatus("current")
_CambiumStaticRoutesNetmask_Type = IpAddress
_CambiumStaticRoutesNetmask_Object = MibTableColumn
cambiumStaticRoutesNetmask = _CambiumStaticRoutesNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 4),
    _CambiumStaticRoutesNetmask_Type()
)
cambiumStaticRoutesNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesNetmask.setStatus("current")


class _CambiumStaticRoutesInterface_Type(DisplayString):
    """Custom type cambiumStaticRoutesInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_CambiumStaticRoutesInterface_Type.__name__ = "DisplayString"
_CambiumStaticRoutesInterface_Object = MibTableColumn
cambiumStaticRoutesInterface = _CambiumStaticRoutesInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 5),
    _CambiumStaticRoutesInterface_Type()
)
cambiumStaticRoutesInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesInterface.setStatus("current")
_CambiumIPAliasTable_Object = MibTable
cambiumIPAliasTable = _CambiumIPAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32)
)
if mibBuilder.loadTexts:
    cambiumIPAliasTable.setStatus("current")
_CambiumIPAliasEntry_Object = MibTableRow
cambiumIPAliasEntry = _CambiumIPAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1)
)
cambiumIPAliasEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumIPAliasTableIndex"),
)
if mibBuilder.loadTexts:
    cambiumIPAliasEntry.setStatus("current")


class _CambiumIPAliasTableIndex_Type(Integer32):
    """Custom type cambiumIPAliasTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumIPAliasTableIndex_Type.__name__ = "Integer32"
_CambiumIPAliasTableIndex_Object = MibTableColumn
cambiumIPAliasTableIndex = _CambiumIPAliasTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 1),
    _CambiumIPAliasTableIndex_Type()
)
cambiumIPAliasTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasTableIndex.setStatus("current")
_CambiumIPAliasIP_Type = IpAddress
_CambiumIPAliasIP_Object = MibTableColumn
cambiumIPAliasIP = _CambiumIPAliasIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 2),
    _CambiumIPAliasIP_Type()
)
cambiumIPAliasIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasIP.setStatus("current")
_CambiumIPAliasNetmask_Type = IpAddress
_CambiumIPAliasNetmask_Object = MibTableColumn
cambiumIPAliasNetmask = _CambiumIPAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 3),
    _CambiumIPAliasNetmask_Type()
)
cambiumIPAliasNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasNetmask.setStatus("current")


class _CambiumCnsServConsStat_Type(DisplayString):
    """Custom type cambiumCnsServConsStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCnsServConsStat_Type.__name__ = "DisplayString"
_CambiumCnsServConsStat_Object = MibScalar
cambiumCnsServConsStat = _CambiumCnsServConsStat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 33),
    _CambiumCnsServConsStat_Type()
)
cambiumCnsServConsStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCnsServConsStat.setStatus("current")


class _CambiumCnsServAccountID_Type(DisplayString):
    """Custom type cambiumCnsServAccountID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCnsServAccountID_Type.__name__ = "DisplayString"
_CambiumCnsServAccountID_Object = MibScalar
cambiumCnsServAccountID = _CambiumCnsServAccountID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 34),
    _CambiumCnsServAccountID_Type()
)
cambiumCnsServAccountID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCnsServAccountID.setStatus("current")


class _CambiumAPCnsMGMTState_Type(Integer32):
    """Custom type cambiumAPCnsMGMTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambiumAPCnsMGMTState_Type.__name__ = "Integer32"
_CambiumAPCnsMGMTState_Object = MibScalar
cambiumAPCnsMGMTState = _CambiumAPCnsMGMTState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 35),
    _CambiumAPCnsMGMTState_Type()
)
cambiumAPCnsMGMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCnsMGMTState.setStatus("current")
_CambiumEffectiveDeviceIPv6Address_Type = Ipv6Address
_CambiumEffectiveDeviceIPv6Address_Object = MibScalar
cambiumEffectiveDeviceIPv6Address = _CambiumEffectiveDeviceIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 36),
    _CambiumEffectiveDeviceIPv6Address_Type()
)
cambiumEffectiveDeviceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceIPv6Address.setStatus("current")
_CambiumLinkLocalDeviceIPv6Address_Type = Ipv6Address
_CambiumLinkLocalDeviceIPv6Address_Object = MibScalar
cambiumLinkLocalDeviceIPv6Address = _CambiumLinkLocalDeviceIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 37),
    _CambiumLinkLocalDeviceIPv6Address_Type()
)
cambiumLinkLocalDeviceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkLocalDeviceIPv6Address.setStatus("current")
_CambiumEffectiveWANIPv6Address_Type = Ipv6Address
_CambiumEffectiveWANIPv6Address_Object = MibScalar
cambiumEffectiveWANIPv6Address = _CambiumEffectiveWANIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 38),
    _CambiumEffectiveWANIPv6Address_Type()
)
cambiumEffectiveWANIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveWANIPv6Address.setStatus("current")
_CambiumLinkLocalWANIPv6Address_Type = Ipv6Address
_CambiumLinkLocalWANIPv6Address_Object = MibScalar
cambiumLinkLocalWANIPv6Address = _CambiumLinkLocalWANIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 39),
    _CambiumLinkLocalWANIPv6Address_Type()
)
cambiumLinkLocalWANIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkLocalWANIPv6Address.setStatus("current")
_CambiumManagementIFIPv6Address_Type = Ipv6Address
_CambiumManagementIFIPv6Address_Object = MibScalar
cambiumManagementIFIPv6Address = _CambiumManagementIFIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 40),
    _CambiumManagementIFIPv6Address_Type()
)
cambiumManagementIFIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFIPv6Address.setStatus("current")
_CambiumLinkLocalManagementIFIPv6Address_Type = Ipv6Address
_CambiumLinkLocalManagementIFIPv6Address_Object = MibScalar
cambiumLinkLocalManagementIFIPv6Address = _CambiumLinkLocalManagementIFIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 41),
    _CambiumLinkLocalManagementIFIPv6Address_Type()
)
cambiumLinkLocalManagementIFIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkLocalManagementIFIPv6Address.setStatus("current")
_CambiumEffectiveDeviceIPv6DefaultGateWay_Type = Ipv6Address
_CambiumEffectiveDeviceIPv6DefaultGateWay_Object = MibScalar
cambiumEffectiveDeviceIPv6DefaultGateWay = _CambiumEffectiveDeviceIPv6DefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 42),
    _CambiumEffectiveDeviceIPv6DefaultGateWay_Type()
)
cambiumEffectiveDeviceIPv6DefaultGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceIPv6DefaultGateWay.setStatus("current")
_CambiumManagementIFIPv6Gateway_Type = Ipv6Address
_CambiumManagementIFIPv6Gateway_Object = MibScalar
cambiumManagementIFIPv6Gateway = _CambiumManagementIFIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 43),
    _CambiumManagementIFIPv6Gateway_Type()
)
cambiumManagementIFIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFIPv6Gateway.setStatus("current")


class _CambiumSFPConnectorType_Type(Integer32):
    """Custom type cambiumSFPConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CambiumSFPConnectorType_Type.__name__ = "Integer32"
_CambiumSFPConnectorType_Object = MibScalar
cambiumSFPConnectorType = _CambiumSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 44),
    _CambiumSFPConnectorType_Type()
)
cambiumSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPConnectorType.setStatus("current")


class _CambiumSFPEthernetCodes_Type(Integer32):
    """Custom type cambiumSFPEthernetCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_CambiumSFPEthernetCodes_Type.__name__ = "Integer32"
_CambiumSFPEthernetCodes_Object = MibScalar
cambiumSFPEthernetCodes = _CambiumSFPEthernetCodes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 45),
    _CambiumSFPEthernetCodes_Type()
)
cambiumSFPEthernetCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPEthernetCodes.setStatus("current")


class _CambiumSFPEncodingCodes_Type(Integer32):
    """Custom type cambiumSFPEncodingCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CambiumSFPEncodingCodes_Type.__name__ = "Integer32"
_CambiumSFPEncodingCodes_Object = MibScalar
cambiumSFPEncodingCodes = _CambiumSFPEncodingCodes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 46),
    _CambiumSFPEncodingCodes_Type()
)
cambiumSFPEncodingCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPEncodingCodes.setStatus("current")
_CambiumSFPBRNominal_Type = Integer32
_CambiumSFPBRNominal_Object = MibScalar
cambiumSFPBRNominal = _CambiumSFPBRNominal_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 47),
    _CambiumSFPBRNominal_Type()
)
cambiumSFPBRNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPBRNominal.setStatus("current")


class _CambiumSFPVendorName_Type(DisplayString):
    """Custom type cambiumSFPVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CambiumSFPVendorName_Type.__name__ = "DisplayString"
_CambiumSFPVendorName_Object = MibScalar
cambiumSFPVendorName = _CambiumSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 48),
    _CambiumSFPVendorName_Type()
)
cambiumSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPVendorName.setStatus("current")


class _CambiumSFPVendorOUI_Type(DisplayString):
    """Custom type cambiumSFPVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_CambiumSFPVendorOUI_Type.__name__ = "DisplayString"
_CambiumSFPVendorOUI_Object = MibScalar
cambiumSFPVendorOUI = _CambiumSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 49),
    _CambiumSFPVendorOUI_Type()
)
cambiumSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPVendorOUI.setStatus("current")


class _CambiumSFPVendorPN_Type(DisplayString):
    """Custom type cambiumSFPVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CambiumSFPVendorPN_Type.__name__ = "DisplayString"
_CambiumSFPVendorPN_Object = MibScalar
cambiumSFPVendorPN = _CambiumSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 50),
    _CambiumSFPVendorPN_Type()
)
cambiumSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSFPVendorPN.setStatus("current")


class _CambiumEffectiveNetworkLan2MTU_Type(Integer32):
    """Custom type cambiumEffectiveNetworkLan2MTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_CambiumEffectiveNetworkLan2MTU_Type.__name__ = "Integer32"
_CambiumEffectiveNetworkLan2MTU_Object = MibScalar
cambiumEffectiveNetworkLan2MTU = _CambiumEffectiveNetworkLan2MTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 51),
    _CambiumEffectiveNetworkLan2MTU_Type()
)
cambiumEffectiveNetworkLan2MTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNetworkLan2MTU.setStatus("current")
_CambiumEffectiveManagementIFIPv6Address_Type = Ipv6Address
_CambiumEffectiveManagementIFIPv6Address_Object = MibScalar
cambiumEffectiveManagementIFIPv6Address = _CambiumEffectiveManagementIFIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 52),
    _CambiumEffectiveManagementIFIPv6Address_Type()
)
cambiumEffectiveManagementIFIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveManagementIFIPv6Address.setStatus("current")
_CambiumLanIPv6PrefixDelegated_Type = Ipv6Address
_CambiumLanIPv6PrefixDelegated_Object = MibScalar
cambiumLanIPv6PrefixDelegated = _CambiumLanIPv6PrefixDelegated_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 53),
    _CambiumLanIPv6PrefixDelegated_Type()
)
cambiumLanIPv6PrefixDelegated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLanIPv6PrefixDelegated.setStatus("current")


class _LanSwitchPortsNum_Type(Integer32):
    """Custom type lanSwitchPortsNum based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_LanSwitchPortsNum_Type.__name__ = "Integer32"
_LanSwitchPortsNum_Object = MibScalar
lanSwitchPortsNum = _LanSwitchPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 60),
    _LanSwitchPortsNum_Type()
)
lanSwitchPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortsNum.setStatus("current")
_LanSwitchPortStatusTable_Object = MibTable
lanSwitchPortStatusTable = _LanSwitchPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61)
)
if mibBuilder.loadTexts:
    lanSwitchPortStatusTable.setStatus("current")
_LanSwitchPortStatusEntry_Object = MibTableRow
lanSwitchPortStatusEntry = _LanSwitchPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1)
)
lanSwitchPortStatusEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "lanSwitchPortsNum"),
)
if mibBuilder.loadTexts:
    lanSwitchPortStatusEntry.setStatus("current")
_LanSwitchPortCAPS_Type = Integer32
_LanSwitchPortCAPS_Object = MibTableColumn
lanSwitchPortCAPS = _LanSwitchPortCAPS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 1),
    _LanSwitchPortCAPS_Type()
)
lanSwitchPortCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortCAPS.setStatus("current")
_LanSwitchPortEnableStatus_Type = Integer32
_LanSwitchPortEnableStatus_Object = MibTableColumn
lanSwitchPortEnableStatus = _LanSwitchPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 2),
    _LanSwitchPortEnableStatus_Type()
)
lanSwitchPortEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortEnableStatus.setStatus("current")
_LanSwitchPortLinkStatus_Type = Integer32
_LanSwitchPortLinkStatus_Object = MibTableColumn
lanSwitchPortLinkStatus = _LanSwitchPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 3),
    _LanSwitchPortLinkStatus_Type()
)
lanSwitchPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortLinkStatus.setStatus("current")
_LanSwitchPortAutonegStatus_Type = Integer32
_LanSwitchPortAutonegStatus_Object = MibTableColumn
lanSwitchPortAutonegStatus = _LanSwitchPortAutonegStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 4),
    _LanSwitchPortAutonegStatus_Type()
)
lanSwitchPortAutonegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortAutonegStatus.setStatus("current")
_LanSwitchPortSpeedStatus_Type = Integer32
_LanSwitchPortSpeedStatus_Object = MibTableColumn
lanSwitchPortSpeedStatus = _LanSwitchPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 5),
    _LanSwitchPortSpeedStatus_Type()
)
lanSwitchPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortSpeedStatus.setStatus("current")
_LanSwitchPortDuplexStatus_Type = Integer32
_LanSwitchPortDuplexStatus_Object = MibTableColumn
lanSwitchPortDuplexStatus = _LanSwitchPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 6),
    _LanSwitchPortDuplexStatus_Type()
)
lanSwitchPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortDuplexStatus.setStatus("current")
_LanSwitchPortPoEStatus_Type = Integer32
_LanSwitchPortPoEStatus_Object = MibTableColumn
lanSwitchPortPoEStatus = _LanSwitchPortPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 7),
    _LanSwitchPortPoEStatus_Type()
)
lanSwitchPortPoEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortPoEStatus.setStatus("current")
_LanSwitchPortPoEVoltage_Type = Integer32
_LanSwitchPortPoEVoltage_Object = MibTableColumn
lanSwitchPortPoEVoltage = _LanSwitchPortPoEVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 8),
    _LanSwitchPortPoEVoltage_Type()
)
lanSwitchPortPoEVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortPoEVoltage.setStatus("current")
_LanSwitchPortPoECurrent_Type = Integer32
_LanSwitchPortPoECurrent_Object = MibTableColumn
lanSwitchPortPoECurrent = _LanSwitchPortPoECurrent_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 61, 1, 9),
    _LanSwitchPortPoECurrent_Type()
)
lanSwitchPortPoECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortPoECurrent.setStatus("current")


class _CambiumWLAN2Status_Type(Integer32):
    """Custom type cambiumWLAN2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumWLAN2Status_Type.__name__ = "Integer32"
_CambiumWLAN2Status_Object = MibScalar
cambiumWLAN2Status = _CambiumWLAN2Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 102),
    _CambiumWLAN2Status_Type()
)
cambiumWLAN2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWLAN2Status.setStatus("current")
_CambiumAcsStatus_ObjectIdentity = ObjectIdentity
cambiumAcsStatus = _CambiumAcsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 5)
)


class _AcsState_Type(Integer32):
    """Custom type acsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcsState_Type.__name__ = "Integer32"
_AcsState_Object = MibScalar
acsState = _AcsState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 5, 1),
    _AcsState_Type()
)
acsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsState.setStatus("current")
_CambiumMcastStatus_ObjectIdentity = ObjectIdentity
cambiumMcastStatus = _CambiumMcastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6)
)


class _CambiumEffectiveMcastGroupLimit_Type(Integer32):
    """Custom type cambiumEffectiveMcastGroupLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumEffectiveMcastGroupLimit_Type.__name__ = "Integer32"
_CambiumEffectiveMcastGroupLimit_Object = MibScalar
cambiumEffectiveMcastGroupLimit = _CambiumEffectiveMcastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 1),
    _CambiumEffectiveMcastGroupLimit_Type()
)
cambiumEffectiveMcastGroupLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveMcastGroupLimit.setStatus("current")


class _CambiumSubscribedMcastGroupNum_Type(Integer32):
    """Custom type cambiumSubscribedMcastGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumSubscribedMcastGroupNum_Type.__name__ = "Integer32"
_CambiumSubscribedMcastGroupNum_Object = MibScalar
cambiumSubscribedMcastGroupNum = _CambiumSubscribedMcastGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 2),
    _CambiumSubscribedMcastGroupNum_Type()
)
cambiumSubscribedMcastGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupNum.setStatus("current")


class _CambiumAPMcastTotalGroupCount_Type(Integer32):
    """Custom type cambiumAPMcastTotalGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CambiumAPMcastTotalGroupCount_Type.__name__ = "Integer32"
_CambiumAPMcastTotalGroupCount_Object = MibScalar
cambiumAPMcastTotalGroupCount = _CambiumAPMcastTotalGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 3),
    _CambiumAPMcastTotalGroupCount_Type()
)
cambiumAPMcastTotalGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPMcastTotalGroupCount.setStatus("current")


class _CambiumMcastHandlingStatus_Type(Integer32):
    """Custom type cambiumMcastHandlingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
    )


_CambiumMcastHandlingStatus_Type.__name__ = "Integer32"
_CambiumMcastHandlingStatus_Object = MibScalar
cambiumMcastHandlingStatus = _CambiumMcastHandlingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 4),
    _CambiumMcastHandlingStatus_Type()
)
cambiumMcastHandlingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMcastHandlingStatus.setStatus("current")
_CambiumSubscribedMcastGroupTable_Object = MibTable
cambiumSubscribedMcastGroupTable = _CambiumSubscribedMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10)
)
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupTable.setStatus("current")
_CambiumSubscribedMcastGroupEntry_Object = MibTableRow
cambiumSubscribedMcastGroupEntry = _CambiumSubscribedMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10, 1)
)
cambiumSubscribedMcastGroupEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumSubscribedMcastGroupNum"),
)
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupEntry.setStatus("current")
_CambiumRegisteredMcastGroupIP_Type = IpAddress
_CambiumRegisteredMcastGroupIP_Object = MibTableColumn
cambiumRegisteredMcastGroupIP = _CambiumRegisteredMcastGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10, 1, 1),
    _CambiumRegisteredMcastGroupIP_Type()
)
cambiumRegisteredMcastGroupIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRegisteredMcastGroupIP.setStatus("current")
_CambiumDhcpStatus_ObjectIdentity = ObjectIdentity
cambiumDhcpStatus = _CambiumDhcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7)
)
_DhcpServerStartIP_Type = IpAddress
_DhcpServerStartIP_Object = MibScalar
dhcpServerStartIP = _DhcpServerStartIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 1),
    _DhcpServerStartIP_Type()
)
dhcpServerStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStartIP.setStatus("current")
_DhcpServerEndIP_Type = IpAddress
_DhcpServerEndIP_Object = MibScalar
dhcpServerEndIP = _DhcpServerEndIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 2),
    _DhcpServerEndIP_Type()
)
dhcpServerEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerEndIP.setStatus("current")
_DhcpServerGatewayIP_Type = IpAddress
_DhcpServerGatewayIP_Object = MibScalar
dhcpServerGatewayIP = _DhcpServerGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 3),
    _DhcpServerGatewayIP_Type()
)
dhcpServerGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerGatewayIP.setStatus("current")
_DhcpServerDNSIP_Type = IpAddress
_DhcpServerDNSIP_Object = MibScalar
dhcpServerDNSIP = _DhcpServerDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 4),
    _DhcpServerDNSIP_Type()
)
dhcpServerDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDNSIP.setStatus("current")
_DhcpServerStaticHostTable_Object = MibTable
dhcpServerStaticHostTable = _DhcpServerStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5)
)
if mibBuilder.loadTexts:
    dhcpServerStaticHostTable.setStatus("current")
_DhcpServerStaticHostEntry_Object = MibTableRow
dhcpServerStaticHostEntry = _DhcpServerStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1)
)
dhcpServerStaticHostEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpStaticIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerStaticHostEntry.setStatus("current")


class _DhcpStaticIndex_Type(Integer32):
    """Custom type dhcpStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpStaticIndex_Type.__name__ = "Integer32"
_DhcpStaticIndex_Object = MibTableColumn
dhcpStaticIndex = _DhcpStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 1),
    _DhcpStaticIndex_Type()
)
dhcpStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIndex.setStatus("current")


class _DhcpStaticMAC_Type(DisplayString):
    """Custom type dhcpStaticMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpStaticMAC_Type.__name__ = "DisplayString"
_DhcpStaticMAC_Object = MibTableColumn
dhcpStaticMAC = _DhcpStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 2),
    _DhcpStaticMAC_Type()
)
dhcpStaticMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticMAC.setStatus("current")
_DhcpStaticIP_Type = IpAddress
_DhcpStaticIP_Object = MibTableColumn
dhcpStaticIP = _DhcpStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 3),
    _DhcpStaticIP_Type()
)
dhcpStaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIP.setStatus("current")
_DhcpServerLeaseTable_Object = MibTable
dhcpServerLeaseTable = _DhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dhcpServerLeaseTable.setStatus("current")
_DhcpServerLeaseEntry_Object = MibTableRow
dhcpServerLeaseEntry = _DhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1)
)
dhcpServerLeaseEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpLeaseIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerLeaseEntry.setStatus("current")


class _DhcpLeaseIndex_Type(Integer32):
    """Custom type dhcpLeaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpLeaseIndex_Type.__name__ = "Integer32"
_DhcpLeaseIndex_Object = MibTableColumn
dhcpLeaseIndex = _DhcpLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 1),
    _DhcpLeaseIndex_Type()
)
dhcpLeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIndex.setStatus("current")


class _DhcpLeaseMAC_Type(DisplayString):
    """Custom type dhcpLeaseMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpLeaseMAC_Type.__name__ = "DisplayString"
_DhcpLeaseMAC_Object = MibTableColumn
dhcpLeaseMAC = _DhcpLeaseMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 2),
    _DhcpLeaseMAC_Type()
)
dhcpLeaseMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseMAC.setStatus("current")
_DhcpLeaseIP_Type = IpAddress
_DhcpLeaseIP_Object = MibTableColumn
dhcpLeaseIP = _DhcpLeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 3),
    _DhcpLeaseIP_Type()
)
dhcpLeaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIP.setStatus("current")
_DhcpLeaseDevName_Type = DisplayString
_DhcpLeaseDevName_Object = MibTableColumn
dhcpLeaseDevName = _DhcpLeaseDevName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 4),
    _DhcpLeaseDevName_Type()
)
dhcpLeaseDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseDevName.setStatus("current")
_CambiumLicenseInfo_ObjectIdentity = ObjectIdentity
cambiumLicenseInfo = _CambiumLicenseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8)
)


class _CambLicenseVersion_Type(DisplayString):
    """Custom type cambLicenseVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_CambLicenseVersion_Type.__name__ = "DisplayString"
_CambLicenseVersion_Object = MibScalar
cambLicenseVersion = _CambLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 1),
    _CambLicenseVersion_Type()
)
cambLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseVersion.setStatus("current")


class _CambLicenseSMcntUnlock_Type(DisplayString):
    """Custom type cambLicenseSMcntUnlock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_CambLicenseSMcntUnlock_Type.__name__ = "DisplayString"
_CambLicenseSMcntUnlock_Object = MibScalar
cambLicenseSMcntUnlock = _CambLicenseSMcntUnlock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 2),
    _CambLicenseSMcntUnlock_Type()
)
cambLicenseSMcntUnlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseSMcntUnlock.setStatus("current")


class _CambLicenseMACaddr_Type(DisplayString):
    """Custom type cambLicenseMACaddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CambLicenseMACaddr_Type.__name__ = "DisplayString"
_CambLicenseMACaddr_Object = MibScalar
cambLicenseMACaddr = _CambLicenseMACaddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 3),
    _CambLicenseMACaddr_Type()
)
cambLicenseMACaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseMACaddr.setStatus("current")


class _CambLicenseCountry_Type(DisplayString):
    """Custom type cambLicenseCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 2),
    )


_CambLicenseCountry_Type.__name__ = "DisplayString"
_CambLicenseCountry_Object = MibScalar
cambLicenseCountry = _CambLicenseCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 4),
    _CambLicenseCountry_Type()
)
cambLicenseCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseCountry.setStatus("current")


class _CambLicenseStatus_Type(Integer32):
    """Custom type cambLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CambLicenseStatus_Type.__name__ = "Integer32"
_CambLicenseStatus_Object = MibScalar
cambLicenseStatus = _CambLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 5),
    _CambLicenseStatus_Type()
)
cambLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseStatus.setStatus("current")


class _CambLicenseDPIUnlockQoS_Type(Integer32):
    """Custom type cambLicenseDPIUnlockQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambLicenseDPIUnlockQoS_Type.__name__ = "Integer32"
_CambLicenseDPIUnlockQoS_Object = MibScalar
cambLicenseDPIUnlockQoS = _CambLicenseDPIUnlockQoS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 8, 6),
    _CambLicenseDPIUnlockQoS_Type()
)
cambLicenseDPIUnlockQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambLicenseDPIUnlockQoS.setStatus("current")
_CambiumRadiusVSAStatus_ObjectIdentity = ObjectIdentity
cambiumRadiusVSAStatus = _CambiumRadiusVSAStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9)
)


class _NetworkRadiusVSAmgmtVLANVID_Type(Integer32):
    """Custom type networkRadiusVSAmgmtVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmgmtVLANVID_Type.__name__ = "Integer32"
_NetworkRadiusVSAmgmtVLANVID_Object = MibScalar
networkRadiusVSAmgmtVLANVID = _NetworkRadiusVSAmgmtVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 1),
    _NetworkRadiusVSAmgmtVLANVID_Type()
)
networkRadiusVSAmgmtVLANVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmgmtVLANVID.setStatus("current")


class _NetworkRadiusVSAmgmtVLANVP_Type(Integer32):
    """Custom type networkRadiusVSAmgmtVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 7),
    )


_NetworkRadiusVSAmgmtVLANVP_Type.__name__ = "Integer32"
_NetworkRadiusVSAmgmtVLANVP_Object = MibScalar
networkRadiusVSAmgmtVLANVP = _NetworkRadiusVSAmgmtVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 2),
    _NetworkRadiusVSAmgmtVLANVP_Type()
)
networkRadiusVSAmgmtVLANVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmgmtVLANVP.setStatus("current")


class _NetworkRadiusVSAdataVLANVID_Type(Integer32):
    """Custom type networkRadiusVSAdataVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAdataVLANVID_Type.__name__ = "Integer32"
_NetworkRadiusVSAdataVLANVID_Object = MibScalar
networkRadiusVSAdataVLANVID = _NetworkRadiusVSAdataVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 3),
    _NetworkRadiusVSAdataVLANVID_Type()
)
networkRadiusVSAdataVLANVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAdataVLANVID.setStatus("current")


class _NetworkRadiusVSAdataVLANVP_Type(Integer32):
    """Custom type networkRadiusVSAdataVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 7),
    )


_NetworkRadiusVSAdataVLANVP_Type.__name__ = "Integer32"
_NetworkRadiusVSAdataVLANVP_Object = MibScalar
networkRadiusVSAdataVLANVP = _NetworkRadiusVSAdataVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 4),
    _NetworkRadiusVSAdataVLANVP_Type()
)
networkRadiusVSAdataVLANVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAdataVLANVP.setStatus("current")


class _NetworkRadiusVSAmgmtIFVID_Type(Integer32):
    """Custom type networkRadiusVSAmgmtIFVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmgmtIFVID_Type.__name__ = "Integer32"
_NetworkRadiusVSAmgmtIFVID_Object = MibScalar
networkRadiusVSAmgmtIFVID = _NetworkRadiusVSAmgmtIFVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 5),
    _NetworkRadiusVSAmgmtIFVID_Type()
)
networkRadiusVSAmgmtIFVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmgmtIFVID.setStatus("current")


class _NetworkRadiusVSAmgmtIFVP_Type(Integer32):
    """Custom type networkRadiusVSAmgmtIFVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 7),
    )


_NetworkRadiusVSAmgmtIFVP_Type.__name__ = "Integer32"
_NetworkRadiusVSAmgmtIFVP_Object = MibScalar
networkRadiusVSAmgmtIFVP = _NetworkRadiusVSAmgmtIFVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 6),
    _NetworkRadiusVSAmgmtIFVP_Type()
)
networkRadiusVSAmgmtIFVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmgmtIFVP.setStatus("current")


class _NetworkRadiusVSAmcastVLANVID_Type(Integer32):
    """Custom type networkRadiusVSAmcastVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmcastVLANVID_Type.__name__ = "Integer32"
_NetworkRadiusVSAmcastVLANVID_Object = MibScalar
networkRadiusVSAmcastVLANVID = _NetworkRadiusVSAmcastVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 7),
    _NetworkRadiusVSAmcastVLANVID_Type()
)
networkRadiusVSAmcastVLANVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmcastVLANVID.setStatus("current")


class _NetworkRadiusVSAGUIauthType_Type(Integer32):
    """Custom type networkRadiusVSAGUIauthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkRadiusVSAGUIauthType_Type.__name__ = "Integer32"
_NetworkRadiusVSAGUIauthType_Object = MibScalar
networkRadiusVSAGUIauthType = _NetworkRadiusVSAGUIauthType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 8),
    _NetworkRadiusVSAGUIauthType_Type()
)
networkRadiusVSAGUIauthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAGUIauthType.setStatus("current")
_NetworkRadiusVSAmembershipVLANTable_Object = MibTable
networkRadiusVSAmembershipVLANTable = _NetworkRadiusVSAmembershipVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 10)
)
if mibBuilder.loadTexts:
    networkRadiusVSAmembershipVLANTable.setStatus("current")
_NetworkRadiusVSAmembershipVLANEntry_Object = MibTableRow
networkRadiusVSAmembershipVLANEntry = _NetworkRadiusVSAmembershipVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 10, 1)
)
networkRadiusVSAmembershipVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "networkRadiusVSAmembershipVLANIndex"),
)
if mibBuilder.loadTexts:
    networkRadiusVSAmembershipVLANEntry.setStatus("current")


class _NetworkRadiusVSAmembershipVLANIndex_Type(Integer32):
    """Custom type networkRadiusVSAmembershipVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NetworkRadiusVSAmembershipVLANIndex_Type.__name__ = "Integer32"
_NetworkRadiusVSAmembershipVLANIndex_Object = MibTableColumn
networkRadiusVSAmembershipVLANIndex = _NetworkRadiusVSAmembershipVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 10, 1, 1),
    _NetworkRadiusVSAmembershipVLANIndex_Type()
)
networkRadiusVSAmembershipVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmembershipVLANIndex.setStatus("current")


class _NetworkRadiusVSAmembershipVLANVIDBegin_Type(Integer32):
    """Custom type networkRadiusVSAmembershipVLANVIDBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmembershipVLANVIDBegin_Type.__name__ = "Integer32"
_NetworkRadiusVSAmembershipVLANVIDBegin_Object = MibTableColumn
networkRadiusVSAmembershipVLANVIDBegin = _NetworkRadiusVSAmembershipVLANVIDBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 10, 1, 2),
    _NetworkRadiusVSAmembershipVLANVIDBegin_Type()
)
networkRadiusVSAmembershipVLANVIDBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmembershipVLANVIDBegin.setStatus("current")


class _NetworkRadiusVSAmembershipVLANVIDEnd_Type(Integer32):
    """Custom type networkRadiusVSAmembershipVLANVIDEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmembershipVLANVIDEnd_Type.__name__ = "Integer32"
_NetworkRadiusVSAmembershipVLANVIDEnd_Object = MibTableColumn
networkRadiusVSAmembershipVLANVIDEnd = _NetworkRadiusVSAmembershipVLANVIDEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 10, 1, 3),
    _NetworkRadiusVSAmembershipVLANVIDEnd_Type()
)
networkRadiusVSAmembershipVLANVIDEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmembershipVLANVIDEnd.setStatus("current")
_NetworkRadiusVSAmappingVLANTable_Object = MibTable
networkRadiusVSAmappingVLANTable = _NetworkRadiusVSAmappingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 20)
)
if mibBuilder.loadTexts:
    networkRadiusVSAmappingVLANTable.setStatus("current")
_NetworkRadiusVSAmappingVLANEntry_Object = MibTableRow
networkRadiusVSAmappingVLANEntry = _NetworkRadiusVSAmappingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 20, 1)
)
networkRadiusVSAmappingVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "networkRadiusVSAmappingVLANIndex"),
)
if mibBuilder.loadTexts:
    networkRadiusVSAmappingVLANEntry.setStatus("current")


class _NetworkRadiusVSAmappingVLANIndex_Type(Integer32):
    """Custom type networkRadiusVSAmappingVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NetworkRadiusVSAmappingVLANIndex_Type.__name__ = "Integer32"
_NetworkRadiusVSAmappingVLANIndex_Object = MibTableColumn
networkRadiusVSAmappingVLANIndex = _NetworkRadiusVSAmappingVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 20, 1, 1),
    _NetworkRadiusVSAmappingVLANIndex_Type()
)
networkRadiusVSAmappingVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmappingVLANIndex.setStatus("current")


class _NetworkRadiusVSAmappingVLANCVLAN_Type(Integer32):
    """Custom type networkRadiusVSAmappingVLANCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmappingVLANCVLAN_Type.__name__ = "Integer32"
_NetworkRadiusVSAmappingVLANCVLAN_Object = MibTableColumn
networkRadiusVSAmappingVLANCVLAN = _NetworkRadiusVSAmappingVLANCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 20, 1, 2),
    _NetworkRadiusVSAmappingVLANCVLAN_Type()
)
networkRadiusVSAmappingVLANCVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmappingVLANCVLAN.setStatus("current")


class _NetworkRadiusVSAmappingVLANSVLAN_Type(Integer32):
    """Custom type networkRadiusVSAmappingVLANSVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_NetworkRadiusVSAmappingVLANSVLAN_Type.__name__ = "Integer32"
_NetworkRadiusVSAmappingVLANSVLAN_Object = MibTableColumn
networkRadiusVSAmappingVLANSVLAN = _NetworkRadiusVSAmappingVLANSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 9, 20, 1, 3),
    _NetworkRadiusVSAmappingVLANSVLAN_Type()
)
networkRadiusVSAmappingVLANSVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRadiusVSAmappingVLANSVLAN.setStatus("current")
_CambiumCCTVStatus_ObjectIdentity = ObjectIdentity
cambiumCCTVStatus = _CambiumCCTVStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10)
)
_CambiumONVIFTable_Object = MibTable
cambiumONVIFTable = _CambiumONVIFTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cambiumONVIFTable.setStatus("current")
_CambiumONVIFEntry_Object = MibTableRow
cambiumONVIFEntry = _CambiumONVIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1)
)
cambiumONVIFEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumONVIFMAC"),
)
if mibBuilder.loadTexts:
    cambiumONVIFEntry.setStatus("current")
_CambiumONVIFIndex_Type = Integer32
_CambiumONVIFIndex_Object = MibTableColumn
cambiumONVIFIndex = _CambiumONVIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 1),
    _CambiumONVIFIndex_Type()
)
cambiumONVIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFIndex.setStatus("current")


class _CambiumONVIFMAC_Type(DisplayString):
    """Custom type cambiumONVIFMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CambiumONVIFMAC_Type.__name__ = "DisplayString"
_CambiumONVIFMAC_Object = MibTableColumn
cambiumONVIFMAC = _CambiumONVIFMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 2),
    _CambiumONVIFMAC_Type()
)
cambiumONVIFMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFMAC.setStatus("current")
_CambiumONVIFIP_Type = IpAddress
_CambiumONVIFIP_Object = MibTableColumn
cambiumONVIFIP = _CambiumONVIFIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 3),
    _CambiumONVIFIP_Type()
)
cambiumONVIFIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFIP.setStatus("current")


class _CambiumONVIFHardware_Type(DisplayString):
    """Custom type cambiumONVIFHardware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_CambiumONVIFHardware_Type.__name__ = "DisplayString"
_CambiumONVIFHardware_Object = MibTableColumn
cambiumONVIFHardware = _CambiumONVIFHardware_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 4),
    _CambiumONVIFHardware_Type()
)
cambiumONVIFHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFHardware.setStatus("current")


class _CambiumONVIFName_Type(DisplayString):
    """Custom type cambiumONVIFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_CambiumONVIFName_Type.__name__ = "DisplayString"
_CambiumONVIFName_Object = MibTableColumn
cambiumONVIFName = _CambiumONVIFName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 5),
    _CambiumONVIFName_Type()
)
cambiumONVIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFName.setStatus("current")


class _CambiumONVIFLocation_Type(DisplayString):
    """Custom type cambiumONVIFLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_CambiumONVIFLocation_Type.__name__ = "DisplayString"
_CambiumONVIFLocation_Object = MibTableColumn
cambiumONVIFLocation = _CambiumONVIFLocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 6),
    _CambiumONVIFLocation_Type()
)
cambiumONVIFLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFLocation.setStatus("current")
_CambiumONVIFProbeTime_Type = Counter32
_CambiumONVIFProbeTime_Object = MibTableColumn
cambiumONVIFProbeTime = _CambiumONVIFProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 7),
    _CambiumONVIFProbeTime_Type()
)
cambiumONVIFProbeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFProbeTime.setStatus("current")


class _CambiumONVIFSTAMAC_Type(DisplayString):
    """Custom type cambiumONVIFSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CambiumONVIFSTAMAC_Type.__name__ = "DisplayString"
_CambiumONVIFSTAMAC_Object = MibTableColumn
cambiumONVIFSTAMAC = _CambiumONVIFSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 10, 1, 1, 8),
    _CambiumONVIFSTAMAC_Type()
)
cambiumONVIFSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumONVIFSTAMAC.setStatus("current")
_CambiumPmp80211SystemMonitoring_ObjectIdentity = ObjectIdentity
cambiumPmp80211SystemMonitoring = _CambiumPmp80211SystemMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2)
)
_CambiumPerformanceMonitoring_ObjectIdentity = ObjectIdentity
cambiumPerformanceMonitoring = _CambiumPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1)
)


class _CambiumStatsForceUpdate_Type(Integer32):
    """Custom type cambiumStatsForceUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumStatsForceUpdate_Type.__name__ = "Integer32"
_CambiumStatsForceUpdate_Object = MibScalar
cambiumStatsForceUpdate = _CambiumStatsForceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 1),
    _CambiumStatsForceUpdate_Type()
)
cambiumStatsForceUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStatsForceUpdate.setStatus("current")
_CambiumEthRXBytes_Type = Counter64
_CambiumEthRXBytes_Object = MibScalar
cambiumEthRXBytes = _CambiumEthRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 2),
    _CambiumEthRXBytes_Type()
)
cambiumEthRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXBytes.setStatus("current")
_CambiumEthRXPackets_Type = Counter64
_CambiumEthRXPackets_Object = MibScalar
cambiumEthRXPackets = _CambiumEthRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 3),
    _CambiumEthRXPackets_Type()
)
cambiumEthRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXPackets.setStatus("current")
_CambiumEthRXErrors_Type = Counter64
_CambiumEthRXErrors_Object = MibScalar
cambiumEthRXErrors = _CambiumEthRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 4),
    _CambiumEthRXErrors_Type()
)
cambiumEthRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXErrors.setStatus("current")
_CambiumEthRXDrops_Type = Counter64
_CambiumEthRXDrops_Object = MibScalar
cambiumEthRXDrops = _CambiumEthRXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 5),
    _CambiumEthRXDrops_Type()
)
cambiumEthRXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXDrops.setStatus("current")
_CambiumEthRXMulticast_Type = Counter64
_CambiumEthRXMulticast_Object = MibScalar
cambiumEthRXMulticast = _CambiumEthRXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 6),
    _CambiumEthRXMulticast_Type()
)
cambiumEthRXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXMulticast.setStatus("current")
_CambiumEthRXBroadcast_Type = Counter64
_CambiumEthRXBroadcast_Object = MibScalar
cambiumEthRXBroadcast = _CambiumEthRXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 7),
    _CambiumEthRXBroadcast_Type()
)
cambiumEthRXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXBroadcast.setStatus("current")
_CambiumEthTXBytes_Type = Counter64
_CambiumEthTXBytes_Object = MibScalar
cambiumEthTXBytes = _CambiumEthTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 8),
    _CambiumEthTXBytes_Type()
)
cambiumEthTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXBytes.setStatus("current")
_CambiumEthTXPackets_Type = Counter64
_CambiumEthTXPackets_Object = MibScalar
cambiumEthTXPackets = _CambiumEthTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 9),
    _CambiumEthTXPackets_Type()
)
cambiumEthTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXPackets.setStatus("current")
_CambiumEthTXErrors_Type = Counter64
_CambiumEthTXErrors_Object = MibScalar
cambiumEthTXErrors = _CambiumEthTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 10),
    _CambiumEthTXErrors_Type()
)
cambiumEthTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXErrors.setStatus("current")
_CambiumEthTXDrops_Type = Counter64
_CambiumEthTXDrops_Object = MibScalar
cambiumEthTXDrops = _CambiumEthTXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 11),
    _CambiumEthTXDrops_Type()
)
cambiumEthTXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXDrops.setStatus("current")
_CambiumEthTXMulticast_Type = Counter64
_CambiumEthTXMulticast_Object = MibScalar
cambiumEthTXMulticast = _CambiumEthTXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 12),
    _CambiumEthTXMulticast_Type()
)
cambiumEthTXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXMulticast.setStatus("current")
_CambiumEthTXBroadcast_Type = Counter64
_CambiumEthTXBroadcast_Object = MibScalar
cambiumEthTXBroadcast = _CambiumEthTXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 13),
    _CambiumEthTXBroadcast_Type()
)
cambiumEthTXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXBroadcast.setStatus("current")
_CambiumAthRXBytes_Type = Counter64
_CambiumAthRXBytes_Object = MibScalar
cambiumAthRXBytes = _CambiumAthRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 21),
    _CambiumAthRXBytes_Type()
)
cambiumAthRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXBytes.setStatus("obsolete")
_CambiumAthRXPackets_Type = Counter64
_CambiumAthRXPackets_Object = MibScalar
cambiumAthRXPackets = _CambiumAthRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 22),
    _CambiumAthRXPackets_Type()
)
cambiumAthRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXPackets.setStatus("obsolete")
_CambiumAthRXErrors_Type = Counter64
_CambiumAthRXErrors_Object = MibScalar
cambiumAthRXErrors = _CambiumAthRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 23),
    _CambiumAthRXErrors_Type()
)
cambiumAthRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXErrors.setStatus("obsolete")
_CambiumAthRXDrops_Type = Counter64
_CambiumAthRXDrops_Object = MibScalar
cambiumAthRXDrops = _CambiumAthRXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 24),
    _CambiumAthRXDrops_Type()
)
cambiumAthRXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXDrops.setStatus("obsolete")
_CambiumAthRXMulticast_Type = Counter64
_CambiumAthRXMulticast_Object = MibScalar
cambiumAthRXMulticast = _CambiumAthRXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 25),
    _CambiumAthRXMulticast_Type()
)
cambiumAthRXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXMulticast.setStatus("obsolete")
_CambiumAthRXBroadcast_Type = Counter64
_CambiumAthRXBroadcast_Object = MibScalar
cambiumAthRXBroadcast = _CambiumAthRXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 26),
    _CambiumAthRXBroadcast_Type()
)
cambiumAthRXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXBroadcast.setStatus("obsolete")
_CambiumAthTXBytes_Type = Counter64
_CambiumAthTXBytes_Object = MibScalar
cambiumAthTXBytes = _CambiumAthTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 27),
    _CambiumAthTXBytes_Type()
)
cambiumAthTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXBytes.setStatus("obsolete")
_CambiumAthTXPackets_Type = Counter64
_CambiumAthTXPackets_Object = MibScalar
cambiumAthTXPackets = _CambiumAthTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 28),
    _CambiumAthTXPackets_Type()
)
cambiumAthTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXPackets.setStatus("obsolete")
_CambiumAthTXErrors_Type = Counter64
_CambiumAthTXErrors_Object = MibScalar
cambiumAthTXErrors = _CambiumAthTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 29),
    _CambiumAthTXErrors_Type()
)
cambiumAthTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXErrors.setStatus("obsolete")
_CambiumAthTXDrops_Type = Counter64
_CambiumAthTXDrops_Object = MibScalar
cambiumAthTXDrops = _CambiumAthTXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 30),
    _CambiumAthTXDrops_Type()
)
cambiumAthTXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXDrops.setStatus("obsolete")
_CambiumAthTXMulticast_Type = Counter64
_CambiumAthTXMulticast_Object = MibScalar
cambiumAthTXMulticast = _CambiumAthTXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 31),
    _CambiumAthTXMulticast_Type()
)
cambiumAthTXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXMulticast.setStatus("obsolete")
_CambiumAthTXBroadcast_Type = Counter64
_CambiumAthTXBroadcast_Object = MibScalar
cambiumAthTXBroadcast = _CambiumAthTXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 32),
    _CambiumAthTXBroadcast_Type()
)
cambiumAthTXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXBroadcast.setStatus("obsolete")
_SysNetworkEntryAttempt_Type = Counter32
_SysNetworkEntryAttempt_Object = MibScalar
sysNetworkEntryAttempt = _SysNetworkEntryAttempt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 33),
    _SysNetworkEntryAttempt_Type()
)
sysNetworkEntryAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntryAttempt.setStatus("current")
_SysNetworkEntrySuccess_Type = Counter32
_SysNetworkEntrySuccess_Object = MibScalar
sysNetworkEntrySuccess = _SysNetworkEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 34),
    _SysNetworkEntrySuccess_Type()
)
sysNetworkEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntrySuccess.setStatus("current")
_SysNetworkEntryAuthenticationFailure_Type = Counter32
_SysNetworkEntryAuthenticationFailure_Object = MibScalar
sysNetworkEntryAuthenticationFailure = _SysNetworkEntryAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 35),
    _SysNetworkEntryAuthenticationFailure_Type()
)
sysNetworkEntryAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntryAuthenticationFailure.setStatus("current")
_SysDFSDetectedCount_Type = Counter32
_SysDFSDetectedCount_Object = MibScalar
sysDFSDetectedCount = _SysDFSDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 36),
    _SysDFSDetectedCount_Type()
)
sysDFSDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDFSDetectedCount.setStatus("current")
_UlWLanKbitCount_Type = Counter64
_UlWLanKbitCount_Object = MibScalar
ulWLanKbitCount = _UlWLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 37),
    _UlWLanKbitCount_Type()
)
ulWLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanKbitCount.setStatus("current")
_DlWLanKbitCount_Type = Counter64
_DlWLanKbitCount_Object = MibScalar
dlWLanKbitCount = _DlWLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 38),
    _DlWLanKbitCount_Type()
)
dlWLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanKbitCount.setStatus("current")
_UlWLanTotalPacketCount_Type = Counter64
_UlWLanTotalPacketCount_Object = MibScalar
ulWLanTotalPacketCount = _UlWLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 39),
    _UlWLanTotalPacketCount_Type()
)
ulWLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalPacketCount.setStatus("current")
_MuWLanKbitCount_Type = Counter64
_MuWLanKbitCount_Object = MibScalar
muWLanKbitCount = _MuWLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 40),
    _MuWLanKbitCount_Type()
)
muWLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muWLanKbitCount.setStatus("current")
_SysRebootCount_Type = Integer32
_SysRebootCount_Object = MibScalar
sysRebootCount = _SysRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 41),
    _SysRebootCount_Type()
)
sysRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRebootCount.setStatus("obsolete")
_DlWLanTotalPacketCount_Type = Counter64
_DlWLanTotalPacketCount_Object = MibScalar
dlWLanTotalPacketCount = _DlWLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 42),
    _DlWLanTotalPacketCount_Type()
)
dlWLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalPacketCount.setStatus("current")
_UlWLanMultiBroadcastKbitCount_Type = Counter64
_UlWLanMultiBroadcastKbitCount_Object = MibScalar
ulWLanMultiBroadcastKbitCount = _UlWLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 43),
    _UlWLanMultiBroadcastKbitCount_Type()
)
ulWLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMultiBroadcastKbitCount.setStatus("current")
_DlWLanMultiBroadcastKbitCount_Type = Counter64
_DlWLanMultiBroadcastKbitCount_Object = MibScalar
dlWLanMultiBroadcastKbitCount = _DlWLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 44),
    _DlWLanMultiBroadcastKbitCount_Type()
)
dlWLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMultiBroadcastKbitCount.setStatus("current")
_WLanSessionDroppedCount_Type = Counter32
_WLanSessionDroppedCount_Object = MibScalar
wLanSessionDroppedCount = _WLanSessionDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 45),
    _WLanSessionDroppedCount_Type()
)
wLanSessionDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSessionDroppedCount.setStatus("current")
_CambiumTDDStatsPerSTATable_Object = MibTable
cambiumTDDStatsPerSTATable = _CambiumTDDStatsPerSTATable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46)
)
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTATable.setStatus("current")
_CambiumTDDStatsPerSTAEntry_Object = MibTableRow
cambiumTDDStatsPerSTAEntry = _CambiumTDDStatsPerSTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1)
)
cambiumTDDStatsPerSTAEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumTDDStatsPerSTAIndex"),
)
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTAEntry.setStatus("current")


class _CambiumTDDStatsPerSTAIndex_Type(Integer32):
    """Custom type cambiumTDDStatsPerSTAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CambiumTDDStatsPerSTAIndex_Type.__name__ = "Integer32"
_CambiumTDDStatsPerSTAIndex_Object = MibTableColumn
cambiumTDDStatsPerSTAIndex = _CambiumTDDStatsPerSTAIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 1),
    _CambiumTDDStatsPerSTAIndex_Type()
)
cambiumTDDStatsPerSTAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTAIndex.setStatus("current")


class _CambiumTDDStatsListMAC_Type(DisplayString):
    """Custom type cambiumTDDStatsListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_CambiumTDDStatsListMAC_Type.__name__ = "DisplayString"
_CambiumTDDStatsListMAC_Object = MibTableColumn
cambiumTDDStatsListMAC = _CambiumTDDStatsListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 2),
    _CambiumTDDStatsListMAC_Type()
)
cambiumTDDStatsListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsListMAC.setStatus("current")
_UlWLanPerUserKbitCount_Type = Counter64
_UlWLanPerUserKbitCount_Object = MibTableColumn
ulWLanPerUserKbitCount = _UlWLanPerUserKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 3),
    _UlWLanPerUserKbitCount_Type()
)
ulWLanPerUserKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserKbitCount.setStatus("current")
_DlWLanPerUserKbitCount_Type = Counter64
_DlWLanPerUserKbitCount_Object = MibTableColumn
dlWLanPerUserKbitCount = _DlWLanPerUserKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 4),
    _DlWLanPerUserKbitCount_Type()
)
dlWLanPerUserKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserKbitCount.setStatus("current")
_UlWLanPerUserTotalPacketCount_Type = Counter64
_UlWLanPerUserTotalPacketCount_Object = MibTableColumn
ulWLanPerUserTotalPacketCount = _UlWLanPerUserTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 5),
    _UlWLanPerUserTotalPacketCount_Type()
)
ulWLanPerUserTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserTotalPacketCount.setStatus("current")
_DlWLanPerUserTotalPacketCount_Type = Counter64
_DlWLanPerUserTotalPacketCount_Object = MibTableColumn
dlWLanPerUserTotalPacketCount = _DlWLanPerUserTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 6),
    _DlWLanPerUserTotalPacketCount_Type()
)
dlWLanPerUserTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserTotalPacketCount.setStatus("current")
_UlWLanPerUserErrorDroppedPacketCount_Type = Counter64
_UlWLanPerUserErrorDroppedPacketCount_Object = MibTableColumn
ulWLanPerUserErrorDroppedPacketCount = _UlWLanPerUserErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 7),
    _UlWLanPerUserErrorDroppedPacketCount_Type()
)
ulWLanPerUserErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserErrorDroppedPacketCount.setStatus("current")
_DlWLanPerUserErrorDroppedPacketCount_Type = Counter64
_DlWLanPerUserErrorDroppedPacketCount_Object = MibTableColumn
dlWLanPerUserErrorDroppedPacketCount = _DlWLanPerUserErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 8),
    _DlWLanPerUserErrorDroppedPacketCount_Type()
)
dlWLanPerUserErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserErrorDroppedPacketCount.setStatus("current")
_DlWLanPerUserCapacityDroppedPacketCount_Type = Counter64
_DlWLanPerUserCapacityDroppedPacketCount_Object = MibTableColumn
dlWLanPerUserCapacityDroppedPacketCount = _DlWLanPerUserCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 9),
    _DlWLanPerUserCapacityDroppedPacketCount_Type()
)
dlWLanPerUserCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserCapacityDroppedPacketCount.setStatus("current")
_DlWLanPerUserRetransmitPacketCount_Type = Counter64
_DlWLanPerUserRetransmitPacketCount_Object = MibTableColumn
dlWLanPerUserRetransmitPacketCount = _DlWLanPerUserRetransmitPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 10),
    _DlWLanPerUserRetransmitPacketCount_Type()
)
dlWLanPerUserRetransmitPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserRetransmitPacketCount.setStatus("current")
_DlWLanPerUserTxPower_Type = Integer32
_DlWLanPerUserTxPower_Object = MibTableColumn
dlWLanPerUserTxPower = _DlWLanPerUserTxPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 11),
    _DlWLanPerUserTxPower_Type()
)
dlWLanPerUserTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserTxPower.setStatus("current")
_CambiumTDDStatsIP_Type = IpAddress
_CambiumTDDStatsIP_Object = MibTableColumn
cambiumTDDStatsIP = _CambiumTDDStatsIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 12),
    _CambiumTDDStatsIP_Type()
)
cambiumTDDStatsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsIP.setStatus("current")


class _CambiumTDDStatsDevName_Type(DisplayString):
    """Custom type cambiumTDDStatsDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_CambiumTDDStatsDevName_Type.__name__ = "DisplayString"
_CambiumTDDStatsDevName_Object = MibTableColumn
cambiumTDDStatsDevName = _CambiumTDDStatsDevName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 13),
    _CambiumTDDStatsDevName_Type()
)
cambiumTDDStatsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsDevName.setStatus("current")
_DlWLanPerUserRetransmitMsduCount_Type = Counter64
_DlWLanPerUserRetransmitMsduCount_Object = MibTableColumn
dlWLanPerUserRetransmitMsduCount = _DlWLanPerUserRetransmitMsduCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 14),
    _DlWLanPerUserRetransmitMsduCount_Type()
)
dlWLanPerUserRetransmitMsduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserRetransmitMsduCount.setStatus("current")
_UlWLanErrorDroppedPacketCount_Type = Counter64
_UlWLanErrorDroppedPacketCount_Object = MibScalar
ulWLanErrorDroppedPacketCount = _UlWLanErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 47),
    _UlWLanErrorDroppedPacketCount_Type()
)
ulWLanErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanErrorDroppedPacketCount.setStatus("current")
_DlWLanErrorDroppedPacketCount_Type = Counter64
_DlWLanErrorDroppedPacketCount_Object = MibScalar
dlWLanErrorDroppedPacketCount = _DlWLanErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 48),
    _DlWLanErrorDroppedPacketCount_Type()
)
dlWLanErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanErrorDroppedPacketCount.setStatus("current")
_UlWLanCapacityDroppedPacketCount_Type = Counter64
_UlWLanCapacityDroppedPacketCount_Object = MibScalar
ulWLanCapacityDroppedPacketCount = _UlWLanCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 49),
    _UlWLanCapacityDroppedPacketCount_Type()
)
ulWLanCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanCapacityDroppedPacketCount.setStatus("current")
_DlWLanCapacityDroppedPacketCount_Type = Counter64
_DlWLanCapacityDroppedPacketCount_Object = MibScalar
dlWLanCapacityDroppedPacketCount = _DlWLanCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 50),
    _DlWLanCapacityDroppedPacketCount_Type()
)
dlWLanCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanCapacityDroppedPacketCount.setStatus("current")
_UlWLanTotalAvailableFrameTimePerSecond_Type = Integer32
_UlWLanTotalAvailableFrameTimePerSecond_Object = MibScalar
ulWLanTotalAvailableFrameTimePerSecond = _UlWLanTotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 51),
    _UlWLanTotalAvailableFrameTimePerSecond_Type()
)
ulWLanTotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalAvailableFrameTimePerSecond.setStatus("current")
_DlWLanTotalAvailableFrameTimePerSecond_Type = Integer32
_DlWLanTotalAvailableFrameTimePerSecond_Object = MibScalar
dlWLanTotalAvailableFrameTimePerSecond = _DlWLanTotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 52),
    _DlWLanTotalAvailableFrameTimePerSecond_Type()
)
dlWLanTotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalAvailableFrameTimePerSecond.setStatus("current")
_UlWLanTotalUsedFrameTimePerSecond_Type = Integer32
_UlWLanTotalUsedFrameTimePerSecond_Object = MibScalar
ulWLanTotalUsedFrameTimePerSecond = _UlWLanTotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 53),
    _UlWLanTotalUsedFrameTimePerSecond_Type()
)
ulWLanTotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalUsedFrameTimePerSecond.setStatus("current")
_DlWLanTotalUsedFrameTimePerSecond_Type = Integer32
_DlWLanTotalUsedFrameTimePerSecond_Object = MibScalar
dlWLanTotalUsedFrameTimePerSecond = _DlWLanTotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 54),
    _DlWLanTotalUsedFrameTimePerSecond_Type()
)
dlWLanTotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalUsedFrameTimePerSecond.setStatus("current")
_UlWLanTotalOverheadFrameTimePerSecond_Type = Integer32
_UlWLanTotalOverheadFrameTimePerSecond_Object = MibScalar
ulWLanTotalOverheadFrameTimePerSecond = _UlWLanTotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 55),
    _UlWLanTotalOverheadFrameTimePerSecond_Type()
)
ulWLanTotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalOverheadFrameTimePerSecond.setStatus("current")
_DlWLanTotalOverheadFrameTimePerSecond_Type = Integer32
_DlWLanTotalOverheadFrameTimePerSecond_Object = MibScalar
dlWLanTotalOverheadFrameTimePerSecond = _DlWLanTotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 56),
    _DlWLanTotalOverheadFrameTimePerSecond_Type()
)
dlWLanTotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalOverheadFrameTimePerSecond.setStatus("current")
_CambiumMCSTable_Object = MibTable
cambiumMCSTable = _CambiumMCSTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57)
)
if mibBuilder.loadTexts:
    cambiumMCSTable.setStatus("obsolete")
_CambiumMCSEntry_Object = MibTableRow
cambiumMCSEntry = _CambiumMCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1)
)
cambiumMCSEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumMCSIndex"),
)
if mibBuilder.loadTexts:
    cambiumMCSEntry.setStatus("obsolete")


class _CambiumMCSIndex_Type(Integer32):
    """Custom type cambiumMCSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CambiumMCSIndex_Type.__name__ = "Integer32"
_CambiumMCSIndex_Object = MibTableColumn
cambiumMCSIndex = _CambiumMCSIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 1),
    _CambiumMCSIndex_Type()
)
cambiumMCSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMCSIndex.setStatus("obsolete")
_CambiumMCSNumber_Type = DisplayString
_CambiumMCSNumber_Object = MibTableColumn
cambiumMCSNumber = _CambiumMCSNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 2),
    _CambiumMCSNumber_Type()
)
cambiumMCSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMCSNumber.setStatus("obsolete")
_UlWLanMCSUsedFrameTimePerSecond_Type = Counter32
_UlWLanMCSUsedFrameTimePerSecond_Object = MibTableColumn
ulWLanMCSUsedFrameTimePerSecond = _UlWLanMCSUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 3),
    _UlWLanMCSUsedFrameTimePerSecond_Type()
)
ulWLanMCSUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCSUsedFrameTimePerSecond.setStatus("obsolete")
_DlWLanMCSUsedFrameTimePerSecond_Type = Counter32
_DlWLanMCSUsedFrameTimePerSecond_Object = MibTableColumn
dlWLanMCSUsedFrameTimePerSecond = _DlWLanMCSUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 4),
    _DlWLanMCSUsedFrameTimePerSecond_Type()
)
dlWLanMCSUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCSUsedFrameTimePerSecond.setStatus("obsolete")
_UlWLanRetransPacketCount_Type = Counter64
_UlWLanRetransPacketCount_Object = MibScalar
ulWLanRetransPacketCount = _UlWLanRetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 58),
    _UlWLanRetransPacketCount_Type()
)
ulWLanRetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanRetransPacketCount.setStatus("current")
_DlWLanRetransPacketCount_Type = Counter64
_DlWLanRetransPacketCount_Object = MibScalar
dlWLanRetransPacketCount = _DlWLanRetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 59),
    _DlWLanRetransPacketCount_Type()
)
dlWLanRetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanRetransPacketCount.setStatus("current")
_UlWLanBroadcastPacketCount_Type = Counter64
_UlWLanBroadcastPacketCount_Object = MibScalar
ulWLanBroadcastPacketCount = _UlWLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 60),
    _UlWLanBroadcastPacketCount_Type()
)
ulWLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanBroadcastPacketCount.setStatus("current")
_DlWLanBroadcastPacketCount_Type = Counter64
_DlWLanBroadcastPacketCount_Object = MibScalar
dlWLanBroadcastPacketCount = _DlWLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 61),
    _DlWLanBroadcastPacketCount_Type()
)
dlWLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanBroadcastPacketCount.setStatus("current")
_UlWLanMulticastPacketCount_Type = Counter64
_UlWLanMulticastPacketCount_Object = MibScalar
ulWLanMulticastPacketCount = _UlWLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 62),
    _UlWLanMulticastPacketCount_Type()
)
ulWLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMulticastPacketCount.setStatus("current")
_DlWLanMulticastPacketCount_Type = Counter64
_DlWLanMulticastPacketCount_Object = MibScalar
dlWLanMulticastPacketCount = _DlWLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 63),
    _DlWLanMulticastPacketCount_Type()
)
dlWLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMulticastPacketCount.setStatus("current")
_SysCPUUsage_Type = Counter32
_SysCPUUsage_Object = MibScalar
sysCPUUsage = _SysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 64),
    _SysCPUUsage_Type()
)
sysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUsage.setStatus("current")
_RxEtherLanKbitCount_Type = Counter64
_RxEtherLanKbitCount_Object = MibScalar
rxEtherLanKbitCount = _RxEtherLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 65),
    _RxEtherLanKbitCount_Type()
)
rxEtherLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanKbitCount.setStatus("current")
_RxEtherLanTotalPacketCount_Type = Counter64
_RxEtherLanTotalPacketCount_Object = MibScalar
rxEtherLanTotalPacketCount = _RxEtherLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 66),
    _RxEtherLanTotalPacketCount_Type()
)
rxEtherLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanTotalPacketCount.setStatus("current")
_RxEtherLanErrorPacketCount_Type = Counter64
_RxEtherLanErrorPacketCount_Object = MibScalar
rxEtherLanErrorPacketCount = _RxEtherLanErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 67),
    _RxEtherLanErrorPacketCount_Type()
)
rxEtherLanErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanErrorPacketCount.setStatus("current")
_RxEtherLanDroppedPacketCount_Type = Counter64
_RxEtherLanDroppedPacketCount_Object = MibScalar
rxEtherLanDroppedPacketCount = _RxEtherLanDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 68),
    _RxEtherLanDroppedPacketCount_Type()
)
rxEtherLanDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanDroppedPacketCount.setStatus("current")
_RxEtherLanMulticastPacketCount_Type = Counter64
_RxEtherLanMulticastPacketCount_Object = MibScalar
rxEtherLanMulticastPacketCount = _RxEtherLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 69),
    _RxEtherLanMulticastPacketCount_Type()
)
rxEtherLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanMulticastPacketCount.setStatus("current")
_RxEtherLanBroadcastPacketCount_Type = Counter64
_RxEtherLanBroadcastPacketCount_Object = MibScalar
rxEtherLanBroadcastPacketCount = _RxEtherLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 70),
    _RxEtherLanBroadcastPacketCount_Type()
)
rxEtherLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanBroadcastPacketCount.setStatus("current")
_RxEtherLanMultiBroadcastKbitCount_Type = Counter64
_RxEtherLanMultiBroadcastKbitCount_Object = MibScalar
rxEtherLanMultiBroadcastKbitCount = _RxEtherLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 71),
    _RxEtherLanMultiBroadcastKbitCount_Type()
)
rxEtherLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanMultiBroadcastKbitCount.setStatus("current")
_TxEtherLanKbitCount_Type = Counter64
_TxEtherLanKbitCount_Object = MibScalar
txEtherLanKbitCount = _TxEtherLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 72),
    _TxEtherLanKbitCount_Type()
)
txEtherLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanKbitCount.setStatus("current")
_TxEtherLanTotalPacketCount_Type = Counter64
_TxEtherLanTotalPacketCount_Object = MibScalar
txEtherLanTotalPacketCount = _TxEtherLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 73),
    _TxEtherLanTotalPacketCount_Type()
)
txEtherLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanTotalPacketCount.setStatus("current")
_TxEtherLanErrorPacketCount_Type = Counter64
_TxEtherLanErrorPacketCount_Object = MibScalar
txEtherLanErrorPacketCount = _TxEtherLanErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 74),
    _TxEtherLanErrorPacketCount_Type()
)
txEtherLanErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanErrorPacketCount.setStatus("current")
_TxEtherLanDroppedPacketCount_Type = Counter64
_TxEtherLanDroppedPacketCount_Object = MibScalar
txEtherLanDroppedPacketCount = _TxEtherLanDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 75),
    _TxEtherLanDroppedPacketCount_Type()
)
txEtherLanDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanDroppedPacketCount.setStatus("current")
_TxEtherLanMulticastPacketCount_Type = Counter64
_TxEtherLanMulticastPacketCount_Object = MibScalar
txEtherLanMulticastPacketCount = _TxEtherLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 76),
    _TxEtherLanMulticastPacketCount_Type()
)
txEtherLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanMulticastPacketCount.setStatus("current")
_TxEtherLanBroadcastPacketCount_Type = Counter64
_TxEtherLanBroadcastPacketCount_Object = MibScalar
txEtherLanBroadcastPacketCount = _TxEtherLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 77),
    _TxEtherLanBroadcastPacketCount_Type()
)
txEtherLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanBroadcastPacketCount.setStatus("current")
_TxEtherLanMultiBroadcastKbitCount_Type = Counter64
_TxEtherLanMultiBroadcastKbitCount_Object = MibScalar
txEtherLanMultiBroadcastKbitCount = _TxEtherLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 78),
    _TxEtherLanMultiBroadcastKbitCount_Type()
)
txEtherLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanMultiBroadcastKbitCount.setStatus("current")
_CambiumStatsResetTimer_Type = TimeTicks
_CambiumStatsResetTimer_Object = MibScalar
cambiumStatsResetTimer = _CambiumStatsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 79),
    _CambiumStatsResetTimer_Type()
)
cambiumStatsResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStatsResetTimer.setStatus("current")
_UlWLanMCS00Packets_Type = Counter64
_UlWLanMCS00Packets_Object = MibScalar
ulWLanMCS00Packets = _UlWLanMCS00Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 80),
    _UlWLanMCS00Packets_Type()
)
ulWLanMCS00Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS00Packets.setStatus("current")
_UlWLanMCS01Packets_Type = Counter64
_UlWLanMCS01Packets_Object = MibScalar
ulWLanMCS01Packets = _UlWLanMCS01Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 81),
    _UlWLanMCS01Packets_Type()
)
ulWLanMCS01Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS01Packets.setStatus("current")
_UlWLanMCS02Packets_Type = Counter64
_UlWLanMCS02Packets_Object = MibScalar
ulWLanMCS02Packets = _UlWLanMCS02Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 82),
    _UlWLanMCS02Packets_Type()
)
ulWLanMCS02Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS02Packets.setStatus("current")
_UlWLanMCS03Packets_Type = Counter64
_UlWLanMCS03Packets_Object = MibScalar
ulWLanMCS03Packets = _UlWLanMCS03Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 83),
    _UlWLanMCS03Packets_Type()
)
ulWLanMCS03Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS03Packets.setStatus("current")
_UlWLanMCS04Packets_Type = Counter64
_UlWLanMCS04Packets_Object = MibScalar
ulWLanMCS04Packets = _UlWLanMCS04Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 84),
    _UlWLanMCS04Packets_Type()
)
ulWLanMCS04Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS04Packets.setStatus("current")
_UlWLanMCS05Packets_Type = Counter64
_UlWLanMCS05Packets_Object = MibScalar
ulWLanMCS05Packets = _UlWLanMCS05Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 85),
    _UlWLanMCS05Packets_Type()
)
ulWLanMCS05Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS05Packets.setStatus("current")
_UlWLanMCS06Packets_Type = Counter64
_UlWLanMCS06Packets_Object = MibScalar
ulWLanMCS06Packets = _UlWLanMCS06Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 86),
    _UlWLanMCS06Packets_Type()
)
ulWLanMCS06Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS06Packets.setStatus("current")
_UlWLanMCS07Packets_Type = Counter64
_UlWLanMCS07Packets_Object = MibScalar
ulWLanMCS07Packets = _UlWLanMCS07Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 87),
    _UlWLanMCS07Packets_Type()
)
ulWLanMCS07Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS07Packets.setStatus("current")
_UlWLanMCS08Packets_Type = Counter64
_UlWLanMCS08Packets_Object = MibScalar
ulWLanMCS08Packets = _UlWLanMCS08Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 88),
    _UlWLanMCS08Packets_Type()
)
ulWLanMCS08Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS08Packets.setStatus("current")
_UlWLanMCS09Packets_Type = Counter64
_UlWLanMCS09Packets_Object = MibScalar
ulWLanMCS09Packets = _UlWLanMCS09Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 89),
    _UlWLanMCS09Packets_Type()
)
ulWLanMCS09Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS09Packets.setStatus("current")
_UlWLanMCS10Packets_Type = Counter64
_UlWLanMCS10Packets_Object = MibScalar
ulWLanMCS10Packets = _UlWLanMCS10Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 90),
    _UlWLanMCS10Packets_Type()
)
ulWLanMCS10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS10Packets.setStatus("current")
_UlWLanMCS11Packets_Type = Counter64
_UlWLanMCS11Packets_Object = MibScalar
ulWLanMCS11Packets = _UlWLanMCS11Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 91),
    _UlWLanMCS11Packets_Type()
)
ulWLanMCS11Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS11Packets.setStatus("current")
_UlWLanMCS12Packets_Type = Counter64
_UlWLanMCS12Packets_Object = MibScalar
ulWLanMCS12Packets = _UlWLanMCS12Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 92),
    _UlWLanMCS12Packets_Type()
)
ulWLanMCS12Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS12Packets.setStatus("current")
_UlWLanMCS13Packets_Type = Counter64
_UlWLanMCS13Packets_Object = MibScalar
ulWLanMCS13Packets = _UlWLanMCS13Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 93),
    _UlWLanMCS13Packets_Type()
)
ulWLanMCS13Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS13Packets.setStatus("current")
_UlWLanMCS14Packets_Type = Counter64
_UlWLanMCS14Packets_Object = MibScalar
ulWLanMCS14Packets = _UlWLanMCS14Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 94),
    _UlWLanMCS14Packets_Type()
)
ulWLanMCS14Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS14Packets.setStatus("current")
_UlWLanMCS15Packets_Type = Counter64
_UlWLanMCS15Packets_Object = MibScalar
ulWLanMCS15Packets = _UlWLanMCS15Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 95),
    _UlWLanMCS15Packets_Type()
)
ulWLanMCS15Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS15Packets.setStatus("current")
_DlWLanMCS00Packets_Type = Counter64
_DlWLanMCS00Packets_Object = MibScalar
dlWLanMCS00Packets = _DlWLanMCS00Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 96),
    _DlWLanMCS00Packets_Type()
)
dlWLanMCS00Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS00Packets.setStatus("current")
_DlWLanMCS01Packets_Type = Counter64
_DlWLanMCS01Packets_Object = MibScalar
dlWLanMCS01Packets = _DlWLanMCS01Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 97),
    _DlWLanMCS01Packets_Type()
)
dlWLanMCS01Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS01Packets.setStatus("current")
_DlWLanMCS02Packets_Type = Counter64
_DlWLanMCS02Packets_Object = MibScalar
dlWLanMCS02Packets = _DlWLanMCS02Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 98),
    _DlWLanMCS02Packets_Type()
)
dlWLanMCS02Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS02Packets.setStatus("current")
_DlWLanMCS03Packets_Type = Counter64
_DlWLanMCS03Packets_Object = MibScalar
dlWLanMCS03Packets = _DlWLanMCS03Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 99),
    _DlWLanMCS03Packets_Type()
)
dlWLanMCS03Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS03Packets.setStatus("current")
_DlWLanMCS04Packets_Type = Counter64
_DlWLanMCS04Packets_Object = MibScalar
dlWLanMCS04Packets = _DlWLanMCS04Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 100),
    _DlWLanMCS04Packets_Type()
)
dlWLanMCS04Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS04Packets.setStatus("current")
_DlWLanMCS05Packets_Type = Counter64
_DlWLanMCS05Packets_Object = MibScalar
dlWLanMCS05Packets = _DlWLanMCS05Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 101),
    _DlWLanMCS05Packets_Type()
)
dlWLanMCS05Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS05Packets.setStatus("current")
_DlWLanMCS06Packets_Type = Counter64
_DlWLanMCS06Packets_Object = MibScalar
dlWLanMCS06Packets = _DlWLanMCS06Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 102),
    _DlWLanMCS06Packets_Type()
)
dlWLanMCS06Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS06Packets.setStatus("current")
_DlWLanMCS07Packets_Type = Counter64
_DlWLanMCS07Packets_Object = MibScalar
dlWLanMCS07Packets = _DlWLanMCS07Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 103),
    _DlWLanMCS07Packets_Type()
)
dlWLanMCS07Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS07Packets.setStatus("current")
_DlWLanMCS08Packets_Type = Counter64
_DlWLanMCS08Packets_Object = MibScalar
dlWLanMCS08Packets = _DlWLanMCS08Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 104),
    _DlWLanMCS08Packets_Type()
)
dlWLanMCS08Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS08Packets.setStatus("current")
_DlWLanMCS09Packets_Type = Counter64
_DlWLanMCS09Packets_Object = MibScalar
dlWLanMCS09Packets = _DlWLanMCS09Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 105),
    _DlWLanMCS09Packets_Type()
)
dlWLanMCS09Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS09Packets.setStatus("current")
_DlWLanMCS10Packets_Type = Counter64
_DlWLanMCS10Packets_Object = MibScalar
dlWLanMCS10Packets = _DlWLanMCS10Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 106),
    _DlWLanMCS10Packets_Type()
)
dlWLanMCS10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS10Packets.setStatus("current")
_DlWLanMCS11Packets_Type = Counter64
_DlWLanMCS11Packets_Object = MibScalar
dlWLanMCS11Packets = _DlWLanMCS11Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 107),
    _DlWLanMCS11Packets_Type()
)
dlWLanMCS11Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS11Packets.setStatus("current")
_DlWLanMCS12Packets_Type = Counter64
_DlWLanMCS12Packets_Object = MibScalar
dlWLanMCS12Packets = _DlWLanMCS12Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 108),
    _DlWLanMCS12Packets_Type()
)
dlWLanMCS12Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS12Packets.setStatus("current")
_DlWLanMCS13Packets_Type = Counter64
_DlWLanMCS13Packets_Object = MibScalar
dlWLanMCS13Packets = _DlWLanMCS13Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 109),
    _DlWLanMCS13Packets_Type()
)
dlWLanMCS13Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS13Packets.setStatus("current")
_DlWLanMCS14Packets_Type = Counter64
_DlWLanMCS14Packets_Object = MibScalar
dlWLanMCS14Packets = _DlWLanMCS14Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 110),
    _DlWLanMCS14Packets_Type()
)
dlWLanMCS14Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS14Packets.setStatus("current")
_DlWLanMCS15Packets_Type = Counter64
_DlWLanMCS15Packets_Object = MibScalar
dlWLanMCS15Packets = _DlWLanMCS15Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 111),
    _DlWLanMCS15Packets_Type()
)
dlWLanMCS15Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS15Packets.setStatus("current")
_UlWLanTotalAvailableFrameTimePercentage_Type = Integer32
_UlWLanTotalAvailableFrameTimePercentage_Object = MibScalar
ulWLanTotalAvailableFrameTimePercentage = _UlWLanTotalAvailableFrameTimePercentage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 112),
    _UlWLanTotalAvailableFrameTimePercentage_Type()
)
ulWLanTotalAvailableFrameTimePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalAvailableFrameTimePercentage.setStatus("current")
_DlWLanTotalAvailableFrameTimePercentage_Type = Integer32
_DlWLanTotalAvailableFrameTimePercentage_Object = MibScalar
dlWLanTotalAvailableFrameTimePercentage = _DlWLanTotalAvailableFrameTimePercentage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 113),
    _DlWLanTotalAvailableFrameTimePercentage_Type()
)
dlWLanTotalAvailableFrameTimePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalAvailableFrameTimePercentage.setStatus("current")
_WlanMCSPackets_ObjectIdentity = ObjectIdentity
wlanMCSPackets = _WlanMCSPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114)
)
_DlWLanMCS00UnicastPackets_Type = Counter64
_DlWLanMCS00UnicastPackets_Object = MibScalar
dlWLanMCS00UnicastPackets = _DlWLanMCS00UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 1),
    _DlWLanMCS00UnicastPackets_Type()
)
dlWLanMCS00UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS00UnicastPackets.setStatus("current")
_DlWLanMCS01UnicastPackets_Type = Counter64
_DlWLanMCS01UnicastPackets_Object = MibScalar
dlWLanMCS01UnicastPackets = _DlWLanMCS01UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 2),
    _DlWLanMCS01UnicastPackets_Type()
)
dlWLanMCS01UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS01UnicastPackets.setStatus("current")
_DlWLanMCS02UnicastPackets_Type = Counter64
_DlWLanMCS02UnicastPackets_Object = MibScalar
dlWLanMCS02UnicastPackets = _DlWLanMCS02UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 3),
    _DlWLanMCS02UnicastPackets_Type()
)
dlWLanMCS02UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS02UnicastPackets.setStatus("current")
_DlWLanMCS03UnicastPackets_Type = Counter64
_DlWLanMCS03UnicastPackets_Object = MibScalar
dlWLanMCS03UnicastPackets = _DlWLanMCS03UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 4),
    _DlWLanMCS03UnicastPackets_Type()
)
dlWLanMCS03UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS03UnicastPackets.setStatus("current")
_DlWLanMCS04UnicastPackets_Type = Counter64
_DlWLanMCS04UnicastPackets_Object = MibScalar
dlWLanMCS04UnicastPackets = _DlWLanMCS04UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 5),
    _DlWLanMCS04UnicastPackets_Type()
)
dlWLanMCS04UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS04UnicastPackets.setStatus("current")
_DlWLanMCS05UnicastPackets_Type = Counter64
_DlWLanMCS05UnicastPackets_Object = MibScalar
dlWLanMCS05UnicastPackets = _DlWLanMCS05UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 6),
    _DlWLanMCS05UnicastPackets_Type()
)
dlWLanMCS05UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS05UnicastPackets.setStatus("current")
_DlWLanMCS06UnicastPackets_Type = Counter64
_DlWLanMCS06UnicastPackets_Object = MibScalar
dlWLanMCS06UnicastPackets = _DlWLanMCS06UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 7),
    _DlWLanMCS06UnicastPackets_Type()
)
dlWLanMCS06UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS06UnicastPackets.setStatus("current")
_DlWLanMCS07UnicastPackets_Type = Counter64
_DlWLanMCS07UnicastPackets_Object = MibScalar
dlWLanMCS07UnicastPackets = _DlWLanMCS07UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 8),
    _DlWLanMCS07UnicastPackets_Type()
)
dlWLanMCS07UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS07UnicastPackets.setStatus("current")
_DlWLanMCS08UnicastPackets_Type = Counter64
_DlWLanMCS08UnicastPackets_Object = MibScalar
dlWLanMCS08UnicastPackets = _DlWLanMCS08UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 9),
    _DlWLanMCS08UnicastPackets_Type()
)
dlWLanMCS08UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS08UnicastPackets.setStatus("current")
_DlWLanMCS09UnicastPackets_Type = Counter64
_DlWLanMCS09UnicastPackets_Object = MibScalar
dlWLanMCS09UnicastPackets = _DlWLanMCS09UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 10),
    _DlWLanMCS09UnicastPackets_Type()
)
dlWLanMCS09UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS09UnicastPackets.setStatus("current")
_DlWLanMCS10UnicastPackets_Type = Counter64
_DlWLanMCS10UnicastPackets_Object = MibScalar
dlWLanMCS10UnicastPackets = _DlWLanMCS10UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 11),
    _DlWLanMCS10UnicastPackets_Type()
)
dlWLanMCS10UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS10UnicastPackets.setStatus("current")
_DlWLanMCS11UnicastPackets_Type = Counter64
_DlWLanMCS11UnicastPackets_Object = MibScalar
dlWLanMCS11UnicastPackets = _DlWLanMCS11UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 12),
    _DlWLanMCS11UnicastPackets_Type()
)
dlWLanMCS11UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS11UnicastPackets.setStatus("current")
_DlWLanMCS12UnicastPackets_Type = Counter64
_DlWLanMCS12UnicastPackets_Object = MibScalar
dlWLanMCS12UnicastPackets = _DlWLanMCS12UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 13),
    _DlWLanMCS12UnicastPackets_Type()
)
dlWLanMCS12UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS12UnicastPackets.setStatus("current")
_DlWLanMCS13UnicastPackets_Type = Counter64
_DlWLanMCS13UnicastPackets_Object = MibScalar
dlWLanMCS13UnicastPackets = _DlWLanMCS13UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 14),
    _DlWLanMCS13UnicastPackets_Type()
)
dlWLanMCS13UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS13UnicastPackets.setStatus("current")
_DlWLanMCS14UnicastPackets_Type = Counter64
_DlWLanMCS14UnicastPackets_Object = MibScalar
dlWLanMCS14UnicastPackets = _DlWLanMCS14UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 15),
    _DlWLanMCS14UnicastPackets_Type()
)
dlWLanMCS14UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS14UnicastPackets.setStatus("current")
_DlWLanMCS15UnicastPackets_Type = Counter64
_DlWLanMCS15UnicastPackets_Object = MibScalar
dlWLanMCS15UnicastPackets = _DlWLanMCS15UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 16),
    _DlWLanMCS15UnicastPackets_Type()
)
dlWLanMCS15UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS15UnicastPackets.setStatus("current")
_UlWLanMCS00UnicastPackets_Type = Counter64
_UlWLanMCS00UnicastPackets_Object = MibScalar
ulWLanMCS00UnicastPackets = _UlWLanMCS00UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 17),
    _UlWLanMCS00UnicastPackets_Type()
)
ulWLanMCS00UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS00UnicastPackets.setStatus("current")
_UlWLanMCS01UnicastPackets_Type = Counter64
_UlWLanMCS01UnicastPackets_Object = MibScalar
ulWLanMCS01UnicastPackets = _UlWLanMCS01UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 18),
    _UlWLanMCS01UnicastPackets_Type()
)
ulWLanMCS01UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS01UnicastPackets.setStatus("current")
_UlWLanMCS02UnicastPackets_Type = Counter64
_UlWLanMCS02UnicastPackets_Object = MibScalar
ulWLanMCS02UnicastPackets = _UlWLanMCS02UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 19),
    _UlWLanMCS02UnicastPackets_Type()
)
ulWLanMCS02UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS02UnicastPackets.setStatus("current")
_UlWLanMCS03UnicastPackets_Type = Counter64
_UlWLanMCS03UnicastPackets_Object = MibScalar
ulWLanMCS03UnicastPackets = _UlWLanMCS03UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 20),
    _UlWLanMCS03UnicastPackets_Type()
)
ulWLanMCS03UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS03UnicastPackets.setStatus("current")
_UlWLanMCS04UnicastPackets_Type = Counter64
_UlWLanMCS04UnicastPackets_Object = MibScalar
ulWLanMCS04UnicastPackets = _UlWLanMCS04UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 21),
    _UlWLanMCS04UnicastPackets_Type()
)
ulWLanMCS04UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS04UnicastPackets.setStatus("current")
_UlWLanMCS05UnicastPackets_Type = Counter64
_UlWLanMCS05UnicastPackets_Object = MibScalar
ulWLanMCS05UnicastPackets = _UlWLanMCS05UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 22),
    _UlWLanMCS05UnicastPackets_Type()
)
ulWLanMCS05UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS05UnicastPackets.setStatus("current")
_UlWLanMCS06UnicastPackets_Type = Counter64
_UlWLanMCS06UnicastPackets_Object = MibScalar
ulWLanMCS06UnicastPackets = _UlWLanMCS06UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 23),
    _UlWLanMCS06UnicastPackets_Type()
)
ulWLanMCS06UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS06UnicastPackets.setStatus("current")
_UlWLanMCS07UnicastPackets_Type = Counter64
_UlWLanMCS07UnicastPackets_Object = MibScalar
ulWLanMCS07UnicastPackets = _UlWLanMCS07UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 24),
    _UlWLanMCS07UnicastPackets_Type()
)
ulWLanMCS07UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS07UnicastPackets.setStatus("current")
_UlWLanMCS08UnicastPackets_Type = Counter64
_UlWLanMCS08UnicastPackets_Object = MibScalar
ulWLanMCS08UnicastPackets = _UlWLanMCS08UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 25),
    _UlWLanMCS08UnicastPackets_Type()
)
ulWLanMCS08UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS08UnicastPackets.setStatus("current")
_UlWLanMCS09UnicastPackets_Type = Counter64
_UlWLanMCS09UnicastPackets_Object = MibScalar
ulWLanMCS09UnicastPackets = _UlWLanMCS09UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 26),
    _UlWLanMCS09UnicastPackets_Type()
)
ulWLanMCS09UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS09UnicastPackets.setStatus("current")
_UlWLanMCS10UnicastPackets_Type = Counter64
_UlWLanMCS10UnicastPackets_Object = MibScalar
ulWLanMCS10UnicastPackets = _UlWLanMCS10UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 27),
    _UlWLanMCS10UnicastPackets_Type()
)
ulWLanMCS10UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS10UnicastPackets.setStatus("current")
_UlWLanMCS11UnicastPackets_Type = Counter64
_UlWLanMCS11UnicastPackets_Object = MibScalar
ulWLanMCS11UnicastPackets = _UlWLanMCS11UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 28),
    _UlWLanMCS11UnicastPackets_Type()
)
ulWLanMCS11UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS11UnicastPackets.setStatus("current")
_UlWLanMCS12UnicastPackets_Type = Counter64
_UlWLanMCS12UnicastPackets_Object = MibScalar
ulWLanMCS12UnicastPackets = _UlWLanMCS12UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 29),
    _UlWLanMCS12UnicastPackets_Type()
)
ulWLanMCS12UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS12UnicastPackets.setStatus("current")
_UlWLanMCS13UnicastPackets_Type = Counter64
_UlWLanMCS13UnicastPackets_Object = MibScalar
ulWLanMCS13UnicastPackets = _UlWLanMCS13UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 30),
    _UlWLanMCS13UnicastPackets_Type()
)
ulWLanMCS13UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS13UnicastPackets.setStatus("current")
_UlWLanMCS14UnicastPackets_Type = Counter64
_UlWLanMCS14UnicastPackets_Object = MibScalar
ulWLanMCS14UnicastPackets = _UlWLanMCS14UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 31),
    _UlWLanMCS14UnicastPackets_Type()
)
ulWLanMCS14UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS14UnicastPackets.setStatus("current")
_UlWLanMCS15UnicastPackets_Type = Counter64
_UlWLanMCS15UnicastPackets_Object = MibScalar
ulWLanMCS15UnicastPackets = _UlWLanMCS15UnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 32),
    _UlWLanMCS15UnicastPackets_Type()
)
ulWLanMCS15UnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS15UnicastPackets.setStatus("current")
_DlWLanMCS00MulticastPackets_Type = Counter64
_DlWLanMCS00MulticastPackets_Object = MibScalar
dlWLanMCS00MulticastPackets = _DlWLanMCS00MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 33),
    _DlWLanMCS00MulticastPackets_Type()
)
dlWLanMCS00MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS00MulticastPackets.setStatus("current")
_DlWLanMCS01MulticastPackets_Type = Counter64
_DlWLanMCS01MulticastPackets_Object = MibScalar
dlWLanMCS01MulticastPackets = _DlWLanMCS01MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 34),
    _DlWLanMCS01MulticastPackets_Type()
)
dlWLanMCS01MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS01MulticastPackets.setStatus("current")
_DlWLanMCS02MulticastPackets_Type = Counter64
_DlWLanMCS02MulticastPackets_Object = MibScalar
dlWLanMCS02MulticastPackets = _DlWLanMCS02MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 35),
    _DlWLanMCS02MulticastPackets_Type()
)
dlWLanMCS02MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS02MulticastPackets.setStatus("current")
_DlWLanMCS03MulticastPackets_Type = Counter64
_DlWLanMCS03MulticastPackets_Object = MibScalar
dlWLanMCS03MulticastPackets = _DlWLanMCS03MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 36),
    _DlWLanMCS03MulticastPackets_Type()
)
dlWLanMCS03MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS03MulticastPackets.setStatus("current")
_DlWLanMCS04MulticastPackets_Type = Counter64
_DlWLanMCS04MulticastPackets_Object = MibScalar
dlWLanMCS04MulticastPackets = _DlWLanMCS04MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 37),
    _DlWLanMCS04MulticastPackets_Type()
)
dlWLanMCS04MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS04MulticastPackets.setStatus("current")
_DlWLanMCS05MulticastPackets_Type = Counter64
_DlWLanMCS05MulticastPackets_Object = MibScalar
dlWLanMCS05MulticastPackets = _DlWLanMCS05MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 38),
    _DlWLanMCS05MulticastPackets_Type()
)
dlWLanMCS05MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS05MulticastPackets.setStatus("current")
_DlWLanMCS06MulticastPackets_Type = Counter64
_DlWLanMCS06MulticastPackets_Object = MibScalar
dlWLanMCS06MulticastPackets = _DlWLanMCS06MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 39),
    _DlWLanMCS06MulticastPackets_Type()
)
dlWLanMCS06MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS06MulticastPackets.setStatus("current")
_DlWLanMCS07MulticastPackets_Type = Counter64
_DlWLanMCS07MulticastPackets_Object = MibScalar
dlWLanMCS07MulticastPackets = _DlWLanMCS07MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 40),
    _DlWLanMCS07MulticastPackets_Type()
)
dlWLanMCS07MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS07MulticastPackets.setStatus("current")
_DlWLanMCS08MulticastPackets_Type = Counter64
_DlWLanMCS08MulticastPackets_Object = MibScalar
dlWLanMCS08MulticastPackets = _DlWLanMCS08MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 41),
    _DlWLanMCS08MulticastPackets_Type()
)
dlWLanMCS08MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS08MulticastPackets.setStatus("current")
_DlWLanMCS09MulticastPackets_Type = Counter64
_DlWLanMCS09MulticastPackets_Object = MibScalar
dlWLanMCS09MulticastPackets = _DlWLanMCS09MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 42),
    _DlWLanMCS09MulticastPackets_Type()
)
dlWLanMCS09MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS09MulticastPackets.setStatus("current")
_DlWLanMCS10MulticastPackets_Type = Counter64
_DlWLanMCS10MulticastPackets_Object = MibScalar
dlWLanMCS10MulticastPackets = _DlWLanMCS10MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 43),
    _DlWLanMCS10MulticastPackets_Type()
)
dlWLanMCS10MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS10MulticastPackets.setStatus("current")
_DlWLanMCS11MulticastPackets_Type = Counter64
_DlWLanMCS11MulticastPackets_Object = MibScalar
dlWLanMCS11MulticastPackets = _DlWLanMCS11MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 44),
    _DlWLanMCS11MulticastPackets_Type()
)
dlWLanMCS11MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS11MulticastPackets.setStatus("current")
_DlWLanMCS12MulticastPackets_Type = Counter64
_DlWLanMCS12MulticastPackets_Object = MibScalar
dlWLanMCS12MulticastPackets = _DlWLanMCS12MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 45),
    _DlWLanMCS12MulticastPackets_Type()
)
dlWLanMCS12MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS12MulticastPackets.setStatus("current")
_DlWLanMCS13MulticastPackets_Type = Counter64
_DlWLanMCS13MulticastPackets_Object = MibScalar
dlWLanMCS13MulticastPackets = _DlWLanMCS13MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 46),
    _DlWLanMCS13MulticastPackets_Type()
)
dlWLanMCS13MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS13MulticastPackets.setStatus("current")
_DlWLanMCS14MulticastPackets_Type = Counter64
_DlWLanMCS14MulticastPackets_Object = MibScalar
dlWLanMCS14MulticastPackets = _DlWLanMCS14MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 47),
    _DlWLanMCS14MulticastPackets_Type()
)
dlWLanMCS14MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS14MulticastPackets.setStatus("current")
_DlWLanMCS15MulticastPackets_Type = Counter64
_DlWLanMCS15MulticastPackets_Object = MibScalar
dlWLanMCS15MulticastPackets = _DlWLanMCS15MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 48),
    _DlWLanMCS15MulticastPackets_Type()
)
dlWLanMCS15MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS15MulticastPackets.setStatus("current")
_UlWLanMCS00MulticastPackets_Type = Counter64
_UlWLanMCS00MulticastPackets_Object = MibScalar
ulWLanMCS00MulticastPackets = _UlWLanMCS00MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 49),
    _UlWLanMCS00MulticastPackets_Type()
)
ulWLanMCS00MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS00MulticastPackets.setStatus("current")
_UlWLanMCS01MulticastPackets_Type = Counter64
_UlWLanMCS01MulticastPackets_Object = MibScalar
ulWLanMCS01MulticastPackets = _UlWLanMCS01MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 50),
    _UlWLanMCS01MulticastPackets_Type()
)
ulWLanMCS01MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS01MulticastPackets.setStatus("current")
_UlWLanMCS02MulticastPackets_Type = Counter64
_UlWLanMCS02MulticastPackets_Object = MibScalar
ulWLanMCS02MulticastPackets = _UlWLanMCS02MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 51),
    _UlWLanMCS02MulticastPackets_Type()
)
ulWLanMCS02MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS02MulticastPackets.setStatus("current")
_UlWLanMCS03MulticastPackets_Type = Counter64
_UlWLanMCS03MulticastPackets_Object = MibScalar
ulWLanMCS03MulticastPackets = _UlWLanMCS03MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 52),
    _UlWLanMCS03MulticastPackets_Type()
)
ulWLanMCS03MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS03MulticastPackets.setStatus("current")
_UlWLanMCS04MulticastPackets_Type = Counter64
_UlWLanMCS04MulticastPackets_Object = MibScalar
ulWLanMCS04MulticastPackets = _UlWLanMCS04MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 53),
    _UlWLanMCS04MulticastPackets_Type()
)
ulWLanMCS04MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS04MulticastPackets.setStatus("current")
_UlWLanMCS05MulticastPackets_Type = Counter64
_UlWLanMCS05MulticastPackets_Object = MibScalar
ulWLanMCS05MulticastPackets = _UlWLanMCS05MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 54),
    _UlWLanMCS05MulticastPackets_Type()
)
ulWLanMCS05MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS05MulticastPackets.setStatus("current")
_UlWLanMCS06MulticastPackets_Type = Counter64
_UlWLanMCS06MulticastPackets_Object = MibScalar
ulWLanMCS06MulticastPackets = _UlWLanMCS06MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 55),
    _UlWLanMCS06MulticastPackets_Type()
)
ulWLanMCS06MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS06MulticastPackets.setStatus("current")
_UlWLanMCS07MulticastPackets_Type = Counter64
_UlWLanMCS07MulticastPackets_Object = MibScalar
ulWLanMCS07MulticastPackets = _UlWLanMCS07MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 56),
    _UlWLanMCS07MulticastPackets_Type()
)
ulWLanMCS07MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS07MulticastPackets.setStatus("current")
_UlWLanMCS08MulticastPackets_Type = Counter64
_UlWLanMCS08MulticastPackets_Object = MibScalar
ulWLanMCS08MulticastPackets = _UlWLanMCS08MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 57),
    _UlWLanMCS08MulticastPackets_Type()
)
ulWLanMCS08MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS08MulticastPackets.setStatus("current")
_UlWLanMCS09MulticastPackets_Type = Counter64
_UlWLanMCS09MulticastPackets_Object = MibScalar
ulWLanMCS09MulticastPackets = _UlWLanMCS09MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 58),
    _UlWLanMCS09MulticastPackets_Type()
)
ulWLanMCS09MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS09MulticastPackets.setStatus("current")
_UlWLanMCS10MulticastPackets_Type = Counter64
_UlWLanMCS10MulticastPackets_Object = MibScalar
ulWLanMCS10MulticastPackets = _UlWLanMCS10MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 59),
    _UlWLanMCS10MulticastPackets_Type()
)
ulWLanMCS10MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS10MulticastPackets.setStatus("current")
_UlWLanMCS11MulticastPackets_Type = Counter64
_UlWLanMCS11MulticastPackets_Object = MibScalar
ulWLanMCS11MulticastPackets = _UlWLanMCS11MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 60),
    _UlWLanMCS11MulticastPackets_Type()
)
ulWLanMCS11MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS11MulticastPackets.setStatus("current")
_UlWLanMCS12MulticastPackets_Type = Counter64
_UlWLanMCS12MulticastPackets_Object = MibScalar
ulWLanMCS12MulticastPackets = _UlWLanMCS12MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 61),
    _UlWLanMCS12MulticastPackets_Type()
)
ulWLanMCS12MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS12MulticastPackets.setStatus("current")
_UlWLanMCS13MulticastPackets_Type = Counter64
_UlWLanMCS13MulticastPackets_Object = MibScalar
ulWLanMCS13MulticastPackets = _UlWLanMCS13MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 62),
    _UlWLanMCS13MulticastPackets_Type()
)
ulWLanMCS13MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS13MulticastPackets.setStatus("current")
_UlWLanMCS14MulticastPackets_Type = Counter64
_UlWLanMCS14MulticastPackets_Object = MibScalar
ulWLanMCS14MulticastPackets = _UlWLanMCS14MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 63),
    _UlWLanMCS14MulticastPackets_Type()
)
ulWLanMCS14MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS14MulticastPackets.setStatus("current")
_UlWLanMCS15MulticastPackets_Type = Counter64
_UlWLanMCS15MulticastPackets_Object = MibScalar
ulWLanMCS15MulticastPackets = _UlWLanMCS15MulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 114, 64),
    _UlWLanMCS15MulticastPackets_Type()
)
ulWLanMCS15MulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS15MulticastPackets.setStatus("current")
_EPMP2000MapMissCounter_Type = Counter32
_EPMP2000MapMissCounter_Object = MibScalar
ePMP2000MapMissCounter = _EPMP2000MapMissCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 115),
    _EPMP2000MapMissCounter_Type()
)
ePMP2000MapMissCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000MapMissCounter.setStatus("current")
_EPMP2000PatternSkipCounter_Type = Counter32
_EPMP2000PatternSkipCounter_Object = MibScalar
ePMP2000PatternSkipCounter = _EPMP2000PatternSkipCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 116),
    _EPMP2000PatternSkipCounter_Type()
)
ePMP2000PatternSkipCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000PatternSkipCounter.setStatus("current")
_EPMP2000ErrorsSmartAntennaInterface_Type = Counter32
_EPMP2000ErrorsSmartAntennaInterface_Object = MibScalar
ePMP2000ErrorsSmartAntennaInterface = _EPMP2000ErrorsSmartAntennaInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 117),
    _EPMP2000ErrorsSmartAntennaInterface_Type()
)
ePMP2000ErrorsSmartAntennaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePMP2000ErrorsSmartAntennaInterface.setStatus("current")
_ClassificationVoiceQueuePutPacketCount_Type = Counter32
_ClassificationVoiceQueuePutPacketCount_Object = MibScalar
classificationVoiceQueuePutPacketCount = _ClassificationVoiceQueuePutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 118),
    _ClassificationVoiceQueuePutPacketCount_Type()
)
classificationVoiceQueuePutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationVoiceQueuePutPacketCount.setStatus("current")
_ClassificationVoiceQueueGetPacketCount_Type = Counter32
_ClassificationVoiceQueueGetPacketCount_Object = MibScalar
classificationVoiceQueueGetPacketCount = _ClassificationVoiceQueueGetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 119),
    _ClassificationVoiceQueueGetPacketCount_Type()
)
classificationVoiceQueueGetPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationVoiceQueueGetPacketCount.setStatus("current")
_ClassificationVoiceQueueDropPacketCount_Type = Counter32
_ClassificationVoiceQueueDropPacketCount_Object = MibScalar
classificationVoiceQueueDropPacketCount = _ClassificationVoiceQueueDropPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 120),
    _ClassificationVoiceQueueDropPacketCount_Type()
)
classificationVoiceQueueDropPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationVoiceQueueDropPacketCount.setStatus("current")
_ClassificationHighQueuePutPacketCount_Type = Counter32
_ClassificationHighQueuePutPacketCount_Object = MibScalar
classificationHighQueuePutPacketCount = _ClassificationHighQueuePutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 121),
    _ClassificationHighQueuePutPacketCount_Type()
)
classificationHighQueuePutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationHighQueuePutPacketCount.setStatus("current")
_ClassificationHighQueueGetPacketCount_Type = Counter32
_ClassificationHighQueueGetPacketCount_Object = MibScalar
classificationHighQueueGetPacketCount = _ClassificationHighQueueGetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 122),
    _ClassificationHighQueueGetPacketCount_Type()
)
classificationHighQueueGetPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationHighQueueGetPacketCount.setStatus("current")
_ClassificationHighQueueDropPacketCount_Type = Counter32
_ClassificationHighQueueDropPacketCount_Object = MibScalar
classificationHighQueueDropPacketCount = _ClassificationHighQueueDropPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 123),
    _ClassificationHighQueueDropPacketCount_Type()
)
classificationHighQueueDropPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationHighQueueDropPacketCount.setStatus("current")
_ClassificationLowQueuePutPacketCount_Type = Counter32
_ClassificationLowQueuePutPacketCount_Object = MibScalar
classificationLowQueuePutPacketCount = _ClassificationLowQueuePutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 124),
    _ClassificationLowQueuePutPacketCount_Type()
)
classificationLowQueuePutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationLowQueuePutPacketCount.setStatus("current")
_ClassificationLowQueueGetPacketCount_Type = Counter32
_ClassificationLowQueueGetPacketCount_Object = MibScalar
classificationLowQueueGetPacketCount = _ClassificationLowQueueGetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 125),
    _ClassificationLowQueueGetPacketCount_Type()
)
classificationLowQueueGetPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationLowQueueGetPacketCount.setStatus("current")
_ClassificationLowQueueDropPacketCount_Type = Counter32
_ClassificationLowQueueDropPacketCount_Object = MibScalar
classificationLowQueueDropPacketCount = _ClassificationLowQueueDropPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 126),
    _ClassificationLowQueueDropPacketCount_Type()
)
classificationLowQueueDropPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationLowQueueDropPacketCount.setStatus("current")
_ClassificationTotalQueuePutPacketCount_Type = Counter32
_ClassificationTotalQueuePutPacketCount_Object = MibScalar
classificationTotalQueuePutPacketCount = _ClassificationTotalQueuePutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 127),
    _ClassificationTotalQueuePutPacketCount_Type()
)
classificationTotalQueuePutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationTotalQueuePutPacketCount.setStatus("current")
_ClassificationTotalQueueGetPacketCount_Type = Counter32
_ClassificationTotalQueueGetPacketCount_Object = MibScalar
classificationTotalQueueGetPacketCount = _ClassificationTotalQueueGetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 128),
    _ClassificationTotalQueueGetPacketCount_Type()
)
classificationTotalQueueGetPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationTotalQueueGetPacketCount.setStatus("current")
_ClassificationTotalQueueDropPacketCount_Type = Counter32
_ClassificationTotalQueueDropPacketCount_Object = MibScalar
classificationTotalQueueDropPacketCount = _ClassificationTotalQueueDropPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 129),
    _ClassificationTotalQueueDropPacketCount_Type()
)
classificationTotalQueueDropPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classificationTotalQueueDropPacketCount.setStatus("current")
_UlWLanVHTMCS0SSPackets_Type = Counter64
_UlWLanVHTMCS0SSPackets_Object = MibScalar
ulWLanVHTMCS0SSPackets = _UlWLanVHTMCS0SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 130),
    _UlWLanVHTMCS0SSPackets_Type()
)
ulWLanVHTMCS0SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS0SSPackets.setStatus("current")
_UlWLanVHTMCS1SSPackets_Type = Counter64
_UlWLanVHTMCS1SSPackets_Object = MibScalar
ulWLanVHTMCS1SSPackets = _UlWLanVHTMCS1SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 131),
    _UlWLanVHTMCS1SSPackets_Type()
)
ulWLanVHTMCS1SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS1SSPackets.setStatus("current")
_UlWLanVHTMCS2SSPackets_Type = Counter64
_UlWLanVHTMCS2SSPackets_Object = MibScalar
ulWLanVHTMCS2SSPackets = _UlWLanVHTMCS2SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 132),
    _UlWLanVHTMCS2SSPackets_Type()
)
ulWLanVHTMCS2SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS2SSPackets.setStatus("current")
_UlWLanVHTMCS3SSPackets_Type = Counter64
_UlWLanVHTMCS3SSPackets_Object = MibScalar
ulWLanVHTMCS3SSPackets = _UlWLanVHTMCS3SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 133),
    _UlWLanVHTMCS3SSPackets_Type()
)
ulWLanVHTMCS3SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS3SSPackets.setStatus("current")
_UlWLanVHTMCS4SSPackets_Type = Counter64
_UlWLanVHTMCS4SSPackets_Object = MibScalar
ulWLanVHTMCS4SSPackets = _UlWLanVHTMCS4SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 134),
    _UlWLanVHTMCS4SSPackets_Type()
)
ulWLanVHTMCS4SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS4SSPackets.setStatus("current")
_UlWLanVHTMCS5SSPackets_Type = Counter64
_UlWLanVHTMCS5SSPackets_Object = MibScalar
ulWLanVHTMCS5SSPackets = _UlWLanVHTMCS5SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 135),
    _UlWLanVHTMCS5SSPackets_Type()
)
ulWLanVHTMCS5SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS5SSPackets.setStatus("current")
_UlWLanVHTMCS6SSPackets_Type = Counter64
_UlWLanVHTMCS6SSPackets_Object = MibScalar
ulWLanVHTMCS6SSPackets = _UlWLanVHTMCS6SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 136),
    _UlWLanVHTMCS6SSPackets_Type()
)
ulWLanVHTMCS6SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS6SSPackets.setStatus("current")
_UlWLanVHTMCS7SSPackets_Type = Counter64
_UlWLanVHTMCS7SSPackets_Object = MibScalar
ulWLanVHTMCS7SSPackets = _UlWLanVHTMCS7SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 137),
    _UlWLanVHTMCS7SSPackets_Type()
)
ulWLanVHTMCS7SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS7SSPackets.setStatus("current")
_UlWLanVHTMCS8SSPackets_Type = Counter64
_UlWLanVHTMCS8SSPackets_Object = MibScalar
ulWLanVHTMCS8SSPackets = _UlWLanVHTMCS8SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 138),
    _UlWLanVHTMCS8SSPackets_Type()
)
ulWLanVHTMCS8SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS8SSPackets.setStatus("current")
_UlWLanVHTMCS9SSPackets_Type = Counter64
_UlWLanVHTMCS9SSPackets_Object = MibScalar
ulWLanVHTMCS9SSPackets = _UlWLanVHTMCS9SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 139),
    _UlWLanVHTMCS9SSPackets_Type()
)
ulWLanVHTMCS9SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS9SSPackets.setStatus("current")
_UlWLanVHTMCS0DSPackets_Type = Counter64
_UlWLanVHTMCS0DSPackets_Object = MibScalar
ulWLanVHTMCS0DSPackets = _UlWLanVHTMCS0DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 140),
    _UlWLanVHTMCS0DSPackets_Type()
)
ulWLanVHTMCS0DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS0DSPackets.setStatus("current")
_UlWLanVHTMCS1DSPackets_Type = Counter64
_UlWLanVHTMCS1DSPackets_Object = MibScalar
ulWLanVHTMCS1DSPackets = _UlWLanVHTMCS1DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 141),
    _UlWLanVHTMCS1DSPackets_Type()
)
ulWLanVHTMCS1DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS1DSPackets.setStatus("current")
_UlWLanVHTMCS2DSPackets_Type = Counter64
_UlWLanVHTMCS2DSPackets_Object = MibScalar
ulWLanVHTMCS2DSPackets = _UlWLanVHTMCS2DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 142),
    _UlWLanVHTMCS2DSPackets_Type()
)
ulWLanVHTMCS2DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS2DSPackets.setStatus("current")
_UlWLanVHTMCS3DSPackets_Type = Counter64
_UlWLanVHTMCS3DSPackets_Object = MibScalar
ulWLanVHTMCS3DSPackets = _UlWLanVHTMCS3DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 143),
    _UlWLanVHTMCS3DSPackets_Type()
)
ulWLanVHTMCS3DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS3DSPackets.setStatus("current")
_UlWLanVHTMCS4DSPackets_Type = Counter64
_UlWLanVHTMCS4DSPackets_Object = MibScalar
ulWLanVHTMCS4DSPackets = _UlWLanVHTMCS4DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 144),
    _UlWLanVHTMCS4DSPackets_Type()
)
ulWLanVHTMCS4DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS4DSPackets.setStatus("current")
_UlWLanVHTMCS5DSPackets_Type = Counter64
_UlWLanVHTMCS5DSPackets_Object = MibScalar
ulWLanVHTMCS5DSPackets = _UlWLanVHTMCS5DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 145),
    _UlWLanVHTMCS5DSPackets_Type()
)
ulWLanVHTMCS5DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS5DSPackets.setStatus("current")
_UlWLanVHTMCS6DSPackets_Type = Counter64
_UlWLanVHTMCS6DSPackets_Object = MibScalar
ulWLanVHTMCS6DSPackets = _UlWLanVHTMCS6DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 146),
    _UlWLanVHTMCS6DSPackets_Type()
)
ulWLanVHTMCS6DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS6DSPackets.setStatus("current")
_UlWLanVHTMCS7DSPackets_Type = Counter64
_UlWLanVHTMCS7DSPackets_Object = MibScalar
ulWLanVHTMCS7DSPackets = _UlWLanVHTMCS7DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 147),
    _UlWLanVHTMCS7DSPackets_Type()
)
ulWLanVHTMCS7DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS7DSPackets.setStatus("current")
_UlWLanVHTMCS8DSPackets_Type = Counter64
_UlWLanVHTMCS8DSPackets_Object = MibScalar
ulWLanVHTMCS8DSPackets = _UlWLanVHTMCS8DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 148),
    _UlWLanVHTMCS8DSPackets_Type()
)
ulWLanVHTMCS8DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS8DSPackets.setStatus("current")
_UlWLanVHTMCS9DSPackets_Type = Counter64
_UlWLanVHTMCS9DSPackets_Object = MibScalar
ulWLanVHTMCS9DSPackets = _UlWLanVHTMCS9DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 149),
    _UlWLanVHTMCS9DSPackets_Type()
)
ulWLanVHTMCS9DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanVHTMCS9DSPackets.setStatus("current")
_DlWLanVHTMCS0SSPackets_Type = Counter64
_DlWLanVHTMCS0SSPackets_Object = MibScalar
dlWLanVHTMCS0SSPackets = _DlWLanVHTMCS0SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 150),
    _DlWLanVHTMCS0SSPackets_Type()
)
dlWLanVHTMCS0SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS0SSPackets.setStatus("current")
_DlWLanVHTMCS1SSPackets_Type = Counter64
_DlWLanVHTMCS1SSPackets_Object = MibScalar
dlWLanVHTMCS1SSPackets = _DlWLanVHTMCS1SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 151),
    _DlWLanVHTMCS1SSPackets_Type()
)
dlWLanVHTMCS1SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS1SSPackets.setStatus("current")
_DlWLanVHTMCS2SSPackets_Type = Counter64
_DlWLanVHTMCS2SSPackets_Object = MibScalar
dlWLanVHTMCS2SSPackets = _DlWLanVHTMCS2SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 152),
    _DlWLanVHTMCS2SSPackets_Type()
)
dlWLanVHTMCS2SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS2SSPackets.setStatus("current")
_DlWLanVHTMCS3SSPackets_Type = Counter64
_DlWLanVHTMCS3SSPackets_Object = MibScalar
dlWLanVHTMCS3SSPackets = _DlWLanVHTMCS3SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 153),
    _DlWLanVHTMCS3SSPackets_Type()
)
dlWLanVHTMCS3SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS3SSPackets.setStatus("current")
_DlWLanVHTMCS4SSPackets_Type = Counter64
_DlWLanVHTMCS4SSPackets_Object = MibScalar
dlWLanVHTMCS4SSPackets = _DlWLanVHTMCS4SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 154),
    _DlWLanVHTMCS4SSPackets_Type()
)
dlWLanVHTMCS4SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS4SSPackets.setStatus("current")
_DlWLanVHTMCS5SSPackets_Type = Counter64
_DlWLanVHTMCS5SSPackets_Object = MibScalar
dlWLanVHTMCS5SSPackets = _DlWLanVHTMCS5SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 155),
    _DlWLanVHTMCS5SSPackets_Type()
)
dlWLanVHTMCS5SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS5SSPackets.setStatus("current")
_DlWLanVHTMCS6SSPackets_Type = Counter64
_DlWLanVHTMCS6SSPackets_Object = MibScalar
dlWLanVHTMCS6SSPackets = _DlWLanVHTMCS6SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 156),
    _DlWLanVHTMCS6SSPackets_Type()
)
dlWLanVHTMCS6SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS6SSPackets.setStatus("current")
_DlWLanVHTMCS7SSPackets_Type = Counter64
_DlWLanVHTMCS7SSPackets_Object = MibScalar
dlWLanVHTMCS7SSPackets = _DlWLanVHTMCS7SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 157),
    _DlWLanVHTMCS7SSPackets_Type()
)
dlWLanVHTMCS7SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS7SSPackets.setStatus("current")
_DlWLanVHTMCS8SSPackets_Type = Counter64
_DlWLanVHTMCS8SSPackets_Object = MibScalar
dlWLanVHTMCS8SSPackets = _DlWLanVHTMCS8SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 158),
    _DlWLanVHTMCS8SSPackets_Type()
)
dlWLanVHTMCS8SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS8SSPackets.setStatus("current")
_DlWLanVHTMCS9SSPackets_Type = Counter64
_DlWLanVHTMCS9SSPackets_Object = MibScalar
dlWLanVHTMCS9SSPackets = _DlWLanVHTMCS9SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 159),
    _DlWLanVHTMCS9SSPackets_Type()
)
dlWLanVHTMCS9SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS9SSPackets.setStatus("current")
_DlWLanVHTMCS0DSPackets_Type = Counter64
_DlWLanVHTMCS0DSPackets_Object = MibScalar
dlWLanVHTMCS0DSPackets = _DlWLanVHTMCS0DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 160),
    _DlWLanVHTMCS0DSPackets_Type()
)
dlWLanVHTMCS0DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS0DSPackets.setStatus("current")
_DlWLanVHTMCS1DSPackets_Type = Counter64
_DlWLanVHTMCS1DSPackets_Object = MibScalar
dlWLanVHTMCS1DSPackets = _DlWLanVHTMCS1DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 161),
    _DlWLanVHTMCS1DSPackets_Type()
)
dlWLanVHTMCS1DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS1DSPackets.setStatus("current")
_DlWLanVHTMCS2DSPackets_Type = Counter64
_DlWLanVHTMCS2DSPackets_Object = MibScalar
dlWLanVHTMCS2DSPackets = _DlWLanVHTMCS2DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 162),
    _DlWLanVHTMCS2DSPackets_Type()
)
dlWLanVHTMCS2DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS2DSPackets.setStatus("current")
_DlWLanVHTMCS3DSPackets_Type = Counter64
_DlWLanVHTMCS3DSPackets_Object = MibScalar
dlWLanVHTMCS3DSPackets = _DlWLanVHTMCS3DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 163),
    _DlWLanVHTMCS3DSPackets_Type()
)
dlWLanVHTMCS3DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS3DSPackets.setStatus("current")
_DlWLanVHTMCS4DSPackets_Type = Counter64
_DlWLanVHTMCS4DSPackets_Object = MibScalar
dlWLanVHTMCS4DSPackets = _DlWLanVHTMCS4DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 164),
    _DlWLanVHTMCS4DSPackets_Type()
)
dlWLanVHTMCS4DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS4DSPackets.setStatus("current")
_DlWLanVHTMCS5DSPackets_Type = Counter64
_DlWLanVHTMCS5DSPackets_Object = MibScalar
dlWLanVHTMCS5DSPackets = _DlWLanVHTMCS5DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 165),
    _DlWLanVHTMCS5DSPackets_Type()
)
dlWLanVHTMCS5DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS5DSPackets.setStatus("current")
_DlWLanVHTMCS6DSPackets_Type = Counter64
_DlWLanVHTMCS6DSPackets_Object = MibScalar
dlWLanVHTMCS6DSPackets = _DlWLanVHTMCS6DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 166),
    _DlWLanVHTMCS6DSPackets_Type()
)
dlWLanVHTMCS6DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS6DSPackets.setStatus("current")
_DlWLanVHTMCS7DSPackets_Type = Counter64
_DlWLanVHTMCS7DSPackets_Object = MibScalar
dlWLanVHTMCS7DSPackets = _DlWLanVHTMCS7DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 167),
    _DlWLanVHTMCS7DSPackets_Type()
)
dlWLanVHTMCS7DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS7DSPackets.setStatus("current")
_DlWLanVHTMCS8DSPackets_Type = Counter64
_DlWLanVHTMCS8DSPackets_Object = MibScalar
dlWLanVHTMCS8DSPackets = _DlWLanVHTMCS8DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 168),
    _DlWLanVHTMCS8DSPackets_Type()
)
dlWLanVHTMCS8DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS8DSPackets.setStatus("current")
_DlWLanVHTMCS9DSPackets_Type = Counter64
_DlWLanVHTMCS9DSPackets_Object = MibScalar
dlWLanVHTMCS9DSPackets = _DlWLanVHTMCS9DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 169),
    _DlWLanVHTMCS9DSPackets_Type()
)
dlWLanVHTMCS9DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanVHTMCS9DSPackets.setStatus("current")
_WLanSNRDeviation00Cnt_Type = Counter64
_WLanSNRDeviation00Cnt_Object = MibScalar
wLanSNRDeviation00Cnt = _WLanSNRDeviation00Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 170),
    _WLanSNRDeviation00Cnt_Type()
)
wLanSNRDeviation00Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation00Cnt.setStatus("current")
_WLanSNRDeviation01Cnt_Type = Counter64
_WLanSNRDeviation01Cnt_Object = MibScalar
wLanSNRDeviation01Cnt = _WLanSNRDeviation01Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 171),
    _WLanSNRDeviation01Cnt_Type()
)
wLanSNRDeviation01Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation01Cnt.setStatus("current")
_WLanSNRDeviation02Cnt_Type = Counter64
_WLanSNRDeviation02Cnt_Object = MibScalar
wLanSNRDeviation02Cnt = _WLanSNRDeviation02Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 172),
    _WLanSNRDeviation02Cnt_Type()
)
wLanSNRDeviation02Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation02Cnt.setStatus("current")
_WLanSNRDeviation03Cnt_Type = Counter64
_WLanSNRDeviation03Cnt_Object = MibScalar
wLanSNRDeviation03Cnt = _WLanSNRDeviation03Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 173),
    _WLanSNRDeviation03Cnt_Type()
)
wLanSNRDeviation03Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation03Cnt.setStatus("current")
_WLanSNRDeviation04Cnt_Type = Counter64
_WLanSNRDeviation04Cnt_Object = MibScalar
wLanSNRDeviation04Cnt = _WLanSNRDeviation04Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 174),
    _WLanSNRDeviation04Cnt_Type()
)
wLanSNRDeviation04Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation04Cnt.setStatus("current")
_WLanSNRDeviation05Cnt_Type = Counter64
_WLanSNRDeviation05Cnt_Object = MibScalar
wLanSNRDeviation05Cnt = _WLanSNRDeviation05Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 175),
    _WLanSNRDeviation05Cnt_Type()
)
wLanSNRDeviation05Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation05Cnt.setStatus("current")
_WLanSNRDeviation06Cnt_Type = Counter64
_WLanSNRDeviation06Cnt_Object = MibScalar
wLanSNRDeviation06Cnt = _WLanSNRDeviation06Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 176),
    _WLanSNRDeviation06Cnt_Type()
)
wLanSNRDeviation06Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation06Cnt.setStatus("current")
_WLanSNRDeviation07Cnt_Type = Counter64
_WLanSNRDeviation07Cnt_Object = MibScalar
wLanSNRDeviation07Cnt = _WLanSNRDeviation07Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 177),
    _WLanSNRDeviation07Cnt_Type()
)
wLanSNRDeviation07Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation07Cnt.setStatus("current")
_WLanSNRDeviation08Cnt_Type = Counter64
_WLanSNRDeviation08Cnt_Object = MibScalar
wLanSNRDeviation08Cnt = _WLanSNRDeviation08Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 178),
    _WLanSNRDeviation08Cnt_Type()
)
wLanSNRDeviation08Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation08Cnt.setStatus("current")
_WLanSNRDeviation09Cnt_Type = Counter64
_WLanSNRDeviation09Cnt_Object = MibScalar
wLanSNRDeviation09Cnt = _WLanSNRDeviation09Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 179),
    _WLanSNRDeviation09Cnt_Type()
)
wLanSNRDeviation09Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation09Cnt.setStatus("current")
_WLanSNRDeviation10Cnt_Type = Counter64
_WLanSNRDeviation10Cnt_Object = MibScalar
wLanSNRDeviation10Cnt = _WLanSNRDeviation10Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 180),
    _WLanSNRDeviation10Cnt_Type()
)
wLanSNRDeviation10Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation10Cnt.setStatus("current")
_WLanSNRDeviation11Cnt_Type = Counter64
_WLanSNRDeviation11Cnt_Object = MibScalar
wLanSNRDeviation11Cnt = _WLanSNRDeviation11Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 181),
    _WLanSNRDeviation11Cnt_Type()
)
wLanSNRDeviation11Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation11Cnt.setStatus("current")
_WLanSNRDeviation12Cnt_Type = Counter64
_WLanSNRDeviation12Cnt_Object = MibScalar
wLanSNRDeviation12Cnt = _WLanSNRDeviation12Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 182),
    _WLanSNRDeviation12Cnt_Type()
)
wLanSNRDeviation12Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation12Cnt.setStatus("current")
_WLanSNRDeviation13Cnt_Type = Counter64
_WLanSNRDeviation13Cnt_Object = MibScalar
wLanSNRDeviation13Cnt = _WLanSNRDeviation13Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 183),
    _WLanSNRDeviation13Cnt_Type()
)
wLanSNRDeviation13Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation13Cnt.setStatus("current")
_WLanSNRDeviation14Cnt_Type = Counter64
_WLanSNRDeviation14Cnt_Object = MibScalar
wLanSNRDeviation14Cnt = _WLanSNRDeviation14Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 184),
    _WLanSNRDeviation14Cnt_Type()
)
wLanSNRDeviation14Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation14Cnt.setStatus("current")
_WLanSNRDeviation15Cnt_Type = Counter64
_WLanSNRDeviation15Cnt_Object = MibScalar
wLanSNRDeviation15Cnt = _WLanSNRDeviation15Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 185),
    _WLanSNRDeviation15Cnt_Type()
)
wLanSNRDeviation15Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation15Cnt.setStatus("current")
_WLanSNRDeviation16Cnt_Type = Counter64
_WLanSNRDeviation16Cnt_Object = MibScalar
wLanSNRDeviation16Cnt = _WLanSNRDeviation16Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 186),
    _WLanSNRDeviation16Cnt_Type()
)
wLanSNRDeviation16Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation16Cnt.setStatus("current")
_WLanSNRDeviation17Cnt_Type = Counter64
_WLanSNRDeviation17Cnt_Object = MibScalar
wLanSNRDeviation17Cnt = _WLanSNRDeviation17Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 187),
    _WLanSNRDeviation17Cnt_Type()
)
wLanSNRDeviation17Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation17Cnt.setStatus("current")
_WLanSNRDeviation18Cnt_Type = Counter64
_WLanSNRDeviation18Cnt_Object = MibScalar
wLanSNRDeviation18Cnt = _WLanSNRDeviation18Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 188),
    _WLanSNRDeviation18Cnt_Type()
)
wLanSNRDeviation18Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation18Cnt.setStatus("current")
_WLanSNRDeviation19Cnt_Type = Counter64
_WLanSNRDeviation19Cnt_Object = MibScalar
wLanSNRDeviation19Cnt = _WLanSNRDeviation19Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 189),
    _WLanSNRDeviation19Cnt_Type()
)
wLanSNRDeviation19Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSNRDeviation19Cnt.setStatus("current")
_WlanHEMCSPackets_ObjectIdentity = ObjectIdentity
wlanHEMCSPackets = _WlanHEMCSPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190)
)
_DlWlanHEMCSPackets_ObjectIdentity = ObjectIdentity
dlWlanHEMCSPackets = _DlWlanHEMCSPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1)
)
_DlWLanHEMCS0S1Packets_Type = Counter64
_DlWLanHEMCS0S1Packets_Object = MibScalar
dlWLanHEMCS0S1Packets = _DlWLanHEMCS0S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 1),
    _DlWLanHEMCS0S1Packets_Type()
)
dlWLanHEMCS0S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S1Packets.setStatus("current")
_DlWLanHEMCS1S1Packets_Type = Counter64
_DlWLanHEMCS1S1Packets_Object = MibScalar
dlWLanHEMCS1S1Packets = _DlWLanHEMCS1S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 2),
    _DlWLanHEMCS1S1Packets_Type()
)
dlWLanHEMCS1S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S1Packets.setStatus("current")
_DlWLanHEMCS2S1Packets_Type = Counter64
_DlWLanHEMCS2S1Packets_Object = MibScalar
dlWLanHEMCS2S1Packets = _DlWLanHEMCS2S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 3),
    _DlWLanHEMCS2S1Packets_Type()
)
dlWLanHEMCS2S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S1Packets.setStatus("current")
_DlWLanHEMCS3S1Packets_Type = Counter64
_DlWLanHEMCS3S1Packets_Object = MibScalar
dlWLanHEMCS3S1Packets = _DlWLanHEMCS3S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 4),
    _DlWLanHEMCS3S1Packets_Type()
)
dlWLanHEMCS3S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S1Packets.setStatus("current")
_DlWLanHEMCS4S1Packets_Type = Counter64
_DlWLanHEMCS4S1Packets_Object = MibScalar
dlWLanHEMCS4S1Packets = _DlWLanHEMCS4S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 5),
    _DlWLanHEMCS4S1Packets_Type()
)
dlWLanHEMCS4S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S1Packets.setStatus("current")
_DlWLanHEMCS5S1Packets_Type = Counter64
_DlWLanHEMCS5S1Packets_Object = MibScalar
dlWLanHEMCS5S1Packets = _DlWLanHEMCS5S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 6),
    _DlWLanHEMCS5S1Packets_Type()
)
dlWLanHEMCS5S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S1Packets.setStatus("current")
_DlWLanHEMCS6S1Packets_Type = Counter64
_DlWLanHEMCS6S1Packets_Object = MibScalar
dlWLanHEMCS6S1Packets = _DlWLanHEMCS6S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 7),
    _DlWLanHEMCS6S1Packets_Type()
)
dlWLanHEMCS6S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S1Packets.setStatus("current")
_DlWLanHEMCS7S1Packets_Type = Counter64
_DlWLanHEMCS7S1Packets_Object = MibScalar
dlWLanHEMCS7S1Packets = _DlWLanHEMCS7S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 8),
    _DlWLanHEMCS7S1Packets_Type()
)
dlWLanHEMCS7S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S1Packets.setStatus("current")
_DlWLanHEMCS8S1Packets_Type = Counter64
_DlWLanHEMCS8S1Packets_Object = MibScalar
dlWLanHEMCS8S1Packets = _DlWLanHEMCS8S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 9),
    _DlWLanHEMCS8S1Packets_Type()
)
dlWLanHEMCS8S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S1Packets.setStatus("current")
_DlWLanHEMCS9S1Packets_Type = Counter64
_DlWLanHEMCS9S1Packets_Object = MibScalar
dlWLanHEMCS9S1Packets = _DlWLanHEMCS9S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 10),
    _DlWLanHEMCS9S1Packets_Type()
)
dlWLanHEMCS9S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S1Packets.setStatus("current")
_DlWLanHEMCS10S1Packets_Type = Counter64
_DlWLanHEMCS10S1Packets_Object = MibScalar
dlWLanHEMCS10S1Packets = _DlWLanHEMCS10S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 11),
    _DlWLanHEMCS10S1Packets_Type()
)
dlWLanHEMCS10S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S1Packets.setStatus("current")
_DlWLanHEMCS11S1Packets_Type = Counter64
_DlWLanHEMCS11S1Packets_Object = MibScalar
dlWLanHEMCS11S1Packets = _DlWLanHEMCS11S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 12),
    _DlWLanHEMCS11S1Packets_Type()
)
dlWLanHEMCS11S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S1Packets.setStatus("current")
_DlWLanHEMCS0S2Packets_Type = Counter64
_DlWLanHEMCS0S2Packets_Object = MibScalar
dlWLanHEMCS0S2Packets = _DlWLanHEMCS0S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 13),
    _DlWLanHEMCS0S2Packets_Type()
)
dlWLanHEMCS0S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S2Packets.setStatus("current")
_DlWLanHEMCS1S2Packets_Type = Counter64
_DlWLanHEMCS1S2Packets_Object = MibScalar
dlWLanHEMCS1S2Packets = _DlWLanHEMCS1S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 14),
    _DlWLanHEMCS1S2Packets_Type()
)
dlWLanHEMCS1S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S2Packets.setStatus("current")
_DlWLanHEMCS2S2Packets_Type = Counter64
_DlWLanHEMCS2S2Packets_Object = MibScalar
dlWLanHEMCS2S2Packets = _DlWLanHEMCS2S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 15),
    _DlWLanHEMCS2S2Packets_Type()
)
dlWLanHEMCS2S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S2Packets.setStatus("current")
_DlWLanHEMCS3S2Packets_Type = Counter64
_DlWLanHEMCS3S2Packets_Object = MibScalar
dlWLanHEMCS3S2Packets = _DlWLanHEMCS3S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 16),
    _DlWLanHEMCS3S2Packets_Type()
)
dlWLanHEMCS3S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S2Packets.setStatus("current")
_DlWLanHEMCS4S2Packets_Type = Counter64
_DlWLanHEMCS4S2Packets_Object = MibScalar
dlWLanHEMCS4S2Packets = _DlWLanHEMCS4S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 17),
    _DlWLanHEMCS4S2Packets_Type()
)
dlWLanHEMCS4S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S2Packets.setStatus("current")
_DlWLanHEMCS5S2Packets_Type = Counter64
_DlWLanHEMCS5S2Packets_Object = MibScalar
dlWLanHEMCS5S2Packets = _DlWLanHEMCS5S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 18),
    _DlWLanHEMCS5S2Packets_Type()
)
dlWLanHEMCS5S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S2Packets.setStatus("current")
_DlWLanHEMCS6S2Packets_Type = Counter64
_DlWLanHEMCS6S2Packets_Object = MibScalar
dlWLanHEMCS6S2Packets = _DlWLanHEMCS6S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 19),
    _DlWLanHEMCS6S2Packets_Type()
)
dlWLanHEMCS6S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S2Packets.setStatus("current")
_DlWLanHEMCS7S2Packets_Type = Counter64
_DlWLanHEMCS7S2Packets_Object = MibScalar
dlWLanHEMCS7S2Packets = _DlWLanHEMCS7S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 20),
    _DlWLanHEMCS7S2Packets_Type()
)
dlWLanHEMCS7S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S2Packets.setStatus("current")
_DlWLanHEMCS8S2Packets_Type = Counter64
_DlWLanHEMCS8S2Packets_Object = MibScalar
dlWLanHEMCS8S2Packets = _DlWLanHEMCS8S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 21),
    _DlWLanHEMCS8S2Packets_Type()
)
dlWLanHEMCS8S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S2Packets.setStatus("current")
_DlWLanHEMCS9S2Packets_Type = Counter64
_DlWLanHEMCS9S2Packets_Object = MibScalar
dlWLanHEMCS9S2Packets = _DlWLanHEMCS9S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 22),
    _DlWLanHEMCS9S2Packets_Type()
)
dlWLanHEMCS9S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S2Packets.setStatus("current")
_DlWLanHEMCS10S2Packets_Type = Counter64
_DlWLanHEMCS10S2Packets_Object = MibScalar
dlWLanHEMCS10S2Packets = _DlWLanHEMCS10S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 23),
    _DlWLanHEMCS10S2Packets_Type()
)
dlWLanHEMCS10S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S2Packets.setStatus("current")
_DlWLanHEMCS11S2Packets_Type = Counter64
_DlWLanHEMCS11S2Packets_Object = MibScalar
dlWLanHEMCS11S2Packets = _DlWLanHEMCS11S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 24),
    _DlWLanHEMCS11S2Packets_Type()
)
dlWLanHEMCS11S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S2Packets.setStatus("current")
_DlWLanHEMCS0S3Packets_Type = Counter64
_DlWLanHEMCS0S3Packets_Object = MibScalar
dlWLanHEMCS0S3Packets = _DlWLanHEMCS0S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 25),
    _DlWLanHEMCS0S3Packets_Type()
)
dlWLanHEMCS0S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S3Packets.setStatus("current")
_DlWLanHEMCS1S3Packets_Type = Counter64
_DlWLanHEMCS1S3Packets_Object = MibScalar
dlWLanHEMCS1S3Packets = _DlWLanHEMCS1S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 26),
    _DlWLanHEMCS1S3Packets_Type()
)
dlWLanHEMCS1S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S3Packets.setStatus("current")
_DlWLanHEMCS2S3Packets_Type = Counter64
_DlWLanHEMCS2S3Packets_Object = MibScalar
dlWLanHEMCS2S3Packets = _DlWLanHEMCS2S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 27),
    _DlWLanHEMCS2S3Packets_Type()
)
dlWLanHEMCS2S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S3Packets.setStatus("current")
_DlWLanHEMCS3S3Packets_Type = Counter64
_DlWLanHEMCS3S3Packets_Object = MibScalar
dlWLanHEMCS3S3Packets = _DlWLanHEMCS3S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 28),
    _DlWLanHEMCS3S3Packets_Type()
)
dlWLanHEMCS3S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S3Packets.setStatus("current")
_DlWLanHEMCS4S3Packets_Type = Counter64
_DlWLanHEMCS4S3Packets_Object = MibScalar
dlWLanHEMCS4S3Packets = _DlWLanHEMCS4S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 29),
    _DlWLanHEMCS4S3Packets_Type()
)
dlWLanHEMCS4S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S3Packets.setStatus("current")
_DlWLanHEMCS5S3Packets_Type = Counter64
_DlWLanHEMCS5S3Packets_Object = MibScalar
dlWLanHEMCS5S3Packets = _DlWLanHEMCS5S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 30),
    _DlWLanHEMCS5S3Packets_Type()
)
dlWLanHEMCS5S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S3Packets.setStatus("current")
_DlWLanHEMCS6S3Packets_Type = Counter64
_DlWLanHEMCS6S3Packets_Object = MibScalar
dlWLanHEMCS6S3Packets = _DlWLanHEMCS6S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 31),
    _DlWLanHEMCS6S3Packets_Type()
)
dlWLanHEMCS6S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S3Packets.setStatus("current")
_DlWLanHEMCS7S3Packets_Type = Counter64
_DlWLanHEMCS7S3Packets_Object = MibScalar
dlWLanHEMCS7S3Packets = _DlWLanHEMCS7S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 32),
    _DlWLanHEMCS7S3Packets_Type()
)
dlWLanHEMCS7S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S3Packets.setStatus("current")
_DlWLanHEMCS8S3Packets_Type = Counter64
_DlWLanHEMCS8S3Packets_Object = MibScalar
dlWLanHEMCS8S3Packets = _DlWLanHEMCS8S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 33),
    _DlWLanHEMCS8S3Packets_Type()
)
dlWLanHEMCS8S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S3Packets.setStatus("current")
_DlWLanHEMCS9S3Packets_Type = Counter64
_DlWLanHEMCS9S3Packets_Object = MibScalar
dlWLanHEMCS9S3Packets = _DlWLanHEMCS9S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 34),
    _DlWLanHEMCS9S3Packets_Type()
)
dlWLanHEMCS9S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S3Packets.setStatus("current")
_DlWLanHEMCS10S3Packets_Type = Counter64
_DlWLanHEMCS10S3Packets_Object = MibScalar
dlWLanHEMCS10S3Packets = _DlWLanHEMCS10S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 35),
    _DlWLanHEMCS10S3Packets_Type()
)
dlWLanHEMCS10S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S3Packets.setStatus("current")
_DlWLanHEMCS11S3Packets_Type = Counter64
_DlWLanHEMCS11S3Packets_Object = MibScalar
dlWLanHEMCS11S3Packets = _DlWLanHEMCS11S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 36),
    _DlWLanHEMCS11S3Packets_Type()
)
dlWLanHEMCS11S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S3Packets.setStatus("current")
_DlWLanHEMCS0S4Packets_Type = Counter64
_DlWLanHEMCS0S4Packets_Object = MibScalar
dlWLanHEMCS0S4Packets = _DlWLanHEMCS0S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 37),
    _DlWLanHEMCS0S4Packets_Type()
)
dlWLanHEMCS0S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S4Packets.setStatus("current")
_DlWLanHEMCS1S4Packets_Type = Counter64
_DlWLanHEMCS1S4Packets_Object = MibScalar
dlWLanHEMCS1S4Packets = _DlWLanHEMCS1S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 38),
    _DlWLanHEMCS1S4Packets_Type()
)
dlWLanHEMCS1S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S4Packets.setStatus("current")
_DlWLanHEMCS2S4Packets_Type = Counter64
_DlWLanHEMCS2S4Packets_Object = MibScalar
dlWLanHEMCS2S4Packets = _DlWLanHEMCS2S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 39),
    _DlWLanHEMCS2S4Packets_Type()
)
dlWLanHEMCS2S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S4Packets.setStatus("current")
_DlWLanHEMCS3S4Packets_Type = Counter64
_DlWLanHEMCS3S4Packets_Object = MibScalar
dlWLanHEMCS3S4Packets = _DlWLanHEMCS3S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 40),
    _DlWLanHEMCS3S4Packets_Type()
)
dlWLanHEMCS3S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S4Packets.setStatus("current")
_DlWLanHEMCS4S4Packets_Type = Counter64
_DlWLanHEMCS4S4Packets_Object = MibScalar
dlWLanHEMCS4S4Packets = _DlWLanHEMCS4S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 41),
    _DlWLanHEMCS4S4Packets_Type()
)
dlWLanHEMCS4S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S4Packets.setStatus("current")
_DlWLanHEMCS5S4Packets_Type = Counter64
_DlWLanHEMCS5S4Packets_Object = MibScalar
dlWLanHEMCS5S4Packets = _DlWLanHEMCS5S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 42),
    _DlWLanHEMCS5S4Packets_Type()
)
dlWLanHEMCS5S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S4Packets.setStatus("current")
_DlWLanHEMCS6S4Packets_Type = Counter64
_DlWLanHEMCS6S4Packets_Object = MibScalar
dlWLanHEMCS6S4Packets = _DlWLanHEMCS6S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 43),
    _DlWLanHEMCS6S4Packets_Type()
)
dlWLanHEMCS6S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S4Packets.setStatus("current")
_DlWLanHEMCS7S4Packets_Type = Counter64
_DlWLanHEMCS7S4Packets_Object = MibScalar
dlWLanHEMCS7S4Packets = _DlWLanHEMCS7S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 44),
    _DlWLanHEMCS7S4Packets_Type()
)
dlWLanHEMCS7S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S4Packets.setStatus("current")
_DlWLanHEMCS8S4Packets_Type = Counter64
_DlWLanHEMCS8S4Packets_Object = MibScalar
dlWLanHEMCS8S4Packets = _DlWLanHEMCS8S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 45),
    _DlWLanHEMCS8S4Packets_Type()
)
dlWLanHEMCS8S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S4Packets.setStatus("current")
_DlWLanHEMCS9S4Packets_Type = Counter64
_DlWLanHEMCS9S4Packets_Object = MibScalar
dlWLanHEMCS9S4Packets = _DlWLanHEMCS9S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 46),
    _DlWLanHEMCS9S4Packets_Type()
)
dlWLanHEMCS9S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S4Packets.setStatus("current")
_DlWLanHEMCS10S4Packets_Type = Counter64
_DlWLanHEMCS10S4Packets_Object = MibScalar
dlWLanHEMCS10S4Packets = _DlWLanHEMCS10S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 47),
    _DlWLanHEMCS10S4Packets_Type()
)
dlWLanHEMCS10S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S4Packets.setStatus("current")
_DlWLanHEMCS11S4Packets_Type = Counter64
_DlWLanHEMCS11S4Packets_Object = MibScalar
dlWLanHEMCS11S4Packets = _DlWLanHEMCS11S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 48),
    _DlWLanHEMCS11S4Packets_Type()
)
dlWLanHEMCS11S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S4Packets.setStatus("current")
_DlWLanHEMCS0S5Packets_Type = Counter64
_DlWLanHEMCS0S5Packets_Object = MibScalar
dlWLanHEMCS0S5Packets = _DlWLanHEMCS0S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 49),
    _DlWLanHEMCS0S5Packets_Type()
)
dlWLanHEMCS0S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S5Packets.setStatus("current")
_DlWLanHEMCS1S5Packets_Type = Counter64
_DlWLanHEMCS1S5Packets_Object = MibScalar
dlWLanHEMCS1S5Packets = _DlWLanHEMCS1S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 50),
    _DlWLanHEMCS1S5Packets_Type()
)
dlWLanHEMCS1S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S5Packets.setStatus("current")
_DlWLanHEMCS2S5Packets_Type = Counter64
_DlWLanHEMCS2S5Packets_Object = MibScalar
dlWLanHEMCS2S5Packets = _DlWLanHEMCS2S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 51),
    _DlWLanHEMCS2S5Packets_Type()
)
dlWLanHEMCS2S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S5Packets.setStatus("current")
_DlWLanHEMCS3S5Packets_Type = Counter64
_DlWLanHEMCS3S5Packets_Object = MibScalar
dlWLanHEMCS3S5Packets = _DlWLanHEMCS3S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 52),
    _DlWLanHEMCS3S5Packets_Type()
)
dlWLanHEMCS3S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S5Packets.setStatus("current")
_DlWLanHEMCS4S5Packets_Type = Counter64
_DlWLanHEMCS4S5Packets_Object = MibScalar
dlWLanHEMCS4S5Packets = _DlWLanHEMCS4S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 53),
    _DlWLanHEMCS4S5Packets_Type()
)
dlWLanHEMCS4S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S5Packets.setStatus("current")
_DlWLanHEMCS5S5Packets_Type = Counter64
_DlWLanHEMCS5S5Packets_Object = MibScalar
dlWLanHEMCS5S5Packets = _DlWLanHEMCS5S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 54),
    _DlWLanHEMCS5S5Packets_Type()
)
dlWLanHEMCS5S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S5Packets.setStatus("current")
_DlWLanHEMCS6S5Packets_Type = Counter64
_DlWLanHEMCS6S5Packets_Object = MibScalar
dlWLanHEMCS6S5Packets = _DlWLanHEMCS6S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 55),
    _DlWLanHEMCS6S5Packets_Type()
)
dlWLanHEMCS6S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S5Packets.setStatus("current")
_DlWLanHEMCS7S5Packets_Type = Counter64
_DlWLanHEMCS7S5Packets_Object = MibScalar
dlWLanHEMCS7S5Packets = _DlWLanHEMCS7S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 56),
    _DlWLanHEMCS7S5Packets_Type()
)
dlWLanHEMCS7S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S5Packets.setStatus("current")
_DlWLanHEMCS8S5Packets_Type = Counter64
_DlWLanHEMCS8S5Packets_Object = MibScalar
dlWLanHEMCS8S5Packets = _DlWLanHEMCS8S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 57),
    _DlWLanHEMCS8S5Packets_Type()
)
dlWLanHEMCS8S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S5Packets.setStatus("current")
_DlWLanHEMCS9S5Packets_Type = Counter64
_DlWLanHEMCS9S5Packets_Object = MibScalar
dlWLanHEMCS9S5Packets = _DlWLanHEMCS9S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 58),
    _DlWLanHEMCS9S5Packets_Type()
)
dlWLanHEMCS9S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S5Packets.setStatus("current")
_DlWLanHEMCS10S5Packets_Type = Counter64
_DlWLanHEMCS10S5Packets_Object = MibScalar
dlWLanHEMCS10S5Packets = _DlWLanHEMCS10S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 59),
    _DlWLanHEMCS10S5Packets_Type()
)
dlWLanHEMCS10S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S5Packets.setStatus("current")
_DlWLanHEMCS11S5Packets_Type = Counter64
_DlWLanHEMCS11S5Packets_Object = MibScalar
dlWLanHEMCS11S5Packets = _DlWLanHEMCS11S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 60),
    _DlWLanHEMCS11S5Packets_Type()
)
dlWLanHEMCS11S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S5Packets.setStatus("current")
_DlWLanHEMCS0S6Packets_Type = Counter64
_DlWLanHEMCS0S6Packets_Object = MibScalar
dlWLanHEMCS0S6Packets = _DlWLanHEMCS0S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 61),
    _DlWLanHEMCS0S6Packets_Type()
)
dlWLanHEMCS0S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S6Packets.setStatus("current")
_DlWLanHEMCS1S6Packets_Type = Counter64
_DlWLanHEMCS1S6Packets_Object = MibScalar
dlWLanHEMCS1S6Packets = _DlWLanHEMCS1S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 62),
    _DlWLanHEMCS1S6Packets_Type()
)
dlWLanHEMCS1S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S6Packets.setStatus("current")
_DlWLanHEMCS2S6Packets_Type = Counter64
_DlWLanHEMCS2S6Packets_Object = MibScalar
dlWLanHEMCS2S6Packets = _DlWLanHEMCS2S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 63),
    _DlWLanHEMCS2S6Packets_Type()
)
dlWLanHEMCS2S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S6Packets.setStatus("current")
_DlWLanHEMCS3S6Packets_Type = Counter64
_DlWLanHEMCS3S6Packets_Object = MibScalar
dlWLanHEMCS3S6Packets = _DlWLanHEMCS3S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 64),
    _DlWLanHEMCS3S6Packets_Type()
)
dlWLanHEMCS3S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S6Packets.setStatus("current")
_DlWLanHEMCS4S6Packets_Type = Counter64
_DlWLanHEMCS4S6Packets_Object = MibScalar
dlWLanHEMCS4S6Packets = _DlWLanHEMCS4S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 65),
    _DlWLanHEMCS4S6Packets_Type()
)
dlWLanHEMCS4S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S6Packets.setStatus("current")
_DlWLanHEMCS5S6Packets_Type = Counter64
_DlWLanHEMCS5S6Packets_Object = MibScalar
dlWLanHEMCS5S6Packets = _DlWLanHEMCS5S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 66),
    _DlWLanHEMCS5S6Packets_Type()
)
dlWLanHEMCS5S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S6Packets.setStatus("current")
_DlWLanHEMCS6S6Packets_Type = Counter64
_DlWLanHEMCS6S6Packets_Object = MibScalar
dlWLanHEMCS6S6Packets = _DlWLanHEMCS6S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 67),
    _DlWLanHEMCS6S6Packets_Type()
)
dlWLanHEMCS6S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S6Packets.setStatus("current")
_DlWLanHEMCS7S6Packets_Type = Counter64
_DlWLanHEMCS7S6Packets_Object = MibScalar
dlWLanHEMCS7S6Packets = _DlWLanHEMCS7S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 68),
    _DlWLanHEMCS7S6Packets_Type()
)
dlWLanHEMCS7S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S6Packets.setStatus("current")
_DlWLanHEMCS8S6Packets_Type = Counter64
_DlWLanHEMCS8S6Packets_Object = MibScalar
dlWLanHEMCS8S6Packets = _DlWLanHEMCS8S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 69),
    _DlWLanHEMCS8S6Packets_Type()
)
dlWLanHEMCS8S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S6Packets.setStatus("current")
_DlWLanHEMCS9S6Packets_Type = Counter64
_DlWLanHEMCS9S6Packets_Object = MibScalar
dlWLanHEMCS9S6Packets = _DlWLanHEMCS9S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 70),
    _DlWLanHEMCS9S6Packets_Type()
)
dlWLanHEMCS9S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S6Packets.setStatus("current")
_DlWLanHEMCS10S6Packets_Type = Counter64
_DlWLanHEMCS10S6Packets_Object = MibScalar
dlWLanHEMCS10S6Packets = _DlWLanHEMCS10S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 71),
    _DlWLanHEMCS10S6Packets_Type()
)
dlWLanHEMCS10S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S6Packets.setStatus("current")
_DlWLanHEMCS11S6Packets_Type = Counter64
_DlWLanHEMCS11S6Packets_Object = MibScalar
dlWLanHEMCS11S6Packets = _DlWLanHEMCS11S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 72),
    _DlWLanHEMCS11S6Packets_Type()
)
dlWLanHEMCS11S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S6Packets.setStatus("current")
_DlWLanHEMCS0S7Packets_Type = Counter64
_DlWLanHEMCS0S7Packets_Object = MibScalar
dlWLanHEMCS0S7Packets = _DlWLanHEMCS0S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 73),
    _DlWLanHEMCS0S7Packets_Type()
)
dlWLanHEMCS0S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S7Packets.setStatus("current")
_DlWLanHEMCS1S7Packets_Type = Counter64
_DlWLanHEMCS1S7Packets_Object = MibScalar
dlWLanHEMCS1S7Packets = _DlWLanHEMCS1S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 74),
    _DlWLanHEMCS1S7Packets_Type()
)
dlWLanHEMCS1S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S7Packets.setStatus("current")
_DlWLanHEMCS2S7Packets_Type = Counter64
_DlWLanHEMCS2S7Packets_Object = MibScalar
dlWLanHEMCS2S7Packets = _DlWLanHEMCS2S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 75),
    _DlWLanHEMCS2S7Packets_Type()
)
dlWLanHEMCS2S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S7Packets.setStatus("current")
_DlWLanHEMCS3S7Packets_Type = Counter64
_DlWLanHEMCS3S7Packets_Object = MibScalar
dlWLanHEMCS3S7Packets = _DlWLanHEMCS3S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 76),
    _DlWLanHEMCS3S7Packets_Type()
)
dlWLanHEMCS3S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S7Packets.setStatus("current")
_DlWLanHEMCS4S7Packets_Type = Counter64
_DlWLanHEMCS4S7Packets_Object = MibScalar
dlWLanHEMCS4S7Packets = _DlWLanHEMCS4S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 77),
    _DlWLanHEMCS4S7Packets_Type()
)
dlWLanHEMCS4S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S7Packets.setStatus("current")
_DlWLanHEMCS5S7Packets_Type = Counter64
_DlWLanHEMCS5S7Packets_Object = MibScalar
dlWLanHEMCS5S7Packets = _DlWLanHEMCS5S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 78),
    _DlWLanHEMCS5S7Packets_Type()
)
dlWLanHEMCS5S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S7Packets.setStatus("current")
_DlWLanHEMCS6S7Packets_Type = Counter64
_DlWLanHEMCS6S7Packets_Object = MibScalar
dlWLanHEMCS6S7Packets = _DlWLanHEMCS6S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 79),
    _DlWLanHEMCS6S7Packets_Type()
)
dlWLanHEMCS6S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S7Packets.setStatus("current")
_DlWLanHEMCS7S7Packets_Type = Counter64
_DlWLanHEMCS7S7Packets_Object = MibScalar
dlWLanHEMCS7S7Packets = _DlWLanHEMCS7S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 80),
    _DlWLanHEMCS7S7Packets_Type()
)
dlWLanHEMCS7S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S7Packets.setStatus("current")
_DlWLanHEMCS8S7Packets_Type = Counter64
_DlWLanHEMCS8S7Packets_Object = MibScalar
dlWLanHEMCS8S7Packets = _DlWLanHEMCS8S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 81),
    _DlWLanHEMCS8S7Packets_Type()
)
dlWLanHEMCS8S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S7Packets.setStatus("current")
_DlWLanHEMCS9S7Packets_Type = Counter64
_DlWLanHEMCS9S7Packets_Object = MibScalar
dlWLanHEMCS9S7Packets = _DlWLanHEMCS9S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 82),
    _DlWLanHEMCS9S7Packets_Type()
)
dlWLanHEMCS9S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S7Packets.setStatus("current")
_DlWLanHEMCS10S7Packets_Type = Counter64
_DlWLanHEMCS10S7Packets_Object = MibScalar
dlWLanHEMCS10S7Packets = _DlWLanHEMCS10S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 83),
    _DlWLanHEMCS10S7Packets_Type()
)
dlWLanHEMCS10S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S7Packets.setStatus("current")
_DlWLanHEMCS11S7Packets_Type = Counter64
_DlWLanHEMCS11S7Packets_Object = MibScalar
dlWLanHEMCS11S7Packets = _DlWLanHEMCS11S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 84),
    _DlWLanHEMCS11S7Packets_Type()
)
dlWLanHEMCS11S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S7Packets.setStatus("current")
_DlWLanHEMCS0S8Packets_Type = Counter64
_DlWLanHEMCS0S8Packets_Object = MibScalar
dlWLanHEMCS0S8Packets = _DlWLanHEMCS0S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 85),
    _DlWLanHEMCS0S8Packets_Type()
)
dlWLanHEMCS0S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS0S8Packets.setStatus("current")
_DlWLanHEMCS1S8Packets_Type = Counter64
_DlWLanHEMCS1S8Packets_Object = MibScalar
dlWLanHEMCS1S8Packets = _DlWLanHEMCS1S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 86),
    _DlWLanHEMCS1S8Packets_Type()
)
dlWLanHEMCS1S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS1S8Packets.setStatus("current")
_DlWLanHEMCS2S8Packets_Type = Counter64
_DlWLanHEMCS2S8Packets_Object = MibScalar
dlWLanHEMCS2S8Packets = _DlWLanHEMCS2S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 87),
    _DlWLanHEMCS2S8Packets_Type()
)
dlWLanHEMCS2S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS2S8Packets.setStatus("current")
_DlWLanHEMCS3S8Packets_Type = Counter64
_DlWLanHEMCS3S8Packets_Object = MibScalar
dlWLanHEMCS3S8Packets = _DlWLanHEMCS3S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 88),
    _DlWLanHEMCS3S8Packets_Type()
)
dlWLanHEMCS3S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS3S8Packets.setStatus("current")
_DlWLanHEMCS4S8Packets_Type = Counter64
_DlWLanHEMCS4S8Packets_Object = MibScalar
dlWLanHEMCS4S8Packets = _DlWLanHEMCS4S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 89),
    _DlWLanHEMCS4S8Packets_Type()
)
dlWLanHEMCS4S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS4S8Packets.setStatus("current")
_DlWLanHEMCS5S8Packets_Type = Counter64
_DlWLanHEMCS5S8Packets_Object = MibScalar
dlWLanHEMCS5S8Packets = _DlWLanHEMCS5S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 90),
    _DlWLanHEMCS5S8Packets_Type()
)
dlWLanHEMCS5S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS5S8Packets.setStatus("current")
_DlWLanHEMCS6S8Packets_Type = Counter64
_DlWLanHEMCS6S8Packets_Object = MibScalar
dlWLanHEMCS6S8Packets = _DlWLanHEMCS6S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 91),
    _DlWLanHEMCS6S8Packets_Type()
)
dlWLanHEMCS6S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS6S8Packets.setStatus("current")
_DlWLanHEMCS7S8Packets_Type = Counter64
_DlWLanHEMCS7S8Packets_Object = MibScalar
dlWLanHEMCS7S8Packets = _DlWLanHEMCS7S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 92),
    _DlWLanHEMCS7S8Packets_Type()
)
dlWLanHEMCS7S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS7S8Packets.setStatus("current")
_DlWLanHEMCS8S8Packets_Type = Counter64
_DlWLanHEMCS8S8Packets_Object = MibScalar
dlWLanHEMCS8S8Packets = _DlWLanHEMCS8S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 93),
    _DlWLanHEMCS8S8Packets_Type()
)
dlWLanHEMCS8S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS8S8Packets.setStatus("current")
_DlWLanHEMCS9S8Packets_Type = Counter64
_DlWLanHEMCS9S8Packets_Object = MibScalar
dlWLanHEMCS9S8Packets = _DlWLanHEMCS9S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 94),
    _DlWLanHEMCS9S8Packets_Type()
)
dlWLanHEMCS9S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS9S8Packets.setStatus("current")
_DlWLanHEMCS10S8Packets_Type = Counter64
_DlWLanHEMCS10S8Packets_Object = MibScalar
dlWLanHEMCS10S8Packets = _DlWLanHEMCS10S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 95),
    _DlWLanHEMCS10S8Packets_Type()
)
dlWLanHEMCS10S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS10S8Packets.setStatus("current")
_DlWLanHEMCS11S8Packets_Type = Counter64
_DlWLanHEMCS11S8Packets_Object = MibScalar
dlWLanHEMCS11S8Packets = _DlWLanHEMCS11S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 96),
    _DlWLanHEMCS11S8Packets_Type()
)
dlWLanHEMCS11S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS11S8Packets.setStatus("current")
_DlWLanHEMCS12S1Packets_Type = Counter64
_DlWLanHEMCS12S1Packets_Object = MibScalar
dlWLanHEMCS12S1Packets = _DlWLanHEMCS12S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 97),
    _DlWLanHEMCS12S1Packets_Type()
)
dlWLanHEMCS12S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S1Packets.setStatus("current")
_DlWLanHEMCS13S1Packets_Type = Counter64
_DlWLanHEMCS13S1Packets_Object = MibScalar
dlWLanHEMCS13S1Packets = _DlWLanHEMCS13S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 98),
    _DlWLanHEMCS13S1Packets_Type()
)
dlWLanHEMCS13S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S1Packets.setStatus("current")
_DlWLanHEMCS12S2Packets_Type = Counter64
_DlWLanHEMCS12S2Packets_Object = MibScalar
dlWLanHEMCS12S2Packets = _DlWLanHEMCS12S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 99),
    _DlWLanHEMCS12S2Packets_Type()
)
dlWLanHEMCS12S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S2Packets.setStatus("current")
_DlWLanHEMCS13S2Packets_Type = Counter64
_DlWLanHEMCS13S2Packets_Object = MibScalar
dlWLanHEMCS13S2Packets = _DlWLanHEMCS13S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 100),
    _DlWLanHEMCS13S2Packets_Type()
)
dlWLanHEMCS13S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S2Packets.setStatus("current")
_DlWLanHEMCS12S3Packets_Type = Counter64
_DlWLanHEMCS12S3Packets_Object = MibScalar
dlWLanHEMCS12S3Packets = _DlWLanHEMCS12S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 101),
    _DlWLanHEMCS12S3Packets_Type()
)
dlWLanHEMCS12S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S3Packets.setStatus("current")
_DlWLanHEMCS13S3Packets_Type = Counter64
_DlWLanHEMCS13S3Packets_Object = MibScalar
dlWLanHEMCS13S3Packets = _DlWLanHEMCS13S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 102),
    _DlWLanHEMCS13S3Packets_Type()
)
dlWLanHEMCS13S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S3Packets.setStatus("current")
_DlWLanHEMCS12S4Packets_Type = Counter64
_DlWLanHEMCS12S4Packets_Object = MibScalar
dlWLanHEMCS12S4Packets = _DlWLanHEMCS12S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 103),
    _DlWLanHEMCS12S4Packets_Type()
)
dlWLanHEMCS12S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S4Packets.setStatus("current")
_DlWLanHEMCS13S4Packets_Type = Counter64
_DlWLanHEMCS13S4Packets_Object = MibScalar
dlWLanHEMCS13S4Packets = _DlWLanHEMCS13S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 104),
    _DlWLanHEMCS13S4Packets_Type()
)
dlWLanHEMCS13S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S4Packets.setStatus("current")
_DlWLanHEMCS12S5Packets_Type = Counter64
_DlWLanHEMCS12S5Packets_Object = MibScalar
dlWLanHEMCS12S5Packets = _DlWLanHEMCS12S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 105),
    _DlWLanHEMCS12S5Packets_Type()
)
dlWLanHEMCS12S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S5Packets.setStatus("current")
_DlWLanHEMCS13S5Packets_Type = Counter64
_DlWLanHEMCS13S5Packets_Object = MibScalar
dlWLanHEMCS13S5Packets = _DlWLanHEMCS13S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 106),
    _DlWLanHEMCS13S5Packets_Type()
)
dlWLanHEMCS13S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S5Packets.setStatus("current")
_DlWLanHEMCS12S6Packets_Type = Counter64
_DlWLanHEMCS12S6Packets_Object = MibScalar
dlWLanHEMCS12S6Packets = _DlWLanHEMCS12S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 107),
    _DlWLanHEMCS12S6Packets_Type()
)
dlWLanHEMCS12S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S6Packets.setStatus("current")
_DlWLanHEMCS13S6Packets_Type = Counter64
_DlWLanHEMCS13S6Packets_Object = MibScalar
dlWLanHEMCS13S6Packets = _DlWLanHEMCS13S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 108),
    _DlWLanHEMCS13S6Packets_Type()
)
dlWLanHEMCS13S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S6Packets.setStatus("current")
_DlWLanHEMCS12S7Packets_Type = Counter64
_DlWLanHEMCS12S7Packets_Object = MibScalar
dlWLanHEMCS12S7Packets = _DlWLanHEMCS12S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 109),
    _DlWLanHEMCS12S7Packets_Type()
)
dlWLanHEMCS12S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S7Packets.setStatus("current")
_DlWLanHEMCS13S7Packets_Type = Counter64
_DlWLanHEMCS13S7Packets_Object = MibScalar
dlWLanHEMCS13S7Packets = _DlWLanHEMCS13S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 110),
    _DlWLanHEMCS13S7Packets_Type()
)
dlWLanHEMCS13S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S7Packets.setStatus("current")
_DlWLanHEMCS12S8Packets_Type = Counter64
_DlWLanHEMCS12S8Packets_Object = MibScalar
dlWLanHEMCS12S8Packets = _DlWLanHEMCS12S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 111),
    _DlWLanHEMCS12S8Packets_Type()
)
dlWLanHEMCS12S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS12S8Packets.setStatus("current")
_DlWLanHEMCS13S8Packets_Type = Counter64
_DlWLanHEMCS13S8Packets_Object = MibScalar
dlWLanHEMCS13S8Packets = _DlWLanHEMCS13S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 1, 112),
    _DlWLanHEMCS13S8Packets_Type()
)
dlWLanHEMCS13S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanHEMCS13S8Packets.setStatus("current")
_UlWlanHEMCSPackets_ObjectIdentity = ObjectIdentity
ulWlanHEMCSPackets = _UlWlanHEMCSPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2)
)
_UlWLanHEMCS0S1Packets_Type = Counter64
_UlWLanHEMCS0S1Packets_Object = MibScalar
ulWLanHEMCS0S1Packets = _UlWLanHEMCS0S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 1),
    _UlWLanHEMCS0S1Packets_Type()
)
ulWLanHEMCS0S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S1Packets.setStatus("current")
_UlWLanHEMCS1S1Packets_Type = Counter64
_UlWLanHEMCS1S1Packets_Object = MibScalar
ulWLanHEMCS1S1Packets = _UlWLanHEMCS1S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 2),
    _UlWLanHEMCS1S1Packets_Type()
)
ulWLanHEMCS1S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S1Packets.setStatus("current")
_UlWLanHEMCS2S1Packets_Type = Counter64
_UlWLanHEMCS2S1Packets_Object = MibScalar
ulWLanHEMCS2S1Packets = _UlWLanHEMCS2S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 3),
    _UlWLanHEMCS2S1Packets_Type()
)
ulWLanHEMCS2S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S1Packets.setStatus("current")
_UlWLanHEMCS3S1Packets_Type = Counter64
_UlWLanHEMCS3S1Packets_Object = MibScalar
ulWLanHEMCS3S1Packets = _UlWLanHEMCS3S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 4),
    _UlWLanHEMCS3S1Packets_Type()
)
ulWLanHEMCS3S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S1Packets.setStatus("current")
_UlWLanHEMCS4S1Packets_Type = Counter64
_UlWLanHEMCS4S1Packets_Object = MibScalar
ulWLanHEMCS4S1Packets = _UlWLanHEMCS4S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 5),
    _UlWLanHEMCS4S1Packets_Type()
)
ulWLanHEMCS4S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S1Packets.setStatus("current")
_UlWLanHEMCS5S1Packets_Type = Counter64
_UlWLanHEMCS5S1Packets_Object = MibScalar
ulWLanHEMCS5S1Packets = _UlWLanHEMCS5S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 6),
    _UlWLanHEMCS5S1Packets_Type()
)
ulWLanHEMCS5S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S1Packets.setStatus("current")
_UlWLanHEMCS6S1Packets_Type = Counter64
_UlWLanHEMCS6S1Packets_Object = MibScalar
ulWLanHEMCS6S1Packets = _UlWLanHEMCS6S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 7),
    _UlWLanHEMCS6S1Packets_Type()
)
ulWLanHEMCS6S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S1Packets.setStatus("current")
_UlWLanHEMCS7S1Packets_Type = Counter64
_UlWLanHEMCS7S1Packets_Object = MibScalar
ulWLanHEMCS7S1Packets = _UlWLanHEMCS7S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 8),
    _UlWLanHEMCS7S1Packets_Type()
)
ulWLanHEMCS7S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S1Packets.setStatus("current")
_UlWLanHEMCS8S1Packets_Type = Counter64
_UlWLanHEMCS8S1Packets_Object = MibScalar
ulWLanHEMCS8S1Packets = _UlWLanHEMCS8S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 9),
    _UlWLanHEMCS8S1Packets_Type()
)
ulWLanHEMCS8S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S1Packets.setStatus("current")
_UlWLanHEMCS9S1Packets_Type = Counter64
_UlWLanHEMCS9S1Packets_Object = MibScalar
ulWLanHEMCS9S1Packets = _UlWLanHEMCS9S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 10),
    _UlWLanHEMCS9S1Packets_Type()
)
ulWLanHEMCS9S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S1Packets.setStatus("current")
_UlWLanHEMCS10S1Packets_Type = Counter64
_UlWLanHEMCS10S1Packets_Object = MibScalar
ulWLanHEMCS10S1Packets = _UlWLanHEMCS10S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 11),
    _UlWLanHEMCS10S1Packets_Type()
)
ulWLanHEMCS10S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S1Packets.setStatus("current")
_UlWLanHEMCS11S1Packets_Type = Counter64
_UlWLanHEMCS11S1Packets_Object = MibScalar
ulWLanHEMCS11S1Packets = _UlWLanHEMCS11S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 12),
    _UlWLanHEMCS11S1Packets_Type()
)
ulWLanHEMCS11S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S1Packets.setStatus("current")
_UlWLanHEMCS0S2Packets_Type = Counter64
_UlWLanHEMCS0S2Packets_Object = MibScalar
ulWLanHEMCS0S2Packets = _UlWLanHEMCS0S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 13),
    _UlWLanHEMCS0S2Packets_Type()
)
ulWLanHEMCS0S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S2Packets.setStatus("current")
_UlWLanHEMCS1S2Packets_Type = Counter64
_UlWLanHEMCS1S2Packets_Object = MibScalar
ulWLanHEMCS1S2Packets = _UlWLanHEMCS1S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 14),
    _UlWLanHEMCS1S2Packets_Type()
)
ulWLanHEMCS1S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S2Packets.setStatus("current")
_UlWLanHEMCS2S2Packets_Type = Counter64
_UlWLanHEMCS2S2Packets_Object = MibScalar
ulWLanHEMCS2S2Packets = _UlWLanHEMCS2S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 15),
    _UlWLanHEMCS2S2Packets_Type()
)
ulWLanHEMCS2S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S2Packets.setStatus("current")
_UlWLanHEMCS3S2Packets_Type = Counter64
_UlWLanHEMCS3S2Packets_Object = MibScalar
ulWLanHEMCS3S2Packets = _UlWLanHEMCS3S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 16),
    _UlWLanHEMCS3S2Packets_Type()
)
ulWLanHEMCS3S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S2Packets.setStatus("current")
_UlWLanHEMCS4S2Packets_Type = Counter64
_UlWLanHEMCS4S2Packets_Object = MibScalar
ulWLanHEMCS4S2Packets = _UlWLanHEMCS4S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 17),
    _UlWLanHEMCS4S2Packets_Type()
)
ulWLanHEMCS4S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S2Packets.setStatus("current")
_UlWLanHEMCS5S2Packets_Type = Counter64
_UlWLanHEMCS5S2Packets_Object = MibScalar
ulWLanHEMCS5S2Packets = _UlWLanHEMCS5S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 18),
    _UlWLanHEMCS5S2Packets_Type()
)
ulWLanHEMCS5S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S2Packets.setStatus("current")
_UlWLanHEMCS6S2Packets_Type = Counter64
_UlWLanHEMCS6S2Packets_Object = MibScalar
ulWLanHEMCS6S2Packets = _UlWLanHEMCS6S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 19),
    _UlWLanHEMCS6S2Packets_Type()
)
ulWLanHEMCS6S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S2Packets.setStatus("current")
_UlWLanHEMCS7S2Packets_Type = Counter64
_UlWLanHEMCS7S2Packets_Object = MibScalar
ulWLanHEMCS7S2Packets = _UlWLanHEMCS7S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 20),
    _UlWLanHEMCS7S2Packets_Type()
)
ulWLanHEMCS7S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S2Packets.setStatus("current")
_UlWLanHEMCS8S2Packets_Type = Counter64
_UlWLanHEMCS8S2Packets_Object = MibScalar
ulWLanHEMCS8S2Packets = _UlWLanHEMCS8S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 21),
    _UlWLanHEMCS8S2Packets_Type()
)
ulWLanHEMCS8S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S2Packets.setStatus("current")
_UlWLanHEMCS9S2Packets_Type = Counter64
_UlWLanHEMCS9S2Packets_Object = MibScalar
ulWLanHEMCS9S2Packets = _UlWLanHEMCS9S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 22),
    _UlWLanHEMCS9S2Packets_Type()
)
ulWLanHEMCS9S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S2Packets.setStatus("current")
_UlWLanHEMCS10S2Packets_Type = Counter64
_UlWLanHEMCS10S2Packets_Object = MibScalar
ulWLanHEMCS10S2Packets = _UlWLanHEMCS10S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 23),
    _UlWLanHEMCS10S2Packets_Type()
)
ulWLanHEMCS10S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S2Packets.setStatus("current")
_UlWLanHEMCS11S2Packets_Type = Counter64
_UlWLanHEMCS11S2Packets_Object = MibScalar
ulWLanHEMCS11S2Packets = _UlWLanHEMCS11S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 24),
    _UlWLanHEMCS11S2Packets_Type()
)
ulWLanHEMCS11S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S2Packets.setStatus("current")
_UlWLanHEMCS0S3Packets_Type = Counter64
_UlWLanHEMCS0S3Packets_Object = MibScalar
ulWLanHEMCS0S3Packets = _UlWLanHEMCS0S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 25),
    _UlWLanHEMCS0S3Packets_Type()
)
ulWLanHEMCS0S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S3Packets.setStatus("current")
_UlWLanHEMCS1S3Packets_Type = Counter64
_UlWLanHEMCS1S3Packets_Object = MibScalar
ulWLanHEMCS1S3Packets = _UlWLanHEMCS1S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 26),
    _UlWLanHEMCS1S3Packets_Type()
)
ulWLanHEMCS1S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S3Packets.setStatus("current")
_UlWLanHEMCS2S3Packets_Type = Counter64
_UlWLanHEMCS2S3Packets_Object = MibScalar
ulWLanHEMCS2S3Packets = _UlWLanHEMCS2S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 27),
    _UlWLanHEMCS2S3Packets_Type()
)
ulWLanHEMCS2S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S3Packets.setStatus("current")
_UlWLanHEMCS3S3Packets_Type = Counter64
_UlWLanHEMCS3S3Packets_Object = MibScalar
ulWLanHEMCS3S3Packets = _UlWLanHEMCS3S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 28),
    _UlWLanHEMCS3S3Packets_Type()
)
ulWLanHEMCS3S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S3Packets.setStatus("current")
_UlWLanHEMCS4S3Packets_Type = Counter64
_UlWLanHEMCS4S3Packets_Object = MibScalar
ulWLanHEMCS4S3Packets = _UlWLanHEMCS4S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 29),
    _UlWLanHEMCS4S3Packets_Type()
)
ulWLanHEMCS4S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S3Packets.setStatus("current")
_UlWLanHEMCS5S3Packets_Type = Counter64
_UlWLanHEMCS5S3Packets_Object = MibScalar
ulWLanHEMCS5S3Packets = _UlWLanHEMCS5S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 30),
    _UlWLanHEMCS5S3Packets_Type()
)
ulWLanHEMCS5S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S3Packets.setStatus("current")
_UlWLanHEMCS6S3Packets_Type = Counter64
_UlWLanHEMCS6S3Packets_Object = MibScalar
ulWLanHEMCS6S3Packets = _UlWLanHEMCS6S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 31),
    _UlWLanHEMCS6S3Packets_Type()
)
ulWLanHEMCS6S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S3Packets.setStatus("current")
_UlWLanHEMCS7S3Packets_Type = Counter64
_UlWLanHEMCS7S3Packets_Object = MibScalar
ulWLanHEMCS7S3Packets = _UlWLanHEMCS7S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 32),
    _UlWLanHEMCS7S3Packets_Type()
)
ulWLanHEMCS7S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S3Packets.setStatus("current")
_UlWLanHEMCS8S3Packets_Type = Counter64
_UlWLanHEMCS8S3Packets_Object = MibScalar
ulWLanHEMCS8S3Packets = _UlWLanHEMCS8S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 33),
    _UlWLanHEMCS8S3Packets_Type()
)
ulWLanHEMCS8S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S3Packets.setStatus("current")
_UlWLanHEMCS9S3Packets_Type = Counter64
_UlWLanHEMCS9S3Packets_Object = MibScalar
ulWLanHEMCS9S3Packets = _UlWLanHEMCS9S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 34),
    _UlWLanHEMCS9S3Packets_Type()
)
ulWLanHEMCS9S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S3Packets.setStatus("current")
_UlWLanHEMCS10S3Packets_Type = Counter64
_UlWLanHEMCS10S3Packets_Object = MibScalar
ulWLanHEMCS10S3Packets = _UlWLanHEMCS10S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 35),
    _UlWLanHEMCS10S3Packets_Type()
)
ulWLanHEMCS10S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S3Packets.setStatus("current")
_UlWLanHEMCS11S3Packets_Type = Counter64
_UlWLanHEMCS11S3Packets_Object = MibScalar
ulWLanHEMCS11S3Packets = _UlWLanHEMCS11S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 36),
    _UlWLanHEMCS11S3Packets_Type()
)
ulWLanHEMCS11S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S3Packets.setStatus("current")
_UlWLanHEMCS0S4Packets_Type = Counter64
_UlWLanHEMCS0S4Packets_Object = MibScalar
ulWLanHEMCS0S4Packets = _UlWLanHEMCS0S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 37),
    _UlWLanHEMCS0S4Packets_Type()
)
ulWLanHEMCS0S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S4Packets.setStatus("current")
_UlWLanHEMCS1S4Packets_Type = Counter64
_UlWLanHEMCS1S4Packets_Object = MibScalar
ulWLanHEMCS1S4Packets = _UlWLanHEMCS1S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 38),
    _UlWLanHEMCS1S4Packets_Type()
)
ulWLanHEMCS1S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S4Packets.setStatus("current")
_UlWLanHEMCS2S4Packets_Type = Counter64
_UlWLanHEMCS2S4Packets_Object = MibScalar
ulWLanHEMCS2S4Packets = _UlWLanHEMCS2S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 39),
    _UlWLanHEMCS2S4Packets_Type()
)
ulWLanHEMCS2S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S4Packets.setStatus("current")
_UlWLanHEMCS3S4Packets_Type = Counter64
_UlWLanHEMCS3S4Packets_Object = MibScalar
ulWLanHEMCS3S4Packets = _UlWLanHEMCS3S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 40),
    _UlWLanHEMCS3S4Packets_Type()
)
ulWLanHEMCS3S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S4Packets.setStatus("current")
_UlWLanHEMCS4S4Packets_Type = Counter64
_UlWLanHEMCS4S4Packets_Object = MibScalar
ulWLanHEMCS4S4Packets = _UlWLanHEMCS4S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 41),
    _UlWLanHEMCS4S4Packets_Type()
)
ulWLanHEMCS4S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S4Packets.setStatus("current")
_UlWLanHEMCS5S4Packets_Type = Counter64
_UlWLanHEMCS5S4Packets_Object = MibScalar
ulWLanHEMCS5S4Packets = _UlWLanHEMCS5S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 42),
    _UlWLanHEMCS5S4Packets_Type()
)
ulWLanHEMCS5S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S4Packets.setStatus("current")
_UlWLanHEMCS6S4Packets_Type = Counter64
_UlWLanHEMCS6S4Packets_Object = MibScalar
ulWLanHEMCS6S4Packets = _UlWLanHEMCS6S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 43),
    _UlWLanHEMCS6S4Packets_Type()
)
ulWLanHEMCS6S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S4Packets.setStatus("current")
_UlWLanHEMCS7S4Packets_Type = Counter64
_UlWLanHEMCS7S4Packets_Object = MibScalar
ulWLanHEMCS7S4Packets = _UlWLanHEMCS7S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 44),
    _UlWLanHEMCS7S4Packets_Type()
)
ulWLanHEMCS7S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S4Packets.setStatus("current")
_UlWLanHEMCS8S4Packets_Type = Counter64
_UlWLanHEMCS8S4Packets_Object = MibScalar
ulWLanHEMCS8S4Packets = _UlWLanHEMCS8S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 45),
    _UlWLanHEMCS8S4Packets_Type()
)
ulWLanHEMCS8S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S4Packets.setStatus("current")
_UlWLanHEMCS9S4Packets_Type = Counter64
_UlWLanHEMCS9S4Packets_Object = MibScalar
ulWLanHEMCS9S4Packets = _UlWLanHEMCS9S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 46),
    _UlWLanHEMCS9S4Packets_Type()
)
ulWLanHEMCS9S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S4Packets.setStatus("current")
_UlWLanHEMCS10S4Packets_Type = Counter64
_UlWLanHEMCS10S4Packets_Object = MibScalar
ulWLanHEMCS10S4Packets = _UlWLanHEMCS10S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 47),
    _UlWLanHEMCS10S4Packets_Type()
)
ulWLanHEMCS10S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S4Packets.setStatus("current")
_UlWLanHEMCS11S4Packets_Type = Counter64
_UlWLanHEMCS11S4Packets_Object = MibScalar
ulWLanHEMCS11S4Packets = _UlWLanHEMCS11S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 48),
    _UlWLanHEMCS11S4Packets_Type()
)
ulWLanHEMCS11S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S4Packets.setStatus("current")
_UlWLanHEMCS0S5Packets_Type = Counter64
_UlWLanHEMCS0S5Packets_Object = MibScalar
ulWLanHEMCS0S5Packets = _UlWLanHEMCS0S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 49),
    _UlWLanHEMCS0S5Packets_Type()
)
ulWLanHEMCS0S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S5Packets.setStatus("current")
_UlWLanHEMCS1S5Packets_Type = Counter64
_UlWLanHEMCS1S5Packets_Object = MibScalar
ulWLanHEMCS1S5Packets = _UlWLanHEMCS1S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 50),
    _UlWLanHEMCS1S5Packets_Type()
)
ulWLanHEMCS1S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S5Packets.setStatus("current")
_UlWLanHEMCS2S5Packets_Type = Counter64
_UlWLanHEMCS2S5Packets_Object = MibScalar
ulWLanHEMCS2S5Packets = _UlWLanHEMCS2S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 51),
    _UlWLanHEMCS2S5Packets_Type()
)
ulWLanHEMCS2S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S5Packets.setStatus("current")
_UlWLanHEMCS3S5Packets_Type = Counter64
_UlWLanHEMCS3S5Packets_Object = MibScalar
ulWLanHEMCS3S5Packets = _UlWLanHEMCS3S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 52),
    _UlWLanHEMCS3S5Packets_Type()
)
ulWLanHEMCS3S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S5Packets.setStatus("current")
_UlWLanHEMCS4S5Packets_Type = Counter64
_UlWLanHEMCS4S5Packets_Object = MibScalar
ulWLanHEMCS4S5Packets = _UlWLanHEMCS4S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 53),
    _UlWLanHEMCS4S5Packets_Type()
)
ulWLanHEMCS4S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S5Packets.setStatus("current")
_UlWLanHEMCS5S5Packets_Type = Counter64
_UlWLanHEMCS5S5Packets_Object = MibScalar
ulWLanHEMCS5S5Packets = _UlWLanHEMCS5S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 54),
    _UlWLanHEMCS5S5Packets_Type()
)
ulWLanHEMCS5S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S5Packets.setStatus("current")
_UlWLanHEMCS6S5Packets_Type = Counter64
_UlWLanHEMCS6S5Packets_Object = MibScalar
ulWLanHEMCS6S5Packets = _UlWLanHEMCS6S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 55),
    _UlWLanHEMCS6S5Packets_Type()
)
ulWLanHEMCS6S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S5Packets.setStatus("current")
_UlWLanHEMCS7S5Packets_Type = Counter64
_UlWLanHEMCS7S5Packets_Object = MibScalar
ulWLanHEMCS7S5Packets = _UlWLanHEMCS7S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 56),
    _UlWLanHEMCS7S5Packets_Type()
)
ulWLanHEMCS7S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S5Packets.setStatus("current")
_UlWLanHEMCS8S5Packets_Type = Counter64
_UlWLanHEMCS8S5Packets_Object = MibScalar
ulWLanHEMCS8S5Packets = _UlWLanHEMCS8S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 57),
    _UlWLanHEMCS8S5Packets_Type()
)
ulWLanHEMCS8S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S5Packets.setStatus("current")
_UlWLanHEMCS9S5Packets_Type = Counter64
_UlWLanHEMCS9S5Packets_Object = MibScalar
ulWLanHEMCS9S5Packets = _UlWLanHEMCS9S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 58),
    _UlWLanHEMCS9S5Packets_Type()
)
ulWLanHEMCS9S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S5Packets.setStatus("current")
_UlWLanHEMCS10S5Packets_Type = Counter64
_UlWLanHEMCS10S5Packets_Object = MibScalar
ulWLanHEMCS10S5Packets = _UlWLanHEMCS10S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 59),
    _UlWLanHEMCS10S5Packets_Type()
)
ulWLanHEMCS10S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S5Packets.setStatus("current")
_UlWLanHEMCS11S5Packets_Type = Counter64
_UlWLanHEMCS11S5Packets_Object = MibScalar
ulWLanHEMCS11S5Packets = _UlWLanHEMCS11S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 60),
    _UlWLanHEMCS11S5Packets_Type()
)
ulWLanHEMCS11S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S5Packets.setStatus("current")
_UlWLanHEMCS0S6Packets_Type = Counter64
_UlWLanHEMCS0S6Packets_Object = MibScalar
ulWLanHEMCS0S6Packets = _UlWLanHEMCS0S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 61),
    _UlWLanHEMCS0S6Packets_Type()
)
ulWLanHEMCS0S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S6Packets.setStatus("current")
_UlWLanHEMCS1S6Packets_Type = Counter64
_UlWLanHEMCS1S6Packets_Object = MibScalar
ulWLanHEMCS1S6Packets = _UlWLanHEMCS1S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 62),
    _UlWLanHEMCS1S6Packets_Type()
)
ulWLanHEMCS1S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S6Packets.setStatus("current")
_UlWLanHEMCS2S6Packets_Type = Counter64
_UlWLanHEMCS2S6Packets_Object = MibScalar
ulWLanHEMCS2S6Packets = _UlWLanHEMCS2S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 63),
    _UlWLanHEMCS2S6Packets_Type()
)
ulWLanHEMCS2S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S6Packets.setStatus("current")
_UlWLanHEMCS3S6Packets_Type = Counter64
_UlWLanHEMCS3S6Packets_Object = MibScalar
ulWLanHEMCS3S6Packets = _UlWLanHEMCS3S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 64),
    _UlWLanHEMCS3S6Packets_Type()
)
ulWLanHEMCS3S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S6Packets.setStatus("current")
_UlWLanHEMCS4S6Packets_Type = Counter64
_UlWLanHEMCS4S6Packets_Object = MibScalar
ulWLanHEMCS4S6Packets = _UlWLanHEMCS4S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 65),
    _UlWLanHEMCS4S6Packets_Type()
)
ulWLanHEMCS4S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S6Packets.setStatus("current")
_UlWLanHEMCS5S6Packets_Type = Counter64
_UlWLanHEMCS5S6Packets_Object = MibScalar
ulWLanHEMCS5S6Packets = _UlWLanHEMCS5S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 66),
    _UlWLanHEMCS5S6Packets_Type()
)
ulWLanHEMCS5S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S6Packets.setStatus("current")
_UlWLanHEMCS6S6Packets_Type = Counter64
_UlWLanHEMCS6S6Packets_Object = MibScalar
ulWLanHEMCS6S6Packets = _UlWLanHEMCS6S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 67),
    _UlWLanHEMCS6S6Packets_Type()
)
ulWLanHEMCS6S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S6Packets.setStatus("current")
_UlWLanHEMCS7S6Packets_Type = Counter64
_UlWLanHEMCS7S6Packets_Object = MibScalar
ulWLanHEMCS7S6Packets = _UlWLanHEMCS7S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 68),
    _UlWLanHEMCS7S6Packets_Type()
)
ulWLanHEMCS7S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S6Packets.setStatus("current")
_UlWLanHEMCS8S6Packets_Type = Counter64
_UlWLanHEMCS8S6Packets_Object = MibScalar
ulWLanHEMCS8S6Packets = _UlWLanHEMCS8S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 69),
    _UlWLanHEMCS8S6Packets_Type()
)
ulWLanHEMCS8S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S6Packets.setStatus("current")
_UlWLanHEMCS9S6Packets_Type = Counter64
_UlWLanHEMCS9S6Packets_Object = MibScalar
ulWLanHEMCS9S6Packets = _UlWLanHEMCS9S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 70),
    _UlWLanHEMCS9S6Packets_Type()
)
ulWLanHEMCS9S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S6Packets.setStatus("current")
_UlWLanHEMCS10S6Packets_Type = Counter64
_UlWLanHEMCS10S6Packets_Object = MibScalar
ulWLanHEMCS10S6Packets = _UlWLanHEMCS10S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 71),
    _UlWLanHEMCS10S6Packets_Type()
)
ulWLanHEMCS10S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S6Packets.setStatus("current")
_UlWLanHEMCS11S6Packets_Type = Counter64
_UlWLanHEMCS11S6Packets_Object = MibScalar
ulWLanHEMCS11S6Packets = _UlWLanHEMCS11S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 72),
    _UlWLanHEMCS11S6Packets_Type()
)
ulWLanHEMCS11S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S6Packets.setStatus("current")
_UlWLanHEMCS0S7Packets_Type = Counter64
_UlWLanHEMCS0S7Packets_Object = MibScalar
ulWLanHEMCS0S7Packets = _UlWLanHEMCS0S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 73),
    _UlWLanHEMCS0S7Packets_Type()
)
ulWLanHEMCS0S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S7Packets.setStatus("current")
_UlWLanHEMCS1S7Packets_Type = Counter64
_UlWLanHEMCS1S7Packets_Object = MibScalar
ulWLanHEMCS1S7Packets = _UlWLanHEMCS1S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 74),
    _UlWLanHEMCS1S7Packets_Type()
)
ulWLanHEMCS1S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S7Packets.setStatus("current")
_UlWLanHEMCS2S7Packets_Type = Counter64
_UlWLanHEMCS2S7Packets_Object = MibScalar
ulWLanHEMCS2S7Packets = _UlWLanHEMCS2S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 75),
    _UlWLanHEMCS2S7Packets_Type()
)
ulWLanHEMCS2S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S7Packets.setStatus("current")
_UlWLanHEMCS3S7Packets_Type = Counter64
_UlWLanHEMCS3S7Packets_Object = MibScalar
ulWLanHEMCS3S7Packets = _UlWLanHEMCS3S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 76),
    _UlWLanHEMCS3S7Packets_Type()
)
ulWLanHEMCS3S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S7Packets.setStatus("current")
_UlWLanHEMCS4S7Packets_Type = Counter64
_UlWLanHEMCS4S7Packets_Object = MibScalar
ulWLanHEMCS4S7Packets = _UlWLanHEMCS4S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 77),
    _UlWLanHEMCS4S7Packets_Type()
)
ulWLanHEMCS4S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S7Packets.setStatus("current")
_UlWLanHEMCS5S7Packets_Type = Counter64
_UlWLanHEMCS5S7Packets_Object = MibScalar
ulWLanHEMCS5S7Packets = _UlWLanHEMCS5S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 78),
    _UlWLanHEMCS5S7Packets_Type()
)
ulWLanHEMCS5S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S7Packets.setStatus("current")
_UlWLanHEMCS6S7Packets_Type = Counter64
_UlWLanHEMCS6S7Packets_Object = MibScalar
ulWLanHEMCS6S7Packets = _UlWLanHEMCS6S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 79),
    _UlWLanHEMCS6S7Packets_Type()
)
ulWLanHEMCS6S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S7Packets.setStatus("current")
_UlWLanHEMCS7S7Packets_Type = Counter64
_UlWLanHEMCS7S7Packets_Object = MibScalar
ulWLanHEMCS7S7Packets = _UlWLanHEMCS7S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 80),
    _UlWLanHEMCS7S7Packets_Type()
)
ulWLanHEMCS7S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S7Packets.setStatus("current")
_UlWLanHEMCS8S7Packets_Type = Counter64
_UlWLanHEMCS8S7Packets_Object = MibScalar
ulWLanHEMCS8S7Packets = _UlWLanHEMCS8S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 81),
    _UlWLanHEMCS8S7Packets_Type()
)
ulWLanHEMCS8S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S7Packets.setStatus("current")
_UlWLanHEMCS9S7Packets_Type = Counter64
_UlWLanHEMCS9S7Packets_Object = MibScalar
ulWLanHEMCS9S7Packets = _UlWLanHEMCS9S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 82),
    _UlWLanHEMCS9S7Packets_Type()
)
ulWLanHEMCS9S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S7Packets.setStatus("current")
_UlWLanHEMCS10S7Packets_Type = Counter64
_UlWLanHEMCS10S7Packets_Object = MibScalar
ulWLanHEMCS10S7Packets = _UlWLanHEMCS10S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 83),
    _UlWLanHEMCS10S7Packets_Type()
)
ulWLanHEMCS10S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S7Packets.setStatus("current")
_UlWLanHEMCS11S7Packets_Type = Counter64
_UlWLanHEMCS11S7Packets_Object = MibScalar
ulWLanHEMCS11S7Packets = _UlWLanHEMCS11S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 84),
    _UlWLanHEMCS11S7Packets_Type()
)
ulWLanHEMCS11S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S7Packets.setStatus("current")
_UlWLanHEMCS0S8Packets_Type = Counter64
_UlWLanHEMCS0S8Packets_Object = MibScalar
ulWLanHEMCS0S8Packets = _UlWLanHEMCS0S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 85),
    _UlWLanHEMCS0S8Packets_Type()
)
ulWLanHEMCS0S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS0S8Packets.setStatus("current")
_UlWLanHEMCS1S8Packets_Type = Counter64
_UlWLanHEMCS1S8Packets_Object = MibScalar
ulWLanHEMCS1S8Packets = _UlWLanHEMCS1S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 86),
    _UlWLanHEMCS1S8Packets_Type()
)
ulWLanHEMCS1S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS1S8Packets.setStatus("current")
_UlWLanHEMCS2S8Packets_Type = Counter64
_UlWLanHEMCS2S8Packets_Object = MibScalar
ulWLanHEMCS2S8Packets = _UlWLanHEMCS2S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 87),
    _UlWLanHEMCS2S8Packets_Type()
)
ulWLanHEMCS2S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS2S8Packets.setStatus("current")
_UlWLanHEMCS3S8Packets_Type = Counter64
_UlWLanHEMCS3S8Packets_Object = MibScalar
ulWLanHEMCS3S8Packets = _UlWLanHEMCS3S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 88),
    _UlWLanHEMCS3S8Packets_Type()
)
ulWLanHEMCS3S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS3S8Packets.setStatus("current")
_UlWLanHEMCS4S8Packets_Type = Counter64
_UlWLanHEMCS4S8Packets_Object = MibScalar
ulWLanHEMCS4S8Packets = _UlWLanHEMCS4S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 89),
    _UlWLanHEMCS4S8Packets_Type()
)
ulWLanHEMCS4S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS4S8Packets.setStatus("current")
_UlWLanHEMCS5S8Packets_Type = Counter64
_UlWLanHEMCS5S8Packets_Object = MibScalar
ulWLanHEMCS5S8Packets = _UlWLanHEMCS5S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 90),
    _UlWLanHEMCS5S8Packets_Type()
)
ulWLanHEMCS5S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS5S8Packets.setStatus("current")
_UlWLanHEMCS6S8Packets_Type = Counter64
_UlWLanHEMCS6S8Packets_Object = MibScalar
ulWLanHEMCS6S8Packets = _UlWLanHEMCS6S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 91),
    _UlWLanHEMCS6S8Packets_Type()
)
ulWLanHEMCS6S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS6S8Packets.setStatus("current")
_UlWLanHEMCS7S8Packets_Type = Counter64
_UlWLanHEMCS7S8Packets_Object = MibScalar
ulWLanHEMCS7S8Packets = _UlWLanHEMCS7S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 92),
    _UlWLanHEMCS7S8Packets_Type()
)
ulWLanHEMCS7S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS7S8Packets.setStatus("current")
_UlWLanHEMCS8S8Packets_Type = Counter64
_UlWLanHEMCS8S8Packets_Object = MibScalar
ulWLanHEMCS8S8Packets = _UlWLanHEMCS8S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 93),
    _UlWLanHEMCS8S8Packets_Type()
)
ulWLanHEMCS8S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS8S8Packets.setStatus("current")
_UlWLanHEMCS9S8Packets_Type = Counter64
_UlWLanHEMCS9S8Packets_Object = MibScalar
ulWLanHEMCS9S8Packets = _UlWLanHEMCS9S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 94),
    _UlWLanHEMCS9S8Packets_Type()
)
ulWLanHEMCS9S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS9S8Packets.setStatus("current")
_UlWLanHEMCS10S8Packets_Type = Counter64
_UlWLanHEMCS10S8Packets_Object = MibScalar
ulWLanHEMCS10S8Packets = _UlWLanHEMCS10S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 95),
    _UlWLanHEMCS10S8Packets_Type()
)
ulWLanHEMCS10S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS10S8Packets.setStatus("current")
_UlWLanHEMCS11S8Packets_Type = Counter64
_UlWLanHEMCS11S8Packets_Object = MibScalar
ulWLanHEMCS11S8Packets = _UlWLanHEMCS11S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 96),
    _UlWLanHEMCS11S8Packets_Type()
)
ulWLanHEMCS11S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS11S8Packets.setStatus("current")
_UlWLanHEMCS12S1Packets_Type = Counter64
_UlWLanHEMCS12S1Packets_Object = MibScalar
ulWLanHEMCS12S1Packets = _UlWLanHEMCS12S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 97),
    _UlWLanHEMCS12S1Packets_Type()
)
ulWLanHEMCS12S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S1Packets.setStatus("current")
_UlWLanHEMCS13S1Packets_Type = Counter64
_UlWLanHEMCS13S1Packets_Object = MibScalar
ulWLanHEMCS13S1Packets = _UlWLanHEMCS13S1Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 98),
    _UlWLanHEMCS13S1Packets_Type()
)
ulWLanHEMCS13S1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S1Packets.setStatus("current")
_UlWLanHEMCS12S2Packets_Type = Counter64
_UlWLanHEMCS12S2Packets_Object = MibScalar
ulWLanHEMCS12S2Packets = _UlWLanHEMCS12S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 99),
    _UlWLanHEMCS12S2Packets_Type()
)
ulWLanHEMCS12S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S2Packets.setStatus("current")
_UlWLanHEMCS13S2Packets_Type = Counter64
_UlWLanHEMCS13S2Packets_Object = MibScalar
ulWLanHEMCS13S2Packets = _UlWLanHEMCS13S2Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 100),
    _UlWLanHEMCS13S2Packets_Type()
)
ulWLanHEMCS13S2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S2Packets.setStatus("current")
_UlWLanHEMCS12S3Packets_Type = Counter64
_UlWLanHEMCS12S3Packets_Object = MibScalar
ulWLanHEMCS12S3Packets = _UlWLanHEMCS12S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 101),
    _UlWLanHEMCS12S3Packets_Type()
)
ulWLanHEMCS12S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S3Packets.setStatus("current")
_UlWLanHEMCS13S3Packets_Type = Counter64
_UlWLanHEMCS13S3Packets_Object = MibScalar
ulWLanHEMCS13S3Packets = _UlWLanHEMCS13S3Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 102),
    _UlWLanHEMCS13S3Packets_Type()
)
ulWLanHEMCS13S3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S3Packets.setStatus("current")
_UlWLanHEMCS12S4Packets_Type = Counter64
_UlWLanHEMCS12S4Packets_Object = MibScalar
ulWLanHEMCS12S4Packets = _UlWLanHEMCS12S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 103),
    _UlWLanHEMCS12S4Packets_Type()
)
ulWLanHEMCS12S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S4Packets.setStatus("current")
_UlWLanHEMCS13S4Packets_Type = Counter64
_UlWLanHEMCS13S4Packets_Object = MibScalar
ulWLanHEMCS13S4Packets = _UlWLanHEMCS13S4Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 104),
    _UlWLanHEMCS13S4Packets_Type()
)
ulWLanHEMCS13S4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S4Packets.setStatus("current")
_UlWLanHEMCS12S5Packets_Type = Counter64
_UlWLanHEMCS12S5Packets_Object = MibScalar
ulWLanHEMCS12S5Packets = _UlWLanHEMCS12S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 105),
    _UlWLanHEMCS12S5Packets_Type()
)
ulWLanHEMCS12S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S5Packets.setStatus("current")
_UlWLanHEMCS13S5Packets_Type = Counter64
_UlWLanHEMCS13S5Packets_Object = MibScalar
ulWLanHEMCS13S5Packets = _UlWLanHEMCS13S5Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 106),
    _UlWLanHEMCS13S5Packets_Type()
)
ulWLanHEMCS13S5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S5Packets.setStatus("current")
_UlWLanHEMCS12S6Packets_Type = Counter64
_UlWLanHEMCS12S6Packets_Object = MibScalar
ulWLanHEMCS12S6Packets = _UlWLanHEMCS12S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 107),
    _UlWLanHEMCS12S6Packets_Type()
)
ulWLanHEMCS12S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S6Packets.setStatus("current")
_UlWLanHEMCS13S6Packets_Type = Counter64
_UlWLanHEMCS13S6Packets_Object = MibScalar
ulWLanHEMCS13S6Packets = _UlWLanHEMCS13S6Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 108),
    _UlWLanHEMCS13S6Packets_Type()
)
ulWLanHEMCS13S6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S6Packets.setStatus("current")
_UlWLanHEMCS12S7Packets_Type = Counter64
_UlWLanHEMCS12S7Packets_Object = MibScalar
ulWLanHEMCS12S7Packets = _UlWLanHEMCS12S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 109),
    _UlWLanHEMCS12S7Packets_Type()
)
ulWLanHEMCS12S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S7Packets.setStatus("current")
_UlWLanHEMCS13S7Packets_Type = Counter64
_UlWLanHEMCS13S7Packets_Object = MibScalar
ulWLanHEMCS13S7Packets = _UlWLanHEMCS13S7Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 110),
    _UlWLanHEMCS13S7Packets_Type()
)
ulWLanHEMCS13S7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S7Packets.setStatus("current")
_UlWLanHEMCS12S8Packets_Type = Counter64
_UlWLanHEMCS12S8Packets_Object = MibScalar
ulWLanHEMCS12S8Packets = _UlWLanHEMCS12S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 111),
    _UlWLanHEMCS12S8Packets_Type()
)
ulWLanHEMCS12S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS12S8Packets.setStatus("current")
_UlWLanHEMCS13S8Packets_Type = Counter64
_UlWLanHEMCS13S8Packets_Object = MibScalar
ulWLanHEMCS13S8Packets = _UlWLanHEMCS13S8Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 190, 2, 112),
    _UlWLanHEMCS13S8Packets_Type()
)
ulWLanHEMCS13S8Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanHEMCS13S8Packets.setStatus("current")
_LanSwitchPortPerfTable_Object = MibTable
lanSwitchPortPerfTable = _LanSwitchPortPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191)
)
if mibBuilder.loadTexts:
    lanSwitchPortPerfTable.setStatus("current")
_LanSwitchPortPerfEntry_Object = MibTableRow
lanSwitchPortPerfEntry = _LanSwitchPortPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1)
)
lanSwitchPortPerfEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "lanSwitchPortsNum"),
)
if mibBuilder.loadTexts:
    lanSwitchPortPerfEntry.setStatus("current")
_RxSwitchPortKBCount_Type = Counter64
_RxSwitchPortKBCount_Object = MibTableColumn
rxSwitchPortKBCount = _RxSwitchPortKBCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 1),
    _RxSwitchPortKBCount_Type()
)
rxSwitchPortKBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortKBCount.setStatus("current")
_RxSwitchPortTotalPacketCount_Type = Counter64
_RxSwitchPortTotalPacketCount_Object = MibTableColumn
rxSwitchPortTotalPacketCount = _RxSwitchPortTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 2),
    _RxSwitchPortTotalPacketCount_Type()
)
rxSwitchPortTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortTotalPacketCount.setStatus("current")
_RxSwitchPortErrorPacketCount_Type = Counter64
_RxSwitchPortErrorPacketCount_Object = MibTableColumn
rxSwitchPortErrorPacketCount = _RxSwitchPortErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 3),
    _RxSwitchPortErrorPacketCount_Type()
)
rxSwitchPortErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortErrorPacketCount.setStatus("current")
_RxSwitchPortUnicastPacketCount_Type = Counter64
_RxSwitchPortUnicastPacketCount_Object = MibTableColumn
rxSwitchPortUnicastPacketCount = _RxSwitchPortUnicastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 4),
    _RxSwitchPortUnicastPacketCount_Type()
)
rxSwitchPortUnicastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortUnicastPacketCount.setStatus("current")
_RxSwitchPortMulticastPacketCount_Type = Counter64
_RxSwitchPortMulticastPacketCount_Object = MibTableColumn
rxSwitchPortMulticastPacketCount = _RxSwitchPortMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 5),
    _RxSwitchPortMulticastPacketCount_Type()
)
rxSwitchPortMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortMulticastPacketCount.setStatus("current")
_RxSwitchPortBroadcastPacketCount_Type = Counter64
_RxSwitchPortBroadcastPacketCount_Object = MibTableColumn
rxSwitchPortBroadcastPacketCount = _RxSwitchPortBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 6),
    _RxSwitchPortBroadcastPacketCount_Type()
)
rxSwitchPortBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSwitchPortBroadcastPacketCount.setStatus("current")
_TxSwitchPortKBCount_Type = Counter64
_TxSwitchPortKBCount_Object = MibTableColumn
txSwitchPortKBCount = _TxSwitchPortKBCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 7),
    _TxSwitchPortKBCount_Type()
)
txSwitchPortKBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortKBCount.setStatus("current")
_TxSwitchPortTotalPacketCount_Type = Counter64
_TxSwitchPortTotalPacketCount_Object = MibTableColumn
txSwitchPortTotalPacketCount = _TxSwitchPortTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 8),
    _TxSwitchPortTotalPacketCount_Type()
)
txSwitchPortTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortTotalPacketCount.setStatus("current")
_TxSwitchPortErrorPacketCount_Type = Counter64
_TxSwitchPortErrorPacketCount_Object = MibTableColumn
txSwitchPortErrorPacketCount = _TxSwitchPortErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 9),
    _TxSwitchPortErrorPacketCount_Type()
)
txSwitchPortErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortErrorPacketCount.setStatus("current")
_TxSwitchPortUnicastPacketCount_Type = Counter64
_TxSwitchPortUnicastPacketCount_Object = MibTableColumn
txSwitchPortUnicastPacketCount = _TxSwitchPortUnicastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 10),
    _TxSwitchPortUnicastPacketCount_Type()
)
txSwitchPortUnicastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortUnicastPacketCount.setStatus("current")
_TxSwitchPortMulticastPacketCount_Type = Counter64
_TxSwitchPortMulticastPacketCount_Object = MibTableColumn
txSwitchPortMulticastPacketCount = _TxSwitchPortMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 11),
    _TxSwitchPortMulticastPacketCount_Type()
)
txSwitchPortMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortMulticastPacketCount.setStatus("current")
_TxSwitchPortBroadcastPacketCount_Type = Counter64
_TxSwitchPortBroadcastPacketCount_Object = MibTableColumn
txSwitchPortBroadcastPacketCount = _TxSwitchPortBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 191, 1, 12),
    _TxSwitchPortBroadcastPacketCount_Type()
)
txSwitchPortBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSwitchPortBroadcastPacketCount.setStatus("current")
_DlWLanRetransMpduPacketCount_Type = Counter64
_DlWLanRetransMpduPacketCount_Object = MibScalar
dlWLanRetransMpduPacketCount = _DlWLanRetransMpduPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 192),
    _DlWLanRetransMpduPacketCount_Type()
)
dlWLanRetransMpduPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanRetransMpduPacketCount.setStatus("current")
_UlWLanRetransMpduPacketCount_Type = Counter64
_UlWLanRetransMpduPacketCount_Object = MibScalar
ulWLanRetransMpduPacketCount = _UlWLanRetransMpduPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 193),
    _UlWLanRetransMpduPacketCount_Type()
)
ulWLanRetransMpduPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanRetransMpduPacketCount.setStatus("current")
_UlWLan2KbitCount_Type = Counter64
_UlWLan2KbitCount_Object = MibScalar
ulWLan2KbitCount = _UlWLan2KbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 237),
    _UlWLan2KbitCount_Type()
)
ulWLan2KbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2KbitCount.setStatus("current")
_DlWLan2KbitCount_Type = Counter64
_DlWLan2KbitCount_Object = MibScalar
dlWLan2KbitCount = _DlWLan2KbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 238),
    _DlWLan2KbitCount_Type()
)
dlWLan2KbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2KbitCount.setStatus("current")
_UlWLan2TotalPacketCount_Type = Counter64
_UlWLan2TotalPacketCount_Object = MibScalar
ulWLan2TotalPacketCount = _UlWLan2TotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 239),
    _UlWLan2TotalPacketCount_Type()
)
ulWLan2TotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2TotalPacketCount.setStatus("current")
_DlWLan2TotalPacketCount_Type = Counter64
_DlWLan2TotalPacketCount_Object = MibScalar
dlWLan2TotalPacketCount = _DlWLan2TotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 242),
    _DlWLan2TotalPacketCount_Type()
)
dlWLan2TotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2TotalPacketCount.setStatus("current")
_UlWLan2MultiBroadcastKbitCount_Type = Counter64
_UlWLan2MultiBroadcastKbitCount_Object = MibScalar
ulWLan2MultiBroadcastKbitCount = _UlWLan2MultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 243),
    _UlWLan2MultiBroadcastKbitCount_Type()
)
ulWLan2MultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2MultiBroadcastKbitCount.setStatus("current")
_DlWLan2MultiBroadcastKbitCount_Type = Counter64
_DlWLan2MultiBroadcastKbitCount_Object = MibScalar
dlWLan2MultiBroadcastKbitCount = _DlWLan2MultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 244),
    _DlWLan2MultiBroadcastKbitCount_Type()
)
dlWLan2MultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2MultiBroadcastKbitCount.setStatus("current")
_WLan2SessionDroppedCount_Type = Counter32
_WLan2SessionDroppedCount_Object = MibScalar
wLan2SessionDroppedCount = _WLan2SessionDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 245),
    _WLan2SessionDroppedCount_Type()
)
wLan2SessionDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SessionDroppedCount.setStatus("current")
_UlWLan2ErrorDroppedPacketCount_Type = Counter64
_UlWLan2ErrorDroppedPacketCount_Object = MibScalar
ulWLan2ErrorDroppedPacketCount = _UlWLan2ErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 247),
    _UlWLan2ErrorDroppedPacketCount_Type()
)
ulWLan2ErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2ErrorDroppedPacketCount.setStatus("current")
_DlWLan2ErrorDroppedPacketCount_Type = Counter64
_DlWLan2ErrorDroppedPacketCount_Object = MibScalar
dlWLan2ErrorDroppedPacketCount = _DlWLan2ErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 248),
    _DlWLan2ErrorDroppedPacketCount_Type()
)
dlWLan2ErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2ErrorDroppedPacketCount.setStatus("current")
_UlWLan2CapacityDroppedPacketCount_Type = Counter64
_UlWLan2CapacityDroppedPacketCount_Object = MibScalar
ulWLan2CapacityDroppedPacketCount = _UlWLan2CapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 249),
    _UlWLan2CapacityDroppedPacketCount_Type()
)
ulWLan2CapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2CapacityDroppedPacketCount.setStatus("current")
_DlWLan2CapacityDroppedPacketCount_Type = Counter64
_DlWLan2CapacityDroppedPacketCount_Object = MibScalar
dlWLan2CapacityDroppedPacketCount = _DlWLan2CapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 250),
    _DlWLan2CapacityDroppedPacketCount_Type()
)
dlWLan2CapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2CapacityDroppedPacketCount.setStatus("current")
_UlWLan2TotalAvailableFrameTimePerSecond_Type = Integer32
_UlWLan2TotalAvailableFrameTimePerSecond_Object = MibScalar
ulWLan2TotalAvailableFrameTimePerSecond = _UlWLan2TotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 251),
    _UlWLan2TotalAvailableFrameTimePerSecond_Type()
)
ulWLan2TotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2TotalAvailableFrameTimePerSecond.setStatus("current")
_DlWLan2TotalAvailableFrameTimePerSecond_Type = Integer32
_DlWLan2TotalAvailableFrameTimePerSecond_Object = MibScalar
dlWLan2TotalAvailableFrameTimePerSecond = _DlWLan2TotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 252),
    _DlWLan2TotalAvailableFrameTimePerSecond_Type()
)
dlWLan2TotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2TotalAvailableFrameTimePerSecond.setStatus("current")
_UlWLan2TotalUsedFrameTimePerSecond_Type = Integer32
_UlWLan2TotalUsedFrameTimePerSecond_Object = MibScalar
ulWLan2TotalUsedFrameTimePerSecond = _UlWLan2TotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 253),
    _UlWLan2TotalUsedFrameTimePerSecond_Type()
)
ulWLan2TotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2TotalUsedFrameTimePerSecond.setStatus("current")
_DlWLan2TotalUsedFrameTimePerSecond_Type = Integer32
_DlWLan2TotalUsedFrameTimePerSecond_Object = MibScalar
dlWLan2TotalUsedFrameTimePerSecond = _DlWLan2TotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 254),
    _DlWLan2TotalUsedFrameTimePerSecond_Type()
)
dlWLan2TotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2TotalUsedFrameTimePerSecond.setStatus("current")
_UlWLan2TotalOverheadFrameTimePerSecond_Type = Integer32
_UlWLan2TotalOverheadFrameTimePerSecond_Object = MibScalar
ulWLan2TotalOverheadFrameTimePerSecond = _UlWLan2TotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 255),
    _UlWLan2TotalOverheadFrameTimePerSecond_Type()
)
ulWLan2TotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2TotalOverheadFrameTimePerSecond.setStatus("current")
_DlWLan2TotalOverheadFrameTimePerSecond_Type = Integer32
_DlWLan2TotalOverheadFrameTimePerSecond_Object = MibScalar
dlWLan2TotalOverheadFrameTimePerSecond = _DlWLan2TotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 256),
    _DlWLan2TotalOverheadFrameTimePerSecond_Type()
)
dlWLan2TotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2TotalOverheadFrameTimePerSecond.setStatus("current")
_UlWLan2RetransPacketCount_Type = Counter64
_UlWLan2RetransPacketCount_Object = MibScalar
ulWLan2RetransPacketCount = _UlWLan2RetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 258),
    _UlWLan2RetransPacketCount_Type()
)
ulWLan2RetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2RetransPacketCount.setStatus("current")
_DlWLan2RetransPacketCount_Type = Counter64
_DlWLan2RetransPacketCount_Object = MibScalar
dlWLan2RetransPacketCount = _DlWLan2RetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 259),
    _DlWLan2RetransPacketCount_Type()
)
dlWLan2RetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2RetransPacketCount.setStatus("current")
_UlWLan2BroadcastPacketCount_Type = Counter64
_UlWLan2BroadcastPacketCount_Object = MibScalar
ulWLan2BroadcastPacketCount = _UlWLan2BroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 260),
    _UlWLan2BroadcastPacketCount_Type()
)
ulWLan2BroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2BroadcastPacketCount.setStatus("current")
_DlWLan2BroadcastPacketCount_Type = Counter64
_DlWLan2BroadcastPacketCount_Object = MibScalar
dlWLan2BroadcastPacketCount = _DlWLan2BroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 261),
    _DlWLan2BroadcastPacketCount_Type()
)
dlWLan2BroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2BroadcastPacketCount.setStatus("current")
_UlWLan2MulticastPacketCount_Type = Counter64
_UlWLan2MulticastPacketCount_Object = MibScalar
ulWLan2MulticastPacketCount = _UlWLan2MulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 262),
    _UlWLan2MulticastPacketCount_Type()
)
ulWLan2MulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2MulticastPacketCount.setStatus("current")
_DlWLan2MulticastPacketCount_Type = Counter64
_DlWLan2MulticastPacketCount_Object = MibScalar
dlWLan2MulticastPacketCount = _DlWLan2MulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 263),
    _DlWLan2MulticastPacketCount_Type()
)
dlWLan2MulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2MulticastPacketCount.setStatus("current")
_RxEtherLan2KbitCount_Type = Counter64
_RxEtherLan2KbitCount_Object = MibScalar
rxEtherLan2KbitCount = _RxEtherLan2KbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 265),
    _RxEtherLan2KbitCount_Type()
)
rxEtherLan2KbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2KbitCount.setStatus("current")
_RxEtherLan2TotalPacketCount_Type = Counter64
_RxEtherLan2TotalPacketCount_Object = MibScalar
rxEtherLan2TotalPacketCount = _RxEtherLan2TotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 266),
    _RxEtherLan2TotalPacketCount_Type()
)
rxEtherLan2TotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2TotalPacketCount.setStatus("current")
_RxEtherLan2ErrorPacketCount_Type = Counter64
_RxEtherLan2ErrorPacketCount_Object = MibScalar
rxEtherLan2ErrorPacketCount = _RxEtherLan2ErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 267),
    _RxEtherLan2ErrorPacketCount_Type()
)
rxEtherLan2ErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2ErrorPacketCount.setStatus("current")
_RxEtherLan2DroppedPacketCount_Type = Counter64
_RxEtherLan2DroppedPacketCount_Object = MibScalar
rxEtherLan2DroppedPacketCount = _RxEtherLan2DroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 268),
    _RxEtherLan2DroppedPacketCount_Type()
)
rxEtherLan2DroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2DroppedPacketCount.setStatus("current")
_RxEtherLan2MulticastPacketCount_Type = Counter64
_RxEtherLan2MulticastPacketCount_Object = MibScalar
rxEtherLan2MulticastPacketCount = _RxEtherLan2MulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 269),
    _RxEtherLan2MulticastPacketCount_Type()
)
rxEtherLan2MulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2MulticastPacketCount.setStatus("current")
_RxEtherLan2BroadcastPacketCount_Type = Counter64
_RxEtherLan2BroadcastPacketCount_Object = MibScalar
rxEtherLan2BroadcastPacketCount = _RxEtherLan2BroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 270),
    _RxEtherLan2BroadcastPacketCount_Type()
)
rxEtherLan2BroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2BroadcastPacketCount.setStatus("current")
_RxEtherLan2MultiBroadcastKbitCount_Type = Counter64
_RxEtherLan2MultiBroadcastKbitCount_Object = MibScalar
rxEtherLan2MultiBroadcastKbitCount = _RxEtherLan2MultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 271),
    _RxEtherLan2MultiBroadcastKbitCount_Type()
)
rxEtherLan2MultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLan2MultiBroadcastKbitCount.setStatus("current")
_TxEtherLan2KbitCount_Type = Counter64
_TxEtherLan2KbitCount_Object = MibScalar
txEtherLan2KbitCount = _TxEtherLan2KbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 272),
    _TxEtherLan2KbitCount_Type()
)
txEtherLan2KbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2KbitCount.setStatus("current")
_TxEtherLan2TotalPacketCount_Type = Counter64
_TxEtherLan2TotalPacketCount_Object = MibScalar
txEtherLan2TotalPacketCount = _TxEtherLan2TotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 273),
    _TxEtherLan2TotalPacketCount_Type()
)
txEtherLan2TotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2TotalPacketCount.setStatus("current")
_TxEtherLan2ErrorPacketCount_Type = Counter64
_TxEtherLan2ErrorPacketCount_Object = MibScalar
txEtherLan2ErrorPacketCount = _TxEtherLan2ErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 274),
    _TxEtherLan2ErrorPacketCount_Type()
)
txEtherLan2ErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2ErrorPacketCount.setStatus("current")
_TxEtherLan2DroppedPacketCount_Type = Counter64
_TxEtherLan2DroppedPacketCount_Object = MibScalar
txEtherLan2DroppedPacketCount = _TxEtherLan2DroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 275),
    _TxEtherLan2DroppedPacketCount_Type()
)
txEtherLan2DroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2DroppedPacketCount.setStatus("current")
_TxEtherLan2MulticastPacketCount_Type = Counter64
_TxEtherLan2MulticastPacketCount_Object = MibScalar
txEtherLan2MulticastPacketCount = _TxEtherLan2MulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 276),
    _TxEtherLan2MulticastPacketCount_Type()
)
txEtherLan2MulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2MulticastPacketCount.setStatus("current")
_TxEtherLan2BroadcastPacketCount_Type = Counter64
_TxEtherLan2BroadcastPacketCount_Object = MibScalar
txEtherLan2BroadcastPacketCount = _TxEtherLan2BroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 277),
    _TxEtherLan2BroadcastPacketCount_Type()
)
txEtherLan2BroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2BroadcastPacketCount.setStatus("current")
_TxEtherLan2MultiBroadcastKbitCount_Type = Counter64
_TxEtherLan2MultiBroadcastKbitCount_Object = MibScalar
txEtherLan2MultiBroadcastKbitCount = _TxEtherLan2MultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 278),
    _TxEtherLan2MultiBroadcastKbitCount_Type()
)
txEtherLan2MultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLan2MultiBroadcastKbitCount.setStatus("current")
_UlWLan2TotalAvailableFrameTimePercentage_Type = Integer32
_UlWLan2TotalAvailableFrameTimePercentage_Object = MibScalar
ulWLan2TotalAvailableFrameTimePercentage = _UlWLan2TotalAvailableFrameTimePercentage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 312),
    _UlWLan2TotalAvailableFrameTimePercentage_Type()
)
ulWLan2TotalAvailableFrameTimePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2TotalAvailableFrameTimePercentage.setStatus("current")
_DlWLan2TotalAvailableFrameTimePercentage_Type = Integer32
_DlWLan2TotalAvailableFrameTimePercentage_Object = MibScalar
dlWLan2TotalAvailableFrameTimePercentage = _DlWLan2TotalAvailableFrameTimePercentage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 313),
    _DlWLan2TotalAvailableFrameTimePercentage_Type()
)
dlWLan2TotalAvailableFrameTimePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2TotalAvailableFrameTimePercentage.setStatus("current")
_UlWLan2VHTMCS0SSPackets_Type = Counter64
_UlWLan2VHTMCS0SSPackets_Object = MibScalar
ulWLan2VHTMCS0SSPackets = _UlWLan2VHTMCS0SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 330),
    _UlWLan2VHTMCS0SSPackets_Type()
)
ulWLan2VHTMCS0SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS0SSPackets.setStatus("current")
_UlWLan2VHTMCS1SSPackets_Type = Counter64
_UlWLan2VHTMCS1SSPackets_Object = MibScalar
ulWLan2VHTMCS1SSPackets = _UlWLan2VHTMCS1SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 331),
    _UlWLan2VHTMCS1SSPackets_Type()
)
ulWLan2VHTMCS1SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS1SSPackets.setStatus("current")
_UlWLan2VHTMCS2SSPackets_Type = Counter64
_UlWLan2VHTMCS2SSPackets_Object = MibScalar
ulWLan2VHTMCS2SSPackets = _UlWLan2VHTMCS2SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 332),
    _UlWLan2VHTMCS2SSPackets_Type()
)
ulWLan2VHTMCS2SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS2SSPackets.setStatus("current")
_UlWLan2VHTMCS3SSPackets_Type = Counter64
_UlWLan2VHTMCS3SSPackets_Object = MibScalar
ulWLan2VHTMCS3SSPackets = _UlWLan2VHTMCS3SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 333),
    _UlWLan2VHTMCS3SSPackets_Type()
)
ulWLan2VHTMCS3SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS3SSPackets.setStatus("current")
_UlWLan2VHTMCS4SSPackets_Type = Counter64
_UlWLan2VHTMCS4SSPackets_Object = MibScalar
ulWLan2VHTMCS4SSPackets = _UlWLan2VHTMCS4SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 334),
    _UlWLan2VHTMCS4SSPackets_Type()
)
ulWLan2VHTMCS4SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS4SSPackets.setStatus("current")
_UlWLan2VHTMCS5SSPackets_Type = Counter64
_UlWLan2VHTMCS5SSPackets_Object = MibScalar
ulWLan2VHTMCS5SSPackets = _UlWLan2VHTMCS5SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 335),
    _UlWLan2VHTMCS5SSPackets_Type()
)
ulWLan2VHTMCS5SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS5SSPackets.setStatus("current")
_UlWLan2VHTMCS6SSPackets_Type = Counter64
_UlWLan2VHTMCS6SSPackets_Object = MibScalar
ulWLan2VHTMCS6SSPackets = _UlWLan2VHTMCS6SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 336),
    _UlWLan2VHTMCS6SSPackets_Type()
)
ulWLan2VHTMCS6SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS6SSPackets.setStatus("current")
_UlWLan2VHTMCS7SSPackets_Type = Counter64
_UlWLan2VHTMCS7SSPackets_Object = MibScalar
ulWLan2VHTMCS7SSPackets = _UlWLan2VHTMCS7SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 337),
    _UlWLan2VHTMCS7SSPackets_Type()
)
ulWLan2VHTMCS7SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS7SSPackets.setStatus("current")
_UlWLan2VHTMCS8SSPackets_Type = Counter64
_UlWLan2VHTMCS8SSPackets_Object = MibScalar
ulWLan2VHTMCS8SSPackets = _UlWLan2VHTMCS8SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 338),
    _UlWLan2VHTMCS8SSPackets_Type()
)
ulWLan2VHTMCS8SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS8SSPackets.setStatus("current")
_UlWLan2VHTMCS9SSPackets_Type = Counter64
_UlWLan2VHTMCS9SSPackets_Object = MibScalar
ulWLan2VHTMCS9SSPackets = _UlWLan2VHTMCS9SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 339),
    _UlWLan2VHTMCS9SSPackets_Type()
)
ulWLan2VHTMCS9SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS9SSPackets.setStatus("current")
_UlWLan2VHTMCS0DSPackets_Type = Counter64
_UlWLan2VHTMCS0DSPackets_Object = MibScalar
ulWLan2VHTMCS0DSPackets = _UlWLan2VHTMCS0DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 340),
    _UlWLan2VHTMCS0DSPackets_Type()
)
ulWLan2VHTMCS0DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS0DSPackets.setStatus("current")
_UlWLan2VHTMCS1DSPackets_Type = Counter64
_UlWLan2VHTMCS1DSPackets_Object = MibScalar
ulWLan2VHTMCS1DSPackets = _UlWLan2VHTMCS1DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 341),
    _UlWLan2VHTMCS1DSPackets_Type()
)
ulWLan2VHTMCS1DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS1DSPackets.setStatus("current")
_UlWLan2VHTMCS2DSPackets_Type = Counter64
_UlWLan2VHTMCS2DSPackets_Object = MibScalar
ulWLan2VHTMCS2DSPackets = _UlWLan2VHTMCS2DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 342),
    _UlWLan2VHTMCS2DSPackets_Type()
)
ulWLan2VHTMCS2DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS2DSPackets.setStatus("current")
_UlWLan2VHTMCS3DSPackets_Type = Counter64
_UlWLan2VHTMCS3DSPackets_Object = MibScalar
ulWLan2VHTMCS3DSPackets = _UlWLan2VHTMCS3DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 343),
    _UlWLan2VHTMCS3DSPackets_Type()
)
ulWLan2VHTMCS3DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS3DSPackets.setStatus("current")
_UlWLan2VHTMCS4DSPackets_Type = Counter64
_UlWLan2VHTMCS4DSPackets_Object = MibScalar
ulWLan2VHTMCS4DSPackets = _UlWLan2VHTMCS4DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 344),
    _UlWLan2VHTMCS4DSPackets_Type()
)
ulWLan2VHTMCS4DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS4DSPackets.setStatus("current")
_UlWLan2VHTMCS5DSPackets_Type = Counter64
_UlWLan2VHTMCS5DSPackets_Object = MibScalar
ulWLan2VHTMCS5DSPackets = _UlWLan2VHTMCS5DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 345),
    _UlWLan2VHTMCS5DSPackets_Type()
)
ulWLan2VHTMCS5DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS5DSPackets.setStatus("current")
_UlWLan2VHTMCS6DSPackets_Type = Counter64
_UlWLan2VHTMCS6DSPackets_Object = MibScalar
ulWLan2VHTMCS6DSPackets = _UlWLan2VHTMCS6DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 346),
    _UlWLan2VHTMCS6DSPackets_Type()
)
ulWLan2VHTMCS6DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS6DSPackets.setStatus("current")
_UlWLan2VHTMCS7DSPackets_Type = Counter64
_UlWLan2VHTMCS7DSPackets_Object = MibScalar
ulWLan2VHTMCS7DSPackets = _UlWLan2VHTMCS7DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 347),
    _UlWLan2VHTMCS7DSPackets_Type()
)
ulWLan2VHTMCS7DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS7DSPackets.setStatus("current")
_UlWLan2VHTMCS8DSPackets_Type = Counter64
_UlWLan2VHTMCS8DSPackets_Object = MibScalar
ulWLan2VHTMCS8DSPackets = _UlWLan2VHTMCS8DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 348),
    _UlWLan2VHTMCS8DSPackets_Type()
)
ulWLan2VHTMCS8DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS8DSPackets.setStatus("current")
_UlWLan2VHTMCS9DSPackets_Type = Counter64
_UlWLan2VHTMCS9DSPackets_Object = MibScalar
ulWLan2VHTMCS9DSPackets = _UlWLan2VHTMCS9DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 349),
    _UlWLan2VHTMCS9DSPackets_Type()
)
ulWLan2VHTMCS9DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLan2VHTMCS9DSPackets.setStatus("current")
_DlWLan2VHTMCS0SSPackets_Type = Counter64
_DlWLan2VHTMCS0SSPackets_Object = MibScalar
dlWLan2VHTMCS0SSPackets = _DlWLan2VHTMCS0SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 350),
    _DlWLan2VHTMCS0SSPackets_Type()
)
dlWLan2VHTMCS0SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS0SSPackets.setStatus("current")
_DlWLan2VHTMCS1SSPackets_Type = Counter64
_DlWLan2VHTMCS1SSPackets_Object = MibScalar
dlWLan2VHTMCS1SSPackets = _DlWLan2VHTMCS1SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 351),
    _DlWLan2VHTMCS1SSPackets_Type()
)
dlWLan2VHTMCS1SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS1SSPackets.setStatus("current")
_DlWLan2VHTMCS2SSPackets_Type = Counter64
_DlWLan2VHTMCS2SSPackets_Object = MibScalar
dlWLan2VHTMCS2SSPackets = _DlWLan2VHTMCS2SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 352),
    _DlWLan2VHTMCS2SSPackets_Type()
)
dlWLan2VHTMCS2SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS2SSPackets.setStatus("current")
_DlWLan2VHTMCS3SSPackets_Type = Counter64
_DlWLan2VHTMCS3SSPackets_Object = MibScalar
dlWLan2VHTMCS3SSPackets = _DlWLan2VHTMCS3SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 353),
    _DlWLan2VHTMCS3SSPackets_Type()
)
dlWLan2VHTMCS3SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS3SSPackets.setStatus("current")
_DlWLan2VHTMCS4SSPackets_Type = Counter64
_DlWLan2VHTMCS4SSPackets_Object = MibScalar
dlWLan2VHTMCS4SSPackets = _DlWLan2VHTMCS4SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 354),
    _DlWLan2VHTMCS4SSPackets_Type()
)
dlWLan2VHTMCS4SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS4SSPackets.setStatus("current")
_DlWLan2VHTMCS5SSPackets_Type = Counter64
_DlWLan2VHTMCS5SSPackets_Object = MibScalar
dlWLan2VHTMCS5SSPackets = _DlWLan2VHTMCS5SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 355),
    _DlWLan2VHTMCS5SSPackets_Type()
)
dlWLan2VHTMCS5SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS5SSPackets.setStatus("current")
_DlWLan2VHTMCS6SSPackets_Type = Counter64
_DlWLan2VHTMCS6SSPackets_Object = MibScalar
dlWLan2VHTMCS6SSPackets = _DlWLan2VHTMCS6SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 356),
    _DlWLan2VHTMCS6SSPackets_Type()
)
dlWLan2VHTMCS6SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS6SSPackets.setStatus("current")
_DlWLan2VHTMCS7SSPackets_Type = Counter64
_DlWLan2VHTMCS7SSPackets_Object = MibScalar
dlWLan2VHTMCS7SSPackets = _DlWLan2VHTMCS7SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 357),
    _DlWLan2VHTMCS7SSPackets_Type()
)
dlWLan2VHTMCS7SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS7SSPackets.setStatus("current")
_DlWLan2VHTMCS8SSPackets_Type = Counter64
_DlWLan2VHTMCS8SSPackets_Object = MibScalar
dlWLan2VHTMCS8SSPackets = _DlWLan2VHTMCS8SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 358),
    _DlWLan2VHTMCS8SSPackets_Type()
)
dlWLan2VHTMCS8SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS8SSPackets.setStatus("current")
_DlWLan2VHTMCS9SSPackets_Type = Counter64
_DlWLan2VHTMCS9SSPackets_Object = MibScalar
dlWLan2VHTMCS9SSPackets = _DlWLan2VHTMCS9SSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 359),
    _DlWLan2VHTMCS9SSPackets_Type()
)
dlWLan2VHTMCS9SSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS9SSPackets.setStatus("current")
_DlWLan2VHTMCS0DSPackets_Type = Counter64
_DlWLan2VHTMCS0DSPackets_Object = MibScalar
dlWLan2VHTMCS0DSPackets = _DlWLan2VHTMCS0DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 360),
    _DlWLan2VHTMCS0DSPackets_Type()
)
dlWLan2VHTMCS0DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS0DSPackets.setStatus("current")
_DlWLan2VHTMCS1DSPackets_Type = Counter64
_DlWLan2VHTMCS1DSPackets_Object = MibScalar
dlWLan2VHTMCS1DSPackets = _DlWLan2VHTMCS1DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 361),
    _DlWLan2VHTMCS1DSPackets_Type()
)
dlWLan2VHTMCS1DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS1DSPackets.setStatus("current")
_DlWLan2VHTMCS2DSPackets_Type = Counter64
_DlWLan2VHTMCS2DSPackets_Object = MibScalar
dlWLan2VHTMCS2DSPackets = _DlWLan2VHTMCS2DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 362),
    _DlWLan2VHTMCS2DSPackets_Type()
)
dlWLan2VHTMCS2DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS2DSPackets.setStatus("current")
_DlWLan2VHTMCS3DSPackets_Type = Counter64
_DlWLan2VHTMCS3DSPackets_Object = MibScalar
dlWLan2VHTMCS3DSPackets = _DlWLan2VHTMCS3DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 363),
    _DlWLan2VHTMCS3DSPackets_Type()
)
dlWLan2VHTMCS3DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS3DSPackets.setStatus("current")
_DlWLan2VHTMCS4DSPackets_Type = Counter64
_DlWLan2VHTMCS4DSPackets_Object = MibScalar
dlWLan2VHTMCS4DSPackets = _DlWLan2VHTMCS4DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 364),
    _DlWLan2VHTMCS4DSPackets_Type()
)
dlWLan2VHTMCS4DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS4DSPackets.setStatus("current")
_DlWLan2VHTMCS5DSPackets_Type = Counter64
_DlWLan2VHTMCS5DSPackets_Object = MibScalar
dlWLan2VHTMCS5DSPackets = _DlWLan2VHTMCS5DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 365),
    _DlWLan2VHTMCS5DSPackets_Type()
)
dlWLan2VHTMCS5DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS5DSPackets.setStatus("current")
_DlWLan2VHTMCS6DSPackets_Type = Counter64
_DlWLan2VHTMCS6DSPackets_Object = MibScalar
dlWLan2VHTMCS6DSPackets = _DlWLan2VHTMCS6DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 366),
    _DlWLan2VHTMCS6DSPackets_Type()
)
dlWLan2VHTMCS6DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS6DSPackets.setStatus("current")
_DlWLan2VHTMCS7DSPackets_Type = Counter64
_DlWLan2VHTMCS7DSPackets_Object = MibScalar
dlWLan2VHTMCS7DSPackets = _DlWLan2VHTMCS7DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 367),
    _DlWLan2VHTMCS7DSPackets_Type()
)
dlWLan2VHTMCS7DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS7DSPackets.setStatus("current")
_DlWLan2VHTMCS8DSPackets_Type = Counter64
_DlWLan2VHTMCS8DSPackets_Object = MibScalar
dlWLan2VHTMCS8DSPackets = _DlWLan2VHTMCS8DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 368),
    _DlWLan2VHTMCS8DSPackets_Type()
)
dlWLan2VHTMCS8DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS8DSPackets.setStatus("current")
_DlWLan2VHTMCS9DSPackets_Type = Counter64
_DlWLan2VHTMCS9DSPackets_Object = MibScalar
dlWLan2VHTMCS9DSPackets = _DlWLan2VHTMCS9DSPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 369),
    _DlWLan2VHTMCS9DSPackets_Type()
)
dlWLan2VHTMCS9DSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLan2VHTMCS9DSPackets.setStatus("current")
_WLan2SNRDeviation00Cnt_Type = Counter64
_WLan2SNRDeviation00Cnt_Object = MibScalar
wLan2SNRDeviation00Cnt = _WLan2SNRDeviation00Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 370),
    _WLan2SNRDeviation00Cnt_Type()
)
wLan2SNRDeviation00Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation00Cnt.setStatus("current")
_WLan2SNRDeviation01Cnt_Type = Counter64
_WLan2SNRDeviation01Cnt_Object = MibScalar
wLan2SNRDeviation01Cnt = _WLan2SNRDeviation01Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 371),
    _WLan2SNRDeviation01Cnt_Type()
)
wLan2SNRDeviation01Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation01Cnt.setStatus("current")
_WLan2SNRDeviation02Cnt_Type = Counter64
_WLan2SNRDeviation02Cnt_Object = MibScalar
wLan2SNRDeviation02Cnt = _WLan2SNRDeviation02Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 372),
    _WLan2SNRDeviation02Cnt_Type()
)
wLan2SNRDeviation02Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation02Cnt.setStatus("current")
_WLan2SNRDeviation03Cnt_Type = Counter64
_WLan2SNRDeviation03Cnt_Object = MibScalar
wLan2SNRDeviation03Cnt = _WLan2SNRDeviation03Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 373),
    _WLan2SNRDeviation03Cnt_Type()
)
wLan2SNRDeviation03Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation03Cnt.setStatus("current")
_WLan2SNRDeviation04Cnt_Type = Counter64
_WLan2SNRDeviation04Cnt_Object = MibScalar
wLan2SNRDeviation04Cnt = _WLan2SNRDeviation04Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 374),
    _WLan2SNRDeviation04Cnt_Type()
)
wLan2SNRDeviation04Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation04Cnt.setStatus("current")
_WLan2SNRDeviation05Cnt_Type = Counter64
_WLan2SNRDeviation05Cnt_Object = MibScalar
wLan2SNRDeviation05Cnt = _WLan2SNRDeviation05Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 375),
    _WLan2SNRDeviation05Cnt_Type()
)
wLan2SNRDeviation05Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation05Cnt.setStatus("current")
_WLan2SNRDeviation06Cnt_Type = Counter64
_WLan2SNRDeviation06Cnt_Object = MibScalar
wLan2SNRDeviation06Cnt = _WLan2SNRDeviation06Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 376),
    _WLan2SNRDeviation06Cnt_Type()
)
wLan2SNRDeviation06Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation06Cnt.setStatus("current")
_WLan2SNRDeviation07Cnt_Type = Counter64
_WLan2SNRDeviation07Cnt_Object = MibScalar
wLan2SNRDeviation07Cnt = _WLan2SNRDeviation07Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 377),
    _WLan2SNRDeviation07Cnt_Type()
)
wLan2SNRDeviation07Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation07Cnt.setStatus("current")
_WLan2SNRDeviation08Cnt_Type = Counter64
_WLan2SNRDeviation08Cnt_Object = MibScalar
wLan2SNRDeviation08Cnt = _WLan2SNRDeviation08Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 378),
    _WLan2SNRDeviation08Cnt_Type()
)
wLan2SNRDeviation08Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation08Cnt.setStatus("current")
_WLan2SNRDeviation09Cnt_Type = Counter64
_WLan2SNRDeviation09Cnt_Object = MibScalar
wLan2SNRDeviation09Cnt = _WLan2SNRDeviation09Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 379),
    _WLan2SNRDeviation09Cnt_Type()
)
wLan2SNRDeviation09Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation09Cnt.setStatus("current")
_WLan2SNRDeviation10Cnt_Type = Counter64
_WLan2SNRDeviation10Cnt_Object = MibScalar
wLan2SNRDeviation10Cnt = _WLan2SNRDeviation10Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 380),
    _WLan2SNRDeviation10Cnt_Type()
)
wLan2SNRDeviation10Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation10Cnt.setStatus("current")
_WLan2SNRDeviation11Cnt_Type = Counter64
_WLan2SNRDeviation11Cnt_Object = MibScalar
wLan2SNRDeviation11Cnt = _WLan2SNRDeviation11Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 381),
    _WLan2SNRDeviation11Cnt_Type()
)
wLan2SNRDeviation11Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation11Cnt.setStatus("current")
_WLan2SNRDeviation12Cnt_Type = Counter64
_WLan2SNRDeviation12Cnt_Object = MibScalar
wLan2SNRDeviation12Cnt = _WLan2SNRDeviation12Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 382),
    _WLan2SNRDeviation12Cnt_Type()
)
wLan2SNRDeviation12Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation12Cnt.setStatus("current")
_WLan2SNRDeviation13Cnt_Type = Counter64
_WLan2SNRDeviation13Cnt_Object = MibScalar
wLan2SNRDeviation13Cnt = _WLan2SNRDeviation13Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 383),
    _WLan2SNRDeviation13Cnt_Type()
)
wLan2SNRDeviation13Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation13Cnt.setStatus("current")
_WLan2SNRDeviation14Cnt_Type = Counter64
_WLan2SNRDeviation14Cnt_Object = MibScalar
wLan2SNRDeviation14Cnt = _WLan2SNRDeviation14Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 384),
    _WLan2SNRDeviation14Cnt_Type()
)
wLan2SNRDeviation14Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation14Cnt.setStatus("current")
_WLan2SNRDeviation15Cnt_Type = Counter64
_WLan2SNRDeviation15Cnt_Object = MibScalar
wLan2SNRDeviation15Cnt = _WLan2SNRDeviation15Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 385),
    _WLan2SNRDeviation15Cnt_Type()
)
wLan2SNRDeviation15Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation15Cnt.setStatus("current")
_WLan2SNRDeviation16Cnt_Type = Counter64
_WLan2SNRDeviation16Cnt_Object = MibScalar
wLan2SNRDeviation16Cnt = _WLan2SNRDeviation16Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 386),
    _WLan2SNRDeviation16Cnt_Type()
)
wLan2SNRDeviation16Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation16Cnt.setStatus("current")
_WLan2SNRDeviation17Cnt_Type = Counter64
_WLan2SNRDeviation17Cnt_Object = MibScalar
wLan2SNRDeviation17Cnt = _WLan2SNRDeviation17Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 387),
    _WLan2SNRDeviation17Cnt_Type()
)
wLan2SNRDeviation17Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation17Cnt.setStatus("current")
_WLan2SNRDeviation18Cnt_Type = Counter64
_WLan2SNRDeviation18Cnt_Object = MibScalar
wLan2SNRDeviation18Cnt = _WLan2SNRDeviation18Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 388),
    _WLan2SNRDeviation18Cnt_Type()
)
wLan2SNRDeviation18Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation18Cnt.setStatus("current")
_WLan2SNRDeviation19Cnt_Type = Counter64
_WLan2SNRDeviation19Cnt_Object = MibScalar
wLan2SNRDeviation19Cnt = _WLan2SNRDeviation19Cnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 389),
    _WLan2SNRDeviation19Cnt_Type()
)
wLan2SNRDeviation19Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLan2SNRDeviation19Cnt.setStatus("current")
_CambiumRealTimeStatsMonitoring_ObjectIdentity = ObjectIdentity
cambiumRealTimeStatsMonitoring = _CambiumRealTimeStatsMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 2)
)
_CambiumAdvancedPerformanceMonitoring_ObjectIdentity = ObjectIdentity
cambiumAdvancedPerformanceMonitoring = _CambiumAdvancedPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 3)
)
_Cambiumpmp80211SystemConfiguration_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemConfiguration = _Cambiumpmp80211SystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3)
)
_CambiumSystemLog_ObjectIdentity = ObjectIdentity
cambiumSystemLog = _CambiumSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1)
)
_SyslogServerIPFirst_Type = IpAddress
_SyslogServerIPFirst_Object = MibScalar
syslogServerIPFirst = _SyslogServerIPFirst_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 1),
    _SyslogServerIPFirst_Type()
)
syslogServerIPFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPFirst.setStatus("current")
_SyslogServerIPSecond_Type = IpAddress
_SyslogServerIPSecond_Object = MibScalar
syslogServerIPSecond = _SyslogServerIPSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 2),
    _SyslogServerIPSecond_Type()
)
syslogServerIPSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPSecond.setStatus("current")
_SyslogServerIPThird_Type = IpAddress
_SyslogServerIPThird_Object = MibScalar
syslogServerIPThird = _SyslogServerIPThird_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 3),
    _SyslogServerIPThird_Type()
)
syslogServerIPThird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPThird.setStatus("current")
_SyslogServerIPFourth_Type = IpAddress
_SyslogServerIPFourth_Object = MibScalar
syslogServerIPFourth = _SyslogServerIPFourth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 4),
    _SyslogServerIPFourth_Type()
)
syslogServerIPFourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPFourth.setStatus("current")


class _SyslogServerLogToWeb_Type(Integer32):
    """Custom type syslogServerLogToWeb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SyslogServerLogToWeb_Type.__name__ = "Integer32"
_SyslogServerLogToWeb_Object = MibScalar
syslogServerLogToWeb = _SyslogServerLogToWeb_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 5),
    _SyslogServerLogToWeb_Type()
)
syslogServerLogToWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogToWeb.setStatus("current")


class _SyslogServerLogMask_Type(Integer32):
    """Custom type syslogServerLogMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SyslogServerLogMask_Type.__name__ = "Integer32"
_SyslogServerLogMask_Object = MibScalar
syslogServerLogMask = _SyslogServerLogMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 6),
    _SyslogServerLogMask_Type()
)
syslogServerLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogMask.setStatus("current")


class _SyslogServerLogDA_Type(Integer32):
    """Custom type syslogServerLogDA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SyslogServerLogDA_Type.__name__ = "Integer32"
_SyslogServerLogDA_Object = MibScalar
syslogServerLogDA = _SyslogServerLogDA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 7),
    _SyslogServerLogDA_Type()
)
syslogServerLogDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogDA.setStatus("current")


class _SyslogServerLogCLISH_Type(Integer32):
    """Custom type syslogServerLogCLISH based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SyslogServerLogCLISH_Type.__name__ = "Integer32"
_SyslogServerLogCLISH_Object = MibScalar
syslogServerLogCLISH = _SyslogServerLogCLISH_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 8),
    _SyslogServerLogCLISH_Type()
)
syslogServerLogCLISH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogCLISH.setStatus("current")


class _SyslogServerPortFirst_Type(Integer32):
    """Custom type syslogServerPortFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogServerPortFirst_Type.__name__ = "Integer32"
_SyslogServerPortFirst_Object = MibScalar
syslogServerPortFirst = _SyslogServerPortFirst_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 11),
    _SyslogServerPortFirst_Type()
)
syslogServerPortFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPortFirst.setStatus("current")


class _SyslogServerPortSecond_Type(Integer32):
    """Custom type syslogServerPortSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogServerPortSecond_Type.__name__ = "Integer32"
_SyslogServerPortSecond_Object = MibScalar
syslogServerPortSecond = _SyslogServerPortSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 12),
    _SyslogServerPortSecond_Type()
)
syslogServerPortSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPortSecond.setStatus("current")


class _SyslogServerPortThird_Type(Integer32):
    """Custom type syslogServerPortThird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogServerPortThird_Type.__name__ = "Integer32"
_SyslogServerPortThird_Object = MibScalar
syslogServerPortThird = _SyslogServerPortThird_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 13),
    _SyslogServerPortThird_Type()
)
syslogServerPortThird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPortThird.setStatus("current")


class _SyslogServerPortFourth_Type(Integer32):
    """Custom type syslogServerPortFourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogServerPortFourth_Type.__name__ = "Integer32"
_SyslogServerPortFourth_Object = MibScalar
syslogServerPortFourth = _SyslogServerPortFourth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 14),
    _SyslogServerPortFourth_Type()
)
syslogServerPortFourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPortFourth.setStatus("current")
_CambiumDHCP_ObjectIdentity = ObjectIdentity
cambiumDHCP = _CambiumDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2)
)


class _DhcpLanEnable_Type(Integer32):
    """Custom type dhcpLanEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DhcpLanEnable_Type.__name__ = "Integer32"
_DhcpLanEnable_Object = MibScalar
dhcpLanEnable = _DhcpLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 1),
    _DhcpLanEnable_Type()
)
dhcpLanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanEnable.setStatus("current")


class _DhcpLanStart_Type(Integer32):
    """Custom type dhcpLanStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpLanStart_Type.__name__ = "Integer32"
_DhcpLanStart_Object = MibScalar
dhcpLanStart = _DhcpLanStart_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 2),
    _DhcpLanStart_Type()
)
dhcpLanStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanStart.setStatus("current")


class _DhcpLanLimit_Type(Integer32):
    """Custom type dhcpLanLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpLanLimit_Type.__name__ = "Integer32"
_DhcpLanLimit_Object = MibScalar
dhcpLanLimit = _DhcpLanLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 3),
    _DhcpLanLimit_Type()
)
dhcpLanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanLimit.setStatus("current")


class _DhcpLanLeasetime_Type(Integer32):
    """Custom type dhcpLanLeasetime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_DhcpLanLeasetime_Type.__name__ = "Integer32"
_DhcpLanLeasetime_Object = MibScalar
dhcpLanLeasetime = _DhcpLanLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 4),
    _DhcpLanLeasetime_Type()
)
dhcpLanLeasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanLeasetime.setStatus("current")
_DhcpLanHostTable_Object = MibTable
dhcpLanHostTable = _DhcpLanHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5)
)
if mibBuilder.loadTexts:
    dhcpLanHostTable.setStatus("current")
_DhcpLanHostEntry_Object = MibTableRow
dhcpLanHostEntry = _DhcpLanHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1)
)
dhcpLanHostEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpLanHostIndex"),
)
if mibBuilder.loadTexts:
    dhcpLanHostEntry.setStatus("current")


class _DhcpLanHostIndex_Type(Integer32):
    """Custom type dhcpLanHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DhcpLanHostIndex_Type.__name__ = "Integer32"
_DhcpLanHostIndex_Object = MibTableColumn
dhcpLanHostIndex = _DhcpLanHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 1),
    _DhcpLanHostIndex_Type()
)
dhcpLanHostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostIndex.setStatus("current")
_DhcpLanHostIP_Type = IpAddress
_DhcpLanHostIP_Object = MibTableColumn
dhcpLanHostIP = _DhcpLanHostIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 2),
    _DhcpLanHostIP_Type()
)
dhcpLanHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostIP.setStatus("current")


class _DhcpLanHostMAC_Type(DisplayString):
    """Custom type dhcpLanHostMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpLanHostMAC_Type.__name__ = "DisplayString"
_DhcpLanHostMAC_Object = MibTableColumn
dhcpLanHostMAC = _DhcpLanHostMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 3),
    _DhcpLanHostMAC_Type()
)
dhcpLanHostMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostMAC.setStatus("current")


class _DhcpLanHostName_Type(DisplayString):
    """Custom type dhcpLanHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_DhcpLanHostName_Type.__name__ = "DisplayString"
_DhcpLanHostName_Object = MibTableColumn
dhcpLanHostName = _DhcpLanHostName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 4),
    _DhcpLanHostName_Type()
)
dhcpLanHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostName.setStatus("current")


class _DhcpOption82_Type(Integer32):
    """Custom type dhcpOption82 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DhcpOption82_Type.__name__ = "Integer32"
_DhcpOption82_Object = MibScalar
dhcpOption82 = _DhcpOption82_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 6),
    _DhcpOption82_Type()
)
dhcpOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82.setStatus("current")


class _DhcpOption66_Type(Integer32):
    """Custom type dhcpOption66 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DhcpOption66_Type.__name__ = "Integer32"
_DhcpOption66_Object = MibScalar
dhcpOption66 = _DhcpOption66_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 7),
    _DhcpOption66_Type()
)
dhcpOption66.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption66.setStatus("current")


class _DhcpOption82CircuitIDType_Type(Integer32):
    """Custom type dhcpOption82CircuitIDType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DhcpOption82CircuitIDType_Type.__name__ = "Integer32"
_DhcpOption82CircuitIDType_Object = MibScalar
dhcpOption82CircuitIDType = _DhcpOption82CircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 8),
    _DhcpOption82CircuitIDType_Type()
)
dhcpOption82CircuitIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82CircuitIDType.setStatus("current")


class _DhcpOption82CircuitValue_Type(DisplayString):
    """Custom type dhcpOption82CircuitValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 31),
    )


_DhcpOption82CircuitValue_Type.__name__ = "DisplayString"
_DhcpOption82CircuitValue_Object = MibScalar
dhcpOption82CircuitValue = _DhcpOption82CircuitValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 9),
    _DhcpOption82CircuitValue_Type()
)
dhcpOption82CircuitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82CircuitValue.setStatus("current")


class _DhcpOption82RemoteIDType_Type(Integer32):
    """Custom type dhcpOption82RemoteIDType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DhcpOption82RemoteIDType_Type.__name__ = "Integer32"
_DhcpOption82RemoteIDType_Object = MibScalar
dhcpOption82RemoteIDType = _DhcpOption82RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 10),
    _DhcpOption82RemoteIDType_Type()
)
dhcpOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82RemoteIDType.setStatus("current")


class _DhcpOption82RemoteValue_Type(DisplayString):
    """Custom type dhcpOption82RemoteValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 31),
    )


_DhcpOption82RemoteValue_Type.__name__ = "DisplayString"
_DhcpOption82RemoteValue_Object = MibScalar
dhcpOption82RemoteValue = _DhcpOption82RemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 11),
    _DhcpOption82RemoteValue_Type()
)
dhcpOption82RemoteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82RemoteValue.setStatus("current")
_CambiumSSHServer_ObjectIdentity = ObjectIdentity
cambiumSSHServer = _CambiumSSHServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3)
)


class _CambiumSSHServerEnable_Type(Integer32):
    """Custom type cambiumSSHServerEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumSSHServerEnable_Type.__name__ = "Integer32"
_CambiumSSHServerEnable_Object = MibScalar
cambiumSSHServerEnable = _CambiumSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3, 1),
    _CambiumSSHServerEnable_Type()
)
cambiumSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSSHServerEnable.setStatus("current")


class _CambiumSSHServerPort_Type(Integer32):
    """Custom type cambiumSSHServerPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CambiumSSHServerPort_Type.__name__ = "Integer32"
_CambiumSSHServerPort_Object = MibScalar
cambiumSSHServerPort = _CambiumSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3, 2),
    _CambiumSSHServerPort_Type()
)
cambiumSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSSHServerPort.setStatus("current")


class _CambiumSSHServerDeprecatedAlgorithms_Type(Integer32):
    """Custom type cambiumSSHServerDeprecatedAlgorithms based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumSSHServerDeprecatedAlgorithms_Type.__name__ = "Integer32"
_CambiumSSHServerDeprecatedAlgorithms_Object = MibScalar
cambiumSSHServerDeprecatedAlgorithms = _CambiumSSHServerDeprecatedAlgorithms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3, 3),
    _CambiumSSHServerDeprecatedAlgorithms_Type()
)
cambiumSSHServerDeprecatedAlgorithms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSSHServerDeprecatedAlgorithms.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4)
)


class _NetworkMode_Type(Integer32):
    """Custom type networkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_NetworkMode_Type.__name__ = "Integer32"
_NetworkMode_Object = MibScalar
networkMode = _NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 1),
    _NetworkMode_Type()
)
networkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMode.setStatus("current")
_NetworkLan_ObjectIdentity = ObjectIdentity
networkLan = _NetworkLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2)
)


class _NetworkLanIPAddressMode_Type(Integer32):
    """Custom type networkLanIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkLanIPAddressMode_Type.__name__ = "Integer32"
_NetworkLanIPAddressMode_Object = MibScalar
networkLanIPAddressMode = _NetworkLanIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 1),
    _NetworkLanIPAddressMode_Type()
)
networkLanIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPAddressMode.setStatus("current")
_NetworkLanIPAddr_Type = IpAddress
_NetworkLanIPAddr_Object = MibScalar
networkLanIPAddr = _NetworkLanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 2),
    _NetworkLanIPAddr_Type()
)
networkLanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPAddr.setStatus("current")
_NetworkLanNetmask_Type = IpAddress
_NetworkLanNetmask_Object = MibScalar
networkLanNetmask = _NetworkLanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 3),
    _NetworkLanNetmask_Type()
)
networkLanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanNetmask.setStatus("current")
_NetworkLanGatewayIP_Type = IpAddress
_NetworkLanGatewayIP_Object = MibScalar
networkLanGatewayIP = _NetworkLanGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 4),
    _NetworkLanGatewayIP_Type()
)
networkLanGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanGatewayIP.setStatus("current")
_NetworkLanDNSIPAddr_Type = IpAddress
_NetworkLanDNSIPAddr_Object = MibScalar
networkLanDNSIPAddr = _NetworkLanDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 5),
    _NetworkLanDNSIPAddr_Type()
)
networkLanDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddr.setStatus("obsolete")


class _NetworkLanMTU_Type(Integer32):
    """Custom type networkLanMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_NetworkLanMTU_Type.__name__ = "Integer32"
_NetworkLanMTU_Object = MibScalar
networkLanMTU = _NetworkLanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 6),
    _NetworkLanMTU_Type()
)
networkLanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanMTU.setStatus("current")
_NetworkLanDNSIPAddrPrimary_Type = IpAddress
_NetworkLanDNSIPAddrPrimary_Object = MibScalar
networkLanDNSIPAddrPrimary = _NetworkLanDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 7),
    _NetworkLanDNSIPAddrPrimary_Type()
)
networkLanDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddrPrimary.setStatus("current")
_NetworkLanDNSIPAddrSecondary_Type = IpAddress
_NetworkLanDNSIPAddrSecondary_Object = MibScalar
networkLanDNSIPAddrSecondary = _NetworkLanDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 8),
    _NetworkLanDNSIPAddrSecondary_Type()
)
networkLanDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddrSecondary.setStatus("current")


class _NetworkLanAutoNegotiation_Type(Integer32):
    """Custom type networkLanAutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanAutoNegotiation_Type.__name__ = "Integer32"
_NetworkLanAutoNegotiation_Object = MibScalar
networkLanAutoNegotiation = _NetworkLanAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 9),
    _NetworkLanAutoNegotiation_Type()
)
networkLanAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanAutoNegotiation.setStatus("current")


class _NetworkLanSpeed_Type(Integer32):
    """Custom type networkLanSpeed based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_NetworkLanSpeed_Type.__name__ = "Integer32"
_NetworkLanSpeed_Object = MibScalar
networkLanSpeed = _NetworkLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 10),
    _NetworkLanSpeed_Type()
)
networkLanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanSpeed.setStatus("current")


class _NetworkLanDuplex_Type(Integer32):
    """Custom type networkLanDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanDuplex_Type.__name__ = "Integer32"
_NetworkLanDuplex_Object = MibScalar
networkLanDuplex = _NetworkLanDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 11),
    _NetworkLanDuplex_Type()
)
networkLanDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDuplex.setStatus("current")


class _NetworkBroadcastStormEnabled_Type(Integer32):
    """Custom type networkBroadcastStormEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkBroadcastStormEnabled_Type.__name__ = "Integer32"
_NetworkBroadcastStormEnabled_Object = MibScalar
networkBroadcastStormEnabled = _NetworkBroadcastStormEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 12),
    _NetworkBroadcastStormEnabled_Type()
)
networkBroadcastStormEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBroadcastStormEnabled.setStatus("current")


class _NetworkBroadcastStormRate_Type(Integer32):
    """Custom type networkBroadcastStormRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 16000),
    )


_NetworkBroadcastStormRate_Type.__name__ = "Integer32"
_NetworkBroadcastStormRate_Object = MibScalar
networkBroadcastStormRate = _NetworkBroadcastStormRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 13),
    _NetworkBroadcastStormRate_Type()
)
networkBroadcastStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBroadcastStormRate.setStatus("current")


class _NetworkLanSmartSpeedMode_Type(Integer32):
    """Custom type networkLanSmartSpeedMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanSmartSpeedMode_Type.__name__ = "Integer32"
_NetworkLanSmartSpeedMode_Object = MibScalar
networkLanSmartSpeedMode = _NetworkLanSmartSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 14),
    _NetworkLanSmartSpeedMode_Type()
)
networkLanSmartSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanSmartSpeedMode.setStatus("current")


class _NetworkLan2Enabled_Type(Integer32):
    """Custom type networkLan2Enabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2Enabled_Type.__name__ = "Integer32"
_NetworkLan2Enabled_Object = MibScalar
networkLan2Enabled = _NetworkLan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 20),
    _NetworkLan2Enabled_Type()
)
networkLan2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Enabled.setStatus("current")


class _NetworkLan2AutoNegotiation_Type(Integer32):
    """Custom type networkLan2AutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2AutoNegotiation_Type.__name__ = "Integer32"
_NetworkLan2AutoNegotiation_Object = MibScalar
networkLan2AutoNegotiation = _NetworkLan2AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 21),
    _NetworkLan2AutoNegotiation_Type()
)
networkLan2AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2AutoNegotiation.setStatus("current")


class _NetworkLan2Speed_Type(Integer32):
    """Custom type networkLan2Speed based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_NetworkLan2Speed_Type.__name__ = "Integer32"
_NetworkLan2Speed_Object = MibScalar
networkLan2Speed = _NetworkLan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 22),
    _NetworkLan2Speed_Type()
)
networkLan2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Speed.setStatus("current")


class _NetworkLan2Duplex_Type(Integer32):
    """Custom type networkLan2Duplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2Duplex_Type.__name__ = "Integer32"
_NetworkLan2Duplex_Object = MibScalar
networkLan2Duplex = _NetworkLan2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 23),
    _NetworkLan2Duplex_Type()
)
networkLan2Duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Duplex.setStatus("current")


class _NetworkLan2PoEEnabled_Type(Integer32):
    """Custom type networkLan2PoEEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2PoEEnabled_Type.__name__ = "Integer32"
_NetworkLan2PoEEnabled_Object = MibScalar
networkLan2PoEEnabled = _NetworkLan2PoEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 24),
    _NetworkLan2PoEEnabled_Type()
)
networkLan2PoEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2PoEEnabled.setStatus("current")


class _NetworkLanEnabled_Type(Integer32):
    """Custom type networkLanEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanEnabled_Type.__name__ = "Integer32"
_NetworkLanEnabled_Object = MibScalar
networkLanEnabled = _NetworkLanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 25),
    _NetworkLanEnabled_Type()
)
networkLanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanEnabled.setStatus("current")


class _NetworkLan2MTU_Type(Integer32):
    """Custom type networkLan2MTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_NetworkLan2MTU_Type.__name__ = "Integer32"
_NetworkLan2MTU_Object = MibScalar
networkLan2MTU = _NetworkLan2MTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 26),
    _NetworkLan2MTU_Type()
)
networkLan2MTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2MTU.setStatus("current")


class _NetworkLanAdvertise_Type(Integer32):
    """Custom type networkLanAdvertise based on Integer32"""
    defaultValue = 47


_NetworkLanAdvertise_Type.__name__ = "Integer32"
_NetworkLanAdvertise_Object = MibScalar
networkLanAdvertise = _NetworkLanAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 27),
    _NetworkLanAdvertise_Type()
)
networkLanAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanAdvertise.setStatus("current")
_NetworkLanIPv6Addr_Type = Ipv6Address
_NetworkLanIPv6Addr_Object = MibScalar
networkLanIPv6Addr = _NetworkLanIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 31),
    _NetworkLanIPv6Addr_Type()
)
networkLanIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPv6Addr.setStatus("current")
_NetworkLanGatewayIPv6_Type = Ipv6Address
_NetworkLanGatewayIPv6_Object = MibScalar
networkLanGatewayIPv6 = _NetworkLanGatewayIPv6_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 32),
    _NetworkLanGatewayIPv6_Type()
)
networkLanGatewayIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanGatewayIPv6.setStatus("current")


class _NetworkLanIPv6AddressType_Type(Integer32):
    """Custom type networkLanIPv6AddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_NetworkLanIPv6AddressType_Type.__name__ = "Integer32"
_NetworkLanIPv6AddressType_Object = MibScalar
networkLanIPv6AddressType = _NetworkLanIPv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 33),
    _NetworkLanIPv6AddressType_Type()
)
networkLanIPv6AddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPv6AddressType.setStatus("current")


class _NetworkLanIPv6PrefixLength_Type(Integer32):
    """Custom type networkLanIPv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NetworkLanIPv6PrefixLength_Type.__name__ = "Integer32"
_NetworkLanIPv6PrefixLength_Object = MibScalar
networkLanIPv6PrefixLength = _NetworkLanIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 34),
    _NetworkLanIPv6PrefixLength_Type()
)
networkLanIPv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPv6PrefixLength.setStatus("current")


class _NetworkLanIPv6DHCPServer_Type(Integer32):
    """Custom type networkLanIPv6DHCPServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_NetworkLanIPv6DHCPServer_Type.__name__ = "Integer32"
_NetworkLanIPv6DHCPServer_Object = MibScalar
networkLanIPv6DHCPServer = _NetworkLanIPv6DHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 35),
    _NetworkLanIPv6DHCPServer_Type()
)
networkLanIPv6DHCPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPv6DHCPServer.setStatus("current")
_LanSwitch_ObjectIdentity = ObjectIdentity
lanSwitch = _LanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100)
)
_LanSwitchPortTable_Object = MibTable
lanSwitchPortTable = _LanSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10)
)
if mibBuilder.loadTexts:
    lanSwitchPortTable.setStatus("current")
_LanSwitchPortEntry_Object = MibTableRow
lanSwitchPortEntry = _LanSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1)
)
lanSwitchPortEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "lanSwitchPortNum"),
)
if mibBuilder.loadTexts:
    lanSwitchPortEntry.setStatus("current")


class _LanSwitchPortNum_Type(Integer32):
    """Custom type lanSwitchPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LanSwitchPortNum_Type.__name__ = "Integer32"
_LanSwitchPortNum_Object = MibTableColumn
lanSwitchPortNum = _LanSwitchPortNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 1),
    _LanSwitchPortNum_Type()
)
lanSwitchPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSwitchPortNum.setStatus("current")


class _LanSwitchPortEnable_Type(Integer32):
    """Custom type lanSwitchPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_LanSwitchPortEnable_Type.__name__ = "Integer32"
_LanSwitchPortEnable_Object = MibTableColumn
lanSwitchPortEnable = _LanSwitchPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 2),
    _LanSwitchPortEnable_Type()
)
lanSwitchPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSwitchPortEnable.setStatus("current")


class _LanSwitchPortAutoneg_Type(Integer32):
    """Custom type lanSwitchPortAutoneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_LanSwitchPortAutoneg_Type.__name__ = "Integer32"
_LanSwitchPortAutoneg_Object = MibTableColumn
lanSwitchPortAutoneg = _LanSwitchPortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 3),
    _LanSwitchPortAutoneg_Type()
)
lanSwitchPortAutoneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSwitchPortAutoneg.setStatus("current")


class _LanSwitchPortSpeed_Type(Integer32):
    """Custom type lanSwitchPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_LanSwitchPortSpeed_Type.__name__ = "Integer32"
_LanSwitchPortSpeed_Object = MibTableColumn
lanSwitchPortSpeed = _LanSwitchPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 4),
    _LanSwitchPortSpeed_Type()
)
lanSwitchPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSwitchPortSpeed.setStatus("current")


class _LanSwitchPortDuplex_Type(Integer32):
    """Custom type lanSwitchPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_LanSwitchPortDuplex_Type.__name__ = "Integer32"
_LanSwitchPortDuplex_Object = MibTableColumn
lanSwitchPortDuplex = _LanSwitchPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 5),
    _LanSwitchPortDuplex_Type()
)
lanSwitchPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSwitchPortDuplex.setStatus("current")


class _LanSwitchPortPoEMode_Type(Integer32):
    """Custom type lanSwitchPortPoEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_LanSwitchPortPoEMode_Type.__name__ = "Integer32"
_LanSwitchPortPoEMode_Object = MibTableColumn
lanSwitchPortPoEMode = _LanSwitchPortPoEMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 100, 10, 1, 6),
    _LanSwitchPortPoEMode_Type()
)
lanSwitchPortPoEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSwitchPortPoEMode.setStatus("current")
_NetworkWan_ObjectIdentity = ObjectIdentity
networkWan = _NetworkWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3)
)


class _NetworkWanIPAddressMode_Type(Integer32):
    """Custom type networkWanIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkWanIPAddressMode_Type.__name__ = "Integer32"
_NetworkWanIPAddressMode_Object = MibScalar
networkWanIPAddressMode = _NetworkWanIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 1),
    _NetworkWanIPAddressMode_Type()
)
networkWanIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPAddressMode.setStatus("current")
_NetworkWanIPAddr_Type = IpAddress
_NetworkWanIPAddr_Object = MibScalar
networkWanIPAddr = _NetworkWanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 2),
    _NetworkWanIPAddr_Type()
)
networkWanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPAddr.setStatus("current")
_NetworkWanNetmask_Type = IpAddress
_NetworkWanNetmask_Object = MibScalar
networkWanNetmask = _NetworkWanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 3),
    _NetworkWanNetmask_Type()
)
networkWanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanNetmask.setStatus("current")
_NetworkWanGatewayIP_Type = IpAddress
_NetworkWanGatewayIP_Object = MibScalar
networkWanGatewayIP = _NetworkWanGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 4),
    _NetworkWanGatewayIP_Type()
)
networkWanGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanGatewayIP.setStatus("current")
_NetworkWanDNSIPAddr_Type = IpAddress
_NetworkWanDNSIPAddr_Object = MibScalar
networkWanDNSIPAddr = _NetworkWanDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 5),
    _NetworkWanDNSIPAddr_Type()
)
networkWanDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddr.setStatus("obsolete")


class _NetworkWanMTU_Type(Integer32):
    """Custom type networkWanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 3508),
    )


_NetworkWanMTU_Type.__name__ = "Integer32"
_NetworkWanMTU_Object = MibScalar
networkWanMTU = _NetworkWanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 6),
    _NetworkWanMTU_Type()
)
networkWanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanMTU.setStatus("current")
_NetworkWanDNSIPAddrPrimary_Type = IpAddress
_NetworkWanDNSIPAddrPrimary_Object = MibScalar
networkWanDNSIPAddrPrimary = _NetworkWanDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 7),
    _NetworkWanDNSIPAddrPrimary_Type()
)
networkWanDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddrPrimary.setStatus("current")
_NetworkWanDNSIPAddrSecondary_Type = IpAddress
_NetworkWanDNSIPAddrSecondary_Object = MibScalar
networkWanDNSIPAddrSecondary = _NetworkWanDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 8),
    _NetworkWanDNSIPAddrSecondary_Type()
)
networkWanDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddrSecondary.setStatus("current")


class _NetworkWanPPPoE_Type(Integer32):
    """Custom type networkWanPPPoE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkWanPPPoE_Type.__name__ = "Integer32"
_NetworkWanPPPoE_Object = MibScalar
networkWanPPPoE = _NetworkWanPPPoE_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 9),
    _NetworkWanPPPoE_Type()
)
networkWanPPPoE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoE.setStatus("current")


class _NetworkWanPPPoEUsername_Type(DisplayString):
    """Custom type networkWanPPPoEUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEUsername_Type.__name__ = "DisplayString"
_NetworkWanPPPoEUsername_Object = MibScalar
networkWanPPPoEUsername = _NetworkWanPPPoEUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 10),
    _NetworkWanPPPoEUsername_Type()
)
networkWanPPPoEUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEUsername.setStatus("current")


class _NetworkWanPPPoEPassword_Type(OctetString):
    """Custom type networkWanPPPoEPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEPassword_Type.__name__ = "OctetString"
_NetworkWanPPPoEPassword_Object = MibScalar
networkWanPPPoEPassword = _NetworkWanPPPoEPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 11),
    _NetworkWanPPPoEPassword_Type()
)
networkWanPPPoEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEPassword.setStatus("current")


class _NetworkWanPPPoEAC_Type(DisplayString):
    """Custom type networkWanPPPoEAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEAC_Type.__name__ = "DisplayString"
_NetworkWanPPPoEAC_Object = MibScalar
networkWanPPPoEAC = _NetworkWanPPPoEAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 12),
    _NetworkWanPPPoEAC_Type()
)
networkWanPPPoEAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEAC.setStatus("current")


class _NetworkWanPPPoEService_Type(DisplayString):
    """Custom type networkWanPPPoEService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEService_Type.__name__ = "DisplayString"
_NetworkWanPPPoEService_Object = MibScalar
networkWanPPPoEService = _NetworkWanPPPoEService_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 13),
    _NetworkWanPPPoEService_Type()
)
networkWanPPPoEService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEService.setStatus("current")


class _NetworkWanPPPoEAuth_Type(Integer32):
    """Custom type networkWanPPPoEAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkWanPPPoEAuth_Type.__name__ = "Integer32"
_NetworkWanPPPoEAuth_Object = MibScalar
networkWanPPPoEAuth = _NetworkWanPPPoEAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 14),
    _NetworkWanPPPoEAuth_Type()
)
networkWanPPPoEAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEAuth.setStatus("current")


class _NetworkWanPPPoEMTU_Type(Integer32):
    """Custom type networkWanPPPoEMTU based on Integer32"""
    defaultValue = 1492

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1492),
    )


_NetworkWanPPPoEMTU_Type.__name__ = "Integer32"
_NetworkWanPPPoEMTU_Object = MibScalar
networkWanPPPoEMTU = _NetworkWanPPPoEMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 15),
    _NetworkWanPPPoEMTU_Type()
)
networkWanPPPoEMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEMTU.setStatus("current")


class _NetworkWanPPPoEKeepAlive_Type(Integer32):
    """Custom type networkWanPPPoEKeepAlive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 180),
    )


_NetworkWanPPPoEKeepAlive_Type.__name__ = "Integer32"
_NetworkWanPPPoEKeepAlive_Object = MibScalar
networkWanPPPoEKeepAlive = _NetworkWanPPPoEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 16),
    _NetworkWanPPPoEKeepAlive_Type()
)
networkWanPPPoEKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEKeepAlive.setStatus("current")


class _NetworkWanPPPoEMSSClamping_Type(Integer32):
    """Custom type networkWanPPPoEMSSClamping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkWanPPPoEMSSClamping_Type.__name__ = "Integer32"
_NetworkWanPPPoEMSSClamping_Object = MibScalar
networkWanPPPoEMSSClamping = _NetworkWanPPPoEMSSClamping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 17),
    _NetworkWanPPPoEMSSClamping_Type()
)
networkWanPPPoEMSSClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEMSSClamping.setStatus("current")


class _NetworkWanPPPoEAttempts_Type(Integer32):
    """Custom type networkWanPPPoEAttempts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_NetworkWanPPPoEAttempts_Type.__name__ = "Integer32"
_NetworkWanPPPoEAttempts_Object = MibScalar
networkWanPPPoEAttempts = _NetworkWanPPPoEAttempts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 18),
    _NetworkWanPPPoEAttempts_Type()
)
networkWanPPPoEAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEAttempts.setStatus("current")


class _NetworkWanIPv6AddressMode_Type(Integer32):
    """Custom type networkWanIPv6AddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NetworkWanIPv6AddressMode_Type.__name__ = "Integer32"
_NetworkWanIPv6AddressMode_Object = MibScalar
networkWanIPv6AddressMode = _NetworkWanIPv6AddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 30),
    _NetworkWanIPv6AddressMode_Type()
)
networkWanIPv6AddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPv6AddressMode.setStatus("current")
_NetworkWanIPv6Addr_Type = Ipv6Address
_NetworkWanIPv6Addr_Object = MibScalar
networkWanIPv6Addr = _NetworkWanIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 31),
    _NetworkWanIPv6Addr_Type()
)
networkWanIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPv6Addr.setStatus("current")
_NetworkWanGatewayIPv6_Type = Ipv6Address
_NetworkWanGatewayIPv6_Object = MibScalar
networkWanGatewayIPv6 = _NetworkWanGatewayIPv6_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 32),
    _NetworkWanGatewayIPv6_Type()
)
networkWanGatewayIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanGatewayIPv6.setStatus("current")
_NetworkWanIPv6LocalInterfaceId_Type = Ipv6Address
_NetworkWanIPv6LocalInterfaceId_Object = MibScalar
networkWanIPv6LocalInterfaceId = _NetworkWanIPv6LocalInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 33),
    _NetworkWanIPv6LocalInterfaceId_Type()
)
networkWanIPv6LocalInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPv6LocalInterfaceId.setStatus("current")
_MgmtVLAN_ObjectIdentity = ObjectIdentity
mgmtVLAN = _MgmtVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4)
)


class _MgmtVLANEnable_Type(Integer32):
    """Custom type mgmtVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtVLANEnable_Type.__name__ = "Integer32"
_MgmtVLANEnable_Object = MibScalar
mgmtVLANEnable = _MgmtVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 1),
    _MgmtVLANEnable_Type()
)
mgmtVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANEnable.setStatus("current")


class _MgmtVLANVID_Type(Integer32):
    """Custom type mgmtVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MgmtVLANVID_Type.__name__ = "Integer32"
_MgmtVLANVID_Object = MibScalar
mgmtVLANVID = _MgmtVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 2),
    _MgmtVLANVID_Type()
)
mgmtVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANVID.setStatus("current")


class _MgmtVLANVP_Type(Integer32):
    """Custom type mgmtVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtVLANVP_Type.__name__ = "Integer32"
_MgmtVLANVP_Object = MibScalar
mgmtVLANVP = _MgmtVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 3),
    _MgmtVLANVP_Type()
)
mgmtVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANVP.setStatus("current")
_DataVLAN_ObjectIdentity = ObjectIdentity
dataVLAN = _DataVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5)
)


class _DataVLANEnable_Type(Integer32):
    """Custom type dataVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DataVLANEnable_Type.__name__ = "Integer32"
_DataVLANEnable_Object = MibScalar
dataVLANEnable = _DataVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 1),
    _DataVLANEnable_Type()
)
dataVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANEnable.setStatus("current")


class _DataVLANVID_Type(Integer32):
    """Custom type dataVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DataVLANVID_Type.__name__ = "Integer32"
_DataVLANVID_Object = MibScalar
dataVLANVID = _DataVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 2),
    _DataVLANVID_Type()
)
dataVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANVID.setStatus("current")


class _DataVLANVP_Type(Integer32):
    """Custom type dataVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DataVLANVP_Type.__name__ = "Integer32"
_DataVLANVP_Object = MibScalar
dataVLANVP = _DataVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 3),
    _DataVLANVP_Type()
)
dataVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANVP.setStatus("current")


class _NetworkSTP_Type(Integer32):
    """Custom type networkSTP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkSTP_Type.__name__ = "Integer32"
_NetworkSTP_Object = MibScalar
networkSTP = _NetworkSTP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 6),
    _NetworkSTP_Type()
)
networkSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkSTP.setStatus("current")
_NetworkBridge_ObjectIdentity = ObjectIdentity
networkBridge = _NetworkBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7)
)


class _NetworkBridgeIPAddressMode_Type(Integer32):
    """Custom type networkBridgeIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkBridgeIPAddressMode_Type.__name__ = "Integer32"
_NetworkBridgeIPAddressMode_Object = MibScalar
networkBridgeIPAddressMode = _NetworkBridgeIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 1),
    _NetworkBridgeIPAddressMode_Type()
)
networkBridgeIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPAddressMode.setStatus("current")
_NetworkBridgeIPAddr_Type = IpAddress
_NetworkBridgeIPAddr_Object = MibScalar
networkBridgeIPAddr = _NetworkBridgeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 2),
    _NetworkBridgeIPAddr_Type()
)
networkBridgeIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPAddr.setStatus("current")
_NetworkBridgeNetmask_Type = IpAddress
_NetworkBridgeNetmask_Object = MibScalar
networkBridgeNetmask = _NetworkBridgeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 3),
    _NetworkBridgeNetmask_Type()
)
networkBridgeNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeNetmask.setStatus("current")
_NetworkBridgeGatewayIP_Type = IpAddress
_NetworkBridgeGatewayIP_Object = MibScalar
networkBridgeGatewayIP = _NetworkBridgeGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 4),
    _NetworkBridgeGatewayIP_Type()
)
networkBridgeGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeGatewayIP.setStatus("current")
_NetworkBridgeDNSIPAddr_Type = IpAddress
_NetworkBridgeDNSIPAddr_Object = MibScalar
networkBridgeDNSIPAddr = _NetworkBridgeDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 5),
    _NetworkBridgeDNSIPAddr_Type()
)
networkBridgeDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddr.setStatus("obsolete")


class _NetworkBridgeMTU_Type(Integer32):
    """Custom type networkBridgeMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 3508),
    )


_NetworkBridgeMTU_Type.__name__ = "Integer32"
_NetworkBridgeMTU_Object = MibScalar
networkBridgeMTU = _NetworkBridgeMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 6),
    _NetworkBridgeMTU_Type()
)
networkBridgeMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeMTU.setStatus("current")
_NetworkBridgeDNSIPAddrPrimary_Type = IpAddress
_NetworkBridgeDNSIPAddrPrimary_Object = MibScalar
networkBridgeDNSIPAddrPrimary = _NetworkBridgeDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 7),
    _NetworkBridgeDNSIPAddrPrimary_Type()
)
networkBridgeDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddrPrimary.setStatus("current")
_NetworkBridgeDNSIPAddrSecondary_Type = IpAddress
_NetworkBridgeDNSIPAddrSecondary_Object = MibScalar
networkBridgeDNSIPAddrSecondary = _NetworkBridgeDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 8),
    _NetworkBridgeDNSIPAddrSecondary_Type()
)
networkBridgeDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddrSecondary.setStatus("current")


class _NetworkBridgeIPv6AddressMode_Type(Integer32):
    """Custom type networkBridgeIPv6AddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NetworkBridgeIPv6AddressMode_Type.__name__ = "Integer32"
_NetworkBridgeIPv6AddressMode_Object = MibScalar
networkBridgeIPv6AddressMode = _NetworkBridgeIPv6AddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 30),
    _NetworkBridgeIPv6AddressMode_Type()
)
networkBridgeIPv6AddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPv6AddressMode.setStatus("current")
_NetworkBridgeIPv6Addr_Type = Ipv6Address
_NetworkBridgeIPv6Addr_Object = MibScalar
networkBridgeIPv6Addr = _NetworkBridgeIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 31),
    _NetworkBridgeIPv6Addr_Type()
)
networkBridgeIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPv6Addr.setStatus("current")
_NetworkBridgeGatewayIPv6_Type = Ipv6Address
_NetworkBridgeGatewayIPv6_Object = MibScalar
networkBridgeGatewayIPv6 = _NetworkBridgeGatewayIPv6_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 32),
    _NetworkBridgeGatewayIPv6_Type()
)
networkBridgeGatewayIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeGatewayIPv6.setStatus("current")


class _NetworkPortSecurity_Type(Integer32):
    """Custom type networkPortSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkPortSecurity_Type.__name__ = "Integer32"
_NetworkPortSecurity_Object = MibScalar
networkPortSecurity = _NetworkPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 8),
    _NetworkPortSecurity_Type()
)
networkPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurity.setStatus("current")


class _NetworkPortSecurityMax_Type(Integer32):
    """Custom type networkPortSecurityMax based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_NetworkPortSecurityMax_Type.__name__ = "Integer32"
_NetworkPortSecurityMax_Object = MibScalar
networkPortSecurityMax = _NetworkPortSecurityMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 9),
    _NetworkPortSecurityMax_Type()
)
networkPortSecurityMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurityMax.setStatus("current")


class _NetworkPortSecurityAgingTime_Type(Integer32):
    """Custom type networkPortSecurityAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_NetworkPortSecurityAgingTime_Type.__name__ = "Integer32"
_NetworkPortSecurityAgingTime_Object = MibScalar
networkPortSecurityAgingTime = _NetworkPortSecurityAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 10),
    _NetworkPortSecurityAgingTime_Type()
)
networkPortSecurityAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurityAgingTime.setStatus("current")
_McastVLAN_ObjectIdentity = ObjectIdentity
mcastVLAN = _McastVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15)
)


class _McastVLANEnable_Type(Integer32):
    """Custom type mcastVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_McastVLANEnable_Type.__name__ = "Integer32"
_McastVLANEnable_Object = MibScalar
mcastVLANEnable = _McastVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 1),
    _McastVLANEnable_Type()
)
mcastVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANEnable.setStatus("current")


class _McastVLANVID_Type(Integer32):
    """Custom type mcastVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_McastVLANVID_Type.__name__ = "Integer32"
_McastVLANVID_Object = MibScalar
mcastVLANVID = _McastVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 2),
    _McastVLANVID_Type()
)
mcastVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANVID.setStatus("current")


class _McastVLANVP_Type(Integer32):
    """Custom type mcastVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_McastVLANVP_Type.__name__ = "Integer32"
_McastVLANVP_Object = MibScalar
mcastVLANVP = _McastVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 3),
    _McastVLANVP_Type()
)
mcastVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANVP.setStatus("current")


class _McastGroupLimit_Type(Integer32):
    """Custom type mcastGroupLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5),
    )


_McastGroupLimit_Type.__name__ = "Integer32"
_McastGroupLimit_Object = MibScalar
mcastGroupLimit = _McastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 17),
    _McastGroupLimit_Type()
)
mcastGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastGroupLimit.setStatus("current")
_MgmtIF_ObjectIdentity = ObjectIdentity
mgmtIF = _MgmtIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20)
)


class _MgmtIFEnable_Type(Integer32):
    """Custom type mgmtIFEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtIFEnable_Type.__name__ = "Integer32"
_MgmtIFEnable_Object = MibScalar
mgmtIFEnable = _MgmtIFEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 1),
    _MgmtIFEnable_Type()
)
mgmtIFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFEnable.setStatus("current")


class _MgmtIFVLAN_Type(Integer32):
    """Custom type mgmtIFVLAN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtIFVLAN_Type.__name__ = "Integer32"
_MgmtIFVLAN_Object = MibScalar
mgmtIFVLAN = _MgmtIFVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 2),
    _MgmtIFVLAN_Type()
)
mgmtIFVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVLAN.setStatus("current")


class _MgmtIFVID_Type(Integer32):
    """Custom type mgmtIFVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MgmtIFVID_Type.__name__ = "Integer32"
_MgmtIFVID_Object = MibScalar
mgmtIFVID = _MgmtIFVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 3),
    _MgmtIFVID_Type()
)
mgmtIFVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVID.setStatus("current")


class _MgmtIFVP_Type(Integer32):
    """Custom type mgmtIFVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtIFVP_Type.__name__ = "Integer32"
_MgmtIFVP_Object = MibScalar
mgmtIFVP = _MgmtIFVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 4),
    _MgmtIFVP_Type()
)
mgmtIFVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVP.setStatus("current")


class _MgmtIFIPAddressMode_Type(Integer32):
    """Custom type mgmtIFIPAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_MgmtIFIPAddressMode_Type.__name__ = "Integer32"
_MgmtIFIPAddressMode_Object = MibScalar
mgmtIFIPAddressMode = _MgmtIFIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 5),
    _MgmtIFIPAddressMode_Type()
)
mgmtIFIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPAddressMode.setStatus("current")
_MgmtIFIPAddr_Type = IpAddress
_MgmtIFIPAddr_Object = MibScalar
mgmtIFIPAddr = _MgmtIFIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 6),
    _MgmtIFIPAddr_Type()
)
mgmtIFIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPAddr.setStatus("current")
_MgmtIFNetmask_Type = IpAddress
_MgmtIFNetmask_Object = MibScalar
mgmtIFNetmask = _MgmtIFNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 7),
    _MgmtIFNetmask_Type()
)
mgmtIFNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFNetmask.setStatus("current")
_MgmtIFGateway_Type = IpAddress
_MgmtIFGateway_Object = MibScalar
mgmtIFGateway = _MgmtIFGateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 8),
    _MgmtIFGateway_Type()
)
mgmtIFGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFGateway.setStatus("current")


class _MgmtIFIPv6AddressMode_Type(Integer32):
    """Custom type mgmtIFIPv6AddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MgmtIFIPv6AddressMode_Type.__name__ = "Integer32"
_MgmtIFIPv6AddressMode_Object = MibScalar
mgmtIFIPv6AddressMode = _MgmtIFIPv6AddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 30),
    _MgmtIFIPv6AddressMode_Type()
)
mgmtIFIPv6AddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPv6AddressMode.setStatus("current")
_MgmtIFIPv6Addr_Type = Ipv6Address
_MgmtIFIPv6Addr_Object = MibScalar
mgmtIFIPv6Addr = _MgmtIFIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 31),
    _MgmtIFIPv6Addr_Type()
)
mgmtIFIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPv6Addr.setStatus("current")
_MgmtIFIPv6Gateway_Type = Ipv6Address
_MgmtIFIPv6Gateway_Object = MibScalar
mgmtIFIPv6Gateway = _MgmtIFIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 32),
    _MgmtIFIPv6Gateway_Type()
)
mgmtIFIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPv6Gateway.setStatus("current")
_NetworkLanDefaultIP_Type = IpAddress
_NetworkLanDefaultIP_Object = MibScalar
networkLanDefaultIP = _NetworkLanDefaultIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 25),
    _NetworkLanDefaultIP_Type()
)
networkLanDefaultIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDefaultIP.setStatus("current")


class _NetworkRelaydEnable_Type(Integer32):
    """Custom type networkRelaydEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkRelaydEnable_Type.__name__ = "Integer32"
_NetworkRelaydEnable_Object = MibScalar
networkRelaydEnable = _NetworkRelaydEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 26),
    _NetworkRelaydEnable_Type()
)
networkRelaydEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRelaydEnable.setStatus("current")
_NetworkAliases_ObjectIdentity = ObjectIdentity
networkAliases = _NetworkAliases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27)
)
_CambiumIPAliasCnfTable_Object = MibTable
cambiumIPAliasCnfTable = _CambiumIPAliasCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1)
)
if mibBuilder.loadTexts:
    cambiumIPAliasCnfTable.setStatus("current")
_CambiumIPAliasCnfEntry_Object = MibTableRow
cambiumIPAliasCnfEntry = _CambiumIPAliasCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1)
)
cambiumIPAliasCnfEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumIPAliasesIndex"),
)
if mibBuilder.loadTexts:
    cambiumIPAliasCnfEntry.setStatus("current")


class _CambiumIPAliasesIndex_Type(Integer32):
    """Custom type cambiumIPAliasesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CambiumIPAliasesIndex_Type.__name__ = "Integer32"
_CambiumIPAliasesIndex_Object = MibTableColumn
cambiumIPAliasesIndex = _CambiumIPAliasesIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 1),
    _CambiumIPAliasesIndex_Type()
)
cambiumIPAliasesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesIndex.setStatus("current")
_CambiumIPAliasesIpAddr_Type = IpAddress
_CambiumIPAliasesIpAddr_Object = MibTableColumn
cambiumIPAliasesIpAddr = _CambiumIPAliasesIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 2),
    _CambiumIPAliasesIpAddr_Type()
)
cambiumIPAliasesIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesIpAddr.setStatus("current")
_CambiumIPAliasesNetmask_Type = IpAddress
_CambiumIPAliasesNetmask_Object = MibTableColumn
cambiumIPAliasesNetmask = _CambiumIPAliasesNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 3),
    _CambiumIPAliasesNetmask_Type()
)
cambiumIPAliasesNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesNetmask.setStatus("current")


class _CambiumIPAliasesInfo_Type(DisplayString):
    """Custom type cambiumIPAliasesInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumIPAliasesInfo_Type.__name__ = "DisplayString"
_CambiumIPAliasesInfo_Object = MibTableColumn
cambiumIPAliasesInfo = _CambiumIPAliasesInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 4),
    _CambiumIPAliasesInfo_Type()
)
cambiumIPAliasesInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesInfo.setStatus("current")


class _CambiumIPAliasesIface_Type(Integer32):
    """Custom type cambiumIPAliasesIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumIPAliasesIface_Type.__name__ = "Integer32"
_CambiumIPAliasesIface_Object = MibTableColumn
cambiumIPAliasesIface = _CambiumIPAliasesIface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 5),
    _CambiumIPAliasesIface_Type()
)
cambiumIPAliasesIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesIface.setStatus("current")


class _CambiumIPAliasesEnable_Type(Integer32):
    """Custom type cambiumIPAliasesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumIPAliasesEnable_Type.__name__ = "Integer32"
_CambiumIPAliasesEnable_Object = MibScalar
cambiumIPAliasesEnable = _CambiumIPAliasesEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 2),
    _CambiumIPAliasesEnable_Type()
)
cambiumIPAliasesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesEnable.setStatus("current")
_NetworkPPPoE_ObjectIdentity = ObjectIdentity
networkPPPoE = _NetworkPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30)
)


class _NetworkPPPoEIAEnable_Type(Integer32):
    """Custom type networkPPPoEIAEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkPPPoEIAEnable_Type.__name__ = "Integer32"
_NetworkPPPoEIAEnable_Object = MibScalar
networkPPPoEIAEnable = _NetworkPPPoEIAEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 1),
    _NetworkPPPoEIAEnable_Type()
)
networkPPPoEIAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAEnable.setStatus("current")
_NetworkPPPoEIATable_Object = MibTable
networkPPPoEIATable = _NetworkPPPoEIATable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2)
)
if mibBuilder.loadTexts:
    networkPPPoEIATable.setStatus("current")
_NetworkPPPoEIAEntry_Object = MibTableRow
networkPPPoEIAEntry = _NetworkPPPoEIAEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1)
)
networkPPPoEIAEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "networkPPPoEIAIndex"),
)
if mibBuilder.loadTexts:
    networkPPPoEIAEntry.setStatus("current")


class _NetworkPPPoEIAIndex_Type(Integer32):
    """Custom type networkPPPoEIAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_NetworkPPPoEIAIndex_Type.__name__ = "Integer32"
_NetworkPPPoEIAIndex_Object = MibTableColumn
networkPPPoEIAIndex = _NetworkPPPoEIAIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 1),
    _NetworkPPPoEIAIndex_Type()
)
networkPPPoEIAIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAIndex.setStatus("current")


class _NetworkPPPoEIAUID_Type(Integer32):
    """Custom type networkPPPoEIAUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NetworkPPPoEIAUID_Type.__name__ = "Integer32"
_NetworkPPPoEIAUID_Object = MibTableColumn
networkPPPoEIAUID = _NetworkPPPoEIAUID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 2),
    _NetworkPPPoEIAUID_Type()
)
networkPPPoEIAUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAUID.setStatus("current")


class _NetworkPPPoEIASMMAC_Type(DisplayString):
    """Custom type networkPPPoEIASMMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_NetworkPPPoEIASMMAC_Type.__name__ = "DisplayString"
_NetworkPPPoEIASMMAC_Object = MibTableColumn
networkPPPoEIASMMAC = _NetworkPPPoEIASMMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 3),
    _NetworkPPPoEIASMMAC_Type()
)
networkPPPoEIASMMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIASMMAC.setStatus("current")


class _NetworkPPPoEIAPhoneNumber_Type(DisplayString):
    """Custom type networkPPPoEIAPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NetworkPPPoEIAPhoneNumber_Type.__name__ = "DisplayString"
_NetworkPPPoEIAPhoneNumber_Object = MibTableColumn
networkPPPoEIAPhoneNumber = _NetworkPPPoEIAPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 4),
    _NetworkPPPoEIAPhoneNumber_Type()
)
networkPPPoEIAPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAPhoneNumber.setStatus("current")


class _NetworkPPPoEIATerminal_Type(DisplayString):
    """Custom type networkPPPoEIATerminal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NetworkPPPoEIATerminal_Type.__name__ = "DisplayString"
_NetworkPPPoEIATerminal_Object = MibTableColumn
networkPPPoEIATerminal = _NetworkPPPoEIATerminal_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 5),
    _NetworkPPPoEIATerminal_Type()
)
networkPPPoEIATerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIATerminal.setStatus("current")


class _NetworkPPPoEIAFrame_Type(DisplayString):
    """Custom type networkPPPoEIAFrame based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_NetworkPPPoEIAFrame_Type.__name__ = "DisplayString"
_NetworkPPPoEIAFrame_Object = MibTableColumn
networkPPPoEIAFrame = _NetworkPPPoEIAFrame_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 6),
    _NetworkPPPoEIAFrame_Type()
)
networkPPPoEIAFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAFrame.setStatus("current")


class _NetworkPPPoEIASlot_Type(DisplayString):
    """Custom type networkPPPoEIASlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_NetworkPPPoEIASlot_Type.__name__ = "DisplayString"
_NetworkPPPoEIASlot_Object = MibTableColumn
networkPPPoEIASlot = _NetworkPPPoEIASlot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 7),
    _NetworkPPPoEIASlot_Type()
)
networkPPPoEIASlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIASlot.setStatus("current")


class _NetworkPPPoEIAPort_Type(DisplayString):
    """Custom type networkPPPoEIAPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_NetworkPPPoEIAPort_Type.__name__ = "DisplayString"
_NetworkPPPoEIAPort_Object = MibTableColumn
networkPPPoEIAPort = _NetworkPPPoEIAPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 8),
    _NetworkPPPoEIAPort_Type()
)
networkPPPoEIAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAPort.setStatus("current")


class _NetworkPPPoEIAVlanId_Type(Integer32):
    """Custom type networkPPPoEIAVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_NetworkPPPoEIAVlanId_Type.__name__ = "Integer32"
_NetworkPPPoEIAVlanId_Object = MibTableColumn
networkPPPoEIAVlanId = _NetworkPPPoEIAVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 30, 2, 1, 9),
    _NetworkPPPoEIAVlanId_Type()
)
networkPPPoEIAVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPPPoEIAVlanId.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5)
)


class _SnmpReadOnlyCommunity_Type(DisplayString):
    """Custom type snmpReadOnlyCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_SnmpReadOnlyCommunity_Type.__name__ = "DisplayString"
_SnmpReadOnlyCommunity_Object = MibScalar
snmpReadOnlyCommunity = _SnmpReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 1),
    _SnmpReadOnlyCommunity_Type()
)
snmpReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadOnlyCommunity.setStatus("current")


class _SnmpReadWriteCommunity_Type(DisplayString):
    """Custom type snmpReadWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")


_SnmpReadWriteCommunity_Type.__name__ = "DisplayString"
_SnmpReadWriteCommunity_Object = MibScalar
snmpReadWriteCommunity = _SnmpReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 2),
    _SnmpReadWriteCommunity_Type()
)
snmpReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadWriteCommunity.setStatus("current")


class _SnmpSystemName_Type(DisplayString):
    """Custom type snmpSystemName based on DisplayString"""
    defaultValue = OctetString("CambiumNetworks")


_SnmpSystemName_Type.__name__ = "DisplayString"
_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 3),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("current")
_SnmpSystemDescription_Type = DisplayString
_SnmpSystemDescription_Object = MibScalar
snmpSystemDescription = _SnmpSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 4),
    _SnmpSystemDescription_Type()
)
snmpSystemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemDescription.setStatus("current")


class _SnmpTrapEnable_Type(Integer32):
    """Custom type snmpTrapEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpTrapEnable_Type.__name__ = "Integer32"
_SnmpTrapEnable_Object = MibScalar
snmpTrapEnable = _SnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 5),
    _SnmpTrapEnable_Type()
)
snmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEnable.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 6),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("current")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "snmpTrapEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("current")


class _SnmpTrapEntryIndex_Type(Integer32):
    """Custom type snmpTrapEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SnmpTrapEntryIndex_Type.__name__ = "Integer32"
_SnmpTrapEntryIndex_Object = MibTableColumn
snmpTrapEntryIndex = _SnmpTrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 1),
    _SnmpTrapEntryIndex_Type()
)
snmpTrapEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryIndex.setStatus("current")
_SnmpTrapEntryIP_Type = IpAddress
_SnmpTrapEntryIP_Object = MibTableColumn
snmpTrapEntryIP = _SnmpTrapEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 2),
    _SnmpTrapEntryIP_Type()
)
snmpTrapEntryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryIP.setStatus("current")


class _SnmpTrapEntryPort_Type(Integer32):
    """Custom type snmpTrapEntryPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrapEntryPort_Type.__name__ = "Integer32"
_SnmpTrapEntryPort_Object = MibTableColumn
snmpTrapEntryPort = _SnmpTrapEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 3),
    _SnmpTrapEntryPort_Type()
)
snmpTrapEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryPort.setStatus("current")


class _SnmpDomainAccessEnable_Type(Integer32):
    """Custom type snmpDomainAccessEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpDomainAccessEnable_Type.__name__ = "Integer32"
_SnmpDomainAccessEnable_Object = MibScalar
snmpDomainAccessEnable = _SnmpDomainAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 8),
    _SnmpDomainAccessEnable_Type()
)
snmpDomainAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessEnable.setStatus("current")


class _SnmpDomainAccessIP_Type(DisplayString):
    """Custom type snmpDomainAccessIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 15),
    )


_SnmpDomainAccessIP_Type.__name__ = "DisplayString"
_SnmpDomainAccessIP_Object = MibScalar
snmpDomainAccessIP = _SnmpDomainAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 9),
    _SnmpDomainAccessIP_Type()
)
snmpDomainAccessIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessIP.setStatus("current")


class _SnmpDomainAccessIPMask_Type(DisplayString):
    """Custom type snmpDomainAccessIPMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 15),
    )


_SnmpDomainAccessIPMask_Type.__name__ = "DisplayString"
_SnmpDomainAccessIPMask_Object = MibScalar
snmpDomainAccessIPMask = _SnmpDomainAccessIPMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 10),
    _SnmpDomainAccessIPMask_Type()
)
snmpDomainAccessIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessIPMask.setStatus("current")


class _SnmpProtocolVersion_Type(Integer32):
    """Custom type snmpProtocolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SnmpProtocolVersion_Type.__name__ = "Integer32"
_SnmpProtocolVersion_Object = MibScalar
snmpProtocolVersion = _SnmpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 11),
    _SnmpProtocolVersion_Type()
)
snmpProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProtocolVersion.setStatus("current")


class _SnmpAgentPort_Type(Integer32):
    """Custom type snmpAgentPort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAgentPort_Type.__name__ = "Integer32"
_SnmpAgentPort_Object = MibScalar
snmpAgentPort = _SnmpAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 12),
    _SnmpAgentPort_Type()
)
snmpAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentPort.setStatus("current")


class _SnmpRemoteAccess_Type(Integer32):
    """Custom type snmpRemoteAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpRemoteAccess_Type.__name__ = "Integer32"
_SnmpRemoteAccess_Object = MibScalar
snmpRemoteAccess = _SnmpRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 13),
    _SnmpRemoteAccess_Type()
)
snmpRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRemoteAccess.setStatus("current")


class _SnmpLinkTrapEnable_Type(Integer32):
    """Custom type snmpLinkTrapEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpLinkTrapEnable_Type.__name__ = "Integer32"
_SnmpLinkTrapEnable_Object = MibScalar
snmpLinkTrapEnable = _SnmpLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 14),
    _SnmpLinkTrapEnable_Type()
)
snmpLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkTrapEnable.setStatus("current")
_Snmpv3UsersTable_Object = MibTable
snmpv3UsersTable = _Snmpv3UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20)
)
if mibBuilder.loadTexts:
    snmpv3UsersTable.setStatus("current")
_Snmpv3UsersEntry_Object = MibTableRow
snmpv3UsersEntry = _Snmpv3UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1)
)
snmpv3UsersEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "snmpv3UsersTableIndex"),
)
if mibBuilder.loadTexts:
    snmpv3UsersEntry.setStatus("current")


class _Snmpv3UsersTableIndex_Type(Integer32):
    """Custom type snmpv3UsersTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Snmpv3UsersTableIndex_Type.__name__ = "Integer32"
_Snmpv3UsersTableIndex_Object = MibTableColumn
snmpv3UsersTableIndex = _Snmpv3UsersTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 1),
    _Snmpv3UsersTableIndex_Type()
)
snmpv3UsersTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UsersTableIndex.setStatus("current")


class _Snmpv3UserName_Type(DisplayString):
    """Custom type snmpv3UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Snmpv3UserName_Type.__name__ = "DisplayString"
_Snmpv3UserName_Object = MibTableColumn
snmpv3UserName = _Snmpv3UserName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 2),
    _Snmpv3UserName_Type()
)
snmpv3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserName.setStatus("current")


class _Snmpv3UserPassPhrase_Type(DisplayString):
    """Custom type snmpv3UserPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_Snmpv3UserPassPhrase_Type.__name__ = "DisplayString"
_Snmpv3UserPassPhrase_Object = MibTableColumn
snmpv3UserPassPhrase = _Snmpv3UserPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 3),
    _Snmpv3UserPassPhrase_Type()
)
snmpv3UserPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserPassPhrase.setStatus("current")


class _Snmpv3UserSecurityLevel_Type(Integer32):
    """Custom type snmpv3UserSecurityLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Snmpv3UserSecurityLevel_Type.__name__ = "Integer32"
_Snmpv3UserSecurityLevel_Object = MibTableColumn
snmpv3UserSecurityLevel = _Snmpv3UserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 4),
    _Snmpv3UserSecurityLevel_Type()
)
snmpv3UserSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserSecurityLevel.setStatus("current")


class _Snmpv3UserRWAccess_Type(Integer32):
    """Custom type snmpv3UserRWAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Snmpv3UserRWAccess_Type.__name__ = "Integer32"
_Snmpv3UserRWAccess_Object = MibTableColumn
snmpv3UserRWAccess = _Snmpv3UserRWAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 5),
    _Snmpv3UserRWAccess_Type()
)
snmpv3UserRWAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserRWAccess.setStatus("current")


class _Snmpv3UserAuthMethod_Type(Integer32):
    """Custom type snmpv3UserAuthMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Snmpv3UserAuthMethod_Type.__name__ = "Integer32"
_Snmpv3UserAuthMethod_Object = MibTableColumn
snmpv3UserAuthMethod = _Snmpv3UserAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 6),
    _Snmpv3UserAuthMethod_Type()
)
snmpv3UserAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserAuthMethod.setStatus("current")


class _Snmpv3UserEncryption_Type(Integer32):
    """Custom type snmpv3UserEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Snmpv3UserEncryption_Type.__name__ = "Integer32"
_Snmpv3UserEncryption_Object = MibTableColumn
snmpv3UserEncryption = _Snmpv3UserEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 20, 1, 7),
    _Snmpv3UserEncryption_Type()
)
snmpv3UserEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserEncryption.setStatus("current")
_CambiumSystem_ObjectIdentity = ObjectIdentity
cambiumSystem = _CambiumSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6)
)
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1)
)


class _SystemConfigTimezone_Type(DisplayString):
    """Custom type systemConfigTimezone based on DisplayString"""
    defaultValue = OctetString("GMT")


_SystemConfigTimezone_Type.__name__ = "DisplayString"
_SystemConfigTimezone_Object = MibScalar
systemConfigTimezone = _SystemConfigTimezone_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 1),
    _SystemConfigTimezone_Type()
)
systemConfigTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigTimezone.setStatus("current")


class _SystemConfigDeviceName_Type(DisplayString):
    """Custom type systemConfigDeviceName based on DisplayString"""
    defaultValue = OctetString("Cambium-STA")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_SystemConfigDeviceName_Type.__name__ = "DisplayString"
_SystemConfigDeviceName_Object = MibScalar
systemConfigDeviceName = _SystemConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 2),
    _SystemConfigDeviceName_Type()
)
systemConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigDeviceName.setStatus("current")


class _SystemConfigETSILicense_Type(DisplayString):
    """Custom type systemConfigETSILicense based on DisplayString"""
    defaultValue = OctetString("ETSIkey")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemConfigETSILicense_Type.__name__ = "DisplayString"
_SystemConfigETSILicense_Object = MibScalar
systemConfigETSILicense = _SystemConfigETSILicense_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 3),
    _SystemConfigETSILicense_Type()
)
systemConfigETSILicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigETSILicense.setStatus("obsolete")


class _SystemConfigSWLockBit_Type(Integer32):
    """Custom type systemConfigSWLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigSWLockBit_Type.__name__ = "Integer32"
_SystemConfigSWLockBit_Object = MibScalar
systemConfigSWLockBit = _SystemConfigSWLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 4),
    _SystemConfigSWLockBit_Type()
)
systemConfigSWLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSWLockBit.setStatus("current")


class _SystemConfigHWLockBit_Type(Integer32):
    """Custom type systemConfigHWLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigHWLockBit_Type.__name__ = "Integer32"
_SystemConfigHWLockBit_Object = MibScalar
systemConfigHWLockBit = _SystemConfigHWLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 5),
    _SystemConfigHWLockBit_Type()
)
systemConfigHWLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigHWLockBit.setStatus("current")


class _SystemDeviceLocLatitude_Type(DisplayString):
    """Custom type systemDeviceLocLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocLatitude_Type.__name__ = "DisplayString"
_SystemDeviceLocLatitude_Object = MibScalar
systemDeviceLocLatitude = _SystemDeviceLocLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 6),
    _SystemDeviceLocLatitude_Type()
)
systemDeviceLocLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocLatitude.setStatus("current")


class _SystemDeviceLocLongitude_Type(DisplayString):
    """Custom type systemDeviceLocLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocLongitude_Type.__name__ = "DisplayString"
_SystemDeviceLocLongitude_Object = MibScalar
systemDeviceLocLongitude = _SystemDeviceLocLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 7),
    _SystemDeviceLocLongitude_Type()
)
systemDeviceLocLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocLongitude.setStatus("current")


class _SystemDeviceLocHeight_Type(DisplayString):
    """Custom type systemDeviceLocHeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocHeight_Type.__name__ = "DisplayString"
_SystemDeviceLocHeight_Object = MibScalar
systemDeviceLocHeight = _SystemDeviceLocHeight_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 8),
    _SystemDeviceLocHeight_Type()
)
systemDeviceLocHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocHeight.setStatus("current")


class _SystemConfigisGPSkeyOK_Type(Integer32):
    """Custom type systemConfigisGPSkeyOK based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigisGPSkeyOK_Type.__name__ = "Integer32"
_SystemConfigisGPSkeyOK_Object = MibScalar
systemConfigisGPSkeyOK = _SystemConfigisGPSkeyOK_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 10),
    _SystemConfigisGPSkeyOK_Type()
)
systemConfigisGPSkeyOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigisGPSkeyOK.setStatus("obsolete")


class _SystemConfigGPSLockBit_Type(Integer32):
    """Custom type systemConfigGPSLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SystemConfigGPSLockBit_Type.__name__ = "Integer32"
_SystemConfigGPSLockBit_Object = MibScalar
systemConfigGPSLockBit = _SystemConfigGPSLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 11),
    _SystemConfigGPSLockBit_Type()
)
systemConfigGPSLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigGPSLockBit.setStatus("obsolete")


class _SystemConfigSMLockBit_Type(Integer32):
    """Custom type systemConfigSMLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SystemConfigSMLockBit_Type.__name__ = "Integer32"
_SystemConfigSMLockBit_Object = MibScalar
systemConfigSMLockBit = _SystemConfigSMLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 12),
    _SystemConfigSMLockBit_Type()
)
systemConfigSMLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSMLockBit.setStatus("current")


class _SystemConfigSMLimit_Type(Integer32):
    """Custom type systemConfigSMLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SystemConfigSMLimit_Type.__name__ = "Integer32"
_SystemConfigSMLimit_Object = MibScalar
systemConfigSMLimit = _SystemConfigSMLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 13),
    _SystemConfigSMLimit_Type()
)
systemConfigSMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSMLimit.setStatus("current")


class _CambiumePMPElevateHWLicenseLimit_Type(Integer32):
    """Custom type cambiumePMPElevateHWLicenseLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CambiumePMPElevateHWLicenseLimit_Type.__name__ = "Integer32"
_CambiumePMPElevateHWLicenseLimit_Object = MibScalar
cambiumePMPElevateHWLicenseLimit = _CambiumePMPElevateHWLicenseLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 14),
    _CambiumePMPElevateHWLicenseLimit_Type()
)
cambiumePMPElevateHWLicenseLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumePMPElevateHWLicenseLimit.setStatus("current")


class _PowerSequenceFactoryDefault_Type(Integer32):
    """Custom type powerSequenceFactoryDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_PowerSequenceFactoryDefault_Type.__name__ = "Integer32"
_PowerSequenceFactoryDefault_Object = MibScalar
powerSequenceFactoryDefault = _PowerSequenceFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 15),
    _PowerSequenceFactoryDefault_Type()
)
powerSequenceFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSequenceFactoryDefault.setStatus("current")


class _SystemConfigLockedCC_Type(DisplayString):
    """Custom type systemConfigLockedCC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 2),
    )


_SystemConfigLockedCC_Type.__name__ = "DisplayString"
_SystemConfigLockedCC_Object = MibScalar
systemConfigLockedCC = _SystemConfigLockedCC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 16),
    _SystemConfigLockedCC_Type()
)
systemConfigLockedCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigLockedCC.setStatus("current")


class _SystemConfigMinAntGain_Type(Integer32):
    """Custom type systemConfigMinAntGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SystemConfigMinAntGain_Type.__name__ = "Integer32"
_SystemConfigMinAntGain_Object = MibScalar
systemConfigMinAntGain = _SystemConfigMinAntGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 17),
    _SystemConfigMinAntGain_Type()
)
systemConfigMinAntGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigMinAntGain.setStatus("current")


class _SystemConfigOperationalLicense_Type(DisplayString):
    """Custom type systemConfigOperationalLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemConfigOperationalLicense_Type.__name__ = "DisplayString"
_SystemConfigOperationalLicense_Object = MibScalar
systemConfigOperationalLicense = _SystemConfigOperationalLicense_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 18),
    _SystemConfigOperationalLicense_Type()
)
systemConfigOperationalLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigOperationalLicense.setStatus("current")


class _SystemConfigIPv6Support_Type(Integer32):
    """Custom type systemConfigIPv6Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigIPv6Support_Type.__name__ = "Integer32"
_SystemConfigIPv6Support_Object = MibScalar
systemConfigIPv6Support = _SystemConfigIPv6Support_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 19),
    _SystemConfigIPv6Support_Type()
)
systemConfigIPv6Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigIPv6Support.setStatus("current")


class _SystemConfigFactoryResetKeepPwd_Type(Integer32):
    """Custom type systemConfigFactoryResetKeepPwd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigFactoryResetKeepPwd_Type.__name__ = "Integer32"
_SystemConfigFactoryResetKeepPwd_Object = MibScalar
systemConfigFactoryResetKeepPwd = _SystemConfigFactoryResetKeepPwd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 20),
    _SystemConfigFactoryResetKeepPwd_Type()
)
systemConfigFactoryResetKeepPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigFactoryResetKeepPwd.setStatus("current")


class _CambiumDeviceNameLoginDisplay_Type(Integer32):
    """Custom type cambiumDeviceNameLoginDisplay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDeviceNameLoginDisplay_Type.__name__ = "Integer32"
_CambiumDeviceNameLoginDisplay_Object = MibScalar
cambiumDeviceNameLoginDisplay = _CambiumDeviceNameLoginDisplay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 21),
    _CambiumDeviceNameLoginDisplay_Type()
)
cambiumDeviceNameLoginDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceNameLoginDisplay.setStatus("current")


class _SystemConfigStartDHT_Type(Integer32):
    """Custom type systemConfigStartDHT based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, 70),
    )


_SystemConfigStartDHT_Type.__name__ = "Integer32"
_SystemConfigStartDHT_Object = MibScalar
systemConfigStartDHT = _SystemConfigStartDHT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 22),
    _SystemConfigStartDHT_Type()
)
systemConfigStartDHT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigStartDHT.setStatus("current")


class _SystemConfigStopDHT_Type(Integer32):
    """Custom type systemConfigStopDHT based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, 70),
    )


_SystemConfigStopDHT_Type.__name__ = "Integer32"
_SystemConfigStopDHT_Object = MibScalar
systemConfigStopDHT = _SystemConfigStopDHT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 23),
    _SystemConfigStopDHT_Type()
)
systemConfigStopDHT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigStopDHT.setStatus("current")


class _SystemConfigPreheatStopTemp_Type(Integer32):
    """Custom type systemConfigPreheatStopTemp based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, 40),
    )


_SystemConfigPreheatStopTemp_Type.__name__ = "Integer32"
_SystemConfigPreheatStopTemp_Object = MibScalar
systemConfigPreheatStopTemp = _SystemConfigPreheatStopTemp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 24),
    _SystemConfigPreheatStopTemp_Type()
)
systemConfigPreheatStopTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigPreheatStopTemp.setStatus("current")


class _SystemConfigPreheatStopTimeout_Type(Integer32):
    """Custom type systemConfigPreheatStopTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SystemConfigPreheatStopTimeout_Type.__name__ = "Integer32"
_SystemConfigPreheatStopTimeout_Object = MibScalar
systemConfigPreheatStopTimeout = _SystemConfigPreheatStopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 25),
    _SystemConfigPreheatStopTimeout_Type()
)
systemConfigPreheatStopTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigPreheatStopTimeout.setStatus("current")


class _SystemConfigBIB_Type(Integer32):
    """Custom type systemConfigBIB based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SystemConfigBIB_Type.__name__ = "Integer32"
_SystemConfigBIB_Object = MibScalar
systemConfigBIB = _SystemConfigBIB_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 26),
    _SystemConfigBIB_Type()
)
systemConfigBIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigBIB.setStatus("current")


class _SystemConfigLanguage_Type(DisplayString):
    """Custom type systemConfigLanguage based on DisplayString"""
    defaultValue = OctetString("en")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SystemConfigLanguage_Type.__name__ = "DisplayString"
_SystemConfigLanguage_Object = MibScalar
systemConfigLanguage = _SystemConfigLanguage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 27),
    _SystemConfigLanguage_Type()
)
systemConfigLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigLanguage.setStatus("current")


class _SystemConfigCNVision_Type(Integer32):
    """Custom type systemConfigCNVision based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigCNVision_Type.__name__ = "Integer32"
_SystemConfigCNVision_Object = MibScalar
systemConfigCNVision = _SystemConfigCNVision_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 28),
    _SystemConfigCNVision_Type()
)
systemConfigCNVision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigCNVision.setStatus("current")


class _SystemConfigSCLockBit_Type(Integer32):
    """Custom type systemConfigSCLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigSCLockBit_Type.__name__ = "Integer32"
_SystemConfigSCLockBit_Object = MibScalar
systemConfigSCLockBit = _SystemConfigSCLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 29),
    _SystemConfigSCLockBit_Type()
)
systemConfigSCLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSCLockBit.setStatus("current")
_SystemNtpServer_ObjectIdentity = ObjectIdentity
systemNtpServer = _SystemNtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2)
)


class _SystemNtpServerIPMode_Type(Integer32):
    """Custom type systemNtpServerIPMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SystemNtpServerIPMode_Type.__name__ = "Integer32"
_SystemNtpServerIPMode_Object = MibScalar
systemNtpServerIPMode = _SystemNtpServerIPMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 1),
    _SystemNtpServerIPMode_Type()
)
systemNtpServerIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerIPMode.setStatus("current")


class _SystemNtpServerPrimaryIP_Type(DisplayString):
    """Custom type systemNtpServerPrimaryIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_SystemNtpServerPrimaryIP_Type.__name__ = "DisplayString"
_SystemNtpServerPrimaryIP_Object = MibScalar
systemNtpServerPrimaryIP = _SystemNtpServerPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 2),
    _SystemNtpServerPrimaryIP_Type()
)
systemNtpServerPrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerPrimaryIP.setStatus("current")


class _SystemNtpServerSecondaryIP_Type(DisplayString):
    """Custom type systemNtpServerSecondaryIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_SystemNtpServerSecondaryIP_Type.__name__ = "DisplayString"
_SystemNtpServerSecondaryIP_Object = MibScalar
systemNtpServerSecondaryIP = _SystemNtpServerSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 3),
    _SystemNtpServerSecondaryIP_Type()
)
systemNtpServerSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerSecondaryIP.setStatus("current")
_CambiumWebServer_ObjectIdentity = ObjectIdentity
cambiumWebServer = _CambiumWebServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7)
)


class _WebService_Type(Integer32):
    """Custom type webService based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WebService_Type.__name__ = "Integer32"
_WebService_Object = MibScalar
webService = _WebService_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 1),
    _WebService_Type()
)
webService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webService.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 2),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _HttpsPort_Type(Integer32):
    """Custom type httpsPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpsPort_Type.__name__ = "Integer32"
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 3),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")


class _UhttpdMainPem_Type(OctetString):
    """Custom type uhttpdMainPem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_UhttpdMainPem_Type.__name__ = "OctetString"
_UhttpdMainPem_Object = MibScalar
uhttpdMainPem = _UhttpdMainPem_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 4),
    _UhttpdMainPem_Type()
)
uhttpdMainPem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uhttpdMainPem.setStatus("current")


class _UhttpdMainInactLogout_Type(Integer32):
    """Custom type uhttpdMainInactLogout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_UhttpdMainInactLogout_Type.__name__ = "Integer32"
_UhttpdMainInactLogout_Object = MibScalar
uhttpdMainInactLogout = _UhttpdMainInactLogout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 5),
    _UhttpdMainInactLogout_Type()
)
uhttpdMainInactLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uhttpdMainInactLogout.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8)
)
_WirelessDevice_ObjectIdentity = ObjectIdentity
wirelessDevice = _WirelessDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1)
)


class _WirelessDeviceCountryCode_Type(DisplayString):
    """Custom type wirelessDeviceCountryCode based on DisplayString"""
    defaultValue = OctetString("NS")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_WirelessDeviceCountryCode_Type.__name__ = "DisplayString"
_WirelessDeviceCountryCode_Object = MibScalar
wirelessDeviceCountryCode = _WirelessDeviceCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 1),
    _WirelessDeviceCountryCode_Type()
)
wirelessDeviceCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDeviceCountryCode.setStatus("current")


class _WirelessType_Type(Integer32):
    """Custom type wirelessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessType_Type.__name__ = "Integer32"
_WirelessType_Object = MibScalar
wirelessType = _WirelessType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 2),
    _WirelessType_Type()
)
wirelessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessType.setStatus("obsolete")


class _WirelessDefaultCountryCode_Type(DisplayString):
    """Custom type wirelessDefaultCountryCode based on DisplayString"""
    defaultValue = OctetString("OT")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_WirelessDefaultCountryCode_Type.__name__ = "DisplayString"
_WirelessDefaultCountryCode_Object = MibScalar
wirelessDefaultCountryCode = _WirelessDefaultCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 3),
    _WirelessDefaultCountryCode_Type()
)
wirelessDefaultCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDefaultCountryCode.setStatus("current")


class _WirelessSmartAntennaEnabled_Type(Integer32):
    """Custom type wirelessSmartAntennaEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessSmartAntennaEnabled_Type.__name__ = "Integer32"
_WirelessSmartAntennaEnabled_Object = MibScalar
wirelessSmartAntennaEnabled = _WirelessSmartAntennaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 4),
    _WirelessSmartAntennaEnabled_Type()
)
wirelessSmartAntennaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSmartAntennaEnabled.setStatus("current")


class _WirelessAPForcedSector_Type(Integer32):
    """Custom type wirelessAPForcedSector based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessAPForcedSector_Type.__name__ = "Integer32"
_WirelessAPForcedSector_Object = MibScalar
wirelessAPForcedSector = _WirelessAPForcedSector_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 5),
    _WirelessAPForcedSector_Type()
)
wirelessAPForcedSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPForcedSector.setStatus("current")


class _WirelessSTAForcedSector_Type(Integer32):
    """Custom type wirelessSTAForcedSector based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessSTAForcedSector_Type.__name__ = "Integer32"
_WirelessSTAForcedSector_Object = MibScalar
wirelessSTAForcedSector = _WirelessSTAForcedSector_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 6),
    _WirelessSTAForcedSector_Type()
)
wirelessSTAForcedSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSTAForcedSector.setStatus("current")


class _WirelessMUMIMOEnable_Type(Integer32):
    """Custom type wirelessMUMIMOEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessMUMIMOEnable_Type.__name__ = "Integer32"
_WirelessMUMIMOEnable_Object = MibScalar
wirelessMUMIMOEnable = _WirelessMUMIMOEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 10),
    _WirelessMUMIMOEnable_Type()
)
wirelessMUMIMOEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMUMIMOEnable.setStatus("current")


class _WirelessMUMIMOSoundingInterval_Type(Integer32):
    """Custom type wirelessMUMIMOSoundingInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WirelessMUMIMOSoundingInterval_Type.__name__ = "Integer32"
_WirelessMUMIMOSoundingInterval_Object = MibScalar
wirelessMUMIMOSoundingInterval = _WirelessMUMIMOSoundingInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 11),
    _WirelessMUMIMOSoundingInterval_Type()
)
wirelessMUMIMOSoundingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMUMIMOSoundingInterval.setStatus("current")


class _WirelessMUMIMOSoundingAzimuthCycle_Type(Integer32):
    """Custom type wirelessMUMIMOSoundingAzimuthCycle based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WirelessMUMIMOSoundingAzimuthCycle_Type.__name__ = "Integer32"
_WirelessMUMIMOSoundingAzimuthCycle_Object = MibScalar
wirelessMUMIMOSoundingAzimuthCycle = _WirelessMUMIMOSoundingAzimuthCycle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 12),
    _WirelessMUMIMOSoundingAzimuthCycle_Type()
)
wirelessMUMIMOSoundingAzimuthCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMUMIMOSoundingAzimuthCycle.setStatus("current")


class _WirelessMUMIMOCBFRateAdapt_Type(Integer32):
    """Custom type wirelessMUMIMOCBFRateAdapt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMUMIMOCBFRateAdapt_Type.__name__ = "Integer32"
_WirelessMUMIMOCBFRateAdapt_Object = MibScalar
wirelessMUMIMOCBFRateAdapt = _WirelessMUMIMOCBFRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 13),
    _WirelessMUMIMOCBFRateAdapt_Type()
)
wirelessMUMIMOCBFRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMUMIMOCBFRateAdapt.setStatus("current")


class _WirelessMUMIMOCBFRateAdaptIndex_Type(Integer32):
    """Custom type wirelessMUMIMOCBFRateAdaptIndex based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WirelessMUMIMOCBFRateAdaptIndex_Type.__name__ = "Integer32"
_WirelessMUMIMOCBFRateAdaptIndex_Object = MibScalar
wirelessMUMIMOCBFRateAdaptIndex = _WirelessMUMIMOCBFRateAdaptIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 14),
    _WirelessMUMIMOCBFRateAdaptIndex_Type()
)
wirelessMUMIMOCBFRateAdaptIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMUMIMOCBFRateAdaptIndex.setStatus("current")


class _WirelessRandFD_Type(Integer32):
    """Custom type wirelessRandFD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRandFD_Type.__name__ = "Integer32"
_WirelessRandFD_Object = MibScalar
wirelessRandFD = _WirelessRandFD_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 15),
    _WirelessRandFD_Type()
)
wirelessRandFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRandFD.setStatus("current")


class _WirelessEPTPPPDUDuration_Type(Integer32):
    """Custom type wirelessEPTPPPDUDuration based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(2000, 2000),
        ValueRangeConstraint(4000, 4000),
    )


_WirelessEPTPPPDUDuration_Type.__name__ = "Integer32"
_WirelessEPTPPPDUDuration_Object = MibScalar
wirelessEPTPPPDUDuration = _WirelessEPTPPPDUDuration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 16),
    _WirelessEPTPPPDUDuration_Type()
)
wirelessEPTPPPDUDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessEPTPPPDUDuration.setStatus("obsolete")


class _WirelessRadioTransmissionOptimization_Type(Integer32):
    """Custom type wirelessRadioTransmissionOptimization based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WirelessRadioTransmissionOptimization_Type.__name__ = "Integer32"
_WirelessRadioTransmissionOptimization_Object = MibScalar
wirelessRadioTransmissionOptimization = _WirelessRadioTransmissionOptimization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 17),
    _WirelessRadioTransmissionOptimization_Type()
)
wirelessRadioTransmissionOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadioTransmissionOptimization.setStatus("current")
_WirelessInterface_ObjectIdentity = ObjectIdentity
wirelessInterface = _WirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2)
)


class _WirelessInterfaceMode_Type(Integer32):
    """Custom type wirelessInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceMode_Type.__name__ = "Integer32"
_WirelessInterfaceMode_Object = MibScalar
wirelessInterfaceMode = _WirelessInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 1),
    _WirelessInterfaceMode_Type()
)
wirelessInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceMode.setStatus("current")


class _WirelessInterfaceSSID_Type(OctetString):
    """Custom type wirelessInterfaceSSID based on OctetString"""
    defaultValue = OctetString("Cambium-AP")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessInterfaceSSID_Type.__name__ = "OctetString"
_WirelessInterfaceSSID_Object = MibScalar
wirelessInterfaceSSID = _WirelessInterfaceSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 2),
    _WirelessInterfaceSSID_Type()
)
wirelessInterfaceSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSSID.setStatus("current")


class _WirelessInterfaceEncryption_Type(Integer32):
    """Custom type wirelessInterfaceEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceEncryption_Type.__name__ = "Integer32"
_WirelessInterfaceEncryption_Object = MibScalar
wirelessInterfaceEncryption = _WirelessInterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 3),
    _WirelessInterfaceEncryption_Type()
)
wirelessInterfaceEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceEncryption.setStatus("current")


class _WirelessInterfaceEncryptionKey_Type(OctetString):
    """Custom type wirelessInterfaceEncryptionKey based on OctetString"""
    defaultValue = OctetString("Cam39-Tai!wdmv")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )


_WirelessInterfaceEncryptionKey_Type.__name__ = "OctetString"
_WirelessInterfaceEncryptionKey_Object = MibScalar
wirelessInterfaceEncryptionKey = _WirelessInterfaceEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 4),
    _WirelessInterfaceEncryptionKey_Type()
)
wirelessInterfaceEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceEncryptionKey.setStatus("current")


class _WirelessInterfaceHTMode_Type(Integer32):
    """Custom type wirelessInterfaceHTMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_WirelessInterfaceHTMode_Type.__name__ = "Integer32"
_WirelessInterfaceHTMode_Object = MibScalar
wirelessInterfaceHTMode = _WirelessInterfaceHTMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 5),
    _WirelessInterfaceHTMode_Type()
)
wirelessInterfaceHTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceHTMode.setStatus("current")


class _WirelessInterfaceTXPower_Type(Integer32):
    """Custom type wirelessInterfaceTXPower based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 33),
    )


_WirelessInterfaceTXPower_Type.__name__ = "Integer32"
_WirelessInterfaceTXPower_Object = MibScalar
wirelessInterfaceTXPower = _WirelessInterfaceTXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 6),
    _WirelessInterfaceTXPower_Type()
)
wirelessInterfaceTXPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTXPower.setStatus("current")


class _WirelessInterfaceTDDAntennaGain_Type(Integer32):
    """Custom type wirelessInterfaceTDDAntennaGain based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_WirelessInterfaceTDDAntennaGain_Type.__name__ = "Integer32"
_WirelessInterfaceTDDAntennaGain_Object = MibScalar
wirelessInterfaceTDDAntennaGain = _WirelessInterfaceTDDAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 7),
    _WirelessInterfaceTDDAntennaGain_Type()
)
wirelessInterfaceTDDAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDAntennaGain.setStatus("current")


class _WirelessInterfaceTDDRatio_Type(Integer32):
    """Custom type wirelessInterfaceTDDRatio based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
    )


_WirelessInterfaceTDDRatio_Type.__name__ = "Integer32"
_WirelessInterfaceTDDRatio_Object = MibScalar
wirelessInterfaceTDDRatio = _WirelessInterfaceTDDRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 9),
    _WirelessInterfaceTDDRatio_Type()
)
wirelessInterfaceTDDRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDRatio.setStatus("current")


class _WirelessInterfaceTPCTRL_Type(Integer32):
    """Custom type wirelessInterfaceTPCTRL based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -30),
    )


_WirelessInterfaceTPCTRL_Type.__name__ = "Integer32"
_WirelessInterfaceTPCTRL_Object = MibScalar
wirelessInterfaceTPCTRL = _WirelessInterfaceTPCTRL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 10),
    _WirelessInterfaceTPCTRL_Type()
)
wirelessInterfaceTPCTRL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTPCTRL.setStatus("current")


class _WirelessInterfaceTPCMode_Type(Integer32):
    """Custom type wirelessInterfaceTPCMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceTPCMode_Type.__name__ = "Integer32"
_WirelessInterfaceTPCMode_Object = MibScalar
wirelessInterfaceTPCMode = _WirelessInterfaceTPCMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 11),
    _WirelessInterfaceTPCMode_Type()
)
wirelessInterfaceTPCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTPCMode.setStatus("obsolete")


class _WirelessInterfacePTPMode_Type(Integer32):
    """Custom type wirelessInterfacePTPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfacePTPMode_Type.__name__ = "Integer32"
_WirelessInterfacePTPMode_Object = MibScalar
wirelessInterfacePTPMode = _WirelessInterfacePTPMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 12),
    _WirelessInterfacePTPMode_Type()
)
wirelessInterfacePTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfacePTPMode.setStatus("current")


class _WirelessInterfacePTPMACAddress_Type(DisplayString):
    """Custom type wirelessInterfacePTPMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_WirelessInterfacePTPMACAddress_Type.__name__ = "DisplayString"
_WirelessInterfacePTPMACAddress_Object = MibScalar
wirelessInterfacePTPMACAddress = _WirelessInterfacePTPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 13),
    _WirelessInterfacePTPMACAddress_Type()
)
wirelessInterfacePTPMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfacePTPMACAddress.setStatus("current")


class _WirelessInterfaceSyncSource_Type(Integer32):
    """Custom type wirelessInterfaceSyncSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_WirelessInterfaceSyncSource_Type.__name__ = "Integer32"
_WirelessInterfaceSyncSource_Object = MibScalar
wirelessInterfaceSyncSource = _WirelessInterfaceSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 14),
    _WirelessInterfaceSyncSource_Type()
)
wirelessInterfaceSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSyncSource.setStatus("current")


class _WirelessInterfaceSyncHoldTime_Type(Integer32):
    """Custom type wirelessInterfaceSyncHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 864000),
    )


_WirelessInterfaceSyncHoldTime_Type.__name__ = "Integer32"
_WirelessInterfaceSyncHoldTime_Object = MibScalar
wirelessInterfaceSyncHoldTime = _WirelessInterfaceSyncHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 15),
    _WirelessInterfaceSyncHoldTime_Type()
)
wirelessInterfaceSyncHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSyncHoldTime.setStatus("current")


class _WirelessInterfaceScanFrequencyListTwenty_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListTwenty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyListTwenty_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListTwenty_Object = MibScalar
wirelessInterfaceScanFrequencyListTwenty = _WirelessInterfaceScanFrequencyListTwenty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 16),
    _WirelessInterfaceScanFrequencyListTwenty_Type()
)
wirelessInterfaceScanFrequencyListTwenty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListTwenty.setStatus("current")


class _WirelessInterfaceScanFrequencyListForty_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListForty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyListForty_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListForty_Object = MibScalar
wirelessInterfaceScanFrequencyListForty = _WirelessInterfaceScanFrequencyListForty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 17),
    _WirelessInterfaceScanFrequencyListForty_Type()
)
wirelessInterfaceScanFrequencyListForty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListForty.setStatus("current")


class _CenterFrequency_Type(Integer32):
    """Custom type centerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_CenterFrequency_Type.__name__ = "Integer32"
_CenterFrequency_Object = MibScalar
centerFrequency = _CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 18),
    _CenterFrequency_Type()
)
centerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    centerFrequency.setStatus("current")


class _DfsAlternative1CenterFrequency_Type(Integer32):
    """Custom type dfsAlternative1CenterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_DfsAlternative1CenterFrequency_Type.__name__ = "Integer32"
_DfsAlternative1CenterFrequency_Object = MibScalar
dfsAlternative1CenterFrequency = _DfsAlternative1CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 19),
    _DfsAlternative1CenterFrequency_Type()
)
dfsAlternative1CenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1CenterFrequency.setStatus("current")


class _DfsAlternative2CenterFrequency_Type(Integer32):
    """Custom type dfsAlternative2CenterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_DfsAlternative2CenterFrequency_Type.__name__ = "Integer32"
_DfsAlternative2CenterFrequency_Object = MibScalar
dfsAlternative2CenterFrequency = _DfsAlternative2CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 20),
    _DfsAlternative2CenterFrequency_Type()
)
dfsAlternative2CenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2CenterFrequency.setStatus("current")


class _WirelessMaximumCellSize_Type(Integer32):
    """Custom type wirelessMaximumCellSize based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WirelessMaximumCellSize_Type.__name__ = "Integer32"
_WirelessMaximumCellSize_Object = MibScalar
wirelessMaximumCellSize = _WirelessMaximumCellSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 21),
    _WirelessMaximumCellSize_Type()
)
wirelessMaximumCellSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMaximumCellSize.setStatus("current")


class _WirelessCellSizeUnit_Type(Integer32):
    """Custom type wirelessCellSizeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessCellSizeUnit_Type.__name__ = "Integer32"
_WirelessCellSizeUnit_Object = MibScalar
wirelessCellSizeUnit = _WirelessCellSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 22),
    _WirelessCellSizeUnit_Type()
)
wirelessCellSizeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessCellSizeUnit.setStatus("current")


class _WirelessMaximumSTA_Type(Integer32):
    """Custom type wirelessMaximumSTA based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_WirelessMaximumSTA_Type.__name__ = "Integer32"
_WirelessMaximumSTA_Object = MibScalar
wirelessMaximumSTA = _WirelessMaximumSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 23),
    _WirelessMaximumSTA_Type()
)
wirelessMaximumSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMaximumSTA.setStatus("current")


class _DfsAlternative1Bandwidth_Type(Integer32):
    """Custom type dfsAlternative1Bandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DfsAlternative1Bandwidth_Type.__name__ = "Integer32"
_DfsAlternative1Bandwidth_Object = MibScalar
dfsAlternative1Bandwidth = _DfsAlternative1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 24),
    _DfsAlternative1Bandwidth_Type()
)
dfsAlternative1Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1Bandwidth.setStatus("current")


class _DfsAlternative2Bandwidth_Type(Integer32):
    """Custom type dfsAlternative2Bandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DfsAlternative2Bandwidth_Type.__name__ = "Integer32"
_DfsAlternative2Bandwidth_Object = MibScalar
dfsAlternative2Bandwidth = _DfsAlternative2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 25),
    _DfsAlternative2Bandwidth_Type()
)
dfsAlternative2Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2Bandwidth.setStatus("current")


class _WirelessAcceptableAPRSSIThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPRSSIThreshold based on Integer32"""
    defaultValue = -90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_WirelessAcceptableAPRSSIThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPRSSIThreshold_Object = MibScalar
wirelessAcceptableAPRSSIThreshold = _WirelessAcceptableAPRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 26),
    _WirelessAcceptableAPRSSIThreshold_Type()
)
wirelessAcceptableAPRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPRSSIThreshold.setStatus("current")


class _WirelessAcceptableAPCINRThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPCINRThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 60),
    )


_WirelessAcceptableAPCINRThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPCINRThreshold_Object = MibScalar
wirelessAcceptableAPCINRThreshold = _WirelessAcceptableAPCINRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 27),
    _WirelessAcceptableAPCINRThreshold_Type()
)
wirelessAcceptableAPCINRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPCINRThreshold.setStatus("obsolete")


class _WirelessInterfaceUnblockUSfreqs_Type(Integer32):
    """Custom type wirelessInterfaceUnblockUSfreqs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceUnblockUSfreqs_Type.__name__ = "Integer32"
_WirelessInterfaceUnblockUSfreqs_Object = MibScalar
wirelessInterfaceUnblockUSfreqs = _WirelessInterfaceUnblockUSfreqs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 28),
    _WirelessInterfaceUnblockUSfreqs_Type()
)
wirelessInterfaceUnblockUSfreqs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceUnblockUSfreqs.setStatus("obsolete")


class _WirelessMIREnable_Type(Integer32):
    """Custom type wirelessMIREnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMIREnable_Type.__name__ = "Integer32"
_WirelessMIREnable_Object = MibScalar
wirelessMIREnable = _WirelessMIREnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 29),
    _WirelessMIREnable_Type()
)
wirelessMIREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIREnable.setStatus("current")


class _WirelessMIRSTAProfileNumber_Type(Integer32):
    """Custom type wirelessMIRSTAProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRSTAProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRSTAProfileNumber_Object = MibScalar
wirelessMIRSTAProfileNumber = _WirelessMIRSTAProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 30),
    _WirelessMIRSTAProfileNumber_Type()
)
wirelessMIRSTAProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRSTAProfileNumber.setStatus("current")


class _WirelessMIRAPDefaultProfileNumber_Type(Integer32):
    """Custom type wirelessMIRAPDefaultProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRAPDefaultProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRAPDefaultProfileNumber_Object = MibScalar
wirelessMIRAPDefaultProfileNumber = _WirelessMIRAPDefaultProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 31),
    _WirelessMIRAPDefaultProfileNumber_Type()
)
wirelessMIRAPDefaultProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRAPDefaultProfileNumber.setStatus("current")


class _WirelessInterfaceScanFrequencyBandwidth_Type(Integer32):
    """Custom type wirelessInterfaceScanFrequencyBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WirelessInterfaceScanFrequencyBandwidth_Type.__name__ = "Integer32"
_WirelessInterfaceScanFrequencyBandwidth_Object = MibScalar
wirelessInterfaceScanFrequencyBandwidth = _WirelessInterfaceScanFrequencyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 32),
    _WirelessInterfaceScanFrequencyBandwidth_Type()
)
wirelessInterfaceScanFrequencyBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyBandwidth.setStatus("current")


class _WirelessInterfaceGuardInterval_Type(Integer32):
    """Custom type wirelessInterfaceGuardInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_WirelessInterfaceGuardInterval_Type.__name__ = "Integer32"
_WirelessInterfaceGuardInterval_Object = MibScalar
wirelessInterfaceGuardInterval = _WirelessInterfaceGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 33),
    _WirelessInterfaceGuardInterval_Type()
)
wirelessInterfaceGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceGuardInterval.setStatus("current")


class _WirelessInterfaceiFreqReuseMode_Type(Integer32):
    """Custom type wirelessInterfaceiFreqReuseMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceiFreqReuseMode_Type.__name__ = "Integer32"
_WirelessInterfaceiFreqReuseMode_Object = MibScalar
wirelessInterfaceiFreqReuseMode = _WirelessInterfaceiFreqReuseMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 34),
    _WirelessInterfaceiFreqReuseMode_Type()
)
wirelessInterfaceiFreqReuseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceiFreqReuseMode.setStatus("current")


class _WirelessSTAPriority_Type(Integer32):
    """Custom type wirelessSTAPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessSTAPriority_Type.__name__ = "Integer32"
_WirelessSTAPriority_Object = MibScalar
wirelessSTAPriority = _WirelessSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 35),
    _WirelessSTAPriority_Type()
)
wirelessSTAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSTAPriority.setStatus("current")


class _WirelessSmoothingBit_Type(Integer32):
    """Custom type wirelessSmoothingBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessSmoothingBit_Type.__name__ = "Integer32"
_WirelessSmoothingBit_Object = MibScalar
wirelessSmoothingBit = _WirelessSmoothingBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 36),
    _WirelessSmoothingBit_Type()
)
wirelessSmoothingBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSmoothingBit.setStatus("obsolete")


class _WirelessSecurityMethod_Type(Integer32):
    """Custom type wirelessSecurityMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WirelessSecurityMethod_Type.__name__ = "Integer32"
_WirelessSecurityMethod_Object = MibScalar
wirelessSecurityMethod = _WirelessSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 37),
    _WirelessSecurityMethod_Type()
)
wirelessSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityMethod.setStatus("current")


class _WirelessAcceptableAPSNRThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPSNRThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 60),
    )


_WirelessAcceptableAPSNRThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPSNRThreshold_Object = MibScalar
wirelessAcceptableAPSNRThreshold = _WirelessAcceptableAPSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 38),
    _WirelessAcceptableAPSNRThreshold_Type()
)
wirelessAcceptableAPSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPSNRThreshold.setStatus("current")


class _WirelessMgmtPacketRate_Type(Integer32):
    """Custom type wirelessMgmtPacketRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMgmtPacketRate_Type.__name__ = "Integer32"
_WirelessMgmtPacketRate_Object = MibScalar
wirelessMgmtPacketRate = _WirelessMgmtPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 39),
    _WirelessMgmtPacketRate_Type()
)
wirelessMgmtPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMgmtPacketRate.setStatus("obsolete")


class _WirelessStaIsolate_Type(Integer32):
    """Custom type wirelessStaIsolate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessStaIsolate_Type.__name__ = "Integer32"
_WirelessStaIsolate_Object = MibScalar
wirelessStaIsolate = _WirelessStaIsolate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 40),
    _WirelessStaIsolate_Type()
)
wirelessStaIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessStaIsolate.setStatus("current")


class _WirelessCcaEnable_Type(Integer32):
    """Custom type wirelessCcaEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessCcaEnable_Type.__name__ = "Integer32"
_WirelessCcaEnable_Object = MibScalar
wirelessCcaEnable = _WirelessCcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 41),
    _WirelessCcaEnable_Type()
)
wirelessCcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessCcaEnable.setStatus("current")


class _WirelessInterfaceScanFrequencyListTen_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListTen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyListTen_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListTen_Object = MibScalar
wirelessInterfaceScanFrequencyListTen = _WirelessInterfaceScanFrequencyListTen_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 42),
    _WirelessInterfaceScanFrequencyListTen_Type()
)
wirelessInterfaceScanFrequencyListTen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListTen.setStatus("current")


class _WirelessInterfaceScanFrequencyListFive_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyListFive_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListFive_Object = MibScalar
wirelessInterfaceScanFrequencyListFive = _WirelessInterfaceScanFrequencyListFive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 43),
    _WirelessInterfaceScanFrequencyListFive_Type()
)
wirelessInterfaceScanFrequencyListFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListFive.setStatus("current")


class _WirelessMulticastEnhanceMode_Type(Integer32):
    """Custom type wirelessMulticastEnhanceMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
    )


_WirelessMulticastEnhanceMode_Type.__name__ = "Integer32"
_WirelessMulticastEnhanceMode_Object = MibScalar
wirelessMulticastEnhanceMode = _WirelessMulticastEnhanceMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 44),
    _WirelessMulticastEnhanceMode_Type()
)
wirelessMulticastEnhanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMulticastEnhanceMode.setStatus("current")


class _WirelessTXPowerManualLimit_Type(Integer32):
    """Custom type wirelessTXPowerManualLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessTXPowerManualLimit_Type.__name__ = "Integer32"
_WirelessTXPowerManualLimit_Object = MibScalar
wirelessTXPowerManualLimit = _WirelessTXPowerManualLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 48),
    _WirelessTXPowerManualLimit_Type()
)
wirelessTXPowerManualLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTXPowerManualLimit.setStatus("current")


class _WirelessRateMaxMCS_Type(Integer32):
    """Custom type wirelessRateMaxMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WirelessRateMaxMCS_Type.__name__ = "Integer32"
_WirelessRateMaxMCS_Object = MibScalar
wirelessRateMaxMCS = _WirelessRateMaxMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 49),
    _WirelessRateMaxMCS_Type()
)
wirelessRateMaxMCS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wirelessRateMaxMCS.setStatus("obsolete")


class _WirelessSMWifiDistance_Type(Integer32):
    """Custom type wirelessSMWifiDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WirelessSMWifiDistance_Type.__name__ = "Integer32"
_WirelessSMWifiDistance_Object = MibScalar
wirelessSMWifiDistance = _WirelessSMWifiDistance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 50),
    _WirelessSMWifiDistance_Type()
)
wirelessSMWifiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSMWifiDistance.setStatus("current")


class _WirelessInterfaceProtocolMode_Type(Integer32):
    """Custom type wirelessInterfaceProtocolMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WirelessInterfaceProtocolMode_Type.__name__ = "Integer32"
_WirelessInterfaceProtocolMode_Object = MibScalar
wirelessInterfaceProtocolMode = _WirelessInterfaceProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 51),
    _WirelessInterfaceProtocolMode_Type()
)
wirelessInterfaceProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceProtocolMode.setStatus("current")


class _WirelessClientBridgeMode_Type(Integer32):
    """Custom type wirelessClientBridgeMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessClientBridgeMode_Type.__name__ = "Integer32"
_WirelessClientBridgeMode_Object = MibScalar
wirelessClientBridgeMode = _WirelessClientBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 52),
    _WirelessClientBridgeMode_Type()
)
wirelessClientBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessClientBridgeMode.setStatus("current")


class _ForceMcastBcast4Addr_Type(Integer32):
    """Custom type forceMcastBcast4Addr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ForceMcastBcast4Addr_Type.__name__ = "Integer32"
_ForceMcastBcast4Addr_Object = MibScalar
forceMcastBcast4Addr = _ForceMcastBcast4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 53),
    _ForceMcastBcast4Addr_Type()
)
forceMcastBcast4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceMcastBcast4Addr.setStatus("current")


class _WirelessInterfaceCipher_Type(Integer32):
    """Custom type wirelessInterfaceCipher based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceCipher_Type.__name__ = "Integer32"
_WirelessInterfaceCipher_Object = MibScalar
wirelessInterfaceCipher = _WirelessInterfaceCipher_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 54),
    _WirelessInterfaceCipher_Type()
)
wirelessInterfaceCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceCipher.setStatus("current")


class _WirelessInterfaceRateMinMCS_Type(Integer32):
    """Custom type wirelessInterfaceRateMinMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(9, 15),
        ValueRangeConstraint(21, 29),
        ValueRangeConstraint(31, 39),
    )


_WirelessInterfaceRateMinMCS_Type.__name__ = "Integer32"
_WirelessInterfaceRateMinMCS_Object = MibScalar
wirelessInterfaceRateMinMCS = _WirelessInterfaceRateMinMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 55),
    _WirelessInterfaceRateMinMCS_Type()
)
wirelessInterfaceRateMinMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceRateMinMCS.setStatus("current")


class _WirelessInterfaceRateMaxMCS_Type(Integer32):
    """Custom type wirelessInterfaceRateMaxMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(9, 15),
        ValueRangeConstraint(21, 29),
        ValueRangeConstraint(31, 39),
    )


_WirelessInterfaceRateMaxMCS_Type.__name__ = "Integer32"
_WirelessInterfaceRateMaxMCS_Object = MibScalar
wirelessInterfaceRateMaxMCS = _WirelessInterfaceRateMaxMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 56),
    _WirelessInterfaceRateMaxMCS_Type()
)
wirelessInterfaceRateMaxMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceRateMaxMCS.setStatus("current")


class _WirelessMulticastIgmpFastLeave_Type(Integer32):
    """Custom type wirelessMulticastIgmpFastLeave based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMulticastIgmpFastLeave_Type.__name__ = "Integer32"
_WirelessMulticastIgmpFastLeave_Object = MibScalar
wirelessMulticastIgmpFastLeave = _WirelessMulticastIgmpFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 57),
    _WirelessMulticastIgmpFastLeave_Type()
)
wirelessMulticastIgmpFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMulticastIgmpFastLeave.setStatus("current")


class _WirelessInterfaceTDDFrameSize_Type(Integer32):
    """Custom type wirelessInterfaceTDDFrameSize based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 2500),
        ValueRangeConstraint(5000, 5000),
    )


_WirelessInterfaceTDDFrameSize_Type.__name__ = "Integer32"
_WirelessInterfaceTDDFrameSize_Object = MibScalar
wirelessInterfaceTDDFrameSize = _WirelessInterfaceTDDFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 58),
    _WirelessInterfaceTDDFrameSize_Type()
)
wirelessInterfaceTDDFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDFrameSize.setStatus("current")


class _WirelessInterfaceColocState_Type(Integer32):
    """Custom type wirelessInterfaceColocState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceColocState_Type.__name__ = "Integer32"
_WirelessInterfaceColocState_Object = MibScalar
wirelessInterfaceColocState = _WirelessInterfaceColocState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 59),
    _WirelessInterfaceColocState_Type()
)
wirelessInterfaceColocState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceColocState.setStatus("current")


class _WirelessInterfaceColocSystemSyncSrc_Type(Integer32):
    """Custom type wirelessInterfaceColocSystemSyncSrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_WirelessInterfaceColocSystemSyncSrc_Type.__name__ = "Integer32"
_WirelessInterfaceColocSystemSyncSrc_Object = MibScalar
wirelessInterfaceColocSystemSyncSrc = _WirelessInterfaceColocSystemSyncSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 60),
    _WirelessInterfaceColocSystemSyncSrc_Type()
)
wirelessInterfaceColocSystemSyncSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceColocSystemSyncSrc.setStatus("current")


class _WirelessAPWifiWLANmode_Type(Integer32):
    """Custom type wirelessAPWifiWLANmode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessAPWifiWLANmode_Type.__name__ = "Integer32"
_WirelessAPWifiWLANmode_Object = MibScalar
wirelessAPWifiWLANmode = _WirelessAPWifiWLANmode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 61),
    _WirelessAPWifiWLANmode_Type()
)
wirelessAPWifiWLANmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPWifiWLANmode.setStatus("current")


class _ApWiFiDLCTSMode_Type(Integer32):
    """Custom type apWiFiDLCTSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ApWiFiDLCTSMode_Type.__name__ = "Integer32"
_ApWiFiDLCTSMode_Object = MibScalar
apWiFiDLCTSMode = _ApWiFiDLCTSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 62),
    _ApWiFiDLCTSMode_Type()
)
apWiFiDLCTSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiDLCTSMode.setStatus("current")


class _ApWiFiULCTSRTSMode_Type(Integer32):
    """Custom type apWiFiULCTSRTSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ApWiFiULCTSRTSMode_Type.__name__ = "Integer32"
_ApWiFiULCTSRTSMode_Object = MibScalar
apWiFiULCTSRTSMode = _ApWiFiULCTSRTSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 63),
    _ApWiFiULCTSRTSMode_Type()
)
apWiFiULCTSRTSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiULCTSRTSMode.setStatus("current")


class _ApWiFiRTSThreshold_Type(Integer32):
    """Custom type apWiFiRTSThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2346),
    )


_ApWiFiRTSThreshold_Type.__name__ = "Integer32"
_ApWiFiRTSThreshold_Object = MibScalar
apWiFiRTSThreshold = _ApWiFiRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 64),
    _ApWiFiRTSThreshold_Type()
)
apWiFiRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiRTSThreshold.setStatus("current")


class _ApWiFiCompWDSTrBridge_Type(Integer32):
    """Custom type apWiFiCompWDSTrBridge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ApWiFiCompWDSTrBridge_Type.__name__ = "Integer32"
_ApWiFiCompWDSTrBridge_Object = MibScalar
apWiFiCompWDSTrBridge = _ApWiFiCompWDSTrBridge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 65),
    _ApWiFiCompWDSTrBridge_Type()
)
apWiFiCompWDSTrBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiCompWDSTrBridge.setStatus("current")


class _WirelessFreqShift_Type(Integer32):
    """Custom type wirelessFreqShift based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WirelessFreqShift_Type.__name__ = "Integer32"
_WirelessFreqShift_Object = MibScalar
wirelessFreqShift = _WirelessFreqShift_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 66),
    _WirelessFreqShift_Type()
)
wirelessFreqShift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFreqShift.setStatus("current")


class _WirelessFBCompatibility_Type(Integer32):
    """Custom type wirelessFBCompatibility based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessFBCompatibility_Type.__name__ = "Integer32"
_WirelessFBCompatibility_Object = MibScalar
wirelessFBCompatibility = _WirelessFBCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 67),
    _WirelessFBCompatibility_Type()
)
wirelessFBCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFBCompatibility.setStatus("current")


class _WirelessMACFilter_Type(Integer32):
    """Custom type wirelessMACFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMACFilter_Type.__name__ = "Integer32"
_WirelessMACFilter_Object = MibScalar
wirelessMACFilter = _WirelessMACFilter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 70),
    _WirelessMACFilter_Type()
)
wirelessMACFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMACFilter.setStatus("current")


class _WirelessMACFilterPolicy_Type(Integer32):
    """Custom type wirelessMACFilterPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessMACFilterPolicy_Type.__name__ = "Integer32"
_WirelessMACFilterPolicy_Object = MibScalar
wirelessMACFilterPolicy = _WirelessMACFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 71),
    _WirelessMACFilterPolicy_Type()
)
wirelessMACFilterPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMACFilterPolicy.setStatus("current")
_WirelessMACFilterTable_Object = MibTable
wirelessMACFilterTable = _WirelessMACFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 72)
)
if mibBuilder.loadTexts:
    wirelessMACFilterTable.setStatus("current")
_WirelessMACFilterEntry_Object = MibTableRow
wirelessMACFilterEntry = _WirelessMACFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 72, 1)
)
wirelessMACFilterEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "wirelessMACFilterIndex"),
)
if mibBuilder.loadTexts:
    wirelessMACFilterEntry.setStatus("current")


class _WirelessMACFilterIndex_Type(Integer32):
    """Custom type wirelessMACFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WirelessMACFilterIndex_Type.__name__ = "Integer32"
_WirelessMACFilterIndex_Object = MibTableColumn
wirelessMACFilterIndex = _WirelessMACFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 72, 1, 1),
    _WirelessMACFilterIndex_Type()
)
wirelessMACFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMACFilterIndex.setStatus("current")


class _WirelessFilterMAC_Type(DisplayString):
    """Custom type wirelessFilterMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessFilterMAC_Type.__name__ = "DisplayString"
_WirelessFilterMAC_Object = MibTableColumn
wirelessFilterMAC = _WirelessFilterMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 72, 1, 2),
    _WirelessFilterMAC_Type()
)
wirelessFilterMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFilterMAC.setStatus("current")


class _WirelessFilterInfo_Type(DisplayString):
    """Custom type wirelessFilterInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessFilterInfo_Type.__name__ = "DisplayString"
_WirelessFilterInfo_Object = MibTableColumn
wirelessFilterInfo = _WirelessFilterInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 72, 1, 3),
    _WirelessFilterInfo_Type()
)
wirelessFilterInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFilterInfo.setStatus("current")


class _WirelessInterfaceMgmtRadioBoarddata_Type(Integer32):
    """Custom type wirelessInterfaceMgmtRadioBoarddata based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceMgmtRadioBoarddata_Type.__name__ = "Integer32"
_WirelessInterfaceMgmtRadioBoarddata_Object = MibScalar
wirelessInterfaceMgmtRadioBoarddata = _WirelessInterfaceMgmtRadioBoarddata_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 73),
    _WirelessInterfaceMgmtRadioBoarddata_Type()
)
wirelessInterfaceMgmtRadioBoarddata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceMgmtRadioBoarddata.setStatus("current")


class _WirelessPMPWDSUnknownMACFlood_Type(Integer32):
    """Custom type wirelessPMPWDSUnknownMACFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessPMPWDSUnknownMACFlood_Type.__name__ = "Integer32"
_WirelessPMPWDSUnknownMACFlood_Object = MibScalar
wirelessPMPWDSUnknownMACFlood = _WirelessPMPWDSUnknownMACFlood_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 74),
    _WirelessPMPWDSUnknownMACFlood_Type()
)
wirelessPMPWDSUnknownMACFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPMPWDSUnknownMACFlood.setStatus("current")


class _WirelessInterfaceScanFrequencyListEighty_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListEighty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyListEighty_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListEighty_Object = MibScalar
wirelessInterfaceScanFrequencyListEighty = _WirelessInterfaceScanFrequencyListEighty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 80),
    _WirelessInterfaceScanFrequencyListEighty_Type()
)
wirelessInterfaceScanFrequencyListEighty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListEighty.setStatus("current")


class _WirelessInterfaceVHTMCS_Type(Integer32):
    """Custom type wirelessInterfaceVHTMCS based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WirelessInterfaceVHTMCS_Type.__name__ = "Integer32"
_WirelessInterfaceVHTMCS_Object = MibScalar
wirelessInterfaceVHTMCS = _WirelessInterfaceVHTMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 81),
    _WirelessInterfaceVHTMCS_Type()
)
wirelessInterfaceVHTMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceVHTMCS.setStatus("current")


class _WirelessInterfaceNSS_Type(Integer32):
    """Custom type wirelessInterfaceNSS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WirelessInterfaceNSS_Type.__name__ = "Integer32"
_WirelessInterfaceNSS_Object = MibScalar
wirelessInterfaceNSS = _WirelessInterfaceNSS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 82),
    _WirelessInterfaceNSS_Type()
)
wirelessInterfaceNSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceNSS.setStatus("current")


class _MikrotikFreqShift_Type(Integer32):
    """Custom type mikrotikFreqShift based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 50),
    )


_MikrotikFreqShift_Type.__name__ = "Integer32"
_MikrotikFreqShift_Object = MibScalar
mikrotikFreqShift = _MikrotikFreqShift_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 83),
    _MikrotikFreqShift_Type()
)
mikrotikFreqShift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mikrotikFreqShift.setStatus("current")
_CambiumKeepAliveIface1_ObjectIdentity = ObjectIdentity
cambiumKeepAliveIface1 = _CambiumKeepAliveIface1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 84)
)


class _WirelessInterface1KeepAliveEnable_Type(Integer32):
    """Custom type wirelessInterface1KeepAliveEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface1KeepAliveEnable_Type.__name__ = "Integer32"
_WirelessInterface1KeepAliveEnable_Object = MibScalar
wirelessInterface1KeepAliveEnable = _WirelessInterface1KeepAliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 84, 1),
    _WirelessInterface1KeepAliveEnable_Type()
)
wirelessInterface1KeepAliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface1KeepAliveEnable.setStatus("current")


class _WirelessInterface1KeepAliveEPTPEnable_Type(Integer32):
    """Custom type wirelessInterface1KeepAliveEPTPEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface1KeepAliveEPTPEnable_Type.__name__ = "Integer32"
_WirelessInterface1KeepAliveEPTPEnable_Object = MibScalar
wirelessInterface1KeepAliveEPTPEnable = _WirelessInterface1KeepAliveEPTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 84, 2),
    _WirelessInterface1KeepAliveEPTPEnable_Type()
)
wirelessInterface1KeepAliveEPTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface1KeepAliveEPTPEnable.setStatus("current")


class _WirelessInterface1KeepAlivePMPEnable_Type(Integer32):
    """Custom type wirelessInterface1KeepAlivePMPEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface1KeepAlivePMPEnable_Type.__name__ = "Integer32"
_WirelessInterface1KeepAlivePMPEnable_Object = MibScalar
wirelessInterface1KeepAlivePMPEnable = _WirelessInterface1KeepAlivePMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 84, 3),
    _WirelessInterface1KeepAlivePMPEnable_Type()
)
wirelessInterface1KeepAlivePMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface1KeepAlivePMPEnable.setStatus("current")


class _WirelessInterface1KeepAliveWLREnable_Type(Integer32):
    """Custom type wirelessInterface1KeepAliveWLREnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface1KeepAliveWLREnable_Type.__name__ = "Integer32"
_WirelessInterface1KeepAliveWLREnable_Object = MibScalar
wirelessInterface1KeepAliveWLREnable = _WirelessInterface1KeepAliveWLREnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 84, 4),
    _WirelessInterface1KeepAliveWLREnable_Type()
)
wirelessInterface1KeepAliveWLREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface1KeepAliveWLREnable.setStatus("current")


class _WirelessInterfaceSTAMaxDLMCSLimit_Type(Integer32):
    """Custom type wirelessInterfaceSTAMaxDLMCSLimit based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(16, 25),
        ValueRangeConstraint(255, 255),
    )


_WirelessInterfaceSTAMaxDLMCSLimit_Type.__name__ = "Integer32"
_WirelessInterfaceSTAMaxDLMCSLimit_Object = MibScalar
wirelessInterfaceSTAMaxDLMCSLimit = _WirelessInterfaceSTAMaxDLMCSLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 85),
    _WirelessInterfaceSTAMaxDLMCSLimit_Type()
)
wirelessInterfaceSTAMaxDLMCSLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSTAMaxDLMCSLimit.setStatus("current")


class _WirelessInterfaceScanFrequencyList160M_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyList160M based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceScanFrequencyList160M_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyList160M_Object = MibScalar
wirelessInterfaceScanFrequencyList160M = _WirelessInterfaceScanFrequencyList160M_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 86),
    _WirelessInterfaceScanFrequencyList160M_Type()
)
wirelessInterfaceScanFrequencyList160M.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyList160M.setStatus("current")


class _WirelessInterfaceSuRxBfOff_Type(Integer32):
    """Custom type wirelessInterfaceSuRxBfOff based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceSuRxBfOff_Type.__name__ = "Integer32"
_WirelessInterfaceSuRxBfOff_Object = MibScalar
wirelessInterfaceSuRxBfOff = _WirelessInterfaceSuRxBfOff_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 87),
    _WirelessInterfaceSuRxBfOff_Type()
)
wirelessInterfaceSuRxBfOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSuRxBfOff.setStatus("current")
_WirelessPrefList_ObjectIdentity = ObjectIdentity
wirelessPrefList = _WirelessPrefList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3)
)
_PrefferedAPTable_Object = MibTable
prefferedAPTable = _PrefferedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1)
)
if mibBuilder.loadTexts:
    prefferedAPTable.setStatus("current")
_PrefferedAPEntry_Object = MibTableRow
prefferedAPEntry = _PrefferedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1)
)
prefferedAPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "prefferedListTableEntryIndex"),
)
if mibBuilder.loadTexts:
    prefferedAPEntry.setStatus("current")


class _PrefferedListTableEntryIndex_Type(Integer32):
    """Custom type prefferedListTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PrefferedListTableEntryIndex_Type.__name__ = "Integer32"
_PrefferedListTableEntryIndex_Object = MibTableColumn
prefferedListTableEntryIndex = _PrefferedListTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 1),
    _PrefferedListTableEntryIndex_Type()
)
prefferedListTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntryIndex.setStatus("current")


class _PrefferedListTableEntrySSID_Type(OctetString):
    """Custom type prefferedListTableEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_PrefferedListTableEntrySSID_Type.__name__ = "OctetString"
_PrefferedListTableEntrySSID_Object = MibTableColumn
prefferedListTableEntrySSID = _PrefferedListTableEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 2),
    _PrefferedListTableEntrySSID_Type()
)
prefferedListTableEntrySSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntrySSID.setStatus("current")


class _PrefferedListTableEntryKEY_Type(OctetString):
    """Custom type prefferedListTableEntryKEY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )


_PrefferedListTableEntryKEY_Type.__name__ = "OctetString"
_PrefferedListTableEntryKEY_Object = MibTableColumn
prefferedListTableEntryKEY = _PrefferedListTableEntryKEY_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 3),
    _PrefferedListTableEntryKEY_Type()
)
prefferedListTableEntryKEY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntryKEY.setStatus("current")


class _PrefferedListTableSecurityMethod_Type(Integer32):
    """Custom type prefferedListTableSecurityMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PrefferedListTableSecurityMethod_Type.__name__ = "Integer32"
_PrefferedListTableSecurityMethod_Object = MibTableColumn
prefferedListTableSecurityMethod = _PrefferedListTableSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 4),
    _PrefferedListTableSecurityMethod_Type()
)
prefferedListTableSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableSecurityMethod.setStatus("current")
_WirelessMIRList_ObjectIdentity = ObjectIdentity
wirelessMIRList = _WirelessMIRList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4)
)
_WirelessMIRProfileTable_Object = MibTable
wirelessMIRProfileTable = _WirelessMIRProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1)
)
if mibBuilder.loadTexts:
    wirelessMIRProfileTable.setStatus("current")
_WirelessMIRProfileEntry_Object = MibTableRow
wirelessMIRProfileEntry = _WirelessMIRProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1)
)
wirelessMIRProfileEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "wirelessMIRProfileIndex"),
)
if mibBuilder.loadTexts:
    wirelessMIRProfileEntry.setStatus("current")


class _WirelessMIRProfileIndex_Type(Integer32):
    """Custom type wirelessMIRProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WirelessMIRProfileIndex_Type.__name__ = "Integer32"
_WirelessMIRProfileIndex_Object = MibTableColumn
wirelessMIRProfileIndex = _WirelessMIRProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 1),
    _WirelessMIRProfileIndex_Type()
)
wirelessMIRProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileIndex.setStatus("current")


class _WirelessMIRProfileNumber_Type(Integer32):
    """Custom type wirelessMIRProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRProfileNumber_Object = MibTableColumn
wirelessMIRProfileNumber = _WirelessMIRProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 2),
    _WirelessMIRProfileNumber_Type()
)
wirelessMIRProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileNumber.setStatus("current")


class _WirelessMIRProfileDescription_Type(DisplayString):
    """Custom type wirelessMIRProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessMIRProfileDescription_Type.__name__ = "DisplayString"
_WirelessMIRProfileDescription_Object = MibTableColumn
wirelessMIRProfileDescription = _WirelessMIRProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 3),
    _WirelessMIRProfileDescription_Type()
)
wirelessMIRProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileDescription.setStatus("current")


class _WirelessDLMIR_Type(Integer32):
    """Custom type wirelessDLMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_WirelessDLMIR_Type.__name__ = "Integer32"
_WirelessDLMIR_Object = MibTableColumn
wirelessDLMIR = _WirelessDLMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 4),
    _WirelessDLMIR_Type()
)
wirelessDLMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDLMIR.setStatus("current")


class _WirelessULMIR_Type(Integer32):
    """Custom type wirelessULMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_WirelessULMIR_Type.__name__ = "Integer32"
_WirelessULMIR_Object = MibTableColumn
wirelessULMIR = _WirelessULMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 5),
    _WirelessULMIR_Type()
)
wirelessULMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessULMIR.setStatus("current")
_WirelessRadius_ObjectIdentity = ObjectIdentity
wirelessRadius = _WirelessRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5)
)


class _WirelessRadiusTimeout_Type(Integer32):
    """Custom type wirelessRadiusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WirelessRadiusTimeout_Type.__name__ = "Integer32"
_WirelessRadiusTimeout_Object = MibScalar
wirelessRadiusTimeout = _WirelessRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 1),
    _WirelessRadiusTimeout_Type()
)
wirelessRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusTimeout.setStatus("current")


class _WirelessRadiusRetry_Type(Integer32):
    """Custom type wirelessRadiusRetry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WirelessRadiusRetry_Type.__name__ = "Integer32"
_WirelessRadiusRetry_Object = MibScalar
wirelessRadiusRetry = _WirelessRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 2),
    _WirelessRadiusRetry_Type()
)
wirelessRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusRetry.setStatus("current")


class _WirelessRadiusGUIUserAuth_Type(Integer32):
    """Custom type wirelessRadiusGUIUserAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessRadiusGUIUserAuth_Type.__name__ = "Integer32"
_WirelessRadiusGUIUserAuth_Object = MibScalar
wirelessRadiusGUIUserAuth = _WirelessRadiusGUIUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 3),
    _WirelessRadiusGUIUserAuth_Type()
)
wirelessRadiusGUIUserAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusGUIUserAuth.setStatus("current")


class _WirelessRadiusCurrentGUIUserAuth_Type(Integer32):
    """Custom type wirelessRadiusCurrentGUIUserAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessRadiusCurrentGUIUserAuth_Type.__name__ = "Integer32"
_WirelessRadiusCurrentGUIUserAuth_Object = MibScalar
wirelessRadiusCurrentGUIUserAuth = _WirelessRadiusCurrentGUIUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 4),
    _WirelessRadiusCurrentGUIUserAuth_Type()
)
wirelessRadiusCurrentGUIUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusCurrentGUIUserAuth.setStatus("obsolete")


class _WirelessRadiusSeverInfo_Type(DisplayString):
    """Custom type wirelessRadiusSeverInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusSeverInfo_Type.__name__ = "DisplayString"
_WirelessRadiusSeverInfo_Object = MibScalar
wirelessRadiusSeverInfo = _WirelessRadiusSeverInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 5),
    _WirelessRadiusSeverInfo_Type()
)
wirelessRadiusSeverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusSeverInfo.setStatus("current")


class _WirelessRadiusIdentityStr_Type(DisplayString):
    """Custom type wirelessRadiusIdentityStr based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusIdentityStr_Type.__name__ = "DisplayString"
_WirelessRadiusIdentityStr_Object = MibScalar
wirelessRadiusIdentityStr = _WirelessRadiusIdentityStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 6),
    _WirelessRadiusIdentityStr_Type()
)
wirelessRadiusIdentityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusIdentityStr.setStatus("current")


class _WirelessRadiusIdentityRealm_Type(DisplayString):
    """Custom type wirelessRadiusIdentityRealm based on DisplayString"""
    defaultValue = OctetString("cambiumnetworks.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusIdentityRealm_Type.__name__ = "DisplayString"
_WirelessRadiusIdentityRealm_Object = MibScalar
wirelessRadiusIdentityRealm = _WirelessRadiusIdentityRealm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 7),
    _WirelessRadiusIdentityRealm_Type()
)
wirelessRadiusIdentityRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusIdentityRealm.setStatus("current")


class _WirelessRadiusUsername_Type(DisplayString):
    """Custom type wirelessRadiusUsername based on DisplayString"""
    defaultValue = OctetString("cambium-station")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WirelessRadiusUsername_Type.__name__ = "DisplayString"
_WirelessRadiusUsername_Object = MibScalar
wirelessRadiusUsername = _WirelessRadiusUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 8),
    _WirelessRadiusUsername_Type()
)
wirelessRadiusUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsername.setStatus("current")


class _WirelessRadiusPassword_Type(OctetString):
    """Custom type wirelessRadiusPassword based on OctetString"""
    defaultValue = OctetString("cambium123")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusPassword_Type.__name__ = "OctetString"
_WirelessRadiusPassword_Object = MibScalar
wirelessRadiusPassword = _WirelessRadiusPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 9),
    _WirelessRadiusPassword_Type()
)
wirelessRadiusPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusPassword.setStatus("current")


class _UseMACAddressAsWirelessRadiusUsername_Type(Integer32):
    """Custom type useMACAddressAsWirelessRadiusUsername based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_UseMACAddressAsWirelessRadiusUsername_Type.__name__ = "Integer32"
_UseMACAddressAsWirelessRadiusUsername_Object = MibScalar
useMACAddressAsWirelessRadiusUsername = _UseMACAddressAsWirelessRadiusUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 10),
    _UseMACAddressAsWirelessRadiusUsername_Type()
)
useMACAddressAsWirelessRadiusUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useMACAddressAsWirelessRadiusUsername.setStatus("current")
_WirelessRadiusServerList_ObjectIdentity = ObjectIdentity
wirelessRadiusServerList = _WirelessRadiusServerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6)
)
_WirelessRadiusServerTable_Object = MibTable
wirelessRadiusServerTable = _WirelessRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1)
)
if mibBuilder.loadTexts:
    wirelessRadiusServerTable.setStatus("current")
_WirelessRadiusServerEntry_Object = MibTableRow
wirelessRadiusServerEntry = _WirelessRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1)
)
wirelessRadiusServerEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "wirelessRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    wirelessRadiusServerEntry.setStatus("current")


class _WirelessRadiusServerIndex_Type(Integer32):
    """Custom type wirelessRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WirelessRadiusServerIndex_Type.__name__ = "Integer32"
_WirelessRadiusServerIndex_Object = MibTableColumn
wirelessRadiusServerIndex = _WirelessRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 1),
    _WirelessRadiusServerIndex_Type()
)
wirelessRadiusServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerIndex.setStatus("current")
_WirelessRadiusServerIP_Type = IpAddress
_WirelessRadiusServerIP_Object = MibTableColumn
wirelessRadiusServerIP = _WirelessRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 2),
    _WirelessRadiusServerIP_Type()
)
wirelessRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerIP.setStatus("current")


class _WirelessRadiusServerPort_Type(Integer32):
    """Custom type wirelessRadiusServerPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WirelessRadiusServerPort_Type.__name__ = "Integer32"
_WirelessRadiusServerPort_Object = MibTableColumn
wirelessRadiusServerPort = _WirelessRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 3),
    _WirelessRadiusServerPort_Type()
)
wirelessRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerPort.setStatus("current")


class _WirelessRadiusServerSecret_Type(OctetString):
    """Custom type wirelessRadiusServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessRadiusServerSecret_Type.__name__ = "OctetString"
_WirelessRadiusServerSecret_Object = MibTableColumn
wirelessRadiusServerSecret = _WirelessRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 4),
    _WirelessRadiusServerSecret_Type()
)
wirelessRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerSecret.setStatus("current")
_WirelessRadiusCertificateList_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateList = _WirelessRadiusCertificateList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7)
)
_WirelessRadiusCertificateListRow1_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow1 = _WirelessRadiusCertificateListRow1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1)
)


class _WirelessRadiusUseDefCertificate_Type(Integer32):
    """Custom type wirelessRadiusUseDefCertificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUseDefCertificate_Type.__name__ = "Integer32"
_WirelessRadiusUseDefCertificate_Object = MibScalar
wirelessRadiusUseDefCertificate = _WirelessRadiusUseDefCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1, 1),
    _WirelessRadiusUseDefCertificate_Type()
)
wirelessRadiusUseDefCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUseDefCertificate.setStatus("obsolete")
_WirelessRadiusDefCertificateView_Type = DisplayString
_WirelessRadiusDefCertificateView_Object = MibScalar
wirelessRadiusDefCertificateView = _WirelessRadiusDefCertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1, 2),
    _WirelessRadiusDefCertificateView_Type()
)
wirelessRadiusDefCertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusDefCertificateView.setStatus("obsolete")
_WirelessRadiusCertificateListRow2_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow2 = _WirelessRadiusCertificateListRow2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2)
)


class _WirelessRadiusUser1CertificateName_Type(DisplayString):
    """Custom type wirelessRadiusUser1CertificateName based on DisplayString"""
    defaultValue = OctetString("cert2")


_WirelessRadiusUser1CertificateName_Type.__name__ = "DisplayString"
_WirelessRadiusUser1CertificateName_Object = MibScalar
wirelessRadiusUser1CertificateName = _WirelessRadiusUser1CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2, 1),
    _WirelessRadiusUser1CertificateName_Type()
)
wirelessRadiusUser1CertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser1CertificateName.setStatus("obsolete")
_WirelessRadiusUser1CertificateView_Type = DisplayString
_WirelessRadiusUser1CertificateView_Object = MibScalar
wirelessRadiusUser1CertificateView = _WirelessRadiusUser1CertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2, 2),
    _WirelessRadiusUser1CertificateView_Type()
)
wirelessRadiusUser1CertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusUser1CertificateView.setStatus("obsolete")
_WirelessRadiusCertificateListRow3_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow3 = _WirelessRadiusCertificateListRow3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3)
)


class _WirelessRadiusUser2CertificateName_Type(DisplayString):
    """Custom type wirelessRadiusUser2CertificateName based on DisplayString"""
    defaultValue = OctetString("cert3")


_WirelessRadiusUser2CertificateName_Type.__name__ = "DisplayString"
_WirelessRadiusUser2CertificateName_Object = MibScalar
wirelessRadiusUser2CertificateName = _WirelessRadiusUser2CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3, 1),
    _WirelessRadiusUser2CertificateName_Type()
)
wirelessRadiusUser2CertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser2CertificateName.setStatus("obsolete")
_WirelessRadiusUser2CertificateView_Type = DisplayString
_WirelessRadiusUser2CertificateView_Object = MibScalar
wirelessRadiusUser2CertificateView = _WirelessRadiusUser2CertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3, 2),
    _WirelessRadiusUser2CertificateView_Type()
)
wirelessRadiusUser2CertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusUser2CertificateView.setStatus("obsolete")
_WirelessRadiusCertificateSet_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateSet = _WirelessRadiusCertificateSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8)
)


class _WirelessRadiusDefaultCertificate_Type(OctetString):
    """Custom type wirelessRadiusDefaultCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusDefaultCertificate_Type.__name__ = "OctetString"
_WirelessRadiusDefaultCertificate_Object = MibScalar
wirelessRadiusDefaultCertificate = _WirelessRadiusDefaultCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 1),
    _WirelessRadiusDefaultCertificate_Type()
)
wirelessRadiusDefaultCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusDefaultCertificate.setStatus("current")


class _WirelessRadiusUser1Certificate_Type(OctetString):
    """Custom type wirelessRadiusUser1Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 8192),
    )


_WirelessRadiusUser1Certificate_Type.__name__ = "OctetString"
_WirelessRadiusUser1Certificate_Object = MibScalar
wirelessRadiusUser1Certificate = _WirelessRadiusUser1Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 2),
    _WirelessRadiusUser1Certificate_Type()
)
wirelessRadiusUser1Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser1Certificate.setStatus("current")


class _WirelessRadiusUser2Certificate_Type(OctetString):
    """Custom type wirelessRadiusUser2Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 8192),
    )


_WirelessRadiusUser2Certificate_Type.__name__ = "OctetString"
_WirelessRadiusUser2Certificate_Object = MibScalar
wirelessRadiusUser2Certificate = _WirelessRadiusUser2Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 3),
    _WirelessRadiusUser2Certificate_Type()
)
wirelessRadiusUser2Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser2Certificate.setStatus("current")


class _WirelessRadiusUseDefaultCertificate_Type(Integer32):
    """Custom type wirelessRadiusUseDefaultCertificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUseDefaultCertificate_Type.__name__ = "Integer32"
_WirelessRadiusUseDefaultCertificate_Object = MibScalar
wirelessRadiusUseDefaultCertificate = _WirelessRadiusUseDefaultCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 4),
    _WirelessRadiusUseDefaultCertificate_Type()
)
wirelessRadiusUseDefaultCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUseDefaultCertificate.setStatus("current")
_WirelessRadiusExtraCertificateSet_ObjectIdentity = ObjectIdentity
wirelessRadiusExtraCertificateSet = _WirelessRadiusExtraCertificateSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9)
)


class _WirelessRadiusPMP320Certificate_Type(OctetString):
    """Custom type wirelessRadiusPMP320Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusPMP320Certificate_Type.__name__ = "OctetString"
_WirelessRadiusPMP320Certificate_Object = MibScalar
wirelessRadiusPMP320Certificate = _WirelessRadiusPMP320Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 1),
    _WirelessRadiusPMP320Certificate_Type()
)
wirelessRadiusPMP320Certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusPMP320Certificate.setStatus("current")


class _WirelessRadiusUsePMP320Certificate_Type(Integer32):
    """Custom type wirelessRadiusUsePMP320Certificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUsePMP320Certificate_Type.__name__ = "Integer32"
_WirelessRadiusUsePMP320Certificate_Object = MibScalar
wirelessRadiusUsePMP320Certificate = _WirelessRadiusUsePMP320Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 2),
    _WirelessRadiusUsePMP320Certificate_Type()
)
wirelessRadiusUsePMP320Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsePMP320Certificate.setStatus("current")


class _WirelessRadiusPMP450Certificate_Type(OctetString):
    """Custom type wirelessRadiusPMP450Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusPMP450Certificate_Type.__name__ = "OctetString"
_WirelessRadiusPMP450Certificate_Object = MibScalar
wirelessRadiusPMP450Certificate = _WirelessRadiusPMP450Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 3),
    _WirelessRadiusPMP450Certificate_Type()
)
wirelessRadiusPMP450Certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusPMP450Certificate.setStatus("current")


class _WirelessRadiusUsePMP450Certificate_Type(Integer32):
    """Custom type wirelessRadiusUsePMP450Certificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUsePMP450Certificate_Type.__name__ = "Integer32"
_WirelessRadiusUsePMP450Certificate_Object = MibScalar
wirelessRadiusUsePMP450Certificate = _WirelessRadiusUsePMP450Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 4),
    _WirelessRadiusUsePMP450Certificate_Type()
)
wirelessRadiusUsePMP450Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsePMP450Certificate.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 10)
)
_WirelessInterface2_ObjectIdentity = ObjectIdentity
wirelessInterface2 = _WirelessInterface2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12)
)


class _WirelessInterface2HTMode_Type(Integer32):
    """Custom type wirelessInterface2HTMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WirelessInterface2HTMode_Type.__name__ = "Integer32"
_WirelessInterface2HTMode_Object = MibScalar
wirelessInterface2HTMode = _WirelessInterface2HTMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 5),
    _WirelessInterface2HTMode_Type()
)
wirelessInterface2HTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2HTMode.setStatus("current")


class _WirelessInterface2TXPower_Type(Integer32):
    """Custom type wirelessInterface2TXPower based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 30),
    )


_WirelessInterface2TXPower_Type.__name__ = "Integer32"
_WirelessInterface2TXPower_Object = MibScalar
wirelessInterface2TXPower = _WirelessInterface2TXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 6),
    _WirelessInterface2TXPower_Type()
)
wirelessInterface2TXPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2TXPower.setStatus("current")


class _WirelessInterface2ScanFrequencyListTwenty_Type(DisplayString):
    """Custom type wirelessInterface2ScanFrequencyListTwenty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterface2ScanFrequencyListTwenty_Type.__name__ = "DisplayString"
_WirelessInterface2ScanFrequencyListTwenty_Object = MibScalar
wirelessInterface2ScanFrequencyListTwenty = _WirelessInterface2ScanFrequencyListTwenty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 16),
    _WirelessInterface2ScanFrequencyListTwenty_Type()
)
wirelessInterface2ScanFrequencyListTwenty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyListTwenty.setStatus("current")


class _WirelessInterface2ScanFrequencyListForty_Type(DisplayString):
    """Custom type wirelessInterface2ScanFrequencyListForty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterface2ScanFrequencyListForty_Type.__name__ = "DisplayString"
_WirelessInterface2ScanFrequencyListForty_Object = MibScalar
wirelessInterface2ScanFrequencyListForty = _WirelessInterface2ScanFrequencyListForty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 17),
    _WirelessInterface2ScanFrequencyListForty_Type()
)
wirelessInterface2ScanFrequencyListForty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyListForty.setStatus("current")


class _CenterFrequency2_Type(Integer32):
    """Custom type centerFrequency2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_CenterFrequency2_Type.__name__ = "Integer32"
_CenterFrequency2_Object = MibScalar
centerFrequency2 = _CenterFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 18),
    _CenterFrequency2_Type()
)
centerFrequency2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    centerFrequency2.setStatus("current")


class _DfsAlternative1CenterFrequency2_Type(Integer32):
    """Custom type dfsAlternative1CenterFrequency2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_DfsAlternative1CenterFrequency2_Type.__name__ = "Integer32"
_DfsAlternative1CenterFrequency2_Object = MibScalar
dfsAlternative1CenterFrequency2 = _DfsAlternative1CenterFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 19),
    _DfsAlternative1CenterFrequency2_Type()
)
dfsAlternative1CenterFrequency2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1CenterFrequency2.setStatus("current")


class _DfsAlternative2CenterFrequency2_Type(Integer32):
    """Custom type dfsAlternative2CenterFrequency2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2355, 7200),
    )


_DfsAlternative2CenterFrequency2_Type.__name__ = "Integer32"
_DfsAlternative2CenterFrequency2_Object = MibScalar
dfsAlternative2CenterFrequency2 = _DfsAlternative2CenterFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 20),
    _DfsAlternative2CenterFrequency2_Type()
)
dfsAlternative2CenterFrequency2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2CenterFrequency2.setStatus("current")


class _DfsAlternative1Bandwidth2_Type(Integer32):
    """Custom type dfsAlternative1Bandwidth2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DfsAlternative1Bandwidth2_Type.__name__ = "Integer32"
_DfsAlternative1Bandwidth2_Object = MibScalar
dfsAlternative1Bandwidth2 = _DfsAlternative1Bandwidth2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 24),
    _DfsAlternative1Bandwidth2_Type()
)
dfsAlternative1Bandwidth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1Bandwidth2.setStatus("current")


class _DfsAlternative2Bandwidth2_Type(Integer32):
    """Custom type dfsAlternative2Bandwidth2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DfsAlternative2Bandwidth2_Type.__name__ = "Integer32"
_DfsAlternative2Bandwidth2_Object = MibScalar
dfsAlternative2Bandwidth2 = _DfsAlternative2Bandwidth2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 25),
    _DfsAlternative2Bandwidth2_Type()
)
dfsAlternative2Bandwidth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2Bandwidth2.setStatus("current")


class _WirelessInterface2ScanFrequencyBandwidth_Type(Integer32):
    """Custom type wirelessInterface2ScanFrequencyBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WirelessInterface2ScanFrequencyBandwidth_Type.__name__ = "Integer32"
_WirelessInterface2ScanFrequencyBandwidth_Object = MibScalar
wirelessInterface2ScanFrequencyBandwidth = _WirelessInterface2ScanFrequencyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 32),
    _WirelessInterface2ScanFrequencyBandwidth_Type()
)
wirelessInterface2ScanFrequencyBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyBandwidth.setStatus("current")


class _WirelessInterface2ScanFrequencyListFive_Type(DisplayString):
    """Custom type wirelessInterface2ScanFrequencyListFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterface2ScanFrequencyListFive_Type.__name__ = "DisplayString"
_WirelessInterface2ScanFrequencyListFive_Object = MibScalar
wirelessInterface2ScanFrequencyListFive = _WirelessInterface2ScanFrequencyListFive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 42),
    _WirelessInterface2ScanFrequencyListFive_Type()
)
wirelessInterface2ScanFrequencyListFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyListFive.setStatus("current")


class _WirelessInterface2ScanFrequencyListTen_Type(DisplayString):
    """Custom type wirelessInterface2ScanFrequencyListTen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterface2ScanFrequencyListTen_Type.__name__ = "DisplayString"
_WirelessInterface2ScanFrequencyListTen_Object = MibScalar
wirelessInterface2ScanFrequencyListTen = _WirelessInterface2ScanFrequencyListTen_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 43),
    _WirelessInterface2ScanFrequencyListTen_Type()
)
wirelessInterface2ScanFrequencyListTen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyListTen.setStatus("current")


class _WirelessTXPowerManualLimit2_Type(Integer32):
    """Custom type wirelessTXPowerManualLimit2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessTXPowerManualLimit2_Type.__name__ = "Integer32"
_WirelessTXPowerManualLimit2_Object = MibScalar
wirelessTXPowerManualLimit2 = _WirelessTXPowerManualLimit2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 48),
    _WirelessTXPowerManualLimit2_Type()
)
wirelessTXPowerManualLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTXPowerManualLimit2.setStatus("current")


class _WirelessInterface2RateMinMCS_Type(Integer32):
    """Custom type wirelessInterface2RateMinMCS based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 29),
        ValueRangeConstraint(31, 39),
    )


_WirelessInterface2RateMinMCS_Type.__name__ = "Integer32"
_WirelessInterface2RateMinMCS_Object = MibScalar
wirelessInterface2RateMinMCS = _WirelessInterface2RateMinMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 55),
    _WirelessInterface2RateMinMCS_Type()
)
wirelessInterface2RateMinMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2RateMinMCS.setStatus("current")


class _WirelessInterface2RateMaxMCS_Type(Integer32):
    """Custom type wirelessInterface2RateMaxMCS based on Integer32"""
    defaultValue = 39

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 29),
        ValueRangeConstraint(31, 39),
    )


_WirelessInterface2RateMaxMCS_Type.__name__ = "Integer32"
_WirelessInterface2RateMaxMCS_Object = MibScalar
wirelessInterface2RateMaxMCS = _WirelessInterface2RateMaxMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 56),
    _WirelessInterface2RateMaxMCS_Type()
)
wirelessInterface2RateMaxMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2RateMaxMCS.setStatus("current")


class _WirelessInterface2ScanFrequencyListEighty_Type(DisplayString):
    """Custom type wirelessInterface2ScanFrequencyListEighty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterface2ScanFrequencyListEighty_Type.__name__ = "DisplayString"
_WirelessInterface2ScanFrequencyListEighty_Object = MibScalar
wirelessInterface2ScanFrequencyListEighty = _WirelessInterface2ScanFrequencyListEighty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 80),
    _WirelessInterface2ScanFrequencyListEighty_Type()
)
wirelessInterface2ScanFrequencyListEighty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2ScanFrequencyListEighty.setStatus("current")
_CambiumKeepAliveIface2_ObjectIdentity = ObjectIdentity
cambiumKeepAliveIface2 = _CambiumKeepAliveIface2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 84)
)


class _WirelessInterface2KeepAliveEnable_Type(Integer32):
    """Custom type wirelessInterface2KeepAliveEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface2KeepAliveEnable_Type.__name__ = "Integer32"
_WirelessInterface2KeepAliveEnable_Object = MibScalar
wirelessInterface2KeepAliveEnable = _WirelessInterface2KeepAliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 84, 1),
    _WirelessInterface2KeepAliveEnable_Type()
)
wirelessInterface2KeepAliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2KeepAliveEnable.setStatus("current")


class _WirelessInterface2KeepAliveEPTPEnable_Type(Integer32):
    """Custom type wirelessInterface2KeepAliveEPTPEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface2KeepAliveEPTPEnable_Type.__name__ = "Integer32"
_WirelessInterface2KeepAliveEPTPEnable_Object = MibScalar
wirelessInterface2KeepAliveEPTPEnable = _WirelessInterface2KeepAliveEPTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 84, 2),
    _WirelessInterface2KeepAliveEPTPEnable_Type()
)
wirelessInterface2KeepAliveEPTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2KeepAliveEPTPEnable.setStatus("current")


class _WirelessInterface2STAMaxDLMCSLimit_Type(Integer32):
    """Custom type wirelessInterface2STAMaxDLMCSLimit based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(16, 25),
        ValueRangeConstraint(255, 255),
    )


_WirelessInterface2STAMaxDLMCSLimit_Type.__name__ = "Integer32"
_WirelessInterface2STAMaxDLMCSLimit_Object = MibScalar
wirelessInterface2STAMaxDLMCSLimit = _WirelessInterface2STAMaxDLMCSLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 85),
    _WirelessInterface2STAMaxDLMCSLimit_Type()
)
wirelessInterface2STAMaxDLMCSLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2STAMaxDLMCSLimit.setStatus("current")


class _WirelessInterface2SuRxBfOff_Type(Integer32):
    """Custom type wirelessInterface2SuRxBfOff based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterface2SuRxBfOff_Type.__name__ = "Integer32"
_WirelessInterface2SuRxBfOff_Object = MibScalar
wirelessInterface2SuRxBfOff = _WirelessInterface2SuRxBfOff_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 12, 87),
    _WirelessInterface2SuRxBfOff_Type()
)
wirelessInterface2SuRxBfOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterface2SuRxBfOff.setStatus("current")
_Wlr_ObjectIdentity = ObjectIdentity
wlr = _Wlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 13)
)


class _WlrMUMIMOEnable_Type(Integer32):
    """Custom type wlrMUMIMOEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WlrMUMIMOEnable_Type.__name__ = "Integer32"
_WlrMUMIMOEnable_Object = MibScalar
wlrMUMIMOEnable = _WlrMUMIMOEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 13, 1),
    _WlrMUMIMOEnable_Type()
)
wlrMUMIMOEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrMUMIMOEnable.setStatus("current")
_L2Firewall_ObjectIdentity = ObjectIdentity
l2Firewall = _L2Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9)
)


class _L2FirewallEnable_Type(Integer32):
    """Custom type l2FirewallEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEnable_Type.__name__ = "Integer32"
_L2FirewallEnable_Object = MibScalar
l2FirewallEnable = _L2FirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 1),
    _L2FirewallEnable_Type()
)
l2FirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEnable.setStatus("current")
_L2FirewallTable_Object = MibTable
l2FirewallTable = _L2FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2)
)
if mibBuilder.loadTexts:
    l2FirewallTable.setStatus("current")
_L2FirewallEntry_Object = MibTableRow
l2FirewallEntry = _L2FirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1)
)
l2FirewallEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "l2FirewallEntryIndex"),
)
if mibBuilder.loadTexts:
    l2FirewallEntry.setStatus("current")


class _L2FirewallEntryIndex_Type(Integer32):
    """Custom type l2FirewallEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_L2FirewallEntryIndex_Type.__name__ = "Integer32"
_L2FirewallEntryIndex_Object = MibTableColumn
l2FirewallEntryIndex = _L2FirewallEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 1),
    _L2FirewallEntryIndex_Type()
)
l2FirewallEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryIndex.setStatus("current")


class _L2FirewallEntryName_Type(DisplayString):
    """Custom type l2FirewallEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_L2FirewallEntryName_Type.__name__ = "DisplayString"
_L2FirewallEntryName_Object = MibTableColumn
l2FirewallEntryName = _L2FirewallEntryName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 2),
    _L2FirewallEntryName_Type()
)
l2FirewallEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryName.setStatus("current")


class _L2FirewallEntryAction_Type(Integer32):
    """Custom type l2FirewallEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEntryAction_Type.__name__ = "Integer32"
_L2FirewallEntryAction_Object = MibTableColumn
l2FirewallEntryAction = _L2FirewallEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 3),
    _L2FirewallEntryAction_Type()
)
l2FirewallEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryAction.setStatus("current")


class _L2FirewallEntryInterface_Type(Integer32):
    """Custom type l2FirewallEntryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_L2FirewallEntryInterface_Type.__name__ = "Integer32"
_L2FirewallEntryInterface_Object = MibTableColumn
l2FirewallEntryInterface = _L2FirewallEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 4),
    _L2FirewallEntryInterface_Type()
)
l2FirewallEntryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryInterface.setStatus("current")


class _L2FirewallEntryLog_Type(Integer32):
    """Custom type l2FirewallEntryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEntryLog_Type.__name__ = "Integer32"
_L2FirewallEntryLog_Object = MibTableColumn
l2FirewallEntryLog = _L2FirewallEntryLog_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 5),
    _L2FirewallEntryLog_Type()
)
l2FirewallEntryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryLog.setStatus("current")


class _L2FirewallEntryEtherType_Type(Integer32):
    """Custom type l2FirewallEntryEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2FirewallEntryEtherType_Type.__name__ = "Integer32"
_L2FirewallEntryEtherType_Object = MibTableColumn
l2FirewallEntryEtherType = _L2FirewallEntryEtherType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 6),
    _L2FirewallEntryEtherType_Type()
)
l2FirewallEntryEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryEtherType.setStatus("current")


class _L2FirewallEntryVlanID_Type(Integer32):
    """Custom type l2FirewallEntryVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_L2FirewallEntryVlanID_Type.__name__ = "Integer32"
_L2FirewallEntryVlanID_Object = MibTableColumn
l2FirewallEntryVlanID = _L2FirewallEntryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 7),
    _L2FirewallEntryVlanID_Type()
)
l2FirewallEntryVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryVlanID.setStatus("current")


class _L2FirewallEntrySrcMAC_Type(DisplayString):
    """Custom type l2FirewallEntrySrcMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntrySrcMAC_Type.__name__ = "DisplayString"
_L2FirewallEntrySrcMAC_Object = MibTableColumn
l2FirewallEntrySrcMAC = _L2FirewallEntrySrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 8),
    _L2FirewallEntrySrcMAC_Type()
)
l2FirewallEntrySrcMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntrySrcMAC.setStatus("current")


class _L2FirewallEntrySrcMask_Type(DisplayString):
    """Custom type l2FirewallEntrySrcMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntrySrcMask_Type.__name__ = "DisplayString"
_L2FirewallEntrySrcMask_Object = MibTableColumn
l2FirewallEntrySrcMask = _L2FirewallEntrySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 9),
    _L2FirewallEntrySrcMask_Type()
)
l2FirewallEntrySrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntrySrcMask.setStatus("current")


class _L2FirewallEntryDstMAC_Type(DisplayString):
    """Custom type l2FirewallEntryDstMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntryDstMAC_Type.__name__ = "DisplayString"
_L2FirewallEntryDstMAC_Object = MibTableColumn
l2FirewallEntryDstMAC = _L2FirewallEntryDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 10),
    _L2FirewallEntryDstMAC_Type()
)
l2FirewallEntryDstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryDstMAC.setStatus("current")


class _L2FirewallEntryDstMask_Type(DisplayString):
    """Custom type l2FirewallEntryDstMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntryDstMask_Type.__name__ = "DisplayString"
_L2FirewallEntryDstMask_Object = MibTableColumn
l2FirewallEntryDstMask = _L2FirewallEntryDstMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 11),
    _L2FirewallEntryDstMask_Type()
)
l2FirewallEntryDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryDstMask.setStatus("current")


class _L2WanRemoteAccess_Type(Integer32):
    """Custom type l2WanRemoteAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2WanRemoteAccess_Type.__name__ = "Integer32"
_L2WanRemoteAccess_Object = MibScalar
l2WanRemoteAccess = _L2WanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 3),
    _L2WanRemoteAccess_Type()
)
l2WanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2WanRemoteAccess.setStatus("current")


class _L2SnmpLanRemoteAccess_Type(Integer32):
    """Custom type l2SnmpLanRemoteAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2SnmpLanRemoteAccess_Type.__name__ = "Integer32"
_L2SnmpLanRemoteAccess_Object = MibScalar
l2SnmpLanRemoteAccess = _L2SnmpLanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 4),
    _L2SnmpLanRemoteAccess_Type()
)
l2SnmpLanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2SnmpLanRemoteAccess.setStatus("current")


class _L2DHCPServersBelowSTA_Type(Integer32):
    """Custom type l2DHCPServersBelowSTA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2DHCPServersBelowSTA_Type.__name__ = "Integer32"
_L2DHCPServersBelowSTA_Object = MibScalar
l2DHCPServersBelowSTA = _L2DHCPServersBelowSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 5),
    _L2DHCPServersBelowSTA_Type()
)
l2DHCPServersBelowSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2DHCPServersBelowSTA.setStatus("current")


class _L2LanRemoteAccess_Type(Integer32):
    """Custom type l2LanRemoteAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2LanRemoteAccess_Type.__name__ = "Integer32"
_L2LanRemoteAccess_Object = MibScalar
l2LanRemoteAccess = _L2LanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 6),
    _L2LanRemoteAccess_Type()
)
l2LanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2LanRemoteAccess.setStatus("current")
_L3Firewall_ObjectIdentity = ObjectIdentity
l3Firewall = _L3Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10)
)


class _L3FirewallEnable_Type(Integer32):
    """Custom type l3FirewallEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEnable_Type.__name__ = "Integer32"
_L3FirewallEnable_Object = MibScalar
l3FirewallEnable = _L3FirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 1),
    _L3FirewallEnable_Type()
)
l3FirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEnable.setStatus("current")
_L3FirewallTable_Object = MibTable
l3FirewallTable = _L3FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2)
)
if mibBuilder.loadTexts:
    l3FirewallTable.setStatus("current")
_L3FirewallEntry_Object = MibTableRow
l3FirewallEntry = _L3FirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1)
)
l3FirewallEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "l3FirewallEntryIndex"),
)
if mibBuilder.loadTexts:
    l3FirewallEntry.setStatus("current")


class _L3FirewallEntryIndex_Type(Integer32):
    """Custom type l3FirewallEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_L3FirewallEntryIndex_Type.__name__ = "Integer32"
_L3FirewallEntryIndex_Object = MibTableColumn
l3FirewallEntryIndex = _L3FirewallEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 1),
    _L3FirewallEntryIndex_Type()
)
l3FirewallEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryIndex.setStatus("current")


class _L3FirewallEntryName_Type(DisplayString):
    """Custom type l3FirewallEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_L3FirewallEntryName_Type.__name__ = "DisplayString"
_L3FirewallEntryName_Object = MibTableColumn
l3FirewallEntryName = _L3FirewallEntryName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 2),
    _L3FirewallEntryName_Type()
)
l3FirewallEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryName.setStatus("current")


class _L3FirewallEntryAction_Type(Integer32):
    """Custom type l3FirewallEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEntryAction_Type.__name__ = "Integer32"
_L3FirewallEntryAction_Object = MibTableColumn
l3FirewallEntryAction = _L3FirewallEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 3),
    _L3FirewallEntryAction_Type()
)
l3FirewallEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryAction.setStatus("current")


class _L3FirewallEntryInterface_Type(Integer32):
    """Custom type l3FirewallEntryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_L3FirewallEntryInterface_Type.__name__ = "Integer32"
_L3FirewallEntryInterface_Object = MibTableColumn
l3FirewallEntryInterface = _L3FirewallEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 4),
    _L3FirewallEntryInterface_Type()
)
l3FirewallEntryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryInterface.setStatus("current")


class _L3FirewallEntryLog_Type(Integer32):
    """Custom type l3FirewallEntryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEntryLog_Type.__name__ = "Integer32"
_L3FirewallEntryLog_Object = MibTableColumn
l3FirewallEntryLog = _L3FirewallEntryLog_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 5),
    _L3FirewallEntryLog_Type()
)
l3FirewallEntryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryLog.setStatus("current")


class _L3FirewallEntryProtocol_Type(Integer32):
    """Custom type l3FirewallEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_L3FirewallEntryProtocol_Type.__name__ = "Integer32"
_L3FirewallEntryProtocol_Object = MibTableColumn
l3FirewallEntryProtocol = _L3FirewallEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 6),
    _L3FirewallEntryProtocol_Type()
)
l3FirewallEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryProtocol.setStatus("current")


class _L3FirewallEntryPort_Type(Integer32):
    """Custom type l3FirewallEntryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FirewallEntryPort_Type.__name__ = "Integer32"
_L3FirewallEntryPort_Object = MibTableColumn
l3FirewallEntryPort = _L3FirewallEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 7),
    _L3FirewallEntryPort_Type()
)
l3FirewallEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryPort.setStatus("current")
_L3FirewallEntrySrcIP_Type = IpAddress
_L3FirewallEntrySrcIP_Object = MibTableColumn
l3FirewallEntrySrcIP = _L3FirewallEntrySrcIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 8),
    _L3FirewallEntrySrcIP_Type()
)
l3FirewallEntrySrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntrySrcIP.setStatus("current")
_L3FirewallEntrySrcMask_Type = IpAddress
_L3FirewallEntrySrcMask_Object = MibTableColumn
l3FirewallEntrySrcMask = _L3FirewallEntrySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 9),
    _L3FirewallEntrySrcMask_Type()
)
l3FirewallEntrySrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntrySrcMask.setStatus("current")
_L3FirewallEntryDstIP_Type = IpAddress
_L3FirewallEntryDstIP_Object = MibTableColumn
l3FirewallEntryDstIP = _L3FirewallEntryDstIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 10),
    _L3FirewallEntryDstIP_Type()
)
l3FirewallEntryDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDstIP.setStatus("current")
_L3FirewallEntryDstMask_Type = IpAddress
_L3FirewallEntryDstMask_Object = MibTableColumn
l3FirewallEntryDstMask = _L3FirewallEntryDstMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 11),
    _L3FirewallEntryDstMask_Type()
)
l3FirewallEntryDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDstMask.setStatus("current")


class _L3FirewallEntryDSCP_Type(Integer32):
    """Custom type l3FirewallEntryDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_L3FirewallEntryDSCP_Type.__name__ = "Integer32"
_L3FirewallEntryDSCP_Object = MibTableColumn
l3FirewallEntryDSCP = _L3FirewallEntryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 12),
    _L3FirewallEntryDSCP_Type()
)
l3FirewallEntryDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDSCP.setStatus("current")


class _L3FirewallEntryToS_Type(Integer32):
    """Custom type l3FirewallEntryToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_L3FirewallEntryToS_Type.__name__ = "Integer32"
_L3FirewallEntryToS_Object = MibTableColumn
l3FirewallEntryToS = _L3FirewallEntryToS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 13),
    _L3FirewallEntryToS_Type()
)
l3FirewallEntryToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryToS.setStatus("current")


class _L3FirewallEntrySrcPort_Type(Integer32):
    """Custom type l3FirewallEntrySrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FirewallEntrySrcPort_Type.__name__ = "Integer32"
_L3FirewallEntrySrcPort_Object = MibTableColumn
l3FirewallEntrySrcPort = _L3FirewallEntrySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 14),
    _L3FirewallEntrySrcPort_Type()
)
l3FirewallEntrySrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntrySrcPort.setStatus("current")
_ConfQoS_ObjectIdentity = ObjectIdentity
confQoS = _ConfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11)
)


class _VoipEnable_Type(Integer32):
    """Custom type voipEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_VoipEnable_Type.__name__ = "Integer32"
_VoipEnable_Object = MibScalar
voipEnable = _VoipEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 1),
    _VoipEnable_Type()
)
voipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipEnable.setStatus("current")


class _QosEnable_Type(Integer32):
    """Custom type qosEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_QosEnable_Type.__name__ = "Integer32"
_QosEnable_Object = MibScalar
qosEnable = _QosEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 2),
    _QosEnable_Type()
)
qosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEnable.setStatus("current")
_ClassificationListTable_Object = MibTable
classificationListTable = _ClassificationListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3)
)
if mibBuilder.loadTexts:
    classificationListTable.setStatus("current")
_ClassificationListEntry_Object = MibTableRow
classificationListEntry = _ClassificationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1)
)
classificationListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "classificationRuleIndex"),
)
if mibBuilder.loadTexts:
    classificationListEntry.setStatus("current")


class _ClassificationRuleIndex_Type(Integer32):
    """Custom type classificationRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ClassificationRuleIndex_Type.__name__ = "Integer32"
_ClassificationRuleIndex_Object = MibTableColumn
classificationRuleIndex = _ClassificationRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 1),
    _ClassificationRuleIndex_Type()
)
classificationRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleIndex.setStatus("current")


class _ClassificationRuleType_Type(Integer32):
    """Custom type classificationRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 9),
    )


_ClassificationRuleType_Type.__name__ = "Integer32"
_ClassificationRuleType_Object = MibTableColumn
classificationRuleType = _ClassificationRuleType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 2),
    _ClassificationRuleType_Type()
)
classificationRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleType.setStatus("current")


class _ClassificationRuleValue_Type(Integer32):
    """Custom type classificationRuleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClassificationRuleValue_Type.__name__ = "Integer32"
_ClassificationRuleValue_Object = MibTableColumn
classificationRuleValue = _ClassificationRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 3),
    _ClassificationRuleValue_Type()
)
classificationRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleValue.setStatus("current")
_ClassificationRuleIP_Type = IpAddress
_ClassificationRuleIP_Object = MibTableColumn
classificationRuleIP = _ClassificationRuleIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 4),
    _ClassificationRuleIP_Type()
)
classificationRuleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleIP.setStatus("current")


class _ClassificationRuleMAC_Type(DisplayString):
    """Custom type classificationRuleMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_ClassificationRuleMAC_Type.__name__ = "DisplayString"
_ClassificationRuleMAC_Object = MibTableColumn
classificationRuleMAC = _ClassificationRuleMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 5),
    _ClassificationRuleMAC_Type()
)
classificationRuleMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleMAC.setStatus("current")


class _ClassificationRuleMask_Type(DisplayString):
    """Custom type classificationRuleMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 17),
    )


_ClassificationRuleMask_Type.__name__ = "DisplayString"
_ClassificationRuleMask_Object = MibTableColumn
classificationRuleMask = _ClassificationRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 6),
    _ClassificationRuleMask_Type()
)
classificationRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleMask.setStatus("current")


class _ClassificationRuleDirection_Type(Integer32):
    """Custom type classificationRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_ClassificationRuleDirection_Type.__name__ = "Integer32"
_ClassificationRuleDirection_Object = MibTableColumn
classificationRuleDirection = _ClassificationRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 7),
    _ClassificationRuleDirection_Type()
)
classificationRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleDirection.setStatus("current")


class _ClassificationRuleQueue_Type(Integer32):
    """Custom type classificationRuleQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_ClassificationRuleQueue_Type.__name__ = "Integer32"
_ClassificationRuleQueue_Object = MibTableColumn
classificationRuleQueue = _ClassificationRuleQueue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 8),
    _ClassificationRuleQueue_Type()
)
classificationRuleQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleQueue.setStatus("current")


class _McPriority_Type(Integer32):
    """Custom type mcPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_McPriority_Type.__name__ = "Integer32"
_McPriority_Object = MibScalar
mcPriority = _McPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 4),
    _McPriority_Type()
)
mcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPriority.setStatus("current")


class _BcPriority_Type(Integer32):
    """Custom type bcPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_BcPriority_Type.__name__ = "Integer32"
_BcPriority_Object = MibScalar
bcPriority = _BcPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 5),
    _BcPriority_Type()
)
bcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcPriority.setStatus("current")
_Dmz_ObjectIdentity = ObjectIdentity
dmz = _Dmz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12)
)


class _DmzEnable_Type(Integer32):
    """Custom type dmzEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DmzEnable_Type.__name__ = "Integer32"
_DmzEnable_Object = MibScalar
dmzEnable = _DmzEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12, 1),
    _DmzEnable_Type()
)
dmzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzEnable.setStatus("current")
_DmzIPAddress_Type = IpAddress
_DmzIPAddress_Object = MibScalar
dmzIPAddress = _DmzIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12, 2),
    _DmzIPAddress_Type()
)
dmzIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzIPAddress.setStatus("current")


class _DmzAllowICMP_Type(Integer32):
    """Custom type dmzAllowICMP based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DmzAllowICMP_Type.__name__ = "Integer32"
_DmzAllowICMP_Object = MibScalar
dmzAllowICMP = _DmzAllowICMP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12, 3),
    _DmzAllowICMP_Type()
)
dmzAllowICMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzAllowICMP.setStatus("current")
_PortForwarding_ObjectIdentity = ObjectIdentity
portForwarding = _PortForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13)
)


class _PortForwardingEntryEnable_Type(Integer32):
    """Custom type portForwardingEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_PortForwardingEntryEnable_Type.__name__ = "Integer32"
_PortForwardingEntryEnable_Object = MibScalar
portForwardingEntryEnable = _PortForwardingEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 1),
    _PortForwardingEntryEnable_Type()
)
portForwardingEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingEntryEnable.setStatus("current")
_PortForwardingTable_Object = MibTable
portForwardingTable = _PortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2)
)
if mibBuilder.loadTexts:
    portForwardingTable.setStatus("current")
_PortForwardingEntry_Object = MibTableRow
portForwardingEntry = _PortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1)
)
portForwardingEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "portForwardingTableEntryIndex"),
)
if mibBuilder.loadTexts:
    portForwardingEntry.setStatus("current")


class _PortForwardingTableEntryIndex_Type(Integer32):
    """Custom type portForwardingTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PortForwardingTableEntryIndex_Type.__name__ = "Integer32"
_PortForwardingTableEntryIndex_Object = MibTableColumn
portForwardingTableEntryIndex = _PortForwardingTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 1),
    _PortForwardingTableEntryIndex_Type()
)
portForwardingTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryIndex.setStatus("current")


class _PortForwardingTableEntryProtocol_Type(Integer32):
    """Custom type portForwardingTableEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_PortForwardingTableEntryProtocol_Type.__name__ = "Integer32"
_PortForwardingTableEntryProtocol_Object = MibTableColumn
portForwardingTableEntryProtocol = _PortForwardingTableEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 2),
    _PortForwardingTableEntryProtocol_Type()
)
portForwardingTableEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryProtocol.setStatus("current")


class _PortForwardingTableEntryWLANPortBegin_Type(Integer32):
    """Custom type portForwardingTableEntryWLANPortBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingTableEntryWLANPortBegin_Type.__name__ = "Integer32"
_PortForwardingTableEntryWLANPortBegin_Object = MibTableColumn
portForwardingTableEntryWLANPortBegin = _PortForwardingTableEntryWLANPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 3),
    _PortForwardingTableEntryWLANPortBegin_Type()
)
portForwardingTableEntryWLANPortBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryWLANPortBegin.setStatus("current")


class _PortForwardingTableEntryWLANPortEnd_Type(Integer32):
    """Custom type portForwardingTableEntryWLANPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingTableEntryWLANPortEnd_Type.__name__ = "Integer32"
_PortForwardingTableEntryWLANPortEnd_Object = MibTableColumn
portForwardingTableEntryWLANPortEnd = _PortForwardingTableEntryWLANPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 4),
    _PortForwardingTableEntryWLANPortEnd_Type()
)
portForwardingTableEntryWLANPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryWLANPortEnd.setStatus("current")
_PortForwardingTableEntryLANIP_Type = IpAddress
_PortForwardingTableEntryLANIP_Object = MibTableColumn
portForwardingTableEntryLANIP = _PortForwardingTableEntryLANIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 5),
    _PortForwardingTableEntryLANIP_Type()
)
portForwardingTableEntryLANIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryLANIP.setStatus("current")


class _PortForwardingTableEntryWLANPortMappedBegin_Type(Integer32):
    """Custom type portForwardingTableEntryWLANPortMappedBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingTableEntryWLANPortMappedBegin_Type.__name__ = "Integer32"
_PortForwardingTableEntryWLANPortMappedBegin_Object = MibTableColumn
portForwardingTableEntryWLANPortMappedBegin = _PortForwardingTableEntryWLANPortMappedBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 6),
    _PortForwardingTableEntryWLANPortMappedBegin_Type()
)
portForwardingTableEntryWLANPortMappedBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryWLANPortMappedBegin.setStatus("current")


class _PortForwardingSepMangIPEntryEnable_Type(Integer32):
    """Custom type portForwardingSepMangIPEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_PortForwardingSepMangIPEntryEnable_Type.__name__ = "Integer32"
_PortForwardingSepMangIPEntryEnable_Object = MibScalar
portForwardingSepMangIPEntryEnable = _PortForwardingSepMangIPEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 3),
    _PortForwardingSepMangIPEntryEnable_Type()
)
portForwardingSepMangIPEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPEntryEnable.setStatus("current")
_PortForwardingSepMangIPTable_Object = MibTable
portForwardingSepMangIPTable = _PortForwardingSepMangIPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4)
)
if mibBuilder.loadTexts:
    portForwardingSepMangIPTable.setStatus("current")
_PortForwardingSepMangIPEntry_Object = MibTableRow
portForwardingSepMangIPEntry = _PortForwardingSepMangIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1)
)
portForwardingSepMangIPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "portForwardingSepMangIPTableEntryIndex"),
)
if mibBuilder.loadTexts:
    portForwardingSepMangIPEntry.setStatus("current")


class _PortForwardingSepMangIPTableEntryIndex_Type(Integer32):
    """Custom type portForwardingSepMangIPTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PortForwardingSepMangIPTableEntryIndex_Type.__name__ = "Integer32"
_PortForwardingSepMangIPTableEntryIndex_Object = MibTableColumn
portForwardingSepMangIPTableEntryIndex = _PortForwardingSepMangIPTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 1),
    _PortForwardingSepMangIPTableEntryIndex_Type()
)
portForwardingSepMangIPTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryIndex.setStatus("current")


class _PortForwardingSepMangIPTableEntryProtocol_Type(Integer32):
    """Custom type portForwardingSepMangIPTableEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_PortForwardingSepMangIPTableEntryProtocol_Type.__name__ = "Integer32"
_PortForwardingSepMangIPTableEntryProtocol_Object = MibTableColumn
portForwardingSepMangIPTableEntryProtocol = _PortForwardingSepMangIPTableEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 2),
    _PortForwardingSepMangIPTableEntryProtocol_Type()
)
portForwardingSepMangIPTableEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryProtocol.setStatus("current")


class _PortForwardingSepMangIPTableEntryWLANPortBegin_Type(Integer32):
    """Custom type portForwardingSepMangIPTableEntryWLANPortBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingSepMangIPTableEntryWLANPortBegin_Type.__name__ = "Integer32"
_PortForwardingSepMangIPTableEntryWLANPortBegin_Object = MibTableColumn
portForwardingSepMangIPTableEntryWLANPortBegin = _PortForwardingSepMangIPTableEntryWLANPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 3),
    _PortForwardingSepMangIPTableEntryWLANPortBegin_Type()
)
portForwardingSepMangIPTableEntryWLANPortBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryWLANPortBegin.setStatus("current")


class _PortForwardingSepMangIPTableEntryWLANPortEnd_Type(Integer32):
    """Custom type portForwardingSepMangIPTableEntryWLANPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingSepMangIPTableEntryWLANPortEnd_Type.__name__ = "Integer32"
_PortForwardingSepMangIPTableEntryWLANPortEnd_Object = MibTableColumn
portForwardingSepMangIPTableEntryWLANPortEnd = _PortForwardingSepMangIPTableEntryWLANPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 4),
    _PortForwardingSepMangIPTableEntryWLANPortEnd_Type()
)
portForwardingSepMangIPTableEntryWLANPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryWLANPortEnd.setStatus("current")
_PortForwardingSepMangIPTableEntryLANIP_Type = IpAddress
_PortForwardingSepMangIPTableEntryLANIP_Object = MibTableColumn
portForwardingSepMangIPTableEntryLANIP = _PortForwardingSepMangIPTableEntryLANIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 5),
    _PortForwardingSepMangIPTableEntryLANIP_Type()
)
portForwardingSepMangIPTableEntryLANIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryLANIP.setStatus("current")


class _PortForwardingSepMangIPTableEntryWLANPortMappedBegin_Type(Integer32):
    """Custom type portForwardingSepMangIPTableEntryWLANPortMappedBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingSepMangIPTableEntryWLANPortMappedBegin_Type.__name__ = "Integer32"
_PortForwardingSepMangIPTableEntryWLANPortMappedBegin_Object = MibTableColumn
portForwardingSepMangIPTableEntryWLANPortMappedBegin = _PortForwardingSepMangIPTableEntryWLANPortMappedBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 4, 1, 6),
    _PortForwardingSepMangIPTableEntryWLANPortMappedBegin_Type()
)
portForwardingSepMangIPTableEntryWLANPortMappedBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingSepMangIPTableEntryWLANPortMappedBegin.setStatus("current")
_Vlans_ObjectIdentity = ObjectIdentity
vlans = _Vlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14)
)
_MembershipVLANTable_Object = MibTable
membershipVLANTable = _MembershipVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3)
)
if mibBuilder.loadTexts:
    membershipVLANTable.setStatus("current")
_MembershipVLANEntry_Object = MibTableRow
membershipVLANEntry = _MembershipVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1)
)
membershipVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "membershipVLANTableEntryIndex"),
)
if mibBuilder.loadTexts:
    membershipVLANEntry.setStatus("current")


class _MembershipVLANTableEntryIndex_Type(Integer32):
    """Custom type membershipVLANTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MembershipVLANTableEntryIndex_Type.__name__ = "Integer32"
_MembershipVLANTableEntryIndex_Object = MibTableColumn
membershipVLANTableEntryIndex = _MembershipVLANTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 1),
    _MembershipVLANTableEntryIndex_Type()
)
membershipVLANTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryIndex.setStatus("current")


class _MembershipVLANTableEntryVIDBegin_Type(Integer32):
    """Custom type membershipVLANTableEntryVIDBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MembershipVLANTableEntryVIDBegin_Type.__name__ = "Integer32"
_MembershipVLANTableEntryVIDBegin_Object = MibTableColumn
membershipVLANTableEntryVIDBegin = _MembershipVLANTableEntryVIDBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 2),
    _MembershipVLANTableEntryVIDBegin_Type()
)
membershipVLANTableEntryVIDBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryVIDBegin.setStatus("current")


class _MembershipVLANTableEntryVIDEnd_Type(Integer32):
    """Custom type membershipVLANTableEntryVIDEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MembershipVLANTableEntryVIDEnd_Type.__name__ = "Integer32"
_MembershipVLANTableEntryVIDEnd_Object = MibTableColumn
membershipVLANTableEntryVIDEnd = _MembershipVLANTableEntryVIDEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 3),
    _MembershipVLANTableEntryVIDEnd_Type()
)
membershipVLANTableEntryVIDEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryVIDEnd.setStatus("current")


class _MembershipVLANTableEntryInfo_Type(DisplayString):
    """Custom type membershipVLANTableEntryInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_MembershipVLANTableEntryInfo_Type.__name__ = "DisplayString"
_MembershipVLANTableEntryInfo_Object = MibTableColumn
membershipVLANTableEntryInfo = _MembershipVLANTableEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 4),
    _MembershipVLANTableEntryInfo_Type()
)
membershipVLANTableEntryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryInfo.setStatus("current")
_MappingVLANTable_Object = MibTable
mappingVLANTable = _MappingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5)
)
if mibBuilder.loadTexts:
    mappingVLANTable.setStatus("current")
_MappingVLANEntry_Object = MibTableRow
mappingVLANEntry = _MappingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1)
)
mappingVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "mappingVLANTableEntryIndex"),
)
if mibBuilder.loadTexts:
    mappingVLANEntry.setStatus("current")


class _MappingVLANTableEntryIndex_Type(Integer32):
    """Custom type mappingVLANTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MappingVLANTableEntryIndex_Type.__name__ = "Integer32"
_MappingVLANTableEntryIndex_Object = MibTableColumn
mappingVLANTableEntryIndex = _MappingVLANTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 1),
    _MappingVLANTableEntryIndex_Type()
)
mappingVLANTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntryIndex.setStatus("current")


class _MappingVLANTableEntryCVLAN_Type(Integer32):
    """Custom type mappingVLANTableEntryCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MappingVLANTableEntryCVLAN_Type.__name__ = "Integer32"
_MappingVLANTableEntryCVLAN_Object = MibTableColumn
mappingVLANTableEntryCVLAN = _MappingVLANTableEntryCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 2),
    _MappingVLANTableEntryCVLAN_Type()
)
mappingVLANTableEntryCVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntryCVLAN.setStatus("current")


class _MappingVLANTableEntrySVLAN_Type(Integer32):
    """Custom type mappingVLANTableEntrySVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MappingVLANTableEntrySVLAN_Type.__name__ = "Integer32"
_MappingVLANTableEntrySVLAN_Object = MibTableColumn
mappingVLANTableEntrySVLAN = _MappingVLANTableEntrySVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 3),
    _MappingVLANTableEntrySVLAN_Type()
)
mappingVLANTableEntrySVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntrySVLAN.setStatus("current")


class _MappingVLANTableEntryInfo_Type(DisplayString):
    """Custom type mappingVLANTableEntryInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_MappingVLANTableEntryInfo_Type.__name__ = "DisplayString"
_MappingVLANTableEntryInfo_Object = MibTableColumn
mappingVLANTableEntryInfo = _MappingVLANTableEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 4),
    _MappingVLANTableEntryInfo_Type()
)
mappingVLANTableEntryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntryInfo.setStatus("current")
_Dlkm_ObjectIdentity = ObjectIdentity
dlkm = _Dlkm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 15)
)


class _DlkmNATSIPHelpers_Type(Integer32):
    """Custom type dlkmNATSIPHelpers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DlkmNATSIPHelpers_Type.__name__ = "Integer32"
_DlkmNATSIPHelpers_Object = MibScalar
dlkmNATSIPHelpers = _DlkmNATSIPHelpers_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 15, 1),
    _DlkmNATSIPHelpers_Type()
)
dlkmNATSIPHelpers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlkmNATSIPHelpers.setStatus("current")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16)
)


class _StaticRoutesEnableMain_Type(Integer32):
    """Custom type staticRoutesEnableMain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_StaticRoutesEnableMain_Type.__name__ = "Integer32"
_StaticRoutesEnableMain_Object = MibScalar
staticRoutesEnableMain = _StaticRoutesEnableMain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 1),
    _StaticRoutesEnableMain_Type()
)
staticRoutesEnableMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutesEnableMain.setStatus("current")
_CambiumStaticRoutesCnfTable_Object = MibTable
cambiumStaticRoutesCnfTable = _CambiumStaticRoutesCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2)
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfTable.setStatus("current")
_CambiumStaticRoutesCnfEntry_Object = MibTableRow
cambiumStaticRoutesCnfEntry = _CambiumStaticRoutesCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1)
)
cambiumStaticRoutesCnfEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumStaticRoutesCnfIndex"),
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfEntry.setStatus("current")


class _CambiumStaticRoutesCnfIndex_Type(Integer32):
    """Custom type cambiumStaticRoutesCnfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CambiumStaticRoutesCnfIndex_Type.__name__ = "Integer32"
_CambiumStaticRoutesCnfIndex_Object = MibTableColumn
cambiumStaticRoutesCnfIndex = _CambiumStaticRoutesCnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 1),
    _CambiumStaticRoutesCnfIndex_Type()
)
cambiumStaticRoutesCnfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfIndex.setStatus("current")
_CambiumStaticRoutesCnfDestIP_Type = IpAddress
_CambiumStaticRoutesCnfDestIP_Object = MibTableColumn
cambiumStaticRoutesCnfDestIP = _CambiumStaticRoutesCnfDestIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 2),
    _CambiumStaticRoutesCnfDestIP_Type()
)
cambiumStaticRoutesCnfDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfDestIP.setStatus("current")
_CambiumStaticRoutesCnfGW_Type = IpAddress
_CambiumStaticRoutesCnfGW_Object = MibTableColumn
cambiumStaticRoutesCnfGW = _CambiumStaticRoutesCnfGW_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 3),
    _CambiumStaticRoutesCnfGW_Type()
)
cambiumStaticRoutesCnfGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfGW.setStatus("current")
_CambiumStaticRoutesCnfNetmask_Type = IpAddress
_CambiumStaticRoutesCnfNetmask_Object = MibTableColumn
cambiumStaticRoutesCnfNetmask = _CambiumStaticRoutesCnfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 4),
    _CambiumStaticRoutesCnfNetmask_Type()
)
cambiumStaticRoutesCnfNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfNetmask.setStatus("current")


class _CambiumStaticRoutesCnfEnbl_Type(Integer32):
    """Custom type cambiumStaticRoutesCnfEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumStaticRoutesCnfEnbl_Type.__name__ = "Integer32"
_CambiumStaticRoutesCnfEnbl_Object = MibTableColumn
cambiumStaticRoutesCnfEnbl = _CambiumStaticRoutesCnfEnbl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 5),
    _CambiumStaticRoutesCnfEnbl_Type()
)
cambiumStaticRoutesCnfEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfEnbl.setStatus("current")


class _CambiumStaticRoutesCnfInfo_Type(DisplayString):
    """Custom type cambiumStaticRoutesCnfInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CambiumStaticRoutesCnfInfo_Type.__name__ = "DisplayString"
_CambiumStaticRoutesCnfInfo_Object = MibTableColumn
cambiumStaticRoutesCnfInfo = _CambiumStaticRoutesCnfInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 6),
    _CambiumStaticRoutesCnfInfo_Type()
)
cambiumStaticRoutesCnfInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfInfo.setStatus("current")
_CambiumTelnetServer_ObjectIdentity = ObjectIdentity
cambiumTelnetServer = _CambiumTelnetServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 17)
)


class _CambiumTelnetServerEnable_Type(Integer32):
    """Custom type cambiumTelnetServerEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumTelnetServerEnable_Type.__name__ = "Integer32"
_CambiumTelnetServerEnable_Object = MibScalar
cambiumTelnetServerEnable = _CambiumTelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 17, 1),
    _CambiumTelnetServerEnable_Type()
)
cambiumTelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTelnetServerEnable.setStatus("current")


class _CambiumTelnetServerPort_Type(Integer32):
    """Custom type cambiumTelnetServerPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CambiumTelnetServerPort_Type.__name__ = "Integer32"
_CambiumTelnetServerPort_Object = MibScalar
cambiumTelnetServerPort = _CambiumTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 17, 2),
    _CambiumTelnetServerPort_Type()
)
cambiumTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTelnetServerPort.setStatus("current")
_CambiumDeviceAgent_ObjectIdentity = ObjectIdentity
cambiumDeviceAgent = _CambiumDeviceAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20)
)


class _CambiumDeviceAgentEnable_Type(Integer32):
    """Custom type cambiumDeviceAgentEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDeviceAgentEnable_Type.__name__ = "Integer32"
_CambiumDeviceAgentEnable_Object = MibScalar
cambiumDeviceAgentEnable = _CambiumDeviceAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 1),
    _CambiumDeviceAgentEnable_Type()
)
cambiumDeviceAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentEnable.setStatus("current")


class _CambiumDeviceAgentCNSURL_Type(OctetString):
    """Custom type cambiumDeviceAgentCNSURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDeviceAgentCNSURL_Type.__name__ = "OctetString"
_CambiumDeviceAgentCNSURL_Object = MibScalar
cambiumDeviceAgentCNSURL = _CambiumDeviceAgentCNSURL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 2),
    _CambiumDeviceAgentCNSURL_Type()
)
cambiumDeviceAgentCNSURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentCNSURL.setStatus("current")


class _CambiumCNSDeviceAgentID_Type(OctetString):
    """Custom type cambiumCNSDeviceAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCNSDeviceAgentID_Type.__name__ = "OctetString"
_CambiumCNSDeviceAgentID_Object = MibScalar
cambiumCNSDeviceAgentID = _CambiumCNSDeviceAgentID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 3),
    _CambiumCNSDeviceAgentID_Type()
)
cambiumCNSDeviceAgentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentID.setStatus("current")


class _CambiumCNSDeviceAgentPassword_Type(OctetString):
    """Custom type cambiumCNSDeviceAgentPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCNSDeviceAgentPassword_Type.__name__ = "OctetString"
_CambiumCNSDeviceAgentPassword_Object = MibScalar
cambiumCNSDeviceAgentPassword = _CambiumCNSDeviceAgentPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 4),
    _CambiumCNSDeviceAgentPassword_Type()
)
cambiumCNSDeviceAgentPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentPassword.setStatus("current")


class _CambiumDeviceAgentZeroTouchEnable_Type(Integer32):
    """Custom type cambiumDeviceAgentZeroTouchEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDeviceAgentZeroTouchEnable_Type.__name__ = "Integer32"
_CambiumDeviceAgentZeroTouchEnable_Object = MibScalar
cambiumDeviceAgentZeroTouchEnable = _CambiumDeviceAgentZeroTouchEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 5),
    _CambiumDeviceAgentZeroTouchEnable_Type()
)
cambiumDeviceAgentZeroTouchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentZeroTouchEnable.setStatus("current")


class _CambiumDeviceAgentMGMTRoutingEnable_Type(Integer32):
    """Custom type cambiumDeviceAgentMGMTRoutingEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDeviceAgentMGMTRoutingEnable_Type.__name__ = "Integer32"
_CambiumDeviceAgentMGMTRoutingEnable_Object = MibScalar
cambiumDeviceAgentMGMTRoutingEnable = _CambiumDeviceAgentMGMTRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 6),
    _CambiumDeviceAgentMGMTRoutingEnable_Type()
)
cambiumDeviceAgentMGMTRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentMGMTRoutingEnable.setStatus("current")
_Upnpd_ObjectIdentity = ObjectIdentity
upnpd = _Upnpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21)
)


class _NetworkUPNP_Type(Integer32):
    """Custom type networkUPNP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkUPNP_Type.__name__ = "Integer32"
_NetworkUPNP_Object = MibScalar
networkUPNP = _NetworkUPNP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21, 1),
    _NetworkUPNP_Type()
)
networkUPNP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkUPNP.setStatus("current")


class _NetworkNATPMP_Type(Integer32):
    """Custom type networkNATPMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkNATPMP_Type.__name__ = "Integer32"
_NetworkNATPMP_Object = MibScalar
networkNATPMP = _NetworkNATPMP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21, 2),
    _NetworkNATPMP_Type()
)
networkNATPMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkNATPMP.setStatus("current")
_Lldpd_ObjectIdentity = ObjectIdentity
lldpd = _Lldpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 23)
)


class _NetworkLLDP_Type(Integer32):
    """Custom type networkLLDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLLDP_Type.__name__ = "Integer32"
_NetworkLLDP_Object = MibScalar
networkLLDP = _NetworkLLDP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 23, 1),
    _NetworkLLDP_Type()
)
networkLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLLDP.setStatus("current")


class _NetworkLLDPMode_Type(Integer32):
    """Custom type networkLLDPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkLLDPMode_Type.__name__ = "Integer32"
_NetworkLLDPMode_Object = MibScalar
networkLLDPMode = _NetworkLLDPMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 23, 2),
    _NetworkLLDPMode_Type()
)
networkLLDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLLDPMode.setStatus("current")
_Mactelnet_ObjectIdentity = ObjectIdentity
mactelnet = _Mactelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 25)
)


class _NetworkMACTELNET_Type(Integer32):
    """Custom type networkMACTELNET based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkMACTELNET_Type.__name__ = "Integer32"
_NetworkMACTELNET_Object = MibScalar
networkMACTELNET = _NetworkMACTELNET_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 25, 1),
    _NetworkMACTELNET_Type()
)
networkMACTELNET.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMACTELNET.setStatus("current")


class _NetworkMACTELNETProto_Type(Integer32):
    """Custom type networkMACTELNETProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkMACTELNETProto_Type.__name__ = "Integer32"
_NetworkMACTELNETProto_Object = MibScalar
networkMACTELNETProto = _NetworkMACTELNETProto_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 25, 2),
    _NetworkMACTELNETProto_Type()
)
networkMACTELNETProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMACTELNETProto.setStatus("current")
_Licensed_ObjectIdentity = ObjectIdentity
licensed = _Licensed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27)
)


class _CambiumLicenseServerEnable_Type(Integer32):
    """Custom type cambiumLicenseServerEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLicenseServerEnable_Type.__name__ = "Integer32"
_CambiumLicenseServerEnable_Object = MibScalar
cambiumLicenseServerEnable = _CambiumLicenseServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 1),
    _CambiumLicenseServerEnable_Type()
)
cambiumLicenseServerEnable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerEnable.setStatus("obsolete")
_CambiumLicenseServerCloudLicensingID_Type = DisplayString
_CambiumLicenseServerCloudLicensingID_Object = MibScalar
cambiumLicenseServerCloudLicensingID = _CambiumLicenseServerCloudLicensingID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 2),
    _CambiumLicenseServerCloudLicensingID_Type()
)
cambiumLicenseServerCloudLicensingID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerCloudLicensingID.setStatus("obsolete")


class _CambiumLicenseServerStatus_Type(Integer32):
    """Custom type cambiumLicenseServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(2001, 2034),
    )


_CambiumLicenseServerStatus_Type.__name__ = "Integer32"
_CambiumLicenseServerStatus_Object = MibScalar
cambiumLicenseServerStatus = _CambiumLicenseServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 3),
    _CambiumLicenseServerStatus_Type()
)
cambiumLicenseServerStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerStatus.setStatus("obsolete")
_CambiumLicenseServerRefreshFail_Type = Integer32
_CambiumLicenseServerRefreshFail_Object = MibScalar
cambiumLicenseServerRefreshFail = _CambiumLicenseServerRefreshFail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 4),
    _CambiumLicenseServerRefreshFail_Type()
)
cambiumLicenseServerRefreshFail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerRefreshFail.setStatus("obsolete")
_CambiumLicenseServerUpdateFail_Type = Integer32
_CambiumLicenseServerUpdateFail_Object = MibScalar
cambiumLicenseServerUpdateFail = _CambiumLicenseServerUpdateFail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 5),
    _CambiumLicenseServerUpdateFail_Type()
)
cambiumLicenseServerUpdateFail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerUpdateFail.setStatus("obsolete")


class _CambiumLicenseServerProxyEnable_Type(Integer32):
    """Custom type cambiumLicenseServerProxyEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLicenseServerProxyEnable_Type.__name__ = "Integer32"
_CambiumLicenseServerProxyEnable_Object = MibScalar
cambiumLicenseServerProxyEnable = _CambiumLicenseServerProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 6),
    _CambiumLicenseServerProxyEnable_Type()
)
cambiumLicenseServerProxyEnable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerProxyEnable.setStatus("obsolete")
_CambiumLicenseServerProxyIP_Type = IpAddress
_CambiumLicenseServerProxyIP_Object = MibScalar
cambiumLicenseServerProxyIP = _CambiumLicenseServerProxyIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 7),
    _CambiumLicenseServerProxyIP_Type()
)
cambiumLicenseServerProxyIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerProxyIP.setStatus("obsolete")


class _CambiumLicenseServerProxyPort_Type(Integer32):
    """Custom type cambiumLicenseServerProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CambiumLicenseServerProxyPort_Type.__name__ = "Integer32"
_CambiumLicenseServerProxyPort_Object = MibScalar
cambiumLicenseServerProxyPort = _CambiumLicenseServerProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 27, 8),
    _CambiumLicenseServerProxyPort_Type()
)
cambiumLicenseServerProxyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cambiumLicenseServerProxyPort.setStatus("obsolete")
_Tr069_ObjectIdentity = ObjectIdentity
tr069 = _Tr069_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28)
)
_Tr069Local_ObjectIdentity = ObjectIdentity
tr069Local = _Tr069Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1)
)


class _CambiumTR069Enable_Type(Integer32):
    """Custom type cambiumTR069Enable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumTR069Enable_Type.__name__ = "Integer32"
_CambiumTR069Enable_Object = MibScalar
cambiumTR069Enable = _CambiumTR069Enable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1, 1),
    _CambiumTR069Enable_Type()
)
cambiumTR069Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTR069Enable.setStatus("current")


class _CambiumTR069Interface_Type(OctetString):
    """Custom type cambiumTR069Interface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumTR069Interface_Type.__name__ = "OctetString"
_CambiumTR069Interface_Object = MibScalar
cambiumTR069Interface = _CambiumTR069Interface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1, 2),
    _CambiumTR069Interface_Type()
)
cambiumTR069Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTR069Interface.setStatus("current")


class _CambiumTR069Port_Type(Integer32):
    """Custom type cambiumTR069Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CambiumTR069Port_Type.__name__ = "Integer32"
_CambiumTR069Port_Object = MibScalar
cambiumTR069Port = _CambiumTR069Port_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1, 3),
    _CambiumTR069Port_Type()
)
cambiumTR069Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTR069Port.setStatus("current")


class _CambiumTR069Username_Type(DisplayString):
    """Custom type cambiumTR069Username based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CambiumTR069Username_Type.__name__ = "DisplayString"
_CambiumTR069Username_Object = MibScalar
cambiumTR069Username = _CambiumTR069Username_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1, 4),
    _CambiumTR069Username_Type()
)
cambiumTR069Username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTR069Username.setStatus("current")


class _CambiumTR069Password_Type(OctetString):
    """Custom type cambiumTR069Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CambiumTR069Password_Type.__name__ = "OctetString"
_CambiumTR069Password_Object = MibScalar
cambiumTR069Password = _CambiumTR069Password_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 1, 5),
    _CambiumTR069Password_Type()
)
cambiumTR069Password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTR069Password.setStatus("current")
_Tr069ACS_ObjectIdentity = ObjectIdentity
tr069ACS = _Tr069ACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 2)
)


class _CambiumTR069ACSURL_Type(DisplayString):
    """Custom type cambiumTR069ACSURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CambiumTR069ACSURL_Type.__name__ = "DisplayString"
_CambiumTR069ACSURL_Object = MibScalar
cambiumTR069ACSURL = _CambiumTR069ACSURL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 2, 1),
    _CambiumTR069ACSURL_Type()
)
cambiumTR069ACSURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTR069ACSURL.setStatus("current")


class _CambiumTR069ACSUsername_Type(DisplayString):
    """Custom type cambiumTR069ACSUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CambiumTR069ACSUsername_Type.__name__ = "DisplayString"
_CambiumTR069ACSUsername_Object = MibScalar
cambiumTR069ACSUsername = _CambiumTR069ACSUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 2, 2),
    _CambiumTR069ACSUsername_Type()
)
cambiumTR069ACSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTR069ACSUsername.setStatus("current")


class _CambiumTR069ACSPassword_Type(OctetString):
    """Custom type cambiumTR069ACSPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CambiumTR069ACSPassword_Type.__name__ = "OctetString"
_CambiumTR069ACSPassword_Object = MibScalar
cambiumTR069ACSPassword = _CambiumTR069ACSPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 2, 3),
    _CambiumTR069ACSPassword_Type()
)
cambiumTR069ACSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTR069ACSPassword.setStatus("current")
_CambiumTR069Interval_Type = Integer32
_CambiumTR069Interval_Object = MibScalar
cambiumTR069Interval = _CambiumTR069Interval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 28, 2, 4),
    _CambiumTR069Interval_Type()
)
cambiumTR069Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumTR069Interval.setStatus("current")
_Bonding_ObjectIdentity = ObjectIdentity
bonding = _Bonding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 30)
)


class _CambiumChannelBondingEnable_Type(Integer32):
    """Custom type cambiumChannelBondingEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumChannelBondingEnable_Type.__name__ = "Integer32"
_CambiumChannelBondingEnable_Object = MibScalar
cambiumChannelBondingEnable = _CambiumChannelBondingEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 30, 1),
    _CambiumChannelBondingEnable_Type()
)
cambiumChannelBondingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumChannelBondingEnable.setStatus("current")
_AccelerationEngine_ObjectIdentity = ObjectIdentity
accelerationEngine = _AccelerationEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 31)
)


class _CambiumAccelerationEngine_Type(Integer32):
    """Custom type cambiumAccelerationEngine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CambiumAccelerationEngine_Type.__name__ = "Integer32"
_CambiumAccelerationEngine_Object = MibScalar
cambiumAccelerationEngine = _CambiumAccelerationEngine_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 31, 1),
    _CambiumAccelerationEngine_Type()
)
cambiumAccelerationEngine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumAccelerationEngine.setStatus("current")
_CambiumDCS_ObjectIdentity = ObjectIdentity
cambiumDCS = _CambiumDCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32)
)


class _DcsEnable_Type(Integer32):
    """Custom type dcsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_DcsEnable_Type.__name__ = "Integer32"
_DcsEnable_Object = MibScalar
dcsEnable = _DcsEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 1),
    _DcsEnable_Type()
)
dcsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsEnable.setStatus("current")


class _DcsLogFile_Type(DisplayString):
    """Custom type dcsLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_DcsLogFile_Type.__name__ = "DisplayString"
_DcsLogFile_Object = MibScalar
dcsLogFile = _DcsLogFile_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 2),
    _DcsLogFile_Type()
)
dcsLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcsLogFile.setStatus("current")


class _DcsFrequencyListFive_Type(DisplayString):
    """Custom type dcsFrequencyListFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_DcsFrequencyListFive_Type.__name__ = "DisplayString"
_DcsFrequencyListFive_Object = MibScalar
dcsFrequencyListFive = _DcsFrequencyListFive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 3),
    _DcsFrequencyListFive_Type()
)
dcsFrequencyListFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsFrequencyListFive.setStatus("current")


class _DcsFrequencyListTen_Type(DisplayString):
    """Custom type dcsFrequencyListTen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_DcsFrequencyListTen_Type.__name__ = "DisplayString"
_DcsFrequencyListTen_Object = MibScalar
dcsFrequencyListTen = _DcsFrequencyListTen_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 4),
    _DcsFrequencyListTen_Type()
)
dcsFrequencyListTen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsFrequencyListTen.setStatus("current")


class _DcsFrequencyListTwenty_Type(DisplayString):
    """Custom type dcsFrequencyListTwenty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_DcsFrequencyListTwenty_Type.__name__ = "DisplayString"
_DcsFrequencyListTwenty_Object = MibScalar
dcsFrequencyListTwenty = _DcsFrequencyListTwenty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 5),
    _DcsFrequencyListTwenty_Type()
)
dcsFrequencyListTwenty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsFrequencyListTwenty.setStatus("current")


class _DcsFrequencyListForty_Type(DisplayString):
    """Custom type dcsFrequencyListForty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_DcsFrequencyListForty_Type.__name__ = "DisplayString"
_DcsFrequencyListForty_Object = MibScalar
dcsFrequencyListForty = _DcsFrequencyListForty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 6),
    _DcsFrequencyListForty_Type()
)
dcsFrequencyListForty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsFrequencyListForty.setStatus("current")


class _DcsFrequencyListEighty_Type(DisplayString):
    """Custom type dcsFrequencyListEighty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_DcsFrequencyListEighty_Type.__name__ = "DisplayString"
_DcsFrequencyListEighty_Object = MibScalar
dcsFrequencyListEighty = _DcsFrequencyListEighty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 7),
    _DcsFrequencyListEighty_Type()
)
dcsFrequencyListEighty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsFrequencyListEighty.setStatus("current")


class _DcsSwitchThreshold_Type(Integer32):
    """Custom type dcsSwitchThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12),
    )


_DcsSwitchThreshold_Type.__name__ = "Integer32"
_DcsSwitchThreshold_Object = MibScalar
dcsSwitchThreshold = _DcsSwitchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 8),
    _DcsSwitchThreshold_Type()
)
dcsSwitchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsSwitchThreshold.setStatus("current")


class _DcsSwitchMinHoldTime_Type(Integer32):
    """Custom type dcsSwitchMinHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 300),
    )


_DcsSwitchMinHoldTime_Type.__name__ = "Integer32"
_DcsSwitchMinHoldTime_Object = MibScalar
dcsSwitchMinHoldTime = _DcsSwitchMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 9),
    _DcsSwitchMinHoldTime_Type()
)
dcsSwitchMinHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsSwitchMinHoldTime.setStatus("current")


class _DcsThroughputDropThreshold_Type(Integer32):
    """Custom type dcsThroughputDropThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_DcsThroughputDropThreshold_Type.__name__ = "Integer32"
_DcsThroughputDropThreshold_Object = MibScalar
dcsThroughputDropThreshold = _DcsThroughputDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 10),
    _DcsThroughputDropThreshold_Type()
)
dcsThroughputDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsThroughputDropThreshold.setStatus("current")


class _DcsBandwidthMask_Type(Integer32):
    """Custom type dcsBandwidthMask based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DcsBandwidthMask_Type.__name__ = "Integer32"
_DcsBandwidthMask_Object = MibScalar
dcsBandwidthMask = _DcsBandwidthMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 32, 11),
    _DcsBandwidthMask_Type()
)
dcsBandwidthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcsBandwidthMask.setStatus("current")
_CambiumGPSConfig_ObjectIdentity = ObjectIdentity
cambiumGPSConfig = _CambiumGPSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 33)
)


class _CambiumGPSConfigResetTimeout_Type(Integer32):
    """Custom type cambiumGPSConfigResetTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_CambiumGPSConfigResetTimeout_Type.__name__ = "Integer32"
_CambiumGPSConfigResetTimeout_Object = MibScalar
cambiumGPSConfigResetTimeout = _CambiumGPSConfigResetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 33, 4),
    _CambiumGPSConfigResetTimeout_Type()
)
cambiumGPSConfigResetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumGPSConfigResetTimeout.setStatus("current")
_Vmsagent_ObjectIdentity = ObjectIdentity
vmsagent = _Vmsagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34)
)


class _VmsagentEnable_Type(Integer32):
    """Custom type vmsagentEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_VmsagentEnable_Type.__name__ = "Integer32"
_VmsagentEnable_Object = MibScalar
vmsagentEnable = _VmsagentEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 1),
    _VmsagentEnable_Type()
)
vmsagentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentEnable.setStatus("current")


class _VmsagentVMSType_Type(Integer32):
    """Custom type vmsagentVMSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VmsagentVMSType_Type.__name__ = "Integer32"
_VmsagentVMSType_Object = MibScalar
vmsagentVMSType = _VmsagentVMSType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 2),
    _VmsagentVMSType_Type()
)
vmsagentVMSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentVMSType.setStatus("current")


class _VmsagentVMSAddr_Type(OctetString):
    """Custom type vmsagentVMSAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmsagentVMSAddr_Type.__name__ = "OctetString"
_VmsagentVMSAddr_Object = MibScalar
vmsagentVMSAddr = _VmsagentVMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 3),
    _VmsagentVMSAddr_Type()
)
vmsagentVMSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentVMSAddr.setStatus("current")


class _VmsagentVMSPort_Type(Integer32):
    """Custom type vmsagentVMSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmsagentVMSPort_Type.__name__ = "Integer32"
_VmsagentVMSPort_Object = MibScalar
vmsagentVMSPort = _VmsagentVMSPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 4),
    _VmsagentVMSPort_Type()
)
vmsagentVMSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentVMSPort.setStatus("current")


class _VmsagentUsername_Type(DisplayString):
    """Custom type vmsagentUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmsagentUsername_Type.__name__ = "DisplayString"
_VmsagentUsername_Object = MibScalar
vmsagentUsername = _VmsagentUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 5),
    _VmsagentUsername_Type()
)
vmsagentUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentUsername.setStatus("current")


class _VmsagentPassword_Type(OctetString):
    """Custom type vmsagentPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmsagentPassword_Type.__name__ = "OctetString"
_VmsagentPassword_Object = MibScalar
vmsagentPassword = _VmsagentPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 6),
    _VmsagentPassword_Type()
)
vmsagentPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsagentPassword.setStatus("current")


class _CnvisionVMSPreviewHash_Type(DisplayString):
    """Custom type cnvisionVMSPreviewHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CnvisionVMSPreviewHash_Type.__name__ = "DisplayString"
_CnvisionVMSPreviewHash_Object = MibScalar
cnvisionVMSPreviewHash = _CnvisionVMSPreviewHash_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 34, 7),
    _CnvisionVMSPreviewHash_Type()
)
cnvisionVMSPreviewHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvisionVMSPreviewHash.setStatus("current")
_CambiumNSS_ObjectIdentity = ObjectIdentity
cambiumNSS = _CambiumNSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35)
)


class _CambiumNSSAcceleratedConn_Type(Integer32):
    """Custom type cambiumNSSAcceleratedConn based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(8192, 8192),
    )


_CambiumNSSAcceleratedConn_Type.__name__ = "Integer32"
_CambiumNSSAcceleratedConn_Object = MibScalar
cambiumNSSAcceleratedConn = _CambiumNSSAcceleratedConn_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35, 1),
    _CambiumNSSAcceleratedConn_Type()
)
cambiumNSSAcceleratedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumNSSAcceleratedConn.setStatus("current")


class _CambiumNSSAcceleratedIPv4Conn_Type(Integer32):
    """Custom type cambiumNSSAcceleratedIPv4Conn based on Integer32"""
    defaultValue = 7168

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(3072, 3072),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(5120, 5120),
        ValueRangeConstraint(6144, 6144),
        ValueRangeConstraint(7168, 7168),
    )


_CambiumNSSAcceleratedIPv4Conn_Type.__name__ = "Integer32"
_CambiumNSSAcceleratedIPv4Conn_Object = MibScalar
cambiumNSSAcceleratedIPv4Conn = _CambiumNSSAcceleratedIPv4Conn_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35, 2),
    _CambiumNSSAcceleratedIPv4Conn_Type()
)
cambiumNSSAcceleratedIPv4Conn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumNSSAcceleratedIPv4Conn.setStatus("current")


class _CambiumNSSAcceleratedIPv6Conn_Type(Integer32):
    """Custom type cambiumNSSAcceleratedIPv6Conn based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(3072, 3072),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(5120, 5120),
        ValueRangeConstraint(6144, 6144),
        ValueRangeConstraint(7168, 7168),
    )


_CambiumNSSAcceleratedIPv6Conn_Type.__name__ = "Integer32"
_CambiumNSSAcceleratedIPv6Conn_Object = MibScalar
cambiumNSSAcceleratedIPv6Conn = _CambiumNSSAcceleratedIPv6Conn_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35, 3),
    _CambiumNSSAcceleratedIPv6Conn_Type()
)
cambiumNSSAcceleratedIPv6Conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumNSSAcceleratedIPv6Conn.setStatus("current")


class _CambiumNSSMcastFloodDestAth_Type(Integer32):
    """Custom type cambiumNSSMcastFloodDestAth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16),
    )


_CambiumNSSMcastFloodDestAth_Type.__name__ = "Integer32"
_CambiumNSSMcastFloodDestAth_Object = MibScalar
cambiumNSSMcastFloodDestAth = _CambiumNSSMcastFloodDestAth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35, 4),
    _CambiumNSSMcastFloodDestAth_Type()
)
cambiumNSSMcastFloodDestAth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumNSSMcastFloodDestAth.setStatus("current")


class _CambiumNSSMcastFloodDestEth_Type(Integer32):
    """Custom type cambiumNSSMcastFloodDestEth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16),
    )


_CambiumNSSMcastFloodDestEth_Type.__name__ = "Integer32"
_CambiumNSSMcastFloodDestEth_Object = MibScalar
cambiumNSSMcastFloodDestEth = _CambiumNSSMcastFloodDestEth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 35, 5),
    _CambiumNSSMcastFloodDestEth_Type()
)
cambiumNSSMcastFloodDestEth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumNSSMcastFloodDestEth.setStatus("current")
_Dpi_ObjectIdentity = ObjectIdentity
dpi = _Dpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36)
)


class _DpiEnable_Type(Integer32):
    """Custom type dpiEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DpiEnable_Type.__name__ = "Integer32"
_DpiEnable_Object = MibScalar
dpiEnable = _DpiEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 1),
    _DpiEnable_Type()
)
dpiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiEnable.setStatus("current")


class _DpiQoSEnable_Type(Integer32):
    """Custom type dpiQoSEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DpiQoSEnable_Type.__name__ = "Integer32"
_DpiQoSEnable_Object = MibScalar
dpiQoSEnable = _DpiQoSEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 2),
    _DpiQoSEnable_Type()
)
dpiQoSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiQoSEnable.setStatus("current")


class _DpiLogLevel_Type(DisplayString):
    """Custom type dpiLogLevel based on DisplayString"""
    defaultValue = OctetString("system")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DpiLogLevel_Type.__name__ = "DisplayString"
_DpiLogLevel_Object = MibScalar
dpiLogLevel = _DpiLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 3),
    _DpiLogLevel_Type()
)
dpiLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogLevel.setStatus("current")


class _DpiLogComponents_Type(DisplayString):
    """Custom type dpiLogComponents based on DisplayString"""
    defaultValue = OctetString("all")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DpiLogComponents_Type.__name__ = "DisplayString"
_DpiLogComponents_Object = MibScalar
dpiLogComponents = _DpiLogComponents_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 4),
    _DpiLogComponents_Type()
)
dpiLogComponents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiLogComponents.setStatus("current")
_DpiQoSAppRulesTable_Object = MibTable
dpiQoSAppRulesTable = _DpiQoSAppRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15)
)
if mibBuilder.loadTexts:
    dpiQoSAppRulesTable.setStatus("current")
_DpiQoSAppRulesEntry_Object = MibTableRow
dpiQoSAppRulesEntry = _DpiQoSAppRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15, 1)
)
dpiQoSAppRulesEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dpiQoSAppRulesIndex"),
)
if mibBuilder.loadTexts:
    dpiQoSAppRulesEntry.setStatus("current")


class _DpiQoSAppRulesIndex_Type(Integer32):
    """Custom type dpiQoSAppRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DpiQoSAppRulesIndex_Type.__name__ = "Integer32"
_DpiQoSAppRulesIndex_Object = MibTableColumn
dpiQoSAppRulesIndex = _DpiQoSAppRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15, 1, 1),
    _DpiQoSAppRulesIndex_Type()
)
dpiQoSAppRulesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiQoSAppRulesIndex.setStatus("current")


class _DpiQoSAppID_Type(Integer32):
    """Custom type dpiQoSAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpiQoSAppID_Type.__name__ = "Integer32"
_DpiQoSAppID_Object = MibTableColumn
dpiQoSAppID = _DpiQoSAppID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15, 1, 2),
    _DpiQoSAppID_Type()
)
dpiQoSAppID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiQoSAppID.setStatus("current")


class _DpiQoSAppPriority_Type(Integer32):
    """Custom type dpiQoSAppPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DpiQoSAppPriority_Type.__name__ = "Integer32"
_DpiQoSAppPriority_Object = MibTableColumn
dpiQoSAppPriority = _DpiQoSAppPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15, 1, 3),
    _DpiQoSAppPriority_Type()
)
dpiQoSAppPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiQoSAppPriority.setStatus("current")


class _DpiQoSAppRuleType_Type(Integer32):
    """Custom type dpiQoSAppRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DpiQoSAppRuleType_Type.__name__ = "Integer32"
_DpiQoSAppRuleType_Object = MibTableColumn
dpiQoSAppRuleType = _DpiQoSAppRuleType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 36, 15, 1, 4),
    _DpiQoSAppRuleType_Type()
)
dpiQoSAppRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpiQoSAppRuleType.setStatus("current")
_Cambiumpmp80211SystemActions_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemActions = _Cambiumpmp80211SystemActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4)
)


class _Cambiumpmp80211DeviceReboot_Type(Integer32):
    """Custom type cambiumpmp80211DeviceReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211DeviceReboot_Type.__name__ = "Integer32"
_Cambiumpmp80211DeviceReboot_Object = MibScalar
cambiumpmp80211DeviceReboot = _Cambiumpmp80211DeviceReboot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 1),
    _Cambiumpmp80211DeviceReboot_Type()
)
cambiumpmp80211DeviceReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211DeviceReboot.setStatus("current")


class _Cambiumpmp80211ConfigurationReset_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cambiumpmp80211ConfigurationReset_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationReset_Object = MibScalar
cambiumpmp80211ConfigurationReset = _Cambiumpmp80211ConfigurationReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 2),
    _Cambiumpmp80211ConfigurationReset_Type()
)
cambiumpmp80211ConfigurationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationReset.setStatus("current")


class _Cambiumpmp80211ConfigurationSave_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationSave_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationSave_Object = MibScalar
cambiumpmp80211ConfigurationSave = _Cambiumpmp80211ConfigurationSave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 3),
    _Cambiumpmp80211ConfigurationSave_Type()
)
cambiumpmp80211ConfigurationSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationSave.setStatus("current")


class _Cambiumpmp80211ConfigurationApply_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationApply_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationApply_Object = MibScalar
cambiumpmp80211ConfigurationApply = _Cambiumpmp80211ConfigurationApply_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 4),
    _Cambiumpmp80211ConfigurationApply_Type()
)
cambiumpmp80211ConfigurationApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationApply.setStatus("current")


class _Cambiumpmp80211ConfigurationDiscard_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationDiscard_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationDiscard_Object = MibScalar
cambiumpmp80211ConfigurationDiscard = _Cambiumpmp80211ConfigurationDiscard_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 5),
    _Cambiumpmp80211ConfigurationDiscard_Type()
)
cambiumpmp80211ConfigurationDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationDiscard.setStatus("current")


class _Cambiumpmp80211ConfigurationState_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cambiumpmp80211ConfigurationState_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationState_Object = MibScalar
cambiumpmp80211ConfigurationState = _Cambiumpmp80211ConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 6),
    _Cambiumpmp80211ConfigurationState_Type()
)
cambiumpmp80211ConfigurationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationState.setStatus("current")
_Cambiumpmp80211SoftwareUpdate_Type = OctetString
_Cambiumpmp80211SoftwareUpdate_Object = MibScalar
cambiumpmp80211SoftwareUpdate = _Cambiumpmp80211SoftwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 7),
    _Cambiumpmp80211SoftwareUpdate_Type()
)
cambiumpmp80211SoftwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdate.setStatus("current")


class _Cambiumpmp80211SoftwareUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211SoftwareUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cambiumpmp80211SoftwareUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211SoftwareUpdateStatus_Object = MibScalar
cambiumpmp80211SoftwareUpdateStatus = _Cambiumpmp80211SoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 8),
    _Cambiumpmp80211SoftwareUpdateStatus_Type()
)
cambiumpmp80211SoftwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateStatus.setStatus("current")


class _Cambiumpmp80211STAListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211STAListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211STAListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211STAListUpdate_Object = MibScalar
cambiumpmp80211STAListUpdate = _Cambiumpmp80211STAListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 9),
    _Cambiumpmp80211STAListUpdate_Type()
)
cambiumpmp80211STAListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STAListUpdate.setStatus("current")


class _Cambiumpmp80211STAListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211STAListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211STAListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211STAListUpdateStatus_Object = MibScalar
cambiumpmp80211STAListUpdateStatus = _Cambiumpmp80211STAListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 10),
    _Cambiumpmp80211STAListUpdateStatus_Type()
)
cambiumpmp80211STAListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STAListUpdateStatus.setStatus("current")


class _Cambiumpmp80211APListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211APListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211APListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211APListUpdate_Object = MibScalar
cambiumpmp80211APListUpdate = _Cambiumpmp80211APListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 11),
    _Cambiumpmp80211APListUpdate_Type()
)
cambiumpmp80211APListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211APListUpdate.setStatus("current")


class _Cambiumpmp80211APListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211APListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211APListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211APListUpdateStatus_Object = MibScalar
cambiumpmp80211APListUpdateStatus = _Cambiumpmp80211APListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 12),
    _Cambiumpmp80211APListUpdateStatus_Type()
)
cambiumpmp80211APListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211APListUpdateStatus.setStatus("current")
_Cambiumpmp80211SoftwareUpdateError_Type = Integer32
_Cambiumpmp80211SoftwareUpdateError_Object = MibScalar
cambiumpmp80211SoftwareUpdateError = _Cambiumpmp80211SoftwareUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 13),
    _Cambiumpmp80211SoftwareUpdateError_Type()
)
cambiumpmp80211SoftwareUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateError.setStatus("current")


class _Cambiumpmp80211StatsPerSTAListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211StatsPerSTAListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211StatsPerSTAListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211StatsPerSTAListUpdateStatus_Object = MibScalar
cambiumpmp80211StatsPerSTAListUpdateStatus = _Cambiumpmp80211StatsPerSTAListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 14),
    _Cambiumpmp80211StatsPerSTAListUpdateStatus_Type()
)
cambiumpmp80211StatsPerSTAListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211StatsPerSTAListUpdateStatus.setStatus("current")


class _Cambiumpmp80211StatsPerSTAListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211StatsPerSTAListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211StatsPerSTAListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211StatsPerSTAListUpdate_Object = MibScalar
cambiumpmp80211StatsPerSTAListUpdate = _Cambiumpmp80211StatsPerSTAListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 15),
    _Cambiumpmp80211StatsPerSTAListUpdate_Type()
)
cambiumpmp80211StatsPerSTAListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211StatsPerSTAListUpdate.setStatus("current")


class _Cambiumpmp80211STADisconnect_Type(Integer32):
    """Custom type cambiumpmp80211STADisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Cambiumpmp80211STADisconnect_Type.__name__ = "Integer32"
_Cambiumpmp80211STADisconnect_Object = MibScalar
cambiumpmp80211STADisconnect = _Cambiumpmp80211STADisconnect_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 16),
    _Cambiumpmp80211STADisconnect_Type()
)
cambiumpmp80211STADisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STADisconnect.setStatus("current")


class _Cambiumpmp80211GPSAutopopulate_Type(Integer32):
    """Custom type cambiumpmp80211GPSAutopopulate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211GPSAutopopulate_Type.__name__ = "Integer32"
_Cambiumpmp80211GPSAutopopulate_Object = MibScalar
cambiumpmp80211GPSAutopopulate = _Cambiumpmp80211GPSAutopopulate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 17),
    _Cambiumpmp80211GPSAutopopulate_Type()
)
cambiumpmp80211GPSAutopopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211GPSAutopopulate.setStatus("current")


class _Cambiumpmp80211SoftwareUpdateErrorStr_Type(DisplayString):
    """Custom type cambiumpmp80211SoftwareUpdateErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cambiumpmp80211SoftwareUpdateErrorStr_Type.__name__ = "DisplayString"
_Cambiumpmp80211SoftwareUpdateErrorStr_Object = MibScalar
cambiumpmp80211SoftwareUpdateErrorStr = _Cambiumpmp80211SoftwareUpdateErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 18),
    _Cambiumpmp80211SoftwareUpdateErrorStr_Type()
)
cambiumpmp80211SoftwareUpdateErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateErrorStr.setStatus("current")
_Cambiumpmp80211GpsFirmwareUpdate_Type = OctetString
_Cambiumpmp80211GpsFirmwareUpdate_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdate = _Cambiumpmp80211GpsFirmwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 19),
    _Cambiumpmp80211GpsFirmwareUpdate_Type()
)
cambiumpmp80211GpsFirmwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdate.setStatus("current")


class _Cambiumpmp80211GpsFirmwareUpdateError_Type(Integer32):
    """Custom type cambiumpmp80211GpsFirmwareUpdateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Cambiumpmp80211GpsFirmwareUpdateError_Type.__name__ = "Integer32"
_Cambiumpmp80211GpsFirmwareUpdateError_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdateError = _Cambiumpmp80211GpsFirmwareUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 21),
    _Cambiumpmp80211GpsFirmwareUpdateError_Type()
)
cambiumpmp80211GpsFirmwareUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateError.setStatus("current")


class _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type(DisplayString):
    """Custom type cambiumpmp80211GpsFirmwareUpdateErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type.__name__ = "DisplayString"
_Cambiumpmp80211GpsFirmwareUpdateErrorStr_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdateErrorStr = _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 22),
    _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type()
)
cambiumpmp80211GpsFirmwareUpdateErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateErrorStr.setStatus("current")


class _CambiumBridgeTableAPStatus_Type(Integer32):
    """Custom type cambiumBridgeTableAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumBridgeTableAPStatus_Type.__name__ = "Integer32"
_CambiumBridgeTableAPStatus_Object = MibScalar
cambiumBridgeTableAPStatus = _CambiumBridgeTableAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 25),
    _CambiumBridgeTableAPStatus_Type()
)
cambiumBridgeTableAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableAPStatus.setStatus("current")


class _CambiumBridgeTableSTAUpdate_Type(Integer32):
    """Custom type cambiumBridgeTableSTAUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumBridgeTableSTAUpdate_Type.__name__ = "Integer32"
_CambiumBridgeTableSTAUpdate_Object = MibScalar
cambiumBridgeTableSTAUpdate = _CambiumBridgeTableSTAUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 26),
    _CambiumBridgeTableSTAUpdate_Type()
)
cambiumBridgeTableSTAUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableSTAUpdate.setStatus("current")


class _CambiumBridgeTableSTAStatus_Type(Integer32):
    """Custom type cambiumBridgeTableSTAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumBridgeTableSTAStatus_Type.__name__ = "Integer32"
_CambiumBridgeTableSTAStatus_Object = MibScalar
cambiumBridgeTableSTAStatus = _CambiumBridgeTableSTAStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 27),
    _CambiumBridgeTableSTAStatus_Type()
)
cambiumBridgeTableSTAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableSTAStatus.setStatus("current")


class _CambiumBridgeTableAPUpdate_Type(Integer32):
    """Custom type cambiumBridgeTableAPUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumBridgeTableAPUpdate_Type.__name__ = "Integer32"
_CambiumBridgeTableAPUpdate_Object = MibScalar
cambiumBridgeTableAPUpdate = _CambiumBridgeTableAPUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 28),
    _CambiumBridgeTableAPUpdate_Type()
)
cambiumBridgeTableAPUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableAPUpdate.setStatus("current")


class _CambiumForceTabUpdDHCP_Type(Integer32):
    """Custom type cambiumForceTabUpdDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdDHCP_Type.__name__ = "Integer32"
_CambiumForceTabUpdDHCP_Object = MibScalar
cambiumForceTabUpdDHCP = _CambiumForceTabUpdDHCP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 30),
    _CambiumForceTabUpdDHCP_Type()
)
cambiumForceTabUpdDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdDHCP.setStatus("current")


class _CambiumForceTabUpdTrap_Type(Integer32):
    """Custom type cambiumForceTabUpdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdTrap_Type.__name__ = "Integer32"
_CambiumForceTabUpdTrap_Object = MibScalar
cambiumForceTabUpdTrap = _CambiumForceTabUpdTrap_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 31),
    _CambiumForceTabUpdTrap_Type()
)
cambiumForceTabUpdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdTrap.setStatus("current")


class _CambiumForceTabUpdl2Frw_Type(Integer32):
    """Custom type cambiumForceTabUpdl2Frw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdl2Frw_Type.__name__ = "Integer32"
_CambiumForceTabUpdl2Frw_Object = MibScalar
cambiumForceTabUpdl2Frw = _CambiumForceTabUpdl2Frw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 32),
    _CambiumForceTabUpdl2Frw_Type()
)
cambiumForceTabUpdl2Frw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdl2Frw.setStatus("current")


class _CambiumForceTabUpdl3Frw_Type(Integer32):
    """Custom type cambiumForceTabUpdl3Frw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdl3Frw_Type.__name__ = "Integer32"
_CambiumForceTabUpdl3Frw_Object = MibScalar
cambiumForceTabUpdl3Frw = _CambiumForceTabUpdl3Frw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 33),
    _CambiumForceTabUpdl3Frw_Type()
)
cambiumForceTabUpdl3Frw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdl3Frw.setStatus("current")


class _CambiumForceTabUpdQos_Type(Integer32):
    """Custom type cambiumForceTabUpdQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdQos_Type.__name__ = "Integer32"
_CambiumForceTabUpdQos_Object = MibScalar
cambiumForceTabUpdQos = _CambiumForceTabUpdQos_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 34),
    _CambiumForceTabUpdQos_Type()
)
cambiumForceTabUpdQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdQos.setStatus("current")


class _CambiumForceTabUpdPortFw_Type(Integer32):
    """Custom type cambiumForceTabUpdPortFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdPortFw_Type.__name__ = "Integer32"
_CambiumForceTabUpdPortFw_Object = MibScalar
cambiumForceTabUpdPortFw = _CambiumForceTabUpdPortFw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 35),
    _CambiumForceTabUpdPortFw_Type()
)
cambiumForceTabUpdPortFw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdPortFw.setStatus("current")


class _CambiumForceTabUpdVlan_Type(Integer32):
    """Custom type cambiumForceTabUpdVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdVlan_Type.__name__ = "Integer32"
_CambiumForceTabUpdVlan_Object = MibScalar
cambiumForceTabUpdVlan = _CambiumForceTabUpdVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 36),
    _CambiumForceTabUpdVlan_Type()
)
cambiumForceTabUpdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdVlan.setStatus("current")


class _CambiumForceTabUpdMappingVlan_Type(Integer32):
    """Custom type cambiumForceTabUpdMappingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMappingVlan_Type.__name__ = "Integer32"
_CambiumForceTabUpdMappingVlan_Object = MibScalar
cambiumForceTabUpdMappingVlan = _CambiumForceTabUpdMappingVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 37),
    _CambiumForceTabUpdMappingVlan_Type()
)
cambiumForceTabUpdMappingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMappingVlan.setStatus("current")


class _CambiumConfigurationApplyOnReboot_Type(Integer32):
    """Custom type cambiumConfigurationApplyOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumConfigurationApplyOnReboot_Type.__name__ = "Integer32"
_CambiumConfigurationApplyOnReboot_Object = MibScalar
cambiumConfigurationApplyOnReboot = _CambiumConfigurationApplyOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 38),
    _CambiumConfigurationApplyOnReboot_Type()
)
cambiumConfigurationApplyOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumConfigurationApplyOnReboot.setStatus("current")


class _CambiumForceSTARescan_Type(Integer32):
    """Custom type cambiumForceSTARescan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceSTARescan_Type.__name__ = "Integer32"
_CambiumForceSTARescan_Object = MibScalar
cambiumForceSTARescan = _CambiumForceSTARescan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 39),
    _CambiumForceSTARescan_Type()
)
cambiumForceSTARescan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceSTARescan.setStatus("current")


class _CambiumForceTabUpdMcastDeny_Type(Integer32):
    """Custom type cambiumForceTabUpdMcastDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMcastDeny_Type.__name__ = "Integer32"
_CambiumForceTabUpdMcastDeny_Object = MibScalar
cambiumForceTabUpdMcastDeny = _CambiumForceTabUpdMcastDeny_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 40),
    _CambiumForceTabUpdMcastDeny_Type()
)
cambiumForceTabUpdMcastDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMcastDeny.setStatus("current")


class _CambiumForceTabUpdStaticRoutesCnf_Type(Integer32):
    """Custom type cambiumForceTabUpdStaticRoutesCnf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdStaticRoutesCnf_Type.__name__ = "Integer32"
_CambiumForceTabUpdStaticRoutesCnf_Object = MibScalar
cambiumForceTabUpdStaticRoutesCnf = _CambiumForceTabUpdStaticRoutesCnf_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 41),
    _CambiumForceTabUpdStaticRoutesCnf_Type()
)
cambiumForceTabUpdStaticRoutesCnf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdStaticRoutesCnf.setStatus("current")


class _CambiumForceTabUpdMIR_Type(Integer32):
    """Custom type cambiumForceTabUpdMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMIR_Type.__name__ = "Integer32"
_CambiumForceTabUpdMIR_Object = MibScalar
cambiumForceTabUpdMIR = _CambiumForceTabUpdMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 42),
    _CambiumForceTabUpdMIR_Type()
)
cambiumForceTabUpdMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMIR.setStatus("current")


class _CambiumForceTabUpdRadiusServ_Type(Integer32):
    """Custom type cambiumForceTabUpdRadiusServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdRadiusServ_Type.__name__ = "Integer32"
_CambiumForceTabUpdRadiusServ_Object = MibScalar
cambiumForceTabUpdRadiusServ = _CambiumForceTabUpdRadiusServ_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 43),
    _CambiumForceTabUpdRadiusServ_Type()
)
cambiumForceTabUpdRadiusServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdRadiusServ.setStatus("current")


class _CambiumForceTabUpdPrefAPList_Type(Integer32):
    """Custom type cambiumForceTabUpdPrefAPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdPrefAPList_Type.__name__ = "Integer32"
_CambiumForceTabUpdPrefAPList_Object = MibScalar
cambiumForceTabUpdPrefAPList = _CambiumForceTabUpdPrefAPList_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 44),
    _CambiumForceTabUpdPrefAPList_Type()
)
cambiumForceTabUpdPrefAPList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdPrefAPList.setStatus("current")


class _CambiumForceTabUpdAPAlias_Type(Integer32):
    """Custom type cambiumForceTabUpdAPAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdAPAlias_Type.__name__ = "Integer32"
_CambiumForceTabUpdAPAlias_Object = MibScalar
cambiumForceTabUpdAPAlias = _CambiumForceTabUpdAPAlias_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 45),
    _CambiumForceTabUpdAPAlias_Type()
)
cambiumForceTabUpdAPAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdAPAlias.setStatus("current")


class _CambiumForceTabUpdPortFwSepMangIP_Type(Integer32):
    """Custom type cambiumForceTabUpdPortFwSepMangIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdPortFwSepMangIP_Type.__name__ = "Integer32"
_CambiumForceTabUpdPortFwSepMangIP_Object = MibScalar
cambiumForceTabUpdPortFwSepMangIP = _CambiumForceTabUpdPortFwSepMangIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 46),
    _CambiumForceTabUpdPortFwSepMangIP_Type()
)
cambiumForceTabUpdPortFwSepMangIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdPortFwSepMangIP.setStatus("current")


class _CambiumAPListFlush_Type(Integer32):
    """Custom type cambiumAPListFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumAPListFlush_Type.__name__ = "Integer32"
_CambiumAPListFlush_Object = MibScalar
cambiumAPListFlush = _CambiumAPListFlush_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 47),
    _CambiumAPListFlush_Type()
)
cambiumAPListFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumAPListFlush.setStatus("current")


class _CambiumCCTVListUpdate_Type(Integer32):
    """Custom type cambiumCCTVListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumCCTVListUpdate_Type.__name__ = "Integer32"
_CambiumCCTVListUpdate_Object = MibScalar
cambiumCCTVListUpdate = _CambiumCCTVListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 48),
    _CambiumCCTVListUpdate_Type()
)
cambiumCCTVListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCCTVListUpdate.setStatus("current")


class _CambiumCCTVListUpdateStatus_Type(Integer32):
    """Custom type cambiumCCTVListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumCCTVListUpdateStatus_Type.__name__ = "Integer32"
_CambiumCCTVListUpdateStatus_Object = MibScalar
cambiumCCTVListUpdateStatus = _CambiumCCTVListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 49),
    _CambiumCCTVListUpdateStatus_Type()
)
cambiumCCTVListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCCTVListUpdateStatus.setStatus("current")


class _CambiumCCTVListFlush_Type(Integer32):
    """Custom type cambiumCCTVListFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumCCTVListFlush_Type.__name__ = "Integer32"
_CambiumCCTVListFlush_Object = MibScalar
cambiumCCTVListFlush = _CambiumCCTVListFlush_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 50),
    _CambiumCCTVListFlush_Type()
)
cambiumCCTVListFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCCTVListFlush.setStatus("current")


class _CambiumForceTabUpdSwitch_Type(Integer32):
    """Custom type cambiumForceTabUpdSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdSwitch_Type.__name__ = "Integer32"
_CambiumForceTabUpdSwitch_Object = MibScalar
cambiumForceTabUpdSwitch = _CambiumForceTabUpdSwitch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 51),
    _CambiumForceTabUpdSwitch_Type()
)
cambiumForceTabUpdSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdSwitch.setStatus("current")


class _CambiumForceTabUpdDPIQoSApp_Type(Integer32):
    """Custom type cambiumForceTabUpdDPIQoSApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdDPIQoSApp_Type.__name__ = "Integer32"
_CambiumForceTabUpdDPIQoSApp_Object = MibScalar
cambiumForceTabUpdDPIQoSApp = _CambiumForceTabUpdDPIQoSApp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 52),
    _CambiumForceTabUpdDPIQoSApp_Type()
)
cambiumForceTabUpdDPIQoSApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdDPIQoSApp.setStatus("current")
_Cambiumpmp80211Tools_ObjectIdentity = ObjectIdentity
cambiumpmp80211Tools = _Cambiumpmp80211Tools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6)
)
_CambiumLinkTest_ObjectIdentity = ObjectIdentity
cambiumLinkTest = _CambiumLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1)
)


class _CambiumLinkTestDuration_Type(Integer32):
    """Custom type cambiumLinkTestDuration based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(18, 18),
        ValueRangeConstraint(20, 20),
    )


_CambiumLinkTestDuration_Type.__name__ = "Integer32"
_CambiumLinkTestDuration_Object = MibScalar
cambiumLinkTestDuration = _CambiumLinkTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 1),
    _CambiumLinkTestDuration_Type()
)
cambiumLinkTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestDuration.setStatus("current")


class _CambiumLinkTestPckSize_Type(Integer32):
    """Custom type cambiumLinkTestPckSize based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(1500, 1500),
    )


_CambiumLinkTestPckSize_Type.__name__ = "Integer32"
_CambiumLinkTestPckSize_Object = MibScalar
cambiumLinkTestPckSize = _CambiumLinkTestPckSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 2),
    _CambiumLinkTestPckSize_Type()
)
cambiumLinkTestPckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestPckSize.setStatus("current")


class _CambiumLinkTestStartForMAC_Type(DisplayString):
    """Custom type cambiumLinkTestStartForMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumLinkTestStartForMAC_Type.__name__ = "DisplayString"
_CambiumLinkTestStartForMAC_Object = MibScalar
cambiumLinkTestStartForMAC = _CambiumLinkTestStartForMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 3),
    _CambiumLinkTestStartForMAC_Type()
)
cambiumLinkTestStartForMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestStartForMAC.setStatus("current")


class _CambiumLinkTestStatus_Type(Integer32):
    """Custom type cambiumLinkTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CambiumLinkTestStatus_Type.__name__ = "Integer32"
_CambiumLinkTestStatus_Object = MibScalar
cambiumLinkTestStatus = _CambiumLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 4),
    _CambiumLinkTestStatus_Type()
)
cambiumLinkTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestStatus.setStatus("current")


class _CambiumLinkTestResultDate_Type(DisplayString):
    """Custom type cambiumLinkTestResultDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 24),
    )


_CambiumLinkTestResultDate_Type.__name__ = "DisplayString"
_CambiumLinkTestResultDate_Object = MibScalar
cambiumLinkTestResultDate = _CambiumLinkTestResultDate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 5),
    _CambiumLinkTestResultDate_Type()
)
cambiumLinkTestResultDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultDate.setStatus("current")


class _CambiumLinkTestResultUL_Type(Integer32):
    """Custom type cambiumLinkTestResultUL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CambiumLinkTestResultUL_Type.__name__ = "Integer32"
_CambiumLinkTestResultUL_Object = MibScalar
cambiumLinkTestResultUL = _CambiumLinkTestResultUL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 6),
    _CambiumLinkTestResultUL_Type()
)
cambiumLinkTestResultUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultUL.setStatus("current")


class _CambiumLinkTestResultDL_Type(Integer32):
    """Custom type cambiumLinkTestResultDL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CambiumLinkTestResultDL_Type.__name__ = "Integer32"
_CambiumLinkTestResultDL_Object = MibScalar
cambiumLinkTestResultDL = _CambiumLinkTestResultDL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 7),
    _CambiumLinkTestResultDL_Type()
)
cambiumLinkTestResultDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultDL.setStatus("current")


class _CambiumLinkTestForceAnt_Type(Integer32):
    """Custom type cambiumLinkTestForceAnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLinkTestForceAnt_Type.__name__ = "Integer32"
_CambiumLinkTestForceAnt_Object = MibScalar
cambiumLinkTestForceAnt = _CambiumLinkTestForceAnt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 8),
    _CambiumLinkTestForceAnt_Type()
)
cambiumLinkTestForceAnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestForceAnt.setStatus("current")


class _CambiumLinkTestMode_Type(Integer32):
    """Custom type cambiumLinkTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLinkTestMode_Type.__name__ = "Integer32"
_CambiumLinkTestMode_Object = MibScalar
cambiumLinkTestMode = _CambiumLinkTestMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 9),
    _CambiumLinkTestMode_Type()
)
cambiumLinkTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestMode.setStatus("current")
_CambiumLinkTestMACs_Type = OctetString
_CambiumLinkTestMACs_Object = MibScalar
cambiumLinkTestMACs = _CambiumLinkTestMACs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 10),
    _CambiumLinkTestMACs_Type()
)
cambiumLinkTestMACs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestMACs.setStatus("current")


class _CambiumLinkTestStart_Type(Integer32):
    """Custom type cambiumLinkTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumLinkTestStart_Type.__name__ = "Integer32"
_CambiumLinkTestStart_Object = MibScalar
cambiumLinkTestStart = _CambiumLinkTestStart_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 20),
    _CambiumLinkTestStart_Type()
)
cambiumLinkTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestStart.setStatus("current")
_Caminfo_ObjectIdentity = ObjectIdentity
caminfo = _Caminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2)
)


class _CaminfoScanFrequencyListCountry_Type(OctetString):
    """Custom type caminfoScanFrequencyListCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CaminfoScanFrequencyListCountry_Type.__name__ = "OctetString"
_CaminfoScanFrequencyListCountry_Object = MibScalar
caminfoScanFrequencyListCountry = _CaminfoScanFrequencyListCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 1),
    _CaminfoScanFrequencyListCountry_Type()
)
caminfoScanFrequencyListCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListCountry.setStatus("current")


class _CaminfoScanFrequencyListTwentyBand_Type(DisplayString):
    """Custom type caminfoScanFrequencyListTwentyBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_CaminfoScanFrequencyListTwentyBand_Type.__name__ = "DisplayString"
_CaminfoScanFrequencyListTwentyBand_Object = MibScalar
caminfoScanFrequencyListTwentyBand = _CaminfoScanFrequencyListTwentyBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 2),
    _CaminfoScanFrequencyListTwentyBand_Type()
)
caminfoScanFrequencyListTwentyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListTwentyBand.setStatus("current")


class _CaminfoScanFrequencyListFortyBand_Type(DisplayString):
    """Custom type caminfoScanFrequencyListFortyBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_CaminfoScanFrequencyListFortyBand_Type.__name__ = "DisplayString"
_CaminfoScanFrequencyListFortyBand_Object = MibScalar
caminfoScanFrequencyListFortyBand = _CaminfoScanFrequencyListFortyBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 3),
    _CaminfoScanFrequencyListFortyBand_Type()
)
caminfoScanFrequencyListFortyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListFortyBand.setStatus("current")


class _CaminfoScanFrequencyListAllow59band_Type(Integer32):
    """Custom type caminfoScanFrequencyListAllow59band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CaminfoScanFrequencyListAllow59band_Type.__name__ = "Integer32"
_CaminfoScanFrequencyListAllow59band_Object = MibScalar
caminfoScanFrequencyListAllow59band = _CaminfoScanFrequencyListAllow59band_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 4),
    _CaminfoScanFrequencyListAllow59band_Type()
)
caminfoScanFrequencyListAllow59band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListAllow59band.setStatus("current")


class _CaminfoScanFrequencyListAllow5and10bw_Type(Integer32):
    """Custom type caminfoScanFrequencyListAllow5and10bw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CaminfoScanFrequencyListAllow5and10bw_Type.__name__ = "Integer32"
_CaminfoScanFrequencyListAllow5and10bw_Object = MibScalar
caminfoScanFrequencyListAllow5and10bw = _CaminfoScanFrequencyListAllow5and10bw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 5),
    _CaminfoScanFrequencyListAllow5and10bw_Type()
)
caminfoScanFrequencyListAllow5and10bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListAllow5and10bw.setStatus("current")
_CambiumToolBar_ObjectIdentity = ObjectIdentity
cambiumToolBar = _CambiumToolBar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3)
)
_CambiumToolBarOpts_ObjectIdentity = ObjectIdentity
cambiumToolBarOpts = _CambiumToolBarOpts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1)
)
_CambiumInternetConnectionServerIP_Type = IpAddress
_CambiumInternetConnectionServerIP_Object = MibScalar
cambiumInternetConnectionServerIP = _CambiumInternetConnectionServerIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1, 1),
    _CambiumInternetConnectionServerIP_Type()
)
cambiumInternetConnectionServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumInternetConnectionServerIP.setStatus("current")


class _CambiumInternetConnectionPollPeriod_Type(Integer32):
    """Custom type cambiumInternetConnectionPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CambiumInternetConnectionPollPeriod_Type.__name__ = "Integer32"
_CambiumInternetConnectionPollPeriod_Object = MibScalar
cambiumInternetConnectionPollPeriod = _CambiumInternetConnectionPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1, 2),
    _CambiumInternetConnectionPollPeriod_Type()
)
cambiumInternetConnectionPollPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumInternetConnectionPollPeriod.setStatus("current")
_CambiumToolBarStates_ObjectIdentity = ObjectIdentity
cambiumToolBarStates = _CambiumToolBarStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2)
)


class _CambiumToolbarGlobeState_Type(Integer32):
    """Custom type cambiumToolbarGlobeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumToolbarGlobeState_Type.__name__ = "Integer32"
_CambiumToolbarGlobeState_Object = MibScalar
cambiumToolbarGlobeState = _CambiumToolbarGlobeState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 1),
    _CambiumToolbarGlobeState_Type()
)
cambiumToolbarGlobeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGlobeState.setStatus("current")


class _CambiumToolbarGPSSyncState_Type(Integer32):
    """Custom type cambiumToolbarGPSSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumToolbarGPSSyncState_Type.__name__ = "Integer32"
_CambiumToolbarGPSSyncState_Object = MibScalar
cambiumToolbarGPSSyncState = _CambiumToolbarGPSSyncState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 2),
    _CambiumToolbarGPSSyncState_Type()
)
cambiumToolbarGPSSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGPSSyncState.setStatus("current")


class _CambiumToolbarDeviceConfigurationState_Type(Integer32):
    """Custom type cambiumToolbarDeviceConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CambiumToolbarDeviceConfigurationState_Type.__name__ = "Integer32"
_CambiumToolbarDeviceConfigurationState_Object = MibScalar
cambiumToolbarDeviceConfigurationState = _CambiumToolbarDeviceConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 3),
    _CambiumToolbarDeviceConfigurationState_Type()
)
cambiumToolbarDeviceConfigurationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarDeviceConfigurationState.setStatus("current")


class _CambiumToolbarSyncSource_Type(Integer32):
    """Custom type cambiumToolbarSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_CambiumToolbarSyncSource_Type.__name__ = "Integer32"
_CambiumToolbarSyncSource_Object = MibScalar
cambiumToolbarSyncSource = _CambiumToolbarSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 4),
    _CambiumToolbarSyncSource_Type()
)
cambiumToolbarSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarSyncSource.setStatus("current")


class _CambiumToolbarGPSSyncStateStr_Type(DisplayString):
    """Custom type cambiumToolbarGPSSyncStateStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumToolbarGPSSyncStateStr_Type.__name__ = "DisplayString"
_CambiumToolbarGPSSyncStateStr_Object = MibScalar
cambiumToolbarGPSSyncStateStr = _CambiumToolbarGPSSyncStateStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 5),
    _CambiumToolbarGPSSyncStateStr_Type()
)
cambiumToolbarGPSSyncStateStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGPSSyncStateStr.setStatus("current")
_CambiumCfg_ObjectIdentity = ObjectIdentity
cambiumCfg = _CambiumCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4)
)


class _CambiumJSONCfgImport_Type(OctetString):
    """Custom type cambiumJSONCfgImport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumJSONCfgImport_Type.__name__ = "OctetString"
_CambiumJSONCfgImport_Object = MibScalar
cambiumJSONCfgImport = _CambiumJSONCfgImport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 1),
    _CambiumJSONCfgImport_Type()
)
cambiumJSONCfgImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumJSONCfgImport.setStatus("current")


class _CambiumJSONCfgImportStatus_Type(Integer32):
    """Custom type cambiumJSONCfgImportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3),
    )


_CambiumJSONCfgImportStatus_Type.__name__ = "Integer32"
_CambiumJSONCfgImportStatus_Object = MibScalar
cambiumJSONCfgImportStatus = _CambiumJSONCfgImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 2),
    _CambiumJSONCfgImportStatus_Type()
)
cambiumJSONCfgImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgImportStatus.setStatus("current")


class _CambiumJSONCfgImportError_Type(DisplayString):
    """Custom type cambiumJSONCfgImportError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumJSONCfgImportError_Type.__name__ = "DisplayString"
_CambiumJSONCfgImportError_Object = MibScalar
cambiumJSONCfgImportError = _CambiumJSONCfgImportError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 3),
    _CambiumJSONCfgImportError_Type()
)
cambiumJSONCfgImportError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgImportError.setStatus("current")


class _CambiumJSONCfgImportMode_Type(Integer32):
    """Custom type cambiumJSONCfgImportMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumJSONCfgImportMode_Type.__name__ = "Integer32"
_CambiumJSONCfgImportMode_Object = MibScalar
cambiumJSONCfgImportMode = _CambiumJSONCfgImportMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 4),
    _CambiumJSONCfgImportMode_Type()
)
cambiumJSONCfgImportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumJSONCfgImportMode.setStatus("current")


class _CambiumJSONCfgExport_Type(Integer32):
    """Custom type cambiumJSONCfgExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumJSONCfgExport_Type.__name__ = "Integer32"
_CambiumJSONCfgExport_Object = MibScalar
cambiumJSONCfgExport = _CambiumJSONCfgExport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 10),
    _CambiumJSONCfgExport_Type()
)
cambiumJSONCfgExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumJSONCfgExport.setStatus("current")


class _CambiumJSONCfgExportStatus_Type(Integer32):
    """Custom type cambiumJSONCfgExportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_CambiumJSONCfgExportStatus_Type.__name__ = "Integer32"
_CambiumJSONCfgExportStatus_Object = MibScalar
cambiumJSONCfgExportStatus = _CambiumJSONCfgExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 11),
    _CambiumJSONCfgExportStatus_Type()
)
cambiumJSONCfgExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportStatus.setStatus("current")


class _CambiumJSONCfgExportError_Type(DisplayString):
    """Custom type cambiumJSONCfgExportError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumJSONCfgExportError_Type.__name__ = "DisplayString"
_CambiumJSONCfgExportError_Object = MibScalar
cambiumJSONCfgExportError = _CambiumJSONCfgExportError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 12),
    _CambiumJSONCfgExportError_Type()
)
cambiumJSONCfgExportError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportError.setStatus("current")


class _CambiumJSONCfgExportLink_Type(DisplayString):
    """Custom type cambiumJSONCfgExportLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumJSONCfgExportLink_Type.__name__ = "DisplayString"
_CambiumJSONCfgExportLink_Object = MibScalar
cambiumJSONCfgExportLink = _CambiumJSONCfgExportLink_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 13),
    _CambiumJSONCfgExportLink_Type()
)
cambiumJSONCfgExportLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportLink.setStatus("current")


class _CambiumFullCfgRestore_Type(OctetString):
    """Custom type cambiumFullCfgRestore based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumFullCfgRestore_Type.__name__ = "OctetString"
_CambiumFullCfgRestore_Object = MibScalar
cambiumFullCfgRestore = _CambiumFullCfgRestore_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 20),
    _CambiumFullCfgRestore_Type()
)
cambiumFullCfgRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumFullCfgRestore.setStatus("current")


class _CambiumFullCfgRestoreStatus_Type(Integer32):
    """Custom type cambiumFullCfgRestoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_CambiumFullCfgRestoreStatus_Type.__name__ = "Integer32"
_CambiumFullCfgRestoreStatus_Object = MibScalar
cambiumFullCfgRestoreStatus = _CambiumFullCfgRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 21),
    _CambiumFullCfgRestoreStatus_Type()
)
cambiumFullCfgRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgRestoreStatus.setStatus("current")


class _CambiumFullCfgRestoreError_Type(DisplayString):
    """Custom type cambiumFullCfgRestoreError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumFullCfgRestoreError_Type.__name__ = "DisplayString"
_CambiumFullCfgRestoreError_Object = MibScalar
cambiumFullCfgRestoreError = _CambiumFullCfgRestoreError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 22),
    _CambiumFullCfgRestoreError_Type()
)
cambiumFullCfgRestoreError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgRestoreError.setStatus("current")


class _CambiumFullCfgRestoreMode_Type(Integer32):
    """Custom type cambiumFullCfgRestoreMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumFullCfgRestoreMode_Type.__name__ = "Integer32"
_CambiumFullCfgRestoreMode_Object = MibScalar
cambiumFullCfgRestoreMode = _CambiumFullCfgRestoreMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 23),
    _CambiumFullCfgRestoreMode_Type()
)
cambiumFullCfgRestoreMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumFullCfgRestoreMode.setStatus("current")


class _CambiumFullCfgBackUp_Type(Integer32):
    """Custom type cambiumFullCfgBackUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CambiumFullCfgBackUp_Type.__name__ = "Integer32"
_CambiumFullCfgBackUp_Object = MibScalar
cambiumFullCfgBackUp = _CambiumFullCfgBackUp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 30),
    _CambiumFullCfgBackUp_Type()
)
cambiumFullCfgBackUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUp.setStatus("current")


class _CambiumFullCfgBackUpStatus_Type(Integer32):
    """Custom type cambiumFullCfgBackUpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_CambiumFullCfgBackUpStatus_Type.__name__ = "Integer32"
_CambiumFullCfgBackUpStatus_Object = MibScalar
cambiumFullCfgBackUpStatus = _CambiumFullCfgBackUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 31),
    _CambiumFullCfgBackUpStatus_Type()
)
cambiumFullCfgBackUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpStatus.setStatus("current")


class _CambiumFullCfgBackUpError_Type(DisplayString):
    """Custom type cambiumFullCfgBackUpError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumFullCfgBackUpError_Type.__name__ = "DisplayString"
_CambiumFullCfgBackUpError_Object = MibScalar
cambiumFullCfgBackUpError = _CambiumFullCfgBackUpError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 32),
    _CambiumFullCfgBackUpError_Type()
)
cambiumFullCfgBackUpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpError.setStatus("current")
_CambiumFullCfgBackUpLink_Type = DisplayString
_CambiumFullCfgBackUpLink_Object = MibScalar
cambiumFullCfgBackUpLink = _CambiumFullCfgBackUpLink_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 33),
    _CambiumFullCfgBackUpLink_Type()
)
cambiumFullCfgBackUpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpLink.setStatus("current")


class _CambiumCfgTrialImport_Type(OctetString):
    """Custom type cambiumCfgTrialImport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCfgTrialImport_Type.__name__ = "OctetString"
_CambiumCfgTrialImport_Object = MibScalar
cambiumCfgTrialImport = _CambiumCfgTrialImport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 40),
    _CambiumCfgTrialImport_Type()
)
cambiumCfgTrialImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCfgTrialImport.setStatus("current")


class _CambiumCfgTrialStatus_Type(Integer32):
    """Custom type cambiumCfgTrialStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3),
    )


_CambiumCfgTrialStatus_Type.__name__ = "Integer32"
_CambiumCfgTrialStatus_Object = MibScalar
cambiumCfgTrialStatus = _CambiumCfgTrialStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 41),
    _CambiumCfgTrialStatus_Type()
)
cambiumCfgTrialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCfgTrialStatus.setStatus("current")


class _CambiumCfgTrialError_Type(DisplayString):
    """Custom type cambiumCfgTrialError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumCfgTrialError_Type.__name__ = "DisplayString"
_CambiumCfgTrialError_Object = MibScalar
cambiumCfgTrialError = _CambiumCfgTrialError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 42),
    _CambiumCfgTrialError_Type()
)
cambiumCfgTrialError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCfgTrialError.setStatus("current")


class _CambiumCfgTrialFinish_Type(Integer32):
    """Custom type cambiumCfgTrialFinish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumCfgTrialFinish_Type.__name__ = "Integer32"
_CambiumCfgTrialFinish_Object = MibScalar
cambiumCfgTrialFinish = _CambiumCfgTrialFinish_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 43),
    _CambiumCfgTrialFinish_Type()
)
cambiumCfgTrialFinish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCfgTrialFinish.setStatus("current")


class _CambiumCfgTrialTimer_Type(Integer32):
    """Custom type cambiumCfgTrialTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CambiumCfgTrialTimer_Type.__name__ = "Integer32"
_CambiumCfgTrialTimer_Object = MibScalar
cambiumCfgTrialTimer = _CambiumCfgTrialTimer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 44),
    _CambiumCfgTrialTimer_Type()
)
cambiumCfgTrialTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCfgTrialTimer.setStatus("current")


class _CambiumCfgTrialTimeout_Type(Integer32):
    """Custom type cambiumCfgTrialTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_CambiumCfgTrialTimeout_Type.__name__ = "Integer32"
_CambiumCfgTrialTimeout_Object = MibScalar
cambiumCfgTrialTimeout = _CambiumCfgTrialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 45),
    _CambiumCfgTrialTimeout_Type()
)
cambiumCfgTrialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCfgTrialTimeout.setStatus("current")
_CambiumIDM_ObjectIdentity = ObjectIdentity
cambiumIDM = _CambiumIDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5)
)


class _CambiumIDMMode_Type(Integer32):
    """Custom type cambiumIDMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambiumIDMMode_Type.__name__ = "Integer32"
_CambiumIDMMode_Object = MibScalar
cambiumIDMMode = _CambiumIDMMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 1),
    _CambiumIDMMode_Type()
)
cambiumIDMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMMode.setStatus("current")


class _CambiumIDMTime_Type(Integer32):
    """Custom type cambiumIDMTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )


_CambiumIDMTime_Type.__name__ = "Integer32"
_CambiumIDMTime_Object = MibScalar
cambiumIDMTime = _CambiumIDMTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 2),
    _CambiumIDMTime_Type()
)
cambiumIDMTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMTime.setStatus("current")


class _CambiumIDMEnable_Type(Integer32):
    """Custom type cambiumIDMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumIDMEnable_Type.__name__ = "Integer32"
_CambiumIDMEnable_Object = MibScalar
cambiumIDMEnable = _CambiumIDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 3),
    _CambiumIDMEnable_Type()
)
cambiumIDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMEnable.setStatus("current")
_CambiumIDMResultsTable_Object = MibTable
cambiumIDMResultsTable = _CambiumIDMResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10)
)
if mibBuilder.loadTexts:
    cambiumIDMResultsTable.setStatus("current")
_CambiumIDMResultsEntry_Object = MibTableRow
cambiumIDMResultsEntry = _CambiumIDMResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1)
)
cambiumIDMResultsEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumIDMResultsEntry.setStatus("current")


class _IdmDeviceListCycle_Type(Integer32):
    """Custom type idmDeviceListCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IdmDeviceListCycle_Type.__name__ = "Integer32"
_IdmDeviceListCycle_Object = MibTableColumn
idmDeviceListCycle = _IdmDeviceListCycle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 1),
    _IdmDeviceListCycle_Type()
)
idmDeviceListCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCycle.setStatus("current")


class _IdmDeviceListMAC_Type(DisplayString):
    """Custom type idmDeviceListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_IdmDeviceListMAC_Type.__name__ = "DisplayString"
_IdmDeviceListMAC_Object = MibTableColumn
idmDeviceListMAC = _IdmDeviceListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 2),
    _IdmDeviceListMAC_Type()
)
idmDeviceListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListMAC.setStatus("current")


class _IdmDeviceListLCombRSSI_Type(Integer32):
    """Custom type idmDeviceListLCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListLCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListLCombRSSI_Object = MibTableColumn
idmDeviceListLCombRSSI = _IdmDeviceListLCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 3),
    _IdmDeviceListLCombRSSI_Type()
)
idmDeviceListLCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListLCombRSSI.setStatus("current")


class _IdmDeviceListLRate_Type(DisplayString):
    """Custom type idmDeviceListLRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_IdmDeviceListLRate_Type.__name__ = "DisplayString"
_IdmDeviceListLRate_Object = MibTableColumn
idmDeviceListLRate = _IdmDeviceListLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 4),
    _IdmDeviceListLRate_Type()
)
idmDeviceListLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListLRate.setStatus("current")


class _IdmDeviceListMaxRate_Type(DisplayString):
    """Custom type idmDeviceListMaxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_IdmDeviceListMaxRate_Type.__name__ = "DisplayString"
_IdmDeviceListMaxRate_Object = MibTableColumn
idmDeviceListMaxRate = _IdmDeviceListMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 5),
    _IdmDeviceListMaxRate_Type()
)
idmDeviceListMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListMaxRate.setStatus("current")
_IdmDeviceListPcktsNum_Type = Integer32
_IdmDeviceListPcktsNum_Object = MibTableColumn
idmDeviceListPcktsNum = _IdmDeviceListPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 6),
    _IdmDeviceListPcktsNum_Type()
)
idmDeviceListPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPcktsNum.setStatus("current")


class _IdmDeviceListCRCCombRSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCombRSSI_Object = MibTableColumn
idmDeviceListCRCCombRSSI = _IdmDeviceListCRCCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 7),
    _IdmDeviceListCRCCombRSSI_Type()
)
idmDeviceListCRCCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCombRSSI.setStatus("current")


class _IdmDeviceListCRCCh0RSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCh0RSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCh0RSSI_Object = MibTableColumn
idmDeviceListCRCCh0RSSI = _IdmDeviceListCRCCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 8),
    _IdmDeviceListCRCCh0RSSI_Type()
)
idmDeviceListCRCCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCh0RSSI.setStatus("current")


class _IdmDeviceListCRCCh1RSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCh1RSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCh1RSSI_Object = MibTableColumn
idmDeviceListCRCCh1RSSI = _IdmDeviceListCRCCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 9),
    _IdmDeviceListCRCCh1RSSI_Type()
)
idmDeviceListCRCCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCh1RSSI.setStatus("current")
_IdmDeviceListCRCPcktsNum_Type = Integer32
_IdmDeviceListCRCPcktsNum_Object = MibTableColumn
idmDeviceListCRCPcktsNum = _IdmDeviceListCRCPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 10),
    _IdmDeviceListCRCPcktsNum_Type()
)
idmDeviceListCRCPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCPcktsNum.setStatus("current")


class _IdmDeviceListPRQCombRSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCombRSSI_Object = MibTableColumn
idmDeviceListPRQCombRSSI = _IdmDeviceListPRQCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 11),
    _IdmDeviceListPRQCombRSSI_Type()
)
idmDeviceListPRQCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCombRSSI.setStatus("current")


class _IdmDeviceListPRQCh0RSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCh0RSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCh0RSSI_Object = MibTableColumn
idmDeviceListPRQCh0RSSI = _IdmDeviceListPRQCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 12),
    _IdmDeviceListPRQCh0RSSI_Type()
)
idmDeviceListPRQCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCh0RSSI.setStatus("current")


class _IdmDeviceListPRQCh1RSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCh1RSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCh1RSSI_Object = MibTableColumn
idmDeviceListPRQCh1RSSI = _IdmDeviceListPRQCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 13),
    _IdmDeviceListPRQCh1RSSI_Type()
)
idmDeviceListPRQCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCh1RSSI.setStatus("current")
_IdmDeviceListPRQPcktsNum_Type = Integer32
_IdmDeviceListPRQPcktsNum_Object = MibTableColumn
idmDeviceListPRQPcktsNum = _IdmDeviceListPRQPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 14),
    _IdmDeviceListPRQPcktsNum_Type()
)
idmDeviceListPRQPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQPcktsNum.setStatus("current")


class _CambiumIDMSumMAC_Type(DisplayString):
    """Custom type cambiumIDMSumMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumIDMSumMAC_Type.__name__ = "DisplayString"
_CambiumIDMSumMAC_Object = MibScalar
cambiumIDMSumMAC = _CambiumIDMSumMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 11),
    _CambiumIDMSumMAC_Type()
)
cambiumIDMSumMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMSumMAC.setStatus("current")


class _CambiumIDMSumLCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumLCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumLCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumLCombRSSI_Object = MibScalar
cambiumIDMSumLCombRSSI = _CambiumIDMSumLCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 12),
    _CambiumIDMSumLCombRSSI_Type()
)
cambiumIDMSumLCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumLCombRSSI.setStatus("current")


class _CambiumIDMSumLRate_Type(DisplayString):
    """Custom type cambiumIDMSumLRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CambiumIDMSumLRate_Type.__name__ = "DisplayString"
_CambiumIDMSumLRate_Object = MibScalar
cambiumIDMSumLRate = _CambiumIDMSumLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 13),
    _CambiumIDMSumLRate_Type()
)
cambiumIDMSumLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumLRate.setStatus("current")


class _CambiumIDMSumMaxRate_Type(DisplayString):
    """Custom type cambiumIDMSumMaxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CambiumIDMSumMaxRate_Type.__name__ = "DisplayString"
_CambiumIDMSumMaxRate_Object = MibScalar
cambiumIDMSumMaxRate = _CambiumIDMSumMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 14),
    _CambiumIDMSumMaxRate_Type()
)
cambiumIDMSumMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumMaxRate.setStatus("current")
_CambiumIDMSumPcktsNum_Type = Integer32
_CambiumIDMSumPcktsNum_Object = MibScalar
cambiumIDMSumPcktsNum = _CambiumIDMSumPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 15),
    _CambiumIDMSumPcktsNum_Type()
)
cambiumIDMSumPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPcktsNum.setStatus("current")


class _CambiumIDMSumCRCCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCombRSSI_Object = MibScalar
cambiumIDMSumCRCCombRSSI = _CambiumIDMSumCRCCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 16),
    _CambiumIDMSumCRCCombRSSI_Type()
)
cambiumIDMSumCRCCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCombRSSI.setStatus("current")


class _CambiumIDMSumCRCCh0RSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCh0RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCh0RSSI_Object = MibScalar
cambiumIDMSumCRCCh0RSSI = _CambiumIDMSumCRCCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 17),
    _CambiumIDMSumCRCCh0RSSI_Type()
)
cambiumIDMSumCRCCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCh0RSSI.setStatus("current")


class _CambiumIDMSumCRCCh1RSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCh1RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCh1RSSI_Object = MibScalar
cambiumIDMSumCRCCh1RSSI = _CambiumIDMSumCRCCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 18),
    _CambiumIDMSumCRCCh1RSSI_Type()
)
cambiumIDMSumCRCCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCh1RSSI.setStatus("current")
_CambiumIDMSumCRCPcktsNum_Type = Integer32
_CambiumIDMSumCRCPcktsNum_Object = MibScalar
cambiumIDMSumCRCPcktsNum = _CambiumIDMSumCRCPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 19),
    _CambiumIDMSumCRCPcktsNum_Type()
)
cambiumIDMSumCRCPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCPcktsNum.setStatus("current")


class _CambiumIDMSumPRQCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCombRSSI_Object = MibScalar
cambiumIDMSumPRQCombRSSI = _CambiumIDMSumPRQCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 20),
    _CambiumIDMSumPRQCombRSSI_Type()
)
cambiumIDMSumPRQCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCombRSSI.setStatus("current")


class _CambiumIDMSumPRQCh0RSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCh0RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCh0RSSI_Object = MibScalar
cambiumIDMSumPRQCh0RSSI = _CambiumIDMSumPRQCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 21),
    _CambiumIDMSumPRQCh0RSSI_Type()
)
cambiumIDMSumPRQCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCh0RSSI.setStatus("current")


class _CambiumIDMSumPRQCh1RSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCh1RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCh1RSSI_Object = MibScalar
cambiumIDMSumPRQCh1RSSI = _CambiumIDMSumPRQCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 22),
    _CambiumIDMSumPRQCh1RSSI_Type()
)
cambiumIDMSumPRQCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCh1RSSI.setStatus("current")
_CambiumIDMSumPRQPcktsNum_Type = Integer32
_CambiumIDMSumPRQPcktsNum_Object = MibScalar
cambiumIDMSumPRQPcktsNum = _CambiumIDMSumPRQPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 23),
    _CambiumIDMSumPRQPcktsNum_Type()
)
cambiumIDMSumPRQPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQPcktsNum.setStatus("current")
_CambiumIDMSummaryTable_Object = MibTable
cambiumIDMSummaryTable = _CambiumIDMSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30)
)
if mibBuilder.loadTexts:
    cambiumIDMSummaryTable.setStatus("current")
_CambiumIDMSummaryEntry_Object = MibTableRow
cambiumIDMSummaryEntry = _CambiumIDMSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1)
)
cambiumIDMSummaryEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumIDMSummaryEntry.setStatus("current")


class _IdmSummaryIntMAC_Type(DisplayString):
    """Custom type idmSummaryIntMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_IdmSummaryIntMAC_Type.__name__ = "DisplayString"
_IdmSummaryIntMAC_Object = MibTableColumn
idmSummaryIntMAC = _IdmSummaryIntMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 1),
    _IdmSummaryIntMAC_Type()
)
idmSummaryIntMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntMAC.setStatus("current")


class _IdmSummaryIntCombRSSI_Type(Integer32):
    """Custom type idmSummaryIntCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCombRSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCombRSSI_Object = MibTableColumn
idmSummaryIntCombRSSI = _IdmSummaryIntCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 2),
    _IdmSummaryIntCombRSSI_Type()
)
idmSummaryIntCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCombRSSI.setStatus("current")


class _IdmSummaryIntCh0RSSI_Type(Integer32):
    """Custom type idmSummaryIntCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCh0RSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCh0RSSI_Object = MibTableColumn
idmSummaryIntCh0RSSI = _IdmSummaryIntCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 3),
    _IdmSummaryIntCh0RSSI_Type()
)
idmSummaryIntCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCh0RSSI.setStatus("current")


class _IdmSummaryIntCh1RSSI_Type(Integer32):
    """Custom type idmSummaryIntCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCh1RSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCh1RSSI_Object = MibTableColumn
idmSummaryIntCh1RSSI = _IdmSummaryIntCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 4),
    _IdmSummaryIntCh1RSSI_Type()
)
idmSummaryIntCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCh1RSSI.setStatus("current")


class _IdmSummaryIntSSID_Type(DisplayString):
    """Custom type idmSummaryIntSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IdmSummaryIntSSID_Type.__name__ = "DisplayString"
_IdmSummaryIntSSID_Object = MibTableColumn
idmSummaryIntSSID = _IdmSummaryIntSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 5),
    _IdmSummaryIntSSID_Type()
)
idmSummaryIntSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntSSID.setStatus("current")
_CambiumACSCfg_ObjectIdentity = ObjectIdentity
cambiumACSCfg = _CambiumACSCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6)
)


class _AcsEnable_Type(Integer32):
    """Custom type acsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_AcsEnable_Type.__name__ = "Integer32"
_AcsEnable_Object = MibScalar
acsEnable = _AcsEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 1),
    _AcsEnable_Type()
)
acsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsEnable.setStatus("current")


class _AcsScanMinDwellTime_Type(Integer32):
    """Custom type acsScanMinDwellTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_AcsScanMinDwellTime_Type.__name__ = "Integer32"
_AcsScanMinDwellTime_Object = MibScalar
acsScanMinDwellTime = _AcsScanMinDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 2),
    _AcsScanMinDwellTime_Type()
)
acsScanMinDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScanMinDwellTime.setStatus("current")


class _AcsScanMaxDwellTime_Type(Integer32):
    """Custom type acsScanMaxDwellTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_AcsScanMaxDwellTime_Type.__name__ = "Integer32"
_AcsScanMaxDwellTime_Object = MibScalar
acsScanMaxDwellTime = _AcsScanMaxDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 3),
    _AcsScanMaxDwellTime_Type()
)
acsScanMaxDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScanMaxDwellTime.setStatus("current")


class _AcsControl_Type(Integer32):
    """Custom type acsControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcsControl_Type.__name__ = "Integer32"
_AcsControl_Object = MibScalar
acsControl = _AcsControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 4),
    _AcsControl_Type()
)
acsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsControl.setStatus("current")
_CambiumSpectral_ObjectIdentity = ObjectIdentity
cambiumSpectral = _CambiumSpectral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 7)
)


class _SpectralEnable_Type(Integer32):
    """Custom type spectralEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SpectralEnable_Type.__name__ = "Integer32"
_SpectralEnable_Object = MibScalar
spectralEnable = _SpectralEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 7, 1),
    _SpectralEnable_Type()
)
spectralEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectralEnable.setStatus("current")
_CambiumArcher_ObjectIdentity = ObjectIdentity
cambiumArcher = _CambiumArcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8)
)


class _WirelessInterfaceAttemptScanFrequencyListFive_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyListFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyListFive_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyListFive_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyListFive = _WirelessInterfaceAttemptScanFrequencyListFive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 1),
    _WirelessInterfaceAttemptScanFrequencyListFive_Type()
)
wirelessInterfaceAttemptScanFrequencyListFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyListFive.setStatus("current")


class _WirelessInterfaceAttemptScanFrequencyListTen_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyListTen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyListTen_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyListTen_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyListTen = _WirelessInterfaceAttemptScanFrequencyListTen_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 2),
    _WirelessInterfaceAttemptScanFrequencyListTen_Type()
)
wirelessInterfaceAttemptScanFrequencyListTen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyListTen.setStatus("current")


class _WirelessInterfaceAttemptScanFrequencyListTwenty_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyListTwenty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyListTwenty_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyListTwenty_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyListTwenty = _WirelessInterfaceAttemptScanFrequencyListTwenty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 3),
    _WirelessInterfaceAttemptScanFrequencyListTwenty_Type()
)
wirelessInterfaceAttemptScanFrequencyListTwenty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyListTwenty.setStatus("current")


class _WirelessInterfaceAttemptScanFrequencyListForty_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyListForty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyListForty_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyListForty_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyListForty = _WirelessInterfaceAttemptScanFrequencyListForty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 4),
    _WirelessInterfaceAttemptScanFrequencyListForty_Type()
)
wirelessInterfaceAttemptScanFrequencyListForty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyListForty.setStatus("current")


class _WirelessInterfaceAttemptScanFrequencyListEighty_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyListEighty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyListEighty_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyListEighty_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyListEighty = _WirelessInterfaceAttemptScanFrequencyListEighty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 5),
    _WirelessInterfaceAttemptScanFrequencyListEighty_Type()
)
wirelessInterfaceAttemptScanFrequencyListEighty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyListEighty.setStatus("current")


class _WirelessInterfaceAttemptScanFrequencyList160M_Type(DisplayString):
    """Custom type wirelessInterfaceAttemptScanFrequencyList160M based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1500),
    )


_WirelessInterfaceAttemptScanFrequencyList160M_Type.__name__ = "DisplayString"
_WirelessInterfaceAttemptScanFrequencyList160M_Object = MibScalar
wirelessInterfaceAttemptScanFrequencyList160M = _WirelessInterfaceAttemptScanFrequencyList160M_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 6),
    _WirelessInterfaceAttemptScanFrequencyList160M_Type()
)
wirelessInterfaceAttemptScanFrequencyList160M.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencyList160M.setStatus("current")
_WirelessInterfaceAttemptScanFrequencySkipCounter_Type = Integer32
_WirelessInterfaceAttemptScanFrequencySkipCounter_Object = MibScalar
wirelessInterfaceAttemptScanFrequencySkipCounter = _WirelessInterfaceAttemptScanFrequencySkipCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 8, 21),
    _WirelessInterfaceAttemptScanFrequencySkipCounter_Type()
)
wirelessInterfaceAttemptScanFrequencySkipCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessInterfaceAttemptScanFrequencySkipCounter.setStatus("current")
_CambiumWatchdog_ObjectIdentity = ObjectIdentity
cambiumWatchdog = _CambiumWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9)
)


class _WatchdogEnable_Type(Integer32):
    """Custom type watchdogEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WatchdogEnable_Type.__name__ = "Integer32"
_WatchdogEnable_Object = MibScalar
watchdogEnable = _WatchdogEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 1),
    _WatchdogEnable_Type()
)
watchdogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogEnable.setStatus("current")


class _WatchdogMode_Type(Integer32):
    """Custom type watchdogMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WatchdogMode_Type.__name__ = "Integer32"
_WatchdogMode_Object = MibScalar
watchdogMode = _WatchdogMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 2),
    _WatchdogMode_Type()
)
watchdogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogMode.setStatus("current")


class _WatchdogTargetIPAddress_Type(OctetString):
    """Custom type watchdogTargetIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WatchdogTargetIPAddress_Type.__name__ = "OctetString"
_WatchdogTargetIPAddress_Object = MibScalar
watchdogTargetIPAddress = _WatchdogTargetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 3),
    _WatchdogTargetIPAddress_Type()
)
watchdogTargetIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogTargetIPAddress.setStatus("current")


class _WatchdogPingInterval_Type(Integer32):
    """Custom type watchdogPingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WatchdogPingInterval_Type.__name__ = "Integer32"
_WatchdogPingInterval_Object = MibScalar
watchdogPingInterval = _WatchdogPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 4),
    _WatchdogPingInterval_Type()
)
watchdogPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogPingInterval.setStatus("current")


class _WatchdogPingRetries_Type(Integer32):
    """Custom type watchdogPingRetries based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_WatchdogPingRetries_Type.__name__ = "Integer32"
_WatchdogPingRetries_Object = MibScalar
watchdogPingRetries = _WatchdogPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 5),
    _WatchdogPingRetries_Type()
)
watchdogPingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogPingRetries.setStatus("current")
_WatchdogRF_ObjectIdentity = ObjectIdentity
watchdogRF = _WatchdogRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 6)
)


class _WatchdogRFEnable_Type(Integer32):
    """Custom type watchdogRFEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WatchdogRFEnable_Type.__name__ = "Integer32"
_WatchdogRFEnable_Object = MibScalar
watchdogRFEnable = _WatchdogRFEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 6, 1),
    _WatchdogRFEnable_Type()
)
watchdogRFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogRFEnable.setStatus("current")


class _WatchdogRFRSSIThreshold_Type(Integer32):
    """Custom type watchdogRFRSSIThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 60),
    )


_WatchdogRFRSSIThreshold_Type.__name__ = "Integer32"
_WatchdogRFRSSIThreshold_Object = MibScalar
watchdogRFRSSIThreshold = _WatchdogRFRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 6, 2),
    _WatchdogRFRSSIThreshold_Type()
)
watchdogRFRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogRFRSSIThreshold.setStatus("current")


class _WatchdogRFSNRThreshold_Type(Integer32):
    """Custom type watchdogRFSNRThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 60),
    )


_WatchdogRFSNRThreshold_Type.__name__ = "Integer32"
_WatchdogRFSNRThreshold_Object = MibScalar
watchdogRFSNRThreshold = _WatchdogRFSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 6, 3),
    _WatchdogRFSNRThreshold_Type()
)
watchdogRFSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogRFSNRThreshold.setStatus("current")


class _WatchdogRFCountThreshold_Type(Integer32):
    """Custom type watchdogRFCountThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WatchdogRFCountThreshold_Type.__name__ = "Integer32"
_WatchdogRFCountThreshold_Object = MibScalar
watchdogRFCountThreshold = _WatchdogRFCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 6, 4),
    _WatchdogRFCountThreshold_Type()
)
watchdogRFCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogRFCountThreshold.setStatus("current")
_WatchdogGPS_ObjectIdentity = ObjectIdentity
watchdogGPS = _WatchdogGPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 10)
)


class _WatchdogGPSAllowHardReset_Type(Integer32):
    """Custom type watchdogGPSAllowHardReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WatchdogGPSAllowHardReset_Type.__name__ = "Integer32"
_WatchdogGPSAllowHardReset_Object = MibScalar
watchdogGPSAllowHardReset = _WatchdogGPSAllowHardReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 9, 10, 1),
    _WatchdogGPSAllowHardReset_Type()
)
watchdogGPSAllowHardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogGPSAllowHardReset.setStatus("current")
_CambiumCrashReporter_ObjectIdentity = ObjectIdentity
cambiumCrashReporter = _CambiumCrashReporter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 10)
)


class _CrashReporterEnable_Type(Integer32):
    """Custom type crashReporterEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CrashReporterEnable_Type.__name__ = "Integer32"
_CrashReporterEnable_Object = MibScalar
crashReporterEnable = _CrashReporterEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 10, 1),
    _CrashReporterEnable_Type()
)
crashReporterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crashReporterEnable.setStatus("current")
_ReconnectPrimaryAPSelectIface_ObjectIdentity = ObjectIdentity
reconnectPrimaryAPSelectIface = _ReconnectPrimaryAPSelectIface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 11)
)


class _WirelessInterfaceReconnectPrimaryAPEnable_Type(Integer32):
    """Custom type wirelessInterfaceReconnectPrimaryAPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceReconnectPrimaryAPEnable_Type.__name__ = "Integer32"
_WirelessInterfaceReconnectPrimaryAPEnable_Object = MibScalar
wirelessInterfaceReconnectPrimaryAPEnable = _WirelessInterfaceReconnectPrimaryAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 11, 1),
    _WirelessInterfaceReconnectPrimaryAPEnable_Type()
)
wirelessInterfaceReconnectPrimaryAPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceReconnectPrimaryAPEnable.setStatus("current")


class _WirelessInterfaceReconnectPrimaryAPPeriod_Type(Integer32):
    """Custom type wirelessInterfaceReconnectPrimaryAPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 720),
    )


_WirelessInterfaceReconnectPrimaryAPPeriod_Type.__name__ = "Integer32"
_WirelessInterfaceReconnectPrimaryAPPeriod_Object = MibScalar
wirelessInterfaceReconnectPrimaryAPPeriod = _WirelessInterfaceReconnectPrimaryAPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 11, 2),
    _WirelessInterfaceReconnectPrimaryAPPeriod_Type()
)
wirelessInterfaceReconnectPrimaryAPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceReconnectPrimaryAPPeriod.setStatus("current")


class _WirelessInterfaceReconnectPrimaryAPScanBG_Type(Integer32):
    """Custom type wirelessInterfaceReconnectPrimaryAPScanBG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceReconnectPrimaryAPScanBG_Type.__name__ = "Integer32"
_WirelessInterfaceReconnectPrimaryAPScanBG_Object = MibScalar
wirelessInterfaceReconnectPrimaryAPScanBG = _WirelessInterfaceReconnectPrimaryAPScanBG_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 11, 3),
    _WirelessInterfaceReconnectPrimaryAPScanBG_Type()
)
wirelessInterfaceReconnectPrimaryAPScanBG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceReconnectPrimaryAPScanBG.setStatus("current")
_CambiumHWGroupInfo_ObjectIdentity = ObjectIdentity
cambiumHWGroupInfo = _CambiumHWGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9)
)
_EPMPavenger5gconnectorizedsync_ObjectIdentity = ObjectIdentity
ePMPavenger5gconnectorizedsync = _EPMPavenger5gconnectorizedsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 0)
)
_EPMPavenger5gconnectorized_ObjectIdentity = ObjectIdentity
ePMPavenger5gconnectorized = _EPMPavenger5gconnectorized_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 1)
)
_EPMPavenger5gintegrated_ObjectIdentity = ObjectIdentity
ePMPavenger5gintegrated = _EPMPavenger5gintegrated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 2)
)
_EPMPavenger2gconnectorizedsync_ObjectIdentity = ObjectIdentity
ePMPavenger2gconnectorizedsync = _EPMPavenger2gconnectorizedsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 3)
)
_EPMPavenger2gconnectorized_ObjectIdentity = ObjectIdentity
ePMPavenger2gconnectorized = _EPMPavenger2gconnectorized_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 4)
)
_EPMPavenger2gintegrated_ObjectIdentity = ObjectIdentity
ePMPavenger2gintegrated = _EPMPavenger2gintegrated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 5)
)
_EPMPironman25grow_ObjectIdentity = ObjectIdentity
ePMPironman25grow = _EPMPironman25grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 6)
)
_EPMPironman22grow_ObjectIdentity = ObjectIdentity
ePMPironman22grow = _EPMPironman22grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 7)
)
_EPMPironman25gfccextflt_ObjectIdentity = ObjectIdentity
ePMPironman25gfccextflt = _EPMPironman25gfccextflt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 8)
)
_EPMPironman22gfccrowextflt_ObjectIdentity = ObjectIdentity
ePMPironman22gfccrowextflt = _EPMPironman22gfccrowextflt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 9)
)
_EPMPhawkeye_ObjectIdentity = ObjectIdentity
ePMPhawkeye = _EPMPhawkeye_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 10)
)
_EPMPironlad5grow_ObjectIdentity = ObjectIdentity
ePMPironlad5grow = _EPMPironlad5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 11)
)
_EPMPironlad5gfccextflt_ObjectIdentity = ObjectIdentity
ePMPironlad5gfccextflt = _EPMPironlad5gfccextflt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 12)
)
_EPMPdarkchocolate5grow_ObjectIdentity = ObjectIdentity
ePMPdarkchocolate5grow = _EPMPdarkchocolate5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 13)
)
_EPMPdarkchocolate5gfcc_ObjectIdentity = ObjectIdentity
ePMPdarkchocolate5gfcc = _EPMPdarkchocolate5gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 14)
)
_EPMPhawkeyecrystal_ObjectIdentity = ObjectIdentity
ePMPhawkeyecrystal = _EPMPhawkeyecrystal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 15)
)
_EPMPmargaret6gironlad_ObjectIdentity = ObjectIdentity
ePMPmargaret6gironlad = _EPMPmargaret6gironlad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 16)
)
_EPMPmargaret6gconnectorizedsync_ObjectIdentity = ObjectIdentity
ePMPmargaret6gconnectorizedsync = _EPMPmargaret6gconnectorizedsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 17)
)
_EPMPmargaret6gconnectorized_ObjectIdentity = ObjectIdentity
ePMPmargaret6gconnectorized = _EPMPmargaret6gconnectorized_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 18)
)
_EPMPelectra25gconnectorizedsync_ObjectIdentity = ObjectIdentity
ePMPelectra25gconnectorizedsync = _EPMPelectra25gconnectorizedsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 19)
)
_EPMPelectra25gconnectorized_ObjectIdentity = ObjectIdentity
ePMPelectra25gconnectorized = _EPMPelectra25gconnectorized_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 20)
)
_EPMPforce1305g_ObjectIdentity = ObjectIdentity
ePMPforce1305g = _EPMPforce1305g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 22)
)
_EPMPforce1302g_ObjectIdentity = ObjectIdentity
ePMPforce1302g = _EPMPforce1302g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 23)
)
_EPMPforce200l_ObjectIdentity = ObjectIdentity
ePMPforce200l = _EPMPforce200l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 24)
)
_EPMPforce200lv2_ObjectIdentity = ObjectIdentity
ePMPforce200lv2 = _EPMPforce200lv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 25)
)
_EPMPptp5505gintegratedfcc_ObjectIdentity = ObjectIdentity
ePMPptp5505gintegratedfcc = _EPMPptp5505gintegratedfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 33)
)
_EPMPptp5505gconnectorizedfcc_ObjectIdentity = ObjectIdentity
ePMPptp5505gconnectorizedfcc = _EPMPptp5505gconnectorizedfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 34)
)
_EPMPf300fcc_ObjectIdentity = ObjectIdentity
ePMPf300fcc = _EPMPf300fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 35)
)
_EPMPf300row_ObjectIdentity = ObjectIdentity
ePMPf300row = _EPMPf300row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 36)
)
_EPMPepmp3000fcc_ObjectIdentity = ObjectIdentity
ePMPepmp3000fcc = _EPMPepmp3000fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 37)
)
_EPMPf220fcc_ObjectIdentity = ObjectIdentity
ePMPf220fcc = _EPMPf220fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 38)
)
_EPMPf220row_ObjectIdentity = ObjectIdentity
ePMPf220row = _EPMPf220row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 39)
)
_EPMPepmp3000row_ObjectIdentity = ObjectIdentity
ePMPepmp3000row = _EPMPepmp3000row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 40)
)
_EPMPptp5505gintegratedrow_ObjectIdentity = ObjectIdentity
ePMPptp5505gintegratedrow = _EPMPptp5505gintegratedrow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 41)
)
_EPMPptp5505gconnectorizedrow_ObjectIdentity = ObjectIdentity
ePMPptp5505gconnectorizedrow = _EPMPptp5505gconnectorizedrow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 42)
)
_EPMPmystiquefccsync_ObjectIdentity = ObjectIdentity
ePMPmystiquefccsync = _EPMPmystiquefccsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 43)
)
_EPMPmystiquerowsync_ObjectIdentity = ObjectIdentity
ePMPmystiquerowsync = _EPMPmystiquerowsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 44)
)
_EPMPmystiquefcc_ObjectIdentity = ObjectIdentity
ePMPmystiquefcc = _EPMPmystiquefcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 45)
)
_EPMPmystiquerow_ObjectIdentity = ObjectIdentity
ePMPmystiquerow = _EPMPmystiquerow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 46)
)
_EPMPxorn13fcc_ObjectIdentity = ObjectIdentity
ePMPxorn13fcc = _EPMPxorn13fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 47)
)
_EPMPxorn13row_ObjectIdentity = ObjectIdentity
ePMPxorn13row = _EPMPxorn13row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 48)
)
_EPMPxorn19fcc_ObjectIdentity = ObjectIdentity
ePMPxorn19fcc = _EPMPxorn19fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 49)
)
_EPMPxorn19row_ObjectIdentity = ObjectIdentity
ePMPxorn19row = _EPMPxorn19row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 50)
)
_EPMPxorn19rip67row_ObjectIdentity = ObjectIdentity
ePMPxorn19rip67row = _EPMPxorn19rip67row_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 51)
)
_EPMPxorn19rip67fcc_ObjectIdentity = ObjectIdentity
ePMPxorn19rip67fcc = _EPMPxorn19rip67fcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 52)
)
_EPMPhellcowfcc_ObjectIdentity = ObjectIdentity
ePMPhellcowfcc = _EPMPhellcowfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53)
)
_EPMPhellcowrow_ObjectIdentity = ObjectIdentity
ePMPhellcowrow = _EPMPhellcowrow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 54)
)
_EPMPf300fccv2_ObjectIdentity = ObjectIdentity
ePMPf300fccv2 = _EPMPf300fccv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 55)
)
_EPMPf30025l_ObjectIdentity = ObjectIdentity
ePMPf30025l = _EPMPf30025l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 58)
)
_EPMPf30025lv2_ObjectIdentity = ObjectIdentity
ePMPf30025lv2 = _EPMPf30025lv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 60)
)
_EPMPf30013l_ObjectIdentity = ObjectIdentity
ePMPf30013l = _EPMPf30013l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 61)
)
_EPMPe510_ObjectIdentity = ObjectIdentity
ePMPe510 = _EPMPe510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 62)
)
_EPMPnanostationm5v3xw_ObjectIdentity = ObjectIdentity
ePMPnanostationm5v3xw = _EPMPnanostationm5v3xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 100)
)
_EPMPnanostationlocom5v3_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom5v3 = _EPMPnanostationlocom5v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 110)
)
_EPMPnanostationlocom2xw_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom2xw = _EPMPnanostationlocom2xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 111)
)
_EPMPnanostationlocom2v2xw_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom2v2xw = _EPMPnanostationlocom2v2xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 112)
)
_EPMPnanostationlocom2v3xw_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom2v3xw = _EPMPnanostationlocom2v3xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 113)
)
_EPMProcketm5xwv1_ObjectIdentity = ObjectIdentity
ePMProcketm5xwv1 = _EPMProcketm5xwv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 120)
)
_EPMProcketm5x3wv2_ObjectIdentity = ObjectIdentity
ePMProcketm5x3wv2 = _EPMProcketm5x3wv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 121)
)
_EPMPnanobeamm516xw_ObjectIdentity = ObjectIdentity
ePMPnanobeamm516xw = _EPMPnanobeamm516xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 130)
)
_EPMPnanobeamm519xw_ObjectIdentity = ObjectIdentity
ePMPnanobeamm519xw = _EPMPnanobeamm519xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 131)
)
_EPMPnanobeamm2xw_ObjectIdentity = ObjectIdentity
ePMPnanobeamm2xw = _EPMPnanobeamm2xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 132)
)
_EPMPrbsxtlite5_ObjectIdentity = ObjectIdentity
ePMPrbsxtlite5 = _EPMPrbsxtlite5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 140)
)
_EPMPintelbras_ObjectIdentity = ObjectIdentity
ePMPintelbras = _EPMPintelbras_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 141)
)
_EPMPlhg5_ObjectIdentity = ObjectIdentity
ePMPlhg5 = _EPMPlhg5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 142)
)
_EPMPdisclite5_ObjectIdentity = ObjectIdentity
ePMPdisclite5 = _EPMPdisclite5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 143)
)
_EPMPmk911l_ObjectIdentity = ObjectIdentity
ePMPmk911l = _EPMPmk911l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 144)
)
_EPMPsextant_ObjectIdentity = ObjectIdentity
ePMPsextant = _EPMPsextant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 145)
)
_EPMPpowerbeamm5300_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5300 = _EPMPpowerbeamm5300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 150)
)
_EPMPpowerbeamm5400_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5400 = _EPMPpowerbeamm5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 151)
)
_EPMPpowerbeamm5620_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5620 = _EPMPpowerbeamm5620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 152)
)
_EPMPpowerbeamm2400_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm2400 = _EPMPpowerbeamm2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 153)
)
_EPMPpowerbeamm5400iso_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5400iso = _EPMPpowerbeamm5400iso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 154)
)
_EPMPpowerbeamm5300iso_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5300iso = _EPMPpowerbeamm5300iso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 155)
)
_EPMPpowerbeamm5600iso_ObjectIdentity = ObjectIdentity
ePMPpowerbeamm5600iso = _EPMPpowerbeamm5600iso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 156)
)
_EPMPnanostationm5v1xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm5v1xm = _EPMPnanostationm5v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 170)
)
_EPMPnanostationm5v2xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm5v2xm = _EPMPnanostationm5v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 171)
)
_EPMPnanostationm365xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm365xm = _EPMPnanostationm365xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 172)
)
_EPMPnanostationm2v1xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm2v1xm = _EPMPnanostationm2v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 173)
)
_EPMPnanostationm3xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm3xm = _EPMPnanostationm3xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 174)
)
_EPMPnanostationm900xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm900xm = _EPMPnanostationm900xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 175)
)
_EPMPnanostationm2v2xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm2v2xm = _EPMPnanostationm2v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 176)
)
_EPMPnanostationlocom5v1xm_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom5v1xm = _EPMPnanostationlocom5v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 180)
)
_EPMPnanostationlocom5v2xm_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom5v2xm = _EPMPnanostationlocom5v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 181)
)
_EPMPnanostationlocom900xm_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom900xm = _EPMPnanostationlocom900xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 182)
)
_EPMPnanostationlocom2xm_ObjectIdentity = ObjectIdentity
ePMPnanostationlocom2xm = _EPMPnanostationlocom2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 183)
)
_EPMPnanobridgem365xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem365xm = _EPMPnanobridgem365xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 190)
)
_EPMPnanobridgem900xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem900xm = _EPMPnanobridgem900xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 191)
)
_EPMPnanobridgem3xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem3xm = _EPMPnanobridgem3xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 192)
)
_EPMPnanobridgem5nb5g22xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem5nb5g22xm = _EPMPnanobridgem5nb5g22xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 193)
)
_EPMPnanobridgem5nb5g25xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem5nb5g25xm = _EPMPnanobridgem5nb5g25xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 194)
)
_EPMPnanobridgem5nbxm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem5nbxm = _EPMPnanobridgem5nbxm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 195)
)
_EPMPnanobridgem2v1xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem2v1xm = _EPMPnanobridgem2v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 196)
)
_EPMPnanobridgem2v2xm_ObjectIdentity = ObjectIdentity
ePMPnanobridgem2v2xm = _EPMPnanobridgem2v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 197)
)
_EPMPintelbraswom5amimo_ObjectIdentity = ObjectIdentity
ePMPintelbraswom5amimo = _EPMPintelbraswom5amimo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 200)
)
_EPMPintelbraswom5a23_ObjectIdentity = ObjectIdentity
ePMPintelbraswom5a23 = _EPMPintelbraswom5a23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 201)
)
_EPMPpowerbridgem365xm_ObjectIdentity = ObjectIdentity
ePMPpowerbridgem365xm = _EPMPpowerbridgem365xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 210)
)
_EPMPpowerbridgem3xm_ObjectIdentity = ObjectIdentity
ePMPpowerbridgem3xm = _EPMPpowerbridgem3xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 211)
)
_EPMPnanostationm6xm_ObjectIdentity = ObjectIdentity
ePMPnanostationm6xm = _EPMPnanostationm6xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 220)
)
_EPMProcketm5v1xm_ObjectIdentity = ObjectIdentity
ePMProcketm5v1xm = _EPMProcketm5v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 241)
)
_EPMProcketm5v2xm_ObjectIdentity = ObjectIdentity
ePMProcketm5v2xm = _EPMProcketm5v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 242)
)
_EPMProcketm5v3xm_ObjectIdentity = ObjectIdentity
ePMProcketm5v3xm = _EPMProcketm5v3xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 243)
)
_EPMProcketm5v4xm_ObjectIdentity = ObjectIdentity
ePMProcketm5v4xm = _EPMProcketm5v4xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 244)
)
_EPMProcketm2v1xm_ObjectIdentity = ObjectIdentity
ePMProcketm2v1xm = _EPMProcketm2v1xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 245)
)
_EPMProcketm2v2xm_ObjectIdentity = ObjectIdentity
ePMProcketm2v2xm = _EPMProcketm2v2xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 246)
)
_EPMProcketm2v3xm_ObjectIdentity = ObjectIdentity
ePMProcketm2v3xm = _EPMProcketm2v3xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 247)
)
_EPMProcketm2v4xm_ObjectIdentity = ObjectIdentity
ePMProcketm2v4xm = _EPMProcketm2v4xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 248)
)
_EPMPepmp60004x46growfcc_ObjectIdentity = ObjectIdentity
ePMPepmp60004x46growfcc = _EPMPepmp60004x46growfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53264)
)
_EPMPepmp40008x85grow_ObjectIdentity = ObjectIdentity
ePMPepmp40008x85grow = _EPMPepmp40008x85grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53280)
)
_EPMPepmp4500c8x85grow_ObjectIdentity = ObjectIdentity
ePMPepmp4500c8x85grow = _EPMPepmp4500c8x85grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53281)
)
_EPMPepmp40008x85gfcc_ObjectIdentity = ObjectIdentity
ePMPepmp40008x85gfcc = _EPMPepmp40008x85gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53288)
)
_EPMPepmp4500c8x85gfcc_ObjectIdentity = ObjectIdentity
ePMPepmp4500c8x85gfcc = _EPMPepmp4500c8x85gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53289)
)
_EPMPepmp4600l6growfcc_ObjectIdentity = ObjectIdentity
ePMPepmp4600l6growfcc = _EPMPepmp4600l6growfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53296)
)
_EPMPf400gps5grow_ObjectIdentity = ObjectIdentity
ePMPf400gps5grow = _EPMPf400gps5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53344)
)
_EPMPf400gps5gfcc_ObjectIdentity = ObjectIdentity
ePMPf400gps5gfcc = _EPMPf400gps5gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53352)
)
_EPMPcnppilottiger5g_ObjectIdentity = ObjectIdentity
ePMPcnppilottiger5g = _EPMPcnppilottiger5g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53376)
)
_EPMPf4255grow_ObjectIdentity = ObjectIdentity
ePMPf4255grow = _EPMPf4255grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53504)
)
_EPMPf400c5grow_ObjectIdentity = ObjectIdentity
ePMPf400c5grow = _EPMPf400c5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53505)
)
_EPMPf4255gfcc_ObjectIdentity = ObjectIdentity
ePMPf4255gfcc = _EPMPf4255gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53512)
)
_EPMPf400c5gfcc_ObjectIdentity = ObjectIdentity
ePMPf400c5gfcc = _EPMPf400c5gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53513)
)
_EPMPf600c6growfcc_ObjectIdentity = ObjectIdentity
ePMPf600c6growfcc = _EPMPf600c6growfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53520)
)
_EPMPf600c6gfcc_ObjectIdentity = ObjectIdentity
ePMPf600c6gfcc = _EPMPf600c6gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53528)
)
_EPMPf4165grow_ObjectIdentity = ObjectIdentity
ePMPf4165grow = _EPMPf4165grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53536)
)
_EPMPf425l5grow_ObjectIdentity = ObjectIdentity
ePMPf425l5grow = _EPMPf425l5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53537)
)
_EPMPf425ulnomcu5grow_ObjectIdentity = ObjectIdentity
ePMPf425ulnomcu5grow = _EPMPf425ulnomcu5grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53538)
)
_EPMPf4165gfcc_ObjectIdentity = ObjectIdentity
ePMPf4165gfcc = _EPMPf4165gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53544)
)
_EPMPf425l5gfcc_ObjectIdentity = ObjectIdentity
ePMPf425l5gfcc = _EPMPf425l5gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53545)
)
_EPMPf6166grow_ObjectIdentity = ObjectIdentity
ePMPf6166grow = _EPMPf6166grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53552)
)
_EPMPf6256grow_ObjectIdentity = ObjectIdentity
ePMPf6256grow = _EPMPf6256grow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53553)
)
_EPMPf616usbgps6gfcc_ObjectIdentity = ObjectIdentity
ePMPf616usbgps6gfcc = _EPMPf616usbgps6gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53560)
)
_EPMPf625usbgps6gfcc_ObjectIdentity = ObjectIdentity
ePMPf625usbgps6gfcc = _EPMPf625usbgps6gfcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 9, 53561)
)

# Managed Objects groups


# Notification objects

cambiumpmp80211SoftwareUpdateStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 1)
)
cambiumpmp80211SoftwareUpdateStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumpmp80211SoftwareUpdateError"),
        ("CAMBIUM-PMP80211-MIB", "cambiumpmp80211SoftwareUpdateErrorStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211GPSSyncStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 2)
)
cambiumpmp80211GPSSyncStatusTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumToolbarGPSSyncStateStr")
)
if mibBuilder.loadTexts:
    cambiumpmp80211GPSSyncStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211SystemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 3)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SystemUpTrap.setStatus(
        "current"
    )

cambiumpmp80211DFSStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 4)
)
cambiumpmp80211DFSStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumDFSStatus"),
        ("CAMBIUM-PMP80211-MIB", "cambiumDFSStatusStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211DFSStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211JSONCfgImportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 5)
)
cambiumpmp80211JSONCfgImportTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumJSONCfgImportError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211JSONCfgImportTrap.setStatus(
        "current"
    )

cambiumpmp80211JSONCfgExportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 6)
)
cambiumpmp80211JSONCfgExportTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumJSONCfgExportError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211JSONCfgExportTrap.setStatus(
        "current"
    )

cambiumpmp80211FullCfgRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 7)
)
cambiumpmp80211FullCfgRestoreTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumFullCfgRestoreError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211FullCfgRestoreTrap.setStatus(
        "current"
    )

cambiumpmp80211FullCfgBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 8)
)
cambiumpmp80211FullCfgBackupTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumFullCfgBackUpError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211FullCfgBackupTrap.setStatus(
        "current"
    )

cambiumpmp80211GpsFirmwareUpdateStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 9)
)
cambiumpmp80211GpsFirmwareUpdateStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumpmp80211GpsFirmwareUpdateError"),
        ("CAMBIUM-PMP80211-MIB", "cambiumpmp80211GpsFirmwareUpdateErrorStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211STADropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 10)
)
cambiumpmp80211STADropTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumSTAMAC"),
        ("CAMBIUM-PMP80211-MIB", "cambiumSTADropReason"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211STADropTrap.setStatus(
        "current"
    )

cambiumpmp80211SMRegTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 11)
)
cambiumpmp80211SMRegTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumSTAMAC")
)
if mibBuilder.loadTexts:
    cambiumpmp80211SMRegTrap.setStatus(
        "current"
    )

cambiumpmp80211SystemRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 12)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SystemRebootTrap.setStatus(
        "current"
    )

cambiumpmp80211SAModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 13)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SAModeTrap.setStatus(
        "current"
    )

cambiumpmpETSIframeSkipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 14)
)
if mibBuilder.loadTexts:
    cambiumpmpETSIframeSkipTrap.setStatus(
        "current"
    )

cambiumpmp80211NetworkEntryFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 15)
)
cambiumpmp80211NetworkEntryFailureTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumNetworkEntryFailureSTAMAC"),
        ("CAMBIUM-PMP80211-MIB", "cambiumNetworkEntryFailureReason"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211NetworkEntryFailureTrap.setStatus(
        "current"
    )

cambiumpmp80211RFWatchdogTriggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 16)
)
if mibBuilder.loadTexts:
    cambiumpmp80211RFWatchdogTriggerTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PMP80211-MIB",
    **{"cambium": cambium,
       "pmpMibTree": pmpMibTree,
       "cambiumpmp80211SystemTraps": cambiumpmp80211SystemTraps,
       "cambiumpmp80211SoftwareUpdateStatusTrap": cambiumpmp80211SoftwareUpdateStatusTrap,
       "cambiumpmp80211GPSSyncStatusTrap": cambiumpmp80211GPSSyncStatusTrap,
       "cambiumpmp80211SystemUpTrap": cambiumpmp80211SystemUpTrap,
       "cambiumpmp80211DFSStatusTrap": cambiumpmp80211DFSStatusTrap,
       "cambiumpmp80211JSONCfgImportTrap": cambiumpmp80211JSONCfgImportTrap,
       "cambiumpmp80211JSONCfgExportTrap": cambiumpmp80211JSONCfgExportTrap,
       "cambiumpmp80211FullCfgRestoreTrap": cambiumpmp80211FullCfgRestoreTrap,
       "cambiumpmp80211FullCfgBackupTrap": cambiumpmp80211FullCfgBackupTrap,
       "cambiumpmp80211GpsFirmwareUpdateStatusTrap": cambiumpmp80211GpsFirmwareUpdateStatusTrap,
       "cambiumpmp80211STADropTrap": cambiumpmp80211STADropTrap,
       "cambiumpmp80211SMRegTrap": cambiumpmp80211SMRegTrap,
       "cambiumpmp80211SystemRebootTrap": cambiumpmp80211SystemRebootTrap,
       "cambiumpmp80211SAModeTrap": cambiumpmp80211SAModeTrap,
       "cambiumpmpETSIframeSkipTrap": cambiumpmpETSIframeSkipTrap,
       "cambiumpmp80211NetworkEntryFailureTrap": cambiumpmp80211NetworkEntryFailureTrap,
       "cambiumpmp80211RFWatchdogTriggerTrap": cambiumpmp80211RFWatchdogTriggerTrap,
       "cambiumPmp80211SystemStatus": cambiumPmp80211SystemStatus,
       "cambiumGeneralStatus": cambiumGeneralStatus,
       "cambiumCurrentSWInfo": cambiumCurrentSWInfo,
       "cambiumHWInfo": cambiumHWInfo,
       "cambiumDateTime": cambiumDateTime,
       "cambiumSystemUptime": cambiumSystemUptime,
       "cambiumWirelessMACAddress": cambiumWirelessMACAddress,
       "cambiumDFSStatus": cambiumDFSStatus,
       "cambiumEffectiveSyncSource": cambiumEffectiveSyncSource,
       "cambiumEffectiveCountryCode": cambiumEffectiveCountryCode,
       "cambiumEffectiveAntennaGain": cambiumEffectiveAntennaGain,
       "cambiumEffectiveTDDRatio": cambiumEffectiveTDDRatio,
       "cambiumEffectiveSSID": cambiumEffectiveSSID,
       "cambiumEffectiveAuthenticationType": cambiumEffectiveAuthenticationType,
       "cambiumEffectiveDeviceName": cambiumEffectiveDeviceName,
       "cambiumUbootVersion": cambiumUbootVersion,
       "cambiumLANMACAddress": cambiumLANMACAddress,
       "cambiumCurrentuImageIVersion": cambiumCurrentuImageIVersion,
       "cambiumCurrentuImageVersion": cambiumCurrentuImageVersion,
       "cambiumDeviceLatitude": cambiumDeviceLatitude,
       "cambiumDeviceLongitude": cambiumDeviceLongitude,
       "sysRebootCounter": sysRebootCounter,
       "cambiumDFSStatusStr": cambiumDFSStatusStr,
       "cambiumDriverType": cambiumDriverType,
       "cambiumSFPMACAddress": cambiumSFPMACAddress,
       "sysSoftRebootCounter": sysSoftRebootCounter,
       "sysHardRebootCounter": sysHardRebootCounter,
       "sysConfigFlashStatus": sysConfigFlashStatus,
       "sysWDTRebootCounter": sysWDTRebootCounter,
       "cambiumESN": cambiumESN,
       "cambiumEPMPMSN": cambiumEPMPMSN,
       "cambiumFactoryReset": cambiumFactoryReset,
       "cambiumSubModeType": cambiumSubModeType,
       "cambiumDAVersion": cambiumDAVersion,
       "ePMP2000PowerSupplyStatus": ePMP2000PowerSupplyStatus,
       "ePMP2000SmartAntennaStatus": ePMP2000SmartAntennaStatus,
       "ePMP2000ULAntennaStatus": ePMP2000ULAntennaStatus,
       "ePMP2000FPGALoadStatus": ePMP2000FPGALoadStatus,
       "cambiumSTAForceAntennaSelection": cambiumSTAForceAntennaSelection,
       "cambiumSTALinktestForceSelection": cambiumSTALinktestForceSelection,
       "cambiumEffectiveNTPServers": cambiumEffectiveNTPServers,
       "cambiumNTPDateState": cambiumNTPDateState,
       "cambiumMCUVersion": cambiumMCUVersion,
       "cambiumWireless2MACAddress": cambiumWireless2MACAddress,
       "cambiumDFS2Status": cambiumDFS2Status,
       "cambiumEffectiveSSID2": cambiumEffectiveSSID2,
       "cambiumDFS2StatusStr": cambiumDFS2StatusStr,
       "crashReporterKernelDataAvailable": crashReporterKernelDataAvailable,
       "cambiumTR069Status": cambiumTR069Status,
       "cambiumDPIStatus": cambiumDPIStatus,
       "cambiumRFStatus": cambiumRFStatus,
       "cambiumSTAConnectedRFFrequency": cambiumSTAConnectedRFFrequency,
       "cambiumSTAConnectedRFBandwidth": cambiumSTAConnectedRFBandwidth,
       "cambiumSTADLRSSI": cambiumSTADLRSSI,
       "cambiumSTADLCINR": cambiumSTADLCINR,
       "cambiumSTAConductedTXPower": cambiumSTAConductedTXPower,
       "cambiumSTAUplinkMCSMode": cambiumSTAUplinkMCSMode,
       "cambiumSTADownlinkMCSMode": cambiumSTADownlinkMCSMode,
       "cambiumSTAConnectedAP": cambiumSTAConnectedAP,
       "cambiumSTAPowerControlMode": cambiumSTAPowerControlMode,
       "cambiumAPNumberOfConnectedSTA": cambiumAPNumberOfConnectedSTA,
       "cambiumAPConnectedSTAListTable": cambiumAPConnectedSTAListTable,
       "cambiumAPConnectedSTAListEntry": cambiumAPConnectedSTAListEntry,
       "connectedSTAListMAC": connectedSTAListMAC,
       "connectedSTAListAID": connectedSTAListAID,
       "connectedSTAListChannel": connectedSTAListChannel,
       "connectedSTAListULRSSI": connectedSTAListULRSSI,
       "connectedSTAListDLRSSI": connectedSTAListDLRSSI,
       "connectedSTAListULCINR": connectedSTAListULCINR,
       "connectedSTAListDLCINR": connectedSTAListDLCINR,
       "connectedSTAListULMCS": connectedSTAListULMCS,
       "connectedSTAListDLMCS": connectedSTAListDLMCS,
       "connectedSTAListIP": connectedSTAListIP,
       "connectedSTAListMirSrc": connectedSTAListMirSrc,
       "connectedSTAListMirULRate": connectedSTAListMirULRate,
       "connectedSTAListMirDLRate": connectedSTAListMirDLRate,
       "cambiumSTADistanceKm": cambiumSTADistanceKm,
       "cambiumSTADistanceMil": cambiumSTADistanceMil,
       "cambiumPropagationDelay": cambiumPropagationDelay,
       "cambiumSTAConnectedAPListTable": cambiumSTAConnectedAPListTable,
       "cambiumSTAConnectedAPListEntry": cambiumSTAConnectedAPListEntry,
       "connectedAPListSSID": connectedAPListSSID,
       "connectedAPListBSSID": connectedAPListBSSID,
       "connectedAPListChannel": connectedAPListChannel,
       "connectedAPListFrequency": connectedAPListFrequency,
       "connectedAPListBandwidth": connectedAPListBandwidth,
       "connectedAPListRate": connectedAPListRate,
       "connectedAPListCINR": connectedAPListCINR,
       "connectedAPListRSSI": connectedAPListRSSI,
       "connectedAPListNoise": connectedAPListNoise,
       "connectedAPListINT": connectedAPListINT,
       "connectedAPListNEState": connectedAPListNEState,
       "connectedAPListNEAge": connectedAPListNEAge,
       "connectedAPListScanAge": connectedAPListScanAge,
       "connectedAPListRemainingSTA": connectedAPListRemainingSTA,
       "connectedAPListCAPS": connectedAPListCAPS,
       "connectedAPAuthMethod": connectedAPAuthMethod,
       "connectedAPListMeetNEAttemptCriteria": connectedAPListMeetNEAttemptCriteria,
       "wirelessInterfaceConnectionState": wirelessInterfaceConnectionState,
       "cambiumSTAPriority": cambiumSTAPriority,
       "cambiumSTADLSNR": cambiumSTADLSNR,
       "cambiumConnectedAPMACAddress": cambiumConnectedAPMACAddress,
       "cambiumSTAConnectedAPTable": cambiumSTAConnectedAPTable,
       "cambiumSTAConnectedAPEntry": cambiumSTAConnectedAPEntry,
       "connectedAPSSID": connectedAPSSID,
       "connectedAPBSSID": connectedAPBSSID,
       "connectedAPChannel": connectedAPChannel,
       "connectedAPFrequency": connectedAPFrequency,
       "connectedAPBandwidth": connectedAPBandwidth,
       "connectedAPRate": connectedAPRate,
       "connectedAPSNR": connectedAPSNR,
       "connectedAPRSSI": connectedAPRSSI,
       "connectedAPNoise": connectedAPNoise,
       "connectedAPINT": connectedAPINT,
       "connectedAPNEState": connectedAPNEState,
       "connectedAPNEAge": connectedAPNEAge,
       "connectedAPScanAge": connectedAPScanAge,
       "connectedAPRemainingSTA": connectedAPRemainingSTA,
       "connectedAPCAPS": connectedAPCAPS,
       "connectedAPAuthenticationMethod": connectedAPAuthenticationMethod,
       "connectedAPMeetNEAttemptCriteria": connectedAPMeetNEAttemptCriteria,
       "connectedAPIsViaInterface": connectedAPIsViaInterface,
       "connectedAPDriverMode": connectedAPDriverMode,
       "staTxCapacity": staTxCapacity,
       "staTxQuality": staTxQuality,
       "cambiumePMPElevateConnected": cambiumePMPElevateConnected,
       "cambiumRSSICh0": cambiumRSSICh0,
       "cambiumRSSICh1": cambiumRSSICh1,
       "cambiumAPConnectedSTATable": cambiumAPConnectedSTATable,
       "cambiumAPConnectedSTAEntry": cambiumAPConnectedSTAEntry,
       "connectedSTAMAC": connectedSTAMAC,
       "connectedSTAAID": connectedSTAAID,
       "connectedSTAChannel": connectedSTAChannel,
       "connectedSTAULRSSI": connectedSTAULRSSI,
       "connectedSTADLRSSI": connectedSTADLRSSI,
       "connectedSTAULSNR": connectedSTAULSNR,
       "connectedSTADLSNR": connectedSTADLSNR,
       "connectedSTAULMCS": connectedSTAULMCS,
       "connectedSTADLMCS": connectedSTADLMCS,
       "connectedSTAIP": connectedSTAIP,
       "connectedSTAPriority": connectedSTAPriority,
       "connectedSTAMirSrc": connectedSTAMirSrc,
       "connectedSTAMirULRate": connectedSTAMirULRate,
       "connectedSTAMirDLRate": connectedSTAMirDLRate,
       "connectedSTAClickTHWAddr": connectedSTAClickTHWAddr,
       "connectedSTAClickTWebPort": connectedSTAClickTWebPort,
       "connectedSTAClickTWebSec": connectedSTAClickTWebSec,
       "connectedSTAClickTHostName": connectedSTAClickTHostName,
       "connectedSTATXCapacity": connectedSTATXCapacity,
       "connectedSTATXQuality": connectedSTATXQuality,
       "connectedSTAMcastTotalGroups": connectedSTAMcastTotalGroups,
       "connectedSTAMcastGRP0": connectedSTAMcastGRP0,
       "connectedSTAMcastGRP1": connectedSTAMcastGRP1,
       "connectedSTAMcastGRP2": connectedSTAMcastGRP2,
       "connectedSTAMcastGRP3": connectedSTAMcastGRP3,
       "connectedSTAMcastGRP4": connectedSTAMcastGRP4,
       "connectedSTASessionTime": connectedSTASessionTime,
       "connectedSTADLRateMbps": connectedSTADLRateMbps,
       "connectedSTADistance": connectedSTADistance,
       "connectedSTAVerticalAngle": connectedSTAVerticalAngle,
       "connectedSTAHorizontalAngle": connectedSTAHorizontalAngle,
       "connectedSTAIsForcedAngle": connectedSTAIsForcedAngle,
       "connectedSTASKU": connectedSTASKU,
       "connectedSTALinktestForceAllow": connectedSTALinktestForceAllow,
       "connectedSTAIPv6": connectedSTAIPv6,
       "connectedSTAIsViaInterface": connectedSTAIsViaInterface,
       "connectedSTAMUMIMOGain": connectedSTAMUMIMOGain,
       "connectedSTAModelName": connectedSTAModelName,
       "connectedSTAMUMIMOAzMetric": connectedSTAMUMIMOAzMetric,
       "connectedSTAMUMIMOQuality": connectedSTAMUMIMOQuality,
       "connectedSTAMUMIMORate": connectedSTAMUMIMORate,
       "connectedSTAMUMIMOPairs": connectedSTAMUMIMOPairs,
       "connectedSTASoftwareVersion": connectedSTASoftwareVersion,
       "cambiumAPBridgeTable": cambiumAPBridgeTable,
       "cambiumAPBridgeEntry": cambiumAPBridgeEntry,
       "camAPBrTabBridgeName": camAPBrTabBridgeName,
       "camAPBrTabDevMACAddress": camAPBrTabDevMACAddress,
       "camAPBrTabDevPort": camAPBrTabDevPort,
       "camAPBrTabSTAMACAddress": camAPBrTabSTAMACAddress,
       "camAPBrTabAgingTime": camAPBrTabAgingTime,
       "cambiumSTABridgeTable": cambiumSTABridgeTable,
       "cambiumSTABridgeEntry": cambiumSTABridgeEntry,
       "camSTABrTabBridgeName": camSTABrTabBridgeName,
       "camSTABrTabDevMACAddress": camSTABrTabDevMACAddress,
       "camSTABrTabDevPort": camSTABrTabDevPort,
       "camSTABrTabAgingTime": camSTABrTabAgingTime,
       "cambiumSTAMAC": cambiumSTAMAC,
       "cambiumSTADropReason": cambiumSTADropReason,
       "cambiumNetworkEntryFailureSTAMAC": cambiumNetworkEntryFailureSTAMAC,
       "cambiumNetworkEntryFailureReason": cambiumNetworkEntryFailureReason,
       "wirelessLinkDroppedCount": wirelessLinkDroppedCount,
       "cambiumMUMIMOGainAggregated": cambiumMUMIMOGainAggregated,
       "cambiumSTA2ConnectedRFFrequency": cambiumSTA2ConnectedRFFrequency,
       "cambiumSTA2ConnectedRFBandwidth": cambiumSTA2ConnectedRFBandwidth,
       "cambiumSTA2DLRSSI": cambiumSTA2DLRSSI,
       "cambiumSTA2ConductedTXPower": cambiumSTA2ConductedTXPower,
       "cambiumSTA2UplinkMCSMode": cambiumSTA2UplinkMCSMode,
       "cambiumSTA2DownlinkMCSMode": cambiumSTA2DownlinkMCSMode,
       "cambiumSTA2ConnectedAP": cambiumSTA2ConnectedAP,
       "cambiumSTA2DLSNR": cambiumSTA2DLSNR,
       "cambiumConnectedAP2MACAddress": cambiumConnectedAP2MACAddress,
       "sta2TxCapacity": sta2TxCapacity,
       "sta2TxQuality": sta2TxQuality,
       "cambiumRSSI2Ch0": cambiumRSSI2Ch0,
       "cambiumRSSI2Ch1": cambiumRSSI2Ch1,
       "cambiumGPSStatus": cambiumGPSStatus,
       "cambiumGPSCurrentSyncState": cambiumGPSCurrentSyncState,
       "cambiumGPSLatitude": cambiumGPSLatitude,
       "cambiumGPSLongitude": cambiumGPSLongitude,
       "cambiumGPSHeight": cambiumGPSHeight,
       "cambiumGPSTime": cambiumGPSTime,
       "cambiumGPSNumTrackedSat": cambiumGPSNumTrackedSat,
       "cambiumGPSNumVisibleSat": cambiumGPSNumVisibleSat,
       "cambiumGPSSatSNRTable": cambiumGPSSatSNRTable,
       "cambiumGPSSatSNREntry": cambiumGPSSatSNREntry,
       "gpsSatelliteId": gpsSatelliteId,
       "gpsSnrValue": gpsSnrValue,
       "gpsSatelliteStatus": gpsSatelliteStatus,
       "cambiumGPSDeviceInfo": cambiumGPSDeviceInfo,
       "cambiumGPSFirmwareUpdateStatus": cambiumGPSFirmwareUpdateStatus,
       "cambiumGPSAntennaType": cambiumGPSAntennaType,
       "tddSyncInternalStateDur": tddSyncInternalStateDur,
       "tddSyncExpectedDrift": tddSyncExpectedDrift,
       "tddSyncExpectedJitter": tddSyncExpectedJitter,
       "tddSyncStatTable": tddSyncStatTable,
       "tddSyncStatEntry": tddSyncStatEntry,
       "tddSyncStatPeriod": tddSyncStatPeriod,
       "tddSyncPulseCount": tddSyncPulseCount,
       "tddSyncLostPulseCount": tddSyncLostPulseCount,
       "tddSyncInvalidPulseCount": tddSyncInvalidPulseCount,
       "tddSyncInvPulseDeviationMin": tddSyncInvPulseDeviationMin,
       "tddSyncInvPulseDeviationMax": tddSyncInvPulseDeviationMax,
       "tddSyncInvPulseDeviationAvgAbs": tddSyncInvPulseDeviationAvgAbs,
       "tddSyncDriftMin": tddSyncDriftMin,
       "tddSyncDriftMax": tddSyncDriftMax,
       "tddSyncDriftAvg": tddSyncDriftAvg,
       "tddSyncJitterMin": tddSyncJitterMin,
       "tddSyncJitterMax": tddSyncJitterMax,
       "tddSyncJitterAvgAbs": tddSyncJitterAvgAbs,
       "tddSyncState1Count": tddSyncState1Count,
       "tddSyncState1Duration": tddSyncState1Duration,
       "tddSyncState2Count": tddSyncState2Count,
       "tddSyncState2Duration": tddSyncState2Duration,
       "tddSyncState3Count": tddSyncState3Count,
       "tddSyncState3Duration": tddSyncState3Duration,
       "cambiumLinkStatus": cambiumLinkStatus,
       "cambiumLANStatus": cambiumLANStatus,
       "cambiumWLANStatus": cambiumWLANStatus,
       "cambiumEffectiveDeviceIPAddress": cambiumEffectiveDeviceIPAddress,
       "cambiumEffectiveSTANetworkMode": cambiumEffectiveSTANetworkMode,
       "cambiumEffectiveDeviceLANNetMask": cambiumEffectiveDeviceLANNetMask,
       "cambiumEffectiveDeviceDefaultGateWay": cambiumEffectiveDeviceDefaultGateWay,
       "cambiumEffectiveDeviceDNSIPAddress": cambiumEffectiveDeviceDNSIPAddress,
       "cambiumEffectiveWANIPAddress": cambiumEffectiveWANIPAddress,
       "cambiumEffectiveDeviceWANNetMask": cambiumEffectiveDeviceWANNetMask,
       "cambiumEffectiveDeviceWANPPPoEStatus": cambiumEffectiveDeviceWANPPPoEStatus,
       "cambiumLANModeStatus": cambiumLANModeStatus,
       "cambiumLANSpeedStatus": cambiumLANSpeedStatus,
       "cambiumDHCPOption82Status": cambiumDHCPOption82Status,
       "cambiumLAN2ModeStatus": cambiumLAN2ModeStatus,
       "cambiumLAN2SpeedStatus": cambiumLAN2SpeedStatus,
       "cambiumLAN2Status": cambiumLAN2Status,
       "cambiumDHCPOption66Status": cambiumDHCPOption66Status,
       "cambiumDHCPOption66URL": cambiumDHCPOption66URL,
       "cambiumDHCPOption66Error": cambiumDHCPOption66Error,
       "cambiumARPTable": cambiumARPTable,
       "cambiumARPEntry": cambiumARPEntry,
       "cambiumARPIndex": cambiumARPIndex,
       "cambiumARPMAC": cambiumARPMAC,
       "cambiumARPIP": cambiumARPIP,
       "cambiumARPInterface": cambiumARPInterface,
       "cambiumDHCPOption43URL": cambiumDHCPOption43URL,
       "cambiumManagementIFStatus": cambiumManagementIFStatus,
       "cambiumManagementIFIPAddress": cambiumManagementIFIPAddress,
       "cambiumManagementIFNetMask": cambiumManagementIFNetMask,
       "cambiumManagementIFGateway": cambiumManagementIFGateway,
       "cambiumEffectiveNetworkLanMTU": cambiumEffectiveNetworkLanMTU,
       "cambiumEffectiveNetworkBridgeMTU": cambiumEffectiveNetworkBridgeMTU,
       "cambiumStaticRoutesTable": cambiumStaticRoutesTable,
       "cambiumStaticRoutesEntry": cambiumStaticRoutesEntry,
       "cambiumStaticRoutesIndex": cambiumStaticRoutesIndex,
       "cambiumStaticRoutesDestIP": cambiumStaticRoutesDestIP,
       "cambiumStaticRoutesGW": cambiumStaticRoutesGW,
       "cambiumStaticRoutesNetmask": cambiumStaticRoutesNetmask,
       "cambiumStaticRoutesInterface": cambiumStaticRoutesInterface,
       "cambiumIPAliasTable": cambiumIPAliasTable,
       "cambiumIPAliasEntry": cambiumIPAliasEntry,
       "cambiumIPAliasTableIndex": cambiumIPAliasTableIndex,
       "cambiumIPAliasIP": cambiumIPAliasIP,
       "cambiumIPAliasNetmask": cambiumIPAliasNetmask,
       "cambiumCnsServConsStat": cambiumCnsServConsStat,
       "cambiumCnsServAccountID": cambiumCnsServAccountID,
       "cambiumAPCnsMGMTState": cambiumAPCnsMGMTState,
       "cambiumEffectiveDeviceIPv6Address": cambiumEffectiveDeviceIPv6Address,
       "cambiumLinkLocalDeviceIPv6Address": cambiumLinkLocalDeviceIPv6Address,
       "cambiumEffectiveWANIPv6Address": cambiumEffectiveWANIPv6Address,
       "cambiumLinkLocalWANIPv6Address": cambiumLinkLocalWANIPv6Address,
       "cambiumManagementIFIPv6Address": cambiumManagementIFIPv6Address,
       "cambiumLinkLocalManagementIFIPv6Address": cambiumLinkLocalManagementIFIPv6Address,
       "cambiumEffectiveDeviceIPv6DefaultGateWay": cambiumEffectiveDeviceIPv6DefaultGateWay,
       "cambiumManagementIFIPv6Gateway": cambiumManagementIFIPv6Gateway,
       "cambiumSFPConnectorType": cambiumSFPConnectorType,
       "cambiumSFPEthernetCodes": cambiumSFPEthernetCodes,
       "cambiumSFPEncodingCodes": cambiumSFPEncodingCodes,
       "cambiumSFPBRNominal": cambiumSFPBRNominal,
       "cambiumSFPVendorName": cambiumSFPVendorName,
       "cambiumSFPVendorOUI": cambiumSFPVendorOUI,
       "cambiumSFPVendorPN": cambiumSFPVendorPN,
       "cambiumEffectiveNetworkLan2MTU": cambiumEffectiveNetworkLan2MTU,
       "cambiumEffectiveManagementIFIPv6Address": cambiumEffectiveManagementIFIPv6Address,
       "cambiumLanIPv6PrefixDelegated": cambiumLanIPv6PrefixDelegated,
       "lanSwitchPortsNum": lanSwitchPortsNum,
       "lanSwitchPortStatusTable": lanSwitchPortStatusTable,
       "lanSwitchPortStatusEntry": lanSwitchPortStatusEntry,
       "lanSwitchPortCAPS": lanSwitchPortCAPS,
       "lanSwitchPortEnableStatus": lanSwitchPortEnableStatus,
       "lanSwitchPortLinkStatus": lanSwitchPortLinkStatus,
       "lanSwitchPortAutonegStatus": lanSwitchPortAutonegStatus,
       "lanSwitchPortSpeedStatus": lanSwitchPortSpeedStatus,
       "lanSwitchPortDuplexStatus": lanSwitchPortDuplexStatus,
       "lanSwitchPortPoEStatus": lanSwitchPortPoEStatus,
       "lanSwitchPortPoEVoltage": lanSwitchPortPoEVoltage,
       "lanSwitchPortPoECurrent": lanSwitchPortPoECurrent,
       "cambiumWLAN2Status": cambiumWLAN2Status,
       "cambiumAcsStatus": cambiumAcsStatus,
       "acsState": acsState,
       "cambiumMcastStatus": cambiumMcastStatus,
       "cambiumEffectiveMcastGroupLimit": cambiumEffectiveMcastGroupLimit,
       "cambiumSubscribedMcastGroupNum": cambiumSubscribedMcastGroupNum,
       "cambiumAPMcastTotalGroupCount": cambiumAPMcastTotalGroupCount,
       "cambiumMcastHandlingStatus": cambiumMcastHandlingStatus,
       "cambiumSubscribedMcastGroupTable": cambiumSubscribedMcastGroupTable,
       "cambiumSubscribedMcastGroupEntry": cambiumSubscribedMcastGroupEntry,
       "cambiumRegisteredMcastGroupIP": cambiumRegisteredMcastGroupIP,
       "cambiumDhcpStatus": cambiumDhcpStatus,
       "dhcpServerStartIP": dhcpServerStartIP,
       "dhcpServerEndIP": dhcpServerEndIP,
       "dhcpServerGatewayIP": dhcpServerGatewayIP,
       "dhcpServerDNSIP": dhcpServerDNSIP,
       "dhcpServerStaticHostTable": dhcpServerStaticHostTable,
       "dhcpServerStaticHostEntry": dhcpServerStaticHostEntry,
       "dhcpStaticIndex": dhcpStaticIndex,
       "dhcpStaticMAC": dhcpStaticMAC,
       "dhcpStaticIP": dhcpStaticIP,
       "dhcpServerLeaseTable": dhcpServerLeaseTable,
       "dhcpServerLeaseEntry": dhcpServerLeaseEntry,
       "dhcpLeaseIndex": dhcpLeaseIndex,
       "dhcpLeaseMAC": dhcpLeaseMAC,
       "dhcpLeaseIP": dhcpLeaseIP,
       "dhcpLeaseDevName": dhcpLeaseDevName,
       "cambiumLicenseInfo": cambiumLicenseInfo,
       "cambLicenseVersion": cambLicenseVersion,
       "cambLicenseSMcntUnlock": cambLicenseSMcntUnlock,
       "cambLicenseMACaddr": cambLicenseMACaddr,
       "cambLicenseCountry": cambLicenseCountry,
       "cambLicenseStatus": cambLicenseStatus,
       "cambLicenseDPIUnlockQoS": cambLicenseDPIUnlockQoS,
       "cambiumRadiusVSAStatus": cambiumRadiusVSAStatus,
       "networkRadiusVSAmgmtVLANVID": networkRadiusVSAmgmtVLANVID,
       "networkRadiusVSAmgmtVLANVP": networkRadiusVSAmgmtVLANVP,
       "networkRadiusVSAdataVLANVID": networkRadiusVSAdataVLANVID,
       "networkRadiusVSAdataVLANVP": networkRadiusVSAdataVLANVP,
       "networkRadiusVSAmgmtIFVID": networkRadiusVSAmgmtIFVID,
       "networkRadiusVSAmgmtIFVP": networkRadiusVSAmgmtIFVP,
       "networkRadiusVSAmcastVLANVID": networkRadiusVSAmcastVLANVID,
       "networkRadiusVSAGUIauthType": networkRadiusVSAGUIauthType,
       "networkRadiusVSAmembershipVLANTable": networkRadiusVSAmembershipVLANTable,
       "networkRadiusVSAmembershipVLANEntry": networkRadiusVSAmembershipVLANEntry,
       "networkRadiusVSAmembershipVLANIndex": networkRadiusVSAmembershipVLANIndex,
       "networkRadiusVSAmembershipVLANVIDBegin": networkRadiusVSAmembershipVLANVIDBegin,
       "networkRadiusVSAmembershipVLANVIDEnd": networkRadiusVSAmembershipVLANVIDEnd,
       "networkRadiusVSAmappingVLANTable": networkRadiusVSAmappingVLANTable,
       "networkRadiusVSAmappingVLANEntry": networkRadiusVSAmappingVLANEntry,
       "networkRadiusVSAmappingVLANIndex": networkRadiusVSAmappingVLANIndex,
       "networkRadiusVSAmappingVLANCVLAN": networkRadiusVSAmappingVLANCVLAN,
       "networkRadiusVSAmappingVLANSVLAN": networkRadiusVSAmappingVLANSVLAN,
       "cambiumCCTVStatus": cambiumCCTVStatus,
       "cambiumONVIFTable": cambiumONVIFTable,
       "cambiumONVIFEntry": cambiumONVIFEntry,
       "cambiumONVIFIndex": cambiumONVIFIndex,
       "cambiumONVIFMAC": cambiumONVIFMAC,
       "cambiumONVIFIP": cambiumONVIFIP,
       "cambiumONVIFHardware": cambiumONVIFHardware,
       "cambiumONVIFName": cambiumONVIFName,
       "cambiumONVIFLocation": cambiumONVIFLocation,
       "cambiumONVIFProbeTime": cambiumONVIFProbeTime,
       "cambiumONVIFSTAMAC": cambiumONVIFSTAMAC,
       "cambiumPmp80211SystemMonitoring": cambiumPmp80211SystemMonitoring,
       "cambiumPerformanceMonitoring": cambiumPerformanceMonitoring,
       "cambiumStatsForceUpdate": cambiumStatsForceUpdate,
       "cambiumEthRXBytes": cambiumEthRXBytes,
       "cambiumEthRXPackets": cambiumEthRXPackets,
       "cambiumEthRXErrors": cambiumEthRXErrors,
       "cambiumEthRXDrops": cambiumEthRXDrops,
       "cambiumEthRXMulticast": cambiumEthRXMulticast,
       "cambiumEthRXBroadcast": cambiumEthRXBroadcast,
       "cambiumEthTXBytes": cambiumEthTXBytes,
       "cambiumEthTXPackets": cambiumEthTXPackets,
       "cambiumEthTXErrors": cambiumEthTXErrors,
       "cambiumEthTXDrops": cambiumEthTXDrops,
       "cambiumEthTXMulticast": cambiumEthTXMulticast,
       "cambiumEthTXBroadcast": cambiumEthTXBroadcast,
       "cambiumAthRXBytes": cambiumAthRXBytes,
       "cambiumAthRXPackets": cambiumAthRXPackets,
       "cambiumAthRXErrors": cambiumAthRXErrors,
       "cambiumAthRXDrops": cambiumAthRXDrops,
       "cambiumAthRXMulticast": cambiumAthRXMulticast,
       "cambiumAthRXBroadcast": cambiumAthRXBroadcast,
       "cambiumAthTXBytes": cambiumAthTXBytes,
       "cambiumAthTXPackets": cambiumAthTXPackets,
       "cambiumAthTXErrors": cambiumAthTXErrors,
       "cambiumAthTXDrops": cambiumAthTXDrops,
       "cambiumAthTXMulticast": cambiumAthTXMulticast,
       "cambiumAthTXBroadcast": cambiumAthTXBroadcast,
       "sysNetworkEntryAttempt": sysNetworkEntryAttempt,
       "sysNetworkEntrySuccess": sysNetworkEntrySuccess,
       "sysNetworkEntryAuthenticationFailure": sysNetworkEntryAuthenticationFailure,
       "sysDFSDetectedCount": sysDFSDetectedCount,
       "ulWLanKbitCount": ulWLanKbitCount,
       "dlWLanKbitCount": dlWLanKbitCount,
       "ulWLanTotalPacketCount": ulWLanTotalPacketCount,
       "muWLanKbitCount": muWLanKbitCount,
       "sysRebootCount": sysRebootCount,
       "dlWLanTotalPacketCount": dlWLanTotalPacketCount,
       "ulWLanMultiBroadcastKbitCount": ulWLanMultiBroadcastKbitCount,
       "dlWLanMultiBroadcastKbitCount": dlWLanMultiBroadcastKbitCount,
       "wLanSessionDroppedCount": wLanSessionDroppedCount,
       "cambiumTDDStatsPerSTATable": cambiumTDDStatsPerSTATable,
       "cambiumTDDStatsPerSTAEntry": cambiumTDDStatsPerSTAEntry,
       "cambiumTDDStatsPerSTAIndex": cambiumTDDStatsPerSTAIndex,
       "cambiumTDDStatsListMAC": cambiumTDDStatsListMAC,
       "ulWLanPerUserKbitCount": ulWLanPerUserKbitCount,
       "dlWLanPerUserKbitCount": dlWLanPerUserKbitCount,
       "ulWLanPerUserTotalPacketCount": ulWLanPerUserTotalPacketCount,
       "dlWLanPerUserTotalPacketCount": dlWLanPerUserTotalPacketCount,
       "ulWLanPerUserErrorDroppedPacketCount": ulWLanPerUserErrorDroppedPacketCount,
       "dlWLanPerUserErrorDroppedPacketCount": dlWLanPerUserErrorDroppedPacketCount,
       "dlWLanPerUserCapacityDroppedPacketCount": dlWLanPerUserCapacityDroppedPacketCount,
       "dlWLanPerUserRetransmitPacketCount": dlWLanPerUserRetransmitPacketCount,
       "dlWLanPerUserTxPower": dlWLanPerUserTxPower,
       "cambiumTDDStatsIP": cambiumTDDStatsIP,
       "cambiumTDDStatsDevName": cambiumTDDStatsDevName,
       "dlWLanPerUserRetransmitMsduCount": dlWLanPerUserRetransmitMsduCount,
       "ulWLanErrorDroppedPacketCount": ulWLanErrorDroppedPacketCount,
       "dlWLanErrorDroppedPacketCount": dlWLanErrorDroppedPacketCount,
       "ulWLanCapacityDroppedPacketCount": ulWLanCapacityDroppedPacketCount,
       "dlWLanCapacityDroppedPacketCount": dlWLanCapacityDroppedPacketCount,
       "ulWLanTotalAvailableFrameTimePerSecond": ulWLanTotalAvailableFrameTimePerSecond,
       "dlWLanTotalAvailableFrameTimePerSecond": dlWLanTotalAvailableFrameTimePerSecond,
       "ulWLanTotalUsedFrameTimePerSecond": ulWLanTotalUsedFrameTimePerSecond,
       "dlWLanTotalUsedFrameTimePerSecond": dlWLanTotalUsedFrameTimePerSecond,
       "ulWLanTotalOverheadFrameTimePerSecond": ulWLanTotalOverheadFrameTimePerSecond,
       "dlWLanTotalOverheadFrameTimePerSecond": dlWLanTotalOverheadFrameTimePerSecond,
       "cambiumMCSTable": cambiumMCSTable,
       "cambiumMCSEntry": cambiumMCSEntry,
       "cambiumMCSIndex": cambiumMCSIndex,
       "cambiumMCSNumber": cambiumMCSNumber,
       "ulWLanMCSUsedFrameTimePerSecond": ulWLanMCSUsedFrameTimePerSecond,
       "dlWLanMCSUsedFrameTimePerSecond": dlWLanMCSUsedFrameTimePerSecond,
       "ulWLanRetransPacketCount": ulWLanRetransPacketCount,
       "dlWLanRetransPacketCount": dlWLanRetransPacketCount,
       "ulWLanBroadcastPacketCount": ulWLanBroadcastPacketCount,
       "dlWLanBroadcastPacketCount": dlWLanBroadcastPacketCount,
       "ulWLanMulticastPacketCount": ulWLanMulticastPacketCount,
       "dlWLanMulticastPacketCount": dlWLanMulticastPacketCount,
       "sysCPUUsage": sysCPUUsage,
       "rxEtherLanKbitCount": rxEtherLanKbitCount,
       "rxEtherLanTotalPacketCount": rxEtherLanTotalPacketCount,
       "rxEtherLanErrorPacketCount": rxEtherLanErrorPacketCount,
       "rxEtherLanDroppedPacketCount": rxEtherLanDroppedPacketCount,
       "rxEtherLanMulticastPacketCount": rxEtherLanMulticastPacketCount,
       "rxEtherLanBroadcastPacketCount": rxEtherLanBroadcastPacketCount,
       "rxEtherLanMultiBroadcastKbitCount": rxEtherLanMultiBroadcastKbitCount,
       "txEtherLanKbitCount": txEtherLanKbitCount,
       "txEtherLanTotalPacketCount": txEtherLanTotalPacketCount,
       "txEtherLanErrorPacketCount": txEtherLanErrorPacketCount,
       "txEtherLanDroppedPacketCount": txEtherLanDroppedPacketCount,
       "txEtherLanMulticastPacketCount": txEtherLanMulticastPacketCount,
       "txEtherLanBroadcastPacketCount": txEtherLanBroadcastPacketCount,
       "txEtherLanMultiBroadcastKbitCount": txEtherLanMultiBroadcastKbitCount,
       "cambiumStatsResetTimer": cambiumStatsResetTimer,
       "ulWLanMCS00Packets": ulWLanMCS00Packets,
       "ulWLanMCS01Packets": ulWLanMCS01Packets,
       "ulWLanMCS02Packets": ulWLanMCS02Packets,
       "ulWLanMCS03Packets": ulWLanMCS03Packets,
       "ulWLanMCS04Packets": ulWLanMCS04Packets,
       "ulWLanMCS05Packets": ulWLanMCS05Packets,
       "ulWLanMCS06Packets": ulWLanMCS06Packets,
       "ulWLanMCS07Packets": ulWLanMCS07Packets,
       "ulWLanMCS08Packets": ulWLanMCS08Packets,
       "ulWLanMCS09Packets": ulWLanMCS09Packets,
       "ulWLanMCS10Packets": ulWLanMCS10Packets,
       "ulWLanMCS11Packets": ulWLanMCS11Packets,
       "ulWLanMCS12Packets": ulWLanMCS12Packets,
       "ulWLanMCS13Packets": ulWLanMCS13Packets,
       "ulWLanMCS14Packets": ulWLanMCS14Packets,
       "ulWLanMCS15Packets": ulWLanMCS15Packets,
       "dlWLanMCS00Packets": dlWLanMCS00Packets,
       "dlWLanMCS01Packets": dlWLanMCS01Packets,
       "dlWLanMCS02Packets": dlWLanMCS02Packets,
       "dlWLanMCS03Packets": dlWLanMCS03Packets,
       "dlWLanMCS04Packets": dlWLanMCS04Packets,
       "dlWLanMCS05Packets": dlWLanMCS05Packets,
       "dlWLanMCS06Packets": dlWLanMCS06Packets,
       "dlWLanMCS07Packets": dlWLanMCS07Packets,
       "dlWLanMCS08Packets": dlWLanMCS08Packets,
       "dlWLanMCS09Packets": dlWLanMCS09Packets,
       "dlWLanMCS10Packets": dlWLanMCS10Packets,
       "dlWLanMCS11Packets": dlWLanMCS11Packets,
       "dlWLanMCS12Packets": dlWLanMCS12Packets,
       "dlWLanMCS13Packets": dlWLanMCS13Packets,
       "dlWLanMCS14Packets": dlWLanMCS14Packets,
       "dlWLanMCS15Packets": dlWLanMCS15Packets,
       "ulWLanTotalAvailableFrameTimePercentage": ulWLanTotalAvailableFrameTimePercentage,
       "dlWLanTotalAvailableFrameTimePercentage": dlWLanTotalAvailableFrameTimePercentage,
       "wlanMCSPackets": wlanMCSPackets,
       "dlWLanMCS00UnicastPackets": dlWLanMCS00UnicastPackets,
       "dlWLanMCS01UnicastPackets": dlWLanMCS01UnicastPackets,
       "dlWLanMCS02UnicastPackets": dlWLanMCS02UnicastPackets,
       "dlWLanMCS03UnicastPackets": dlWLanMCS03UnicastPackets,
       "dlWLanMCS04UnicastPackets": dlWLanMCS04UnicastPackets,
       "dlWLanMCS05UnicastPackets": dlWLanMCS05UnicastPackets,
       "dlWLanMCS06UnicastPackets": dlWLanMCS06UnicastPackets,
       "dlWLanMCS07UnicastPackets": dlWLanMCS07UnicastPackets,
       "dlWLanMCS08UnicastPackets": dlWLanMCS08UnicastPackets,
       "dlWLanMCS09UnicastPackets": dlWLanMCS09UnicastPackets,
       "dlWLanMCS10UnicastPackets": dlWLanMCS10UnicastPackets,
       "dlWLanMCS11UnicastPackets": dlWLanMCS11UnicastPackets,
       "dlWLanMCS12UnicastPackets": dlWLanMCS12UnicastPackets,
       "dlWLanMCS13UnicastPackets": dlWLanMCS13UnicastPackets,
       "dlWLanMCS14UnicastPackets": dlWLanMCS14UnicastPackets,
       "dlWLanMCS15UnicastPackets": dlWLanMCS15UnicastPackets,
       "ulWLanMCS00UnicastPackets": ulWLanMCS00UnicastPackets,
       "ulWLanMCS01UnicastPackets": ulWLanMCS01UnicastPackets,
       "ulWLanMCS02UnicastPackets": ulWLanMCS02UnicastPackets,
       "ulWLanMCS03UnicastPackets": ulWLanMCS03UnicastPackets,
       "ulWLanMCS04UnicastPackets": ulWLanMCS04UnicastPackets,
       "ulWLanMCS05UnicastPackets": ulWLanMCS05UnicastPackets,
       "ulWLanMCS06UnicastPackets": ulWLanMCS06UnicastPackets,
       "ulWLanMCS07UnicastPackets": ulWLanMCS07UnicastPackets,
       "ulWLanMCS08UnicastPackets": ulWLanMCS08UnicastPackets,
       "ulWLanMCS09UnicastPackets": ulWLanMCS09UnicastPackets,
       "ulWLanMCS10UnicastPackets": ulWLanMCS10UnicastPackets,
       "ulWLanMCS11UnicastPackets": ulWLanMCS11UnicastPackets,
       "ulWLanMCS12UnicastPackets": ulWLanMCS12UnicastPackets,
       "ulWLanMCS13UnicastPackets": ulWLanMCS13UnicastPackets,
       "ulWLanMCS14UnicastPackets": ulWLanMCS14UnicastPackets,
       "ulWLanMCS15UnicastPackets": ulWLanMCS15UnicastPackets,
       "dlWLanMCS00MulticastPackets": dlWLanMCS00MulticastPackets,
       "dlWLanMCS01MulticastPackets": dlWLanMCS01MulticastPackets,
       "dlWLanMCS02MulticastPackets": dlWLanMCS02MulticastPackets,
       "dlWLanMCS03MulticastPackets": dlWLanMCS03MulticastPackets,
       "dlWLanMCS04MulticastPackets": dlWLanMCS04MulticastPackets,
       "dlWLanMCS05MulticastPackets": dlWLanMCS05MulticastPackets,
       "dlWLanMCS06MulticastPackets": dlWLanMCS06MulticastPackets,
       "dlWLanMCS07MulticastPackets": dlWLanMCS07MulticastPackets,
       "dlWLanMCS08MulticastPackets": dlWLanMCS08MulticastPackets,
       "dlWLanMCS09MulticastPackets": dlWLanMCS09MulticastPackets,
       "dlWLanMCS10MulticastPackets": dlWLanMCS10MulticastPackets,
       "dlWLanMCS11MulticastPackets": dlWLanMCS11MulticastPackets,
       "dlWLanMCS12MulticastPackets": dlWLanMCS12MulticastPackets,
       "dlWLanMCS13MulticastPackets": dlWLanMCS13MulticastPackets,
       "dlWLanMCS14MulticastPackets": dlWLanMCS14MulticastPackets,
       "dlWLanMCS15MulticastPackets": dlWLanMCS15MulticastPackets,
       "ulWLanMCS00MulticastPackets": ulWLanMCS00MulticastPackets,
       "ulWLanMCS01MulticastPackets": ulWLanMCS01MulticastPackets,
       "ulWLanMCS02MulticastPackets": ulWLanMCS02MulticastPackets,
       "ulWLanMCS03MulticastPackets": ulWLanMCS03MulticastPackets,
       "ulWLanMCS04MulticastPackets": ulWLanMCS04MulticastPackets,
       "ulWLanMCS05MulticastPackets": ulWLanMCS05MulticastPackets,
       "ulWLanMCS06MulticastPackets": ulWLanMCS06MulticastPackets,
       "ulWLanMCS07MulticastPackets": ulWLanMCS07MulticastPackets,
       "ulWLanMCS08MulticastPackets": ulWLanMCS08MulticastPackets,
       "ulWLanMCS09MulticastPackets": ulWLanMCS09MulticastPackets,
       "ulWLanMCS10MulticastPackets": ulWLanMCS10MulticastPackets,
       "ulWLanMCS11MulticastPackets": ulWLanMCS11MulticastPackets,
       "ulWLanMCS12MulticastPackets": ulWLanMCS12MulticastPackets,
       "ulWLanMCS13MulticastPackets": ulWLanMCS13MulticastPackets,
       "ulWLanMCS14MulticastPackets": ulWLanMCS14MulticastPackets,
       "ulWLanMCS15MulticastPackets": ulWLanMCS15MulticastPackets,
       "ePMP2000MapMissCounter": ePMP2000MapMissCounter,
       "ePMP2000PatternSkipCounter": ePMP2000PatternSkipCounter,
       "ePMP2000ErrorsSmartAntennaInterface": ePMP2000ErrorsSmartAntennaInterface,
       "classificationVoiceQueuePutPacketCount": classificationVoiceQueuePutPacketCount,
       "classificationVoiceQueueGetPacketCount": classificationVoiceQueueGetPacketCount,
       "classificationVoiceQueueDropPacketCount": classificationVoiceQueueDropPacketCount,
       "classificationHighQueuePutPacketCount": classificationHighQueuePutPacketCount,
       "classificationHighQueueGetPacketCount": classificationHighQueueGetPacketCount,
       "classificationHighQueueDropPacketCount": classificationHighQueueDropPacketCount,
       "classificationLowQueuePutPacketCount": classificationLowQueuePutPacketCount,
       "classificationLowQueueGetPacketCount": classificationLowQueueGetPacketCount,
       "classificationLowQueueDropPacketCount": classificationLowQueueDropPacketCount,
       "classificationTotalQueuePutPacketCount": classificationTotalQueuePutPacketCount,
       "classificationTotalQueueGetPacketCount": classificationTotalQueueGetPacketCount,
       "classificationTotalQueueDropPacketCount": classificationTotalQueueDropPacketCount,
       "ulWLanVHTMCS0SSPackets": ulWLanVHTMCS0SSPackets,
       "ulWLanVHTMCS1SSPackets": ulWLanVHTMCS1SSPackets,
       "ulWLanVHTMCS2SSPackets": ulWLanVHTMCS2SSPackets,
       "ulWLanVHTMCS3SSPackets": ulWLanVHTMCS3SSPackets,
       "ulWLanVHTMCS4SSPackets": ulWLanVHTMCS4SSPackets,
       "ulWLanVHTMCS5SSPackets": ulWLanVHTMCS5SSPackets,
       "ulWLanVHTMCS6SSPackets": ulWLanVHTMCS6SSPackets,
       "ulWLanVHTMCS7SSPackets": ulWLanVHTMCS7SSPackets,
       "ulWLanVHTMCS8SSPackets": ulWLanVHTMCS8SSPackets,
       "ulWLanVHTMCS9SSPackets": ulWLanVHTMCS9SSPackets,
       "ulWLanVHTMCS0DSPackets": ulWLanVHTMCS0DSPackets,
       "ulWLanVHTMCS1DSPackets": ulWLanVHTMCS1DSPackets,
       "ulWLanVHTMCS2DSPackets": ulWLanVHTMCS2DSPackets,
       "ulWLanVHTMCS3DSPackets": ulWLanVHTMCS3DSPackets,
       "ulWLanVHTMCS4DSPackets": ulWLanVHTMCS4DSPackets,
       "ulWLanVHTMCS5DSPackets": ulWLanVHTMCS5DSPackets,
       "ulWLanVHTMCS6DSPackets": ulWLanVHTMCS6DSPackets,
       "ulWLanVHTMCS7DSPackets": ulWLanVHTMCS7DSPackets,
       "ulWLanVHTMCS8DSPackets": ulWLanVHTMCS8DSPackets,
       "ulWLanVHTMCS9DSPackets": ulWLanVHTMCS9DSPackets,
       "dlWLanVHTMCS0SSPackets": dlWLanVHTMCS0SSPackets,
       "dlWLanVHTMCS1SSPackets": dlWLanVHTMCS1SSPackets,
       "dlWLanVHTMCS2SSPackets": dlWLanVHTMCS2SSPackets,
       "dlWLanVHTMCS3SSPackets": dlWLanVHTMCS3SSPackets,
       "dlWLanVHTMCS4SSPackets": dlWLanVHTMCS4SSPackets,
       "dlWLanVHTMCS5SSPackets": dlWLanVHTMCS5SSPackets,
       "dlWLanVHTMCS6SSPackets": dlWLanVHTMCS6SSPackets,
       "dlWLanVHTMCS7SSPackets": dlWLanVHTMCS7SSPackets,
       "dlWLanVHTMCS8SSPackets": dlWLanVHTMCS8SSPackets,
       "dlWLanVHTMCS9SSPackets": dlWLanVHTMCS9SSPackets,
       "dlWLanVHTMCS0DSPackets": dlWLanVHTMCS0DSPackets,
       "dlWLanVHTMCS1DSPackets": dlWLanVHTMCS1DSPackets,
       "dlWLanVHTMCS2DSPackets": dlWLanVHTMCS2DSPackets,
       "dlWLanVHTMCS3DSPackets": dlWLanVHTMCS3DSPackets,
       "dlWLanVHTMCS4DSPackets": dlWLanVHTMCS4DSPackets,
       "dlWLanVHTMCS5DSPackets": dlWLanVHTMCS5DSPackets,
       "dlWLanVHTMCS6DSPackets": dlWLanVHTMCS6DSPackets,
       "dlWLanVHTMCS7DSPackets": dlWLanVHTMCS7DSPackets,
       "dlWLanVHTMCS8DSPackets": dlWLanVHTMCS8DSPackets,
       "dlWLanVHTMCS9DSPackets": dlWLanVHTMCS9DSPackets,
       "wLanSNRDeviation00Cnt": wLanSNRDeviation00Cnt,
       "wLanSNRDeviation01Cnt": wLanSNRDeviation01Cnt,
       "wLanSNRDeviation02Cnt": wLanSNRDeviation02Cnt,
       "wLanSNRDeviation03Cnt": wLanSNRDeviation03Cnt,
       "wLanSNRDeviation04Cnt": wLanSNRDeviation04Cnt,
       "wLanSNRDeviation05Cnt": wLanSNRDeviation05Cnt,
       "wLanSNRDeviation06Cnt": wLanSNRDeviation06Cnt,
       "wLanSNRDeviation07Cnt": wLanSNRDeviation07Cnt,
       "wLanSNRDeviation08Cnt": wLanSNRDeviation08Cnt,
       "wLanSNRDeviation09Cnt": wLanSNRDeviation09Cnt,
       "wLanSNRDeviation10Cnt": wLanSNRDeviation10Cnt,
       "wLanSNRDeviation11Cnt": wLanSNRDeviation11Cnt,
       "wLanSNRDeviation12Cnt": wLanSNRDeviation12Cnt,
       "wLanSNRDeviation13Cnt": wLanSNRDeviation13Cnt,
       "wLanSNRDeviation14Cnt": wLanSNRDeviation14Cnt,
       "wLanSNRDeviation15Cnt": wLanSNRDeviation15Cnt,
       "wLanSNRDeviation16Cnt": wLanSNRDeviation16Cnt,
       "wLanSNRDeviation17Cnt": wLanSNRDeviation17Cnt,
       "wLanSNRDeviation18Cnt": wLanSNRDeviation18Cnt,
       "wLanSNRDeviation19Cnt": wLanSNRDeviation19Cnt,
       "wlanHEMCSPackets": wlanHEMCSPackets,
       "dlWlanHEMCSPackets": dlWlanHEMCSPackets,
       "dlWLanHEMCS0S1Packets": dlWLanHEMCS0S1Packets,
       "dlWLanHEMCS1S1Packets": dlWLanHEMCS1S1Packets,
       "dlWLanHEMCS2S1Packets": dlWLanHEMCS2S1Packets,
       "dlWLanHEMCS3S1Packets": dlWLanHEMCS3S1Packets,
       "dlWLanHEMCS4S1Packets": dlWLanHEMCS4S1Packets,
       "dlWLanHEMCS5S1Packets": dlWLanHEMCS5S1Packets,
       "dlWLanHEMCS6S1Packets": dlWLanHEMCS6S1Packets,
       "dlWLanHEMCS7S1Packets": dlWLanHEMCS7S1Packets,
       "dlWLanHEMCS8S1Packets": dlWLanHEMCS8S1Packets,
       "dlWLanHEMCS9S1Packets": dlWLanHEMCS9S1Packets,
       "dlWLanHEMCS10S1Packets": dlWLanHEMCS10S1Packets,
       "dlWLanHEMCS11S1Packets": dlWLanHEMCS11S1Packets,
       "dlWLanHEMCS0S2Packets": dlWLanHEMCS0S2Packets,
       "dlWLanHEMCS1S2Packets": dlWLanHEMCS1S2Packets,
       "dlWLanHEMCS2S2Packets": dlWLanHEMCS2S2Packets,
       "dlWLanHEMCS3S2Packets": dlWLanHEMCS3S2Packets,
       "dlWLanHEMCS4S2Packets": dlWLanHEMCS4S2Packets,
       "dlWLanHEMCS5S2Packets": dlWLanHEMCS5S2Packets,
       "dlWLanHEMCS6S2Packets": dlWLanHEMCS6S2Packets,
       "dlWLanHEMCS7S2Packets": dlWLanHEMCS7S2Packets,
       "dlWLanHEMCS8S2Packets": dlWLanHEMCS8S2Packets,
       "dlWLanHEMCS9S2Packets": dlWLanHEMCS9S2Packets,
       "dlWLanHEMCS10S2Packets": dlWLanHEMCS10S2Packets,
       "dlWLanHEMCS11S2Packets": dlWLanHEMCS11S2Packets,
       "dlWLanHEMCS0S3Packets": dlWLanHEMCS0S3Packets,
       "dlWLanHEMCS1S3Packets": dlWLanHEMCS1S3Packets,
       "dlWLanHEMCS2S3Packets": dlWLanHEMCS2S3Packets,
       "dlWLanHEMCS3S3Packets": dlWLanHEMCS3S3Packets,
       "dlWLanHEMCS4S3Packets": dlWLanHEMCS4S3Packets,
       "dlWLanHEMCS5S3Packets": dlWLanHEMCS5S3Packets,
       "dlWLanHEMCS6S3Packets": dlWLanHEMCS6S3Packets,
       "dlWLanHEMCS7S3Packets": dlWLanHEMCS7S3Packets,
       "dlWLanHEMCS8S3Packets": dlWLanHEMCS8S3Packets,
       "dlWLanHEMCS9S3Packets": dlWLanHEMCS9S3Packets,
       "dlWLanHEMCS10S3Packets": dlWLanHEMCS10S3Packets,
       "dlWLanHEMCS11S3Packets": dlWLanHEMCS11S3Packets,
       "dlWLanHEMCS0S4Packets": dlWLanHEMCS0S4Packets,
       "dlWLanHEMCS1S4Packets": dlWLanHEMCS1S4Packets,
       "dlWLanHEMCS2S4Packets": dlWLanHEMCS2S4Packets,
       "dlWLanHEMCS3S4Packets": dlWLanHEMCS3S4Packets,
       "dlWLanHEMCS4S4Packets": dlWLanHEMCS4S4Packets,
       "dlWLanHEMCS5S4Packets": dlWLanHEMCS5S4Packets,
       "dlWLanHEMCS6S4Packets": dlWLanHEMCS6S4Packets,
       "dlWLanHEMCS7S4Packets": dlWLanHEMCS7S4Packets,
       "dlWLanHEMCS8S4Packets": dlWLanHEMCS8S4Packets,
       "dlWLanHEMCS9S4Packets": dlWLanHEMCS9S4Packets,
       "dlWLanHEMCS10S4Packets": dlWLanHEMCS10S4Packets,
       "dlWLanHEMCS11S4Packets": dlWLanHEMCS11S4Packets,
       "dlWLanHEMCS0S5Packets": dlWLanHEMCS0S5Packets,
       "dlWLanHEMCS1S5Packets": dlWLanHEMCS1S5Packets,
       "dlWLanHEMCS2S5Packets": dlWLanHEMCS2S5Packets,
       "dlWLanHEMCS3S5Packets": dlWLanHEMCS3S5Packets,
       "dlWLanHEMCS4S5Packets": dlWLanHEMCS4S5Packets,
       "dlWLanHEMCS5S5Packets": dlWLanHEMCS5S5Packets,
       "dlWLanHEMCS6S5Packets": dlWLanHEMCS6S5Packets,
       "dlWLanHEMCS7S5Packets": dlWLanHEMCS7S5Packets,
       "dlWLanHEMCS8S5Packets": dlWLanHEMCS8S5Packets,
       "dlWLanHEMCS9S5Packets": dlWLanHEMCS9S5Packets,
       "dlWLanHEMCS10S5Packets": dlWLanHEMCS10S5Packets,
       "dlWLanHEMCS11S5Packets": dlWLanHEMCS11S5Packets,
       "dlWLanHEMCS0S6Packets": dlWLanHEMCS0S6Packets,
       "dlWLanHEMCS1S6Packets": dlWLanHEMCS1S6Packets,
       "dlWLanHEMCS2S6Packets": dlWLanHEMCS2S6Packets,
       "dlWLanHEMCS3S6Packets": dlWLanHEMCS3S6Packets,
       "dlWLanHEMCS4S6Packets": dlWLanHEMCS4S6Packets,
       "dlWLanHEMCS5S6Packets": dlWLanHEMCS5S6Packets,
       "dlWLanHEMCS6S6Packets": dlWLanHEMCS6S6Packets,
       "dlWLanHEMCS7S6Packets": dlWLanHEMCS7S6Packets,
       "dlWLanHEMCS8S6Packets": dlWLanHEMCS8S6Packets,
       "dlWLanHEMCS9S6Packets": dlWLanHEMCS9S6Packets,
       "dlWLanHEMCS10S6Packets": dlWLanHEMCS10S6Packets,
       "dlWLanHEMCS11S6Packets": dlWLanHEMCS11S6Packets,
       "dlWLanHEMCS0S7Packets": dlWLanHEMCS0S7Packets,
       "dlWLanHEMCS1S7Packets": dlWLanHEMCS1S7Packets,
       "dlWLanHEMCS2S7Packets": dlWLanHEMCS2S7Packets,
       "dlWLanHEMCS3S7Packets": dlWLanHEMCS3S7Packets,
       "dlWLanHEMCS4S7Packets": dlWLanHEMCS4S7Packets,
       "dlWLanHEMCS5S7Packets": dlWLanHEMCS5S7Packets,
       "dlWLanHEMCS6S7Packets": dlWLanHEMCS6S7Packets,
       "dlWLanHEMCS7S7Packets": dlWLanHEMCS7S7Packets,
       "dlWLanHEMCS8S7Packets": dlWLanHEMCS8S7Packets,
       "dlWLanHEMCS9S7Packets": dlWLanHEMCS9S7Packets,
       "dlWLanHEMCS10S7Packets": dlWLanHEMCS10S7Packets,
       "dlWLanHEMCS11S7Packets": dlWLanHEMCS11S7Packets,
       "dlWLanHEMCS0S8Packets": dlWLanHEMCS0S8Packets,
       "dlWLanHEMCS1S8Packets": dlWLanHEMCS1S8Packets,
       "dlWLanHEMCS2S8Packets": dlWLanHEMCS2S8Packets,
       "dlWLanHEMCS3S8Packets": dlWLanHEMCS3S8Packets,
       "dlWLanHEMCS4S8Packets": dlWLanHEMCS4S8Packets,
       "dlWLanHEMCS5S8Packets": dlWLanHEMCS5S8Packets,
       "dlWLanHEMCS6S8Packets": dlWLanHEMCS6S8Packets,
       "dlWLanHEMCS7S8Packets": dlWLanHEMCS7S8Packets,
       "dlWLanHEMCS8S8Packets": dlWLanHEMCS8S8Packets,
       "dlWLanHEMCS9S8Packets": dlWLanHEMCS9S8Packets,
       "dlWLanHEMCS10S8Packets": dlWLanHEMCS10S8Packets,
       "dlWLanHEMCS11S8Packets": dlWLanHEMCS11S8Packets,
       "dlWLanHEMCS12S1Packets": dlWLanHEMCS12S1Packets,
       "dlWLanHEMCS13S1Packets": dlWLanHEMCS13S1Packets,
       "dlWLanHEMCS12S2Packets": dlWLanHEMCS12S2Packets,
       "dlWLanHEMCS13S2Packets": dlWLanHEMCS13S2Packets,
       "dlWLanHEMCS12S3Packets": dlWLanHEMCS12S3Packets,
       "dlWLanHEMCS13S3Packets": dlWLanHEMCS13S3Packets,
       "dlWLanHEMCS12S4Packets": dlWLanHEMCS12S4Packets,
       "dlWLanHEMCS13S4Packets": dlWLanHEMCS13S4Packets,
       "dlWLanHEMCS12S5Packets": dlWLanHEMCS12S5Packets,
       "dlWLanHEMCS13S5Packets": dlWLanHEMCS13S5Packets,
       "dlWLanHEMCS12S6Packets": dlWLanHEMCS12S6Packets,
       "dlWLanHEMCS13S6Packets": dlWLanHEMCS13S6Packets,
       "dlWLanHEMCS12S7Packets": dlWLanHEMCS12S7Packets,
       "dlWLanHEMCS13S7Packets": dlWLanHEMCS13S7Packets,
       "dlWLanHEMCS12S8Packets": dlWLanHEMCS12S8Packets,
       "dlWLanHEMCS13S8Packets": dlWLanHEMCS13S8Packets,
       "ulWlanHEMCSPackets": ulWlanHEMCSPackets,
       "ulWLanHEMCS0S1Packets": ulWLanHEMCS0S1Packets,
       "ulWLanHEMCS1S1Packets": ulWLanHEMCS1S1Packets,
       "ulWLanHEMCS2S1Packets": ulWLanHEMCS2S1Packets,
       "ulWLanHEMCS3S1Packets": ulWLanHEMCS3S1Packets,
       "ulWLanHEMCS4S1Packets": ulWLanHEMCS4S1Packets,
       "ulWLanHEMCS5S1Packets": ulWLanHEMCS5S1Packets,
       "ulWLanHEMCS6S1Packets": ulWLanHEMCS6S1Packets,
       "ulWLanHEMCS7S1Packets": ulWLanHEMCS7S1Packets,
       "ulWLanHEMCS8S1Packets": ulWLanHEMCS8S1Packets,
       "ulWLanHEMCS9S1Packets": ulWLanHEMCS9S1Packets,
       "ulWLanHEMCS10S1Packets": ulWLanHEMCS10S1Packets,
       "ulWLanHEMCS11S1Packets": ulWLanHEMCS11S1Packets,
       "ulWLanHEMCS0S2Packets": ulWLanHEMCS0S2Packets,
       "ulWLanHEMCS1S2Packets": ulWLanHEMCS1S2Packets,
       "ulWLanHEMCS2S2Packets": ulWLanHEMCS2S2Packets,
       "ulWLanHEMCS3S2Packets": ulWLanHEMCS3S2Packets,
       "ulWLanHEMCS4S2Packets": ulWLanHEMCS4S2Packets,
       "ulWLanHEMCS5S2Packets": ulWLanHEMCS5S2Packets,
       "ulWLanHEMCS6S2Packets": ulWLanHEMCS6S2Packets,
       "ulWLanHEMCS7S2Packets": ulWLanHEMCS7S2Packets,
       "ulWLanHEMCS8S2Packets": ulWLanHEMCS8S2Packets,
       "ulWLanHEMCS9S2Packets": ulWLanHEMCS9S2Packets,
       "ulWLanHEMCS10S2Packets": ulWLanHEMCS10S2Packets,
       "ulWLanHEMCS11S2Packets": ulWLanHEMCS11S2Packets,
       "ulWLanHEMCS0S3Packets": ulWLanHEMCS0S3Packets,
       "ulWLanHEMCS1S3Packets": ulWLanHEMCS1S3Packets,
       "ulWLanHEMCS2S3Packets": ulWLanHEMCS2S3Packets,
       "ulWLanHEMCS3S3Packets": ulWLanHEMCS3S3Packets,
       "ulWLanHEMCS4S3Packets": ulWLanHEMCS4S3Packets,
       "ulWLanHEMCS5S3Packets": ulWLanHEMCS5S3Packets,
       "ulWLanHEMCS6S3Packets": ulWLanHEMCS6S3Packets,
       "ulWLanHEMCS7S3Packets": ulWLanHEMCS7S3Packets,
       "ulWLanHEMCS8S3Packets": ulWLanHEMCS8S3Packets,
       "ulWLanHEMCS9S3Packets": ulWLanHEMCS9S3Packets,
       "ulWLanHEMCS10S3Packets": ulWLanHEMCS10S3Packets,
       "ulWLanHEMCS11S3Packets": ulWLanHEMCS11S3Packets,
       "ulWLanHEMCS0S4Packets": ulWLanHEMCS0S4Packets,
       "ulWLanHEMCS1S4Packets": ulWLanHEMCS1S4Packets,
       "ulWLanHEMCS2S4Packets": ulWLanHEMCS2S4Packets,
       "ulWLanHEMCS3S4Packets": ulWLanHEMCS3S4Packets,
       "ulWLanHEMCS4S4Packets": ulWLanHEMCS4S4Packets,
       "ulWLanHEMCS5S4Packets": ulWLanHEMCS5S4Packets,
       "ulWLanHEMCS6S4Packets": ulWLanHEMCS6S4Packets,
       "ulWLanHEMCS7S4Packets": ulWLanHEMCS7S4Packets,
       "ulWLanHEMCS8S4Packets": ulWLanHEMCS8S4Packets,
       "ulWLanHEMCS9S4Packets": ulWLanHEMCS9S4Packets,
       "ulWLanHEMCS10S4Packets": ulWLanHEMCS10S4Packets,
       "ulWLanHEMCS11S4Packets": ulWLanHEMCS11S4Packets,
       "ulWLanHEMCS0S5Packets": ulWLanHEMCS0S5Packets,
       "ulWLanHEMCS1S5Packets": ulWLanHEMCS1S5Packets,
       "ulWLanHEMCS2S5Packets": ulWLanHEMCS2S5Packets,
       "ulWLanHEMCS3S5Packets": ulWLanHEMCS3S5Packets,
       "ulWLanHEMCS4S5Packets": ulWLanHEMCS4S5Packets,
       "ulWLanHEMCS5S5Packets": ulWLanHEMCS5S5Packets,
       "ulWLanHEMCS6S5Packets": ulWLanHEMCS6S5Packets,
       "ulWLanHEMCS7S5Packets": ulWLanHEMCS7S5Packets,
       "ulWLanHEMCS8S5Packets": ulWLanHEMCS8S5Packets,
       "ulWLanHEMCS9S5Packets": ulWLanHEMCS9S5Packets,
       "ulWLanHEMCS10S5Packets": ulWLanHEMCS10S5Packets,
       "ulWLanHEMCS11S5Packets": ulWLanHEMCS11S5Packets,
       "ulWLanHEMCS0S6Packets": ulWLanHEMCS0S6Packets,
       "ulWLanHEMCS1S6Packets": ulWLanHEMCS1S6Packets,
       "ulWLanHEMCS2S6Packets": ulWLanHEMCS2S6Packets,
       "ulWLanHEMCS3S6Packets": ulWLanHEMCS3S6Packets,
       "ulWLanHEMCS4S6Packets": ulWLanHEMCS4S6Packets,
       "ulWLanHEMCS5S6Packets": ulWLanHEMCS5S6Packets,
       "ulWLanHEMCS6S6Packets": ulWLanHEMCS6S6Packets,
       "ulWLanHEMCS7S6Packets": ulWLanHEMCS7S6Packets,
       "ulWLanHEMCS8S6Packets": ulWLanHEMCS8S6Packets,
       "ulWLanHEMCS9S6Packets": ulWLanHEMCS9S6Packets,
       "ulWLanHEMCS10S6Packets": ulWLanHEMCS10S6Packets,
       "ulWLanHEMCS11S6Packets": ulWLanHEMCS11S6Packets,
       "ulWLanHEMCS0S7Packets": ulWLanHEMCS0S7Packets,
       "ulWLanHEMCS1S7Packets": ulWLanHEMCS1S7Packets,
       "ulWLanHEMCS2S7Packets": ulWLanHEMCS2S7Packets,
       "ulWLanHEMCS3S7Packets": ulWLanHEMCS3S7Packets,
       "ulWLanHEMCS4S7Packets": ulWLanHEMCS4S7Packets,
       "ulWLanHEMCS5S7Packets": ulWLanHEMCS5S7Packets,
       "ulWLanHEMCS6S7Packets": ulWLanHEMCS6S7Packets,
       "ulWLanHEMCS7S7Packets": ulWLanHEMCS7S7Packets,
       "ulWLanHEMCS8S7Packets": ulWLanHEMCS8S7Packets,
       "ulWLanHEMCS9S7Packets": ulWLanHEMCS9S7Packets,
       "ulWLanHEMCS10S7Packets": ulWLanHEMCS10S7Packets,
       "ulWLanHEMCS11S7Packets": ulWLanHEMCS11S7Packets,
       "ulWLanHEMCS0S8Packets": ulWLanHEMCS0S8Packets,
       "ulWLanHEMCS1S8Packets": ulWLanHEMCS1S8Packets,
       "ulWLanHEMCS2S8Packets": ulWLanHEMCS2S8Packets,
       "ulWLanHEMCS3S8Packets": ulWLanHEMCS3S8Packets,
       "ulWLanHEMCS4S8Packets": ulWLanHEMCS4S8Packets,
       "ulWLanHEMCS5S8Packets": ulWLanHEMCS5S8Packets,
       "ulWLanHEMCS6S8Packets": ulWLanHEMCS6S8Packets,
       "ulWLanHEMCS7S8Packets": ulWLanHEMCS7S8Packets,
       "ulWLanHEMCS8S8Packets": ulWLanHEMCS8S8Packets,
       "ulWLanHEMCS9S8Packets": ulWLanHEMCS9S8Packets,
       "ulWLanHEMCS10S8Packets": ulWLanHEMCS10S8Packets,
       "ulWLanHEMCS11S8Packets": ulWLanHEMCS11S8Packets,
       "ulWLanHEMCS12S1Packets": ulWLanHEMCS12S1Packets,
       "ulWLanHEMCS13S1Packets": ulWLanHEMCS13S1Packets,
       "ulWLanHEMCS12S2Packets": ulWLanHEMCS12S2Packets,
       "ulWLanHEMCS13S2Packets": ulWLanHEMCS13S2Packets,
       "ulWLanHEMCS12S3Packets": ulWLanHEMCS12S3Packets,
       "ulWLanHEMCS13S3Packets": ulWLanHEMCS13S3Packets,
       "ulWLanHEMCS12S4Packets": ulWLanHEMCS12S4Packets,
       "ulWLanHEMCS13S4Packets": ulWLanHEMCS13S4Packets,
       "ulWLanHEMCS12S5Packets": ulWLanHEMCS12S5Packets,
       "ulWLanHEMCS13S5Packets": ulWLanHEMCS13S5Packets,
       "ulWLanHEMCS12S6Packets": ulWLanHEMCS12S6Packets,
       "ulWLanHEMCS13S6Packets": ulWLanHEMCS13S6Packets,
       "ulWLanHEMCS12S7Packets": ulWLanHEMCS12S7Packets,
       "ulWLanHEMCS13S7Packets": ulWLanHEMCS13S7Packets,
       "ulWLanHEMCS12S8Packets": ulWLanHEMCS12S8Packets,
       "ulWLanHEMCS13S8Packets": ulWLanHEMCS13S8Packets,
       "lanSwitchPortPerfTable": lanSwitchPortPerfTable,
       "lanSwitchPortPerfEntry": lanSwitchPortPerfEntry,
       "rxSwitchPortKBCount": rxSwitchPortKBCount,
       "rxSwitchPortTotalPacketCount": rxSwitchPortTotalPacketCount,
       "rxSwitchPortErrorPacketCount": rxSwitchPortErrorPacketCount,
       "rxSwitchPortUnicastPacketCount": rxSwitchPortUnicastPacketCount,
       "rxSwitchPortMulticastPacketCount": rxSwitchPortMulticastPacketCount,
       "rxSwitchPortBroadcastPacketCount": rxSwitchPortBroadcastPacketCount,
       "txSwitchPortKBCount": txSwitchPortKBCount,
       "txSwitchPortTotalPacketCount": txSwitchPortTotalPacketCount,
       "txSwitchPortErrorPacketCount": txSwitchPortErrorPacketCount,
       "txSwitchPortUnicastPacketCount": txSwitchPortUnicastPacketCount,
       "txSwitchPortMulticastPacketCount": txSwitchPortMulticastPacketCount,
       "txSwitchPortBroadcastPacketCount": txSwitchPortBroadcastPacketCount,
       "dlWLanRetransMpduPacketCount": dlWLanRetransMpduPacketCount,
       "ulWLanRetransMpduPacketCount": ulWLanRetransMpduPacketCount,
       "ulWLan2KbitCount": ulWLan2KbitCount,
       "dlWLan2KbitCount": dlWLan2KbitCount,
       "ulWLan2TotalPacketCount": ulWLan2TotalPacketCount,
       "dlWLan2TotalPacketCount": dlWLan2TotalPacketCount,
       "ulWLan2MultiBroadcastKbitCount": ulWLan2MultiBroadcastKbitCount,
       "dlWLan2MultiBroadcastKbitCount": dlWLan2MultiBroadcastKbitCount,
       "wLan2SessionDroppedCount": wLan2SessionDroppedCount,
       "ulWLan2ErrorDroppedPacketCount": ulWLan2ErrorDroppedPacketCount,
       "dlWLan2ErrorDroppedPacketCount": dlWLan2ErrorDroppedPacketCount,
       "ulWLan2CapacityDroppedPacketCount": ulWLan2CapacityDroppedPacketCount,
       "dlWLan2CapacityDroppedPacketCount": dlWLan2CapacityDroppedPacketCount,
       "ulWLan2TotalAvailableFrameTimePerSecond": ulWLan2TotalAvailableFrameTimePerSecond,
       "dlWLan2TotalAvailableFrameTimePerSecond": dlWLan2TotalAvailableFrameTimePerSecond,
       "ulWLan2TotalUsedFrameTimePerSecond": ulWLan2TotalUsedFrameTimePerSecond,
       "dlWLan2TotalUsedFrameTimePerSecond": dlWLan2TotalUsedFrameTimePerSecond,
       "ulWLan2TotalOverheadFrameTimePerSecond": ulWLan2TotalOverheadFrameTimePerSecond,
       "dlWLan2TotalOverheadFrameTimePerSecond": dlWLan2TotalOverheadFrameTimePerSecond,
       "ulWLan2RetransPacketCount": ulWLan2RetransPacketCount,
       "dlWLan2RetransPacketCount": dlWLan2RetransPacketCount,
       "ulWLan2BroadcastPacketCount": ulWLan2BroadcastPacketCount,
       "dlWLan2BroadcastPacketCount": dlWLan2BroadcastPacketCount,
       "ulWLan2MulticastPacketCount": ulWLan2MulticastPacketCount,
       "dlWLan2MulticastPacketCount": dlWLan2MulticastPacketCount,
       "rxEtherLan2KbitCount": rxEtherLan2KbitCount,
       "rxEtherLan2TotalPacketCount": rxEtherLan2TotalPacketCount,
       "rxEtherLan2ErrorPacketCount": rxEtherLan2ErrorPacketCount,
       "rxEtherLan2DroppedPacketCount": rxEtherLan2DroppedPacketCount,
       "rxEtherLan2MulticastPacketCount": rxEtherLan2MulticastPacketCount,
       "rxEtherLan2BroadcastPacketCount": rxEtherLan2BroadcastPacketCount,
       "rxEtherLan2MultiBroadcastKbitCount": rxEtherLan2MultiBroadcastKbitCount,
       "txEtherLan2KbitCount": txEtherLan2KbitCount,
       "txEtherLan2TotalPacketCount": txEtherLan2TotalPacketCount,
       "txEtherLan2ErrorPacketCount": txEtherLan2ErrorPacketCount,
       "txEtherLan2DroppedPacketCount": txEtherLan2DroppedPacketCount,
       "txEtherLan2MulticastPacketCount": txEtherLan2MulticastPacketCount,
       "txEtherLan2BroadcastPacketCount": txEtherLan2BroadcastPacketCount,
       "txEtherLan2MultiBroadcastKbitCount": txEtherLan2MultiBroadcastKbitCount,
       "ulWLan2TotalAvailableFrameTimePercentage": ulWLan2TotalAvailableFrameTimePercentage,
       "dlWLan2TotalAvailableFrameTimePercentage": dlWLan2TotalAvailableFrameTimePercentage,
       "ulWLan2VHTMCS0SSPackets": ulWLan2VHTMCS0SSPackets,
       "ulWLan2VHTMCS1SSPackets": ulWLan2VHTMCS1SSPackets,
       "ulWLan2VHTMCS2SSPackets": ulWLan2VHTMCS2SSPackets,
       "ulWLan2VHTMCS3SSPackets": ulWLan2VHTMCS3SSPackets,
       "ulWLan2VHTMCS4SSPackets": ulWLan2VHTMCS4SSPackets,
       "ulWLan2VHTMCS5SSPackets": ulWLan2VHTMCS5SSPackets,
       "ulWLan2VHTMCS6SSPackets": ulWLan2VHTMCS6SSPackets,
       "ulWLan2VHTMCS7SSPackets": ulWLan2VHTMCS7SSPackets,
       "ulWLan2VHTMCS8SSPackets": ulWLan2VHTMCS8SSPackets,
       "ulWLan2VHTMCS9SSPackets": ulWLan2VHTMCS9SSPackets,
       "ulWLan2VHTMCS0DSPackets": ulWLan2VHTMCS0DSPackets,
       "ulWLan2VHTMCS1DSPackets": ulWLan2VHTMCS1DSPackets,
       "ulWLan2VHTMCS2DSPackets": ulWLan2VHTMCS2DSPackets,
       "ulWLan2VHTMCS3DSPackets": ulWLan2VHTMCS3DSPackets,
       "ulWLan2VHTMCS4DSPackets": ulWLan2VHTMCS4DSPackets,
       "ulWLan2VHTMCS5DSPackets": ulWLan2VHTMCS5DSPackets,
       "ulWLan2VHTMCS6DSPackets": ulWLan2VHTMCS6DSPackets,
       "ulWLan2VHTMCS7DSPackets": ulWLan2VHTMCS7DSPackets,
       "ulWLan2VHTMCS8DSPackets": ulWLan2VHTMCS8DSPackets,
       "ulWLan2VHTMCS9DSPackets": ulWLan2VHTMCS9DSPackets,
       "dlWLan2VHTMCS0SSPackets": dlWLan2VHTMCS0SSPackets,
       "dlWLan2VHTMCS1SSPackets": dlWLan2VHTMCS1SSPackets,
       "dlWLan2VHTMCS2SSPackets": dlWLan2VHTMCS2SSPackets,
       "dlWLan2VHTMCS3SSPackets": dlWLan2VHTMCS3SSPackets,
       "dlWLan2VHTMCS4SSPackets": dlWLan2VHTMCS4SSPackets,
       "dlWLan2VHTMCS5SSPackets": dlWLan2VHTMCS5SSPackets,
       "dlWLan2VHTMCS6SSPackets": dlWLan2VHTMCS6SSPackets,
       "dlWLan2VHTMCS7SSPackets": dlWLan2VHTMCS7SSPackets,
       "dlWLan2VHTMCS8SSPackets": dlWLan2VHTMCS8SSPackets,
       "dlWLan2VHTMCS9SSPackets": dlWLan2VHTMCS9SSPackets,
       "dlWLan2VHTMCS0DSPackets": dlWLan2VHTMCS0DSPackets,
       "dlWLan2VHTMCS1DSPackets": dlWLan2VHTMCS1DSPackets,
       "dlWLan2VHTMCS2DSPackets": dlWLan2VHTMCS2DSPackets,
       "dlWLan2VHTMCS3DSPackets": dlWLan2VHTMCS3DSPackets,
       "dlWLan2VHTMCS4DSPackets": dlWLan2VHTMCS4DSPackets,
       "dlWLan2VHTMCS5DSPackets": dlWLan2VHTMCS5DSPackets,
       "dlWLan2VHTMCS6DSPackets": dlWLan2VHTMCS6DSPackets,
       "dlWLan2VHTMCS7DSPackets": dlWLan2VHTMCS7DSPackets,
       "dlWLan2VHTMCS8DSPackets": dlWLan2VHTMCS8DSPackets,
       "dlWLan2VHTMCS9DSPackets": dlWLan2VHTMCS9DSPackets,
       "wLan2SNRDeviation00Cnt": wLan2SNRDeviation00Cnt,
       "wLan2SNRDeviation01Cnt": wLan2SNRDeviation01Cnt,
       "wLan2SNRDeviation02Cnt": wLan2SNRDeviation02Cnt,
       "wLan2SNRDeviation03Cnt": wLan2SNRDeviation03Cnt,
       "wLan2SNRDeviation04Cnt": wLan2SNRDeviation04Cnt,
       "wLan2SNRDeviation05Cnt": wLan2SNRDeviation05Cnt,
       "wLan2SNRDeviation06Cnt": wLan2SNRDeviation06Cnt,
       "wLan2SNRDeviation07Cnt": wLan2SNRDeviation07Cnt,
       "wLan2SNRDeviation08Cnt": wLan2SNRDeviation08Cnt,
       "wLan2SNRDeviation09Cnt": wLan2SNRDeviation09Cnt,
       "wLan2SNRDeviation10Cnt": wLan2SNRDeviation10Cnt,
       "wLan2SNRDeviation11Cnt": wLan2SNRDeviation11Cnt,
       "wLan2SNRDeviation12Cnt": wLan2SNRDeviation12Cnt,
       "wLan2SNRDeviation13Cnt": wLan2SNRDeviation13Cnt,
       "wLan2SNRDeviation14Cnt": wLan2SNRDeviation14Cnt,
       "wLan2SNRDeviation15Cnt": wLan2SNRDeviation15Cnt,
       "wLan2SNRDeviation16Cnt": wLan2SNRDeviation16Cnt,
       "wLan2SNRDeviation17Cnt": wLan2SNRDeviation17Cnt,
       "wLan2SNRDeviation18Cnt": wLan2SNRDeviation18Cnt,
       "wLan2SNRDeviation19Cnt": wLan2SNRDeviation19Cnt,
       "cambiumRealTimeStatsMonitoring": cambiumRealTimeStatsMonitoring,
       "cambiumAdvancedPerformanceMonitoring": cambiumAdvancedPerformanceMonitoring,
       "cambiumpmp80211SystemConfiguration": cambiumpmp80211SystemConfiguration,
       "cambiumSystemLog": cambiumSystemLog,
       "syslogServerIPFirst": syslogServerIPFirst,
       "syslogServerIPSecond": syslogServerIPSecond,
       "syslogServerIPThird": syslogServerIPThird,
       "syslogServerIPFourth": syslogServerIPFourth,
       "syslogServerLogToWeb": syslogServerLogToWeb,
       "syslogServerLogMask": syslogServerLogMask,
       "syslogServerLogDA": syslogServerLogDA,
       "syslogServerLogCLISH": syslogServerLogCLISH,
       "syslogServerPortFirst": syslogServerPortFirst,
       "syslogServerPortSecond": syslogServerPortSecond,
       "syslogServerPortThird": syslogServerPortThird,
       "syslogServerPortFourth": syslogServerPortFourth,
       "cambiumDHCP": cambiumDHCP,
       "dhcpLanEnable": dhcpLanEnable,
       "dhcpLanStart": dhcpLanStart,
       "dhcpLanLimit": dhcpLanLimit,
       "dhcpLanLeasetime": dhcpLanLeasetime,
       "dhcpLanHostTable": dhcpLanHostTable,
       "dhcpLanHostEntry": dhcpLanHostEntry,
       "dhcpLanHostIndex": dhcpLanHostIndex,
       "dhcpLanHostIP": dhcpLanHostIP,
       "dhcpLanHostMAC": dhcpLanHostMAC,
       "dhcpLanHostName": dhcpLanHostName,
       "dhcpOption82": dhcpOption82,
       "dhcpOption66": dhcpOption66,
       "dhcpOption82CircuitIDType": dhcpOption82CircuitIDType,
       "dhcpOption82CircuitValue": dhcpOption82CircuitValue,
       "dhcpOption82RemoteIDType": dhcpOption82RemoteIDType,
       "dhcpOption82RemoteValue": dhcpOption82RemoteValue,
       "cambiumSSHServer": cambiumSSHServer,
       "cambiumSSHServerEnable": cambiumSSHServerEnable,
       "cambiumSSHServerPort": cambiumSSHServerPort,
       "cambiumSSHServerDeprecatedAlgorithms": cambiumSSHServerDeprecatedAlgorithms,
       "network": network,
       "networkMode": networkMode,
       "networkLan": networkLan,
       "networkLanIPAddressMode": networkLanIPAddressMode,
       "networkLanIPAddr": networkLanIPAddr,
       "networkLanNetmask": networkLanNetmask,
       "networkLanGatewayIP": networkLanGatewayIP,
       "networkLanDNSIPAddr": networkLanDNSIPAddr,
       "networkLanMTU": networkLanMTU,
       "networkLanDNSIPAddrPrimary": networkLanDNSIPAddrPrimary,
       "networkLanDNSIPAddrSecondary": networkLanDNSIPAddrSecondary,
       "networkLanAutoNegotiation": networkLanAutoNegotiation,
       "networkLanSpeed": networkLanSpeed,
       "networkLanDuplex": networkLanDuplex,
       "networkBroadcastStormEnabled": networkBroadcastStormEnabled,
       "networkBroadcastStormRate": networkBroadcastStormRate,
       "networkLanSmartSpeedMode": networkLanSmartSpeedMode,
       "networkLan2Enabled": networkLan2Enabled,
       "networkLan2AutoNegotiation": networkLan2AutoNegotiation,
       "networkLan2Speed": networkLan2Speed,
       "networkLan2Duplex": networkLan2Duplex,
       "networkLan2PoEEnabled": networkLan2PoEEnabled,
       "networkLanEnabled": networkLanEnabled,
       "networkLan2MTU": networkLan2MTU,
       "networkLanAdvertise": networkLanAdvertise,
       "networkLanIPv6Addr": networkLanIPv6Addr,
       "networkLanGatewayIPv6": networkLanGatewayIPv6,
       "networkLanIPv6AddressType": networkLanIPv6AddressType,
       "networkLanIPv6PrefixLength": networkLanIPv6PrefixLength,
       "networkLanIPv6DHCPServer": networkLanIPv6DHCPServer,
       "lanSwitch": lanSwitch,
       "lanSwitchPortTable": lanSwitchPortTable,
       "lanSwitchPortEntry": lanSwitchPortEntry,
       "lanSwitchPortNum": lanSwitchPortNum,
       "lanSwitchPortEnable": lanSwitchPortEnable,
       "lanSwitchPortAutoneg": lanSwitchPortAutoneg,
       "lanSwitchPortSpeed": lanSwitchPortSpeed,
       "lanSwitchPortDuplex": lanSwitchPortDuplex,
       "lanSwitchPortPoEMode": lanSwitchPortPoEMode,
       "networkWan": networkWan,
       "networkWanIPAddressMode": networkWanIPAddressMode,
       "networkWanIPAddr": networkWanIPAddr,
       "networkWanNetmask": networkWanNetmask,
       "networkWanGatewayIP": networkWanGatewayIP,
       "networkWanDNSIPAddr": networkWanDNSIPAddr,
       "networkWanMTU": networkWanMTU,
       "networkWanDNSIPAddrPrimary": networkWanDNSIPAddrPrimary,
       "networkWanDNSIPAddrSecondary": networkWanDNSIPAddrSecondary,
       "networkWanPPPoE": networkWanPPPoE,
       "networkWanPPPoEUsername": networkWanPPPoEUsername,
       "networkWanPPPoEPassword": networkWanPPPoEPassword,
       "networkWanPPPoEAC": networkWanPPPoEAC,
       "networkWanPPPoEService": networkWanPPPoEService,
       "networkWanPPPoEAuth": networkWanPPPoEAuth,
       "networkWanPPPoEMTU": networkWanPPPoEMTU,
       "networkWanPPPoEKeepAlive": networkWanPPPoEKeepAlive,
       "networkWanPPPoEMSSClamping": networkWanPPPoEMSSClamping,
       "networkWanPPPoEAttempts": networkWanPPPoEAttempts,
       "networkWanIPv6AddressMode": networkWanIPv6AddressMode,
       "networkWanIPv6Addr": networkWanIPv6Addr,
       "networkWanGatewayIPv6": networkWanGatewayIPv6,
       "networkWanIPv6LocalInterfaceId": networkWanIPv6LocalInterfaceId,
       "mgmtVLAN": mgmtVLAN,
       "mgmtVLANEnable": mgmtVLANEnable,
       "mgmtVLANVID": mgmtVLANVID,
       "mgmtVLANVP": mgmtVLANVP,
       "dataVLAN": dataVLAN,
       "dataVLANEnable": dataVLANEnable,
       "dataVLANVID": dataVLANVID,
       "dataVLANVP": dataVLANVP,
       "networkSTP": networkSTP,
       "networkBridge": networkBridge,
       "networkBridgeIPAddressMode": networkBridgeIPAddressMode,
       "networkBridgeIPAddr": networkBridgeIPAddr,
       "networkBridgeNetmask": networkBridgeNetmask,
       "networkBridgeGatewayIP": networkBridgeGatewayIP,
       "networkBridgeDNSIPAddr": networkBridgeDNSIPAddr,
       "networkBridgeMTU": networkBridgeMTU,
       "networkBridgeDNSIPAddrPrimary": networkBridgeDNSIPAddrPrimary,
       "networkBridgeDNSIPAddrSecondary": networkBridgeDNSIPAddrSecondary,
       "networkBridgeIPv6AddressMode": networkBridgeIPv6AddressMode,
       "networkBridgeIPv6Addr": networkBridgeIPv6Addr,
       "networkBridgeGatewayIPv6": networkBridgeGatewayIPv6,
       "networkPortSecurity": networkPortSecurity,
       "networkPortSecurityMax": networkPortSecurityMax,
       "networkPortSecurityAgingTime": networkPortSecurityAgingTime,
       "mcastVLAN": mcastVLAN,
       "mcastVLANEnable": mcastVLANEnable,
       "mcastVLANVID": mcastVLANVID,
       "mcastVLANVP": mcastVLANVP,
       "mcastGroupLimit": mcastGroupLimit,
       "mgmtIF": mgmtIF,
       "mgmtIFEnable": mgmtIFEnable,
       "mgmtIFVLAN": mgmtIFVLAN,
       "mgmtIFVID": mgmtIFVID,
       "mgmtIFVP": mgmtIFVP,
       "mgmtIFIPAddressMode": mgmtIFIPAddressMode,
       "mgmtIFIPAddr": mgmtIFIPAddr,
       "mgmtIFNetmask": mgmtIFNetmask,
       "mgmtIFGateway": mgmtIFGateway,
       "mgmtIFIPv6AddressMode": mgmtIFIPv6AddressMode,
       "mgmtIFIPv6Addr": mgmtIFIPv6Addr,
       "mgmtIFIPv6Gateway": mgmtIFIPv6Gateway,
       "networkLanDefaultIP": networkLanDefaultIP,
       "networkRelaydEnable": networkRelaydEnable,
       "networkAliases": networkAliases,
       "cambiumIPAliasCnfTable": cambiumIPAliasCnfTable,
       "cambiumIPAliasCnfEntry": cambiumIPAliasCnfEntry,
       "cambiumIPAliasesIndex": cambiumIPAliasesIndex,
       "cambiumIPAliasesIpAddr": cambiumIPAliasesIpAddr,
       "cambiumIPAliasesNetmask": cambiumIPAliasesNetmask,
       "cambiumIPAliasesInfo": cambiumIPAliasesInfo,
       "cambiumIPAliasesIface": cambiumIPAliasesIface,
       "cambiumIPAliasesEnable": cambiumIPAliasesEnable,
       "networkPPPoE": networkPPPoE,
       "networkPPPoEIAEnable": networkPPPoEIAEnable,
       "networkPPPoEIATable": networkPPPoEIATable,
       "networkPPPoEIAEntry": networkPPPoEIAEntry,
       "networkPPPoEIAIndex": networkPPPoEIAIndex,
       "networkPPPoEIAUID": networkPPPoEIAUID,
       "networkPPPoEIASMMAC": networkPPPoEIASMMAC,
       "networkPPPoEIAPhoneNumber": networkPPPoEIAPhoneNumber,
       "networkPPPoEIATerminal": networkPPPoEIATerminal,
       "networkPPPoEIAFrame": networkPPPoEIAFrame,
       "networkPPPoEIASlot": networkPPPoEIASlot,
       "networkPPPoEIAPort": networkPPPoEIAPort,
       "networkPPPoEIAVlanId": networkPPPoEIAVlanId,
       "snmp": snmp,
       "snmpReadOnlyCommunity": snmpReadOnlyCommunity,
       "snmpReadWriteCommunity": snmpReadWriteCommunity,
       "snmpSystemName": snmpSystemName,
       "snmpSystemDescription": snmpSystemDescription,
       "snmpTrapEnable": snmpTrapEnable,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapEntryIndex": snmpTrapEntryIndex,
       "snmpTrapEntryIP": snmpTrapEntryIP,
       "snmpTrapEntryPort": snmpTrapEntryPort,
       "snmpDomainAccessEnable": snmpDomainAccessEnable,
       "snmpDomainAccessIP": snmpDomainAccessIP,
       "snmpDomainAccessIPMask": snmpDomainAccessIPMask,
       "snmpProtocolVersion": snmpProtocolVersion,
       "snmpAgentPort": snmpAgentPort,
       "snmpRemoteAccess": snmpRemoteAccess,
       "snmpLinkTrapEnable": snmpLinkTrapEnable,
       "snmpv3UsersTable": snmpv3UsersTable,
       "snmpv3UsersEntry": snmpv3UsersEntry,
       "snmpv3UsersTableIndex": snmpv3UsersTableIndex,
       "snmpv3UserName": snmpv3UserName,
       "snmpv3UserPassPhrase": snmpv3UserPassPhrase,
       "snmpv3UserSecurityLevel": snmpv3UserSecurityLevel,
       "snmpv3UserRWAccess": snmpv3UserRWAccess,
       "snmpv3UserAuthMethod": snmpv3UserAuthMethod,
       "snmpv3UserEncryption": snmpv3UserEncryption,
       "cambiumSystem": cambiumSystem,
       "systemConfig": systemConfig,
       "systemConfigTimezone": systemConfigTimezone,
       "systemConfigDeviceName": systemConfigDeviceName,
       "systemConfigETSILicense": systemConfigETSILicense,
       "systemConfigSWLockBit": systemConfigSWLockBit,
       "systemConfigHWLockBit": systemConfigHWLockBit,
       "systemDeviceLocLatitude": systemDeviceLocLatitude,
       "systemDeviceLocLongitude": systemDeviceLocLongitude,
       "systemDeviceLocHeight": systemDeviceLocHeight,
       "systemConfigisGPSkeyOK": systemConfigisGPSkeyOK,
       "systemConfigGPSLockBit": systemConfigGPSLockBit,
       "systemConfigSMLockBit": systemConfigSMLockBit,
       "systemConfigSMLimit": systemConfigSMLimit,
       "cambiumePMPElevateHWLicenseLimit": cambiumePMPElevateHWLicenseLimit,
       "powerSequenceFactoryDefault": powerSequenceFactoryDefault,
       "systemConfigLockedCC": systemConfigLockedCC,
       "systemConfigMinAntGain": systemConfigMinAntGain,
       "systemConfigOperationalLicense": systemConfigOperationalLicense,
       "systemConfigIPv6Support": systemConfigIPv6Support,
       "systemConfigFactoryResetKeepPwd": systemConfigFactoryResetKeepPwd,
       "cambiumDeviceNameLoginDisplay": cambiumDeviceNameLoginDisplay,
       "systemConfigStartDHT": systemConfigStartDHT,
       "systemConfigStopDHT": systemConfigStopDHT,
       "systemConfigPreheatStopTemp": systemConfigPreheatStopTemp,
       "systemConfigPreheatStopTimeout": systemConfigPreheatStopTimeout,
       "systemConfigBIB": systemConfigBIB,
       "systemConfigLanguage": systemConfigLanguage,
       "systemConfigCNVision": systemConfigCNVision,
       "systemConfigSCLockBit": systemConfigSCLockBit,
       "systemNtpServer": systemNtpServer,
       "systemNtpServerIPMode": systemNtpServerIPMode,
       "systemNtpServerPrimaryIP": systemNtpServerPrimaryIP,
       "systemNtpServerSecondaryIP": systemNtpServerSecondaryIP,
       "cambiumWebServer": cambiumWebServer,
       "webService": webService,
       "httpPort": httpPort,
       "httpsPort": httpsPort,
       "uhttpdMainPem": uhttpdMainPem,
       "uhttpdMainInactLogout": uhttpdMainInactLogout,
       "wireless": wireless,
       "wirelessDevice": wirelessDevice,
       "wirelessDeviceCountryCode": wirelessDeviceCountryCode,
       "wirelessType": wirelessType,
       "wirelessDefaultCountryCode": wirelessDefaultCountryCode,
       "wirelessSmartAntennaEnabled": wirelessSmartAntennaEnabled,
       "wirelessAPForcedSector": wirelessAPForcedSector,
       "wirelessSTAForcedSector": wirelessSTAForcedSector,
       "wirelessMUMIMOEnable": wirelessMUMIMOEnable,
       "wirelessMUMIMOSoundingInterval": wirelessMUMIMOSoundingInterval,
       "wirelessMUMIMOSoundingAzimuthCycle": wirelessMUMIMOSoundingAzimuthCycle,
       "wirelessMUMIMOCBFRateAdapt": wirelessMUMIMOCBFRateAdapt,
       "wirelessMUMIMOCBFRateAdaptIndex": wirelessMUMIMOCBFRateAdaptIndex,
       "wirelessRandFD": wirelessRandFD,
       "wirelessEPTPPPDUDuration": wirelessEPTPPPDUDuration,
       "wirelessRadioTransmissionOptimization": wirelessRadioTransmissionOptimization,
       "wirelessInterface": wirelessInterface,
       "wirelessInterfaceMode": wirelessInterfaceMode,
       "wirelessInterfaceSSID": wirelessInterfaceSSID,
       "wirelessInterfaceEncryption": wirelessInterfaceEncryption,
       "wirelessInterfaceEncryptionKey": wirelessInterfaceEncryptionKey,
       "wirelessInterfaceHTMode": wirelessInterfaceHTMode,
       "wirelessInterfaceTXPower": wirelessInterfaceTXPower,
       "wirelessInterfaceTDDAntennaGain": wirelessInterfaceTDDAntennaGain,
       "wirelessInterfaceTDDRatio": wirelessInterfaceTDDRatio,
       "wirelessInterfaceTPCTRL": wirelessInterfaceTPCTRL,
       "wirelessInterfaceTPCMode": wirelessInterfaceTPCMode,
       "wirelessInterfacePTPMode": wirelessInterfacePTPMode,
       "wirelessInterfacePTPMACAddress": wirelessInterfacePTPMACAddress,
       "wirelessInterfaceSyncSource": wirelessInterfaceSyncSource,
       "wirelessInterfaceSyncHoldTime": wirelessInterfaceSyncHoldTime,
       "wirelessInterfaceScanFrequencyListTwenty": wirelessInterfaceScanFrequencyListTwenty,
       "wirelessInterfaceScanFrequencyListForty": wirelessInterfaceScanFrequencyListForty,
       "centerFrequency": centerFrequency,
       "dfsAlternative1CenterFrequency": dfsAlternative1CenterFrequency,
       "dfsAlternative2CenterFrequency": dfsAlternative2CenterFrequency,
       "wirelessMaximumCellSize": wirelessMaximumCellSize,
       "wirelessCellSizeUnit": wirelessCellSizeUnit,
       "wirelessMaximumSTA": wirelessMaximumSTA,
       "dfsAlternative1Bandwidth": dfsAlternative1Bandwidth,
       "dfsAlternative2Bandwidth": dfsAlternative2Bandwidth,
       "wirelessAcceptableAPRSSIThreshold": wirelessAcceptableAPRSSIThreshold,
       "wirelessAcceptableAPCINRThreshold": wirelessAcceptableAPCINRThreshold,
       "wirelessInterfaceUnblockUSfreqs": wirelessInterfaceUnblockUSfreqs,
       "wirelessMIREnable": wirelessMIREnable,
       "wirelessMIRSTAProfileNumber": wirelessMIRSTAProfileNumber,
       "wirelessMIRAPDefaultProfileNumber": wirelessMIRAPDefaultProfileNumber,
       "wirelessInterfaceScanFrequencyBandwidth": wirelessInterfaceScanFrequencyBandwidth,
       "wirelessInterfaceGuardInterval": wirelessInterfaceGuardInterval,
       "wirelessInterfaceiFreqReuseMode": wirelessInterfaceiFreqReuseMode,
       "wirelessSTAPriority": wirelessSTAPriority,
       "wirelessSmoothingBit": wirelessSmoothingBit,
       "wirelessSecurityMethod": wirelessSecurityMethod,
       "wirelessAcceptableAPSNRThreshold": wirelessAcceptableAPSNRThreshold,
       "wirelessMgmtPacketRate": wirelessMgmtPacketRate,
       "wirelessStaIsolate": wirelessStaIsolate,
       "wirelessCcaEnable": wirelessCcaEnable,
       "wirelessInterfaceScanFrequencyListTen": wirelessInterfaceScanFrequencyListTen,
       "wirelessInterfaceScanFrequencyListFive": wirelessInterfaceScanFrequencyListFive,
       "wirelessMulticastEnhanceMode": wirelessMulticastEnhanceMode,
       "wirelessTXPowerManualLimit": wirelessTXPowerManualLimit,
       "wirelessRateMaxMCS": wirelessRateMaxMCS,
       "wirelessSMWifiDistance": wirelessSMWifiDistance,
       "wirelessInterfaceProtocolMode": wirelessInterfaceProtocolMode,
       "wirelessClientBridgeMode": wirelessClientBridgeMode,
       "forceMcastBcast4Addr": forceMcastBcast4Addr,
       "wirelessInterfaceCipher": wirelessInterfaceCipher,
       "wirelessInterfaceRateMinMCS": wirelessInterfaceRateMinMCS,
       "wirelessInterfaceRateMaxMCS": wirelessInterfaceRateMaxMCS,
       "wirelessMulticastIgmpFastLeave": wirelessMulticastIgmpFastLeave,
       "wirelessInterfaceTDDFrameSize": wirelessInterfaceTDDFrameSize,
       "wirelessInterfaceColocState": wirelessInterfaceColocState,
       "wirelessInterfaceColocSystemSyncSrc": wirelessInterfaceColocSystemSyncSrc,
       "wirelessAPWifiWLANmode": wirelessAPWifiWLANmode,
       "apWiFiDLCTSMode": apWiFiDLCTSMode,
       "apWiFiULCTSRTSMode": apWiFiULCTSRTSMode,
       "apWiFiRTSThreshold": apWiFiRTSThreshold,
       "apWiFiCompWDSTrBridge": apWiFiCompWDSTrBridge,
       "wirelessFreqShift": wirelessFreqShift,
       "wirelessFBCompatibility": wirelessFBCompatibility,
       "wirelessMACFilter": wirelessMACFilter,
       "wirelessMACFilterPolicy": wirelessMACFilterPolicy,
       "wirelessMACFilterTable": wirelessMACFilterTable,
       "wirelessMACFilterEntry": wirelessMACFilterEntry,
       "wirelessMACFilterIndex": wirelessMACFilterIndex,
       "wirelessFilterMAC": wirelessFilterMAC,
       "wirelessFilterInfo": wirelessFilterInfo,
       "wirelessInterfaceMgmtRadioBoarddata": wirelessInterfaceMgmtRadioBoarddata,
       "wirelessPMPWDSUnknownMACFlood": wirelessPMPWDSUnknownMACFlood,
       "wirelessInterfaceScanFrequencyListEighty": wirelessInterfaceScanFrequencyListEighty,
       "wirelessInterfaceVHTMCS": wirelessInterfaceVHTMCS,
       "wirelessInterfaceNSS": wirelessInterfaceNSS,
       "mikrotikFreqShift": mikrotikFreqShift,
       "cambiumKeepAliveIface1": cambiumKeepAliveIface1,
       "wirelessInterface1KeepAliveEnable": wirelessInterface1KeepAliveEnable,
       "wirelessInterface1KeepAliveEPTPEnable": wirelessInterface1KeepAliveEPTPEnable,
       "wirelessInterface1KeepAlivePMPEnable": wirelessInterface1KeepAlivePMPEnable,
       "wirelessInterface1KeepAliveWLREnable": wirelessInterface1KeepAliveWLREnable,
       "wirelessInterfaceSTAMaxDLMCSLimit": wirelessInterfaceSTAMaxDLMCSLimit,
       "wirelessInterfaceScanFrequencyList160M": wirelessInterfaceScanFrequencyList160M,
       "wirelessInterfaceSuRxBfOff": wirelessInterfaceSuRxBfOff,
       "wirelessPrefList": wirelessPrefList,
       "prefferedAPTable": prefferedAPTable,
       "prefferedAPEntry": prefferedAPEntry,
       "prefferedListTableEntryIndex": prefferedListTableEntryIndex,
       "prefferedListTableEntrySSID": prefferedListTableEntrySSID,
       "prefferedListTableEntryKEY": prefferedListTableEntryKEY,
       "prefferedListTableSecurityMethod": prefferedListTableSecurityMethod,
       "wirelessMIRList": wirelessMIRList,
       "wirelessMIRProfileTable": wirelessMIRProfileTable,
       "wirelessMIRProfileEntry": wirelessMIRProfileEntry,
       "wirelessMIRProfileIndex": wirelessMIRProfileIndex,
       "wirelessMIRProfileNumber": wirelessMIRProfileNumber,
       "wirelessMIRProfileDescription": wirelessMIRProfileDescription,
       "wirelessDLMIR": wirelessDLMIR,
       "wirelessULMIR": wirelessULMIR,
       "wirelessRadius": wirelessRadius,
       "wirelessRadiusTimeout": wirelessRadiusTimeout,
       "wirelessRadiusRetry": wirelessRadiusRetry,
       "wirelessRadiusGUIUserAuth": wirelessRadiusGUIUserAuth,
       "wirelessRadiusCurrentGUIUserAuth": wirelessRadiusCurrentGUIUserAuth,
       "wirelessRadiusSeverInfo": wirelessRadiusSeverInfo,
       "wirelessRadiusIdentityStr": wirelessRadiusIdentityStr,
       "wirelessRadiusIdentityRealm": wirelessRadiusIdentityRealm,
       "wirelessRadiusUsername": wirelessRadiusUsername,
       "wirelessRadiusPassword": wirelessRadiusPassword,
       "useMACAddressAsWirelessRadiusUsername": useMACAddressAsWirelessRadiusUsername,
       "wirelessRadiusServerList": wirelessRadiusServerList,
       "wirelessRadiusServerTable": wirelessRadiusServerTable,
       "wirelessRadiusServerEntry": wirelessRadiusServerEntry,
       "wirelessRadiusServerIndex": wirelessRadiusServerIndex,
       "wirelessRadiusServerIP": wirelessRadiusServerIP,
       "wirelessRadiusServerPort": wirelessRadiusServerPort,
       "wirelessRadiusServerSecret": wirelessRadiusServerSecret,
       "wirelessRadiusCertificateList": wirelessRadiusCertificateList,
       "wirelessRadiusCertificateListRow1": wirelessRadiusCertificateListRow1,
       "wirelessRadiusUseDefCertificate": wirelessRadiusUseDefCertificate,
       "wirelessRadiusDefCertificateView": wirelessRadiusDefCertificateView,
       "wirelessRadiusCertificateListRow2": wirelessRadiusCertificateListRow2,
       "wirelessRadiusUser1CertificateName": wirelessRadiusUser1CertificateName,
       "wirelessRadiusUser1CertificateView": wirelessRadiusUser1CertificateView,
       "wirelessRadiusCertificateListRow3": wirelessRadiusCertificateListRow3,
       "wirelessRadiusUser2CertificateName": wirelessRadiusUser2CertificateName,
       "wirelessRadiusUser2CertificateView": wirelessRadiusUser2CertificateView,
       "wirelessRadiusCertificateSet": wirelessRadiusCertificateSet,
       "wirelessRadiusDefaultCertificate": wirelessRadiusDefaultCertificate,
       "wirelessRadiusUser1Certificate": wirelessRadiusUser1Certificate,
       "wirelessRadiusUser2Certificate": wirelessRadiusUser2Certificate,
       "wirelessRadiusUseDefaultCertificate": wirelessRadiusUseDefaultCertificate,
       "wirelessRadiusExtraCertificateSet": wirelessRadiusExtraCertificateSet,
       "wirelessRadiusPMP320Certificate": wirelessRadiusPMP320Certificate,
       "wirelessRadiusUsePMP320Certificate": wirelessRadiusUsePMP320Certificate,
       "wirelessRadiusPMP450Certificate": wirelessRadiusPMP450Certificate,
       "wirelessRadiusUsePMP450Certificate": wirelessRadiusUsePMP450Certificate,
       "multicast": multicast,
       "wirelessInterface2": wirelessInterface2,
       "wirelessInterface2HTMode": wirelessInterface2HTMode,
       "wirelessInterface2TXPower": wirelessInterface2TXPower,
       "wirelessInterface2ScanFrequencyListTwenty": wirelessInterface2ScanFrequencyListTwenty,
       "wirelessInterface2ScanFrequencyListForty": wirelessInterface2ScanFrequencyListForty,
       "centerFrequency2": centerFrequency2,
       "dfsAlternative1CenterFrequency2": dfsAlternative1CenterFrequency2,
       "dfsAlternative2CenterFrequency2": dfsAlternative2CenterFrequency2,
       "dfsAlternative1Bandwidth2": dfsAlternative1Bandwidth2,
       "dfsAlternative2Bandwidth2": dfsAlternative2Bandwidth2,
       "wirelessInterface2ScanFrequencyBandwidth": wirelessInterface2ScanFrequencyBandwidth,
       "wirelessInterface2ScanFrequencyListFive": wirelessInterface2ScanFrequencyListFive,
       "wirelessInterface2ScanFrequencyListTen": wirelessInterface2ScanFrequencyListTen,
       "wirelessTXPowerManualLimit2": wirelessTXPowerManualLimit2,
       "wirelessInterface2RateMinMCS": wirelessInterface2RateMinMCS,
       "wirelessInterface2RateMaxMCS": wirelessInterface2RateMaxMCS,
       "wirelessInterface2ScanFrequencyListEighty": wirelessInterface2ScanFrequencyListEighty,
       "cambiumKeepAliveIface2": cambiumKeepAliveIface2,
       "wirelessInterface2KeepAliveEnable": wirelessInterface2KeepAliveEnable,
       "wirelessInterface2KeepAliveEPTPEnable": wirelessInterface2KeepAliveEPTPEnable,
       "wirelessInterface2STAMaxDLMCSLimit": wirelessInterface2STAMaxDLMCSLimit,
       "wirelessInterface2SuRxBfOff": wirelessInterface2SuRxBfOff,
       "wlr": wlr,
       "wlrMUMIMOEnable": wlrMUMIMOEnable,
       "l2Firewall": l2Firewall,
       "l2FirewallEnable": l2FirewallEnable,
       "l2FirewallTable": l2FirewallTable,
       "l2FirewallEntry": l2FirewallEntry,
       "l2FirewallEntryIndex": l2FirewallEntryIndex,
       "l2FirewallEntryName": l2FirewallEntryName,
       "l2FirewallEntryAction": l2FirewallEntryAction,
       "l2FirewallEntryInterface": l2FirewallEntryInterface,
       "l2FirewallEntryLog": l2FirewallEntryLog,
       "l2FirewallEntryEtherType": l2FirewallEntryEtherType,
       "l2FirewallEntryVlanID": l2FirewallEntryVlanID,
       "l2FirewallEntrySrcMAC": l2FirewallEntrySrcMAC,
       "l2FirewallEntrySrcMask": l2FirewallEntrySrcMask,
       "l2FirewallEntryDstMAC": l2FirewallEntryDstMAC,
       "l2FirewallEntryDstMask": l2FirewallEntryDstMask,
       "l2WanRemoteAccess": l2WanRemoteAccess,
       "l2SnmpLanRemoteAccess": l2SnmpLanRemoteAccess,
       "l2DHCPServersBelowSTA": l2DHCPServersBelowSTA,
       "l2LanRemoteAccess": l2LanRemoteAccess,
       "l3Firewall": l3Firewall,
       "l3FirewallEnable": l3FirewallEnable,
       "l3FirewallTable": l3FirewallTable,
       "l3FirewallEntry": l3FirewallEntry,
       "l3FirewallEntryIndex": l3FirewallEntryIndex,
       "l3FirewallEntryName": l3FirewallEntryName,
       "l3FirewallEntryAction": l3FirewallEntryAction,
       "l3FirewallEntryInterface": l3FirewallEntryInterface,
       "l3FirewallEntryLog": l3FirewallEntryLog,
       "l3FirewallEntryProtocol": l3FirewallEntryProtocol,
       "l3FirewallEntryPort": l3FirewallEntryPort,
       "l3FirewallEntrySrcIP": l3FirewallEntrySrcIP,
       "l3FirewallEntrySrcMask": l3FirewallEntrySrcMask,
       "l3FirewallEntryDstIP": l3FirewallEntryDstIP,
       "l3FirewallEntryDstMask": l3FirewallEntryDstMask,
       "l3FirewallEntryDSCP": l3FirewallEntryDSCP,
       "l3FirewallEntryToS": l3FirewallEntryToS,
       "l3FirewallEntrySrcPort": l3FirewallEntrySrcPort,
       "confQoS": confQoS,
       "voipEnable": voipEnable,
       "qosEnable": qosEnable,
       "classificationListTable": classificationListTable,
       "classificationListEntry": classificationListEntry,
       "classificationRuleIndex": classificationRuleIndex,
       "classificationRuleType": classificationRuleType,
       "classificationRuleValue": classificationRuleValue,
       "classificationRuleIP": classificationRuleIP,
       "classificationRuleMAC": classificationRuleMAC,
       "classificationRuleMask": classificationRuleMask,
       "classificationRuleDirection": classificationRuleDirection,
       "classificationRuleQueue": classificationRuleQueue,
       "mcPriority": mcPriority,
       "bcPriority": bcPriority,
       "dmz": dmz,
       "dmzEnable": dmzEnable,
       "dmzIPAddress": dmzIPAddress,
       "dmzAllowICMP": dmzAllowICMP,
       "portForwarding": portForwarding,
       "portForwardingEntryEnable": portForwardingEntryEnable,
       "portForwardingTable": portForwardingTable,
       "portForwardingEntry": portForwardingEntry,
       "portForwardingTableEntryIndex": portForwardingTableEntryIndex,
       "portForwardingTableEntryProtocol": portForwardingTableEntryProtocol,
       "portForwardingTableEntryWLANPortBegin": portForwardingTableEntryWLANPortBegin,
       "portForwardingTableEntryWLANPortEnd": portForwardingTableEntryWLANPortEnd,
       "portForwardingTableEntryLANIP": portForwardingTableEntryLANIP,
       "portForwardingTableEntryWLANPortMappedBegin": portForwardingTableEntryWLANPortMappedBegin,
       "portForwardingSepMangIPEntryEnable": portForwardingSepMangIPEntryEnable,
       "portForwardingSepMangIPTable": portForwardingSepMangIPTable,
       "portForwardingSepMangIPEntry": portForwardingSepMangIPEntry,
       "portForwardingSepMangIPTableEntryIndex": portForwardingSepMangIPTableEntryIndex,
       "portForwardingSepMangIPTableEntryProtocol": portForwardingSepMangIPTableEntryProtocol,
       "portForwardingSepMangIPTableEntryWLANPortBegin": portForwardingSepMangIPTableEntryWLANPortBegin,
       "portForwardingSepMangIPTableEntryWLANPortEnd": portForwardingSepMangIPTableEntryWLANPortEnd,
       "portForwardingSepMangIPTableEntryLANIP": portForwardingSepMangIPTableEntryLANIP,
       "portForwardingSepMangIPTableEntryWLANPortMappedBegin": portForwardingSepMangIPTableEntryWLANPortMappedBegin,
       "vlans": vlans,
       "membershipVLANTable": membershipVLANTable,
       "membershipVLANEntry": membershipVLANEntry,
       "membershipVLANTableEntryIndex": membershipVLANTableEntryIndex,
       "membershipVLANTableEntryVIDBegin": membershipVLANTableEntryVIDBegin,
       "membershipVLANTableEntryVIDEnd": membershipVLANTableEntryVIDEnd,
       "membershipVLANTableEntryInfo": membershipVLANTableEntryInfo,
       "mappingVLANTable": mappingVLANTable,
       "mappingVLANEntry": mappingVLANEntry,
       "mappingVLANTableEntryIndex": mappingVLANTableEntryIndex,
       "mappingVLANTableEntryCVLAN": mappingVLANTableEntryCVLAN,
       "mappingVLANTableEntrySVLAN": mappingVLANTableEntrySVLAN,
       "mappingVLANTableEntryInfo": mappingVLANTableEntryInfo,
       "dlkm": dlkm,
       "dlkmNATSIPHelpers": dlkmNATSIPHelpers,
       "routing": routing,
       "staticRoutesEnableMain": staticRoutesEnableMain,
       "cambiumStaticRoutesCnfTable": cambiumStaticRoutesCnfTable,
       "cambiumStaticRoutesCnfEntry": cambiumStaticRoutesCnfEntry,
       "cambiumStaticRoutesCnfIndex": cambiumStaticRoutesCnfIndex,
       "cambiumStaticRoutesCnfDestIP": cambiumStaticRoutesCnfDestIP,
       "cambiumStaticRoutesCnfGW": cambiumStaticRoutesCnfGW,
       "cambiumStaticRoutesCnfNetmask": cambiumStaticRoutesCnfNetmask,
       "cambiumStaticRoutesCnfEnbl": cambiumStaticRoutesCnfEnbl,
       "cambiumStaticRoutesCnfInfo": cambiumStaticRoutesCnfInfo,
       "cambiumTelnetServer": cambiumTelnetServer,
       "cambiumTelnetServerEnable": cambiumTelnetServerEnable,
       "cambiumTelnetServerPort": cambiumTelnetServerPort,
       "cambiumDeviceAgent": cambiumDeviceAgent,
       "cambiumDeviceAgentEnable": cambiumDeviceAgentEnable,
       "cambiumDeviceAgentCNSURL": cambiumDeviceAgentCNSURL,
       "cambiumCNSDeviceAgentID": cambiumCNSDeviceAgentID,
       "cambiumCNSDeviceAgentPassword": cambiumCNSDeviceAgentPassword,
       "cambiumDeviceAgentZeroTouchEnable": cambiumDeviceAgentZeroTouchEnable,
       "cambiumDeviceAgentMGMTRoutingEnable": cambiumDeviceAgentMGMTRoutingEnable,
       "upnpd": upnpd,
       "networkUPNP": networkUPNP,
       "networkNATPMP": networkNATPMP,
       "lldpd": lldpd,
       "networkLLDP": networkLLDP,
       "networkLLDPMode": networkLLDPMode,
       "mactelnet": mactelnet,
       "networkMACTELNET": networkMACTELNET,
       "networkMACTELNETProto": networkMACTELNETProto,
       "licensed": licensed,
       "cambiumLicenseServerEnable": cambiumLicenseServerEnable,
       "cambiumLicenseServerCloudLicensingID": cambiumLicenseServerCloudLicensingID,
       "cambiumLicenseServerStatus": cambiumLicenseServerStatus,
       "cambiumLicenseServerRefreshFail": cambiumLicenseServerRefreshFail,
       "cambiumLicenseServerUpdateFail": cambiumLicenseServerUpdateFail,
       "cambiumLicenseServerProxyEnable": cambiumLicenseServerProxyEnable,
       "cambiumLicenseServerProxyIP": cambiumLicenseServerProxyIP,
       "cambiumLicenseServerProxyPort": cambiumLicenseServerProxyPort,
       "tr069": tr069,
       "tr069Local": tr069Local,
       "cambiumTR069Enable": cambiumTR069Enable,
       "cambiumTR069Interface": cambiumTR069Interface,
       "cambiumTR069Port": cambiumTR069Port,
       "cambiumTR069Username": cambiumTR069Username,
       "cambiumTR069Password": cambiumTR069Password,
       "tr069ACS": tr069ACS,
       "cambiumTR069ACSURL": cambiumTR069ACSURL,
       "cambiumTR069ACSUsername": cambiumTR069ACSUsername,
       "cambiumTR069ACSPassword": cambiumTR069ACSPassword,
       "cambiumTR069Interval": cambiumTR069Interval,
       "bonding": bonding,
       "cambiumChannelBondingEnable": cambiumChannelBondingEnable,
       "accelerationEngine": accelerationEngine,
       "cambiumAccelerationEngine": cambiumAccelerationEngine,
       "cambiumDCS": cambiumDCS,
       "dcsEnable": dcsEnable,
       "dcsLogFile": dcsLogFile,
       "dcsFrequencyListFive": dcsFrequencyListFive,
       "dcsFrequencyListTen": dcsFrequencyListTen,
       "dcsFrequencyListTwenty": dcsFrequencyListTwenty,
       "dcsFrequencyListForty": dcsFrequencyListForty,
       "dcsFrequencyListEighty": dcsFrequencyListEighty,
       "dcsSwitchThreshold": dcsSwitchThreshold,
       "dcsSwitchMinHoldTime": dcsSwitchMinHoldTime,
       "dcsThroughputDropThreshold": dcsThroughputDropThreshold,
       "dcsBandwidthMask": dcsBandwidthMask,
       "cambiumGPSConfig": cambiumGPSConfig,
       "cambiumGPSConfigResetTimeout": cambiumGPSConfigResetTimeout,
       "vmsagent": vmsagent,
       "vmsagentEnable": vmsagentEnable,
       "vmsagentVMSType": vmsagentVMSType,
       "vmsagentVMSAddr": vmsagentVMSAddr,
       "vmsagentVMSPort": vmsagentVMSPort,
       "vmsagentUsername": vmsagentUsername,
       "vmsagentPassword": vmsagentPassword,
       "cnvisionVMSPreviewHash": cnvisionVMSPreviewHash,
       "cambiumNSS": cambiumNSS,
       "cambiumNSSAcceleratedConn": cambiumNSSAcceleratedConn,
       "cambiumNSSAcceleratedIPv4Conn": cambiumNSSAcceleratedIPv4Conn,
       "cambiumNSSAcceleratedIPv6Conn": cambiumNSSAcceleratedIPv6Conn,
       "cambiumNSSMcastFloodDestAth": cambiumNSSMcastFloodDestAth,
       "cambiumNSSMcastFloodDestEth": cambiumNSSMcastFloodDestEth,
       "dpi": dpi,
       "dpiEnable": dpiEnable,
       "dpiQoSEnable": dpiQoSEnable,
       "dpiLogLevel": dpiLogLevel,
       "dpiLogComponents": dpiLogComponents,
       "dpiQoSAppRulesTable": dpiQoSAppRulesTable,
       "dpiQoSAppRulesEntry": dpiQoSAppRulesEntry,
       "dpiQoSAppRulesIndex": dpiQoSAppRulesIndex,
       "dpiQoSAppID": dpiQoSAppID,
       "dpiQoSAppPriority": dpiQoSAppPriority,
       "dpiQoSAppRuleType": dpiQoSAppRuleType,
       "cambiumpmp80211SystemActions": cambiumpmp80211SystemActions,
       "cambiumpmp80211DeviceReboot": cambiumpmp80211DeviceReboot,
       "cambiumpmp80211ConfigurationReset": cambiumpmp80211ConfigurationReset,
       "cambiumpmp80211ConfigurationSave": cambiumpmp80211ConfigurationSave,
       "cambiumpmp80211ConfigurationApply": cambiumpmp80211ConfigurationApply,
       "cambiumpmp80211ConfigurationDiscard": cambiumpmp80211ConfigurationDiscard,
       "cambiumpmp80211ConfigurationState": cambiumpmp80211ConfigurationState,
       "cambiumpmp80211SoftwareUpdate": cambiumpmp80211SoftwareUpdate,
       "cambiumpmp80211SoftwareUpdateStatus": cambiumpmp80211SoftwareUpdateStatus,
       "cambiumpmp80211STAListUpdate": cambiumpmp80211STAListUpdate,
       "cambiumpmp80211STAListUpdateStatus": cambiumpmp80211STAListUpdateStatus,
       "cambiumpmp80211APListUpdate": cambiumpmp80211APListUpdate,
       "cambiumpmp80211APListUpdateStatus": cambiumpmp80211APListUpdateStatus,
       "cambiumpmp80211SoftwareUpdateError": cambiumpmp80211SoftwareUpdateError,
       "cambiumpmp80211StatsPerSTAListUpdateStatus": cambiumpmp80211StatsPerSTAListUpdateStatus,
       "cambiumpmp80211StatsPerSTAListUpdate": cambiumpmp80211StatsPerSTAListUpdate,
       "cambiumpmp80211STADisconnect": cambiumpmp80211STADisconnect,
       "cambiumpmp80211GPSAutopopulate": cambiumpmp80211GPSAutopopulate,
       "cambiumpmp80211SoftwareUpdateErrorStr": cambiumpmp80211SoftwareUpdateErrorStr,
       "cambiumpmp80211GpsFirmwareUpdate": cambiumpmp80211GpsFirmwareUpdate,
       "cambiumpmp80211GpsFirmwareUpdateError": cambiumpmp80211GpsFirmwareUpdateError,
       "cambiumpmp80211GpsFirmwareUpdateErrorStr": cambiumpmp80211GpsFirmwareUpdateErrorStr,
       "cambiumBridgeTableAPStatus": cambiumBridgeTableAPStatus,
       "cambiumBridgeTableSTAUpdate": cambiumBridgeTableSTAUpdate,
       "cambiumBridgeTableSTAStatus": cambiumBridgeTableSTAStatus,
       "cambiumBridgeTableAPUpdate": cambiumBridgeTableAPUpdate,
       "cambiumForceTabUpdDHCP": cambiumForceTabUpdDHCP,
       "cambiumForceTabUpdTrap": cambiumForceTabUpdTrap,
       "cambiumForceTabUpdl2Frw": cambiumForceTabUpdl2Frw,
       "cambiumForceTabUpdl3Frw": cambiumForceTabUpdl3Frw,
       "cambiumForceTabUpdQos": cambiumForceTabUpdQos,
       "cambiumForceTabUpdPortFw": cambiumForceTabUpdPortFw,
       "cambiumForceTabUpdVlan": cambiumForceTabUpdVlan,
       "cambiumForceTabUpdMappingVlan": cambiumForceTabUpdMappingVlan,
       "cambiumConfigurationApplyOnReboot": cambiumConfigurationApplyOnReboot,
       "cambiumForceSTARescan": cambiumForceSTARescan,
       "cambiumForceTabUpdMcastDeny": cambiumForceTabUpdMcastDeny,
       "cambiumForceTabUpdStaticRoutesCnf": cambiumForceTabUpdStaticRoutesCnf,
       "cambiumForceTabUpdMIR": cambiumForceTabUpdMIR,
       "cambiumForceTabUpdRadiusServ": cambiumForceTabUpdRadiusServ,
       "cambiumForceTabUpdPrefAPList": cambiumForceTabUpdPrefAPList,
       "cambiumForceTabUpdAPAlias": cambiumForceTabUpdAPAlias,
       "cambiumForceTabUpdPortFwSepMangIP": cambiumForceTabUpdPortFwSepMangIP,
       "cambiumAPListFlush": cambiumAPListFlush,
       "cambiumCCTVListUpdate": cambiumCCTVListUpdate,
       "cambiumCCTVListUpdateStatus": cambiumCCTVListUpdateStatus,
       "cambiumCCTVListFlush": cambiumCCTVListFlush,
       "cambiumForceTabUpdSwitch": cambiumForceTabUpdSwitch,
       "cambiumForceTabUpdDPIQoSApp": cambiumForceTabUpdDPIQoSApp,
       "cambiumpmp80211Tools": cambiumpmp80211Tools,
       "cambiumLinkTest": cambiumLinkTest,
       "cambiumLinkTestDuration": cambiumLinkTestDuration,
       "cambiumLinkTestPckSize": cambiumLinkTestPckSize,
       "cambiumLinkTestStartForMAC": cambiumLinkTestStartForMAC,
       "cambiumLinkTestStatus": cambiumLinkTestStatus,
       "cambiumLinkTestResultDate": cambiumLinkTestResultDate,
       "cambiumLinkTestResultUL": cambiumLinkTestResultUL,
       "cambiumLinkTestResultDL": cambiumLinkTestResultDL,
       "cambiumLinkTestForceAnt": cambiumLinkTestForceAnt,
       "cambiumLinkTestMode": cambiumLinkTestMode,
       "cambiumLinkTestMACs": cambiumLinkTestMACs,
       "cambiumLinkTestStart": cambiumLinkTestStart,
       "caminfo": caminfo,
       "caminfoScanFrequencyListCountry": caminfoScanFrequencyListCountry,
       "caminfoScanFrequencyListTwentyBand": caminfoScanFrequencyListTwentyBand,
       "caminfoScanFrequencyListFortyBand": caminfoScanFrequencyListFortyBand,
       "caminfoScanFrequencyListAllow59band": caminfoScanFrequencyListAllow59band,
       "caminfoScanFrequencyListAllow5and10bw": caminfoScanFrequencyListAllow5and10bw,
       "cambiumToolBar": cambiumToolBar,
       "cambiumToolBarOpts": cambiumToolBarOpts,
       "cambiumInternetConnectionServerIP": cambiumInternetConnectionServerIP,
       "cambiumInternetConnectionPollPeriod": cambiumInternetConnectionPollPeriod,
       "cambiumToolBarStates": cambiumToolBarStates,
       "cambiumToolbarGlobeState": cambiumToolbarGlobeState,
       "cambiumToolbarGPSSyncState": cambiumToolbarGPSSyncState,
       "cambiumToolbarDeviceConfigurationState": cambiumToolbarDeviceConfigurationState,
       "cambiumToolbarSyncSource": cambiumToolbarSyncSource,
       "cambiumToolbarGPSSyncStateStr": cambiumToolbarGPSSyncStateStr,
       "cambiumCfg": cambiumCfg,
       "cambiumJSONCfgImport": cambiumJSONCfgImport,
       "cambiumJSONCfgImportStatus": cambiumJSONCfgImportStatus,
       "cambiumJSONCfgImportError": cambiumJSONCfgImportError,
       "cambiumJSONCfgImportMode": cambiumJSONCfgImportMode,
       "cambiumJSONCfgExport": cambiumJSONCfgExport,
       "cambiumJSONCfgExportStatus": cambiumJSONCfgExportStatus,
       "cambiumJSONCfgExportError": cambiumJSONCfgExportError,
       "cambiumJSONCfgExportLink": cambiumJSONCfgExportLink,
       "cambiumFullCfgRestore": cambiumFullCfgRestore,
       "cambiumFullCfgRestoreStatus": cambiumFullCfgRestoreStatus,
       "cambiumFullCfgRestoreError": cambiumFullCfgRestoreError,
       "cambiumFullCfgRestoreMode": cambiumFullCfgRestoreMode,
       "cambiumFullCfgBackUp": cambiumFullCfgBackUp,
       "cambiumFullCfgBackUpStatus": cambiumFullCfgBackUpStatus,
       "cambiumFullCfgBackUpError": cambiumFullCfgBackUpError,
       "cambiumFullCfgBackUpLink": cambiumFullCfgBackUpLink,
       "cambiumCfgTrialImport": cambiumCfgTrialImport,
       "cambiumCfgTrialStatus": cambiumCfgTrialStatus,
       "cambiumCfgTrialError": cambiumCfgTrialError,
       "cambiumCfgTrialFinish": cambiumCfgTrialFinish,
       "cambiumCfgTrialTimer": cambiumCfgTrialTimer,
       "cambiumCfgTrialTimeout": cambiumCfgTrialTimeout,
       "cambiumIDM": cambiumIDM,
       "cambiumIDMMode": cambiumIDMMode,
       "cambiumIDMTime": cambiumIDMTime,
       "cambiumIDMEnable": cambiumIDMEnable,
       "cambiumIDMResultsTable": cambiumIDMResultsTable,
       "cambiumIDMResultsEntry": cambiumIDMResultsEntry,
       "idmDeviceListCycle": idmDeviceListCycle,
       "idmDeviceListMAC": idmDeviceListMAC,
       "idmDeviceListLCombRSSI": idmDeviceListLCombRSSI,
       "idmDeviceListLRate": idmDeviceListLRate,
       "idmDeviceListMaxRate": idmDeviceListMaxRate,
       "idmDeviceListPcktsNum": idmDeviceListPcktsNum,
       "idmDeviceListCRCCombRSSI": idmDeviceListCRCCombRSSI,
       "idmDeviceListCRCCh0RSSI": idmDeviceListCRCCh0RSSI,
       "idmDeviceListCRCCh1RSSI": idmDeviceListCRCCh1RSSI,
       "idmDeviceListCRCPcktsNum": idmDeviceListCRCPcktsNum,
       "idmDeviceListPRQCombRSSI": idmDeviceListPRQCombRSSI,
       "idmDeviceListPRQCh0RSSI": idmDeviceListPRQCh0RSSI,
       "idmDeviceListPRQCh1RSSI": idmDeviceListPRQCh1RSSI,
       "idmDeviceListPRQPcktsNum": idmDeviceListPRQPcktsNum,
       "cambiumIDMSumMAC": cambiumIDMSumMAC,
       "cambiumIDMSumLCombRSSI": cambiumIDMSumLCombRSSI,
       "cambiumIDMSumLRate": cambiumIDMSumLRate,
       "cambiumIDMSumMaxRate": cambiumIDMSumMaxRate,
       "cambiumIDMSumPcktsNum": cambiumIDMSumPcktsNum,
       "cambiumIDMSumCRCCombRSSI": cambiumIDMSumCRCCombRSSI,
       "cambiumIDMSumCRCCh0RSSI": cambiumIDMSumCRCCh0RSSI,
       "cambiumIDMSumCRCCh1RSSI": cambiumIDMSumCRCCh1RSSI,
       "cambiumIDMSumCRCPcktsNum": cambiumIDMSumCRCPcktsNum,
       "cambiumIDMSumPRQCombRSSI": cambiumIDMSumPRQCombRSSI,
       "cambiumIDMSumPRQCh0RSSI": cambiumIDMSumPRQCh0RSSI,
       "cambiumIDMSumPRQCh1RSSI": cambiumIDMSumPRQCh1RSSI,
       "cambiumIDMSumPRQPcktsNum": cambiumIDMSumPRQPcktsNum,
       "cambiumIDMSummaryTable": cambiumIDMSummaryTable,
       "cambiumIDMSummaryEntry": cambiumIDMSummaryEntry,
       "idmSummaryIntMAC": idmSummaryIntMAC,
       "idmSummaryIntCombRSSI": idmSummaryIntCombRSSI,
       "idmSummaryIntCh0RSSI": idmSummaryIntCh0RSSI,
       "idmSummaryIntCh1RSSI": idmSummaryIntCh1RSSI,
       "idmSummaryIntSSID": idmSummaryIntSSID,
       "cambiumACSCfg": cambiumACSCfg,
       "acsEnable": acsEnable,
       "acsScanMinDwellTime": acsScanMinDwellTime,
       "acsScanMaxDwellTime": acsScanMaxDwellTime,
       "acsControl": acsControl,
       "cambiumSpectral": cambiumSpectral,
       "spectralEnable": spectralEnable,
       "cambiumArcher": cambiumArcher,
       "wirelessInterfaceAttemptScanFrequencyListFive": wirelessInterfaceAttemptScanFrequencyListFive,
       "wirelessInterfaceAttemptScanFrequencyListTen": wirelessInterfaceAttemptScanFrequencyListTen,
       "wirelessInterfaceAttemptScanFrequencyListTwenty": wirelessInterfaceAttemptScanFrequencyListTwenty,
       "wirelessInterfaceAttemptScanFrequencyListForty": wirelessInterfaceAttemptScanFrequencyListForty,
       "wirelessInterfaceAttemptScanFrequencyListEighty": wirelessInterfaceAttemptScanFrequencyListEighty,
       "wirelessInterfaceAttemptScanFrequencyList160M": wirelessInterfaceAttemptScanFrequencyList160M,
       "wirelessInterfaceAttemptScanFrequencySkipCounter": wirelessInterfaceAttemptScanFrequencySkipCounter,
       "cambiumWatchdog": cambiumWatchdog,
       "watchdogEnable": watchdogEnable,
       "watchdogMode": watchdogMode,
       "watchdogTargetIPAddress": watchdogTargetIPAddress,
       "watchdogPingInterval": watchdogPingInterval,
       "watchdogPingRetries": watchdogPingRetries,
       "watchdogRF": watchdogRF,
       "watchdogRFEnable": watchdogRFEnable,
       "watchdogRFRSSIThreshold": watchdogRFRSSIThreshold,
       "watchdogRFSNRThreshold": watchdogRFSNRThreshold,
       "watchdogRFCountThreshold": watchdogRFCountThreshold,
       "watchdogGPS": watchdogGPS,
       "watchdogGPSAllowHardReset": watchdogGPSAllowHardReset,
       "cambiumCrashReporter": cambiumCrashReporter,
       "crashReporterEnable": crashReporterEnable,
       "reconnectPrimaryAPSelectIface": reconnectPrimaryAPSelectIface,
       "wirelessInterfaceReconnectPrimaryAPEnable": wirelessInterfaceReconnectPrimaryAPEnable,
       "wirelessInterfaceReconnectPrimaryAPPeriod": wirelessInterfaceReconnectPrimaryAPPeriod,
       "wirelessInterfaceReconnectPrimaryAPScanBG": wirelessInterfaceReconnectPrimaryAPScanBG,
       "cambiumHWGroupInfo": cambiumHWGroupInfo,
       "ePMPavenger5gconnectorizedsync": ePMPavenger5gconnectorizedsync,
       "ePMPavenger5gconnectorized": ePMPavenger5gconnectorized,
       "ePMPavenger5gintegrated": ePMPavenger5gintegrated,
       "ePMPavenger2gconnectorizedsync": ePMPavenger2gconnectorizedsync,
       "ePMPavenger2gconnectorized": ePMPavenger2gconnectorized,
       "ePMPavenger2gintegrated": ePMPavenger2gintegrated,
       "ePMPironman25grow": ePMPironman25grow,
       "ePMPironman22grow": ePMPironman22grow,
       "ePMPironman25gfccextflt": ePMPironman25gfccextflt,
       "ePMPironman22gfccrowextflt": ePMPironman22gfccrowextflt,
       "ePMPhawkeye": ePMPhawkeye,
       "ePMPironlad5grow": ePMPironlad5grow,
       "ePMPironlad5gfccextflt": ePMPironlad5gfccextflt,
       "ePMPdarkchocolate5grow": ePMPdarkchocolate5grow,
       "ePMPdarkchocolate5gfcc": ePMPdarkchocolate5gfcc,
       "ePMPhawkeyecrystal": ePMPhawkeyecrystal,
       "ePMPmargaret6gironlad": ePMPmargaret6gironlad,
       "ePMPmargaret6gconnectorizedsync": ePMPmargaret6gconnectorizedsync,
       "ePMPmargaret6gconnectorized": ePMPmargaret6gconnectorized,
       "ePMPelectra25gconnectorizedsync": ePMPelectra25gconnectorizedsync,
       "ePMPelectra25gconnectorized": ePMPelectra25gconnectorized,
       "ePMPforce1305g": ePMPforce1305g,
       "ePMPforce1302g": ePMPforce1302g,
       "ePMPforce200l": ePMPforce200l,
       "ePMPforce200lv2": ePMPforce200lv2,
       "ePMPptp5505gintegratedfcc": ePMPptp5505gintegratedfcc,
       "ePMPptp5505gconnectorizedfcc": ePMPptp5505gconnectorizedfcc,
       "ePMPf300fcc": ePMPf300fcc,
       "ePMPf300row": ePMPf300row,
       "ePMPepmp3000fcc": ePMPepmp3000fcc,
       "ePMPf220fcc": ePMPf220fcc,
       "ePMPf220row": ePMPf220row,
       "ePMPepmp3000row": ePMPepmp3000row,
       "ePMPptp5505gintegratedrow": ePMPptp5505gintegratedrow,
       "ePMPptp5505gconnectorizedrow": ePMPptp5505gconnectorizedrow,
       "ePMPmystiquefccsync": ePMPmystiquefccsync,
       "ePMPmystiquerowsync": ePMPmystiquerowsync,
       "ePMPmystiquefcc": ePMPmystiquefcc,
       "ePMPmystiquerow": ePMPmystiquerow,
       "ePMPxorn13fcc": ePMPxorn13fcc,
       "ePMPxorn13row": ePMPxorn13row,
       "ePMPxorn19fcc": ePMPxorn19fcc,
       "ePMPxorn19row": ePMPxorn19row,
       "ePMPxorn19rip67row": ePMPxorn19rip67row,
       "ePMPxorn19rip67fcc": ePMPxorn19rip67fcc,
       "ePMPhellcowfcc": ePMPhellcowfcc,
       "ePMPhellcowrow": ePMPhellcowrow,
       "ePMPf300fccv2": ePMPf300fccv2,
       "ePMPf30025l": ePMPf30025l,
       "ePMPf30025lv2": ePMPf30025lv2,
       "ePMPf30013l": ePMPf30013l,
       "ePMPe510": ePMPe510,
       "ePMPnanostationm5v3xw": ePMPnanostationm5v3xw,
       "ePMPnanostationlocom5v3": ePMPnanostationlocom5v3,
       "ePMPnanostationlocom2xw": ePMPnanostationlocom2xw,
       "ePMPnanostationlocom2v2xw": ePMPnanostationlocom2v2xw,
       "ePMPnanostationlocom2v3xw": ePMPnanostationlocom2v3xw,
       "ePMProcketm5xwv1": ePMProcketm5xwv1,
       "ePMProcketm5x3wv2": ePMProcketm5x3wv2,
       "ePMPnanobeamm516xw": ePMPnanobeamm516xw,
       "ePMPnanobeamm519xw": ePMPnanobeamm519xw,
       "ePMPnanobeamm2xw": ePMPnanobeamm2xw,
       "ePMPrbsxtlite5": ePMPrbsxtlite5,
       "ePMPintelbras": ePMPintelbras,
       "ePMPlhg5": ePMPlhg5,
       "ePMPdisclite5": ePMPdisclite5,
       "ePMPmk911l": ePMPmk911l,
       "ePMPsextant": ePMPsextant,
       "ePMPpowerbeamm5300": ePMPpowerbeamm5300,
       "ePMPpowerbeamm5400": ePMPpowerbeamm5400,
       "ePMPpowerbeamm5620": ePMPpowerbeamm5620,
       "ePMPpowerbeamm2400": ePMPpowerbeamm2400,
       "ePMPpowerbeamm5400iso": ePMPpowerbeamm5400iso,
       "ePMPpowerbeamm5300iso": ePMPpowerbeamm5300iso,
       "ePMPpowerbeamm5600iso": ePMPpowerbeamm5600iso,
       "ePMPnanostationm5v1xm": ePMPnanostationm5v1xm,
       "ePMPnanostationm5v2xm": ePMPnanostationm5v2xm,
       "ePMPnanostationm365xm": ePMPnanostationm365xm,
       "ePMPnanostationm2v1xm": ePMPnanostationm2v1xm,
       "ePMPnanostationm3xm": ePMPnanostationm3xm,
       "ePMPnanostationm900xm": ePMPnanostationm900xm,
       "ePMPnanostationm2v2xm": ePMPnanostationm2v2xm,
       "ePMPnanostationlocom5v1xm": ePMPnanostationlocom5v1xm,
       "ePMPnanostationlocom5v2xm": ePMPnanostationlocom5v2xm,
       "ePMPnanostationlocom900xm": ePMPnanostationlocom900xm,
       "ePMPnanostationlocom2xm": ePMPnanostationlocom2xm,
       "ePMPnanobridgem365xm": ePMPnanobridgem365xm,
       "ePMPnanobridgem900xm": ePMPnanobridgem900xm,
       "ePMPnanobridgem3xm": ePMPnanobridgem3xm,
       "ePMPnanobridgem5nb5g22xm": ePMPnanobridgem5nb5g22xm,
       "ePMPnanobridgem5nb5g25xm": ePMPnanobridgem5nb5g25xm,
       "ePMPnanobridgem5nbxm": ePMPnanobridgem5nbxm,
       "ePMPnanobridgem2v1xm": ePMPnanobridgem2v1xm,
       "ePMPnanobridgem2v2xm": ePMPnanobridgem2v2xm,
       "ePMPintelbraswom5amimo": ePMPintelbraswom5amimo,
       "ePMPintelbraswom5a23": ePMPintelbraswom5a23,
       "ePMPpowerbridgem365xm": ePMPpowerbridgem365xm,
       "ePMPpowerbridgem3xm": ePMPpowerbridgem3xm,
       "ePMPnanostationm6xm": ePMPnanostationm6xm,
       "ePMProcketm5v1xm": ePMProcketm5v1xm,
       "ePMProcketm5v2xm": ePMProcketm5v2xm,
       "ePMProcketm5v3xm": ePMProcketm5v3xm,
       "ePMProcketm5v4xm": ePMProcketm5v4xm,
       "ePMProcketm2v1xm": ePMProcketm2v1xm,
       "ePMProcketm2v2xm": ePMProcketm2v2xm,
       "ePMProcketm2v3xm": ePMProcketm2v3xm,
       "ePMProcketm2v4xm": ePMProcketm2v4xm,
       "ePMPepmp60004x46growfcc": ePMPepmp60004x46growfcc,
       "ePMPepmp40008x85grow": ePMPepmp40008x85grow,
       "ePMPepmp4500c8x85grow": ePMPepmp4500c8x85grow,
       "ePMPepmp40008x85gfcc": ePMPepmp40008x85gfcc,
       "ePMPepmp4500c8x85gfcc": ePMPepmp4500c8x85gfcc,
       "ePMPepmp4600l6growfcc": ePMPepmp4600l6growfcc,
       "ePMPf400gps5grow": ePMPf400gps5grow,
       "ePMPf400gps5gfcc": ePMPf400gps5gfcc,
       "ePMPcnppilottiger5g": ePMPcnppilottiger5g,
       "ePMPf4255grow": ePMPf4255grow,
       "ePMPf400c5grow": ePMPf400c5grow,
       "ePMPf4255gfcc": ePMPf4255gfcc,
       "ePMPf400c5gfcc": ePMPf400c5gfcc,
       "ePMPf600c6growfcc": ePMPf600c6growfcc,
       "ePMPf600c6gfcc": ePMPf600c6gfcc,
       "ePMPf4165grow": ePMPf4165grow,
       "ePMPf425l5grow": ePMPf425l5grow,
       "ePMPf425ulnomcu5grow": ePMPf425ulnomcu5grow,
       "ePMPf4165gfcc": ePMPf4165gfcc,
       "ePMPf425l5gfcc": ePMPf425l5gfcc,
       "ePMPf6166grow": ePMPf6166grow,
       "ePMPf6256grow": ePMPf6256grow,
       "ePMPf616usbgps6gfcc": ePMPf616usbgps6gfcc,
       "ePMPf625usbgps6gfcc": ePMPf625usbgps6gfcc}
)
