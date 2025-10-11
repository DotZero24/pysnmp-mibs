# SNMP MIB module (DGS-3420-26SC-L3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DGS-3420-26SC-L3MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:46 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(dlink_Dgs3420Proj_Dgs3420_26SC,) = mibBuilder.importSymbols(
    "SWDGS3420PRIMGMT-MIB",
    "dlink-Dgs3420Proj-Dgs3420-26SC")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3)
)


# Types definitions



class NodeAddress(OctetString):
    """Custom type NodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class NetAddress(OctetString):
    """Custom type NetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



class VrId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SwL3DevMgmt_ObjectIdentity = ObjectIdentity
swL3DevMgmt = _SwL3DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 1)
)
_SwL3DevCtrl_ObjectIdentity = ObjectIdentity
swL3DevCtrl = _SwL3DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 1, 1)
)


class _SwL3DevCtrlRIPState_Type(Integer32):
    """Custom type swL3DevCtrlRIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3DevCtrlRIPState_Type.__name__ = "Integer32"
_SwL3DevCtrlRIPState_Object = MibScalar
swL3DevCtrlRIPState = _SwL3DevCtrlRIPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 1, 1, 1),
    _SwL3DevCtrlRIPState_Type()
)
swL3DevCtrlRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlRIPState.setStatus("current")


class _SwL3DevCtrlVRRPState_Type(Integer32):
    """Custom type swL3DevCtrlVRRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3DevCtrlVRRPState_Type.__name__ = "Integer32"
_SwL3DevCtrlVRRPState_Object = MibScalar
swL3DevCtrlVRRPState = _SwL3DevCtrlVRRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 1, 1, 5),
    _SwL3DevCtrlVRRPState_Type()
)
swL3DevCtrlVRRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVRRPState.setStatus("current")


class _SwL3DevCtrlVrrpPingState_Type(Integer32):
    """Custom type swL3DevCtrlVrrpPingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3DevCtrlVrrpPingState_Type.__name__ = "Integer32"
_SwL3DevCtrlVrrpPingState_Object = MibScalar
swL3DevCtrlVrrpPingState = _SwL3DevCtrlVrrpPingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 1, 1, 6),
    _SwL3DevCtrlVrrpPingState_Type()
)
swL3DevCtrlVrrpPingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVrrpPingState.setStatus("current")
_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpCtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3IpCtrlEntry.setStatus("current")


class _SwL3IpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3IpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3IpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3IpCtrlInterfaceName_Object = MibTableColumn
swL3IpCtrlInterfaceName = _SwL3IpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 1),
    _SwL3IpCtrlInterfaceName_Type()
)
swL3IpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlInterfaceName.setStatus("current")


class _SwL3IpCtrlIfIndex_Type(Integer32):
    """Custom type swL3IpCtrlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpCtrlIfIndex_Type.__name__ = "Integer32"
_SwL3IpCtrlIfIndex_Object = MibTableColumn
swL3IpCtrlIfIndex = _SwL3IpCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 4),
    _SwL3IpCtrlIpSubnetMask_Type()
)
swL3IpCtrlIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpSubnetMask.setStatus("current")


class _SwL3IpCtrlVlanName_Type(DisplayString):
    """Custom type swL3IpCtrlVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL3IpCtrlVlanName_Type.__name__ = "DisplayString"
_SwL3IpCtrlVlanName_Object = MibTableColumn
swL3IpCtrlVlanName = _SwL3IpCtrlVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 5),
    _SwL3IpCtrlVlanName_Type()
)
swL3IpCtrlVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlVlanName.setStatus("current")


class _SwL3IpCtrlProxyArp_Type(Integer32):
    """Custom type swL3IpCtrlProxyArp based on Integer32"""
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


_SwL3IpCtrlProxyArp_Type.__name__ = "Integer32"
_SwL3IpCtrlProxyArp_Object = MibTableColumn
swL3IpCtrlProxyArp = _SwL3IpCtrlProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 6),
    _SwL3IpCtrlProxyArp_Type()
)
swL3IpCtrlProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlProxyArp.setStatus("current")
_SwL3IpCtrlSecondary_Type = TruthValue
_SwL3IpCtrlSecondary_Object = MibTableColumn
swL3IpCtrlSecondary = _SwL3IpCtrlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 7),
    _SwL3IpCtrlSecondary_Type()
)
swL3IpCtrlSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlSecondary.setStatus("current")


class _SwL3IpCtrlMode_Type(Integer32):
    """Custom type swL3IpCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("bootp", 3),
          ("dhcp", 4))
    )


_SwL3IpCtrlMode_Type.__name__ = "Integer32"
_SwL3IpCtrlMode_Object = MibTableColumn
swL3IpCtrlMode = _SwL3IpCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 8),
    _SwL3IpCtrlMode_Type()
)
swL3IpCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlMode.setStatus("current")


class _SwL3IpCtrlAdminState_Type(Integer32):
    """Custom type swL3IpCtrlAdminState based on Integer32"""
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


_SwL3IpCtrlAdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlAdminState_Object = MibTableColumn
swL3IpCtrlAdminState = _SwL3IpCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 9),
    _SwL3IpCtrlAdminState_Type()
)
swL3IpCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAdminState.setStatus("current")


class _SwL3IpCtrlIpv4AdminState_Type(Integer32):
    """Custom type swL3IpCtrlIpv4AdminState based on Integer32"""
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


_SwL3IpCtrlIpv4AdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv4AdminState_Object = MibTableColumn
swL3IpCtrlIpv4AdminState = _SwL3IpCtrlIpv4AdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 10),
    _SwL3IpCtrlIpv4AdminState_Type()
)
swL3IpCtrlIpv4AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv4AdminState.setStatus("current")


class _SwL3IpCtrlIpv6AdminState_Type(Integer32):
    """Custom type swL3IpCtrlIpv6AdminState based on Integer32"""
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


_SwL3IpCtrlIpv6AdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv6AdminState_Object = MibTableColumn
swL3IpCtrlIpv6AdminState = _SwL3IpCtrlIpv6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 12),
    _SwL3IpCtrlIpv6AdminState_Type()
)
swL3IpCtrlIpv6AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 16),
    _SwL3IpCtrlState_Type()
)
swL3IpCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlState.setStatus("current")


class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):
    """Custom type swL3IpCtrlIpv6LinkLocalAutoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv6LinkLocalAutoState_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState = _SwL3IpCtrlIpv6LinkLocalAutoState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 17),
    _SwL3IpCtrlIpv6LinkLocalAutoState_Type()
)
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAutoState.setStatus("current")


class _SwL3IpCtrlLocalProxyArp_Type(Integer32):
    """Custom type swL3IpCtrlLocalProxyArp based on Integer32"""
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


_SwL3IpCtrlLocalProxyArp_Type.__name__ = "Integer32"
_SwL3IpCtrlLocalProxyArp_Object = MibTableColumn
swL3IpCtrlLocalProxyArp = _SwL3IpCtrlLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 18),
    _SwL3IpCtrlLocalProxyArp_Type()
)
swL3IpCtrlLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlLocalProxyArp.setStatus("current")


class _SwL3IpCtrlIpMtu_Type(Integer32):
    """Custom type swL3IpCtrlIpMtu based on Integer32"""
    defaultValue = 1500


_SwL3IpCtrlIpMtu_Type.__name__ = "Integer32"
_SwL3IpCtrlIpMtu_Object = MibTableColumn
swL3IpCtrlIpMtu = _SwL3IpCtrlIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 19),
    _SwL3IpCtrlIpMtu_Type()
)
swL3IpCtrlIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlIpMtu.setStatus("current")
if mibBuilder.loadTexts:
    swL3IpCtrlIpMtu.setUnits("bytes")


class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):
    """Custom type swL3IpCtrlDhcpv6ClientState based on Integer32"""
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


_SwL3IpCtrlDhcpv6ClientState_Type.__name__ = "Integer32"
_SwL3IpCtrlDhcpv6ClientState_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientState = _SwL3IpCtrlDhcpv6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 20),
    _SwL3IpCtrlDhcpv6ClientState_Type()
)
swL3IpCtrlDhcpv6ClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientState.setStatus("current")


class _SwL3IpCtrlIpDirectedBroadcastState_Type(Integer32):
    """Custom type swL3IpCtrlIpDirectedBroadcastState based on Integer32"""
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


_SwL3IpCtrlIpDirectedBroadcastState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpDirectedBroadcastState_Object = MibTableColumn
swL3IpCtrlIpDirectedBroadcastState = _SwL3IpCtrlIpDirectedBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 21),
    _SwL3IpCtrlIpDirectedBroadcastState_Type()
)
swL3IpCtrlIpDirectedBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDirectedBroadcastState.setStatus("current")


class _SwL3IpCtrlIpDhcpOption12State_Type(Integer32):
    """Custom type swL3IpCtrlIpDhcpOption12State based on Integer32"""
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


_SwL3IpCtrlIpDhcpOption12State_Type.__name__ = "Integer32"
_SwL3IpCtrlIpDhcpOption12State_Object = MibTableColumn
swL3IpCtrlIpDhcpOption12State = _SwL3IpCtrlIpDhcpOption12State_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 22),
    _SwL3IpCtrlIpDhcpOption12State_Type()
)
swL3IpCtrlIpDhcpOption12State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12State.setStatus("current")


class _SwL3IpCtrlIpDhcpOption12HostName_Type(DisplayString):
    """Custom type swL3IpCtrlIpDhcpOption12HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SwL3IpCtrlIpDhcpOption12HostName_Type.__name__ = "DisplayString"
