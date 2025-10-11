# SNMP MIB module (H3C-IPSEC-MONITOR-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-IPSEC-MONITOR-V2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:58 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cIPsecMonitorV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126)
)
if mibBuilder.loadTexts:
    h3cIPsecMonitorV2.setRevisions(
        ("2017-10-31 16:50",
         "2012-06-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cIPsecDiffHellmanGrpV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              24,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dhGroup1", 1),
          ("dhGroup2", 2),
          ("dhGroup5", 5),
          ("dhGroup14", 14),
          ("dhGroup24", 24),
          ("invalidGroup", 2147483647))
    )



class H3cIPsecEncapModeV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2),
          ("invalidMode", 2147483647))
    )



class H3cIPsecEncryptAlgoV2(TextualConvention, Integer32):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("blowfishCbc", 3),
          ("rc5R16B64Cbc", 4),
          ("tripleDesCbc", 5),
          ("castCbc", 6),
          ("aesCbc", 7),
          ("nsaCbc", 8),
          ("aesCbc128", 9),
          ("aesCbc192", 10),
          ("aesCbc256", 11),
          ("aesCtr", 12),
          ("aesCamelliaCbc", 13),
          ("rc4", 14),
          ("invalidAlg", 2147483647))
    )



class H3cIPsecAuthAlgoV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha1", 2),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5),
          ("invalidAlg", 2147483647))
    )



class H3cIPsecSaProtocolV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("ah", 2),
          ("esp", 3),
          ("ipcomp", 4))
    )



class H3cIPsecIDTypeV2(TextualConvention, Integer32):
    status = "current"
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("ipv4Addr", 1),
          ("fqdn", 2),
          ("userFqdn", 3),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrSubnet", 6),
          ("ipv4AddrRange", 7),
          ("ipv6AddrRange", 8),
          ("derAsn1Dn", 9),
          ("derAsn1Gn", 10),
          ("keyId", 11))
    )



class H3cIPsecTrafficTypeV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrSubnet", 6),
          ("ipv4AddrRange", 7),
          ("ipv6AddrRange", 8))
    )



class H3cIPsecNegoTypeV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2),
          ("invalidType", 2147483647))
    )



class H3cIPsecTunnelStateV2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("timeout", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cIPsecObjectsV2_ObjectIdentity = ObjectIdentity
h3cIPsecObjectsV2 = _H3cIPsecObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1)
)
_H3cIPsecScalarObjectsV2_ObjectIdentity = ObjectIdentity
h3cIPsecScalarObjectsV2 = _H3cIPsecScalarObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 1)
)
_H3cIPsecMIBVersion_Type = DisplayString
_H3cIPsecMIBVersion_Object = MibScalar
h3cIPsecMIBVersion = _H3cIPsecMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 1, 1),
    _H3cIPsecMIBVersion_Type()
)
h3cIPsecMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecMIBVersion.setStatus("current")
_H3cIPsecTunnelV2Table_Object = MibTable
h3cIPsecTunnelV2Table = _H3cIPsecTunnelV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelV2Table.setStatus("current")
_H3cIPsecTunnelV2Entry_Object = MibTableRow
h3cIPsecTunnelV2Entry = _H3cIPsecTunnelV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1)
)
h3cIPsecTunnelV2Entry.setIndexNames(
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelV2Entry.setStatus("current")


class _H3cIPsecTunIndexV2_Type(Integer32):
    """Custom type h3cIPsecTunIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPsecTunIndexV2_Type.__name__ = "Integer32"
_H3cIPsecTunIndexV2_Object = MibTableColumn
h3cIPsecTunIndexV2 = _H3cIPsecTunIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 1),
    _H3cIPsecTunIndexV2_Type()
)
h3cIPsecTunIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecTunIndexV2.setStatus("current")
_H3cIPsecTunIfIndexV2_Type = InterfaceIndex
_H3cIPsecTunIfIndexV2_Object = MibTableColumn
h3cIPsecTunIfIndexV2 = _H3cIPsecTunIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 2),
    _H3cIPsecTunIfIndexV2_Type()
)
h3cIPsecTunIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIfIndexV2.setStatus("current")


class _H3cIPsecTunIKETunnelIndexV2_Type(Integer32):
    """Custom type h3cIPsecTunIKETunnelIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPsecTunIKETunnelIndexV2_Type.__name__ = "Integer32"
_H3cIPsecTunIKETunnelIndexV2_Object = MibTableColumn
h3cIPsecTunIKETunnelIndexV2 = _H3cIPsecTunIKETunnelIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 3),
    _H3cIPsecTunIKETunnelIndexV2_Type()
)
h3cIPsecTunIKETunnelIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunnelIndexV2.setStatus("current")
_H3cIPsecTunIKETunLocalIDTypeV2_Type = H3cIPsecIDTypeV2
_H3cIPsecTunIKETunLocalIDTypeV2_Object = MibTableColumn
h3cIPsecTunIKETunLocalIDTypeV2 = _H3cIPsecTunIKETunLocalIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 4),
    _H3cIPsecTunIKETunLocalIDTypeV2_Type()
)
h3cIPsecTunIKETunLocalIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunLocalIDTypeV2.setStatus("current")
_H3cIPsecTunIKETunLocalIDVal1V2_Type = DisplayString
_H3cIPsecTunIKETunLocalIDVal1V2_Object = MibTableColumn
h3cIPsecTunIKETunLocalIDVal1V2 = _H3cIPsecTunIKETunLocalIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 5),
    _H3cIPsecTunIKETunLocalIDVal1V2_Type()
)
h3cIPsecTunIKETunLocalIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunLocalIDVal1V2.setStatus("current")
_H3cIPsecTunIKETunLocalIDVal2V2_Type = DisplayString
_H3cIPsecTunIKETunLocalIDVal2V2_Object = MibTableColumn
h3cIPsecTunIKETunLocalIDVal2V2 = _H3cIPsecTunIKETunLocalIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 6),
    _H3cIPsecTunIKETunLocalIDVal2V2_Type()
)
h3cIPsecTunIKETunLocalIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunLocalIDVal2V2.setStatus("current")
_H3cIPsecTunIKETunRemoteIDTypeV2_Type = H3cIPsecIDTypeV2
_H3cIPsecTunIKETunRemoteIDTypeV2_Object = MibTableColumn
h3cIPsecTunIKETunRemoteIDTypeV2 = _H3cIPsecTunIKETunRemoteIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 7),
    _H3cIPsecTunIKETunRemoteIDTypeV2_Type()
)
h3cIPsecTunIKETunRemoteIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunRemoteIDTypeV2.setStatus("current")
_H3cIPsecTunIKETunRemoteIDVal1V2_Type = DisplayString
_H3cIPsecTunIKETunRemoteIDVal1V2_Object = MibTableColumn
h3cIPsecTunIKETunRemoteIDVal1V2 = _H3cIPsecTunIKETunRemoteIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 8),
    _H3cIPsecTunIKETunRemoteIDVal1V2_Type()
)
h3cIPsecTunIKETunRemoteIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunRemoteIDVal1V2.setStatus("current")
_H3cIPsecTunIKETunRemoteIDVal2V2_Type = DisplayString
_H3cIPsecTunIKETunRemoteIDVal2V2_Object = MibTableColumn
h3cIPsecTunIKETunRemoteIDVal2V2 = _H3cIPsecTunIKETunRemoteIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 9),
    _H3cIPsecTunIKETunRemoteIDVal2V2_Type()
)
h3cIPsecTunIKETunRemoteIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunIKETunRemoteIDVal2V2.setStatus("current")
_H3cIPsecTunLocalAddrTypeV2_Type = InetAddressType
_H3cIPsecTunLocalAddrTypeV2_Object = MibTableColumn
h3cIPsecTunLocalAddrTypeV2 = _H3cIPsecTunLocalAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 10),
    _H3cIPsecTunLocalAddrTypeV2_Type()
)
h3cIPsecTunLocalAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunLocalAddrTypeV2.setStatus("current")
_H3cIPsecTunLocalAddrV2_Type = InetAddress
_H3cIPsecTunLocalAddrV2_Object = MibTableColumn
h3cIPsecTunLocalAddrV2 = _H3cIPsecTunLocalAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 11),
    _H3cIPsecTunLocalAddrV2_Type()
)
h3cIPsecTunLocalAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunLocalAddrV2.setStatus("current")
_H3cIPsecTunRemoteAddrTypeV2_Type = InetAddressType
_H3cIPsecTunRemoteAddrTypeV2_Object = MibTableColumn
h3cIPsecTunRemoteAddrTypeV2 = _H3cIPsecTunRemoteAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 12),
    _H3cIPsecTunRemoteAddrTypeV2_Type()
)
h3cIPsecTunRemoteAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunRemoteAddrTypeV2.setStatus("current")
_H3cIPsecTunRemoteAddrV2_Type = InetAddress
_H3cIPsecTunRemoteAddrV2_Object = MibTableColumn
h3cIPsecTunRemoteAddrV2 = _H3cIPsecTunRemoteAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 13),
    _H3cIPsecTunRemoteAddrV2_Type()
)
h3cIPsecTunRemoteAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunRemoteAddrV2.setStatus("current")
_H3cIPsecTunKeyTypeV2_Type = H3cIPsecNegoTypeV2
_H3cIPsecTunKeyTypeV2_Object = MibTableColumn
h3cIPsecTunKeyTypeV2 = _H3cIPsecTunKeyTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 14),
    _H3cIPsecTunKeyTypeV2_Type()
)
h3cIPsecTunKeyTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunKeyTypeV2.setStatus("current")
_H3cIPsecTunEncapModeV2_Type = H3cIPsecEncapModeV2
_H3cIPsecTunEncapModeV2_Object = MibTableColumn
h3cIPsecTunEncapModeV2 = _H3cIPsecTunEncapModeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 15),
    _H3cIPsecTunEncapModeV2_Type()
)
h3cIPsecTunEncapModeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunEncapModeV2.setStatus("current")


class _H3cIPsecTunInitiatorV2_Type(Integer32):
    """Custom type h3cIPsecTunInitiatorV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("none", 2147483647))
    )


_H3cIPsecTunInitiatorV2_Type.__name__ = "Integer32"
_H3cIPsecTunInitiatorV2_Object = MibTableColumn
h3cIPsecTunInitiatorV2 = _H3cIPsecTunInitiatorV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 16),
    _H3cIPsecTunInitiatorV2_Type()
)
h3cIPsecTunInitiatorV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInitiatorV2.setStatus("current")
_H3cIPsecTunLifeSizeV2_Type = Gauge32
_H3cIPsecTunLifeSizeV2_Object = MibTableColumn
h3cIPsecTunLifeSizeV2 = _H3cIPsecTunLifeSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 17),
    _H3cIPsecTunLifeSizeV2_Type()
)
h3cIPsecTunLifeSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunLifeSizeV2.setStatus("current")


class _H3cIPsecTunLifeTimeV2_Type(Integer32):
    """Custom type h3cIPsecTunLifeTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPsecTunLifeTimeV2_Type.__name__ = "Integer32"
