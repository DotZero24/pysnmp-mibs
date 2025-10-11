# SNMP MIB module (RUGGEDCOM-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-DOT11-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:41 2025
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

(ruggedcomMgmt,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt")

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
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDot11GlobalParams_ObjectIdentity = ObjectIdentity
rcDot11GlobalParams = _RcDot11GlobalParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rcDot11GlobalParams.setStatus("current")


class _RcDot11OpMode_Type(Integer32):
    """Custom type rcDot11OpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("clientBridge", 2),
          ("clientIpBridge", 3))
    )


_RcDot11OpMode_Type.__name__ = "Integer32"
_RcDot11OpMode_Object = MibScalar
rcDot11OpMode = _RcDot11OpMode_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 1),
    _RcDot11OpMode_Type()
)
rcDot11OpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11OpMode.setStatus("current")
_RcDot11RFMAC_Type = MacAddress
_RcDot11RFMAC_Object = MibScalar
rcDot11RFMAC = _RcDot11RFMAC_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 2),
    _RcDot11RFMAC_Type()
)
rcDot11RFMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11RFMAC.setStatus("current")
_RcDot11IpAddress_Type = IpAddress
_RcDot11IpAddress_Object = MibScalar
rcDot11IpAddress = _RcDot11IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 3),
    _RcDot11IpAddress_Type()
)
rcDot11IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11IpAddress.setStatus("current")
_RcDot11IpSubnet_Type = IpAddress
_RcDot11IpSubnet_Object = MibScalar
rcDot11IpSubnet = _RcDot11IpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 4),
    _RcDot11IpSubnet_Type()
)
rcDot11IpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11IpSubnet.setStatus("current")
_RcDot11DefaultGateway_Type = IpAddress
_RcDot11DefaultGateway_Object = MibScalar
rcDot11DefaultGateway = _RcDot11DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 5),
    _RcDot11DefaultGateway_Type()
)
rcDot11DefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11DefaultGateway.setStatus("current")


class _RcDot11Status_Type(Integer32):
    """Custom type rcDot11Status based on Integer32"""
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
        *(("unknown", 1),
          ("booting", 2),
          ("running", 3),
          ("cmdProcessing", 4),
          ("softwareUpgrade", 5))
    )


_RcDot11Status_Type.__name__ = "Integer32"
_RcDot11Status_Object = MibScalar
rcDot11Status = _RcDot11Status_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 6),
    _RcDot11Status_Type()
)
rcDot11Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11Status.setStatus("current")
_RcDot11UpTime_Type = DisplayString
_RcDot11UpTime_Object = MibScalar
rcDot11UpTime = _RcDot11UpTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 7),
    _RcDot11UpTime_Type()
)
rcDot11UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11UpTime.setStatus("current")
_RcDot11Version_Type = DisplayString
_RcDot11Version_Object = MibScalar
rcDot11Version = _RcDot11Version_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 8),
    _RcDot11Version_Type()
)
rcDot11Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11Version.setStatus("current")
_RcDot11TftpServerIpAddress_Type = IpAddress
_RcDot11TftpServerIpAddress_Object = MibScalar
rcDot11TftpServerIpAddress = _RcDot11TftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 9),
    _RcDot11TftpServerIpAddress_Type()
)
rcDot11TftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11TftpServerIpAddress.setStatus("current")
_RcDot11SwUpgrade_Type = TruthValue
_RcDot11SwUpgrade_Object = MibScalar
rcDot11SwUpgrade = _RcDot11SwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 10),
    _RcDot11SwUpgrade_Type()
)
rcDot11SwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SwUpgrade.setStatus("current")
_RcDot11SwUpgradeStatus_Type = DisplayString
_RcDot11SwUpgradeStatus_Object = MibScalar
rcDot11SwUpgradeStatus = _RcDot11SwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 11),
    _RcDot11SwUpgradeStatus_Type()
)
rcDot11SwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11SwUpgradeStatus.setStatus("current")


class _RcDot11WlanReset_Type(Integer32):
    """Custom type rcDot11WlanReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("fullReset", 2),
          ("quickReset", 3))
    )


