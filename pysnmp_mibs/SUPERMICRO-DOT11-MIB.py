# SNMP MIB module (SUPERMICRO-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DOT11-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:07 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83)
)
if mibBuilder.loadTexts:
    fsDot11.setRevisions(
        ("2013-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CapwapBaseRadioIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class CapwapDot11WlanIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class CapwapDot11WlanIdProfileTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsDot11Radio_ObjectIdentity = ObjectIdentity
fsDot11Radio = _FsDot11Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1)
)


class _FsDot11aNetworkEnable_Type(EnabledStatus):
    """Custom type fsDot11aNetworkEnable based on EnabledStatus"""
    defaultValue = 1


_FsDot11aNetworkEnable_Type.__name__ = "EnabledStatus"
_FsDot11aNetworkEnable_Object = MibScalar
fsDot11aNetworkEnable = _FsDot11aNetworkEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 1),
    _FsDot11aNetworkEnable_Type()
)
fsDot11aNetworkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11aNetworkEnable.setStatus("current")


class _FsDot11bNetworkEnable_Type(EnabledStatus):
    """Custom type fsDot11bNetworkEnable based on EnabledStatus"""
    defaultValue = 1


_FsDot11bNetworkEnable_Type.__name__ = "EnabledStatus"
_FsDot11bNetworkEnable_Object = MibScalar
fsDot11bNetworkEnable = _FsDot11bNetworkEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 2),
    _FsDot11bNetworkEnable_Type()
)
fsDot11bNetworkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11bNetworkEnable.setStatus("current")


class _FsDot11gSupport_Type(EnabledStatus):
    """Custom type fsDot11gSupport based on EnabledStatus"""
    defaultValue = 2


_FsDot11gSupport_Type.__name__ = "EnabledStatus"
_FsDot11gSupport_Object = MibScalar
fsDot11gSupport = _FsDot11gSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 3),
    _FsDot11gSupport_Type()
)
fsDot11gSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11gSupport.setStatus("current")


class _FsDot11anSupport_Type(EnabledStatus):
    """Custom type fsDot11anSupport based on EnabledStatus"""
    defaultValue = 2


_FsDot11anSupport_Type.__name__ = "EnabledStatus"
_FsDot11anSupport_Object = MibScalar
fsDot11anSupport = _FsDot11anSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 4),
    _FsDot11anSupport_Type()
)
fsDot11anSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11anSupport.setStatus("current")


class _FsDot11bnSupport_Type(EnabledStatus):
    """Custom type fsDot11bnSupport based on EnabledStatus"""
    defaultValue = 2


_FsDot11bnSupport_Type.__name__ = "EnabledStatus"
_FsDot11bnSupport_Object = MibScalar
fsDot11bnSupport = _FsDot11bnSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 5),
    _FsDot11bnSupport_Type()
)
fsDot11bnSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11bnSupport.setStatus("current")


class _FsDot11ManagmentSSID_Type(CapwapDot11WlanIdProfileTC):
    """Custom type fsDot11ManagmentSSID based on CapwapDot11WlanIdProfileTC"""
    defaultValue = 0


_FsDot11ManagmentSSID_Type.__name__ = "CapwapDot11WlanIdProfileTC"
_FsDot11ManagmentSSID_Object = MibScalar
fsDot11ManagmentSSID = _FsDot11ManagmentSSID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 6),
    _FsDot11ManagmentSSID_Type()
)
fsDot11ManagmentSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ManagmentSSID.setStatus("current")


class _FsDot11CountryString_Type(OctetString):
    """Custom type fsDot11CountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_FsDot11CountryString_Type.__name__ = "OctetString"
_FsDot11CountryString_Object = MibScalar
fsDot11CountryString = _FsDot11CountryString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 1, 7),
    _FsDot11CountryString_Type()
)
fsDot11CountryString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11CountryString.setStatus("current")
_FsSecurityWebAuthParams_ObjectIdentity = ObjectIdentity
fsSecurityWebAuthParams = _FsSecurityWebAuthParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2)
)


class _FsSecurityWebAuthType_Type(Integer32):
    """Custom type fsSecurityWebAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_FsSecurityWebAuthType_Type.__name__ = "Integer32"
_FsSecurityWebAuthType_Object = MibScalar
fsSecurityWebAuthType = _FsSecurityWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 1),
    _FsSecurityWebAuthType_Type()
)
fsSecurityWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthType.setStatus("current")
_FsSecurityWebAuthUrl_Type = DisplayString
_FsSecurityWebAuthUrl_Object = MibScalar
fsSecurityWebAuthUrl = _FsSecurityWebAuthUrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 2),
    _FsSecurityWebAuthUrl_Type()
)
fsSecurityWebAuthUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthUrl.setStatus("current")
_FsSecurityWebAuthRedirectUrl_Type = DisplayString
_FsSecurityWebAuthRedirectUrl_Object = MibScalar
fsSecurityWebAuthRedirectUrl = _FsSecurityWebAuthRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 3),
    _FsSecurityWebAuthRedirectUrl_Type()
)
fsSecurityWebAuthRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthRedirectUrl.setStatus("current")
_FsSecurityWebAddr_Type = Integer32
_FsSecurityWebAddr_Object = MibScalar
fsSecurityWebAddr = _FsSecurityWebAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 4),
    _FsSecurityWebAddr_Type()
)
fsSecurityWebAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAddr.setStatus("current")


class _FsSecurityWebAuthWebTitle_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebTitle based on DisplayString"""
    defaultValue = OctetString("Web Authentication")


_FsSecurityWebAuthWebTitle_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebTitle_Object = MibScalar
fsSecurityWebAuthWebTitle = _FsSecurityWebAuthWebTitle_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 5),
    _FsSecurityWebAuthWebTitle_Type()
)
fsSecurityWebAuthWebTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebTitle.setStatus("current")


class _FsSecurityWebAuthWebMessage_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebMessage based on DisplayString"""
    defaultValue = OctetString("Hello welcome aboard!")


_FsSecurityWebAuthWebMessage_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebMessage_Object = MibScalar
fsSecurityWebAuthWebMessage = _FsSecurityWebAuthWebMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 6),
    _FsSecurityWebAuthWebMessage_Type()
)
fsSecurityWebAuthWebMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebMessage.setStatus("current")


class _FsSecurityWebAuthWebLogoFileName_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebLogoFileName based on DisplayString"""
    defaultValue = OctetString("smc_loginnewcr.jpg")


_FsSecurityWebAuthWebLogoFileName_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebLogoFileName_Object = MibScalar
fsSecurityWebAuthWebLogoFileName = _FsSecurityWebAuthWebLogoFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 7),
    _FsSecurityWebAuthWebLogoFileName_Type()
)
fsSecurityWebAuthWebLogoFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebLogoFileName.setStatus("current")


class _FsSecurityWebAuthWebSuccMessage_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebSuccMessage based on DisplayString"""
    defaultValue = OctetString("Authenticated Successfully")


_FsSecurityWebAuthWebSuccMessage_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebSuccMessage_Object = MibScalar
fsSecurityWebAuthWebSuccMessage = _FsSecurityWebAuthWebSuccMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 8),
    _FsSecurityWebAuthWebSuccMessage_Type()
)
fsSecurityWebAuthWebSuccMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebSuccMessage.setStatus("current")


class _FsSecurityWebAuthWebFailMessage_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebFailMessage based on DisplayString"""
    defaultValue = OctetString("Authentication Failed")


_FsSecurityWebAuthWebFailMessage_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebFailMessage_Object = MibScalar
fsSecurityWebAuthWebFailMessage = _FsSecurityWebAuthWebFailMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 9),
    _FsSecurityWebAuthWebFailMessage_Type()
)
fsSecurityWebAuthWebFailMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebFailMessage.setStatus("current")


class _FsSecurityWebAuthWebButtonText_Type(DisplayString):
    """Custom type fsSecurityWebAuthWebButtonText based on DisplayString"""
    defaultValue = OctetString("Submit")


_FsSecurityWebAuthWebButtonText_Type.__name__ = "DisplayString"
_FsSecurityWebAuthWebButtonText_Object = MibScalar
fsSecurityWebAuthWebButtonText = _FsSecurityWebAuthWebButtonText_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 10),
    _FsSecurityWebAuthWebButtonText_Type()
)
fsSecurityWebAuthWebButtonText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebButtonText.setStatus("current")
_FsSecurityWebAuthWebLoadBalInfo_Type = DisplayString
_FsSecurityWebAuthWebLoadBalInfo_Object = MibScalar
fsSecurityWebAuthWebLoadBalInfo = _FsSecurityWebAuthWebLoadBalInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 11),
    _FsSecurityWebAuthWebLoadBalInfo_Type()
)
fsSecurityWebAuthWebLoadBalInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthWebLoadBalInfo.setStatus("current")


class _FsSecurityWebAuthDisplayLang_Type(Integer32):
    """Custom type fsSecurityWebAuthDisplayLang based on Integer32"""
    defaultValue = 1


_FsSecurityWebAuthDisplayLang_Type.__name__ = "Integer32"
_FsSecurityWebAuthDisplayLang_Object = MibScalar
fsSecurityWebAuthDisplayLang = _FsSecurityWebAuthDisplayLang_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 12),
    _FsSecurityWebAuthDisplayLang_Type()
)
fsSecurityWebAuthDisplayLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthDisplayLang.setStatus("current")


class _FsSecurityWebAuthColor_Type(Integer32):
    """Custom type fsSecurityWebAuthColor based on Integer32"""
    defaultValue = 1


_FsSecurityWebAuthColor_Type.__name__ = "Integer32"
_FsSecurityWebAuthColor_Object = MibScalar
fsSecurityWebAuthColor = _FsSecurityWebAuthColor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 2, 13),
    _FsSecurityWebAuthColor_Type()
)
fsSecurityWebAuthColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthColor.setStatus("current")
_FsDot11smt_ObjectIdentity = ObjectIdentity
fsDot11smt = _FsDot11smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3)
)
_FsDot11StationConfigTable_Object = MibTable
fsDot11StationConfigTable = _FsDot11StationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 1)
)
if mibBuilder.loadTexts:
    fsDot11StationConfigTable.setStatus("current")
_FsDot11StationConfigEntry_Object = MibTableRow
fsDot11StationConfigEntry = _FsDot11StationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 1, 1)
)
fsDot11StationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11StationConfigEntry.setStatus("current")


class _FsDot11SupressSSID_Type(TruthValue):
    """Custom type fsDot11SupressSSID based on TruthValue"""
    defaultValue = 2


_FsDot11SupressSSID_Type.__name__ = "TruthValue"
_FsDot11SupressSSID_Object = MibTableColumn
fsDot11SupressSSID = _FsDot11SupressSSID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 1, 1, 1),
    _FsDot11SupressSSID_Type()
)
fsDot11SupressSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11SupressSSID.setStatus("current")


class _FsDot11VlanId_Type(Integer32):
    """Custom type fsDot11VlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsDot11VlanId_Type.__name__ = "Integer32"
_FsDot11VlanId_Object = MibTableColumn
fsDot11VlanId = _FsDot11VlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 1, 1, 2),
    _FsDot11VlanId_Type()
)
fsDot11VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VlanId.setStatus("current")
_FsDot11CapabilityProfileTable_Object = MibTable
fsDot11CapabilityProfileTable = _FsDot11CapabilityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2)
)
if mibBuilder.loadTexts:
    fsDot11CapabilityProfileTable.setStatus("current")
_FsDot11CapabilityProfileEntry_Object = MibTableRow
fsDot11CapabilityProfileEntry = _FsDot11CapabilityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1)
)
fsDot11CapabilityProfileEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsDot11CapabilityProfileName"),
)
if mibBuilder.loadTexts:
    fsDot11CapabilityProfileEntry.setStatus("current")


class _FsDot11CapabilityProfileName_Type(OctetString):
    """Custom type fsDot11CapabilityProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11CapabilityProfileName_Type.__name__ = "OctetString"
_FsDot11CapabilityProfileName_Object = MibTableColumn
fsDot11CapabilityProfileName = _FsDot11CapabilityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 1),
    _FsDot11CapabilityProfileName_Type()
)
fsDot11CapabilityProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11CapabilityProfileName.setStatus("current")


class _FsDot11CFPollable_Type(TruthValue):
    """Custom type fsDot11CFPollable based on TruthValue"""
    defaultValue = 2


_FsDot11CFPollable_Type.__name__ = "TruthValue"
_FsDot11CFPollable_Object = MibTableColumn
fsDot11CFPollable = _FsDot11CFPollable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 2),
    _FsDot11CFPollable_Type()
)
fsDot11CFPollable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11CFPollable.setStatus("current")


class _FsDot11CFPollRequest_Type(TruthValue):
    """Custom type fsDot11CFPollRequest based on TruthValue"""
    defaultValue = 2


_FsDot11CFPollRequest_Type.__name__ = "TruthValue"
_FsDot11CFPollRequest_Object = MibTableColumn
fsDot11CFPollRequest = _FsDot11CFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 3),
    _FsDot11CFPollRequest_Type()
)
fsDot11CFPollRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11CFPollRequest.setStatus("current")


class _FsDot11PrivacyOptionImplemented_Type(TruthValue):
    """Custom type fsDot11PrivacyOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11PrivacyOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11PrivacyOptionImplemented_Object = MibTableColumn
