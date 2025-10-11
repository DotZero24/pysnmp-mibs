# SNMP MIB module (SWITCH-L3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-L3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:56 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

rcL3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16)
)
if mibBuilder.loadTexts:
    rcL3.setRevisions(
        ("1904-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcL3IpSubnet_ObjectIdentity = ObjectIdentity
rcL3IpSubnet = _RcL3IpSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1)
)
_RcL3IpSubnetMaxRows_Type = Unsigned32
_RcL3IpSubnetMaxRows_Object = MibScalar
rcL3IpSubnetMaxRows = _RcL3IpSubnetMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 1),
    _RcL3IpSubnetMaxRows_Type()
)
rcL3IpSubnetMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpSubnetMaxRows.setStatus("current")
_RcL3IpSubnetCurrentRows_Type = Unsigned32
_RcL3IpSubnetCurrentRows_Object = MibScalar
rcL3IpSubnetCurrentRows = _RcL3IpSubnetCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 2),
    _RcL3IpSubnetCurrentRows_Type()
)
rcL3IpSubnetCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpSubnetCurrentRows.setStatus("current")
_RcL3IpSubnetTable_Object = MibTable
rcL3IpSubnetTable = _RcL3IpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    rcL3IpSubnetTable.setStatus("current")
_RcL3IpSubnetEntry_Object = MibTableRow
rcL3IpSubnetEntry = _RcL3IpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1)
)
rcL3IpSubnetEntry.setIndexNames(
    (0, "SWITCH-L3-MIB", "rcL3IpSubnetIfIndex"),
    (0, "SWITCH-L3-MIB", "rcL3IpSubnetIpAddress"),
)
if mibBuilder.loadTexts:
    rcL3IpSubnetEntry.setStatus("current")
_RcL3IpSubnetIfIndex_Type = Integer32
_RcL3IpSubnetIfIndex_Object = MibTableColumn
rcL3IpSubnetIfIndex = _RcL3IpSubnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 1),
    _RcL3IpSubnetIfIndex_Type()
)
rcL3IpSubnetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpSubnetIfIndex.setStatus("current")
_RcL3IpSubnetIpAddress_Type = IpAddress
_RcL3IpSubnetIpAddress_Object = MibTableColumn
rcL3IpSubnetIpAddress = _RcL3IpSubnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 2),
    _RcL3IpSubnetIpAddress_Type()
)
rcL3IpSubnetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpSubnetIpAddress.setStatus("current")
_RcL3IpSubnetMask_Type = IpAddress
_RcL3IpSubnetMask_Object = MibTableColumn
rcL3IpSubnetMask = _RcL3IpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 3),
    _RcL3IpSubnetMask_Type()
)
rcL3IpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetMask.setStatus("current")
_RcL3IpSubnetVlans_Type = Vlanset
_RcL3IpSubnetVlans_Object = MibTableColumn
rcL3IpSubnetVlans = _RcL3IpSubnetVlans_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 4),
    _RcL3IpSubnetVlans_Type()
)
rcL3IpSubnetVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetVlans.setStatus("current")