_RcDot11WlanReset_Type.__name__ = "Integer32"
_RcDot11WlanReset_Object = MibScalar
rcDot11WlanReset = _RcDot11WlanReset_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 1, 12),
    _RcDot11WlanReset_Type()
)
rcDot11WlanReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11WlanReset.setStatus("current")
_RcDot11NetworkParams_ObjectIdentity = ObjectIdentity
rcDot11NetworkParams = _RcDot11NetworkParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2)
)
if mibBuilder.loadTexts:
    rcDot11NetworkParams.setStatus("current")


class _RcDot11NetworkPhyMode_Type(Integer32):
    """Custom type rcDot11NetworkPhyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_RcDot11NetworkPhyMode_Type.__name__ = "Integer32"
_RcDot11NetworkPhyMode_Object = MibScalar
rcDot11NetworkPhyMode = _RcDot11NetworkPhyMode_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 1),
    _RcDot11NetworkPhyMode_Type()
)
rcDot11NetworkPhyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkPhyMode.setStatus("current")


class _RcDot11NetworkDesiredSsid_Type(OctetString):
    """Custom type rcDot11NetworkDesiredSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_RcDot11NetworkDesiredSsid_Type.__name__ = "OctetString"
_RcDot11NetworkDesiredSsid_Object = MibScalar
rcDot11NetworkDesiredSsid = _RcDot11NetworkDesiredSsid_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 2),
    _RcDot11NetworkDesiredSsid_Type()
)
rcDot11NetworkDesiredSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkDesiredSsid.setStatus("current")


class _RcDot11NetworkPrimarySsid_Type(OctetString):
    """Custom type rcDot11NetworkPrimarySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_RcDot11NetworkPrimarySsid_Type.__name__ = "OctetString"
_RcDot11NetworkPrimarySsid_Object = MibScalar
rcDot11NetworkPrimarySsid = _RcDot11NetworkPrimarySsid_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 3),
    _RcDot11NetworkPrimarySsid_Type()
)
rcDot11NetworkPrimarySsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkPrimarySsid.setStatus("current")


class _RcDot11NetworkSecondary1Ssid_Type(OctetString):
    """Custom type rcDot11NetworkSecondary1Ssid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_RcDot11NetworkSecondary1Ssid_Type.__name__ = "OctetString"
_RcDot11NetworkSecondary1Ssid_Object = MibScalar
rcDot11NetworkSecondary1Ssid = _RcDot11NetworkSecondary1Ssid_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 4),
    _RcDot11NetworkSecondary1Ssid_Type()
)
rcDot11NetworkSecondary1Ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkSecondary1Ssid.setStatus("current")


class _RcDot11NetworkSecondary2Ssid_Type(OctetString):
    """Custom type rcDot11NetworkSecondary2Ssid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_RcDot11NetworkSecondary2Ssid_Type.__name__ = "OctetString"
_RcDot11NetworkSecondary2Ssid_Object = MibScalar
rcDot11NetworkSecondary2Ssid = _RcDot11NetworkSecondary2Ssid_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 5),
    _RcDot11NetworkSecondary2Ssid_Type()
)
rcDot11NetworkSecondary2Ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkSecondary2Ssid.setStatus("current")


class _RcDot11NetworkRfChannel_Type(Integer32):
    """Custom type rcDot11NetworkRfChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_RcDot11NetworkRfChannel_Type.__name__ = "Integer32"
_RcDot11NetworkRfChannel_Object = MibScalar
rcDot11NetworkRfChannel = _RcDot11NetworkRfChannel_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 6),
    _RcDot11NetworkRfChannel_Type()
)
rcDot11NetworkRfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkRfChannel.setStatus("current")
_RcDot11NetworkSsidTxSuppress_Type = TruthValue
_RcDot11NetworkSsidTxSuppress_Object = MibScalar
rcDot11NetworkSsidTxSuppress = _RcDot11NetworkSsidTxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 7),
    _RcDot11NetworkSsidTxSuppress_Type()
)
rcDot11NetworkSsidTxSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkSsidTxSuppress.setStatus("current")
_RcDot11NetworkRfTxEnable_Type = TruthValue
_RcDot11NetworkRfTxEnable_Object = MibScalar
rcDot11NetworkRfTxEnable = _RcDot11NetworkRfTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 8),
    _RcDot11NetworkRfTxEnable_Type()
)
rcDot11NetworkRfTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkRfTxEnable.setStatus("current")


