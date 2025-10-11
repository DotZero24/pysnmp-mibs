# SNMP MIB module (ACKSYS-WLG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/acksys/ACKSYS-WLG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:17 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

acksysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 2)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Acksys_ObjectIdentity = ObjectIdentity
acksys = _Acksys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097)
)
_Network_product_ObjectIdentity = ObjectIdentity
network_product = _Network_product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1)
)
_WifiInterface_ObjectIdentity = ObjectIdentity
wifiInterface = _WifiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1)
)


class _SettingInterfaceSsid_Type(DisplayString):
    """Custom type settingInterfaceSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SettingInterfaceSsid_Type.__name__ = "DisplayString"
_SettingInterfaceSsid_Object = MibScalar
settingInterfaceSsid = _SettingInterfaceSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 1),
    _SettingInterfaceSsid_Type()
)
settingInterfaceSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingInterfaceSsid.setStatus("current")


class _SettingInterfaceWifiMode_Type(Integer32):
    """Custom type settingInterfaceWifiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("access-point", 2))
    )


_SettingInterfaceWifiMode_Type.__name__ = "Integer32"
_SettingInterfaceWifiMode_Object = MibScalar
settingInterfaceWifiMode = _SettingInterfaceWifiMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 2),
    _SettingInterfaceWifiMode_Type()
)
settingInterfaceWifiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingInterfaceWifiMode.setStatus("current")
_SettingInterfaceChannel_Type = Integer32
_SettingInterfaceChannel_Object = MibScalar
settingInterfaceChannel = _SettingInterfaceChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 3),
    _SettingInterfaceChannel_Type()
)
settingInterfaceChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingInterfaceChannel.setStatus("current")


class _SettingInterface80211Mode_Type(Integer32):
    """Custom type settingInterface80211Mode based on Integer32"""
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
        *(("b-only", 1),
          ("g-only", 2),
          ("mixed-b-g", 3),
          ("a-only", 4))
    )


_SettingInterface80211Mode_Type.__name__ = "Integer32"
_SettingInterface80211Mode_Object = MibScalar
settingInterface80211Mode = _SettingInterface80211Mode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 4),
    _SettingInterface80211Mode_Type()
)
settingInterface80211Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingInterface80211Mode.setStatus("current")


class _SettingInterfaceSuper_a_g_Mode_Type(Integer32):
    """Custom type settingInterfaceSuper_a_g_Mode based on Integer32"""
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
        *(("disable", 1),
          ("super-g-without-turbo", 2),
          ("super-g-with-static-turbo", 3),
          ("super-g-with-dynamic-turbo", 4))
    )


_SettingInterfaceSuper_a_g_Mode_Type.__name__ = "Integer32"
_SettingInterfaceSuper_a_g_Mode_Object = MibScalar
settingInterfaceSuper_a_g_Mode = _SettingInterfaceSuper_a_g_Mode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 5),
    _SettingInterfaceSuper_a_g_Mode_Type()
)
settingInterfaceSuper_a_g_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingInterfaceSuper_a_g_Mode.setStatus("current")


class _SettingEnableRadio_Type(Integer32):
    """Custom type settingEnableRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SettingEnableRadio_Type.__name__ = "Integer32"
_SettingEnableRadio_Object = MibScalar
settingEnableRadio = _SettingEnableRadio_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 6),
    _SettingEnableRadio_Type()
)
settingEnableRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingEnableRadio.setStatus("current")


class _SettingTxPoxer_Type(Integer32):
    """Custom type settingTxPoxer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("low", 3))
    )


_SettingTxPoxer_Type.__name__ = "Integer32"
_SettingTxPoxer_Object = MibScalar
settingTxPoxer = _SettingTxPoxer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 7),
    _SettingTxPoxer_Type()
)
settingTxPoxer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingTxPoxer.setStatus("current")


class _SettingRegion_Type(Integer32):
    """Custom type settingRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              6,
              7,
              10,
              14,
              17,
              18,
              20,
              21,
              22,
              23,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("israel", 2),
          ("usa", 4),
          ("hong-kong", 5),
          ("canada", 6),
          ("australia", 7),
          ("franceoutdoor", 10),
          ("europe", 14),
          ("japan", 17),
          ("singapore", 18),
          ("korea", 20),
          ("mexico", 21),
          ("indonesia", 22),
          ("china", 23),
          ("russia", 27),
          ("brazil", 28),
          ("chile", 29),
          ("thailand", 30),
          ("peru", 31))
    )


_SettingRegion_Type.__name__ = "Integer32"
_SettingRegion_Object = MibScalar
settingRegion = _SettingRegion_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 8),
    _SettingRegion_Type()
)
settingRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingRegion.setStatus("current")
_SecuritySettings_ObjectIdentity = ObjectIdentity
securitySettings = _SecuritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9)
)


class _SecurityMode_Type(Integer32):
    """Custom type securityMode based on Integer32"""
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
        *(("none", 1),
          ("wep", 2),
          ("wpa-wpa2-psk", 3),
          ("wpa-wpa2", 4))
    )


_SecurityMode_Type.__name__ = "Integer32"
_SecurityMode_Object = MibScalar
securityMode = _SecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 1),
    _SecurityMode_Type()
)
securityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMode.setStatus("current")
_SecurityWEP_ObjectIdentity = ObjectIdentity
securityWEP = _SecurityWEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2)
)
_SecurityModeWepKeyLen_Type = Integer32
_SecurityModeWepKeyLen_Object = MibScalar
securityModeWepKeyLen = _SecurityModeWepKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 1),
    _SecurityModeWepKeyLen_Type()
)
securityModeWepKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKeyLen.setStatus("current")


class _SecurityModeWepKey_1_Type(OctetString):
    """Custom type securityModeWepKey_1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_SecurityModeWepKey_1_Type.__name__ = "OctetString"
_SecurityModeWepKey_1_Object = MibScalar
securityModeWepKey_1 = _SecurityModeWepKey_1_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 2),
    _SecurityModeWepKey_1_Type()
)
securityModeWepKey_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_1.setStatus("current")


class _SecurityModeWepKey_2_Type(OctetString):
    """Custom type securityModeWepKey_2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_SecurityModeWepKey_2_Type.__name__ = "OctetString"
_SecurityModeWepKey_2_Object = MibScalar
securityModeWepKey_2 = _SecurityModeWepKey_2_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 3),
    _SecurityModeWepKey_2_Type()
)
securityModeWepKey_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_2.setStatus("current")


class _SecurityModeWepKey_3_Type(OctetString):
    """Custom type securityModeWepKey_3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_SecurityModeWepKey_3_Type.__name__ = "OctetString"
_SecurityModeWepKey_3_Object = MibScalar
securityModeWepKey_3 = _SecurityModeWepKey_3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 4),
    _SecurityModeWepKey_3_Type()
)
securityModeWepKey_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_3.setStatus("current")


class _SecurityModeWepKey_4_Type(OctetString):
    """Custom type securityModeWepKey_4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_SecurityModeWepKey_4_Type.__name__ = "OctetString"
_SecurityModeWepKey_4_Object = MibScalar
securityModeWepKey_4 = _SecurityModeWepKey_4_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 5),
    _SecurityModeWepKey_4_Type()
)
securityModeWepKey_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_4.setStatus("current")
_SecurityModeDefaultWepKey_Type = Integer32
_SecurityModeDefaultWepKey_Object = MibScalar
securityModeDefaultWepKey = _SecurityModeDefaultWepKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 6),
    _SecurityModeDefaultWepKey_Type()
)
securityModeDefaultWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeDefaultWepKey.setStatus("current")


class _SecurityModeWepAuthentication_Type(Integer32):
    """Custom type securityModeWepAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared", 2))
    )


_SecurityModeWepAuthentication_Type.__name__ = "Integer32"
_SecurityModeWepAuthentication_Object = MibScalar
securityModeWepAuthentication = _SecurityModeWepAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 7),
    _SecurityModeWepAuthentication_Type()
)
securityModeWepAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepAuthentication.setStatus("current")
_SecurityWPA_WPA2_ObjectIdentity = ObjectIdentity
securityWPA_WPA2 = _SecurityWPA_WPA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3)
)
_SecurityPresharedKey_ObjectIdentity = ObjectIdentity
securityPresharedKey = _SecurityPresharedKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 1)
)


class _SecurityModeWpaPresharedKey_Type(OctetString):
    """Custom type securityModeWpaPresharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_SecurityModeWpaPresharedKey_Type.__name__ = "OctetString"
_SecurityModeWpaPresharedKey_Object = MibScalar
securityModeWpaPresharedKey = _SecurityModeWpaPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 1, 1),
    _SecurityModeWpaPresharedKey_Type()
)
securityModeWpaPresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWpaPresharedKey.setStatus("current")
_SecurityRadius_ObjectIdentity = ObjectIdentity
securityRadius = _SecurityRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2)
)
_SecurityModeWPARadiusAuthenticationTimeout_Type = Integer32
_SecurityModeWPARadiusAuthenticationTimeout_Object = MibScalar
securityModeWPARadiusAuthenticationTimeout = _SecurityModeWPARadiusAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 1),
    _SecurityModeWPARadiusAuthenticationTimeout_Type()
)
securityModeWPARadiusAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAuthenticationTimeout.setStatus("obsolete")
_SecurityModeWPARadiusIP_Type = IpAddress
_SecurityModeWPARadiusIP_Object = MibScalar
securityModeWPARadiusIP = _SecurityModeWPARadiusIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 2),
    _SecurityModeWPARadiusIP_Type()
)
securityModeWPARadiusIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusIP.setStatus("obsolete")
_SecurityModeWPARadiusPort_Type = Integer32
_SecurityModeWPARadiusPort_Object = MibScalar
securityModeWPARadiusPort = _SecurityModeWPARadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 3),
    _SecurityModeWPARadiusPort_Type()
)
securityModeWPARadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusPort.setStatus("obsolete")


class _SecurityModeWPARadiusSecret_Type(OctetString):
    """Custom type securityModeWPARadiusSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusSecret_Type.__name__ = "OctetString"
_SecurityModeWPARadiusSecret_Object = MibScalar
securityModeWPARadiusSecret = _SecurityModeWPARadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 4),
    _SecurityModeWPARadiusSecret_Type()
)
securityModeWPARadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusSecret.setStatus("obsolete")


class _SecurityModeWPARadiusMacAddressAuthentication_Type(Integer32):
    """Custom type securityModeWPARadiusMacAddressAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityModeWPARadiusMacAddressAuthentication_Type.__name__ = "Integer32"
_SecurityModeWPARadiusMacAddressAuthentication_Object = MibScalar
securityModeWPARadiusMacAddressAuthentication = _SecurityModeWPARadiusMacAddressAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 5),
    _SecurityModeWPARadiusMacAddressAuthentication_Type()
)
securityModeWPARadiusMacAddressAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusMacAddressAuthentication.setStatus("obsolete")
_SecurityRadiusAP_ObjectIdentity = ObjectIdentity
securityRadiusAP = _SecurityRadiusAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6)
)
_SecurityModeWPARadiusAPAuthenticationTimeout_Type = Integer32
_SecurityModeWPARadiusAPAuthenticationTimeout_Object = MibScalar
securityModeWPARadiusAPAuthenticationTimeout = _SecurityModeWPARadiusAPAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 1),
    _SecurityModeWPARadiusAPAuthenticationTimeout_Type()
)
securityModeWPARadiusAPAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAPAuthenticationTimeout.setStatus("current")
_SecurityModeWPARadiusAPIP_Type = IpAddress
_SecurityModeWPARadiusAPIP_Object = MibScalar
securityModeWPARadiusAPIP = _SecurityModeWPARadiusAPIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 2),
    _SecurityModeWPARadiusAPIP_Type()
)
securityModeWPARadiusAPIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAPIP.setStatus("current")
_SecurityModeWPARadiusAPPort_Type = Integer32
_SecurityModeWPARadiusAPPort_Object = MibScalar
securityModeWPARadiusAPPort = _SecurityModeWPARadiusAPPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 3),
    _SecurityModeWPARadiusAPPort_Type()
)
securityModeWPARadiusAPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAPPort.setStatus("current")


class _SecurityModeWPARadiusAPSecret_Type(OctetString):
    """Custom type securityModeWPARadiusAPSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusAPSecret_Type.__name__ = "OctetString"
_SecurityModeWPARadiusAPSecret_Object = MibScalar
securityModeWPARadiusAPSecret = _SecurityModeWPARadiusAPSecret_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 4),
    _SecurityModeWPARadiusAPSecret_Type()
)
securityModeWPARadiusAPSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAPSecret.setStatus("current")