_SwL3IpCtrlIpDhcpOption12HostName_Object = MibTableColumn
swL3IpCtrlIpDhcpOption12HostName = _SwL3IpCtrlIpDhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 23),
    _SwL3IpCtrlIpDhcpOption12HostName_Type()
)
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12HostName.setStatus("current")


class _SwL3IpCtrlDhcpv6ClientPDState_Type(Integer32):
    """Custom type swL3IpCtrlDhcpv6ClientPDState based on Integer32"""
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


_SwL3IpCtrlDhcpv6ClientPDState_Type.__name__ = "Integer32"
_SwL3IpCtrlDhcpv6ClientPDState_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDState = _SwL3IpCtrlDhcpv6ClientPDState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 24),
    _SwL3IpCtrlDhcpv6ClientPDState_Type()
)
swL3IpCtrlDhcpv6ClientPDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDState.setStatus("current")


class _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type(DisplayString):
    """Custom type swL3IpCtrlDhcpv6ClientPDPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type.__name__ = "DisplayString"
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixName = _SwL3IpCtrlDhcpv6ClientPDPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 25),
    _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefixName.setStatus("current")
_SwL3IpCtrlDhcpv6ClientPDPrefix_Type = Ipv6Address
_SwL3IpCtrlDhcpv6ClientPDPrefix_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefix = _SwL3IpCtrlDhcpv6ClientPDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 26),
    _SwL3IpCtrlDhcpv6ClientPDPrefix_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefix.setStatus("current")
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type = Integer32
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixLen = _SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 3, 1, 27),
    _SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefixLen.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlEntry.setStatus("current")


class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6CtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6CtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6CtrlInterfaceName_Object = MibTableColumn
swL3Ipv6CtrlInterfaceName = _SwL3Ipv6CtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")
_SwL3Ipv6CtrlMaxReassmblySize_Type = Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object = MibTableColumn
swL3Ipv6CtrlMaxReassmblySize = _SwL3Ipv6CtrlMaxReassmblySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 2),
    _SwL3Ipv6CtrlMaxReassmblySize_Type()
)
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlMaxReassmblySize.setStatus("current")


class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):
    """Custom type swL3Ipv6CtrlNsRetransTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwL3Ipv6CtrlNsRetransTimer_Type.__name__ = "Unsigned32"
_SwL3Ipv6CtrlNsRetransTimer_Object = MibTableColumn
swL3Ipv6CtrlNsRetransTimer = _SwL3Ipv6CtrlNsRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 3),
    _SwL3Ipv6CtrlNsRetransTimer_Type()
)
swL3Ipv6CtrlNsRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlNsRetransTimer.setStatus("current")


class _SwL3Ipv6CtrlRaState_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaState based on Integer32"""
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


_SwL3Ipv6CtrlRaState_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaState_Object = MibTableColumn
swL3Ipv6CtrlRaState = _SwL3Ipv6CtrlRaState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 5),
    _SwL3Ipv6CtrlRaState_Type()
)
swL3Ipv6CtrlRaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaState.setStatus("current")


class _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaMinRtrAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1350),
    )


_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object = MibTableColumn
swL3Ipv6CtrlRaMinRtrAdvInterval = _SwL3Ipv6CtrlRaMinRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 6),
    _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type()
)
swL3Ipv6CtrlRaMinRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus("current")


class _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaMaxRtrAdvInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object = MibTableColumn
swL3Ipv6CtrlRaMaxRtrAdvInterval = _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 7),
    _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type()
)
swL3Ipv6CtrlRaMaxRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus("current")


class _SwL3Ipv6CtrlRaLifeTime_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_SwL3Ipv6CtrlRaLifeTime_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaLifeTime_Object = MibTableColumn
swL3Ipv6CtrlRaLifeTime = _SwL3Ipv6CtrlRaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 8),
    _SwL3Ipv6CtrlRaLifeTime_Type()
)
swL3Ipv6CtrlRaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaLifeTime.setStatus("current")


class _SwL3Ipv6CtrlRaReachableTime_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaReachableTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_SwL3Ipv6CtrlRaReachableTime_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaReachableTime_Object = MibTableColumn
swL3Ipv6CtrlRaReachableTime = _SwL3Ipv6CtrlRaReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 9),
    _SwL3Ipv6CtrlRaReachableTime_Type()
)
swL3Ipv6CtrlRaReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaReachableTime.setStatus("current")


class _SwL3Ipv6CtrlRaRetransTime_Type(Unsigned32):
    """Custom type swL3Ipv6CtrlRaRetransTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwL3Ipv6CtrlRaRetransTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6CtrlRaRetransTime_Object = MibTableColumn
swL3Ipv6CtrlRaRetransTime = _SwL3Ipv6CtrlRaRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 10),
    _SwL3Ipv6CtrlRaRetransTime_Type()
)
swL3Ipv6CtrlRaRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaRetransTime.setStatus("current")


class _SwL3Ipv6CtrlRaHopLimit_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3Ipv6CtrlRaHopLimit_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaHopLimit_Object = MibTableColumn
swL3Ipv6CtrlRaHopLimit = _SwL3Ipv6CtrlRaHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 11),
    _SwL3Ipv6CtrlRaHopLimit_Type()
)
swL3Ipv6CtrlRaHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaHopLimit.setStatus("current")


class _SwL3Ipv6CtrlRaManagedFlag_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaManagedFlag based on Integer32"""
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


_SwL3Ipv6CtrlRaManagedFlag_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaManagedFlag_Object = MibTableColumn
swL3Ipv6CtrlRaManagedFlag = _SwL3Ipv6CtrlRaManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 12),
    _SwL3Ipv6CtrlRaManagedFlag_Type()
)
swL3Ipv6CtrlRaManagedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaManagedFlag.setStatus("current")


class _SwL3Ipv6CtrlRaOtherConfigFlag_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaOtherConfigFlag based on Integer32"""
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


_SwL3Ipv6CtrlRaOtherConfigFlag_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaOtherConfigFlag_Object = MibTableColumn
swL3Ipv6CtrlRaOtherConfigFlag = _SwL3Ipv6CtrlRaOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 4, 1, 13),
    _SwL3Ipv6CtrlRaOtherConfigFlag_Type()
)
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaOtherConfigFlag.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlEntry.setStatus("current")


class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6AddressCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6AddressCtrlInterfaceName_Object = MibTableColumn
swL3Ipv6AddressCtrlInterfaceName = _SwL3Ipv6AddressCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 3),
    _SwL3Ipv6AddressCtrlPrefixLen_Type()
)
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPrefixLen.setStatus("current")


