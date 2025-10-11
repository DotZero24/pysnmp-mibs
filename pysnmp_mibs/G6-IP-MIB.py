# SNMP MIB module (G6-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:12 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22)
)
_IpPingTest_Type = DisplayString
_IpPingTest_Object = MibScalar
ipPingTest = _IpPingTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 1),
    _IpPingTest_Type()
)
ipPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPingTest.setStatus("current")
_IpTraceRoute_Type = DisplayString
_IpTraceRoute_Object = MibScalar
ipTraceRoute = _IpTraceRoute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 2),
    _IpTraceRoute_Type()
)
ipTraceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTraceRoute.setStatus("current")
_IpDnsLookup_Type = DisplayString
_IpDnsLookup_Object = MibScalar
ipDnsLookup = _IpDnsLookup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 3),
    _IpDnsLookup_Type()
)
ipDnsLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsLookup.setStatus("current")
_IpArpTable_Type = DisplayString
_IpArpTable_Object = MibScalar
ipArpTable = _IpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 4),
    _IpArpTable_Type()
)
ipArpTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipArpTable.setStatus("current")
_IpHostname_Type = DisplayString
_IpHostname_Object = MibScalar
ipHostname = _IpHostname_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 5),
    _IpHostname_Type()
)
ipHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostname.setStatus("current")


class _IpLocalMtu_Type(Integer32):
    """Custom type ipLocalMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpLocalMtu_Type.__name__ = "Integer32"
_IpLocalMtu_Object = MibScalar
ipLocalMtu = _IpLocalMtu_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 6),
    _IpLocalMtu_Type()
)
ipLocalMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLocalMtu.setStatus("current")
_V4ConfigTable_Object = MibTable
v4ConfigTable = _V4ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7)
)
if mibBuilder.loadTexts:
    v4ConfigTable.setStatus("current")
_V4ConfigEntry_Object = MibTableRow
v4ConfigEntry = _V4ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1)
)
v4ConfigEntry.setIndexNames(
    (0, "G6-IP-MIB", "v4ConfigIndex"),
)
if mibBuilder.loadTexts:
    v4ConfigEntry.setStatus("current")


class _V4ConfigIndex_Type(Integer32):
    """Custom type v4ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_V4ConfigIndex_Type.__name__ = "Integer32"
_V4ConfigIndex_Object = MibTableColumn
v4ConfigIndex = _V4ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 1),
    _V4ConfigIndex_Type()
)
v4ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v4ConfigIndex.setStatus("current")


class _V4ConfigDhcpMode_Type(Integer32):
    """Custom type v4ConfigDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("useDhcp", 1),
          ("dhcpWithScript", 2))
    )


_V4ConfigDhcpMode_Type.__name__ = "Integer32"
_V4ConfigDhcpMode_Object = MibTableColumn
v4ConfigDhcpMode = _V4ConfigDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 2),
    _V4ConfigDhcpMode_Type()
)
v4ConfigDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigDhcpMode.setStatus("current")


class _V4ConfigStaticDeviceIp_Type(OctetString):
    """Custom type v4ConfigStaticDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigStaticDeviceIp_Type.__name__ = "OctetString"
_V4ConfigStaticDeviceIp_Object = MibTableColumn
v4ConfigStaticDeviceIp = _V4ConfigStaticDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 3),
    _V4ConfigStaticDeviceIp_Type()
)
v4ConfigStaticDeviceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigStaticDeviceIp.setStatus("current")


class _V4ConfigStaticSubnetMask_Type(OctetString):
    """Custom type v4ConfigStaticSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigStaticSubnetMask_Type.__name__ = "OctetString"
_V4ConfigStaticSubnetMask_Object = MibTableColumn
v4ConfigStaticSubnetMask = _V4ConfigStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 4),
    _V4ConfigStaticSubnetMask_Type()
)
v4ConfigStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigStaticSubnetMask.setStatus("current")


class _V4ConfigStaticGateway_Type(OctetString):
    """Custom type v4ConfigStaticGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigStaticGateway_Type.__name__ = "OctetString"