class _SecurityModeWPARadiusAPMacAddressAuthentication_Type(Integer32):
    """Custom type securityModeWPARadiusAPMacAddressAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityModeWPARadiusAPMacAddressAuthentication_Type.__name__ = "Integer32"
_SecurityModeWPARadiusAPMacAddressAuthentication_Object = MibScalar
securityModeWPARadiusAPMacAddressAuthentication = _SecurityModeWPARadiusAPMacAddressAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 5),
    _SecurityModeWPARadiusAPMacAddressAuthentication_Type()
)
securityModeWPARadiusAPMacAddressAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusAPMacAddressAuthentication.setStatus("current")
_SecurityRadiusAPBackup_ObjectIdentity = ObjectIdentity
securityRadiusAPBackup = _SecurityRadiusAPBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 6)
)
_SecurityModeWPABackupRadiusAPIP_Type = IpAddress
_SecurityModeWPABackupRadiusAPIP_Object = MibScalar
securityModeWPABackupRadiusAPIP = _SecurityModeWPABackupRadiusAPIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 6, 1),
    _SecurityModeWPABackupRadiusAPIP_Type()
)
securityModeWPABackupRadiusAPIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPABackupRadiusAPIP.setStatus("current")
_SecurityModeWPARadiusBackupAPPort_Type = Integer32
_SecurityModeWPARadiusBackupAPPort_Object = MibScalar
securityModeWPARadiusBackupAPPort = _SecurityModeWPARadiusBackupAPPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 6, 2),
    _SecurityModeWPARadiusBackupAPPort_Type()
)
securityModeWPARadiusBackupAPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusBackupAPPort.setStatus("current")


class _SecurityModeWPARadiusBackupAPSecret_Type(OctetString):
    """Custom type securityModeWPARadiusBackupAPSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusBackupAPSecret_Type.__name__ = "OctetString"
_SecurityModeWPARadiusBackupAPSecret_Object = MibScalar
securityModeWPARadiusBackupAPSecret = _SecurityModeWPARadiusBackupAPSecret_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 6, 3),
    _SecurityModeWPARadiusBackupAPSecret_Type()
)
securityModeWPARadiusBackupAPSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusBackupAPSecret.setStatus("current")


class _SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type(Integer32):
    """Custom type securityModeWPABackupRadiusAPMacAddressAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type.__name__ = "Integer32"
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object = MibScalar
securityModeWPABackupRadiusAPMacAddressAuthentication = _SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 6, 6, 4),
    _SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type()
)
securityModeWPABackupRadiusAPMacAddressAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPABackupRadiusAPMacAddressAuthentication.setStatus("current")
_SecurityRadiusBridge_ObjectIdentity = ObjectIdentity
securityRadiusBridge = _SecurityRadiusBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 7)
)


class _SecurityModeWPARadiusLogin_Type(OctetString):
    """Custom type securityModeWPARadiusLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusLogin_Type.__name__ = "OctetString"
_SecurityModeWPARadiusLogin_Object = MibScalar
securityModeWPARadiusLogin = _SecurityModeWPARadiusLogin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 7, 1),
    _SecurityModeWPARadiusLogin_Type()
)
securityModeWPARadiusLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusLogin.setStatus("current")


class _SecurityModeWPARadiusPassword_Type(OctetString):
    """Custom type securityModeWPARadiusPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusPassword_Type.__name__ = "OctetString"
_SecurityModeWPARadiusPassword_Object = MibScalar
securityModeWPARadiusPassword = _SecurityModeWPARadiusPassword_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 2, 7, 2),
    _SecurityModeWPARadiusPassword_Type()
)
securityModeWPARadiusPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusPassword.setStatus("current")
_SecurityBackupRadius_ObjectIdentity = ObjectIdentity
securityBackupRadius = _SecurityBackupRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 3)
)
_SecurityModeWPABackupRadiusIP_Type = IpAddress
_SecurityModeWPABackupRadiusIP_Object = MibScalar
securityModeWPABackupRadiusIP = _SecurityModeWPABackupRadiusIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 3, 1),
    _SecurityModeWPABackupRadiusIP_Type()
)
securityModeWPABackupRadiusIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPABackupRadiusIP.setStatus("obsolete")
_SecurityModeWPARadiusBackupPort_Type = Integer32
_SecurityModeWPARadiusBackupPort_Object = MibScalar
securityModeWPARadiusBackupPort = _SecurityModeWPARadiusBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 3, 2),
    _SecurityModeWPARadiusBackupPort_Type()
)
securityModeWPARadiusBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusBackupPort.setStatus("obsolete")


class _SecurityModeWPARadiusBackupSecret_Type(OctetString):
    """Custom type securityModeWPARadiusBackupSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityModeWPARadiusBackupSecret_Type.__name__ = "OctetString"
_SecurityModeWPARadiusBackupSecret_Object = MibScalar
securityModeWPARadiusBackupSecret = _SecurityModeWPARadiusBackupSecret_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 3, 3),
    _SecurityModeWPARadiusBackupSecret_Type()
)
securityModeWPARadiusBackupSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPARadiusBackupSecret.setStatus("obsolete")


class _SecurityModeWPABackupRadiusMacAddressAuthentication_Type(Integer32):
    """Custom type securityModeWPABackupRadiusMacAddressAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityModeWPABackupRadiusMacAddressAuthentication_Type.__name__ = "Integer32"
_SecurityModeWPABackupRadiusMacAddressAuthentication_Object = MibScalar
securityModeWPABackupRadiusMacAddressAuthentication = _SecurityModeWPABackupRadiusMacAddressAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 3, 4),
    _SecurityModeWPABackupRadiusMacAddressAuthentication_Type()
)
securityModeWPABackupRadiusMacAddressAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWPABackupRadiusMacAddressAuthentication.setStatus("obsolete")


class _SecurityModeWpaMode_Type(Integer32):
    """Custom type securityModeWpaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wpa", 1),
          ("wpa2", 2))
    )


_SecurityModeWpaMode_Type.__name__ = "Integer32"
_SecurityModeWpaMode_Object = MibScalar
securityModeWpaMode = _SecurityModeWpaMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 4),
    _SecurityModeWpaMode_Type()
)
securityModeWpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWpaMode.setStatus("current")


class _SecurityModeWpaCipherType_Type(Integer32):
    """Custom type securityModeWpaCipherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2))
    )


_SecurityModeWpaCipherType_Type.__name__ = "Integer32"
_SecurityModeWpaCipherType_Object = MibScalar
securityModeWpaCipherType = _SecurityModeWpaCipherType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 5),
    _SecurityModeWpaCipherType_Type()
)
securityModeWpaCipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWpaCipherType.setStatus("current")
_SecurityModeWpaKeyUpdateInterval_Type = Integer32
_SecurityModeWpaKeyUpdateInterval_Object = MibScalar
securityModeWpaKeyUpdateInterval = _SecurityModeWpaKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 3, 6),
    _SecurityModeWpaKeyUpdateInterval_Type()
)
securityModeWpaKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWpaKeyUpdateInterval.setStatus("current")


class _SettingAntennaChoice_Type(Integer32):
    """Custom type settingAntennaChoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 1),
          ("main", 2),
          ("aux", 3))
    )


_SettingAntennaChoice_Type.__name__ = "Integer32"
_SettingAntennaChoice_Object = MibScalar
settingAntennaChoice = _SettingAntennaChoice_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 10),
    _SettingAntennaChoice_Type()
)
settingAntennaChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingAntennaChoice.setStatus("current")
_SettingTransmisionRate_Type = Integer32
_SettingTransmisionRate_Object = MibScalar
settingTransmisionRate = _SettingTransmisionRate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 11),
    _SettingTransmisionRate_Type()
)
settingTransmisionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingTransmisionRate.setStatus("current")


class _SettingFlagUdapnopassword_Type(Integer32):
    """Custom type settingFlagUdapnopassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SettingFlagUdapnopassword_Type.__name__ = "Integer32"
_SettingFlagUdapnopassword_Object = MibScalar
settingFlagUdapnopassword = _SettingFlagUdapnopassword_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 12),
    _SettingFlagUdapnopassword_Type()
)
settingFlagUdapnopassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingFlagUdapnopassword.setStatus("current")


class _SettingFlagFiltersamenet_Type(Integer32):
    """Custom type settingFlagFiltersamenet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("different-subnet-filter", 2),
          ("custom-subnet-filter", 3))
    )


_SettingFlagFiltersamenet_Type.__name__ = "Integer32"
_SettingFlagFiltersamenet_Object = MibScalar
settingFlagFiltersamenet = _SettingFlagFiltersamenet_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 13),
    _SettingFlagFiltersamenet_Type()
)
settingFlagFiltersamenet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingFlagFiltersamenet.setStatus("current")


class _SettingFlagFilterframecosom_Type(Integer32):
    """Custom type settingFlagFilterframecosom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SettingFlagFilterframecosom_Type.__name__ = "Integer32"
_SettingFlagFilterframecosom_Object = MibScalar
settingFlagFilterframecosom = _SettingFlagFilterframecosom_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 14),
    _SettingFlagFilterframecosom_Type()
)
settingFlagFilterframecosom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingFlagFilterframecosom.setStatus("current")


class _SettingDFSsupport_Type(Integer32):
    """Custom type settingDFSsupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SettingDFSsupport_Type.__name__ = "Integer32"
_SettingDFSsupport_Object = MibScalar
settingDFSsupport = _SettingDFSsupport_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 15),
    _SettingDFSsupport_Type()
)
settingDFSsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingDFSsupport.setStatus("current")
_SettingFilterCustomIpAddr_Type = IpAddress
_SettingFilterCustomIpAddr_Object = MibScalar
settingFilterCustomIpAddr = _SettingFilterCustomIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 16),
    _SettingFilterCustomIpAddr_Type()
)
settingFilterCustomIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingFilterCustomIpAddr.setStatus("current")
_SettingFilterCustomSubnetMask_Type = IpAddress
_SettingFilterCustomSubnetMask_Object = MibScalar
settingFilterCustomSubnetMask = _SettingFilterCustomSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 17),
    _SettingFilterCustomSubnetMask_Type()
)
settingFilterCustomSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingFilterCustomSubnetMask.setStatus("current")
_Bridge_mode_ObjectIdentity = ObjectIdentity
bridge_mode = _Bridge_mode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2)
)


class _Bridge_modeLinkStatus_Type(Integer32):
    """Custom type bridge_modeLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Bridge_modeLinkStatus_Type.__name__ = "Integer32"
_Bridge_modeLinkStatus_Object = MibScalar
bridge_modeLinkStatus = _Bridge_modeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 1),
    _Bridge_modeLinkStatus_Type()
)
bridge_modeLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeLinkStatus.setStatus("current")
_Bridge_modeMacAP_Type = PhysAddress
_Bridge_modeMacAP_Object = MibScalar
bridge_modeMacAP = _Bridge_modeMacAP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 2),
    _Bridge_modeMacAP_Type()
)
bridge_modeMacAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeMacAP.setStatus("current")
_Bridge_modeRSSI_Type = Gauge32
_Bridge_modeRSSI_Object = MibScalar
bridge_modeRSSI = _Bridge_modeRSSI_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 3),
    _Bridge_modeRSSI_Type()
)
bridge_modeRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeRSSI.setStatus("current")
_Bridge_modeRSSIdBm_Type = Gauge32
_Bridge_modeRSSIdBm_Object = MibScalar
bridge_modeRSSIdBm = _Bridge_modeRSSIdBm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 4),
    _Bridge_modeRSSIdBm_Type()
)
bridge_modeRSSIdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeRSSIdBm.setStatus("current")
_Bridge_modeRSSIPercent_Type = Gauge32
_Bridge_modeRSSIPercent_Object = MibScalar
bridge_modeRSSIPercent = _Bridge_modeRSSIPercent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 5),
    _Bridge_modeRSSIPercent_Type()
)
bridge_modeRSSIPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeRSSIPercent.setStatus("current")
_Bridge_modeCurrentTxRate_Type = Integer32
_Bridge_modeCurrentTxRate_Object = MibScalar
bridge_modeCurrentTxRate = _Bridge_modeCurrentTxRate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 6),
    _Bridge_modeCurrentTxRate_Type()
)
bridge_modeCurrentTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridge_modeCurrentTxRate.setStatus("current")


class _Bridge_WirelessMode_Type(Integer32):
    """Custom type bridge_WirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 1),
          ("ad-hoc", 2))
    )


_Bridge_WirelessMode_Type.__name__ = "Integer32"
_Bridge_WirelessMode_Object = MibScalar
bridge_WirelessMode = _Bridge_WirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 7),
    _Bridge_WirelessMode_Type()
)
bridge_WirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridge_WirelessMode.setStatus("current")
_BridgeAPFiltering_ObjectIdentity = ObjectIdentity
bridgeAPFiltering = _BridgeAPFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8)
)


class _BridgeAPFilteringEnable_Type(Integer32):
    """Custom type bridgeAPFilteringEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BridgeAPFilteringEnable_Type.__name__ = "Integer32"
_BridgeAPFilteringEnable_Object = MibScalar
bridgeAPFilteringEnable = _BridgeAPFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 1),
    _BridgeAPFilteringEnable_Type()
)
bridgeAPFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringEnable.setStatus("current")


class _BridgeAPFilteringMode_Type(Integer32):
    """Custom type bridgeAPFilteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_BridgeAPFilteringMode_Type.__name__ = "Integer32"
_BridgeAPFilteringMode_Object = MibScalar
bridgeAPFilteringMode = _BridgeAPFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 2),
    _BridgeAPFilteringMode_Type()
)
bridgeAPFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringMode.setStatus("current")
_BridgeAPFilteringMACAddress_Type = PhysAddress
_BridgeAPFilteringMACAddress_Object = MibScalar
bridgeAPFilteringMACAddress = _BridgeAPFilteringMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 3),
    _BridgeAPFilteringMACAddress_Type()
)
bridgeAPFilteringMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringMACAddress.setStatus("current")