class _SwL3Ipv6AddressCtrlPreferredLifeTime_Type(Unsigned32):
    """Custom type swL3Ipv6AddressCtrlPreferredLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SwL3Ipv6AddressCtrlPreferredLifeTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6AddressCtrlPreferredLifeTime_Object = MibTableColumn
swL3Ipv6AddressCtrlPreferredLifeTime = _SwL3Ipv6AddressCtrlPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 4),
    _SwL3Ipv6AddressCtrlPreferredLifeTime_Type()
)
swL3Ipv6AddressCtrlPreferredLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPreferredLifeTime.setStatus("current")


class _SwL3Ipv6AddressCtrlValidLifeTime_Type(Unsigned32):
    """Custom type swL3Ipv6AddressCtrlValidLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SwL3Ipv6AddressCtrlValidLifeTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6AddressCtrlValidLifeTime_Object = MibTableColumn
swL3Ipv6AddressCtrlValidLifeTime = _SwL3Ipv6AddressCtrlValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 5),
    _SwL3Ipv6AddressCtrlValidLifeTime_Type()
)
swL3Ipv6AddressCtrlValidLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlValidLifeTime.setStatus("current")


class _SwL3Ipv6AddressCtrlOnLinkFlag_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlOnLinkFlag based on Integer32"""
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


_SwL3Ipv6AddressCtrlOnLinkFlag_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlOnLinkFlag_Object = MibTableColumn
swL3Ipv6AddressCtrlOnLinkFlag = _SwL3Ipv6AddressCtrlOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 6),
    _SwL3Ipv6AddressCtrlOnLinkFlag_Type()
)
swL3Ipv6AddressCtrlOnLinkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlOnLinkFlag.setStatus("current")


class _SwL3Ipv6AddressCtrlAutonomousFlag_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlAutonomousFlag based on Integer32"""
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


_SwL3Ipv6AddressCtrlAutonomousFlag_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlAutonomousFlag_Object = MibTableColumn
swL3Ipv6AddressCtrlAutonomousFlag = _SwL3Ipv6AddressCtrlAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 7),
    _SwL3Ipv6AddressCtrlAutonomousFlag_Type()
)
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAutonomousFlag.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 8),
    _SwL3Ipv6AddressCtrlState_Type()
)
swL3Ipv6AddressCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlState.setStatus("current")


class _SwL3Ipv6AddressCtrlAddressType_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dhcpv6", 2),
          ("stateless", 3))
    )


_SwL3Ipv6AddressCtrlAddressType_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlAddressType_Object = MibTableColumn
swL3Ipv6AddressCtrlAddressType = _SwL3Ipv6AddressCtrlAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 5, 1, 9),
    _SwL3Ipv6AddressCtrlAddressType_Type()
)
swL3Ipv6AddressCtrlAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAddressType.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object = MibTable
swL3Ipv6DHCPv6CPDAddrCtrlTable = _SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlTable.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object = MibTableRow
swL3Ipv6DHCPv6CPDAddrCtrlEntry = _SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1)
)
swL3Ipv6DHCPv6CPDAddrCtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlPrefixName"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen"),
)
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlEntry.setStatus("current")


class _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName = _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1, 1),
    _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setStatus("current")


class _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type(DisplayString):
    """Custom type swL3Ipv6DHCPv6CPDAddrCtrlPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type.__name__ = "DisplayString"
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName = _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1, 2),
    _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type = Ipv6Address
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr = _SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1, 3),
    _SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type = Integer32
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen = _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1, 4),
    _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type = RowStatus
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlState = _SwL3Ipv6DHCPv6CPDAddrCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 6, 1, 5),
    _SwL3Ipv6DHCPv6CPDAddrCtrlState_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlState.setStatus("current")


class _SwL3IpCtrlAllIpIfState_Type(Integer32):
    """Custom type swL3IpCtrlAllIpIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_SwL3IpCtrlAllIpIfState_Type.__name__ = "Integer32"
_SwL3IpCtrlAllIpIfState_Object = MibScalar
swL3IpCtrlAllIpIfState = _SwL3IpCtrlAllIpIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")
_SwL3LoopBackIpCtrlTable_Object = MibTable
swL3LoopBackIpCtrlTable = _SwL3LoopBackIpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlTable.setStatus("current")
_SwL3LoopBackIpCtrlEntry_Object = MibTableRow
swL3LoopBackIpCtrlEntry = _SwL3LoopBackIpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1)
)
swL3LoopBackIpCtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3LoopBackIpCtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlEntry.setStatus("current")


class _SwL3LoopBackIpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3LoopBackIpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3LoopBackIpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3LoopBackIpCtrlInterfaceName_Object = MibTableColumn
swL3LoopBackIpCtrlInterfaceName = _SwL3LoopBackIpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 1),
    _SwL3LoopBackIpCtrlInterfaceName_Type()
)
swL3LoopBackIpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlInterfaceName.setStatus("current")


class _SwL3LoopBackIpCtrlIfIndex_Type(Integer32):
    """Custom type swL3LoopBackIpCtrlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3LoopBackIpCtrlIfIndex_Type.__name__ = "Integer32"
_SwL3LoopBackIpCtrlIfIndex_Object = MibTableColumn
swL3LoopBackIpCtrlIfIndex = _SwL3LoopBackIpCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 2),
    _SwL3LoopBackIpCtrlIfIndex_Type()
)
swL3LoopBackIpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIfIndex.setStatus("current")
_SwL3LoopBackIpCtrlIpAddr_Type = IpAddress
_SwL3LoopBackIpCtrlIpAddr_Object = MibTableColumn
swL3LoopBackIpCtrlIpAddr = _SwL3LoopBackIpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 3),
    _SwL3LoopBackIpCtrlIpAddr_Type()
)
swL3LoopBackIpCtrlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIpAddr.setStatus("current")
_SwL3LoopBackIpCtrlIpSubnetMask_Type = IpAddress
_SwL3LoopBackIpCtrlIpSubnetMask_Object = MibTableColumn
swL3LoopBackIpCtrlIpSubnetMask = _SwL3LoopBackIpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 4),
    _SwL3LoopBackIpCtrlIpSubnetMask_Type()
)
swL3LoopBackIpCtrlIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIpSubnetMask.setStatus("current")


class _SwL3LoopBackIpCtrlAdminState_Type(Integer32):
    """Custom type swL3LoopBackIpCtrlAdminState based on Integer32"""
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


_SwL3LoopBackIpCtrlAdminState_Type.__name__ = "Integer32"
_SwL3LoopBackIpCtrlAdminState_Object = MibTableColumn
swL3LoopBackIpCtrlAdminState = _SwL3LoopBackIpCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 5),
    _SwL3LoopBackIpCtrlAdminState_Type()
)
swL3LoopBackIpCtrlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlAdminState.setStatus("current")
_SwL3LoopBackIpCtrlRowStatus_Type = RowStatus
_SwL3LoopBackIpCtrlRowStatus_Object = MibTableColumn
swL3LoopBackIpCtrlRowStatus = _SwL3LoopBackIpCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 1, 8, 1, 6),
    _SwL3LoopBackIpCtrlRowStatus_Type()
)
swL3LoopBackIpCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlRowStatus.setStatus("current")
_SwL3IpFdbMgmt_ObjectIdentity = ObjectIdentity
swL3IpFdbMgmt = _SwL3IpFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2)
)
_SwL3IpFdbInfoTable_Object = MibTable
swL3IpFdbInfoTable = _SwL3IpFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoTable.setStatus("current")
_SwL3IpFdbInfoEntry_Object = MibTableRow
swL3IpFdbInfoEntry = _SwL3IpFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1, 1)
)
swL3IpFdbInfoEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpFdbInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoEntry.setStatus("current")
_SwL3IpFdbInfoIpAddr_Type = IpAddress
_SwL3IpFdbInfoIpAddr_Object = MibTableColumn
swL3IpFdbInfoIpAddr = _SwL3IpFdbInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1, 1, 1),
    _SwL3IpFdbInfoIpAddr_Type()
)
swL3IpFdbInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpAddr.setStatus("current")
_SwL3IpFdbInfoIpSubnetMask_Type = IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object = MibTableColumn
swL3IpFdbInfoIpSubnetMask = _SwL3IpFdbInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1, 1, 2),
    _SwL3IpFdbInfoIpSubnetMask_Type()
)
swL3IpFdbInfoIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpSubnetMask.setStatus("current")


class _SwL3IpFdbInfoPort_Type(Integer32):
    """Custom type swL3IpFdbInfoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpFdbInfoPort_Type.__name__ = "Integer32"