_H3cIPsecTunLifeTimeV2_Object = MibTableColumn
h3cIPsecTunLifeTimeV2 = _H3cIPsecTunLifeTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 18),
    _H3cIPsecTunLifeTimeV2_Type()
)
h3cIPsecTunLifeTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunLifeTimeV2.setStatus("current")


class _H3cIPsecTunRemainTimeV2_Type(Integer32):
    """Custom type h3cIPsecTunRemainTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIPsecTunRemainTimeV2_Type.__name__ = "Integer32"
_H3cIPsecTunRemainTimeV2_Object = MibTableColumn
h3cIPsecTunRemainTimeV2 = _H3cIPsecTunRemainTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 19),
    _H3cIPsecTunRemainTimeV2_Type()
)
h3cIPsecTunRemainTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunRemainTimeV2.setStatus("current")


class _H3cIPsecTunActiveTimeV2_Type(Integer32):
    """Custom type h3cIPsecTunActiveTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIPsecTunActiveTimeV2_Type.__name__ = "Integer32"
_H3cIPsecTunActiveTimeV2_Object = MibTableColumn
h3cIPsecTunActiveTimeV2 = _H3cIPsecTunActiveTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 20),
    _H3cIPsecTunActiveTimeV2_Type()
)
h3cIPsecTunActiveTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunActiveTimeV2.setStatus("current")
_H3cIPsecTunRemainSizeV2_Type = Gauge32
_H3cIPsecTunRemainSizeV2_Object = MibTableColumn
h3cIPsecTunRemainSizeV2 = _H3cIPsecTunRemainSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 21),
    _H3cIPsecTunRemainSizeV2_Type()
)
h3cIPsecTunRemainSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunRemainSizeV2.setStatus("current")
_H3cIPsecTunTotalRefreshesV2_Type = Counter32
_H3cIPsecTunTotalRefreshesV2_Object = MibTableColumn
h3cIPsecTunTotalRefreshesV2 = _H3cIPsecTunTotalRefreshesV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 22),
    _H3cIPsecTunTotalRefreshesV2_Type()
)
h3cIPsecTunTotalRefreshesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunTotalRefreshesV2.setStatus("current")
_H3cIPsecTunCurrentSaInstancesV2_Type = Gauge32
_H3cIPsecTunCurrentSaInstancesV2_Object = MibTableColumn
h3cIPsecTunCurrentSaInstancesV2 = _H3cIPsecTunCurrentSaInstancesV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 23),
    _H3cIPsecTunCurrentSaInstancesV2_Type()
)
h3cIPsecTunCurrentSaInstancesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunCurrentSaInstancesV2.setStatus("current")
_H3cIPsecTunInSaEncryptAlgoV2_Type = H3cIPsecEncryptAlgoV2
_H3cIPsecTunInSaEncryptAlgoV2_Object = MibTableColumn
h3cIPsecTunInSaEncryptAlgoV2 = _H3cIPsecTunInSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 24),
    _H3cIPsecTunInSaEncryptAlgoV2_Type()
)
h3cIPsecTunInSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInSaEncryptAlgoV2.setStatus("current")
_H3cIPsecTunInSaAhAuthAlgoV2_Type = H3cIPsecAuthAlgoV2
_H3cIPsecTunInSaAhAuthAlgoV2_Object = MibTableColumn
h3cIPsecTunInSaAhAuthAlgoV2 = _H3cIPsecTunInSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 25),
    _H3cIPsecTunInSaAhAuthAlgoV2_Type()
)
h3cIPsecTunInSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInSaAhAuthAlgoV2.setStatus("current")
_H3cIPsecTunInSaEspAuthAlgoV2_Type = H3cIPsecAuthAlgoV2
_H3cIPsecTunInSaEspAuthAlgoV2_Object = MibTableColumn
h3cIPsecTunInSaEspAuthAlgoV2 = _H3cIPsecTunInSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 26),
    _H3cIPsecTunInSaEspAuthAlgoV2_Type()
)
h3cIPsecTunInSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInSaEspAuthAlgoV2.setStatus("current")
_H3cIPsecTunDiffHellmanGrpV2_Type = H3cIPsecDiffHellmanGrpV2
_H3cIPsecTunDiffHellmanGrpV2_Object = MibTableColumn
h3cIPsecTunDiffHellmanGrpV2 = _H3cIPsecTunDiffHellmanGrpV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 27),
    _H3cIPsecTunDiffHellmanGrpV2_Type()
)
h3cIPsecTunDiffHellmanGrpV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunDiffHellmanGrpV2.setStatus("current")
_H3cIPsecTunOutSaEncryptAlgoV2_Type = H3cIPsecEncryptAlgoV2
_H3cIPsecTunOutSaEncryptAlgoV2_Object = MibTableColumn
h3cIPsecTunOutSaEncryptAlgoV2 = _H3cIPsecTunOutSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 28),
    _H3cIPsecTunOutSaEncryptAlgoV2_Type()
)
h3cIPsecTunOutSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutSaEncryptAlgoV2.setStatus("current")
_H3cIPsecTunOutSaAhAuthAlgoV2_Type = H3cIPsecAuthAlgoV2
_H3cIPsecTunOutSaAhAuthAlgoV2_Object = MibTableColumn
h3cIPsecTunOutSaAhAuthAlgoV2 = _H3cIPsecTunOutSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 29),
    _H3cIPsecTunOutSaAhAuthAlgoV2_Type()
)
h3cIPsecTunOutSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutSaAhAuthAlgoV2.setStatus("current")
_H3cIPsecTunOutSaEspAuthAlgoV2_Type = H3cIPsecAuthAlgoV2
_H3cIPsecTunOutSaEspAuthAlgoV2_Object = MibTableColumn
h3cIPsecTunOutSaEspAuthAlgoV2 = _H3cIPsecTunOutSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 30),
    _H3cIPsecTunOutSaEspAuthAlgoV2_Type()
)
h3cIPsecTunOutSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutSaEspAuthAlgoV2.setStatus("current")


class _H3cIPsecTunPolicyNameV2_Type(OctetString):
    """Custom type h3cIPsecTunPolicyNameV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cIPsecTunPolicyNameV2_Type.__name__ = "OctetString"
_H3cIPsecTunPolicyNameV2_Object = MibTableColumn
h3cIPsecTunPolicyNameV2 = _H3cIPsecTunPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 31),
    _H3cIPsecTunPolicyNameV2_Type()
)
h3cIPsecTunPolicyNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunPolicyNameV2.setStatus("current")


class _H3cIPsecTunPolicyNumV2_Type(Integer32):
    """Custom type h3cIPsecTunPolicyNumV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPsecTunPolicyNumV2_Type.__name__ = "Integer32"
_H3cIPsecTunPolicyNumV2_Object = MibTableColumn
h3cIPsecTunPolicyNumV2 = _H3cIPsecTunPolicyNumV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 32),
    _H3cIPsecTunPolicyNumV2_Type()
)
h3cIPsecTunPolicyNumV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunPolicyNumV2.setStatus("current")


class _H3cIPsecTunStatusV2_Type(Integer32):
    """Custom type h3cIPsecTunStatusV2 based on Integer32"""
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
        *(("initial", 1),
          ("ready", 2),
          ("rekeyed", 3),
          ("closed", 4))
    )


_H3cIPsecTunStatusV2_Type.__name__ = "Integer32"
_H3cIPsecTunStatusV2_Object = MibTableColumn
h3cIPsecTunStatusV2 = _H3cIPsecTunStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 33),
    _H3cIPsecTunStatusV2_Type()
)
h3cIPsecTunStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunStatusV2.setStatus("current")