fsDot11PrivacyOptionImplemented = _FsDot11PrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 4),
    _FsDot11PrivacyOptionImplemented_Type()
)
fsDot11PrivacyOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PrivacyOptionImplemented.setStatus("current")


class _FsDot11ShortPreambleOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ShortPreambleOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ShortPreambleOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ShortPreambleOptionImplemented_Object = MibTableColumn
fsDot11ShortPreambleOptionImplemented = _FsDot11ShortPreambleOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 5),
    _FsDot11ShortPreambleOptionImplemented_Type()
)
fsDot11ShortPreambleOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ShortPreambleOptionImplemented.setStatus("current")


class _FsDot11PBCCOptionImplemented_Type(TruthValue):
    """Custom type fsDot11PBCCOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11PBCCOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11PBCCOptionImplemented_Object = MibTableColumn
fsDot11PBCCOptionImplemented = _FsDot11PBCCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 6),
    _FsDot11PBCCOptionImplemented_Type()
)
fsDot11PBCCOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PBCCOptionImplemented.setStatus("current")


class _FsDot11ChannelAgilityPresent_Type(TruthValue):
    """Custom type fsDot11ChannelAgilityPresent based on TruthValue"""
    defaultValue = 2


_FsDot11ChannelAgilityPresent_Type.__name__ = "TruthValue"
_FsDot11ChannelAgilityPresent_Object = MibTableColumn
fsDot11ChannelAgilityPresent = _FsDot11ChannelAgilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 7),
    _FsDot11ChannelAgilityPresent_Type()
)
fsDot11ChannelAgilityPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ChannelAgilityPresent.setStatus("current")


class _FsDot11QosOptionImplemented_Type(TruthValue):
    """Custom type fsDot11QosOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11QosOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11QosOptionImplemented_Object = MibTableColumn
fsDot11QosOptionImplemented = _FsDot11QosOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 8),
    _FsDot11QosOptionImplemented_Type()
)
fsDot11QosOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosOptionImplemented.setStatus("current")


class _FsDot11SpectrumManagementRequired_Type(TruthValue):
    """Custom type fsDot11SpectrumManagementRequired based on TruthValue"""
    defaultValue = 2


_FsDot11SpectrumManagementRequired_Type.__name__ = "TruthValue"
_FsDot11SpectrumManagementRequired_Object = MibTableColumn
fsDot11SpectrumManagementRequired = _FsDot11SpectrumManagementRequired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 9),
    _FsDot11SpectrumManagementRequired_Type()
)
fsDot11SpectrumManagementRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11SpectrumManagementRequired.setStatus("current")


class _FsDot11ShortSlotTimeOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ShortSlotTimeOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ShortSlotTimeOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ShortSlotTimeOptionImplemented_Object = MibTableColumn
fsDot11ShortSlotTimeOptionImplemented = _FsDot11ShortSlotTimeOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 10),
    _FsDot11ShortSlotTimeOptionImplemented_Type()
)
fsDot11ShortSlotTimeOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ShortSlotTimeOptionImplemented.setStatus("current")


class _FsDot11APSDOptionImplemented_Type(TruthValue):
    """Custom type fsDot11APSDOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11APSDOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11APSDOptionImplemented_Object = MibTableColumn
fsDot11APSDOptionImplemented = _FsDot11APSDOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 11),
    _FsDot11APSDOptionImplemented_Type()
)
fsDot11APSDOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11APSDOptionImplemented.setStatus("current")


class _FsDot11DSSSOFDMOptionEnabled_Type(TruthValue):
    """Custom type fsDot11DSSSOFDMOptionEnabled based on TruthValue"""
    defaultValue = 2


_FsDot11DSSSOFDMOptionEnabled_Type.__name__ = "TruthValue"
_FsDot11DSSSOFDMOptionEnabled_Object = MibTableColumn
fsDot11DSSSOFDMOptionEnabled = _FsDot11DSSSOFDMOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 12),
    _FsDot11DSSSOFDMOptionEnabled_Type()
)
fsDot11DSSSOFDMOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DSSSOFDMOptionEnabled.setStatus("current")


class _FsDot11DelayedBlockAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11DelayedBlockAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11DelayedBlockAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11DelayedBlockAckOptionImplemented_Object = MibTableColumn
fsDot11DelayedBlockAckOptionImplemented = _FsDot11DelayedBlockAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 13),
    _FsDot11DelayedBlockAckOptionImplemented_Type()
)
fsDot11DelayedBlockAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DelayedBlockAckOptionImplemented.setStatus("current")


class _FsDot11ImmediateBlockAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ImmediateBlockAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ImmediateBlockAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ImmediateBlockAckOptionImplemented_Object = MibTableColumn
fsDot11ImmediateBlockAckOptionImplemented = _FsDot11ImmediateBlockAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 14),
    _FsDot11ImmediateBlockAckOptionImplemented_Type()
)
fsDot11ImmediateBlockAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ImmediateBlockAckOptionImplemented.setStatus("current")


class _FsDot11QAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11QAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11QAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11QAckOptionImplemented_Object = MibTableColumn
fsDot11QAckOptionImplemented = _FsDot11QAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 15),
    _FsDot11QAckOptionImplemented_Type()
)
fsDot11QAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QAckOptionImplemented.setStatus("current")


class _FsDot11QueueRequestOptionImplemented_Type(TruthValue):
    """Custom type fsDot11QueueRequestOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11QueueRequestOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11QueueRequestOptionImplemented_Object = MibTableColumn
fsDot11QueueRequestOptionImplemented = _FsDot11QueueRequestOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 16),
    _FsDot11QueueRequestOptionImplemented_Type()
)
fsDot11QueueRequestOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QueueRequestOptionImplemented.setStatus("current")


class _FsDot11TXOPRequestOptionImplemented_Type(TruthValue):
    """Custom type fsDot11TXOPRequestOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11TXOPRequestOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11TXOPRequestOptionImplemented_Object = MibTableColumn
fsDot11TXOPRequestOptionImplemented = _FsDot11TXOPRequestOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 17),
    _FsDot11TXOPRequestOptionImplemented_Type()
)
fsDot11TXOPRequestOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11TXOPRequestOptionImplemented.setStatus("current")


class _FsDot11RSNAOptionImplemented_Type(TruthValue):
    """Custom type fsDot11RSNAOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11RSNAOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11RSNAOptionImplemented_Object = MibTableColumn
fsDot11RSNAOptionImplemented = _FsDot11RSNAOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 18),
    _FsDot11RSNAOptionImplemented_Type()
)
fsDot11RSNAOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11RSNAOptionImplemented.setStatus("current")


class _FsDot11RSNAPreauthenticationImplemented_Type(TruthValue):
    """Custom type fsDot11RSNAPreauthenticationImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11RSNAPreauthenticationImplemented_Type.__name__ = "TruthValue"
_FsDot11RSNAPreauthenticationImplemented_Object = MibTableColumn
fsDot11RSNAPreauthenticationImplemented = _FsDot11RSNAPreauthenticationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 19),
    _FsDot11RSNAPreauthenticationImplemented_Type()
)
fsDot11RSNAPreauthenticationImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11RSNAPreauthenticationImplemented.setStatus("current")
_FsDot11CapabilityRowStatus_Type = RowStatus
_FsDot11CapabilityRowStatus_Object = MibTableColumn
fsDot11CapabilityRowStatus = _FsDot11CapabilityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 2, 1, 20),
    _FsDot11CapabilityRowStatus_Type()
)
fsDot11CapabilityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11CapabilityRowStatus.setStatus("current")
_FsDot11AuthenticationProfileTable_Object = MibTable
fsDot11AuthenticationProfileTable = _FsDot11AuthenticationProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3)
)
if mibBuilder.loadTexts:
    fsDot11AuthenticationProfileTable.setStatus("current")
_FsDot11AuthenticationProfileEntry_Object = MibTableRow
fsDot11AuthenticationProfileEntry = _FsDot11AuthenticationProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1)
)
fsDot11AuthenticationProfileEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsDot11AuthenticationProfileName"),
)
if mibBuilder.loadTexts:
    fsDot11AuthenticationProfileEntry.setStatus("current")


class _FsDot11AuthenticationProfileName_Type(OctetString):
    """Custom type fsDot11AuthenticationProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11AuthenticationProfileName_Type.__name__ = "OctetString"
_FsDot11AuthenticationProfileName_Object = MibTableColumn
fsDot11AuthenticationProfileName = _FsDot11AuthenticationProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 1),
    _FsDot11AuthenticationProfileName_Type()
)
fsDot11AuthenticationProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11AuthenticationProfileName.setStatus("current")


class _FsDot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type fsDot11AuthenticationAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_FsDot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_FsDot11AuthenticationAlgorithm_Object = MibTableColumn
fsDot11AuthenticationAlgorithm = _FsDot11AuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 2),
    _FsDot11AuthenticationAlgorithm_Type()
)
fsDot11AuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AuthenticationAlgorithm.setStatus("current")


class _FsDot11WepKeyIndex_Type(Integer32):
    """Custom type fsDot11WepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsDot11WepKeyIndex_Type.__name__ = "Integer32"
_FsDot11WepKeyIndex_Object = MibTableColumn
fsDot11WepKeyIndex = _FsDot11WepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 3),
    _FsDot11WepKeyIndex_Type()
)
fsDot11WepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WepKeyIndex.setStatus("current")


class _FsDot11WepKeyType_Type(Integer32):
    """Custom type fsDot11WepKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_FsDot11WepKeyType_Type.__name__ = "Integer32"
_FsDot11WepKeyType_Object = MibTableColumn
fsDot11WepKeyType = _FsDot11WepKeyType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 4),
    _FsDot11WepKeyType_Type()
)
fsDot11WepKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WepKeyType.setStatus("current")
_FsDot11WepKeyLength_Type = Integer32
_FsDot11WepKeyLength_Object = MibTableColumn
fsDot11WepKeyLength = _FsDot11WepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 5),
    _FsDot11WepKeyLength_Type()
)
fsDot11WepKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WepKeyLength.setStatus("current")


class _FsDot11WepKey_Type(OctetString):
    """Custom type fsDot11WepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(104, 104),
    )
    fixed_length = 104


_FsDot11WepKey_Type.__name__ = "OctetString"
_FsDot11WepKey_Object = MibTableColumn
fsDot11WepKey = _FsDot11WepKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 6),
    _FsDot11WepKey_Type()
)
fsDot11WepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WepKey.setStatus("current")


class _FsDot11WebAuthentication_Type(Integer32):
    """Custom type fsDot11WebAuthentication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsDot11WebAuthentication_Type.__name__ = "Integer32"
_FsDot11WebAuthentication_Object = MibTableColumn
fsDot11WebAuthentication = _FsDot11WebAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 7),
    _FsDot11WebAuthentication_Type()
)
fsDot11WebAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WebAuthentication.setStatus("current")
_FsDot11AuthenticationRowStatus_Type = RowStatus
_FsDot11AuthenticationRowStatus_Object = MibTableColumn
fsDot11AuthenticationRowStatus = _FsDot11AuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 3, 1, 8),
    _FsDot11AuthenticationRowStatus_Type()
)
fsDot11AuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AuthenticationRowStatus.setStatus("current")
_FsSecurityWebAuthGuestInfoTable_Object = MibTable
fsSecurityWebAuthGuestInfoTable = _FsSecurityWebAuthGuestInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4)
)
if mibBuilder.loadTexts:
    fsSecurityWebAuthGuestInfoTable.setStatus("current")
_FsSecurityWebAuthGuestInfoEntry_Object = MibTableRow
fsSecurityWebAuthGuestInfoEntry = _FsSecurityWebAuthGuestInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1)
)
fsSecurityWebAuthGuestInfoEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsSecurityWebAuthUName"),
)
if mibBuilder.loadTexts:
    fsSecurityWebAuthGuestInfoEntry.setStatus("current")


