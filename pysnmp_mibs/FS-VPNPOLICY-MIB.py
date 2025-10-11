# SNMP MIB module (FS-VPNPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/FS-VPNPOLICY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:04 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsVpnPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143)
)
if mibBuilder.loadTexts:
    fsVpnPolicy.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVpnObjects_ObjectIdentity = ObjectIdentity
fsVpnObjects = _FsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1)
)
_FsVpnTable_Object = MibTable
fsVpnTable = _FsVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1)
)
if mibBuilder.loadTexts:
    fsVpnTable.setStatus("current")
_FsVpnEntry_Object = MibTableRow
fsVpnEntry = _FsVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1)
)
fsVpnEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnPolicyName"),
)
if mibBuilder.loadTexts:
    fsVpnEntry.setStatus("current")


class _FsVpnPolicyName_Type(DisplayString):
    """Custom type fsVpnPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FsVpnPolicyName_Type.__name__ = "DisplayString"
_FsVpnPolicyName_Object = MibTableColumn
fsVpnPolicyName = _FsVpnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 1),
    _FsVpnPolicyName_Type()
)
fsVpnPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnPolicyName.setStatus("current")


class _FsVpnPolicyType_Type(Integer32):
    """Custom type fsVpnPolicyType based on Integer32"""
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
        *(("ipsecManual", 1),
          ("ikePresharedkey", 2),
          ("ikeCertificate", 3),
          ("xauth", 4),
          ("raVpnPresharedKey", 5))
    )


_FsVpnPolicyType_Type.__name__ = "Integer32"
_FsVpnPolicyType_Object = MibTableColumn
fsVpnPolicyType = _FsVpnPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 2),
    _FsVpnPolicyType_Type()
)
fsVpnPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnPolicyType.setStatus("current")


class _FsVpnPolicyPriority_Type(Integer32):
    """Custom type fsVpnPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsVpnPolicyPriority_Type.__name__ = "Integer32"
_FsVpnPolicyPriority_Object = MibTableColumn
fsVpnPolicyPriority = _FsVpnPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 3),
    _FsVpnPolicyPriority_Type()
)
fsVpnPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnPolicyPriority.setStatus("current")
_FsVpnTunTermAddrType_Type = InetAddressType
_FsVpnTunTermAddrType_Object = MibTableColumn
fsVpnTunTermAddrType = _FsVpnTunTermAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 4),
    _FsVpnTunTermAddrType_Type()
)
fsVpnTunTermAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnTunTermAddrType.setStatus("current")
_FsVpnLocalTunTermAddr_Type = InetAddress
_FsVpnLocalTunTermAddr_Object = MibTableColumn
fsVpnLocalTunTermAddr = _FsVpnLocalTunTermAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 5),
    _FsVpnLocalTunTermAddr_Type()
)
fsVpnLocalTunTermAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnLocalTunTermAddr.setStatus("current")
_FsVpnRemoteTunTermAddr_Type = InetAddress
_FsVpnRemoteTunTermAddr_Object = MibTableColumn
fsVpnRemoteTunTermAddr = _FsVpnRemoteTunTermAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 6),
    _FsVpnRemoteTunTermAddr_Type()
)
fsVpnRemoteTunTermAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRemoteTunTermAddr.setStatus("current")
_FsVpnProtectNetworkType_Type = InetAddressType
_FsVpnProtectNetworkType_Object = MibTableColumn
fsVpnProtectNetworkType = _FsVpnProtectNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 7),
    _FsVpnProtectNetworkType_Type()
)
fsVpnProtectNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnProtectNetworkType.setStatus("current")
_FsVpnLocalProtectNetwork_Type = InetAddress
_FsVpnLocalProtectNetwork_Object = MibTableColumn
fsVpnLocalProtectNetwork = _FsVpnLocalProtectNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 8),
    _FsVpnLocalProtectNetwork_Type()
)
fsVpnLocalProtectNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnLocalProtectNetwork.setStatus("current")
_FsVpnLocalProtectNetworkPrefixLen_Type = InetAddressPrefixLength
_FsVpnLocalProtectNetworkPrefixLen_Object = MibTableColumn
fsVpnLocalProtectNetworkPrefixLen = _FsVpnLocalProtectNetworkPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 9),
    _FsVpnLocalProtectNetworkPrefixLen_Type()
)
fsVpnLocalProtectNetworkPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnLocalProtectNetworkPrefixLen.setStatus("current")
_FsVpnRemoteProtectNetwork_Type = InetAddress
_FsVpnRemoteProtectNetwork_Object = MibTableColumn
fsVpnRemoteProtectNetwork = _FsVpnRemoteProtectNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 10),
    _FsVpnRemoteProtectNetwork_Type()
)
fsVpnRemoteProtectNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRemoteProtectNetwork.setStatus("current")
_FsVpnRemoteProtectNetworkPrefixLen_Type = InetAddressPrefixLength
_FsVpnRemoteProtectNetworkPrefixLen_Object = MibTableColumn
fsVpnRemoteProtectNetworkPrefixLen = _FsVpnRemoteProtectNetworkPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 11),
    _FsVpnRemoteProtectNetworkPrefixLen_Type()
)
fsVpnRemoteProtectNetworkPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRemoteProtectNetworkPrefixLen.setStatus("current")


class _FsVpnIkeSrcPortRange_Type(DisplayString):
    """Custom type fsVpnIkeSrcPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_FsVpnIkeSrcPortRange_Type.__name__ = "DisplayString"
_FsVpnIkeSrcPortRange_Object = MibTableColumn
fsVpnIkeSrcPortRange = _FsVpnIkeSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 12),
    _FsVpnIkeSrcPortRange_Type()
)
fsVpnIkeSrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkeSrcPortRange.setStatus("current")


class _FsVpnIkeDstPortRange_Type(DisplayString):
    """Custom type fsVpnIkeDstPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_FsVpnIkeDstPortRange_Type.__name__ = "DisplayString"
_FsVpnIkeDstPortRange_Object = MibTableColumn
fsVpnIkeDstPortRange = _FsVpnIkeDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 13),
    _FsVpnIkeDstPortRange_Type()
)
fsVpnIkeDstPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkeDstPortRange.setStatus("current")