class _RcL3IpSubnetName_Type(OctetString):
    """Custom type rcL3IpSubnetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcL3IpSubnetName_Type.__name__ = "OctetString"
_RcL3IpSubnetName_Object = MibTableColumn
rcL3IpSubnetName = _RcL3IpSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 5),
    _RcL3IpSubnetName_Type()
)
rcL3IpSubnetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetName.setStatus("current")
_RcL3IpSubnetRowStatus_Type = RowStatus
_RcL3IpSubnetRowStatus_Object = MibTableColumn
rcL3IpSubnetRowStatus = _RcL3IpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 6),
    _RcL3IpSubnetRowStatus_Type()
)
rcL3IpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetRowStatus.setStatus("current")
_RcL3IpSubnetAllowPortList_Type = PortList
_RcL3IpSubnetAllowPortList_Object = MibTableColumn
rcL3IpSubnetAllowPortList = _RcL3IpSubnetAllowPortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 1, 3, 1, 7),
    _RcL3IpSubnetAllowPortList_Type()
)
rcL3IpSubnetAllowPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetAllowPortList.setStatus("current")
_RcL3IpStatic_ObjectIdentity = ObjectIdentity
rcL3IpStatic = _RcL3IpStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2)
)
_RcL3IpStaticMaxHwHosts_Type = Unsigned32
_RcL3IpStaticMaxHwHosts_Object = MibScalar
rcL3IpStaticMaxHwHosts = _RcL3IpStaticMaxHwHosts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 1),
    _RcL3IpStaticMaxHwHosts_Type()
)
rcL3IpStaticMaxHwHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticMaxHwHosts.setStatus("deprecated")


class _RcL3IpStaticNumStaticHwHosts_Type(Unsigned32):
    """Custom type rcL3IpStaticNumStaticHwHosts based on Unsigned32"""
    defaultValue = 1024


_RcL3IpStaticNumStaticHwHosts_Type.__name__ = "Unsigned32"
_RcL3IpStaticNumStaticHwHosts_Object = MibScalar
rcL3IpStaticNumStaticHwHosts = _RcL3IpStaticNumStaticHwHosts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 2),
    _RcL3IpStaticNumStaticHwHosts_Type()
)
rcL3IpStaticNumStaticHwHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticNumStaticHwHosts.setStatus("deprecated")
_RcL3IpStaticMaxHwSubnets_Type = Unsigned32
_RcL3IpStaticMaxHwSubnets_Object = MibScalar
rcL3IpStaticMaxHwSubnets = _RcL3IpStaticMaxHwSubnets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 3),
    _RcL3IpStaticMaxHwSubnets_Type()
)
rcL3IpStaticMaxHwSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticMaxHwSubnets.setStatus("deprecated")
_RcL3IpStaticNumStaticHwSubnets_Type = Unsigned32
_RcL3IpStaticNumStaticHwSubnets_Object = MibScalar
rcL3IpStaticNumStaticHwSubnets = _RcL3IpStaticNumStaticHwSubnets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 4),
    _RcL3IpStaticNumStaticHwSubnets_Type()
)
rcL3IpStaticNumStaticHwSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticNumStaticHwSubnets.setStatus("deprecated")
_RcL3IpStaticRouteMaxRows_Type = Unsigned32
_RcL3IpStaticRouteMaxRows_Object = MibScalar
rcL3IpStaticRouteMaxRows = _RcL3IpStaticRouteMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 5),
    _RcL3IpStaticRouteMaxRows_Type()
)
rcL3IpStaticRouteMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticRouteMaxRows.setStatus("current")
_RcL3IpStaticRouteCurrentRows_Type = Unsigned32
_RcL3IpStaticRouteCurrentRows_Object = MibScalar
rcL3IpStaticRouteCurrentRows = _RcL3IpStaticRouteCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 6),
    _RcL3IpStaticRouteCurrentRows_Type()
)
rcL3IpStaticRouteCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticRouteCurrentRows.setStatus("current")
_RcL3IpStaticRouteTable_Object = MibTable
rcL3IpStaticRouteTable = _RcL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7)
)
if mibBuilder.loadTexts:
    rcL3IpStaticRouteTable.setStatus("deprecated")
_RcL3IpStaticRouteEntry_Object = MibTableRow
rcL3IpStaticRouteEntry = _RcL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1)
)
rcL3IpStaticRouteEntry.setIndexNames(
    (0, "SWITCH-L3-MIB", "rcL3IpStaticDestIpAddress"),
)
if mibBuilder.loadTexts:
    rcL3IpStaticRouteEntry.setStatus("current")
_RcL3IpStaticDestIpAddress_Type = IpAddress
_RcL3IpStaticDestIpAddress_Object = MibTableColumn
rcL3IpStaticDestIpAddress = _RcL3IpStaticDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 1),
    _RcL3IpStaticDestIpAddress_Type()
)
rcL3IpStaticDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpStaticDestIpAddress.setStatus("current")
_RcL3IpStaticMask_Type = IpAddress
_RcL3IpStaticMask_Object = MibTableColumn
rcL3IpStaticMask = _RcL3IpStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 2),
    _RcL3IpStaticMask_Type()
)
rcL3IpStaticMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpStaticMask.setStatus("current")
_RcL3IpStaticNextHop_Type = IpAddress
_RcL3IpStaticNextHop_Object = MibTableColumn
rcL3IpStaticNextHop = _RcL3IpStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 3),
    _RcL3IpStaticNextHop_Type()
)
rcL3IpStaticNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpStaticNextHop.setStatus("current")


class _RcL3IpStaticName_Type(OctetString):
    """Custom type rcL3IpStaticName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RcL3IpStaticName_Type.__name__ = "OctetString"