class _FsSecurityWebAuthUName_Type(DisplayString):
    """Custom type fsSecurityWebAuthUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsSecurityWebAuthUName_Type.__name__ = "DisplayString"
_FsSecurityWebAuthUName_Object = MibTableColumn
fsSecurityWebAuthUName = _FsSecurityWebAuthUName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1, 1),
    _FsSecurityWebAuthUName_Type()
)
fsSecurityWebAuthUName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSecurityWebAuthUName.setStatus("current")
_FsSecurityWlanProfileId_Type = Integer32
_FsSecurityWlanProfileId_Object = MibTableColumn
fsSecurityWlanProfileId = _FsSecurityWlanProfileId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1, 2),
    _FsSecurityWlanProfileId_Type()
)
fsSecurityWlanProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWlanProfileId.setStatus("current")
_FsSecurityWebAuthUserLifetime_Type = Integer32
_FsSecurityWebAuthUserLifetime_Object = MibTableColumn
fsSecurityWebAuthUserLifetime = _FsSecurityWebAuthUserLifetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1, 3),
    _FsSecurityWebAuthUserLifetime_Type()
)
fsSecurityWebAuthUserLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthUserLifetime.setStatus("current")
_FsSecurityWebAuthUserEmailId_Type = DisplayString
_FsSecurityWebAuthUserEmailId_Object = MibTableColumn
fsSecurityWebAuthUserEmailId = _FsSecurityWebAuthUserEmailId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1, 4),
    _FsSecurityWebAuthUserEmailId_Type()
)
fsSecurityWebAuthUserEmailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecurityWebAuthUserEmailId.setStatus("current")
_FsSecurityWebAuthGuestInfoRowStatus_Type = RowStatus
_FsSecurityWebAuthGuestInfoRowStatus_Object = MibTableColumn
fsSecurityWebAuthGuestInfoRowStatus = _FsSecurityWebAuthGuestInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 4, 1, 5),
    _FsSecurityWebAuthGuestInfoRowStatus_Type()
)
fsSecurityWebAuthGuestInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecurityWebAuthGuestInfoRowStatus.setStatus("current")
_FsStationQosParamsTable_Object = MibTable
fsStationQosParamsTable = _FsStationQosParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 5)
)
if mibBuilder.loadTexts:
    fsStationQosParamsTable.setStatus("current")
_FsStationQosParamsEntry_Object = MibTableRow
fsStationQosParamsEntry = _FsStationQosParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 5, 1)
)
fsStationQosParamsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-DOT11-MIB", "fsStaMacAddress"),
)
if mibBuilder.loadTexts:
    fsStationQosParamsEntry.setStatus("current")
_FsStaMacAddress_Type = MacAddress
_FsStaMacAddress_Object = MibTableColumn
fsStaMacAddress = _FsStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 5, 1, 1),
    _FsStaMacAddress_Type()
)
fsStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaMacAddress.setStatus("current")
_FsStaQoSPriority_Type = Integer32
_FsStaQoSPriority_Object = MibTableColumn
fsStaQoSPriority = _FsStaQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 5, 1, 2),
    _FsStaQoSPriority_Type()
)
fsStaQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStaQoSPriority.setStatus("current")
_FsStaQoSDscp_Type = Integer32
_FsStaQoSDscp_Object = MibTableColumn
fsStaQoSDscp = _FsStaQoSDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 5, 1, 3),
    _FsStaQoSDscp_Type()
)
fsStaQoSDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStaQoSDscp.setStatus("current")
_FsVlanIsolationTable_Object = MibTable
fsVlanIsolationTable = _FsVlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 6)
)
if mibBuilder.loadTexts:
    fsVlanIsolationTable.setStatus("current")
_FsVlanIsolationEntry_Object = MibTableRow
fsVlanIsolationEntry = _FsVlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 6, 1)
)
fsVlanIsolationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsVlanIsolationEntry.setStatus("current")


class _FsVlanIsolation_Type(Integer32):
    """Custom type fsVlanIsolation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsVlanIsolation_Type.__name__ = "Integer32"
_FsVlanIsolation_Object = MibTableColumn
fsVlanIsolation = _FsVlanIsolation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 6, 1, 1),
    _FsVlanIsolation_Type()
)
fsVlanIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanIsolation.setStatus("current")
_FsDot11RadioConfigTable_Object = MibTable
fsDot11RadioConfigTable = _FsDot11RadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7)
)
if mibBuilder.loadTexts:
    fsDot11RadioConfigTable.setStatus("current")
_FsDot11RadioConfigEntry_Object = MibTableRow
fsDot11RadioConfigEntry = _FsDot11RadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1)
)
fsDot11RadioConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11RadioConfigEntry.setStatus("current")


class _FsDot11RadioType_Type(Integer32):
    """Custom type fsDot11RadioType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11a", 2),
          ("dot11g", 4),
          ("dot11bg", 5),
          ("dot11an", 10),
          ("dot11bgn", 13))
    )


_FsDot11RadioType_Type.__name__ = "Integer32"
_FsDot11RadioType_Object = MibTableColumn
fsDot11RadioType = _FsDot11RadioType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1, 1),
    _FsDot11RadioType_Type()
)
fsDot11RadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11RadioType.setStatus("current")


class _FsDot11RadioNoOfBssIdSupported_Type(Integer32):
    """Custom type fsDot11RadioNoOfBssIdSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsDot11RadioNoOfBssIdSupported_Type.__name__ = "Integer32"
_FsDot11RadioNoOfBssIdSupported_Object = MibTableColumn
fsDot11RadioNoOfBssIdSupported = _FsDot11RadioNoOfBssIdSupported_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1, 2),
    _FsDot11RadioNoOfBssIdSupported_Type()
)
fsDot11RadioNoOfBssIdSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11RadioNoOfBssIdSupported.setStatus("current")


class _FsDot11RadioAntennaType_Type(Integer32):
    """Custom type fsDot11RadioAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmitter", 1),
          ("receiver", 2))
    )


_FsDot11RadioAntennaType_Type.__name__ = "Integer32"
_FsDot11RadioAntennaType_Object = MibTableColumn
fsDot11RadioAntennaType = _FsDot11RadioAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1, 3),
    _FsDot11RadioAntennaType_Type()
)
fsDot11RadioAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11RadioAntennaType.setStatus("current")


class _FsDot11RadioFailureStatus_Type(Integer32):
    """Custom type fsDot11RadioFailureStatus based on Integer32"""
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


_FsDot11RadioFailureStatus_Type.__name__ = "Integer32"
_FsDot11RadioFailureStatus_Object = MibTableColumn
fsDot11RadioFailureStatus = _FsDot11RadioFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1, 4),
    _FsDot11RadioFailureStatus_Type()
)
fsDot11RadioFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11RadioFailureStatus.setStatus("current")
_FsDot11RowStatus_Type = RowStatus
_FsDot11RowStatus_Object = MibTableColumn
fsDot11RowStatus = _FsDot11RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 7, 1, 15),
    _FsDot11RowStatus_Type()
)
fsDot11RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11RowStatus.setStatus("current")
_FsDot11QosProfileTable_Object = MibTable
fsDot11QosProfileTable = _FsDot11QosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8)
)
if mibBuilder.loadTexts:
    fsDot11QosProfileTable.setStatus("current")
_FsDot11QosProfileEntry_Object = MibTableRow
fsDot11QosProfileEntry = _FsDot11QosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1)
)
fsDot11QosProfileEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsDot11QosProfileName"),
)
if mibBuilder.loadTexts:
    fsDot11QosProfileEntry.setStatus("current")


class _FsDot11QosProfileName_Type(OctetString):
    """Custom type fsDot11QosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11QosProfileName_Type.__name__ = "OctetString"
_FsDot11QosProfileName_Object = MibTableColumn
fsDot11QosProfileName = _FsDot11QosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 1),
    _FsDot11QosProfileName_Type()
)
fsDot11QosProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11QosProfileName.setStatus("current")


class _FsDot11QosTraffic_Type(Integer32):
    """Custom type fsDot11QosTraffic based on Integer32"""
    defaultValue = 1

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
        *(("bestEffort", 1),
          ("video", 2),
          ("voice", 3),
          ("background", 4))
    )


_FsDot11QosTraffic_Type.__name__ = "Integer32"
_FsDot11QosTraffic_Object = MibTableColumn
fsDot11QosTraffic = _FsDot11QosTraffic_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 2),
    _FsDot11QosTraffic_Type()
)
fsDot11QosTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosTraffic.setStatus("current")


class _FsDot11QosPassengerTrustMode_Type(Integer32):
    """Custom type fsDot11QosPassengerTrustMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsDot11QosPassengerTrustMode_Type.__name__ = "Integer32"
_FsDot11QosPassengerTrustMode_Object = MibTableColumn
fsDot11QosPassengerTrustMode = _FsDot11QosPassengerTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 3),
    _FsDot11QosPassengerTrustMode_Type()
)
fsDot11QosPassengerTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosPassengerTrustMode.setStatus("current")


class _FsDot11QosRateLimit_Type(Integer32):
    """Custom type fsDot11QosRateLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsDot11QosRateLimit_Type.__name__ = "Integer32"
_FsDot11QosRateLimit_Object = MibTableColumn
fsDot11QosRateLimit = _FsDot11QosRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 4),
    _FsDot11QosRateLimit_Type()
)
fsDot11QosRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosRateLimit.setStatus("current")


class _FsDot11UpStreamCIR_Type(Integer32):
    """Custom type fsDot11UpStreamCIR based on Integer32"""
    defaultValue = 100


_FsDot11UpStreamCIR_Type.__name__ = "Integer32"
_FsDot11UpStreamCIR_Object = MibTableColumn
fsDot11UpStreamCIR = _FsDot11UpStreamCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 5),
    _FsDot11UpStreamCIR_Type()
)
fsDot11UpStreamCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11UpStreamCIR.setStatus("current")


class _FsDot11UpStreamCBS_Type(Integer32):
    """Custom type fsDot11UpStreamCBS based on Integer32"""
    defaultValue = 1000


_FsDot11UpStreamCBS_Type.__name__ = "Integer32"
_FsDot11UpStreamCBS_Object = MibTableColumn
fsDot11UpStreamCBS = _FsDot11UpStreamCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 6),
    _FsDot11UpStreamCBS_Type()
)
fsDot11UpStreamCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11UpStreamCBS.setStatus("current")


class _FsDot11UpStreamEIR_Type(Integer32):
    """Custom type fsDot11UpStreamEIR based on Integer32"""
    defaultValue = 15000


_FsDot11UpStreamEIR_Type.__name__ = "Integer32"
_FsDot11UpStreamEIR_Object = MibTableColumn
fsDot11UpStreamEIR = _FsDot11UpStreamEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 7),
    _FsDot11UpStreamEIR_Type()
)
fsDot11UpStreamEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11UpStreamEIR.setStatus("current")


class _FsDot11UpStreamEBS_Type(Integer32):
    """Custom type fsDot11UpStreamEBS based on Integer32"""
    defaultValue = 15000


_FsDot11UpStreamEBS_Type.__name__ = "Integer32"
_FsDot11UpStreamEBS_Object = MibTableColumn
fsDot11UpStreamEBS = _FsDot11UpStreamEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 8),
    _FsDot11UpStreamEBS_Type()
)
fsDot11UpStreamEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11UpStreamEBS.setStatus("current")


class _FsDot11DownStreamCIR_Type(Integer32):
    """Custom type fsDot11DownStreamCIR based on Integer32"""
    defaultValue = 100


_FsDot11DownStreamCIR_Type.__name__ = "Integer32"
_FsDot11DownStreamCIR_Object = MibTableColumn
fsDot11DownStreamCIR = _FsDot11DownStreamCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 9),
    _FsDot11DownStreamCIR_Type()
)
fsDot11DownStreamCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DownStreamCIR.setStatus("current")


class _FsDot11DownStreamCBS_Type(Integer32):
    """Custom type fsDot11DownStreamCBS based on Integer32"""
    defaultValue = 1000


_FsDot11DownStreamCBS_Type.__name__ = "Integer32"
_FsDot11DownStreamCBS_Object = MibTableColumn
fsDot11DownStreamCBS = _FsDot11DownStreamCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 10),
    _FsDot11DownStreamCBS_Type()
)
fsDot11DownStreamCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DownStreamCBS.setStatus("current")


class _FsDot11DownStreamEIR_Type(Integer32):
    """Custom type fsDot11DownStreamEIR based on Integer32"""
    defaultValue = 15000


_FsDot11DownStreamEIR_Type.__name__ = "Integer32"
_FsDot11DownStreamEIR_Object = MibTableColumn
fsDot11DownStreamEIR = _FsDot11DownStreamEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 11),
    _FsDot11DownStreamEIR_Type()
)
fsDot11DownStreamEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DownStreamEIR.setStatus("current")


class _FsDot11DownStreamEBS_Type(Integer32):
    """Custom type fsDot11DownStreamEBS based on Integer32"""
    defaultValue = 15000