class _FsVpnSecurityProtocol_Type(Integer32):
    """Custom type fsVpnSecurityProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("espproto", 50),
          ("ahproto", 51))
    )


_FsVpnSecurityProtocol_Type.__name__ = "Integer32"
_FsVpnSecurityProtocol_Object = MibTableColumn
fsVpnSecurityProtocol = _FsVpnSecurityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 14),
    _FsVpnSecurityProtocol_Type()
)
fsVpnSecurityProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnSecurityProtocol.setStatus("current")


class _FsVpnInboundSpi_Type(Integer32):
    """Custom type fsVpnInboundSpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_FsVpnInboundSpi_Type.__name__ = "Integer32"
_FsVpnInboundSpi_Object = MibTableColumn
fsVpnInboundSpi = _FsVpnInboundSpi_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 15),
    _FsVpnInboundSpi_Type()
)
fsVpnInboundSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnInboundSpi.setStatus("current")


class _FsVpnOutboundSpi_Type(Integer32):
    """Custom type fsVpnOutboundSpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_FsVpnOutboundSpi_Type.__name__ = "Integer32"
_FsVpnOutboundSpi_Object = MibTableColumn
fsVpnOutboundSpi = _FsVpnOutboundSpi_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 16),
    _FsVpnOutboundSpi_Type()
)
fsVpnOutboundSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnOutboundSpi.setStatus("current")


class _FsVpnMode_Type(Integer32):
    """Custom type fsVpnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2))
    )


_FsVpnMode_Type.__name__ = "Integer32"
_FsVpnMode_Object = MibTableColumn
fsVpnMode = _FsVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 17),
    _FsVpnMode_Type()
)
fsVpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnMode.setStatus("current")


class _FsVpnAuthAlgo_Type(Integer32):
    """Custom type fsVpnAuthAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 1),
          ("hmacsha1", 2),
          ("xcbcmac", 5),
          ("hmacsha256", 12),
          ("hmacsha384", 13),
          ("hmacsha512", 14))
    )


_FsVpnAuthAlgo_Type.__name__ = "Integer32"
_FsVpnAuthAlgo_Object = MibTableColumn
fsVpnAuthAlgo = _FsVpnAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 18),
    _FsVpnAuthAlgo_Type()
)
fsVpnAuthAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnAuthAlgo.setStatus("current")


class _FsVpnAhKey_Type(OctetString):
    """Custom type fsVpnAhKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsVpnAhKey_Type.__name__ = "OctetString"
_FsVpnAhKey_Object = MibTableColumn
fsVpnAhKey = _FsVpnAhKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 19),
    _FsVpnAhKey_Type()
)
fsVpnAhKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnAhKey.setStatus("current")


class _FsVpnEncrAlgo_Type(Integer32):
    """Custom type fsVpnEncrAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("descbc", 4),
          ("tripledescbc", 5),
          ("aes128", 12),
          ("aes192", 13),
          ("aes256", 14))
    )


_FsVpnEncrAlgo_Type.__name__ = "Integer32"
_FsVpnEncrAlgo_Object = MibTableColumn
fsVpnEncrAlgo = _FsVpnEncrAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 20),
    _FsVpnEncrAlgo_Type()
)
fsVpnEncrAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnEncrAlgo.setStatus("current")


class _FsVpnEspKey_Type(OctetString):
    """Custom type fsVpnEspKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsVpnEspKey_Type.__name__ = "OctetString"
_FsVpnEspKey_Object = MibTableColumn
fsVpnEspKey = _FsVpnEspKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 21),
    _FsVpnEspKey_Type()
)
fsVpnEspKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnEspKey.setStatus("current")


class _FsVpnAntiReplay_Type(Integer32):
    """Custom type fsVpnAntiReplay based on Integer32"""
    defaultValue = 1

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


_FsVpnAntiReplay_Type.__name__ = "Integer32"
_FsVpnAntiReplay_Object = MibTableColumn
fsVpnAntiReplay = _FsVpnAntiReplay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 22),
    _FsVpnAntiReplay_Type()
)
fsVpnAntiReplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnAntiReplay.setStatus("current")


class _FsVpnPolicyFlag_Type(Integer32):
    """Custom type fsVpnPolicyFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("apply", 3),
          ("bypass", 4))
    )


_FsVpnPolicyFlag_Type.__name__ = "Integer32"
_FsVpnPolicyFlag_Object = MibTableColumn
fsVpnPolicyFlag = _FsVpnPolicyFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 23),
    _FsVpnPolicyFlag_Type()
)
fsVpnPolicyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnPolicyFlag.setStatus("current")


class _FsVpnProtocol_Type(Integer32):
    """Custom type fsVpnProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              50,
              51,
              58,
              9000)
        )
    )
    namedValues = NamedValues(
        *(("icmpv4", 1),
          ("tcp", 6),
          ("udp", 17),
          ("espproto", 50),
          ("ahproto", 51),
          ("icmpv6", 58),
          ("any", 9000))
    )


_FsVpnProtocol_Type.__name__ = "Integer32"
_FsVpnProtocol_Object = MibTableColumn
fsVpnProtocol = _FsVpnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 24),
    _FsVpnProtocol_Type()
)
fsVpnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnProtocol.setStatus("current")
_FsVpnPolicyIntfIndex_Type = InterfaceIndexOrZero
_FsVpnPolicyIntfIndex_Object = MibTableColumn
fsVpnPolicyIntfIndex = _FsVpnPolicyIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 25),
    _FsVpnPolicyIntfIndex_Type()
)
fsVpnPolicyIntfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnPolicyIntfIndex.setStatus("current")