class _RcDot11NetworkRate_Type(Integer32):
    """Custom type rcDot11NetworkRate based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("best", 1),
          ("mbps1", 2),
          ("mbps2", 3),
          ("mbps11", 4),
          ("mbps12", 5),
          ("mbps18", 6),
          ("mbps24", 7),
          ("mbps36", 8),
          ("mbps48", 9),
          ("mbps54", 10))
    )


_RcDot11NetworkRate_Type.__name__ = "Integer32"
_RcDot11NetworkRate_Object = MibScalar
rcDot11NetworkRate = _RcDot11NetworkRate_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 9),
    _RcDot11NetworkRate_Type()
)
rcDot11NetworkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkRate.setStatus("current")


class _RcDot11NetworkTxPower_Type(Integer32):
    """Custom type rcDot11NetworkTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RcDot11NetworkTxPower_Type.__name__ = "Integer32"
_RcDot11NetworkTxPower_Object = MibScalar
rcDot11NetworkTxPower = _RcDot11NetworkTxPower_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 10),
    _RcDot11NetworkTxPower_Type()
)
rcDot11NetworkTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkTxPower.setStatus("current")
_RcDot11NetworkWdsEnable_Type = TruthValue
_RcDot11NetworkWdsEnable_Object = MibScalar
rcDot11NetworkWdsEnable = _RcDot11NetworkWdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 11),
    _RcDot11NetworkWdsEnable_Type()
)
rcDot11NetworkWdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkWdsEnable.setStatus("current")
_RcDot11NetworkWmmEnable_Type = TruthValue
_RcDot11NetworkWmmEnable_Object = MibScalar
rcDot11NetworkWmmEnable = _RcDot11NetworkWmmEnable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 12),
    _RcDot11NetworkWmmEnable_Type()
)
rcDot11NetworkWmmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkWmmEnable.setStatus("current")
_RcDot11NetworkTxShortPreamble_Type = TruthValue
_RcDot11NetworkTxShortPreamble_Object = MibScalar
rcDot11NetworkTxShortPreamble = _RcDot11NetworkTxShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 13),
    _RcDot11NetworkTxShortPreamble_Type()
)
rcDot11NetworkTxShortPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkTxShortPreamble.setStatus("current")


class _RcDot11NetworkDistance_Type(Integer32):
    """Custom type rcDot11NetworkDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 15000),
    )


_RcDot11NetworkDistance_Type.__name__ = "Integer32"
_RcDot11NetworkDistance_Object = MibScalar
rcDot11NetworkDistance = _RcDot11NetworkDistance_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 14),
    _RcDot11NetworkDistance_Type()
)
rcDot11NetworkDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11NetworkDistance.setStatus("current")


class _RcDot11NetworkAssociatedStations_Type(Unsigned32):
    """Custom type rcDot11NetworkAssociatedStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RcDot11NetworkAssociatedStations_Type.__name__ = "Unsigned32"
_RcDot11NetworkAssociatedStations_Object = MibScalar
rcDot11NetworkAssociatedStations = _RcDot11NetworkAssociatedStations_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 2, 15),
    _RcDot11NetworkAssociatedStations_Type()
)
rcDot11NetworkAssociatedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11NetworkAssociatedStations.setStatus("current")
_RcDot11SecurityParams_ObjectIdentity = ObjectIdentity
rcDot11SecurityParams = _RcDot11SecurityParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3)
)
if mibBuilder.loadTexts:
    rcDot11SecurityParams.setStatus("current")