class _BridgeAPFilteringName_Type(OctetString):
    """Custom type bridgeAPFilteringName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BridgeAPFilteringName_Type.__name__ = "OctetString"
_BridgeAPFilteringName_Object = MibScalar
bridgeAPFilteringName = _BridgeAPFilteringName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 4),
    _BridgeAPFilteringName_Type()
)
bridgeAPFilteringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringName.setStatus("current")
_BridgeAPFilteringSave_Type = Integer32
_BridgeAPFilteringSave_Object = MibScalar
bridgeAPFilteringSave = _BridgeAPFilteringSave_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 5),
    _BridgeAPFilteringSave_Type()
)
bridgeAPFilteringSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringSave.setStatus("current")
_BridgeAPFilteringDelete_Type = Integer32
_BridgeAPFilteringDelete_Object = MibScalar
bridgeAPFilteringDelete = _BridgeAPFilteringDelete_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 6),
    _BridgeAPFilteringDelete_Type()
)
bridgeAPFilteringDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringDelete.setStatus("current")
_BridgeAPFilteringEnableRule_Type = Integer32
_BridgeAPFilteringEnableRule_Object = MibScalar
bridgeAPFilteringEnableRule = _BridgeAPFilteringEnableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 7),
    _BridgeAPFilteringEnableRule_Type()
)
bridgeAPFilteringEnableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringEnableRule.setStatus("current")
_BridgeAPFilteringDisableRule_Type = Integer32
_BridgeAPFilteringDisableRule_Object = MibScalar
bridgeAPFilteringDisableRule = _BridgeAPFilteringDisableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 8),
    _BridgeAPFilteringDisableRule_Type()
)
bridgeAPFilteringDisableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAPFilteringDisableRule.setStatus("current")
_BridgeAPFilteringTable_Object = MibTable
bridgeAPFilteringTable = _BridgeAPFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9)
)
if mibBuilder.loadTexts:
    bridgeAPFilteringTable.setStatus("current")
_BridgeAPFilteringEntry_Object = MibTableRow
bridgeAPFilteringEntry = _BridgeAPFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9, 1)
)
bridgeAPFilteringEntry.setIndexNames(
    (0, "ACKSYS-WLG-MIB", "bridgeAPFilteringListId"),
)
if mibBuilder.loadTexts:
    bridgeAPFilteringEntry.setStatus("current")
_BridgeAPFilteringListId_Type = Integer32
_BridgeAPFilteringListId_Object = MibTableColumn
bridgeAPFilteringListId = _BridgeAPFilteringListId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9, 1, 1),
    _BridgeAPFilteringListId_Type()
)
bridgeAPFilteringListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAPFilteringListId.setStatus("current")


class _BridgeAPFilteringListName_Type(OctetString):
    """Custom type bridgeAPFilteringListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BridgeAPFilteringListName_Type.__name__ = "OctetString"
_BridgeAPFilteringListName_Object = MibTableColumn
bridgeAPFilteringListName = _BridgeAPFilteringListName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9, 1, 2),
    _BridgeAPFilteringListName_Type()
)
bridgeAPFilteringListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAPFilteringListName.setStatus("current")
_BridgeAPFilteringListMAC_Type = PhysAddress
_BridgeAPFilteringListMAC_Object = MibTableColumn
bridgeAPFilteringListMAC = _BridgeAPFilteringListMAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9, 1, 3),
    _BridgeAPFilteringListMAC_Type()
)
bridgeAPFilteringListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAPFilteringListMAC.setStatus("current")


class _BridgeAPFilteringListEnable_Type(Integer32):
    """Custom type bridgeAPFilteringListEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BridgeAPFilteringListEnable_Type.__name__ = "Integer32"
_BridgeAPFilteringListEnable_Object = MibTableColumn
bridgeAPFilteringListEnable = _BridgeAPFilteringListEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 8, 9, 1, 4),
    _BridgeAPFilteringListEnable_Type()
)
bridgeAPFilteringListEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAPFilteringListEnable.setStatus("current")
_BridgeRoaming_ObjectIdentity = ObjectIdentity
bridgeRoaming = _BridgeRoaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9)
)
_BridgeRoamingAdvanced_ObjectIdentity = ObjectIdentity
bridgeRoamingAdvanced = _BridgeRoamingAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1)
)
_BridgeRoamingAdvancedScanThreshold_dbm_Type = Integer32
_BridgeRoamingAdvancedScanThreshold_dbm_Object = MibScalar
bridgeRoamingAdvancedScanThreshold_dbm = _BridgeRoamingAdvancedScanThreshold_dbm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1, 1),
    _BridgeRoamingAdvancedScanThreshold_dbm_Type()
)
bridgeRoamingAdvancedScanThreshold_dbm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingAdvancedScanThreshold_dbm.setStatus("current")
_BridgeRoamingAdvancedScanThreshold_percent_Type = Integer32
_BridgeRoamingAdvancedScanThreshold_percent_Object = MibScalar
bridgeRoamingAdvancedScanThreshold_percent = _BridgeRoamingAdvancedScanThreshold_percent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1, 2),
    _BridgeRoamingAdvancedScanThreshold_percent_Type()
)
bridgeRoamingAdvancedScanThreshold_percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingAdvancedScanThreshold_percent.setStatus("current")
_BridgeRoamingAdvancedScanPeriod_Type = Integer32
_BridgeRoamingAdvancedScanPeriod_Object = MibScalar
bridgeRoamingAdvancedScanPeriod = _BridgeRoamingAdvancedScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1, 3),
    _BridgeRoamingAdvancedScanPeriod_Type()
)
bridgeRoamingAdvancedScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingAdvancedScanPeriod.setStatus("current")
_BridgeRoamingAdvancedScanDuration_Type = Integer32
_BridgeRoamingAdvancedScanDuration_Object = MibScalar
bridgeRoamingAdvancedScanDuration = _BridgeRoamingAdvancedScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1, 4),
    _BridgeRoamingAdvancedScanDuration_Type()
)
bridgeRoamingAdvancedScanDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingAdvancedScanDuration.setStatus("current")
_BridgeRoamingAdvancedAPLossDetection_Type = Integer32
_BridgeRoamingAdvancedAPLossDetection_Object = MibScalar
bridgeRoamingAdvancedAPLossDetection = _BridgeRoamingAdvancedAPLossDetection_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 1, 5),
    _BridgeRoamingAdvancedAPLossDetection_Type()
)
bridgeRoamingAdvancedAPLossDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingAdvancedAPLossDetection.setStatus("current")


class _BridgeRoamingEnable_Type(Integer32):
    """Custom type bridgeRoamingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BridgeRoamingEnable_Type.__name__ = "Integer32"
_BridgeRoamingEnable_Object = MibScalar
bridgeRoamingEnable = _BridgeRoamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 2),
    _BridgeRoamingEnable_Type()
)
bridgeRoamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingEnable.setStatus("current")
_BridgeRoamingRSSIThreshold_dBm_Type = Integer32
_BridgeRoamingRSSIThreshold_dBm_Object = MibScalar
bridgeRoamingRSSIThreshold_dBm = _BridgeRoamingRSSIThreshold_dBm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 3),
    _BridgeRoamingRSSIThreshold_dBm_Type()
)
bridgeRoamingRSSIThreshold_dBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingRSSIThreshold_dBm.setStatus("current")
_BridgeRoamingRSSIThreshold_percent_Type = Integer32
_BridgeRoamingRSSIThreshold_percent_Object = MibScalar
bridgeRoamingRSSIThreshold_percent = _BridgeRoamingRSSIThreshold_percent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 9, 4),
    _BridgeRoamingRSSIThreshold_percent_Type()
)
bridgeRoamingRSSIThreshold_percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRoamingRSSIThreshold_percent.setStatus("current")


class _BridgeChannelList_Type(OctetString):
    """Custom type bridgeChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_BridgeChannelList_Type.__name__ = "OctetString"
_BridgeChannelList_Object = MibScalar
bridgeChannelList = _BridgeChannelList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 10),
    _BridgeChannelList_Type()
)
bridgeChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeChannelList.setStatus("current")
_BridgeWirelessScan_ObjectIdentity = ObjectIdentity
bridgeWirelessScan = _BridgeWirelessScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11)
)
_BridgeWileressScanTable_Object = MibTable
bridgeWileressScanTable = _BridgeWileressScanTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    bridgeWileressScanTable.setStatus("current")
_BridgeWirelessScanEntry_Object = MibTableRow
bridgeWirelessScanEntry = _BridgeWirelessScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1)
)
bridgeWirelessScanEntry.setIndexNames(
    (0, "ACKSYS-WLG-MIB", "apClientFilteringListId"),
)
if mibBuilder.loadTexts:
    bridgeWirelessScanEntry.setStatus("current")
_BridgeWirelessScanAPMac_Type = PhysAddress
_BridgeWirelessScanAPMac_Object = MibTableColumn
bridgeWirelessScanAPMac = _BridgeWirelessScanAPMac_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 1),
    _BridgeWirelessScanAPMac_Type()
)
bridgeWirelessScanAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanAPMac.setStatus("current")


class _BridgeWirelessScanSSID_Type(DisplayString):
    """Custom type bridgeWirelessScanSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_BridgeWirelessScanSSID_Type.__name__ = "DisplayString"
_BridgeWirelessScanSSID_Object = MibTableColumn
bridgeWirelessScanSSID = _BridgeWirelessScanSSID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 2),
    _BridgeWirelessScanSSID_Type()
)
bridgeWirelessScanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanSSID.setStatus("current")
_BridgeWirelessScanChannel_Type = Integer32
_BridgeWirelessScanChannel_Object = MibTableColumn
bridgeWirelessScanChannel = _BridgeWirelessScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 3),
    _BridgeWirelessScanChannel_Type()
)
bridgeWirelessScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanChannel.setStatus("current")


class _BridgeWirelessScanMode_Type(Integer32):
    """Custom type bridgeWirelessScanMode based on Integer32"""
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
        *(("b-only", 1),
          ("g-only", 2),
          ("mixed-b-g", 3),
          ("a-only", 4))
    )


_BridgeWirelessScanMode_Type.__name__ = "Integer32"
_BridgeWirelessScanMode_Object = MibTableColumn
bridgeWirelessScanMode = _BridgeWirelessScanMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 4),
    _BridgeWirelessScanMode_Type()
)
bridgeWirelessScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanMode.setStatus("current")


class _BridgeWirelessScanSecurity_Type(Integer32):
    """Custom type bridgeWirelessScanSecurity based on Integer32"""
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
          ("wep", 1),
          ("wpa", 2))
    )


_BridgeWirelessScanSecurity_Type.__name__ = "Integer32"
_BridgeWirelessScanSecurity_Object = MibTableColumn
bridgeWirelessScanSecurity = _BridgeWirelessScanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 5),
    _BridgeWirelessScanSecurity_Type()
)
bridgeWirelessScanSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanSecurity.setStatus("current")
_BridgeWirelessScanRssi_Type = Integer32
_BridgeWirelessScanRssi_Object = MibTableColumn
bridgeWirelessScanRssi = _BridgeWirelessScanRssi_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 11, 1, 1, 6),
    _BridgeWirelessScanRssi_Type()
)
bridgeWirelessScanRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeWirelessScanRssi.setStatus("current")
_BridgeNAT_ObjectIdentity = ObjectIdentity
bridgeNAT = _BridgeNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12)
)


class _BrigeNATStatus_Type(Integer32):
    """Custom type brigeNATStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrigeNATStatus_Type.__name__ = "Integer32"
_BrigeNATStatus_Object = MibScalar
brigeNATStatus = _BrigeNATStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 1),
    _BrigeNATStatus_Type()
)
brigeNATStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATStatus.setStatus("current")


class _BrigeNATEnablePing_Type(Integer32):
    """Custom type brigeNATEnablePing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrigeNATEnablePing_Type.__name__ = "Integer32"
_BrigeNATEnablePing_Object = MibScalar
brigeNATEnablePing = _BrigeNATEnablePing_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 2),
    _BrigeNATEnablePing_Type()
)
brigeNATEnablePing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATEnablePing.setStatus("current")


class _BrigeNATEnableProductWebServer_Type(Integer32):
    """Custom type brigeNATEnableProductWebServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrigeNATEnableProductWebServer_Type.__name__ = "Integer32"
_BrigeNATEnableProductWebServer_Object = MibScalar
brigeNATEnableProductWebServer = _BrigeNATEnableProductWebServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 3),
    _BrigeNATEnableProductWebServer_Type()
)
brigeNATEnableProductWebServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATEnableProductWebServer.setStatus("current")
_BrigeNATInternalWebServerPort_Type = Integer32
_BrigeNATInternalWebServerPort_Object = MibScalar
brigeNATInternalWebServerPort = _BrigeNATInternalWebServerPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 4),
    _BrigeNATInternalWebServerPort_Type()
)
brigeNATInternalWebServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATInternalWebServerPort.setStatus("current")


class _BrigeNATEnableProductSnmpServer_Type(Integer32):
    """Custom type brigeNATEnableProductSnmpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrigeNATEnableProductSnmpServer_Type.__name__ = "Integer32"