_FsDot11DownStreamEBS_Type.__name__ = "Integer32"
_FsDot11DownStreamEBS_Object = MibTableColumn
fsDot11DownStreamEBS = _FsDot11DownStreamEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 12),
    _FsDot11DownStreamEBS_Type()
)
fsDot11DownStreamEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DownStreamEBS.setStatus("current")
_FsDot11QosRowStatus_Type = RowStatus
_FsDot11QosRowStatus_Object = MibTableColumn
fsDot11QosRowStatus = _FsDot11QosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 8, 1, 13),
    _FsDot11QosRowStatus_Type()
)
fsDot11QosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosRowStatus.setStatus("current")
_FsDot11WlanCapabilityProfileTable_Object = MibTable
fsDot11WlanCapabilityProfileTable = _FsDot11WlanCapabilityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9)
)
if mibBuilder.loadTexts:
    fsDot11WlanCapabilityProfileTable.setStatus("current")
_FsDot11WlanCapabilityProfileEntry_Object = MibTableRow
fsDot11WlanCapabilityProfileEntry = _FsDot11WlanCapabilityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1)
)
fsDot11WlanCapabilityProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11WlanCapabilityProfileEntry.setStatus("current")


class _FsDot11WlanCFPollable_Type(TruthValue):
    """Custom type fsDot11WlanCFPollable based on TruthValue"""
    defaultValue = 2


_FsDot11WlanCFPollable_Type.__name__ = "TruthValue"
_FsDot11WlanCFPollable_Object = MibTableColumn
fsDot11WlanCFPollable = _FsDot11WlanCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 1),
    _FsDot11WlanCFPollable_Type()
)
fsDot11WlanCFPollable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanCFPollable.setStatus("current")


class _FsDot11WlanCFPollRequest_Type(TruthValue):
    """Custom type fsDot11WlanCFPollRequest based on TruthValue"""
    defaultValue = 2


_FsDot11WlanCFPollRequest_Type.__name__ = "TruthValue"
_FsDot11WlanCFPollRequest_Object = MibTableColumn
fsDot11WlanCFPollRequest = _FsDot11WlanCFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 2),
    _FsDot11WlanCFPollRequest_Type()
)
fsDot11WlanCFPollRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanCFPollRequest.setStatus("current")


class _FsDot11WlanPrivacyOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanPrivacyOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanPrivacyOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanPrivacyOptionImplemented_Object = MibTableColumn
fsDot11WlanPrivacyOptionImplemented = _FsDot11WlanPrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 3),
    _FsDot11WlanPrivacyOptionImplemented_Type()
)
fsDot11WlanPrivacyOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanPrivacyOptionImplemented.setStatus("current")


class _FsDot11WlanShortPreambleOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanShortPreambleOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanShortPreambleOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanShortPreambleOptionImplemented_Object = MibTableColumn
fsDot11WlanShortPreambleOptionImplemented = _FsDot11WlanShortPreambleOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 4),
    _FsDot11WlanShortPreambleOptionImplemented_Type()
)
fsDot11WlanShortPreambleOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanShortPreambleOptionImplemented.setStatus("current")


class _FsDot11WlanPBCCOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanPBCCOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanPBCCOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanPBCCOptionImplemented_Object = MibTableColumn
fsDot11WlanPBCCOptionImplemented = _FsDot11WlanPBCCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 5),
    _FsDot11WlanPBCCOptionImplemented_Type()
)
fsDot11WlanPBCCOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanPBCCOptionImplemented.setStatus("current")


class _FsDot11WlanChannelAgilityPresent_Type(TruthValue):
    """Custom type fsDot11WlanChannelAgilityPresent based on TruthValue"""
    defaultValue = 2


_FsDot11WlanChannelAgilityPresent_Type.__name__ = "TruthValue"
_FsDot11WlanChannelAgilityPresent_Object = MibTableColumn
fsDot11WlanChannelAgilityPresent = _FsDot11WlanChannelAgilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 6),
    _FsDot11WlanChannelAgilityPresent_Type()
)
fsDot11WlanChannelAgilityPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanChannelAgilityPresent.setStatus("current")


class _FsDot11WlanQosOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanQosOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanQosOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanQosOptionImplemented_Object = MibTableColumn
fsDot11WlanQosOptionImplemented = _FsDot11WlanQosOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 7),
    _FsDot11WlanQosOptionImplemented_Type()
)
fsDot11WlanQosOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQosOptionImplemented.setStatus("current")


class _FsDot11WlanSpectrumManagementRequired_Type(TruthValue):
    """Custom type fsDot11WlanSpectrumManagementRequired based on TruthValue"""
    defaultValue = 2


_FsDot11WlanSpectrumManagementRequired_Type.__name__ = "TruthValue"
_FsDot11WlanSpectrumManagementRequired_Object = MibTableColumn
fsDot11WlanSpectrumManagementRequired = _FsDot11WlanSpectrumManagementRequired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 8),
    _FsDot11WlanSpectrumManagementRequired_Type()
)
fsDot11WlanSpectrumManagementRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanSpectrumManagementRequired.setStatus("current")


class _FsDot11WlanShortSlotTimeOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanShortSlotTimeOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanShortSlotTimeOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanShortSlotTimeOptionImplemented_Object = MibTableColumn
fsDot11WlanShortSlotTimeOptionImplemented = _FsDot11WlanShortSlotTimeOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 9),
    _FsDot11WlanShortSlotTimeOptionImplemented_Type()
)
fsDot11WlanShortSlotTimeOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanShortSlotTimeOptionImplemented.setStatus("current")


class _FsDot11WlanAPSDOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanAPSDOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanAPSDOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanAPSDOptionImplemented_Object = MibTableColumn
fsDot11WlanAPSDOptionImplemented = _FsDot11WlanAPSDOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 10),
    _FsDot11WlanAPSDOptionImplemented_Type()
)
fsDot11WlanAPSDOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanAPSDOptionImplemented.setStatus("current")


class _FsDot11WlanDSSSOFDMOptionEnabled_Type(TruthValue):
    """Custom type fsDot11WlanDSSSOFDMOptionEnabled based on TruthValue"""
    defaultValue = 2


_FsDot11WlanDSSSOFDMOptionEnabled_Type.__name__ = "TruthValue"
_FsDot11WlanDSSSOFDMOptionEnabled_Object = MibTableColumn
fsDot11WlanDSSSOFDMOptionEnabled = _FsDot11WlanDSSSOFDMOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 11),
    _FsDot11WlanDSSSOFDMOptionEnabled_Type()
)
fsDot11WlanDSSSOFDMOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDSSSOFDMOptionEnabled.setStatus("current")


class _FsDot11WlanDelayedBlockAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanDelayedBlockAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanDelayedBlockAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanDelayedBlockAckOptionImplemented_Object = MibTableColumn
fsDot11WlanDelayedBlockAckOptionImplemented = _FsDot11WlanDelayedBlockAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 12),
    _FsDot11WlanDelayedBlockAckOptionImplemented_Type()
)
fsDot11WlanDelayedBlockAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDelayedBlockAckOptionImplemented.setStatus("current")


class _FsDot11WlanImmediateBlockAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanImmediateBlockAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanImmediateBlockAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanImmediateBlockAckOptionImplemented_Object = MibTableColumn
fsDot11WlanImmediateBlockAckOptionImplemented = _FsDot11WlanImmediateBlockAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 13),
    _FsDot11WlanImmediateBlockAckOptionImplemented_Type()
)
fsDot11WlanImmediateBlockAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanImmediateBlockAckOptionImplemented.setStatus("current")


class _FsDot11WlanQAckOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanQAckOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanQAckOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanQAckOptionImplemented_Object = MibTableColumn
fsDot11WlanQAckOptionImplemented = _FsDot11WlanQAckOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 14),
    _FsDot11WlanQAckOptionImplemented_Type()
)
fsDot11WlanQAckOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQAckOptionImplemented.setStatus("current")


class _FsDot11WlanQueueRequestOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanQueueRequestOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanQueueRequestOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanQueueRequestOptionImplemented_Object = MibTableColumn
fsDot11WlanQueueRequestOptionImplemented = _FsDot11WlanQueueRequestOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 15),
    _FsDot11WlanQueueRequestOptionImplemented_Type()
)
fsDot11WlanQueueRequestOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQueueRequestOptionImplemented.setStatus("current")


class _FsDot11WlanTXOPRequestOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanTXOPRequestOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanTXOPRequestOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanTXOPRequestOptionImplemented_Object = MibTableColumn
fsDot11WlanTXOPRequestOptionImplemented = _FsDot11WlanTXOPRequestOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 16),
    _FsDot11WlanTXOPRequestOptionImplemented_Type()
)
fsDot11WlanTXOPRequestOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanTXOPRequestOptionImplemented.setStatus("current")


class _FsDot11WlanRSNAOptionImplemented_Type(TruthValue):
    """Custom type fsDot11WlanRSNAOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanRSNAOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanRSNAOptionImplemented_Object = MibTableColumn
fsDot11WlanRSNAOptionImplemented = _FsDot11WlanRSNAOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 17),
    _FsDot11WlanRSNAOptionImplemented_Type()
)
fsDot11WlanRSNAOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanRSNAOptionImplemented.setStatus("current")


class _FsDot11WlanRSNAPreauthenticationImplemented_Type(TruthValue):
    """Custom type fsDot11WlanRSNAPreauthenticationImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11WlanRSNAPreauthenticationImplemented_Type.__name__ = "TruthValue"
_FsDot11WlanRSNAPreauthenticationImplemented_Object = MibTableColumn
fsDot11WlanRSNAPreauthenticationImplemented = _FsDot11WlanRSNAPreauthenticationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 18),
    _FsDot11WlanRSNAPreauthenticationImplemented_Type()
)
fsDot11WlanRSNAPreauthenticationImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanRSNAPreauthenticationImplemented.setStatus("current")
_FsDot11WlanCapabilityRowStatus_Type = RowStatus
_FsDot11WlanCapabilityRowStatus_Object = MibTableColumn
fsDot11WlanCapabilityRowStatus = _FsDot11WlanCapabilityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 9, 1, 19),
    _FsDot11WlanCapabilityRowStatus_Type()
)
fsDot11WlanCapabilityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanCapabilityRowStatus.setStatus("current")
_FsDot11WlanAuthenticationProfileTable_Object = MibTable
fsDot11WlanAuthenticationProfileTable = _FsDot11WlanAuthenticationProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10)
)
if mibBuilder.loadTexts:
    fsDot11WlanAuthenticationProfileTable.setStatus("current")
_FsDot11WlanAuthenticationProfileEntry_Object = MibTableRow
fsDot11WlanAuthenticationProfileEntry = _FsDot11WlanAuthenticationProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1)
)
fsDot11WlanAuthenticationProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11WlanAuthenticationProfileEntry.setStatus("current")


class _FsDot11WlanAuthenticationAlgorithm_Type(Integer32):
    """Custom type fsDot11WlanAuthenticationAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2),
          ("webAuth", 3))
    )


_FsDot11WlanAuthenticationAlgorithm_Type.__name__ = "Integer32"
_FsDot11WlanAuthenticationAlgorithm_Object = MibTableColumn
fsDot11WlanAuthenticationAlgorithm = _FsDot11WlanAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 1),
    _FsDot11WlanAuthenticationAlgorithm_Type()
)
fsDot11WlanAuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanAuthenticationAlgorithm.setStatus("current")


class _FsDot11WlanWepKeyIndex_Type(Integer32):
    """Custom type fsDot11WlanWepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsDot11WlanWepKeyIndex_Type.__name__ = "Integer32"
_FsDot11WlanWepKeyIndex_Object = MibTableColumn
fsDot11WlanWepKeyIndex = _FsDot11WlanWepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 2),
    _FsDot11WlanWepKeyIndex_Type()
)
fsDot11WlanWepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanWepKeyIndex.setStatus("current")


class _FsDot11WlanWepKeyType_Type(Integer32):
    """Custom type fsDot11WlanWepKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_FsDot11WlanWepKeyType_Type.__name__ = "Integer32"
_FsDot11WlanWepKeyType_Object = MibTableColumn
fsDot11WlanWepKeyType = _FsDot11WlanWepKeyType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 3),
    _FsDot11WlanWepKeyType_Type()
)
fsDot11WlanWepKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanWepKeyType.setStatus("current")
_FsDot11WlanWepKeyLength_Type = Integer32
_FsDot11WlanWepKeyLength_Object = MibTableColumn
fsDot11WlanWepKeyLength = _FsDot11WlanWepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 4),
    _FsDot11WlanWepKeyLength_Type()
)
fsDot11WlanWepKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanWepKeyLength.setStatus("current")


class _FsDot11WlanWepKey_Type(OctetString):
    """Custom type fsDot11WlanWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(104, 104),
    )
    fixed_length = 104


_FsDot11WlanWepKey_Type.__name__ = "OctetString"
_FsDot11WlanWepKey_Object = MibTableColumn
fsDot11WlanWepKey = _FsDot11WlanWepKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 5),
    _FsDot11WlanWepKey_Type()
)
fsDot11WlanWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanWepKey.setStatus("current")