_SwL3IpFdbInfoPort_Object = MibTableColumn
swL3IpFdbInfoPort = _SwL3IpFdbInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1, 1, 3),
    _SwL3IpFdbInfoPort_Type()
)
swL3IpFdbInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoPort.setStatus("current")


class _SwL3IpFdbInfoType_Type(Integer32):
    """Custom type swL3IpFdbInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("static", 2),
          ("dynamic", 3))
    )


_SwL3IpFdbInfoType_Type.__name__ = "Integer32"
_SwL3IpFdbInfoType_Object = MibTableColumn
swL3IpFdbInfoType = _SwL3IpFdbInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 2, 1, 1, 4),
    _SwL3IpFdbInfoType_Type()
)
swL3IpFdbInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoType.setStatus("current")


class _SwL3IpArpAgingTime_Type(Integer32):
    """Custom type swL3IpArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpArpAgingTime_Type.__name__ = "Integer32"
_SwL3IpArpAgingTime_Object = MibScalar
swL3IpArpAgingTime = _SwL3IpArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 4),
    _SwL3IpArpAgingTime_Type()
)
swL3IpArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpAgingTime.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 2),
    _SwL3IpStaticRouteMask_Type()
)
swL3IpStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMask.setStatus("current")


class _SwL3IpStaticRouteBkupState_Type(Integer32):
    """Custom type swL3IpStaticRouteBkupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("none", 3))
    )


_SwL3IpStaticRouteBkupState_Type.__name__ = "Integer32"
_SwL3IpStaticRouteBkupState_Object = MibTableColumn
swL3IpStaticRouteBkupState = _SwL3IpStaticRouteBkupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteBkupState_Type()
)
swL3IpStaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteBkupState.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 4),
    _SwL3IpStaticRouteNextHop_Type()
)
swL3IpStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteNextHop.setStatus("current")


class _SwL3IpStaticRouteMetric_Type(Integer32):
    """Custom type swL3IpStaticRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3IpStaticRouteMetric_Type.__name__ = "Integer32"
_SwL3IpStaticRouteMetric_Object = MibTableColumn
swL3IpStaticRouteMetric = _SwL3IpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 5),
    _SwL3IpStaticRouteMetric_Type()
)
swL3IpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMetric.setStatus("current")


class _SwL3IpStaticRouteStatus_Type(Integer32):
    """Custom type swL3IpStaticRouteStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("valid", 3),
          ("active", 4),
          ("inActive", 5))
    )


_SwL3IpStaticRouteStatus_Type.__name__ = "Integer32"
_SwL3IpStaticRouteStatus_Object = MibTableColumn
swL3IpStaticRouteStatus = _SwL3IpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 6),
    _SwL3IpStaticRouteStatus_Type()
)
swL3IpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteStatus.setStatus("current")


class _SwL3IpStaticRouteWeight_Type(Integer32):
    """Custom type swL3IpStaticRouteWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SwL3IpStaticRouteWeight_Type.__name__ = "Integer32"
_SwL3IpStaticRouteWeight_Object = MibTableColumn
swL3IpStaticRouteWeight = _SwL3IpStaticRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 7),
    _SwL3IpStaticRouteWeight_Type()
)
swL3IpStaticRouteWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteWeight.setStatus("current")
_SwL3IpStaticRouteInterfaceName_Type = DisplayString
_SwL3IpStaticRouteInterfaceName_Object = MibTableColumn
swL3IpStaticRouteInterfaceName = _SwL3IpStaticRouteInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 5, 1, 8),
    _SwL3IpStaticRouteInterfaceName_Type()
)
swL3IpStaticRouteInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteInterfaceName.setStatus("current")
_SwL3IpMcastMgmt_ObjectIdentity = ObjectIdentity
swL3IpMcastMgmt = _SwL3IpMcastMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 6)
)
_SwL3IpStaticRouteTunnelTable_Object = MibTable
swL3IpStaticRouteTunnelTable = _SwL3IpStaticRouteTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 7)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTunnelTable.setStatus("current")
_SwL3IpStaticRouteTunnelEntry_Object = MibTableRow
swL3IpStaticRouteTunnelEntry = _SwL3IpStaticRouteTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 7, 1)
)
swL3IpStaticRouteTunnelEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3IpStaticRouteTunnelInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTunnelEntry.setStatus("current")


class _SwL3IpStaticRouteTunnelInterfaceName_Type(DisplayString):
    """Custom type swL3IpStaticRouteTunnelInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL3IpStaticRouteTunnelInterfaceName_Type.__name__ = "DisplayString"
_SwL3IpStaticRouteTunnelInterfaceName_Object = MibTableColumn
swL3IpStaticRouteTunnelInterfaceName = _SwL3IpStaticRouteTunnelInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 7, 1, 1),
    _SwL3IpStaticRouteTunnelInterfaceName_Type()
)
swL3IpStaticRouteTunnelInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteTunnelInterfaceName.setStatus("current")
_SwL3IpStaticRouteTunnelRowStatus_Type = RowStatus
_SwL3IpStaticRouteTunnelRowStatus_Object = MibTableColumn
swL3IpStaticRouteTunnelRowStatus = _SwL3IpStaticRouteTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 2, 7, 1, 2),
    _SwL3IpStaticRouteTunnelRowStatus_Type()
)
swL3IpStaticRouteTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteTunnelRowStatus.setStatus("current")
_SwL3RelayMgmt_ObjectIdentity = ObjectIdentity
swL3RelayMgmt = _SwL3RelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3)
)
_SwL3RelayDnsMgmt_ObjectIdentity = ObjectIdentity
swL3RelayDnsMgmt = _SwL3RelayDnsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3)
)


class _SwL3RelayDnsState_Type(Integer32):
    """Custom type swL3RelayDnsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3RelayDnsState_Type.__name__ = "Integer32"
_SwL3RelayDnsState_Object = MibScalar
swL3RelayDnsState = _SwL3RelayDnsState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 1),
    _SwL3RelayDnsState_Type()
)
swL3RelayDnsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsState.setStatus("current")
_SwL3RelayDnsPrimaryServer_Type = IpAddress
_SwL3RelayDnsPrimaryServer_Object = MibScalar
swL3RelayDnsPrimaryServer = _SwL3RelayDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 2),
    _SwL3RelayDnsPrimaryServer_Type()
)
swL3RelayDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsPrimaryServer.setStatus("current")
_SwL3RelayDnsSecondaryServer_Type = IpAddress
_SwL3RelayDnsSecondaryServer_Object = MibScalar
swL3RelayDnsSecondaryServer = _SwL3RelayDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 3),
    _SwL3RelayDnsSecondaryServer_Type()
)
swL3RelayDnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsSecondaryServer.setStatus("current")


class _SwL3RelayDnsCacheState_Type(Integer32):
    """Custom type swL3RelayDnsCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3RelayDnsCacheState_Type.__name__ = "Integer32"
_SwL3RelayDnsCacheState_Object = MibScalar
swL3RelayDnsCacheState = _SwL3RelayDnsCacheState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 4),
    _SwL3RelayDnsCacheState_Type()
)
swL3RelayDnsCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCacheState.setStatus("current")


class _SwL3RelayDnsStaticTableState_Type(Integer32):
    """Custom type swL3RelayDnsStaticTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL3RelayDnsStaticTableState_Type.__name__ = "Integer32"
_SwL3RelayDnsStaticTableState_Object = MibScalar
swL3RelayDnsStaticTableState = _SwL3RelayDnsStaticTableState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 5),
    _SwL3RelayDnsStaticTableState_Type()
)
swL3RelayDnsStaticTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsStaticTableState.setStatus("current")
_SwL3RelayDnsCtrlTable_Object = MibTable
swL3RelayDnsCtrlTable = _SwL3RelayDnsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 6)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlTable.setStatus("current")
_SwL3RelayDnsCtrlEntry_Object = MibTableRow
swL3RelayDnsCtrlEntry = _SwL3RelayDnsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 6, 1)
)
swL3RelayDnsCtrlEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3RelayDnsCtrlDomainName"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"),
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlEntry.setStatus("current")