_RcL3IpStaticName_Object = MibTableColumn
rcL3IpStaticName = _RcL3IpStaticName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 4),
    _RcL3IpStaticName_Type()
)
rcL3IpStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpStaticName.setStatus("obsolete")


class _RcL3IpStaticUseHw_Type(TruthValue):
    """Custom type rcL3IpStaticUseHw based on TruthValue"""
    defaultValue = 2


_RcL3IpStaticUseHw_Type.__name__ = "TruthValue"
_RcL3IpStaticUseHw_Object = MibTableColumn
rcL3IpStaticUseHw = _RcL3IpStaticUseHw_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 5),
    _RcL3IpStaticUseHw_Type()
)
rcL3IpStaticUseHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpStaticUseHw.setStatus("obsolete")
_RcL3IpStaticInHw_Type = TruthValue
_RcL3IpStaticInHw_Object = MibTableColumn
rcL3IpStaticInHw = _RcL3IpStaticInHw_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 6),
    _RcL3IpStaticInHw_Type()
)
rcL3IpStaticInHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticInHw.setStatus("current")


class _RcL3IpStaticGateway_Type(TruthValue):
    """Custom type rcL3IpStaticGateway based on TruthValue"""
    defaultValue = 2


_RcL3IpStaticGateway_Type.__name__ = "TruthValue"
_RcL3IpStaticGateway_Object = MibTableColumn
rcL3IpStaticGateway = _RcL3IpStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 7),
    _RcL3IpStaticGateway_Type()
)
rcL3IpStaticGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpStaticGateway.setStatus("current")
_RcL3IpStaticRowStatus_Type = RowStatus
_RcL3IpStaticRowStatus_Object = MibTableColumn
rcL3IpStaticRowStatus = _RcL3IpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 7, 1, 8),
    _RcL3IpStaticRowStatus_Type()
)
rcL3IpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpStaticRowStatus.setStatus("current")
_RaisecomIpv6RMDefaultGateway_Type = InetAddress
_RaisecomIpv6RMDefaultGateway_Object = MibScalar
raisecomIpv6RMDefaultGateway = _RaisecomIpv6RMDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 8),
    _RaisecomIpv6RMDefaultGateway_Type()
)
raisecomIpv6RMDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpv6RMDefaultGateway.setStatus("deprecated")
_RcL3StaticRouteTable_Object = MibTable
rcL3StaticRouteTable = _RcL3StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9)
)
if mibBuilder.loadTexts:
    rcL3StaticRouteTable.setStatus("current")
_RcL3StaticRouteEntry_Object = MibTableRow
rcL3StaticRouteEntry = _RcL3StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1)
)
rcL3StaticRouteEntry.setIndexNames(
    (0, "SWITCH-L3-MIB", "rcL3StaticRouteType"),
    (0, "SWITCH-L3-MIB", "rcL3StaticDestAddress"),
    (0, "SWITCH-L3-MIB", "rcL3StaticPrefixLen"),
    (0, "SWITCH-L3-MIB", "rcL3StaticNextHop"),
)
if mibBuilder.loadTexts:
    rcL3StaticRouteEntry.setStatus("current")