class _FsDot11WlanWebAuthentication_Type(Integer32):
    """Custom type fsDot11WlanWebAuthentication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsDot11WlanWebAuthentication_Type.__name__ = "Integer32"
_FsDot11WlanWebAuthentication_Object = MibTableColumn
fsDot11WlanWebAuthentication = _FsDot11WlanWebAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 6),
    _FsDot11WlanWebAuthentication_Type()
)
fsDot11WlanWebAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanWebAuthentication.setStatus("current")
_FsDot11WlanAuthenticationRowStatus_Type = RowStatus
_FsDot11WlanAuthenticationRowStatus_Object = MibTableColumn
fsDot11WlanAuthenticationRowStatus = _FsDot11WlanAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 10, 1, 7),
    _FsDot11WlanAuthenticationRowStatus_Type()
)
fsDot11WlanAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanAuthenticationRowStatus.setStatus("current")
_FsDot11WlanQosProfileTable_Object = MibTable
fsDot11WlanQosProfileTable = _FsDot11WlanQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11)
)
if mibBuilder.loadTexts:
    fsDot11WlanQosProfileTable.setStatus("current")
_FsDot11WlanQosProfileEntry_Object = MibTableRow
fsDot11WlanQosProfileEntry = _FsDot11WlanQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1)
)
fsDot11WlanQosProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11WlanQosProfileEntry.setStatus("current")


class _FsDot11WlanQosTraffic_Type(Integer32):
    """Custom type fsDot11WlanQosTraffic based on Integer32"""
    defaultValue = 1

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
        *(("bestEffort", 1),
          ("video", 2),
          ("voice", 3),
          ("background", 4))
    )


_FsDot11WlanQosTraffic_Type.__name__ = "Integer32"
_FsDot11WlanQosTraffic_Object = MibTableColumn
fsDot11WlanQosTraffic = _FsDot11WlanQosTraffic_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 1),
    _FsDot11WlanQosTraffic_Type()
)
fsDot11WlanQosTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQosTraffic.setStatus("current")


class _FsDot11WlanQosPassengerTrustMode_Type(Integer32):
    """Custom type fsDot11WlanQosPassengerTrustMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsDot11WlanQosPassengerTrustMode_Type.__name__ = "Integer32"
_FsDot11WlanQosPassengerTrustMode_Object = MibTableColumn
fsDot11WlanQosPassengerTrustMode = _FsDot11WlanQosPassengerTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 2),
    _FsDot11WlanQosPassengerTrustMode_Type()
)
fsDot11WlanQosPassengerTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQosPassengerTrustMode.setStatus("current")


class _FsDot11WlanQosRateLimit_Type(Integer32):
    """Custom type fsDot11WlanQosRateLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsDot11WlanQosRateLimit_Type.__name__ = "Integer32"
_FsDot11WlanQosRateLimit_Object = MibTableColumn
fsDot11WlanQosRateLimit = _FsDot11WlanQosRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 3),
    _FsDot11WlanQosRateLimit_Type()
)
fsDot11WlanQosRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQosRateLimit.setStatus("current")


class _FsDot11WlanUpStreamCIR_Type(Integer32):
    """Custom type fsDot11WlanUpStreamCIR based on Integer32"""
    defaultValue = 100


_FsDot11WlanUpStreamCIR_Type.__name__ = "Integer32"
_FsDot11WlanUpStreamCIR_Object = MibTableColumn
fsDot11WlanUpStreamCIR = _FsDot11WlanUpStreamCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 4),
    _FsDot11WlanUpStreamCIR_Type()
)
fsDot11WlanUpStreamCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanUpStreamCIR.setStatus("current")


class _FsDot11WlanUpStreamCBS_Type(Integer32):
    """Custom type fsDot11WlanUpStreamCBS based on Integer32"""
    defaultValue = 1000


_FsDot11WlanUpStreamCBS_Type.__name__ = "Integer32"
_FsDot11WlanUpStreamCBS_Object = MibTableColumn
fsDot11WlanUpStreamCBS = _FsDot11WlanUpStreamCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 5),
    _FsDot11WlanUpStreamCBS_Type()
)
fsDot11WlanUpStreamCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanUpStreamCBS.setStatus("current")


class _FsDot11WlanUpStreamEIR_Type(Integer32):
    """Custom type fsDot11WlanUpStreamEIR based on Integer32"""
    defaultValue = 15000


_FsDot11WlanUpStreamEIR_Type.__name__ = "Integer32"
_FsDot11WlanUpStreamEIR_Object = MibTableColumn
fsDot11WlanUpStreamEIR = _FsDot11WlanUpStreamEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 6),
    _FsDot11WlanUpStreamEIR_Type()
)
fsDot11WlanUpStreamEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanUpStreamEIR.setStatus("current")


class _FsDot11WlanUpStreamEBS_Type(Integer32):
    """Custom type fsDot11WlanUpStreamEBS based on Integer32"""
    defaultValue = 15000


_FsDot11WlanUpStreamEBS_Type.__name__ = "Integer32"
_FsDot11WlanUpStreamEBS_Object = MibTableColumn
fsDot11WlanUpStreamEBS = _FsDot11WlanUpStreamEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 7),
    _FsDot11WlanUpStreamEBS_Type()
)
fsDot11WlanUpStreamEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanUpStreamEBS.setStatus("current")


class _FsDot11WlanDownStreamCIR_Type(Integer32):
    """Custom type fsDot11WlanDownStreamCIR based on Integer32"""
    defaultValue = 100


_FsDot11WlanDownStreamCIR_Type.__name__ = "Integer32"
_FsDot11WlanDownStreamCIR_Object = MibTableColumn
fsDot11WlanDownStreamCIR = _FsDot11WlanDownStreamCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 8),
    _FsDot11WlanDownStreamCIR_Type()
)
fsDot11WlanDownStreamCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDownStreamCIR.setStatus("current")


class _FsDot11WlanDownStreamCBS_Type(Integer32):
    """Custom type fsDot11WlanDownStreamCBS based on Integer32"""
    defaultValue = 1000


_FsDot11WlanDownStreamCBS_Type.__name__ = "Integer32"
_FsDot11WlanDownStreamCBS_Object = MibTableColumn
fsDot11WlanDownStreamCBS = _FsDot11WlanDownStreamCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 9),
    _FsDot11WlanDownStreamCBS_Type()
)
fsDot11WlanDownStreamCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDownStreamCBS.setStatus("current")


class _FsDot11WlanDownStreamEIR_Type(Integer32):
    """Custom type fsDot11WlanDownStreamEIR based on Integer32"""
    defaultValue = 15000


_FsDot11WlanDownStreamEIR_Type.__name__ = "Integer32"
_FsDot11WlanDownStreamEIR_Object = MibTableColumn
fsDot11WlanDownStreamEIR = _FsDot11WlanDownStreamEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 10),
    _FsDot11WlanDownStreamEIR_Type()
)
fsDot11WlanDownStreamEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDownStreamEIR.setStatus("current")


class _FsDot11WlanDownStreamEBS_Type(Integer32):
    """Custom type fsDot11WlanDownStreamEBS based on Integer32"""
    defaultValue = 15000


_FsDot11WlanDownStreamEBS_Type.__name__ = "Integer32"
_FsDot11WlanDownStreamEBS_Object = MibTableColumn
fsDot11WlanDownStreamEBS = _FsDot11WlanDownStreamEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 11),
    _FsDot11WlanDownStreamEBS_Type()
)
fsDot11WlanDownStreamEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanDownStreamEBS.setStatus("current")
_FsDot11WlanQosRowStatus_Type = RowStatus
_FsDot11WlanQosRowStatus_Object = MibTableColumn
fsDot11WlanQosRowStatus = _FsDot11WlanQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 11, 1, 12),
    _FsDot11WlanQosRowStatus_Type()
)
fsDot11WlanQosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanQosRowStatus.setStatus("current")
_FsDot11CapabilityMappingTable_Object = MibTable
fsDot11CapabilityMappingTable = _FsDot11CapabilityMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 12)
)
if mibBuilder.loadTexts:
    fsDot11CapabilityMappingTable.setStatus("current")
_FsDot11CapabilityMappingEntry_Object = MibTableRow
fsDot11CapabilityMappingEntry = _FsDot11CapabilityMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 12, 1)
)
fsDot11CapabilityMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11CapabilityMappingEntry.setStatus("current")


class _FsDot11CapabilityMappingProfileName_Type(OctetString):
    """Custom type fsDot11CapabilityMappingProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11CapabilityMappingProfileName_Type.__name__ = "OctetString"
_FsDot11CapabilityMappingProfileName_Object = MibTableColumn
fsDot11CapabilityMappingProfileName = _FsDot11CapabilityMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 12, 1, 1),
    _FsDot11CapabilityMappingProfileName_Type()
)
fsDot11CapabilityMappingProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11CapabilityMappingProfileName.setStatus("current")
_FsDot11CapabilityMappingRowStatus_Type = RowStatus
_FsDot11CapabilityMappingRowStatus_Object = MibTableColumn
fsDot11CapabilityMappingRowStatus = _FsDot11CapabilityMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 12, 1, 2),
    _FsDot11CapabilityMappingRowStatus_Type()
)
fsDot11CapabilityMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11CapabilityMappingRowStatus.setStatus("current")
_FsDot11AuthMappingTable_Object = MibTable
fsDot11AuthMappingTable = _FsDot11AuthMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 13)
)
if mibBuilder.loadTexts:
    fsDot11AuthMappingTable.setStatus("current")
_FsDot11AuthMappingEntry_Object = MibTableRow
fsDot11AuthMappingEntry = _FsDot11AuthMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 13, 1)
)
fsDot11AuthMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11AuthMappingEntry.setStatus("current")


class _FsDot11AuthMappingProfileName_Type(OctetString):
    """Custom type fsDot11AuthMappingProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11AuthMappingProfileName_Type.__name__ = "OctetString"
_FsDot11AuthMappingProfileName_Object = MibTableColumn
fsDot11AuthMappingProfileName = _FsDot11AuthMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 13, 1, 1),
    _FsDot11AuthMappingProfileName_Type()
)
fsDot11AuthMappingProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AuthMappingProfileName.setStatus("current")
_FsDot11AuthMappingRowStatus_Type = RowStatus
_FsDot11AuthMappingRowStatus_Object = MibTableColumn
fsDot11AuthMappingRowStatus = _FsDot11AuthMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 13, 1, 2),
    _FsDot11AuthMappingRowStatus_Type()
)
fsDot11AuthMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AuthMappingRowStatus.setStatus("current")
_FsDot11QosMappingTable_Object = MibTable
fsDot11QosMappingTable = _FsDot11QosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 14)
)
if mibBuilder.loadTexts:
    fsDot11QosMappingTable.setStatus("current")
_FsDot11QosMappingEntry_Object = MibTableRow
fsDot11QosMappingEntry = _FsDot11QosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 14, 1)
)
fsDot11QosMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11QosMappingEntry.setStatus("current")


class _FsDot11QosMappingProfileName_Type(OctetString):
    """Custom type fsDot11QosMappingProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot11QosMappingProfileName_Type.__name__ = "OctetString"
_FsDot11QosMappingProfileName_Object = MibTableColumn
fsDot11QosMappingProfileName = _FsDot11QosMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 14, 1, 1),
    _FsDot11QosMappingProfileName_Type()
)
fsDot11QosMappingProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosMappingProfileName.setStatus("current")
_FsDot11QosMappingRowStatus_Type = RowStatus
_FsDot11QosMappingRowStatus_Object = MibTableColumn
fsDot11QosMappingRowStatus = _FsDot11QosMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 14, 1, 2),
    _FsDot11QosMappingRowStatus_Type()
)
fsDot11QosMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11QosMappingRowStatus.setStatus("current")
_FsDot11ClientSummaryTable_Object = MibTable
fsDot11ClientSummaryTable = _FsDot11ClientSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15)
)
if mibBuilder.loadTexts:
    fsDot11ClientSummaryTable.setStatus("current")
_FsDot11ClientSummaryEntry_Object = MibTableRow
fsDot11ClientSummaryEntry = _FsDot11ClientSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1)
)
fsDot11ClientSummaryEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsDot11ClientMacAddress"),
)
if mibBuilder.loadTexts:
    fsDot11ClientSummaryEntry.setStatus("current")