_BrigeNATEnableProductSnmpServer_Object = MibScalar
brigeNATEnableProductSnmpServer = _BrigeNATEnableProductSnmpServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 5),
    _BrigeNATEnableProductSnmpServer_Type()
)
brigeNATEnableProductSnmpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATEnableProductSnmpServer.setStatus("current")
_BrigeNATInternalWebSnmpPort_Type = Integer32
_BrigeNATInternalWebSnmpPort_Object = MibScalar
brigeNATInternalWebSnmpPort = _BrigeNATInternalWebSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 6),
    _BrigeNATInternalWebSnmpPort_Type()
)
brigeNATInternalWebSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATInternalWebSnmpPort.setStatus("current")


class _BrigeNATWanIpAddrMode_Type(Integer32):
    """Custom type brigeNATWanIpAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_BrigeNATWanIpAddrMode_Type.__name__ = "Integer32"
_BrigeNATWanIpAddrMode_Object = MibScalar
brigeNATWanIpAddrMode = _BrigeNATWanIpAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 7),
    _BrigeNATWanIpAddrMode_Type()
)
brigeNATWanIpAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATWanIpAddrMode.setStatus("current")
_BrigeNATWanIpAddr_Type = IpAddress
_BrigeNATWanIpAddr_Object = MibScalar
brigeNATWanIpAddr = _BrigeNATWanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 8),
    _BrigeNATWanIpAddr_Type()
)
brigeNATWanIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATWanIpAddr.setStatus("current")
_BrigeNATWanSubnetMask_Type = IpAddress
_BrigeNATWanSubnetMask_Object = MibScalar
brigeNATWanSubnetMask = _BrigeNATWanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 9),
    _BrigeNATWanSubnetMask_Type()
)
brigeNATWanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATWanSubnetMask.setStatus("current")
_BrigeNATWanGateway_Type = IpAddress
_BrigeNATWanGateway_Object = MibScalar
brigeNATWanGateway = _BrigeNATWanGateway_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 10),
    _BrigeNATWanGateway_Type()
)
brigeNATWanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brigeNATWanGateway.setStatus("current")
_BridgeNatPortForwarding_ObjectIdentity = ObjectIdentity
bridgeNatPortForwarding = _BridgeNatPortForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11)
)
_BridgeNatPortForwardingTable_Object = MibTable
bridgeNatPortForwardingTable = _BridgeNatPortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    bridgeNatPortForwardingTable.setStatus("current")
_BridgeNatPortForwardingEntry_Object = MibTableRow
bridgeNatPortForwardingEntry = _BridgeNatPortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1)
)
bridgeNatPortForwardingEntry.setIndexNames(
    (0, "ACKSYS-WLG-MIB", "bridgeNatPortForwardingListId"),
)
if mibBuilder.loadTexts:
    bridgeNatPortForwardingEntry.setStatus("current")
_BridgeNatPortForwardingListId_Type = Integer32
_BridgeNatPortForwardingListId_Object = MibTableColumn
bridgeNatPortForwardingListId = _BridgeNatPortForwardingListId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 1),
    _BridgeNatPortForwardingListId_Type()
)
bridgeNatPortForwardingListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListId.setStatus("current")


class _BridgeNatPortForwardingListName_Type(OctetString):
    """Custom type bridgeNatPortForwardingListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingListName_Type.__name__ = "OctetString"
_BridgeNatPortForwardingListName_Object = MibTableColumn
bridgeNatPortForwardingListName = _BridgeNatPortForwardingListName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 2),
    _BridgeNatPortForwardingListName_Type()
)
bridgeNatPortForwardingListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListName.setStatus("current")
_BridgeNatPortForwardingListIpAddr_Type = IpAddress
_BridgeNatPortForwardingListIpAddr_Object = MibTableColumn
bridgeNatPortForwardingListIpAddr = _BridgeNatPortForwardingListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 3),
    _BridgeNatPortForwardingListIpAddr_Type()
)
bridgeNatPortForwardingListIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListIpAddr.setStatus("current")


class _BridgeNatPortForwardingListPublicTcpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingListPublicTcpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingListPublicTcpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingListPublicTcpPort_Object = MibTableColumn
bridgeNatPortForwardingListPublicTcpPort = _BridgeNatPortForwardingListPublicTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 4),
    _BridgeNatPortForwardingListPublicTcpPort_Type()
)
bridgeNatPortForwardingListPublicTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListPublicTcpPort.setStatus("current")


class _BridgeNatPortForwardingListPrivateTcpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingListPrivateTcpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingListPrivateTcpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingListPrivateTcpPort_Object = MibTableColumn
bridgeNatPortForwardingListPrivateTcpPort = _BridgeNatPortForwardingListPrivateTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 5),
    _BridgeNatPortForwardingListPrivateTcpPort_Type()
)
bridgeNatPortForwardingListPrivateTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListPrivateTcpPort.setStatus("current")


class _BridgeNatPortForwardingListPublicUdpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingListPublicUdpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingListPublicUdpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingListPublicUdpPort_Object = MibTableColumn
bridgeNatPortForwardingListPublicUdpPort = _BridgeNatPortForwardingListPublicUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 6),
    _BridgeNatPortForwardingListPublicUdpPort_Type()
)
bridgeNatPortForwardingListPublicUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListPublicUdpPort.setStatus("current")


class _BridgeNatPortForwardingListPrivateUdpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingListPrivateUdpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingListPrivateUdpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingListPrivateUdpPort_Object = MibTableColumn
bridgeNatPortForwardingListPrivateUdpPort = _BridgeNatPortForwardingListPrivateUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 7),
    _BridgeNatPortForwardingListPrivateUdpPort_Type()
)
bridgeNatPortForwardingListPrivateUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListPrivateUdpPort.setStatus("current")


class _BridgeNatPortForwardingListEnable_Type(Integer32):
    """Custom type bridgeNatPortForwardingListEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BridgeNatPortForwardingListEnable_Type.__name__ = "Integer32"
_BridgeNatPortForwardingListEnable_Object = MibTableColumn
bridgeNatPortForwardingListEnable = _BridgeNatPortForwardingListEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 1, 1, 8),
    _BridgeNatPortForwardingListEnable_Type()
)
bridgeNatPortForwardingListEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingListEnable.setStatus("current")


class _BridgeNatPortForwardingName_Type(OctetString):
    """Custom type bridgeNatPortForwardingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingName_Type.__name__ = "OctetString"
_BridgeNatPortForwardingName_Object = MibScalar
bridgeNatPortForwardingName = _BridgeNatPortForwardingName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 2),
    _BridgeNatPortForwardingName_Type()
)
bridgeNatPortForwardingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingName.setStatus("current")
_BridgeNatPortForwardingIpAddr_Type = IpAddress
_BridgeNatPortForwardingIpAddr_Object = MibScalar
bridgeNatPortForwardingIpAddr = _BridgeNatPortForwardingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 3),
    _BridgeNatPortForwardingIpAddr_Type()
)
bridgeNatPortForwardingIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingIpAddr.setStatus("current")


class _BridgeNatPortForwardingPublicTcpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingPublicTcpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingPublicTcpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingPublicTcpPort_Object = MibScalar
bridgeNatPortForwardingPublicTcpPort = _BridgeNatPortForwardingPublicTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 4),
    _BridgeNatPortForwardingPublicTcpPort_Type()
)
bridgeNatPortForwardingPublicTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingPublicTcpPort.setStatus("current")


class _BridgeNatPortForwardingPrivateTcpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingPrivateTcpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingPrivateTcpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingPrivateTcpPort_Object = MibScalar
bridgeNatPortForwardingPrivateTcpPort = _BridgeNatPortForwardingPrivateTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 5),
    _BridgeNatPortForwardingPrivateTcpPort_Type()
)
bridgeNatPortForwardingPrivateTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingPrivateTcpPort.setStatus("current")


class _BridgeNatPortForwardingPublicUdpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingPublicUdpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingPublicUdpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingPublicUdpPort_Object = MibScalar
bridgeNatPortForwardingPublicUdpPort = _BridgeNatPortForwardingPublicUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 6),
    _BridgeNatPortForwardingPublicUdpPort_Type()
)
bridgeNatPortForwardingPublicUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingPublicUdpPort.setStatus("current")


class _BridgeNatPortForwardingPrivateUdpPort_Type(OctetString):
    """Custom type bridgeNatPortForwardingPrivateUdpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeNatPortForwardingPrivateUdpPort_Type.__name__ = "OctetString"
_BridgeNatPortForwardingPrivateUdpPort_Object = MibScalar
bridgeNatPortForwardingPrivateUdpPort = _BridgeNatPortForwardingPrivateUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 7),
    _BridgeNatPortForwardingPrivateUdpPort_Type()
)
bridgeNatPortForwardingPrivateUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingPrivateUdpPort.setStatus("current")
_BridgeNatPortForwardingEnableRule_Type = Integer32
_BridgeNatPortForwardingEnableRule_Object = MibScalar
bridgeNatPortForwardingEnableRule = _BridgeNatPortForwardingEnableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 8),
    _BridgeNatPortForwardingEnableRule_Type()
)
bridgeNatPortForwardingEnableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingEnableRule.setStatus("current")
_BridgeNatPortForwardingDisableRule_Type = Integer32
_BridgeNatPortForwardingDisableRule_Object = MibScalar
bridgeNatPortForwardingDisableRule = _BridgeNatPortForwardingDisableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 9),
    _BridgeNatPortForwardingDisableRule_Type()
)
bridgeNatPortForwardingDisableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingDisableRule.setStatus("current")
_BridgeNatPortForwardingSaveRule_Type = Integer32
_BridgeNatPortForwardingSaveRule_Object = MibScalar
bridgeNatPortForwardingSaveRule = _BridgeNatPortForwardingSaveRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 10),
    _BridgeNatPortForwardingSaveRule_Type()
)
bridgeNatPortForwardingSaveRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingSaveRule.setStatus("current")
_BridgeNatPortForwardingDeleteRule_Type = Integer32
_BridgeNatPortForwardingDeleteRule_Object = MibScalar
bridgeNatPortForwardingDeleteRule = _BridgeNatPortForwardingDeleteRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 2, 12, 11, 11),
    _BridgeNatPortForwardingDeleteRule_Type()
)
bridgeNatPortForwardingDeleteRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeNatPortForwardingDeleteRule.setStatus("current")
_Access_point_mode_ObjectIdentity = ObjectIdentity
access_point_mode = _Access_point_mode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3)
)
_ApClientTable_Object = MibTable
apClientTable = _ApClientTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apClientTable.setStatus("current")
_ApClientEntry_Object = MibTableRow
apClientEntry = _ApClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1, 1)
)
apClientEntry.setIndexNames(
    (0, "ACKSYS-WLG-MIB", "clientMacAddr"),
)
if mibBuilder.loadTexts:
    apClientEntry.setStatus("current")
_ClientMacAddr_Type = PhysAddress
_ClientMacAddr_Object = MibTableColumn
clientMacAddr = _ClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1, 1, 1),
    _ClientMacAddr_Type()
)
clientMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMacAddr.setStatus("current")


class _Client80211Mode_Type(Integer32):
    """Custom type client80211Mode based on Integer32"""
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
        *(("b-only", 1),
          ("g-only", 2),
          ("mixed-b-g", 3),
          ("a-only", 4))
    )


_Client80211Mode_Type.__name__ = "Integer32"
_Client80211Mode_Object = MibTableColumn
client80211Mode = _Client80211Mode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1, 1, 2),
    _Client80211Mode_Type()
)
client80211Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    client80211Mode.setStatus("current")
_ClientTxRate_Type = Integer32
_ClientTxRate_Object = MibTableColumn
clientTxRate = _ClientTxRate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1, 1, 3),
    _ClientTxRate_Type()
)
clientTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientTxRate.setStatus("current")
_ClientRssiPercent_Type = Gauge32
_ClientRssiPercent_Object = MibTableColumn
clientRssiPercent = _ClientRssiPercent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 1, 1, 4),
    _ClientRssiPercent_Type()
)
clientRssiPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRssiPercent.setStatus("current")


class _ApAutomaticChannel_Type(Integer32):
    """Custom type apAutomaticChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ApAutomaticChannel_Type.__name__ = "Integer32"
_ApAutomaticChannel_Object = MibScalar
apAutomaticChannel = _ApAutomaticChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 2),
    _ApAutomaticChannel_Type()
)
apAutomaticChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAutomaticChannel.setStatus("current")
_ApClientCount_Type = Integer32
_ApClientCount_Object = MibScalar
apClientCount = _ApClientCount_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 3),
    _ApClientCount_Type()
)
apClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apClientCount.setStatus("current")
_ApClientFiltering_ObjectIdentity = ObjectIdentity
apClientFiltering = _ApClientFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4)
)


class _ApClientFilteringEnable_Type(Integer32):
    """Custom type apClientFilteringEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ApClientFilteringEnable_Type.__name__ = "Integer32"
_ApClientFilteringEnable_Object = MibScalar
apClientFilteringEnable = _ApClientFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 1),
    _ApClientFilteringEnable_Type()
)
apClientFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringEnable.setStatus("current")


class _ApClientFilteringMode_Type(Integer32):
    """Custom type apClientFilteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApClientFilteringMode_Type.__name__ = "Integer32"
_ApClientFilteringMode_Object = MibScalar
apClientFilteringMode = _ApClientFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 2),
    _ApClientFilteringMode_Type()
)
apClientFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringMode.setStatus("current")