class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):
    """Custom type swL3RelayDnsCtrlDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL3RelayDnsCtrlDomainName_Type.__name__ = "DisplayString"
_SwL3RelayDnsCtrlDomainName_Object = MibTableColumn
swL3RelayDnsCtrlDomainName = _SwL3RelayDnsCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 6, 1, 1),
    _SwL3RelayDnsCtrlDomainName_Type()
)
swL3RelayDnsCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlDomainName.setStatus("current")
_SwL3RelayDnsCtrlIpAddr_Type = IpAddress
_SwL3RelayDnsCtrlIpAddr_Object = MibTableColumn
swL3RelayDnsCtrlIpAddr = _SwL3RelayDnsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 6, 1, 2),
    _SwL3RelayDnsCtrlIpAddr_Type()
)
swL3RelayDnsCtrlIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlIpAddr.setStatus("current")


class _SwL3RelayDnsCtrlState_Type(Integer32):
    """Custom type swL3RelayDnsCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("valid", 3))
    )


_SwL3RelayDnsCtrlState_Type.__name__ = "Integer32"
_SwL3RelayDnsCtrlState_Object = MibTableColumn
swL3RelayDnsCtrlState = _SwL3RelayDnsCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 3, 3, 6, 1, 3),
    _SwL3RelayDnsCtrlState_Type()
)
swL3RelayDnsCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlState.setStatus("current")
_SwL3RouteRedistriTable_Object = MibTable
swL3RouteRedistriTable = _SwL3RouteRedistriTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5)
)
if mibBuilder.loadTexts:
    swL3RouteRedistriTable.setStatus("current")
_SwL3RouteRedistriEntry_Object = MibTableRow
swL3RouteRedistriEntry = _SwL3RouteRedistriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1)
)
swL3RouteRedistriEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3RouteRedistriSrcProtocol"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3RouteRedistriDstProtocol"),
)
if mibBuilder.loadTexts:
    swL3RouteRedistriEntry.setStatus("current")


class _SwL3RouteRedistriSrcProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriSrcProtocol based on Integer32"""
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
        *(("other", 1),
          ("rip", 2),
          ("ospf", 3),
          ("static", 4),
          ("local", 5),
          ("bgp", 6))
    )


_SwL3RouteRedistriSrcProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriSrcProtocol_Object = MibTableColumn
swL3RouteRedistriSrcProtocol = _SwL3RouteRedistriSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1, 1),
    _SwL3RouteRedistriSrcProtocol_Type()
)
swL3RouteRedistriSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriSrcProtocol.setStatus("current")


class _SwL3RouteRedistriDstProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriDstProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rip", 2),
          ("ospf", 3),
          ("bgp", 6))
    )


_SwL3RouteRedistriDstProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriDstProtocol_Object = MibTableColumn
swL3RouteRedistriDstProtocol = _SwL3RouteRedistriDstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1, 2),
    _SwL3RouteRedistriDstProtocol_Type()
)
swL3RouteRedistriDstProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriDstProtocol.setStatus("current")


class _SwL3RouteRedistriType_Type(Integer32):
    """Custom type swL3RouteRedistriType based on Integer32"""
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
        *(("other", 1),
          ("all", 2),
          ("type-1", 3),
          ("type-2", 4),
          ("internal", 5),
          ("external", 6),
          ("inter-E1", 7),
          ("inter-E2", 8),
          ("extType1", 9),
          ("extType2", 10))
    )


_SwL3RouteRedistriType_Type.__name__ = "Integer32"
_SwL3RouteRedistriType_Object = MibTableColumn
swL3RouteRedistriType = _SwL3RouteRedistriType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1, 3),
    _SwL3RouteRedistriType_Type()
)
swL3RouteRedistriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriType.setStatus("current")
_SwL3RouteRedistriMetric_Type = Unsigned32
_SwL3RouteRedistriMetric_Object = MibTableColumn
swL3RouteRedistriMetric = _SwL3RouteRedistriMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1, 4),
    _SwL3RouteRedistriMetric_Type()
)
swL3RouteRedistriMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriMetric.setStatus("current")
_SwL3RouteRedistriRowStatus_Type = RowStatus
_SwL3RouteRedistriRowStatus_Object = MibTableColumn
swL3RouteRedistriRowStatus = _SwL3RouteRedistriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 5, 1, 5),
    _SwL3RouteRedistriRowStatus_Type()
)
swL3RouteRedistriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriRowStatus.setStatus("current")
_SwL3RoutePreference_ObjectIdentity = ObjectIdentity
swL3RoutePreference = _SwL3RoutePreference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 9)
)


class _SwL3RoutePreferenceRIP_Type(Integer32):
    """Custom type swL3RoutePreferenceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceRIP_Type.__name__ = "Integer32"
_SwL3RoutePreferenceRIP_Object = MibScalar
swL3RoutePreferenceRIP = _SwL3RoutePreferenceRIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 9, 1),
    _SwL3RoutePreferenceRIP_Type()
)
swL3RoutePreferenceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceRIP.setStatus("current")


class _SwL3RoutePreferenceStatic_Type(Integer32):
    """Custom type swL3RoutePreferenceStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceStatic_Type.__name__ = "Integer32"
_SwL3RoutePreferenceStatic_Object = MibScalar
swL3RoutePreferenceStatic = _SwL3RoutePreferenceStatic_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 9, 3),
    _SwL3RoutePreferenceStatic_Type()
)
swL3RoutePreferenceStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceStatic.setStatus("current")


class _SwL3RoutePreferenceLocal_Type(Integer32):
    """Custom type swL3RoutePreferenceLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_SwL3RoutePreferenceLocal_Type.__name__ = "Integer32"
_SwL3RoutePreferenceLocal_Object = MibScalar
swL3RoutePreferenceLocal = _SwL3RoutePreferenceLocal_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 9, 4),
    _SwL3RoutePreferenceLocal_Type()
)
swL3RoutePreferenceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RoutePreferenceLocal.setStatus("current")


class _SwL3RoutePreferenceDefault_Type(Integer32):
    """Custom type swL3RoutePreferenceDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceDefault_Type.__name__ = "Integer32"
_SwL3RoutePreferenceDefault_Object = MibScalar
swL3RoutePreferenceDefault = _SwL3RoutePreferenceDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 9, 8),
    _SwL3RoutePreferenceDefault_Type()
)
swL3RoutePreferenceDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceDefault.setStatus("current")
_SwL3OspfLsdbMgmt_ObjectIdentity = ObjectIdentity
swL3OspfLsdbMgmt = _SwL3OspfLsdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 13)
)
_SwL3VrrpOperMgmt_ObjectIdentity = ObjectIdentity
swL3VrrpOperMgmt = _SwL3VrrpOperMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14)
)
_SwL3VrrpOperTable_Object = MibTable
swL3VrrpOperTable = _SwL3VrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1)
)
if mibBuilder.loadTexts:
    swL3VrrpOperTable.setStatus("current")
_SwL3VrrpOperEntry_Object = MibTableRow
swL3VrrpOperEntry = _SwL3VrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1)
)
swL3VrrpOperEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3VrrpOperIfIndex"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3VrrpOperVrId"),
)
if mibBuilder.loadTexts:
    swL3VrrpOperEntry.setStatus("current")
_SwL3VrrpOperIfIndex_Type = Integer32
_SwL3VrrpOperIfIndex_Object = MibTableColumn
swL3VrrpOperIfIndex = _SwL3VrrpOperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 1),
    _SwL3VrrpOperIfIndex_Type()
)
swL3VrrpOperIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperIfIndex.setStatus("current")
_SwL3VrrpOperVrId_Type = VrId
_SwL3VrrpOperVrId_Object = MibTableColumn
swL3VrrpOperVrId = _SwL3VrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 2),
    _SwL3VrrpOperVrId_Type()
)
swL3VrrpOperVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVrId.setStatus("current")
_SwL3VrrpOperVirtualMacAddr_Type = MacAddress
_SwL3VrrpOperVirtualMacAddr_Object = MibTableColumn
swL3VrrpOperVirtualMacAddr = _SwL3VrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 3),
    _SwL3VrrpOperVirtualMacAddr_Type()
)
swL3VrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualMacAddr.setStatus("current")


class _SwL3VrrpOperState_Type(Integer32):
    """Custom type swL3VrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("backup", 2),
          ("master", 3))
    )