_FsDot11ClientMacAddress_Type = MacAddress
_FsDot11ClientMacAddress_Object = MibTableColumn
fsDot11ClientMacAddress = _FsDot11ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 1),
    _FsDot11ClientMacAddress_Type()
)
fsDot11ClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11ClientMacAddress.setStatus("current")
_FsDot11WlanProfileId_Type = CapwapDot11WlanIdProfileTC
_FsDot11WlanProfileId_Object = MibTableColumn
fsDot11WlanProfileId = _FsDot11WlanProfileId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 2),
    _FsDot11WlanProfileId_Type()
)
fsDot11WlanProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WlanProfileId.setStatus("current")
_FsDot11WtpProfileName_Type = SnmpAdminString
_FsDot11WtpProfileName_Object = MibTableColumn
fsDot11WtpProfileName = _FsDot11WtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 3),
    _FsDot11WtpProfileName_Type()
)
fsDot11WtpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WtpProfileName.setStatus("current")
_FsDot11WtpRadioId_Type = CapwapBaseRadioIdTC
_FsDot11WtpRadioId_Object = MibTableColumn
fsDot11WtpRadioId = _FsDot11WtpRadioId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 4),
    _FsDot11WtpRadioId_Type()
)
fsDot11WtpRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WtpRadioId.setStatus("current")
_FsDot11AuthStatus_Type = TruthValue
_FsDot11AuthStatus_Object = MibTableColumn
fsDot11AuthStatus = _FsDot11AuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 5),
    _FsDot11AuthStatus_Type()
)
fsDot11AuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11AuthStatus.setStatus("current")
_FsDot11AssocStatus_Type = TruthValue
_FsDot11AssocStatus_Object = MibTableColumn
fsDot11AssocStatus = _FsDot11AssocStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 3, 15, 1, 6),
    _FsDot11AssocStatus_Type()
)
fsDot11AssocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11AssocStatus.setStatus("current")
_FsDot11mac_ObjectIdentity = ObjectIdentity
fsDot11mac = _FsDot11mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4)
)
_FsDot11RadioQosTable_Object = MibTable
fsDot11RadioQosTable = _FsDot11RadioQosTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 1)
)
if mibBuilder.loadTexts:
    fsDot11RadioQosTable.setStatus("current")
_FsDot11RadioQosEntry_Object = MibTableRow
fsDot11RadioQosEntry = _FsDot11RadioQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 1, 1)
)
fsDot11RadioQosEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11RadioQosEntry.setStatus("current")


class _FsDot11TaggingPolicy_Type(Bits):
    """Custom type fsDot11TaggingPolicy based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("dot1p", 0),
          ("dot1q", 1),
          ("dscp", 2),
          ("outerHeader", 3),
          ("innerHeader", 4))
    )

_FsDot11TaggingPolicy_Type.__name__ = "Bits"
_FsDot11TaggingPolicy_Object = MibTableColumn
fsDot11TaggingPolicy = _FsDot11TaggingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 1, 1, 1),
    _FsDot11TaggingPolicy_Type()
)
fsDot11TaggingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11TaggingPolicy.setStatus("current")
_FsDot11QAPTable_Object = MibTable
fsDot11QAPTable = _FsDot11QAPTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 2)
)
if mibBuilder.loadTexts:
    fsDot11QAPTable.setStatus("current")
_FsDot11QAPEntry_Object = MibTableRow
fsDot11QAPEntry = _FsDot11QAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 2, 1)
)
fsDot11QAPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-DOT11-MIB", "dot11EDCATableIndex"),
)
if mibBuilder.loadTexts:
    fsDot11QAPEntry.setStatus("current")


class _FsDot11QueueDepth_Type(Integer32):
    """Custom type fsDot11QueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsDot11QueueDepth_Type.__name__ = "Integer32"
_FsDot11QueueDepth_Object = MibTableColumn
fsDot11QueueDepth = _FsDot11QueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 2, 1, 2),
    _FsDot11QueueDepth_Type()
)
fsDot11QueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11QueueDepth.setStatus("current")


class _FsDot11PriorityValue_Type(Integer32):
    """Custom type fsDot11PriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot11PriorityValue_Type.__name__ = "Integer32"
_FsDot11PriorityValue_Object = MibTableColumn
fsDot11PriorityValue = _FsDot11PriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 2, 1, 3),
    _FsDot11PriorityValue_Type()
)
fsDot11PriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PriorityValue.setStatus("current")


class _FsDot11DscpValue_Type(Integer32):
    """Custom type fsDot11DscpValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsDot11DscpValue_Type.__name__ = "Integer32"
_FsDot11DscpValue_Object = MibTableColumn
fsDot11DscpValue = _FsDot11DscpValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 2, 1, 4),
    _FsDot11DscpValue_Type()
)
fsDot11DscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11DscpValue.setStatus("current")
_FsQAPProfileTable_Object = MibTable
fsQAPProfileTable = _FsQAPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3)
)
if mibBuilder.loadTexts:
    fsQAPProfileTable.setStatus("current")
_FsQAPProfileEntry_Object = MibTableRow
fsQAPProfileEntry = _FsQAPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1)
)
fsQAPProfileEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "fsQAPProfileName"),
    (0, "SUPERMICRO-DOT11-MIB", "fsQAPProfileIndex"),
)
if mibBuilder.loadTexts:
    fsQAPProfileEntry.setStatus("current")


class _FsQAPProfileName_Type(OctetString):
    """Custom type fsQAPProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsQAPProfileName_Type.__name__ = "OctetString"
_FsQAPProfileName_Object = MibTableColumn
fsQAPProfileName = _FsQAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 1),
    _FsQAPProfileName_Type()
)
fsQAPProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQAPProfileName.setStatus("current")


class _FsQAPProfileIndex_Type(Integer32):
    """Custom type fsQAPProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsQAPProfileIndex_Type.__name__ = "Integer32"
_FsQAPProfileIndex_Object = MibTableColumn
fsQAPProfileIndex = _FsQAPProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 2),
    _FsQAPProfileIndex_Type()
)
fsQAPProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQAPProfileIndex.setStatus("current")


class _FsQAPProfileCWmin_Type(Integer32):
    """Custom type fsQAPProfileCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsQAPProfileCWmin_Type.__name__ = "Integer32"
_FsQAPProfileCWmin_Object = MibTableColumn
fsQAPProfileCWmin = _FsQAPProfileCWmin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 3),
    _FsQAPProfileCWmin_Type()
)
fsQAPProfileCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileCWmin.setStatus("current")


class _FsQAPProfileCWmax_Type(Integer32):
    """Custom type fsQAPProfileCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQAPProfileCWmax_Type.__name__ = "Integer32"
_FsQAPProfileCWmax_Object = MibTableColumn
fsQAPProfileCWmax = _FsQAPProfileCWmax_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 4),
    _FsQAPProfileCWmax_Type()
)
fsQAPProfileCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileCWmax.setStatus("current")


class _FsQAPProfileAIFSN_Type(Integer32):
    """Custom type fsQAPProfileAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsQAPProfileAIFSN_Type.__name__ = "Integer32"
_FsQAPProfileAIFSN_Object = MibTableColumn
fsQAPProfileAIFSN = _FsQAPProfileAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 5),
    _FsQAPProfileAIFSN_Type()
)
fsQAPProfileAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileAIFSN.setStatus("current")


class _FsQAPProfileTXOPLimit_Type(Integer32):
    """Custom type fsQAPProfileTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQAPProfileTXOPLimit_Type.__name__ = "Integer32"
_FsQAPProfileTXOPLimit_Object = MibTableColumn
fsQAPProfileTXOPLimit = _FsQAPProfileTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 6),
    _FsQAPProfileTXOPLimit_Type()
)
fsQAPProfileTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileTXOPLimit.setStatus("current")


class _FsQAPProfileQueueDepth_Type(Integer32):
    """Custom type fsQAPProfileQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsQAPProfileQueueDepth_Type.__name__ = "Integer32"
_FsQAPProfileQueueDepth_Object = MibTableColumn
fsQAPProfileQueueDepth = _FsQAPProfileQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 7),
    _FsQAPProfileQueueDepth_Type()
)
fsQAPProfileQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQAPProfileQueueDepth.setStatus("current")


class _FsQAPProfilePriorityValue_Type(Integer32):
    """Custom type fsQAPProfilePriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQAPProfilePriorityValue_Type.__name__ = "Integer32"
_FsQAPProfilePriorityValue_Object = MibTableColumn
fsQAPProfilePriorityValue = _FsQAPProfilePriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 8),
    _FsQAPProfilePriorityValue_Type()
)
fsQAPProfilePriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfilePriorityValue.setStatus("current")


class _FsQAPProfileDscpValue_Type(Integer32):
    """Custom type fsQAPProfileDscpValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsQAPProfileDscpValue_Type.__name__ = "Integer32"
_FsQAPProfileDscpValue_Object = MibTableColumn
fsQAPProfileDscpValue = _FsQAPProfileDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 9),
    _FsQAPProfileDscpValue_Type()
)
fsQAPProfileDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileDscpValue.setStatus("current")
_FsQAPProfileRowStatus_Type = RowStatus
_FsQAPProfileRowStatus_Object = MibTableColumn
fsQAPProfileRowStatus = _FsQAPProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 4, 3, 1, 10),
    _FsQAPProfileRowStatus_Type()
)
fsQAPProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQAPProfileRowStatus.setStatus("current")
_FsDot11phy_ObjectIdentity = ObjectIdentity
fsDot11phy = _FsDot11phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5)
)
_FsDot11AntennasListTable_Object = MibTable
fsDot11AntennasListTable = _FsDot11AntennasListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 1)
)
if mibBuilder.loadTexts:
    fsDot11AntennasListTable.setStatus("current")
_FsDot11AntennasListEntry_Object = MibTableRow
fsDot11AntennasListEntry = _FsDot11AntennasListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 1, 1)
)
fsDot11AntennasListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-DOT11-MIB", "dot11AntennaListIndex"),
)
if mibBuilder.loadTexts:
    fsDot11AntennasListEntry.setStatus("current")


class _FsAntennaMode_Type(Integer32):
    """Custom type fsAntennaMode based on Integer32"""
    defaultValue = 3

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
        *(("sectorA", 1),
          ("sectorB", 2),
          ("omni", 3),
          ("mimo", 4))
    )


_FsAntennaMode_Type.__name__ = "Integer32"
_FsAntennaMode_Object = MibTableColumn
fsAntennaMode = _FsAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 1, 1, 1),
    _FsAntennaMode_Type()
)
fsAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAntennaMode.setStatus("current")


class _FsAntennaSelection_Type(Integer32):
    """Custom type fsAntennaSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_FsAntennaSelection_Type.__name__ = "Integer32"
_FsAntennaSelection_Object = MibTableColumn
fsAntennaSelection = _FsAntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 1, 1, 2),
    _FsAntennaSelection_Type()
)
fsAntennaSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAntennaSelection.setStatus("current")
_FsDot11WlanTable_Object = MibTable
fsDot11WlanTable = _FsDot11WlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 2)
)
if mibBuilder.loadTexts:
    fsDot11WlanTable.setStatus("current")
_FsDot11WlanEntry_Object = MibTableRow
fsDot11WlanEntry = _FsDot11WlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 2, 1)
)
fsDot11WlanEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "capwapDot11WlanProfileId"),
)
if mibBuilder.loadTexts:
    fsDot11WlanEntry.setStatus("current")
_FsDot11WlanProfileIfIndex_Type = InterfaceIndex
_FsDot11WlanProfileIfIndex_Object = MibTableColumn
fsDot11WlanProfileIfIndex = _FsDot11WlanProfileIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 2, 1, 1),
    _FsDot11WlanProfileIfIndex_Type()
)
fsDot11WlanProfileIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanProfileIfIndex.setStatus("current")
_FsDot11WlanRowStatus_Type = RowStatus
_FsDot11WlanRowStatus_Object = MibTableColumn
fsDot11WlanRowStatus = _FsDot11WlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 2, 1, 2),
    _FsDot11WlanRowStatus_Type()
)
fsDot11WlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot11WlanRowStatus.setStatus("current")
_FsDot11WlanBindTable_Object = MibTable
fsDot11WlanBindTable = _FsDot11WlanBindTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 3)
)
if mibBuilder.loadTexts:
    fsDot11WlanBindTable.setStatus("current")
_FsDot11WlanBindEntry_Object = MibTableRow
fsDot11WlanBindEntry = _FsDot11WlanBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 3, 1)
)
fsDot11WlanBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-DOT11-MIB", "capwapDot11WlanProfileId"),
)
if mibBuilder.loadTexts:
    fsDot11WlanBindEntry.setStatus("current")