class _FsVpnIkePhase1HashAlgo_Type(Integer32):
    """Custom type fsVpnIkePhase1HashAlgo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2),
          ("sha256", 12),
          ("sha384", 13),
          ("sha512", 14))
    )


_FsVpnIkePhase1HashAlgo_Type.__name__ = "Integer32"
_FsVpnIkePhase1HashAlgo_Object = MibTableColumn
fsVpnIkePhase1HashAlgo = _FsVpnIkePhase1HashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 26),
    _FsVpnIkePhase1HashAlgo_Type()
)
fsVpnIkePhase1HashAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1HashAlgo.setStatus("current")


class _FsVpnIkePhase1EncryptionAlgo_Type(Integer32):
    """Custom type fsVpnIkePhase1EncryptionAlgo based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("descbc", 4),
          ("tripledescbc", 5),
          ("aes128", 12),
          ("aes192", 13),
          ("aes256", 14))
    )


_FsVpnIkePhase1EncryptionAlgo_Type.__name__ = "Integer32"
_FsVpnIkePhase1EncryptionAlgo_Object = MibTableColumn
fsVpnIkePhase1EncryptionAlgo = _FsVpnIkePhase1EncryptionAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 27),
    _FsVpnIkePhase1EncryptionAlgo_Type()
)
fsVpnIkePhase1EncryptionAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1EncryptionAlgo.setStatus("current")


class _FsVpnIkePhase1DHGroup_Type(Integer32):
    """Custom type fsVpnIkePhase1DHGroup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14))
    )


_FsVpnIkePhase1DHGroup_Type.__name__ = "Integer32"
_FsVpnIkePhase1DHGroup_Object = MibTableColumn
fsVpnIkePhase1DHGroup = _FsVpnIkePhase1DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 28),
    _FsVpnIkePhase1DHGroup_Type()
)
fsVpnIkePhase1DHGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1DHGroup.setStatus("current")


class _FsVpnIkePhase1LocalIdType_Type(Integer32):
    """Custom type fsVpnIkePhase1LocalIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("fqdn", 2),
          ("email", 3),
          ("ipv6", 5),
          ("dn", 9),
          ("keyId", 11))
    )


_FsVpnIkePhase1LocalIdType_Type.__name__ = "Integer32"
_FsVpnIkePhase1LocalIdType_Object = MibTableColumn
fsVpnIkePhase1LocalIdType = _FsVpnIkePhase1LocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 29),
    _FsVpnIkePhase1LocalIdType_Type()
)
fsVpnIkePhase1LocalIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1LocalIdType.setStatus("current")
_FsVpnIkePhase1LocalIdValue_Type = DisplayString
_FsVpnIkePhase1LocalIdValue_Object = MibTableColumn
fsVpnIkePhase1LocalIdValue = _FsVpnIkePhase1LocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 30),
    _FsVpnIkePhase1LocalIdValue_Type()
)
fsVpnIkePhase1LocalIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1LocalIdValue.setStatus("current")


class _FsVpnIkePhase1PeerIdType_Type(Integer32):
    """Custom type fsVpnIkePhase1PeerIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("fqdn", 2),
          ("email", 3),
          ("ipv6", 5),
          ("dn", 9),
          ("keyId", 11))
    )


_FsVpnIkePhase1PeerIdType_Type.__name__ = "Integer32"
_FsVpnIkePhase1PeerIdType_Object = MibTableColumn
fsVpnIkePhase1PeerIdType = _FsVpnIkePhase1PeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 31),
    _FsVpnIkePhase1PeerIdType_Type()
)
fsVpnIkePhase1PeerIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1PeerIdType.setStatus("current")
_FsVpnIkePhase1PeerIdValue_Type = DisplayString
_FsVpnIkePhase1PeerIdValue_Object = MibTableColumn
fsVpnIkePhase1PeerIdValue = _FsVpnIkePhase1PeerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 32),
    _FsVpnIkePhase1PeerIdValue_Type()
)
fsVpnIkePhase1PeerIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1PeerIdValue.setStatus("current")


class _FsVpnIkePhase1LifeTimeType_Type(Integer32):
    """Custom type fsVpnIkePhase1LifeTimeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("secs", 1),
          ("mins", 3),
          ("hrs", 4),
          ("days", 5))
    )


_FsVpnIkePhase1LifeTimeType_Type.__name__ = "Integer32"
_FsVpnIkePhase1LifeTimeType_Object = MibTableColumn
fsVpnIkePhase1LifeTimeType = _FsVpnIkePhase1LifeTimeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 33),
    _FsVpnIkePhase1LifeTimeType_Type()
)
fsVpnIkePhase1LifeTimeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1LifeTimeType.setStatus("current")


class _FsVpnIkePhase1LifeTime_Type(Integer32):
    """Custom type fsVpnIkePhase1LifeTime based on Integer32"""
    defaultValue = 2400


_FsVpnIkePhase1LifeTime_Type.__name__ = "Integer32"
_FsVpnIkePhase1LifeTime_Object = MibTableColumn
fsVpnIkePhase1LifeTime = _FsVpnIkePhase1LifeTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 34),
    _FsVpnIkePhase1LifeTime_Type()
)
fsVpnIkePhase1LifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1LifeTime.setStatus("current")


class _FsVpnIkePhase1Mode_Type(Integer32):
    """Custom type fsVpnIkePhase1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("main", 2),
          ("aggressive", 4))
    )


_FsVpnIkePhase1Mode_Type.__name__ = "Integer32"
_FsVpnIkePhase1Mode_Object = MibTableColumn
fsVpnIkePhase1Mode = _FsVpnIkePhase1Mode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 35),
    _FsVpnIkePhase1Mode_Type()
)
fsVpnIkePhase1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase1Mode.setStatus("current")


class _FsVpnIkePhase2AuthAlgo_Type(Integer32):
    """Custom type fsVpnIkePhase2AuthAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2),
          ("xcbcmac", 5),
          ("hmacsha256", 12),
          ("hmacsha384", 13),
          ("hmacsha512", 14))
    )


_FsVpnIkePhase2AuthAlgo_Type.__name__ = "Integer32"
_FsVpnIkePhase2AuthAlgo_Object = MibTableColumn
fsVpnIkePhase2AuthAlgo = _FsVpnIkePhase2AuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 36),
    _FsVpnIkePhase2AuthAlgo_Type()
)
fsVpnIkePhase2AuthAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase2AuthAlgo.setStatus("current")