_SwL3VrrpOperState_Type.__name__ = "Integer32"
_SwL3VrrpOperState_Object = MibTableColumn
swL3VrrpOperState = _SwL3VrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 4),
    _SwL3VrrpOperState_Type()
)
swL3VrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperState.setStatus("current")


class _SwL3VrrpOperAdminState_Type(Integer32):
    """Custom type swL3VrrpOperAdminState based on Integer32"""
    defaultValue = 2

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


_SwL3VrrpOperAdminState_Type.__name__ = "Integer32"
_SwL3VrrpOperAdminState_Object = MibTableColumn
swL3VrrpOperAdminState = _SwL3VrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 5),
    _SwL3VrrpOperAdminState_Type()
)
swL3VrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAdminState.setStatus("current")


class _SwL3VrrpOperPriority_Type(Integer32):
    """Custom type swL3VrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3VrrpOperPriority_Type.__name__ = "Integer32"
_SwL3VrrpOperPriority_Object = MibTableColumn
swL3VrrpOperPriority = _SwL3VrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 6),
    _SwL3VrrpOperPriority_Type()
)
swL3VrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperPriority.setStatus("current")
_SwL3VrrpOperMasterIpAddr_Type = IpAddress
_SwL3VrrpOperMasterIpAddr_Object = MibTableColumn
swL3VrrpOperMasterIpAddr = _SwL3VrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 7),
    _SwL3VrrpOperMasterIpAddr_Type()
)
swL3VrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperMasterIpAddr.setStatus("current")


class _SwL3VrrpOperCriticalIpAddr_Type(IpAddress):
    """Custom type swL3VrrpOperCriticalIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SwL3VrrpOperCriticalIpAddr_Type.__name__ = "IpAddress"
_SwL3VrrpOperCriticalIpAddr_Object = MibTableColumn
swL3VrrpOperCriticalIpAddr = _SwL3VrrpOperCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 8),
    _SwL3VrrpOperCriticalIpAddr_Type()
)
swL3VrrpOperCriticalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperCriticalIpAddr.setStatus("current")


class _SwL3VrrpOperCheckCriticalIpState_Type(Integer32):
    """Custom type swL3VrrpOperCheckCriticalIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_SwL3VrrpOperCheckCriticalIpState_Type.__name__ = "Integer32"
_SwL3VrrpOperCheckCriticalIpState_Object = MibTableColumn
swL3VrrpOperCheckCriticalIpState = _SwL3VrrpOperCheckCriticalIpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 9),
    _SwL3VrrpOperCheckCriticalIpState_Type()
)
swL3VrrpOperCheckCriticalIpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperCheckCriticalIpState.setStatus("current")


class _SwL3VrrpOperAuthType_Type(Integer32):
    """Custom type swL3VrrpOperAuthType based on Integer32"""
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
        *(("noAuthentication", 1),
          ("simpleTextPassword", 2),
          ("ipAuthenticationHeader", 3))
    )


_SwL3VrrpOperAuthType_Type.__name__ = "Integer32"
_SwL3VrrpOperAuthType_Object = MibTableColumn
swL3VrrpOperAuthType = _SwL3VrrpOperAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 10),
    _SwL3VrrpOperAuthType_Type()
)
swL3VrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAuthType.setStatus("current")


class _SwL3VrrpOperAuthKey_Type(OctetString):
    """Custom type swL3VrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwL3VrrpOperAuthKey_Type.__name__ = "OctetString"
_SwL3VrrpOperAuthKey_Object = MibTableColumn
swL3VrrpOperAuthKey = _SwL3VrrpOperAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 11),
    _SwL3VrrpOperAuthKey_Type()
)
swL3VrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAuthKey.setStatus("current")


class _SwL3VrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type swL3VrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL3VrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_SwL3VrrpOperAdvertisementInterval_Object = MibTableColumn
swL3VrrpOperAdvertisementInterval = _SwL3VrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 12),
    _SwL3VrrpOperAdvertisementInterval_Type()
)
swL3VrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    swL3VrrpOperAdvertisementInterval.setUnits("seconds")


class _SwL3VrrpOperPreemptMode_Type(TruthValue):
    """Custom type swL3VrrpOperPreemptMode based on TruthValue"""
    defaultValue = 1


_SwL3VrrpOperPreemptMode_Type.__name__ = "TruthValue"
_SwL3VrrpOperPreemptMode_Object = MibTableColumn
swL3VrrpOperPreemptMode = _SwL3VrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 13),
    _SwL3VrrpOperPreemptMode_Type()
)
swL3VrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperPreemptMode.setStatus("current")
_SwL3VrrpOperVirtualRouterUpTime_Type = TimeStamp
_SwL3VrrpOperVirtualRouterUpTime_Object = MibTableColumn
swL3VrrpOperVirtualRouterUpTime = _SwL3VrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 14),
    _SwL3VrrpOperVirtualRouterUpTime_Type()
)
swL3VrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualRouterUpTime.setStatus("current")
_SwL3VrrpOperVirtualIpAddr_Type = IpAddress
_SwL3VrrpOperVirtualIpAddr_Object = MibTableColumn
swL3VrrpOperVirtualIpAddr = _SwL3VrrpOperVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 15),
    _SwL3VrrpOperVirtualIpAddr_Type()
)
swL3VrrpOperVirtualIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualIpAddr.setStatus("current")
_SwL3VrrpOperRowStatus_Type = RowStatus
_SwL3VrrpOperRowStatus_Object = MibTableColumn
swL3VrrpOperRowStatus = _SwL3VrrpOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 14, 1, 1, 16),
    _SwL3VrrpOperRowStatus_Type()
)
swL3VrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperRowStatus.setStatus("current")
_SwL3RIPTimerMgmt_ObjectIdentity = ObjectIdentity
swL3RIPTimerMgmt = _SwL3RIPTimerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 17)
)


class _SwL3RIPUpdateTime_Type(Integer32):
    """Custom type swL3RIPUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SwL3RIPUpdateTime_Type.__name__ = "Integer32"
_SwL3RIPUpdateTime_Object = MibScalar
swL3RIPUpdateTime = _SwL3RIPUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 17, 1),
    _SwL3RIPUpdateTime_Type()
)
swL3RIPUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RIPUpdateTime.setStatus("current")


class _SwL3RIPTimeOutTime_Type(Integer32):
    """Custom type swL3RIPTimeOutTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SwL3RIPTimeOutTime_Type.__name__ = "Integer32"
_SwL3RIPTimeOutTime_Object = MibScalar
swL3RIPTimeOutTime = _SwL3RIPTimeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 17, 2),
    _SwL3RIPTimeOutTime_Type()
)
swL3RIPTimeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RIPTimeOutTime.setStatus("current")


class _SwL3RIPGarbageCollectionTime_Type(Integer32):
    """Custom type swL3RIPGarbageCollectionTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SwL3RIPGarbageCollectionTime_Type.__name__ = "Integer32"
_SwL3RIPGarbageCollectionTime_Object = MibScalar
swL3RIPGarbageCollectionTime = _SwL3RIPGarbageCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 17, 3),
    _SwL3RIPGarbageCollectionTime_Type()
)
swL3RIPGarbageCollectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RIPGarbageCollectionTime.setStatus("current")
_SwL3Route6RedistriTable_Object = MibTable
swL3Route6RedistriTable = _SwL3Route6RedistriTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20)
)
if mibBuilder.loadTexts:
    swL3Route6RedistriTable.setStatus("current")
_SwL3Route6RedistriEntry_Object = MibTableRow
swL3Route6RedistriEntry = _SwL3Route6RedistriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1)
)
swL3Route6RedistriEntry.setIndexNames(
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Route6RedistriSrcProtocol"),
    (0, "DGS-3420-26SC-L3MGMT-MIB", "swL3Route6RedistriDstProtocol"),
)
if mibBuilder.loadTexts:
    swL3Route6RedistriEntry.setStatus("current")


class _SwL3Route6RedistriSrcProtocol_Type(Integer32):
    """Custom type swL3Route6RedistriSrcProtocol based on Integer32"""
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
        *(("local", 1),
          ("static", 2),
          ("ripng", 3),
          ("ospfv3", 4))
    )


_SwL3Route6RedistriSrcProtocol_Type.__name__ = "Integer32"
_SwL3Route6RedistriSrcProtocol_Object = MibTableColumn
swL3Route6RedistriSrcProtocol = _SwL3Route6RedistriSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1, 1),
    _SwL3Route6RedistriSrcProtocol_Type()
)
swL3Route6RedistriSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Route6RedistriSrcProtocol.setStatus("current")


class _SwL3Route6RedistriDstProtocol_Type(Integer32):
    """Custom type swL3Route6RedistriDstProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripng", 1),
          ("ospfv3", 2))
    )