_FsDot11WlanBindWlanId_Type = CapwapDot11WlanIdTC
_FsDot11WlanBindWlanId_Object = MibTableColumn
fsDot11WlanBindWlanId = _FsDot11WlanBindWlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 3, 1, 1),
    _FsDot11WlanBindWlanId_Type()
)
fsDot11WlanBindWlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanBindWlanId.setStatus("current")
_FsDot11WlanBindBssIfIndex_Type = InterfaceIndex
_FsDot11WlanBindBssIfIndex_Object = MibTableColumn
fsDot11WlanBindBssIfIndex = _FsDot11WlanBindBssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 3, 1, 2),
    _FsDot11WlanBindBssIfIndex_Type()
)
fsDot11WlanBindBssIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WlanBindBssIfIndex.setStatus("current")
_FsDot11WlanBindRowStatus_Type = RowStatus
_FsDot11WlanBindRowStatus_Object = MibTableColumn
fsDot11WlanBindRowStatus = _FsDot11WlanBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 3, 1, 3),
    _FsDot11WlanBindRowStatus_Type()
)
fsDot11WlanBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot11WlanBindRowStatus.setStatus("current")
_FsDot11nConfigTable_Object = MibTable
fsDot11nConfigTable = _FsDot11nConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 4)
)
if mibBuilder.loadTexts:
    fsDot11nConfigTable.setStatus("current")
_FsDot11nConfigEntry_Object = MibTableRow
fsDot11nConfigEntry = _FsDot11nConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 4, 1)
)
fsDot11nConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11nConfigEntry.setStatus("current")


class _FsDot11nConfigShortGIfor20MHz_Type(TruthValue):
    """Custom type fsDot11nConfigShortGIfor20MHz based on TruthValue"""
    defaultValue = 2


_FsDot11nConfigShortGIfor20MHz_Type.__name__ = "TruthValue"
_FsDot11nConfigShortGIfor20MHz_Object = MibTableColumn
fsDot11nConfigShortGIfor20MHz = _FsDot11nConfigShortGIfor20MHz_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 4, 1, 1),
    _FsDot11nConfigShortGIfor20MHz_Type()
)
fsDot11nConfigShortGIfor20MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11nConfigShortGIfor20MHz.setStatus("current")


class _FsDot11nConfigShortGIfor40MHz_Type(TruthValue):
    """Custom type fsDot11nConfigShortGIfor40MHz based on TruthValue"""
    defaultValue = 2


_FsDot11nConfigShortGIfor40MHz_Type.__name__ = "TruthValue"
_FsDot11nConfigShortGIfor40MHz_Object = MibTableColumn
fsDot11nConfigShortGIfor40MHz = _FsDot11nConfigShortGIfor40MHz_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 4, 1, 2),
    _FsDot11nConfigShortGIfor40MHz_Type()
)
fsDot11nConfigShortGIfor40MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11nConfigShortGIfor40MHz.setStatus("current")


class _FsDot11nConfigChannelWidth_Type(Integer32):
    """Custom type fsDot11nConfigChannelWidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("width20MHz", 1),
          ("width40MHz", 2))
    )


_FsDot11nConfigChannelWidth_Type.__name__ = "Integer32"
_FsDot11nConfigChannelWidth_Object = MibTableColumn
fsDot11nConfigChannelWidth = _FsDot11nConfigChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 4, 1, 3),
    _FsDot11nConfigChannelWidth_Type()
)
fsDot11nConfigChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11nConfigChannelWidth.setStatus("current")
_FsDot11nMCSDataRateTable_Object = MibTable
fsDot11nMCSDataRateTable = _FsDot11nMCSDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 5)
)
if mibBuilder.loadTexts:
    fsDot11nMCSDataRateTable.setStatus("current")
_FsDot11nMCSDataRateEntry_Object = MibTableRow
fsDot11nMCSDataRateEntry = _FsDot11nMCSDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 5, 1)
)
fsDot11nMCSDataRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-DOT11-MIB", "fsDot11nMCSDataRateIndex"),
)
if mibBuilder.loadTexts:
    fsDot11nMCSDataRateEntry.setStatus("current")


class _FsDot11nMCSDataRateIndex_Type(Integer32):
    """Custom type fsDot11nMCSDataRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsDot11nMCSDataRateIndex_Type.__name__ = "Integer32"
_FsDot11nMCSDataRateIndex_Object = MibTableColumn
fsDot11nMCSDataRateIndex = _FsDot11nMCSDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 5, 1, 1),
    _FsDot11nMCSDataRateIndex_Type()
)
fsDot11nMCSDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11nMCSDataRateIndex.setStatus("current")


class _FsDot11nMCSDataRate_Type(TruthValue):
    """Custom type fsDot11nMCSDataRate based on TruthValue"""
    defaultValue = 2


_FsDot11nMCSDataRate_Type.__name__ = "TruthValue"
_FsDot11nMCSDataRate_Object = MibTableColumn
fsDot11nMCSDataRate = _FsDot11nMCSDataRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 5, 5, 1, 2),
    _FsDot11nMCSDataRate_Type()
)
fsDot11nMCSDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11nMCSDataRate.setStatus("current")
_FsWlanSystem_ObjectIdentity = ObjectIdentity
fsWlanSystem = _FsWlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6)
)
_FsWtpImageUpgradeTable_Object = MibTable
fsWtpImageUpgradeTable = _FsWtpImageUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1)
)
if mibBuilder.loadTexts:
    fsWtpImageUpgradeTable.setStatus("current")
_FsWtpImageUpgradeEntry_Object = MibTableRow
fsWtpImageUpgradeEntry = _FsWtpImageUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1)
)
fsWtpImageUpgradeEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11-MIB", "capwapBaseWtpProfileWtpModelNumber"),
)
if mibBuilder.loadTexts:
    fsWtpImageUpgradeEntry.setStatus("current")
_FsWtpImageVersion_Type = OctetString
_FsWtpImageVersion_Object = MibTableColumn
fsWtpImageVersion = _FsWtpImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 1),
    _FsWtpImageVersion_Type()
)
fsWtpImageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpImageVersion.setStatus("current")


class _FsWtpUpgradeDev_Type(Integer32):
    """Custom type fsWtpUpgradeDev based on Integer32"""
    defaultValue = 1

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
          ("perAP", 2),
          ("allAP", 3))
    )


_FsWtpUpgradeDev_Type.__name__ = "Integer32"
_FsWtpUpgradeDev_Object = MibTableColumn
fsWtpUpgradeDev = _FsWtpUpgradeDev_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 2),
    _FsWtpUpgradeDev_Type()
)
fsWtpUpgradeDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpUpgradeDev.setStatus("current")
_FsWtpName_Type = SnmpAdminString
_FsWtpName_Object = MibTableColumn
fsWtpName = _FsWtpName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 3),
    _FsWtpName_Type()
)
fsWtpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpName.setStatus("current")
_FsWtpImageName_Type = OctetString
_FsWtpImageName_Object = MibTableColumn
fsWtpImageName = _FsWtpImageName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 4),
    _FsWtpImageName_Type()
)
fsWtpImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpImageName.setStatus("current")


class _FsWtpAddressType_Type(InetAddressType):
    """Custom type fsWtpAddressType based on InetAddressType"""
    defaultValue = 1


_FsWtpAddressType_Type.__name__ = "InetAddressType"
_FsWtpAddressType_Object = MibTableColumn
fsWtpAddressType = _FsWtpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 5),
    _FsWtpAddressType_Type()
)
fsWtpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpAddressType.setStatus("current")