class _H3cIPsecTunPolicyDescriptionV2_Type(OctetString):
    """Custom type h3cIPsecTunPolicyDescriptionV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cIPsecTunPolicyDescriptionV2_Type.__name__ = "OctetString"
_H3cIPsecTunPolicyDescriptionV2_Object = MibTableColumn
h3cIPsecTunPolicyDescriptionV2 = _H3cIPsecTunPolicyDescriptionV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 2, 1, 34),
    _H3cIPsecTunPolicyDescriptionV2_Type()
)
h3cIPsecTunPolicyDescriptionV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunPolicyDescriptionV2.setStatus("current")
_H3cIPsecTunnelStatV2Table_Object = MibTable
h3cIPsecTunnelStatV2Table = _H3cIPsecTunnelStatV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStatV2Table.setStatus("current")
_H3cIPsecTunnelStatV2Entry_Object = MibTableRow
h3cIPsecTunnelStatV2Entry = _H3cIPsecTunnelStatV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1)
)
h3cIPsecTunnelStatV2Entry.setIndexNames(
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStatV2Entry.setStatus("current")
_H3cIPsecTunInOctetsV2_Type = Counter64
_H3cIPsecTunInOctetsV2_Object = MibTableColumn
h3cIPsecTunInOctetsV2 = _H3cIPsecTunInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 1),
    _H3cIPsecTunInOctetsV2_Type()
)
h3cIPsecTunInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInOctetsV2.setStatus("current")
_H3cIPsecTunInDecompOctetsV2_Type = Counter64
_H3cIPsecTunInDecompOctetsV2_Object = MibTableColumn
h3cIPsecTunInDecompOctetsV2 = _H3cIPsecTunInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 2),
    _H3cIPsecTunInDecompOctetsV2_Type()
)
h3cIPsecTunInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDecompOctetsV2.setStatus("current")
_H3cIPsecTunInPktsV2_Type = Counter64
_H3cIPsecTunInPktsV2_Object = MibTableColumn
h3cIPsecTunInPktsV2 = _H3cIPsecTunInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 3),
    _H3cIPsecTunInPktsV2_Type()
)
h3cIPsecTunInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInPktsV2.setStatus("current")
_H3cIPsecTunInDropPktsV2_Type = Counter64
_H3cIPsecTunInDropPktsV2_Object = MibTableColumn
h3cIPsecTunInDropPktsV2 = _H3cIPsecTunInDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 4),
    _H3cIPsecTunInDropPktsV2_Type()
)
h3cIPsecTunInDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDropPktsV2.setStatus("current")
_H3cIPsecTunInReplayDropPktsV2_Type = Counter64
_H3cIPsecTunInReplayDropPktsV2_Object = MibTableColumn
h3cIPsecTunInReplayDropPktsV2 = _H3cIPsecTunInReplayDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 5),
    _H3cIPsecTunInReplayDropPktsV2_Type()
)
h3cIPsecTunInReplayDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInReplayDropPktsV2.setStatus("current")
_H3cIPsecTunInAuthFailsV2_Type = Counter64
_H3cIPsecTunInAuthFailsV2_Object = MibTableColumn
h3cIPsecTunInAuthFailsV2 = _H3cIPsecTunInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 6),
    _H3cIPsecTunInAuthFailsV2_Type()
)
h3cIPsecTunInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInAuthFailsV2.setStatus("current")
_H3cIPsecTunInDecryptFailsV2_Type = Counter64
_H3cIPsecTunInDecryptFailsV2_Object = MibTableColumn
h3cIPsecTunInDecryptFailsV2 = _H3cIPsecTunInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 7),
    _H3cIPsecTunInDecryptFailsV2_Type()
)
h3cIPsecTunInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDecryptFailsV2.setStatus("current")
_H3cIPsecTunOutOctetsV2_Type = Counter64
_H3cIPsecTunOutOctetsV2_Object = MibTableColumn
h3cIPsecTunOutOctetsV2 = _H3cIPsecTunOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 8),
    _H3cIPsecTunOutOctetsV2_Type()
)
h3cIPsecTunOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutOctetsV2.setStatus("current")
_H3cIPsecTunOutUncompOctetsV2_Type = Counter64
_H3cIPsecTunOutUncompOctetsV2_Object = MibTableColumn
h3cIPsecTunOutUncompOctetsV2 = _H3cIPsecTunOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 9),
    _H3cIPsecTunOutUncompOctetsV2_Type()
)
h3cIPsecTunOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutUncompOctetsV2.setStatus("current")
_H3cIPsecTunOutPktsV2_Type = Counter64
_H3cIPsecTunOutPktsV2_Object = MibTableColumn
h3cIPsecTunOutPktsV2 = _H3cIPsecTunOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 10),
    _H3cIPsecTunOutPktsV2_Type()
)
h3cIPsecTunOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutPktsV2.setStatus("current")
_H3cIPsecTunOutDropPktsV2_Type = Counter64
_H3cIPsecTunOutDropPktsV2_Object = MibTableColumn
h3cIPsecTunOutDropPktsV2 = _H3cIPsecTunOutDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 11),
    _H3cIPsecTunOutDropPktsV2_Type()
)
h3cIPsecTunOutDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutDropPktsV2.setStatus("current")
_H3cIPsecTunOutEncryptFailsV2_Type = Counter64
_H3cIPsecTunOutEncryptFailsV2_Object = MibTableColumn
h3cIPsecTunOutEncryptFailsV2 = _H3cIPsecTunOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 12),
    _H3cIPsecTunOutEncryptFailsV2_Type()
)
h3cIPsecTunOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutEncryptFailsV2.setStatus("current")
_H3cIPsecTunNoMemoryDropPktsV2_Type = Counter64
_H3cIPsecTunNoMemoryDropPktsV2_Object = MibTableColumn
h3cIPsecTunNoMemoryDropPktsV2 = _H3cIPsecTunNoMemoryDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 13),
    _H3cIPsecTunNoMemoryDropPktsV2_Type()
)
h3cIPsecTunNoMemoryDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunNoMemoryDropPktsV2.setStatus("current")
_H3cIPsecTunQueueFullDropPktsV2_Type = Counter64
_H3cIPsecTunQueueFullDropPktsV2_Object = MibTableColumn
h3cIPsecTunQueueFullDropPktsV2 = _H3cIPsecTunQueueFullDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 14),
    _H3cIPsecTunQueueFullDropPktsV2_Type()
)
h3cIPsecTunQueueFullDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunQueueFullDropPktsV2.setStatus("current")
_H3cIPsecTunInvalidLenDropPktsV2_Type = Counter64
_H3cIPsecTunInvalidLenDropPktsV2_Object = MibTableColumn
h3cIPsecTunInvalidLenDropPktsV2 = _H3cIPsecTunInvalidLenDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 15),
    _H3cIPsecTunInvalidLenDropPktsV2_Type()
)
h3cIPsecTunInvalidLenDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInvalidLenDropPktsV2.setStatus("current")
_H3cIPsecTunTooLongDropPktsV2_Type = Counter64
_H3cIPsecTunTooLongDropPktsV2_Object = MibTableColumn
h3cIPsecTunTooLongDropPktsV2 = _H3cIPsecTunTooLongDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 16),
    _H3cIPsecTunTooLongDropPktsV2_Type()
)
h3cIPsecTunTooLongDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunTooLongDropPktsV2.setStatus("current")
_H3cIPsecTunInvalidSaDropPktsV2_Type = Counter64
_H3cIPsecTunInvalidSaDropPktsV2_Object = MibTableColumn
h3cIPsecTunInvalidSaDropPktsV2 = _H3cIPsecTunInvalidSaDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 3, 1, 17),
    _H3cIPsecTunInvalidSaDropPktsV2_Type()
)
h3cIPsecTunInvalidSaDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInvalidSaDropPktsV2.setStatus("current")
_H3cIPsecSaV2Table_Object = MibTable
h3cIPsecSaV2Table = _H3cIPsecSaV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIPsecSaV2Table.setStatus("current")
_H3cIPsecSaV2Entry_Object = MibTableRow
h3cIPsecSaV2Entry = _H3cIPsecSaV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1)
)
h3cIPsecSaV2Entry.setIndexNames(
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaIndexV2"),
)
if mibBuilder.loadTexts:
    h3cIPsecSaV2Entry.setStatus("current")


class _H3cIPsecSaIndexV2_Type(Integer32):
    """Custom type h3cIPsecSaIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPsecSaIndexV2_Type.__name__ = "Integer32"
_H3cIPsecSaIndexV2_Object = MibTableColumn
h3cIPsecSaIndexV2 = _H3cIPsecSaIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 1),
    _H3cIPsecSaIndexV2_Type()
)
h3cIPsecSaIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecSaIndexV2.setStatus("current")


class _H3cIPsecSaDirectionV2_Type(Integer32):
    """Custom type h3cIPsecSaDirectionV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_H3cIPsecSaDirectionV2_Type.__name__ = "Integer32"
_H3cIPsecSaDirectionV2_Object = MibTableColumn
h3cIPsecSaDirectionV2 = _H3cIPsecSaDirectionV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 2),
    _H3cIPsecSaDirectionV2_Type()
)
h3cIPsecSaDirectionV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaDirectionV2.setStatus("current")


class _H3cIPsecSaSpiValueV2_Type(Unsigned32):
    """Custom type h3cIPsecSaSpiValueV2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cIPsecSaSpiValueV2_Type.__name__ = "Unsigned32"
_H3cIPsecSaSpiValueV2_Object = MibTableColumn
h3cIPsecSaSpiValueV2 = _H3cIPsecSaSpiValueV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 3),
    _H3cIPsecSaSpiValueV2_Type()
)
h3cIPsecSaSpiValueV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaSpiValueV2.setStatus("current")
_H3cIPsecSaSecProtocolV2_Type = H3cIPsecSaProtocolV2
_H3cIPsecSaSecProtocolV2_Object = MibTableColumn
h3cIPsecSaSecProtocolV2 = _H3cIPsecSaSecProtocolV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 4),
    _H3cIPsecSaSecProtocolV2_Type()
)
h3cIPsecSaSecProtocolV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaSecProtocolV2.setStatus("current")
_H3cIPsecSaEncryptAlgoV2_Type = H3cIPsecEncryptAlgoV2
_H3cIPsecSaEncryptAlgoV2_Object = MibTableColumn
h3cIPsecSaEncryptAlgoV2 = _H3cIPsecSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 5),
    _H3cIPsecSaEncryptAlgoV2_Type()
)
h3cIPsecSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaEncryptAlgoV2.setStatus("current")
_H3cIPsecSaAuthAlgoV2_Type = H3cIPsecAuthAlgoV2
_H3cIPsecSaAuthAlgoV2_Object = MibTableColumn
h3cIPsecSaAuthAlgoV2 = _H3cIPsecSaAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 6),
    _H3cIPsecSaAuthAlgoV2_Type()
)
h3cIPsecSaAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaAuthAlgoV2.setStatus("current")


class _H3cIPsecSaStatusV2_Type(Integer32):
    """Custom type h3cIPsecSaStatusV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expiring", 2))
    )


_H3cIPsecSaStatusV2_Type.__name__ = "Integer32"
_H3cIPsecSaStatusV2_Object = MibTableColumn
h3cIPsecSaStatusV2 = _H3cIPsecSaStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 4, 1, 7),
    _H3cIPsecSaStatusV2_Type()
)
h3cIPsecSaStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecSaStatusV2.setStatus("current")
_H3cIPsecTrafficV2Table_Object = MibTable
h3cIPsecTrafficV2Table = _H3cIPsecTrafficV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5)
)
if mibBuilder.loadTexts:
    h3cIPsecTrafficV2Table.setStatus("current")
_H3cIPsecTrafficV2Entry_Object = MibTableRow
h3cIPsecTrafficV2Entry = _H3cIPsecTrafficV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1)
)
h3cIPsecTrafficV2Entry.setIndexNames(
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    h3cIPsecTrafficV2Entry.setStatus("current")
_H3cIPsecTrafficLocalTypeV2_Type = H3cIPsecTrafficTypeV2
_H3cIPsecTrafficLocalTypeV2_Object = MibTableColumn
h3cIPsecTrafficLocalTypeV2 = _H3cIPsecTrafficLocalTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 1),
    _H3cIPsecTrafficLocalTypeV2_Type()
)
h3cIPsecTrafficLocalTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalTypeV2.setStatus("current")
_H3cIPsecTrafficLocalAddr1TypeV2_Type = InetAddressType
_H3cIPsecTrafficLocalAddr1TypeV2_Object = MibTableColumn
h3cIPsecTrafficLocalAddr1TypeV2 = _H3cIPsecTrafficLocalAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 2),
    _H3cIPsecTrafficLocalAddr1TypeV2_Type()
)
h3cIPsecTrafficLocalAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalAddr1TypeV2.setStatus("current")
_H3cIPsecTrafficLocalAddr1V2_Type = InetAddress
_H3cIPsecTrafficLocalAddr1V2_Object = MibTableColumn
h3cIPsecTrafficLocalAddr1V2 = _H3cIPsecTrafficLocalAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 3),
    _H3cIPsecTrafficLocalAddr1V2_Type()
)
h3cIPsecTrafficLocalAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalAddr1V2.setStatus("current")
_H3cIPsecTrafficLocalAddr2TypeV2_Type = InetAddressType
_H3cIPsecTrafficLocalAddr2TypeV2_Object = MibTableColumn
h3cIPsecTrafficLocalAddr2TypeV2 = _H3cIPsecTrafficLocalAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 4),
    _H3cIPsecTrafficLocalAddr2TypeV2_Type()
)
h3cIPsecTrafficLocalAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalAddr2TypeV2.setStatus("current")
_H3cIPsecTrafficLocalAddr2V2_Type = InetAddress
_H3cIPsecTrafficLocalAddr2V2_Object = MibTableColumn
h3cIPsecTrafficLocalAddr2V2 = _H3cIPsecTrafficLocalAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 5),
    _H3cIPsecTrafficLocalAddr2V2_Type()
)
h3cIPsecTrafficLocalAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalAddr2V2.setStatus("current")


class _H3cIPsecTrafficLocalProtocol1V2_Type(Integer32):
    """Custom type h3cIPsecTrafficLocalProtocol1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPsecTrafficLocalProtocol1V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficLocalProtocol1V2_Object = MibTableColumn
h3cIPsecTrafficLocalProtocol1V2 = _H3cIPsecTrafficLocalProtocol1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 6),
    _H3cIPsecTrafficLocalProtocol1V2_Type()
)
h3cIPsecTrafficLocalProtocol1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalProtocol1V2.setStatus("current")