class _RcDot11SecurityAuthMode_Type(Integer32):
    """Custom type rcDot11SecurityAuthMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep", 2),
          ("dot1x", 3),
          ("wpa", 4),
          ("wpaPsk", 5),
          ("wpa2", 6),
          ("wpa2psk", 7),
          ("wpaAuto", 8),
          ("wpaAutoPsk", 9))
    )


_RcDot11SecurityAuthMode_Type.__name__ = "Integer32"
_RcDot11SecurityAuthMode_Object = MibScalar
rcDot11SecurityAuthMode = _RcDot11SecurityAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 1),
    _RcDot11SecurityAuthMode_Type()
)
rcDot11SecurityAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityAuthMode.setStatus("current")


class _RcDot11SecurityEncrypType_Type(Integer32):
    """Custom type rcDot11SecurityEncrypType based on Integer32"""
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
        *(("auto", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes", 4))
    )


_RcDot11SecurityEncrypType_Type.__name__ = "Integer32"
_RcDot11SecurityEncrypType_Object = MibScalar
rcDot11SecurityEncrypType = _RcDot11SecurityEncrypType_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 2),
    _RcDot11SecurityEncrypType_Type()
)
rcDot11SecurityEncrypType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityEncrypType.setStatus("current")


class _RcDot11SecurityPassPhrase_Type(OctetString):
    """Custom type rcDot11SecurityPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RcDot11SecurityPassPhrase_Type.__name__ = "OctetString"
_RcDot11SecurityPassPhrase_Object = MibScalar
rcDot11SecurityPassPhrase = _RcDot11SecurityPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 3),
    _RcDot11SecurityPassPhrase_Type()
)
rcDot11SecurityPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityPassPhrase.setStatus("current")


class _RcDot11SecurityWepKey_Type(OctetString):
    """Custom type rcDot11SecurityWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_RcDot11SecurityWepKey_Type.__name__ = "OctetString"
_RcDot11SecurityWepKey_Object = MibScalar
rcDot11SecurityWepKey = _RcDot11SecurityWepKey_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 4),
    _RcDot11SecurityWepKey_Type()
)
rcDot11SecurityWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityWepKey.setStatus("current")
_RcDot11SecurityKeyRenewal_Type = TimeTicks
_RcDot11SecurityKeyRenewal_Object = MibScalar
rcDot11SecurityKeyRenewal = _RcDot11SecurityKeyRenewal_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 5),
    _RcDot11SecurityKeyRenewal_Type()
)
rcDot11SecurityKeyRenewal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityKeyRenewal.setStatus("current")
_RcDot11SecurityRadiusIpAddress_Type = IpAddress
_RcDot11SecurityRadiusIpAddress_Object = MibScalar
rcDot11SecurityRadiusIpAddress = _RcDot11SecurityRadiusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 6),
    _RcDot11SecurityRadiusIpAddress_Type()
)
rcDot11SecurityRadiusIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityRadiusIpAddress.setStatus("current")


class _RcDot11SecurityRadiusPort_Type(Integer32):
    """Custom type rcDot11SecurityRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcDot11SecurityRadiusPort_Type.__name__ = "Integer32"
_RcDot11SecurityRadiusPort_Object = MibScalar
rcDot11SecurityRadiusPort = _RcDot11SecurityRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 7),
    _RcDot11SecurityRadiusPort_Type()
)
rcDot11SecurityRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityRadiusPort.setStatus("current")


class _RcDot11SecurityRadiusSecret_Type(OctetString):
    """Custom type rcDot11SecurityRadiusSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 48),
    )


_RcDot11SecurityRadiusSecret_Type.__name__ = "OctetString"
_RcDot11SecurityRadiusSecret_Object = MibScalar
rcDot11SecurityRadiusSecret = _RcDot11SecurityRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 3, 8),
    _RcDot11SecurityRadiusSecret_Type()
)
rcDot11SecurityRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11SecurityRadiusSecret.setStatus("current")
_RcDot11MacFiltering_ObjectIdentity = ObjectIdentity
rcDot11MacFiltering = _RcDot11MacFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4)
)
if mibBuilder.loadTexts:
    rcDot11MacFiltering.setStatus("current")


class _RcDot11MacFilteringControl_Type(Integer32):
    """Custom type rcDot11MacFilteringControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("allow", 2),
          ("deny", 3))
    )