class _FsVpnIkePhase2EspEncryptionAlgo_Type(Integer32):
    """Custom type fsVpnIkePhase2EspEncryptionAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("descbc", 4),
          ("tripledescbc", 5),
          ("null", 11),
          ("aes128", 12),
          ("aes192", 13),
          ("aes256", 14),
          ("aesctr128", 15),
          ("aesctr192", 16),
          ("aesctr256", 17))
    )


_FsVpnIkePhase2EspEncryptionAlgo_Type.__name__ = "Integer32"
_FsVpnIkePhase2EspEncryptionAlgo_Object = MibTableColumn
fsVpnIkePhase2EspEncryptionAlgo = _FsVpnIkePhase2EspEncryptionAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 37),
    _FsVpnIkePhase2EspEncryptionAlgo_Type()
)
fsVpnIkePhase2EspEncryptionAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase2EspEncryptionAlgo.setStatus("current")


class _FsVpnIkePhase2LifeTimeType_Type(Integer32):
    """Custom type fsVpnIkePhase2LifeTimeType based on Integer32"""
    defaultValue = 1

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
        *(("secs", 1),
          ("kb", 2),
          ("mins", 3),
          ("hrs", 4),
          ("days", 5))
    )


_FsVpnIkePhase2LifeTimeType_Type.__name__ = "Integer32"
_FsVpnIkePhase2LifeTimeType_Object = MibTableColumn
fsVpnIkePhase2LifeTimeType = _FsVpnIkePhase2LifeTimeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 38),
    _FsVpnIkePhase2LifeTimeType_Type()
)
fsVpnIkePhase2LifeTimeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase2LifeTimeType.setStatus("current")


class _FsVpnIkePhase2LifeTime_Type(Integer32):
    """Custom type fsVpnIkePhase2LifeTime based on Integer32"""
    defaultValue = 800


_FsVpnIkePhase2LifeTime_Type.__name__ = "Integer32"
_FsVpnIkePhase2LifeTime_Object = MibTableColumn
fsVpnIkePhase2LifeTime = _FsVpnIkePhase2LifeTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 39),
    _FsVpnIkePhase2LifeTime_Type()
)
fsVpnIkePhase2LifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase2LifeTime.setStatus("current")


class _FsVpnIkePhase2DHGroup_Type(Integer32):
    """Custom type fsVpnIkePhase2DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14))
    )


_FsVpnIkePhase2DHGroup_Type.__name__ = "Integer32"
_FsVpnIkePhase2DHGroup_Object = MibTableColumn
fsVpnIkePhase2DHGroup = _FsVpnIkePhase2DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 40),
    _FsVpnIkePhase2DHGroup_Type()
)
fsVpnIkePhase2DHGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkePhase2DHGroup.setStatus("current")


class _FsVpnIkeVersion_Type(Integer32):
    """Custom type fsVpnIkeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ikev1", 1),
          ("ikev2", 2))
    )


_FsVpnIkeVersion_Type.__name__ = "Integer32"
_FsVpnIkeVersion_Object = MibTableColumn
fsVpnIkeVersion = _FsVpnIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 41),
    _FsVpnIkeVersion_Type()
)
fsVpnIkeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnIkeVersion.setStatus("current")


class _FsVpnCertAlgoType_Type(Integer32):
    """Custom type fsVpnCertAlgoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_FsVpnCertAlgoType_Type.__name__ = "Integer32"
_FsVpnCertAlgoType_Object = MibTableColumn
fsVpnCertAlgoType = _FsVpnCertAlgoType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 42),
    _FsVpnCertAlgoType_Type()
)
fsVpnCertAlgoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCertAlgoType.setStatus("current")
_FsVpnPolicyRowStatus_Type = RowStatus
_FsVpnPolicyRowStatus_Object = MibTableColumn
fsVpnPolicyRowStatus = _FsVpnPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 1, 1, 43),
    _FsVpnPolicyRowStatus_Type()
)
fsVpnPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnPolicyRowStatus.setStatus("current")
_FsVpnRaUsersTable_Object = MibTable
fsVpnRaUsersTable = _FsVpnRaUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 2)
)
if mibBuilder.loadTexts:
    fsVpnRaUsersTable.setStatus("current")
_FsVpnRaUsersEntry_Object = MibTableRow
fsVpnRaUsersEntry = _FsVpnRaUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 2, 1)
)
fsVpnRaUsersEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnRaUserName"),
)
if mibBuilder.loadTexts:
    fsVpnRaUsersEntry.setStatus("current")


class _FsVpnRaUserName_Type(DisplayString):
    """Custom type fsVpnRaUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVpnRaUserName_Type.__name__ = "DisplayString"
_FsVpnRaUserName_Object = MibTableColumn
fsVpnRaUserName = _FsVpnRaUserName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 2, 1, 1),
    _FsVpnRaUserName_Type()
)
fsVpnRaUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnRaUserName.setStatus("current")


class _FsVpnRaUserSecret_Type(DisplayString):
    """Custom type fsVpnRaUserSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVpnRaUserSecret_Type.__name__ = "DisplayString"
_FsVpnRaUserSecret_Object = MibTableColumn
fsVpnRaUserSecret = _FsVpnRaUserSecret_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 2, 1, 2),
    _FsVpnRaUserSecret_Type()
)
fsVpnRaUserSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaUserSecret.setStatus("current")
_FsVpnRaUserRowStatus_Type = RowStatus
_FsVpnRaUserRowStatus_Object = MibTableColumn
fsVpnRaUserRowStatus = _FsVpnRaUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 2, 1, 3),
    _FsVpnRaUserRowStatus_Type()
)
fsVpnRaUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnRaUserRowStatus.setStatus("current")
_FsVpnRaAddressPoolTable_Object = MibTable
fsVpnRaAddressPoolTable = _FsVpnRaAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3)
)
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolTable.setStatus("current")
_FsVpnRaAddressPoolEntry_Object = MibTableRow
fsVpnRaAddressPoolEntry = _FsVpnRaAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1)
)
fsVpnRaAddressPoolEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnRaAddressPoolName"),
)
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolEntry.setStatus("current")


