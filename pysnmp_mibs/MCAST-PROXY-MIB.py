# SNMP MIB module (MCAST-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/MCAST-PROXY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:41 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swMcastProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwMcastProxyCtrl_ObjectIdentity = ObjectIdentity
swMcastProxyCtrl = _SwMcastProxyCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 1)
)


class _SwIGMPProxyGlobalState_Type(Integer32):
    """Custom type swIGMPProxyGlobalState based on Integer32"""
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


_SwIGMPProxyGlobalState_Type.__name__ = "Integer32"
_SwIGMPProxyGlobalState_Object = MibScalar
swIGMPProxyGlobalState = _SwIGMPProxyGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 1, 1),
    _SwIGMPProxyGlobalState_Type()
)
swIGMPProxyGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPProxyGlobalState.setStatus("current")


class _SwMLDProxyGlobalState_Type(Integer32):
    """Custom type swMLDProxyGlobalState based on Integer32"""
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


_SwMLDProxyGlobalState_Type.__name__ = "Integer32"
_SwMLDProxyGlobalState_Object = MibScalar
swMLDProxyGlobalState = _SwMLDProxyGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 1, 2),
    _SwMLDProxyGlobalState_Type()
)
swMLDProxyGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMLDProxyGlobalState.setStatus("current")
_SwMcastProxyInfo_ObjectIdentity = ObjectIdentity
swMcastProxyInfo = _SwMcastProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2)
)
_SwIGMPProxyInfo_ObjectIdentity = ObjectIdentity
swIGMPProxyInfo = _SwIGMPProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1)
)
_SwIGMPProxyGroupTable_Object = MibTable
swIGMPProxyGroupTable = _SwIGMPProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swIGMPProxyGroupTable.setStatus("current")
_SwIGMPProxyGroupEntry_Object = MibTableRow
swIGMPProxyGroupEntry = _SwIGMPProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1)
)
swIGMPProxyGroupEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swIGMPProxyGroupDesAddr"),
    (0, "MCAST-PROXY-MIB", "swIGMPProxyGroupSrcAddr"),
    (0, "MCAST-PROXY-MIB", "swIGMPProxyDownstreamVlanID"),
)
if mibBuilder.loadTexts:
    swIGMPProxyGroupEntry.setStatus("current")
_SwIGMPProxyGroupDesAddr_Type = IpAddress
_SwIGMPProxyGroupDesAddr_Object = MibTableColumn
swIGMPProxyGroupDesAddr = _SwIGMPProxyGroupDesAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1, 1),
    _SwIGMPProxyGroupDesAddr_Type()
)
swIGMPProxyGroupDesAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIGMPProxyGroupDesAddr.setStatus("current")
_SwIGMPProxyGroupSrcAddr_Type = IpAddress
_SwIGMPProxyGroupSrcAddr_Object = MibTableColumn
swIGMPProxyGroupSrcAddr = _SwIGMPProxyGroupSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1, 2),
    _SwIGMPProxyGroupSrcAddr_Type()
)
swIGMPProxyGroupSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIGMPProxyGroupSrcAddr.setStatus("current")
_SwIGMPProxyDownstreamVlanID_Type = VlanId
_SwIGMPProxyDownstreamVlanID_Object = MibTableColumn
swIGMPProxyDownstreamVlanID = _SwIGMPProxyDownstreamVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1, 3),
    _SwIGMPProxyDownstreamVlanID_Type()
)
swIGMPProxyDownstreamVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIGMPProxyDownstreamVlanID.setStatus("current")
_SwIGMPProxyDownstreamVlanMemberPorts_Type = PortList
_SwIGMPProxyDownstreamVlanMemberPorts_Object = MibTableColumn
swIGMPProxyDownstreamVlanMemberPorts = _SwIGMPProxyDownstreamVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1, 4),
    _SwIGMPProxyDownstreamVlanMemberPorts_Type()
)
swIGMPProxyDownstreamVlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPProxyDownstreamVlanMemberPorts.setStatus("current")