_RcDot11MacFilteringControl_Type.__name__ = "Integer32"
_RcDot11MacFilteringControl_Object = MibScalar
rcDot11MacFilteringControl = _RcDot11MacFilteringControl_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4, 1),
    _RcDot11MacFilteringControl_Type()
)
rcDot11MacFilteringControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11MacFilteringControl.setStatus("current")
_RcDot11MacFilteringTable_Object = MibTable
rcDot11MacFilteringTable = _RcDot11MacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4, 2)
)
if mibBuilder.loadTexts:
    rcDot11MacFilteringTable.setStatus("current")
_RcDot11MacFilteringEntry_Object = MibTableRow
rcDot11MacFilteringEntry = _RcDot11MacFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4, 2, 1)
)
rcDot11MacFilteringEntry.setIndexNames(
    (0, "RUGGEDCOM-DOT11-MIB", "rcDot11FilterMacAddress"),
)
if mibBuilder.loadTexts:
    rcDot11MacFilteringEntry.setStatus("current")
_RcDot11FilterMacAddress_Type = MacAddress
_RcDot11FilterMacAddress_Object = MibTableColumn
rcDot11FilterMacAddress = _RcDot11FilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4, 2, 1, 1),
    _RcDot11FilterMacAddress_Type()
)
rcDot11FilterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot11FilterMacAddress.setStatus("current")


class _RcDot11RowStatus_Type(Integer32):
    """Custom type rcDot11RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("delete", 6))
    )


_RcDot11RowStatus_Type.__name__ = "Integer32"
_RcDot11RowStatus_Object = MibTableColumn
rcDot11RowStatus = _RcDot11RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 4, 2, 1, 2),
    _RcDot11RowStatus_Type()
)
rcDot11RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot11RowStatus.setStatus("current")
_RcDot11DhcpParams_ObjectIdentity = ObjectIdentity
rcDot11DhcpParams = _RcDot11DhcpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5)
)
if mibBuilder.loadTexts:
    rcDot11DhcpParams.setStatus("current")
_RcDot11DhcpServerEnable_Type = TruthValue
_RcDot11DhcpServerEnable_Object = MibScalar
rcDot11DhcpServerEnable = _RcDot11DhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 1),
    _RcDot11DhcpServerEnable_Type()
)
rcDot11DhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpServerEnable.setStatus("current")
_RcDot11DhcpStartOfPool_Type = IpAddress
_RcDot11DhcpStartOfPool_Object = MibScalar
rcDot11DhcpStartOfPool = _RcDot11DhcpStartOfPool_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 2),
    _RcDot11DhcpStartOfPool_Type()
)
rcDot11DhcpStartOfPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpStartOfPool.setStatus("current")


class _RcDot11DhcpIpPoolSize_Type(Integer32):
    """Custom type rcDot11DhcpIpPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RcDot11DhcpIpPoolSize_Type.__name__ = "Integer32"