class _FsVpnRaAddressPoolName_Type(DisplayString):
    """Custom type fsVpnRaAddressPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVpnRaAddressPoolName_Type.__name__ = "DisplayString"
_FsVpnRaAddressPoolName_Object = MibTableColumn
fsVpnRaAddressPoolName = _FsVpnRaAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 1),
    _FsVpnRaAddressPoolName_Type()
)
fsVpnRaAddressPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolName.setStatus("current")
_FsVpnRaAddressPoolAddrType_Type = InetAddressType
_FsVpnRaAddressPoolAddrType_Object = MibTableColumn
fsVpnRaAddressPoolAddrType = _FsVpnRaAddressPoolAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 2),
    _FsVpnRaAddressPoolAddrType_Type()
)
fsVpnRaAddressPoolAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolAddrType.setStatus("current")
_FsVpnRaAddressPoolStart_Type = InetAddress
_FsVpnRaAddressPoolStart_Object = MibTableColumn
fsVpnRaAddressPoolStart = _FsVpnRaAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 3),
    _FsVpnRaAddressPoolStart_Type()
)
fsVpnRaAddressPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolStart.setStatus("current")
_FsVpnRaAddressPoolEnd_Type = InetAddress
_FsVpnRaAddressPoolEnd_Object = MibTableColumn
fsVpnRaAddressPoolEnd = _FsVpnRaAddressPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 4),
    _FsVpnRaAddressPoolEnd_Type()
)
fsVpnRaAddressPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolEnd.setStatus("current")
_FsVpnRaAddressPoolPrefixLen_Type = InetAddressPrefixLength
_FsVpnRaAddressPoolPrefixLen_Object = MibTableColumn
fsVpnRaAddressPoolPrefixLen = _FsVpnRaAddressPoolPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 5),
    _FsVpnRaAddressPoolPrefixLen_Type()
)
fsVpnRaAddressPoolPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolPrefixLen.setStatus("current")
_FsVpnRaAddressPoolRowStatus_Type = RowStatus
_FsVpnRaAddressPoolRowStatus_Object = MibTableColumn
fsVpnRaAddressPoolRowStatus = _FsVpnRaAddressPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 3, 1, 6),
    _FsVpnRaAddressPoolRowStatus_Type()
)
fsVpnRaAddressPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnRaAddressPoolRowStatus.setStatus("current")
_FsVpnRemoteIdTable_Object = MibTable
fsVpnRemoteIdTable = _FsVpnRemoteIdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4)
)
if mibBuilder.loadTexts:
    fsVpnRemoteIdTable.setStatus("current")
_FsVpnRemoteIdEntry_Object = MibTableRow
fsVpnRemoteIdEntry = _FsVpnRemoteIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1)
)
fsVpnRemoteIdEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnRemoteIdType"),
    (0, "FS-VPNPOLICY-MIB", "fsVpnRemoteIdValue"),
)
if mibBuilder.loadTexts:
    fsVpnRemoteIdEntry.setStatus("current")


class _FsVpnRemoteIdType_Type(Integer32):
    """Custom type fsVpnRemoteIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("fqdn", 2),
          ("email", 3),
          ("ipv6", 5),
          ("dn", 9),
          ("keyId", 11))
    )


_FsVpnRemoteIdType_Type.__name__ = "Integer32"
_FsVpnRemoteIdType_Object = MibTableColumn
fsVpnRemoteIdType = _FsVpnRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1, 1),
    _FsVpnRemoteIdType_Type()
)
fsVpnRemoteIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnRemoteIdType.setStatus("current")
_FsVpnRemoteIdValue_Type = DisplayString
_FsVpnRemoteIdValue_Object = MibTableColumn
fsVpnRemoteIdValue = _FsVpnRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1, 2),
    _FsVpnRemoteIdValue_Type()
)
fsVpnRemoteIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnRemoteIdValue.setStatus("current")
_FsVpnRemoteIdKey_Type = DisplayString
_FsVpnRemoteIdKey_Object = MibTableColumn
fsVpnRemoteIdKey = _FsVpnRemoteIdKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1, 3),
    _FsVpnRemoteIdKey_Type()
)
fsVpnRemoteIdKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRemoteIdKey.setStatus("current")
_FsVpnRemoteIdAuthType_Type = Integer32
_FsVpnRemoteIdAuthType_Object = MibTableColumn
fsVpnRemoteIdAuthType = _FsVpnRemoteIdAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1, 4),
    _FsVpnRemoteIdAuthType_Type()
)
fsVpnRemoteIdAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRemoteIdAuthType.setStatus("current")
_FsVpnRemoteIdStatus_Type = RowStatus
_FsVpnRemoteIdStatus_Object = MibTableColumn
fsVpnRemoteIdStatus = _FsVpnRemoteIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 4, 1, 5),
    _FsVpnRemoteIdStatus_Type()
)
fsVpnRemoteIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnRemoteIdStatus.setStatus("current")
_FsVpnCertInfoTable_Object = MibTable
fsVpnCertInfoTable = _FsVpnCertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5)
)
if mibBuilder.loadTexts:
    fsVpnCertInfoTable.setStatus("current")
_FsVpnCertInfoEntry_Object = MibTableRow
fsVpnCertInfoEntry = _FsVpnCertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1)
)
fsVpnCertInfoEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnCertKeyString"),
)
if mibBuilder.loadTexts:
    fsVpnCertInfoEntry.setStatus("current")
_FsVpnCertKeyString_Type = DisplayString
_FsVpnCertKeyString_Object = MibTableColumn
fsVpnCertKeyString = _FsVpnCertKeyString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 1),
    _FsVpnCertKeyString_Type()
)
fsVpnCertKeyString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnCertKeyString.setStatus("current")