class _ApClientWirelessFiltering_Type(Integer32):
    """Custom type apClientWirelessFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApClientWirelessFiltering_Type.__name__ = "Integer32"
_ApClientWirelessFiltering_Object = MibScalar
apClientWirelessFiltering = _ApClientWirelessFiltering_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 3),
    _ApClientWirelessFiltering_Type()
)
apClientWirelessFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientWirelessFiltering.setStatus("current")


class _ApClientWiredFiltering_Type(Integer32):
    """Custom type apClientWiredFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApClientWiredFiltering_Type.__name__ = "Integer32"
_ApClientWiredFiltering_Object = MibScalar
apClientWiredFiltering = _ApClientWiredFiltering_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 4),
    _ApClientWiredFiltering_Type()
)
apClientWiredFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientWiredFiltering.setStatus("current")
_ApClientFilteringMACAddress_Type = PhysAddress
_ApClientFilteringMACAddress_Object = MibScalar
apClientFilteringMACAddress = _ApClientFilteringMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 5),
    _ApClientFilteringMACAddress_Type()
)
apClientFilteringMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringMACAddress.setStatus("current")


class _ApClientFilteringName_Type(OctetString):
    """Custom type apClientFilteringName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApClientFilteringName_Type.__name__ = "OctetString"
_ApClientFilteringName_Object = MibScalar
apClientFilteringName = _ApClientFilteringName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 6),
    _ApClientFilteringName_Type()
)
apClientFilteringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringName.setStatus("current")
_ApClientFilteringSave_Type = Integer32
_ApClientFilteringSave_Object = MibScalar
apClientFilteringSave = _ApClientFilteringSave_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 7),
    _ApClientFilteringSave_Type()
)
apClientFilteringSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringSave.setStatus("current")
_ApClientFilteringDelete_Type = Integer32
_ApClientFilteringDelete_Object = MibScalar
apClientFilteringDelete = _ApClientFilteringDelete_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 8),
    _ApClientFilteringDelete_Type()
)
apClientFilteringDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringDelete.setStatus("current")
_ApClientFilteringEnableRule_Type = Integer32
_ApClientFilteringEnableRule_Object = MibScalar
apClientFilteringEnableRule = _ApClientFilteringEnableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 9),
    _ApClientFilteringEnableRule_Type()
)
apClientFilteringEnableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringEnableRule.setStatus("current")
_ApClientFilteringDisableRule_Type = Integer32
_ApClientFilteringDisableRule_Object = MibScalar
apClientFilteringDisableRule = _ApClientFilteringDisableRule_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 10),
    _ApClientFilteringDisableRule_Type()
)
apClientFilteringDisableRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientFilteringDisableRule.setStatus("current")
_ApClientFilteringTable_Object = MibTable
apClientFilteringTable = _ApClientFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11)
)
if mibBuilder.loadTexts:
    apClientFilteringTable.setStatus("current")
_ApClientFilteringEntry_Object = MibTableRow
apClientFilteringEntry = _ApClientFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11, 1)
)
apClientFilteringEntry.setIndexNames(
    (0, "ACKSYS-WLG-MIB", "apClientFilteringListId"),
)
if mibBuilder.loadTexts:
    apClientFilteringEntry.setStatus("current")
_ApClientFilteringListId_Type = Integer32
_ApClientFilteringListId_Object = MibTableColumn
apClientFilteringListId = _ApClientFilteringListId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11, 1, 1),
    _ApClientFilteringListId_Type()
)
apClientFilteringListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apClientFilteringListId.setStatus("current")


class _ApClientFilteringListName_Type(OctetString):
    """Custom type apClientFilteringListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApClientFilteringListName_Type.__name__ = "OctetString"
_ApClientFilteringListName_Object = MibTableColumn
apClientFilteringListName = _ApClientFilteringListName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11, 1, 2),
    _ApClientFilteringListName_Type()
)
apClientFilteringListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apClientFilteringListName.setStatus("current")
_ApClientFilteringListMAC_Type = PhysAddress
_ApClientFilteringListMAC_Object = MibTableColumn
apClientFilteringListMAC = _ApClientFilteringListMAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11, 1, 3),
    _ApClientFilteringListMAC_Type()
)
apClientFilteringListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apClientFilteringListMAC.setStatus("current")


class _ApClientFilteringListEnable_Type(Integer32):
    """Custom type apClientFilteringListEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApClientFilteringListEnable_Type.__name__ = "Integer32"
_ApClientFilteringListEnable_Object = MibTableColumn
apClientFilteringListEnable = _ApClientFilteringListEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 11, 1, 4),
    _ApClientFilteringListEnable_Type()
)
apClientFilteringListEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apClientFilteringListEnable.setStatus("current")
_Wds_ObjectIdentity = ObjectIdentity
wds = _Wds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5)
)


class _ApWDSEnable_Type(Integer32):
    """Custom type apWDSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApWDSEnable_Type.__name__ = "Integer32"
_ApWDSEnable_Object = MibScalar
apWDSEnable = _ApWDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 1),
    _ApWDSEnable_Type()
)
apWDSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSEnable.setStatus("current")


class _ApWDSEnableSTP_Type(Integer32):
    """Custom type apWDSEnableSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApWDSEnableSTP_Type.__name__ = "Integer32"
_ApWDSEnableSTP_Object = MibScalar
apWDSEnableSTP = _ApWDSEnableSTP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 2),
    _ApWDSEnableSTP_Type()
)
apWDSEnableSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSEnableSTP.setStatus("current")
_ApWDSMAC1_Type = PhysAddress
_ApWDSMAC1_Object = MibScalar
apWDSMAC1 = _ApWDSMAC1_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 3),
    _ApWDSMAC1_Type()
)
apWDSMAC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC1.setStatus("current")
_ApWDSMAC2_Type = PhysAddress
_ApWDSMAC2_Object = MibScalar
apWDSMAC2 = _ApWDSMAC2_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 4),
    _ApWDSMAC2_Type()
)
apWDSMAC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC2.setStatus("current")
_ApWDSMAC3_Type = PhysAddress
_ApWDSMAC3_Object = MibScalar
apWDSMAC3 = _ApWDSMAC3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 5),
    _ApWDSMAC3_Type()
)
apWDSMAC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC3.setStatus("current")
_ApWDSMAC4_Type = PhysAddress
_ApWDSMAC4_Object = MibScalar
apWDSMAC4 = _ApWDSMAC4_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 6),
    _ApWDSMAC4_Type()
)
apWDSMAC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC4.setStatus("current")
_ApWDSMAC5_Type = PhysAddress
_ApWDSMAC5_Object = MibScalar
apWDSMAC5 = _ApWDSMAC5_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 7),
    _ApWDSMAC5_Type()
)
apWDSMAC5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC5.setStatus("current")
_ApWDSMAC6_Type = PhysAddress
_ApWDSMAC6_Object = MibScalar
apWDSMAC6 = _ApWDSMAC6_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 8),
    _ApWDSMAC6_Type()
)
apWDSMAC6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSMAC6.setStatus("current")


class _SettingSSIDVisibility_Type(Integer32):
    """Custom type settingSSIDVisibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invisible", 1),
          ("visible", 2))
    )


_SettingSSIDVisibility_Type.__name__ = "Integer32"
_SettingSSIDVisibility_Object = MibScalar
settingSSIDVisibility = _SettingSSIDVisibility_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 6),
    _SettingSSIDVisibility_Type()
)
settingSSIDVisibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingSSIDVisibility.setStatus("current")


class _EnableSTP_Type(Integer32):
    """Custom type enableSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableSTP_Type.__name__ = "Integer32"
_EnableSTP_Object = MibScalar
enableSTP = _EnableSTP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 7),
    _EnableSTP_Type()
)
enableSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSTP.setStatus("current")
_LanTimeOutSettings_ObjectIdentity = ObjectIdentity
lanTimeOutSettings = _LanTimeOutSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8)
)


class _EnableLanTimeout_Type(Integer32):
    """Custom type enableLanTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableLanTimeout_Type.__name__ = "Integer32"
_EnableLanTimeout_Object = MibScalar
enableLanTimeout = _EnableLanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8, 1),
    _EnableLanTimeout_Type()
)
enableLanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLanTimeout.setStatus("current")
_LanTimeoutIPSurvey_Type = Integer32
_LanTimeoutIPSurvey_Object = MibScalar
lanTimeoutIPSurvey = _LanTimeoutIPSurvey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8, 2),
    _LanTimeoutIPSurvey_Type()
)
lanTimeoutIPSurvey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanTimeoutIPSurvey.setStatus("current")
_LanTimeoutMaxProbe_Type = Integer32
_LanTimeoutMaxProbe_Object = MibScalar
lanTimeoutMaxProbe = _LanTimeoutMaxProbe_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8, 3),
    _LanTimeoutMaxProbe_Type()
)
lanTimeoutMaxProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanTimeoutMaxProbe.setStatus("current")
_LanTimeoutProbeTimeout_Type = Integer32
_LanTimeoutProbeTimeout_Object = MibScalar
lanTimeoutProbeTimeout = _LanTimeoutProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8, 4),
    _LanTimeoutProbeTimeout_Type()
)
lanTimeoutProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanTimeoutProbeTimeout.setStatus("current")
_LanTimeoutProbeInterval_Type = Integer32
_LanTimeoutProbeInterval_Object = MibScalar
lanTimeoutProbeInterval = _LanTimeoutProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 8, 5),
    _LanTimeoutProbeInterval_Type()
)
lanTimeoutProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanTimeoutProbeInterval.setStatus("current")
_AdvancedSettings_ObjectIdentity = ObjectIdentity
advancedSettings = _AdvancedSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4)
)
_LongDistanceSettings_ObjectIdentity = ObjectIdentity
longDistanceSettings = _LongDistanceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1)
)


class _EnableLongDistance_Type(Integer32):
    """Custom type enableLongDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableLongDistance_Type.__name__ = "Integer32"
_EnableLongDistance_Object = MibScalar
enableLongDistance = _EnableLongDistance_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1, 1),
    _EnableLongDistance_Type()
)
enableLongDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLongDistance.setStatus("current")
_DistanceAntennaMeter_Type = Integer32
_DistanceAntennaMeter_Object = MibScalar
distanceAntennaMeter = _DistanceAntennaMeter_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1, 2),
    _DistanceAntennaMeter_Type()
)
distanceAntennaMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distanceAntennaMeter.setStatus("current")
_DistanceSlotTime_Type = Integer32
_DistanceSlotTime_Object = MibScalar
distanceSlotTime = _DistanceSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1, 3),
    _DistanceSlotTime_Type()
)
distanceSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distanceSlotTime.setStatus("current")
_DistanceAckTimeout_Type = Integer32
_DistanceAckTimeout_Object = MibScalar
distanceAckTimeout = _DistanceAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1, 4),
    _DistanceAckTimeout_Type()
)
distanceAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distanceAckTimeout.setStatus("current")
_DistanceCtsTimeout_Type = Integer32
_DistanceCtsTimeout_Object = MibScalar
distanceCtsTimeout = _DistanceCtsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 1, 5),
    _DistanceCtsTimeout_Type()
)
distanceCtsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distanceCtsTimeout.setStatus("current")


class _Enable802_11d_Type(Integer32):
    """Custom type enable802_11d based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Enable802_11d_Type.__name__ = "Integer32"
_Enable802_11d_Object = MibScalar
enable802_11d = _Enable802_11d_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 2),
    _Enable802_11d_Type()
)
enable802_11d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable802_11d.setStatus("current")


class _EnableIsolateSTA_Type(Integer32):
    """Custom type enableIsolateSTA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableIsolateSTA_Type.__name__ = "Integer32"
_EnableIsolateSTA_Object = MibScalar
enableIsolateSTA = _EnableIsolateSTA_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 4, 3),
    _EnableIsolateSTA_Type()
)
enableIsolateSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIsolateSTA.setStatus("current")
_Administration_ObjectIdentity = ObjectIdentity
administration = _Administration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2)
)


class _AdminReset_Type(Integer32):
    """Custom type adminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdminReset_Type.__name__ = "Integer32"
_AdminReset_Object = MibScalar
adminReset = _AdminReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 1),
    _AdminReset_Type()
)
adminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminReset.setStatus("current")


class _AdminResetFactory_Type(Integer32):
    """Custom type adminResetFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetfactory", 1)
    )


_AdminResetFactory_Type.__name__ = "Integer32"
_AdminResetFactory_Object = MibScalar
adminResetFactory = _AdminResetFactory_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 2),
    _AdminResetFactory_Type()
)
adminResetFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminResetFactory.setStatus("current")


class _AdminEnableWebServer_Type(Integer32):
    """Custom type adminEnableWebServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdminEnableWebServer_Type.__name__ = "Integer32"
_AdminEnableWebServer_Object = MibScalar
adminEnableWebServer = _AdminEnableWebServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 3),
    _AdminEnableWebServer_Type()
)
adminEnableWebServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEnableWebServer.setStatus("current")


class _AdminAutoSave_Type(Integer32):
    """Custom type adminAutoSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdminAutoSave_Type.__name__ = "Integer32"
_AdminAutoSave_Object = MibScalar
adminAutoSave = _AdminAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 4),
    _AdminAutoSave_Type()
)
adminAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAutoSave.setStatus("current")


class _AdminSave_Type(Integer32):
    """Custom type adminSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saveRequire", 2),
          ("saveNotRequire", 3))
    )