class _SwIGMPProxyGroupStatus_Type(Integer32):
    """Custom type swIGMPProxyGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwIGMPProxyGroupStatus_Type.__name__ = "Integer32"
_SwIGMPProxyGroupStatus_Object = MibTableColumn
swIGMPProxyGroupStatus = _SwIGMPProxyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 1, 1, 1, 5),
    _SwIGMPProxyGroupStatus_Type()
)
swIGMPProxyGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPProxyGroupStatus.setStatus("current")
_SwMLDProxyInfo_ObjectIdentity = ObjectIdentity
swMLDProxyInfo = _SwMLDProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2)
)
_SwMLDProxyGroupTable_Object = MibTable
swMLDProxyGroupTable = _SwMLDProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swMLDProxyGroupTable.setStatus("current")
_SwMLDProxyGroupEntry_Object = MibTableRow
swMLDProxyGroupEntry = _SwMLDProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1)
)
swMLDProxyGroupEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swMLDProxyGroupDesAddr"),
    (0, "MCAST-PROXY-MIB", "swMLDProxyGroupSrcAddr"),
    (0, "MCAST-PROXY-MIB", "swMLDProxyDownstreamVlanID"),
)
if mibBuilder.loadTexts:
    swMLDProxyGroupEntry.setStatus("current")
_SwMLDProxyGroupDesAddr_Type = Ipv6Address
_SwMLDProxyGroupDesAddr_Object = MibTableColumn
swMLDProxyGroupDesAddr = _SwMLDProxyGroupDesAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1, 1),
    _SwMLDProxyGroupDesAddr_Type()
)
swMLDProxyGroupDesAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMLDProxyGroupDesAddr.setStatus("current")
_SwMLDProxyGroupSrcAddr_Type = Ipv6Address
_SwMLDProxyGroupSrcAddr_Object = MibTableColumn
swMLDProxyGroupSrcAddr = _SwMLDProxyGroupSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1, 2),
    _SwMLDProxyGroupSrcAddr_Type()
)
swMLDProxyGroupSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMLDProxyGroupSrcAddr.setStatus("current")
_SwMLDProxyDownstreamVlanID_Type = VlanId
_SwMLDProxyDownstreamVlanID_Object = MibTableColumn
swMLDProxyDownstreamVlanID = _SwMLDProxyDownstreamVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1, 3),
    _SwMLDProxyDownstreamVlanID_Type()
)
swMLDProxyDownstreamVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMLDProxyDownstreamVlanID.setStatus("current")
_SwMLDProxyDownstreamVlanMemberPorts_Type = PortList
_SwMLDProxyDownstreamVlanMemberPorts_Object = MibTableColumn
swMLDProxyDownstreamVlanMemberPorts = _SwMLDProxyDownstreamVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1, 4),
    _SwMLDProxyDownstreamVlanMemberPorts_Type()
)
swMLDProxyDownstreamVlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDProxyDownstreamVlanMemberPorts.setStatus("current")


class _SwMLDProxyGroupStatus_Type(Integer32):
    """Custom type swMLDProxyGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwMLDProxyGroupStatus_Type.__name__ = "Integer32"
_SwMLDProxyGroupStatus_Object = MibTableColumn
swMLDProxyGroupStatus = _SwMLDProxyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 2, 2, 1, 1, 5),
    _SwMLDProxyGroupStatus_Type()
)
swMLDProxyGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDProxyGroupStatus.setStatus("current")
_SwMcastProxyMgmt_ObjectIdentity = ObjectIdentity
swMcastProxyMgmt = _SwMcastProxyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3)
)
_SwIGMPProxyMgmt_ObjectIdentity = ObjectIdentity
swIGMPProxyMgmt = _SwIGMPProxyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1)
)
_SwIGMPProxyUpstreamInterfaceTable_Object = MibTable
swIGMPProxyUpstreamInterfaceTable = _SwIGMPProxyUpstreamInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1)
)
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamInterfaceTable.setStatus("current")
_SwIGMPProxyUpstreamInterfaceEntry_Object = MibTableRow
swIGMPProxyUpstreamInterfaceEntry = _SwIGMPProxyUpstreamInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1)
)
swIGMPProxyUpstreamInterfaceEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swIGMPProxyUpstreamIndex"),
)
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamInterfaceEntry.setStatus("current")
_SwIGMPProxyUpstreamIndex_Type = Integer32
_SwIGMPProxyUpstreamIndex_Object = MibTableColumn
swIGMPProxyUpstreamIndex = _SwIGMPProxyUpstreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 1),
    _SwIGMPProxyUpstreamIndex_Type()
)
swIGMPProxyUpstreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamIndex.setStatus("current")
_SwIGMPProxyUpstreamVlanID_Type = VlanId
_SwIGMPProxyUpstreamVlanID_Object = MibTableColumn
swIGMPProxyUpstreamVlanID = _SwIGMPProxyUpstreamVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 2),
    _SwIGMPProxyUpstreamVlanID_Type()
)
swIGMPProxyUpstreamVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamVlanID.setStatus("current")
_SwIGMPProxyUpstreamDynamicRouterPorts_Type = PortList
_SwIGMPProxyUpstreamDynamicRouterPorts_Object = MibTableColumn
swIGMPProxyUpstreamDynamicRouterPorts = _SwIGMPProxyUpstreamDynamicRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 3),
    _SwIGMPProxyUpstreamDynamicRouterPorts_Type()
)
swIGMPProxyUpstreamDynamicRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamDynamicRouterPorts.setStatus("current")
_SwIGMPProxyUpstreamStaticRouterPorts_Type = PortList
_SwIGMPProxyUpstreamStaticRouterPorts_Object = MibTableColumn
swIGMPProxyUpstreamStaticRouterPorts = _SwIGMPProxyUpstreamStaticRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 4),
    _SwIGMPProxyUpstreamStaticRouterPorts_Type()
)
swIGMPProxyUpstreamStaticRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamStaticRouterPorts.setStatus("current")