_V4ConfigStaticGateway_Object = MibTableColumn
v4ConfigStaticGateway = _V4ConfigStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 5),
    _V4ConfigStaticGateway_Type()
)
v4ConfigStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigStaticGateway.setStatus("current")


class _V4ConfigStaticDnsServer_Type(OctetString):
    """Custom type v4ConfigStaticDnsServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigStaticDnsServer_Type.__name__ = "OctetString"
_V4ConfigStaticDnsServer_Object = MibTableColumn
v4ConfigStaticDnsServer = _V4ConfigStaticDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 6),
    _V4ConfigStaticDnsServer_Type()
)
v4ConfigStaticDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigStaticDnsServer.setStatus("current")


class _V4ConfigSecondaryDeviceIp_Type(OctetString):
    """Custom type v4ConfigSecondaryDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigSecondaryDeviceIp_Type.__name__ = "OctetString"
_V4ConfigSecondaryDeviceIp_Object = MibTableColumn
v4ConfigSecondaryDeviceIp = _V4ConfigSecondaryDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 7),
    _V4ConfigSecondaryDeviceIp_Type()
)
v4ConfigSecondaryDeviceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigSecondaryDeviceIp.setStatus("current")


class _V4ConfigSecondarySubnetMask_Type(OctetString):
    """Custom type v4ConfigSecondarySubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4ConfigSecondarySubnetMask_Type.__name__ = "OctetString"
_V4ConfigSecondarySubnetMask_Object = MibTableColumn
v4ConfigSecondarySubnetMask = _V4ConfigSecondarySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 8),
    _V4ConfigSecondarySubnetMask_Type()
)
v4ConfigSecondarySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigSecondarySubnetMask.setStatus("current")


class _V4ConfigDefaultAddressSelection_Type(Integer32):
    """Custom type v4ConfigDefaultAddressSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_V4ConfigDefaultAddressSelection_Type.__name__ = "Integer32"
_V4ConfigDefaultAddressSelection_Object = MibTableColumn
v4ConfigDefaultAddressSelection = _V4ConfigDefaultAddressSelection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 7, 1, 9),
    _V4ConfigDefaultAddressSelection_Type()
)
v4ConfigDefaultAddressSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4ConfigDefaultAddressSelection.setStatus("current")
_V6ConfigTable_Object = MibTable
v6ConfigTable = _V6ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8)
)
if mibBuilder.loadTexts:
    v6ConfigTable.setStatus("current")
_V6ConfigEntry_Object = MibTableRow
v6ConfigEntry = _V6ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8, 1)
)
v6ConfigEntry.setIndexNames(
    (0, "G6-IP-MIB", "v6ConfigIndex"),
)
if mibBuilder.loadTexts:
    v6ConfigEntry.setStatus("current")


class _V6ConfigIndex_Type(Integer32):
    """Custom type v6ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_V6ConfigIndex_Type.__name__ = "Integer32"
_V6ConfigIndex_Object = MibTableColumn
v6ConfigIndex = _V6ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8, 1, 1),
    _V6ConfigIndex_Type()
)
v6ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v6ConfigIndex.setStatus("current")


class _V6ConfigEnableIpv6_Type(Integer32):
    """Custom type v6ConfigEnableIpv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V6ConfigEnableIpv6_Type.__name__ = "Integer32"
_V6ConfigEnableIpv6_Object = MibTableColumn
v6ConfigEnableIpv6 = _V6ConfigEnableIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8, 1, 2),
    _V6ConfigEnableIpv6_Type()
)
v6ConfigEnableIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v6ConfigEnableIpv6.setStatus("current")