class _FsVpnCertKeyType_Type(Integer32):
    """Custom type fsVpnCertKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_FsVpnCertKeyType_Type.__name__ = "Integer32"
_FsVpnCertKeyType_Object = MibTableColumn
fsVpnCertKeyType = _FsVpnCertKeyType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 2),
    _FsVpnCertKeyType_Type()
)
fsVpnCertKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCertKeyType.setStatus("current")
_FsVpnCertKeyFileName_Type = DisplayString
_FsVpnCertKeyFileName_Object = MibTableColumn
fsVpnCertKeyFileName = _FsVpnCertKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 3),
    _FsVpnCertKeyFileName_Type()
)
fsVpnCertKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCertKeyFileName.setStatus("current")
_FsVpnCertFileName_Type = DisplayString
_FsVpnCertFileName_Object = MibTableColumn
fsVpnCertFileName = _FsVpnCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 4),
    _FsVpnCertFileName_Type()
)
fsVpnCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCertFileName.setStatus("current")


class _FsVpnCertEncodeType_Type(Integer32):
    """Custom type fsVpnCertEncodeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pem", 1),
          ("der", 2))
    )


_FsVpnCertEncodeType_Type.__name__ = "Integer32"
_FsVpnCertEncodeType_Object = MibTableColumn
fsVpnCertEncodeType = _FsVpnCertEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 5),
    _FsVpnCertEncodeType_Type()
)
fsVpnCertEncodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCertEncodeType.setStatus("current")
_FsVpnCertStatus_Type = RowStatus
_FsVpnCertStatus_Object = MibTableColumn
fsVpnCertStatus = _FsVpnCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 5, 1, 6),
    _FsVpnCertStatus_Type()
)
fsVpnCertStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnCertStatus.setStatus("current")
_FsVpnCaCertInfoTable_Object = MibTable
fsVpnCaCertInfoTable = _FsVpnCaCertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6)
)
if mibBuilder.loadTexts:
    fsVpnCaCertInfoTable.setStatus("current")
_FsVpnCaCertInfoEntry_Object = MibTableRow
fsVpnCaCertInfoEntry = _FsVpnCaCertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6, 1)
)
fsVpnCaCertInfoEntry.setIndexNames(
    (0, "FS-VPNPOLICY-MIB", "fsVpnCaCertKeyString"),
)
if mibBuilder.loadTexts:
    fsVpnCaCertInfoEntry.setStatus("current")
_FsVpnCaCertKeyString_Type = DisplayString
_FsVpnCaCertKeyString_Object = MibTableColumn
fsVpnCaCertKeyString = _FsVpnCaCertKeyString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6, 1, 1),
    _FsVpnCaCertKeyString_Type()
)
fsVpnCaCertKeyString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVpnCaCertKeyString.setStatus("current")
_FsVpnCaCertFileName_Type = DisplayString
_FsVpnCaCertFileName_Object = MibTableColumn
fsVpnCaCertFileName = _FsVpnCaCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6, 1, 2),
    _FsVpnCaCertFileName_Type()
)
fsVpnCaCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCaCertFileName.setStatus("current")


class _FsVpnCaCertEncodeType_Type(Integer32):
    """Custom type fsVpnCaCertEncodeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pem", 1),
          ("der", 2))
    )


_FsVpnCaCertEncodeType_Type.__name__ = "Integer32"
_FsVpnCaCertEncodeType_Object = MibTableColumn
fsVpnCaCertEncodeType = _FsVpnCaCertEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6, 1, 3),
    _FsVpnCaCertEncodeType_Type()
)
fsVpnCaCertEncodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnCaCertEncodeType.setStatus("current")
_FsVpnCaCertStatus_Type = RowStatus
_FsVpnCaCertStatus_Object = MibTableColumn
fsVpnCaCertStatus = _FsVpnCaCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 1, 6, 1, 4),
    _FsVpnCaCertStatus_Type()
)
fsVpnCaCertStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVpnCaCertStatus.setStatus("current")
_FsVpnScalars_ObjectIdentity = ObjectIdentity
fsVpnScalars = _FsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2)
)


class _FsVpnGlobalStatus_Type(Integer32):
    """Custom type fsVpnGlobalStatus based on Integer32"""
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


_FsVpnGlobalStatus_Type.__name__ = "Integer32"
_FsVpnGlobalStatus_Object = MibScalar
fsVpnGlobalStatus = _FsVpnGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 1),
    _FsVpnGlobalStatus_Type()
)
fsVpnGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnGlobalStatus.setStatus("current")
_FsVpnMaxTunnels_Type = Integer32
_FsVpnMaxTunnels_Object = MibScalar
fsVpnMaxTunnels = _FsVpnMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 2),
    _FsVpnMaxTunnels_Type()
)
fsVpnMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnMaxTunnels.setStatus("current")
_FsVpnIpPktsIn_Type = Counter32
_FsVpnIpPktsIn_Object = MibScalar
fsVpnIpPktsIn = _FsVpnIpPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 3),
    _FsVpnIpPktsIn_Type()
)
fsVpnIpPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIpPktsIn.setStatus("current")
_FsVpnIpPktsOut_Type = Counter32
_FsVpnIpPktsOut_Object = MibScalar
fsVpnIpPktsOut = _FsVpnIpPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 4),
    _FsVpnIpPktsOut_Type()
)
fsVpnIpPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIpPktsOut.setStatus("current")
_FsVpnPktsSecured_Type = Counter32
_FsVpnPktsSecured_Object = MibScalar
fsVpnPktsSecured = _FsVpnPktsSecured_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 5),
    _FsVpnPktsSecured_Type()
)
fsVpnPktsSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnPktsSecured.setStatus("current")
_FsVpnPktsDropped_Type = Counter32
_FsVpnPktsDropped_Object = MibScalar
fsVpnPktsDropped = _FsVpnPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 6),
    _FsVpnPktsDropped_Type()
)
fsVpnPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnPktsDropped.setStatus("current")
_FsVpnIkeSAsActive_Type = Counter32
_FsVpnIkeSAsActive_Object = MibScalar
fsVpnIkeSAsActive = _FsVpnIkeSAsActive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 7),
    _FsVpnIkeSAsActive_Type()
)
fsVpnIkeSAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIkeSAsActive.setStatus("current")
_FsVpnIkeNegotiations_Type = Counter32
_FsVpnIkeNegotiations_Object = MibScalar
fsVpnIkeNegotiations = _FsVpnIkeNegotiations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 8),
    _FsVpnIkeNegotiations_Type()
)
fsVpnIkeNegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIkeNegotiations.setStatus("current")
_FsVpnIkeRekeys_Type = Counter32
_FsVpnIkeRekeys_Object = MibScalar
fsVpnIkeRekeys = _FsVpnIkeRekeys_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 9),
    _FsVpnIkeRekeys_Type()
)
fsVpnIkeRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIkeRekeys.setStatus("current")
_FsVpnIkeNegoFailed_Type = Counter32
_FsVpnIkeNegoFailed_Object = MibScalar
fsVpnIkeNegoFailed = _FsVpnIkeNegoFailed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 10),
    _FsVpnIkeNegoFailed_Type()
)
fsVpnIkeNegoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIkeNegoFailed.setStatus("current")
_FsVpnIPSecSAsActive_Type = Counter32
_FsVpnIPSecSAsActive_Object = MibScalar
fsVpnIPSecSAsActive = _FsVpnIPSecSAsActive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 11),
    _FsVpnIPSecSAsActive_Type()
)
fsVpnIPSecSAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIPSecSAsActive.setStatus("current")
_FsVpnIPSecNegotiations_Type = Counter32
_FsVpnIPSecNegotiations_Object = MibScalar
fsVpnIPSecNegotiations = _FsVpnIPSecNegotiations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 12),
    _FsVpnIPSecNegotiations_Type()
)
fsVpnIPSecNegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIPSecNegotiations.setStatus("current")
_FsVpnIPSecNegoFailed_Type = Counter32
_FsVpnIPSecNegoFailed_Object = MibScalar
fsVpnIPSecNegoFailed = _FsVpnIPSecNegoFailed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 13),
    _FsVpnIPSecNegoFailed_Type()
)
fsVpnIPSecNegoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnIPSecNegoFailed.setStatus("current")
_FsVpnTotalRekeys_Type = Counter32
_FsVpnTotalRekeys_Object = MibScalar
fsVpnTotalRekeys = _FsVpnTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 14),
    _FsVpnTotalRekeys_Type()
)
fsVpnTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVpnTotalRekeys.setStatus("current")


class _FsVpnRaServer_Type(Integer32):
    """Custom type fsVpnRaServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsVpnRaServer_Type.__name__ = "Integer32"
