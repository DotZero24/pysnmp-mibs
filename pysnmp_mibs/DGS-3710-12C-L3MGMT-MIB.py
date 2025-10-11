# SNMP MIB module (DGS-3710-12C-L3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DGS-3710-12C-L3MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:34 2025
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

(dgs3712c,) = mibBuilder.importSymbols(
    "SW3700PRIMGMT-MIB",
    "dgs3712c")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3)
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



class Ipv6Address(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class VrId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3IpCtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 5),
    _SwL3IpCtrlVlanName_Type()
)
swL3IpCtrlVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlVlanName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 12),
    _SwL3IpCtrlIpv6AdminState_Type()
)
swL3IpCtrlIpv6AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 17),
    _SwL3IpCtrlIpv6LinkLocalAutoState_Type()
)
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAutoState.setStatus("current")


class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):
    """Custom type swL3IpCtrlDhcpv6ClientState based on Integer32"""
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


_SwL3IpCtrlDhcpv6ClientState_Type.__name__ = "Integer32"
_SwL3IpCtrlDhcpv6ClientState_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientState = _SwL3IpCtrlDhcpv6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 3, 1, 20),
    _SwL3IpCtrlDhcpv6ClientState_Type()
)
swL3IpCtrlDhcpv6ClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientState.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")