class _V6ConfigEnableIcmpAutoAddress_Type(Integer32):
    """Custom type v6ConfigEnableIcmpAutoAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V6ConfigEnableIcmpAutoAddress_Type.__name__ = "Integer32"
_V6ConfigEnableIcmpAutoAddress_Object = MibTableColumn
v6ConfigEnableIcmpAutoAddress = _V6ConfigEnableIcmpAutoAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8, 1, 3),
    _V6ConfigEnableIcmpAutoAddress_Type()
)
v6ConfigEnableIcmpAutoAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v6ConfigEnableIcmpAutoAddress.setStatus("current")


class _V6ConfigEnableDhcpAutoAddress_Type(Integer32):
    """Custom type v6ConfigEnableDhcpAutoAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V6ConfigEnableDhcpAutoAddress_Type.__name__ = "Integer32"
_V6ConfigEnableDhcpAutoAddress_Object = MibTableColumn
v6ConfigEnableDhcpAutoAddress = _V6ConfigEnableDhcpAutoAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 8, 1, 4),
    _V6ConfigEnableDhcpAutoAddress_Type()
)
v6ConfigEnableDhcpAutoAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v6ConfigEnableDhcpAutoAddress.setStatus("current")
_V6AddressTable_Object = MibTable
v6AddressTable = _V6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 9)
)
if mibBuilder.loadTexts:
    v6AddressTable.setStatus("current")
_V6AddressEntry_Object = MibTableRow
v6AddressEntry = _V6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 9, 1)
)
v6AddressEntry.setIndexNames(
    (0, "G6-IP-MIB", "v6AddressIndex"),
)
if mibBuilder.loadTexts:
    v6AddressEntry.setStatus("current")


class _V6AddressIndex_Type(Integer32):
    """Custom type v6AddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_V6AddressIndex_Type.__name__ = "Integer32"
_V6AddressIndex_Object = MibTableColumn
v6AddressIndex = _V6AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 9, 1, 1),
    _V6AddressIndex_Type()
)
v6AddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v6AddressIndex.setStatus("current")
_V6AddressIp_Type = DisplayString
_V6AddressIp_Object = MibTableColumn
v6AddressIp = _V6AddressIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 9, 1, 2),
    _V6AddressIp_Type()
)
v6AddressIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v6AddressIp.setStatus("current")
_V4StatusTable_Object = MibTable
v4StatusTable = _V4StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100)
)
if mibBuilder.loadTexts:
    v4StatusTable.setStatus("current")
_V4StatusEntry_Object = MibTableRow
v4StatusEntry = _V4StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1)
)
v4StatusEntry.setIndexNames(
    (0, "G6-IP-MIB", "v4StatusIndex"),
)
if mibBuilder.loadTexts:
    v4StatusEntry.setStatus("current")


class _V4StatusIndex_Type(Integer32):
    """Custom type v4StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_V4StatusIndex_Type.__name__ = "Integer32"
_V4StatusIndex_Object = MibTableColumn
v4StatusIndex = _V4StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 1),
    _V4StatusIndex_Type()
)
v4StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v4StatusIndex.setStatus("current")


class _V4StatusDynamicDeviceIp_Type(OctetString):
    """Custom type v4StatusDynamicDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicDeviceIp_Type.__name__ = "OctetString"
_V4StatusDynamicDeviceIp_Object = MibTableColumn
v4StatusDynamicDeviceIp = _V4StatusDynamicDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 2),
    _V4StatusDynamicDeviceIp_Type()
)
v4StatusDynamicDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicDeviceIp.setStatus("current")


class _V4StatusDynamicSubnetMask_Type(OctetString):
    """Custom type v4StatusDynamicSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicSubnetMask_Type.__name__ = "OctetString"
_V4StatusDynamicSubnetMask_Object = MibTableColumn
v4StatusDynamicSubnetMask = _V4StatusDynamicSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 3),
    _V4StatusDynamicSubnetMask_Type()
)
v4StatusDynamicSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicSubnetMask.setStatus("current")