_FsVpnRaServer_Object = MibScalar
fsVpnRaServer = _FsVpnRaServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 15),
    _FsVpnRaServer_Type()
)
fsVpnRaServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnRaServer.setStatus("current")


class _FsVpnDummyPktGen_Type(Integer32):
    """Custom type fsVpnDummyPktGen based on Integer32"""
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


_FsVpnDummyPktGen_Type.__name__ = "Integer32"
_FsVpnDummyPktGen_Object = MibScalar
fsVpnDummyPktGen = _FsVpnDummyPktGen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 16),
    _FsVpnDummyPktGen_Type()
)
fsVpnDummyPktGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnDummyPktGen.setStatus("current")


class _FsVpnDummyPktParam_Type(Integer32):
    """Custom type fsVpnDummyPktParam based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsVpnDummyPktParam_Type.__name__ = "Integer32"
_FsVpnDummyPktParam_Object = MibScalar
fsVpnDummyPktParam = _FsVpnDummyPktParam_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 17),
    _FsVpnDummyPktParam_Type()
)
fsVpnDummyPktParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVpnDummyPktParam.setStatus("current")


class _FsIkeTraceOption_Type(Integer32):
    """Custom type fsIkeTraceOption based on Integer32"""
    defaultValue = 0


_FsIkeTraceOption_Type.__name__ = "Integer32"
_FsIkeTraceOption_Object = MibScalar
fsIkeTraceOption = _FsIkeTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 18),
    _FsIkeTraceOption_Type()
)
fsIkeTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIkeTraceOption.setStatus("current")


class _FsIpsecTraceOption_Type(Integer32):
    """Custom type fsIpsecTraceOption based on Integer32"""
    defaultValue = 0


_FsIpsecTraceOption_Type.__name__ = "Integer32"
_FsIpsecTraceOption_Object = MibScalar
fsIpsecTraceOption = _FsIpsecTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 143, 2, 19),
    _FsIpsecTraceOption_Type()
)
fsIpsecTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpsecTraceOption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VPNPOLICY-MIB",
    **{"fsVpnPolicy": fsVpnPolicy,
       "fsVpnObjects": fsVpnObjects,
       "fsVpnTable": fsVpnTable,
       "fsVpnEntry": fsVpnEntry,
       "fsVpnPolicyName": fsVpnPolicyName,
       "fsVpnPolicyType": fsVpnPolicyType,
       "fsVpnPolicyPriority": fsVpnPolicyPriority,
       "fsVpnTunTermAddrType": fsVpnTunTermAddrType,
       "fsVpnLocalTunTermAddr": fsVpnLocalTunTermAddr,
       "fsVpnRemoteTunTermAddr": fsVpnRemoteTunTermAddr,
       "fsVpnProtectNetworkType": fsVpnProtectNetworkType,
       "fsVpnLocalProtectNetwork": fsVpnLocalProtectNetwork,
       "fsVpnLocalProtectNetworkPrefixLen": fsVpnLocalProtectNetworkPrefixLen,
       "fsVpnRemoteProtectNetwork": fsVpnRemoteProtectNetwork,
       "fsVpnRemoteProtectNetworkPrefixLen": fsVpnRemoteProtectNetworkPrefixLen,
       "fsVpnIkeSrcPortRange": fsVpnIkeSrcPortRange,
       "fsVpnIkeDstPortRange": fsVpnIkeDstPortRange,
       "fsVpnSecurityProtocol": fsVpnSecurityProtocol,
       "fsVpnInboundSpi": fsVpnInboundSpi,
       "fsVpnOutboundSpi": fsVpnOutboundSpi,
       "fsVpnMode": fsVpnMode,
       "fsVpnAuthAlgo": fsVpnAuthAlgo,
       "fsVpnAhKey": fsVpnAhKey,
       "fsVpnEncrAlgo": fsVpnEncrAlgo,
       "fsVpnEspKey": fsVpnEspKey,
       "fsVpnAntiReplay": fsVpnAntiReplay,
       "fsVpnPolicyFlag": fsVpnPolicyFlag,
       "fsVpnProtocol": fsVpnProtocol,
       "fsVpnPolicyIntfIndex": fsVpnPolicyIntfIndex,
       "fsVpnIkePhase1HashAlgo": fsVpnIkePhase1HashAlgo,
       "fsVpnIkePhase1EncryptionAlgo": fsVpnIkePhase1EncryptionAlgo,
       "fsVpnIkePhase1DHGroup": fsVpnIkePhase1DHGroup,
       "fsVpnIkePhase1LocalIdType": fsVpnIkePhase1LocalIdType,
       "fsVpnIkePhase1LocalIdValue": fsVpnIkePhase1LocalIdValue,
       "fsVpnIkePhase1PeerIdType": fsVpnIkePhase1PeerIdType,
       "fsVpnIkePhase1PeerIdValue": fsVpnIkePhase1PeerIdValue,
       "fsVpnIkePhase1LifeTimeType": fsVpnIkePhase1LifeTimeType,
       "fsVpnIkePhase1LifeTime": fsVpnIkePhase1LifeTime,
       "fsVpnIkePhase1Mode": fsVpnIkePhase1Mode,
       "fsVpnIkePhase2AuthAlgo": fsVpnIkePhase2AuthAlgo,
       "fsVpnIkePhase2EspEncryptionAlgo": fsVpnIkePhase2EspEncryptionAlgo,
       "fsVpnIkePhase2LifeTimeType": fsVpnIkePhase2LifeTimeType,
       "fsVpnIkePhase2LifeTime": fsVpnIkePhase2LifeTime,
       "fsVpnIkePhase2DHGroup": fsVpnIkePhase2DHGroup,
       "fsVpnIkeVersion": fsVpnIkeVersion,
       "fsVpnCertAlgoType": fsVpnCertAlgoType,
       "fsVpnPolicyRowStatus": fsVpnPolicyRowStatus,
       "fsVpnRaUsersTable": fsVpnRaUsersTable,
       "fsVpnRaUsersEntry": fsVpnRaUsersEntry,
       "fsVpnRaUserName": fsVpnRaUserName,
       "fsVpnRaUserSecret": fsVpnRaUserSecret,
       "fsVpnRaUserRowStatus": fsVpnRaUserRowStatus,
       "fsVpnRaAddressPoolTable": fsVpnRaAddressPoolTable,
       "fsVpnRaAddressPoolEntry": fsVpnRaAddressPoolEntry,
       "fsVpnRaAddressPoolName": fsVpnRaAddressPoolName,
       "fsVpnRaAddressPoolAddrType": fsVpnRaAddressPoolAddrType,
       "fsVpnRaAddressPoolStart": fsVpnRaAddressPoolStart,
       "fsVpnRaAddressPoolEnd": fsVpnRaAddressPoolEnd,
       "fsVpnRaAddressPoolPrefixLen": fsVpnRaAddressPoolPrefixLen,
       "fsVpnRaAddressPoolRowStatus": fsVpnRaAddressPoolRowStatus,
       "fsVpnRemoteIdTable": fsVpnRemoteIdTable,
       "fsVpnRemoteIdEntry": fsVpnRemoteIdEntry,
       "fsVpnRemoteIdType": fsVpnRemoteIdType,
       "fsVpnRemoteIdValue": fsVpnRemoteIdValue,
       "fsVpnRemoteIdKey": fsVpnRemoteIdKey,
       "fsVpnRemoteIdAuthType": fsVpnRemoteIdAuthType,
       "fsVpnRemoteIdStatus": fsVpnRemoteIdStatus,
       "fsVpnCertInfoTable": fsVpnCertInfoTable,
       "fsVpnCertInfoEntry": fsVpnCertInfoEntry,
       "fsVpnCertKeyString": fsVpnCertKeyString,
       "fsVpnCertKeyType": fsVpnCertKeyType,
       "fsVpnCertKeyFileName": fsVpnCertKeyFileName,
       "fsVpnCertFileName": fsVpnCertFileName,
       "fsVpnCertEncodeType": fsVpnCertEncodeType,
       "fsVpnCertStatus": fsVpnCertStatus,
       "fsVpnCaCertInfoTable": fsVpnCaCertInfoTable,
       "fsVpnCaCertInfoEntry": fsVpnCaCertInfoEntry,
       "fsVpnCaCertKeyString": fsVpnCaCertKeyString,
       "fsVpnCaCertFileName": fsVpnCaCertFileName,
       "fsVpnCaCertEncodeType": fsVpnCaCertEncodeType,
       "fsVpnCaCertStatus": fsVpnCaCertStatus,
       "fsVpnScalars": fsVpnScalars,
       "fsVpnGlobalStatus": fsVpnGlobalStatus,
       "fsVpnMaxTunnels": fsVpnMaxTunnels,
       "fsVpnIpPktsIn": fsVpnIpPktsIn,
       "fsVpnIpPktsOut": fsVpnIpPktsOut,
       "fsVpnPktsSecured": fsVpnPktsSecured,
       "fsVpnPktsDropped": fsVpnPktsDropped,
       "fsVpnIkeSAsActive": fsVpnIkeSAsActive,
       "fsVpnIkeNegotiations": fsVpnIkeNegotiations,
       "fsVpnIkeRekeys": fsVpnIkeRekeys,
       "fsVpnIkeNegoFailed": fsVpnIkeNegoFailed,
       "fsVpnIPSecSAsActive": fsVpnIPSecSAsActive,
       "fsVpnIPSecNegotiations": fsVpnIPSecNegotiations,
       "fsVpnIPSecNegoFailed": fsVpnIPSecNegoFailed,
       "fsVpnTotalRekeys": fsVpnTotalRekeys,
       "fsVpnRaServer": fsVpnRaServer,
       "fsVpnDummyPktGen": fsVpnDummyPktGen,
       "fsVpnDummyPktParam": fsVpnDummyPktParam,
       "fsIkeTraceOption": fsIkeTraceOption,
       "fsIpsecTraceOption": fsIpsecTraceOption}
)