_SwL3Route6RedistriDstProtocol_Type.__name__ = "Integer32"
_SwL3Route6RedistriDstProtocol_Object = MibTableColumn
swL3Route6RedistriDstProtocol = _SwL3Route6RedistriDstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1, 2),
    _SwL3Route6RedistriDstProtocol_Type()
)
swL3Route6RedistriDstProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Route6RedistriDstProtocol.setStatus("current")


class _SwL3Route6RedistriType_Type(Integer32):
    """Custom type swL3Route6RedistriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type-1", 1),
          ("type-2", 2),
          ("all", 3))
    )


_SwL3Route6RedistriType_Type.__name__ = "Integer32"
_SwL3Route6RedistriType_Object = MibTableColumn
swL3Route6RedistriType = _SwL3Route6RedistriType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1, 3),
    _SwL3Route6RedistriType_Type()
)
swL3Route6RedistriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Route6RedistriType.setStatus("current")
_SwL3Route6RedistriMetric_Type = Unsigned32
_SwL3Route6RedistriMetric_Object = MibTableColumn
swL3Route6RedistriMetric = _SwL3Route6RedistriMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1, 4),
    _SwL3Route6RedistriMetric_Type()
)
swL3Route6RedistriMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Route6RedistriMetric.setStatus("current")
_SwL3Route6RedistriRowStatus_Type = RowStatus
_SwL3Route6RedistriRowStatus_Object = MibTableColumn
swL3Route6RedistriRowStatus = _SwL3Route6RedistriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6, 3, 20, 1, 5),
    _SwL3Route6RedistriRowStatus_Type()
)
swL3Route6RedistriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Route6RedistriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-3420-26SC-L3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "VrId": VrId,
       "swL3MgmtMIB": swL3MgmtMIB,
       "swL3DevMgmt": swL3DevMgmt,
       "swL3DevCtrl": swL3DevCtrl,
       "swL3DevCtrlRIPState": swL3DevCtrlRIPState,
       "swL3DevCtrlVRRPState": swL3DevCtrlVRRPState,
       "swL3DevCtrlVrrpPingState": swL3DevCtrlVrrpPingState,
       "swL3IpMgmt": swL3IpMgmt,
       "swL3IpCtrlMgmt": swL3IpCtrlMgmt,
       "swL3IpCtrlTable": swL3IpCtrlTable,
       "swL3IpCtrlEntry": swL3IpCtrlEntry,
       "swL3IpCtrlInterfaceName": swL3IpCtrlInterfaceName,
       "swL3IpCtrlIfIndex": swL3IpCtrlIfIndex,
       "swL3IpCtrlIpAddr": swL3IpCtrlIpAddr,
       "swL3IpCtrlIpSubnetMask": swL3IpCtrlIpSubnetMask,
       "swL3IpCtrlVlanName": swL3IpCtrlVlanName,
       "swL3IpCtrlProxyArp": swL3IpCtrlProxyArp,
       "swL3IpCtrlSecondary": swL3IpCtrlSecondary,
       "swL3IpCtrlMode": swL3IpCtrlMode,
       "swL3IpCtrlAdminState": swL3IpCtrlAdminState,
       "swL3IpCtrlIpv4AdminState": swL3IpCtrlIpv4AdminState,
       "swL3IpCtrlIpv6AdminState": swL3IpCtrlIpv6AdminState,
       "swL3IpCtrlIpv6LinkLocalAddress": swL3IpCtrlIpv6LinkLocalAddress,
       "swL3IpCtrlIpv6LinkLocalPrefixLen": swL3IpCtrlIpv6LinkLocalPrefixLen,
       "swL3IpCtrlState": swL3IpCtrlState,
       "swL3IpCtrlIpv6LinkLocalAutoState": swL3IpCtrlIpv6LinkLocalAutoState,
       "swL3IpCtrlLocalProxyArp": swL3IpCtrlLocalProxyArp,
       "swL3IpCtrlIpMtu": swL3IpCtrlIpMtu,
       "swL3IpCtrlDhcpv6ClientState": swL3IpCtrlDhcpv6ClientState,
       "swL3IpCtrlIpDirectedBroadcastState": swL3IpCtrlIpDirectedBroadcastState,
       "swL3IpCtrlIpDhcpOption12State": swL3IpCtrlIpDhcpOption12State,
       "swL3IpCtrlIpDhcpOption12HostName": swL3IpCtrlIpDhcpOption12HostName,
       "swL3IpCtrlDhcpv6ClientPDState": swL3IpCtrlDhcpv6ClientPDState,
       "swL3IpCtrlDhcpv6ClientPDPrefixName": swL3IpCtrlDhcpv6ClientPDPrefixName,
       "swL3IpCtrlDhcpv6ClientPDPrefix": swL3IpCtrlDhcpv6ClientPDPrefix,
       "swL3IpCtrlDhcpv6ClientPDPrefixLen": swL3IpCtrlDhcpv6ClientPDPrefixLen,
       "swL3Ipv6CtrlTable": swL3Ipv6CtrlTable,
       "swL3Ipv6CtrlEntry": swL3Ipv6CtrlEntry,
       "swL3Ipv6CtrlInterfaceName": swL3Ipv6CtrlInterfaceName,
       "swL3Ipv6CtrlMaxReassmblySize": swL3Ipv6CtrlMaxReassmblySize,
       "swL3Ipv6CtrlNsRetransTimer": swL3Ipv6CtrlNsRetransTimer,
       "swL3Ipv6CtrlRaState": swL3Ipv6CtrlRaState,
       "swL3Ipv6CtrlRaMinRtrAdvInterval": swL3Ipv6CtrlRaMinRtrAdvInterval,
       "swL3Ipv6CtrlRaMaxRtrAdvInterval": swL3Ipv6CtrlRaMaxRtrAdvInterval,
       "swL3Ipv6CtrlRaLifeTime": swL3Ipv6CtrlRaLifeTime,
       "swL3Ipv6CtrlRaReachableTime": swL3Ipv6CtrlRaReachableTime,
       "swL3Ipv6CtrlRaRetransTime": swL3Ipv6CtrlRaRetransTime,
       "swL3Ipv6CtrlRaHopLimit": swL3Ipv6CtrlRaHopLimit,
       "swL3Ipv6CtrlRaManagedFlag": swL3Ipv6CtrlRaManagedFlag,
       "swL3Ipv6CtrlRaOtherConfigFlag": swL3Ipv6CtrlRaOtherConfigFlag,
       "swL3Ipv6AddressCtrlTable": swL3Ipv6AddressCtrlTable,
       "swL3Ipv6AddressCtrlEntry": swL3Ipv6AddressCtrlEntry,
       "swL3Ipv6AddressCtrlInterfaceName": swL3Ipv6AddressCtrlInterfaceName,
       "swL3Ipv6Address": swL3Ipv6Address,
       "swL3Ipv6AddressCtrlPrefixLen": swL3Ipv6AddressCtrlPrefixLen,
       "swL3Ipv6AddressCtrlPreferredLifeTime": swL3Ipv6AddressCtrlPreferredLifeTime,
       "swL3Ipv6AddressCtrlValidLifeTime": swL3Ipv6AddressCtrlValidLifeTime,
       "swL3Ipv6AddressCtrlOnLinkFlag": swL3Ipv6AddressCtrlOnLinkFlag,
       "swL3Ipv6AddressCtrlAutonomousFlag": swL3Ipv6AddressCtrlAutonomousFlag,
       "swL3Ipv6AddressCtrlState": swL3Ipv6AddressCtrlState,
       "swL3Ipv6AddressCtrlAddressType": swL3Ipv6AddressCtrlAddressType,
       "swL3Ipv6DHCPv6CPDAddrCtrlTable": swL3Ipv6DHCPv6CPDAddrCtrlTable,
       "swL3Ipv6DHCPv6CPDAddrCtrlEntry": swL3Ipv6DHCPv6CPDAddrCtrlEntry,
       "swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName": swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName,
       "swL3Ipv6DHCPv6CPDAddrCtrlPrefixName": swL3Ipv6DHCPv6CPDAddrCtrlPrefixName,
       "swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr": swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr,
       "swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen": swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen,
       "swL3Ipv6DHCPv6CPDAddrCtrlState": swL3Ipv6DHCPv6CPDAddrCtrlState,
       "swL3IpCtrlAllIpIfState": swL3IpCtrlAllIpIfState,
       "swL3LoopBackIpCtrlTable": swL3LoopBackIpCtrlTable,
       "swL3LoopBackIpCtrlEntry": swL3LoopBackIpCtrlEntry,
       "swL3LoopBackIpCtrlInterfaceName": swL3LoopBackIpCtrlInterfaceName,
       "swL3LoopBackIpCtrlIfIndex": swL3LoopBackIpCtrlIfIndex,
       "swL3LoopBackIpCtrlIpAddr": swL3LoopBackIpCtrlIpAddr,
       "swL3LoopBackIpCtrlIpSubnetMask": swL3LoopBackIpCtrlIpSubnetMask,
       "swL3LoopBackIpCtrlAdminState": swL3LoopBackIpCtrlAdminState,
       "swL3LoopBackIpCtrlRowStatus": swL3LoopBackIpCtrlRowStatus,
       "swL3IpFdbMgmt": swL3IpFdbMgmt,
       "swL3IpFdbInfoTable": swL3IpFdbInfoTable,
       "swL3IpFdbInfoEntry": swL3IpFdbInfoEntry,
       "swL3IpFdbInfoIpAddr": swL3IpFdbInfoIpAddr,
       "swL3IpFdbInfoIpSubnetMask": swL3IpFdbInfoIpSubnetMask,
       "swL3IpFdbInfoPort": swL3IpFdbInfoPort,
       "swL3IpFdbInfoType": swL3IpFdbInfoType,
       "swL3IpArpAgingTime": swL3IpArpAgingTime,
       "swL3IpStaticRouteTable": swL3IpStaticRouteTable,
       "swL3IpStaticRouteEntry": swL3IpStaticRouteEntry,
       "swL3IpStaticRouteDest": swL3IpStaticRouteDest,
       "swL3IpStaticRouteMask": swL3IpStaticRouteMask,
       "swL3IpStaticRouteBkupState": swL3IpStaticRouteBkupState,
       "swL3IpStaticRouteNextHop": swL3IpStaticRouteNextHop,
       "swL3IpStaticRouteMetric": swL3IpStaticRouteMetric,
       "swL3IpStaticRouteStatus": swL3IpStaticRouteStatus,
       "swL3IpStaticRouteWeight": swL3IpStaticRouteWeight,
       "swL3IpStaticRouteInterfaceName": swL3IpStaticRouteInterfaceName,
       "swL3IpMcastMgmt": swL3IpMcastMgmt,
       "swL3IpStaticRouteTunnelTable": swL3IpStaticRouteTunnelTable,
       "swL3IpStaticRouteTunnelEntry": swL3IpStaticRouteTunnelEntry,
       "swL3IpStaticRouteTunnelInterfaceName": swL3IpStaticRouteTunnelInterfaceName,
       "swL3IpStaticRouteTunnelRowStatus": swL3IpStaticRouteTunnelRowStatus,
       "swL3RelayMgmt": swL3RelayMgmt,
       "swL3RelayDnsMgmt": swL3RelayDnsMgmt,
       "swL3RelayDnsState": swL3RelayDnsState,
       "swL3RelayDnsPrimaryServer": swL3RelayDnsPrimaryServer,
       "swL3RelayDnsSecondaryServer": swL3RelayDnsSecondaryServer,
       "swL3RelayDnsCacheState": swL3RelayDnsCacheState,
       "swL3RelayDnsStaticTableState": swL3RelayDnsStaticTableState,
       "swL3RelayDnsCtrlTable": swL3RelayDnsCtrlTable,
       "swL3RelayDnsCtrlEntry": swL3RelayDnsCtrlEntry,
       "swL3RelayDnsCtrlDomainName": swL3RelayDnsCtrlDomainName,
       "swL3RelayDnsCtrlIpAddr": swL3RelayDnsCtrlIpAddr,
       "swL3RelayDnsCtrlState": swL3RelayDnsCtrlState,
       "swL3RouteRedistriTable": swL3RouteRedistriTable,
       "swL3RouteRedistriEntry": swL3RouteRedistriEntry,
       "swL3RouteRedistriSrcProtocol": swL3RouteRedistriSrcProtocol,
       "swL3RouteRedistriDstProtocol": swL3RouteRedistriDstProtocol,
       "swL3RouteRedistriType": swL3RouteRedistriType,
       "swL3RouteRedistriMetric": swL3RouteRedistriMetric,
       "swL3RouteRedistriRowStatus": swL3RouteRedistriRowStatus,
       "swL3RoutePreference": swL3RoutePreference,
       "swL3RoutePreferenceRIP": swL3RoutePreferenceRIP,
       "swL3RoutePreferenceStatic": swL3RoutePreferenceStatic,
       "swL3RoutePreferenceLocal": swL3RoutePreferenceLocal,
       "swL3RoutePreferenceDefault": swL3RoutePreferenceDefault,
       "swL3OspfLsdbMgmt": swL3OspfLsdbMgmt,
       "swL3VrrpOperMgmt": swL3VrrpOperMgmt,
       "swL3VrrpOperTable": swL3VrrpOperTable,
       "swL3VrrpOperEntry": swL3VrrpOperEntry,
       "swL3VrrpOperIfIndex": swL3VrrpOperIfIndex,
       "swL3VrrpOperVrId": swL3VrrpOperVrId,
       "swL3VrrpOperVirtualMacAddr": swL3VrrpOperVirtualMacAddr,
       "swL3VrrpOperState": swL3VrrpOperState,
       "swL3VrrpOperAdminState": swL3VrrpOperAdminState,
       "swL3VrrpOperPriority": swL3VrrpOperPriority,
       "swL3VrrpOperMasterIpAddr": swL3VrrpOperMasterIpAddr,
       "swL3VrrpOperCriticalIpAddr": swL3VrrpOperCriticalIpAddr,
       "swL3VrrpOperCheckCriticalIpState": swL3VrrpOperCheckCriticalIpState,
       "swL3VrrpOperAuthType": swL3VrrpOperAuthType,
       "swL3VrrpOperAuthKey": swL3VrrpOperAuthKey,
       "swL3VrrpOperAdvertisementInterval": swL3VrrpOperAdvertisementInterval,
       "swL3VrrpOperPreemptMode": swL3VrrpOperPreemptMode,
       "swL3VrrpOperVirtualRouterUpTime": swL3VrrpOperVirtualRouterUpTime,
       "swL3VrrpOperVirtualIpAddr": swL3VrrpOperVirtualIpAddr,
       "swL3VrrpOperRowStatus": swL3VrrpOperRowStatus,
       "swL3RIPTimerMgmt": swL3RIPTimerMgmt,
       "swL3RIPUpdateTime": swL3RIPUpdateTime,
       "swL3RIPTimeOutTime": swL3RIPTimeOutTime,
       "swL3RIPGarbageCollectionTime": swL3RIPGarbageCollectionTime,
       "swL3Route6RedistriTable": swL3Route6RedistriTable,
       "swL3Route6RedistriEntry": swL3Route6RedistriEntry,
       "swL3Route6RedistriSrcProtocol": swL3Route6RedistriSrcProtocol,
       "swL3Route6RedistriDstProtocol": swL3Route6RedistriDstProtocol,
       "swL3Route6RedistriType": swL3Route6RedistriType,
       "swL3Route6RedistriMetric": swL3Route6RedistriMetric,
       "swL3Route6RedistriRowStatus": swL3Route6RedistriRowStatus}
)