class _V4StatusDynamicGateway_Type(OctetString):
    """Custom type v4StatusDynamicGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicGateway_Type.__name__ = "OctetString"
_V4StatusDynamicGateway_Object = MibTableColumn
v4StatusDynamicGateway = _V4StatusDynamicGateway_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 4),
    _V4StatusDynamicGateway_Type()
)
v4StatusDynamicGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicGateway.setStatus("current")


class _V4StatusDynamicDnsServer1_Type(OctetString):
    """Custom type v4StatusDynamicDnsServer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicDnsServer1_Type.__name__ = "OctetString"
_V4StatusDynamicDnsServer1_Object = MibTableColumn
v4StatusDynamicDnsServer1 = _V4StatusDynamicDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 5),
    _V4StatusDynamicDnsServer1_Type()
)
v4StatusDynamicDnsServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicDnsServer1.setStatus("current")


class _V4StatusDynamicDnsServer2_Type(OctetString):
    """Custom type v4StatusDynamicDnsServer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicDnsServer2_Type.__name__ = "OctetString"
_V4StatusDynamicDnsServer2_Object = MibTableColumn
v4StatusDynamicDnsServer2 = _V4StatusDynamicDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 6),
    _V4StatusDynamicDnsServer2_Type()
)
v4StatusDynamicDnsServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicDnsServer2.setStatus("current")


class _V4StatusDynamicDnsServer3_Type(OctetString):
    """Custom type v4StatusDynamicDnsServer3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicDnsServer3_Type.__name__ = "OctetString"
_V4StatusDynamicDnsServer3_Object = MibTableColumn
v4StatusDynamicDnsServer3 = _V4StatusDynamicDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 7),
    _V4StatusDynamicDnsServer3_Type()
)
v4StatusDynamicDnsServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicDnsServer3.setStatus("current")


class _V4StatusDynamicDnsServer4_Type(OctetString):
    """Custom type v4StatusDynamicDnsServer4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusDynamicDnsServer4_Type.__name__ = "OctetString"
_V4StatusDynamicDnsServer4_Object = MibTableColumn
v4StatusDynamicDnsServer4 = _V4StatusDynamicDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 8),
    _V4StatusDynamicDnsServer4_Type()
)
v4StatusDynamicDnsServer4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusDynamicDnsServer4.setStatus("current")


class _V4StatusOutgoingDeviceIp_Type(OctetString):
    """Custom type v4StatusOutgoingDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V4StatusOutgoingDeviceIp_Type.__name__ = "OctetString"
_V4StatusOutgoingDeviceIp_Object = MibTableColumn
v4StatusOutgoingDeviceIp = _V4StatusOutgoingDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 100, 1, 9),
    _V4StatusOutgoingDeviceIp_Type()
)
v4StatusOutgoingDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4StatusOutgoingDeviceIp.setStatus("current")
_V6StatusTable_Object = MibTable
v6StatusTable = _V6StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101)
)
if mibBuilder.loadTexts:
    v6StatusTable.setStatus("current")
_V6StatusEntry_Object = MibTableRow
v6StatusEntry = _V6StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101, 1)
)
v6StatusEntry.setIndexNames(
    (0, "G6-IP-MIB", "v6StatusIndex"),
)
if mibBuilder.loadTexts:
    v6StatusEntry.setStatus("current")


class _V6StatusIndex_Type(Integer32):
    """Custom type v6StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_V6StatusIndex_Type.__name__ = "Integer32"
_V6StatusIndex_Object = MibTableColumn
v6StatusIndex = _V6StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101, 1, 1),
    _V6StatusIndex_Type()
)
v6StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v6StatusIndex.setStatus("current")


class _V6StatusIp_Type(OctetString):
    """Custom type v6StatusIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_V6StatusIp_Type.__name__ = "OctetString"
_V6StatusIp_Object = MibTableColumn
v6StatusIp = _V6StatusIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101, 1, 2),
    _V6StatusIp_Type()
)
v6StatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v6StatusIp.setStatus("current")