_AdminSave_Type.__name__ = "Integer32"
_AdminSave_Object = MibScalar
adminSave = _AdminSave_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 5),
    _AdminSave_Type()
)
adminSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSave.setStatus("current")
_Os_stat_ObjectIdentity = ObjectIdentity
os_stat = _Os_stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3)
)
_Os_statFreeHeap_Type = Integer32
_Os_statFreeHeap_Object = MibScalar
os_statFreeHeap = _Os_statFreeHeap_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3, 1),
    _Os_statFreeHeap_Type()
)
os_statFreeHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os_statFreeHeap.setStatus("current")
_Os_statTotalHeap_Type = Integer32
_Os_statTotalHeap_Object = MibScalar
os_statTotalHeap = _Os_statTotalHeap_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3, 2),
    _Os_statTotalHeap_Type()
)
os_statTotalHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os_statTotalHeap.setStatus("current")
_Os_statHeapLowWater_Type = Integer32
_Os_statHeapLowWater_Object = MibScalar
os_statHeapLowWater = _Os_statHeapLowWater_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3, 3),
    _Os_statHeapLowWater_Type()
)
os_statHeapLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os_statHeapLowWater.setStatus("current")
_Os_statNetpageFree_Type = Integer32
_Os_statNetpageFree_Object = MibScalar
os_statNetpageFree = _Os_statNetpageFree_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3, 4),
    _Os_statNetpageFree_Type()
)
os_statNetpageFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os_statNetpageFree.setStatus("current")
_Os_statNetpageLowWater_Type = Integer32
_Os_statNetpageLowWater_Object = MibScalar
os_statNetpageLowWater = _Os_statNetpageLowWater_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 3, 5),
    _Os_statNetpageLowWater_Type()
)
os_statNetpageLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os_statNetpageLowWater.setStatus("current")
_ProductSpecific_ObjectIdentity = ObjectIdentity
productSpecific = _ProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 4)
)
_Wlg_aboard_ObjectIdentity = ObjectIdentity
wlg_aboard = _Wlg_aboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 4, 1)
)


class _Wlg_aboard_PW1_state_Type(Integer32):
    """Custom type wlg_aboard_PW1_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2))
    )


_Wlg_aboard_PW1_state_Type.__name__ = "Integer32"
_Wlg_aboard_PW1_state_Object = MibScalar
wlg_aboard_PW1_state = _Wlg_aboard_PW1_state_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 4, 1, 1),
    _Wlg_aboard_PW1_state_Type()
)
wlg_aboard_PW1_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlg_aboard_PW1_state.setStatus("obsolete")


class _Wlg_aboard_PW2_state_Type(Integer32):
    """Custom type wlg_aboard_PW2_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2))
    )


_Wlg_aboard_PW2_state_Type.__name__ = "Integer32"
_Wlg_aboard_PW2_state_Object = MibScalar
wlg_aboard_PW2_state = _Wlg_aboard_PW2_state_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 4, 1, 2),
    _Wlg_aboard_PW2_state_Type()
)
wlg_aboard_PW2_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlg_aboard_PW2_state.setStatus("obsolete")
_LanInterface_ObjectIdentity = ObjectIdentity
lanInterface = _LanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5)
)


class _LanInterfaceIpAddrMode_Type(Integer32):
    """Custom type lanInterfaceIpAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_LanInterfaceIpAddrMode_Type.__name__ = "Integer32"
_LanInterfaceIpAddrMode_Object = MibScalar
lanInterfaceIpAddrMode = _LanInterfaceIpAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 1),
    _LanInterfaceIpAddrMode_Type()
)
lanInterfaceIpAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceIpAddrMode.setStatus("current")
_LanInterfaceIpAddr_Type = IpAddress
_LanInterfaceIpAddr_Object = MibScalar
lanInterfaceIpAddr = _LanInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 2),
    _LanInterfaceIpAddr_Type()
)
lanInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceIpAddr.setStatus("current")
_LanInterfaceSubNetMask_Type = IpAddress
_LanInterfaceSubNetMask_Object = MibScalar
lanInterfaceSubNetMask = _LanInterfaceSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 3),
    _LanInterfaceSubNetMask_Type()
)
lanInterfaceSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceSubNetMask.setStatus("current")
_LanInterfaceGatewayIp_Type = IpAddress
_LanInterfaceGatewayIp_Object = MibScalar
lanInterfaceGatewayIp = _LanInterfaceGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 4),
    _LanInterfaceGatewayIp_Type()
)
lanInterfaceGatewayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceGatewayIp.setStatus("current")


class _LanInterfaceHostName_Type(OctetString):
    """Custom type lanInterfaceHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LanInterfaceHostName_Type.__name__ = "OctetString"
_LanInterfaceHostName_Object = MibScalar
lanInterfaceHostName = _LanInterfaceHostName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 5),
    _LanInterfaceHostName_Type()
)
lanInterfaceHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceHostName.setStatus("current")


class _LanInterfaceLocalDomainName_Type(OctetString):
    """Custom type lanInterfaceLocalDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_LanInterfaceLocalDomainName_Type.__name__ = "OctetString"
_LanInterfaceLocalDomainName_Object = MibScalar
lanInterfaceLocalDomainName = _LanInterfaceLocalDomainName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 5, 6),
    _LanInterfaceLocalDomainName_Type()
)
lanInterfaceLocalDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanInterfaceLocalDomainName.setStatus("current")


class _AcksysProductID_Type(Integer32):
    """Custom type acksysProductID based on Integer32"""
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
        *(("wlg-link", 1),
          ("wlg-aboard-n", 2),
          ("wlg-link-v2", 3),
          ("wlg-aboard-n-v2", 4))
    )


_AcksysProductID_Type.__name__ = "Integer32"
_AcksysProductID_Object = MibScalar
acksysProductID = _AcksysProductID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 3),
    _AcksysProductID_Type()
)
acksysProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acksysProductID.setStatus("current")
_C_key_management_ObjectIdentity = ObjectIdentity
c_key_management = _C_key_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 4)
)
_CkeyManagementCopySettingTo_Type = Integer32
_CkeyManagementCopySettingTo_Object = MibScalar
ckeyManagementCopySettingTo = _CkeyManagementCopySettingTo_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 1),
    _CkeyManagementCopySettingTo_Type()
)
ckeyManagementCopySettingTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementCopySettingTo.setStatus("current")
_CkeyManagementCopySettingFrom_Type = Integer32
_CkeyManagementCopySettingFrom_Object = MibScalar
ckeyManagementCopySettingFrom = _CkeyManagementCopySettingFrom_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 2),
    _CkeyManagementCopySettingFrom_Type()
)
ckeyManagementCopySettingFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementCopySettingFrom.setStatus("current")
_AlarmSettings_ObjectIdentity = ObjectIdentity
alarmSettings = _AlarmSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5)
)


class _AlarmSettingsTest_Type(Integer32):
    """Custom type alarmSettingsTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("clear", 2))
    )


_AlarmSettingsTest_Type.__name__ = "Integer32"
_AlarmSettingsTest_Object = MibScalar
alarmSettingsTest = _AlarmSettingsTest_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 1),
    _AlarmSettingsTest_Type()
)
alarmSettingsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsTest.setStatus("current")
_AlarmSettingsPower1Down_ObjectIdentity = ObjectIdentity
alarmSettingsPower1Down = _AlarmSettingsPower1Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 2)
)


class _AlarmSettingsPower1DownEnable_Type(Integer32):
    """Custom type alarmSettingsPower1DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsPower1DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsPower1DownEnable_Object = MibScalar
alarmSettingsPower1DownEnable = _AlarmSettingsPower1DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 2, 1),
    _AlarmSettingsPower1DownEnable_Type()
)
alarmSettingsPower1DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower1DownEnable.setStatus("current")


class _AlarmSettingsPower1DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsPower1DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsPower1DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsPower1DownEnableAutomaticReset_Object = MibScalar
alarmSettingsPower1DownEnableAutomaticReset = _AlarmSettingsPower1DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 2, 2),
    _AlarmSettingsPower1DownEnableAutomaticReset_Type()
)
alarmSettingsPower1DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower1DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsPower1DownStatus_Type(Integer32):
    """Custom type alarmSettingsPower1DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsPower1DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsPower1DownStatus_Object = MibScalar
alarmSettingsPower1DownStatus = _AlarmSettingsPower1DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 2, 3),
    _AlarmSettingsPower1DownStatus_Type()
)
alarmSettingsPower1DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower1DownStatus.setStatus("current")
_AlarmSettingsPower2Down_ObjectIdentity = ObjectIdentity
alarmSettingsPower2Down = _AlarmSettingsPower2Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 3)
)


class _AlarmSettingsPower2DownEnable_Type(Integer32):
    """Custom type alarmSettingsPower2DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsPower2DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsPower2DownEnable_Object = MibScalar
alarmSettingsPower2DownEnable = _AlarmSettingsPower2DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 3, 1),
    _AlarmSettingsPower2DownEnable_Type()
)
alarmSettingsPower2DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower2DownEnable.setStatus("current")


class _AlarmSettingsPower2DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsPower2DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsPower2DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsPower2DownEnableAutomaticReset_Object = MibScalar
alarmSettingsPower2DownEnableAutomaticReset = _AlarmSettingsPower2DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 3, 2),
    _AlarmSettingsPower2DownEnableAutomaticReset_Type()
)
alarmSettingsPower2DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower2DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsPower2DownStatus_Type(Integer32):
    """Custom type alarmSettingsPower2DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsPower2DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsPower2DownStatus_Object = MibScalar
alarmSettingsPower2DownStatus = _AlarmSettingsPower2DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 3, 3),
    _AlarmSettingsPower2DownStatus_Type()
)
alarmSettingsPower2DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower2DownStatus.setStatus("current")
_AlarmSettingsLan1Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan1Down = _AlarmSettingsLan1Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 4)
)


class _AlarmSettingsLan1DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan1DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan1DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan1DownEnable_Object = MibScalar
alarmSettingsLan1DownEnable = _AlarmSettingsLan1DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 4, 1),
    _AlarmSettingsLan1DownEnable_Type()
)
alarmSettingsLan1DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan1DownEnable.setStatus("current")


class _AlarmSettingsLan1DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan1DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan1DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan1DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan1DownEnableAutomaticReset = _AlarmSettingsLan1DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 4, 2),
    _AlarmSettingsLan1DownEnableAutomaticReset_Type()
)
alarmSettingsLan1DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan1DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan1DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan1DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan1DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan1DownStatus_Object = MibScalar
alarmSettingsLan1DownStatus = _AlarmSettingsLan1DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 4, 3),
    _AlarmSettingsLan1DownStatus_Type()
)
alarmSettingsLan1DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan1DownStatus.setStatus("current")
_AlarmSettingsLan2Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan2Down = _AlarmSettingsLan2Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 5)
)


class _AlarmSettingsLan2DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan2DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan2DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan2DownEnable_Object = MibScalar
alarmSettingsLan2DownEnable = _AlarmSettingsLan2DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 5, 1),
    _AlarmSettingsLan2DownEnable_Type()
)
alarmSettingsLan2DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan2DownEnable.setStatus("current")


class _AlarmSettingsLan2DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan2DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan2DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan2DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan2DownEnableAutomaticReset = _AlarmSettingsLan2DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 5, 2),
    _AlarmSettingsLan2DownEnableAutomaticReset_Type()
)
alarmSettingsLan2DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan2DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan2DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan2DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan2DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan2DownStatus_Object = MibScalar
alarmSettingsLan2DownStatus = _AlarmSettingsLan2DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 5, 3),
    _AlarmSettingsLan2DownStatus_Type()
)
alarmSettingsLan2DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan2DownStatus.setStatus("current")
_AlarmSettingsLan3Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan3Down = _AlarmSettingsLan3Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 6)
)


class _AlarmSettingsLan3DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan3DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan3DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan3DownEnable_Object = MibScalar
alarmSettingsLan3DownEnable = _AlarmSettingsLan3DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 6, 1),
    _AlarmSettingsLan3DownEnable_Type()
)
alarmSettingsLan3DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan3DownEnable.setStatus("current")


class _AlarmSettingsLan3DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan3DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan3DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan3DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan3DownEnableAutomaticReset = _AlarmSettingsLan3DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 6, 2),
    _AlarmSettingsLan3DownEnableAutomaticReset_Type()
)
alarmSettingsLan3DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan3DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan3DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan3DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan3DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan3DownStatus_Object = MibScalar
alarmSettingsLan3DownStatus = _AlarmSettingsLan3DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 6, 3),
    _AlarmSettingsLan3DownStatus_Type()
)
alarmSettingsLan3DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan3DownStatus.setStatus("current")
_AlarmSettingsLan4Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan4Down = _AlarmSettingsLan4Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 7)
)


class _AlarmSettingsLan4DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan4DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan4DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan4DownEnable_Object = MibScalar
alarmSettingsLan4DownEnable = _AlarmSettingsLan4DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 7, 1),
    _AlarmSettingsLan4DownEnable_Type()
)
alarmSettingsLan4DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan4DownEnable.setStatus("current")