class _SwIGMPProxyUpstreamUnsolicitedReportInterval_Type(Integer32):
    """Custom type swIGMPProxyUpstreamUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_SwIGMPProxyUpstreamUnsolicitedReportInterval_Type.__name__ = "Integer32"
_SwIGMPProxyUpstreamUnsolicitedReportInterval_Object = MibTableColumn
swIGMPProxyUpstreamUnsolicitedReportInterval = _SwIGMPProxyUpstreamUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 5),
    _SwIGMPProxyUpstreamUnsolicitedReportInterval_Type()
)
swIGMPProxyUpstreamUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamUnsolicitedReportInterval.setStatus("current")
_SwIGMPProxyUpstreamSourceIP_Type = IpAddress
_SwIGMPProxyUpstreamSourceIP_Object = MibTableColumn
swIGMPProxyUpstreamSourceIP = _SwIGMPProxyUpstreamSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 1, 1, 6),
    _SwIGMPProxyUpstreamSourceIP_Type()
)
swIGMPProxyUpstreamSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPProxyUpstreamSourceIP.setStatus("current")
_SwIGMPProxyDownstreamInterfaceTable_Object = MibTable
swIGMPProxyDownstreamInterfaceTable = _SwIGMPProxyDownstreamInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 2)
)
if mibBuilder.loadTexts:
    swIGMPProxyDownstreamInterfaceTable.setStatus("current")
_SwIGMPProxyDownstreamInterfaceEntry_Object = MibTableRow
swIGMPProxyDownstreamInterfaceEntry = _SwIGMPProxyDownstreamInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 2, 1)
)
swIGMPProxyDownstreamInterfaceEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swIGMPProxyDownstreamVlanID"),
)
if mibBuilder.loadTexts:
    swIGMPProxyDownstreamInterfaceEntry.setStatus("current")
_SwIGMPProxyDownstreamRowStatus_Type = RowStatus
_SwIGMPProxyDownstreamRowStatus_Object = MibTableColumn
swIGMPProxyDownstreamRowStatus = _SwIGMPProxyDownstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 1, 2, 1, 1),
    _SwIGMPProxyDownstreamRowStatus_Type()
)
swIGMPProxyDownstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPProxyDownstreamRowStatus.setStatus("current")
_SwMLDProxyMgmt_ObjectIdentity = ObjectIdentity
swMLDProxyMgmt = _SwMLDProxyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2)
)
_SwMLDProxyUpstreamInterfaceTable_Object = MibTable
swMLDProxyUpstreamInterfaceTable = _SwMLDProxyUpstreamInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1)
)
if mibBuilder.loadTexts:
    swMLDProxyUpstreamInterfaceTable.setStatus("current")
_SwMLDProxyUpstreamInterfaceEntry_Object = MibTableRow
swMLDProxyUpstreamInterfaceEntry = _SwMLDProxyUpstreamInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1)
)
swMLDProxyUpstreamInterfaceEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swMLDProxyUpstreamIndex"),
)
if mibBuilder.loadTexts:
    swMLDProxyUpstreamInterfaceEntry.setStatus("current")
_SwMLDProxyUpstreamIndex_Type = Integer32
_SwMLDProxyUpstreamIndex_Object = MibTableColumn
swMLDProxyUpstreamIndex = _SwMLDProxyUpstreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 1),
    _SwMLDProxyUpstreamIndex_Type()
)
swMLDProxyUpstreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamIndex.setStatus("current")
_SwMLDProxyUpstreamVlanID_Type = VlanId
_SwMLDProxyUpstreamVlanID_Object = MibTableColumn
swMLDProxyUpstreamVlanID = _SwMLDProxyUpstreamVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 2),
    _SwMLDProxyUpstreamVlanID_Type()
)
swMLDProxyUpstreamVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamVlanID.setStatus("current")
_SwMLDProxyUpstreamDynamicRouterPorts_Type = PortList
_SwMLDProxyUpstreamDynamicRouterPorts_Object = MibTableColumn
swMLDProxyUpstreamDynamicRouterPorts = _SwMLDProxyUpstreamDynamicRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 3),
    _SwMLDProxyUpstreamDynamicRouterPorts_Type()
)
swMLDProxyUpstreamDynamicRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamDynamicRouterPorts.setStatus("current")
_SwMLDProxyUpstreamStaticRouterPorts_Type = PortList
_SwMLDProxyUpstreamStaticRouterPorts_Object = MibTableColumn
swMLDProxyUpstreamStaticRouterPorts = _SwMLDProxyUpstreamStaticRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 4),
    _SwMLDProxyUpstreamStaticRouterPorts_Type()
)
swMLDProxyUpstreamStaticRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamStaticRouterPorts.setStatus("current")


class _SwMLDProxyUpstreamUnsolicitedReportInterval_Type(Integer32):
    """Custom type swMLDProxyUpstreamUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_SwMLDProxyUpstreamUnsolicitedReportInterval_Type.__name__ = "Integer32"