class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):
    """Custom type swL3Ipv6CtrlNsRetransTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwL3Ipv6CtrlNsRetransTimer_Type.__name__ = "Unsigned32"
_SwL3Ipv6CtrlNsRetransTimer_Object = MibTableColumn
swL3Ipv6CtrlNsRetransTimer = _SwL3Ipv6CtrlNsRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 4, 1, 3),
    _SwL3Ipv6CtrlNsRetransTimer_Type()
)
swL3Ipv6CtrlNsRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlNsRetransTimer.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1, 3),
    _SwL3Ipv6AddressCtrlPrefixLen_Type()
)
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPrefixLen.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 5, 1, 9),
    _SwL3Ipv6AddressCtrlAddressType_Type()
)
swL3Ipv6AddressCtrlAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAddressType.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 2),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_SwL3IpStaticRouteBkupState_Type.__name__ = "Integer32"
_SwL3IpStaticRouteBkupState_Object = MibTableColumn
swL3IpStaticRouteBkupState = _SwL3IpStaticRouteBkupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteBkupState_Type()
)
swL3IpStaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteBkupState.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 4),
    _SwL3IpStaticRouteNextHop_Type()
)
swL3IpStaticRouteNextHop.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 5),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("valid", 3))
    )


_SwL3IpStaticRouteStatus_Type.__name__ = "Integer32"
_SwL3IpStaticRouteStatus_Object = MibTableColumn
swL3IpStaticRouteStatus = _SwL3IpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 2, 5, 1, 6),
    _SwL3IpStaticRouteStatus_Type()
)
swL3IpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteStatus.setStatus("current")
_SwL3RelayMgmt_ObjectIdentity = ObjectIdentity
swL3RelayMgmt = _SwL3RelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3)
)
_SwL3RelayDnsMgmt_ObjectIdentity = ObjectIdentity
swL3RelayDnsMgmt = _SwL3RelayDnsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 1),
    _SwL3RelayDnsState_Type()
)
swL3RelayDnsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsState.setStatus("current")
_SwL3RelayDnsPrimaryServer_Type = IpAddress
_SwL3RelayDnsPrimaryServer_Object = MibScalar
swL3RelayDnsPrimaryServer = _SwL3RelayDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 2),
    _SwL3RelayDnsPrimaryServer_Type()
)
swL3RelayDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsPrimaryServer.setStatus("current")
_SwL3RelayDnsSecondaryServer_Type = IpAddress
_SwL3RelayDnsSecondaryServer_Object = MibScalar
swL3RelayDnsSecondaryServer = _SwL3RelayDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 5),
    _SwL3RelayDnsStaticTableState_Type()
)
swL3RelayDnsStaticTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsStaticTableState.setStatus("current")
_SwL3RelayDnsCtrlTable_Object = MibTable
swL3RelayDnsCtrlTable = _SwL3RelayDnsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlTable.setStatus("current")
_SwL3RelayDnsCtrlEntry_Object = MibTableRow
swL3RelayDnsCtrlEntry = _SwL3RelayDnsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 6, 1)
)
swL3RelayDnsCtrlEntry.setIndexNames(
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3RelayDnsCtrlDomainName"),
    (0, "DGS-3710-12C-L3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 6, 1, 1),
    _SwL3RelayDnsCtrlDomainName_Type()
)
swL3RelayDnsCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlDomainName.setStatus("current")
_SwL3RelayDnsCtrlIpAddr_Type = IpAddress
_SwL3RelayDnsCtrlIpAddr_Object = MibTableColumn
swL3RelayDnsCtrlIpAddr = _SwL3RelayDnsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5, 3, 3, 2, 6, 1, 3),
    _SwL3RelayDnsCtrlState_Type()
)
swL3RelayDnsCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-3710-12C-L3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "Ipv6Address": Ipv6Address,
       "VrId": VrId,
       "swL3MgmtMIB": swL3MgmtMIB,
       "swL3IpMgmt": swL3IpMgmt,
       "swL3IpCtrlMgmt": swL3IpCtrlMgmt,
       "swL3IpCtrlTable": swL3IpCtrlTable,
       "swL3IpCtrlEntry": swL3IpCtrlEntry,
       "swL3IpCtrlInterfaceName": swL3IpCtrlInterfaceName,
       "swL3IpCtrlIfIndex": swL3IpCtrlIfIndex,
       "swL3IpCtrlIpAddr": swL3IpCtrlIpAddr,
       "swL3IpCtrlIpSubnetMask": swL3IpCtrlIpSubnetMask,
       "swL3IpCtrlVlanName": swL3IpCtrlVlanName,
       "swL3IpCtrlMode": swL3IpCtrlMode,
       "swL3IpCtrlAdminState": swL3IpCtrlAdminState,
       "swL3IpCtrlIpv4AdminState": swL3IpCtrlIpv4AdminState,
       "swL3IpCtrlIpv6AdminState": swL3IpCtrlIpv6AdminState,
       "swL3IpCtrlIpv6LinkLocalAddress": swL3IpCtrlIpv6LinkLocalAddress,
       "swL3IpCtrlIpv6LinkLocalPrefixLen": swL3IpCtrlIpv6LinkLocalPrefixLen,
       "swL3IpCtrlState": swL3IpCtrlState,
       "swL3IpCtrlIpv6LinkLocalAutoState": swL3IpCtrlIpv6LinkLocalAutoState,
       "swL3IpCtrlDhcpv6ClientState": swL3IpCtrlDhcpv6ClientState,
       "swL3Ipv6CtrlTable": swL3Ipv6CtrlTable,
       "swL3Ipv6CtrlEntry": swL3Ipv6CtrlEntry,
       "swL3Ipv6CtrlInterfaceName": swL3Ipv6CtrlInterfaceName,
       "swL3Ipv6CtrlNsRetransTimer": swL3Ipv6CtrlNsRetransTimer,
       "swL3Ipv6AddressCtrlTable": swL3Ipv6AddressCtrlTable,
       "swL3Ipv6AddressCtrlEntry": swL3Ipv6AddressCtrlEntry,
       "swL3Ipv6AddressCtrlInterfaceName": swL3Ipv6AddressCtrlInterfaceName,
       "swL3Ipv6Address": swL3Ipv6Address,
       "swL3Ipv6AddressCtrlPrefixLen": swL3Ipv6AddressCtrlPrefixLen,
       "swL3Ipv6AddressCtrlState": swL3Ipv6AddressCtrlState,
       "swL3Ipv6AddressCtrlAddressType": swL3Ipv6AddressCtrlAddressType,
       "swL3IpCtrlAllIpIfState": swL3IpCtrlAllIpIfState,
       "swL3IpStaticRouteTable": swL3IpStaticRouteTable,
       "swL3IpStaticRouteEntry": swL3IpStaticRouteEntry,
       "swL3IpStaticRouteDest": swL3IpStaticRouteDest,
       "swL3IpStaticRouteMask": swL3IpStaticRouteMask,
       "swL3IpStaticRouteBkupState": swL3IpStaticRouteBkupState,
       "swL3IpStaticRouteNextHop": swL3IpStaticRouteNextHop,
       "swL3IpStaticRouteMetric": swL3IpStaticRouteMetric,
       "swL3IpStaticRouteStatus": swL3IpStaticRouteStatus,
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
       "swL3RelayDnsCtrlState": swL3RelayDnsCtrlState}
)
