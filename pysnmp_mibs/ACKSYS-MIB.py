# SNMP MIB module (ACKSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/acksys/ACKSYS-MIB
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acksys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28097)
)
if mibBuilder.loadTexts:
    acksys.setRevisions(
        ("2022-02-18 15:05",
         "2021-07-02 11:13")
    )


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class WifiFlavor(Integer32):
    """Custom type WifiFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              12,
              16)
        )
    )
    namedValues = NamedValues(
        *(("b-only", 1),
          ("g-only", 2),
          ("mixed-b-g", 3),
          ("a-only", 4),
          ("n-g", 10),
          ("n-bg", 11),
          ("n-a", 12),
          ("ac", 16))
    )





class NetifName(OctetString):
    """Custom type NetifName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class SecurityModes(Integer32):
    """Custom type SecurityModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep", 2),
          ("wpa-wpa2-psk", 3),
          ("wpa-wpa2", 4),
          ("sae-wpa3-psk", 5),
          ("wpa3", 6),
          ("owe", 7))
    )





class CellSecurityProtocol(Integer32):
    """Custom type CellSecurityProtocol based on Integer32"""
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
          ("pap", 1),
          ("chap", 2))
    )





class PeapSecurityProtocol(Integer32):
    """Custom type PeapSecurityProtocol based on Integer32"""
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
        *(("peap-pap", 1),
          ("peap-chap", 2),
          ("peap-mschap", 3),
          ("peap-mschapv2", 4))
    )





class WpaVersions(Integer32):
    """Custom type WpaVersions based on Integer32"""
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
        *(("wpa", 1),
          ("wpa2", 2),
          ("wpa-wpa2-mixed", 3),
          ("wpa3", 4),
          ("wpa2-wpa3-mixed", 5))
    )





class CipherTypes(Integer32):
    """Custom type CipherTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("aestkip", 3))
    )





class WepKeys(OctetString):
    """Custom type WepKeys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )





class WifiLevel(Integer32):
    """Custom type WifiLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )





class DisableEnable(Integer32):
    """Custom type DisableEnable based on Integer32"""
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





class TriState(Integer32):
    """Custom type TriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("disable", 1),
          ("enable", 2))
    )





class AsyncSetStatus(Integer32):
    """Custom type AsyncSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("set-init", 0),
          ("set-more", 1),
          ("set-wait", 2),
          ("set-ok", 3),
          ("set-fail", 4))
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class PortId(OctetString):
    """Custom type PortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2





class CellAttachMode(Integer32):
    """Custom type CellAttachMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("reg-hung", 0),
          ("reg-home", 1),
          ("reg-searching", 2),
          ("reg-denied", 3),
          ("reg-noCell", 4),
          ("reg-roaming", 5),
          ("reg-homeSMS", 6),
          ("reg-roamingSMS", 7),
          ("reg-emgOnly", 8),
          ("reg-homeNoCSFB", 9),
          ("reg-roamingNoCSFB", 10))
    )





class CellAccessTech(Integer32):
    """Custom type CellAccessTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("at-gsm", 0),
          ("at-gsmCompact", 1),
          ("at-UTRAN", 2),
          ("at-EGPRS", 3),
          ("at-HSDPA", 4),
          ("at-HSUPA", 5),
          ("at-HSPA", 6),
          ("at-EUTRAN", 7),
          ("at-GSM-IoT", 8),
          ("at-EUTRAN-NB-S1", 9))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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
              4,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("b-only", 1),
          ("g-only", 2),
          ("mixed-b-g", 3),
          ("a-only", 4),
          ("n-g", 10),
          ("n-bg", 11),
          ("n-a", 12))
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


class _SettingTxPower_Type(Integer32):
    """Custom type settingTxPower based on Integer32"""
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


_SettingTxPower_Type.__name__ = "Integer32"
_SettingTxPower_Object = MibScalar
settingTxPower = _SettingTxPower_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 7),
    _SettingTxPower_Type()
)
settingTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    settingTxPower.setStatus("current")


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
_SecurityMode_Type = SecurityModes
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
_SecurityModeWepKey_1_Type = WepKeys
_SecurityModeWepKey_1_Object = MibScalar
securityModeWepKey_1 = _SecurityModeWepKey_1_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 2),
    _SecurityModeWepKey_1_Type()
)
securityModeWepKey_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_1.setStatus("current")
_SecurityModeWepKey_2_Type = WepKeys
_SecurityModeWepKey_2_Object = MibScalar
securityModeWepKey_2 = _SecurityModeWepKey_2_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 3),
    _SecurityModeWepKey_2_Type()
)
securityModeWepKey_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_2.setStatus("current")
_SecurityModeWepKey_3_Type = WepKeys
_SecurityModeWepKey_3_Object = MibScalar
securityModeWepKey_3 = _SecurityModeWepKey_3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 1, 9, 2, 4),
    _SecurityModeWepKey_3_Type()
)
securityModeWepKey_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityModeWepKey_3.setStatus("current")
_SecurityModeWepKey_4_Type = WepKeys
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
_SecurityModeWPARadiusMacAddressAuthentication_Type = DisableEnable
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
_SecurityModeWPARadiusAPMacAddressAuthentication_Type = DisableEnable
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
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type = DisableEnable
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
_SecurityModeWPABackupRadiusMacAddressAuthentication_Type = DisableEnable
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wpa", 1),
          ("wpa2", 2),
          ("wpa3", 3))
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
_SecurityModeWpaCipherType_Type = CipherTypes
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
          ("different-subnet-filtre", 2),
          ("custom-subnet-filtre", 3))
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
    (0, "ACKSYS-MIB", "bridgeAPFilteringListId"),
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
_BridgeAPFilteringListEnable_Type = DisableEnable
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
_BridgeRoamingEnable_Type = DisableEnable
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
    (0, "ACKSYS-MIB", "bridgeWirelessScanAPMac"),
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


class _BridgeWirelessScanSSID_Type(OctetString):
    """Custom type bridgeWirelessScanSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_BridgeWirelessScanSSID_Type.__name__ = "OctetString"
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
    (0, "ACKSYS-MIB", "bridgeNatPortForwardingListId"),
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
    (0, "ACKSYS-MIB", "clientMacAddr"),
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
_ApClientWirelessFiltering_Type = DisableEnable
_ApClientWirelessFiltering_Object = MibScalar
apClientWirelessFiltering = _ApClientWirelessFiltering_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 4, 3),
    _ApClientWirelessFiltering_Type()
)
apClientWirelessFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClientWirelessFiltering.setStatus("current")
_ApClientWiredFiltering_Type = DisableEnable
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
    (0, "ACKSYS-MIB", "apClientFilteringListId"),
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
_ApClientFilteringListEnable_Type = DisableEnable
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
_ApWDSEnable_Type = DisableEnable
_ApWDSEnable_Object = MibScalar
apWDSEnable = _ApWDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 1, 3, 5, 1),
    _ApWDSEnable_Type()
)
apWDSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWDSEnable.setStatus("current")
_ApWDSEnableSTP_Type = DisableEnable
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
_EnableSTP_Type = DisableEnable
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
_EnableLanTimeout_Type = DisableEnable
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
_EnableLongDistance_Type = DisableEnable
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
_Enable802_11d_Type = DisableEnable
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
_AdminEnableWebServer_Type = DisableEnable
_AdminEnableWebServer_Object = MibScalar
adminEnableWebServer = _AdminEnableWebServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 3),
    _AdminEnableWebServer_Type()
)
adminEnableWebServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEnableWebServer.setStatus("current")
_AdminAutoSave_Type = DisableEnable
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("save", 1),
          ("saveRequired", 2),
          ("saveNotRequired", 3))
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


class _AdminApply_Type(Integer32):
    """Custom type adminApply based on Integer32"""
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
          ("applyRequire", 3))
    )


_AdminApply_Type.__name__ = "Integer32"
_AdminApply_Object = MibScalar
adminApply = _AdminApply_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 6),
    _AdminApply_Type()
)
adminApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminApply.setStatus("current")


class _AdminConfigHash_Type(OctetString):
    """Custom type adminConfigHash based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminConfigHash_Type.__name__ = "OctetString"
_AdminConfigHash_Object = MibScalar
adminConfigHash = _AdminConfigHash_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 7),
    _AdminConfigHash_Type()
)
adminConfigHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminConfigHash.setStatus("current")
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8)
)


class _FileTransferAction_Type(Integer32):
    """Custom type fileTransferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2))
    )


_FileTransferAction_Type.__name__ = "Integer32"
_FileTransferAction_Object = MibScalar
fileTransferAction = _FileTransferAction_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 1),
    _FileTransferAction_Type()
)
fileTransferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferAction.setStatus("current")


class _FileTransferType_Type(Integer32):
    """Custom type fileTransferType based on Integer32"""
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
        *(("config", 1),
          ("firmware", 2),
          ("lte-firmware", 3),
          ("wids-config", 4),
          ("ssh-auth-keys", 5))
    )


_FileTransferType_Type.__name__ = "Integer32"
_FileTransferType_Object = MibScalar
fileTransferType = _FileTransferType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 2),
    _FileTransferType_Type()
)
fileTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferType.setStatus("current")
_FileTransferSize_Type = Integer32
_FileTransferSize_Object = MibScalar
fileTransferSize = _FileTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 3),
    _FileTransferSize_Type()
)
fileTransferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferSize.setStatus("current")
_FileTransferIndex_Type = Integer32
_FileTransferIndex_Object = MibScalar
fileTransferIndex = _FileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 4),
    _FileTransferIndex_Type()
)
fileTransferIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferIndex.setStatus("current")
_FileTransferHash_Type = OctetString
_FileTransferHash_Object = MibScalar
fileTransferHash = _FileTransferHash_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 5),
    _FileTransferHash_Type()
)
fileTransferHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferHash.setStatus("current")
_FileTransferChunk_Type = OctetString
_FileTransferChunk_Object = MibScalar
fileTransferChunk = _FileTransferChunk_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 6),
    _FileTransferChunk_Type()
)
fileTransferChunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferChunk.setStatus("current")


class _FileTransferResult_Type(Integer32):
    """Custom type fileTransferResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("in-progress", 2),
          ("nok", 3))
    )


_FileTransferResult_Type.__name__ = "Integer32"
_FileTransferResult_Object = MibScalar
fileTransferResult = _FileTransferResult_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 7),
    _FileTransferResult_Type()
)
fileTransferResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferResult.setStatus("current")
_FileTransferSession_Type = Integer32
_FileTransferSession_Object = MibScalar
fileTransferSession = _FileTransferSession_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 8, 8),
    _FileTransferSession_Type()
)
fileTransferSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferSession.setStatus("current")
_AdminIdentify_Type = Integer32
_AdminIdentify_Object = MibScalar
adminIdentify = _AdminIdentify_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 9),
    _AdminIdentify_Type()
)
adminIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminIdentify.setStatus("current")
_AdminEvents_ObjectIdentity = ObjectIdentity
adminEvents = _AdminEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 10)
)
_AdminEventDisable_Type = OctetString
_AdminEventDisable_Object = MibScalar
adminEventDisable = _AdminEventDisable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 10, 1),
    _AdminEventDisable_Type()
)
adminEventDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEventDisable.setStatus("current")
_AdminEventEnable_Type = OctetString
_AdminEventEnable_Object = MibScalar
adminEventEnable = _AdminEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 10, 2),
    _AdminEventEnable_Type()
)
adminEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEventEnable.setStatus("current")
_AdminEventTrigger_Type = OctetString
_AdminEventTrigger_Object = MibScalar
adminEventTrigger = _AdminEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 10, 3),
    _AdminEventTrigger_Type()
)
adminEventTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEventTrigger.setStatus("current")
_AdminTimeZone_ObjectIdentity = ObjectIdentity
adminTimeZone = _AdminTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 11)
)
_AdminTimeZoneDBVersion_Type = DisplayString
_AdminTimeZoneDBVersion_Object = MibScalar
adminTimeZoneDBVersion = _AdminTimeZoneDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 11, 1),
    _AdminTimeZoneDBVersion_Type()
)
adminTimeZoneDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminTimeZoneDBVersion.setStatus("current")


class _AdminTimeZoneName_Type(OctetString):
    """Custom type adminTimeZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AdminTimeZoneName_Type.__name__ = "OctetString"
_AdminTimeZoneName_Object = MibScalar
adminTimeZoneName = _AdminTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 11, 2),
    _AdminTimeZoneName_Type()
)
adminTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTimeZoneName.setStatus("current")
_AdminSystemDateAndTime_ObjectIdentity = ObjectIdentity
adminSystemDateAndTime = _AdminSystemDateAndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 12)
)
_AdminSystemDateAndTimeLocal_Type = DateAndTime
_AdminSystemDateAndTimeLocal_Object = MibScalar
adminSystemDateAndTimeLocal = _AdminSystemDateAndTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 12, 1),
    _AdminSystemDateAndTimeLocal_Type()
)
adminSystemDateAndTimeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSystemDateAndTimeLocal.setStatus("current")
_AdminSystemDateAndTimeUTC_Type = DateAndTime
_AdminSystemDateAndTimeUTC_Object = MibScalar
adminSystemDateAndTimeUTC = _AdminSystemDateAndTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 2, 12, 2),
    _AdminSystemDateAndTimeUTC_Type()
)
adminSystemDateAndTimeUTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSystemDateAndTimeUTC.setStatus("current")
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
_SerialInterface_ObjectIdentity = ObjectIdentity
serialInterface = _SerialInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6)
)


class _SerialServicetype_Type(Integer32):
    """Custom type serialServicetype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("virtualcom", 1),
          ("modbusTcpSlave", 2),
          ("modbusTcpMaster", 3),
          ("tcpRawPortServer", 4),
          ("tcpRawPortClient", 5),
          ("udpRawPortServer", 6),
          ("serialServiceInvalid", 7))
    )


_SerialServicetype_Type.__name__ = "Integer32"
_SerialServicetype_Object = MibScalar
serialServicetype = _SerialServicetype_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 1),
    _SerialServicetype_Type()
)
serialServicetype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialServicetype.setStatus("current")
_SerialFormat_ObjectIdentity = ObjectIdentity
serialFormat = _SerialFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2)
)
_SerialFormatBaudRate_Type = Integer32
_SerialFormatBaudRate_Object = MibScalar
serialFormatBaudRate = _SerialFormatBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2, 1),
    _SerialFormatBaudRate_Type()
)
serialFormatBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFormatBaudRate.setStatus("current")
_SerialFormatDataBit_Type = Integer32
_SerialFormatDataBit_Object = MibScalar
serialFormatDataBit = _SerialFormatDataBit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2, 2),
    _SerialFormatDataBit_Type()
)
serialFormatDataBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFormatDataBit.setStatus("current")


class _SerialFormatParityBit_Type(Integer32):
    """Custom type serialFormatParityBit based on Integer32"""
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
        *(("none", 1),
          ("odd", 2),
          ("even", 3),
          ("mark", 4),
          ("space", 5))
    )


_SerialFormatParityBit_Type.__name__ = "Integer32"
_SerialFormatParityBit_Object = MibScalar
serialFormatParityBit = _SerialFormatParityBit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2, 3),
    _SerialFormatParityBit_Type()
)
serialFormatParityBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFormatParityBit.setStatus("current")
_SerialFormatStopBit_Type = Integer32
_SerialFormatStopBit_Object = MibScalar
serialFormatStopBit = _SerialFormatStopBit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2, 4),
    _SerialFormatStopBit_Type()
)
serialFormatStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFormatStopBit.setStatus("current")


class _SerialElectricalInterface_Type(Integer32):
    """Custom type serialElectricalInterface based on Integer32"""
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
        *(("rs232", 1),
          ("rs422Master", 2),
          ("rs422Slave", 3),
          ("rs485NoEcho", 4),
          ("rs485echo", 5))
    )


_SerialElectricalInterface_Type.__name__ = "Integer32"
_SerialElectricalInterface_Object = MibScalar
serialElectricalInterface = _SerialElectricalInterface_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 2, 5),
    _SerialElectricalInterface_Type()
)
serialElectricalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialElectricalInterface.setStatus("current")
_SerialSendTriggers_ObjectIdentity = ObjectIdentity
serialSendTriggers = _SerialSendTriggers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3)
)
_SerialSendTriggerCharcount_ObjectIdentity = ObjectIdentity
serialSendTriggerCharcount = _SerialSendTriggerCharcount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 1)
)


class _SendTriggerCharCountEnable_Type(Integer32):
    """Custom type sendTriggerCharCountEnable based on Integer32"""
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


_SendTriggerCharCountEnable_Type.__name__ = "Integer32"
_SendTriggerCharCountEnable_Object = MibScalar
sendTriggerCharCountEnable = _SendTriggerCharCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 1, 1),
    _SendTriggerCharCountEnable_Type()
)
sendTriggerCharCountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerCharCountEnable.setStatus("current")
_SendTriggerCharCountValue_Type = Integer32
_SendTriggerCharCountValue_Object = MibScalar
sendTriggerCharCountValue = _SendTriggerCharCountValue_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 1, 2),
    _SendTriggerCharCountValue_Type()
)
sendTriggerCharCountValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerCharCountValue.setStatus("current")
_SerialSendTriggerIdleDelay_ObjectIdentity = ObjectIdentity
serialSendTriggerIdleDelay = _SerialSendTriggerIdleDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 2)
)


class _SendTriggerIdleDelayEnable_Type(Integer32):
    """Custom type sendTriggerIdleDelayEnable based on Integer32"""
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


_SendTriggerIdleDelayEnable_Type.__name__ = "Integer32"
_SendTriggerIdleDelayEnable_Object = MibScalar
sendTriggerIdleDelayEnable = _SendTriggerIdleDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 2, 1),
    _SendTriggerIdleDelayEnable_Type()
)
sendTriggerIdleDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerIdleDelayEnable.setStatus("current")
_SendTriggerIdleDelayValue_Type = Integer32
_SendTriggerIdleDelayValue_Object = MibScalar
sendTriggerIdleDelayValue = _SendTriggerIdleDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 2, 2),
    _SendTriggerIdleDelayValue_Type()
)
sendTriggerIdleDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerIdleDelayValue.setStatus("current")


class _SendTriggerIdleDelayUnit_Type(Integer32):
    """Custom type sendTriggerIdleDelayUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("charTime", 1),
          ("millisecond", 2))
    )


_SendTriggerIdleDelayUnit_Type.__name__ = "Integer32"
_SendTriggerIdleDelayUnit_Object = MibScalar
sendTriggerIdleDelayUnit = _SendTriggerIdleDelayUnit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 2, 3),
    _SendTriggerIdleDelayUnit_Type()
)
sendTriggerIdleDelayUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerIdleDelayUnit.setStatus("current")
_SerialSendTriggerFrameDelay_ObjectIdentity = ObjectIdentity
serialSendTriggerFrameDelay = _SerialSendTriggerFrameDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 3)
)


class _SendTriggerFrameDelayEnable_Type(Integer32):
    """Custom type sendTriggerFrameDelayEnable based on Integer32"""
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


_SendTriggerFrameDelayEnable_Type.__name__ = "Integer32"
_SendTriggerFrameDelayEnable_Object = MibScalar
sendTriggerFrameDelayEnable = _SendTriggerFrameDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 3, 1),
    _SendTriggerFrameDelayEnable_Type()
)
sendTriggerFrameDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerFrameDelayEnable.setStatus("current")
_SendTriggerFrameDelayValue_Type = Integer32
_SendTriggerFrameDelayValue_Object = MibScalar
sendTriggerFrameDelayValue = _SendTriggerFrameDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 3, 2),
    _SendTriggerFrameDelayValue_Type()
)
sendTriggerFrameDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerFrameDelayValue.setStatus("current")


class _SendTriggerFrameDelayUnit_Type(Integer32):
    """Custom type sendTriggerFrameDelayUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("charTime", 1),
          ("millisecond", 2))
    )


_SendTriggerFrameDelayUnit_Type.__name__ = "Integer32"
_SendTriggerFrameDelayUnit_Object = MibScalar
sendTriggerFrameDelayUnit = _SendTriggerFrameDelayUnit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 3, 3, 3),
    _SendTriggerFrameDelayUnit_Type()
)
sendTriggerFrameDelayUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTriggerFrameDelayUnit.setStatus("current")
_SerialServiceVirtualCom_ObjectIdentity = ObjectIdentity
serialServiceVirtualCom = _SerialServiceVirtualCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 4)
)
_SerialServiceModbusSlave_ObjectIdentity = ObjectIdentity
serialServiceModbusSlave = _SerialServiceModbusSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 5)
)


class _ModbusSlaveFormat_Type(Integer32):
    """Custom type modbusSlaveFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("rtu", 2))
    )


_ModbusSlaveFormat_Type.__name__ = "Integer32"
_ModbusSlaveFormat_Object = MibScalar
modbusSlaveFormat = _ModbusSlaveFormat_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 5, 1),
    _ModbusSlaveFormat_Type()
)
modbusSlaveFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusSlaveFormat.setStatus("current")
_ModbusSlaveSerialTransactionTimeout_Type = Integer32
_ModbusSlaveSerialTransactionTimeout_Object = MibScalar
modbusSlaveSerialTransactionTimeout = _ModbusSlaveSerialTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 5, 2),
    _ModbusSlaveSerialTransactionTimeout_Type()
)
modbusSlaveSerialTransactionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusSlaveSerialTransactionTimeout.setStatus("current")
_SerialServiceModbusMaster_ObjectIdentity = ObjectIdentity
serialServiceModbusMaster = _SerialServiceModbusMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6)
)


class _ModbusMasterFormat_Type(Integer32):
    """Custom type modbusMasterFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("rtu", 2))
    )


_ModbusMasterFormat_Type.__name__ = "Integer32"
_ModbusMasterFormat_Object = MibScalar
modbusMasterFormat = _ModbusMasterFormat_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 1),
    _ModbusMasterFormat_Type()
)
modbusMasterFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusMasterFormat.setStatus("current")
_ModbusMasterTransactionTimeout_Type = Integer32
_ModbusMasterTransactionTimeout_Object = MibScalar
modbusMasterTransactionTimeout = _ModbusMasterTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 2),
    _ModbusMasterTransactionTimeout_Type()
)
modbusMasterTransactionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusMasterTransactionTimeout.setStatus("current")
_ModbusMasterForwardingTable_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable = _ModbusMasterForwardingTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3)
)
_ModbusMasterForwardingTable_Rule1_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule1 = _ModbusMasterForwardingTable_Rule1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1)
)
_MmForwardingTable_Rule1_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule1_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule1_FirstLocalAddr = _MmForwardingTable_Rule1_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1, 1),
    _MmForwardingTable_Rule1_FirstLocalAddr_Type()
)
mmForwardingTable_Rule1_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule1_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule1_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule1_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule1_LastLocalAddr = _MmForwardingTable_Rule1_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1, 2),
    _MmForwardingTable_Rule1_LastLocalAddr_Type()
)
mmForwardingTable_Rule1_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule1_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule1_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule1_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule1_FirstRemoteAddr = _MmForwardingTable_Rule1_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1, 3),
    _MmForwardingTable_Rule1_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule1_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule1_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule1_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule1_SlaveIpAddrIncrement = _MmForwardingTable_Rule1_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1, 4),
    _MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule1_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule1_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule1_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule1_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule1_SlaveIpAddr = _MmForwardingTable_Rule1_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 1, 5),
    _MmForwardingTable_Rule1_SlaveIpAddr_Type()
)
mmForwardingTable_Rule1_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule1_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule2_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule2 = _ModbusMasterForwardingTable_Rule2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2)
)
_MmForwardingTable_Rule2_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule2_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule2_FirstLocalAddr = _MmForwardingTable_Rule2_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2, 1),
    _MmForwardingTable_Rule2_FirstLocalAddr_Type()
)
mmForwardingTable_Rule2_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule2_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule2_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule2_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule2_LastLocalAddr = _MmForwardingTable_Rule2_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2, 2),
    _MmForwardingTable_Rule2_LastLocalAddr_Type()
)
mmForwardingTable_Rule2_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule2_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule2_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule2_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule2_FirstRemoteAddr = _MmForwardingTable_Rule2_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2, 3),
    _MmForwardingTable_Rule2_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule2_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule2_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule2_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule2_SlaveIpAddrIncrement = _MmForwardingTable_Rule2_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2, 4),
    _MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule2_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule2_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule2_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule2_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule2_SlaveIpAddr = _MmForwardingTable_Rule2_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 2, 5),
    _MmForwardingTable_Rule2_SlaveIpAddr_Type()
)
mmForwardingTable_Rule2_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule2_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule3_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule3 = _ModbusMasterForwardingTable_Rule3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3)
)
_MmForwardingTable_Rule3_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule3_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule3_FirstLocalAddr = _MmForwardingTable_Rule3_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3, 1),
    _MmForwardingTable_Rule3_FirstLocalAddr_Type()
)
mmForwardingTable_Rule3_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule3_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule3_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule3_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule3_LastLocalAddr = _MmForwardingTable_Rule3_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3, 2),
    _MmForwardingTable_Rule3_LastLocalAddr_Type()
)
mmForwardingTable_Rule3_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule3_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule3_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule3_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule3_FirstRemoteAddr = _MmForwardingTable_Rule3_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3, 3),
    _MmForwardingTable_Rule3_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule3_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule3_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule3_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule3_SlaveIpAddrIncrement = _MmForwardingTable_Rule3_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3, 4),
    _MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule3_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule3_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule3_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule3_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule3_SlaveIpAddr = _MmForwardingTable_Rule3_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 3, 5),
    _MmForwardingTable_Rule3_SlaveIpAddr_Type()
)
mmForwardingTable_Rule3_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule3_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule4_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule4 = _ModbusMasterForwardingTable_Rule4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4)
)
_MmForwardingTable_Rule4_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule4_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule4_FirstLocalAddr = _MmForwardingTable_Rule4_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4, 1),
    _MmForwardingTable_Rule4_FirstLocalAddr_Type()
)
mmForwardingTable_Rule4_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule4_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule4_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule4_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule4_LastLocalAddr = _MmForwardingTable_Rule4_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4, 2),
    _MmForwardingTable_Rule4_LastLocalAddr_Type()
)
mmForwardingTable_Rule4_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule4_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule4_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule4_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule4_FirstRemoteAddr = _MmForwardingTable_Rule4_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4, 3),
    _MmForwardingTable_Rule4_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule4_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule4_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule4_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule4_SlaveIpAddrIncrement = _MmForwardingTable_Rule4_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4, 4),
    _MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule4_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule4_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule4_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule4_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule4_SlaveIpAddr = _MmForwardingTable_Rule4_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 4, 5),
    _MmForwardingTable_Rule4_SlaveIpAddr_Type()
)
mmForwardingTable_Rule4_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule4_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule5_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule5 = _ModbusMasterForwardingTable_Rule5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5)
)
_MmForwardingTable_Rule5_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule5_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule5_FirstLocalAddr = _MmForwardingTable_Rule5_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5, 1),
    _MmForwardingTable_Rule5_FirstLocalAddr_Type()
)
mmForwardingTable_Rule5_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule5_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule5_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule5_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule5_LastLocalAddr = _MmForwardingTable_Rule5_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5, 2),
    _MmForwardingTable_Rule5_LastLocalAddr_Type()
)
mmForwardingTable_Rule5_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule5_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule5_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule5_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule5_FirstRemoteAddr = _MmForwardingTable_Rule5_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5, 3),
    _MmForwardingTable_Rule5_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule5_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule5_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule5_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule5_SlaveIpAddrIncrement = _MmForwardingTable_Rule5_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5, 4),
    _MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule5_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule5_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule5_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule5_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule5_SlaveIpAddr = _MmForwardingTable_Rule5_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 5, 5),
    _MmForwardingTable_Rule5_SlaveIpAddr_Type()
)
mmForwardingTable_Rule5_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule5_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule6_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule6 = _ModbusMasterForwardingTable_Rule6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6)
)
_MmForwardingTable_Rule6_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule6_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule6_FirstLocalAddr = _MmForwardingTable_Rule6_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6, 1),
    _MmForwardingTable_Rule6_FirstLocalAddr_Type()
)
mmForwardingTable_Rule6_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule6_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule6_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule6_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule6_LastLocalAddr = _MmForwardingTable_Rule6_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6, 2),
    _MmForwardingTable_Rule6_LastLocalAddr_Type()
)
mmForwardingTable_Rule6_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule6_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule6_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule6_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule6_FirstRemoteAddr = _MmForwardingTable_Rule6_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6, 3),
    _MmForwardingTable_Rule6_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule6_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule6_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule6_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule6_SlaveIpAddrIncrement = _MmForwardingTable_Rule6_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6, 4),
    _MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule6_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule6_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule6_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule6_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule6_SlaveIpAddr = _MmForwardingTable_Rule6_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 6, 5),
    _MmForwardingTable_Rule6_SlaveIpAddr_Type()
)
mmForwardingTable_Rule6_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule6_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule7_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule7 = _ModbusMasterForwardingTable_Rule7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7)
)
_MmForwardingTable_Rule7_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule7_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule7_FirstLocalAddr = _MmForwardingTable_Rule7_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7, 1),
    _MmForwardingTable_Rule7_FirstLocalAddr_Type()
)
mmForwardingTable_Rule7_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule7_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule7_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule7_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule7_LastLocalAddr = _MmForwardingTable_Rule7_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7, 2),
    _MmForwardingTable_Rule7_LastLocalAddr_Type()
)
mmForwardingTable_Rule7_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule7_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule7_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule7_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule7_FirstRemoteAddr = _MmForwardingTable_Rule7_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7, 3),
    _MmForwardingTable_Rule7_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule7_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule7_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule7_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule7_SlaveIpAddrIncrement = _MmForwardingTable_Rule7_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7, 4),
    _MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule7_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule7_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule7_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule7_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule7_SlaveIpAddr = _MmForwardingTable_Rule7_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 7, 5),
    _MmForwardingTable_Rule7_SlaveIpAddr_Type()
)
mmForwardingTable_Rule7_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule7_SlaveIpAddr.setStatus("current")
_ModbusMasterForwardingTable_Rule8_ObjectIdentity = ObjectIdentity
modbusMasterForwardingTable_Rule8 = _ModbusMasterForwardingTable_Rule8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8)
)
_MmForwardingTable_Rule8_FirstLocalAddr_Type = Integer32
_MmForwardingTable_Rule8_FirstLocalAddr_Object = MibScalar
mmForwardingTable_Rule8_FirstLocalAddr = _MmForwardingTable_Rule8_FirstLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8, 1),
    _MmForwardingTable_Rule8_FirstLocalAddr_Type()
)
mmForwardingTable_Rule8_FirstLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule8_FirstLocalAddr.setStatus("current")
_MmForwardingTable_Rule8_LastLocalAddr_Type = Integer32
_MmForwardingTable_Rule8_LastLocalAddr_Object = MibScalar
mmForwardingTable_Rule8_LastLocalAddr = _MmForwardingTable_Rule8_LastLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8, 2),
    _MmForwardingTable_Rule8_LastLocalAddr_Type()
)
mmForwardingTable_Rule8_LastLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule8_LastLocalAddr.setStatus("current")
_MmForwardingTable_Rule8_FirstRemoteAddr_Type = Integer32
_MmForwardingTable_Rule8_FirstRemoteAddr_Object = MibScalar
mmForwardingTable_Rule8_FirstRemoteAddr = _MmForwardingTable_Rule8_FirstRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8, 3),
    _MmForwardingTable_Rule8_FirstRemoteAddr_Type()
)
mmForwardingTable_Rule8_FirstRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule8_FirstRemoteAddr.setStatus("current")


class _MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type(Integer32):
    """Custom type mmForwardingTable_Rule8_SlaveIpAddrIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type.__name__ = "Integer32"
_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Object = MibScalar
mmForwardingTable_Rule8_SlaveIpAddrIncrement = _MmForwardingTable_Rule8_SlaveIpAddrIncrement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8, 4),
    _MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type()
)
mmForwardingTable_Rule8_SlaveIpAddrIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule8_SlaveIpAddrIncrement.setStatus("current")
_MmForwardingTable_Rule8_SlaveIpAddr_Type = IpAddress
_MmForwardingTable_Rule8_SlaveIpAddr_Object = MibScalar
mmForwardingTable_Rule8_SlaveIpAddr = _MmForwardingTable_Rule8_SlaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 6, 3, 8, 5),
    _MmForwardingTable_Rule8_SlaveIpAddr_Type()
)
mmForwardingTable_Rule8_SlaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmForwardingTable_Rule8_SlaveIpAddr.setStatus("current")
_SerialServiceTcpRawPortServer_ObjectIdentity = ObjectIdentity
serialServiceTcpRawPortServer = _SerialServiceTcpRawPortServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7)
)
_TcpRawServerSerialExtraConfig_ObjectIdentity = ObjectIdentity
tcpRawServerSerialExtraConfig = _TcpRawServerSerialExtraConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1)
)


class _TrsExtraConfigDTR_Type(Integer32):
    """Custom type trsExtraConfigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("tcpConnected", 2),
          ("inputFlow", 4),
          ("low", 5),
          ("high", 6))
    )


_TrsExtraConfigDTR_Type.__name__ = "Integer32"
_TrsExtraConfigDTR_Object = MibScalar
trsExtraConfigDTR = _TrsExtraConfigDTR_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 1),
    _TrsExtraConfigDTR_Type()
)
trsExtraConfigDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigDTR.setStatus("current")


class _TrsExtraConfigRTS_Type(Integer32):
    """Custom type trsExtraConfigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("modem", 2),
          ("inputFlow", 4),
          ("low", 5),
          ("high", 6))
    )


_TrsExtraConfigRTS_Type.__name__ = "Integer32"
_TrsExtraConfigRTS_Object = MibScalar
trsExtraConfigRTS = _TrsExtraConfigRTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 2),
    _TrsExtraConfigRTS_Type()
)
trsExtraConfigRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigRTS.setStatus("current")


class _TrsExtraConfigDSR_Type(Integer32):
    """Custom type trsExtraConfigDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("acceptCall", 2))
    )


_TrsExtraConfigDSR_Type.__name__ = "Integer32"
_TrsExtraConfigDSR_Object = MibScalar
trsExtraConfigDSR = _TrsExtraConfigDSR_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 3),
    _TrsExtraConfigDSR_Type()
)
trsExtraConfigDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigDSR.setStatus("current")


class _TrsExtraConfigCTS_Type(Integer32):
    """Custom type trsExtraConfigCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("outputFlow", 4))
    )


_TrsExtraConfigCTS_Type.__name__ = "Integer32"
_TrsExtraConfigCTS_Object = MibScalar
trsExtraConfigCTS = _TrsExtraConfigCTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 4),
    _TrsExtraConfigCTS_Type()
)
trsExtraConfigCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigCTS.setStatus("current")


class _TrsExtraConfigDCD_Type(Integer32):
    """Custom type trsExtraConfigDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("rxData", 2))
    )


_TrsExtraConfigDCD_Type.__name__ = "Integer32"
_TrsExtraConfigDCD_Object = MibScalar
trsExtraConfigDCD = _TrsExtraConfigDCD_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 5),
    _TrsExtraConfigDCD_Type()
)
trsExtraConfigDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigDCD.setStatus("current")


class _TrsExtraConfigXonXoff_Type(Integer32):
    """Custom type trsExtraConfigXonXoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("flowControl", 7))
    )


_TrsExtraConfigXonXoff_Type.__name__ = "Integer32"
_TrsExtraConfigXonXoff_Object = MibScalar
trsExtraConfigXonXoff = _TrsExtraConfigXonXoff_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 7, 1, 6),
    _TrsExtraConfigXonXoff_Type()
)
trsExtraConfigXonXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsExtraConfigXonXoff.setStatus("current")
_SerialServiceTcpRawPortClient_ObjectIdentity = ObjectIdentity
serialServiceTcpRawPortClient = _SerialServiceTcpRawPortClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8)
)
_TcpRawClientSerialExtraConfig_ObjectIdentity = ObjectIdentity
tcpRawClientSerialExtraConfig = _TcpRawClientSerialExtraConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1)
)


class _TrcExtraConfigDTR_Type(Integer32):
    """Custom type trcExtraConfigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("low", 5),
          ("high", 6))
    )


_TrcExtraConfigDTR_Type.__name__ = "Integer32"
_TrcExtraConfigDTR_Object = MibScalar
trcExtraConfigDTR = _TrcExtraConfigDTR_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1, 1),
    _TrcExtraConfigDTR_Type()
)
trcExtraConfigDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcExtraConfigDTR.setStatus("current")


class _TrcExtraConfigRTS_Type(Integer32):
    """Custom type trcExtraConfigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("modem", 2),
          ("inputFlow", 4),
          ("low", 5),
          ("high", 6))
    )


_TrcExtraConfigRTS_Type.__name__ = "Integer32"
_TrcExtraConfigRTS_Object = MibScalar
trcExtraConfigRTS = _TrcExtraConfigRTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1, 2),
    _TrcExtraConfigRTS_Type()
)
trcExtraConfigRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcExtraConfigRTS.setStatus("current")


class _TrcExtraConfigCTS_Type(Integer32):
    """Custom type trcExtraConfigCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("outputFlow", 4))
    )


_TrcExtraConfigCTS_Type.__name__ = "Integer32"
_TrcExtraConfigCTS_Object = MibScalar
trcExtraConfigCTS = _TrcExtraConfigCTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1, 4),
    _TrcExtraConfigCTS_Type()
)
trcExtraConfigCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcExtraConfigCTS.setStatus("current")


class _TrcExtraConfigDCD_Type(Integer32):
    """Custom type trcExtraConfigDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("rxData", 2))
    )


_TrcExtraConfigDCD_Type.__name__ = "Integer32"
_TrcExtraConfigDCD_Object = MibScalar
trcExtraConfigDCD = _TrcExtraConfigDCD_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1, 5),
    _TrcExtraConfigDCD_Type()
)
trcExtraConfigDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcExtraConfigDCD.setStatus("current")


class _TrcExtraConfigXonXoff_Type(Integer32):
    """Custom type trcExtraConfigXonXoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("flowControl", 7))
    )


_TrcExtraConfigXonXoff_Type.__name__ = "Integer32"
_TrcExtraConfigXonXoff_Object = MibScalar
trcExtraConfigXonXoff = _TrcExtraConfigXonXoff_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 1, 6),
    _TrcExtraConfigXonXoff_Type()
)
trcExtraConfigXonXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcExtraConfigXonXoff.setStatus("current")
_TcpRawClientConnectionTimeout_Type = Integer32
_TcpRawClientConnectionTimeout_Object = MibScalar
tcpRawClientConnectionTimeout = _TcpRawClientConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 4),
    _TcpRawClientConnectionTimeout_Type()
)
tcpRawClientConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawClientConnectionTimeout.setStatus("current")
_TcpRawClientPollPeriode_Type = Integer32
_TcpRawClientPollPeriode_Object = MibScalar
tcpRawClientPollPeriode = _TcpRawClientPollPeriode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 5),
    _TcpRawClientPollPeriode_Type()
)
tcpRawClientPollPeriode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawClientPollPeriode.setStatus("current")


class _TcpRawClientDSRUse_Type(Integer32):
    """Custom type tcpRawClientDSRUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("graceful", 2),
          ("fast", 3))
    )


_TcpRawClientDSRUse_Type.__name__ = "Integer32"
_TcpRawClientDSRUse_Object = MibScalar
tcpRawClientDSRUse = _TcpRawClientDSRUse_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 6),
    _TcpRawClientDSRUse_Type()
)
tcpRawClientDSRUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawClientDSRUse.setStatus("current")
_TcpRawClientRemoteServers_ObjectIdentity = ObjectIdentity
tcpRawClientRemoteServers = _TcpRawClientRemoteServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7)
)
_TcpRawClientServer1_ObjectIdentity = ObjectIdentity
tcpRawClientServer1 = _TcpRawClientServer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 1)
)
_TcpRawClienServer1_IpAddress_Type = IpAddress
_TcpRawClienServer1_IpAddress_Object = MibScalar
tcpRawClienServer1_IpAddress = _TcpRawClienServer1_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 1, 1),
    _TcpRawClienServer1_IpAddress_Type()
)
tcpRawClienServer1_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawClienServer1_IpAddress.setStatus("current")
_TcpRawclientServer1_TcpPort_Type = Integer32
_TcpRawclientServer1_TcpPort_Object = MibScalar
tcpRawclientServer1_TcpPort = _TcpRawclientServer1_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 1, 2),
    _TcpRawclientServer1_TcpPort_Type()
)
tcpRawclientServer1_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer1_TcpPort.setStatus("current")
_TcpRawClientServer2_ObjectIdentity = ObjectIdentity
tcpRawClientServer2 = _TcpRawClientServer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 2)
)
_TcpRawclientServer2_IpAddress_Type = IpAddress
_TcpRawclientServer2_IpAddress_Object = MibScalar
tcpRawclientServer2_IpAddress = _TcpRawclientServer2_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 2, 1),
    _TcpRawclientServer2_IpAddress_Type()
)
tcpRawclientServer2_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer2_IpAddress.setStatus("current")
_TcpRawclientServer2_TcpPort_Type = Integer32
_TcpRawclientServer2_TcpPort_Object = MibScalar
tcpRawclientServer2_TcpPort = _TcpRawclientServer2_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 2, 2),
    _TcpRawclientServer2_TcpPort_Type()
)
tcpRawclientServer2_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer2_TcpPort.setStatus("current")
_TcpRawClientServer3_ObjectIdentity = ObjectIdentity
tcpRawClientServer3 = _TcpRawClientServer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 3)
)
_TcpRawclientServer3_IpAddress_Type = IpAddress
_TcpRawclientServer3_IpAddress_Object = MibScalar
tcpRawclientServer3_IpAddress = _TcpRawclientServer3_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 3, 1),
    _TcpRawclientServer3_IpAddress_Type()
)
tcpRawclientServer3_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer3_IpAddress.setStatus("current")
_TcpRawclientServer3_TcpPort_Type = Integer32
_TcpRawclientServer3_TcpPort_Object = MibScalar
tcpRawclientServer3_TcpPort = _TcpRawclientServer3_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 3, 2),
    _TcpRawclientServer3_TcpPort_Type()
)
tcpRawclientServer3_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer3_TcpPort.setStatus("current")
_TcpRawClientServer4_ObjectIdentity = ObjectIdentity
tcpRawClientServer4 = _TcpRawClientServer4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 4)
)
_TcpRawclientServer4_IpAddress_Type = IpAddress
_TcpRawclientServer4_IpAddress_Object = MibScalar
tcpRawclientServer4_IpAddress = _TcpRawclientServer4_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 4, 1),
    _TcpRawclientServer4_IpAddress_Type()
)
tcpRawclientServer4_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer4_IpAddress.setStatus("current")
_TcpRawclientServer4_TcpPort_Type = Integer32
_TcpRawclientServer4_TcpPort_Object = MibScalar
tcpRawclientServer4_TcpPort = _TcpRawclientServer4_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 4, 2),
    _TcpRawclientServer4_TcpPort_Type()
)
tcpRawclientServer4_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer4_TcpPort.setStatus("current")
_TcpRawClientServer5_ObjectIdentity = ObjectIdentity
tcpRawClientServer5 = _TcpRawClientServer5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 5)
)
_TcpRawclientServer5_IpAddress_Type = IpAddress
_TcpRawclientServer5_IpAddress_Object = MibScalar
tcpRawclientServer5_IpAddress = _TcpRawclientServer5_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 5, 1),
    _TcpRawclientServer5_IpAddress_Type()
)
tcpRawclientServer5_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer5_IpAddress.setStatus("current")
_TcpRawclientServer5_TcpPort_Type = Integer32
_TcpRawclientServer5_TcpPort_Object = MibScalar
tcpRawclientServer5_TcpPort = _TcpRawclientServer5_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 5, 2),
    _TcpRawclientServer5_TcpPort_Type()
)
tcpRawclientServer5_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer5_TcpPort.setStatus("current")
_TcpRawClientServer6_ObjectIdentity = ObjectIdentity
tcpRawClientServer6 = _TcpRawClientServer6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 6)
)
_TcpRawclientServer6_IpAddress_Type = IpAddress
_TcpRawclientServer6_IpAddress_Object = MibScalar
tcpRawclientServer6_IpAddress = _TcpRawclientServer6_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 6, 1),
    _TcpRawclientServer6_IpAddress_Type()
)
tcpRawclientServer6_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer6_IpAddress.setStatus("current")
_TcpRawclientServer6_TcpPort_Type = Integer32
_TcpRawclientServer6_TcpPort_Object = MibScalar
tcpRawclientServer6_TcpPort = _TcpRawclientServer6_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 6, 2),
    _TcpRawclientServer6_TcpPort_Type()
)
tcpRawclientServer6_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer6_TcpPort.setStatus("current")
_TcpRawClientServer7_ObjectIdentity = ObjectIdentity
tcpRawClientServer7 = _TcpRawClientServer7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 7)
)
_TcpRawclientServer7_IpAddress_Type = IpAddress
_TcpRawclientServer7_IpAddress_Object = MibScalar
tcpRawclientServer7_IpAddress = _TcpRawclientServer7_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 7, 1),
    _TcpRawclientServer7_IpAddress_Type()
)
tcpRawclientServer7_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer7_IpAddress.setStatus("current")
_TcpRawclientServer7_TcpPort_Type = Integer32
_TcpRawclientServer7_TcpPort_Object = MibScalar
tcpRawclientServer7_TcpPort = _TcpRawclientServer7_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 7, 2),
    _TcpRawclientServer7_TcpPort_Type()
)
tcpRawclientServer7_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer7_TcpPort.setStatus("current")
_TcpRawClientServer8_ObjectIdentity = ObjectIdentity
tcpRawClientServer8 = _TcpRawClientServer8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 8)
)
_TcpRawclientServer8_IpAddress_Type = IpAddress
_TcpRawclientServer8_IpAddress_Object = MibScalar
tcpRawclientServer8_IpAddress = _TcpRawclientServer8_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 8, 1),
    _TcpRawclientServer8_IpAddress_Type()
)
tcpRawclientServer8_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer8_IpAddress.setStatus("current")
_TcpRawclientServer8_TcpPort_Type = Integer32
_TcpRawclientServer8_TcpPort_Object = MibScalar
tcpRawclientServer8_TcpPort = _TcpRawclientServer8_TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 8, 7, 8, 2),
    _TcpRawclientServer8_TcpPort_Type()
)
tcpRawclientServer8_TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRawclientServer8_TcpPort.setStatus("current")
_SerialServiceUdpRawPortServer_ObjectIdentity = ObjectIdentity
serialServiceUdpRawPortServer = _SerialServiceUdpRawPortServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9)
)
_UdpRawServerSerialExtraConfig_ObjectIdentity = ObjectIdentity
udpRawServerSerialExtraConfig = _UdpRawServerSerialExtraConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 1)
)


class _UrsExtraConfigDTR_Type(Integer32):
    """Custom type ursExtraConfigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("low", 5),
          ("high", 6))
    )


_UrsExtraConfigDTR_Type.__name__ = "Integer32"
_UrsExtraConfigDTR_Object = MibScalar
ursExtraConfigDTR = _UrsExtraConfigDTR_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 1, 1),
    _UrsExtraConfigDTR_Type()
)
ursExtraConfigDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ursExtraConfigDTR.setStatus("current")


class _UrsExtraConfigRTS_Type(Integer32):
    """Custom type ursExtraConfigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("modem", 2),
          ("inputFlow", 4),
          ("low", 5),
          ("high", 6))
    )


_UrsExtraConfigRTS_Type.__name__ = "Integer32"
_UrsExtraConfigRTS_Object = MibScalar
ursExtraConfigRTS = _UrsExtraConfigRTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 1, 2),
    _UrsExtraConfigRTS_Type()
)
ursExtraConfigRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ursExtraConfigRTS.setStatus("current")


class _UrsExtraConfigCTS_Type(Integer32):
    """Custom type ursExtraConfigCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("outputFlow", 4))
    )


_UrsExtraConfigCTS_Type.__name__ = "Integer32"
_UrsExtraConfigCTS_Object = MibScalar
ursExtraConfigCTS = _UrsExtraConfigCTS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 1, 3),
    _UrsExtraConfigCTS_Type()
)
ursExtraConfigCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ursExtraConfigCTS.setStatus("current")


class _UrsExtraConfigXonXoff_Type(Integer32):
    """Custom type ursExtraConfigXonXoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("flowControl", 7))
    )


_UrsExtraConfigXonXoff_Type.__name__ = "Integer32"
_UrsExtraConfigXonXoff_Object = MibScalar
ursExtraConfigXonXoff = _UrsExtraConfigXonXoff_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 1, 4),
    _UrsExtraConfigXonXoff_Type()
)
ursExtraConfigXonXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ursExtraConfigXonXoff.setStatus("current")
_UdpRawServerRemoteIP_Type = IpAddress
_UdpRawServerRemoteIP_Object = MibScalar
udpRawServerRemoteIP = _UdpRawServerRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 2),
    _UdpRawServerRemoteIP_Type()
)
udpRawServerRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpRawServerRemoteIP.setStatus("current")
_UdpRawServerRemotePort_Type = Integer32
_UdpRawServerRemotePort_Object = MibScalar
udpRawServerRemotePort = _UdpRawServerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 3),
    _UdpRawServerRemotePort_Type()
)
udpRawServerRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpRawServerRemotePort.setStatus("current")
_UdpRawServerLocalPort_Type = Integer32
_UdpRawServerLocalPort_Object = MibScalar
udpRawServerLocalPort = _UdpRawServerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 1, 6, 9, 4),
    _UdpRawServerLocalPort_Type()
)
udpRawServerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpRawServerLocalPort.setStatus("current")
_AcksysInternals_ObjectIdentity = ObjectIdentity
acksysInternals = _AcksysInternals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 2)
)
_InternalUniqueID_Type = PhysAddress
_InternalUniqueID_Object = MibScalar
internalUniqueID = _InternalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 1),
    _InternalUniqueID_Type()
)
internalUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalUniqueID.setStatus("current")
_InternalSerial_Type = Integer32
_InternalSerial_Object = MibScalar
internalSerial = _InternalSerial_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 2),
    _InternalSerial_Type()
)
internalSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSerial.setStatus("current")
_InternalWlanChange_Type = Integer32
_InternalWlanChange_Object = MibScalar
internalWlanChange = _InternalWlanChange_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 3),
    _InternalWlanChange_Type()
)
internalWlanChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalWlanChange.setStatus("current")
_InternalRadioChange_Type = Integer32
_InternalRadioChange_Object = MibScalar
internalRadioChange = _InternalRadioChange_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 4),
    _InternalRadioChange_Type()
)
internalRadioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalRadioChange.setStatus("current")
_InternalSerialTest_Type = Integer32
_InternalSerialTest_Object = MibScalar
internalSerialTest = _InternalSerialTest_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 5),
    _InternalSerialTest_Type()
)
internalSerialTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalSerialTest.setStatus("current")
_InternalSerialTestResult_Type = Integer32
_InternalSerialTestResult_Object = MibScalar
internalSerialTestResult = _InternalSerialTestResult_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 6),
    _InternalSerialTestResult_Type()
)
internalSerialTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSerialTestResult.setStatus("current")
_InternalAlarmSwitch_Type = Integer32
_InternalAlarmSwitch_Object = MibScalar
internalAlarmSwitch = _InternalAlarmSwitch_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 7),
    _InternalAlarmSwitch_Type()
)
internalAlarmSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalAlarmSwitch.setStatus("current")
_InternalDigitalInput_Type = Integer32
_InternalDigitalInput_Object = MibScalar
internalDigitalInput = _InternalDigitalInput_Object(
    (1, 3, 6, 1, 4, 1, 28097, 2, 8),
    _InternalDigitalInput_Type()
)
internalDigitalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalDigitalInput.setStatus("current")


class _AcksysProductID_Type(Integer32):
    """Custom type acksysProductID based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              18,
              19,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              35,
              36,
              37,
              38,
              45)
        )
    )
    namedValues = NamedValues(
        *(("wlg-link", 1),
          ("wlg-aboard-n", 2),
          ("wlg-link-v2", 3),
          ("wlg-aboard-n-v2", 4),
          ("wlg-switch", 5),
          ("wlg-dongle-oem", 6),
          ("wlg-dongle", 7),
          ("msw-aboard", 8),
          ("wlg-xroad-n", 9),
          ("wlg-xroad-s", 10),
          ("wlg-ida-n", 11),
          ("wlg-ida-s", 12),
          ("wlg-xroad-np", 13),
          ("wlg-ida-np", 14),
          ("m340-wc", 18),
          ("wlg-aboard-npi-v3", 19),
          ("wln-aboard", 22),
          ("wln-aboard-n", 23),
          ("wln-aboard-24", 24),
          ("wln-aboard-48", 25),
          ("wln-aboard-72", 26),
          ("wln-aboard-110", 27),
          ("wln-link-oem-rj", 28),
          ("wln-link-oem-ttl", 29),
          ("wln-xroad", 30),
          ("wln-xroad-v2", 31),
          ("wlg-link-v3", 32),
          ("wlg-4lan", 33),
          ("wln-railbox-1", 35),
          ("wln-railbox-1p", 36),
          ("wln-railbox-2", 37),
          ("wln-railbox-2p", 38),
          ("wln-link-oem-ttl-v2", 45))
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
_CkeyManagementErase_Type = Integer32
_CkeyManagementErase_Object = MibScalar
ckeyManagementErase = _CkeyManagementErase_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 3),
    _CkeyManagementErase_Type()
)
ckeyManagementErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementErase.setStatus("current")


class _CkeyManagementStatus_Type(Integer32):
    """Custom type ckeyManagementStatus based on Integer32"""
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
        *(("ckeyStatusNotDetected", 1),
          ("ckeyStatusNotValid", 2),
          ("ckeyStatusValidAndApplied", 3),
          ("ckeyStatusValidAndBackup", 4),
          ("ckeyStatusValidAndIgnored", 5),
          ("ckeyStatusContainsWlg", 6),
          ("ckeyStatusTooSmall", 7),
          ("ckeyStatusWrongProduct", 8),
          ("ckeyStatusIgnored", 9),
          ("ckeyStatusBusy", 10))
    )


_CkeyManagementStatus_Type.__name__ = "Integer32"
_CkeyManagementStatus_Object = MibScalar
ckeyManagementStatus = _CkeyManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 4),
    _CkeyManagementStatus_Type()
)
ckeyManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckeyManagementStatus.setStatus("current")
_CkeyManagementIgnoreSetting_Type = DisableEnable
_CkeyManagementIgnoreSetting_Object = MibScalar
ckeyManagementIgnoreSetting = _CkeyManagementIgnoreSetting_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 5),
    _CkeyManagementIgnoreSetting_Type()
)
ckeyManagementIgnoreSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementIgnoreSetting.setStatus("current")
_CkeyManagementDisableLed_Type = DisableEnable
_CkeyManagementDisableLed_Object = MibScalar
ckeyManagementDisableLed = _CkeyManagementDisableLed_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 6),
    _CkeyManagementDisableLed_Type()
)
ckeyManagementDisableLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementDisableLed.setStatus("current")
_CkeyManagementTest_Type = Integer32
_CkeyManagementTest_Object = MibScalar
ckeyManagementTest = _CkeyManagementTest_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 7),
    _CkeyManagementTest_Type()
)
ckeyManagementTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ckeyManagementTest.setStatus("current")


class _CkeyManagementTestResult_Type(Integer32):
    """Custom type ckeyManagementTestResult based on Integer32"""
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
        *(("ckeyTestInternalError", 1),
          ("ckeyTestNotAvailAble", 2),
          ("ckeyTestInProgress", 3),
          ("ckeyTestNotOk", 4),
          ("ckeyTestOk", 5))
    )


_CkeyManagementTestResult_Type.__name__ = "Integer32"
_CkeyManagementTestResult_Object = MibScalar
ckeyManagementTestResult = _CkeyManagementTestResult_Object(
    (1, 3, 6, 1, 4, 1, 28097, 4, 8),
    _CkeyManagementTestResult_Type()
)
ckeyManagementTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckeyManagementTestResult.setStatus("current")
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
_AlarmSettingsPower1DownEnable_Type = DisableEnable
_AlarmSettingsPower1DownEnable_Object = MibScalar
alarmSettingsPower1DownEnable = _AlarmSettingsPower1DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 2, 1),
    _AlarmSettingsPower1DownEnable_Type()
)
alarmSettingsPower1DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower1DownEnable.setStatus("current")
_AlarmSettingsPower1DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsPower2DownEnable_Type = DisableEnable
_AlarmSettingsPower2DownEnable_Object = MibScalar
alarmSettingsPower2DownEnable = _AlarmSettingsPower2DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 3, 1),
    _AlarmSettingsPower2DownEnable_Type()
)
alarmSettingsPower2DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsPower2DownEnable.setStatus("current")
_AlarmSettingsPower2DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan1DownEnable_Type = DisableEnable
_AlarmSettingsLan1DownEnable_Object = MibScalar
alarmSettingsLan1DownEnable = _AlarmSettingsLan1DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 4, 1),
    _AlarmSettingsLan1DownEnable_Type()
)
alarmSettingsLan1DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan1DownEnable.setStatus("current")
_AlarmSettingsLan1DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan2DownEnable_Type = DisableEnable
_AlarmSettingsLan2DownEnable_Object = MibScalar
alarmSettingsLan2DownEnable = _AlarmSettingsLan2DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 5, 1),
    _AlarmSettingsLan2DownEnable_Type()
)
alarmSettingsLan2DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan2DownEnable.setStatus("current")
_AlarmSettingsLan2DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan3DownEnable_Type = DisableEnable
_AlarmSettingsLan3DownEnable_Object = MibScalar
alarmSettingsLan3DownEnable = _AlarmSettingsLan3DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 6, 1),
    _AlarmSettingsLan3DownEnable_Type()
)
alarmSettingsLan3DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan3DownEnable.setStatus("current")
_AlarmSettingsLan3DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan4DownEnable_Type = DisableEnable
_AlarmSettingsLan4DownEnable_Object = MibScalar
alarmSettingsLan4DownEnable = _AlarmSettingsLan4DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 7, 1),
    _AlarmSettingsLan4DownEnable_Type()
)
alarmSettingsLan4DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan4DownEnable.setStatus("current")
_AlarmSettingsLan4DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan5DownEnable_Type = DisableEnable
_AlarmSettingsLan5DownEnable_Object = MibScalar
alarmSettingsLan5DownEnable = _AlarmSettingsLan5DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 8, 1),
    _AlarmSettingsLan5DownEnable_Type()
)
alarmSettingsLan5DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan5DownEnable.setStatus("current")
_AlarmSettingsLan5DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan6DownEnable_Type = DisableEnable
_AlarmSettingsLan6DownEnable_Object = MibScalar
alarmSettingsLan6DownEnable = _AlarmSettingsLan6DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 9, 1),
    _AlarmSettingsLan6DownEnable_Type()
)
alarmSettingsLan6DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan6DownEnable.setStatus("current")
_AlarmSettingsLan6DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan7DownEnable_Type = DisableEnable
_AlarmSettingsLan7DownEnable_Object = MibScalar
alarmSettingsLan7DownEnable = _AlarmSettingsLan7DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 10, 1),
    _AlarmSettingsLan7DownEnable_Type()
)
alarmSettingsLan7DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan7DownEnable.setStatus("current")
_AlarmSettingsLan7DownEnableAutomaticReset_Type = DisableEnable
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
_AlarmSettingsLan8DownEnable_Type = DisableEnable
_AlarmSettingsLan8DownEnable_Object = MibScalar
alarmSettingsLan8DownEnable = _AlarmSettingsLan8DownEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 5, 11, 1),
    _AlarmSettingsLan8DownEnable_Type()
)
alarmSettingsLan8DownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSettingsLan8DownEnable.setStatus("current")
_AlarmSettingsLan8DownEnableAutomaticReset_Type = DisableEnable
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
_NetworkStatus_ObjectIdentity = ObjectIdentity
networkStatus = _NetworkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 7)
)
_StatusIpSubnetTable_Object = MibTable
statusIpSubnetTable = _StatusIpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1)
)
if mibBuilder.loadTexts:
    statusIpSubnetTable.setStatus("current")
_StatusIpSubnetEntry_Object = MibTableRow
statusIpSubnetEntry = _StatusIpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1)
)
statusIpSubnetEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusIpSubnetIndex"),
)
if mibBuilder.loadTexts:
    statusIpSubnetEntry.setStatus("current")
_StatusIpSubnetIndex_Type = Integer32
_StatusIpSubnetIndex_Object = MibTableColumn
statusIpSubnetIndex = _StatusIpSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 1),
    _StatusIpSubnetIndex_Type()
)
statusIpSubnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetIndex.setStatus("current")
_StatusIpSubnetName_Type = NetifName
_StatusIpSubnetName_Object = MibTableColumn
statusIpSubnetName = _StatusIpSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 2),
    _StatusIpSubnetName_Type()
)
statusIpSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetName.setStatus("current")
_StatusIpSubnetLabel_Type = DisplayString
_StatusIpSubnetLabel_Object = MibTableColumn
statusIpSubnetLabel = _StatusIpSubnetLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 3),
    _StatusIpSubnetLabel_Type()
)
statusIpSubnetLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetLabel.setStatus("current")
_StatusIpSubnetIfIndex_Type = Integer32
_StatusIpSubnetIfIndex_Object = MibTableColumn
statusIpSubnetIfIndex = _StatusIpSubnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 4),
    _StatusIpSubnetIfIndex_Type()
)
statusIpSubnetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetIfIndex.setStatus("current")


class _StatusIpSubnetAddrMode_Type(Integer32):
    """Custom type statusIpSubnetAddrMode based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("none", 3),
          ("vrrp", 4))
    )


_StatusIpSubnetAddrMode_Type.__name__ = "Integer32"
_StatusIpSubnetAddrMode_Object = MibTableColumn
statusIpSubnetAddrMode = _StatusIpSubnetAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 5),
    _StatusIpSubnetAddrMode_Type()
)
statusIpSubnetAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetAddrMode.setStatus("current")
_StatusIpSubnetIPv4Addr_Type = IpAddress
_StatusIpSubnetIPv4Addr_Object = MibTableColumn
statusIpSubnetIPv4Addr = _StatusIpSubnetIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 6),
    _StatusIpSubnetIPv4Addr_Type()
)
statusIpSubnetIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetIPv4Addr.setStatus("current")
_StatusIpSubnetIPv4Mask_Type = IpAddress
_StatusIpSubnetIPv4Mask_Object = MibTableColumn
statusIpSubnetIPv4Mask = _StatusIpSubnetIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 7),
    _StatusIpSubnetIPv4Mask_Type()
)
statusIpSubnetIPv4Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetIPv4Mask.setStatus("current")
_StatusIpSubnetDNS_Type = DisplayString
_StatusIpSubnetDNS_Object = MibTableColumn
statusIpSubnetDNS = _StatusIpSubnetDNS_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 8),
    _StatusIpSubnetDNS_Type()
)
statusIpSubnetDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetDNS.setStatus("current")
_StatusIpSubnetMember_Type = DisplayString
_StatusIpSubnetMember_Object = MibTableColumn
statusIpSubnetMember = _StatusIpSubnetMember_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 9),
    _StatusIpSubnetMember_Type()
)
statusIpSubnetMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetMember.setStatus("current")
_StatusIpSubnetMemberIndex_Type = DisplayString
_StatusIpSubnetMemberIndex_Object = MibTableColumn
statusIpSubnetMemberIndex = _StatusIpSubnetMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 1, 1, 10),
    _StatusIpSubnetMemberIndex_Type()
)
statusIpSubnetMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIpSubnetMemberIndex.setStatus("current")
_StatusIfWlanTable_Object = MibTable
statusIfWlanTable = _StatusIfWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2)
)
if mibBuilder.loadTexts:
    statusIfWlanTable.setStatus("current")
_StatusIfWlanEntry_Object = MibTableRow
statusIfWlanEntry = _StatusIfWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1)
)
statusIfWlanEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusIfWlanIndex"),
)
if mibBuilder.loadTexts:
    statusIfWlanEntry.setStatus("current")
_StatusIfWlanIndex_Type = Integer32
_StatusIfWlanIndex_Object = MibTableColumn
statusIfWlanIndex = _StatusIfWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 1),
    _StatusIfWlanIndex_Type()
)
statusIfWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanIndex.setStatus("current")


class _StatusIfWlanSSID_Type(OctetString):
    """Custom type statusIfWlanSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StatusIfWlanSSID_Type.__name__ = "OctetString"
_StatusIfWlanSSID_Object = MibTableColumn
statusIfWlanSSID = _StatusIfWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 2),
    _StatusIfWlanSSID_Type()
)
statusIfWlanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanSSID.setStatus("current")


class _StatusIfWlanMode_Type(Integer32):
    """Custom type statusIfWlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("infra-client", 1),
          ("access-point", 2),
          ("ad-hoc", 3),
          ("monitor", 5),
          ("ieee80211s", 6),
          ("repeater", 7),
          ("isolating-access-point", 8))
    )


_StatusIfWlanMode_Type.__name__ = "Integer32"
_StatusIfWlanMode_Object = MibTableColumn
statusIfWlanMode = _StatusIfWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 3),
    _StatusIfWlanMode_Type()
)
statusIfWlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanMode.setStatus("current")
_StatusIfWlanBand_Type = WifiFlavor
_StatusIfWlanBand_Object = MibTableColumn
statusIfWlanBand = _StatusIfWlanBand_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 4),
    _StatusIfWlanBand_Type()
)
statusIfWlanBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanBand.setStatus("current")
_StatusIfWlanChannel_Type = Integer32
_StatusIfWlanChannel_Object = MibTableColumn
statusIfWlanChannel = _StatusIfWlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 5),
    _StatusIfWlanChannel_Type()
)
statusIfWlanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanChannel.setStatus("current")
_StatusIfWlanFrequency_Type = Integer32
_StatusIfWlanFrequency_Object = MibTableColumn
statusIfWlanFrequency = _StatusIfWlanFrequency_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 6),
    _StatusIfWlanFrequency_Type()
)
statusIfWlanFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanFrequency.setStatus("current")
_StatusIfWlanEnable_Type = DisableEnable
_StatusIfWlanEnable_Object = MibTableColumn
statusIfWlanEnable = _StatusIfWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 7),
    _StatusIfWlanEnable_Type()
)
statusIfWlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanEnable.setStatus("current")
_StatusIfWlanPhy_Type = Integer32
_StatusIfWlanPhy_Object = MibTableColumn
statusIfWlanPhy = _StatusIfWlanPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 8),
    _StatusIfWlanPhy_Type()
)
statusIfWlanPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanPhy.setStatus("current")
_StatusIfWlanSecurityMode_Type = SecurityModes
_StatusIfWlanSecurityMode_Object = MibTableColumn
statusIfWlanSecurityMode = _StatusIfWlanSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 9),
    _StatusIfWlanSecurityMode_Type()
)
statusIfWlanSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanSecurityMode.setStatus("current")
_StatusIfWlanWpaVersion_Type = Integer32
_StatusIfWlanWpaVersion_Object = MibTableColumn
statusIfWlanWpaVersion = _StatusIfWlanWpaVersion_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 10),
    _StatusIfWlanWpaVersion_Type()
)
statusIfWlanWpaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanWpaVersion.setStatus("current")
_StatusIfWlanNPeers_Type = Integer32
_StatusIfWlanNPeers_Object = MibTableColumn
statusIfWlanNPeers = _StatusIfWlanNPeers_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 11),
    _StatusIfWlanNPeers_Type()
)
statusIfWlanNPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanNPeers.setStatus("current")
_StatusIfWlanQuality_Type = Integer32
_StatusIfWlanQuality_Object = MibTableColumn
statusIfWlanQuality = _StatusIfWlanQuality_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 12),
    _StatusIfWlanQuality_Type()
)
statusIfWlanQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanQuality.setStatus("current")
_StatusIfWlanBssid_Type = PhysAddress
_StatusIfWlanBssid_Object = MibTableColumn
statusIfWlanBssid = _StatusIfWlanBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 13),
    _StatusIfWlanBssid_Type()
)
statusIfWlanBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanBssid.setStatus("current")


class _StatusIfWlanState_Type(Integer32):
    """Custom type statusIfWlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 9))
    )


_StatusIfWlanState_Type.__name__ = "Integer32"
_StatusIfWlanState_Object = MibTableColumn
statusIfWlanState = _StatusIfWlanState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 14),
    _StatusIfWlanState_Type()
)
statusIfWlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanState.setStatus("current")
_StatusIfStaFastBSSTransitionActivated_Type = DisableEnable
_StatusIfStaFastBSSTransitionActivated_Object = MibTableColumn
statusIfStaFastBSSTransitionActivated = _StatusIfStaFastBSSTransitionActivated_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 15),
    _StatusIfStaFastBSSTransitionActivated_Type()
)
statusIfStaFastBSSTransitionActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfStaFastBSSTransitionActivated.setStatus("current")
_StatusIfWlanBeaconSignalAvg_Type = Integer32
_StatusIfWlanBeaconSignalAvg_Object = MibTableColumn
statusIfWlanBeaconSignalAvg = _StatusIfWlanBeaconSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 16),
    _StatusIfWlanBeaconSignalAvg_Type()
)
statusIfWlanBeaconSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanBeaconSignalAvg.setStatus("current")
_StatusIfWlanNoise_Type = Integer32
_StatusIfWlanNoise_Object = MibTableColumn
statusIfWlanNoise = _StatusIfWlanNoise_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 17),
    _StatusIfWlanNoise_Type()
)
statusIfWlanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanNoise.setStatus("current")
_StatusIfWlanWpaCipher_Type = CipherTypes
_StatusIfWlanWpaCipher_Object = MibTableColumn
statusIfWlanWpaCipher = _StatusIfWlanWpaCipher_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 18),
    _StatusIfWlanWpaCipher_Type()
)
statusIfWlanWpaCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanWpaCipher.setStatus("current")
_StatusIfWlanWpaPreSharedKey_Type = OctetString
_StatusIfWlanWpaPreSharedKey_Object = MibTableColumn
statusIfWlanWpaPreSharedKey = _StatusIfWlanWpaPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 19),
    _StatusIfWlanWpaPreSharedKey_Type()
)
statusIfWlanWpaPreSharedKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanWpaPreSharedKey.setStatus("current")
_StatusIfWlanName_Type = DisplayString
_StatusIfWlanName_Object = MibTableColumn
statusIfWlanName = _StatusIfWlanName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 20),
    _StatusIfWlanName_Type()
)
statusIfWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanName.setStatus("current")
_StatusIfWlanIfIndex_Type = Integer32
_StatusIfWlanIfIndex_Object = MibTableColumn
statusIfWlanIfIndex = _StatusIfWlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 2, 1, 21),
    _StatusIfWlanIfIndex_Type()
)
statusIfWlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIfWlanIfIndex.setStatus("current")
_StatusPhyWifiTable_Object = MibTable
statusPhyWifiTable = _StatusPhyWifiTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3)
)
if mibBuilder.loadTexts:
    statusPhyWifiTable.setStatus("current")
_StatusPhyWifiEntry_Object = MibTableRow
statusPhyWifiEntry = _StatusPhyWifiEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1)
)
statusPhyWifiEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusPhyWifiIndex"),
)
if mibBuilder.loadTexts:
    statusPhyWifiEntry.setStatus("current")
_StatusPhyWifiIndex_Type = Integer32
_StatusPhyWifiIndex_Object = MibTableColumn
statusPhyWifiIndex = _StatusPhyWifiIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 1),
    _StatusPhyWifiIndex_Type()
)
statusPhyWifiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiIndex.setStatus("current")
_StatusPhyWifiLabel_Type = DisplayString
_StatusPhyWifiLabel_Object = MibTableColumn
statusPhyWifiLabel = _StatusPhyWifiLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 2),
    _StatusPhyWifiLabel_Type()
)
statusPhyWifiLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiLabel.setStatus("current")
_StatusPhyWifiEnable_Type = DisableEnable
_StatusPhyWifiEnable_Object = MibTableColumn
statusPhyWifiEnable = _StatusPhyWifiEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 3),
    _StatusPhyWifiEnable_Type()
)
statusPhyWifiEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiEnable.setStatus("current")
_StatusPhyWifiName_Type = NetifName
_StatusPhyWifiName_Object = MibTableColumn
statusPhyWifiName = _StatusPhyWifiName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 4),
    _StatusPhyWifiName_Type()
)
statusPhyWifiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiName.setStatus("current")


class _StatusPhyWifiClusterMode_Type(OctetString):
    """Custom type statusPhyWifiClusterMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StatusPhyWifiClusterMode_Type.__name__ = "OctetString"
_StatusPhyWifiClusterMode_Object = MibTableColumn
statusPhyWifiClusterMode = _StatusPhyWifiClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 5),
    _StatusPhyWifiClusterMode_Type()
)
statusPhyWifiClusterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiClusterMode.setStatus("current")


class _StatusPhyWifiClusterList_Type(OctetString):
    """Custom type statusPhyWifiClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatusPhyWifiClusterList_Type.__name__ = "OctetString"
_StatusPhyWifiClusterList_Object = MibTableColumn
statusPhyWifiClusterList = _StatusPhyWifiClusterList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 6),
    _StatusPhyWifiClusterList_Type()
)
statusPhyWifiClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiClusterList.setStatus("current")


class _StatusPhyWifiClusterArgs_Type(OctetString):
    """Custom type statusPhyWifiClusterArgs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatusPhyWifiClusterArgs_Type.__name__ = "OctetString"
_StatusPhyWifiClusterArgs_Object = MibTableColumn
statusPhyWifiClusterArgs = _StatusPhyWifiClusterArgs_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 7),
    _StatusPhyWifiClusterArgs_Type()
)
statusPhyWifiClusterArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiClusterArgs.setStatus("current")
_StatusPhyWifiMAC_Type = PhysAddress
_StatusPhyWifiMAC_Object = MibTableColumn
statusPhyWifiMAC = _StatusPhyWifiMAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 8),
    _StatusPhyWifiMAC_Type()
)
statusPhyWifiMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiMAC.setStatus("current")
_StatusPhyWifiWids_Type = Integer32
_StatusPhyWifiWids_Object = MibTableColumn
statusPhyWifiWids = _StatusPhyWifiWids_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 3, 1, 9),
    _StatusPhyWifiWids_Type()
)
statusPhyWifiWids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiWids.setStatus("current")
_StatusPhyWifiScanTable_Object = MibTable
statusPhyWifiScanTable = _StatusPhyWifiScanTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4)
)
if mibBuilder.loadTexts:
    statusPhyWifiScanTable.setStatus("current")
_StatusPhyWifiScanEntry_Object = MibTableRow
statusPhyWifiScanEntry = _StatusPhyWifiScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1)
)
statusPhyWifiScanEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusPhyWifiScanTableIndex"),
)
if mibBuilder.loadTexts:
    statusPhyWifiScanEntry.setStatus("current")
_StatusPhyWifiScanTableIndex_Type = Integer32
_StatusPhyWifiScanTableIndex_Object = MibTableColumn
statusPhyWifiScanTableIndex = _StatusPhyWifiScanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 1),
    _StatusPhyWifiScanTableIndex_Type()
)
statusPhyWifiScanTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanTableIndex.setStatus("current")


class _StatusPhyWifiScanSSID_Type(OctetString):
    """Custom type statusPhyWifiScanSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StatusPhyWifiScanSSID_Type.__name__ = "OctetString"
_StatusPhyWifiScanSSID_Object = MibTableColumn
statusPhyWifiScanSSID = _StatusPhyWifiScanSSID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 2),
    _StatusPhyWifiScanSSID_Type()
)
statusPhyWifiScanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanSSID.setStatus("current")
_StatusPhyWifiScanSignal_Type = Integer32
_StatusPhyWifiScanSignal_Object = MibTableColumn
statusPhyWifiScanSignal = _StatusPhyWifiScanSignal_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 3),
    _StatusPhyWifiScanSignal_Type()
)
statusPhyWifiScanSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanSignal.setStatus("current")
_StatusPhyWifiScanFreq_Type = Integer32
_StatusPhyWifiScanFreq_Object = MibTableColumn
statusPhyWifiScanFreq = _StatusPhyWifiScanFreq_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 4),
    _StatusPhyWifiScanFreq_Type()
)
statusPhyWifiScanFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanFreq.setStatus("current")


class _StatusPhyWifiScanMode_Type(Integer32):
    """Custom type statusPhyWifiScanMode based on Integer32"""
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
        *(("unknown", 1),
          ("infrastructure", 2),
          ("adhoc", 3),
          ("mesh", 4))
    )


_StatusPhyWifiScanMode_Type.__name__ = "Integer32"
_StatusPhyWifiScanMode_Object = MibTableColumn
statusPhyWifiScanMode = _StatusPhyWifiScanMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 5),
    _StatusPhyWifiScanMode_Type()
)
statusPhyWifiScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanMode.setStatus("current")
_StatusPhyWifiScanSecurity_Type = SecurityModes
_StatusPhyWifiScanSecurity_Object = MibTableColumn
statusPhyWifiScanSecurity = _StatusPhyWifiScanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 6),
    _StatusPhyWifiScanSecurity_Type()
)
statusPhyWifiScanSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanSecurity.setStatus("current")
_StatusPhyWifiScanBssid_Type = PhysAddress
_StatusPhyWifiScanBssid_Object = MibTableColumn
statusPhyWifiScanBssid = _StatusPhyWifiScanBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 7),
    _StatusPhyWifiScanBssid_Type()
)
statusPhyWifiScanBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanBssid.setStatus("current")
_StatusPhyWifiScanPhyNum_Type = Integer32
_StatusPhyWifiScanPhyNum_Object = MibTableColumn
statusPhyWifiScanPhyNum = _StatusPhyWifiScanPhyNum_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 8),
    _StatusPhyWifiScanPhyNum_Type()
)
statusPhyWifiScanPhyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanPhyNum.setStatus("current")
_StatusPhyWifiScanChWidth_Type = Integer32
_StatusPhyWifiScanChWidth_Object = MibTableColumn
statusPhyWifiScanChWidth = _StatusPhyWifiScanChWidth_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 4, 1, 9),
    _StatusPhyWifiScanChWidth_Type()
)
statusPhyWifiScanChWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyWifiScanChWidth.setStatus("current")
_StatusPhyWifiScanTableStart_Type = Integer32
_StatusPhyWifiScanTableStart_Object = MibScalar
statusPhyWifiScanTableStart = _StatusPhyWifiScanTableStart_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 5),
    _StatusPhyWifiScanTableStart_Type()
)
statusPhyWifiScanTableStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusPhyWifiScanTableStart.setStatus("current")


class _StatusPhyWifiScanUpdateTbl_Type(OctetString):
    """Custom type statusPhyWifiScanUpdateTbl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StatusPhyWifiScanUpdateTbl_Type.__name__ = "OctetString"
_StatusPhyWifiScanUpdateTbl_Object = MibScalar
statusPhyWifiScanUpdateTbl = _StatusPhyWifiScanUpdateTbl_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 6),
    _StatusPhyWifiScanUpdateTbl_Type()
)
statusPhyWifiScanUpdateTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusPhyWifiScanUpdateTbl.setStatus("current")
_StatusSpanningTreeTable_Object = MibTable
statusSpanningTreeTable = _StatusSpanningTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7)
)
if mibBuilder.loadTexts:
    statusSpanningTreeTable.setStatus("current")
_StatusSpanningTreeEntry_Object = MibTableRow
statusSpanningTreeEntry = _StatusSpanningTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1)
)
statusSpanningTreeEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusSpanningTreeBridgeName"),
)
if mibBuilder.loadTexts:
    statusSpanningTreeEntry.setStatus("current")
_StatusSpanningTreeBridgeName_Type = NetifName
_StatusSpanningTreeBridgeName_Object = MibTableColumn
statusSpanningTreeBridgeName = _StatusSpanningTreeBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1, 1),
    _StatusSpanningTreeBridgeName_Type()
)
statusSpanningTreeBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreeBridgeName.setStatus("current")
_StatusSpanningTreeNetworkLabel_Type = DisplayString
_StatusSpanningTreeNetworkLabel_Object = MibTableColumn
statusSpanningTreeNetworkLabel = _StatusSpanningTreeNetworkLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1, 2),
    _StatusSpanningTreeNetworkLabel_Type()
)
statusSpanningTreeNetworkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreeNetworkLabel.setStatus("current")
_StatusSpanningTreeBridgeId_Type = BridgeId
_StatusSpanningTreeBridgeId_Object = MibTableColumn
statusSpanningTreeBridgeId = _StatusSpanningTreeBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1, 3),
    _StatusSpanningTreeBridgeId_Type()
)
statusSpanningTreeBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreeBridgeId.setStatus("current")
_StatusSpanningTreeDesignatedRoot_Type = BridgeId
_StatusSpanningTreeDesignatedRoot_Object = MibTableColumn
statusSpanningTreeDesignatedRoot = _StatusSpanningTreeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1, 4),
    _StatusSpanningTreeDesignatedRoot_Type()
)
statusSpanningTreeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreeDesignatedRoot.setStatus("current")
_StatusSpanningTreeRootPort_Type = NetifName
_StatusSpanningTreeRootPort_Object = MibTableColumn
statusSpanningTreeRootPort = _StatusSpanningTreeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 7, 1, 5),
    _StatusSpanningTreeRootPort_Type()
)
statusSpanningTreeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreeRootPort.setStatus("current")
_StatusSpanningTreePortTable_Object = MibTable
statusSpanningTreePortTable = _StatusSpanningTreePortTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8)
)
if mibBuilder.loadTexts:
    statusSpanningTreePortTable.setStatus("current")
_StatusSpanningTreePortEntry_Object = MibTableRow
statusSpanningTreePortEntry = _StatusSpanningTreePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1)
)
statusSpanningTreePortEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusSpanningTreePortBridgeName"),
    (0, "ACKSYS-MIB", "statusSpanningTreePortName"),
)
if mibBuilder.loadTexts:
    statusSpanningTreePortEntry.setStatus("current")
_StatusSpanningTreePortBridgeName_Type = NetifName
_StatusSpanningTreePortBridgeName_Object = MibTableColumn
statusSpanningTreePortBridgeName = _StatusSpanningTreePortBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 1),
    _StatusSpanningTreePortBridgeName_Type()
)
statusSpanningTreePortBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortBridgeName.setStatus("current")
_StatusSpanningTreePortNetworkLabel_Type = DisplayString
_StatusSpanningTreePortNetworkLabel_Object = MibTableColumn
statusSpanningTreePortNetworkLabel = _StatusSpanningTreePortNetworkLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 2),
    _StatusSpanningTreePortNetworkLabel_Type()
)
statusSpanningTreePortNetworkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortNetworkLabel.setStatus("current")
_StatusSpanningTreePortName_Type = NetifName
_StatusSpanningTreePortName_Object = MibTableColumn
statusSpanningTreePortName = _StatusSpanningTreePortName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 3),
    _StatusSpanningTreePortName_Type()
)
statusSpanningTreePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortName.setStatus("current")
_StatusSpanningTreePortLabel_Type = DisplayString
_StatusSpanningTreePortLabel_Object = MibTableColumn
statusSpanningTreePortLabel = _StatusSpanningTreePortLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 4),
    _StatusSpanningTreePortLabel_Type()
)
statusSpanningTreePortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortLabel.setStatus("current")
_StatusSpanningTreePortId_Type = PortId
_StatusSpanningTreePortId_Object = MibTableColumn
statusSpanningTreePortId = _StatusSpanningTreePortId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 5),
    _StatusSpanningTreePortId_Type()
)
statusSpanningTreePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortId.setStatus("current")


class _StatusSpanningTreePortRole_Type(Integer32):
    """Custom type statusSpanningTreePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("root", 1),
          ("designated", 2),
          ("alternate", 3),
          ("backup", 4),
          ("master", 5))
    )


_StatusSpanningTreePortRole_Type.__name__ = "Integer32"
_StatusSpanningTreePortRole_Object = MibTableColumn
statusSpanningTreePortRole = _StatusSpanningTreePortRole_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 6),
    _StatusSpanningTreePortRole_Type()
)
statusSpanningTreePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortRole.setStatus("current")


class _StatusSpanningTreePortState_Type(Integer32):
    """Custom type statusSpanningTreePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_StatusSpanningTreePortState_Type.__name__ = "Integer32"
_StatusSpanningTreePortState_Object = MibTableColumn
statusSpanningTreePortState = _StatusSpanningTreePortState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 7),
    _StatusSpanningTreePortState_Type()
)
statusSpanningTreePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortState.setStatus("current")


class _StatusSpanningTreePortPathCost_Type(Integer32):
    """Custom type statusSpanningTreePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StatusSpanningTreePortPathCost_Type.__name__ = "Integer32"
_StatusSpanningTreePortPathCost_Object = MibTableColumn
statusSpanningTreePortPathCost = _StatusSpanningTreePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 8),
    _StatusSpanningTreePortPathCost_Type()
)
statusSpanningTreePortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortPathCost.setStatus("current")
_StatusSpanningTreePortDesignatedRoot_Type = BridgeId
_StatusSpanningTreePortDesignatedRoot_Object = MibTableColumn
statusSpanningTreePortDesignatedRoot = _StatusSpanningTreePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 9),
    _StatusSpanningTreePortDesignatedRoot_Type()
)
statusSpanningTreePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortDesignatedRoot.setStatus("current")
_StatusSpanningTreePortDesignatedCost_Type = Integer32
_StatusSpanningTreePortDesignatedCost_Object = MibTableColumn
statusSpanningTreePortDesignatedCost = _StatusSpanningTreePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 10),
    _StatusSpanningTreePortDesignatedCost_Type()
)
statusSpanningTreePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortDesignatedCost.setStatus("current")
_StatusSpanningTreePortDesignatedBridge_Type = BridgeId
_StatusSpanningTreePortDesignatedBridge_Object = MibTableColumn
statusSpanningTreePortDesignatedBridge = _StatusSpanningTreePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 11),
    _StatusSpanningTreePortDesignatedBridge_Type()
)
statusSpanningTreePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortDesignatedBridge.setStatus("current")
_StatusSpanningTreePortDesignatedPort_Type = PortId
_StatusSpanningTreePortDesignatedPort_Object = MibTableColumn
statusSpanningTreePortDesignatedPort = _StatusSpanningTreePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 12),
    _StatusSpanningTreePortDesignatedPort_Type()
)
statusSpanningTreePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortDesignatedPort.setStatus("current")
_StatusSpanningTreePortOperEdgePort_Type = TruthValue
_StatusSpanningTreePortOperEdgePort_Object = MibTableColumn
statusSpanningTreePortOperEdgePort = _StatusSpanningTreePortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 13),
    _StatusSpanningTreePortOperEdgePort_Type()
)
statusSpanningTreePortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortOperEdgePort.setStatus("current")
_StatusSpanningTreePortOperPointToPoint_Type = TruthValue
_StatusSpanningTreePortOperPointToPoint_Object = MibTableColumn
statusSpanningTreePortOperPointToPoint = _StatusSpanningTreePortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 8, 1, 14),
    _StatusSpanningTreePortOperPointToPoint_Type()
)
statusSpanningTreePortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpanningTreePortOperPointToPoint.setStatus("current")
_StatusAssociationTable_Object = MibTable
statusAssociationTable = _StatusAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9)
)
if mibBuilder.loadTexts:
    statusAssociationTable.setStatus("current")
_StatusAssociationEntry_Object = MibTableRow
statusAssociationEntry = _StatusAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1)
)
statusAssociationEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusAssociationIndex"),
)
if mibBuilder.loadTexts:
    statusAssociationEntry.setStatus("current")
_StatusAssociationIndex_Type = Integer32
_StatusAssociationIndex_Object = MibTableColumn
statusAssociationIndex = _StatusAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 1),
    _StatusAssociationIndex_Type()
)
statusAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationIndex.setStatus("current")
_StatusAssociationMacAddr_Type = PhysAddress
_StatusAssociationMacAddr_Object = MibTableColumn
statusAssociationMacAddr = _StatusAssociationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 2),
    _StatusAssociationMacAddr_Type()
)
statusAssociationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationMacAddr.setStatus("current")
_StatusAssociationSSID_Type = DisplayString
_StatusAssociationSSID_Object = MibTableColumn
statusAssociationSSID = _StatusAssociationSSID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 3),
    _StatusAssociationSSID_Type()
)
statusAssociationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationSSID.setStatus("current")
_StatusAssociationBSSID_Type = PhysAddress
_StatusAssociationBSSID_Object = MibTableColumn
statusAssociationBSSID = _StatusAssociationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 4),
    _StatusAssociationBSSID_Type()
)
statusAssociationBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationBSSID.setStatus("current")
_StatusAssociationPhy_Type = DisplayString
_StatusAssociationPhy_Object = MibTableColumn
statusAssociationPhy = _StatusAssociationPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 5),
    _StatusAssociationPhy_Type()
)
statusAssociationPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationPhy.setStatus("current")
_StatusAssociationSignaldBm_Type = Integer32
_StatusAssociationSignaldBm_Object = MibTableColumn
statusAssociationSignaldBm = _StatusAssociationSignaldBm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 6),
    _StatusAssociationSignaldBm_Type()
)
statusAssociationSignaldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationSignaldBm.setStatus("current")
_StatusAssociationNoisedBm_Type = Integer32
_StatusAssociationNoisedBm_Object = MibTableColumn
statusAssociationNoisedBm = _StatusAssociationNoisedBm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 7),
    _StatusAssociationNoisedBm_Type()
)
statusAssociationNoisedBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationNoisedBm.setStatus("current")
_StatusAssociationSNR_Type = Integer32
_StatusAssociationSNR_Object = MibTableColumn
statusAssociationSNR = _StatusAssociationSNR_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 8),
    _StatusAssociationSNR_Type()
)
statusAssociationSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationSNR.setStatus("current")
_StatusAssociationWlanIndex_Type = Integer32
_StatusAssociationWlanIndex_Object = MibTableColumn
statusAssociationWlanIndex = _StatusAssociationWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 9),
    _StatusAssociationWlanIndex_Type()
)
statusAssociationWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationWlanIndex.setStatus("current")
_StatusAssociationSecurityMode_Type = SecurityModes
_StatusAssociationSecurityMode_Object = MibTableColumn
statusAssociationSecurityMode = _StatusAssociationSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 9, 1, 10),
    _StatusAssociationSecurityMode_Type()
)
statusAssociationSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAssociationSecurityMode.setStatus("current")
_StatusPhyLanTable_Object = MibTable
statusPhyLanTable = _StatusPhyLanTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10)
)
if mibBuilder.loadTexts:
    statusPhyLanTable.setStatus("current")
_StatusPhyLanEntry_Object = MibTableRow
statusPhyLanEntry = _StatusPhyLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10, 1)
)
statusPhyLanEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusPhyLanIndex"),
)
if mibBuilder.loadTexts:
    statusPhyLanEntry.setStatus("current")
_StatusPhyLanIndex_Type = Integer32
_StatusPhyLanIndex_Object = MibTableColumn
statusPhyLanIndex = _StatusPhyLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10, 1, 1),
    _StatusPhyLanIndex_Type()
)
statusPhyLanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyLanIndex.setStatus("current")
_StatusPhyLanName_Type = DisplayString
_StatusPhyLanName_Object = MibTableColumn
statusPhyLanName = _StatusPhyLanName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10, 1, 2),
    _StatusPhyLanName_Type()
)
statusPhyLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyLanName.setStatus("current")
_StatusPhyLanLabel_Type = DisplayString
_StatusPhyLanLabel_Object = MibTableColumn
statusPhyLanLabel = _StatusPhyLanLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10, 1, 3),
    _StatusPhyLanLabel_Type()
)
statusPhyLanLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyLanLabel.setStatus("current")
_StatusPhyLanIfIndex_Type = Integer32
_StatusPhyLanIfIndex_Object = MibTableColumn
statusPhyLanIfIndex = _StatusPhyLanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 10, 1, 4),
    _StatusPhyLanIfIndex_Type()
)
statusPhyLanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyLanIfIndex.setStatus("current")
_StatusMeshSurveyTable_Object = MibTable
statusMeshSurveyTable = _StatusMeshSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11)
)
if mibBuilder.loadTexts:
    statusMeshSurveyTable.setStatus("current")
_StatusMeshSurveyEntry_Object = MibTableRow
statusMeshSurveyEntry = _StatusMeshSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1)
)
statusMeshSurveyEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusMeshSurveyIndex"),
)
if mibBuilder.loadTexts:
    statusMeshSurveyEntry.setStatus("current")
_StatusMeshSurveyIndex_Type = Integer32
_StatusMeshSurveyIndex_Object = MibTableColumn
statusMeshSurveyIndex = _StatusMeshSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 1),
    _StatusMeshSurveyIndex_Type()
)
statusMeshSurveyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyIndex.setStatus("current")
_StatusMeshSurveyDstMacAddr_Type = PhysAddress
_StatusMeshSurveyDstMacAddr_Object = MibTableColumn
statusMeshSurveyDstMacAddr = _StatusMeshSurveyDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 2),
    _StatusMeshSurveyDstMacAddr_Type()
)
statusMeshSurveyDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyDstMacAddr.setStatus("current")
_StatusMeshSurveyNextHopMacAddr_Type = PhysAddress
_StatusMeshSurveyNextHopMacAddr_Object = MibTableColumn
statusMeshSurveyNextHopMacAddr = _StatusMeshSurveyNextHopMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 3),
    _StatusMeshSurveyNextHopMacAddr_Type()
)
statusMeshSurveyNextHopMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyNextHopMacAddr.setStatus("current")
_StatusMeshSurveyPhy_Type = DisplayString
_StatusMeshSurveyPhy_Object = MibTableColumn
statusMeshSurveyPhy = _StatusMeshSurveyPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 4),
    _StatusMeshSurveyPhy_Type()
)
statusMeshSurveyPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyPhy.setStatus("current")
_StatusMeshSurveyMetric_Type = Integer32
_StatusMeshSurveyMetric_Object = MibTableColumn
statusMeshSurveyMetric = _StatusMeshSurveyMetric_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 5),
    _StatusMeshSurveyMetric_Type()
)
statusMeshSurveyMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyMetric.setStatus("current")
_StatusMeshSurveyDiscoveryTimeout_Type = Integer32
_StatusMeshSurveyDiscoveryTimeout_Object = MibTableColumn
statusMeshSurveyDiscoveryTimeout = _StatusMeshSurveyDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 6),
    _StatusMeshSurveyDiscoveryTimeout_Type()
)
statusMeshSurveyDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyDiscoveryTimeout.setStatus("current")
_StatusMeshSurveyDiscoveryRetries_Type = Integer32
_StatusMeshSurveyDiscoveryRetries_Object = MibTableColumn
statusMeshSurveyDiscoveryRetries = _StatusMeshSurveyDiscoveryRetries_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 7),
    _StatusMeshSurveyDiscoveryRetries_Type()
)
statusMeshSurveyDiscoveryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyDiscoveryRetries.setStatus("current")
_StatusMeshSurveyStateActive_Type = TruthValue
_StatusMeshSurveyStateActive_Object = MibTableColumn
statusMeshSurveyStateActive = _StatusMeshSurveyStateActive_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 8),
    _StatusMeshSurveyStateActive_Type()
)
statusMeshSurveyStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyStateActive.setStatus("current")
_StatusMeshSurveyStateResolving_Type = TruthValue
_StatusMeshSurveyStateResolving_Object = MibTableColumn
statusMeshSurveyStateResolving = _StatusMeshSurveyStateResolving_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 9),
    _StatusMeshSurveyStateResolving_Type()
)
statusMeshSurveyStateResolving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyStateResolving.setStatus("current")
_StatusMeshSurveyStateDSNValid_Type = TruthValue
_StatusMeshSurveyStateDSNValid_Object = MibTableColumn
statusMeshSurveyStateDSNValid = _StatusMeshSurveyStateDSNValid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 10),
    _StatusMeshSurveyStateDSNValid_Type()
)
statusMeshSurveyStateDSNValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyStateDSNValid.setStatus("current")
_StatusMeshSurveyStateFixed_Type = TruthValue
_StatusMeshSurveyStateFixed_Object = MibTableColumn
statusMeshSurveyStateFixed = _StatusMeshSurveyStateFixed_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 11),
    _StatusMeshSurveyStateFixed_Type()
)
statusMeshSurveyStateFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyStateFixed.setStatus("current")
_StatusMeshSurveyStateResolved_Type = TruthValue
_StatusMeshSurveyStateResolved_Object = MibTableColumn
statusMeshSurveyStateResolved = _StatusMeshSurveyStateResolved_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 12),
    _StatusMeshSurveyStateResolved_Type()
)
statusMeshSurveyStateResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyStateResolved.setStatus("current")
_StatusMeshSurveyMeshId_Type = DisplayString
_StatusMeshSurveyMeshId_Object = MibTableColumn
statusMeshSurveyMeshId = _StatusMeshSurveyMeshId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 13),
    _StatusMeshSurveyMeshId_Type()
)
statusMeshSurveyMeshId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyMeshId.setStatus("current")
_StatusMeshSurveyWlanIndex_Type = Integer32
_StatusMeshSurveyWlanIndex_Object = MibTableColumn
statusMeshSurveyWlanIndex = _StatusMeshSurveyWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 11, 1, 14),
    _StatusMeshSurveyWlanIndex_Type()
)
statusMeshSurveyWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMeshSurveyWlanIndex.setStatus("current")
_StatusPhyCellTable_Object = MibTable
statusPhyCellTable = _StatusPhyCellTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12)
)
if mibBuilder.loadTexts:
    statusPhyCellTable.setStatus("current")
_StatusPhyCellEntry_Object = MibTableRow
statusPhyCellEntry = _StatusPhyCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1)
)
statusPhyCellEntry.setIndexNames(
    (0, "ACKSYS-MIB", "statusPhyCellIndex"),
)
if mibBuilder.loadTexts:
    statusPhyCellEntry.setStatus("current")
_StatusPhyCellIndex_Type = Integer32
_StatusPhyCellIndex_Object = MibTableColumn
statusPhyCellIndex = _StatusPhyCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 1),
    _StatusPhyCellIndex_Type()
)
statusPhyCellIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellIndex.setStatus("current")
_StatusPhyCellLabel_Type = DisplayString
_StatusPhyCellLabel_Object = MibTableColumn
statusPhyCellLabel = _StatusPhyCellLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 2),
    _StatusPhyCellLabel_Type()
)
statusPhyCellLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellLabel.setStatus("current")
_StatusPhyCellFriendlyName_Type = OctetString
_StatusPhyCellFriendlyName_Object = MibTableColumn
statusPhyCellFriendlyName = _StatusPhyCellFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 3),
    _StatusPhyCellFriendlyName_Type()
)
statusPhyCellFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellFriendlyName.setStatus("current")
_StatusPhyCellEnable_Type = DisableEnable
_StatusPhyCellEnable_Object = MibTableColumn
statusPhyCellEnable = _StatusPhyCellEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 4),
    _StatusPhyCellEnable_Type()
)
statusPhyCellEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellEnable.setStatus("current")
_StatusPhyCellIMEI_Type = DisplayString
_StatusPhyCellIMEI_Object = MibTableColumn
statusPhyCellIMEI = _StatusPhyCellIMEI_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 5),
    _StatusPhyCellIMEI_Type()
)
statusPhyCellIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellIMEI.setStatus("current")
_StatusPhyCellModel_Type = DisplayString
_StatusPhyCellModel_Object = MibTableColumn
statusPhyCellModel = _StatusPhyCellModel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 6),
    _StatusPhyCellModel_Type()
)
statusPhyCellModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellModel.setStatus("current")
_StatusPhyCellName_Type = NetifName
_StatusPhyCellName_Object = MibTableColumn
statusPhyCellName = _StatusPhyCellName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 7),
    _StatusPhyCellName_Type()
)
statusPhyCellName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellName.setStatus("current")
_StatusPhyCellSimSelected_Type = Integer32
_StatusPhyCellSimSelected_Object = MibTableColumn
statusPhyCellSimSelected = _StatusPhyCellSimSelected_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 8),
    _StatusPhyCellSimSelected_Type()
)
statusPhyCellSimSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellSimSelected.setStatus("current")
_StatusPhyCellSimState_Type = DisplayString
_StatusPhyCellSimState_Object = MibTableColumn
statusPhyCellSimState = _StatusPhyCellSimState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 9),
    _StatusPhyCellSimState_Type()
)
statusPhyCellSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellSimState.setStatus("current")
_StatusPhyCellSimIMSI_Type = DisplayString
_StatusPhyCellSimIMSI_Object = MibTableColumn
statusPhyCellSimIMSI = _StatusPhyCellSimIMSI_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 10),
    _StatusPhyCellSimIMSI_Type()
)
statusPhyCellSimIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellSimIMSI.setStatus("current")
_StatusPhyCellAttachMode_Type = CellAttachMode
_StatusPhyCellAttachMode_Object = MibTableColumn
statusPhyCellAttachMode = _StatusPhyCellAttachMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 11),
    _StatusPhyCellAttachMode_Type()
)
statusPhyCellAttachMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellAttachMode.setStatus("current")
_StatusPhyCellOperator_Type = DisplayString
_StatusPhyCellOperator_Object = MibTableColumn
statusPhyCellOperator = _StatusPhyCellOperator_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 12),
    _StatusPhyCellOperator_Type()
)
statusPhyCellOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellOperator.setStatus("current")
_StatusPhyCellMcc_Type = Integer32
_StatusPhyCellMcc_Object = MibTableColumn
statusPhyCellMcc = _StatusPhyCellMcc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 13),
    _StatusPhyCellMcc_Type()
)
statusPhyCellMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellMcc.setStatus("current")
_StatusPhyCellMnc_Type = Integer32
_StatusPhyCellMnc_Object = MibTableColumn
statusPhyCellMnc = _StatusPhyCellMnc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 14),
    _StatusPhyCellMnc_Type()
)
statusPhyCellMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellMnc.setStatus("current")
_StatusPhyCellBaseLAC_Type = Integer32
_StatusPhyCellBaseLAC_Object = MibTableColumn
statusPhyCellBaseLAC = _StatusPhyCellBaseLAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 15),
    _StatusPhyCellBaseLAC_Type()
)
statusPhyCellBaseLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellBaseLAC.setStatus("current")
_StatusPhyCellBaseCID_Type = Integer32
_StatusPhyCellBaseCID_Object = MibTableColumn
statusPhyCellBaseCID = _StatusPhyCellBaseCID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 16),
    _StatusPhyCellBaseCID_Type()
)
statusPhyCellBaseCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellBaseCID.setStatus("current")
_StatusPhyCellRegistrationClass_Type = DisplayString
_StatusPhyCellRegistrationClass_Object = MibTableColumn
statusPhyCellRegistrationClass = _StatusPhyCellRegistrationClass_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 17),
    _StatusPhyCellRegistrationClass_Type()
)
statusPhyCellRegistrationClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellRegistrationClass.setStatus("current")
_StatusPhyCellAccessTech_Type = CellAccessTech
_StatusPhyCellAccessTech_Object = MibTableColumn
statusPhyCellAccessTech = _StatusPhyCellAccessTech_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 18),
    _StatusPhyCellAccessTech_Type()
)
statusPhyCellAccessTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellAccessTech.setStatus("current")
_StatusPhyCellBandName_Type = DisplayString
_StatusPhyCellBandName_Object = MibTableColumn
statusPhyCellBandName = _StatusPhyCellBandName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 19),
    _StatusPhyCellBandName_Type()
)
statusPhyCellBandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellBandName.setStatus("current")
_StatusPhyCellARFCN_Type = Integer32
_StatusPhyCellARFCN_Object = MibTableColumn
statusPhyCellARFCN = _StatusPhyCellARFCN_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 20),
    _StatusPhyCellARFCN_Type()
)
statusPhyCellARFCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellARFCN.setStatus("current")
_StatusPhyCellRSSI_Type = Integer32
_StatusPhyCellRSSI_Object = MibTableColumn
statusPhyCellRSSI = _StatusPhyCellRSSI_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 21),
    _StatusPhyCellRSSI_Type()
)
statusPhyCellRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellRSSI.setStatus("current")
_StatusPhyCellBER_Type = Integer32
_StatusPhyCellBER_Object = MibTableColumn
statusPhyCellBER = _StatusPhyCellBER_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 12, 1, 22),
    _StatusPhyCellBER_Type()
)
statusPhyCellBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPhyCellBER.setStatus("current")
_StatusRoaming_ObjectIdentity = ObjectIdentity
statusRoaming = _StatusRoaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13)
)
_StatusRoamingLeaveLvlMax_Type = Integer32
_StatusRoamingLeaveLvlMax_Object = MibScalar
statusRoamingLeaveLvlMax = _StatusRoamingLeaveLvlMax_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 1),
    _StatusRoamingLeaveLvlMax_Type()
)
statusRoamingLeaveLvlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingLeaveLvlMax.setStatus("current")
_StatusRoamingLeaveLvlMin_Type = Integer32
_StatusRoamingLeaveLvlMin_Object = MibScalar
statusRoamingLeaveLvlMin = _StatusRoamingLeaveLvlMin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 2),
    _StatusRoamingLeaveLvlMin_Type()
)
statusRoamingLeaveLvlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingLeaveLvlMin.setStatus("current")
_StatusRoamingRoamLvlMax_Type = Integer32
_StatusRoamingRoamLvlMax_Object = MibScalar
statusRoamingRoamLvlMax = _StatusRoamingRoamLvlMax_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 3),
    _StatusRoamingRoamLvlMax_Type()
)
statusRoamingRoamLvlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingRoamLvlMax.setStatus("current")
_StatusRoamingRoamLvlMin_Type = Integer32
_StatusRoamingRoamLvlMin_Object = MibScalar
statusRoamingRoamLvlMin = _StatusRoamingRoamLvlMin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 4),
    _StatusRoamingRoamLvlMin_Type()
)
statusRoamingRoamLvlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingRoamLvlMin.setStatus("current")
_StatusRoamingThresHyst_Type = Integer32
_StatusRoamingThresHyst_Object = MibScalar
statusRoamingThresHyst = _StatusRoamingThresHyst_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 5),
    _StatusRoamingThresHyst_Type()
)
statusRoamingThresHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingThresHyst.setStatus("current")
_StatusRoamingLeaveBoost_Type = Integer32
_StatusRoamingLeaveBoost_Object = MibScalar
statusRoamingLeaveBoost = _StatusRoamingLeaveBoost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 6),
    _StatusRoamingLeaveBoost_Type()
)
statusRoamingLeaveBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingLeaveBoost.setStatus("current")
_StatusRoamingActiveIf_ObjectIdentity = ObjectIdentity
statusRoamingActiveIf = _StatusRoamingActiveIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7)
)
_StatusRoamingActiveIfName_Type = OctetString
_StatusRoamingActiveIfName_Object = MibScalar
statusRoamingActiveIfName = _StatusRoamingActiveIfName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 1),
    _StatusRoamingActiveIfName_Type()
)
statusRoamingActiveIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfName.setStatus("current")
_StatusRoamingActiveIfBssid_Type = PhysAddress
_StatusRoamingActiveIfBssid_Object = MibScalar
statusRoamingActiveIfBssid = _StatusRoamingActiveIfBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 2),
    _StatusRoamingActiveIfBssid_Type()
)
statusRoamingActiveIfBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfBssid.setStatus("current")
_StatusRoamingActiveIfBeaconSignalAvg_Type = Integer32
_StatusRoamingActiveIfBeaconSignalAvg_Object = MibScalar
statusRoamingActiveIfBeaconSignalAvg = _StatusRoamingActiveIfBeaconSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 3),
    _StatusRoamingActiveIfBeaconSignalAvg_Type()
)
statusRoamingActiveIfBeaconSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfBeaconSignalAvg.setStatus("current")
_StatusRoamingActiveIfNoise_Type = Integer32
_StatusRoamingActiveIfNoise_Object = MibScalar
statusRoamingActiveIfNoise = _StatusRoamingActiveIfNoise_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 4),
    _StatusRoamingActiveIfNoise_Type()
)
statusRoamingActiveIfNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfNoise.setStatus("current")


class _StatusRoamingActiveIfSwitching_Type(Integer32):
    """Custom type statusRoamingActiveIfSwitching based on Integer32"""
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


_StatusRoamingActiveIfSwitching_Type.__name__ = "Integer32"
_StatusRoamingActiveIfSwitching_Object = MibScalar
statusRoamingActiveIfSwitching = _StatusRoamingActiveIfSwitching_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 5),
    _StatusRoamingActiveIfSwitching_Type()
)
statusRoamingActiveIfSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfSwitching.setStatus("current")
_StatusRoamingActiveIfChannel_Type = Integer32
_StatusRoamingActiveIfChannel_Object = MibScalar
statusRoamingActiveIfChannel = _StatusRoamingActiveIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 6),
    _StatusRoamingActiveIfChannel_Type()
)
statusRoamingActiveIfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfChannel.setStatus("current")


class _StatusRoamingActiveIfState_Type(Integer32):
    """Custom type statusRoamingActiveIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 9))
    )


_StatusRoamingActiveIfState_Type.__name__ = "Integer32"
_StatusRoamingActiveIfState_Object = MibScalar
statusRoamingActiveIfState = _StatusRoamingActiveIfState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 7, 7),
    _StatusRoamingActiveIfState_Type()
)
statusRoamingActiveIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingActiveIfState.setStatus("current")
_StatusRoamingPassiveIf_ObjectIdentity = ObjectIdentity
statusRoamingPassiveIf = _StatusRoamingPassiveIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8)
)
_StatusRoamingPassiveIfName_Type = OctetString
_StatusRoamingPassiveIfName_Object = MibScalar
statusRoamingPassiveIfName = _StatusRoamingPassiveIfName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 1),
    _StatusRoamingPassiveIfName_Type()
)
statusRoamingPassiveIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfName.setStatus("current")
_StatusRoamingPassiveIfBssid_Type = PhysAddress
_StatusRoamingPassiveIfBssid_Object = MibScalar
statusRoamingPassiveIfBssid = _StatusRoamingPassiveIfBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 2),
    _StatusRoamingPassiveIfBssid_Type()
)
statusRoamingPassiveIfBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfBssid.setStatus("current")
_StatusRoamingPassiveIfBeaconSignalAvg_Type = Integer32
_StatusRoamingPassiveIfBeaconSignalAvg_Object = MibScalar
statusRoamingPassiveIfBeaconSignalAvg = _StatusRoamingPassiveIfBeaconSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 3),
    _StatusRoamingPassiveIfBeaconSignalAvg_Type()
)
statusRoamingPassiveIfBeaconSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfBeaconSignalAvg.setStatus("current")
_StatusRoamingPassiveIfNoise_Type = Integer32
_StatusRoamingPassiveIfNoise_Object = MibScalar
statusRoamingPassiveIfNoise = _StatusRoamingPassiveIfNoise_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 4),
    _StatusRoamingPassiveIfNoise_Type()
)
statusRoamingPassiveIfNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfNoise.setStatus("current")


class _StatusRoamingPassiveIfSwitching_Type(Integer32):
    """Custom type statusRoamingPassiveIfSwitching based on Integer32"""
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


_StatusRoamingPassiveIfSwitching_Type.__name__ = "Integer32"
_StatusRoamingPassiveIfSwitching_Object = MibScalar
statusRoamingPassiveIfSwitching = _StatusRoamingPassiveIfSwitching_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 5),
    _StatusRoamingPassiveIfSwitching_Type()
)
statusRoamingPassiveIfSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfSwitching.setStatus("current")
_StatusRoamingPassiveIfChannel_Type = Integer32
_StatusRoamingPassiveIfChannel_Object = MibScalar
statusRoamingPassiveIfChannel = _StatusRoamingPassiveIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 6),
    _StatusRoamingPassiveIfChannel_Type()
)
statusRoamingPassiveIfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfChannel.setStatus("current")


class _StatusRoamingPassiveIfState_Type(Integer32):
    """Custom type statusRoamingPassiveIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 9))
    )


_StatusRoamingPassiveIfState_Type.__name__ = "Integer32"
_StatusRoamingPassiveIfState_Object = MibScalar
statusRoamingPassiveIfState = _StatusRoamingPassiveIfState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 8, 7),
    _StatusRoamingPassiveIfState_Type()
)
statusRoamingPassiveIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingPassiveIfState.setStatus("current")
_StatusRoamingUrgent_Type = DisableEnable
_StatusRoamingUrgent_Object = MibScalar
statusRoamingUrgent = _StatusRoamingUrgent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 7, 13, 9),
    _StatusRoamingUrgent_Type()
)
statusRoamingUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRoamingUrgent.setStatus("current")
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8)
)
_Tcpip_ObjectIdentity = ObjectIdentity
tcpip = _Tcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1)
)
_ConfigIpSubnetTable_Object = MibTable
configIpSubnetTable = _ConfigIpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1)
)
if mibBuilder.loadTexts:
    configIpSubnetTable.setStatus("current")
_ConfigIpSubnetEntry_Object = MibTableRow
configIpSubnetEntry = _ConfigIpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1)
)
configIpSubnetEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpSubnetName"),
)
if mibBuilder.loadTexts:
    configIpSubnetEntry.setStatus("current")
_ConfigIpSubnetName_Type = NetifName
_ConfigIpSubnetName_Object = MibTableColumn
configIpSubnetName = _ConfigIpSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 1),
    _ConfigIpSubnetName_Type()
)
configIpSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpSubnetName.setStatus("current")
_ConfigIpSubnetRowStatus_Type = RowStatus
_ConfigIpSubnetRowStatus_Object = MibTableColumn
configIpSubnetRowStatus = _ConfigIpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 2),
    _ConfigIpSubnetRowStatus_Type()
)
configIpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpSubnetRowStatus.setStatus("current")


class _ConfigIpAddressMode_Type(Integer32):
    """Custom type configIpAddressMode based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("none", 3),
          ("vrrp", 4))
    )


_ConfigIpAddressMode_Type.__name__ = "Integer32"
_ConfigIpAddressMode_Object = MibTableColumn
configIpAddressMode = _ConfigIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 3),
    _ConfigIpAddressMode_Type()
)
configIpAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAddressMode.setStatus("current")
_ConfigIpSubnetIPv4Addr_Type = IpAddress
_ConfigIpSubnetIPv4Addr_Object = MibTableColumn
configIpSubnetIPv4Addr = _ConfigIpSubnetIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 4),
    _ConfigIpSubnetIPv4Addr_Type()
)
configIpSubnetIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetIPv4Addr.setStatus("current")
_ConfigIpSubnetIPv4Mask_Type = IpAddress
_ConfigIpSubnetIPv4Mask_Object = MibTableColumn
configIpSubnetIPv4Mask = _ConfigIpSubnetIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 5),
    _ConfigIpSubnetIPv4Mask_Type()
)
configIpSubnetIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetIPv4Mask.setStatus("current")
_ConfigIpSubnetMetric_Type = Integer32
_ConfigIpSubnetMetric_Object = MibTableColumn
configIpSubnetMetric = _ConfigIpSubnetMetric_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 6),
    _ConfigIpSubnetMetric_Type()
)
configIpSubnetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetMetric.setStatus("current")
_ConfigIpSubnetDnsList_Type = OctetString
_ConfigIpSubnetDnsList_Object = MibTableColumn
configIpSubnetDnsList = _ConfigIpSubnetDnsList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 7),
    _ConfigIpSubnetDnsList_Type()
)
configIpSubnetDnsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetDnsList.setStatus("current")
_ConfigIpSubnetInterface_Type = OctetString
_ConfigIpSubnetInterface_Object = MibTableColumn
configIpSubnetInterface = _ConfigIpSubnetInterface_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 8),
    _ConfigIpSubnetInterface_Type()
)
configIpSubnetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetInterface.setStatus("current")
_ConfigIpSubnetIPv4Gateway_Type = IpAddress
_ConfigIpSubnetIPv4Gateway_Object = MibTableColumn
configIpSubnetIPv4Gateway = _ConfigIpSubnetIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 9),
    _ConfigIpSubnetIPv4Gateway_Type()
)
configIpSubnetIPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetIPv4Gateway.setStatus("current")
_ConfigIpSubnetFriendlyName_Type = OctetString
_ConfigIpSubnetFriendlyName_Object = MibTableColumn
configIpSubnetFriendlyName = _ConfigIpSubnetFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 10),
    _ConfigIpSubnetFriendlyName_Type()
)
configIpSubnetFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetFriendlyName.setStatus("current")
_ConfigIpSubnetBridgeEnable_Type = DisableEnable
_ConfigIpSubnetBridgeEnable_Object = MibTableColumn
configIpSubnetBridgeEnable = _ConfigIpSubnetBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 11),
    _ConfigIpSubnetBridgeEnable_Type()
)
configIpSubnetBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetBridgeEnable.setStatus("current")
_ConfigIpSubnetPersistence_Type = TriState
_ConfigIpSubnetPersistence_Object = MibTableColumn
configIpSubnetPersistence = _ConfigIpSubnetPersistence_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 12),
    _ConfigIpSubnetPersistence_Type()
)
configIpSubnetPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetPersistence.setStatus("current")
_ConfigIpSubnetEnable_Type = DisableEnable
_ConfigIpSubnetEnable_Object = MibTableColumn
configIpSubnetEnable = _ConfigIpSubnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 13),
    _ConfigIpSubnetEnable_Type()
)
configIpSubnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetEnable.setStatus("current")
_ConfigIpSubnetAutoStart_Type = TriState
_ConfigIpSubnetAutoStart_Object = MibTableColumn
configIpSubnetAutoStart = _ConfigIpSubnetAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 14),
    _ConfigIpSubnetAutoStart_Type()
)
configIpSubnetAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetAutoStart.setStatus("current")
_ConfigIpSubnetPeerDns_Type = DisableEnable
_ConfigIpSubnetPeerDns_Object = MibTableColumn
configIpSubnetPeerDns = _ConfigIpSubnetPeerDns_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 15),
    _ConfigIpSubnetPeerDns_Type()
)
configIpSubnetPeerDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetPeerDns.setStatus("current")
_ConfigIpSubnetDefaultRoute_Type = DisableEnable
_ConfigIpSubnetDefaultRoute_Object = MibTableColumn
configIpSubnetDefaultRoute = _ConfigIpSubnetDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 1, 1, 16),
    _ConfigIpSubnetDefaultRoute_Type()
)
configIpSubnetDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpSubnetDefaultRoute.setStatus("current")
_IpFactory_ObjectIdentity = ObjectIdentity
ipFactory = _IpFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2)
)
_Synfloodprotection_Type = DisableEnable
_Synfloodprotection_Object = MibScalar
synfloodprotection = _Synfloodprotection_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 1),
    _Synfloodprotection_Type()
)
synfloodprotection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synfloodprotection.setStatus("current")
_Dropinvalidpacket_Type = DisableEnable
_Dropinvalidpacket_Object = MibScalar
dropinvalidpacket = _Dropinvalidpacket_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 2),
    _Dropinvalidpacket_Type()
)
dropinvalidpacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropinvalidpacket.setStatus("current")
_ConfigIpZonesTable_Object = MibTable
configIpZonesTable = _ConfigIpZonesTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    configIpZonesTable.setStatus("current")
_ConfigIpZonesEntry_Object = MibTableRow
configIpZonesEntry = _ConfigIpZonesEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1)
)
configIpZonesEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpZoneIndex"),
)
if mibBuilder.loadTexts:
    configIpZonesEntry.setStatus("current")
_ConfigIpZoneIndex_Type = OctetString
_ConfigIpZoneIndex_Object = MibTableColumn
configIpZoneIndex = _ConfigIpZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 1),
    _ConfigIpZoneIndex_Type()
)
configIpZoneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneIndex.setStatus("current")
_ConfigIpZoneRowStatus_Type = RowStatus
_ConfigIpZoneRowStatus_Object = MibTableColumn
configIpZoneRowStatus = _ConfigIpZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 2),
    _ConfigIpZoneRowStatus_Type()
)
configIpZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpZoneRowStatus.setStatus("current")
_ConfigIpZoneFriendlyName_Type = OctetString
_ConfigIpZoneFriendlyName_Object = MibTableColumn
configIpZoneFriendlyName = _ConfigIpZoneFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 3),
    _ConfigIpZoneFriendlyName_Type()
)
configIpZoneFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneFriendlyName.setStatus("current")
_ConfigIpZoneNAT_Type = DisableEnable
_ConfigIpZoneNAT_Object = MibTableColumn
configIpZoneNAT = _ConfigIpZoneNAT_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 4),
    _ConfigIpZoneNAT_Type()
)
configIpZoneNAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneNAT.setStatus("current")
_ConfigIpZoneMSSClamping_Type = DisableEnable
_ConfigIpZoneMSSClamping_Object = MibTableColumn
configIpZoneMSSClamping = _ConfigIpZoneMSSClamping_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 5),
    _ConfigIpZoneMSSClamping_Type()
)
configIpZoneMSSClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneMSSClamping.setStatus("current")


class _ConfigIpZoneDefaultAcceptancePolicy_Type(Integer32):
    """Custom type configIpZoneDefaultAcceptancePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allenable", 1),
          ("alldisable", 2))
    )


_ConfigIpZoneDefaultAcceptancePolicy_Type.__name__ = "Integer32"
_ConfigIpZoneDefaultAcceptancePolicy_Object = MibTableColumn
configIpZoneDefaultAcceptancePolicy = _ConfigIpZoneDefaultAcceptancePolicy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 6),
    _ConfigIpZoneDefaultAcceptancePolicy_Type()
)
configIpZoneDefaultAcceptancePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneDefaultAcceptancePolicy.setStatus("current")


class _ConfigIpZoneRestrictedAddressFamily_Type(Integer32):
    """Custom type configIpZoneRestrictedAddressFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4ipv6", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_ConfigIpZoneRestrictedAddressFamily_Type.__name__ = "Integer32"
_ConfigIpZoneRestrictedAddressFamily_Object = MibTableColumn
configIpZoneRestrictedAddressFamily = _ConfigIpZoneRestrictedAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 7),
    _ConfigIpZoneRestrictedAddressFamily_Type()
)
configIpZoneRestrictedAddressFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneRestrictedAddressFamily.setStatus("current")
_ConfigIpZoneConnectionTracking_Type = DisableEnable
_ConfigIpZoneConnectionTracking_Object = MibTableColumn
configIpZoneConnectionTracking = _ConfigIpZoneConnectionTracking_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 8),
    _ConfigIpZoneConnectionTracking_Type()
)
configIpZoneConnectionTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneConnectionTracking.setStatus("current")
_ConfigIpZoneLogging_Type = DisableEnable
_ConfigIpZoneLogging_Object = MibTableColumn
configIpZoneLogging = _ConfigIpZoneLogging_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 9),
    _ConfigIpZoneLogging_Type()
)
configIpZoneLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneLogging.setStatus("current")
_ConfigIpZoneLoggingLimit_Type = OctetString
_ConfigIpZoneLoggingLimit_Object = MibTableColumn
configIpZoneLoggingLimit = _ConfigIpZoneLoggingLimit_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 10),
    _ConfigIpZoneLoggingLimit_Type()
)
configIpZoneLoggingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneLoggingLimit.setStatus("current")
_ConfigIpZoneInterfaces_Type = OctetString
_ConfigIpZoneInterfaces_Object = MibTableColumn
configIpZoneInterfaces = _ConfigIpZoneInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 3, 1, 11),
    _ConfigIpZoneInterfaces_Type()
)
configIpZoneInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneInterfaces.setStatus("current")
_ConfigIpNatIpForwardTable_Object = MibTable
configIpNatIpForwardTable = _ConfigIpNatIpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    configIpNatIpForwardTable.setStatus("current")
_ConfigIpNatIpForwardEntry_Object = MibTableRow
configIpNatIpForwardEntry = _ConfigIpNatIpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1)
)
configIpNatIpForwardEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpNatIpForwardIndex"),
)
if mibBuilder.loadTexts:
    configIpNatIpForwardEntry.setStatus("current")
_ConfigIpNatIpForwardIndex_Type = OctetString
_ConfigIpNatIpForwardIndex_Object = MibTableColumn
configIpNatIpForwardIndex = _ConfigIpNatIpForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 1),
    _ConfigIpNatIpForwardIndex_Type()
)
configIpNatIpForwardIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardIndex.setStatus("current")
_ConfigIpNatIpForwardRowStatus_Type = RowStatus
_ConfigIpNatIpForwardRowStatus_Object = MibTableColumn
configIpNatIpForwardRowStatus = _ConfigIpNatIpForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 2),
    _ConfigIpNatIpForwardRowStatus_Type()
)
configIpNatIpForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpNatIpForwardRowStatus.setStatus("current")
_ConfigIpNatIpForwardFriendlyName_Type = OctetString
_ConfigIpNatIpForwardFriendlyName_Object = MibTableColumn
configIpNatIpForwardFriendlyName = _ConfigIpNatIpForwardFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 3),
    _ConfigIpNatIpForwardFriendlyName_Type()
)
configIpNatIpForwardFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardFriendlyName.setStatus("current")
_ConfigIpNatIpForwardZoneName_Type = OctetString
_ConfigIpNatIpForwardZoneName_Object = MibTableColumn
configIpNatIpForwardZoneName = _ConfigIpNatIpForwardZoneName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 4),
    _ConfigIpNatIpForwardZoneName_Type()
)
configIpNatIpForwardZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardZoneName.setStatus("current")
_ConfigIpNatIpForwardSrcIp_Type = IpAddress
_ConfigIpNatIpForwardSrcIp_Object = MibTableColumn
configIpNatIpForwardSrcIp = _ConfigIpNatIpForwardSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 5),
    _ConfigIpNatIpForwardSrcIp_Type()
)
configIpNatIpForwardSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardSrcIp.setStatus("current")


class _ConfigIpNatIpForwardProtocol_Type(Integer32):
    """Custom type configIpNatIpForwardProtocol based on Integer32"""
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
        *(("all", 1),
          ("tcp", 2),
          ("udp", 3),
          ("tcpudp", 4),
          ("icmp", 5))
    )


_ConfigIpNatIpForwardProtocol_Type.__name__ = "Integer32"
_ConfigIpNatIpForwardProtocol_Object = MibTableColumn
configIpNatIpForwardProtocol = _ConfigIpNatIpForwardProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 6),
    _ConfigIpNatIpForwardProtocol_Type()
)
configIpNatIpForwardProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardProtocol.setStatus("current")
_ConfigIpNatIpForwardPublicPort_Type = OctetString
_ConfigIpNatIpForwardPublicPort_Object = MibTableColumn
configIpNatIpForwardPublicPort = _ConfigIpNatIpForwardPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 7),
    _ConfigIpNatIpForwardPublicPort_Type()
)
configIpNatIpForwardPublicPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardPublicPort.setStatus("current")
_ConfigIpNatIpForwardPrivatePort_Type = OctetString
_ConfigIpNatIpForwardPrivatePort_Object = MibTableColumn
configIpNatIpForwardPrivatePort = _ConfigIpNatIpForwardPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 8),
    _ConfigIpNatIpForwardPrivatePort_Type()
)
configIpNatIpForwardPrivatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardPrivatePort.setStatus("current")
_ConfigIpNatIpForwardTargetIp_Type = IpAddress
_ConfigIpNatIpForwardTargetIp_Object = MibTableColumn
configIpNatIpForwardTargetIp = _ConfigIpNatIpForwardTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 4, 1, 9),
    _ConfigIpNatIpForwardTargetIp_Type()
)
configIpNatIpForwardTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpNatIpForwardTargetIp.setStatus("current")
_ConfigIpFirewallTable_Object = MibTable
configIpFirewallTable = _ConfigIpFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    configIpFirewallTable.setStatus("current")
_ConfigIpFirewallEntry_Object = MibTableRow
configIpFirewallEntry = _ConfigIpFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1)
)
configIpFirewallEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpFirewallIndex"),
)
if mibBuilder.loadTexts:
    configIpFirewallEntry.setStatus("current")
_ConfigIpFirewallIndex_Type = OctetString
_ConfigIpFirewallIndex_Object = MibTableColumn
configIpFirewallIndex = _ConfigIpFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 1),
    _ConfigIpFirewallIndex_Type()
)
configIpFirewallIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallIndex.setStatus("current")
_ConfigIpFirewallRowStatus_Type = RowStatus
_ConfigIpFirewallRowStatus_Object = MibTableColumn
configIpFirewallRowStatus = _ConfigIpFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 2),
    _ConfigIpFirewallRowStatus_Type()
)
configIpFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpFirewallRowStatus.setStatus("current")
_ConfigIpFirewallZoneName_Type = OctetString
_ConfigIpFirewallZoneName_Object = MibTableColumn
configIpFirewallZoneName = _ConfigIpFirewallZoneName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 3),
    _ConfigIpFirewallZoneName_Type()
)
configIpFirewallZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallZoneName.setStatus("current")


class _ConfigIpFirewallProtocol_Type(Integer32):
    """Custom type configIpFirewallProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tcp", 2),
          ("udp", 3),
          ("tcpudp", 4),
          ("icmp", 5),
          ("gre", 6))
    )


_ConfigIpFirewallProtocol_Type.__name__ = "Integer32"
_ConfigIpFirewallProtocol_Object = MibTableColumn
configIpFirewallProtocol = _ConfigIpFirewallProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 4),
    _ConfigIpFirewallProtocol_Type()
)
configIpFirewallProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallProtocol.setStatus("current")
_ConfigIpFirewallPort_Type = OctetString
_ConfigIpFirewallPort_Object = MibTableColumn
configIpFirewallPort = _ConfigIpFirewallPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 5),
    _ConfigIpFirewallPort_Type()
)
configIpFirewallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallPort.setStatus("current")


class _ConfigIpFirewallAction_Type(Integer32):
    """Custom type configIpFirewallAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reject", 2),
          ("drop", 3))
    )


_ConfigIpFirewallAction_Type.__name__ = "Integer32"
_ConfigIpFirewallAction_Object = MibTableColumn
configIpFirewallAction = _ConfigIpFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 6),
    _ConfigIpFirewallAction_Type()
)
configIpFirewallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallAction.setStatus("current")
_ConfigIpFirewallDestZone_Type = OctetString
_ConfigIpFirewallDestZone_Object = MibTableColumn
configIpFirewallDestZone = _ConfigIpFirewallDestZone_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 7),
    _ConfigIpFirewallDestZone_Type()
)
configIpFirewallDestZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallDestZone.setStatus("current")
_ConfigIpFirewallSrcIP_Type = IpAddress
_ConfigIpFirewallSrcIP_Object = MibTableColumn
configIpFirewallSrcIP = _ConfigIpFirewallSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 8),
    _ConfigIpFirewallSrcIP_Type()
)
configIpFirewallSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallSrcIP.setStatus("current")
_ConfigIpFirewallTargetIP_Type = IpAddress
_ConfigIpFirewallTargetIP_Object = MibTableColumn
configIpFirewallTargetIP = _ConfigIpFirewallTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 5, 1, 9),
    _ConfigIpFirewallTargetIP_Type()
)
configIpFirewallTargetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFirewallTargetIP.setStatus("current")
_ConfigIpRoutesTable_Object = MibTable
configIpRoutesTable = _ConfigIpRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    configIpRoutesTable.setStatus("current")
_ConfigIpRoutesEntry_Object = MibTableRow
configIpRoutesEntry = _ConfigIpRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1)
)
configIpRoutesEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpRoutesIndex"),
)
if mibBuilder.loadTexts:
    configIpRoutesEntry.setStatus("current")
_ConfigIpRoutesIndex_Type = Integer32
_ConfigIpRoutesIndex_Object = MibTableColumn
configIpRoutesIndex = _ConfigIpRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 1),
    _ConfigIpRoutesIndex_Type()
)
configIpRoutesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesIndex.setStatus("current")
_ConfigIpRoutesRowStatus_Type = RowStatus
_ConfigIpRoutesRowStatus_Object = MibTableColumn
configIpRoutesRowStatus = _ConfigIpRoutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 2),
    _ConfigIpRoutesRowStatus_Type()
)
configIpRoutesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpRoutesRowStatus.setStatus("current")
_ConfigIpRoutesNetwork_Type = OctetString
_ConfigIpRoutesNetwork_Object = MibTableColumn
configIpRoutesNetwork = _ConfigIpRoutesNetwork_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 3),
    _ConfigIpRoutesNetwork_Type()
)
configIpRoutesNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesNetwork.setStatus("current")
_ConfigIpRoutesTarget_Type = IpAddress
_ConfigIpRoutesTarget_Object = MibTableColumn
configIpRoutesTarget = _ConfigIpRoutesTarget_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 4),
    _ConfigIpRoutesTarget_Type()
)
configIpRoutesTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesTarget.setStatus("current")
_ConfigIpRoutesNetmask_Type = IpAddress
_ConfigIpRoutesNetmask_Object = MibTableColumn
configIpRoutesNetmask = _ConfigIpRoutesNetmask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 5),
    _ConfigIpRoutesNetmask_Type()
)
configIpRoutesNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesNetmask.setStatus("current")
_ConfigIpRoutesGateway_Type = IpAddress
_ConfigIpRoutesGateway_Object = MibTableColumn
configIpRoutesGateway = _ConfigIpRoutesGateway_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 6),
    _ConfigIpRoutesGateway_Type()
)
configIpRoutesGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesGateway.setStatus("current")
_ConfigIpRoutesMetric_Type = Integer32
_ConfigIpRoutesMetric_Object = MibTableColumn
configIpRoutesMetric = _ConfigIpRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 7),
    _ConfigIpRoutesMetric_Type()
)
configIpRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesMetric.setStatus("current")
_ConfigIpRoutesMTU_Type = Integer32
_ConfigIpRoutesMTU_Object = MibTableColumn
configIpRoutesMTU = _ConfigIpRoutesMTU_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 6, 1, 8),
    _ConfigIpRoutesMTU_Type()
)
configIpRoutesMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpRoutesMTU.setStatus("current")
_ConfigIpZoneForwardTable_Object = MibTable
configIpZoneForwardTable = _ConfigIpZoneForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7)
)
if mibBuilder.loadTexts:
    configIpZoneForwardTable.setStatus("current")
_ConfigIpZoneForwardEntry_Object = MibTableRow
configIpZoneForwardEntry = _ConfigIpZoneForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7, 1)
)
configIpZoneForwardEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpZoneForwardIndex"),
)
if mibBuilder.loadTexts:
    configIpZoneForwardEntry.setStatus("current")
_ConfigIpZoneForwardIndex_Type = Integer32
_ConfigIpZoneForwardIndex_Object = MibTableColumn
configIpZoneForwardIndex = _ConfigIpZoneForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7, 1, 1),
    _ConfigIpZoneForwardIndex_Type()
)
configIpZoneForwardIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneForwardIndex.setStatus("current")
_ConfigIpZoneForwardRowStatus_Type = RowStatus
_ConfigIpZoneForwardRowStatus_Object = MibTableColumn
configIpZoneForwardRowStatus = _ConfigIpZoneForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7, 1, 2),
    _ConfigIpZoneForwardRowStatus_Type()
)
configIpZoneForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpZoneForwardRowStatus.setStatus("current")
_ConfigIpZoneForwardSrc_Type = OctetString
_ConfigIpZoneForwardSrc_Object = MibTableColumn
configIpZoneForwardSrc = _ConfigIpZoneForwardSrc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7, 1, 3),
    _ConfigIpZoneForwardSrc_Type()
)
configIpZoneForwardSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneForwardSrc.setStatus("current")
_ConfigIpZoneForwardDst_Type = OctetString
_ConfigIpZoneForwardDst_Object = MibTableColumn
configIpZoneForwardDst = _ConfigIpZoneForwardDst_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 7, 1, 4),
    _ConfigIpZoneForwardDst_Type()
)
configIpZoneForwardDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpZoneForwardDst.setStatus("current")
_ConfigIpDscpTaggingTable_Object = MibTable
configIpDscpTaggingTable = _ConfigIpDscpTaggingTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8)
)
if mibBuilder.loadTexts:
    configIpDscpTaggingTable.setStatus("current")
_ConfigIpDscpTaggingEntry_Object = MibTableRow
configIpDscpTaggingEntry = _ConfigIpDscpTaggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1)
)
configIpDscpTaggingEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIpDscpTaggingIndex"),
)
if mibBuilder.loadTexts:
    configIpDscpTaggingEntry.setStatus("current")
_ConfigIpDscpTaggingIndex_Type = OctetString
_ConfigIpDscpTaggingIndex_Object = MibTableColumn
configIpDscpTaggingIndex = _ConfigIpDscpTaggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 1),
    _ConfigIpDscpTaggingIndex_Type()
)
configIpDscpTaggingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingIndex.setStatus("current")
_ConfigIpDscpTaggingRowStatus_Type = RowStatus
_ConfigIpDscpTaggingRowStatus_Object = MibTableColumn
configIpDscpTaggingRowStatus = _ConfigIpDscpTaggingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 2),
    _ConfigIpDscpTaggingRowStatus_Type()
)
configIpDscpTaggingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIpDscpTaggingRowStatus.setStatus("current")
_ConfigIpDscpTaggingFriendlyName_Type = OctetString
_ConfigIpDscpTaggingFriendlyName_Object = MibTableColumn
configIpDscpTaggingFriendlyName = _ConfigIpDscpTaggingFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 3),
    _ConfigIpDscpTaggingFriendlyName_Type()
)
configIpDscpTaggingFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingFriendlyName.setStatus("current")


class _ConfigIpDscpTaggingProtocol_Type(Integer32):
    """Custom type configIpDscpTaggingProtocol based on Integer32"""
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
        *(("all", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4))
    )


_ConfigIpDscpTaggingProtocol_Type.__name__ = "Integer32"
_ConfigIpDscpTaggingProtocol_Object = MibTableColumn
configIpDscpTaggingProtocol = _ConfigIpDscpTaggingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 4),
    _ConfigIpDscpTaggingProtocol_Type()
)
configIpDscpTaggingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingProtocol.setStatus("current")
_ConfigIpDscpTaggingSrcIP_Type = IpAddress
_ConfigIpDscpTaggingSrcIP_Object = MibTableColumn
configIpDscpTaggingSrcIP = _ConfigIpDscpTaggingSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 5),
    _ConfigIpDscpTaggingSrcIP_Type()
)
configIpDscpTaggingSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingSrcIP.setStatus("current")
_ConfigIpDscpTaggingDstIP_Type = IpAddress
_ConfigIpDscpTaggingDstIP_Object = MibTableColumn
configIpDscpTaggingDstIP = _ConfigIpDscpTaggingDstIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 6),
    _ConfigIpDscpTaggingDstIP_Type()
)
configIpDscpTaggingDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingDstIP.setStatus("current")
_ConfigIpDscpTaggingSrcPort_Type = OctetString
_ConfigIpDscpTaggingSrcPort_Object = MibTableColumn
configIpDscpTaggingSrcPort = _ConfigIpDscpTaggingSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 7),
    _ConfigIpDscpTaggingSrcPort_Type()
)
configIpDscpTaggingSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingSrcPort.setStatus("current")
_ConfigIpDscpTaggingDstPort_Type = OctetString
_ConfigIpDscpTaggingDstPort_Object = MibTableColumn
configIpDscpTaggingDstPort = _ConfigIpDscpTaggingDstPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 8),
    _ConfigIpDscpTaggingDstPort_Type()
)
configIpDscpTaggingDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingDstPort.setStatus("current")
_ConfigIpDscpTaggingDscpValue_Type = Integer32
_ConfigIpDscpTaggingDscpValue_Object = MibTableColumn
configIpDscpTaggingDscpValue = _ConfigIpDscpTaggingDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 1, 2, 8, 1, 9),
    _ConfigIpDscpTaggingDscpValue_Type()
)
configIpDscpTaggingDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpDscpTaggingDscpValue.setStatus("current")
_Netphy_ObjectIdentity = ObjectIdentity
netphy = _Netphy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2)
)
_ConfigPhyWifiTable_Object = MibTable
configPhyWifiTable = _ConfigPhyWifiTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1)
)
if mibBuilder.loadTexts:
    configPhyWifiTable.setStatus("current")
_ConfigPhyWifiEntry_Object = MibTableRow
configPhyWifiEntry = _ConfigPhyWifiEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1)
)
configPhyWifiEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configPhyWifiName"),
)
if mibBuilder.loadTexts:
    configPhyWifiEntry.setStatus("current")
_ConfigPhyWifiName_Type = NetifName
_ConfigPhyWifiName_Object = MibTableColumn
configPhyWifiName = _ConfigPhyWifiName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 2),
    _ConfigPhyWifiName_Type()
)
configPhyWifiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyWifiName.setStatus("current")
_ConfigPhyWifiLabel_Type = DisplayString
_ConfigPhyWifiLabel_Object = MibTableColumn
configPhyWifiLabel = _ConfigPhyWifiLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 3),
    _ConfigPhyWifiLabel_Type()
)
configPhyWifiLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyWifiLabel.setStatus("current")
_ConfigPhyWifiMAC_Type = PhysAddress
_ConfigPhyWifiMAC_Object = MibTableColumn
configPhyWifiMAC = _ConfigPhyWifiMAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 4),
    _ConfigPhyWifiMAC_Type()
)
configPhyWifiMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyWifiMAC.setStatus("current")
_ConfigPhyWifiEnable_Type = DisableEnable
_ConfigPhyWifiEnable_Object = MibTableColumn
configPhyWifiEnable = _ConfigPhyWifiEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 5),
    _ConfigPhyWifiEnable_Type()
)
configPhyWifiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiEnable.setStatus("current")
_ConfigPhyWifiMode_Type = WifiFlavor
_ConfigPhyWifiMode_Object = MibTableColumn
configPhyWifiMode = _ConfigPhyWifiMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 6),
    _ConfigPhyWifiMode_Type()
)
configPhyWifiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiMode.setStatus("current")


class _ConfigPhyWifiCountry_Type(OctetString):
    """Custom type configPhyWifiCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ConfigPhyWifiCountry_Type.__name__ = "OctetString"
_ConfigPhyWifiCountry_Object = MibTableColumn
configPhyWifiCountry = _ConfigPhyWifiCountry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 7),
    _ConfigPhyWifiCountry_Type()
)
configPhyWifiCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiCountry.setStatus("current")
_ConfigPhyWifiChannel_Type = Integer32
_ConfigPhyWifiChannel_Object = MibTableColumn
configPhyWifiChannel = _ConfigPhyWifiChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 8),
    _ConfigPhyWifiChannel_Type()
)
configPhyWifiChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiChannel.setStatus("current")


class _ConfigPhyWifiHTMode_Type(Integer32):
    """Custom type configPhyWifiHTMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40-below", 2),
          ("ht40-above", 3),
          ("ht40-auto", 4),
          ("vht20", 5),
          ("vht40", 6),
          ("vht80", 7))
    )


_ConfigPhyWifiHTMode_Type.__name__ = "Integer32"
_ConfigPhyWifiHTMode_Object = MibTableColumn
configPhyWifiHTMode = _ConfigPhyWifiHTMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 9),
    _ConfigPhyWifiHTMode_Type()
)
configPhyWifiHTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiHTMode.setStatus("current")
_ConfigPhyWifiTxPowerDBM_Type = Integer32
_ConfigPhyWifiTxPowerDBM_Object = MibTableColumn
configPhyWifiTxPowerDBM = _ConfigPhyWifiTxPowerDBM_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 10),
    _ConfigPhyWifiTxPowerDBM_Type()
)
configPhyWifiTxPowerDBM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiTxPowerDBM.setStatus("current")
_ConfigPhyWifiDistance_Type = Integer32
_ConfigPhyWifiDistance_Object = MibTableColumn
configPhyWifiDistance = _ConfigPhyWifiDistance_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 11),
    _ConfigPhyWifiDistance_Type()
)
configPhyWifiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiDistance.setStatus("current")


class _ConfigPhyWifiClusterMode_Type(OctetString):
    """Custom type configPhyWifiClusterMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConfigPhyWifiClusterMode_Type.__name__ = "OctetString"
_ConfigPhyWifiClusterMode_Object = MibTableColumn
configPhyWifiClusterMode = _ConfigPhyWifiClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 12),
    _ConfigPhyWifiClusterMode_Type()
)
configPhyWifiClusterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiClusterMode.setStatus("current")


class _ConfigPhyWifiClusterList_Type(OctetString):
    """Custom type configPhyWifiClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigPhyWifiClusterList_Type.__name__ = "OctetString"
_ConfigPhyWifiClusterList_Object = MibTableColumn
configPhyWifiClusterList = _ConfigPhyWifiClusterList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 13),
    _ConfigPhyWifiClusterList_Type()
)
configPhyWifiClusterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiClusterList.setStatus("current")


class _ConfigPhyWifiClusterArgs_Type(OctetString):
    """Custom type configPhyWifiClusterArgs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigPhyWifiClusterArgs_Type.__name__ = "OctetString"
_ConfigPhyWifiClusterArgs_Object = MibTableColumn
configPhyWifiClusterArgs = _ConfigPhyWifiClusterArgs_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 14),
    _ConfigPhyWifiClusterArgs_Type()
)
configPhyWifiClusterArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiClusterArgs.setStatus("current")


class _ConfigPhyWifiAntennaPorts_Type(Integer32):
    """Custom type configPhyWifiAntennaPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("ports12", 3),
          ("ports123", 7))
    )


_ConfigPhyWifiAntennaPorts_Type.__name__ = "Integer32"
_ConfigPhyWifiAntennaPorts_Object = MibTableColumn
configPhyWifiAntennaPorts = _ConfigPhyWifiAntennaPorts_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 15),
    _ConfigPhyWifiAntennaPorts_Type()
)
configPhyWifiAntennaPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiAntennaPorts.setStatus("current")


class _ConfigPhyWifiABGBasicRates_Type(OctetString):
    """Custom type configPhyWifiABGBasicRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 66),
    )


_ConfigPhyWifiABGBasicRates_Type.__name__ = "OctetString"
_ConfigPhyWifiABGBasicRates_Object = MibTableColumn
configPhyWifiABGBasicRates = _ConfigPhyWifiABGBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 16),
    _ConfigPhyWifiABGBasicRates_Type()
)
configPhyWifiABGBasicRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiABGBasicRates.setStatus("current")


class _ConfigPhyWifiABGSupportedRates_Type(OctetString):
    """Custom type configPhyWifiABGSupportedRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 66),
    )


_ConfigPhyWifiABGSupportedRates_Type.__name__ = "OctetString"
_ConfigPhyWifiABGSupportedRates_Object = MibTableColumn
configPhyWifiABGSupportedRates = _ConfigPhyWifiABGSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 17),
    _ConfigPhyWifiABGSupportedRates_Type()
)
configPhyWifiABGSupportedRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiABGSupportedRates.setStatus("current")
_ConfigPhyWifiChannelList_Type = OctetString
_ConfigPhyWifiChannelList_Object = MibTableColumn
configPhyWifiChannelList = _ConfigPhyWifiChannelList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 18),
    _ConfigPhyWifiChannelList_Type()
)
configPhyWifiChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiChannelList.setStatus("current")
_ConfigPhyWifiWids_Type = Integer32
_ConfigPhyWifiWids_Object = MibTableColumn
configPhyWifiWids = _ConfigPhyWifiWids_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 1, 1, 19),
    _ConfigPhyWifiWids_Type()
)
configPhyWifiWids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyWifiWids.setStatus("current")
_ConfigPhyCellTable_Object = MibTable
configPhyCellTable = _ConfigPhyCellTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2)
)
if mibBuilder.loadTexts:
    configPhyCellTable.setStatus("current")
_ConfigPhyCellEntry_Object = MibTableRow
configPhyCellEntry = _ConfigPhyCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1)
)
configPhyCellEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configPhyCellName"),
)
if mibBuilder.loadTexts:
    configPhyCellEntry.setStatus("current")
_ConfigPhyCellName_Type = NetifName
_ConfigPhyCellName_Object = MibTableColumn
configPhyCellName = _ConfigPhyCellName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 1),
    _ConfigPhyCellName_Type()
)
configPhyCellName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyCellName.setStatus("current")
_ConfigPhyCellLabel_Type = DisplayString
_ConfigPhyCellLabel_Object = MibTableColumn
configPhyCellLabel = _ConfigPhyCellLabel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 2),
    _ConfigPhyCellLabel_Type()
)
configPhyCellLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyCellLabel.setStatus("current")
_ConfigPhyCellDisableAtBoot_Type = DisableEnable
_ConfigPhyCellDisableAtBoot_Object = MibTableColumn
configPhyCellDisableAtBoot = _ConfigPhyCellDisableAtBoot_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 3),
    _ConfigPhyCellDisableAtBoot_Type()
)
configPhyCellDisableAtBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellDisableAtBoot.setStatus("current")
_ConfigPhyCellLogAT_Type = DisableEnable
_ConfigPhyCellLogAT_Object = MibTableColumn
configPhyCellLogAT = _ConfigPhyCellLogAT_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 4),
    _ConfigPhyCellLogAT_Type()
)
configPhyCellLogAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellLogAT.setStatus("current")


class _ConfigPhyCellSIM_Type(Integer32):
    """Custom type configPhyCellSIM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sim1", 1),
          ("sim2", 2))
    )


_ConfigPhyCellSIM_Type.__name__ = "Integer32"
_ConfigPhyCellSIM_Object = MibTableColumn
configPhyCellSIM = _ConfigPhyCellSIM_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 5),
    _ConfigPhyCellSIM_Type()
)
configPhyCellSIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSIM.setStatus("current")
_ConfigPhyCellSetPIN_Type = DisplayString
_ConfigPhyCellSetPIN_Object = MibTableColumn
configPhyCellSetPIN = _ConfigPhyCellSetPIN_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 6),
    _ConfigPhyCellSetPIN_Type()
)
configPhyCellSetPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSetPIN.setStatus("current")
_ConfigPhyCellSetPUK_Type = DisplayString
_ConfigPhyCellSetPUK_Object = MibTableColumn
configPhyCellSetPUK = _ConfigPhyCellSetPUK_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 7),
    _ConfigPhyCellSetPUK_Type()
)
configPhyCellSetPUK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSetPUK.setStatus("current")
_ConfigPhyCellSetPINStatus_Type = AsyncSetStatus
_ConfigPhyCellSetPINStatus_Object = MibTableColumn
configPhyCellSetPINStatus = _ConfigPhyCellSetPINStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 8),
    _ConfigPhyCellSetPINStatus_Type()
)
configPhyCellSetPINStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhyCellSetPINStatus.setStatus("current")
_ConfigPhyCellSim1Pin_Type = DisplayString
_ConfigPhyCellSim1Pin_Object = MibTableColumn
configPhyCellSim1Pin = _ConfigPhyCellSim1Pin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 9),
    _ConfigPhyCellSim1Pin_Type()
)
configPhyCellSim1Pin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim1Pin.setStatus("current")
_ConfigPhyCellSim1Apn_Type = DisplayString
_ConfigPhyCellSim1Apn_Object = MibTableColumn
configPhyCellSim1Apn = _ConfigPhyCellSim1Apn_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 10),
    _ConfigPhyCellSim1Apn_Type()
)
configPhyCellSim1Apn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim1Apn.setStatus("current")
_ConfigPhyCellSim1Authentication_Type = CellSecurityProtocol
_ConfigPhyCellSim1Authentication_Object = MibTableColumn
configPhyCellSim1Authentication = _ConfigPhyCellSim1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 11),
    _ConfigPhyCellSim1Authentication_Type()
)
configPhyCellSim1Authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim1Authentication.setStatus("current")
_ConfigPhyCellSim1Identity_Type = DisplayString
_ConfigPhyCellSim1Identity_Object = MibTableColumn
configPhyCellSim1Identity = _ConfigPhyCellSim1Identity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 12),
    _ConfigPhyCellSim1Identity_Type()
)
configPhyCellSim1Identity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim1Identity.setStatus("current")
_ConfigPhyCellSim1Password_Type = DisplayString
_ConfigPhyCellSim1Password_Object = MibTableColumn
configPhyCellSim1Password = _ConfigPhyCellSim1Password_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 13),
    _ConfigPhyCellSim1Password_Type()
)
configPhyCellSim1Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim1Password.setStatus("current")
_ConfigPhyCellSim2Pin_Type = DisplayString
_ConfigPhyCellSim2Pin_Object = MibTableColumn
configPhyCellSim2Pin = _ConfigPhyCellSim2Pin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 14),
    _ConfigPhyCellSim2Pin_Type()
)
configPhyCellSim2Pin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim2Pin.setStatus("current")
_ConfigPhyCellSim2Apn_Type = DisplayString
_ConfigPhyCellSim2Apn_Object = MibTableColumn
configPhyCellSim2Apn = _ConfigPhyCellSim2Apn_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 15),
    _ConfigPhyCellSim2Apn_Type()
)
configPhyCellSim2Apn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim2Apn.setStatus("current")
_ConfigPhyCellSim2Authentication_Type = CellSecurityProtocol
_ConfigPhyCellSim2Authentication_Object = MibTableColumn
configPhyCellSim2Authentication = _ConfigPhyCellSim2Authentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 16),
    _ConfigPhyCellSim2Authentication_Type()
)
configPhyCellSim2Authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim2Authentication.setStatus("current")
_ConfigPhyCellSim2Identity_Type = DisplayString
_ConfigPhyCellSim2Identity_Object = MibTableColumn
configPhyCellSim2Identity = _ConfigPhyCellSim2Identity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 17),
    _ConfigPhyCellSim2Identity_Type()
)
configPhyCellSim2Identity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim2Identity.setStatus("current")
_ConfigPhyCellSim2Password_Type = DisplayString
_ConfigPhyCellSim2Password_Object = MibTableColumn
configPhyCellSim2Password = _ConfigPhyCellSim2Password_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 2, 2, 1, 18),
    _ConfigPhyCellSim2Password_Type()
)
configPhyCellSim2Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPhyCellSim2Password.setStatus("current")
_Netif_ObjectIdentity = ObjectIdentity
netif = _Netif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3)
)
_Netdetails_ObjectIdentity = ObjectIdentity
netdetails = _Netdetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1)
)
_ConfigRadiusTable_Object = MibTable
configRadiusTable = _ConfigRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    configRadiusTable.setStatus("current")
_ConfigRadiusEntry_Object = MibTableRow
configRadiusEntry = _ConfigRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1)
)
configRadiusEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configRadiusIndex"),
)
if mibBuilder.loadTexts:
    configRadiusEntry.setStatus("current")
_ConfigRadiusIndex_Type = Integer32
_ConfigRadiusIndex_Object = MibTableColumn
configRadiusIndex = _ConfigRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1, 1),
    _ConfigRadiusIndex_Type()
)
configRadiusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRadiusIndex.setStatus("current")
_ConfigRadiusRowStatus_Type = RowStatus
_ConfigRadiusRowStatus_Object = MibTableColumn
configRadiusRowStatus = _ConfigRadiusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1, 2),
    _ConfigRadiusRowStatus_Type()
)
configRadiusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configRadiusRowStatus.setStatus("current")
_ConfigRadiusIpAddress_Type = OctetString
_ConfigRadiusIpAddress_Object = MibTableColumn
configRadiusIpAddress = _ConfigRadiusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1, 3),
    _ConfigRadiusIpAddress_Type()
)
configRadiusIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRadiusIpAddress.setStatus("current")
_ConfigRadiusPort_Type = Integer32
_ConfigRadiusPort_Object = MibTableColumn
configRadiusPort = _ConfigRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1, 4),
    _ConfigRadiusPort_Type()
)
configRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRadiusPort.setStatus("current")
_ConfigRadiusSecret_Type = OctetString
_ConfigRadiusSecret_Object = MibTableColumn
configRadiusSecret = _ConfigRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 1, 1, 5),
    _ConfigRadiusSecret_Type()
)
configRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRadiusSecret.setStatus("current")


class _ConfigDetailsNasId_Type(OctetString):
    """Custom type configDetailsNasId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_ConfigDetailsNasId_Type.__name__ = "OctetString"
_ConfigDetailsNasId_Object = MibScalar
configDetailsNasId = _ConfigDetailsNasId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 2),
    _ConfigDetailsNasId_Type()
)
configDetailsNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDetailsNasId.setStatus("current")
_ConfigFilterGroupTable_Object = MibTable
configFilterGroupTable = _ConfigFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 3)
)
if mibBuilder.loadTexts:
    configFilterGroupTable.setStatus("current")
_ConfigFilterGroupEntry_Object = MibTableRow
configFilterGroupEntry = _ConfigFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 3, 1)
)
configFilterGroupEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configFilterGroupIndex"),
)
if mibBuilder.loadTexts:
    configFilterGroupEntry.setStatus("current")
_ConfigFilterGroupIndex_Type = OctetString
_ConfigFilterGroupIndex_Object = MibTableColumn
configFilterGroupIndex = _ConfigFilterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 3, 1, 1),
    _ConfigFilterGroupIndex_Type()
)
configFilterGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupIndex.setStatus("current")
_ConfigFilterGroupRowStatus_Type = RowStatus
_ConfigFilterGroupRowStatus_Object = MibTableColumn
configFilterGroupRowStatus = _ConfigFilterGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 3, 1, 2),
    _ConfigFilterGroupRowStatus_Type()
)
configFilterGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configFilterGroupRowStatus.setStatus("current")
_ConfigFilterGroupFriendlyName_Type = OctetString
_ConfigFilterGroupFriendlyName_Object = MibTableColumn
configFilterGroupFriendlyName = _ConfigFilterGroupFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 3, 1, 3),
    _ConfigFilterGroupFriendlyName_Type()
)
configFilterGroupFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupFriendlyName.setStatus("current")
_ConfigFilterGroupRuleTable_Object = MibTable
configFilterGroupRuleTable = _ConfigFilterGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    configFilterGroupRuleTable.setStatus("current")
_ConfigFilterGroupRuleEntry_Object = MibTableRow
configFilterGroupRuleEntry = _ConfigFilterGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1)
)
configFilterGroupRuleEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configFilterGroupRuleIndex"),
)
if mibBuilder.loadTexts:
    configFilterGroupRuleEntry.setStatus("current")
_ConfigFilterGroupRuleIndex_Type = OctetString
_ConfigFilterGroupRuleIndex_Object = MibTableColumn
configFilterGroupRuleIndex = _ConfigFilterGroupRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 1),
    _ConfigFilterGroupRuleIndex_Type()
)
configFilterGroupRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleIndex.setStatus("current")
_ConfigFilterGroupRuleRowStatus_Type = RowStatus
_ConfigFilterGroupRuleRowStatus_Object = MibTableColumn
configFilterGroupRuleRowStatus = _ConfigFilterGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 2),
    _ConfigFilterGroupRuleRowStatus_Type()
)
configFilterGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configFilterGroupRuleRowStatus.setStatus("current")
_ConfigFilterGroupGroupIndex_Type = OctetString
_ConfigFilterGroupGroupIndex_Object = MibTableColumn
configFilterGroupGroupIndex = _ConfigFilterGroupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 3),
    _ConfigFilterGroupGroupIndex_Type()
)
configFilterGroupGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupGroupIndex.setStatus("current")


class _ConfigFilterGroupRuleMACFrameType_Type(Integer32):
    """Custom type configFilterGroupRuleMACFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("nofilter", 1),
          ("unicast", 2),
          ("broadcast", 3),
          ("multicast", 4))
    )


_ConfigFilterGroupRuleMACFrameType_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleMACFrameType_Object = MibTableColumn
configFilterGroupRuleMACFrameType = _ConfigFilterGroupRuleMACFrameType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 4),
    _ConfigFilterGroupRuleMACFrameType_Type()
)
configFilterGroupRuleMACFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleMACFrameType.setStatus("current")


class _ConfigFilterGroupRuleCheckMAC_Type(Integer32):
    """Custom type configFilterGroupRuleCheckMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("source", 1),
          ("destination", 2))
    )


_ConfigFilterGroupRuleCheckMAC_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleCheckMAC_Object = MibTableColumn
configFilterGroupRuleCheckMAC = _ConfigFilterGroupRuleCheckMAC_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 5),
    _ConfigFilterGroupRuleCheckMAC_Type()
)
configFilterGroupRuleCheckMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleCheckMAC.setStatus("current")


class _ConfigFilterGroupRuleNetworkProtocol_Type(Integer32):
    """Custom type configFilterGroupRuleNetworkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              -3,
              -2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("arp", -3),
          ("ip", -2),
          ("nofilter", -1))
    )


_ConfigFilterGroupRuleNetworkProtocol_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleNetworkProtocol_Object = MibTableColumn
configFilterGroupRuleNetworkProtocol = _ConfigFilterGroupRuleNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 6),
    _ConfigFilterGroupRuleNetworkProtocol_Type()
)
configFilterGroupRuleNetworkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleNetworkProtocol.setStatus("current")
_ConfigFilterGroupRuleIpAddress_Type = IpAddress
_ConfigFilterGroupRuleIpAddress_Object = MibTableColumn
configFilterGroupRuleIpAddress = _ConfigFilterGroupRuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 7),
    _ConfigFilterGroupRuleIpAddress_Type()
)
configFilterGroupRuleIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleIpAddress.setStatus("current")
_ConfigFilterGroupRuleNetmask_Type = IpAddress
_ConfigFilterGroupRuleNetmask_Object = MibTableColumn
configFilterGroupRuleNetmask = _ConfigFilterGroupRuleNetmask_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 8),
    _ConfigFilterGroupRuleNetmask_Type()
)
configFilterGroupRuleNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleNetmask.setStatus("current")


class _ConfigFilterGroupRuleCheckIP_Type(Integer32):
    """Custom type configFilterGroupRuleCheckIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("source", 1),
          ("destination", 2))
    )


_ConfigFilterGroupRuleCheckIP_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleCheckIP_Object = MibTableColumn
configFilterGroupRuleCheckIP = _ConfigFilterGroupRuleCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 9),
    _ConfigFilterGroupRuleCheckIP_Type()
)
configFilterGroupRuleCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleCheckIP.setStatus("current")


class _ConfigFilterGroupRuleTransportProtocol_Type(Integer32):
    """Custom type configFilterGroupRuleTransportProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("nofilter", 1),
          ("udp", 2),
          ("tcp", 3),
          ("icmp", 4))
    )


_ConfigFilterGroupRuleTransportProtocol_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleTransportProtocol_Object = MibTableColumn
configFilterGroupRuleTransportProtocol = _ConfigFilterGroupRuleTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 10),
    _ConfigFilterGroupRuleTransportProtocol_Type()
)
configFilterGroupRuleTransportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleTransportProtocol.setStatus("current")


class _ConfigFilterGroupRuleFirstPort_Type(Integer32):
    """Custom type configFilterGroupRuleFirstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigFilterGroupRuleFirstPort_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleFirstPort_Object = MibTableColumn
configFilterGroupRuleFirstPort = _ConfigFilterGroupRuleFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 11),
    _ConfigFilterGroupRuleFirstPort_Type()
)
configFilterGroupRuleFirstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleFirstPort.setStatus("current")


class _ConfigFilterGroupRuleLastPort_Type(Integer32):
    """Custom type configFilterGroupRuleLastPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigFilterGroupRuleLastPort_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleLastPort_Object = MibTableColumn
configFilterGroupRuleLastPort = _ConfigFilterGroupRuleLastPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 12),
    _ConfigFilterGroupRuleLastPort_Type()
)
configFilterGroupRuleLastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleLastPort.setStatus("current")


class _ConfigFilterGroupRuleCheckPort_Type(Integer32):
    """Custom type configFilterGroupRuleCheckPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -255),
          ("source", 1),
          ("destination", 2))
    )


_ConfigFilterGroupRuleCheckPort_Type.__name__ = "Integer32"
_ConfigFilterGroupRuleCheckPort_Object = MibTableColumn
configFilterGroupRuleCheckPort = _ConfigFilterGroupRuleCheckPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 1, 4, 1, 13),
    _ConfigFilterGroupRuleCheckPort_Type()
)
configFilterGroupRuleCheckPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilterGroupRuleCheckPort.setStatus("current")
_ConfigInterfaceTable_Object = MibTable
configInterfaceTable = _ConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2)
)
if mibBuilder.loadTexts:
    configInterfaceTable.setStatus("current")
_ConfigInterfaceEntry_Object = MibTableRow
configInterfaceEntry = _ConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1)
)
configInterfaceEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configInterfaceName"),
)
if mibBuilder.loadTexts:
    configInterfaceEntry.setStatus("current")
_ConfigInterfaceName_Type = NetifName
_ConfigInterfaceName_Object = MibTableColumn
configInterfaceName = _ConfigInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 1),
    _ConfigInterfaceName_Type()
)
configInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configInterfaceName.setStatus("current")
_ConfigInterfaceRowStatus_Type = RowStatus
_ConfigInterfaceRowStatus_Object = MibTableColumn
configInterfaceRowStatus = _ConfigInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 2),
    _ConfigInterfaceRowStatus_Type()
)
configInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configInterfaceRowStatus.setStatus("current")


class _ConfigInterfaceType_Type(Integer32):
    """Custom type configInterfaceType based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mac-bridge", 2),
          ("wifi-sta", 3),
          ("wifi-ap", 4),
          ("wifi-11s", 5),
          ("wifi-rept", 6),
          ("wifi-adhoc", 7),
          ("vlan8021q", 8),
          ("l2tunnel-gre", 9),
          ("wifi-srcc", 10),
          ("cellular", 11),
          ("mac-bond", 12),
          ("wifi-monitor", 13))
    )


_ConfigInterfaceType_Type.__name__ = "Integer32"
_ConfigInterfaceType_Object = MibTableColumn
configInterfaceType = _ConfigInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 3),
    _ConfigInterfaceType_Type()
)
configInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configInterfaceType.setStatus("current")
_ConfigInterfaceDepends_Type = NetifName
_ConfigInterfaceDepends_Object = MibTableColumn
configInterfaceDepends = _ConfigInterfaceDepends_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 4),
    _ConfigInterfaceDepends_Type()
)
configInterfaceDepends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInterfaceDepends.setStatus("current")
_ConfigInterfaceOutputFilterGroup_Type = OctetString
_ConfigInterfaceOutputFilterGroup_Object = MibTableColumn
configInterfaceOutputFilterGroup = _ConfigInterfaceOutputFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 5),
    _ConfigInterfaceOutputFilterGroup_Type()
)
configInterfaceOutputFilterGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInterfaceOutputFilterGroup.setStatus("current")


class _ConfigInterfaceFilterGroupDir_Type(Integer32):
    """Custom type configInterfaceFilterGroupDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("in", 1),
          ("out", 2),
          ("inout", 3))
    )


_ConfigInterfaceFilterGroupDir_Type.__name__ = "Integer32"
_ConfigInterfaceFilterGroupDir_Object = MibTableColumn
configInterfaceFilterGroupDir = _ConfigInterfaceFilterGroupDir_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 6),
    _ConfigInterfaceFilterGroupDir_Type()
)
configInterfaceFilterGroupDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInterfaceFilterGroupDir.setStatus("obsolete")
_ConfigInterfaceInputFilterGroup_Type = OctetString
_ConfigInterfaceInputFilterGroup_Object = MibTableColumn
configInterfaceInputFilterGroup = _ConfigInterfaceInputFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 2, 1, 7),
    _ConfigInterfaceInputFilterGroup_Type()
)
configInterfaceInputFilterGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInterfaceInputFilterGroup.setStatus("current")
_ConfigIfStaTable_Object = MibTable
configIfStaTable = _ConfigIfStaTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3)
)
if mibBuilder.loadTexts:
    configIfStaTable.setStatus("current")
_ConfigIfStaEntry_Object = MibTableRow
configIfStaEntry = _ConfigIfStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1)
)
configIfStaEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfStaName"),
)
if mibBuilder.loadTexts:
    configIfStaEntry.setStatus("current")
_ConfigIfStaName_Type = NetifName
_ConfigIfStaName_Object = MibTableColumn
configIfStaName = _ConfigIfStaName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 1),
    _ConfigIfStaName_Type()
)
configIfStaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfStaName.setStatus("current")
_ConfigIfStaRowStatus_Type = RowStatus
_ConfigIfStaRowStatus_Object = MibTableColumn
configIfStaRowStatus = _ConfigIfStaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 2),
    _ConfigIfStaRowStatus_Type()
)
configIfStaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfStaRowStatus.setStatus("current")
_ConfigIfStaPhy_Type = NetifName
_ConfigIfStaPhy_Object = MibTableColumn
configIfStaPhy = _ConfigIfStaPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 3),
    _ConfigIfStaPhy_Type()
)
configIfStaPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfStaPhy.setStatus("current")


class _ConfigIfStaSsid_Type(OctetString):
    """Custom type configIfStaSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigIfStaSsid_Type.__name__ = "OctetString"
_ConfigIfStaSsid_Object = MibTableColumn
configIfStaSsid = _ConfigIfStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 4),
    _ConfigIfStaSsid_Type()
)
configIfStaSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaSsid.setStatus("current")
_ConfigIfStaBssid_Type = PhysAddress
_ConfigIfStaBssid_Object = MibTableColumn
configIfStaBssid = _ConfigIfStaBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 5),
    _ConfigIfStaBssid_Type()
)
configIfStaBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaBssid.setStatus("current")


class _ConfigIfStaBridgingMode_Type(Integer32):
    """Custom type configIfStaBridgingMode based on Integer32"""
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
        *(("arpnat", 1),
          ("four-addresses", 2),
          ("mono-eth-cloning", 3),
          ("mono-profinet-clonning", 4),
          ("multi-eth-cloning", 5))
    )


_ConfigIfStaBridgingMode_Type.__name__ = "Integer32"
_ConfigIfStaBridgingMode_Object = MibTableColumn
configIfStaBridgingMode = _ConfigIfStaBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 6),
    _ConfigIfStaBridgingMode_Type()
)
configIfStaBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaBridgingMode.setStatus("current")
_ConfigIfStaScanChannels_Type = OctetString
_ConfigIfStaScanChannels_Object = MibTableColumn
configIfStaScanChannels = _ConfigIfStaScanChannels_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 7),
    _ConfigIfStaScanChannels_Type()
)
configIfStaScanChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaScanChannels.setStatus("current")
_ConfigIfStaScanPassive_Type = DisableEnable
_ConfigIfStaScanPassive_Object = MibTableColumn
configIfStaScanPassive = _ConfigIfStaScanPassive_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 8),
    _ConfigIfStaScanPassive_Type()
)
configIfStaScanPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaScanPassive.setStatus("current")
_ConfigIfStaRoamingEnable_Type = DisableEnable
_ConfigIfStaRoamingEnable_Object = MibTableColumn
configIfStaRoamingEnable = _ConfigIfStaRoamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 9),
    _ConfigIfStaRoamingEnable_Type()
)
configIfStaRoamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingEnable.setStatus("current")
_ConfigIfStaRoamingEnableDBM_Type = Integer32
_ConfigIfStaRoamingEnableDBM_Object = MibTableColumn
configIfStaRoamingEnableDBM = _ConfigIfStaRoamingEnableDBM_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 10),
    _ConfigIfStaRoamingEnableDBM_Type()
)
configIfStaRoamingEnableDBM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingEnableDBM.setStatus("current")
_ConfigIfStaRoamingRequiredBoost_Type = Integer32
_ConfigIfStaRoamingRequiredBoost_Object = MibTableColumn
configIfStaRoamingRequiredBoost = _ConfigIfStaRoamingRequiredBoost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 11),
    _ConfigIfStaRoamingRequiredBoost_Type()
)
configIfStaRoamingRequiredBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingRequiredBoost.setStatus("current")
_ConfigIfStaRoamingScanPeriod_Type = Integer32
_ConfigIfStaRoamingScanPeriod_Object = MibTableColumn
configIfStaRoamingScanPeriod = _ConfigIfStaRoamingScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 12),
    _ConfigIfStaRoamingScanPeriod_Type()
)
configIfStaRoamingScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingScanPeriod.setStatus("current")
_ConfigIfStaSecurityMode_Type = SecurityModes
_ConfigIfStaSecurityMode_Object = MibTableColumn
configIfStaSecurityMode = _ConfigIfStaSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 13),
    _ConfigIfStaSecurityMode_Type()
)
configIfStaSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaSecurityMode.setStatus("current")
_ConfigIfStaWepKey1_Type = WepKeys
_ConfigIfStaWepKey1_Object = MibTableColumn
configIfStaWepKey1 = _ConfigIfStaWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 14),
    _ConfigIfStaWepKey1_Type()
)
configIfStaWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWepKey1.setStatus("current")
_ConfigIfStaWepKey2_Type = WepKeys
_ConfigIfStaWepKey2_Object = MibTableColumn
configIfStaWepKey2 = _ConfigIfStaWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 15),
    _ConfigIfStaWepKey2_Type()
)
configIfStaWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWepKey2.setStatus("current")
_ConfigIfStaWepKey3_Type = WepKeys
_ConfigIfStaWepKey3_Object = MibTableColumn
configIfStaWepKey3 = _ConfigIfStaWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 16),
    _ConfigIfStaWepKey3_Type()
)
configIfStaWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWepKey3.setStatus("current")
_ConfigIfStaWepKey4_Type = WepKeys
_ConfigIfStaWepKey4_Object = MibTableColumn
configIfStaWepKey4 = _ConfigIfStaWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 17),
    _ConfigIfStaWepKey4_Type()
)
configIfStaWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWepKey4.setStatus("current")
_ConfigIfStaWepKey_Type = Integer32
_ConfigIfStaWepKey_Object = MibTableColumn
configIfStaWepKey = _ConfigIfStaWepKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 18),
    _ConfigIfStaWepKey_Type()
)
configIfStaWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWepKey.setStatus("current")
_ConfigIfStaWpaVersion_Type = WpaVersions
_ConfigIfStaWpaVersion_Object = MibTableColumn
configIfStaWpaVersion = _ConfigIfStaWpaVersion_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 19),
    _ConfigIfStaWpaVersion_Type()
)
configIfStaWpaVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWpaVersion.setStatus("current")
_ConfigIfStaWpaCipher_Type = CipherTypes
_ConfigIfStaWpaCipher_Object = MibTableColumn
configIfStaWpaCipher = _ConfigIfStaWpaCipher_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 20),
    _ConfigIfStaWpaCipher_Type()
)
configIfStaWpaCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfStaWpaCipher.setStatus("current")
_ConfigIfStaIdentity_Type = OctetString
_ConfigIfStaIdentity_Object = MibTableColumn
configIfStaIdentity = _ConfigIfStaIdentity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 21),
    _ConfigIfStaIdentity_Type()
)
configIfStaIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaIdentity.setStatus("current")
_ConfigIfStaKey_Type = OctetString
_ConfigIfStaKey_Object = MibTableColumn
configIfStaKey = _ConfigIfStaKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 22),
    _ConfigIfStaKey_Type()
)
configIfStaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaKey.setStatus("current")
_ConfigIfStaPrivateKey_Type = OctetString
_ConfigIfStaPrivateKey_Object = MibTableColumn
configIfStaPrivateKey = _ConfigIfStaPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 23),
    _ConfigIfStaPrivateKey_Type()
)
configIfStaPrivateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaPrivateKey.setStatus("current")
_ConfigIfStaCACert_Type = OctetString
_ConfigIfStaCACert_Object = MibTableColumn
configIfStaCACert = _ConfigIfStaCACert_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 24),
    _ConfigIfStaCACert_Type()
)
configIfStaCACert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaCACert.setStatus("current")


class _ConfigIfStaEapType_Type(Integer32):
    """Custom type configIfStaEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eap-tls", 1),
          ("eap-peap", 2),
          ("eap-leap", 3))
    )


_ConfigIfStaEapType_Type.__name__ = "Integer32"
_ConfigIfStaEapType_Object = MibTableColumn
configIfStaEapType = _ConfigIfStaEapType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 25),
    _ConfigIfStaEapType_Type()
)
configIfStaEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaEapType.setStatus("current")
_ConfigIfStaAuthentication_Type = PeapSecurityProtocol
_ConfigIfStaAuthentication_Object = MibTableColumn
configIfStaAuthentication = _ConfigIfStaAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 26),
    _ConfigIfStaAuthentication_Type()
)
configIfStaAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaAuthentication.setStatus("current")
_ConfigIfStaFastBSSTransitionActivated_Type = DisableEnable
_ConfigIfStaFastBSSTransitionActivated_Object = MibTableColumn
configIfStaFastBSSTransitionActivated = _ConfigIfStaFastBSSTransitionActivated_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 27),
    _ConfigIfStaFastBSSTransitionActivated_Type()
)
configIfStaFastBSSTransitionActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaFastBSSTransitionActivated.setStatus("current")
_ConfigIfStaIgnorePreviousScansResults_Type = DisableEnable
_ConfigIfStaIgnorePreviousScansResults_Object = MibTableColumn
configIfStaIgnorePreviousScansResults = _ConfigIfStaIgnorePreviousScansResults_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 28),
    _ConfigIfStaIgnorePreviousScansResults_Type()
)
configIfStaIgnorePreviousScansResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaIgnorePreviousScansResults.setStatus("current")
_ConfigIfStaRoamingRssiSmoothingFactor_Type = Integer32
_ConfigIfStaRoamingRssiSmoothingFactor_Object = MibTableColumn
configIfStaRoamingRssiSmoothingFactor = _ConfigIfStaRoamingRssiSmoothingFactor_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 29),
    _ConfigIfStaRoamingRssiSmoothingFactor_Type()
)
configIfStaRoamingRssiSmoothingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingRssiSmoothingFactor.setStatus("current")
_ConfigIfStaRoamingBeaconTimeout_Type = Integer32
_ConfigIfStaRoamingBeaconTimeout_Object = MibTableColumn
configIfStaRoamingBeaconTimeout = _ConfigIfStaRoamingBeaconTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 30),
    _ConfigIfStaRoamingBeaconTimeout_Type()
)
configIfStaRoamingBeaconTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingBeaconTimeout.setStatus("current")
_ConfigIfStaWpaKeyCacheLifetime_Type = Integer32
_ConfigIfStaWpaKeyCacheLifetime_Object = MibTableColumn
configIfStaWpaKeyCacheLifetime = _ConfigIfStaWpaKeyCacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 31),
    _ConfigIfStaWpaKeyCacheLifetime_Type()
)
configIfStaWpaKeyCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaWpaKeyCacheLifetime.setStatus("current")
_ConfigIfStaRoamingCurrentApScanThreshold_Type = Integer32
_ConfigIfStaRoamingCurrentApScanThreshold_Object = MibTableColumn
configIfStaRoamingCurrentApScanThreshold = _ConfigIfStaRoamingCurrentApScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 32),
    _ConfigIfStaRoamingCurrentApScanThreshold_Type()
)
configIfStaRoamingCurrentApScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingCurrentApScanThreshold.setStatus("current")
_ConfigIfStaRoamingMinimumStaLevel_Type = Integer32
_ConfigIfStaRoamingMinimumStaLevel_Object = MibTableColumn
configIfStaRoamingMinimumStaLevel = _ConfigIfStaRoamingMinimumStaLevel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 33),
    _ConfigIfStaRoamingMinimumStaLevel_Type()
)
configIfStaRoamingMinimumStaLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingMinimumStaLevel.setStatus("current")
_ConfigIfStaRoamingAboveLevelThreshold_Type = Integer32
_ConfigIfStaRoamingAboveLevelThreshold_Object = MibTableColumn
configIfStaRoamingAboveLevelThreshold = _ConfigIfStaRoamingAboveLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 34),
    _ConfigIfStaRoamingAboveLevelThreshold_Type()
)
configIfStaRoamingAboveLevelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingAboveLevelThreshold.setStatus("current")
_ConfigIfStaRoamingMaxSignalLevel_Type = Integer32
_ConfigIfStaRoamingMaxSignalLevel_Object = MibTableColumn
configIfStaRoamingMaxSignalLevel = _ConfigIfStaRoamingMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 35),
    _ConfigIfStaRoamingMaxSignalLevel_Type()
)
configIfStaRoamingMaxSignalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingMaxSignalLevel.setStatus("current")
_ConfigIfStaRoamingMinRoamDelay_Type = Integer32
_ConfigIfStaRoamingMinRoamDelay_Object = MibTableColumn
configIfStaRoamingMinRoamDelay = _ConfigIfStaRoamingMinRoamDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 36),
    _ConfigIfStaRoamingMinRoamDelay_Type()
)
configIfStaRoamingMinRoamDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingMinRoamDelay.setStatus("current")
_ConfigIfStaRoamingNoReturnDelay_Type = Integer32
_ConfigIfStaRoamingNoReturnDelay_Object = MibTableColumn
configIfStaRoamingNoReturnDelay = _ConfigIfStaRoamingNoReturnDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 37),
    _ConfigIfStaRoamingNoReturnDelay_Type()
)
configIfStaRoamingNoReturnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingNoReturnDelay.setStatus("current")
_ConfigIfStaRoamingThresholdHysteresis_Type = Integer32
_ConfigIfStaRoamingThresholdHysteresis_Object = MibTableColumn
configIfStaRoamingThresholdHysteresis = _ConfigIfStaRoamingThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 38),
    _ConfigIfStaRoamingThresholdHysteresis_Type()
)
configIfStaRoamingThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingThresholdHysteresis.setStatus("current")
_ConfigIfStaRoamingOffChanMaxDelay_Type = Integer32
_ConfigIfStaRoamingOffChanMaxDelay_Object = MibTableColumn
configIfStaRoamingOffChanMaxDelay = _ConfigIfStaRoamingOffChanMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 39),
    _ConfigIfStaRoamingOffChanMaxDelay_Type()
)
configIfStaRoamingOffChanMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingOffChanMaxDelay.setStatus("current")
_ConfigIfStaRoamingOffChanProbeDelay_Type = Integer32
_ConfigIfStaRoamingOffChanProbeDelay_Object = MibTableColumn
configIfStaRoamingOffChanProbeDelay = _ConfigIfStaRoamingOffChanProbeDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 40),
    _ConfigIfStaRoamingOffChanProbeDelay_Type()
)
configIfStaRoamingOffChanProbeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingOffChanProbeDelay.setStatus("current")
_ConfigIfStaRoamingPerChanProbeDelay_Type = Integer32
_ConfigIfStaRoamingPerChanProbeDelay_Object = MibTableColumn
configIfStaRoamingPerChanProbeDelay = _ConfigIfStaRoamingPerChanProbeDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 41),
    _ConfigIfStaRoamingPerChanProbeDelay_Type()
)
configIfStaRoamingPerChanProbeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaRoamingPerChanProbeDelay.setStatus("current")
_ConfigIfStaUserCert_Type = OctetString
_ConfigIfStaUserCert_Object = MibTableColumn
configIfStaUserCert = _ConfigIfStaUserCert_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 42),
    _ConfigIfStaUserCert_Type()
)
configIfStaUserCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaUserCert.setStatus("current")
_ConfigIfStaDeauthBeforeRoamingtoNextAP_Type = DisableEnable
_ConfigIfStaDeauthBeforeRoamingtoNextAP_Object = MibTableColumn
configIfStaDeauthBeforeRoamingtoNextAP = _ConfigIfStaDeauthBeforeRoamingtoNextAP_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 3, 1, 43),
    _ConfigIfStaDeauthBeforeRoamingtoNextAP_Type()
)
configIfStaDeauthBeforeRoamingtoNextAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfStaDeauthBeforeRoamingtoNextAP.setStatus("current")
_ConfigIfAPTable_Object = MibTable
configIfAPTable = _ConfigIfAPTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4)
)
if mibBuilder.loadTexts:
    configIfAPTable.setStatus("current")
_ConfigIfAPEntry_Object = MibTableRow
configIfAPEntry = _ConfigIfAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1)
)
configIfAPEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfAPName"),
)
if mibBuilder.loadTexts:
    configIfAPEntry.setStatus("current")
_ConfigIfAPName_Type = NetifName
_ConfigIfAPName_Object = MibTableColumn
configIfAPName = _ConfigIfAPName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 1),
    _ConfigIfAPName_Type()
)
configIfAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfAPName.setStatus("current")
_ConfigIfAPRowStatus_Type = RowStatus
_ConfigIfAPRowStatus_Object = MibTableColumn
configIfAPRowStatus = _ConfigIfAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 2),
    _ConfigIfAPRowStatus_Type()
)
configIfAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfAPRowStatus.setStatus("current")
_ConfigIfAPPhy_Type = NetifName
_ConfigIfAPPhy_Object = MibTableColumn
configIfAPPhy = _ConfigIfAPPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 3),
    _ConfigIfAPPhy_Type()
)
configIfAPPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfAPPhy.setStatus("current")


class _ConfigIfAPSsid_Type(OctetString):
    """Custom type configIfAPSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigIfAPSsid_Type.__name__ = "OctetString"
_ConfigIfAPSsid_Object = MibTableColumn
configIfAPSsid = _ConfigIfAPSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 4),
    _ConfigIfAPSsid_Type()
)
configIfAPSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPSsid.setStatus("current")
_ConfigIfAPHidden_Type = DisableEnable
_ConfigIfAPHidden_Object = MibTableColumn
configIfAPHidden = _ConfigIfAPHidden_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 5),
    _ConfigIfAPHidden_Type()
)
configIfAPHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPHidden.setStatus("current")
_ConfigIfAPWds_Type = DisableEnable
_ConfigIfAPWds_Object = MibTableColumn
configIfAPWds = _ConfigIfAPWds_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 6),
    _ConfigIfAPWds_Type()
)
configIfAPWds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWds.setStatus("current")
_ConfigIfAPIsolate_Type = DisableEnable
_ConfigIfAPIsolate_Object = MibTableColumn
configIfAPIsolate = _ConfigIfAPIsolate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 7),
    _ConfigIfAPIsolate_Type()
)
configIfAPIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPIsolate.setStatus("current")
_ConfigIfAPSecurityMode_Type = SecurityModes
_ConfigIfAPSecurityMode_Object = MibTableColumn
configIfAPSecurityMode = _ConfigIfAPSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 8),
    _ConfigIfAPSecurityMode_Type()
)
configIfAPSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPSecurityMode.setStatus("current")
_ConfigIfAPWepKey1_Type = WepKeys
_ConfigIfAPWepKey1_Object = MibTableColumn
configIfAPWepKey1 = _ConfigIfAPWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 9),
    _ConfigIfAPWepKey1_Type()
)
configIfAPWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepKey1.setStatus("current")
_ConfigIfAPWepKey2_Type = WepKeys
_ConfigIfAPWepKey2_Object = MibTableColumn
configIfAPWepKey2 = _ConfigIfAPWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 10),
    _ConfigIfAPWepKey2_Type()
)
configIfAPWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepKey2.setStatus("current")
_ConfigIfAPWepKey3_Type = WepKeys
_ConfigIfAPWepKey3_Object = MibTableColumn
configIfAPWepKey3 = _ConfigIfAPWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 11),
    _ConfigIfAPWepKey3_Type()
)
configIfAPWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepKey3.setStatus("current")
_ConfigIfAPWepKey4_Type = WepKeys
_ConfigIfAPWepKey4_Object = MibTableColumn
configIfAPWepKey4 = _ConfigIfAPWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 12),
    _ConfigIfAPWepKey4_Type()
)
configIfAPWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepKey4.setStatus("current")
_ConfigIfAPWepKey_Type = Integer32
_ConfigIfAPWepKey_Object = MibTableColumn
configIfAPWepKey = _ConfigIfAPWepKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 13),
    _ConfigIfAPWepKey_Type()
)
configIfAPWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepKey.setStatus("current")


class _ConfigIfAPWepAuthentication_Type(Integer32):
    """Custom type configIfAPWepAuthentication based on Integer32"""
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


_ConfigIfAPWepAuthentication_Type.__name__ = "Integer32"
_ConfigIfAPWepAuthentication_Object = MibTableColumn
configIfAPWepAuthentication = _ConfigIfAPWepAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 14),
    _ConfigIfAPWepAuthentication_Type()
)
configIfAPWepAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWepAuthentication.setStatus("current")
_ConfigIfAPWpaVersion_Type = WpaVersions
_ConfigIfAPWpaVersion_Object = MibTableColumn
configIfAPWpaVersion = _ConfigIfAPWpaVersion_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 15),
    _ConfigIfAPWpaVersion_Type()
)
configIfAPWpaVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWpaVersion.setStatus("current")
_ConfigIfAPWpaCipher_Type = CipherTypes
_ConfigIfAPWpaCipher_Object = MibTableColumn
configIfAPWpaCipher = _ConfigIfAPWpaCipher_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 16),
    _ConfigIfAPWpaCipher_Type()
)
configIfAPWpaCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfAPWpaCipher.setStatus("current")


class _ConfigIfAPKey_Type(OctetString):
    """Custom type configIfAPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_ConfigIfAPKey_Type.__name__ = "OctetString"
_ConfigIfAPKey_Object = MibTableColumn
configIfAPKey = _ConfigIfAPKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 17),
    _ConfigIfAPKey_Type()
)
configIfAPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPKey.setStatus("current")
_ConfigIfAPRadiusIndex_Type = Integer32
_ConfigIfAPRadiusIndex_Object = MibTableColumn
configIfAPRadiusIndex = _ConfigIfAPRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 18),
    _ConfigIfAPRadiusIndex_Type()
)
configIfAPRadiusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPRadiusIndex.setStatus("current")
_ConfigIfAPPreAuthentication_Type = DisableEnable
_ConfigIfAPPreAuthentication_Object = MibTableColumn
configIfAPPreAuthentication = _ConfigIfAPPreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 19),
    _ConfigIfAPPreAuthentication_Type()
)
configIfAPPreAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPPreAuthentication.setStatus("current")


class _ConfigIfAPMACFilterBehaviour_Type(Integer32):
    """Custom type configIfAPMACFilterBehaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("denyMAC", 2),
          ("allowMAC", 3))
    )


_ConfigIfAPMACFilterBehaviour_Type.__name__ = "Integer32"
_ConfigIfAPMACFilterBehaviour_Object = MibTableColumn
configIfAPMACFilterBehaviour = _ConfigIfAPMACFilterBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 20),
    _ConfigIfAPMACFilterBehaviour_Type()
)
configIfAPMACFilterBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPMACFilterBehaviour.setStatus("current")
_ConfigIfAPMACFilterAddresses_Type = OctetString
_ConfigIfAPMACFilterAddresses_Object = MibTableColumn
configIfAPMACFilterAddresses = _ConfigIfAPMACFilterAddresses_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 21),
    _ConfigIfAPMACFilterAddresses_Type()
)
configIfAPMACFilterAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPMACFilterAddresses.setStatus("current")
_ConfigIfAPWpaGroupRekey_Type = Integer32
_ConfigIfAPWpaGroupRekey_Object = MibTableColumn
configIfAPWpaGroupRekey = _ConfigIfAPWpaGroupRekey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 22),
    _ConfigIfAPWpaGroupRekey_Type()
)
configIfAPWpaGroupRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWpaGroupRekey.setStatus("current")
_ConfigIfAPWpaPairRekey_Type = Integer32
_ConfigIfAPWpaPairRekey_Object = MibTableColumn
configIfAPWpaPairRekey = _ConfigIfAPWpaPairRekey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 23),
    _ConfigIfAPWpaPairRekey_Type()
)
configIfAPWpaPairRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWpaPairRekey.setStatus("current")
_ConfigIfAPWpaMasterRekey_Type = Integer32
_ConfigIfAPWpaMasterRekey_Object = MibTableColumn
configIfAPWpaMasterRekey = _ConfigIfAPWpaMasterRekey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 24),
    _ConfigIfAPWpaMasterRekey_Type()
)
configIfAPWpaMasterRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWpaMasterRekey.setStatus("current")


class _ConfigIfAPWpaProtectedFrame_Type(Integer32):
    """Custom type configIfAPWpaProtectedFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enable-optional", 2),
          ("enable-required", 3))
    )


_ConfigIfAPWpaProtectedFrame_Type.__name__ = "Integer32"
_ConfigIfAPWpaProtectedFrame_Object = MibTableColumn
configIfAPWpaProtectedFrame = _ConfigIfAPWpaProtectedFrame_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 25),
    _ConfigIfAPWpaProtectedFrame_Type()
)
configIfAPWpaProtectedFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPWpaProtectedFrame.setStatus("current")
_ConfigIfAPMaxSimultaneousAssoc_Type = Integer32
_ConfigIfAPMaxSimultaneousAssoc_Object = MibTableColumn
configIfAPMaxSimultaneousAssoc = _ConfigIfAPMaxSimultaneousAssoc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 26),
    _ConfigIfAPMaxSimultaneousAssoc_Type()
)
configIfAPMaxSimultaneousAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPMaxSimultaneousAssoc.setStatus("current")
_ConfigIfAPPasspointConfigName_Type = OctetString
_ConfigIfAPPasspointConfigName_Object = MibTableColumn
configIfAPPasspointConfigName = _ConfigIfAPPasspointConfigName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 4, 1, 27),
    _ConfigIfAPPasspointConfigName_Type()
)
configIfAPPasspointConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfAPPasspointConfigName.setStatus("current")
_ConfigIfMeshTable_Object = MibTable
configIfMeshTable = _ConfigIfMeshTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5)
)
if mibBuilder.loadTexts:
    configIfMeshTable.setStatus("current")
_ConfigIfMeshEntry_Object = MibTableRow
configIfMeshEntry = _ConfigIfMeshEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1)
)
configIfMeshEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfMeshName"),
)
if mibBuilder.loadTexts:
    configIfMeshEntry.setStatus("current")
_ConfigIfMeshName_Type = NetifName
_ConfigIfMeshName_Object = MibTableColumn
configIfMeshName = _ConfigIfMeshName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 1),
    _ConfigIfMeshName_Type()
)
configIfMeshName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfMeshName.setStatus("current")
_ConfigIfMeshRowStatus_Type = RowStatus
_ConfigIfMeshRowStatus_Object = MibTableColumn
configIfMeshRowStatus = _ConfigIfMeshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 2),
    _ConfigIfMeshRowStatus_Type()
)
configIfMeshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfMeshRowStatus.setStatus("current")
_ConfigIfMeshPhy_Type = NetifName
_ConfigIfMeshPhy_Object = MibTableColumn
configIfMeshPhy = _ConfigIfMeshPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 3),
    _ConfigIfMeshPhy_Type()
)
configIfMeshPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfMeshPhy.setStatus("current")


class _ConfigIfMeshId_Type(OctetString):
    """Custom type configIfMeshId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigIfMeshId_Type.__name__ = "OctetString"
_ConfigIfMeshId_Object = MibTableColumn
configIfMeshId = _ConfigIfMeshId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 4),
    _ConfigIfMeshId_Type()
)
configIfMeshId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshId.setStatus("current")


class _ConfigIfMeshSecurityMode_Type(Integer32):
    """Custom type configIfMeshSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sae", 5))
    )


_ConfigIfMeshSecurityMode_Type.__name__ = "Integer32"
_ConfigIfMeshSecurityMode_Object = MibTableColumn
configIfMeshSecurityMode = _ConfigIfMeshSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 5),
    _ConfigIfMeshSecurityMode_Type()
)
configIfMeshSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshSecurityMode.setStatus("current")


class _ConfigIfMeshPreSharedKey_Type(OctetString):
    """Custom type configIfMeshPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_ConfigIfMeshPreSharedKey_Type.__name__ = "OctetString"
_ConfigIfMeshPreSharedKey_Object = MibTableColumn
configIfMeshPreSharedKey = _ConfigIfMeshPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 6),
    _ConfigIfMeshPreSharedKey_Type()
)
configIfMeshPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshPreSharedKey.setStatus("current")
_ConfigIfMeshPathRefreshTime_Type = Integer32
_ConfigIfMeshPathRefreshTime_Object = MibTableColumn
configIfMeshPathRefreshTime = _ConfigIfMeshPathRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 7),
    _ConfigIfMeshPathRefreshTime_Type()
)
configIfMeshPathRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshPathRefreshTime.setStatus("current")
_ConfigIfMeshMinDiscoveryTimeout_Type = Integer32
_ConfigIfMeshMinDiscoveryTimeout_Object = MibTableColumn
configIfMeshMinDiscoveryTimeout = _ConfigIfMeshMinDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 8),
    _ConfigIfMeshMinDiscoveryTimeout_Type()
)
configIfMeshMinDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshMinDiscoveryTimeout.setStatus("current")
_ConfigIfMeshActivePathTimeout_Type = Integer32
_ConfigIfMeshActivePathTimeout_Object = MibTableColumn
configIfMeshActivePathTimeout = _ConfigIfMeshActivePathTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 9),
    _ConfigIfMeshActivePathTimeout_Type()
)
configIfMeshActivePathTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshActivePathTimeout.setStatus("current")
_ConfigIfMeshNetworkDiameterTraversalTime_Type = Integer32
_ConfigIfMeshNetworkDiameterTraversalTime_Object = MibTableColumn
configIfMeshNetworkDiameterTraversalTime = _ConfigIfMeshNetworkDiameterTraversalTime_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 10),
    _ConfigIfMeshNetworkDiameterTraversalTime_Type()
)
configIfMeshNetworkDiameterTraversalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshNetworkDiameterTraversalTime.setStatus("current")


class _ConfigIfMeshRootMode_Type(Integer32):
    """Custom type configIfMeshRootMode based on Integer32"""
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
        *(("notroot", 1),
          ("proactivepreq", 2),
          ("proactivepreqprep", 3),
          ("proactiverann", 4))
    )


_ConfigIfMeshRootMode_Type.__name__ = "Integer32"
_ConfigIfMeshRootMode_Object = MibTableColumn
configIfMeshRootMode = _ConfigIfMeshRootMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 11),
    _ConfigIfMeshRootMode_Type()
)
configIfMeshRootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshRootMode.setStatus("current")
_ConfigIfMeshGatesAnnouncement_Type = DisableEnable
_ConfigIfMeshGatesAnnouncement_Object = MibTableColumn
configIfMeshGatesAnnouncement = _ConfigIfMeshGatesAnnouncement_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 12),
    _ConfigIfMeshGatesAnnouncement_Type()
)
configIfMeshGatesAnnouncement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshGatesAnnouncement.setStatus("current")
_ConfigIfMeshActivePathToRootTimeout_Type = Integer32
_ConfigIfMeshActivePathToRootTimeout_Object = MibTableColumn
configIfMeshActivePathToRootTimeout = _ConfigIfMeshActivePathToRootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 13),
    _ConfigIfMeshActivePathToRootTimeout_Type()
)
configIfMeshActivePathToRootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshActivePathToRootTimeout.setStatus("current")
_ConfigIfMeshPreqRootInterval_Type = Integer32
_ConfigIfMeshPreqRootInterval_Object = MibTableColumn
configIfMeshPreqRootInterval = _ConfigIfMeshPreqRootInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 14),
    _ConfigIfMeshPreqRootInterval_Type()
)
configIfMeshPreqRootInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshPreqRootInterval.setStatus("current")
_ConfigIfMeshRannRootInterval_Type = Integer32
_ConfigIfMeshRannRootInterval_Object = MibTableColumn
configIfMeshRannRootInterval = _ConfigIfMeshRannRootInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 5, 1, 15),
    _ConfigIfMeshRannRootInterval_Type()
)
configIfMeshRannRootInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfMeshRannRootInterval.setStatus("current")
_ConfigIfBridgeTable_Object = MibTable
configIfBridgeTable = _ConfigIfBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6)
)
if mibBuilder.loadTexts:
    configIfBridgeTable.setStatus("current")
_ConfigIfBridgeEntry_Object = MibTableRow
configIfBridgeEntry = _ConfigIfBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1)
)
configIfBridgeEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfBridgeName"),
)
if mibBuilder.loadTexts:
    configIfBridgeEntry.setStatus("current")
_ConfigIfBridgeName_Type = NetifName
_ConfigIfBridgeName_Object = MibTableColumn
configIfBridgeName = _ConfigIfBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 1),
    _ConfigIfBridgeName_Type()
)
configIfBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfBridgeName.setStatus("current")
_ConfigIfBridgeRowStatus_Type = RowStatus
_ConfigIfBridgeRowStatus_Object = MibTableColumn
configIfBridgeRowStatus = _ConfigIfBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 2),
    _ConfigIfBridgeRowStatus_Type()
)
configIfBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfBridgeRowStatus.setStatus("current")


class _ConfigIfBridgeStp_Type(Integer32):
    """Custom type configIfBridgeStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("rstp", 2),
          ("stp-only", 3))
    )


_ConfigIfBridgeStp_Type.__name__ = "Integer32"
_ConfigIfBridgeStp_Object = MibTableColumn
configIfBridgeStp = _ConfigIfBridgeStp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 3),
    _ConfigIfBridgeStp_Type()
)
configIfBridgeStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgeStp.setStatus("current")
_ConfigIfBridgePriority_Type = Integer32
_ConfigIfBridgePriority_Object = MibTableColumn
configIfBridgePriority = _ConfigIfBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 4),
    _ConfigIfBridgePriority_Type()
)
configIfBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgePriority.setStatus("current")
_ConfigIfBridgeHello_Type = Integer32
_ConfigIfBridgeHello_Object = MibTableColumn
configIfBridgeHello = _ConfigIfBridgeHello_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 5),
    _ConfigIfBridgeHello_Type()
)
configIfBridgeHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgeHello.setStatus("current")
_ConfigIfBridgeMaxAge_Type = Integer32
_ConfigIfBridgeMaxAge_Object = MibTableColumn
configIfBridgeMaxAge = _ConfigIfBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 6),
    _ConfigIfBridgeMaxAge_Type()
)
configIfBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgeMaxAge.setStatus("current")
_ConfigIfBridgeForwardDelay_Type = Integer32
_ConfigIfBridgeForwardDelay_Object = MibTableColumn
configIfBridgeForwardDelay = _ConfigIfBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 7),
    _ConfigIfBridgeForwardDelay_Type()
)
configIfBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgeForwardDelay.setStatus("current")
_ConfigIfBridgeLldpForward_Type = DisableEnable
_ConfigIfBridgeLldpForward_Object = MibTableColumn
configIfBridgeLldpForward = _ConfigIfBridgeLldpForward_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 6, 1, 8),
    _ConfigIfBridgeLldpForward_Type()
)
configIfBridgeLldpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfBridgeLldpForward.setStatus("current")
_ConfigIfVlanTable_Object = MibTable
configIfVlanTable = _ConfigIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7)
)
if mibBuilder.loadTexts:
    configIfVlanTable.setStatus("current")
_ConfigIfVlanEntry_Object = MibTableRow
configIfVlanEntry = _ConfigIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1)
)
configIfVlanEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfVlanIndex"),
)
if mibBuilder.loadTexts:
    configIfVlanEntry.setStatus("current")
_ConfigIfVlanIndex_Type = OctetString
_ConfigIfVlanIndex_Object = MibTableColumn
configIfVlanIndex = _ConfigIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1, 1),
    _ConfigIfVlanIndex_Type()
)
configIfVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfVlanIndex.setStatus("current")
_ConfigIfVlanRowStatus_Type = RowStatus
_ConfigIfVlanRowStatus_Object = MibTableColumn
configIfVlanRowStatus = _ConfigIfVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1, 2),
    _ConfigIfVlanRowStatus_Type()
)
configIfVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfVlanRowStatus.setStatus("current")
_ConfigIfVlanFriendlyName_Type = OctetString
_ConfigIfVlanFriendlyName_Object = MibTableColumn
configIfVlanFriendlyName = _ConfigIfVlanFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1, 3),
    _ConfigIfVlanFriendlyName_Type()
)
configIfVlanFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfVlanFriendlyName.setStatus("current")
_ConfigIfVlanHostIfName_Type = NetifName
_ConfigIfVlanHostIfName_Object = MibTableColumn
configIfVlanHostIfName = _ConfigIfVlanHostIfName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1, 4),
    _ConfigIfVlanHostIfName_Type()
)
configIfVlanHostIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfVlanHostIfName.setStatus("current")
_ConfigIfVlanId_Type = Integer32
_ConfigIfVlanId_Object = MibTableColumn
configIfVlanId = _ConfigIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 7, 1, 5),
    _ConfigIfVlanId_Type()
)
configIfVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfVlanId.setStatus("current")
_ConfigIfSrccTable_Object = MibTable
configIfSrccTable = _ConfigIfSrccTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8)
)
if mibBuilder.loadTexts:
    configIfSrccTable.setStatus("current")
_ConfigIfSrccEntry_Object = MibTableRow
configIfSrccEntry = _ConfigIfSrccEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1)
)
configIfSrccEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configIfSrccName"),
)
if mibBuilder.loadTexts:
    configIfSrccEntry.setStatus("current")
_ConfigIfSrccName_Type = NetifName
_ConfigIfSrccName_Object = MibTableColumn
configIfSrccName = _ConfigIfSrccName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 1),
    _ConfigIfSrccName_Type()
)
configIfSrccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfSrccName.setStatus("current")
_ConfigIfSrccRowStatus_Type = RowStatus
_ConfigIfSrccRowStatus_Object = MibTableColumn
configIfSrccRowStatus = _ConfigIfSrccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 2),
    _ConfigIfSrccRowStatus_Type()
)
configIfSrccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configIfSrccRowStatus.setStatus("current")
_ConfigIfSrccPhy_Type = NetifName
_ConfigIfSrccPhy_Object = MibTableColumn
configIfSrccPhy = _ConfigIfSrccPhy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 3),
    _ConfigIfSrccPhy_Type()
)
configIfSrccPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIfSrccPhy.setStatus("current")


class _ConfigIfSrccDiscoverApSsid_Type(OctetString):
    """Custom type configIfSrccDiscoverApSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigIfSrccDiscoverApSsid_Type.__name__ = "OctetString"
_ConfigIfSrccDiscoverApSsid_Object = MibTableColumn
configIfSrccDiscoverApSsid = _ConfigIfSrccDiscoverApSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 4),
    _ConfigIfSrccDiscoverApSsid_Type()
)
configIfSrccDiscoverApSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccDiscoverApSsid.setStatus("current")


class _ConfigIfSrccProductType_Type(Integer32):
    """Custom type configIfSrccProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeA", 1),
          ("typeB", 2))
    )


_ConfigIfSrccProductType_Type.__name__ = "Integer32"
_ConfigIfSrccProductType_Object = MibTableColumn
configIfSrccProductType = _ConfigIfSrccProductType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 5),
    _ConfigIfSrccProductType_Type()
)
configIfSrccProductType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccProductType.setStatus("current")
_ConfigIfSrccDiscSigThreshold_Type = Integer32
_ConfigIfSrccDiscSigThreshold_Object = MibTableColumn
configIfSrccDiscSigThreshold = _ConfigIfSrccDiscSigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 6),
    _ConfigIfSrccDiscSigThreshold_Type()
)
configIfSrccDiscSigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccDiscSigThreshold.setStatus("current")
_ConfigIfSrccDiscDuration_Type = Integer32
_ConfigIfSrccDiscDuration_Object = MibTableColumn
configIfSrccDiscDuration = _ConfigIfSrccDiscDuration_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 7),
    _ConfigIfSrccDiscDuration_Type()
)
configIfSrccDiscDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccDiscDuration.setStatus("current")
_ConfigIfSrccBrokenThreshold_Type = Integer32
_ConfigIfSrccBrokenThreshold_Object = MibTableColumn
configIfSrccBrokenThreshold = _ConfigIfSrccBrokenThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 8),
    _ConfigIfSrccBrokenThreshold_Type()
)
configIfSrccBrokenThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccBrokenThreshold.setStatus("current")
_ConfigIfSrccBrokenDuration_Type = Integer32
_ConfigIfSrccBrokenDuration_Object = MibTableColumn
configIfSrccBrokenDuration = _ConfigIfSrccBrokenDuration_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 9),
    _ConfigIfSrccBrokenDuration_Type()
)
configIfSrccBrokenDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccBrokenDuration.setStatus("current")


class _ConfigIfSrccWifiBand_Type(Integer32):
    """Custom type configIfSrccWifiBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band-5g", 1),
          ("band-24", 2))
    )


_ConfigIfSrccWifiBand_Type.__name__ = "Integer32"
_ConfigIfSrccWifiBand_Object = MibTableColumn
configIfSrccWifiBand = _ConfigIfSrccWifiBand_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 10),
    _ConfigIfSrccWifiBand_Type()
)
configIfSrccWifiBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccWifiBand.setStatus("current")
_ConfigIfSrccFirstChannel_Type = Integer32
_ConfigIfSrccFirstChannel_Object = MibTableColumn
configIfSrccFirstChannel = _ConfigIfSrccFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 11),
    _ConfigIfSrccFirstChannel_Type()
)
configIfSrccFirstChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccFirstChannel.setStatus("current")
_ConfigIfSrccSecondChannel_Type = Integer32
_ConfigIfSrccSecondChannel_Object = MibTableColumn
configIfSrccSecondChannel = _ConfigIfSrccSecondChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 12),
    _ConfigIfSrccSecondChannel_Type()
)
configIfSrccSecondChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccSecondChannel.setStatus("current")
_ConfigIfSrccDiscScanDuration_Type = Integer32
_ConfigIfSrccDiscScanDuration_Object = MibTableColumn
configIfSrccDiscScanDuration = _ConfigIfSrccDiscScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 13),
    _ConfigIfSrccDiscScanDuration_Type()
)
configIfSrccDiscScanDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccDiscScanDuration.setStatus("current")


class _ConfigIfSrccMixRedundancy_Type(Integer32):
    """Custom type configIfSrccMixRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wifi", 1),
          ("ethernet", 2),
          ("none", 3))
    )


_ConfigIfSrccMixRedundancy_Type.__name__ = "Integer32"
_ConfigIfSrccMixRedundancy_Object = MibTableColumn
configIfSrccMixRedundancy = _ConfigIfSrccMixRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 14),
    _ConfigIfSrccMixRedundancy_Type()
)
configIfSrccMixRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccMixRedundancy.setStatus("current")
_ConfigIfSrccMixRedundancyBoost_Type = Integer32
_ConfigIfSrccMixRedundancyBoost_Object = MibTableColumn
configIfSrccMixRedundancyBoost = _ConfigIfSrccMixRedundancyBoost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 15),
    _ConfigIfSrccMixRedundancyBoost_Type()
)
configIfSrccMixRedundancyBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccMixRedundancyBoost.setStatus("current")
_ConfigIfSrccPeerTableTimeout_Type = Integer32
_ConfigIfSrccPeerTableTimeout_Object = MibTableColumn
configIfSrccPeerTableTimeout = _ConfigIfSrccPeerTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 16),
    _ConfigIfSrccPeerTableTimeout_Type()
)
configIfSrccPeerTableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccPeerTableTimeout.setStatus("current")
_ConfigIfSrccTargetTableTimeout_Type = Integer32
_ConfigIfSrccTargetTableTimeout_Object = MibTableColumn
configIfSrccTargetTableTimeout = _ConfigIfSrccTargetTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 17),
    _ConfigIfSrccTargetTableTimeout_Type()
)
configIfSrccTargetTableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccTargetTableTimeout.setStatus("current")
_ConfigIfSrccPeerAcknowTimeout_Type = Integer32
_ConfigIfSrccPeerAcknowTimeout_Object = MibTableColumn
configIfSrccPeerAcknowTimeout = _ConfigIfSrccPeerAcknowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 18),
    _ConfigIfSrccPeerAcknowTimeout_Type()
)
configIfSrccPeerAcknowTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccPeerAcknowTimeout.setStatus("current")
_ConfigIfSrccPeerReconfigTimeout_Type = Integer32
_ConfigIfSrccPeerReconfigTimeout_Object = MibTableColumn
configIfSrccPeerReconfigTimeout = _ConfigIfSrccPeerReconfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 19),
    _ConfigIfSrccPeerReconfigTimeout_Type()
)
configIfSrccPeerReconfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccPeerReconfigTimeout.setStatus("current")
_ConfigIfSrccGreBridgeIpAddr_Type = IpAddress
_ConfigIfSrccGreBridgeIpAddr_Object = MibTableColumn
configIfSrccGreBridgeIpAddr = _ConfigIfSrccGreBridgeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 3, 8, 1, 20),
    _ConfigIfSrccGreBridgeIpAddr_Type()
)
configIfSrccGreBridgeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIfSrccGreBridgeIpAddr.setStatus("current")
_Roaming_ObjectIdentity = ObjectIdentity
roaming = _Roaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4)
)


class _RoamingAlgorithm_Type(Integer32):
    """Custom type roamingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("scan", 1),
          ("cbb", 2),
          ("plh", 3))
    )


_RoamingAlgorithm_Type.__name__ = "Integer32"
_RoamingAlgorithm_Object = MibScalar
roamingAlgorithm = _RoamingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 1),
    _RoamingAlgorithm_Type()
)
roamingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingAlgorithm.setStatus("current")


class _RoamingPLHposition_Type(Integer32):
    """Custom type roamingPLHposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("front", 1),
          ("rear", 2))
    )


_RoamingPLHposition_Type.__name__ = "Integer32"
_RoamingPLHposition_Object = MibScalar
roamingPLHposition = _RoamingPLHposition_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 2),
    _RoamingPLHposition_Type()
)
roamingPLHposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHposition.setStatus("current")


class _RoamingPLHjitter_Type(Integer32):
    """Custom type roamingPLHjitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_RoamingPLHjitter_Type.__name__ = "Integer32"
_RoamingPLHjitter_Object = MibScalar
roamingPLHjitter = _RoamingPLHjitter_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 3),
    _RoamingPLHjitter_Type()
)
roamingPLHjitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHjitter.setStatus("current")
_RoamingPLHurgent_Type = WifiLevel
_RoamingPLHurgent_Object = MibScalar
roamingPLHurgent = _RoamingPLHurgent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 4),
    _RoamingPLHurgent_Type()
)
roamingPLHurgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHurgent.setStatus("current")
_RoamingPLHfront_ObjectIdentity = ObjectIdentity
roamingPLHfront = _RoamingPLHfront_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 5)
)
_RoamingPLHfrontCandMin_Type = WifiLevel
_RoamingPLHfrontCandMin_Object = MibScalar
roamingPLHfrontCandMin = _RoamingPLHfrontCandMin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 5, 1),
    _RoamingPLHfrontCandMin_Type()
)
roamingPLHfrontCandMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHfrontCandMin.setStatus("current")
_RoamingPLHfrontCandMax_Type = WifiLevel
_RoamingPLHfrontCandMax_Object = MibScalar
roamingPLHfrontCandMax = _RoamingPLHfrontCandMax_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 5, 2),
    _RoamingPLHfrontCandMax_Type()
)
roamingPLHfrontCandMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHfrontCandMax.setStatus("current")
_RoamingPLHfrontCurrentLow_Type = WifiLevel
_RoamingPLHfrontCurrentLow_Object = MibScalar
roamingPLHfrontCurrentLow = _RoamingPLHfrontCurrentLow_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 5, 3),
    _RoamingPLHfrontCurrentLow_Type()
)
roamingPLHfrontCurrentLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHfrontCurrentLow.setStatus("current")
_RoamingPLHfrontCurrentHigh_Type = WifiLevel
_RoamingPLHfrontCurrentHigh_Object = MibScalar
roamingPLHfrontCurrentHigh = _RoamingPLHfrontCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 5, 4),
    _RoamingPLHfrontCurrentHigh_Type()
)
roamingPLHfrontCurrentHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHfrontCurrentHigh.setStatus("current")
_RoamingPLHrear_ObjectIdentity = ObjectIdentity
roamingPLHrear = _RoamingPLHrear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 6)
)
_RoamingPLHrearCandMin_Type = WifiLevel
_RoamingPLHrearCandMin_Object = MibScalar
roamingPLHrearCandMin = _RoamingPLHrearCandMin_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 6, 1),
    _RoamingPLHrearCandMin_Type()
)
roamingPLHrearCandMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHrearCandMin.setStatus("current")
_RoamingPLHrearCandMax_Type = WifiLevel
_RoamingPLHrearCandMax_Object = MibScalar
roamingPLHrearCandMax = _RoamingPLHrearCandMax_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 6, 2),
    _RoamingPLHrearCandMax_Type()
)
roamingPLHrearCandMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHrearCandMax.setStatus("current")
_RoamingPLHrearCurrentLow_Type = WifiLevel
_RoamingPLHrearCurrentLow_Object = MibScalar
roamingPLHrearCurrentLow = _RoamingPLHrearCurrentLow_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 6, 3),
    _RoamingPLHrearCurrentLow_Type()
)
roamingPLHrearCurrentLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHrearCurrentLow.setStatus("current")
_RoamingPLHrearCurrentHigh_Type = WifiLevel
_RoamingPLHrearCurrentHigh_Object = MibScalar
roamingPLHrearCurrentHigh = _RoamingPLHrearCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 28097, 8, 4, 6, 4),
    _RoamingPLHrearCurrentHigh_Type()
)
roamingPLHrearCurrentHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamingPLHrearCurrentHigh.setStatus("current")
_ServiceStatus_ObjectIdentity = ObjectIdentity
serviceStatus = _ServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9)
)
_Ss_webserver_ObjectIdentity = ObjectIdentity
ss_webserver = _Ss_webserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 1)
)
_Ss_dhcp_ObjectIdentity = ObjectIdentity
ss_dhcp = _Ss_dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 2)
)
_Ss_ntp_ObjectIdentity = ObjectIdentity
ss_ntp = _Ss_ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 3)
)
_Ss_radius_ObjectIdentity = ObjectIdentity
ss_radius = _Ss_radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 4)
)
_Ss_snmp_ObjectIdentity = ObjectIdentity
ss_snmp = _Ss_snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 5)
)
_SnmpAgentOIDTable_Object = MibTable
snmpAgentOIDTable = _SnmpAgentOIDTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 5, 1)
)
if mibBuilder.loadTexts:
    snmpAgentOIDTable.setStatus("current")
_SnmpAgentOIDEntry_Object = MibTableRow
snmpAgentOIDEntry = _SnmpAgentOIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 5, 1, 1)
)
snmpAgentOIDEntry.setIndexNames(
    (0, "ACKSYS-MIB", "snmpAgentOIDIndex"),
)
if mibBuilder.loadTexts:
    snmpAgentOIDEntry.setStatus("current")
_SnmpAgentOIDIndex_Type = Integer32
_SnmpAgentOIDIndex_Object = MibTableColumn
snmpAgentOIDIndex = _SnmpAgentOIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 5, 1, 1, 1),
    _SnmpAgentOIDIndex_Type()
)
snmpAgentOIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentOIDIndex.setStatus("current")
_SnmpAgentOIDProductID_Type = Integer32
_SnmpAgentOIDProductID_Object = MibTableColumn
snmpAgentOIDProductID = _SnmpAgentOIDProductID_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 5, 1, 1, 2),
    _SnmpAgentOIDProductID_Type()
)
snmpAgentOIDProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentOIDProductID.setStatus("current")
_Ss_dns_ObjectIdentity = ObjectIdentity
ss_dns = _Ss_dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 6)
)
_Ss_system_ObjectIdentity = ObjectIdentity
ss_system = _Ss_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7)
)


class _SystemReady_Type(Integer32):
    """Custom type systemReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 1),
          ("ready", 2))
    )


_SystemReady_Type.__name__ = "Integer32"
_SystemReady_Object = MibScalar
systemReady = _SystemReady_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 1),
    _SystemReady_Type()
)
systemReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemReady.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2)
)
_TempSensors_ObjectIdentity = ObjectIdentity
tempSensors = _TempSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 1)
)
_MotherBoard0_Type = Integer32
_MotherBoard0_Object = MibScalar
motherBoard0 = _MotherBoard0_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 1, 1),
    _MotherBoard0_Type()
)
motherBoard0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motherBoard0.setStatus("current")
_GpioInTable_Object = MibTable
gpioInTable = _GpioInTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gpioInTable.setStatus("current")
_GpioInEntry_Object = MibTableRow
gpioInEntry = _GpioInEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 2, 1)
)
gpioInEntry.setIndexNames(
    (0, "ACKSYS-MIB", "gpioInIndex"),
)
if mibBuilder.loadTexts:
    gpioInEntry.setStatus("current")
_GpioInIndex_Type = Integer32
_GpioInIndex_Object = MibTableColumn
gpioInIndex = _GpioInIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 2, 1, 1),
    _GpioInIndex_Type()
)
gpioInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInIndex.setStatus("current")
_GpioInState_Type = Integer32
_GpioInState_Object = MibTableColumn
gpioInState = _GpioInState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 2, 1, 2),
    _GpioInState_Type()
)
gpioInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInState.setStatus("current")
_GpioOutTable_Object = MibTable
gpioOutTable = _GpioOutTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 3)
)
if mibBuilder.loadTexts:
    gpioOutTable.setStatus("current")
_GpioOutEntry_Object = MibTableRow
gpioOutEntry = _GpioOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 3, 1)
)
gpioOutEntry.setIndexNames(
    (0, "ACKSYS-MIB", "gpioOutIndex"),
)
if mibBuilder.loadTexts:
    gpioOutEntry.setStatus("current")
_GpioOutIndex_Type = Integer32
_GpioOutIndex_Object = MibTableColumn
gpioOutIndex = _GpioOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 3, 1, 1),
    _GpioOutIndex_Type()
)
gpioOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioOutIndex.setStatus("current")
_GpioOutState_Type = Integer32
_GpioOutState_Object = MibTableColumn
gpioOutState = _GpioOutState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 7, 2, 3, 1, 2),
    _GpioOutState_Type()
)
gpioOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpioOutState.setStatus("current")
_Ss_gnss_ObjectIdentity = ObjectIdentity
ss_gnss = _Ss_gnss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8)
)
_Gnss_current_position_ObjectIdentity = ObjectIdentity
gnss_current_position = _Gnss_current_position_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1)
)


class _PositionValid_Type(Integer32):
    """Custom type positionValid based on Integer32"""
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


_PositionValid_Type.__name__ = "Integer32"
_PositionValid_Object = MibScalar
positionValid = _PositionValid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 1),
    _PositionValid_Type()
)
positionValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positionValid.setStatus("current")
_Fixdate_Type = OctetString
_Fixdate_Object = MibScalar
fixdate = _Fixdate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 2),
    _Fixdate_Type()
)
fixdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fixdate.setStatus("current")
_Fixtime_Type = OctetString
_Fixtime_Object = MibScalar
fixtime = _Fixtime_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 3),
    _Fixtime_Type()
)
fixtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fixtime.setStatus("current")
_Latitude_Type = OctetString
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 4),
    _Latitude_Type()
)
latitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Longitude_Type = OctetString
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 5),
    _Longitude_Type()
)
longitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    longitude.setStatus("current")
_Altitude_Type = OctetString
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 6),
    _Altitude_Type()
)
altitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_Speedkmh_Type = OctetString
_Speedkmh_Object = MibScalar
speedkmh = _Speedkmh_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 7),
    _Speedkmh_Type()
)
speedkmh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedkmh.setStatus("current")
_CourseDegrees_Type = OctetString
_CourseDegrees_Object = MibScalar
courseDegrees = _CourseDegrees_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 8),
    _CourseDegrees_Type()
)
courseDegrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    courseDegrees.setStatus("current")
_Fixdimension_Type = Integer32
_Fixdimension_Object = MibScalar
fixdimension = _Fixdimension_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 9),
    _Fixdimension_Type()
)
fixdimension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fixdimension.setStatus("current")
_GnssAllPositions_Type = OctetString
_GnssAllPositions_Object = MibScalar
gnssAllPositions = _GnssAllPositions_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 8, 1, 10),
    _GnssAllPositions_Type()
)
gnssAllPositions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssAllPositions.setStatus("current")
_Ss_tcn_ObjectIdentity = ObjectIdentity
ss_tcn = _Ss_tcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 9)
)
_Ss_async_sysupgrade_ObjectIdentity = ObjectIdentity
ss_async_sysupgrade = _Ss_async_sysupgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 9, 10)
)


class _FirmwareExists_Type(Integer32):
    """Custom type firmwareExists based on Integer32"""
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


_FirmwareExists_Type.__name__ = "Integer32"
_FirmwareExists_Object = MibScalar
firmwareExists = _FirmwareExists_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 10, 1),
    _FirmwareExists_Type()
)
firmwareExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareExists.setStatus("current")
_FirmwareInfo_Type = OctetString
_FirmwareInfo_Object = MibScalar
firmwareInfo = _FirmwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 10, 2),
    _FirmwareInfo_Type()
)
firmwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareInfo.setStatus("current")


class _SysupgradeMissed_Type(Integer32):
    """Custom type sysupgradeMissed based on Integer32"""
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


_SysupgradeMissed_Type.__name__ = "Integer32"
_SysupgradeMissed_Object = MibScalar
sysupgradeMissed = _SysupgradeMissed_Object(
    (1, 3, 6, 1, 4, 1, 28097, 9, 10, 3),
    _SysupgradeMissed_Type()
)
sysupgradeMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysupgradeMissed.setStatus("current")
_ServiceConfiguration_ObjectIdentity = ObjectIdentity
serviceConfiguration = _ServiceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10)
)
_Sc_webserver_ObjectIdentity = ObjectIdentity
sc_webserver = _Sc_webserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1)
)
_ConfigHttpServer_Type = DisableEnable
_ConfigHttpServer_Object = MibScalar
configHttpServer = _ConfigHttpServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1, 1),
    _ConfigHttpServer_Type()
)
configHttpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHttpServer.setStatus("current")


class _ConfigHttpServerPort_Type(Integer32):
    """Custom type configHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigHttpServerPort_Type.__name__ = "Integer32"
_ConfigHttpServerPort_Object = MibScalar
configHttpServerPort = _ConfigHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1, 2),
    _ConfigHttpServerPort_Type()
)
configHttpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHttpServerPort.setStatus("current")
_ConfigHttpsServer_Type = DisableEnable
_ConfigHttpsServer_Object = MibScalar
configHttpsServer = _ConfigHttpsServer_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1, 3),
    _ConfigHttpsServer_Type()
)
configHttpsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHttpsServer.setStatus("current")


class _ConfigHttpsPort_Type(Integer32):
    """Custom type configHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigHttpsPort_Type.__name__ = "Integer32"
_ConfigHttpsPort_Object = MibScalar
configHttpsPort = _ConfigHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1, 4),
    _ConfigHttpsPort_Type()
)
configHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHttpsPort.setStatus("current")
_ConfigHttpsCertificate_Type = OctetString
_ConfigHttpsCertificate_Object = MibScalar
configHttpsCertificate = _ConfigHttpsCertificate_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 1, 5),
    _ConfigHttpsCertificate_Type()
)
configHttpsCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHttpsCertificate.setStatus("current")
_Sc_dhcp_ObjectIdentity = ObjectIdentity
sc_dhcp = _Sc_dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2)
)
_ConfigDhcpTable_Object = MibTable
configDhcpTable = _ConfigDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1)
)
if mibBuilder.loadTexts:
    configDhcpTable.setStatus("current")
_ConfigDhcpEntry_Object = MibTableRow
configDhcpEntry = _ConfigDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1)
)
configDhcpEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configDhcpSubnet"),
)
if mibBuilder.loadTexts:
    configDhcpEntry.setStatus("current")
_ConfigDhcpSubnet_Type = NetifName
_ConfigDhcpSubnet_Object = MibTableColumn
configDhcpSubnet = _ConfigDhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 1),
    _ConfigDhcpSubnet_Type()
)
configDhcpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDhcpSubnet.setStatus("current")
_ConfigDhcpRowStatus_Type = RowStatus
_ConfigDhcpRowStatus_Object = MibTableColumn
configDhcpRowStatus = _ConfigDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 2),
    _ConfigDhcpRowStatus_Type()
)
configDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configDhcpRowStatus.setStatus("current")
_ConfigDhcpEnable_Type = DisableEnable
_ConfigDhcpEnable_Object = MibTableColumn
configDhcpEnable = _ConfigDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 3),
    _ConfigDhcpEnable_Type()
)
configDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDhcpEnable.setStatus("current")
_ConfigDhcpPoolStart_Type = Integer32
_ConfigDhcpPoolStart_Object = MibTableColumn
configDhcpPoolStart = _ConfigDhcpPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 4),
    _ConfigDhcpPoolStart_Type()
)
configDhcpPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDhcpPoolStart.setStatus("current")
_ConfigDhcpPoolCount_Type = Integer32
_ConfigDhcpPoolCount_Object = MibTableColumn
configDhcpPoolCount = _ConfigDhcpPoolCount_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 5),
    _ConfigDhcpPoolCount_Type()
)
configDhcpPoolCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDhcpPoolCount.setStatus("current")
_ConfigDhcpLeaseDuration_Type = Integer32
_ConfigDhcpLeaseDuration_Object = MibTableColumn
configDhcpLeaseDuration = _ConfigDhcpLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 2, 1, 1, 6),
    _ConfigDhcpLeaseDuration_Type()
)
configDhcpLeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDhcpLeaseDuration.setStatus("current")
_Sc_ntp_ObjectIdentity = ObjectIdentity
sc_ntp = _Sc_ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 3)
)
_ConfigNtp_Type = Integer32
_ConfigNtp_Object = MibScalar
configNtp = _ConfigNtp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 3, 1),
    _ConfigNtp_Type()
)
configNtp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configNtp.setStatus("current")
_Sc_radius_ObjectIdentity = ObjectIdentity
sc_radius = _Sc_radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 4)
)
_Sc_snmp_ObjectIdentity = ObjectIdentity
sc_snmp = _Sc_snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 5)
)
_Sc_dns_ObjectIdentity = ObjectIdentity
sc_dns = _Sc_dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 6)
)
_ConfigRelay_ObjectIdentity = ObjectIdentity
configRelay = _ConfigRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 6, 1)
)
_ConfigDnsRebindProtection_Type = DisableEnable
_ConfigDnsRebindProtection_Object = MibScalar
configDnsRebindProtection = _ConfigDnsRebindProtection_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 6, 1, 1),
    _ConfigDnsRebindProtection_Type()
)
configDnsRebindProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDnsRebindProtection.setStatus("current")
_ConfigDnsRebindLocalhost_Type = DisableEnable
_ConfigDnsRebindLocalhost_Object = MibScalar
configDnsRebindLocalhost = _ConfigDnsRebindLocalhost_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 6, 1, 2),
    _ConfigDnsRebindLocalhost_Type()
)
configDnsRebindLocalhost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDnsRebindLocalhost.setStatus("current")
_Sc_ssh_ObjectIdentity = ObjectIdentity
sc_ssh = _Sc_ssh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 7)
)
_ConfigSshEnable_Type = DisableEnable
_ConfigSshEnable_Object = MibScalar
configSshEnable = _ConfigSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 7, 1),
    _ConfigSshEnable_Type()
)
configSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSshEnable.setStatus("current")
_ConfigSshEnablePwd_Type = DisableEnable
_ConfigSshEnablePwd_Object = MibScalar
configSshEnablePwd = _ConfigSshEnablePwd_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 7, 2),
    _ConfigSshEnablePwd_Type()
)
configSshEnablePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSshEnablePwd.setStatus("current")
_Sc_tcn_ObjectIdentity = ObjectIdentity
sc_tcn = _Sc_tcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 8)
)
_Sc_collectd_ObjectIdentity = ObjectIdentity
sc_collectd = _Sc_collectd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9)
)
_ConfigCollectdEnable_Type = DisableEnable
_ConfigCollectdEnable_Object = MibScalar
configCollectdEnable = _ConfigCollectdEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 1),
    _ConfigCollectdEnable_Type()
)
configCollectdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdEnable.setStatus("current")


class _ConfigCollectdSamplingInterval_Type(Integer32):
    """Custom type configCollectdSamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCollectdSamplingInterval_Type.__name__ = "Integer32"
_ConfigCollectdSamplingInterval_Object = MibScalar
configCollectdSamplingInterval = _ConfigCollectdSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 2),
    _ConfigCollectdSamplingInterval_Type()
)
configCollectdSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdSamplingInterval.setStatus("current")
_Plugin_GPS_ObjectIdentity = ObjectIdentity
plugin_GPS = _Plugin_GPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3)
)
_ConfigCollectdGPSEnable_Type = DisableEnable
_ConfigCollectdGPSEnable_Object = MibScalar
configCollectdGPSEnable = _ConfigCollectdGPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3, 1),
    _ConfigCollectdGPSEnable_Type()
)
configCollectdGPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdGPSEnable.setStatus("current")
_ConfigCollectdGPSServerAddr_Type = IpAddress
_ConfigCollectdGPSServerAddr_Object = MibScalar
configCollectdGPSServerAddr = _ConfigCollectdGPSServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3, 2),
    _ConfigCollectdGPSServerAddr_Type()
)
configCollectdGPSServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdGPSServerAddr.setStatus("current")


class _ConfigCollectdGPSServerPort_Type(Integer32):
    """Custom type configCollectdGPSServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigCollectdGPSServerPort_Type.__name__ = "Integer32"
_ConfigCollectdGPSServerPort_Object = MibScalar
configCollectdGPSServerPort = _ConfigCollectdGPSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3, 3),
    _ConfigCollectdGPSServerPort_Type()
)
configCollectdGPSServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdGPSServerPort.setStatus("current")


class _ConfigCollectdGPSConnTimeout_Type(Integer32):
    """Custom type configCollectdGPSConnTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCollectdGPSConnTimeout_Type.__name__ = "Integer32"
_ConfigCollectdGPSConnTimeout_Object = MibScalar
configCollectdGPSConnTimeout = _ConfigCollectdGPSConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3, 4),
    _ConfigCollectdGPSConnTimeout_Type()
)
configCollectdGPSConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdGPSConnTimeout.setStatus("current")


class _ConfigCollectdGPSReqInterval_Type(Integer32):
    """Custom type configCollectdGPSReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCollectdGPSReqInterval_Type.__name__ = "Integer32"
_ConfigCollectdGPSReqInterval_Object = MibScalar
configCollectdGPSReqInterval = _ConfigCollectdGPSReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 3, 5),
    _ConfigCollectdGPSReqInterval_Type()
)
configCollectdGPSReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdGPSReqInterval.setStatus("current")
_Plugin_AcksysScanResult_ObjectIdentity = ObjectIdentity
plugin_AcksysScanResult = _Plugin_AcksysScanResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 4)
)
_ConfigCollectdWirelessScanResult_Type = DisableEnable
_ConfigCollectdWirelessScanResult_Object = MibScalar
configCollectdWirelessScanResult = _ConfigCollectdWirelessScanResult_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 4, 1),
    _ConfigCollectdWirelessScanResult_Type()
)
configCollectdWirelessScanResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdWirelessScanResult.setStatus("current")
_Plugin_iwinfo_ObjectIdentity = ObjectIdentity
plugin_iwinfo = _Plugin_iwinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 5)
)
_ConfigCollectdIwinfo_Type = DisableEnable
_ConfigCollectdIwinfo_Object = MibScalar
configCollectdIwinfo = _ConfigCollectdIwinfo_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 5, 1),
    _ConfigCollectdIwinfo_Type()
)
configCollectdIwinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCollectdIwinfo.setStatus("current")
_Plugin_AcksysTelemetry_ObjectIdentity = ObjectIdentity
plugin_AcksysTelemetry = _Plugin_AcksysTelemetry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 6)
)
_ConfigAcksysTelemetryEnable_Type = DisableEnable
_ConfigAcksysTelemetryEnable_Object = MibScalar
configAcksysTelemetryEnable = _ConfigAcksysTelemetryEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 6, 1),
    _ConfigAcksysTelemetryEnable_Type()
)
configAcksysTelemetryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAcksysTelemetryEnable.setStatus("current")


class _ConfigAcksysTelemetryServerPort_Type(Integer32):
    """Custom type configAcksysTelemetryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigAcksysTelemetryServerPort_Type.__name__ = "Integer32"
_ConfigAcksysTelemetryServerPort_Object = MibScalar
configAcksysTelemetryServerPort = _ConfigAcksysTelemetryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 6, 2),
    _ConfigAcksysTelemetryServerPort_Type()
)
configAcksysTelemetryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAcksysTelemetryServerPort.setStatus("current")


class _ConfigAcksysTelemetryOutputInterval_Type(Integer32):
    """Custom type configAcksysTelemetryOutputInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigAcksysTelemetryOutputInterval_Type.__name__ = "Integer32"
_ConfigAcksysTelemetryOutputInterval_Object = MibScalar
configAcksysTelemetryOutputInterval = _ConfigAcksysTelemetryOutputInterval_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 6, 3),
    _ConfigAcksysTelemetryOutputInterval_Type()
)
configAcksysTelemetryOutputInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAcksysTelemetryOutputInterval.setStatus("current")


class _ConfigAcksysTelemetryMaxBufferSize_Type(Integer32):
    """Custom type configAcksysTelemetryMaxBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigAcksysTelemetryMaxBufferSize_Type.__name__ = "Integer32"
_ConfigAcksysTelemetryMaxBufferSize_Object = MibScalar
configAcksysTelemetryMaxBufferSize = _ConfigAcksysTelemetryMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 9, 6, 4),
    _ConfigAcksysTelemetryMaxBufferSize_Type()
)
configAcksysTelemetryMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAcksysTelemetryMaxBufferSize.setStatus("current")
_Sc_passpoint_ObjectIdentity = ObjectIdentity
sc_passpoint = _Sc_passpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10)
)
_ConfigPasspointConfigTable_Object = MibTable
configPasspointConfigTable = _ConfigPasspointConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1)
)
if mibBuilder.loadTexts:
    configPasspointConfigTable.setStatus("current")
_ConfigPasspointConfigEntry_Object = MibTableRow
configPasspointConfigEntry = _ConfigPasspointConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1)
)
configPasspointConfigEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configPasspointConfigName"),
)
if mibBuilder.loadTexts:
    configPasspointConfigEntry.setStatus("current")
_ConfigPasspointConfigName_Type = OctetString
_ConfigPasspointConfigName_Object = MibTableColumn
configPasspointConfigName = _ConfigPasspointConfigName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 1),
    _ConfigPasspointConfigName_Type()
)
configPasspointConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigName.setStatus("current")
_ConfigPasspointConfigRowStatus_Type = RowStatus
_ConfigPasspointConfigRowStatus_Object = MibTableColumn
configPasspointConfigRowStatus = _ConfigPasspointConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 2),
    _ConfigPasspointConfigRowStatus_Type()
)
configPasspointConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configPasspointConfigRowStatus.setStatus("current")
_ConfigPasspointConfigAnqpAccessNetworkType_Type = Integer32
_ConfigPasspointConfigAnqpAccessNetworkType_Object = MibTableColumn
configPasspointConfigAnqpAccessNetworkType = _ConfigPasspointConfigAnqpAccessNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 3),
    _ConfigPasspointConfigAnqpAccessNetworkType_Type()
)
configPasspointConfigAnqpAccessNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpAccessNetworkType.setStatus("current")
_ConfigPasspointConfigAnqpInternet_Type = DisableEnable
_ConfigPasspointConfigAnqpInternet_Object = MibTableColumn
configPasspointConfigAnqpInternet = _ConfigPasspointConfigAnqpInternet_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 4),
    _ConfigPasspointConfigAnqpInternet_Type()
)
configPasspointConfigAnqpInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpInternet.setStatus("current")
_ConfigPasspointConfigAnqpAsra_Type = DisableEnable
_ConfigPasspointConfigAnqpAsra_Object = MibTableColumn
configPasspointConfigAnqpAsra = _ConfigPasspointConfigAnqpAsra_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 5),
    _ConfigPasspointConfigAnqpAsra_Type()
)
configPasspointConfigAnqpAsra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpAsra.setStatus("current")
_ConfigPasspointConfigAnqpEsr_Type = DisableEnable
_ConfigPasspointConfigAnqpEsr_Object = MibTableColumn
configPasspointConfigAnqpEsr = _ConfigPasspointConfigAnqpEsr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 6),
    _ConfigPasspointConfigAnqpEsr_Type()
)
configPasspointConfigAnqpEsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpEsr.setStatus("current")
_ConfigPasspointConfigAnqpUesa_Type = DisableEnable
_ConfigPasspointConfigAnqpUesa_Object = MibTableColumn
configPasspointConfigAnqpUesa = _ConfigPasspointConfigAnqpUesa_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 7),
    _ConfigPasspointConfigAnqpUesa_Type()
)
configPasspointConfigAnqpUesa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpUesa.setStatus("current")
_ConfigPasspointConfigAnqpHessid_Type = OctetString
_ConfigPasspointConfigAnqpHessid_Object = MibTableColumn
configPasspointConfigAnqpHessid = _ConfigPasspointConfigAnqpHessid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 8),
    _ConfigPasspointConfigAnqpHessid_Type()
)
configPasspointConfigAnqpHessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpHessid.setStatus("current")


class _ConfigPasspointConfigAnqpGasAddress3_Type(Integer32):
    """Custom type configPasspointConfigAnqpGasAddress3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 0),
          ("ieee80211-std", 1),
          ("non-compliant", 2))
    )


_ConfigPasspointConfigAnqpGasAddress3_Type.__name__ = "Integer32"
_ConfigPasspointConfigAnqpGasAddress3_Object = MibTableColumn
configPasspointConfigAnqpGasAddress3 = _ConfigPasspointConfigAnqpGasAddress3_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 9),
    _ConfigPasspointConfigAnqpGasAddress3_Type()
)
configPasspointConfigAnqpGasAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpGasAddress3.setStatus("current")
_ConfigPasspointConfigAnqpVenueProfile_Type = OctetString
_ConfigPasspointConfigAnqpVenueProfile_Object = MibTableColumn
configPasspointConfigAnqpVenueProfile = _ConfigPasspointConfigAnqpVenueProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 10),
    _ConfigPasspointConfigAnqpVenueProfile_Type()
)
configPasspointConfigAnqpVenueProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpVenueProfile.setStatus("current")
_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Type = OctetString
_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Object = MibTableColumn
configPasspointConfigAnqpRoamingConsortiumProfile = _ConfigPasspointConfigAnqpRoamingConsortiumProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 11),
    _ConfigPasspointConfigAnqpRoamingConsortiumProfile_Type()
)
configPasspointConfigAnqpRoamingConsortiumProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpRoamingConsortiumProfile.setStatus("current")
_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Type = OctetString
_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Object = MibTableColumn
configPasspointConfigAnqpNetworkAuthTypeProfile = _ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 12),
    _ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Type()
)
configPasspointConfigAnqpNetworkAuthTypeProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpNetworkAuthTypeProfile.setStatus("current")
_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Type = OctetString
_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Object = MibTableColumn
configPasspointConfigAnqpIpAddrTypeAvailProfile = _ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 13),
    _ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Type()
)
configPasspointConfigAnqpIpAddrTypeAvailProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpIpAddrTypeAvailProfile.setStatus("current")
_ConfigPasspointConfigAnqpDomainNameProfile_Type = OctetString
_ConfigPasspointConfigAnqpDomainNameProfile_Object = MibTableColumn
configPasspointConfigAnqpDomainNameProfile = _ConfigPasspointConfigAnqpDomainNameProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 14),
    _ConfigPasspointConfigAnqpDomainNameProfile_Type()
)
configPasspointConfigAnqpDomainNameProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpDomainNameProfile.setStatus("current")
_ConfigPasspointConfigAnqp3gppCellNetProfile_Type = OctetString
_ConfigPasspointConfigAnqp3gppCellNetProfile_Object = MibTableColumn
configPasspointConfigAnqp3gppCellNetProfile = _ConfigPasspointConfigAnqp3gppCellNetProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 15),
    _ConfigPasspointConfigAnqp3gppCellNetProfile_Type()
)
configPasspointConfigAnqp3gppCellNetProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqp3gppCellNetProfile.setStatus("current")
_ConfigPasspointConfigAnqpNaiRealmProfile_Type = OctetString
_ConfigPasspointConfigAnqpNaiRealmProfile_Object = MibTableColumn
configPasspointConfigAnqpNaiRealmProfile = _ConfigPasspointConfigAnqpNaiRealmProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 16),
    _ConfigPasspointConfigAnqpNaiRealmProfile_Type()
)
configPasspointConfigAnqpNaiRealmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpNaiRealmProfile.setStatus("current")
_ConfigPasspointConfigAnqpOverrideElementProfile_Type = OctetString
_ConfigPasspointConfigAnqpOverrideElementProfile_Object = MibTableColumn
configPasspointConfigAnqpOverrideElementProfile = _ConfigPasspointConfigAnqpOverrideElementProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 17),
    _ConfigPasspointConfigAnqpOverrideElementProfile_Type()
)
configPasspointConfigAnqpOverrideElementProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigAnqpOverrideElementProfile.setStatus("current")
_ConfigPasspointConfigHS20DisableDgaf_Type = DisableEnable
_ConfigPasspointConfigHS20DisableDgaf_Object = MibTableColumn
configPasspointConfigHS20DisableDgaf = _ConfigPasspointConfigHS20DisableDgaf_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 18),
    _ConfigPasspointConfigHS20DisableDgaf_Type()
)
configPasspointConfigHS20DisableDgaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20DisableDgaf.setStatus("current")
_ConfigPasspointConfigHS20DomainId_Type = Integer32
_ConfigPasspointConfigHS20DomainId_Object = MibTableColumn
configPasspointConfigHS20DomainId = _ConfigPasspointConfigHS20DomainId_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 19),
    _ConfigPasspointConfigHS20DomainId_Type()
)
configPasspointConfigHS20DomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20DomainId.setStatus("current")
_ConfigPasspointConfigHS20DeauthReqTimeout_Type = Integer32
_ConfigPasspointConfigHS20DeauthReqTimeout_Object = MibTableColumn
configPasspointConfigHS20DeauthReqTimeout = _ConfigPasspointConfigHS20DeauthReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 20),
    _ConfigPasspointConfigHS20DeauthReqTimeout_Type()
)
configPasspointConfigHS20DeauthReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20DeauthReqTimeout.setStatus("current")
_ConfigPasspointConfigHS20OsuSsid_Type = OctetString
_ConfigPasspointConfigHS20OsuSsid_Object = MibTableColumn
configPasspointConfigHS20OsuSsid = _ConfigPasspointConfigHS20OsuSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 21),
    _ConfigPasspointConfigHS20OsuSsid_Type()
)
configPasspointConfigHS20OsuSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20OsuSsid.setStatus("current")
_ConfigPasspointConfigHS20OperFriendlyNameProfile_Type = OctetString
_ConfigPasspointConfigHS20OperFriendlyNameProfile_Object = MibTableColumn
configPasspointConfigHS20OperFriendlyNameProfile = _ConfigPasspointConfigHS20OperFriendlyNameProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 22),
    _ConfigPasspointConfigHS20OperFriendlyNameProfile_Type()
)
configPasspointConfigHS20OperFriendlyNameProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20OperFriendlyNameProfile.setStatus("current")
_ConfigPasspointConfigHS20ConnCapProfile_Type = OctetString
_ConfigPasspointConfigHS20ConnCapProfile_Object = MibTableColumn
configPasspointConfigHS20ConnCapProfile = _ConfigPasspointConfigHS20ConnCapProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 23),
    _ConfigPasspointConfigHS20ConnCapProfile_Type()
)
configPasspointConfigHS20ConnCapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20ConnCapProfile.setStatus("current")
_ConfigPasspointConfigHS20WanMetricsProfile_Type = OctetString
_ConfigPasspointConfigHS20WanMetricsProfile_Object = MibTableColumn
configPasspointConfigHS20WanMetricsProfile = _ConfigPasspointConfigHS20WanMetricsProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 24),
    _ConfigPasspointConfigHS20WanMetricsProfile_Type()
)
configPasspointConfigHS20WanMetricsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20WanMetricsProfile.setStatus("current")
_ConfigPasspointConfigHS20OperClassProfile_Type = OctetString
_ConfigPasspointConfigHS20OperClassProfile_Object = MibTableColumn
configPasspointConfigHS20OperClassProfile = _ConfigPasspointConfigHS20OperClassProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 25),
    _ConfigPasspointConfigHS20OperClassProfile_Type()
)
configPasspointConfigHS20OperClassProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20OperClassProfile.setStatus("current")
_ConfigPasspointConfigHS20OsuProviderProfile_Type = OctetString
_ConfigPasspointConfigHS20OsuProviderProfile_Object = MibTableColumn
configPasspointConfigHS20OsuProviderProfile = _ConfigPasspointConfigHS20OsuProviderProfile_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 1, 1, 26),
    _ConfigPasspointConfigHS20OsuProviderProfile_Type()
)
configPasspointConfigHS20OsuProviderProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasspointConfigHS20OsuProviderProfile.setStatus("current")
_ConfigAnqpProfileVenueTable_Object = MibTable
configAnqpProfileVenueTable = _ConfigAnqpProfileVenueTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2)
)
if mibBuilder.loadTexts:
    configAnqpProfileVenueTable.setStatus("current")
_ConfigAnqpProfileVenueEntry_Object = MibTableRow
configAnqpProfileVenueEntry = _ConfigAnqpProfileVenueEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1)
)
configAnqpProfileVenueEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileVenueName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileVenueEntry.setStatus("current")
_ConfigProfileVenueName_Type = OctetString
_ConfigProfileVenueName_Object = MibTableColumn
configProfileVenueName = _ConfigProfileVenueName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 1),
    _ConfigProfileVenueName_Type()
)
configProfileVenueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileVenueName.setStatus("current")
_ConfigProfileVenueRowStatus_Type = RowStatus
_ConfigProfileVenueRowStatus_Object = MibTableColumn
configProfileVenueRowStatus = _ConfigProfileVenueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 2),
    _ConfigProfileVenueRowStatus_Type()
)
configProfileVenueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileVenueRowStatus.setStatus("current")
_ConfigProfileVenueDesc_Type = OctetString
_ConfigProfileVenueDesc_Object = MibTableColumn
configProfileVenueDesc = _ConfigProfileVenueDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 3),
    _ConfigProfileVenueDesc_Type()
)
configProfileVenueDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileVenueDesc.setStatus("current")
_ConfigVenueGroup_Type = Integer32
_ConfigVenueGroup_Object = MibTableColumn
configVenueGroup = _ConfigVenueGroup_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 4),
    _ConfigVenueGroup_Type()
)
configVenueGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVenueGroup.setStatus("current")
_ConfigVenueType_Type = Integer32
_ConfigVenueType_Object = MibTableColumn
configVenueType = _ConfigVenueType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 5),
    _ConfigVenueType_Type()
)
configVenueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVenueType.setStatus("current")
_ConfigVenueNameList_Type = OctetString
_ConfigVenueNameList_Object = MibTableColumn
configVenueNameList = _ConfigVenueNameList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 2, 1, 6),
    _ConfigVenueNameList_Type()
)
configVenueNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVenueNameList.setStatus("current")
_ConfigAnqpProfileRoamingConsortiumTable_Object = MibTable
configAnqpProfileRoamingConsortiumTable = _ConfigAnqpProfileRoamingConsortiumTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3)
)
if mibBuilder.loadTexts:
    configAnqpProfileRoamingConsortiumTable.setStatus("current")
_ConfigAnqpProfileRoamingConsortiumEntry_Object = MibTableRow
configAnqpProfileRoamingConsortiumEntry = _ConfigAnqpProfileRoamingConsortiumEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3, 1)
)
configAnqpProfileRoamingConsortiumEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileRoamingConsortiumName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileRoamingConsortiumEntry.setStatus("current")
_ConfigProfileRoamingConsortiumName_Type = OctetString
_ConfigProfileRoamingConsortiumName_Object = MibTableColumn
configProfileRoamingConsortiumName = _ConfigProfileRoamingConsortiumName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3, 1, 1),
    _ConfigProfileRoamingConsortiumName_Type()
)
configProfileRoamingConsortiumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileRoamingConsortiumName.setStatus("current")
_ConfigProfileRoamingConsortiumRowStatus_Type = RowStatus
_ConfigProfileRoamingConsortiumRowStatus_Object = MibTableColumn
configProfileRoamingConsortiumRowStatus = _ConfigProfileRoamingConsortiumRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3, 1, 2),
    _ConfigProfileRoamingConsortiumRowStatus_Type()
)
configProfileRoamingConsortiumRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileRoamingConsortiumRowStatus.setStatus("current")
_ConfigProfileRoamingConsortiumDesc_Type = OctetString
_ConfigProfileRoamingConsortiumDesc_Object = MibTableColumn
configProfileRoamingConsortiumDesc = _ConfigProfileRoamingConsortiumDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3, 1, 3),
    _ConfigProfileRoamingConsortiumDesc_Type()
)
configProfileRoamingConsortiumDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileRoamingConsortiumDesc.setStatus("current")
_ConfigRoamingConsortiumList_Type = OctetString
_ConfigRoamingConsortiumList_Object = MibTableColumn
configRoamingConsortiumList = _ConfigRoamingConsortiumList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 3, 1, 4),
    _ConfigRoamingConsortiumList_Type()
)
configRoamingConsortiumList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRoamingConsortiumList.setStatus("current")
_ConfigAnqpProfileNetworkAuthTypeTable_Object = MibTable
configAnqpProfileNetworkAuthTypeTable = _ConfigAnqpProfileNetworkAuthTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4)
)
if mibBuilder.loadTexts:
    configAnqpProfileNetworkAuthTypeTable.setStatus("current")
_ConfigAnqpProfileNetworkAuthTypeEntry_Object = MibTableRow
configAnqpProfileNetworkAuthTypeEntry = _ConfigAnqpProfileNetworkAuthTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4, 1)
)
configAnqpProfileNetworkAuthTypeEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileNetworkAuthTypeName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileNetworkAuthTypeEntry.setStatus("current")
_ConfigProfileNetworkAuthTypeName_Type = OctetString
_ConfigProfileNetworkAuthTypeName_Object = MibTableColumn
configProfileNetworkAuthTypeName = _ConfigProfileNetworkAuthTypeName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4, 1, 1),
    _ConfigProfileNetworkAuthTypeName_Type()
)
configProfileNetworkAuthTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileNetworkAuthTypeName.setStatus("current")
_ConfigProfileNetworkAuthTypeRowStatus_Type = RowStatus
_ConfigProfileNetworkAuthTypeRowStatus_Object = MibTableColumn
configProfileNetworkAuthTypeRowStatus = _ConfigProfileNetworkAuthTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4, 1, 2),
    _ConfigProfileNetworkAuthTypeRowStatus_Type()
)
configProfileNetworkAuthTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileNetworkAuthTypeRowStatus.setStatus("current")
_ConfigProfileNetworkAuthTypeDesc_Type = OctetString
_ConfigProfileNetworkAuthTypeDesc_Object = MibTableColumn
configProfileNetworkAuthTypeDesc = _ConfigProfileNetworkAuthTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4, 1, 3),
    _ConfigProfileNetworkAuthTypeDesc_Type()
)
configProfileNetworkAuthTypeDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileNetworkAuthTypeDesc.setStatus("current")
_ConfigNetworkAuthType_Type = OctetString
_ConfigNetworkAuthType_Object = MibTableColumn
configNetworkAuthType = _ConfigNetworkAuthType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 4, 1, 4),
    _ConfigNetworkAuthType_Type()
)
configNetworkAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetworkAuthType.setStatus("current")
_ConfigAnqpProfileIpAddrTypeAvailTable_Object = MibTable
configAnqpProfileIpAddrTypeAvailTable = _ConfigAnqpProfileIpAddrTypeAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5)
)
if mibBuilder.loadTexts:
    configAnqpProfileIpAddrTypeAvailTable.setStatus("current")
_ConfigAnqpProfileIpAddrTypeAvailEntry_Object = MibTableRow
configAnqpProfileIpAddrTypeAvailEntry = _ConfigAnqpProfileIpAddrTypeAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1)
)
configAnqpProfileIpAddrTypeAvailEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileIpAddrTypeAvailName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileIpAddrTypeAvailEntry.setStatus("current")
_ConfigProfileIpAddrTypeAvailName_Type = OctetString
_ConfigProfileIpAddrTypeAvailName_Object = MibTableColumn
configProfileIpAddrTypeAvailName = _ConfigProfileIpAddrTypeAvailName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1, 1),
    _ConfigProfileIpAddrTypeAvailName_Type()
)
configProfileIpAddrTypeAvailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileIpAddrTypeAvailName.setStatus("current")
_ConfigProfileIpAddrTypeAvailRowStatus_Type = RowStatus
_ConfigProfileIpAddrTypeAvailRowStatus_Object = MibTableColumn
configProfileIpAddrTypeAvailRowStatus = _ConfigProfileIpAddrTypeAvailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1, 2),
    _ConfigProfileIpAddrTypeAvailRowStatus_Type()
)
configProfileIpAddrTypeAvailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileIpAddrTypeAvailRowStatus.setStatus("current")
_ConfigProfileIpAddrTypeAvailDesc_Type = OctetString
_ConfigProfileIpAddrTypeAvailDesc_Object = MibTableColumn
configProfileIpAddrTypeAvailDesc = _ConfigProfileIpAddrTypeAvailDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1, 3),
    _ConfigProfileIpAddrTypeAvailDesc_Type()
)
configProfileIpAddrTypeAvailDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileIpAddrTypeAvailDesc.setStatus("current")
_ConfigIpv4Type_Type = Integer32
_ConfigIpv4Type_Object = MibTableColumn
configIpv4Type = _ConfigIpv4Type_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1, 4),
    _ConfigIpv4Type_Type()
)
configIpv4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpv4Type.setStatus("current")
_ConfigIpv6Type_Type = Integer32
_ConfigIpv6Type_Object = MibTableColumn
configIpv6Type = _ConfigIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 5, 1, 5),
    _ConfigIpv6Type_Type()
)
configIpv6Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpv6Type.setStatus("current")
_ConfigAnqpProfileDomainNameTable_Object = MibTable
configAnqpProfileDomainNameTable = _ConfigAnqpProfileDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6)
)
if mibBuilder.loadTexts:
    configAnqpProfileDomainNameTable.setStatus("current")
_ConfigAnqpProfileDomainNameEntry_Object = MibTableRow
configAnqpProfileDomainNameEntry = _ConfigAnqpProfileDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6, 1)
)
configAnqpProfileDomainNameEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileDomainNameName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileDomainNameEntry.setStatus("current")
_ConfigProfileDomainNameName_Type = OctetString
_ConfigProfileDomainNameName_Object = MibTableColumn
configProfileDomainNameName = _ConfigProfileDomainNameName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6, 1, 1),
    _ConfigProfileDomainNameName_Type()
)
configProfileDomainNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileDomainNameName.setStatus("current")
_ConfigProfileDomainNameRowStatus_Type = RowStatus
_ConfigProfileDomainNameRowStatus_Object = MibTableColumn
configProfileDomainNameRowStatus = _ConfigProfileDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6, 1, 2),
    _ConfigProfileDomainNameRowStatus_Type()
)
configProfileDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileDomainNameRowStatus.setStatus("current")
_ConfigProfileDomainNameDesc_Type = OctetString
_ConfigProfileDomainNameDesc_Object = MibTableColumn
configProfileDomainNameDesc = _ConfigProfileDomainNameDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6, 1, 3),
    _ConfigProfileDomainNameDesc_Type()
)
configProfileDomainNameDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileDomainNameDesc.setStatus("current")
_ConfigDomainNameList_Type = OctetString
_ConfigDomainNameList_Object = MibTableColumn
configDomainNameList = _ConfigDomainNameList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 6, 1, 4),
    _ConfigDomainNameList_Type()
)
configDomainNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDomainNameList.setStatus("current")
_ConfigAnqpProfile3gppCellNetTable_Object = MibTable
configAnqpProfile3gppCellNetTable = _ConfigAnqpProfile3gppCellNetTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7)
)
if mibBuilder.loadTexts:
    configAnqpProfile3gppCellNetTable.setStatus("current")
_ConfigAnqpProfile3gppCellNetEntry_Object = MibTableRow
configAnqpProfile3gppCellNetEntry = _ConfigAnqpProfile3gppCellNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7, 1)
)
configAnqpProfile3gppCellNetEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfile3gppCellNetName"),
)
if mibBuilder.loadTexts:
    configAnqpProfile3gppCellNetEntry.setStatus("current")
_ConfigProfile3gppCellNetName_Type = OctetString
_ConfigProfile3gppCellNetName_Object = MibTableColumn
configProfile3gppCellNetName = _ConfigProfile3gppCellNetName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7, 1, 1),
    _ConfigProfile3gppCellNetName_Type()
)
configProfile3gppCellNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfile3gppCellNetName.setStatus("current")
_ConfigProfile3gppCellNetRowStatus_Type = RowStatus
_ConfigProfile3gppCellNetRowStatus_Object = MibTableColumn
configProfile3gppCellNetRowStatus = _ConfigProfile3gppCellNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7, 1, 2),
    _ConfigProfile3gppCellNetRowStatus_Type()
)
configProfile3gppCellNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfile3gppCellNetRowStatus.setStatus("current")
_ConfigProfile3gppCellNetDesc_Type = OctetString
_ConfigProfile3gppCellNetDesc_Object = MibTableColumn
configProfile3gppCellNetDesc = _ConfigProfile3gppCellNetDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7, 1, 3),
    _ConfigProfile3gppCellNetDesc_Type()
)
configProfile3gppCellNetDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfile3gppCellNetDesc.setStatus("current")
_Config3gppCellNetList_Type = OctetString
_Config3gppCellNetList_Object = MibTableColumn
config3gppCellNetList = _Config3gppCellNetList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 7, 1, 4),
    _Config3gppCellNetList_Type()
)
config3gppCellNetList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config3gppCellNetList.setStatus("current")
_ConfigAnqpProfileNaiRealmTable_Object = MibTable
configAnqpProfileNaiRealmTable = _ConfigAnqpProfileNaiRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8)
)
if mibBuilder.loadTexts:
    configAnqpProfileNaiRealmTable.setStatus("current")
_ConfigAnqpProfileNaiRealmEntry_Object = MibTableRow
configAnqpProfileNaiRealmEntry = _ConfigAnqpProfileNaiRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1)
)
configAnqpProfileNaiRealmEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileNaiRealmName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileNaiRealmEntry.setStatus("current")
_ConfigProfileNaiRealmName_Type = OctetString
_ConfigProfileNaiRealmName_Object = MibTableColumn
configProfileNaiRealmName = _ConfigProfileNaiRealmName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 1),
    _ConfigProfileNaiRealmName_Type()
)
configProfileNaiRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileNaiRealmName.setStatus("current")
_ConfigProfileNaiRealmRowStatus_Type = RowStatus
_ConfigProfileNaiRealmRowStatus_Object = MibTableColumn
configProfileNaiRealmRowStatus = _ConfigProfileNaiRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 2),
    _ConfigProfileNaiRealmRowStatus_Type()
)
configProfileNaiRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileNaiRealmRowStatus.setStatus("current")
_ConfigProfileNaiRealmDesc_Type = OctetString
_ConfigProfileNaiRealmDesc_Object = MibTableColumn
configProfileNaiRealmDesc = _ConfigProfileNaiRealmDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 3),
    _ConfigProfileNaiRealmDesc_Type()
)
configProfileNaiRealmDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileNaiRealmDesc.setStatus("current")
_ConfigNaiRealmEncode_Type = DisableEnable
_ConfigNaiRealmEncode_Object = MibTableColumn
configNaiRealmEncode = _ConfigNaiRealmEncode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 4),
    _ConfigNaiRealmEncode_Type()
)
configNaiRealmEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNaiRealmEncode.setStatus("current")
_ConfigNaiRealmRealmList_Type = OctetString
_ConfigNaiRealmRealmList_Object = MibTableColumn
configNaiRealmRealmList = _ConfigNaiRealmRealmList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 5),
    _ConfigNaiRealmRealmList_Type()
)
configNaiRealmRealmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNaiRealmRealmList.setStatus("current")
_ConfigNaiRealmEap_Type = OctetString
_ConfigNaiRealmEap_Object = MibTableColumn
configNaiRealmEap = _ConfigNaiRealmEap_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 8, 1, 6),
    _ConfigNaiRealmEap_Type()
)
configNaiRealmEap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNaiRealmEap.setStatus("current")
_ConfigAnqpProfileOverrideElementTable_Object = MibTable
configAnqpProfileOverrideElementTable = _ConfigAnqpProfileOverrideElementTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9)
)
if mibBuilder.loadTexts:
    configAnqpProfileOverrideElementTable.setStatus("current")
_ConfigAnqpProfileOverrideElementEntry_Object = MibTableRow
configAnqpProfileOverrideElementEntry = _ConfigAnqpProfileOverrideElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9, 1)
)
configAnqpProfileOverrideElementEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileOverrideElementName"),
)
if mibBuilder.loadTexts:
    configAnqpProfileOverrideElementEntry.setStatus("current")
_ConfigProfileOverrideElementName_Type = OctetString
_ConfigProfileOverrideElementName_Object = MibTableColumn
configProfileOverrideElementName = _ConfigProfileOverrideElementName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9, 1, 1),
    _ConfigProfileOverrideElementName_Type()
)
configProfileOverrideElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileOverrideElementName.setStatus("current")
_ConfigProfileOverrideElementRowStatus_Type = RowStatus
_ConfigProfileOverrideElementRowStatus_Object = MibTableColumn
configProfileOverrideElementRowStatus = _ConfigProfileOverrideElementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9, 1, 2),
    _ConfigProfileOverrideElementRowStatus_Type()
)
configProfileOverrideElementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileOverrideElementRowStatus.setStatus("current")
_ConfigProfileOverrideElementDesc_Type = OctetString
_ConfigProfileOverrideElementDesc_Object = MibTableColumn
configProfileOverrideElementDesc = _ConfigProfileOverrideElementDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9, 1, 3),
    _ConfigProfileOverrideElementDesc_Type()
)
configProfileOverrideElementDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileOverrideElementDesc.setStatus("current")
_ConfigAnqpOverrideList_Type = OctetString
_ConfigAnqpOverrideList_Object = MibTableColumn
configAnqpOverrideList = _ConfigAnqpOverrideList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 9, 1, 4),
    _ConfigAnqpOverrideList_Type()
)
configAnqpOverrideList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAnqpOverrideList.setStatus("current")
_ConfigHS20ProfileOperFriendlyNameTable_Object = MibTable
configHS20ProfileOperFriendlyNameTable = _ConfigHS20ProfileOperFriendlyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10)
)
if mibBuilder.loadTexts:
    configHS20ProfileOperFriendlyNameTable.setStatus("current")
_ConfigHS20ProfileOperFriendlyNameEntry_Object = MibTableRow
configHS20ProfileOperFriendlyNameEntry = _ConfigHS20ProfileOperFriendlyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10, 1)
)
configHS20ProfileOperFriendlyNameEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileOperFriendlyNameName"),
)
if mibBuilder.loadTexts:
    configHS20ProfileOperFriendlyNameEntry.setStatus("current")
_ConfigProfileOperFriendlyNameName_Type = OctetString
_ConfigProfileOperFriendlyNameName_Object = MibTableColumn
configProfileOperFriendlyNameName = _ConfigProfileOperFriendlyNameName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10, 1, 1),
    _ConfigProfileOperFriendlyNameName_Type()
)
configProfileOperFriendlyNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileOperFriendlyNameName.setStatus("current")
_ConfigProfileOperFriendlyNameRowStatus_Type = RowStatus
_ConfigProfileOperFriendlyNameRowStatus_Object = MibTableColumn
configProfileOperFriendlyNameRowStatus = _ConfigProfileOperFriendlyNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10, 1, 2),
    _ConfigProfileOperFriendlyNameRowStatus_Type()
)
configProfileOperFriendlyNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileOperFriendlyNameRowStatus.setStatus("current")
_ConfigProfileOperFriendlyNameDesc_Type = OctetString
_ConfigProfileOperFriendlyNameDesc_Object = MibTableColumn
configProfileOperFriendlyNameDesc = _ConfigProfileOperFriendlyNameDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10, 1, 3),
    _ConfigProfileOperFriendlyNameDesc_Type()
)
configProfileOperFriendlyNameDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileOperFriendlyNameDesc.setStatus("current")
_ConfigFriendlyNameList_Type = OctetString
_ConfigFriendlyNameList_Object = MibTableColumn
configFriendlyNameList = _ConfigFriendlyNameList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 10, 1, 4),
    _ConfigFriendlyNameList_Type()
)
configFriendlyNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFriendlyNameList.setStatus("current")
_ConfigHS20ProfileConnCapTable_Object = MibTable
configHS20ProfileConnCapTable = _ConfigHS20ProfileConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11)
)
if mibBuilder.loadTexts:
    configHS20ProfileConnCapTable.setStatus("current")
_ConfigHS20ProfileConnCapEntry_Object = MibTableRow
configHS20ProfileConnCapEntry = _ConfigHS20ProfileConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11, 1)
)
configHS20ProfileConnCapEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileConnCapName"),
)
if mibBuilder.loadTexts:
    configHS20ProfileConnCapEntry.setStatus("current")
_ConfigProfileConnCapName_Type = OctetString
_ConfigProfileConnCapName_Object = MibTableColumn
configProfileConnCapName = _ConfigProfileConnCapName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11, 1, 1),
    _ConfigProfileConnCapName_Type()
)
configProfileConnCapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileConnCapName.setStatus("current")
_ConfigProfileConnCapRowStatus_Type = RowStatus
_ConfigProfileConnCapRowStatus_Object = MibTableColumn
configProfileConnCapRowStatus = _ConfigProfileConnCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11, 1, 2),
    _ConfigProfileConnCapRowStatus_Type()
)
configProfileConnCapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileConnCapRowStatus.setStatus("current")
_ConfigProfileConnCapDesc_Type = OctetString
_ConfigProfileConnCapDesc_Object = MibTableColumn
configProfileConnCapDesc = _ConfigProfileConnCapDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11, 1, 3),
    _ConfigProfileConnCapDesc_Type()
)
configProfileConnCapDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileConnCapDesc.setStatus("current")
_ConfigConnCapabList_Type = OctetString
_ConfigConnCapabList_Object = MibTableColumn
configConnCapabList = _ConfigConnCapabList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 11, 1, 4),
    _ConfigConnCapabList_Type()
)
configConnCapabList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configConnCapabList.setStatus("current")
_ConfigHS20ProfileWanMetricsTable_Object = MibTable
configHS20ProfileWanMetricsTable = _ConfigHS20ProfileWanMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12)
)
if mibBuilder.loadTexts:
    configHS20ProfileWanMetricsTable.setStatus("current")
_ConfigHS20ProfileWanMetricsEntry_Object = MibTableRow
configHS20ProfileWanMetricsEntry = _ConfigHS20ProfileWanMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1)
)
configHS20ProfileWanMetricsEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileWanMetricsName"),
)
if mibBuilder.loadTexts:
    configHS20ProfileWanMetricsEntry.setStatus("current")
_ConfigProfileWanMetricsName_Type = OctetString
_ConfigProfileWanMetricsName_Object = MibTableColumn
configProfileWanMetricsName = _ConfigProfileWanMetricsName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 1),
    _ConfigProfileWanMetricsName_Type()
)
configProfileWanMetricsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileWanMetricsName.setStatus("current")
_ConfigProfileWanMetricsRowStatus_Type = RowStatus
_ConfigProfileWanMetricsRowStatus_Object = MibTableColumn
configProfileWanMetricsRowStatus = _ConfigProfileWanMetricsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 2),
    _ConfigProfileWanMetricsRowStatus_Type()
)
configProfileWanMetricsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileWanMetricsRowStatus.setStatus("current")
_ConfigProfileWanMetricsDesc_Type = OctetString
_ConfigProfileWanMetricsDesc_Object = MibTableColumn
configProfileWanMetricsDesc = _ConfigProfileWanMetricsDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 3),
    _ConfigProfileWanMetricsDesc_Type()
)
configProfileWanMetricsDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileWanMetricsDesc.setStatus("current")
_ConfigLinkStatus_Type = Integer32
_ConfigLinkStatus_Object = MibTableColumn
configLinkStatus = _ConfigLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 4),
    _ConfigLinkStatus_Type()
)
configLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLinkStatus.setStatus("current")
_ConfigSymmetric_Type = DisableEnable
_ConfigSymmetric_Object = MibTableColumn
configSymmetric = _ConfigSymmetric_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 5),
    _ConfigSymmetric_Type()
)
configSymmetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSymmetric.setStatus("current")
_ConfigAtCapacity_Type = DisableEnable
_ConfigAtCapacity_Object = MibTableColumn
configAtCapacity = _ConfigAtCapacity_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 6),
    _ConfigAtCapacity_Type()
)
configAtCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAtCapacity.setStatus("current")
_ConfigDownSpeed_Type = Integer32
_ConfigDownSpeed_Object = MibTableColumn
configDownSpeed = _ConfigDownSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 7),
    _ConfigDownSpeed_Type()
)
configDownSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDownSpeed.setStatus("current")
_ConfigUpSpeed_Type = Integer32
_ConfigUpSpeed_Object = MibTableColumn
configUpSpeed = _ConfigUpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 8),
    _ConfigUpSpeed_Type()
)
configUpSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configUpSpeed.setStatus("current")
_ConfigDownLoad_Type = Integer32
_ConfigDownLoad_Object = MibTableColumn
configDownLoad = _ConfigDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 9),
    _ConfigDownLoad_Type()
)
configDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDownLoad.setStatus("current")
_ConfigUpLoad_Type = Integer32
_ConfigUpLoad_Object = MibTableColumn
configUpLoad = _ConfigUpLoad_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 10),
    _ConfigUpLoad_Type()
)
configUpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configUpLoad.setStatus("current")
_ConfigLMD_Type = Integer32
_ConfigLMD_Object = MibTableColumn
configLMD = _ConfigLMD_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 12, 1, 11),
    _ConfigLMD_Type()
)
configLMD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLMD.setStatus("current")
_ConfigHS20ProfileOperClassTable_Object = MibTable
configHS20ProfileOperClassTable = _ConfigHS20ProfileOperClassTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13)
)
if mibBuilder.loadTexts:
    configHS20ProfileOperClassTable.setStatus("current")
_ConfigHS20ProfileOperClassEntry_Object = MibTableRow
configHS20ProfileOperClassEntry = _ConfigHS20ProfileOperClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13, 1)
)
configHS20ProfileOperClassEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileOperClassName"),
)
if mibBuilder.loadTexts:
    configHS20ProfileOperClassEntry.setStatus("current")
_ConfigProfileOperClassName_Type = OctetString
_ConfigProfileOperClassName_Object = MibTableColumn
configProfileOperClassName = _ConfigProfileOperClassName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13, 1, 1),
    _ConfigProfileOperClassName_Type()
)
configProfileOperClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileOperClassName.setStatus("current")
_ConfigProfileOperClassRowStatus_Type = RowStatus
_ConfigProfileOperClassRowStatus_Object = MibTableColumn
configProfileOperClassRowStatus = _ConfigProfileOperClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13, 1, 2),
    _ConfigProfileOperClassRowStatus_Type()
)
configProfileOperClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileOperClassRowStatus.setStatus("current")
_ConfigProfileOperClassDesc_Type = OctetString
_ConfigProfileOperClassDesc_Object = MibTableColumn
configProfileOperClassDesc = _ConfigProfileOperClassDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13, 1, 3),
    _ConfigProfileOperClassDesc_Type()
)
configProfileOperClassDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileOperClassDesc.setStatus("current")
_ConfigOperClassList_Type = OctetString
_ConfigOperClassList_Object = MibTableColumn
configOperClassList = _ConfigOperClassList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 13, 1, 4),
    _ConfigOperClassList_Type()
)
configOperClassList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOperClassList.setStatus("current")
_ConfigHS20ProfileOsuProviderTable_Object = MibTable
configHS20ProfileOsuProviderTable = _ConfigHS20ProfileOsuProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14)
)
if mibBuilder.loadTexts:
    configHS20ProfileOsuProviderTable.setStatus("current")
_ConfigHS20ProfileOsuProviderEntry_Object = MibTableRow
configHS20ProfileOsuProviderEntry = _ConfigHS20ProfileOsuProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1)
)
configHS20ProfileOsuProviderEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileOsuProviderName"),
)
if mibBuilder.loadTexts:
    configHS20ProfileOsuProviderEntry.setStatus("current")
_ConfigProfileOsuProviderName_Type = OctetString
_ConfigProfileOsuProviderName_Object = MibTableColumn
configProfileOsuProviderName = _ConfigProfileOsuProviderName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 1),
    _ConfigProfileOsuProviderName_Type()
)
configProfileOsuProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileOsuProviderName.setStatus("current")
_ConfigProfileOsuProviderRowStatus_Type = RowStatus
_ConfigProfileOsuProviderRowStatus_Object = MibTableColumn
configProfileOsuProviderRowStatus = _ConfigProfileOsuProviderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 2),
    _ConfigProfileOsuProviderRowStatus_Type()
)
configProfileOsuProviderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileOsuProviderRowStatus.setStatus("current")
_ConfigProfileOsuProviderDesc_Type = OctetString
_ConfigProfileOsuProviderDesc_Object = MibTableColumn
configProfileOsuProviderDesc = _ConfigProfileOsuProviderDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 3),
    _ConfigProfileOsuProviderDesc_Type()
)
configProfileOsuProviderDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileOsuProviderDesc.setStatus("current")
_ConfigOsuServerUri_Type = OctetString
_ConfigOsuServerUri_Object = MibTableColumn
configOsuServerUri = _ConfigOsuServerUri_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 4),
    _ConfigOsuServerUri_Type()
)
configOsuServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuServerUri.setStatus("current")
_ConfigOsuFriendlyNameList_Type = OctetString
_ConfigOsuFriendlyNameList_Object = MibTableColumn
configOsuFriendlyNameList = _ConfigOsuFriendlyNameList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 5),
    _ConfigOsuFriendlyNameList_Type()
)
configOsuFriendlyNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuFriendlyNameList.setStatus("current")
_ConfigOsuNai_Type = OctetString
_ConfigOsuNai_Object = MibTableColumn
configOsuNai = _ConfigOsuNai_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 6),
    _ConfigOsuNai_Type()
)
configOsuNai.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuNai.setStatus("current")
_ConfigOsuOmaDm_Type = DisableEnable
_ConfigOsuOmaDm_Object = MibTableColumn
configOsuOmaDm = _ConfigOsuOmaDm_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 7),
    _ConfigOsuOmaDm_Type()
)
configOsuOmaDm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuOmaDm.setStatus("current")
_ConfigOsuSoapXml_Type = DisableEnable
_ConfigOsuSoapXml_Object = MibTableColumn
configOsuSoapXml = _ConfigOsuSoapXml_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 8),
    _ConfigOsuSoapXml_Type()
)
configOsuSoapXml.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuSoapXml.setStatus("current")
_ConfigOsuIconProfileList_Type = OctetString
_ConfigOsuIconProfileList_Object = MibTableColumn
configOsuIconProfileList = _ConfigOsuIconProfileList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 9),
    _ConfigOsuIconProfileList_Type()
)
configOsuIconProfileList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuIconProfileList.setStatus("current")
_ConfigOsuServiceDescList_Type = OctetString
_ConfigOsuServiceDescList_Object = MibTableColumn
configOsuServiceDescList = _ConfigOsuServiceDescList_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 14, 1, 10),
    _ConfigOsuServiceDescList_Type()
)
configOsuServiceDescList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOsuServiceDescList.setStatus("current")
_ConfigProfileIconTable_Object = MibTable
configProfileIconTable = _ConfigProfileIconTable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15)
)
if mibBuilder.loadTexts:
    configProfileIconTable.setStatus("current")
_ConfigProfileIconEntry_Object = MibTableRow
configProfileIconEntry = _ConfigProfileIconEntry_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1)
)
configProfileIconEntry.setIndexNames(
    (0, "ACKSYS-MIB", "configProfileIconName"),
)
if mibBuilder.loadTexts:
    configProfileIconEntry.setStatus("current")
_ConfigProfileIconName_Type = OctetString
_ConfigProfileIconName_Object = MibTableColumn
configProfileIconName = _ConfigProfileIconName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 1),
    _ConfigProfileIconName_Type()
)
configProfileIconName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configProfileIconName.setStatus("current")
_ConfigProfileIconRowStatus_Type = RowStatus
_ConfigProfileIconRowStatus_Object = MibTableColumn
configProfileIconRowStatus = _ConfigProfileIconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 2),
    _ConfigProfileIconRowStatus_Type()
)
configProfileIconRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configProfileIconRowStatus.setStatus("current")
_ConfigProfileIconDesc_Type = OctetString
_ConfigProfileIconDesc_Object = MibTableColumn
configProfileIconDesc = _ConfigProfileIconDesc_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 3),
    _ConfigProfileIconDesc_Type()
)
configProfileIconDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProfileIconDesc.setStatus("current")
_ConfigIconLang_Type = OctetString
_ConfigIconLang_Object = MibTableColumn
configIconLang = _ConfigIconLang_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 4),
    _ConfigIconLang_Type()
)
configIconLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIconLang.setStatus("current")
_ConfigIconSize_Type = OctetString
_ConfigIconSize_Object = MibTableColumn
configIconSize = _ConfigIconSize_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 5),
    _ConfigIconSize_Type()
)
configIconSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIconSize.setStatus("current")
_ConfigIconType_Type = OctetString
_ConfigIconType_Object = MibTableColumn
configIconType = _ConfigIconType_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 6),
    _ConfigIconType_Type()
)
configIconType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIconType.setStatus("current")
_ConfigIconPath_Type = OctetString
_ConfigIconPath_Object = MibTableColumn
configIconPath = _ConfigIconPath_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 7),
    _ConfigIconPath_Type()
)
configIconPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIconPath.setStatus("current")
_ConfigIconFileContent_Type = OctetString
_ConfigIconFileContent_Object = MibTableColumn
configIconFileContent = _ConfigIconFileContent_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 10, 15, 1, 8),
    _ConfigIconFileContent_Type()
)
configIconFileContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIconFileContent.setStatus("current")
_Sc_async_sysupgrade_ObjectIdentity = ObjectIdentity
sc_async_sysupgrade = _Sc_async_sysupgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 11)
)


class _ConfigAsyncUpgradeDoUpgrade_Type(Integer32):
    """Custom type configAsyncUpgradeDoUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("execute", 2)
    )


_ConfigAsyncUpgradeDoUpgrade_Type.__name__ = "Integer32"
_ConfigAsyncUpgradeDoUpgrade_Object = MibScalar
configAsyncUpgradeDoUpgrade = _ConfigAsyncUpgradeDoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 11, 1),
    _ConfigAsyncUpgradeDoUpgrade_Type()
)
configAsyncUpgradeDoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAsyncUpgradeDoUpgrade.setStatus("current")
_ConfigAsyncUpgradeTimerEnable_Type = DisableEnable
_ConfigAsyncUpgradeTimerEnable_Object = MibScalar
configAsyncUpgradeTimerEnable = _ConfigAsyncUpgradeTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 11, 2),
    _ConfigAsyncUpgradeTimerEnable_Type()
)
configAsyncUpgradeTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAsyncUpgradeTimerEnable.setStatus("current")


class _ConfigAsyncUpgradeTimerMode_Type(Integer32):
    """Custom type configAsyncUpgradeTimerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no-retry", 1),
          ("retry-immediately", 2),
          ("retry-after-24h", 3),
          ("missed-upgrade-retry-after-24h", 100))
    )


_ConfigAsyncUpgradeTimerMode_Type.__name__ = "Integer32"
_ConfigAsyncUpgradeTimerMode_Object = MibScalar
configAsyncUpgradeTimerMode = _ConfigAsyncUpgradeTimerMode_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 11, 3),
    _ConfigAsyncUpgradeTimerMode_Type()
)
configAsyncUpgradeTimerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAsyncUpgradeTimerMode.setStatus("current")
_ConfigAsyncUpgradeTimerMinute_Type = Integer32
_ConfigAsyncUpgradeTimerMinute_Object = MibScalar
configAsyncUpgradeTimerMinute = _ConfigAsyncUpgradeTimerMinute_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 11, 4),
    _ConfigAsyncUpgradeTimerMinute_Type()
)
configAsyncUpgradeTimerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAsyncUpgradeTimerMinute.setStatus("current")
_Sc_md5sum_ObjectIdentity = ObjectIdentity
sc_md5sum = _Sc_md5sum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 10, 12)
)
_ConfigMD5SUMstatus_Type = Integer32
_ConfigMD5SUMstatus_Object = MibScalar
configMD5SUMstatus = _ConfigMD5SUMstatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 12, 1),
    _ConfigMD5SUMstatus_Type()
)
configMD5SUMstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMD5SUMstatus.setStatus("current")
_ConfigMD5SUMfiles_Type = DisplayString
_ConfigMD5SUMfiles_Object = MibScalar
configMD5SUMfiles = _ConfigMD5SUMfiles_Object(
    (1, 3, 6, 1, 4, 1, 28097, 10, 12, 2),
    _ConfigMD5SUMfiles_Type()
)
configMD5SUMfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMD5SUMfiles.setStatus("current")
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 11)
)
_NotificationBindings_ObjectIdentity = ObjectIdentity
notificationBindings = _NotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255)
)
_NbClientMacAddress_Type = PhysAddress
_NbClientMacAddress_Object = MibScalar
nbClientMacAddress = _NbClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 1),
    _NbClientMacAddress_Type()
)
nbClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbClientMacAddress.setStatus("current")


class _NbSsid_Type(OctetString):
    """Custom type nbSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_NbSsid_Type.__name__ = "OctetString"
_NbSsid_Object = MibScalar
nbSsid = _NbSsid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 2),
    _NbSsid_Type()
)
nbSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbSsid.setStatus("current")
_NbBssid_Type = PhysAddress
_NbBssid_Object = MibScalar
nbBssid = _NbBssid_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 3),
    _NbBssid_Type()
)
nbBssid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbBssid.setStatus("current")
_NbEventState_Type = DisplayString
_NbEventState_Object = MibScalar
nbEventState = _NbEventState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 4),
    _NbEventState_Type()
)
nbEventState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbEventState.setStatus("current")
_NbEventName_Type = DisplayString
_NbEventName_Object = MibScalar
nbEventName = _NbEventName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 5),
    _NbEventName_Type()
)
nbEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbEventName.setStatus("current")
_NbRadioName_Type = DisplayString
_NbRadioName_Object = MibScalar
nbRadioName = _NbRadioName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 6),
    _NbRadioName_Type()
)
nbRadioName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadioName.setStatus("current")
_NbRadioMacAddress_Type = PhysAddress
_NbRadioMacAddress_Object = MibScalar
nbRadioMacAddress = _NbRadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 7),
    _NbRadioMacAddress_Type()
)
nbRadioMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadioMacAddress.setStatus("current")
_NbRadioChannel_Type = Unsigned32
_NbRadioChannel_Object = MibScalar
nbRadioChannel = _NbRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 8),
    _NbRadioChannel_Type()
)
nbRadioChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadioChannel.setStatus("current")
_NbRadioChannelWidth_Type = Unsigned32
_NbRadioChannelWidth_Object = MibScalar
nbRadioChannelWidth = _NbRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 9),
    _NbRadioChannelWidth_Type()
)
nbRadioChannelWidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadioChannelWidth.setStatus("current")
_NbRadarChannel_Type = Unsigned32
_NbRadarChannel_Object = MibScalar
nbRadarChannel = _NbRadarChannel_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 10),
    _NbRadarChannel_Type()
)
nbRadarChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadarChannel.setStatus("current")
_NbRadarChannelWidth_Type = Unsigned32
_NbRadarChannelWidth_Object = MibScalar
nbRadarChannelWidth = _NbRadarChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 11),
    _NbRadarChannelWidth_Type()
)
nbRadarChannelWidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbRadarChannelWidth.setStatus("current")
_NbHostName_Type = DisplayString
_NbHostName_Object = MibScalar
nbHostName = _NbHostName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 12),
    _NbHostName_Type()
)
nbHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbHostName.setStatus("current")
_NbDigitalInName_Type = DisplayString
_NbDigitalInName_Object = MibScalar
nbDigitalInName = _NbDigitalInName_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 13),
    _NbDigitalInName_Type()
)
nbDigitalInName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbDigitalInName.setStatus("current")
_NbTcnTaiIp_Type = IpAddress
_NbTcnTaiIp_Object = MibScalar
nbTcnTaiIp = _NbTcnTaiIp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 14),
    _NbTcnTaiIp_Type()
)
nbTcnTaiIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnTaiIp.setStatus("current")


class _NbTcnEtbnStatus_Type(Integer32):
    """Custom type nbTcnEtbnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("initConfig", 3),
          ("notInaugurated", 4),
          ("readyForInauguration", 5),
          ("tndValidated", 6),
          ("inaugurating", 7),
          ("initServices", 8),
          ("inaugurated", 9),
          ("interConsistOperational", 10),
          ("tndPendingRemoval", 11))
    )


_NbTcnEtbnStatus_Type.__name__ = "Integer32"
_NbTcnEtbnStatus_Object = MibScalar
nbTcnEtbnStatus = _NbTcnEtbnStatus_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 15),
    _NbTcnEtbnStatus_Type()
)
nbTcnEtbnStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnEtbnStatus.setStatus("current")


class _NbTcnEtbnRole_Type(Integer32):
    """Custom type nbTcnEtbnRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("master", 1),
          ("backup", 2),
          ("notRedundant", 3))
    )


_NbTcnEtbnRole_Type.__name__ = "Integer32"
_NbTcnEtbnRole_Object = MibScalar
nbTcnEtbnRole = _NbTcnEtbnRole_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 16),
    _NbTcnEtbnRole_Type()
)
nbTcnEtbnRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnEtbnRole.setStatus("current")
_NbTcnEtbnTopoCnt_Type = Unsigned32
_NbTcnEtbnTopoCnt_Object = MibScalar
nbTcnEtbnTopoCnt = _NbTcnEtbnTopoCnt_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 17),
    _NbTcnEtbnTopoCnt_Type()
)
nbTcnEtbnTopoCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnEtbnTopoCnt.setStatus("current")


class _NbTcnEtbTopoCntState_Type(Integer32):
    """Custom type nbTcnEtbTopoCntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_NbTcnEtbTopoCntState_Type.__name__ = "Integer32"
_NbTcnEtbTopoCntState_Object = MibScalar
nbTcnEtbTopoCntState = _NbTcnEtbTopoCntState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 18),
    _NbTcnEtbTopoCntState_Type()
)
nbTcnEtbTopoCntState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnEtbTopoCntState.setStatus("current")
_NbTcnLengtheningFlag_Type = TruthValue
_NbTcnLengtheningFlag_Object = MibScalar
nbTcnLengtheningFlag = _NbTcnLengtheningFlag_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 19),
    _NbTcnLengtheningFlag_Type()
)
nbTcnLengtheningFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnLengtheningFlag.setStatus("current")


class _NbTcnShorteningState_Type(OctetString):
    """Custom type nbTcnShorteningState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_NbTcnShorteningState_Type.__name__ = "OctetString"
_NbTcnShorteningState_Object = MibScalar
nbTcnShorteningState = _NbTcnShorteningState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 20),
    _NbTcnShorteningState_Type()
)
nbTcnShorteningState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnShorteningState.setStatus("current")


class _NbTcnRadio1CouplingState_Type(Integer32):
    """Custom type nbTcnRadio1CouplingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("scanning", 1),
          ("signalgood", 2),
          ("signalbad", 3))
    )


_NbTcnRadio1CouplingState_Type.__name__ = "Integer32"
_NbTcnRadio1CouplingState_Object = MibScalar
nbTcnRadio1CouplingState = _NbTcnRadio1CouplingState_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 21),
    _NbTcnRadio1CouplingState_Type()
)
nbTcnRadio1CouplingState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnRadio1CouplingState.setStatus("current")


class _NbTcnConsistCount_Type(Integer32):
    """Custom type nbTcnConsistCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NbTcnConsistCount_Type.__name__ = "Integer32"
_NbTcnConsistCount_Object = MibScalar
nbTcnConsistCount = _NbTcnConsistCount_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 22),
    _NbTcnConsistCount_Type()
)
nbTcnConsistCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnConsistCount.setStatus("current")


class _NbTcnConsistPosition_Type(Integer32):
    """Custom type nbTcnConsistPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NbTcnConsistPosition_Type.__name__ = "Integer32"
_NbTcnConsistPosition_Object = MibScalar
nbTcnConsistPosition = _NbTcnConsistPosition_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 23),
    _NbTcnConsistPosition_Type()
)
nbTcnConsistPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTcnConsistPosition.setStatus("current")
_NbDescription_Type = DisplayString
_NbDescription_Object = MibScalar
nbDescription = _NbDescription_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 24),
    _NbDescription_Type()
)
nbDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbDescription.setStatus("current")
_NbTimestamp_Type = Unsigned32
_NbTimestamp_Object = MibScalar
nbTimestamp = _NbTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 25),
    _NbTimestamp_Type()
)
nbTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbTimestamp.setStatus("current")
_NbMacAddr_Type = PhysAddress
_NbMacAddr_Object = MibScalar
nbMacAddr = _NbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 26),
    _NbMacAddr_Type()
)
nbMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbMacAddr.setStatus("current")
_NbSource_Type = DisplayString
_NbSource_Object = MibScalar
nbSource = _NbSource_Object(
    (1, 3, 6, 1, 4, 1, 28097, 11, 255, 27),
    _NbSource_Type()
)
nbSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbSource.setStatus("current")
_AcksysProductSerialNumber_Type = DisplayString
_AcksysProductSerialNumber_Object = MibScalar
acksysProductSerialNumber = _AcksysProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28097, 12),
    _AcksysProductSerialNumber_Type()
)
acksysProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acksysProductSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects

linkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 1)
)
linkAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    linkAlarm.setStatus(
        "current"
    )

powerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 3)
)
powerAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    powerAlarm.setStatus(
        "current"
    )

digitalInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 4)
)
digitalInputAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    digitalInputAlarm.setStatus(
        "current"
    )

tempExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 5)
)
tempExceededAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    tempExceededAlarm.setStatus(
        "current"
    )

clientLinkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 6)
)
clientLinkAlarm.setObjects(
      *(("ACKSYS-MIB", "nbClientMacAddress"),
        ("ACKSYS-MIB", "nbSsid"),
        ("ACKSYS-MIB", "nbBssid"),
        ("ACKSYS-MIB", "nbEventState"),
        ("ACKSYS-MIB", "nbEventName"))
)
if mibBuilder.loadTexts:
    clientLinkAlarm.setStatus(
        "current"
    )

vrrpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 7)
)
vrrpAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    vrrpAlarm.setStatus(
        "current"
    )

dfsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 8)
)
dfsAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    dfsAlarm.setStatus(
        "current"
    )

pingerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 9)
)
pingerAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    pingerAlarm.setStatus(
        "current"
    )

tcnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 11)
)
tcnAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    tcnAlarm.setStatus(
        "current"
    )

securityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28097, 11, 12)
)
securityAlarm.setObjects(
    ("ACKSYS-MIB", "nbEventName")
)
if mibBuilder.loadTexts:
    securityAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACKSYS-MIB",
    **{"PhysAddress": PhysAddress,
       "WifiFlavor": WifiFlavor,
       "NetifName": NetifName,
       "SecurityModes": SecurityModes,
       "CellSecurityProtocol": CellSecurityProtocol,
       "PeapSecurityProtocol": PeapSecurityProtocol,
       "WpaVersions": WpaVersions,
       "CipherTypes": CipherTypes,
       "WepKeys": WepKeys,
       "WifiLevel": WifiLevel,
       "DisableEnable": DisableEnable,
       "TriState": TriState,
       "AsyncSetStatus": AsyncSetStatus,
       "BridgeId": BridgeId,
       "PortId": PortId,
       "CellAttachMode": CellAttachMode,
       "CellAccessTech": CellAccessTech,
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
       "settingTxPower": settingTxPower,
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
       "adminApply": adminApply,
       "adminConfigHash": adminConfigHash,
       "fileTransfer": fileTransfer,
       "fileTransferAction": fileTransferAction,
       "fileTransferType": fileTransferType,
       "fileTransferSize": fileTransferSize,
       "fileTransferIndex": fileTransferIndex,
       "fileTransferHash": fileTransferHash,
       "fileTransferChunk": fileTransferChunk,
       "fileTransferResult": fileTransferResult,
       "fileTransferSession": fileTransferSession,
       "adminIdentify": adminIdentify,
       "adminEvents": adminEvents,
       "adminEventDisable": adminEventDisable,
       "adminEventEnable": adminEventEnable,
       "adminEventTrigger": adminEventTrigger,
       "adminTimeZone": adminTimeZone,
       "adminTimeZoneDBVersion": adminTimeZoneDBVersion,
       "adminTimeZoneName": adminTimeZoneName,
       "adminSystemDateAndTime": adminSystemDateAndTime,
       "adminSystemDateAndTimeLocal": adminSystemDateAndTimeLocal,
       "adminSystemDateAndTimeUTC": adminSystemDateAndTimeUTC,
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
       "serialInterface": serialInterface,
       "serialServicetype": serialServicetype,
       "serialFormat": serialFormat,
       "serialFormatBaudRate": serialFormatBaudRate,
       "serialFormatDataBit": serialFormatDataBit,
       "serialFormatParityBit": serialFormatParityBit,
       "serialFormatStopBit": serialFormatStopBit,
       "serialElectricalInterface": serialElectricalInterface,
       "serialSendTriggers": serialSendTriggers,
       "serialSendTriggerCharcount": serialSendTriggerCharcount,
       "sendTriggerCharCountEnable": sendTriggerCharCountEnable,
       "sendTriggerCharCountValue": sendTriggerCharCountValue,
       "serialSendTriggerIdleDelay": serialSendTriggerIdleDelay,
       "sendTriggerIdleDelayEnable": sendTriggerIdleDelayEnable,
       "sendTriggerIdleDelayValue": sendTriggerIdleDelayValue,
       "sendTriggerIdleDelayUnit": sendTriggerIdleDelayUnit,
       "serialSendTriggerFrameDelay": serialSendTriggerFrameDelay,
       "sendTriggerFrameDelayEnable": sendTriggerFrameDelayEnable,
       "sendTriggerFrameDelayValue": sendTriggerFrameDelayValue,
       "sendTriggerFrameDelayUnit": sendTriggerFrameDelayUnit,
       "serialServiceVirtualCom": serialServiceVirtualCom,
       "serialServiceModbusSlave": serialServiceModbusSlave,
       "modbusSlaveFormat": modbusSlaveFormat,
       "modbusSlaveSerialTransactionTimeout": modbusSlaveSerialTransactionTimeout,
       "serialServiceModbusMaster": serialServiceModbusMaster,
       "modbusMasterFormat": modbusMasterFormat,
       "modbusMasterTransactionTimeout": modbusMasterTransactionTimeout,
       "modbusMasterForwardingTable": modbusMasterForwardingTable,
       "modbusMasterForwardingTable-Rule1": modbusMasterForwardingTable_Rule1,
       "mmForwardingTable-Rule1-FirstLocalAddr": mmForwardingTable_Rule1_FirstLocalAddr,
       "mmForwardingTable-Rule1-LastLocalAddr": mmForwardingTable_Rule1_LastLocalAddr,
       "mmForwardingTable-Rule1-FirstRemoteAddr": mmForwardingTable_Rule1_FirstRemoteAddr,
       "mmForwardingTable-Rule1-SlaveIpAddrIncrement": mmForwardingTable_Rule1_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule1-SlaveIpAddr": mmForwardingTable_Rule1_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule2": modbusMasterForwardingTable_Rule2,
       "mmForwardingTable-Rule2-FirstLocalAddr": mmForwardingTable_Rule2_FirstLocalAddr,
       "mmForwardingTable-Rule2-LastLocalAddr": mmForwardingTable_Rule2_LastLocalAddr,
       "mmForwardingTable-Rule2-FirstRemoteAddr": mmForwardingTable_Rule2_FirstRemoteAddr,
       "mmForwardingTable-Rule2-SlaveIpAddrIncrement": mmForwardingTable_Rule2_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule2-SlaveIpAddr": mmForwardingTable_Rule2_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule3": modbusMasterForwardingTable_Rule3,
       "mmForwardingTable-Rule3-FirstLocalAddr": mmForwardingTable_Rule3_FirstLocalAddr,
       "mmForwardingTable-Rule3-LastLocalAddr": mmForwardingTable_Rule3_LastLocalAddr,
       "mmForwardingTable-Rule3-FirstRemoteAddr": mmForwardingTable_Rule3_FirstRemoteAddr,
       "mmForwardingTable-Rule3-SlaveIpAddrIncrement": mmForwardingTable_Rule3_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule3-SlaveIpAddr": mmForwardingTable_Rule3_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule4": modbusMasterForwardingTable_Rule4,
       "mmForwardingTable-Rule4-FirstLocalAddr": mmForwardingTable_Rule4_FirstLocalAddr,
       "mmForwardingTable-Rule4-LastLocalAddr": mmForwardingTable_Rule4_LastLocalAddr,
       "mmForwardingTable-Rule4-FirstRemoteAddr": mmForwardingTable_Rule4_FirstRemoteAddr,
       "mmForwardingTable-Rule4-SlaveIpAddrIncrement": mmForwardingTable_Rule4_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule4-SlaveIpAddr": mmForwardingTable_Rule4_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule5": modbusMasterForwardingTable_Rule5,
       "mmForwardingTable-Rule5-FirstLocalAddr": mmForwardingTable_Rule5_FirstLocalAddr,
       "mmForwardingTable-Rule5-LastLocalAddr": mmForwardingTable_Rule5_LastLocalAddr,
       "mmForwardingTable-Rule5-FirstRemoteAddr": mmForwardingTable_Rule5_FirstRemoteAddr,
       "mmForwardingTable-Rule5-SlaveIpAddrIncrement": mmForwardingTable_Rule5_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule5-SlaveIpAddr": mmForwardingTable_Rule5_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule6": modbusMasterForwardingTable_Rule6,
       "mmForwardingTable-Rule6-FirstLocalAddr": mmForwardingTable_Rule6_FirstLocalAddr,
       "mmForwardingTable-Rule6-LastLocalAddr": mmForwardingTable_Rule6_LastLocalAddr,
       "mmForwardingTable-Rule6-FirstRemoteAddr": mmForwardingTable_Rule6_FirstRemoteAddr,
       "mmForwardingTable-Rule6-SlaveIpAddrIncrement": mmForwardingTable_Rule6_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule6-SlaveIpAddr": mmForwardingTable_Rule6_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule7": modbusMasterForwardingTable_Rule7,
       "mmForwardingTable-Rule7-FirstLocalAddr": mmForwardingTable_Rule7_FirstLocalAddr,
       "mmForwardingTable-Rule7-LastLocalAddr": mmForwardingTable_Rule7_LastLocalAddr,
       "mmForwardingTable-Rule7-FirstRemoteAddr": mmForwardingTable_Rule7_FirstRemoteAddr,
       "mmForwardingTable-Rule7-SlaveIpAddrIncrement": mmForwardingTable_Rule7_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule7-SlaveIpAddr": mmForwardingTable_Rule7_SlaveIpAddr,
       "modbusMasterForwardingTable-Rule8": modbusMasterForwardingTable_Rule8,
       "mmForwardingTable-Rule8-FirstLocalAddr": mmForwardingTable_Rule8_FirstLocalAddr,
       "mmForwardingTable-Rule8-LastLocalAddr": mmForwardingTable_Rule8_LastLocalAddr,
       "mmForwardingTable-Rule8-FirstRemoteAddr": mmForwardingTable_Rule8_FirstRemoteAddr,
       "mmForwardingTable-Rule8-SlaveIpAddrIncrement": mmForwardingTable_Rule8_SlaveIpAddrIncrement,
       "mmForwardingTable-Rule8-SlaveIpAddr": mmForwardingTable_Rule8_SlaveIpAddr,
       "serialServiceTcpRawPortServer": serialServiceTcpRawPortServer,
       "tcpRawServerSerialExtraConfig": tcpRawServerSerialExtraConfig,
       "trsExtraConfigDTR": trsExtraConfigDTR,
       "trsExtraConfigRTS": trsExtraConfigRTS,
       "trsExtraConfigDSR": trsExtraConfigDSR,
       "trsExtraConfigCTS": trsExtraConfigCTS,
       "trsExtraConfigDCD": trsExtraConfigDCD,
       "trsExtraConfigXonXoff": trsExtraConfigXonXoff,
       "serialServiceTcpRawPortClient": serialServiceTcpRawPortClient,
       "tcpRawClientSerialExtraConfig": tcpRawClientSerialExtraConfig,
       "trcExtraConfigDTR": trcExtraConfigDTR,
       "trcExtraConfigRTS": trcExtraConfigRTS,
       "trcExtraConfigCTS": trcExtraConfigCTS,
       "trcExtraConfigDCD": trcExtraConfigDCD,
       "trcExtraConfigXonXoff": trcExtraConfigXonXoff,
       "tcpRawClientConnectionTimeout": tcpRawClientConnectionTimeout,
       "tcpRawClientPollPeriode": tcpRawClientPollPeriode,
       "tcpRawClientDSRUse": tcpRawClientDSRUse,
       "tcpRawClientRemoteServers": tcpRawClientRemoteServers,
       "tcpRawClientServer1": tcpRawClientServer1,
       "tcpRawClienServer1-IpAddress": tcpRawClienServer1_IpAddress,
       "tcpRawclientServer1-TcpPort": tcpRawclientServer1_TcpPort,
       "tcpRawClientServer2": tcpRawClientServer2,
       "tcpRawclientServer2-IpAddress": tcpRawclientServer2_IpAddress,
       "tcpRawclientServer2-TcpPort": tcpRawclientServer2_TcpPort,
       "tcpRawClientServer3": tcpRawClientServer3,
       "tcpRawclientServer3-IpAddress": tcpRawclientServer3_IpAddress,
       "tcpRawclientServer3-TcpPort": tcpRawclientServer3_TcpPort,
       "tcpRawClientServer4": tcpRawClientServer4,
       "tcpRawclientServer4-IpAddress": tcpRawclientServer4_IpAddress,
       "tcpRawclientServer4-TcpPort": tcpRawclientServer4_TcpPort,
       "tcpRawClientServer5": tcpRawClientServer5,
       "tcpRawclientServer5-IpAddress": tcpRawclientServer5_IpAddress,
       "tcpRawclientServer5-TcpPort": tcpRawclientServer5_TcpPort,
       "tcpRawClientServer6": tcpRawClientServer6,
       "tcpRawclientServer6-IpAddress": tcpRawclientServer6_IpAddress,
       "tcpRawclientServer6-TcpPort": tcpRawclientServer6_TcpPort,
       "tcpRawClientServer7": tcpRawClientServer7,
       "tcpRawclientServer7-IpAddress": tcpRawclientServer7_IpAddress,
       "tcpRawclientServer7-TcpPort": tcpRawclientServer7_TcpPort,
       "tcpRawClientServer8": tcpRawClientServer8,
       "tcpRawclientServer8-IpAddress": tcpRawclientServer8_IpAddress,
       "tcpRawclientServer8-TcpPort": tcpRawclientServer8_TcpPort,
       "serialServiceUdpRawPortServer": serialServiceUdpRawPortServer,
       "udpRawServerSerialExtraConfig": udpRawServerSerialExtraConfig,
       "ursExtraConfigDTR": ursExtraConfigDTR,
       "ursExtraConfigRTS": ursExtraConfigRTS,
       "ursExtraConfigCTS": ursExtraConfigCTS,
       "ursExtraConfigXonXoff": ursExtraConfigXonXoff,
       "udpRawServerRemoteIP": udpRawServerRemoteIP,
       "udpRawServerRemotePort": udpRawServerRemotePort,
       "udpRawServerLocalPort": udpRawServerLocalPort,
       "acksysInternals": acksysInternals,
       "internalUniqueID": internalUniqueID,
       "internalSerial": internalSerial,
       "internalWlanChange": internalWlanChange,
       "internalRadioChange": internalRadioChange,
       "internalSerialTest": internalSerialTest,
       "internalSerialTestResult": internalSerialTestResult,
       "internalAlarmSwitch": internalAlarmSwitch,
       "internalDigitalInput": internalDigitalInput,
       "acksysProductID": acksysProductID,
       "c-key-management": c_key_management,
       "ckeyManagementCopySettingTo": ckeyManagementCopySettingTo,
       "ckeyManagementCopySettingFrom": ckeyManagementCopySettingFrom,
       "ckeyManagementErase": ckeyManagementErase,
       "ckeyManagementStatus": ckeyManagementStatus,
       "ckeyManagementIgnoreSetting": ckeyManagementIgnoreSetting,
       "ckeyManagementDisableLed": ckeyManagementDisableLed,
       "ckeyManagementTest": ckeyManagementTest,
       "ckeyManagementTestResult": ckeyManagementTestResult,
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
       "powerStatus-PW2-state": powerStatus_PW2_state,
       "networkStatus": networkStatus,
       "statusIpSubnetTable": statusIpSubnetTable,
       "statusIpSubnetEntry": statusIpSubnetEntry,
       "statusIpSubnetIndex": statusIpSubnetIndex,
       "statusIpSubnetName": statusIpSubnetName,
       "statusIpSubnetLabel": statusIpSubnetLabel,
       "statusIpSubnetIfIndex": statusIpSubnetIfIndex,
       "statusIpSubnetAddrMode": statusIpSubnetAddrMode,
       "statusIpSubnetIPv4Addr": statusIpSubnetIPv4Addr,
       "statusIpSubnetIPv4Mask": statusIpSubnetIPv4Mask,
       "statusIpSubnetDNS": statusIpSubnetDNS,
       "statusIpSubnetMember": statusIpSubnetMember,
       "statusIpSubnetMemberIndex": statusIpSubnetMemberIndex,
       "statusIfWlanTable": statusIfWlanTable,
       "statusIfWlanEntry": statusIfWlanEntry,
       "statusIfWlanIndex": statusIfWlanIndex,
       "statusIfWlanSSID": statusIfWlanSSID,
       "statusIfWlanMode": statusIfWlanMode,
       "statusIfWlanBand": statusIfWlanBand,
       "statusIfWlanChannel": statusIfWlanChannel,
       "statusIfWlanFrequency": statusIfWlanFrequency,
       "statusIfWlanEnable": statusIfWlanEnable,
       "statusIfWlanPhy": statusIfWlanPhy,
       "statusIfWlanSecurityMode": statusIfWlanSecurityMode,
       "statusIfWlanWpaVersion": statusIfWlanWpaVersion,
       "statusIfWlanNPeers": statusIfWlanNPeers,
       "statusIfWlanQuality": statusIfWlanQuality,
       "statusIfWlanBssid": statusIfWlanBssid,
       "statusIfWlanState": statusIfWlanState,
       "statusIfStaFastBSSTransitionActivated": statusIfStaFastBSSTransitionActivated,
       "statusIfWlanBeaconSignalAvg": statusIfWlanBeaconSignalAvg,
       "statusIfWlanNoise": statusIfWlanNoise,
       "statusIfWlanWpaCipher": statusIfWlanWpaCipher,
       "statusIfWlanWpaPreSharedKey": statusIfWlanWpaPreSharedKey,
       "statusIfWlanName": statusIfWlanName,
       "statusIfWlanIfIndex": statusIfWlanIfIndex,
       "statusPhyWifiTable": statusPhyWifiTable,
       "statusPhyWifiEntry": statusPhyWifiEntry,
       "statusPhyWifiIndex": statusPhyWifiIndex,
       "statusPhyWifiLabel": statusPhyWifiLabel,
       "statusPhyWifiEnable": statusPhyWifiEnable,
       "statusPhyWifiName": statusPhyWifiName,
       "statusPhyWifiClusterMode": statusPhyWifiClusterMode,
       "statusPhyWifiClusterList": statusPhyWifiClusterList,
       "statusPhyWifiClusterArgs": statusPhyWifiClusterArgs,
       "statusPhyWifiMAC": statusPhyWifiMAC,
       "statusPhyWifiWids": statusPhyWifiWids,
       "statusPhyWifiScanTable": statusPhyWifiScanTable,
       "statusPhyWifiScanEntry": statusPhyWifiScanEntry,
       "statusPhyWifiScanTableIndex": statusPhyWifiScanTableIndex,
       "statusPhyWifiScanSSID": statusPhyWifiScanSSID,
       "statusPhyWifiScanSignal": statusPhyWifiScanSignal,
       "statusPhyWifiScanFreq": statusPhyWifiScanFreq,
       "statusPhyWifiScanMode": statusPhyWifiScanMode,
       "statusPhyWifiScanSecurity": statusPhyWifiScanSecurity,
       "statusPhyWifiScanBssid": statusPhyWifiScanBssid,
       "statusPhyWifiScanPhyNum": statusPhyWifiScanPhyNum,
       "statusPhyWifiScanChWidth": statusPhyWifiScanChWidth,
       "statusPhyWifiScanTableStart": statusPhyWifiScanTableStart,
       "statusPhyWifiScanUpdateTbl": statusPhyWifiScanUpdateTbl,
       "statusSpanningTreeTable": statusSpanningTreeTable,
       "statusSpanningTreeEntry": statusSpanningTreeEntry,
       "statusSpanningTreeBridgeName": statusSpanningTreeBridgeName,
       "statusSpanningTreeNetworkLabel": statusSpanningTreeNetworkLabel,
       "statusSpanningTreeBridgeId": statusSpanningTreeBridgeId,
       "statusSpanningTreeDesignatedRoot": statusSpanningTreeDesignatedRoot,
       "statusSpanningTreeRootPort": statusSpanningTreeRootPort,
       "statusSpanningTreePortTable": statusSpanningTreePortTable,
       "statusSpanningTreePortEntry": statusSpanningTreePortEntry,
       "statusSpanningTreePortBridgeName": statusSpanningTreePortBridgeName,
       "statusSpanningTreePortNetworkLabel": statusSpanningTreePortNetworkLabel,
       "statusSpanningTreePortName": statusSpanningTreePortName,
       "statusSpanningTreePortLabel": statusSpanningTreePortLabel,
       "statusSpanningTreePortId": statusSpanningTreePortId,
       "statusSpanningTreePortRole": statusSpanningTreePortRole,
       "statusSpanningTreePortState": statusSpanningTreePortState,
       "statusSpanningTreePortPathCost": statusSpanningTreePortPathCost,
       "statusSpanningTreePortDesignatedRoot": statusSpanningTreePortDesignatedRoot,
       "statusSpanningTreePortDesignatedCost": statusSpanningTreePortDesignatedCost,
       "statusSpanningTreePortDesignatedBridge": statusSpanningTreePortDesignatedBridge,
       "statusSpanningTreePortDesignatedPort": statusSpanningTreePortDesignatedPort,
       "statusSpanningTreePortOperEdgePort": statusSpanningTreePortOperEdgePort,
       "statusSpanningTreePortOperPointToPoint": statusSpanningTreePortOperPointToPoint,
       "statusAssociationTable": statusAssociationTable,
       "statusAssociationEntry": statusAssociationEntry,
       "statusAssociationIndex": statusAssociationIndex,
       "statusAssociationMacAddr": statusAssociationMacAddr,
       "statusAssociationSSID": statusAssociationSSID,
       "statusAssociationBSSID": statusAssociationBSSID,
       "statusAssociationPhy": statusAssociationPhy,
       "statusAssociationSignaldBm": statusAssociationSignaldBm,
       "statusAssociationNoisedBm": statusAssociationNoisedBm,
       "statusAssociationSNR": statusAssociationSNR,
       "statusAssociationWlanIndex": statusAssociationWlanIndex,
       "statusAssociationSecurityMode": statusAssociationSecurityMode,
       "statusPhyLanTable": statusPhyLanTable,
       "statusPhyLanEntry": statusPhyLanEntry,
       "statusPhyLanIndex": statusPhyLanIndex,
       "statusPhyLanName": statusPhyLanName,
       "statusPhyLanLabel": statusPhyLanLabel,
       "statusPhyLanIfIndex": statusPhyLanIfIndex,
       "statusMeshSurveyTable": statusMeshSurveyTable,
       "statusMeshSurveyEntry": statusMeshSurveyEntry,
       "statusMeshSurveyIndex": statusMeshSurveyIndex,
       "statusMeshSurveyDstMacAddr": statusMeshSurveyDstMacAddr,
       "statusMeshSurveyNextHopMacAddr": statusMeshSurveyNextHopMacAddr,
       "statusMeshSurveyPhy": statusMeshSurveyPhy,
       "statusMeshSurveyMetric": statusMeshSurveyMetric,
       "statusMeshSurveyDiscoveryTimeout": statusMeshSurveyDiscoveryTimeout,
       "statusMeshSurveyDiscoveryRetries": statusMeshSurveyDiscoveryRetries,
       "statusMeshSurveyStateActive": statusMeshSurveyStateActive,
       "statusMeshSurveyStateResolving": statusMeshSurveyStateResolving,
       "statusMeshSurveyStateDSNValid": statusMeshSurveyStateDSNValid,
       "statusMeshSurveyStateFixed": statusMeshSurveyStateFixed,
       "statusMeshSurveyStateResolved": statusMeshSurveyStateResolved,
       "statusMeshSurveyMeshId": statusMeshSurveyMeshId,
       "statusMeshSurveyWlanIndex": statusMeshSurveyWlanIndex,
       "statusPhyCellTable": statusPhyCellTable,
       "statusPhyCellEntry": statusPhyCellEntry,
       "statusPhyCellIndex": statusPhyCellIndex,
       "statusPhyCellLabel": statusPhyCellLabel,
       "statusPhyCellFriendlyName": statusPhyCellFriendlyName,
       "statusPhyCellEnable": statusPhyCellEnable,
       "statusPhyCellIMEI": statusPhyCellIMEI,
       "statusPhyCellModel": statusPhyCellModel,
       "statusPhyCellName": statusPhyCellName,
       "statusPhyCellSimSelected": statusPhyCellSimSelected,
       "statusPhyCellSimState": statusPhyCellSimState,
       "statusPhyCellSimIMSI": statusPhyCellSimIMSI,
       "statusPhyCellAttachMode": statusPhyCellAttachMode,
       "statusPhyCellOperator": statusPhyCellOperator,
       "statusPhyCellMcc": statusPhyCellMcc,
       "statusPhyCellMnc": statusPhyCellMnc,
       "statusPhyCellBaseLAC": statusPhyCellBaseLAC,
       "statusPhyCellBaseCID": statusPhyCellBaseCID,
       "statusPhyCellRegistrationClass": statusPhyCellRegistrationClass,
       "statusPhyCellAccessTech": statusPhyCellAccessTech,
       "statusPhyCellBandName": statusPhyCellBandName,
       "statusPhyCellARFCN": statusPhyCellARFCN,
       "statusPhyCellRSSI": statusPhyCellRSSI,
       "statusPhyCellBER": statusPhyCellBER,
       "statusRoaming": statusRoaming,
       "statusRoamingLeaveLvlMax": statusRoamingLeaveLvlMax,
       "statusRoamingLeaveLvlMin": statusRoamingLeaveLvlMin,
       "statusRoamingRoamLvlMax": statusRoamingRoamLvlMax,
       "statusRoamingRoamLvlMin": statusRoamingRoamLvlMin,
       "statusRoamingThresHyst": statusRoamingThresHyst,
       "statusRoamingLeaveBoost": statusRoamingLeaveBoost,
       "statusRoamingActiveIf": statusRoamingActiveIf,
       "statusRoamingActiveIfName": statusRoamingActiveIfName,
       "statusRoamingActiveIfBssid": statusRoamingActiveIfBssid,
       "statusRoamingActiveIfBeaconSignalAvg": statusRoamingActiveIfBeaconSignalAvg,
       "statusRoamingActiveIfNoise": statusRoamingActiveIfNoise,
       "statusRoamingActiveIfSwitching": statusRoamingActiveIfSwitching,
       "statusRoamingActiveIfChannel": statusRoamingActiveIfChannel,
       "statusRoamingActiveIfState": statusRoamingActiveIfState,
       "statusRoamingPassiveIf": statusRoamingPassiveIf,
       "statusRoamingPassiveIfName": statusRoamingPassiveIfName,
       "statusRoamingPassiveIfBssid": statusRoamingPassiveIfBssid,
       "statusRoamingPassiveIfBeaconSignalAvg": statusRoamingPassiveIfBeaconSignalAvg,
       "statusRoamingPassiveIfNoise": statusRoamingPassiveIfNoise,
       "statusRoamingPassiveIfSwitching": statusRoamingPassiveIfSwitching,
       "statusRoamingPassiveIfChannel": statusRoamingPassiveIfChannel,
       "statusRoamingPassiveIfState": statusRoamingPassiveIfState,
       "statusRoamingUrgent": statusRoamingUrgent,
       "networkConfiguration": networkConfiguration,
       "tcpip": tcpip,
       "configIpSubnetTable": configIpSubnetTable,
       "configIpSubnetEntry": configIpSubnetEntry,
       "configIpSubnetName": configIpSubnetName,
       "configIpSubnetRowStatus": configIpSubnetRowStatus,
       "configIpAddressMode": configIpAddressMode,
       "configIpSubnetIPv4Addr": configIpSubnetIPv4Addr,
       "configIpSubnetIPv4Mask": configIpSubnetIPv4Mask,
       "configIpSubnetMetric": configIpSubnetMetric,
       "configIpSubnetDnsList": configIpSubnetDnsList,
       "configIpSubnetInterface": configIpSubnetInterface,
       "configIpSubnetIPv4Gateway": configIpSubnetIPv4Gateway,
       "configIpSubnetFriendlyName": configIpSubnetFriendlyName,
       "configIpSubnetBridgeEnable": configIpSubnetBridgeEnable,
       "configIpSubnetPersistence": configIpSubnetPersistence,
       "configIpSubnetEnable": configIpSubnetEnable,
       "configIpSubnetAutoStart": configIpSubnetAutoStart,
       "configIpSubnetPeerDns": configIpSubnetPeerDns,
       "configIpSubnetDefaultRoute": configIpSubnetDefaultRoute,
       "ipFactory": ipFactory,
       "synfloodprotection": synfloodprotection,
       "dropinvalidpacket": dropinvalidpacket,
       "configIpZonesTable": configIpZonesTable,
       "configIpZonesEntry": configIpZonesEntry,
       "configIpZoneIndex": configIpZoneIndex,
       "configIpZoneRowStatus": configIpZoneRowStatus,
       "configIpZoneFriendlyName": configIpZoneFriendlyName,
       "configIpZoneNAT": configIpZoneNAT,
       "configIpZoneMSSClamping": configIpZoneMSSClamping,
       "configIpZoneDefaultAcceptancePolicy": configIpZoneDefaultAcceptancePolicy,
       "configIpZoneRestrictedAddressFamily": configIpZoneRestrictedAddressFamily,
       "configIpZoneConnectionTracking": configIpZoneConnectionTracking,
       "configIpZoneLogging": configIpZoneLogging,
       "configIpZoneLoggingLimit": configIpZoneLoggingLimit,
       "configIpZoneInterfaces": configIpZoneInterfaces,
       "configIpNatIpForwardTable": configIpNatIpForwardTable,
       "configIpNatIpForwardEntry": configIpNatIpForwardEntry,
       "configIpNatIpForwardIndex": configIpNatIpForwardIndex,
       "configIpNatIpForwardRowStatus": configIpNatIpForwardRowStatus,
       "configIpNatIpForwardFriendlyName": configIpNatIpForwardFriendlyName,
       "configIpNatIpForwardZoneName": configIpNatIpForwardZoneName,
       "configIpNatIpForwardSrcIp": configIpNatIpForwardSrcIp,
       "configIpNatIpForwardProtocol": configIpNatIpForwardProtocol,
       "configIpNatIpForwardPublicPort": configIpNatIpForwardPublicPort,
       "configIpNatIpForwardPrivatePort": configIpNatIpForwardPrivatePort,
       "configIpNatIpForwardTargetIp": configIpNatIpForwardTargetIp,
       "configIpFirewallTable": configIpFirewallTable,
       "configIpFirewallEntry": configIpFirewallEntry,
       "configIpFirewallIndex": configIpFirewallIndex,
       "configIpFirewallRowStatus": configIpFirewallRowStatus,
       "configIpFirewallZoneName": configIpFirewallZoneName,
       "configIpFirewallProtocol": configIpFirewallProtocol,
       "configIpFirewallPort": configIpFirewallPort,
       "configIpFirewallAction": configIpFirewallAction,
       "configIpFirewallDestZone": configIpFirewallDestZone,
       "configIpFirewallSrcIP": configIpFirewallSrcIP,
       "configIpFirewallTargetIP": configIpFirewallTargetIP,
       "configIpRoutesTable": configIpRoutesTable,
       "configIpRoutesEntry": configIpRoutesEntry,
       "configIpRoutesIndex": configIpRoutesIndex,
       "configIpRoutesRowStatus": configIpRoutesRowStatus,
       "configIpRoutesNetwork": configIpRoutesNetwork,
       "configIpRoutesTarget": configIpRoutesTarget,
       "configIpRoutesNetmask": configIpRoutesNetmask,
       "configIpRoutesGateway": configIpRoutesGateway,
       "configIpRoutesMetric": configIpRoutesMetric,
       "configIpRoutesMTU": configIpRoutesMTU,
       "configIpZoneForwardTable": configIpZoneForwardTable,
       "configIpZoneForwardEntry": configIpZoneForwardEntry,
       "configIpZoneForwardIndex": configIpZoneForwardIndex,
       "configIpZoneForwardRowStatus": configIpZoneForwardRowStatus,
       "configIpZoneForwardSrc": configIpZoneForwardSrc,
       "configIpZoneForwardDst": configIpZoneForwardDst,
       "configIpDscpTaggingTable": configIpDscpTaggingTable,
       "configIpDscpTaggingEntry": configIpDscpTaggingEntry,
       "configIpDscpTaggingIndex": configIpDscpTaggingIndex,
       "configIpDscpTaggingRowStatus": configIpDscpTaggingRowStatus,
       "configIpDscpTaggingFriendlyName": configIpDscpTaggingFriendlyName,
       "configIpDscpTaggingProtocol": configIpDscpTaggingProtocol,
       "configIpDscpTaggingSrcIP": configIpDscpTaggingSrcIP,
       "configIpDscpTaggingDstIP": configIpDscpTaggingDstIP,
       "configIpDscpTaggingSrcPort": configIpDscpTaggingSrcPort,
       "configIpDscpTaggingDstPort": configIpDscpTaggingDstPort,
       "configIpDscpTaggingDscpValue": configIpDscpTaggingDscpValue,
       "netphy": netphy,
       "configPhyWifiTable": configPhyWifiTable,
       "configPhyWifiEntry": configPhyWifiEntry,
       "configPhyWifiName": configPhyWifiName,
       "configPhyWifiLabel": configPhyWifiLabel,
       "configPhyWifiMAC": configPhyWifiMAC,
       "configPhyWifiEnable": configPhyWifiEnable,
       "configPhyWifiMode": configPhyWifiMode,
       "configPhyWifiCountry": configPhyWifiCountry,
       "configPhyWifiChannel": configPhyWifiChannel,
       "configPhyWifiHTMode": configPhyWifiHTMode,
       "configPhyWifiTxPowerDBM": configPhyWifiTxPowerDBM,
       "configPhyWifiDistance": configPhyWifiDistance,
       "configPhyWifiClusterMode": configPhyWifiClusterMode,
       "configPhyWifiClusterList": configPhyWifiClusterList,
       "configPhyWifiClusterArgs": configPhyWifiClusterArgs,
       "configPhyWifiAntennaPorts": configPhyWifiAntennaPorts,
       "configPhyWifiABGBasicRates": configPhyWifiABGBasicRates,
       "configPhyWifiABGSupportedRates": configPhyWifiABGSupportedRates,
       "configPhyWifiChannelList": configPhyWifiChannelList,
       "configPhyWifiWids": configPhyWifiWids,
       "configPhyCellTable": configPhyCellTable,
       "configPhyCellEntry": configPhyCellEntry,
       "configPhyCellName": configPhyCellName,
       "configPhyCellLabel": configPhyCellLabel,
       "configPhyCellDisableAtBoot": configPhyCellDisableAtBoot,
       "configPhyCellLogAT": configPhyCellLogAT,
       "configPhyCellSIM": configPhyCellSIM,
       "configPhyCellSetPIN": configPhyCellSetPIN,
       "configPhyCellSetPUK": configPhyCellSetPUK,
       "configPhyCellSetPINStatus": configPhyCellSetPINStatus,
       "configPhyCellSim1Pin": configPhyCellSim1Pin,
       "configPhyCellSim1Apn": configPhyCellSim1Apn,
       "configPhyCellSim1Authentication": configPhyCellSim1Authentication,
       "configPhyCellSim1Identity": configPhyCellSim1Identity,
       "configPhyCellSim1Password": configPhyCellSim1Password,
       "configPhyCellSim2Pin": configPhyCellSim2Pin,
       "configPhyCellSim2Apn": configPhyCellSim2Apn,
       "configPhyCellSim2Authentication": configPhyCellSim2Authentication,
       "configPhyCellSim2Identity": configPhyCellSim2Identity,
       "configPhyCellSim2Password": configPhyCellSim2Password,
       "netif": netif,
       "netdetails": netdetails,
       "configRadiusTable": configRadiusTable,
       "configRadiusEntry": configRadiusEntry,
       "configRadiusIndex": configRadiusIndex,
       "configRadiusRowStatus": configRadiusRowStatus,
       "configRadiusIpAddress": configRadiusIpAddress,
       "configRadiusPort": configRadiusPort,
       "configRadiusSecret": configRadiusSecret,
       "configDetailsNasId": configDetailsNasId,
       "configFilterGroupTable": configFilterGroupTable,
       "configFilterGroupEntry": configFilterGroupEntry,
       "configFilterGroupIndex": configFilterGroupIndex,
       "configFilterGroupRowStatus": configFilterGroupRowStatus,
       "configFilterGroupFriendlyName": configFilterGroupFriendlyName,
       "configFilterGroupRuleTable": configFilterGroupRuleTable,
       "configFilterGroupRuleEntry": configFilterGroupRuleEntry,
       "configFilterGroupRuleIndex": configFilterGroupRuleIndex,
       "configFilterGroupRuleRowStatus": configFilterGroupRuleRowStatus,
       "configFilterGroupGroupIndex": configFilterGroupGroupIndex,
       "configFilterGroupRuleMACFrameType": configFilterGroupRuleMACFrameType,
       "configFilterGroupRuleCheckMAC": configFilterGroupRuleCheckMAC,
       "configFilterGroupRuleNetworkProtocol": configFilterGroupRuleNetworkProtocol,
       "configFilterGroupRuleIpAddress": configFilterGroupRuleIpAddress,
       "configFilterGroupRuleNetmask": configFilterGroupRuleNetmask,
       "configFilterGroupRuleCheckIP": configFilterGroupRuleCheckIP,
       "configFilterGroupRuleTransportProtocol": configFilterGroupRuleTransportProtocol,
       "configFilterGroupRuleFirstPort": configFilterGroupRuleFirstPort,
       "configFilterGroupRuleLastPort": configFilterGroupRuleLastPort,
       "configFilterGroupRuleCheckPort": configFilterGroupRuleCheckPort,
       "configInterfaceTable": configInterfaceTable,
       "configInterfaceEntry": configInterfaceEntry,
       "configInterfaceName": configInterfaceName,
       "configInterfaceRowStatus": configInterfaceRowStatus,
       "configInterfaceType": configInterfaceType,
       "configInterfaceDepends": configInterfaceDepends,
       "configInterfaceOutputFilterGroup": configInterfaceOutputFilterGroup,
       "configInterfaceFilterGroupDir": configInterfaceFilterGroupDir,
       "configInterfaceInputFilterGroup": configInterfaceInputFilterGroup,
       "configIfStaTable": configIfStaTable,
       "configIfStaEntry": configIfStaEntry,
       "configIfStaName": configIfStaName,
       "configIfStaRowStatus": configIfStaRowStatus,
       "configIfStaPhy": configIfStaPhy,
       "configIfStaSsid": configIfStaSsid,
       "configIfStaBssid": configIfStaBssid,
       "configIfStaBridgingMode": configIfStaBridgingMode,
       "configIfStaScanChannels": configIfStaScanChannels,
       "configIfStaScanPassive": configIfStaScanPassive,
       "configIfStaRoamingEnable": configIfStaRoamingEnable,
       "configIfStaRoamingEnableDBM": configIfStaRoamingEnableDBM,
       "configIfStaRoamingRequiredBoost": configIfStaRoamingRequiredBoost,
       "configIfStaRoamingScanPeriod": configIfStaRoamingScanPeriod,
       "configIfStaSecurityMode": configIfStaSecurityMode,
       "configIfStaWepKey1": configIfStaWepKey1,
       "configIfStaWepKey2": configIfStaWepKey2,
       "configIfStaWepKey3": configIfStaWepKey3,
       "configIfStaWepKey4": configIfStaWepKey4,
       "configIfStaWepKey": configIfStaWepKey,
       "configIfStaWpaVersion": configIfStaWpaVersion,
       "configIfStaWpaCipher": configIfStaWpaCipher,
       "configIfStaIdentity": configIfStaIdentity,
       "configIfStaKey": configIfStaKey,
       "configIfStaPrivateKey": configIfStaPrivateKey,
       "configIfStaCACert": configIfStaCACert,
       "configIfStaEapType": configIfStaEapType,
       "configIfStaAuthentication": configIfStaAuthentication,
       "configIfStaFastBSSTransitionActivated": configIfStaFastBSSTransitionActivated,
       "configIfStaIgnorePreviousScansResults": configIfStaIgnorePreviousScansResults,
       "configIfStaRoamingRssiSmoothingFactor": configIfStaRoamingRssiSmoothingFactor,
       "configIfStaRoamingBeaconTimeout": configIfStaRoamingBeaconTimeout,
       "configIfStaWpaKeyCacheLifetime": configIfStaWpaKeyCacheLifetime,
       "configIfStaRoamingCurrentApScanThreshold": configIfStaRoamingCurrentApScanThreshold,
       "configIfStaRoamingMinimumStaLevel": configIfStaRoamingMinimumStaLevel,
       "configIfStaRoamingAboveLevelThreshold": configIfStaRoamingAboveLevelThreshold,
       "configIfStaRoamingMaxSignalLevel": configIfStaRoamingMaxSignalLevel,
       "configIfStaRoamingMinRoamDelay": configIfStaRoamingMinRoamDelay,
       "configIfStaRoamingNoReturnDelay": configIfStaRoamingNoReturnDelay,
       "configIfStaRoamingThresholdHysteresis": configIfStaRoamingThresholdHysteresis,
       "configIfStaRoamingOffChanMaxDelay": configIfStaRoamingOffChanMaxDelay,
       "configIfStaRoamingOffChanProbeDelay": configIfStaRoamingOffChanProbeDelay,
       "configIfStaRoamingPerChanProbeDelay": configIfStaRoamingPerChanProbeDelay,
       "configIfStaUserCert": configIfStaUserCert,
       "configIfStaDeauthBeforeRoamingtoNextAP": configIfStaDeauthBeforeRoamingtoNextAP,
       "configIfAPTable": configIfAPTable,
       "configIfAPEntry": configIfAPEntry,
       "configIfAPName": configIfAPName,
       "configIfAPRowStatus": configIfAPRowStatus,
       "configIfAPPhy": configIfAPPhy,
       "configIfAPSsid": configIfAPSsid,
       "configIfAPHidden": configIfAPHidden,
       "configIfAPWds": configIfAPWds,
       "configIfAPIsolate": configIfAPIsolate,
       "configIfAPSecurityMode": configIfAPSecurityMode,
       "configIfAPWepKey1": configIfAPWepKey1,
       "configIfAPWepKey2": configIfAPWepKey2,
       "configIfAPWepKey3": configIfAPWepKey3,
       "configIfAPWepKey4": configIfAPWepKey4,
       "configIfAPWepKey": configIfAPWepKey,
       "configIfAPWepAuthentication": configIfAPWepAuthentication,
       "configIfAPWpaVersion": configIfAPWpaVersion,
       "configIfAPWpaCipher": configIfAPWpaCipher,
       "configIfAPKey": configIfAPKey,
       "configIfAPRadiusIndex": configIfAPRadiusIndex,
       "configIfAPPreAuthentication": configIfAPPreAuthentication,
       "configIfAPMACFilterBehaviour": configIfAPMACFilterBehaviour,
       "configIfAPMACFilterAddresses": configIfAPMACFilterAddresses,
       "configIfAPWpaGroupRekey": configIfAPWpaGroupRekey,
       "configIfAPWpaPairRekey": configIfAPWpaPairRekey,
       "configIfAPWpaMasterRekey": configIfAPWpaMasterRekey,
       "configIfAPWpaProtectedFrame": configIfAPWpaProtectedFrame,
       "configIfAPMaxSimultaneousAssoc": configIfAPMaxSimultaneousAssoc,
       "configIfAPPasspointConfigName": configIfAPPasspointConfigName,
       "configIfMeshTable": configIfMeshTable,
       "configIfMeshEntry": configIfMeshEntry,
       "configIfMeshName": configIfMeshName,
       "configIfMeshRowStatus": configIfMeshRowStatus,
       "configIfMeshPhy": configIfMeshPhy,
       "configIfMeshId": configIfMeshId,
       "configIfMeshSecurityMode": configIfMeshSecurityMode,
       "configIfMeshPreSharedKey": configIfMeshPreSharedKey,
       "configIfMeshPathRefreshTime": configIfMeshPathRefreshTime,
       "configIfMeshMinDiscoveryTimeout": configIfMeshMinDiscoveryTimeout,
       "configIfMeshActivePathTimeout": configIfMeshActivePathTimeout,
       "configIfMeshNetworkDiameterTraversalTime": configIfMeshNetworkDiameterTraversalTime,
       "configIfMeshRootMode": configIfMeshRootMode,
       "configIfMeshGatesAnnouncement": configIfMeshGatesAnnouncement,
       "configIfMeshActivePathToRootTimeout": configIfMeshActivePathToRootTimeout,
       "configIfMeshPreqRootInterval": configIfMeshPreqRootInterval,
       "configIfMeshRannRootInterval": configIfMeshRannRootInterval,
       "configIfBridgeTable": configIfBridgeTable,
       "configIfBridgeEntry": configIfBridgeEntry,
       "configIfBridgeName": configIfBridgeName,
       "configIfBridgeRowStatus": configIfBridgeRowStatus,
       "configIfBridgeStp": configIfBridgeStp,
       "configIfBridgePriority": configIfBridgePriority,
       "configIfBridgeHello": configIfBridgeHello,
       "configIfBridgeMaxAge": configIfBridgeMaxAge,
       "configIfBridgeForwardDelay": configIfBridgeForwardDelay,
       "configIfBridgeLldpForward": configIfBridgeLldpForward,
       "configIfVlanTable": configIfVlanTable,
       "configIfVlanEntry": configIfVlanEntry,
       "configIfVlanIndex": configIfVlanIndex,
       "configIfVlanRowStatus": configIfVlanRowStatus,
       "configIfVlanFriendlyName": configIfVlanFriendlyName,
       "configIfVlanHostIfName": configIfVlanHostIfName,
       "configIfVlanId": configIfVlanId,
       "configIfSrccTable": configIfSrccTable,
       "configIfSrccEntry": configIfSrccEntry,
       "configIfSrccName": configIfSrccName,
       "configIfSrccRowStatus": configIfSrccRowStatus,
       "configIfSrccPhy": configIfSrccPhy,
       "configIfSrccDiscoverApSsid": configIfSrccDiscoverApSsid,
       "configIfSrccProductType": configIfSrccProductType,
       "configIfSrccDiscSigThreshold": configIfSrccDiscSigThreshold,
       "configIfSrccDiscDuration": configIfSrccDiscDuration,
       "configIfSrccBrokenThreshold": configIfSrccBrokenThreshold,
       "configIfSrccBrokenDuration": configIfSrccBrokenDuration,
       "configIfSrccWifiBand": configIfSrccWifiBand,
       "configIfSrccFirstChannel": configIfSrccFirstChannel,
       "configIfSrccSecondChannel": configIfSrccSecondChannel,
       "configIfSrccDiscScanDuration": configIfSrccDiscScanDuration,
       "configIfSrccMixRedundancy": configIfSrccMixRedundancy,
       "configIfSrccMixRedundancyBoost": configIfSrccMixRedundancyBoost,
       "configIfSrccPeerTableTimeout": configIfSrccPeerTableTimeout,
       "configIfSrccTargetTableTimeout": configIfSrccTargetTableTimeout,
       "configIfSrccPeerAcknowTimeout": configIfSrccPeerAcknowTimeout,
       "configIfSrccPeerReconfigTimeout": configIfSrccPeerReconfigTimeout,
       "configIfSrccGreBridgeIpAddr": configIfSrccGreBridgeIpAddr,
       "roaming": roaming,
       "roamingAlgorithm": roamingAlgorithm,
       "roamingPLHposition": roamingPLHposition,
       "roamingPLHjitter": roamingPLHjitter,
       "roamingPLHurgent": roamingPLHurgent,
       "roamingPLHfront": roamingPLHfront,
       "roamingPLHfrontCandMin": roamingPLHfrontCandMin,
       "roamingPLHfrontCandMax": roamingPLHfrontCandMax,
       "roamingPLHfrontCurrentLow": roamingPLHfrontCurrentLow,
       "roamingPLHfrontCurrentHigh": roamingPLHfrontCurrentHigh,
       "roamingPLHrear": roamingPLHrear,
       "roamingPLHrearCandMin": roamingPLHrearCandMin,
       "roamingPLHrearCandMax": roamingPLHrearCandMax,
       "roamingPLHrearCurrentLow": roamingPLHrearCurrentLow,
       "roamingPLHrearCurrentHigh": roamingPLHrearCurrentHigh,
       "serviceStatus": serviceStatus,
       "ss-webserver": ss_webserver,
       "ss-dhcp": ss_dhcp,
       "ss-ntp": ss_ntp,
       "ss-radius": ss_radius,
       "ss-snmp": ss_snmp,
       "snmpAgentOIDTable": snmpAgentOIDTable,
       "snmpAgentOIDEntry": snmpAgentOIDEntry,
       "snmpAgentOIDIndex": snmpAgentOIDIndex,
       "snmpAgentOIDProductID": snmpAgentOIDProductID,
       "ss-dns": ss_dns,
       "ss-system": ss_system,
       "systemReady": systemReady,
       "sensors": sensors,
       "tempSensors": tempSensors,
       "motherBoard0": motherBoard0,
       "gpioInTable": gpioInTable,
       "gpioInEntry": gpioInEntry,
       "gpioInIndex": gpioInIndex,
       "gpioInState": gpioInState,
       "gpioOutTable": gpioOutTable,
       "gpioOutEntry": gpioOutEntry,
       "gpioOutIndex": gpioOutIndex,
       "gpioOutState": gpioOutState,
       "ss-gnss": ss_gnss,
       "gnss-current-position": gnss_current_position,
       "positionValid": positionValid,
       "fixdate": fixdate,
       "fixtime": fixtime,
       "latitude": latitude,
       "longitude": longitude,
       "altitude": altitude,
       "speedkmh": speedkmh,
       "courseDegrees": courseDegrees,
       "fixdimension": fixdimension,
       "gnssAllPositions": gnssAllPositions,
       "ss-tcn": ss_tcn,
       "ss-async-sysupgrade": ss_async_sysupgrade,
       "firmwareExists": firmwareExists,
       "firmwareInfo": firmwareInfo,
       "sysupgradeMissed": sysupgradeMissed,
       "serviceConfiguration": serviceConfiguration,
       "sc-webserver": sc_webserver,
       "configHttpServer": configHttpServer,
       "configHttpServerPort": configHttpServerPort,
       "configHttpsServer": configHttpsServer,
       "configHttpsPort": configHttpsPort,
       "configHttpsCertificate": configHttpsCertificate,
       "sc-dhcp": sc_dhcp,
       "configDhcpTable": configDhcpTable,
       "configDhcpEntry": configDhcpEntry,
       "configDhcpSubnet": configDhcpSubnet,
       "configDhcpRowStatus": configDhcpRowStatus,
       "configDhcpEnable": configDhcpEnable,
       "configDhcpPoolStart": configDhcpPoolStart,
       "configDhcpPoolCount": configDhcpPoolCount,
       "configDhcpLeaseDuration": configDhcpLeaseDuration,
       "sc-ntp": sc_ntp,
       "configNtp": configNtp,
       "sc-radius": sc_radius,
       "sc-snmp": sc_snmp,
       "sc-dns": sc_dns,
       "configRelay": configRelay,
       "configDnsRebindProtection": configDnsRebindProtection,
       "configDnsRebindLocalhost": configDnsRebindLocalhost,
       "sc-ssh": sc_ssh,
       "configSshEnable": configSshEnable,
       "configSshEnablePwd": configSshEnablePwd,
       "sc-tcn": sc_tcn,
       "sc-collectd": sc_collectd,
       "configCollectdEnable": configCollectdEnable,
       "configCollectdSamplingInterval": configCollectdSamplingInterval,
       "plugin-GPS": plugin_GPS,
       "configCollectdGPSEnable": configCollectdGPSEnable,
       "configCollectdGPSServerAddr": configCollectdGPSServerAddr,
       "configCollectdGPSServerPort": configCollectdGPSServerPort,
       "configCollectdGPSConnTimeout": configCollectdGPSConnTimeout,
       "configCollectdGPSReqInterval": configCollectdGPSReqInterval,
       "plugin-AcksysScanResult": plugin_AcksysScanResult,
       "configCollectdWirelessScanResult": configCollectdWirelessScanResult,
       "plugin-iwinfo": plugin_iwinfo,
       "configCollectdIwinfo": configCollectdIwinfo,
       "plugin-AcksysTelemetry": plugin_AcksysTelemetry,
       "configAcksysTelemetryEnable": configAcksysTelemetryEnable,
       "configAcksysTelemetryServerPort": configAcksysTelemetryServerPort,
       "configAcksysTelemetryOutputInterval": configAcksysTelemetryOutputInterval,
       "configAcksysTelemetryMaxBufferSize": configAcksysTelemetryMaxBufferSize,
       "sc-passpoint": sc_passpoint,
       "configPasspointConfigTable": configPasspointConfigTable,
       "configPasspointConfigEntry": configPasspointConfigEntry,
       "configPasspointConfigName": configPasspointConfigName,
       "configPasspointConfigRowStatus": configPasspointConfigRowStatus,
       "configPasspointConfigAnqpAccessNetworkType": configPasspointConfigAnqpAccessNetworkType,
       "configPasspointConfigAnqpInternet": configPasspointConfigAnqpInternet,
       "configPasspointConfigAnqpAsra": configPasspointConfigAnqpAsra,
       "configPasspointConfigAnqpEsr": configPasspointConfigAnqpEsr,
       "configPasspointConfigAnqpUesa": configPasspointConfigAnqpUesa,
       "configPasspointConfigAnqpHessid": configPasspointConfigAnqpHessid,
       "configPasspointConfigAnqpGasAddress3": configPasspointConfigAnqpGasAddress3,
       "configPasspointConfigAnqpVenueProfile": configPasspointConfigAnqpVenueProfile,
       "configPasspointConfigAnqpRoamingConsortiumProfile": configPasspointConfigAnqpRoamingConsortiumProfile,
       "configPasspointConfigAnqpNetworkAuthTypeProfile": configPasspointConfigAnqpNetworkAuthTypeProfile,
       "configPasspointConfigAnqpIpAddrTypeAvailProfile": configPasspointConfigAnqpIpAddrTypeAvailProfile,
       "configPasspointConfigAnqpDomainNameProfile": configPasspointConfigAnqpDomainNameProfile,
       "configPasspointConfigAnqp3gppCellNetProfile": configPasspointConfigAnqp3gppCellNetProfile,
       "configPasspointConfigAnqpNaiRealmProfile": configPasspointConfigAnqpNaiRealmProfile,
       "configPasspointConfigAnqpOverrideElementProfile": configPasspointConfigAnqpOverrideElementProfile,
       "configPasspointConfigHS20DisableDgaf": configPasspointConfigHS20DisableDgaf,
       "configPasspointConfigHS20DomainId": configPasspointConfigHS20DomainId,
       "configPasspointConfigHS20DeauthReqTimeout": configPasspointConfigHS20DeauthReqTimeout,
       "configPasspointConfigHS20OsuSsid": configPasspointConfigHS20OsuSsid,
       "configPasspointConfigHS20OperFriendlyNameProfile": configPasspointConfigHS20OperFriendlyNameProfile,
       "configPasspointConfigHS20ConnCapProfile": configPasspointConfigHS20ConnCapProfile,
       "configPasspointConfigHS20WanMetricsProfile": configPasspointConfigHS20WanMetricsProfile,
       "configPasspointConfigHS20OperClassProfile": configPasspointConfigHS20OperClassProfile,
       "configPasspointConfigHS20OsuProviderProfile": configPasspointConfigHS20OsuProviderProfile,
       "configAnqpProfileVenueTable": configAnqpProfileVenueTable,
       "configAnqpProfileVenueEntry": configAnqpProfileVenueEntry,
       "configProfileVenueName": configProfileVenueName,
       "configProfileVenueRowStatus": configProfileVenueRowStatus,
       "configProfileVenueDesc": configProfileVenueDesc,
       "configVenueGroup": configVenueGroup,
       "configVenueType": configVenueType,
       "configVenueNameList": configVenueNameList,
       "configAnqpProfileRoamingConsortiumTable": configAnqpProfileRoamingConsortiumTable,
       "configAnqpProfileRoamingConsortiumEntry": configAnqpProfileRoamingConsortiumEntry,
       "configProfileRoamingConsortiumName": configProfileRoamingConsortiumName,
       "configProfileRoamingConsortiumRowStatus": configProfileRoamingConsortiumRowStatus,
       "configProfileRoamingConsortiumDesc": configProfileRoamingConsortiumDesc,
       "configRoamingConsortiumList": configRoamingConsortiumList,
       "configAnqpProfileNetworkAuthTypeTable": configAnqpProfileNetworkAuthTypeTable,
       "configAnqpProfileNetworkAuthTypeEntry": configAnqpProfileNetworkAuthTypeEntry,
       "configProfileNetworkAuthTypeName": configProfileNetworkAuthTypeName,
       "configProfileNetworkAuthTypeRowStatus": configProfileNetworkAuthTypeRowStatus,
       "configProfileNetworkAuthTypeDesc": configProfileNetworkAuthTypeDesc,
       "configNetworkAuthType": configNetworkAuthType,
       "configAnqpProfileIpAddrTypeAvailTable": configAnqpProfileIpAddrTypeAvailTable,
       "configAnqpProfileIpAddrTypeAvailEntry": configAnqpProfileIpAddrTypeAvailEntry,
       "configProfileIpAddrTypeAvailName": configProfileIpAddrTypeAvailName,
       "configProfileIpAddrTypeAvailRowStatus": configProfileIpAddrTypeAvailRowStatus,
       "configProfileIpAddrTypeAvailDesc": configProfileIpAddrTypeAvailDesc,
       "configIpv4Type": configIpv4Type,
       "configIpv6Type": configIpv6Type,
       "configAnqpProfileDomainNameTable": configAnqpProfileDomainNameTable,
       "configAnqpProfileDomainNameEntry": configAnqpProfileDomainNameEntry,
       "configProfileDomainNameName": configProfileDomainNameName,
       "configProfileDomainNameRowStatus": configProfileDomainNameRowStatus,
       "configProfileDomainNameDesc": configProfileDomainNameDesc,
       "configDomainNameList": configDomainNameList,
       "configAnqpProfile3gppCellNetTable": configAnqpProfile3gppCellNetTable,
       "configAnqpProfile3gppCellNetEntry": configAnqpProfile3gppCellNetEntry,
       "configProfile3gppCellNetName": configProfile3gppCellNetName,
       "configProfile3gppCellNetRowStatus": configProfile3gppCellNetRowStatus,
       "configProfile3gppCellNetDesc": configProfile3gppCellNetDesc,
       "config3gppCellNetList": config3gppCellNetList,
       "configAnqpProfileNaiRealmTable": configAnqpProfileNaiRealmTable,
       "configAnqpProfileNaiRealmEntry": configAnqpProfileNaiRealmEntry,
       "configProfileNaiRealmName": configProfileNaiRealmName,
       "configProfileNaiRealmRowStatus": configProfileNaiRealmRowStatus,
       "configProfileNaiRealmDesc": configProfileNaiRealmDesc,
       "configNaiRealmEncode": configNaiRealmEncode,
       "configNaiRealmRealmList": configNaiRealmRealmList,
       "configNaiRealmEap": configNaiRealmEap,
       "configAnqpProfileOverrideElementTable": configAnqpProfileOverrideElementTable,
       "configAnqpProfileOverrideElementEntry": configAnqpProfileOverrideElementEntry,
       "configProfileOverrideElementName": configProfileOverrideElementName,
       "configProfileOverrideElementRowStatus": configProfileOverrideElementRowStatus,
       "configProfileOverrideElementDesc": configProfileOverrideElementDesc,
       "configAnqpOverrideList": configAnqpOverrideList,
       "configHS20ProfileOperFriendlyNameTable": configHS20ProfileOperFriendlyNameTable,
       "configHS20ProfileOperFriendlyNameEntry": configHS20ProfileOperFriendlyNameEntry,
       "configProfileOperFriendlyNameName": configProfileOperFriendlyNameName,
       "configProfileOperFriendlyNameRowStatus": configProfileOperFriendlyNameRowStatus,
       "configProfileOperFriendlyNameDesc": configProfileOperFriendlyNameDesc,
       "configFriendlyNameList": configFriendlyNameList,
       "configHS20ProfileConnCapTable": configHS20ProfileConnCapTable,
       "configHS20ProfileConnCapEntry": configHS20ProfileConnCapEntry,
       "configProfileConnCapName": configProfileConnCapName,
       "configProfileConnCapRowStatus": configProfileConnCapRowStatus,
       "configProfileConnCapDesc": configProfileConnCapDesc,
       "configConnCapabList": configConnCapabList,
       "configHS20ProfileWanMetricsTable": configHS20ProfileWanMetricsTable,
       "configHS20ProfileWanMetricsEntry": configHS20ProfileWanMetricsEntry,
       "configProfileWanMetricsName": configProfileWanMetricsName,
       "configProfileWanMetricsRowStatus": configProfileWanMetricsRowStatus,
       "configProfileWanMetricsDesc": configProfileWanMetricsDesc,
       "configLinkStatus": configLinkStatus,
       "configSymmetric": configSymmetric,
       "configAtCapacity": configAtCapacity,
       "configDownSpeed": configDownSpeed,
       "configUpSpeed": configUpSpeed,
       "configDownLoad": configDownLoad,
       "configUpLoad": configUpLoad,
       "configLMD": configLMD,
       "configHS20ProfileOperClassTable": configHS20ProfileOperClassTable,
       "configHS20ProfileOperClassEntry": configHS20ProfileOperClassEntry,
       "configProfileOperClassName": configProfileOperClassName,
       "configProfileOperClassRowStatus": configProfileOperClassRowStatus,
       "configProfileOperClassDesc": configProfileOperClassDesc,
       "configOperClassList": configOperClassList,
       "configHS20ProfileOsuProviderTable": configHS20ProfileOsuProviderTable,
       "configHS20ProfileOsuProviderEntry": configHS20ProfileOsuProviderEntry,
       "configProfileOsuProviderName": configProfileOsuProviderName,
       "configProfileOsuProviderRowStatus": configProfileOsuProviderRowStatus,
       "configProfileOsuProviderDesc": configProfileOsuProviderDesc,
       "configOsuServerUri": configOsuServerUri,
       "configOsuFriendlyNameList": configOsuFriendlyNameList,
       "configOsuNai": configOsuNai,
       "configOsuOmaDm": configOsuOmaDm,
       "configOsuSoapXml": configOsuSoapXml,
       "configOsuIconProfileList": configOsuIconProfileList,
       "configOsuServiceDescList": configOsuServiceDescList,
       "configProfileIconTable": configProfileIconTable,
       "configProfileIconEntry": configProfileIconEntry,
       "configProfileIconName": configProfileIconName,
       "configProfileIconRowStatus": configProfileIconRowStatus,
       "configProfileIconDesc": configProfileIconDesc,
       "configIconLang": configIconLang,
       "configIconSize": configIconSize,
       "configIconType": configIconType,
       "configIconPath": configIconPath,
       "configIconFileContent": configIconFileContent,
       "sc-async-sysupgrade": sc_async_sysupgrade,
       "configAsyncUpgradeDoUpgrade": configAsyncUpgradeDoUpgrade,
       "configAsyncUpgradeTimerEnable": configAsyncUpgradeTimerEnable,
       "configAsyncUpgradeTimerMode": configAsyncUpgradeTimerMode,
       "configAsyncUpgradeTimerMinute": configAsyncUpgradeTimerMinute,
       "sc-md5sum": sc_md5sum,
       "configMD5SUMstatus": configMD5SUMstatus,
       "configMD5SUMfiles": configMD5SUMfiles,
       "notification": notification,
       "linkAlarm": linkAlarm,
       "powerAlarm": powerAlarm,
       "digitalInputAlarm": digitalInputAlarm,
       "tempExceededAlarm": tempExceededAlarm,
       "clientLinkAlarm": clientLinkAlarm,
       "vrrpAlarm": vrrpAlarm,
       "dfsAlarm": dfsAlarm,
       "pingerAlarm": pingerAlarm,
       "tcnAlarm": tcnAlarm,
       "securityAlarm": securityAlarm,
       "notificationBindings": notificationBindings,
       "nbClientMacAddress": nbClientMacAddress,
       "nbSsid": nbSsid,
       "nbBssid": nbBssid,
       "nbEventState": nbEventState,
       "nbEventName": nbEventName,
       "nbRadioName": nbRadioName,
       "nbRadioMacAddress": nbRadioMacAddress,
       "nbRadioChannel": nbRadioChannel,
       "nbRadioChannelWidth": nbRadioChannelWidth,
       "nbRadarChannel": nbRadarChannel,
       "nbRadarChannelWidth": nbRadarChannelWidth,
       "nbHostName": nbHostName,
       "nbDigitalInName": nbDigitalInName,
       "nbTcnTaiIp": nbTcnTaiIp,
       "nbTcnEtbnStatus": nbTcnEtbnStatus,
       "nbTcnEtbnRole": nbTcnEtbnRole,
       "nbTcnEtbnTopoCnt": nbTcnEtbnTopoCnt,
       "nbTcnEtbTopoCntState": nbTcnEtbTopoCntState,
       "nbTcnLengtheningFlag": nbTcnLengtheningFlag,
       "nbTcnShorteningState": nbTcnShorteningState,
       "nbTcnRadio1CouplingState": nbTcnRadio1CouplingState,
       "nbTcnConsistCount": nbTcnConsistCount,
       "nbTcnConsistPosition": nbTcnConsistPosition,
       "nbDescription": nbDescription,
       "nbTimestamp": nbTimestamp,
       "nbMacAddr": nbMacAddr,
       "nbSource": nbSource,
       "acksysProductSerialNumber": acksysProductSerialNumber}
)