class _H3cIPsecTrafficLocalProtocol2V2_Type(Integer32):
    """Custom type h3cIPsecTrafficLocalProtocol2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPsecTrafficLocalProtocol2V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficLocalProtocol2V2_Object = MibTableColumn
h3cIPsecTrafficLocalProtocol2V2 = _H3cIPsecTrafficLocalProtocol2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 7),
    _H3cIPsecTrafficLocalProtocol2V2_Type()
)
h3cIPsecTrafficLocalProtocol2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalProtocol2V2.setStatus("current")


class _H3cIPsecTrafficLocalPort1V2_Type(Integer32):
    """Custom type h3cIPsecTrafficLocalPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPsecTrafficLocalPort1V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficLocalPort1V2_Object = MibTableColumn
h3cIPsecTrafficLocalPort1V2 = _H3cIPsecTrafficLocalPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 8),
    _H3cIPsecTrafficLocalPort1V2_Type()
)
h3cIPsecTrafficLocalPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalPort1V2.setStatus("current")


class _H3cIPsecTrafficLocalPort2V2_Type(Integer32):
    """Custom type h3cIPsecTrafficLocalPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPsecTrafficLocalPort2V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficLocalPort2V2_Object = MibTableColumn
h3cIPsecTrafficLocalPort2V2 = _H3cIPsecTrafficLocalPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 9),
    _H3cIPsecTrafficLocalPort2V2_Type()
)
h3cIPsecTrafficLocalPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficLocalPort2V2.setStatus("current")
_H3cIPsecTrafficRemoteTypeV2_Type = H3cIPsecTrafficTypeV2
_H3cIPsecTrafficRemoteTypeV2_Object = MibTableColumn
h3cIPsecTrafficRemoteTypeV2 = _H3cIPsecTrafficRemoteTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 10),
    _H3cIPsecTrafficRemoteTypeV2_Type()
)
h3cIPsecTrafficRemoteTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemoteTypeV2.setStatus("current")
_H3cIPsecTrafficRemAddr1TypeV2_Type = InetAddressType
_H3cIPsecTrafficRemAddr1TypeV2_Object = MibTableColumn
h3cIPsecTrafficRemAddr1TypeV2 = _H3cIPsecTrafficRemAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 11),
    _H3cIPsecTrafficRemAddr1TypeV2_Type()
)
h3cIPsecTrafficRemAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemAddr1TypeV2.setStatus("current")
_H3cIPsecTrafficRemAddr1V2_Type = InetAddress
_H3cIPsecTrafficRemAddr1V2_Object = MibTableColumn
h3cIPsecTrafficRemAddr1V2 = _H3cIPsecTrafficRemAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 12),
    _H3cIPsecTrafficRemAddr1V2_Type()
)
h3cIPsecTrafficRemAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemAddr1V2.setStatus("current")
_H3cIPsecTrafficRemAddr2TypeV2_Type = InetAddressType
_H3cIPsecTrafficRemAddr2TypeV2_Object = MibTableColumn
h3cIPsecTrafficRemAddr2TypeV2 = _H3cIPsecTrafficRemAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 13),
    _H3cIPsecTrafficRemAddr2TypeV2_Type()
)
h3cIPsecTrafficRemAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemAddr2TypeV2.setStatus("current")
_H3cIPsecTrafficRemAddr2V2_Type = InetAddress
_H3cIPsecTrafficRemAddr2V2_Object = MibTableColumn
h3cIPsecTrafficRemAddr2V2 = _H3cIPsecTrafficRemAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 14),
    _H3cIPsecTrafficRemAddr2V2_Type()
)
h3cIPsecTrafficRemAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemAddr2V2.setStatus("current")


class _H3cIPsecTrafficRemoPro1V2_Type(Integer32):
    """Custom type h3cIPsecTrafficRemoPro1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPsecTrafficRemoPro1V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficRemoPro1V2_Object = MibTableColumn
h3cIPsecTrafficRemoPro1V2 = _H3cIPsecTrafficRemoPro1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 15),
    _H3cIPsecTrafficRemoPro1V2_Type()
)
h3cIPsecTrafficRemoPro1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemoPro1V2.setStatus("current")


class _H3cIPsecTrafficRemoPro2V2_Type(Integer32):
    """Custom type h3cIPsecTrafficRemoPro2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPsecTrafficRemoPro2V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficRemoPro2V2_Object = MibTableColumn
h3cIPsecTrafficRemoPro2V2 = _H3cIPsecTrafficRemoPro2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 16),
    _H3cIPsecTrafficRemoPro2V2_Type()
)
h3cIPsecTrafficRemoPro2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemoPro2V2.setStatus("current")


class _H3cIPsecTrafficRemPort1V2_Type(Integer32):
    """Custom type h3cIPsecTrafficRemPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPsecTrafficRemPort1V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficRemPort1V2_Object = MibTableColumn
h3cIPsecTrafficRemPort1V2 = _H3cIPsecTrafficRemPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 17),
    _H3cIPsecTrafficRemPort1V2_Type()
)
h3cIPsecTrafficRemPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemPort1V2.setStatus("current")


class _H3cIPsecTrafficRemPort2V2_Type(Integer32):
    """Custom type h3cIPsecTrafficRemPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPsecTrafficRemPort2V2_Type.__name__ = "Integer32"
_H3cIPsecTrafficRemPort2V2_Object = MibTableColumn
h3cIPsecTrafficRemPort2V2 = _H3cIPsecTrafficRemPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 5, 1, 18),
    _H3cIPsecTrafficRemPort2V2_Type()
)
h3cIPsecTrafficRemPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTrafficRemPort2V2.setStatus("current")
_H3cIPsecGlobalStatsV2_ObjectIdentity = ObjectIdentity
h3cIPsecGlobalStatsV2 = _H3cIPsecGlobalStatsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6)
)
_H3cIPsecGlobalActiveTunnelsV2_Type = Gauge32
_H3cIPsecGlobalActiveTunnelsV2_Object = MibScalar
h3cIPsecGlobalActiveTunnelsV2 = _H3cIPsecGlobalActiveTunnelsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 1),
    _H3cIPsecGlobalActiveTunnelsV2_Type()
)
h3cIPsecGlobalActiveTunnelsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalActiveTunnelsV2.setStatus("current")
_H3cIPsecGlobalActiveSasV2_Type = Gauge32
_H3cIPsecGlobalActiveSasV2_Object = MibScalar
h3cIPsecGlobalActiveSasV2 = _H3cIPsecGlobalActiveSasV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 2),
    _H3cIPsecGlobalActiveSasV2_Type()
)
h3cIPsecGlobalActiveSasV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalActiveSasV2.setStatus("current")
_H3cIPsecGlobalInOctetsV2_Type = Counter64
_H3cIPsecGlobalInOctetsV2_Object = MibScalar
h3cIPsecGlobalInOctetsV2 = _H3cIPsecGlobalInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 3),
    _H3cIPsecGlobalInOctetsV2_Type()
)
h3cIPsecGlobalInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInOctetsV2.setStatus("current")
_H3cIPsecGlobalInDecompOctetsV2_Type = Counter64
_H3cIPsecGlobalInDecompOctetsV2_Object = MibScalar
h3cIPsecGlobalInDecompOctetsV2 = _H3cIPsecGlobalInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 4),
    _H3cIPsecGlobalInDecompOctetsV2_Type()
)
h3cIPsecGlobalInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInDecompOctetsV2.setStatus("current")
_H3cIPsecGlobalInPktsV2_Type = Counter64
_H3cIPsecGlobalInPktsV2_Object = MibScalar
h3cIPsecGlobalInPktsV2 = _H3cIPsecGlobalInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 5),
    _H3cIPsecGlobalInPktsV2_Type()
)
h3cIPsecGlobalInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInPktsV2.setStatus("current")
_H3cIPsecGlobalInDropsV2_Type = Counter64
_H3cIPsecGlobalInDropsV2_Object = MibScalar
h3cIPsecGlobalInDropsV2 = _H3cIPsecGlobalInDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 6),
    _H3cIPsecGlobalInDropsV2_Type()
)
h3cIPsecGlobalInDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInDropsV2.setStatus("current")
_H3cIPsecGlobalInReplayDropsV2_Type = Counter64
_H3cIPsecGlobalInReplayDropsV2_Object = MibScalar
h3cIPsecGlobalInReplayDropsV2 = _H3cIPsecGlobalInReplayDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 7),
    _H3cIPsecGlobalInReplayDropsV2_Type()
)
h3cIPsecGlobalInReplayDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInReplayDropsV2.setStatus("current")
_H3cIPsecGlobalInAuthFailsV2_Type = Counter64
_H3cIPsecGlobalInAuthFailsV2_Object = MibScalar
h3cIPsecGlobalInAuthFailsV2 = _H3cIPsecGlobalInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 8),
    _H3cIPsecGlobalInAuthFailsV2_Type()
)
h3cIPsecGlobalInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInAuthFailsV2.setStatus("current")
_H3cIPsecGlobalInDecryptFailsV2_Type = Counter64
_H3cIPsecGlobalInDecryptFailsV2_Object = MibScalar
h3cIPsecGlobalInDecryptFailsV2 = _H3cIPsecGlobalInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 9),
    _H3cIPsecGlobalInDecryptFailsV2_Type()
)
h3cIPsecGlobalInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInDecryptFailsV2.setStatus("current")
_H3cIPsecGlobalOutOctetsV2_Type = Counter64
_H3cIPsecGlobalOutOctetsV2_Object = MibScalar
h3cIPsecGlobalOutOctetsV2 = _H3cIPsecGlobalOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 10),
    _H3cIPsecGlobalOutOctetsV2_Type()
)
h3cIPsecGlobalOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalOutOctetsV2.setStatus("current")
_H3cIPsecGlobalOutUncompOctetsV2_Type = Counter64
_H3cIPsecGlobalOutUncompOctetsV2_Object = MibScalar
h3cIPsecGlobalOutUncompOctetsV2 = _H3cIPsecGlobalOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 11),
    _H3cIPsecGlobalOutUncompOctetsV2_Type()
)
h3cIPsecGlobalOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalOutUncompOctetsV2.setStatus("current")
_H3cIPsecGlobalOutPktsV2_Type = Counter64
_H3cIPsecGlobalOutPktsV2_Object = MibScalar
h3cIPsecGlobalOutPktsV2 = _H3cIPsecGlobalOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 12),
    _H3cIPsecGlobalOutPktsV2_Type()
)
h3cIPsecGlobalOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalOutPktsV2.setStatus("current")
_H3cIPsecGlobalOutDropsV2_Type = Counter64
_H3cIPsecGlobalOutDropsV2_Object = MibScalar
h3cIPsecGlobalOutDropsV2 = _H3cIPsecGlobalOutDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 13),
    _H3cIPsecGlobalOutDropsV2_Type()
)
h3cIPsecGlobalOutDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalOutDropsV2.setStatus("current")
_H3cIPsecGlobalOutEncryptFailsV2_Type = Counter64
_H3cIPsecGlobalOutEncryptFailsV2_Object = MibScalar
h3cIPsecGlobalOutEncryptFailsV2 = _H3cIPsecGlobalOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 14),
    _H3cIPsecGlobalOutEncryptFailsV2_Type()
)
h3cIPsecGlobalOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalOutEncryptFailsV2.setStatus("current")
_H3cIPsecGlobalNoMemoryDropsV2_Type = Counter64
_H3cIPsecGlobalNoMemoryDropsV2_Object = MibScalar
h3cIPsecGlobalNoMemoryDropsV2 = _H3cIPsecGlobalNoMemoryDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 15),
    _H3cIPsecGlobalNoMemoryDropsV2_Type()
)
h3cIPsecGlobalNoMemoryDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalNoMemoryDropsV2.setStatus("current")
_H3cIPsecGlobalNoFindSaDropsV2_Type = Counter64
_H3cIPsecGlobalNoFindSaDropsV2_Object = MibScalar
h3cIPsecGlobalNoFindSaDropsV2 = _H3cIPsecGlobalNoFindSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 16),
    _H3cIPsecGlobalNoFindSaDropsV2_Type()
)
h3cIPsecGlobalNoFindSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalNoFindSaDropsV2.setStatus("current")
_H3cIPsecGlobalQueueFullDropsV2_Type = Counter64
_H3cIPsecGlobalQueueFullDropsV2_Object = MibScalar
h3cIPsecGlobalQueueFullDropsV2 = _H3cIPsecGlobalQueueFullDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 17),
    _H3cIPsecGlobalQueueFullDropsV2_Type()
)
h3cIPsecGlobalQueueFullDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalQueueFullDropsV2.setStatus("current")
_H3cIPsecGlobalInvalidLenDropsV2_Type = Counter64
_H3cIPsecGlobalInvalidLenDropsV2_Object = MibScalar
h3cIPsecGlobalInvalidLenDropsV2 = _H3cIPsecGlobalInvalidLenDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 18),
    _H3cIPsecGlobalInvalidLenDropsV2_Type()
)
h3cIPsecGlobalInvalidLenDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInvalidLenDropsV2.setStatus("current")
_H3cIPsecGlobalTooLongDropsV2_Type = Counter64
_H3cIPsecGlobalTooLongDropsV2_Object = MibScalar
h3cIPsecGlobalTooLongDropsV2 = _H3cIPsecGlobalTooLongDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 19),
    _H3cIPsecGlobalTooLongDropsV2_Type()
)
h3cIPsecGlobalTooLongDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalTooLongDropsV2.setStatus("current")
_H3cIPsecGlobalInvalidSaDropsV2_Type = Counter64
_H3cIPsecGlobalInvalidSaDropsV2_Object = MibScalar
h3cIPsecGlobalInvalidSaDropsV2 = _H3cIPsecGlobalInvalidSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 6, 20),
    _H3cIPsecGlobalInvalidSaDropsV2_Type()
)
h3cIPsecGlobalInvalidSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecGlobalInvalidSaDropsV2.setStatus("current")
_H3cIPsecTrapObjectV2_ObjectIdentity = ObjectIdentity
h3cIPsecTrapObjectV2 = _H3cIPsecTrapObjectV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 7)
)


class _H3cIPsecPolicyNameV2_Type(OctetString):
    """Custom type h3cIPsecPolicyNameV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cIPsecPolicyNameV2_Type.__name__ = "OctetString"