class _RcL3StaticRouteType_Type(Integer32):
    """Custom type rcL3StaticRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RcL3StaticRouteType_Type.__name__ = "Integer32"
_RcL3StaticRouteType_Object = MibTableColumn
rcL3StaticRouteType = _RcL3StaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 1),
    _RcL3StaticRouteType_Type()
)
rcL3StaticRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3StaticRouteType.setStatus("current")
_RcL3StaticDestAddress_Type = InetAddress
_RcL3StaticDestAddress_Object = MibTableColumn
rcL3StaticDestAddress = _RcL3StaticDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 2),
    _RcL3StaticDestAddress_Type()
)
rcL3StaticDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3StaticDestAddress.setStatus("current")
_RcL3StaticPrefixLen_Type = Unsigned32
_RcL3StaticPrefixLen_Object = MibTableColumn
rcL3StaticPrefixLen = _RcL3StaticPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 3),
    _RcL3StaticPrefixLen_Type()
)
rcL3StaticPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3StaticPrefixLen.setStatus("current")
_RcL3StaticNextHop_Type = InetAddress
_RcL3StaticNextHop_Object = MibTableColumn
rcL3StaticNextHop = _RcL3StaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 4),
    _RcL3StaticNextHop_Type()
)
rcL3StaticNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3StaticNextHop.setStatus("current")


class _RcL3StaticGateway_Type(TruthValue):
    """Custom type rcL3StaticGateway based on TruthValue"""
    defaultValue = 2


_RcL3StaticGateway_Type.__name__ = "TruthValue"
_RcL3StaticGateway_Object = MibTableColumn
rcL3StaticGateway = _RcL3StaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 5),
    _RcL3StaticGateway_Type()
)
rcL3StaticGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3StaticGateway.setStatus("current")
_RcL3StaticDistance_Type = Unsigned32
_RcL3StaticDistance_Object = MibTableColumn
rcL3StaticDistance = _RcL3StaticDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 6),
    _RcL3StaticDistance_Type()
)
rcL3StaticDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3StaticDistance.setStatus("current")
_RcL3StaticRowStatus_Type = RowStatus
_RcL3StaticRowStatus_Object = MibTableColumn
rcL3StaticRowStatus = _RcL3StaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 9, 1, 7),
    _RcL3StaticRowStatus_Type()
)
rcL3StaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3StaticRowStatus.setStatus("current")


class _RcL3IpStaticEcmpPathSelectMode_Type(Integer32):
    """Custom type rcL3IpStaticEcmpPathSelectMode based on Integer32"""
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
        *(("other", 0),
          ("SIP", 1),
          ("DIP", 2),
          ("L4Port", 3),
          ("DIPxorL4Port", 4))
    )


_RcL3IpStaticEcmpPathSelectMode_Type.__name__ = "Integer32"
_RcL3IpStaticEcmpPathSelectMode_Object = MibScalar
rcL3IpStaticEcmpPathSelectMode = _RcL3IpStaticEcmpPathSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 2, 10),
    _RcL3IpStaticEcmpPathSelectMode_Type()
)
rcL3IpStaticEcmpPathSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL3IpStaticEcmpPathSelectMode.setStatus("current")
_RcL3IpRoute_ObjectIdentity = ObjectIdentity
rcL3IpRoute = _RcL3IpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3)
)
_RcL3IpRouteTable_Object = MibTable
rcL3IpRouteTable = _RcL3IpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    rcL3IpRouteTable.setStatus("current")
_RcL3IpRouteEntry_Object = MibTableRow
rcL3IpRouteEntry = _RcL3IpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1)
)
rcL3IpRouteEntry.setIndexNames(
    (0, "SWITCH-L3-MIB", "rcL3IpRouteDest"),
)
if mibBuilder.loadTexts:
    rcL3IpRouteEntry.setStatus("current")
_RcL3IpRouteDest_Type = IpAddress
_RcL3IpRouteDest_Object = MibTableColumn
rcL3IpRouteDest = _RcL3IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 1),
    _RcL3IpRouteDest_Type()
)
rcL3IpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpRouteDest.setStatus("current")
_RcL3IpRouteMask_Type = IpAddress
_RcL3IpRouteMask_Object = MibTableColumn
rcL3IpRouteMask = _RcL3IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 2),
    _RcL3IpRouteMask_Type()
)
rcL3IpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpRouteMask.setStatus("current")
_RcL3IpRouteNextHopIp_Type = IpAddress
_RcL3IpRouteNextHopIp_Object = MibTableColumn
rcL3IpRouteNextHopIp = _RcL3IpRouteNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 3),
    _RcL3IpRouteNextHopIp_Type()
)
rcL3IpRouteNextHopIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpRouteNextHopIp.setStatus("current")
_RcL3IpRouteNextHopMac_Type = MacAddress
_RcL3IpRouteNextHopMac_Object = MibTableColumn
rcL3IpRouteNextHopMac = _RcL3IpRouteNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 4),
    _RcL3IpRouteNextHopMac_Type()
)
rcL3IpRouteNextHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteNextHopMac.setStatus("current")
_RcL3IpRouteIfIndex_Type = Integer32
_RcL3IpRouteIfIndex_Object = MibTableColumn
rcL3IpRouteIfIndex = _RcL3IpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 5),
    _RcL3IpRouteIfIndex_Type()
)
rcL3IpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteIfIndex.setStatus("current")


class _RcL3IpRouteType_Type(Integer32):
    """Custom type rcL3IpRouteType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_RcL3IpRouteType_Type.__name__ = "Integer32"