_RcDot11DhcpIpPoolSize_Object = MibScalar
rcDot11DhcpIpPoolSize = _RcDot11DhcpIpPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 3),
    _RcDot11DhcpIpPoolSize_Type()
)
rcDot11DhcpIpPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpIpPoolSize.setStatus("current")
_RcDot11DhcpSubnet_Type = IpAddress
_RcDot11DhcpSubnet_Object = MibScalar
rcDot11DhcpSubnet = _RcDot11DhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 4),
    _RcDot11DhcpSubnet_Type()
)
rcDot11DhcpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpSubnet.setStatus("current")
_RcDot11DhcpGateway_Type = IpAddress
_RcDot11DhcpGateway_Object = MibScalar
rcDot11DhcpGateway = _RcDot11DhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 5),
    _RcDot11DhcpGateway_Type()
)
rcDot11DhcpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpGateway.setStatus("current")
_RcDot11DhcpDnsIpAddress_Type = IpAddress
_RcDot11DhcpDnsIpAddress_Object = MibScalar
rcDot11DhcpDnsIpAddress = _RcDot11DhcpDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 6),
    _RcDot11DhcpDnsIpAddress_Type()
)
rcDot11DhcpDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpDnsIpAddress.setStatus("current")
_RcDot11DhcpLeaseTime_Type = TimeTicks
_RcDot11DhcpLeaseTime_Object = MibScalar
rcDot11DhcpLeaseTime = _RcDot11DhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 5, 7),
    _RcDot11DhcpLeaseTime_Type()
)
rcDot11DhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot11DhcpLeaseTime.setStatus("current")
_RcDot11AssociationInfo_ObjectIdentity = ObjectIdentity
rcDot11AssociationInfo = _RcDot11AssociationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6)
)
if mibBuilder.loadTexts:
    rcDot11AssociationInfo.setStatus("current")
_RcDot11AssociationTable_Object = MibTable
rcDot11AssociationTable = _RcDot11AssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rcDot11AssociationTable.setStatus("current")
_RcDot11AssociationEntry_Object = MibTableRow
rcDot11AssociationEntry = _RcDot11AssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1)
)
rcDot11AssociationEntry.setIndexNames(
    (0, "RUGGEDCOM-DOT11-MIB", "rcDot11AssociationMac"),
)
if mibBuilder.loadTexts:
    rcDot11AssociationEntry.setStatus("current")
_RcDot11AssociationMac_Type = MacAddress
_RcDot11AssociationMac_Object = MibTableColumn
rcDot11AssociationMac = _RcDot11AssociationMac_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 1),
    _RcDot11AssociationMac_Type()
)
rcDot11AssociationMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot11AssociationMac.setStatus("current")
_RcDot11AssociationChannel_Type = Unsigned32
_RcDot11AssociationChannel_Object = MibTableColumn
rcDot11AssociationChannel = _RcDot11AssociationChannel_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 2),
    _RcDot11AssociationChannel_Type()
)
rcDot11AssociationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationChannel.setStatus("current")
_RcDot11AssociationRate_Type = Unsigned32
_RcDot11AssociationRate_Object = MibTableColumn
rcDot11AssociationRate = _RcDot11AssociationRate_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 3),
    _RcDot11AssociationRate_Type()
)
rcDot11AssociationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationRate.setStatus("current")
_RcDot11AssociationRssi_Type = Unsigned32
_RcDot11AssociationRssi_Object = MibTableColumn
rcDot11AssociationRssi = _RcDot11AssociationRssi_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 4),
    _RcDot11AssociationRssi_Type()
)
rcDot11AssociationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationRssi.setStatus("current")
_RcDot11AssociationTxSeq_Type = Unsigned32
_RcDot11AssociationTxSeq_Object = MibTableColumn
rcDot11AssociationTxSeq = _RcDot11AssociationTxSeq_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 5),
    _RcDot11AssociationTxSeq_Type()
)
rcDot11AssociationTxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationTxSeq.setStatus("current")
_RcDot11AssociationRxSeq_Type = Unsigned32
_RcDot11AssociationRxSeq_Object = MibTableColumn
rcDot11AssociationRxSeq = _RcDot11AssociationRxSeq_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 6),
    _RcDot11AssociationRxSeq_Type()
)
rcDot11AssociationRxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationRxSeq.setStatus("current")
_RcDot11AssociationSecurity_Type = OctetString
_RcDot11AssociationSecurity_Object = MibTableColumn
rcDot11AssociationSecurity = _RcDot11AssociationSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 6, 1, 1, 7),
    _RcDot11AssociationSecurity_Type()
)
rcDot11AssociationSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot11AssociationSecurity.setStatus("current")
_RcDot11Conformance_ObjectIdentity = ObjectIdentity
rcDot11Conformance = _RcDot11Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10)
)
_RcDot11Groups_ObjectIdentity = ObjectIdentity
rcDot11Groups = _RcDot11Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2)
)