_H3cIPsecPolicyNameV2_Object = MibScalar
h3cIPsecPolicyNameV2 = _H3cIPsecPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 7, 1),
    _H3cIPsecPolicyNameV2_Type()
)
h3cIPsecPolicyNameV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecPolicyNameV2.setStatus("current")
_H3cIPsecPolicySeqNumV2_Type = Integer32
_H3cIPsecPolicySeqNumV2_Object = MibScalar
h3cIPsecPolicySeqNumV2 = _H3cIPsecPolicySeqNumV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 7, 2),
    _H3cIPsecPolicySeqNumV2_Type()
)
h3cIPsecPolicySeqNumV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecPolicySeqNumV2.setStatus("current")
_H3cIPsecPolicySizeV2_Type = Integer32
_H3cIPsecPolicySizeV2_Object = MibScalar
h3cIPsecPolicySizeV2 = _H3cIPsecPolicySizeV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 7, 3),
    _H3cIPsecPolicySizeV2_Type()
)
h3cIPsecPolicySizeV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecPolicySizeV2.setStatus("current")
_H3cIPsecTrapCntlV2_ObjectIdentity = ObjectIdentity
h3cIPsecTrapCntlV2 = _H3cIPsecTrapCntlV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8)
)
_H3cIPsecTrapGlobalCntlV2_Type = TruthValue
_H3cIPsecTrapGlobalCntlV2_Object = MibScalar
h3cIPsecTrapGlobalCntlV2 = _H3cIPsecTrapGlobalCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 1),
    _H3cIPsecTrapGlobalCntlV2_Type()
)
h3cIPsecTrapGlobalCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecTrapGlobalCntlV2.setStatus("current")
_H3cIPsecTunnelStartTrapCntlV2_Type = TruthValue
_H3cIPsecTunnelStartTrapCntlV2_Object = MibScalar
h3cIPsecTunnelStartTrapCntlV2 = _H3cIPsecTunnelStartTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 2),
    _H3cIPsecTunnelStartTrapCntlV2_Type()
)
h3cIPsecTunnelStartTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecTunnelStartTrapCntlV2.setStatus("current")
_H3cIPsecTunnelStopTrapCntlV2_Type = TruthValue
_H3cIPsecTunnelStopTrapCntlV2_Object = MibScalar
h3cIPsecTunnelStopTrapCntlV2 = _H3cIPsecTunnelStopTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 3),
    _H3cIPsecTunnelStopTrapCntlV2_Type()
)
h3cIPsecTunnelStopTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecTunnelStopTrapCntlV2.setStatus("current")
_H3cIPsecNoSaTrapCntlV2_Type = TruthValue
_H3cIPsecNoSaTrapCntlV2_Object = MibScalar
h3cIPsecNoSaTrapCntlV2 = _H3cIPsecNoSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 4),
    _H3cIPsecNoSaTrapCntlV2_Type()
)
h3cIPsecNoSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecNoSaTrapCntlV2.setStatus("current")
_H3cIPsecAuthFailureTrapCntlV2_Type = TruthValue
_H3cIPsecAuthFailureTrapCntlV2_Object = MibScalar
h3cIPsecAuthFailureTrapCntlV2 = _H3cIPsecAuthFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 5),
    _H3cIPsecAuthFailureTrapCntlV2_Type()
)
h3cIPsecAuthFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecAuthFailureTrapCntlV2.setStatus("current")
_H3cIPsecEncryFailureTrapCntlV2_Type = TruthValue
_H3cIPsecEncryFailureTrapCntlV2_Object = MibScalar
h3cIPsecEncryFailureTrapCntlV2 = _H3cIPsecEncryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 6),
    _H3cIPsecEncryFailureTrapCntlV2_Type()
)
h3cIPsecEncryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecEncryFailureTrapCntlV2.setStatus("current")
_H3cIPsecDecryFailureTrapCntlV2_Type = TruthValue
_H3cIPsecDecryFailureTrapCntlV2_Object = MibScalar
h3cIPsecDecryFailureTrapCntlV2 = _H3cIPsecDecryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 7),
    _H3cIPsecDecryFailureTrapCntlV2_Type()
)
h3cIPsecDecryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecDecryFailureTrapCntlV2.setStatus("current")
_H3cIPsecInvalidSaTrapCntlV2_Type = TruthValue
_H3cIPsecInvalidSaTrapCntlV2_Object = MibScalar
h3cIPsecInvalidSaTrapCntlV2 = _H3cIPsecInvalidSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 8),
    _H3cIPsecInvalidSaTrapCntlV2_Type()
)
h3cIPsecInvalidSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecInvalidSaTrapCntlV2.setStatus("current")
_H3cIPsecPolicyAddTrapCntlV2_Type = TruthValue
_H3cIPsecPolicyAddTrapCntlV2_Object = MibScalar
h3cIPsecPolicyAddTrapCntlV2 = _H3cIPsecPolicyAddTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 9),
    _H3cIPsecPolicyAddTrapCntlV2_Type()
)
h3cIPsecPolicyAddTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecPolicyAddTrapCntlV2.setStatus("current")
_H3cIPsecPolicyDelTrapCntlV2_Type = TruthValue
_H3cIPsecPolicyDelTrapCntlV2_Object = MibScalar
h3cIPsecPolicyDelTrapCntlV2 = _H3cIPsecPolicyDelTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 10),
    _H3cIPsecPolicyDelTrapCntlV2_Type()
)
h3cIPsecPolicyDelTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecPolicyDelTrapCntlV2.setStatus("current")
_H3cIPsecPolicyAttachTrapCntlV2_Type = TruthValue
_H3cIPsecPolicyAttachTrapCntlV2_Object = MibScalar
h3cIPsecPolicyAttachTrapCntlV2 = _H3cIPsecPolicyAttachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 11),
    _H3cIPsecPolicyAttachTrapCntlV2_Type()
)
h3cIPsecPolicyAttachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecPolicyAttachTrapCntlV2.setStatus("current")
_H3cIPsecPolicyDetachTrapCntlV2_Type = TruthValue
_H3cIPsecPolicyDetachTrapCntlV2_Object = MibScalar
h3cIPsecPolicyDetachTrapCntlV2 = _H3cIPsecPolicyDetachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 12),
    _H3cIPsecPolicyDetachTrapCntlV2_Type()
)
h3cIPsecPolicyDetachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecPolicyDetachTrapCntlV2.setStatus("current")
_H3cIPsecConnectionStartCntlV2_Type = TruthValue
_H3cIPsecConnectionStartCntlV2_Object = MibScalar
h3cIPsecConnectionStartCntlV2 = _H3cIPsecConnectionStartCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 13),
    _H3cIPsecConnectionStartCntlV2_Type()
)
h3cIPsecConnectionStartCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecConnectionStartCntlV2.setStatus("current")
_H3cIPsecConnectionStopCntlV2_Type = TruthValue
_H3cIPsecConnectionStopCntlV2_Object = MibScalar
h3cIPsecConnectionStopCntlV2 = _H3cIPsecConnectionStopCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 8, 14),
    _H3cIPsecConnectionStopCntlV2_Type()
)
h3cIPsecConnectionStopCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPsecConnectionStopCntlV2.setStatus("current")
_H3cIPsecTrapV2_ObjectIdentity = ObjectIdentity
h3cIPsecTrapV2 = _H3cIPsecTrapV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9)
)
_H3cIPsecNotificationsV2_ObjectIdentity = ObjectIdentity
h3cIPsecNotificationsV2 = _H3cIPsecNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0)
)
_H3cIPsecTunnelStatByDescripV2Table_Object = MibTable
h3cIPsecTunnelStatByDescripV2Table = _H3cIPsecTunnelStatByDescripV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10)
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStatByDescripV2Table.setStatus("current")
_H3cIPsecTunnelStatByDescripV2Entry_Object = MibTableRow
h3cIPsecTunnelStatByDescripV2Entry = _H3cIPsecTunnelStatByDescripV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1)
)
h3cIPsecTunnelStatByDescripV2Entry.setIndexNames(
    (0, "H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDescripV2"),
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStatByDescripV2Entry.setStatus("current")


class _H3cIPsecPolicyDescripV2_Type(OctetString):
    """Custom type h3cIPsecPolicyDescripV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cIPsecPolicyDescripV2_Type.__name__ = "OctetString"
_H3cIPsecPolicyDescripV2_Object = MibTableColumn
h3cIPsecPolicyDescripV2 = _H3cIPsecPolicyDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 1),
    _H3cIPsecPolicyDescripV2_Type()
)
h3cIPsecPolicyDescripV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPsecPolicyDescripV2.setStatus("current")
_H3cIPsecTunInOctetsByDescripV2_Type = Counter64
_H3cIPsecTunInOctetsByDescripV2_Object = MibTableColumn
h3cIPsecTunInOctetsByDescripV2 = _H3cIPsecTunInOctetsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 2),
    _H3cIPsecTunInOctetsByDescripV2_Type()
)
h3cIPsecTunInOctetsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInOctetsByDescripV2.setStatus("current")
_H3cIPsecTunInDecompOctetsByDescripV2_Type = Counter64
_H3cIPsecTunInDecompOctetsByDescripV2_Object = MibTableColumn
h3cIPsecTunInDecompOctetsByDescripV2 = _H3cIPsecTunInDecompOctetsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 3),
    _H3cIPsecTunInDecompOctetsByDescripV2_Type()
)
h3cIPsecTunInDecompOctetsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDecompOctetsByDescripV2.setStatus("current")
_H3cIPsecTunInPktsByDescripV2_Type = Counter64
_H3cIPsecTunInPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunInPktsByDescripV2 = _H3cIPsecTunInPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 4),
    _H3cIPsecTunInPktsByDescripV2_Type()
)
h3cIPsecTunInPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInPktsByDescripV2.setStatus("current")
_H3cIPsecTunInDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunInDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunInDropPktsByDescripV2 = _H3cIPsecTunInDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 5),
    _H3cIPsecTunInDropPktsByDescripV2_Type()
)
h3cIPsecTunInDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunInReplayDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunInReplayDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunInReplayDropPktsByDescripV2 = _H3cIPsecTunInReplayDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 6),
    _H3cIPsecTunInReplayDropPktsByDescripV2_Type()
)
h3cIPsecTunInReplayDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInReplayDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunInAuthFailsByDescripV2_Type = Counter64
_H3cIPsecTunInAuthFailsByDescripV2_Object = MibTableColumn
h3cIPsecTunInAuthFailsByDescripV2 = _H3cIPsecTunInAuthFailsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 7),
    _H3cIPsecTunInAuthFailsByDescripV2_Type()
)
h3cIPsecTunInAuthFailsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInAuthFailsByDescripV2.setStatus("current")
_H3cIPsecTunInDecryptFailsByDescripV2_Type = Counter64
_H3cIPsecTunInDecryptFailsByDescripV2_Object = MibTableColumn
h3cIPsecTunInDecryptFailsByDescripV2 = _H3cIPsecTunInDecryptFailsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 8),
    _H3cIPsecTunInDecryptFailsByDescripV2_Type()
)
h3cIPsecTunInDecryptFailsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInDecryptFailsByDescripV2.setStatus("current")
_H3cIPsecTunOutOctetsByDescripV2_Type = Counter64
_H3cIPsecTunOutOctetsByDescripV2_Object = MibTableColumn
h3cIPsecTunOutOctetsByDescripV2 = _H3cIPsecTunOutOctetsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 9),
    _H3cIPsecTunOutOctetsByDescripV2_Type()
)
h3cIPsecTunOutOctetsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutOctetsByDescripV2.setStatus("current")
_H3cIPsecTunOutUncompOctetsByDescripV2_Type = Counter64
_H3cIPsecTunOutUncompOctetsByDescripV2_Object = MibTableColumn
h3cIPsecTunOutUncompOctetsByDescripV2 = _H3cIPsecTunOutUncompOctetsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 10),
    _H3cIPsecTunOutUncompOctetsByDescripV2_Type()
)
h3cIPsecTunOutUncompOctetsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutUncompOctetsByDescripV2.setStatus("current")
_H3cIPsecTunOutPktsByDescripV2_Type = Counter64
_H3cIPsecTunOutPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunOutPktsByDescripV2 = _H3cIPsecTunOutPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 11),
    _H3cIPsecTunOutPktsByDescripV2_Type()
)
h3cIPsecTunOutPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutPktsByDescripV2.setStatus("current")
_H3cIPsecTunOutDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunOutDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunOutDropPktsByDescripV2 = _H3cIPsecTunOutDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 12),
    _H3cIPsecTunOutDropPktsByDescripV2_Type()
)
h3cIPsecTunOutDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunOutEncryptFailsByDescripV2_Type = Counter64
_H3cIPsecTunOutEncryptFailsByDescripV2_Object = MibTableColumn
h3cIPsecTunOutEncryptFailsByDescripV2 = _H3cIPsecTunOutEncryptFailsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 13),
    _H3cIPsecTunOutEncryptFailsByDescripV2_Type()
)
h3cIPsecTunOutEncryptFailsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunOutEncryptFailsByDescripV2.setStatus("current")
_H3cIPsecTunNoMemoryDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunNoMemoryDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunNoMemoryDropPktsByDescripV2 = _H3cIPsecTunNoMemoryDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 14),
    _H3cIPsecTunNoMemoryDropPktsByDescripV2_Type()
)
h3cIPsecTunNoMemoryDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunNoMemoryDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunQueueFullDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunQueueFullDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunQueueFullDropPktsByDescripV2 = _H3cIPsecTunQueueFullDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 15),
    _H3cIPsecTunQueueFullDropPktsByDescripV2_Type()
)
h3cIPsecTunQueueFullDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunQueueFullDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunInvalidLenDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunInvalidLenDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunInvalidLenDropPktsByDescripV2 = _H3cIPsecTunInvalidLenDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 16),
    _H3cIPsecTunInvalidLenDropPktsByDescripV2_Type()
)
h3cIPsecTunInvalidLenDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInvalidLenDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunTooLongDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunTooLongDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunTooLongDropPktsByDescripV2 = _H3cIPsecTunTooLongDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 17),
    _H3cIPsecTunTooLongDropPktsByDescripV2_Type()
)
h3cIPsecTunTooLongDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunTooLongDropPktsByDescripV2.setStatus("current")
_H3cIPsecTunInvalidSaDropPktsByDescripV2_Type = Counter64
_H3cIPsecTunInvalidSaDropPktsByDescripV2_Object = MibTableColumn
h3cIPsecTunInvalidSaDropPktsByDescripV2 = _H3cIPsecTunInvalidSaDropPktsByDescripV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 10, 1, 18),
    _H3cIPsecTunInvalidSaDropPktsByDescripV2_Type()
)
h3cIPsecTunInvalidSaDropPktsByDescripV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPsecTunInvalidSaDropPktsByDescripV2.setStatus("current")
_H3cIPsecConformanceV2_ObjectIdentity = ObjectIdentity
h3cIPsecConformanceV2 = _H3cIPsecConformanceV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2)
)
_H3cIPsecCompliancesV2_ObjectIdentity = ObjectIdentity
h3cIPsecCompliancesV2 = _H3cIPsecCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 1)
)
_H3cIPsecGroupsV2_ObjectIdentity = ObjectIdentity
h3cIPsecGroupsV2 = _H3cIPsecGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2)
)

# Managed Objects groups

h3cIPsecScalarObjectsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 1)
)
h3cIPsecScalarObjectsGroupV2.setObjects(
    ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecMIBVersion")
)
if mibBuilder.loadTexts:
    h3cIPsecScalarObjectsGroupV2.setStatus("current")

h3cIPsecTunnelTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 2)
)
h3cIPsecTunnelTableGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIfIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunnelIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunLocalIDTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunLocalIDVal1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunLocalIDVal2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunRemoteIDTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunRemoteIDVal1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIKETunRemoteIDVal2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunKeyTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunEncapModeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInitiatorV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLifeSizeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLifeTimeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemainTimeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunActiveTimeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemainSizeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunTotalRefreshesV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunCurrentSaInstancesV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInSaEncryptAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInSaAhAuthAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInSaEspAuthAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunDiffHellmanGrpV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutSaEncryptAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutSaAhAuthAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutSaEspAuthAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunPolicyNumV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunStatusV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunPolicyDescriptionV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelTableGroupV2.setStatus("current")

h3cIPsecTunnelStatGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 3)
)
h3cIPsecTunnelStatGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInDecompOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInReplayDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInAuthFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInDecryptFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutUncompOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunOutEncryptFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunNoMemoryDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunQueueFullDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInvalidLenDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunTooLongDropPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunInvalidSaDropPktsV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStatGroupV2.setStatus("current")

h3cIPsecSaGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 4)
)
h3cIPsecSaGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaDirectionV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaSpiValueV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaSecProtocolV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaEncryptAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaAuthAlgoV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaStatusV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecSaGroupV2.setStatus("current")

h3cIPsecTrafficTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 5)
)
h3cIPsecTrafficTableGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalAddr1TypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalAddr1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalAddr2TypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalAddr2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalProtocol1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalProtocol2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalPort1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficLocalPort2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemoteTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemAddr1TypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemAddr1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemAddr2TypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemAddr2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemoPro1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemoPro2V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemPort1V2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficRemPort2V2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTrafficTableGroupV2.setStatus("current")

h3cIPsecGlobalStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 6)
)
h3cIPsecGlobalStatsGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalActiveTunnelsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalActiveSasV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInDecompOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInReplayDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInAuthFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInDecryptFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalOutOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalOutUncompOctetsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalOutPktsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalOutDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalOutEncryptFailsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalNoMemoryDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalNoFindSaDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalQueueFullDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInvalidLenDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalTooLongDropsV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalInvalidSaDropsV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecGlobalStatsGroupV2.setStatus("current")

h3cIPsecTrapObjectGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 7)
)
h3cIPsecTrapObjectGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySeqNumV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTrapObjectGroupV2.setStatus("current")

h3cIPsecTrapCntlGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 8)
)
h3cIPsecTrapCntlGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrapGlobalCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelStartTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelStopTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecNoSaTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecAuthFailureTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecEncryFailureTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecDecryFailureTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecInvalidSaTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyAddTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDelTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyAttachTrapCntlV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDetachTrapCntlV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTrapCntlGroupV2.setStatus("current")


# Notification objects

h3cIPsecTunnelStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 1)
)
h3cIPsecTunnelStartV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLifeTimeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLifeSizeV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStartV2.setStatus(
        "current"
    )

h3cIPsecTunnelStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 2)
)
h3cIPsecTunnelStopV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunActiveTimeV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTunnelStopV2.setStatus(
        "current"
    )

h3cIPsecNoSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 3)
)
h3cIPsecNoSaFailureV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecNoSaFailureV2.setStatus(
        "current"
    )

h3cIPsecAuthFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 4)
)
h3cIPsecAuthFailFailureV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecAuthFailFailureV2.setStatus(
        "current"
    )

h3cIPsecEncryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 5)
)
h3cIPsecEncryFailFailureV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecEncryFailFailureV2.setStatus(
        "current"
    )

h3cIPsecDecryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 6)
)
h3cIPsecDecryFailFailureV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecDecryFailFailureV2.setStatus(
        "current"
    )

h3cIPsecInvalidSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 7)
)
h3cIPsecInvalidSaFailureV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaIndexV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunLocalAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrTypeV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunRemoteAddrV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaSpiValueV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecInvalidSaFailureV2.setStatus(
        "current"
    )

h3cIPsecPolicyAddV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 8)
)
h3cIPsecPolicyAddV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySeqNumV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecPolicyAddV2.setStatus(
        "current"
    )

h3cIPsecPolicyDelV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 9)
)
h3cIPsecPolicyDelV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySeqNumV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecPolicyDelV2.setStatus(
        "current"
    )

h3cIPsecPolicyAttachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 10)
)
h3cIPsecPolicyAttachV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    h3cIPsecPolicyAttachV2.setStatus(
        "current"
    )

h3cIPsecPolicyDetachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 11)
)
h3cIPsecPolicyDetachV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyNameV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    h3cIPsecPolicyDetachV2.setStatus(
        "current"
    )

h3cIPsecConnectionStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 12)
)
h3cIPsecConnectionStartV2.setObjects(
    ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDescripV2")
)
if mibBuilder.loadTexts:
    h3cIPsecConnectionStartV2.setStatus(
        "current"
    )

h3cIPsecConnectionStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 1, 9, 0, 13)
)
h3cIPsecConnectionStopV2.setObjects(
    ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDescripV2")
)
if mibBuilder.loadTexts:
    h3cIPsecConnectionStopV2.setStatus(
        "current"
    )


# Notifications groups

h3cIPsecTrapGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 2, 9)
)
h3cIPsecTrapGroupV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelStartV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelStopV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecNoSaFailureV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecAuthFailFailureV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecEncryFailFailureV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecDecryFailFailureV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecInvalidSaFailureV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyAddV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDelV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyAttachV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecPolicyDetachV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecConnectionStartV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecConnectionStopV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecTrapGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cIPsecComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 126, 2, 1, 1)
)
h3cIPsecComplianceV2.setObjects(
      *(("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecScalarObjectsGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelTableGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTunnelStatGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecSaGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrafficTableGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecGlobalStatsGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrapObjectGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrapCntlGroupV2"),
        ("H3C-IPSEC-MONITOR-V2-MIB", "h3cIPsecTrapGroupV2"))
)
if mibBuilder.loadTexts:
    h3cIPsecComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-IPSEC-MONITOR-V2-MIB",
    **{"H3cIPsecDiffHellmanGrpV2": H3cIPsecDiffHellmanGrpV2,
       "H3cIPsecEncapModeV2": H3cIPsecEncapModeV2,
       "H3cIPsecEncryptAlgoV2": H3cIPsecEncryptAlgoV2,
       "H3cIPsecAuthAlgoV2": H3cIPsecAuthAlgoV2,
       "H3cIPsecSaProtocolV2": H3cIPsecSaProtocolV2,
       "H3cIPsecIDTypeV2": H3cIPsecIDTypeV2,
       "H3cIPsecTrafficTypeV2": H3cIPsecTrafficTypeV2,
       "H3cIPsecNegoTypeV2": H3cIPsecNegoTypeV2,
       "H3cIPsecTunnelStateV2": H3cIPsecTunnelStateV2,
       "h3cIPsecMonitorV2": h3cIPsecMonitorV2,
       "h3cIPsecObjectsV2": h3cIPsecObjectsV2,
       "h3cIPsecScalarObjectsV2": h3cIPsecScalarObjectsV2,
       "h3cIPsecMIBVersion": h3cIPsecMIBVersion,
       "h3cIPsecTunnelV2Table": h3cIPsecTunnelV2Table,
       "h3cIPsecTunnelV2Entry": h3cIPsecTunnelV2Entry,
       "h3cIPsecTunIndexV2": h3cIPsecTunIndexV2,
       "h3cIPsecTunIfIndexV2": h3cIPsecTunIfIndexV2,
       "h3cIPsecTunIKETunnelIndexV2": h3cIPsecTunIKETunnelIndexV2,
       "h3cIPsecTunIKETunLocalIDTypeV2": h3cIPsecTunIKETunLocalIDTypeV2,
       "h3cIPsecTunIKETunLocalIDVal1V2": h3cIPsecTunIKETunLocalIDVal1V2,
       "h3cIPsecTunIKETunLocalIDVal2V2": h3cIPsecTunIKETunLocalIDVal2V2,
       "h3cIPsecTunIKETunRemoteIDTypeV2": h3cIPsecTunIKETunRemoteIDTypeV2,
       "h3cIPsecTunIKETunRemoteIDVal1V2": h3cIPsecTunIKETunRemoteIDVal1V2,
       "h3cIPsecTunIKETunRemoteIDVal2V2": h3cIPsecTunIKETunRemoteIDVal2V2,
       "h3cIPsecTunLocalAddrTypeV2": h3cIPsecTunLocalAddrTypeV2,
       "h3cIPsecTunLocalAddrV2": h3cIPsecTunLocalAddrV2,
       "h3cIPsecTunRemoteAddrTypeV2": h3cIPsecTunRemoteAddrTypeV2,
       "h3cIPsecTunRemoteAddrV2": h3cIPsecTunRemoteAddrV2,
       "h3cIPsecTunKeyTypeV2": h3cIPsecTunKeyTypeV2,
       "h3cIPsecTunEncapModeV2": h3cIPsecTunEncapModeV2,
       "h3cIPsecTunInitiatorV2": h3cIPsecTunInitiatorV2,
       "h3cIPsecTunLifeSizeV2": h3cIPsecTunLifeSizeV2,
       "h3cIPsecTunLifeTimeV2": h3cIPsecTunLifeTimeV2,
       "h3cIPsecTunRemainTimeV2": h3cIPsecTunRemainTimeV2,
       "h3cIPsecTunActiveTimeV2": h3cIPsecTunActiveTimeV2,
       "h3cIPsecTunRemainSizeV2": h3cIPsecTunRemainSizeV2,
       "h3cIPsecTunTotalRefreshesV2": h3cIPsecTunTotalRefreshesV2,
       "h3cIPsecTunCurrentSaInstancesV2": h3cIPsecTunCurrentSaInstancesV2,
       "h3cIPsecTunInSaEncryptAlgoV2": h3cIPsecTunInSaEncryptAlgoV2,
       "h3cIPsecTunInSaAhAuthAlgoV2": h3cIPsecTunInSaAhAuthAlgoV2,
       "h3cIPsecTunInSaEspAuthAlgoV2": h3cIPsecTunInSaEspAuthAlgoV2,
       "h3cIPsecTunDiffHellmanGrpV2": h3cIPsecTunDiffHellmanGrpV2,
       "h3cIPsecTunOutSaEncryptAlgoV2": h3cIPsecTunOutSaEncryptAlgoV2,
       "h3cIPsecTunOutSaAhAuthAlgoV2": h3cIPsecTunOutSaAhAuthAlgoV2,
       "h3cIPsecTunOutSaEspAuthAlgoV2": h3cIPsecTunOutSaEspAuthAlgoV2,
       "h3cIPsecTunPolicyNameV2": h3cIPsecTunPolicyNameV2,
       "h3cIPsecTunPolicyNumV2": h3cIPsecTunPolicyNumV2,
       "h3cIPsecTunStatusV2": h3cIPsecTunStatusV2,
       "h3cIPsecTunPolicyDescriptionV2": h3cIPsecTunPolicyDescriptionV2,
       "h3cIPsecTunnelStatV2Table": h3cIPsecTunnelStatV2Table,
       "h3cIPsecTunnelStatV2Entry": h3cIPsecTunnelStatV2Entry,
       "h3cIPsecTunInOctetsV2": h3cIPsecTunInOctetsV2,
       "h3cIPsecTunInDecompOctetsV2": h3cIPsecTunInDecompOctetsV2,
       "h3cIPsecTunInPktsV2": h3cIPsecTunInPktsV2,
       "h3cIPsecTunInDropPktsV2": h3cIPsecTunInDropPktsV2,
       "h3cIPsecTunInReplayDropPktsV2": h3cIPsecTunInReplayDropPktsV2,
       "h3cIPsecTunInAuthFailsV2": h3cIPsecTunInAuthFailsV2,
       "h3cIPsecTunInDecryptFailsV2": h3cIPsecTunInDecryptFailsV2,
       "h3cIPsecTunOutOctetsV2": h3cIPsecTunOutOctetsV2,
       "h3cIPsecTunOutUncompOctetsV2": h3cIPsecTunOutUncompOctetsV2,
       "h3cIPsecTunOutPktsV2": h3cIPsecTunOutPktsV2,
       "h3cIPsecTunOutDropPktsV2": h3cIPsecTunOutDropPktsV2,
       "h3cIPsecTunOutEncryptFailsV2": h3cIPsecTunOutEncryptFailsV2,
       "h3cIPsecTunNoMemoryDropPktsV2": h3cIPsecTunNoMemoryDropPktsV2,
       "h3cIPsecTunQueueFullDropPktsV2": h3cIPsecTunQueueFullDropPktsV2,
       "h3cIPsecTunInvalidLenDropPktsV2": h3cIPsecTunInvalidLenDropPktsV2,
       "h3cIPsecTunTooLongDropPktsV2": h3cIPsecTunTooLongDropPktsV2,
       "h3cIPsecTunInvalidSaDropPktsV2": h3cIPsecTunInvalidSaDropPktsV2,
       "h3cIPsecSaV2Table": h3cIPsecSaV2Table,
       "h3cIPsecSaV2Entry": h3cIPsecSaV2Entry,
       "h3cIPsecSaIndexV2": h3cIPsecSaIndexV2,
       "h3cIPsecSaDirectionV2": h3cIPsecSaDirectionV2,
       "h3cIPsecSaSpiValueV2": h3cIPsecSaSpiValueV2,
       "h3cIPsecSaSecProtocolV2": h3cIPsecSaSecProtocolV2,
       "h3cIPsecSaEncryptAlgoV2": h3cIPsecSaEncryptAlgoV2,
       "h3cIPsecSaAuthAlgoV2": h3cIPsecSaAuthAlgoV2,
       "h3cIPsecSaStatusV2": h3cIPsecSaStatusV2,
       "h3cIPsecTrafficV2Table": h3cIPsecTrafficV2Table,
       "h3cIPsecTrafficV2Entry": h3cIPsecTrafficV2Entry,
       "h3cIPsecTrafficLocalTypeV2": h3cIPsecTrafficLocalTypeV2,
       "h3cIPsecTrafficLocalAddr1TypeV2": h3cIPsecTrafficLocalAddr1TypeV2,
       "h3cIPsecTrafficLocalAddr1V2": h3cIPsecTrafficLocalAddr1V2,
       "h3cIPsecTrafficLocalAddr2TypeV2": h3cIPsecTrafficLocalAddr2TypeV2,
       "h3cIPsecTrafficLocalAddr2V2": h3cIPsecTrafficLocalAddr2V2,
       "h3cIPsecTrafficLocalProtocol1V2": h3cIPsecTrafficLocalProtocol1V2,
       "h3cIPsecTrafficLocalProtocol2V2": h3cIPsecTrafficLocalProtocol2V2,
       "h3cIPsecTrafficLocalPort1V2": h3cIPsecTrafficLocalPort1V2,
       "h3cIPsecTrafficLocalPort2V2": h3cIPsecTrafficLocalPort2V2,
       "h3cIPsecTrafficRemoteTypeV2": h3cIPsecTrafficRemoteTypeV2,
       "h3cIPsecTrafficRemAddr1TypeV2": h3cIPsecTrafficRemAddr1TypeV2,
       "h3cIPsecTrafficRemAddr1V2": h3cIPsecTrafficRemAddr1V2,
       "h3cIPsecTrafficRemAddr2TypeV2": h3cIPsecTrafficRemAddr2TypeV2,
       "h3cIPsecTrafficRemAddr2V2": h3cIPsecTrafficRemAddr2V2,
       "h3cIPsecTrafficRemoPro1V2": h3cIPsecTrafficRemoPro1V2,
       "h3cIPsecTrafficRemoPro2V2": h3cIPsecTrafficRemoPro2V2,
       "h3cIPsecTrafficRemPort1V2": h3cIPsecTrafficRemPort1V2,
       "h3cIPsecTrafficRemPort2V2": h3cIPsecTrafficRemPort2V2,
       "h3cIPsecGlobalStatsV2": h3cIPsecGlobalStatsV2,
       "h3cIPsecGlobalActiveTunnelsV2": h3cIPsecGlobalActiveTunnelsV2,
       "h3cIPsecGlobalActiveSasV2": h3cIPsecGlobalActiveSasV2,
       "h3cIPsecGlobalInOctetsV2": h3cIPsecGlobalInOctetsV2,
       "h3cIPsecGlobalInDecompOctetsV2": h3cIPsecGlobalInDecompOctetsV2,
       "h3cIPsecGlobalInPktsV2": h3cIPsecGlobalInPktsV2,
       "h3cIPsecGlobalInDropsV2": h3cIPsecGlobalInDropsV2,
       "h3cIPsecGlobalInReplayDropsV2": h3cIPsecGlobalInReplayDropsV2,
       "h3cIPsecGlobalInAuthFailsV2": h3cIPsecGlobalInAuthFailsV2,
       "h3cIPsecGlobalInDecryptFailsV2": h3cIPsecGlobalInDecryptFailsV2,
       "h3cIPsecGlobalOutOctetsV2": h3cIPsecGlobalOutOctetsV2,
       "h3cIPsecGlobalOutUncompOctetsV2": h3cIPsecGlobalOutUncompOctetsV2,
       "h3cIPsecGlobalOutPktsV2": h3cIPsecGlobalOutPktsV2,
       "h3cIPsecGlobalOutDropsV2": h3cIPsecGlobalOutDropsV2,
       "h3cIPsecGlobalOutEncryptFailsV2": h3cIPsecGlobalOutEncryptFailsV2,
       "h3cIPsecGlobalNoMemoryDropsV2": h3cIPsecGlobalNoMemoryDropsV2,
       "h3cIPsecGlobalNoFindSaDropsV2": h3cIPsecGlobalNoFindSaDropsV2,
       "h3cIPsecGlobalQueueFullDropsV2": h3cIPsecGlobalQueueFullDropsV2,
       "h3cIPsecGlobalInvalidLenDropsV2": h3cIPsecGlobalInvalidLenDropsV2,
       "h3cIPsecGlobalTooLongDropsV2": h3cIPsecGlobalTooLongDropsV2,
       "h3cIPsecGlobalInvalidSaDropsV2": h3cIPsecGlobalInvalidSaDropsV2,
       "h3cIPsecTrapObjectV2": h3cIPsecTrapObjectV2,
       "h3cIPsecPolicyNameV2": h3cIPsecPolicyNameV2,
       "h3cIPsecPolicySeqNumV2": h3cIPsecPolicySeqNumV2,
       "h3cIPsecPolicySizeV2": h3cIPsecPolicySizeV2,
       "h3cIPsecTrapCntlV2": h3cIPsecTrapCntlV2,
       "h3cIPsecTrapGlobalCntlV2": h3cIPsecTrapGlobalCntlV2,
       "h3cIPsecTunnelStartTrapCntlV2": h3cIPsecTunnelStartTrapCntlV2,
       "h3cIPsecTunnelStopTrapCntlV2": h3cIPsecTunnelStopTrapCntlV2,
       "h3cIPsecNoSaTrapCntlV2": h3cIPsecNoSaTrapCntlV2,
       "h3cIPsecAuthFailureTrapCntlV2": h3cIPsecAuthFailureTrapCntlV2,
       "h3cIPsecEncryFailureTrapCntlV2": h3cIPsecEncryFailureTrapCntlV2,
       "h3cIPsecDecryFailureTrapCntlV2": h3cIPsecDecryFailureTrapCntlV2,
       "h3cIPsecInvalidSaTrapCntlV2": h3cIPsecInvalidSaTrapCntlV2,
       "h3cIPsecPolicyAddTrapCntlV2": h3cIPsecPolicyAddTrapCntlV2,
       "h3cIPsecPolicyDelTrapCntlV2": h3cIPsecPolicyDelTrapCntlV2,
       "h3cIPsecPolicyAttachTrapCntlV2": h3cIPsecPolicyAttachTrapCntlV2,
       "h3cIPsecPolicyDetachTrapCntlV2": h3cIPsecPolicyDetachTrapCntlV2,
       "h3cIPsecConnectionStartCntlV2": h3cIPsecConnectionStartCntlV2,
       "h3cIPsecConnectionStopCntlV2": h3cIPsecConnectionStopCntlV2,
       "h3cIPsecTrapV2": h3cIPsecTrapV2,
       "h3cIPsecNotificationsV2": h3cIPsecNotificationsV2,
       "h3cIPsecTunnelStartV2": h3cIPsecTunnelStartV2,
       "h3cIPsecTunnelStopV2": h3cIPsecTunnelStopV2,
       "h3cIPsecNoSaFailureV2": h3cIPsecNoSaFailureV2,
       "h3cIPsecAuthFailFailureV2": h3cIPsecAuthFailFailureV2,
       "h3cIPsecEncryFailFailureV2": h3cIPsecEncryFailFailureV2,
       "h3cIPsecDecryFailFailureV2": h3cIPsecDecryFailFailureV2,
       "h3cIPsecInvalidSaFailureV2": h3cIPsecInvalidSaFailureV2,
       "h3cIPsecPolicyAddV2": h3cIPsecPolicyAddV2,
       "h3cIPsecPolicyDelV2": h3cIPsecPolicyDelV2,
       "h3cIPsecPolicyAttachV2": h3cIPsecPolicyAttachV2,
       "h3cIPsecPolicyDetachV2": h3cIPsecPolicyDetachV2,
       "h3cIPsecConnectionStartV2": h3cIPsecConnectionStartV2,
       "h3cIPsecConnectionStopV2": h3cIPsecConnectionStopV2,
       "h3cIPsecTunnelStatByDescripV2Table": h3cIPsecTunnelStatByDescripV2Table,
       "h3cIPsecTunnelStatByDescripV2Entry": h3cIPsecTunnelStatByDescripV2Entry,
       "h3cIPsecPolicyDescripV2": h3cIPsecPolicyDescripV2,
       "h3cIPsecTunInOctetsByDescripV2": h3cIPsecTunInOctetsByDescripV2,
       "h3cIPsecTunInDecompOctetsByDescripV2": h3cIPsecTunInDecompOctetsByDescripV2,
       "h3cIPsecTunInPktsByDescripV2": h3cIPsecTunInPktsByDescripV2,
       "h3cIPsecTunInDropPktsByDescripV2": h3cIPsecTunInDropPktsByDescripV2,
       "h3cIPsecTunInReplayDropPktsByDescripV2": h3cIPsecTunInReplayDropPktsByDescripV2,
       "h3cIPsecTunInAuthFailsByDescripV2": h3cIPsecTunInAuthFailsByDescripV2,
       "h3cIPsecTunInDecryptFailsByDescripV2": h3cIPsecTunInDecryptFailsByDescripV2,
       "h3cIPsecTunOutOctetsByDescripV2": h3cIPsecTunOutOctetsByDescripV2,
       "h3cIPsecTunOutUncompOctetsByDescripV2": h3cIPsecTunOutUncompOctetsByDescripV2,
       "h3cIPsecTunOutPktsByDescripV2": h3cIPsecTunOutPktsByDescripV2,
       "h3cIPsecTunOutDropPktsByDescripV2": h3cIPsecTunOutDropPktsByDescripV2,
       "h3cIPsecTunOutEncryptFailsByDescripV2": h3cIPsecTunOutEncryptFailsByDescripV2,
       "h3cIPsecTunNoMemoryDropPktsByDescripV2": h3cIPsecTunNoMemoryDropPktsByDescripV2,
       "h3cIPsecTunQueueFullDropPktsByDescripV2": h3cIPsecTunQueueFullDropPktsByDescripV2,
       "h3cIPsecTunInvalidLenDropPktsByDescripV2": h3cIPsecTunInvalidLenDropPktsByDescripV2,
       "h3cIPsecTunTooLongDropPktsByDescripV2": h3cIPsecTunTooLongDropPktsByDescripV2,
       "h3cIPsecTunInvalidSaDropPktsByDescripV2": h3cIPsecTunInvalidSaDropPktsByDescripV2,
       "h3cIPsecConformanceV2": h3cIPsecConformanceV2,
       "h3cIPsecCompliancesV2": h3cIPsecCompliancesV2,
       "h3cIPsecComplianceV2": h3cIPsecComplianceV2,
       "h3cIPsecGroupsV2": h3cIPsecGroupsV2,
       "h3cIPsecScalarObjectsGroupV2": h3cIPsecScalarObjectsGroupV2,
       "h3cIPsecTunnelTableGroupV2": h3cIPsecTunnelTableGroupV2,
       "h3cIPsecTunnelStatGroupV2": h3cIPsecTunnelStatGroupV2,
       "h3cIPsecSaGroupV2": h3cIPsecSaGroupV2,
       "h3cIPsecTrafficTableGroupV2": h3cIPsecTrafficTableGroupV2,
       "h3cIPsecGlobalStatsGroupV2": h3cIPsecGlobalStatsGroupV2,
       "h3cIPsecTrapObjectGroupV2": h3cIPsecTrapObjectGroupV2,
       "h3cIPsecTrapCntlGroupV2": h3cIPsecTrapCntlGroupV2,
       "h3cIPsecTrapGroupV2": h3cIPsecTrapGroupV2}
)