_SwMLDProxyUpstreamUnsolicitedReportInterval_Object = MibTableColumn
swMLDProxyUpstreamUnsolicitedReportInterval = _SwMLDProxyUpstreamUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 5),
    _SwMLDProxyUpstreamUnsolicitedReportInterval_Type()
)
swMLDProxyUpstreamUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamUnsolicitedReportInterval.setStatus("current")
_SwMLDProxyUpstreamSourceIP_Type = Ipv6Address
_SwMLDProxyUpstreamSourceIP_Object = MibTableColumn
swMLDProxyUpstreamSourceIP = _SwMLDProxyUpstreamSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 1, 1, 6),
    _SwMLDProxyUpstreamSourceIP_Type()
)
swMLDProxyUpstreamSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMLDProxyUpstreamSourceIP.setStatus("current")
_SwMLDProxyDownstreamInterfaceTable_Object = MibTable
swMLDProxyDownstreamInterfaceTable = _SwMLDProxyDownstreamInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 2)
)
if mibBuilder.loadTexts:
    swMLDProxyDownstreamInterfaceTable.setStatus("current")
_SwMLDProxyDownstreamInterfaceEntry_Object = MibTableRow
swMLDProxyDownstreamInterfaceEntry = _SwMLDProxyDownstreamInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 2, 1)
)
swMLDProxyDownstreamInterfaceEntry.setIndexNames(
    (0, "MCAST-PROXY-MIB", "swMLDProxyDownstreamVlanID"),
)
if mibBuilder.loadTexts:
    swMLDProxyDownstreamInterfaceEntry.setStatus("current")