class _V6StatusScope_Type(Integer32):
    """Custom type v6StatusScope based on Integer32"""
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
        *(("link", 0),
          ("site", 1),
          ("global", 2),
          ("other", 3))
    )


_V6StatusScope_Type.__name__ = "Integer32"
_V6StatusScope_Object = MibTableColumn
v6StatusScope = _V6StatusScope_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101, 1, 3),
    _V6StatusScope_Type()
)
v6StatusScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v6StatusScope.setStatus("current")


class _V6StatusState_Type(Integer32):
    """Custom type v6StatusState based on Integer32"""
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
        *(("stateless", 0),
          ("stateful", 1),
          ("both", 2),
          ("other", 3))
    )


_V6StatusState_Type.__name__ = "Integer32"
_V6StatusState_Object = MibTableColumn
v6StatusState = _V6StatusState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 22, 101, 1, 4),
    _V6StatusState_Type()
)
v6StatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v6StatusState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-IP-MIB",
    **{"device": device,
       "ip": ip,
       "ipPingTest": ipPingTest,
       "ipTraceRoute": ipTraceRoute,
       "ipDnsLookup": ipDnsLookup,
       "ipArpTable": ipArpTable,
       "ipHostname": ipHostname,
       "ipLocalMtu": ipLocalMtu,
       "v4ConfigTable": v4ConfigTable,
       "v4ConfigEntry": v4ConfigEntry,
       "v4ConfigIndex": v4ConfigIndex,
       "v4ConfigDhcpMode": v4ConfigDhcpMode,
       "v4ConfigStaticDeviceIp": v4ConfigStaticDeviceIp,
       "v4ConfigStaticSubnetMask": v4ConfigStaticSubnetMask,
       "v4ConfigStaticGateway": v4ConfigStaticGateway,
       "v4ConfigStaticDnsServer": v4ConfigStaticDnsServer,
       "v4ConfigSecondaryDeviceIp": v4ConfigSecondaryDeviceIp,
       "v4ConfigSecondarySubnetMask": v4ConfigSecondarySubnetMask,
       "v4ConfigDefaultAddressSelection": v4ConfigDefaultAddressSelection,
       "v6ConfigTable": v6ConfigTable,
       "v6ConfigEntry": v6ConfigEntry,
       "v6ConfigIndex": v6ConfigIndex,
       "v6ConfigEnableIpv6": v6ConfigEnableIpv6,
       "v6ConfigEnableIcmpAutoAddress": v6ConfigEnableIcmpAutoAddress,
       "v6ConfigEnableDhcpAutoAddress": v6ConfigEnableDhcpAutoAddress,
       "v6AddressTable": v6AddressTable,
       "v6AddressEntry": v6AddressEntry,
       "v6AddressIndex": v6AddressIndex,
       "v6AddressIp": v6AddressIp,
       "v4StatusTable": v4StatusTable,
       "v4StatusEntry": v4StatusEntry,
       "v4StatusIndex": v4StatusIndex,
       "v4StatusDynamicDeviceIp": v4StatusDynamicDeviceIp,
       "v4StatusDynamicSubnetMask": v4StatusDynamicSubnetMask,
       "v4StatusDynamicGateway": v4StatusDynamicGateway,
       "v4StatusDynamicDnsServer1": v4StatusDynamicDnsServer1,
       "v4StatusDynamicDnsServer2": v4StatusDynamicDnsServer2,
       "v4StatusDynamicDnsServer3": v4StatusDynamicDnsServer3,
       "v4StatusDynamicDnsServer4": v4StatusDynamicDnsServer4,
       "v4StatusOutgoingDeviceIp": v4StatusOutgoingDeviceIp,
       "v6StatusTable": v6StatusTable,
       "v6StatusEntry": v6StatusEntry,
       "v6StatusIndex": v6StatusIndex,
       "v6StatusIp": v6StatusIp,
       "v6StatusScope": v6StatusScope,
       "v6StatusState": v6StatusState}
)