class _AlarmSettingsLan4DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan4DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan4DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan4DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan4DownEnableAutomaticReset = _AlarmSettingsLan4DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 7, 2),
    _AlarmSettingsLan4DownEnableAutomaticReset_Type()
)
alarmSettingsLan4DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan4DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan4DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan4DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan4DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan4DownStatus_Object = MibScalar
alarmSettingsLan4DownStatus = _AlarmSettingsLan4DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 7, 3),
    _AlarmSettingsLan4DownStatus_Type()
)
alarmSettingsLan4DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan4DownStatus.setStatus("current")
_AlarmSettingsLan5Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan5Down = _AlarmSettingsLan5Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 8)
)


class _AlarmSettingsLan5DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan5DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan5DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan5DownEnable_Object = MibScalar
alarmSettingsLan5DownEnable = _AlarmSettingsLan5DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 8, 1),
    _AlarmSettingsLan5DownEnable_Type()
)
alarmSettingsLan5DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan5DownEnable.setStatus("current")


class _AlarmSettingsLan5DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan5DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan5DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan5DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan5DownEnableAutomaticReset = _AlarmSettingsLan5DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 8, 2),
    _AlarmSettingsLan5DownEnableAutomaticReset_Type()
)
alarmSettingsLan5DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan5DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan5DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan5DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan5DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan5DownStatus_Object = MibScalar
alarmSettingsLan5DownStatus = _AlarmSettingsLan5DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 8, 3),
    _AlarmSettingsLan5DownStatus_Type()
)
alarmSettingsLan5DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan5DownStatus.setStatus("current")
_AlarmSettingsLan6Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan6Down = _AlarmSettingsLan6Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 9)
)


class _AlarmSettingsLan6DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan6DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan6DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan6DownEnable_Object = MibScalar
alarmSettingsLan6DownEnable = _AlarmSettingsLan6DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 9, 1),
    _AlarmSettingsLan6DownEnable_Type()
)
alarmSettingsLan6DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan6DownEnable.setStatus("current")


class _AlarmSettingsLan6DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan6DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan6DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan6DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan6DownEnableAutomaticReset = _AlarmSettingsLan6DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 9, 2),
    _AlarmSettingsLan6DownEnableAutomaticReset_Type()
)
alarmSettingsLan6DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan6DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan6DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan6DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan6DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan6DownStatus_Object = MibScalar
alarmSettingsLan6DownStatus = _AlarmSettingsLan6DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 9, 3),
    _AlarmSettingsLan6DownStatus_Type()
)
alarmSettingsLan6DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan6DownStatus.setStatus("current")
_AlarmSettingsLan7Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan7Down = _AlarmSettingsLan7Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 10)
)


class _AlarmSettingsLan7DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan7DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan7DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan7DownEnable_Object = MibScalar
alarmSettingsLan7DownEnable = _AlarmSettingsLan7DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 10, 1),
    _AlarmSettingsLan7DownEnable_Type()
)
alarmSettingsLan7DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan7DownEnable.setStatus("current")


class _AlarmSettingsLan7DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan7DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan7DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan7DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan7DownEnableAutomaticReset = _AlarmSettingsLan7DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 10, 2),
    _AlarmSettingsLan7DownEnableAutomaticReset_Type()
)
alarmSettingsLan7DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan7DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan7DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan7DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan7DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan7DownStatus_Object = MibScalar
alarmSettingsLan7DownStatus = _AlarmSettingsLan7DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 10, 3),
    _AlarmSettingsLan7DownStatus_Type()
)
alarmSettingsLan7DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan7DownStatus.setStatus("current")
_AlarmSettingsLan8Down_ObjectIdentity = ObjectIdentity
alarmSettingsLan8Down = _AlarmSettingsLan8Down_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 11)
)


class _AlarmSettingsLan8DownEnable_Type(Integer32):
    """Custom type alarmSettingsLan8DownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan8DownEnable_Type.__name__ = "Integer32"
_AlarmSettingsLan8DownEnable_Object = MibScalar
alarmSettingsLan8DownEnable = _AlarmSettingsLan8DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 11, 1),
    _AlarmSettingsLan8DownEnable_Type()
)
alarmSettingsLan8DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan8DownEnable.setStatus("current")


class _AlarmSettingsLan8DownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsLan8DownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsLan8DownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsLan8DownEnableAutomaticReset_Object = MibScalar
alarmSettingsLan8DownEnableAutomaticReset = _AlarmSettingsLan8DownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 11, 2),
    _AlarmSettingsLan8DownEnableAutomaticReset_Type()
)
alarmSettingsLan8DownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan8DownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsLan8DownStatus_Type(Integer32):
    """Custom type alarmSettingsLan8DownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsLan8DownStatus_Type.__name__ = "Integer32"
_AlarmSettingsLan8DownStatus_Object = MibScalar
alarmSettingsLan8DownStatus = _AlarmSettingsLan8DownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 11, 3),
    _AlarmSettingsLan8DownStatus_Type()
)
alarmSettingsLan8DownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan8DownStatus.setStatus("current")
_AlarmSettingsWLANDown_ObjectIdentity = ObjectIdentity
alarmSettingsWLANDown = _AlarmSettingsWLANDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 5, 12)
)


class _AlarmSettingsWLANDownEnable_Type(Integer32):
    """Custom type alarmSettingsWLANDownEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsWLANDownEnable_Type.__name__ = "Integer32"
_AlarmSettingsWLANDownEnable_Object = MibScalar
alarmSettingsWLANDownEnable = _AlarmSettingsWLANDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 12, 1),
    _AlarmSettingsWLANDownEnable_Type()
)
alarmSettingsWLANDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsWLANDownEnable.setStatus("current")


class _AlarmSettingsWLANDownEnableAutomaticReset_Type(Integer32):
    """Custom type alarmSettingsWLANDownEnableAutomaticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlarmSettingsWLANDownEnableAutomaticReset_Type.__name__ = "Integer32"
_AlarmSettingsWLANDownEnableAutomaticReset_Object = MibScalar
alarmSettingsWLANDownEnableAutomaticReset = _AlarmSettingsWLANDownEnableAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 12, 2),
    _AlarmSettingsWLANDownEnableAutomaticReset_Type()
)
alarmSettingsWLANDownEnableAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsWLANDownEnableAutomaticReset.setStatus("current")


class _AlarmSettingsWLANDownStatus_Type(Integer32):
    """Custom type alarmSettingsWLANDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ack", 3))
    )


_AlarmSettingsWLANDownStatus_Type.__name__ = "Integer32"
_AlarmSettingsWLANDownStatus_Object = MibScalar
alarmSettingsWLANDownStatus = _AlarmSettingsWLANDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 12, 3),
    _AlarmSettingsWLANDownStatus_Type()
)
alarmSettingsWLANDownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsWLANDownStatus.setStatus("current")
_PowerStatus_ObjectIdentity = ObjectIdentity
powerStatus = _PowerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 6)
)


class _PowerStatus_PW1_state_Type(Integer32):
    """Custom type powerStatus_PW1_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2))
    )


_PowerStatus_PW1_state_Type.__name__ = "Integer32"
_PowerStatus_PW1_state_Object = MibScalar
powerStatus_PW1_state = _PowerStatus_PW1_state_Object(
    (1, 3, 6, 1, 4, 1, 28097, 6, 1),
    _PowerStatus_PW1_state_Type()
)
powerStatus_PW1_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus_PW1_state.setStatus("current")