_SwMLDProxyDownstreamRowStatus_Type = RowStatus
_SwMLDProxyDownstreamRowStatus_Object = MibTableColumn
swMLDProxyDownstreamRowStatus = _SwMLDProxyDownstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 80, 3, 2, 2, 1, 1),
    _SwMLDProxyDownstreamRowStatus_Type()
)
swMLDProxyDownstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMLDProxyDownstreamRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAST-PROXY-MIB",
    **{"swMcastProxyMIB": swMcastProxyMIB,
       "swMcastProxyCtrl": swMcastProxyCtrl,
       "swIGMPProxyGlobalState": swIGMPProxyGlobalState,
       "swMLDProxyGlobalState": swMLDProxyGlobalState,
       "swMcastProxyInfo": swMcastProxyInfo,
       "swIGMPProxyInfo": swIGMPProxyInfo,
       "swIGMPProxyGroupTable": swIGMPProxyGroupTable,
       "swIGMPProxyGroupEntry": swIGMPProxyGroupEntry,
       "swIGMPProxyGroupDesAddr": swIGMPProxyGroupDesAddr,
       "swIGMPProxyGroupSrcAddr": swIGMPProxyGroupSrcAddr,
       "swIGMPProxyDownstreamVlanID": swIGMPProxyDownstreamVlanID,
       "swIGMPProxyDownstreamVlanMemberPorts": swIGMPProxyDownstreamVlanMemberPorts,
       "swIGMPProxyGroupStatus": swIGMPProxyGroupStatus,
       "swMLDProxyInfo": swMLDProxyInfo,
       "swMLDProxyGroupTable": swMLDProxyGroupTable,
       "swMLDProxyGroupEntry": swMLDProxyGroupEntry,
       "swMLDProxyGroupDesAddr": swMLDProxyGroupDesAddr,
       "swMLDProxyGroupSrcAddr": swMLDProxyGroupSrcAddr,
       "swMLDProxyDownstreamVlanID": swMLDProxyDownstreamVlanID,
       "swMLDProxyDownstreamVlanMemberPorts": swMLDProxyDownstreamVlanMemberPorts,
       "swMLDProxyGroupStatus": swMLDProxyGroupStatus,
       "swMcastProxyMgmt": swMcastProxyMgmt,
       "swIGMPProxyMgmt": swIGMPProxyMgmt,
       "swIGMPProxyUpstreamInterfaceTable": swIGMPProxyUpstreamInterfaceTable,
       "swIGMPProxyUpstreamInterfaceEntry": swIGMPProxyUpstreamInterfaceEntry,
       "swIGMPProxyUpstreamIndex": swIGMPProxyUpstreamIndex,
       "swIGMPProxyUpstreamVlanID": swIGMPProxyUpstreamVlanID,
       "swIGMPProxyUpstreamDynamicRouterPorts": swIGMPProxyUpstreamDynamicRouterPorts,
       "swIGMPProxyUpstreamStaticRouterPorts": swIGMPProxyUpstreamStaticRouterPorts,
       "swIGMPProxyUpstreamUnsolicitedReportInterval": swIGMPProxyUpstreamUnsolicitedReportInterval,
       "swIGMPProxyUpstreamSourceIP": swIGMPProxyUpstreamSourceIP,
       "swIGMPProxyDownstreamInterfaceTable": swIGMPProxyDownstreamInterfaceTable,
       "swIGMPProxyDownstreamInterfaceEntry": swIGMPProxyDownstreamInterfaceEntry,
       "swIGMPProxyDownstreamRowStatus": swIGMPProxyDownstreamRowStatus,
       "swMLDProxyMgmt": swMLDProxyMgmt,
       "swMLDProxyUpstreamInterfaceTable": swMLDProxyUpstreamInterfaceTable,
       "swMLDProxyUpstreamInterfaceEntry": swMLDProxyUpstreamInterfaceEntry,
       "swMLDProxyUpstreamIndex": swMLDProxyUpstreamIndex,
       "swMLDProxyUpstreamVlanID": swMLDProxyUpstreamVlanID,
       "swMLDProxyUpstreamDynamicRouterPorts": swMLDProxyUpstreamDynamicRouterPorts,
       "swMLDProxyUpstreamStaticRouterPorts": swMLDProxyUpstreamStaticRouterPorts,
       "swMLDProxyUpstreamUnsolicitedReportInterval": swMLDProxyUpstreamUnsolicitedReportInterval,
       "swMLDProxyUpstreamSourceIP": swMLDProxyUpstreamSourceIP,
       "swMLDProxyDownstreamInterfaceTable": swMLDProxyDownstreamInterfaceTable,
       "swMLDProxyDownstreamInterfaceEntry": swMLDProxyDownstreamInterfaceEntry,
       "swMLDProxyDownstreamRowStatus": swMLDProxyDownstreamRowStatus}
)