class _FsWtpServerIP_Type(InetAddress):
    """Custom type fsWtpServerIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsWtpServerIP_Type.__name__ = "InetAddress"
_FsWtpServerIP_Object = MibTableColumn
fsWtpServerIP = _FsWtpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 6),
    _FsWtpServerIP_Type()
)
fsWtpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpServerIP.setStatus("current")
_FsWtpRowStatus_Type = RowStatus
_FsWtpRowStatus_Object = MibTableColumn
fsWtpRowStatus = _FsWtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 83, 6, 1, 1, 7),
    _FsWtpRowStatus_Type()
)
fsWtpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DOT11-MIB",
    **{"CapwapBaseRadioIdTC": CapwapBaseRadioIdTC,
       "CapwapDot11WlanIdTC": CapwapDot11WlanIdTC,
       "CapwapDot11WlanIdProfileTC": CapwapDot11WlanIdProfileTC,
       "EnabledStatus": EnabledStatus,
       "fsDot11": fsDot11,
       "fsDot11Radio": fsDot11Radio,
       "fsDot11aNetworkEnable": fsDot11aNetworkEnable,
       "fsDot11bNetworkEnable": fsDot11bNetworkEnable,
       "fsDot11gSupport": fsDot11gSupport,
       "fsDot11anSupport": fsDot11anSupport,
       "fsDot11bnSupport": fsDot11bnSupport,
       "fsDot11ManagmentSSID": fsDot11ManagmentSSID,
       "fsDot11CountryString": fsDot11CountryString,
       "fsSecurityWebAuthParams": fsSecurityWebAuthParams,
       "fsSecurityWebAuthType": fsSecurityWebAuthType,
       "fsSecurityWebAuthUrl": fsSecurityWebAuthUrl,
       "fsSecurityWebAuthRedirectUrl": fsSecurityWebAuthRedirectUrl,
       "fsSecurityWebAddr": fsSecurityWebAddr,
       "fsSecurityWebAuthWebTitle": fsSecurityWebAuthWebTitle,
       "fsSecurityWebAuthWebMessage": fsSecurityWebAuthWebMessage,
       "fsSecurityWebAuthWebLogoFileName": fsSecurityWebAuthWebLogoFileName,
       "fsSecurityWebAuthWebSuccMessage": fsSecurityWebAuthWebSuccMessage,
       "fsSecurityWebAuthWebFailMessage": fsSecurityWebAuthWebFailMessage,
       "fsSecurityWebAuthWebButtonText": fsSecurityWebAuthWebButtonText,
       "fsSecurityWebAuthWebLoadBalInfo": fsSecurityWebAuthWebLoadBalInfo,
       "fsSecurityWebAuthDisplayLang": fsSecurityWebAuthDisplayLang,
       "fsSecurityWebAuthColor": fsSecurityWebAuthColor,
       "fsDot11smt": fsDot11smt,
       "fsDot11StationConfigTable": fsDot11StationConfigTable,
       "fsDot11StationConfigEntry": fsDot11StationConfigEntry,
       "fsDot11SupressSSID": fsDot11SupressSSID,
       "fsDot11VlanId": fsDot11VlanId,
       "fsDot11CapabilityProfileTable": fsDot11CapabilityProfileTable,
       "fsDot11CapabilityProfileEntry": fsDot11CapabilityProfileEntry,
       "fsDot11CapabilityProfileName": fsDot11CapabilityProfileName,
       "fsDot11CFPollable": fsDot11CFPollable,
       "fsDot11CFPollRequest": fsDot11CFPollRequest,
       "fsDot11PrivacyOptionImplemented": fsDot11PrivacyOptionImplemented,
       "fsDot11ShortPreambleOptionImplemented": fsDot11ShortPreambleOptionImplemented,
       "fsDot11PBCCOptionImplemented": fsDot11PBCCOptionImplemented,
       "fsDot11ChannelAgilityPresent": fsDot11ChannelAgilityPresent,
       "fsDot11QosOptionImplemented": fsDot11QosOptionImplemented,
       "fsDot11SpectrumManagementRequired": fsDot11SpectrumManagementRequired,
       "fsDot11ShortSlotTimeOptionImplemented": fsDot11ShortSlotTimeOptionImplemented,
       "fsDot11APSDOptionImplemented": fsDot11APSDOptionImplemented,
       "fsDot11DSSSOFDMOptionEnabled": fsDot11DSSSOFDMOptionEnabled,
       "fsDot11DelayedBlockAckOptionImplemented": fsDot11DelayedBlockAckOptionImplemented,
       "fsDot11ImmediateBlockAckOptionImplemented": fsDot11ImmediateBlockAckOptionImplemented,
       "fsDot11QAckOptionImplemented": fsDot11QAckOptionImplemented,
       "fsDot11QueueRequestOptionImplemented": fsDot11QueueRequestOptionImplemented,
       "fsDot11TXOPRequestOptionImplemented": fsDot11TXOPRequestOptionImplemented,
       "fsDot11RSNAOptionImplemented": fsDot11RSNAOptionImplemented,
       "fsDot11RSNAPreauthenticationImplemented": fsDot11RSNAPreauthenticationImplemented,
       "fsDot11CapabilityRowStatus": fsDot11CapabilityRowStatus,
       "fsDot11AuthenticationProfileTable": fsDot11AuthenticationProfileTable,
       "fsDot11AuthenticationProfileEntry": fsDot11AuthenticationProfileEntry,
       "fsDot11AuthenticationProfileName": fsDot11AuthenticationProfileName,
       "fsDot11AuthenticationAlgorithm": fsDot11AuthenticationAlgorithm,
       "fsDot11WepKeyIndex": fsDot11WepKeyIndex,
       "fsDot11WepKeyType": fsDot11WepKeyType,
       "fsDot11WepKeyLength": fsDot11WepKeyLength,
       "fsDot11WepKey": fsDot11WepKey,
       "fsDot11WebAuthentication": fsDot11WebAuthentication,
       "fsDot11AuthenticationRowStatus": fsDot11AuthenticationRowStatus,
       "fsSecurityWebAuthGuestInfoTable": fsSecurityWebAuthGuestInfoTable,
       "fsSecurityWebAuthGuestInfoEntry": fsSecurityWebAuthGuestInfoEntry,
       "fsSecurityWebAuthUName": fsSecurityWebAuthUName,
       "fsSecurityWlanProfileId": fsSecurityWlanProfileId,
       "fsSecurityWebAuthUserLifetime": fsSecurityWebAuthUserLifetime,
       "fsSecurityWebAuthUserEmailId": fsSecurityWebAuthUserEmailId,
       "fsSecurityWebAuthGuestInfoRowStatus": fsSecurityWebAuthGuestInfoRowStatus,
       "fsStationQosParamsTable": fsStationQosParamsTable,
       "fsStationQosParamsEntry": fsStationQosParamsEntry,
       "fsStaMacAddress": fsStaMacAddress,
       "fsStaQoSPriority": fsStaQoSPriority,
       "fsStaQoSDscp": fsStaQoSDscp,
       "fsVlanIsolationTable": fsVlanIsolationTable,
       "fsVlanIsolationEntry": fsVlanIsolationEntry,
       "fsVlanIsolation": fsVlanIsolation,
       "fsDot11RadioConfigTable": fsDot11RadioConfigTable,
       "fsDot11RadioConfigEntry": fsDot11RadioConfigEntry,
       "fsDot11RadioType": fsDot11RadioType,
       "fsDot11RadioNoOfBssIdSupported": fsDot11RadioNoOfBssIdSupported,
       "fsDot11RadioAntennaType": fsDot11RadioAntennaType,
       "fsDot11RadioFailureStatus": fsDot11RadioFailureStatus,
       "fsDot11RowStatus": fsDot11RowStatus,
       "fsDot11QosProfileTable": fsDot11QosProfileTable,
       "fsDot11QosProfileEntry": fsDot11QosProfileEntry,
       "fsDot11QosProfileName": fsDot11QosProfileName,
       "fsDot11QosTraffic": fsDot11QosTraffic,
       "fsDot11QosPassengerTrustMode": fsDot11QosPassengerTrustMode,
       "fsDot11QosRateLimit": fsDot11QosRateLimit,
       "fsDot11UpStreamCIR": fsDot11UpStreamCIR,
       "fsDot11UpStreamCBS": fsDot11UpStreamCBS,
       "fsDot11UpStreamEIR": fsDot11UpStreamEIR,
       "fsDot11UpStreamEBS": fsDot11UpStreamEBS,
       "fsDot11DownStreamCIR": fsDot11DownStreamCIR,
       "fsDot11DownStreamCBS": fsDot11DownStreamCBS,
       "fsDot11DownStreamEIR": fsDot11DownStreamEIR,
       "fsDot11DownStreamEBS": fsDot11DownStreamEBS,
       "fsDot11QosRowStatus": fsDot11QosRowStatus,
       "fsDot11WlanCapabilityProfileTable": fsDot11WlanCapabilityProfileTable,
       "fsDot11WlanCapabilityProfileEntry": fsDot11WlanCapabilityProfileEntry,
       "fsDot11WlanCFPollable": fsDot11WlanCFPollable,
       "fsDot11WlanCFPollRequest": fsDot11WlanCFPollRequest,
       "fsDot11WlanPrivacyOptionImplemented": fsDot11WlanPrivacyOptionImplemented,
       "fsDot11WlanShortPreambleOptionImplemented": fsDot11WlanShortPreambleOptionImplemented,
       "fsDot11WlanPBCCOptionImplemented": fsDot11WlanPBCCOptionImplemented,
       "fsDot11WlanChannelAgilityPresent": fsDot11WlanChannelAgilityPresent,
       "fsDot11WlanQosOptionImplemented": fsDot11WlanQosOptionImplemented,
       "fsDot11WlanSpectrumManagementRequired": fsDot11WlanSpectrumManagementRequired,
       "fsDot11WlanShortSlotTimeOptionImplemented": fsDot11WlanShortSlotTimeOptionImplemented,
       "fsDot11WlanAPSDOptionImplemented": fsDot11WlanAPSDOptionImplemented,
       "fsDot11WlanDSSSOFDMOptionEnabled": fsDot11WlanDSSSOFDMOptionEnabled,
       "fsDot11WlanDelayedBlockAckOptionImplemented": fsDot11WlanDelayedBlockAckOptionImplemented,
       "fsDot11WlanImmediateBlockAckOptionImplemented": fsDot11WlanImmediateBlockAckOptionImplemented,
       "fsDot11WlanQAckOptionImplemented": fsDot11WlanQAckOptionImplemented,
       "fsDot11WlanQueueRequestOptionImplemented": fsDot11WlanQueueRequestOptionImplemented,
       "fsDot11WlanTXOPRequestOptionImplemented": fsDot11WlanTXOPRequestOptionImplemented,
       "fsDot11WlanRSNAOptionImplemented": fsDot11WlanRSNAOptionImplemented,
       "fsDot11WlanRSNAPreauthenticationImplemented": fsDot11WlanRSNAPreauthenticationImplemented,
       "fsDot11WlanCapabilityRowStatus": fsDot11WlanCapabilityRowStatus,
       "fsDot11WlanAuthenticationProfileTable": fsDot11WlanAuthenticationProfileTable,
       "fsDot11WlanAuthenticationProfileEntry": fsDot11WlanAuthenticationProfileEntry,
       "fsDot11WlanAuthenticationAlgorithm": fsDot11WlanAuthenticationAlgorithm,
       "fsDot11WlanWepKeyIndex": fsDot11WlanWepKeyIndex,
       "fsDot11WlanWepKeyType": fsDot11WlanWepKeyType,
       "fsDot11WlanWepKeyLength": fsDot11WlanWepKeyLength,
       "fsDot11WlanWepKey": fsDot11WlanWepKey,
       "fsDot11WlanWebAuthentication": fsDot11WlanWebAuthentication,
       "fsDot11WlanAuthenticationRowStatus": fsDot11WlanAuthenticationRowStatus,
       "fsDot11WlanQosProfileTable": fsDot11WlanQosProfileTable,
       "fsDot11WlanQosProfileEntry": fsDot11WlanQosProfileEntry,
       "fsDot11WlanQosTraffic": fsDot11WlanQosTraffic,
       "fsDot11WlanQosPassengerTrustMode": fsDot11WlanQosPassengerTrustMode,
       "fsDot11WlanQosRateLimit": fsDot11WlanQosRateLimit,
       "fsDot11WlanUpStreamCIR": fsDot11WlanUpStreamCIR,
       "fsDot11WlanUpStreamCBS": fsDot11WlanUpStreamCBS,
       "fsDot11WlanUpStreamEIR": fsDot11WlanUpStreamEIR,
       "fsDot11WlanUpStreamEBS": fsDot11WlanUpStreamEBS,
       "fsDot11WlanDownStreamCIR": fsDot11WlanDownStreamCIR,
       "fsDot11WlanDownStreamCBS": fsDot11WlanDownStreamCBS,
       "fsDot11WlanDownStreamEIR": fsDot11WlanDownStreamEIR,
       "fsDot11WlanDownStreamEBS": fsDot11WlanDownStreamEBS,
       "fsDot11WlanQosRowStatus": fsDot11WlanQosRowStatus,
       "fsDot11CapabilityMappingTable": fsDot11CapabilityMappingTable,
       "fsDot11CapabilityMappingEntry": fsDot11CapabilityMappingEntry,
       "fsDot11CapabilityMappingProfileName": fsDot11CapabilityMappingProfileName,
       "fsDot11CapabilityMappingRowStatus": fsDot11CapabilityMappingRowStatus,
       "fsDot11AuthMappingTable": fsDot11AuthMappingTable,
       "fsDot11AuthMappingEntry": fsDot11AuthMappingEntry,
       "fsDot11AuthMappingProfileName": fsDot11AuthMappingProfileName,
       "fsDot11AuthMappingRowStatus": fsDot11AuthMappingRowStatus,
       "fsDot11QosMappingTable": fsDot11QosMappingTable,
       "fsDot11QosMappingEntry": fsDot11QosMappingEntry,
       "fsDot11QosMappingProfileName": fsDot11QosMappingProfileName,
       "fsDot11QosMappingRowStatus": fsDot11QosMappingRowStatus,
       "fsDot11ClientSummaryTable": fsDot11ClientSummaryTable,
       "fsDot11ClientSummaryEntry": fsDot11ClientSummaryEntry,
       "fsDot11ClientMacAddress": fsDot11ClientMacAddress,
       "fsDot11WlanProfileId": fsDot11WlanProfileId,
       "fsDot11WtpProfileName": fsDot11WtpProfileName,
       "fsDot11WtpRadioId": fsDot11WtpRadioId,
       "fsDot11AuthStatus": fsDot11AuthStatus,
       "fsDot11AssocStatus": fsDot11AssocStatus,
       "fsDot11mac": fsDot11mac,
       "fsDot11RadioQosTable": fsDot11RadioQosTable,
       "fsDot11RadioQosEntry": fsDot11RadioQosEntry,
       "fsDot11TaggingPolicy": fsDot11TaggingPolicy,
       "fsDot11QAPTable": fsDot11QAPTable,
       "fsDot11QAPEntry": fsDot11QAPEntry,
       "fsDot11QueueDepth": fsDot11QueueDepth,
       "fsDot11PriorityValue": fsDot11PriorityValue,
       "fsDot11DscpValue": fsDot11DscpValue,
       "fsQAPProfileTable": fsQAPProfileTable,
       "fsQAPProfileEntry": fsQAPProfileEntry,
       "fsQAPProfileName": fsQAPProfileName,
       "fsQAPProfileIndex": fsQAPProfileIndex,
       "fsQAPProfileCWmin": fsQAPProfileCWmin,
       "fsQAPProfileCWmax": fsQAPProfileCWmax,
       "fsQAPProfileAIFSN": fsQAPProfileAIFSN,
       "fsQAPProfileTXOPLimit": fsQAPProfileTXOPLimit,
       "fsQAPProfileQueueDepth": fsQAPProfileQueueDepth,
       "fsQAPProfilePriorityValue": fsQAPProfilePriorityValue,
       "fsQAPProfileDscpValue": fsQAPProfileDscpValue,
       "fsQAPProfileRowStatus": fsQAPProfileRowStatus,
       "fsDot11phy": fsDot11phy,
       "fsDot11AntennasListTable": fsDot11AntennasListTable,
       "fsDot11AntennasListEntry": fsDot11AntennasListEntry,
       "fsAntennaMode": fsAntennaMode,
       "fsAntennaSelection": fsAntennaSelection,
       "fsDot11WlanTable": fsDot11WlanTable,
       "fsDot11WlanEntry": fsDot11WlanEntry,
       "fsDot11WlanProfileIfIndex": fsDot11WlanProfileIfIndex,
       "fsDot11WlanRowStatus": fsDot11WlanRowStatus,
       "fsDot11WlanBindTable": fsDot11WlanBindTable,
       "fsDot11WlanBindEntry": fsDot11WlanBindEntry,
       "fsDot11WlanBindWlanId": fsDot11WlanBindWlanId,
       "fsDot11WlanBindBssIfIndex": fsDot11WlanBindBssIfIndex,
       "fsDot11WlanBindRowStatus": fsDot11WlanBindRowStatus,
       "fsDot11nConfigTable": fsDot11nConfigTable,
       "fsDot11nConfigEntry": fsDot11nConfigEntry,
       "fsDot11nConfigShortGIfor20MHz": fsDot11nConfigShortGIfor20MHz,
       "fsDot11nConfigShortGIfor40MHz": fsDot11nConfigShortGIfor40MHz,
       "fsDot11nConfigChannelWidth": fsDot11nConfigChannelWidth,
       "fsDot11nMCSDataRateTable": fsDot11nMCSDataRateTable,
       "fsDot11nMCSDataRateEntry": fsDot11nMCSDataRateEntry,
       "fsDot11nMCSDataRateIndex": fsDot11nMCSDataRateIndex,
       "fsDot11nMCSDataRate": fsDot11nMCSDataRate,
       "fsWlanSystem": fsWlanSystem,
       "fsWtpImageUpgradeTable": fsWtpImageUpgradeTable,
       "fsWtpImageUpgradeEntry": fsWtpImageUpgradeEntry,
       "fsWtpImageVersion": fsWtpImageVersion,
       "fsWtpUpgradeDev": fsWtpUpgradeDev,
       "fsWtpName": fsWtpName,
       "fsWtpImageName": fsWtpImageName,
       "fsWtpAddressType": fsWtpAddressType,
       "fsWtpServerIP": fsWtpServerIP,
       "fsWtpRowStatus": fsWtpRowStatus}
)