# Managed Objects groups

rcDot11GlobalParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 1)
)
rcDot11GlobalParamsGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11OpMode"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11RFMAC"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11IpAddress"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11IpSubnet"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DefaultGateway"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11Status"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11UpTime"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11Version"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11TftpServerIpAddress"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SwUpgrade"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SwUpgradeStatus"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11WlanReset"))
)
if mibBuilder.loadTexts:
    rcDot11GlobalParamsGroup.setStatus("current")

rcDot11NetworkParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 2)
)
rcDot11NetworkParamsGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkPhyMode"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkDesiredSsid"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkPrimarySsid"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkSecondary1Ssid"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkSecondary2Ssid"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkRfChannel"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkSsidTxSuppress"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkAssociatedStations"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkRfTxEnable"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkRate"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkTxPower"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkWdsEnable"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkWmmEnable"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkTxShortPreamble"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11NetworkDistance"))
)
if mibBuilder.loadTexts:
    rcDot11NetworkParamsGroup.setStatus("current")

rcDot11SecurityParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 3)
)
rcDot11SecurityParamsGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityAuthMode"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityEncrypType"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityPassPhrase"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityWepKey"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityKeyRenewal"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityRadiusIpAddress"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityRadiusPort"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11SecurityRadiusSecret"))
)
if mibBuilder.loadTexts:
    rcDot11SecurityParamsGroup.setStatus("current")

rcDot11DhcpParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 4)
)
rcDot11DhcpParamsGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpServerEnable"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpStartOfPool"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpIpPoolSize"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpSubnet"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpGateway"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpDnsIpAddress"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11DhcpLeaseTime"))
)
if mibBuilder.loadTexts:
    rcDot11DhcpParamsGroup.setStatus("current")

rcDot11MacFilteringTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 5)
)
rcDot11MacFilteringTableGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11MacFilteringControl"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11RowStatus"))
)
if mibBuilder.loadTexts:
    rcDot11MacFilteringTableGroup.setStatus("current")