_RcL3IpRouteType_Object = MibTableColumn
rcL3IpRouteType = _RcL3IpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 6),
    _RcL3IpRouteType_Type()
)
rcL3IpRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpRouteType.setStatus("current")


class _RcL3IpRouteProto_Type(Integer32):
    """Custom type rcL3IpRouteProto based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("is-is", 9),
          ("es-is", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_RcL3IpRouteProto_Type.__name__ = "Integer32"
_RcL3IpRouteProto_Object = MibTableColumn
rcL3IpRouteProto = _RcL3IpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 7),
    _RcL3IpRouteProto_Type()
)
rcL3IpRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteProto.setStatus("current")
_RcL3IpRouteAge_Type = Unsigned32
_RcL3IpRouteAge_Object = MibTableColumn
rcL3IpRouteAge = _RcL3IpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 8),
    _RcL3IpRouteAge_Type()
)
rcL3IpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteAge.setStatus("current")
_RcL3IpRouteMetric1_Type = Integer32
_RcL3IpRouteMetric1_Object = MibTableColumn
rcL3IpRouteMetric1 = _RcL3IpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 9),
    _RcL3IpRouteMetric1_Type()
)
rcL3IpRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteMetric1.setStatus("current")
_RcL3IpRouteUsingHw_Type = TruthValue
_RcL3IpRouteUsingHw_Object = MibTableColumn
rcL3IpRouteUsingHw = _RcL3IpRouteUsingHw_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 10),
    _RcL3IpRouteUsingHw_Type()
)
rcL3IpRouteUsingHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteUsingHw.setStatus("current")
_RcL3IpRouteIsStatic_Type = TruthValue
_RcL3IpRouteIsStatic_Object = MibTableColumn
rcL3IpRouteIsStatic = _RcL3IpRouteIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 11),
    _RcL3IpRouteIsStatic_Type()
)
rcL3IpRouteIsStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteIsStatic.setStatus("current")
_RcL3IpRouteFlags_Type = Unsigned32
_RcL3IpRouteFlags_Object = MibTableColumn
rcL3IpRouteFlags = _RcL3IpRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 12),
    _RcL3IpRouteFlags_Type()
)
rcL3IpRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteFlags.setStatus("current")
_RcL3IpRouteRef_Type = Gauge32
_RcL3IpRouteRef_Object = MibTableColumn
rcL3IpRouteRef = _RcL3IpRouteRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 13),
    _RcL3IpRouteRef_Type()
)
rcL3IpRouteRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteRef.setStatus("current")
_RcL3IpRouteUse_Type = Counter32
_RcL3IpRouteUse_Object = MibTableColumn
rcL3IpRouteUse = _RcL3IpRouteUse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 14),
    _RcL3IpRouteUse_Type()
)
rcL3IpRouteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL3IpRouteUse.setStatus("current")
_RcL3IpRouteRowStatus_Type = RowStatus
_RcL3IpRouteRowStatus_Object = MibTableColumn
rcL3IpRouteRowStatus = _RcL3IpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 3, 1, 1, 15),
    _RcL3IpRouteRowStatus_Type()
)
rcL3IpRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-L3-MIB",
    **{"rcL3": rcL3,
       "rcL3IpSubnet": rcL3IpSubnet,
       "rcL3IpSubnetMaxRows": rcL3IpSubnetMaxRows,
       "rcL3IpSubnetCurrentRows": rcL3IpSubnetCurrentRows,
       "rcL3IpSubnetTable": rcL3IpSubnetTable,
       "rcL3IpSubnetEntry": rcL3IpSubnetEntry,
       "rcL3IpSubnetIfIndex": rcL3IpSubnetIfIndex,
       "rcL3IpSubnetIpAddress": rcL3IpSubnetIpAddress,
       "rcL3IpSubnetMask": rcL3IpSubnetMask,
       "rcL3IpSubnetVlans": rcL3IpSubnetVlans,
       "rcL3IpSubnetName": rcL3IpSubnetName,
       "rcL3IpSubnetRowStatus": rcL3IpSubnetRowStatus,
       "rcL3IpSubnetAllowPortList": rcL3IpSubnetAllowPortList,
       "rcL3IpStatic": rcL3IpStatic,
       "rcL3IpStaticMaxHwHosts": rcL3IpStaticMaxHwHosts,
       "rcL3IpStaticNumStaticHwHosts": rcL3IpStaticNumStaticHwHosts,
       "rcL3IpStaticMaxHwSubnets": rcL3IpStaticMaxHwSubnets,
       "rcL3IpStaticNumStaticHwSubnets": rcL3IpStaticNumStaticHwSubnets,
       "rcL3IpStaticRouteMaxRows": rcL3IpStaticRouteMaxRows,
       "rcL3IpStaticRouteCurrentRows": rcL3IpStaticRouteCurrentRows,
       "rcL3IpStaticRouteTable": rcL3IpStaticRouteTable,
       "rcL3IpStaticRouteEntry": rcL3IpStaticRouteEntry,
       "rcL3IpStaticDestIpAddress": rcL3IpStaticDestIpAddress,
       "rcL3IpStaticMask": rcL3IpStaticMask,
       "rcL3IpStaticNextHop": rcL3IpStaticNextHop,
       "rcL3IpStaticName": rcL3IpStaticName,
       "rcL3IpStaticUseHw": rcL3IpStaticUseHw,
       "rcL3IpStaticInHw": rcL3IpStaticInHw,
       "rcL3IpStaticGateway": rcL3IpStaticGateway,
       "rcL3IpStaticRowStatus": rcL3IpStaticRowStatus,
       "raisecomIpv6RMDefaultGateway": raisecomIpv6RMDefaultGateway,
       "rcL3StaticRouteTable": rcL3StaticRouteTable,
       "rcL3StaticRouteEntry": rcL3StaticRouteEntry,
       "rcL3StaticRouteType": rcL3StaticRouteType,
       "rcL3StaticDestAddress": rcL3StaticDestAddress,
       "rcL3StaticPrefixLen": rcL3StaticPrefixLen,
       "rcL3StaticNextHop": rcL3StaticNextHop,
       "rcL3StaticGateway": rcL3StaticGateway,
       "rcL3StaticDistance": rcL3StaticDistance,
       "rcL3StaticRowStatus": rcL3StaticRowStatus,
       "rcL3IpStaticEcmpPathSelectMode": rcL3IpStaticEcmpPathSelectMode,
       "rcL3IpRoute": rcL3IpRoute,
       "rcL3IpRouteTable": rcL3IpRouteTable,
       "rcL3IpRouteEntry": rcL3IpRouteEntry,
       "rcL3IpRouteDest": rcL3IpRouteDest,
       "rcL3IpRouteMask": rcL3IpRouteMask,
       "rcL3IpRouteNextHopIp": rcL3IpRouteNextHopIp,
       "rcL3IpRouteNextHopMac": rcL3IpRouteNextHopMac,
       "rcL3IpRouteIfIndex": rcL3IpRouteIfIndex,
       "rcL3IpRouteType": rcL3IpRouteType,
       "rcL3IpRouteProto": rcL3IpRouteProto,
       "rcL3IpRouteAge": rcL3IpRouteAge,
       "rcL3IpRouteMetric1": rcL3IpRouteMetric1,
       "rcL3IpRouteUsingHw": rcL3IpRouteUsingHw,
       "rcL3IpRouteIsStatic": rcL3IpRouteIsStatic,
       "rcL3IpRouteFlags": rcL3IpRouteFlags,
       "rcL3IpRouteRef": rcL3IpRouteRef,
       "rcL3IpRouteUse": rcL3IpRouteUse,
       "rcL3IpRouteRowStatus": rcL3IpRouteRowStatus}
)