class _PowerStatus_PW2_state_Type(Integer32):
    """Custom type powerStatus_PW2_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2))
    )


_PowerStatus_PW2_state_Type.__name__ = "Integer32"
_PowerStatus_PW2_state_Object = MibScalar
powerStatus_PW2_state = _PowerStatus_PW2_state_Object(
    (1, 3, 6, 1, 4, 1, 28097, 6, 2),
    _PowerStatus_PW2_state_Type()
)
powerStatus_PW2_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus_PW2_state.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACKSYS-WLG-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "acksys": acksys,
       "network-product": network_product,
       "wifiInterface": wifiInterface,
       "settings": settings,
       "settingInterfaceSsid": settingInterfaceSsid,
       "settingInterfaceWifiMode": settingInterfaceWifiMode,
       "settingInterfaceChannel": settingInterfaceChannel,
       "settingInterface80211Mode": settingInterface80211Mode,
       "settingInterfaceSuper-a-g-Mode": settingInterfaceSuper_a_g_Mode,
       "settingEnableRadio": settingEnableRadio,
       "settingTxPoxer": settingTxPoxer,
       "settingRegion": settingRegion,
       "securitySettings": securitySettings,
       "securityMode": securityMode,
       "securityWEP": securityWEP,
       "securityModeWepKeyLen": securityModeWepKeyLen,
       "securityModeWepKey-1": securityModeWepKey_1,
       "securityModeWepKey-2": securityModeWepKey_2,
       "securityModeWepKey-3": securityModeWepKey_3,
       "securityModeWepKey-4": securityModeWepKey_4,
       "securityModeDefaultWepKey": securityModeDefaultWepKey,
       "securityModeWepAuthentication": securityModeWepAuthentication,
       "securityWPA-WPA2": securityWPA_WPA2,
       "securityPresharedKey": securityPresharedKey,
       "securityModeWpaPresharedKey": securityModeWpaPresharedKey,
       "securityRadius": securityRadius,
       "securityModeWPARadiusAuthenticationTimeout": securityModeWPARadiusAuthenticationTimeout,
       "securityModeWPARadiusIP": securityModeWPARadiusIP,
       "securityModeWPARadiusPort": securityModeWPARadiusPort,
       "securityModeWPARadiusSecret": securityModeWPARadiusSecret,
       "securityModeWPARadiusMacAddressAuthentication": securityModeWPARadiusMacAddressAuthentication,
       "securityRadiusAP": securityRadiusAP,
       "securityModeWPARadiusAPAuthenticationTimeout": securityModeWPARadiusAPAuthenticationTimeout,
       "securityModeWPARadiusAPIP": securityModeWPARadiusAPIP,
       "securityModeWPARadiusAPPort": securityModeWPARadiusAPPort,
       "securityModeWPARadiusAPSecret": securityModeWPARadiusAPSecret,
       "securityModeWPARadiusAPMacAddressAuthentication": securityModeWPARadiusAPMacAddressAuthentication,
       "securityRadiusAPBackup": securityRadiusAPBackup,
       "securityModeWPABackupRadiusAPIP": securityModeWPABackupRadiusAPIP,
       "securityModeWPARadiusBackupAPPort": securityModeWPARadiusBackupAPPort,
       "securityModeWPARadiusBackupAPSecret": securityModeWPARadiusBackupAPSecret,
       "securityModeWPABackupRadiusAPMacAddressAuthentication": securityModeWPABackupRadiusAPMacAddressAuthentication,
       "securityRadiusBridge": securityRadiusBridge,
       "securityModeWPARadiusLogin": securityModeWPARadiusLogin,
       "securityModeWPARadiusPassword": securityModeWPARadiusPassword,
       "securityBackupRadius": securityBackupRadius,
       "securityModeWPABackupRadiusIP": securityModeWPABackupRadiusIP,
       "securityModeWPARadiusBackupPort": securityModeWPARadiusBackupPort,
       "securityModeWPARadiusBackupSecret": securityModeWPARadiusBackupSecret,
       "securityModeWPABackupRadiusMacAddressAuthentication": securityModeWPABackupRadiusMacAddressAuthentication,
       "securityModeWpaMode": securityModeWpaMode,
       "securityModeWpaCipherType": securityModeWpaCipherType,
       "securityModeWpaKeyUpdateInterval": securityModeWpaKeyUpdateInterval,
       "settingAntennaChoice": settingAntennaChoice,
       "settingTransmisionRate": settingTransmisionRate,
       "settingFlagUdapnopassword": settingFlagUdapnopassword,
       "settingFlagFiltersamenet": settingFlagFiltersamenet,
       "settingFlagFilterframecosom": settingFlagFilterframecosom,
       "settingDFSsupport": settingDFSsupport,
       "settingFilterCustomIpAddr": settingFilterCustomIpAddr,
       "settingFilterCustomSubnetMask": settingFilterCustomSubnetMask,
       "bridge-mode": bridge_mode,
       "bridge-modeLinkStatus": bridge_modeLinkStatus,
       "bridge-modeMacAP": bridge_modeMacAP,
       "bridge-modeRSSI": bridge_modeRSSI,
       "bridge-modeRSSIdBm": bridge_modeRSSIdBm,
       "bridge-modeRSSIPercent": bridge_modeRSSIPercent,
       "bridge-modeCurrentTxRate": bridge_modeCurrentTxRate,
       "bridge-WirelessMode": bridge_WirelessMode,
       "bridgeAPFiltering": bridgeAPFiltering,
       "bridgeAPFilteringEnable": bridgeAPFilteringEnable,
       "bridgeAPFilteringMode": bridgeAPFilteringMode,
       "bridgeAPFilteringMACAddress": bridgeAPFilteringMACAddress,
       "bridgeAPFilteringName": bridgeAPFilteringName,
       "bridgeAPFilteringSave": bridgeAPFilteringSave,
       "bridgeAPFilteringDelete": bridgeAPFilteringDelete,
       "bridgeAPFilteringEnableRule": bridgeAPFilteringEnableRule,
       "bridgeAPFilteringDisableRule": bridgeAPFilteringDisableRule,
       "bridgeAPFilteringTable": bridgeAPFilteringTable,
       "bridgeAPFilteringEntry": bridgeAPFilteringEntry,
       "bridgeAPFilteringListId": bridgeAPFilteringListId,
       "bridgeAPFilteringListName": bridgeAPFilteringListName,
       "bridgeAPFilteringListMAC": bridgeAPFilteringListMAC,
       "bridgeAPFilteringListEnable": bridgeAPFilteringListEnable,
       "bridgeRoaming": bridgeRoaming,
       "bridgeRoamingAdvanced": bridgeRoamingAdvanced,
       "bridgeRoamingAdvancedScanThreshold-dbm": bridgeRoamingAdvancedScanThreshold_dbm,
       "bridgeRoamingAdvancedScanThreshold-percent": bridgeRoamingAdvancedScanThreshold_percent,
       "bridgeRoamingAdvancedScanPeriod": bridgeRoamingAdvancedScanPeriod,
       "bridgeRoamingAdvancedScanDuration": bridgeRoamingAdvancedScanDuration,
       "bridgeRoamingAdvancedAPLossDetection": bridgeRoamingAdvancedAPLossDetection,
       "bridgeRoamingEnable": bridgeRoamingEnable,
       "bridgeRoamingRSSIThreshold-dBm": bridgeRoamingRSSIThreshold_dBm,
       "bridgeRoamingRSSIThreshold-percent": bridgeRoamingRSSIThreshold_percent,
       "bridgeChannelList": bridgeChannelList,
       "bridgeWirelessScan": bridgeWirelessScan,
       "bridgeWileressScanTable": bridgeWileressScanTable,
       "bridgeWirelessScanEntry": bridgeWirelessScanEntry,
       "bridgeWirelessScanAPMac": bridgeWirelessScanAPMac,
       "bridgeWirelessScanSSID": bridgeWirelessScanSSID,
       "bridgeWirelessScanChannel": bridgeWirelessScanChannel,
       "bridgeWirelessScanMode": bridgeWirelessScanMode,
       "bridgeWirelessScanSecurity": bridgeWirelessScanSecurity,
       "bridgeWirelessScanRssi": bridgeWirelessScanRssi,
       "bridgeNAT": bridgeNAT,
       "brigeNATStatus": brigeNATStatus,
       "brigeNATEnablePing": brigeNATEnablePing,
       "brigeNATEnableProductWebServer": brigeNATEnableProductWebServer,
       "brigeNATInternalWebServerPort": brigeNATInternalWebServerPort,
       "brigeNATEnableProductSnmpServer": brigeNATEnableProductSnmpServer,
       "brigeNATInternalWebSnmpPort": brigeNATInternalWebSnmpPort,
       "brigeNATWanIpAddrMode": brigeNATWanIpAddrMode,
       "brigeNATWanIpAddr": brigeNATWanIpAddr,
       "brigeNATWanSubnetMask": brigeNATWanSubnetMask,
       "brigeNATWanGateway": brigeNATWanGateway,
       "bridgeNatPortForwarding": bridgeNatPortForwarding,
       "bridgeNatPortForwardingTable": bridgeNatPortForwardingTable,
       "bridgeNatPortForwardingEntry": bridgeNatPortForwardingEntry,
       "bridgeNatPortForwardingListId": bridgeNatPortForwardingListId,
       "bridgeNatPortForwardingListName": bridgeNatPortForwardingListName,
       "bridgeNatPortForwardingListIpAddr": bridgeNatPortForwardingListIpAddr,
       "bridgeNatPortForwardingListPublicTcpPort": bridgeNatPortForwardingListPublicTcpPort,
       "bridgeNatPortForwardingListPrivateTcpPort": bridgeNatPortForwardingListPrivateTcpPort,
       "bridgeNatPortForwardingListPublicUdpPort": bridgeNatPortForwardingListPublicUdpPort,
       "bridgeNatPortForwardingListPrivateUdpPort": bridgeNatPortForwardingListPrivateUdpPort,
       "bridgeNatPortForwardingListEnable": bridgeNatPortForwardingListEnable,
       "bridgeNatPortForwardingName": bridgeNatPortForwardingName,
       "bridgeNatPortForwardingIpAddr": bridgeNatPortForwardingIpAddr,
       "bridgeNatPortForwardingPublicTcpPort": bridgeNatPortForwardingPublicTcpPort,
       "bridgeNatPortForwardingPrivateTcpPort": bridgeNatPortForwardingPrivateTcpPort,
       "bridgeNatPortForwardingPublicUdpPort": bridgeNatPortForwardingPublicUdpPort,
       "bridgeNatPortForwardingPrivateUdpPort": bridgeNatPortForwardingPrivateUdpPort,
       "bridgeNatPortForwardingEnableRule": bridgeNatPortForwardingEnableRule,
       "bridgeNatPortForwardingDisableRule": bridgeNatPortForwardingDisableRule,
       "bridgeNatPortForwardingSaveRule": bridgeNatPortForwardingSaveRule,
       "bridgeNatPortForwardingDeleteRule": bridgeNatPortForwardingDeleteRule,
       "access-point-mode": access_point_mode,
       "apClientTable": apClientTable,
       "apClientEntry": apClientEntry,
       "clientMacAddr": clientMacAddr,
       "client80211Mode": client80211Mode,
       "clientTxRate": clientTxRate,
       "clientRssiPercent": clientRssiPercent,
       "apAutomaticChannel": apAutomaticChannel,
       "apClientCount": apClientCount,
       "apClientFiltering": apClientFiltering,
       "apClientFilteringEnable": apClientFilteringEnable,
       "apClientFilteringMode": apClientFilteringMode,
       "apClientWirelessFiltering": apClientWirelessFiltering,
       "apClientWiredFiltering": apClientWiredFiltering,
       "apClientFilteringMACAddress": apClientFilteringMACAddress,
       "apClientFilteringName": apClientFilteringName,
       "apClientFilteringSave": apClientFilteringSave,
       "apClientFilteringDelete": apClientFilteringDelete,
       "apClientFilteringEnableRule": apClientFilteringEnableRule,
       "apClientFilteringDisableRule": apClientFilteringDisableRule,
       "apClientFilteringTable": apClientFilteringTable,
       "apClientFilteringEntry": apClientFilteringEntry,
       "apClientFilteringListId": apClientFilteringListId,
       "apClientFilteringListName": apClientFilteringListName,
       "apClientFilteringListMAC": apClientFilteringListMAC,
       "apClientFilteringListEnable": apClientFilteringListEnable,
       "wds": wds,
       "apWDSEnable": apWDSEnable,
       "apWDSEnableSTP": apWDSEnableSTP,
       "apWDSMAC1": apWDSMAC1,
       "apWDSMAC2": apWDSMAC2,
       "apWDSMAC3": apWDSMAC3,
       "apWDSMAC4": apWDSMAC4,
       "apWDSMAC5": apWDSMAC5,
       "apWDSMAC6": apWDSMAC6,
       "settingSSIDVisibility": settingSSIDVisibility,
       "enableSTP": enableSTP,
       "lanTimeOutSettings": lanTimeOutSettings,
       "enableLanTimeout": enableLanTimeout,
       "lanTimeoutIPSurvey": lanTimeoutIPSurvey,
       "lanTimeoutMaxProbe": lanTimeoutMaxProbe,
       "lanTimeoutProbeTimeout": lanTimeoutProbeTimeout,
       "lanTimeoutProbeInterval": lanTimeoutProbeInterval,
       "advancedSettings": advancedSettings,
       "longDistanceSettings": longDistanceSettings,
       "enableLongDistance": enableLongDistance,
       "distanceAntennaMeter": distanceAntennaMeter,
       "distanceSlotTime": distanceSlotTime,
       "distanceAckTimeout": distanceAckTimeout,
       "distanceCtsTimeout": distanceCtsTimeout,
       "enable802-11d": enable802_11d,
       "enableIsolateSTA": enableIsolateSTA,
       "administration": administration,
       "adminReset": adminReset,
       "adminResetFactory": adminResetFactory,
       "adminEnableWebServer": adminEnableWebServer,
       "adminAutoSave": adminAutoSave,
       "adminSave": adminSave,
       "os-stat": os_stat,
       "os-statFreeHeap": os_statFreeHeap,
       "os-statTotalHeap": os_statTotalHeap,
       "os-statHeapLowWater": os_statHeapLowWater,
       "os-statNetpageFree": os_statNetpageFree,
       "os-statNetpageLowWater": os_statNetpageLowWater,
       "productSpecific": productSpecific,
       "wlg-aboard": wlg_aboard,
       "wlg-aboard-PW1-state": wlg_aboard_PW1_state,
       "wlg-aboard-PW2-state": wlg_aboard_PW2_state,
       "lanInterface": lanInterface,
       "lanInterfaceIpAddrMode": lanInterfaceIpAddrMode,
       "lanInterfaceIpAddr": lanInterfaceIpAddr,
       "lanInterfaceSubNetMask": lanInterfaceSubNetMask,
       "lanInterfaceGatewayIp": lanInterfaceGatewayIp,
       "lanInterfaceHostName": lanInterfaceHostName,
       "lanInterfaceLocalDomainName": lanInterfaceLocalDomainName,
       "acksysMIB": acksysMIB,
       "acksysProductID": acksysProductID,
       "c-key-management": c_key_management,
       "ckeyManagementCopySettingTo": ckeyManagementCopySettingTo,
       "ckeyManagementCopySettingFrom": ckeyManagementCopySettingFrom,
       "alarmSettings": alarmSettings,
       "alarmSettingsTest": alarmSettingsTest,
       "alarmSettingsPower1Down": alarmSettingsPower1Down,
       "alarmSettingsPower1DownEnable": alarmSettingsPower1DownEnable,
       "alarmSettingsPower1DownEnableAutomaticReset": alarmSettingsPower1DownEnableAutomaticReset,
       "alarmSettingsPower1DownStatus": alarmSettingsPower1DownStatus,
       "alarmSettingsPower2Down": alarmSettingsPower2Down,
       "alarmSettingsPower2DownEnable": alarmSettingsPower2DownEnable,
       "alarmSettingsPower2DownEnableAutomaticReset": alarmSettingsPower2DownEnableAutomaticReset,
       "alarmSettingsPower2DownStatus": alarmSettingsPower2DownStatus,
       "alarmSettingsLan1Down": alarmSettingsLan1Down,
       "alarmSettingsLan1DownEnable": alarmSettingsLan1DownEnable,
       "alarmSettingsLan1DownEnableAutomaticReset": alarmSettingsLan1DownEnableAutomaticReset,
       "alarmSettingsLan1DownStatus": alarmSettingsLan1DownStatus,
       "alarmSettingsLan2Down": alarmSettingsLan2Down,
       "alarmSettingsLan2DownEnable": alarmSettingsLan2DownEnable,
       "alarmSettingsLan2DownEnableAutomaticReset": alarmSettingsLan2DownEnableAutomaticReset,
       "alarmSettingsLan2DownStatus": alarmSettingsLan2DownStatus,
       "alarmSettingsLan3Down": alarmSettingsLan3Down,
       "alarmSettingsLan3DownEnable": alarmSettingsLan3DownEnable,
       "alarmSettingsLan3DownEnableAutomaticReset": alarmSettingsLan3DownEnableAutomaticReset,
       "alarmSettingsLan3DownStatus": alarmSettingsLan3DownStatus,
       "alarmSettingsLan4Down": alarmSettingsLan4Down,
       "alarmSettingsLan4DownEnable": alarmSettingsLan4DownEnable,
       "alarmSettingsLan4DownEnableAutomaticReset": alarmSettingsLan4DownEnableAutomaticReset,
       "alarmSettingsLan4DownStatus": alarmSettingsLan4DownStatus,
       "alarmSettingsLan5Down": alarmSettingsLan5Down,
       "alarmSettingsLan5DownEnable": alarmSettingsLan5DownEnable,
       "alarmSettingsLan5DownEnableAutomaticReset": alarmSettingsLan5DownEnableAutomaticReset,
       "alarmSettingsLan5DownStatus": alarmSettingsLan5DownStatus,
       "alarmSettingsLan6Down": alarmSettingsLan6Down,
       "alarmSettingsLan6DownEnable": alarmSettingsLan6DownEnable,
       "alarmSettingsLan6DownEnableAutomaticReset": alarmSettingsLan6DownEnableAutomaticReset,
       "alarmSettingsLan6DownStatus": alarmSettingsLan6DownStatus,
       "alarmSettingsLan7Down": alarmSettingsLan7Down,
       "alarmSettingsLan7DownEnable": alarmSettingsLan7DownEnable,
       "alarmSettingsLan7DownEnableAutomaticReset": alarmSettingsLan7DownEnableAutomaticReset,
       "alarmSettingsLan7DownStatus": alarmSettingsLan7DownStatus,
       "alarmSettingsLan8Down": alarmSettingsLan8Down,
       "alarmSettingsLan8DownEnable": alarmSettingsLan8DownEnable,
       "alarmSettingsLan8DownEnableAutomaticReset": alarmSettingsLan8DownEnableAutomaticReset,
       "alarmSettingsLan8DownStatus": alarmSettingsLan8DownStatus,
       "alarmSettingsWLANDown": alarmSettingsWLANDown,
       "alarmSettingsWLANDownEnable": alarmSettingsWLANDownEnable,
       "alarmSettingsWLANDownEnableAutomaticReset": alarmSettingsWLANDownEnableAutomaticReset,
       "alarmSettingsWLANDownStatus": alarmSettingsWLANDownStatus,
       "powerStatus": powerStatus,
       "powerStatus-PW1-state": powerStatus_PW1_state,
       "powerStatus-PW2-state": powerStatus_PW2_state}
)