rcDot11AssociationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 4, 10, 2, 6)
)
rcDot11AssociationTableGroup.setObjects(
      *(("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationChannel"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationRate"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationRssi"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationTxSeq"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationRxSeq"),
        ("RUGGEDCOM-DOT11-MIB", "rcDot11AssociationSecurity"))
)
if mibBuilder.loadTexts:
    rcDot11AssociationTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-DOT11-MIB",
    **{"rcDot11": rcDot11,
       "rcDot11GlobalParams": rcDot11GlobalParams,
       "rcDot11OpMode": rcDot11OpMode,
       "rcDot11RFMAC": rcDot11RFMAC,
       "rcDot11IpAddress": rcDot11IpAddress,
       "rcDot11IpSubnet": rcDot11IpSubnet,
       "rcDot11DefaultGateway": rcDot11DefaultGateway,
       "rcDot11Status": rcDot11Status,
       "rcDot11UpTime": rcDot11UpTime,
       "rcDot11Version": rcDot11Version,
       "rcDot11TftpServerIpAddress": rcDot11TftpServerIpAddress,
       "rcDot11SwUpgrade": rcDot11SwUpgrade,
       "rcDot11SwUpgradeStatus": rcDot11SwUpgradeStatus,
       "rcDot11WlanReset": rcDot11WlanReset,
       "rcDot11NetworkParams": rcDot11NetworkParams,
       "rcDot11NetworkPhyMode": rcDot11NetworkPhyMode,
       "rcDot11NetworkDesiredSsid": rcDot11NetworkDesiredSsid,
       "rcDot11NetworkPrimarySsid": rcDot11NetworkPrimarySsid,
       "rcDot11NetworkSecondary1Ssid": rcDot11NetworkSecondary1Ssid,
       "rcDot11NetworkSecondary2Ssid": rcDot11NetworkSecondary2Ssid,
       "rcDot11NetworkRfChannel": rcDot11NetworkRfChannel,
       "rcDot11NetworkSsidTxSuppress": rcDot11NetworkSsidTxSuppress,
       "rcDot11NetworkRfTxEnable": rcDot11NetworkRfTxEnable,
       "rcDot11NetworkRate": rcDot11NetworkRate,
       "rcDot11NetworkTxPower": rcDot11NetworkTxPower,
       "rcDot11NetworkWdsEnable": rcDot11NetworkWdsEnable,
       "rcDot11NetworkWmmEnable": rcDot11NetworkWmmEnable,
       "rcDot11NetworkTxShortPreamble": rcDot11NetworkTxShortPreamble,
       "rcDot11NetworkDistance": rcDot11NetworkDistance,
       "rcDot11NetworkAssociatedStations": rcDot11NetworkAssociatedStations,
       "rcDot11SecurityParams": rcDot11SecurityParams,
       "rcDot11SecurityAuthMode": rcDot11SecurityAuthMode,
       "rcDot11SecurityEncrypType": rcDot11SecurityEncrypType,
       "rcDot11SecurityPassPhrase": rcDot11SecurityPassPhrase,
       "rcDot11SecurityWepKey": rcDot11SecurityWepKey,
       "rcDot11SecurityKeyRenewal": rcDot11SecurityKeyRenewal,
       "rcDot11SecurityRadiusIpAddress": rcDot11SecurityRadiusIpAddress,
       "rcDot11SecurityRadiusPort": rcDot11SecurityRadiusPort,
       "rcDot11SecurityRadiusSecret": rcDot11SecurityRadiusSecret,
       "rcDot11MacFiltering": rcDot11MacFiltering,
       "rcDot11MacFilteringControl": rcDot11MacFilteringControl,
       "rcDot11MacFilteringTable": rcDot11MacFilteringTable,
       "rcDot11MacFilteringEntry": rcDot11MacFilteringEntry,
       "rcDot11FilterMacAddress": rcDot11FilterMacAddress,
       "rcDot11RowStatus": rcDot11RowStatus,
       "rcDot11DhcpParams": rcDot11DhcpParams,
       "rcDot11DhcpServerEnable": rcDot11DhcpServerEnable,
       "rcDot11DhcpStartOfPool": rcDot11DhcpStartOfPool,
       "rcDot11DhcpIpPoolSize": rcDot11DhcpIpPoolSize,
       "rcDot11DhcpSubnet": rcDot11DhcpSubnet,
       "rcDot11DhcpGateway": rcDot11DhcpGateway,
       "rcDot11DhcpDnsIpAddress": rcDot11DhcpDnsIpAddress,
       "rcDot11DhcpLeaseTime": rcDot11DhcpLeaseTime,
       "rcDot11AssociationInfo": rcDot11AssociationInfo,
       "rcDot11AssociationTable": rcDot11AssociationTable,
       "rcDot11AssociationEntry": rcDot11AssociationEntry,
       "rcDot11AssociationMac": rcDot11AssociationMac,
       "rcDot11AssociationChannel": rcDot11AssociationChannel,
       "rcDot11AssociationRate": rcDot11AssociationRate,
       "rcDot11AssociationRssi": rcDot11AssociationRssi,
       "rcDot11AssociationTxSeq": rcDot11AssociationTxSeq,
       "rcDot11AssociationRxSeq": rcDot11AssociationRxSeq,
       "rcDot11AssociationSecurity": rcDot11AssociationSecurity,
       "rcDot11Conformance": rcDot11Conformance,
       "rcDot11Groups": rcDot11Groups,
       "rcDot11GlobalParamsGroup": rcDot11GlobalParamsGroup,
       "rcDot11NetworkParamsGroup": rcDot11NetworkParamsGroup,
       "rcDot11SecurityParamsGroup": rcDot11SecurityParamsGroup,
       "rcDot11DhcpParamsGroup": rcDot11DhcpParamsGroup,
       "rcDot11MacFilteringTableGroup": rcDot11MacFilteringTableGroup,
       "rcDot11AssociationTableGroup": rcDot11AssociationTableGroup}
)
