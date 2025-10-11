# SNMP MIB module (EGRESSACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/EGRESSACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:20 2025
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
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swEgressAclMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 89)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwEgressAclInfo_ObjectIdentity = ObjectIdentity
swEgressAclInfo = _SwEgressAclInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 1)
)
_SwEgressACLTotalUsedRuleEntries_Type = Integer32
_SwEgressACLTotalUsedRuleEntries_Object = MibScalar
swEgressACLTotalUsedRuleEntries = _SwEgressACLTotalUsedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 1, 1),
    _SwEgressACLTotalUsedRuleEntries_Type()
)
swEgressACLTotalUsedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLTotalUsedRuleEntries.setStatus("current")
_SwEgressACLTotalUnusedRuleEntries_Type = Integer32
_SwEgressACLTotalUnusedRuleEntries_Object = MibScalar
swEgressACLTotalUnusedRuleEntries = _SwEgressACLTotalUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 1, 2),
    _SwEgressACLTotalUnusedRuleEntries_Type()
)
swEgressACLTotalUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLTotalUnusedRuleEntries.setStatus("current")
_SwEgressAclMaskMgmt_ObjectIdentity = ObjectIdentity
swEgressAclMaskMgmt = _SwEgressAclMaskMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2)
)
_SwEgressACLEthernetTable_Object = MibTable
swEgressACLEthernetTable = _SwEgressACLEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1)
)
if mibBuilder.loadTexts:
    swEgressACLEthernetTable.setStatus("current")
_SwEgressACLEthernetEntry_Object = MibTableRow
swEgressACLEthernetEntry = _SwEgressACLEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1)
)
swEgressACLEthernetEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLEthernetProfileID"),
)
if mibBuilder.loadTexts:
    swEgressACLEthernetEntry.setStatus("current")
_SwEgressACLEthernetProfileID_Type = Integer32
_SwEgressACLEthernetProfileID_Object = MibTableColumn
swEgressACLEthernetProfileID = _SwEgressACLEthernetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 1),
    _SwEgressACLEthernetProfileID_Type()
)
swEgressACLEthernetProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLEthernetProfileID.setStatus("current")
_SwEgressACLEthernetRowStatus_Type = RowStatus
_SwEgressACLEthernetRowStatus_Object = MibTableColumn
swEgressACLEthernetRowStatus = _SwEgressACLEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 2),
    _SwEgressACLEthernetRowStatus_Type()
)
swEgressACLEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetRowStatus.setStatus("current")


class _SwEgressACLEthernetProfileName_Type(DisplayString):
    """Custom type swEgressACLEthernetProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwEgressACLEthernetProfileName_Type.__name__ = "DisplayString"
_SwEgressACLEthernetProfileName_Object = MibTableColumn
swEgressACLEthernetProfileName = _SwEgressACLEthernetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 3),
    _SwEgressACLEthernetProfileName_Type()
)
swEgressACLEthernetProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetProfileName.setStatus("current")


class _SwEgressACLEthernetUsevlan_Type(Integer32):
    """Custom type swEgressACLEthernetUsevlan based on Integer32"""
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


_SwEgressACLEthernetUsevlan_Type.__name__ = "Integer32"
_SwEgressACLEthernetUsevlan_Object = MibTableColumn
swEgressACLEthernetUsevlan = _SwEgressACLEthernetUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 4),
    _SwEgressACLEthernetUsevlan_Type()
)
swEgressACLEthernetUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetUsevlan.setStatus("current")


class _SwEgressACLEthernetVlanMask_Type(OctetString):
    """Custom type swEgressACLEthernetVlanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLEthernetVlanMask_Type.__name__ = "OctetString"
_SwEgressACLEthernetVlanMask_Object = MibTableColumn
swEgressACLEthernetVlanMask = _SwEgressACLEthernetVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 5),
    _SwEgressACLEthernetVlanMask_Type()
)
swEgressACLEthernetVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetVlanMask.setStatus("current")


class _SwEgressACLEthernetUse8021p_Type(Integer32):
    """Custom type swEgressACLEthernetUse8021p based on Integer32"""
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


_SwEgressACLEthernetUse8021p_Type.__name__ = "Integer32"
_SwEgressACLEthernetUse8021p_Object = MibTableColumn
swEgressACLEthernetUse8021p = _SwEgressACLEthernetUse8021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 6),
    _SwEgressACLEthernetUse8021p_Type()
)
swEgressACLEthernetUse8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetUse8021p.setStatus("current")


class _SwEgressACLEthernetUseEthernetType_Type(Integer32):
    """Custom type swEgressACLEthernetUseEthernetType based on Integer32"""
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


_SwEgressACLEthernetUseEthernetType_Type.__name__ = "Integer32"
_SwEgressACLEthernetUseEthernetType_Object = MibTableColumn
swEgressACLEthernetUseEthernetType = _SwEgressACLEthernetUseEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 7),
    _SwEgressACLEthernetUseEthernetType_Type()
)
swEgressACLEthernetUseEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetUseEthernetType.setStatus("current")


class _SwEgressACLEthernetMacAddrMaskState_Type(Integer32):
    """Custom type swEgressACLEthernetMacAddrMaskState based on Integer32"""
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
          ("dst-mac-addr", 2),
          ("src-mac-addr", 3),
          ("dst-src-mac-addr", 4))
    )


_SwEgressACLEthernetMacAddrMaskState_Type.__name__ = "Integer32"
_SwEgressACLEthernetMacAddrMaskState_Object = MibTableColumn
swEgressACLEthernetMacAddrMaskState = _SwEgressACLEthernetMacAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 8),
    _SwEgressACLEthernetMacAddrMaskState_Type()
)
swEgressACLEthernetMacAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetMacAddrMaskState.setStatus("current")
_SwEgressACLEthernetSrcMacAddrMask_Type = MacAddress
_SwEgressACLEthernetSrcMacAddrMask_Object = MibTableColumn
swEgressACLEthernetSrcMacAddrMask = _SwEgressACLEthernetSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 9),
    _SwEgressACLEthernetSrcMacAddrMask_Type()
)
swEgressACLEthernetSrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetSrcMacAddrMask.setStatus("current")
_SwEgressACLEthernetDstMacAddrMask_Type = MacAddress
_SwEgressACLEthernetDstMacAddrMask_Object = MibTableColumn
swEgressACLEthernetDstMacAddrMask = _SwEgressACLEthernetDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 10),
    _SwEgressACLEthernetDstMacAddrMask_Type()
)
swEgressACLEthernetDstMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEthernetDstMacAddrMask.setStatus("current")
_SwEgressACLEthernetUnusedRuleEntries_Type = Integer32
_SwEgressACLEthernetUnusedRuleEntries_Object = MibTableColumn
swEgressACLEthernetUnusedRuleEntries = _SwEgressACLEthernetUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 1, 1, 11),
    _SwEgressACLEthernetUnusedRuleEntries_Type()
)
swEgressACLEthernetUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLEthernetUnusedRuleEntries.setStatus("current")
_SwEgressACLIpTable_Object = MibTable
swEgressACLIpTable = _SwEgressACLIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2)
)
if mibBuilder.loadTexts:
    swEgressACLIpTable.setStatus("current")
_SwEgressACLIpEntry_Object = MibTableRow
swEgressACLIpEntry = _SwEgressACLIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1)
)
swEgressACLIpEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLIpProfileID"),
)
if mibBuilder.loadTexts:
    swEgressACLIpEntry.setStatus("current")
_SwEgressACLIpProfileID_Type = Integer32
_SwEgressACLIpProfileID_Object = MibTableColumn
swEgressACLIpProfileID = _SwEgressACLIpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 1),
    _SwEgressACLIpProfileID_Type()
)
swEgressACLIpProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpProfileID.setStatus("current")
_SwEgressACLIpRowStatus_Type = RowStatus
_SwEgressACLIpRowStatus_Object = MibTableColumn
swEgressACLIpRowStatus = _SwEgressACLIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 2),
    _SwEgressACLIpRowStatus_Type()
)
swEgressACLIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRowStatus.setStatus("current")


class _SwEgressACLIpProfileName_Type(DisplayString):
    """Custom type swEgressACLIpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwEgressACLIpProfileName_Type.__name__ = "DisplayString"
_SwEgressACLIpProfileName_Object = MibTableColumn
swEgressACLIpProfileName = _SwEgressACLIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 3),
    _SwEgressACLIpProfileName_Type()
)
swEgressACLIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpProfileName.setStatus("current")


class _SwEgressACLIpUsevlan_Type(Integer32):
    """Custom type swEgressACLIpUsevlan based on Integer32"""
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


_SwEgressACLIpUsevlan_Type.__name__ = "Integer32"
_SwEgressACLIpUsevlan_Object = MibTableColumn
swEgressACLIpUsevlan = _SwEgressACLIpUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 4),
    _SwEgressACLIpUsevlan_Type()
)
swEgressACLIpUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpUsevlan.setStatus("current")


class _SwEgressACLIpVlanMask_Type(OctetString):
    """Custom type swEgressACLIpVlanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpVlanMask_Type.__name__ = "OctetString"
_SwEgressACLIpVlanMask_Object = MibTableColumn
swEgressACLIpVlanMask = _SwEgressACLIpVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 5),
    _SwEgressACLIpVlanMask_Type()
)
swEgressACLIpVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpVlanMask.setStatus("current")


class _SwEgressACLIpIpAddrMaskState_Type(Integer32):
    """Custom type swEgressACLIpIpAddrMaskState based on Integer32"""
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
          ("dst-ip-addr", 2),
          ("src-ip-addr", 3),
          ("dst-src-ip-addr", 4))
    )


_SwEgressACLIpIpAddrMaskState_Type.__name__ = "Integer32"
_SwEgressACLIpIpAddrMaskState_Object = MibTableColumn
swEgressACLIpIpAddrMaskState = _SwEgressACLIpIpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 6),
    _SwEgressACLIpIpAddrMaskState_Type()
)
swEgressACLIpIpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpIpAddrMaskState.setStatus("current")
_SwEgressACLIpSrcIpAddrMask_Type = IpAddress
_SwEgressACLIpSrcIpAddrMask_Object = MibTableColumn
swEgressACLIpSrcIpAddrMask = _SwEgressACLIpSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 7),
    _SwEgressACLIpSrcIpAddrMask_Type()
)
swEgressACLIpSrcIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpSrcIpAddrMask.setStatus("current")
_SwEgressACLIpDstIpAddrMask_Type = IpAddress
_SwEgressACLIpDstIpAddrMask_Object = MibTableColumn
swEgressACLIpDstIpAddrMask = _SwEgressACLIpDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 8),
    _SwEgressACLIpDstIpAddrMask_Type()
)
swEgressACLIpDstIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpDstIpAddrMask.setStatus("current")


class _SwEgressACLIpUseDSCP_Type(Integer32):
    """Custom type swEgressACLIpUseDSCP based on Integer32"""
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


_SwEgressACLIpUseDSCP_Type.__name__ = "Integer32"
_SwEgressACLIpUseDSCP_Object = MibTableColumn
swEgressACLIpUseDSCP = _SwEgressACLIpUseDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 9),
    _SwEgressACLIpUseDSCP_Type()
)
swEgressACLIpUseDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpUseDSCP.setStatus("current")


class _SwEgressACLIpUseProtoType_Type(Integer32):
    """Custom type swEgressACLIpUseProtoType based on Integer32"""
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
        *(("none", 1),
          ("icmp", 2),
          ("igmp", 3),
          ("tcp", 4),
          ("udp", 5),
          ("protocolId", 6))
    )


_SwEgressACLIpUseProtoType_Type.__name__ = "Integer32"
_SwEgressACLIpUseProtoType_Object = MibTableColumn
swEgressACLIpUseProtoType = _SwEgressACLIpUseProtoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 10),
    _SwEgressACLIpUseProtoType_Type()
)
swEgressACLIpUseProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpUseProtoType.setStatus("current")


class _SwEgressACLIpIcmpOption_Type(Integer32):
    """Custom type swEgressACLIpIcmpOption based on Integer32"""
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
          ("type", 2),
          ("code", 3),
          ("type-code", 4))
    )


_SwEgressACLIpIcmpOption_Type.__name__ = "Integer32"
_SwEgressACLIpIcmpOption_Object = MibTableColumn
swEgressACLIpIcmpOption = _SwEgressACLIpIcmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 11),
    _SwEgressACLIpIcmpOption_Type()
)
swEgressACLIpIcmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpIcmpOption.setStatus("current")


class _SwEgressACLIpIgmpOption_Type(Integer32):
    """Custom type swEgressACLIpIgmpOption based on Integer32"""
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


_SwEgressACLIpIgmpOption_Type.__name__ = "Integer32"
_SwEgressACLIpIgmpOption_Object = MibTableColumn
swEgressACLIpIgmpOption = _SwEgressACLIpIgmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 12),
    _SwEgressACLIpIgmpOption_Type()
)
swEgressACLIpIgmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpIgmpOption.setStatus("current")


class _SwEgressACLIpTcpOption_Type(Integer32):
    """Custom type swEgressACLIpTcpOption based on Integer32"""
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
          ("dst-addr", 2),
          ("src-addr", 3),
          ("dst-src-addr", 4))
    )


_SwEgressACLIpTcpOption_Type.__name__ = "Integer32"
_SwEgressACLIpTcpOption_Object = MibTableColumn
swEgressACLIpTcpOption = _SwEgressACLIpTcpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 13),
    _SwEgressACLIpTcpOption_Type()
)
swEgressACLIpTcpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpTcpOption.setStatus("current")


class _SwEgressACLIpUdpOption_Type(Integer32):
    """Custom type swEgressACLIpUdpOption based on Integer32"""
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
          ("dst-addr", 2),
          ("src-addr", 3),
          ("dst-src-addr", 4))
    )


_SwEgressACLIpUdpOption_Type.__name__ = "Integer32"
_SwEgressACLIpUdpOption_Object = MibTableColumn
swEgressACLIpUdpOption = _SwEgressACLIpUdpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 14),
    _SwEgressACLIpUdpOption_Type()
)
swEgressACLIpUdpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpUdpOption.setStatus("current")


class _SwEgressACLIpTCPorUDPSrcPortMask_Type(OctetString):
    """Custom type swEgressACLIpTCPorUDPSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpTCPorUDPSrcPortMask_Type.__name__ = "OctetString"
_SwEgressACLIpTCPorUDPSrcPortMask_Object = MibTableColumn
swEgressACLIpTCPorUDPSrcPortMask = _SwEgressACLIpTCPorUDPSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 15),
    _SwEgressACLIpTCPorUDPSrcPortMask_Type()
)
swEgressACLIpTCPorUDPSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpTCPorUDPSrcPortMask.setStatus("current")


class _SwEgressACLIpTCPorUDPDstPortMask_Type(OctetString):
    """Custom type swEgressACLIpTCPorUDPDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpTCPorUDPDstPortMask_Type.__name__ = "OctetString"
_SwEgressACLIpTCPorUDPDstPortMask_Object = MibTableColumn
swEgressACLIpTCPorUDPDstPortMask = _SwEgressACLIpTCPorUDPDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 16),
    _SwEgressACLIpTCPorUDPDstPortMask_Type()
)
swEgressACLIpTCPorUDPDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpTCPorUDPDstPortMask.setStatus("current")


class _SwEgressACLIpTCPFlagBit_Type(Integer32):
    """Custom type swEgressACLIpTCPFlagBit based on Integer32"""
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


_SwEgressACLIpTCPFlagBit_Type.__name__ = "Integer32"
_SwEgressACLIpTCPFlagBit_Object = MibTableColumn
swEgressACLIpTCPFlagBit = _SwEgressACLIpTCPFlagBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 17),
    _SwEgressACLIpTCPFlagBit_Type()
)
swEgressACLIpTCPFlagBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpTCPFlagBit.setStatus("current")


class _SwEgressACLIpTCPFlagBitMask_Type(Integer32):
    """Custom type swEgressACLIpTCPFlagBitMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwEgressACLIpTCPFlagBitMask_Type.__name__ = "Integer32"
_SwEgressACLIpTCPFlagBitMask_Object = MibTableColumn
swEgressACLIpTCPFlagBitMask = _SwEgressACLIpTCPFlagBitMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 18),
    _SwEgressACLIpTCPFlagBitMask_Type()
)
swEgressACLIpTCPFlagBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpTCPFlagBitMask.setStatus("current")


class _SwEgressACLIpProtoIDOption_Type(Integer32):
    """Custom type swEgressACLIpProtoIDOption based on Integer32"""
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


_SwEgressACLIpProtoIDOption_Type.__name__ = "Integer32"
_SwEgressACLIpProtoIDOption_Object = MibTableColumn
swEgressACLIpProtoIDOption = _SwEgressACLIpProtoIDOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 19),
    _SwEgressACLIpProtoIDOption_Type()
)
swEgressACLIpProtoIDOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpProtoIDOption.setStatus("current")


class _SwEgressACLIpProtoID_Type(Integer32):
    """Custom type swEgressACLIpProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwEgressACLIpProtoID_Type.__name__ = "Integer32"
_SwEgressACLIpProtoID_Object = MibTableColumn
swEgressACLIpProtoID = _SwEgressACLIpProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 20),
    _SwEgressACLIpProtoID_Type()
)
swEgressACLIpProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpProtoID.setStatus("current")


class _SwEgressACLIpProtoIDMask_Type(OctetString):
    """Custom type swEgressACLIpProtoIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwEgressACLIpProtoIDMask_Type.__name__ = "OctetString"
_SwEgressACLIpProtoIDMask_Object = MibTableColumn
swEgressACLIpProtoIDMask = _SwEgressACLIpProtoIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 21),
    _SwEgressACLIpProtoIDMask_Type()
)
swEgressACLIpProtoIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpProtoIDMask.setStatus("current")
_SwEgressACLIpUnusedRuleEntries_Type = Integer32
_SwEgressACLIpUnusedRuleEntries_Object = MibTableColumn
swEgressACLIpUnusedRuleEntries = _SwEgressACLIpUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 2, 1, 22),
    _SwEgressACLIpUnusedRuleEntries_Type()
)
swEgressACLIpUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLIpUnusedRuleEntries.setStatus("current")
_SwEgressACLIpv6MaskTable_Object = MibTable
swEgressACLIpv6MaskTable = _SwEgressACLIpv6MaskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3)
)
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskTable.setStatus("current")
_SwEgressACLIpv6MaskEntry_Object = MibTableRow
swEgressACLIpv6MaskEntry = _SwEgressACLIpv6MaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1)
)
swEgressACLIpv6MaskEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLIpv6MaskProfileID"),
)
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskEntry.setStatus("current")
_SwEgressACLIpv6MaskProfileID_Type = Integer32
_SwEgressACLIpv6MaskProfileID_Object = MibTableColumn
swEgressACLIpv6MaskProfileID = _SwEgressACLIpv6MaskProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 1),
    _SwEgressACLIpv6MaskProfileID_Type()
)
swEgressACLIpv6MaskProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskProfileID.setStatus("current")
_SwEgressACLIpv6MaskRowStatus_Type = RowStatus
_SwEgressACLIpv6MaskRowStatus_Object = MibTableColumn
swEgressACLIpv6MaskRowStatus = _SwEgressACLIpv6MaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 2),
    _SwEgressACLIpv6MaskRowStatus_Type()
)
swEgressACLIpv6MaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskRowStatus.setStatus("current")


class _SwEgressACLIpv6MaskProfileName_Type(DisplayString):
    """Custom type swEgressACLIpv6MaskProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwEgressACLIpv6MaskProfileName_Type.__name__ = "DisplayString"
_SwEgressACLIpv6MaskProfileName_Object = MibTableColumn
swEgressACLIpv6MaskProfileName = _SwEgressACLIpv6MaskProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 3),
    _SwEgressACLIpv6MaskProfileName_Type()
)
swEgressACLIpv6MaskProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskProfileName.setStatus("current")


class _SwEgressACLIpv6MaskClass_Type(Integer32):
    """Custom type swEgressACLIpv6MaskClass based on Integer32"""
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


_SwEgressACLIpv6MaskClass_Type.__name__ = "Integer32"
_SwEgressACLIpv6MaskClass_Object = MibTableColumn
swEgressACLIpv6MaskClass = _SwEgressACLIpv6MaskClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 4),
    _SwEgressACLIpv6MaskClass_Type()
)
swEgressACLIpv6MaskClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskClass.setStatus("current")


class _SwEgressACLIpv6IpAddrMaskState_Type(Integer32):
    """Custom type swEgressACLIpv6IpAddrMaskState based on Integer32"""
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
          ("dst-ipv6-addr", 2),
          ("src-ipv6-addr", 3),
          ("dst-src-ipv6-addr", 4))
    )


_SwEgressACLIpv6IpAddrMaskState_Type.__name__ = "Integer32"
_SwEgressACLIpv6IpAddrMaskState_Object = MibTableColumn
swEgressACLIpv6IpAddrMaskState = _SwEgressACLIpv6IpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 5),
    _SwEgressACLIpv6IpAddrMaskState_Type()
)
swEgressACLIpv6IpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6IpAddrMaskState.setStatus("current")
_SwEgressACLIpv6MaskSrcIpv6Mask_Type = Ipv6Address
_SwEgressACLIpv6MaskSrcIpv6Mask_Object = MibTableColumn
swEgressACLIpv6MaskSrcIpv6Mask = _SwEgressACLIpv6MaskSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 6),
    _SwEgressACLIpv6MaskSrcIpv6Mask_Type()
)
swEgressACLIpv6MaskSrcIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskSrcIpv6Mask.setStatus("current")
_SwEgressACLIpv6MaskDstIpv6Mask_Type = Ipv6Address
_SwEgressACLIpv6MaskDstIpv6Mask_Object = MibTableColumn
swEgressACLIpv6MaskDstIpv6Mask = _SwEgressACLIpv6MaskDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 7),
    _SwEgressACLIpv6MaskDstIpv6Mask_Type()
)
swEgressACLIpv6MaskDstIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskDstIpv6Mask.setStatus("current")


class _SwEgressACLIpv6MaskUseProtoType_Type(Integer32):
    """Custom type swEgressACLIpv6MaskUseProtoType based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4))
    )


_SwEgressACLIpv6MaskUseProtoType_Type.__name__ = "Integer32"
_SwEgressACLIpv6MaskUseProtoType_Object = MibTableColumn
swEgressACLIpv6MaskUseProtoType = _SwEgressACLIpv6MaskUseProtoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 8),
    _SwEgressACLIpv6MaskUseProtoType_Type()
)
swEgressACLIpv6MaskUseProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskUseProtoType.setStatus("current")


class _SwEgressACLIpv6MaskIcmpOption_Type(Integer32):
    """Custom type swEgressACLIpv6MaskIcmpOption based on Integer32"""
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
          ("type", 2),
          ("code", 3),
          ("type-code", 4))
    )


_SwEgressACLIpv6MaskIcmpOption_Type.__name__ = "Integer32"
_SwEgressACLIpv6MaskIcmpOption_Object = MibTableColumn
swEgressACLIpv6MaskIcmpOption = _SwEgressACLIpv6MaskIcmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 9),
    _SwEgressACLIpv6MaskIcmpOption_Type()
)
swEgressACLIpv6MaskIcmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskIcmpOption.setStatus("current")


class _SwEgressACLIpv6MaskTcpOption_Type(Integer32):
    """Custom type swEgressACLIpv6MaskTcpOption based on Integer32"""
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
          ("dst-addr", 2),
          ("src-addr", 3),
          ("dst-src-addr", 4))
    )


_SwEgressACLIpv6MaskTcpOption_Type.__name__ = "Integer32"
_SwEgressACLIpv6MaskTcpOption_Object = MibTableColumn
swEgressACLIpv6MaskTcpOption = _SwEgressACLIpv6MaskTcpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 10),
    _SwEgressACLIpv6MaskTcpOption_Type()
)
swEgressACLIpv6MaskTcpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskTcpOption.setStatus("current")


class _SwEgressACLIpv6MaskUdpOption_Type(Integer32):
    """Custom type swEgressACLIpv6MaskUdpOption based on Integer32"""
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
          ("dst-addr", 2),
          ("src-addr", 3),
          ("dst-src-addr", 4))
    )


_SwEgressACLIpv6MaskUdpOption_Type.__name__ = "Integer32"
_SwEgressACLIpv6MaskUdpOption_Object = MibTableColumn
swEgressACLIpv6MaskUdpOption = _SwEgressACLIpv6MaskUdpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 11),
    _SwEgressACLIpv6MaskUdpOption_Type()
)
swEgressACLIpv6MaskUdpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskUdpOption.setStatus("current")


class _SwEgressACLIpv6MaskTCPorUDPSrcPortMask_Type(OctetString):
    """Custom type swEgressACLIpv6MaskTCPorUDPSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpv6MaskTCPorUDPSrcPortMask_Type.__name__ = "OctetString"
_SwEgressACLIpv6MaskTCPorUDPSrcPortMask_Object = MibTableColumn
swEgressACLIpv6MaskTCPorUDPSrcPortMask = _SwEgressACLIpv6MaskTCPorUDPSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 12),
    _SwEgressACLIpv6MaskTCPorUDPSrcPortMask_Type()
)
swEgressACLIpv6MaskTCPorUDPSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskTCPorUDPSrcPortMask.setStatus("current")


class _SwEgressACLIpv6MaskTCPorUDPDstPortMask_Type(OctetString):
    """Custom type swEgressACLIpv6MaskTCPorUDPDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpv6MaskTCPorUDPDstPortMask_Type.__name__ = "OctetString"
_SwEgressACLIpv6MaskTCPorUDPDstPortMask_Object = MibTableColumn
swEgressACLIpv6MaskTCPorUDPDstPortMask = _SwEgressACLIpv6MaskTCPorUDPDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 13),
    _SwEgressACLIpv6MaskTCPorUDPDstPortMask_Type()
)
swEgressACLIpv6MaskTCPorUDPDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskTCPorUDPDstPortMask.setStatus("current")
_SwEgressACLIpv6MaskUnusedRuleEntries_Type = Integer32
_SwEgressACLIpv6MaskUnusedRuleEntries_Object = MibTableColumn
swEgressACLIpv6MaskUnusedRuleEntries = _SwEgressACLIpv6MaskUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 3, 1, 14),
    _SwEgressACLIpv6MaskUnusedRuleEntries_Type()
)
swEgressACLIpv6MaskUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLIpv6MaskUnusedRuleEntries.setStatus("current")


class _SwEgressACLMaskDelAllState_Type(Integer32):
    """Custom type swEgressACLMaskDelAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwEgressACLMaskDelAllState_Type.__name__ = "Integer32"
_SwEgressACLMaskDelAllState_Object = MibScalar
swEgressACLMaskDelAllState = _SwEgressACLMaskDelAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 2, 4),
    _SwEgressACLMaskDelAllState_Type()
)
swEgressACLMaskDelAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEgressACLMaskDelAllState.setStatus("current")
_SwEgressAclRuleMgmt_ObjectIdentity = ObjectIdentity
swEgressAclRuleMgmt = _SwEgressAclRuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3)
)
_SwEgressACLEtherRuleTable_Object = MibTable
swEgressACLEtherRuleTable = _SwEgressACLEtherRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1)
)
if mibBuilder.loadTexts:
    swEgressACLEtherRuleTable.setStatus("current")
_SwEgressACLEtherRuleEntry_Object = MibTableRow
swEgressACLEtherRuleEntry = _SwEgressACLEtherRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1)
)
swEgressACLEtherRuleEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLEtherRuleProfileID"),
    (0, "EGRESSACL-MIB", "swEgressACLEtherRuleAccessID"),
)
if mibBuilder.loadTexts:
    swEgressACLEtherRuleEntry.setStatus("current")
_SwEgressACLEtherRuleProfileID_Type = Integer32
_SwEgressACLEtherRuleProfileID_Object = MibTableColumn
swEgressACLEtherRuleProfileID = _SwEgressACLEtherRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 1),
    _SwEgressACLEtherRuleProfileID_Type()
)
swEgressACLEtherRuleProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleProfileID.setStatus("current")


class _SwEgressACLEtherRuleAccessID_Type(Integer32):
    """Custom type swEgressACLEtherRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwEgressACLEtherRuleAccessID_Type.__name__ = "Integer32"
_SwEgressACLEtherRuleAccessID_Object = MibTableColumn
swEgressACLEtherRuleAccessID = _SwEgressACLEtherRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 2),
    _SwEgressACLEtherRuleAccessID_Type()
)
swEgressACLEtherRuleAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleAccessID.setStatus("current")
_SwEgressACLEtherRuleRowStatus_Type = RowStatus
_SwEgressACLEtherRuleRowStatus_Object = MibTableColumn
swEgressACLEtherRuleRowStatus = _SwEgressACLEtherRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 3),
    _SwEgressACLEtherRuleRowStatus_Type()
)
swEgressACLEtherRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleRowStatus.setStatus("current")
_SwEgressACLEtherRuleMatchVID_Type = VlanIdOrNone
_SwEgressACLEtherRuleMatchVID_Object = MibTableColumn
swEgressACLEtherRuleMatchVID = _SwEgressACLEtherRuleMatchVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 4),
    _SwEgressACLEtherRuleMatchVID_Type()
)
swEgressACLEtherRuleMatchVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleMatchVID.setStatus("current")


class _SwEgressACLEtherRuleMatchVlanMask_Type(OctetString):
    """Custom type swEgressACLEtherRuleMatchVlanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLEtherRuleMatchVlanMask_Type.__name__ = "OctetString"
_SwEgressACLEtherRuleMatchVlanMask_Object = MibTableColumn
swEgressACLEtherRuleMatchVlanMask = _SwEgressACLEtherRuleMatchVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 5),
    _SwEgressACLEtherRuleMatchVlanMask_Type()
)
swEgressACLEtherRuleMatchVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleMatchVlanMask.setStatus("current")
_SwEgressACLEtherRuleSrcMacAddress_Type = MacAddress
_SwEgressACLEtherRuleSrcMacAddress_Object = MibTableColumn
swEgressACLEtherRuleSrcMacAddress = _SwEgressACLEtherRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 6),
    _SwEgressACLEtherRuleSrcMacAddress_Type()
)
swEgressACLEtherRuleSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleSrcMacAddress.setStatus("current")
_SwEgressACLEtherRuleMaskSrcMacAddress_Type = MacAddress
_SwEgressACLEtherRuleMaskSrcMacAddress_Object = MibTableColumn
swEgressACLEtherRuleMaskSrcMacAddress = _SwEgressACLEtherRuleMaskSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 7),
    _SwEgressACLEtherRuleMaskSrcMacAddress_Type()
)
swEgressACLEtherRuleMaskSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleMaskSrcMacAddress.setStatus("current")
_SwEgressACLEtherRuleDstMacAddress_Type = MacAddress
_SwEgressACLEtherRuleDstMacAddress_Object = MibTableColumn
swEgressACLEtherRuleDstMacAddress = _SwEgressACLEtherRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 8),
    _SwEgressACLEtherRuleDstMacAddress_Type()
)
swEgressACLEtherRuleDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleDstMacAddress.setStatus("current")
_SwEgressACLEtherRuleMaskDstMacAddress_Type = MacAddress
_SwEgressACLEtherRuleMaskDstMacAddress_Object = MibTableColumn
swEgressACLEtherRuleMaskDstMacAddress = _SwEgressACLEtherRuleMaskDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 9),
    _SwEgressACLEtherRuleMaskDstMacAddress_Type()
)
swEgressACLEtherRuleMaskDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleMaskDstMacAddress.setStatus("current")


class _SwEgressACLEtherRule8021P_Type(Integer32):
    """Custom type swEgressACLEtherRule8021P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwEgressACLEtherRule8021P_Type.__name__ = "Integer32"
_SwEgressACLEtherRule8021P_Object = MibTableColumn
swEgressACLEtherRule8021P = _SwEgressACLEtherRule8021P_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 10),
    _SwEgressACLEtherRule8021P_Type()
)
swEgressACLEtherRule8021P.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRule8021P.setStatus("current")


class _SwEgressACLEtherRuleEtherType_Type(OctetString):
    """Custom type swEgressACLEtherRuleEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLEtherRuleEtherType_Type.__name__ = "OctetString"
_SwEgressACLEtherRuleEtherType_Object = MibTableColumn
swEgressACLEtherRuleEtherType = _SwEgressACLEtherRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 11),
    _SwEgressACLEtherRuleEtherType_Type()
)
swEgressACLEtherRuleEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleEtherType.setStatus("current")
_SwEgressACLEtherRuleVID_Type = VlanIdOrNone
_SwEgressACLEtherRuleVID_Object = MibTableColumn
swEgressACLEtherRuleVID = _SwEgressACLEtherRuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 12),
    _SwEgressACLEtherRuleVID_Type()
)
swEgressACLEtherRuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleVID.setStatus("current")
_SwEgressACLEtherRulePort_Type = Integer32
_SwEgressACLEtherRulePort_Object = MibTableColumn
swEgressACLEtherRulePort = _SwEgressACLEtherRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 13),
    _SwEgressACLEtherRulePort_Type()
)
swEgressACLEtherRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRulePort.setStatus("current")
_SwEgressACLEtherRulePortGroup_Type = Integer32
_SwEgressACLEtherRulePortGroup_Object = MibTableColumn
swEgressACLEtherRulePortGroup = _SwEgressACLEtherRulePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 14),
    _SwEgressACLEtherRulePortGroup_Type()
)
swEgressACLEtherRulePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRulePortGroup.setStatus("current")


class _SwEgressACLEtherRulePermit_Type(Integer32):
    """Custom type swEgressACLEtherRulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwEgressACLEtherRulePermit_Type.__name__ = "Integer32"
_SwEgressACLEtherRulePermit_Object = MibTableColumn
swEgressACLEtherRulePermit = _SwEgressACLEtherRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 15),
    _SwEgressACLEtherRulePermit_Type()
)
swEgressACLEtherRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRulePermit.setStatus("current")


class _SwEgressACLEtherRuleEnableReplacePriority_Type(Integer32):
    """Custom type swEgressACLEtherRuleEnableReplacePriority based on Integer32"""
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


_SwEgressACLEtherRuleEnableReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLEtherRuleEnableReplacePriority_Object = MibTableColumn
swEgressACLEtherRuleEnableReplacePriority = _SwEgressACLEtherRuleEnableReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 16),
    _SwEgressACLEtherRuleEnableReplacePriority_Type()
)
swEgressACLEtherRuleEnableReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleEnableReplacePriority.setStatus("current")


class _SwEgressACLEtherRuleReplacePriority_Type(Integer32):
    """Custom type swEgressACLEtherRuleReplacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwEgressACLEtherRuleReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLEtherRuleReplacePriority_Object = MibTableColumn
swEgressACLEtherRuleReplacePriority = _SwEgressACLEtherRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 17),
    _SwEgressACLEtherRuleReplacePriority_Type()
)
swEgressACLEtherRuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleReplacePriority.setStatus("current")


class _SwEgressACLEtherRuleEnableReplaceDscp_Type(Integer32):
    """Custom type swEgressACLEtherRuleEnableReplaceDscp based on Integer32"""
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


_SwEgressACLEtherRuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLEtherRuleEnableReplaceDscp_Object = MibTableColumn
swEgressACLEtherRuleEnableReplaceDscp = _SwEgressACLEtherRuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 18),
    _SwEgressACLEtherRuleEnableReplaceDscp_Type()
)
swEgressACLEtherRuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleEnableReplaceDscp.setStatus("current")


class _SwEgressACLEtherRuleReplaceDscp_Type(Integer32):
    """Custom type swEgressACLEtherRuleReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressACLEtherRuleReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLEtherRuleReplaceDscp_Object = MibTableColumn
swEgressACLEtherRuleReplaceDscp = _SwEgressACLEtherRuleReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 19),
    _SwEgressACLEtherRuleReplaceDscp_Type()
)
swEgressACLEtherRuleReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLEtherRuleReplaceDscp.setStatus("current")
_SwEgressAclEtherRuleTimeRangeName_Type = DisplayString
_SwEgressAclEtherRuleTimeRangeName_Object = MibTableColumn
swEgressAclEtherRuleTimeRangeName = _SwEgressAclEtherRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 1, 1, 20),
    _SwEgressAclEtherRuleTimeRangeName_Type()
)
swEgressAclEtherRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclEtherRuleTimeRangeName.setStatus("current")
_SwEgressACLIpRuleTable_Object = MibTable
swEgressACLIpRuleTable = _SwEgressACLIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2)
)
if mibBuilder.loadTexts:
    swEgressACLIpRuleTable.setStatus("current")
_SwEgressACLIpRuleEntry_Object = MibTableRow
swEgressACLIpRuleEntry = _SwEgressACLIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1)
)
swEgressACLIpRuleEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLIpRuleProfileID"),
    (0, "EGRESSACL-MIB", "swEgressACLIpRuleAccessID"),
)
if mibBuilder.loadTexts:
    swEgressACLIpRuleEntry.setStatus("current")
_SwEgressACLIpRuleProfileID_Type = Integer32
_SwEgressACLIpRuleProfileID_Object = MibTableColumn
swEgressACLIpRuleProfileID = _SwEgressACLIpRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 1),
    _SwEgressACLIpRuleProfileID_Type()
)
swEgressACLIpRuleProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpRuleProfileID.setStatus("current")


class _SwEgressACLIpRuleAccessID_Type(Integer32):
    """Custom type swEgressACLIpRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwEgressACLIpRuleAccessID_Type.__name__ = "Integer32"
_SwEgressACLIpRuleAccessID_Object = MibTableColumn
swEgressACLIpRuleAccessID = _SwEgressACLIpRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 2),
    _SwEgressACLIpRuleAccessID_Type()
)
swEgressACLIpRuleAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpRuleAccessID.setStatus("current")
_SwEgressACLIpRuleRowStatus_Type = RowStatus
_SwEgressACLIpRuleRowStatus_Object = MibTableColumn
swEgressACLIpRuleRowStatus = _SwEgressACLIpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 3),
    _SwEgressACLIpRuleRowStatus_Type()
)
swEgressACLIpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleRowStatus.setStatus("current")
_SwEgressACLIpRuleMatchVID_Type = VlanIdOrNone
_SwEgressACLIpRuleMatchVID_Object = MibTableColumn
swEgressACLIpRuleMatchVID = _SwEgressACLIpRuleMatchVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 4),
    _SwEgressACLIpRuleMatchVID_Type()
)
swEgressACLIpRuleMatchVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleMatchVID.setStatus("current")


class _SwEgressACLIpMatchVlanMask_Type(OctetString):
    """Custom type swEgressACLIpMatchVlanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpMatchVlanMask_Type.__name__ = "OctetString"
_SwEgressACLIpMatchVlanMask_Object = MibTableColumn
swEgressACLIpMatchVlanMask = _SwEgressACLIpMatchVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 5),
    _SwEgressACLIpMatchVlanMask_Type()
)
swEgressACLIpMatchVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpMatchVlanMask.setStatus("current")
_SwEgressACLIpRuleSrcIpaddress_Type = IpAddress
_SwEgressACLIpRuleSrcIpaddress_Object = MibTableColumn
swEgressACLIpRuleSrcIpaddress = _SwEgressACLIpRuleSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 6),
    _SwEgressACLIpRuleSrcIpaddress_Type()
)
swEgressACLIpRuleSrcIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleSrcIpaddress.setStatus("current")
_SwEgressACLIpRuleMaskSrcIpaddress_Type = IpAddress
_SwEgressACLIpRuleMaskSrcIpaddress_Object = MibTableColumn
swEgressACLIpRuleMaskSrcIpaddress = _SwEgressACLIpRuleMaskSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 7),
    _SwEgressACLIpRuleMaskSrcIpaddress_Type()
)
swEgressACLIpRuleMaskSrcIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleMaskSrcIpaddress.setStatus("current")
_SwEgressACLIpRuleDstIpaddress_Type = IpAddress
_SwEgressACLIpRuleDstIpaddress_Object = MibTableColumn
swEgressACLIpRuleDstIpaddress = _SwEgressACLIpRuleDstIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 8),
    _SwEgressACLIpRuleDstIpaddress_Type()
)
swEgressACLIpRuleDstIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleDstIpaddress.setStatus("current")
_SwEgressACLIpRuleMaskDstIpaddress_Type = IpAddress
_SwEgressACLIpRuleMaskDstIpaddress_Object = MibTableColumn
swEgressACLIpRuleMaskDstIpaddress = _SwEgressACLIpRuleMaskDstIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 9),
    _SwEgressACLIpRuleMaskDstIpaddress_Type()
)
swEgressACLIpRuleMaskDstIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleMaskDstIpaddress.setStatus("current")


class _SwEgressACLIpRuleDscp_Type(Integer32):
    """Custom type swEgressACLIpRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressACLIpRuleDscp_Type.__name__ = "Integer32"
_SwEgressACLIpRuleDscp_Object = MibTableColumn
swEgressACLIpRuleDscp = _SwEgressACLIpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 10),
    _SwEgressACLIpRuleDscp_Type()
)
swEgressACLIpRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleDscp.setStatus("current")


class _SwEgressACLIpRuleProtocol_Type(Integer32):
    """Custom type swEgressACLIpRuleProtocol based on Integer32"""
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
        *(("none", 1),
          ("icmp", 2),
          ("igmp", 3),
          ("tcp", 4),
          ("udp", 5),
          ("protocolId", 6))
    )


_SwEgressACLIpRuleProtocol_Type.__name__ = "Integer32"
_SwEgressACLIpRuleProtocol_Object = MibTableColumn
swEgressACLIpRuleProtocol = _SwEgressACLIpRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 11),
    _SwEgressACLIpRuleProtocol_Type()
)
swEgressACLIpRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleProtocol.setStatus("current")


class _SwEgressACLIpRuleType_Type(Integer32):
    """Custom type swEgressACLIpRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpRuleType_Type.__name__ = "Integer32"
_SwEgressACLIpRuleType_Object = MibTableColumn
swEgressACLIpRuleType = _SwEgressACLIpRuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 12),
    _SwEgressACLIpRuleType_Type()
)
swEgressACLIpRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleType.setStatus("current")


class _SwEgressACLIpRuleCode_Type(Integer32):
    """Custom type swEgressACLIpRuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpRuleCode_Type.__name__ = "Integer32"
_SwEgressACLIpRuleCode_Object = MibTableColumn
swEgressACLIpRuleCode = _SwEgressACLIpRuleCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 13),
    _SwEgressACLIpRuleCode_Type()
)
swEgressACLIpRuleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleCode.setStatus("current")


class _SwEgressACLIpRuleSrcPort_Type(Integer32):
    """Custom type swEgressACLIpRuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwEgressACLIpRuleSrcPort_Type.__name__ = "Integer32"
_SwEgressACLIpRuleSrcPort_Object = MibTableColumn
swEgressACLIpRuleSrcPort = _SwEgressACLIpRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 14),
    _SwEgressACLIpRuleSrcPort_Type()
)
swEgressACLIpRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleSrcPort.setStatus("current")


class _SwEgressACLIpRuleMaskSrcPort_Type(OctetString):
    """Custom type swEgressACLIpRuleMaskSrcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpRuleMaskSrcPort_Type.__name__ = "OctetString"
_SwEgressACLIpRuleMaskSrcPort_Object = MibTableColumn
swEgressACLIpRuleMaskSrcPort = _SwEgressACLIpRuleMaskSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 15),
    _SwEgressACLIpRuleMaskSrcPort_Type()
)
swEgressACLIpRuleMaskSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleMaskSrcPort.setStatus("current")


class _SwEgressACLIpRuleDstPort_Type(Integer32):
    """Custom type swEgressACLIpRuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwEgressACLIpRuleDstPort_Type.__name__ = "Integer32"
_SwEgressACLIpRuleDstPort_Object = MibTableColumn
swEgressACLIpRuleDstPort = _SwEgressACLIpRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 16),
    _SwEgressACLIpRuleDstPort_Type()
)
swEgressACLIpRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleDstPort.setStatus("current")


class _SwEgressACLIpRuleMaskDstPort_Type(OctetString):
    """Custom type swEgressACLIpRuleMaskDstPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpRuleMaskDstPort_Type.__name__ = "OctetString"
_SwEgressACLIpRuleMaskDstPort_Object = MibTableColumn
swEgressACLIpRuleMaskDstPort = _SwEgressACLIpRuleMaskDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 17),
    _SwEgressACLIpRuleMaskDstPort_Type()
)
swEgressACLIpRuleMaskDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleMaskDstPort.setStatus("current")


class _SwEgressACLIpRuleFlagBits_Type(Integer32):
    """Custom type swEgressACLIpRuleFlagBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwEgressACLIpRuleFlagBits_Type.__name__ = "Integer32"
_SwEgressACLIpRuleFlagBits_Object = MibTableColumn
swEgressACLIpRuleFlagBits = _SwEgressACLIpRuleFlagBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 18),
    _SwEgressACLIpRuleFlagBits_Type()
)
swEgressACLIpRuleFlagBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleFlagBits.setStatus("current")


class _SwEgressACLIpRuleProtoID_Type(Integer32):
    """Custom type swEgressACLIpRuleProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpRuleProtoID_Type.__name__ = "Integer32"
_SwEgressACLIpRuleProtoID_Object = MibTableColumn
swEgressACLIpRuleProtoID = _SwEgressACLIpRuleProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 19),
    _SwEgressACLIpRuleProtoID_Type()
)
swEgressACLIpRuleProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleProtoID.setStatus("current")


class _SwEgressACLIpRuleUserDefine_Type(OctetString):
    """Custom type swEgressACLIpRuleUserDefine based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwEgressACLIpRuleUserDefine_Type.__name__ = "OctetString"
_SwEgressACLIpRuleUserDefine_Object = MibTableColumn
swEgressACLIpRuleUserDefine = _SwEgressACLIpRuleUserDefine_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 20),
    _SwEgressACLIpRuleUserDefine_Type()
)
swEgressACLIpRuleUserDefine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleUserDefine.setStatus("current")


class _SwEgressACLIpRuleUserDefineMask_Type(OctetString):
    """Custom type swEgressACLIpRuleUserDefineMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwEgressACLIpRuleUserDefineMask_Type.__name__ = "OctetString"
_SwEgressACLIpRuleUserDefineMask_Object = MibTableColumn
swEgressACLIpRuleUserDefineMask = _SwEgressACLIpRuleUserDefineMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 21),
    _SwEgressACLIpRuleUserDefineMask_Type()
)
swEgressACLIpRuleUserDefineMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleUserDefineMask.setStatus("current")
_SwEgressACLIpRuleVID_Type = VlanIdOrNone
_SwEgressACLIpRuleVID_Object = MibTableColumn
swEgressACLIpRuleVID = _SwEgressACLIpRuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 22),
    _SwEgressACLIpRuleVID_Type()
)
swEgressACLIpRuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleVID.setStatus("current")
_SwEgressACLIpRulePort_Type = Integer32
_SwEgressACLIpRulePort_Object = MibTableColumn
swEgressACLIpRulePort = _SwEgressACLIpRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 23),
    _SwEgressACLIpRulePort_Type()
)
swEgressACLIpRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRulePort.setStatus("current")
_SwEgressACLIpRulePortGroup_Type = Integer32
_SwEgressACLIpRulePortGroup_Object = MibTableColumn
swEgressACLIpRulePortGroup = _SwEgressACLIpRulePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 24),
    _SwEgressACLIpRulePortGroup_Type()
)
swEgressACLIpRulePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRulePortGroup.setStatus("current")


class _SwEgressACLIpRulePermit_Type(Integer32):
    """Custom type swEgressACLIpRulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwEgressACLIpRulePermit_Type.__name__ = "Integer32"
_SwEgressACLIpRulePermit_Object = MibTableColumn
swEgressACLIpRulePermit = _SwEgressACLIpRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 25),
    _SwEgressACLIpRulePermit_Type()
)
swEgressACLIpRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRulePermit.setStatus("current")


class _SwEgressACLIpRuleEnableReplacePriority_Type(Integer32):
    """Custom type swEgressACLIpRuleEnableReplacePriority based on Integer32"""
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


_SwEgressACLIpRuleEnableReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLIpRuleEnableReplacePriority_Object = MibTableColumn
swEgressACLIpRuleEnableReplacePriority = _SwEgressACLIpRuleEnableReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 26),
    _SwEgressACLIpRuleEnableReplacePriority_Type()
)
swEgressACLIpRuleEnableReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleEnableReplacePriority.setStatus("current")


class _SwEgressACLIpRuleReplacePriority_Type(Integer32):
    """Custom type swEgressACLIpRuleReplacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwEgressACLIpRuleReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLIpRuleReplacePriority_Object = MibTableColumn
swEgressACLIpRuleReplacePriority = _SwEgressACLIpRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 27),
    _SwEgressACLIpRuleReplacePriority_Type()
)
swEgressACLIpRuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleReplacePriority.setStatus("current")


class _SwEgressACLIpRuleEnableReplaceDscp_Type(Integer32):
    """Custom type swEgressACLIpRuleEnableReplaceDscp based on Integer32"""
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


_SwEgressACLIpRuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLIpRuleEnableReplaceDscp_Object = MibTableColumn
swEgressACLIpRuleEnableReplaceDscp = _SwEgressACLIpRuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 28),
    _SwEgressACLIpRuleEnableReplaceDscp_Type()
)
swEgressACLIpRuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleEnableReplaceDscp.setStatus("current")


class _SwEgressACLIpRuleReplaceDscp_Type(Integer32):
    """Custom type swEgressACLIpRuleReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressACLIpRuleReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLIpRuleReplaceDscp_Object = MibTableColumn
swEgressACLIpRuleReplaceDscp = _SwEgressACLIpRuleReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 29),
    _SwEgressACLIpRuleReplaceDscp_Type()
)
swEgressACLIpRuleReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpRuleReplaceDscp.setStatus("current")
_SwEgressAclIpRuleTimeRangeName_Type = DisplayString
_SwEgressAclIpRuleTimeRangeName_Object = MibTableColumn
swEgressAclIpRuleTimeRangeName = _SwEgressAclIpRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 2, 1, 30),
    _SwEgressAclIpRuleTimeRangeName_Type()
)
swEgressAclIpRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclIpRuleTimeRangeName.setStatus("current")
_SwEgressACLIpv6RuleTable_Object = MibTable
swEgressACLIpv6RuleTable = _SwEgressACLIpv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3)
)
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleTable.setStatus("current")
_SwEgressACLIpv6RuleEntry_Object = MibTableRow
swEgressACLIpv6RuleEntry = _SwEgressACLIpv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1)
)
swEgressACLIpv6RuleEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLIpv6RuleProfileID"),
    (0, "EGRESSACL-MIB", "swEgressACLIpv6RuleAccessID"),
)
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleEntry.setStatus("current")
_SwEgressACLIpv6RuleProfileID_Type = Integer32
_SwEgressACLIpv6RuleProfileID_Object = MibTableColumn
swEgressACLIpv6RuleProfileID = _SwEgressACLIpv6RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 1),
    _SwEgressACLIpv6RuleProfileID_Type()
)
swEgressACLIpv6RuleProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleProfileID.setStatus("current")


class _SwEgressACLIpv6RuleAccessID_Type(Integer32):
    """Custom type swEgressACLIpv6RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwEgressACLIpv6RuleAccessID_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleAccessID_Object = MibTableColumn
swEgressACLIpv6RuleAccessID = _SwEgressACLIpv6RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 2),
    _SwEgressACLIpv6RuleAccessID_Type()
)
swEgressACLIpv6RuleAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleAccessID.setStatus("current")
_SwEgressACLIpv6RuleRowStatus_Type = RowStatus
_SwEgressACLIpv6RuleRowStatus_Object = MibTableColumn
swEgressACLIpv6RuleRowStatus = _SwEgressACLIpv6RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 3),
    _SwEgressACLIpv6RuleRowStatus_Type()
)
swEgressACLIpv6RuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleRowStatus.setStatus("current")


class _SwEgressACLIpv6RuleClass_Type(Integer32):
    """Custom type swEgressACLIpv6RuleClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpv6RuleClass_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleClass_Object = MibTableColumn
swEgressACLIpv6RuleClass = _SwEgressACLIpv6RuleClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 4),
    _SwEgressACLIpv6RuleClass_Type()
)
swEgressACLIpv6RuleClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleClass.setStatus("current")
_SwEgressACLIpv6RuleSrcIpv6Addr_Type = Ipv6Address
_SwEgressACLIpv6RuleSrcIpv6Addr_Object = MibTableColumn
swEgressACLIpv6RuleSrcIpv6Addr = _SwEgressACLIpv6RuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 5),
    _SwEgressACLIpv6RuleSrcIpv6Addr_Type()
)
swEgressACLIpv6RuleSrcIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleSrcIpv6Addr.setStatus("current")
_SwEgressACLIpv6RuleMaskSrcIpv6Addr_Type = Ipv6Address
_SwEgressACLIpv6RuleMaskSrcIpv6Addr_Object = MibTableColumn
swEgressACLIpv6RuleMaskSrcIpv6Addr = _SwEgressACLIpv6RuleMaskSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 6),
    _SwEgressACLIpv6RuleMaskSrcIpv6Addr_Type()
)
swEgressACLIpv6RuleMaskSrcIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleMaskSrcIpv6Addr.setStatus("current")
_SwEgressACLIpv6RuleDstIpv6Addr_Type = Ipv6Address
_SwEgressACLIpv6RuleDstIpv6Addr_Object = MibTableColumn
swEgressACLIpv6RuleDstIpv6Addr = _SwEgressACLIpv6RuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 7),
    _SwEgressACLIpv6RuleDstIpv6Addr_Type()
)
swEgressACLIpv6RuleDstIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleDstIpv6Addr.setStatus("current")
_SwEgressACLIpv6RuleMaskDstIpv6Addr_Type = Ipv6Address
_SwEgressACLIpv6RuleMaskDstIpv6Addr_Object = MibTableColumn
swEgressACLIpv6RuleMaskDstIpv6Addr = _SwEgressACLIpv6RuleMaskDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 8),
    _SwEgressACLIpv6RuleMaskDstIpv6Addr_Type()
)
swEgressACLIpv6RuleMaskDstIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleMaskDstIpv6Addr.setStatus("current")


class _SwEgressACLIpv6RuleProtocol_Type(Integer32):
    """Custom type swEgressACLIpv6RuleProtocol based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4))
    )


_SwEgressACLIpv6RuleProtocol_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleProtocol_Object = MibTableColumn
swEgressACLIpv6RuleProtocol = _SwEgressACLIpv6RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 9),
    _SwEgressACLIpv6RuleProtocol_Type()
)
swEgressACLIpv6RuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleProtocol.setStatus("current")


class _SwEgressACLIpv6RuleType_Type(Integer32):
    """Custom type swEgressACLIpv6RuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpv6RuleType_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleType_Object = MibTableColumn
swEgressACLIpv6RuleType = _SwEgressACLIpv6RuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 10),
    _SwEgressACLIpv6RuleType_Type()
)
swEgressACLIpv6RuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleType.setStatus("current")


class _SwEgressACLIpv6RuleCode_Type(Integer32):
    """Custom type swEgressACLIpv6RuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwEgressACLIpv6RuleCode_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleCode_Object = MibTableColumn
swEgressACLIpv6RuleCode = _SwEgressACLIpv6RuleCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 11),
    _SwEgressACLIpv6RuleCode_Type()
)
swEgressACLIpv6RuleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleCode.setStatus("current")


class _SwEgressACLIpv6RuleSrcPort_Type(Integer32):
    """Custom type swEgressACLIpv6RuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwEgressACLIpv6RuleSrcPort_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleSrcPort_Object = MibTableColumn
swEgressACLIpv6RuleSrcPort = _SwEgressACLIpv6RuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 12),
    _SwEgressACLIpv6RuleSrcPort_Type()
)
swEgressACLIpv6RuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleSrcPort.setStatus("current")


class _SwEgressACLIpv6RuleMaskSrcPort_Type(OctetString):
    """Custom type swEgressACLIpv6RuleMaskSrcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpv6RuleMaskSrcPort_Type.__name__ = "OctetString"
_SwEgressACLIpv6RuleMaskSrcPort_Object = MibTableColumn
swEgressACLIpv6RuleMaskSrcPort = _SwEgressACLIpv6RuleMaskSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 13),
    _SwEgressACLIpv6RuleMaskSrcPort_Type()
)
swEgressACLIpv6RuleMaskSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleMaskSrcPort.setStatus("current")


class _SwEgressACLIpv6RuleDstPort_Type(Integer32):
    """Custom type swEgressACLIpv6RuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwEgressACLIpv6RuleDstPort_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleDstPort_Object = MibTableColumn
swEgressACLIpv6RuleDstPort = _SwEgressACLIpv6RuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 14),
    _SwEgressACLIpv6RuleDstPort_Type()
)
swEgressACLIpv6RuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleDstPort.setStatus("current")


class _SwEgressACLIpv6RuleMaskDstPort_Type(OctetString):
    """Custom type swEgressACLIpv6RuleMaskDstPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwEgressACLIpv6RuleMaskDstPort_Type.__name__ = "OctetString"
_SwEgressACLIpv6RuleMaskDstPort_Object = MibTableColumn
swEgressACLIpv6RuleMaskDstPort = _SwEgressACLIpv6RuleMaskDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 15),
    _SwEgressACLIpv6RuleMaskDstPort_Type()
)
swEgressACLIpv6RuleMaskDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleMaskDstPort.setStatus("current")
_SwEgressACLIpv6RuleVID_Type = VlanIdOrNone
_SwEgressACLIpv6RuleVID_Object = MibTableColumn
swEgressACLIpv6RuleVID = _SwEgressACLIpv6RuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 16),
    _SwEgressACLIpv6RuleVID_Type()
)
swEgressACLIpv6RuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleVID.setStatus("current")
_SwEgressACLIpv6RulePort_Type = Integer32
_SwEgressACLIpv6RulePort_Object = MibTableColumn
swEgressACLIpv6RulePort = _SwEgressACLIpv6RulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 17),
    _SwEgressACLIpv6RulePort_Type()
)
swEgressACLIpv6RulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RulePort.setStatus("current")
_SwEgressACLIpv6RulePortGroup_Type = Integer32
_SwEgressACLIpv6RulePortGroup_Object = MibTableColumn
swEgressACLIpv6RulePortGroup = _SwEgressACLIpv6RulePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 18),
    _SwEgressACLIpv6RulePortGroup_Type()
)
swEgressACLIpv6RulePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RulePortGroup.setStatus("current")


class _SwEgressACLIpv6RulePermit_Type(Integer32):
    """Custom type swEgressACLIpv6RulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwEgressACLIpv6RulePermit_Type.__name__ = "Integer32"
_SwEgressACLIpv6RulePermit_Object = MibTableColumn
swEgressACLIpv6RulePermit = _SwEgressACLIpv6RulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 19),
    _SwEgressACLIpv6RulePermit_Type()
)
swEgressACLIpv6RulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RulePermit.setStatus("current")


class _SwEgressACLIpv6RuleEnableReplacePriority_Type(Integer32):
    """Custom type swEgressACLIpv6RuleEnableReplacePriority based on Integer32"""
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


_SwEgressACLIpv6RuleEnableReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleEnableReplacePriority_Object = MibTableColumn
swEgressACLIpv6RuleEnableReplacePriority = _SwEgressACLIpv6RuleEnableReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 20),
    _SwEgressACLIpv6RuleEnableReplacePriority_Type()
)
swEgressACLIpv6RuleEnableReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleEnableReplacePriority.setStatus("current")


class _SwEgressACLIpv6RuleReplacePriority_Type(Integer32):
    """Custom type swEgressACLIpv6RuleReplacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwEgressACLIpv6RuleReplacePriority_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleReplacePriority_Object = MibTableColumn
swEgressACLIpv6RuleReplacePriority = _SwEgressACLIpv6RuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 21),
    _SwEgressACLIpv6RuleReplacePriority_Type()
)
swEgressACLIpv6RuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleReplacePriority.setStatus("current")


class _SwEgressACLIpv6RuleEnableReplaceDscp_Type(Integer32):
    """Custom type swEgressACLIpv6RuleEnableReplaceDscp based on Integer32"""
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


_SwEgressACLIpv6RuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleEnableReplaceDscp_Object = MibTableColumn
swEgressACLIpv6RuleEnableReplaceDscp = _SwEgressACLIpv6RuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 22),
    _SwEgressACLIpv6RuleEnableReplaceDscp_Type()
)
swEgressACLIpv6RuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleEnableReplaceDscp.setStatus("current")


class _SwEgressACLIpv6RuleReplaceDscp_Type(Integer32):
    """Custom type swEgressACLIpv6RuleReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressACLIpv6RuleReplaceDscp_Type.__name__ = "Integer32"
_SwEgressACLIpv6RuleReplaceDscp_Object = MibTableColumn
swEgressACLIpv6RuleReplaceDscp = _SwEgressACLIpv6RuleReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 23),
    _SwEgressACLIpv6RuleReplaceDscp_Type()
)
swEgressACLIpv6RuleReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressACLIpv6RuleReplaceDscp.setStatus("current")
_SwEgressAclIpv6RuleTimeRangeName_Type = DisplayString
_SwEgressAclIpv6RuleTimeRangeName_Object = MibTableColumn
swEgressAclIpv6RuleTimeRangeName = _SwEgressAclIpv6RuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 3, 1, 24),
    _SwEgressAclIpv6RuleTimeRangeName_Type()
)
swEgressAclIpv6RuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclIpv6RuleTimeRangeName.setStatus("current")
_SwEgressACLCounterTable_Object = MibTable
swEgressACLCounterTable = _SwEgressACLCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4)
)
if mibBuilder.loadTexts:
    swEgressACLCounterTable.setStatus("current")
_SwEgressACLCounterEntry_Object = MibTableRow
swEgressACLCounterEntry = _SwEgressACLCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1)
)
swEgressACLCounterEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressACLCounterProfileID"),
    (0, "EGRESSACL-MIB", "swEgressACLCounterAccessID"),
)
if mibBuilder.loadTexts:
    swEgressACLCounterEntry.setStatus("current")
_SwEgressACLCounterProfileID_Type = Integer32
_SwEgressACLCounterProfileID_Object = MibTableColumn
swEgressACLCounterProfileID = _SwEgressACLCounterProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 1),
    _SwEgressACLCounterProfileID_Type()
)
swEgressACLCounterProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLCounterProfileID.setStatus("current")


class _SwEgressACLCounterAccessID_Type(Integer32):
    """Custom type swEgressACLCounterAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwEgressACLCounterAccessID_Type.__name__ = "Integer32"
_SwEgressACLCounterAccessID_Object = MibTableColumn
swEgressACLCounterAccessID = _SwEgressACLCounterAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 2),
    _SwEgressACLCounterAccessID_Type()
)
swEgressACLCounterAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressACLCounterAccessID.setStatus("current")


class _SwEgressACLCounterState_Type(Integer32):
    """Custom type swEgressACLCounterState based on Integer32"""
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


_SwEgressACLCounterState_Type.__name__ = "Integer32"
_SwEgressACLCounterState_Object = MibTableColumn
swEgressACLCounterState = _SwEgressACLCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 3),
    _SwEgressACLCounterState_Type()
)
swEgressACLCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEgressACLCounterState.setStatus("current")
_SwEgressACLCounterTotalCounter_Type = Counter64
_SwEgressACLCounterTotalCounter_Object = MibTableColumn
swEgressACLCounterTotalCounter = _SwEgressACLCounterTotalCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 4),
    _SwEgressACLCounterTotalCounter_Type()
)
swEgressACLCounterTotalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLCounterTotalCounter.setStatus("current")
_SwEgressACLCounterGreenCounter_Type = Counter64
_SwEgressACLCounterGreenCounter_Object = MibTableColumn
swEgressACLCounterGreenCounter = _SwEgressACLCounterGreenCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 5),
    _SwEgressACLCounterGreenCounter_Type()
)
swEgressACLCounterGreenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLCounterGreenCounter.setStatus("current")
_SwEgressACLCounterYellowCounter_Type = Counter64
_SwEgressACLCounterYellowCounter_Object = MibTableColumn
swEgressACLCounterYellowCounter = _SwEgressACLCounterYellowCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 6),
    _SwEgressACLCounterYellowCounter_Type()
)
swEgressACLCounterYellowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLCounterYellowCounter.setStatus("current")
_SwEgressACLCounterRedCounter_Type = Counter64
_SwEgressACLCounterRedCounter_Object = MibTableColumn
swEgressACLCounterRedCounter = _SwEgressACLCounterRedCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 3, 4, 1, 7),
    _SwEgressACLCounterRedCounter_Type()
)
swEgressACLCounterRedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressACLCounterRedCounter.setStatus("current")
_SwEgressAclMeteringMgmt_ObjectIdentity = ObjectIdentity
swEgressAclMeteringMgmt = _SwEgressAclMeteringMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4)
)
_SwEgressAclMeterTable_Object = MibTable
swEgressAclMeterTable = _SwEgressAclMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1)
)
if mibBuilder.loadTexts:
    swEgressAclMeterTable.setStatus("current")
_SwEgressAclMeterEntry_Object = MibTableRow
swEgressAclMeterEntry = _SwEgressAclMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1)
)
swEgressAclMeterEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressAclMeterProfileID"),
    (0, "EGRESSACL-MIB", "swEgressAclMeterAccessID"),
)
if mibBuilder.loadTexts:
    swEgressAclMeterEntry.setStatus("current")
_SwEgressAclMeterProfileID_Type = Integer32
_SwEgressAclMeterProfileID_Object = MibTableColumn
swEgressAclMeterProfileID = _SwEgressAclMeterProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 1),
    _SwEgressAclMeterProfileID_Type()
)
swEgressAclMeterProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressAclMeterProfileID.setStatus("current")


class _SwEgressAclMeterAccessID_Type(Integer32):
    """Custom type swEgressAclMeterAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwEgressAclMeterAccessID_Type.__name__ = "Integer32"
_SwEgressAclMeterAccessID_Object = MibTableColumn
swEgressAclMeterAccessID = _SwEgressAclMeterAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 2),
    _SwEgressAclMeterAccessID_Type()
)
swEgressAclMeterAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressAclMeterAccessID.setStatus("current")
_SwEgressAclMeterRowStatus_Type = RowStatus
_SwEgressAclMeterRowStatus_Object = MibTableColumn
swEgressAclMeterRowStatus = _SwEgressAclMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 3),
    _SwEgressAclMeterRowStatus_Type()
)
swEgressAclMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterRowStatus.setStatus("current")


class _SwEgressAclMeterMode_Type(Integer32):
    """Custom type swEgressAclMeterMode based on Integer32"""
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
          ("tr-tcm", 2),
          ("sr-tcm", 3))
    )


_SwEgressAclMeterMode_Type.__name__ = "Integer32"
_SwEgressAclMeterMode_Object = MibTableColumn
swEgressAclMeterMode = _SwEgressAclMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 4),
    _SwEgressAclMeterMode_Type()
)
swEgressAclMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterMode.setStatus("current")
_SwEgressAclMeterTrtcmCir_Type = Integer32
_SwEgressAclMeterTrtcmCir_Object = MibTableColumn
swEgressAclMeterTrtcmCir = _SwEgressAclMeterTrtcmCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 5),
    _SwEgressAclMeterTrtcmCir_Type()
)
swEgressAclMeterTrtcmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmCir.setStatus("current")
_SwEgressAclMeterTrtcmCbs_Type = Integer32
_SwEgressAclMeterTrtcmCbs_Object = MibTableColumn
swEgressAclMeterTrtcmCbs = _SwEgressAclMeterTrtcmCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 6),
    _SwEgressAclMeterTrtcmCbs_Type()
)
swEgressAclMeterTrtcmCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmCbs.setStatus("current")
_SwEgressAclMeterTrtcmPir_Type = Integer32
_SwEgressAclMeterTrtcmPir_Object = MibTableColumn
swEgressAclMeterTrtcmPir = _SwEgressAclMeterTrtcmPir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 7),
    _SwEgressAclMeterTrtcmPir_Type()
)
swEgressAclMeterTrtcmPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmPir.setStatus("current")
_SwEgressAclMeterTrtcmPbs_Type = Integer32
_SwEgressAclMeterTrtcmPbs_Object = MibTableColumn
swEgressAclMeterTrtcmPbs = _SwEgressAclMeterTrtcmPbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 8),
    _SwEgressAclMeterTrtcmPbs_Type()
)
swEgressAclMeterTrtcmPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmPbs.setStatus("current")


class _SwEgressAclMeterTrtcmColorMode_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-blind", 1),
          ("color-aware", 2))
    )


_SwEgressAclMeterTrtcmColorMode_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmColorMode_Object = MibTableColumn
swEgressAclMeterTrtcmColorMode = _SwEgressAclMeterTrtcmColorMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 9),
    _SwEgressAclMeterTrtcmColorMode_Type()
)
swEgressAclMeterTrtcmColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmColorMode.setStatus("current")


class _SwEgressAclMeterTrtcmConformState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmConformState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwEgressAclMeterTrtcmConformState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmConformState_Object = MibTableColumn
swEgressAclMeterTrtcmConformState = _SwEgressAclMeterTrtcmConformState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 10),
    _SwEgressAclMeterTrtcmConformState_Type()
)
swEgressAclMeterTrtcmConformState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmConformState.setStatus("current")


class _SwEgressAclMeterTrtcmConformReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmConformReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterTrtcmConformReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmConformReplaceDscp_Object = MibTableColumn
swEgressAclMeterTrtcmConformReplaceDscp = _SwEgressAclMeterTrtcmConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 11),
    _SwEgressAclMeterTrtcmConformReplaceDscp_Type()
)
swEgressAclMeterTrtcmConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmConformReplaceDscp.setStatus("current")


class _SwEgressAclMeterTrtcmConformCounterState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmConformCounterState based on Integer32"""
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


_SwEgressAclMeterTrtcmConformCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmConformCounterState_Object = MibTableColumn
swEgressAclMeterTrtcmConformCounterState = _SwEgressAclMeterTrtcmConformCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 12),
    _SwEgressAclMeterTrtcmConformCounterState_Type()
)
swEgressAclMeterTrtcmConformCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmConformCounterState.setStatus("current")


class _SwEgressAclMeterTrtcmExceedState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmExceedState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3),
          ("drop", 4))
    )


_SwEgressAclMeterTrtcmExceedState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmExceedState_Object = MibTableColumn
swEgressAclMeterTrtcmExceedState = _SwEgressAclMeterTrtcmExceedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 13),
    _SwEgressAclMeterTrtcmExceedState_Type()
)
swEgressAclMeterTrtcmExceedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmExceedState.setStatus("current")


class _SwEgressAclMeterTrtcmExceedReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmExceedReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterTrtcmExceedReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmExceedReplaceDscp_Object = MibTableColumn
swEgressAclMeterTrtcmExceedReplaceDscp = _SwEgressAclMeterTrtcmExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 14),
    _SwEgressAclMeterTrtcmExceedReplaceDscp_Type()
)
swEgressAclMeterTrtcmExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmExceedReplaceDscp.setStatus("current")


class _SwEgressAclMeterTrtcmExceedCounterState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmExceedCounterState based on Integer32"""
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


_SwEgressAclMeterTrtcmExceedCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmExceedCounterState_Object = MibTableColumn
swEgressAclMeterTrtcmExceedCounterState = _SwEgressAclMeterTrtcmExceedCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 15),
    _SwEgressAclMeterTrtcmExceedCounterState_Type()
)
swEgressAclMeterTrtcmExceedCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmExceedCounterState.setStatus("current")


class _SwEgressAclMeterTrtcmViolateState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmViolateState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3),
          ("drop", 4))
    )


_SwEgressAclMeterTrtcmViolateState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmViolateState_Object = MibTableColumn
swEgressAclMeterTrtcmViolateState = _SwEgressAclMeterTrtcmViolateState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 16),
    _SwEgressAclMeterTrtcmViolateState_Type()
)
swEgressAclMeterTrtcmViolateState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmViolateState.setStatus("current")


class _SwEgressAclMeterTrtcmViolateReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmViolateReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterTrtcmViolateReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmViolateReplaceDscp_Object = MibTableColumn
swEgressAclMeterTrtcmViolateReplaceDscp = _SwEgressAclMeterTrtcmViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 17),
    _SwEgressAclMeterTrtcmViolateReplaceDscp_Type()
)
swEgressAclMeterTrtcmViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmViolateReplaceDscp.setStatus("current")


class _SwEgressAclMeterTrtcmViolateCounterState_Type(Integer32):
    """Custom type swEgressAclMeterTrtcmViolateCounterState based on Integer32"""
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


_SwEgressAclMeterTrtcmViolateCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterTrtcmViolateCounterState_Object = MibTableColumn
swEgressAclMeterTrtcmViolateCounterState = _SwEgressAclMeterTrtcmViolateCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 18),
    _SwEgressAclMeterTrtcmViolateCounterState_Type()
)
swEgressAclMeterTrtcmViolateCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterTrtcmViolateCounterState.setStatus("current")
_SwEgressAclMeterSrtcmCir_Type = Integer32
_SwEgressAclMeterSrtcmCir_Object = MibTableColumn
swEgressAclMeterSrtcmCir = _SwEgressAclMeterSrtcmCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 19),
    _SwEgressAclMeterSrtcmCir_Type()
)
swEgressAclMeterSrtcmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmCir.setStatus("current")
_SwEgressAclMeterSrtcmCbs_Type = Integer32
_SwEgressAclMeterSrtcmCbs_Object = MibTableColumn
swEgressAclMeterSrtcmCbs = _SwEgressAclMeterSrtcmCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 20),
    _SwEgressAclMeterSrtcmCbs_Type()
)
swEgressAclMeterSrtcmCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmCbs.setStatus("current")
_SwEgressAclMeterSrtcmEbs_Type = Integer32
_SwEgressAclMeterSrtcmEbs_Object = MibTableColumn
swEgressAclMeterSrtcmEbs = _SwEgressAclMeterSrtcmEbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 21),
    _SwEgressAclMeterSrtcmEbs_Type()
)
swEgressAclMeterSrtcmEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmEbs.setStatus("current")


class _SwEgressAclMeterSrtcmColorMode_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-blind", 1),
          ("color-aware", 2))
    )


_SwEgressAclMeterSrtcmColorMode_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmColorMode_Object = MibTableColumn
swEgressAclMeterSrtcmColorMode = _SwEgressAclMeterSrtcmColorMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 22),
    _SwEgressAclMeterSrtcmColorMode_Type()
)
swEgressAclMeterSrtcmColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmColorMode.setStatus("current")


class _SwEgressAclMeterSrtcmConformState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmConformState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwEgressAclMeterSrtcmConformState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmConformState_Object = MibTableColumn
swEgressAclMeterSrtcmConformState = _SwEgressAclMeterSrtcmConformState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 23),
    _SwEgressAclMeterSrtcmConformState_Type()
)
swEgressAclMeterSrtcmConformState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmConformState.setStatus("current")


class _SwEgressAclMeterSrtcmConformReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmConformReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterSrtcmConformReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmConformReplaceDscp_Object = MibTableColumn
swEgressAclMeterSrtcmConformReplaceDscp = _SwEgressAclMeterSrtcmConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 24),
    _SwEgressAclMeterSrtcmConformReplaceDscp_Type()
)
swEgressAclMeterSrtcmConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmConformReplaceDscp.setStatus("current")


class _SwEgressAclMeterSrtcmConformCounterState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmConformCounterState based on Integer32"""
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


_SwEgressAclMeterSrtcmConformCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmConformCounterState_Object = MibTableColumn
swEgressAclMeterSrtcmConformCounterState = _SwEgressAclMeterSrtcmConformCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 25),
    _SwEgressAclMeterSrtcmConformCounterState_Type()
)
swEgressAclMeterSrtcmConformCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmConformCounterState.setStatus("current")


class _SwEgressAclMeterSrtcmExceedState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmExceedState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3),
          ("drop", 4))
    )


_SwEgressAclMeterSrtcmExceedState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmExceedState_Object = MibTableColumn
swEgressAclMeterSrtcmExceedState = _SwEgressAclMeterSrtcmExceedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 26),
    _SwEgressAclMeterSrtcmExceedState_Type()
)
swEgressAclMeterSrtcmExceedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmExceedState.setStatus("current")


class _SwEgressAclMeterSrtcmExceedReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmExceedReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterSrtcmExceedReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmExceedReplaceDscp_Object = MibTableColumn
swEgressAclMeterSrtcmExceedReplaceDscp = _SwEgressAclMeterSrtcmExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 27),
    _SwEgressAclMeterSrtcmExceedReplaceDscp_Type()
)
swEgressAclMeterSrtcmExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmExceedReplaceDscp.setStatus("current")


class _SwEgressAclMeterSrtcmExceedCounterState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmExceedCounterState based on Integer32"""
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


_SwEgressAclMeterSrtcmExceedCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmExceedCounterState_Object = MibTableColumn
swEgressAclMeterSrtcmExceedCounterState = _SwEgressAclMeterSrtcmExceedCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 28),
    _SwEgressAclMeterSrtcmExceedCounterState_Type()
)
swEgressAclMeterSrtcmExceedCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmExceedCounterState.setStatus("current")


class _SwEgressAclMeterSrtcmViolateState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmViolateState based on Integer32"""
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
          ("permit", 2),
          ("replace-dscp", 3),
          ("drop", 4))
    )


_SwEgressAclMeterSrtcmViolateState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmViolateState_Object = MibTableColumn
swEgressAclMeterSrtcmViolateState = _SwEgressAclMeterSrtcmViolateState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 29),
    _SwEgressAclMeterSrtcmViolateState_Type()
)
swEgressAclMeterSrtcmViolateState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmViolateState.setStatus("current")


class _SwEgressAclMeterSrtcmViolateReplaceDscp_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmViolateReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclMeterSrtcmViolateReplaceDscp_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmViolateReplaceDscp_Object = MibTableColumn
swEgressAclMeterSrtcmViolateReplaceDscp = _SwEgressAclMeterSrtcmViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 30),
    _SwEgressAclMeterSrtcmViolateReplaceDscp_Type()
)
swEgressAclMeterSrtcmViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmViolateReplaceDscp.setStatus("current")


class _SwEgressAclMeterSrtcmViolateCounterState_Type(Integer32):
    """Custom type swEgressAclMeterSrtcmViolateCounterState based on Integer32"""
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


_SwEgressAclMeterSrtcmViolateCounterState_Type.__name__ = "Integer32"
_SwEgressAclMeterSrtcmViolateCounterState_Object = MibTableColumn
swEgressAclMeterSrtcmViolateCounterState = _SwEgressAclMeterSrtcmViolateCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 1, 1, 31),
    _SwEgressAclMeterSrtcmViolateCounterState_Type()
)
swEgressAclMeterSrtcmViolateCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclMeterSrtcmViolateCounterState.setStatus("current")
_SwEgressAclRateTable_Object = MibTable
swEgressAclRateTable = _SwEgressAclRateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2)
)
if mibBuilder.loadTexts:
    swEgressAclRateTable.setStatus("current")
_SwEgressAclRateEntry_Object = MibTableRow
swEgressAclRateEntry = _SwEgressAclRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1)
)
swEgressAclRateEntry.setIndexNames(
    (0, "EGRESSACL-MIB", "swEgressAclRateProfileID"),
    (0, "EGRESSACL-MIB", "swEgressAclRateAccessID"),
)
if mibBuilder.loadTexts:
    swEgressAclRateEntry.setStatus("current")
_SwEgressAclRateProfileID_Type = Integer32
_SwEgressAclRateProfileID_Object = MibTableColumn
swEgressAclRateProfileID = _SwEgressAclRateProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 1),
    _SwEgressAclRateProfileID_Type()
)
swEgressAclRateProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressAclRateProfileID.setStatus("current")


class _SwEgressAclRateAccessID_Type(Integer32):
    """Custom type swEgressAclRateAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwEgressAclRateAccessID_Type.__name__ = "Integer32"
_SwEgressAclRateAccessID_Object = MibTableColumn
swEgressAclRateAccessID = _SwEgressAclRateAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 2),
    _SwEgressAclRateAccessID_Type()
)
swEgressAclRateAccessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEgressAclRateAccessID.setStatus("current")
_SwEgressAclRateRowStatus_Type = RowStatus
_SwEgressAclRateRowStatus_Object = MibTableColumn
swEgressAclRateRowStatus = _SwEgressAclRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 3),
    _SwEgressAclRateRowStatus_Type()
)
swEgressAclRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclRateRowStatus.setStatus("current")
_SwEgressAclRate_Type = Integer32
_SwEgressAclRate_Object = MibTableColumn
swEgressAclRate = _SwEgressAclRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 4),
    _SwEgressAclRate_Type()
)
swEgressAclRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclRate.setStatus("current")
_SwEgressAclBurstSize_Type = Integer32
_SwEgressAclBurstSize_Object = MibTableColumn
swEgressAclBurstSize = _SwEgressAclBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 5),
    _SwEgressAclBurstSize_Type()
)
swEgressAclBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclBurstSize.setStatus("current")


class _SwEgressAclRateActionForRateExceed_Type(Integer32):
    """Custom type swEgressAclRateActionForRateExceed based on Integer32"""
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
          ("drop-packet", 2),
          ("remark-dscp", 3))
    )


_SwEgressAclRateActionForRateExceed_Type.__name__ = "Integer32"
_SwEgressAclRateActionForRateExceed_Object = MibTableColumn
swEgressAclRateActionForRateExceed = _SwEgressAclRateActionForRateExceed_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 6),
    _SwEgressAclRateActionForRateExceed_Type()
)
swEgressAclRateActionForRateExceed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclRateActionForRateExceed.setStatus("current")


class _SwEgressAclRateRemarkDscp_Type(Integer32):
    """Custom type swEgressAclRateRemarkDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwEgressAclRateRemarkDscp_Type.__name__ = "Integer32"
_SwEgressAclRateRemarkDscp_Object = MibTableColumn
swEgressAclRateRemarkDscp = _SwEgressAclRateRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 2, 1, 7),
    _SwEgressAclRateRemarkDscp_Type()
)
swEgressAclRateRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEgressAclRateRemarkDscp.setStatus("current")
_SwEgressAclMeteringNumOfEntryInUse_Type = Integer32
_SwEgressAclMeteringNumOfEntryInUse_Object = MibScalar
swEgressAclMeteringNumOfEntryInUse = _SwEgressAclMeteringNumOfEntryInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 89, 4, 3),
    _SwEgressAclMeteringNumOfEntryInUse_Type()
)
swEgressAclMeteringNumOfEntryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEgressAclMeteringNumOfEntryInUse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EGRESSACL-MIB",
    **{"swEgressAclMgmtMIB": swEgressAclMgmtMIB,
       "swEgressAclInfo": swEgressAclInfo,
       "swEgressACLTotalUsedRuleEntries": swEgressACLTotalUsedRuleEntries,
       "swEgressACLTotalUnusedRuleEntries": swEgressACLTotalUnusedRuleEntries,
       "swEgressAclMaskMgmt": swEgressAclMaskMgmt,
       "swEgressACLEthernetTable": swEgressACLEthernetTable,
       "swEgressACLEthernetEntry": swEgressACLEthernetEntry,
       "swEgressACLEthernetProfileID": swEgressACLEthernetProfileID,
       "swEgressACLEthernetRowStatus": swEgressACLEthernetRowStatus,
       "swEgressACLEthernetProfileName": swEgressACLEthernetProfileName,
       "swEgressACLEthernetUsevlan": swEgressACLEthernetUsevlan,
       "swEgressACLEthernetVlanMask": swEgressACLEthernetVlanMask,
       "swEgressACLEthernetUse8021p": swEgressACLEthernetUse8021p,
       "swEgressACLEthernetUseEthernetType": swEgressACLEthernetUseEthernetType,
       "swEgressACLEthernetMacAddrMaskState": swEgressACLEthernetMacAddrMaskState,
       "swEgressACLEthernetSrcMacAddrMask": swEgressACLEthernetSrcMacAddrMask,
       "swEgressACLEthernetDstMacAddrMask": swEgressACLEthernetDstMacAddrMask,
       "swEgressACLEthernetUnusedRuleEntries": swEgressACLEthernetUnusedRuleEntries,
       "swEgressACLIpTable": swEgressACLIpTable,
       "swEgressACLIpEntry": swEgressACLIpEntry,
       "swEgressACLIpProfileID": swEgressACLIpProfileID,
       "swEgressACLIpRowStatus": swEgressACLIpRowStatus,
       "swEgressACLIpProfileName": swEgressACLIpProfileName,
       "swEgressACLIpUsevlan": swEgressACLIpUsevlan,
       "swEgressACLIpVlanMask": swEgressACLIpVlanMask,
       "swEgressACLIpIpAddrMaskState": swEgressACLIpIpAddrMaskState,
       "swEgressACLIpSrcIpAddrMask": swEgressACLIpSrcIpAddrMask,
       "swEgressACLIpDstIpAddrMask": swEgressACLIpDstIpAddrMask,
       "swEgressACLIpUseDSCP": swEgressACLIpUseDSCP,
       "swEgressACLIpUseProtoType": swEgressACLIpUseProtoType,
       "swEgressACLIpIcmpOption": swEgressACLIpIcmpOption,
       "swEgressACLIpIgmpOption": swEgressACLIpIgmpOption,
       "swEgressACLIpTcpOption": swEgressACLIpTcpOption,
       "swEgressACLIpUdpOption": swEgressACLIpUdpOption,
       "swEgressACLIpTCPorUDPSrcPortMask": swEgressACLIpTCPorUDPSrcPortMask,
       "swEgressACLIpTCPorUDPDstPortMask": swEgressACLIpTCPorUDPDstPortMask,
       "swEgressACLIpTCPFlagBit": swEgressACLIpTCPFlagBit,
       "swEgressACLIpTCPFlagBitMask": swEgressACLIpTCPFlagBitMask,
       "swEgressACLIpProtoIDOption": swEgressACLIpProtoIDOption,
       "swEgressACLIpProtoID": swEgressACLIpProtoID,
       "swEgressACLIpProtoIDMask": swEgressACLIpProtoIDMask,
       "swEgressACLIpUnusedRuleEntries": swEgressACLIpUnusedRuleEntries,
       "swEgressACLIpv6MaskTable": swEgressACLIpv6MaskTable,
       "swEgressACLIpv6MaskEntry": swEgressACLIpv6MaskEntry,
       "swEgressACLIpv6MaskProfileID": swEgressACLIpv6MaskProfileID,
       "swEgressACLIpv6MaskRowStatus": swEgressACLIpv6MaskRowStatus,
       "swEgressACLIpv6MaskProfileName": swEgressACLIpv6MaskProfileName,
       "swEgressACLIpv6MaskClass": swEgressACLIpv6MaskClass,
       "swEgressACLIpv6IpAddrMaskState": swEgressACLIpv6IpAddrMaskState,
       "swEgressACLIpv6MaskSrcIpv6Mask": swEgressACLIpv6MaskSrcIpv6Mask,
       "swEgressACLIpv6MaskDstIpv6Mask": swEgressACLIpv6MaskDstIpv6Mask,
       "swEgressACLIpv6MaskUseProtoType": swEgressACLIpv6MaskUseProtoType,
       "swEgressACLIpv6MaskIcmpOption": swEgressACLIpv6MaskIcmpOption,
       "swEgressACLIpv6MaskTcpOption": swEgressACLIpv6MaskTcpOption,
       "swEgressACLIpv6MaskUdpOption": swEgressACLIpv6MaskUdpOption,
       "swEgressACLIpv6MaskTCPorUDPSrcPortMask": swEgressACLIpv6MaskTCPorUDPSrcPortMask,
       "swEgressACLIpv6MaskTCPorUDPDstPortMask": swEgressACLIpv6MaskTCPorUDPDstPortMask,
       "swEgressACLIpv6MaskUnusedRuleEntries": swEgressACLIpv6MaskUnusedRuleEntries,
       "swEgressACLMaskDelAllState": swEgressACLMaskDelAllState,
       "swEgressAclRuleMgmt": swEgressAclRuleMgmt,
       "swEgressACLEtherRuleTable": swEgressACLEtherRuleTable,
       "swEgressACLEtherRuleEntry": swEgressACLEtherRuleEntry,
       "swEgressACLEtherRuleProfileID": swEgressACLEtherRuleProfileID,
       "swEgressACLEtherRuleAccessID": swEgressACLEtherRuleAccessID,
       "swEgressACLEtherRuleRowStatus": swEgressACLEtherRuleRowStatus,
       "swEgressACLEtherRuleMatchVID": swEgressACLEtherRuleMatchVID,
       "swEgressACLEtherRuleMatchVlanMask": swEgressACLEtherRuleMatchVlanMask,
       "swEgressACLEtherRuleSrcMacAddress": swEgressACLEtherRuleSrcMacAddress,
       "swEgressACLEtherRuleMaskSrcMacAddress": swEgressACLEtherRuleMaskSrcMacAddress,
       "swEgressACLEtherRuleDstMacAddress": swEgressACLEtherRuleDstMacAddress,
       "swEgressACLEtherRuleMaskDstMacAddress": swEgressACLEtherRuleMaskDstMacAddress,
       "swEgressACLEtherRule8021P": swEgressACLEtherRule8021P,
       "swEgressACLEtherRuleEtherType": swEgressACLEtherRuleEtherType,
       "swEgressACLEtherRuleVID": swEgressACLEtherRuleVID,
       "swEgressACLEtherRulePort": swEgressACLEtherRulePort,
       "swEgressACLEtherRulePortGroup": swEgressACLEtherRulePortGroup,
       "swEgressACLEtherRulePermit": swEgressACLEtherRulePermit,
       "swEgressACLEtherRuleEnableReplacePriority": swEgressACLEtherRuleEnableReplacePriority,
       "swEgressACLEtherRuleReplacePriority": swEgressACLEtherRuleReplacePriority,
       "swEgressACLEtherRuleEnableReplaceDscp": swEgressACLEtherRuleEnableReplaceDscp,
       "swEgressACLEtherRuleReplaceDscp": swEgressACLEtherRuleReplaceDscp,
       "swEgressAclEtherRuleTimeRangeName": swEgressAclEtherRuleTimeRangeName,
       "swEgressACLIpRuleTable": swEgressACLIpRuleTable,
       "swEgressACLIpRuleEntry": swEgressACLIpRuleEntry,
       "swEgressACLIpRuleProfileID": swEgressACLIpRuleProfileID,
       "swEgressACLIpRuleAccessID": swEgressACLIpRuleAccessID,
       "swEgressACLIpRuleRowStatus": swEgressACLIpRuleRowStatus,
       "swEgressACLIpRuleMatchVID": swEgressACLIpRuleMatchVID,
       "swEgressACLIpMatchVlanMask": swEgressACLIpMatchVlanMask,
       "swEgressACLIpRuleSrcIpaddress": swEgressACLIpRuleSrcIpaddress,
       "swEgressACLIpRuleMaskSrcIpaddress": swEgressACLIpRuleMaskSrcIpaddress,
       "swEgressACLIpRuleDstIpaddress": swEgressACLIpRuleDstIpaddress,
       "swEgressACLIpRuleMaskDstIpaddress": swEgressACLIpRuleMaskDstIpaddress,
       "swEgressACLIpRuleDscp": swEgressACLIpRuleDscp,
       "swEgressACLIpRuleProtocol": swEgressACLIpRuleProtocol,
       "swEgressACLIpRuleType": swEgressACLIpRuleType,
       "swEgressACLIpRuleCode": swEgressACLIpRuleCode,
       "swEgressACLIpRuleSrcPort": swEgressACLIpRuleSrcPort,
       "swEgressACLIpRuleMaskSrcPort": swEgressACLIpRuleMaskSrcPort,
       "swEgressACLIpRuleDstPort": swEgressACLIpRuleDstPort,
       "swEgressACLIpRuleMaskDstPort": swEgressACLIpRuleMaskDstPort,
       "swEgressACLIpRuleFlagBits": swEgressACLIpRuleFlagBits,
       "swEgressACLIpRuleProtoID": swEgressACLIpRuleProtoID,
       "swEgressACLIpRuleUserDefine": swEgressACLIpRuleUserDefine,
       "swEgressACLIpRuleUserDefineMask": swEgressACLIpRuleUserDefineMask,
       "swEgressACLIpRuleVID": swEgressACLIpRuleVID,
       "swEgressACLIpRulePort": swEgressACLIpRulePort,
       "swEgressACLIpRulePortGroup": swEgressACLIpRulePortGroup,
       "swEgressACLIpRulePermit": swEgressACLIpRulePermit,
       "swEgressACLIpRuleEnableReplacePriority": swEgressACLIpRuleEnableReplacePriority,
       "swEgressACLIpRuleReplacePriority": swEgressACLIpRuleReplacePriority,
       "swEgressACLIpRuleEnableReplaceDscp": swEgressACLIpRuleEnableReplaceDscp,
       "swEgressACLIpRuleReplaceDscp": swEgressACLIpRuleReplaceDscp,
       "swEgressAclIpRuleTimeRangeName": swEgressAclIpRuleTimeRangeName,
       "swEgressACLIpv6RuleTable": swEgressACLIpv6RuleTable,
       "swEgressACLIpv6RuleEntry": swEgressACLIpv6RuleEntry,
       "swEgressACLIpv6RuleProfileID": swEgressACLIpv6RuleProfileID,
       "swEgressACLIpv6RuleAccessID": swEgressACLIpv6RuleAccessID,
       "swEgressACLIpv6RuleRowStatus": swEgressACLIpv6RuleRowStatus,
       "swEgressACLIpv6RuleClass": swEgressACLIpv6RuleClass,
       "swEgressACLIpv6RuleSrcIpv6Addr": swEgressACLIpv6RuleSrcIpv6Addr,
       "swEgressACLIpv6RuleMaskSrcIpv6Addr": swEgressACLIpv6RuleMaskSrcIpv6Addr,
       "swEgressACLIpv6RuleDstIpv6Addr": swEgressACLIpv6RuleDstIpv6Addr,
       "swEgressACLIpv6RuleMaskDstIpv6Addr": swEgressACLIpv6RuleMaskDstIpv6Addr,
       "swEgressACLIpv6RuleProtocol": swEgressACLIpv6RuleProtocol,
       "swEgressACLIpv6RuleType": swEgressACLIpv6RuleType,
       "swEgressACLIpv6RuleCode": swEgressACLIpv6RuleCode,
       "swEgressACLIpv6RuleSrcPort": swEgressACLIpv6RuleSrcPort,
       "swEgressACLIpv6RuleMaskSrcPort": swEgressACLIpv6RuleMaskSrcPort,
       "swEgressACLIpv6RuleDstPort": swEgressACLIpv6RuleDstPort,
       "swEgressACLIpv6RuleMaskDstPort": swEgressACLIpv6RuleMaskDstPort,
       "swEgressACLIpv6RuleVID": swEgressACLIpv6RuleVID,
       "swEgressACLIpv6RulePort": swEgressACLIpv6RulePort,
       "swEgressACLIpv6RulePortGroup": swEgressACLIpv6RulePortGroup,
       "swEgressACLIpv6RulePermit": swEgressACLIpv6RulePermit,
       "swEgressACLIpv6RuleEnableReplacePriority": swEgressACLIpv6RuleEnableReplacePriority,
       "swEgressACLIpv6RuleReplacePriority": swEgressACLIpv6RuleReplacePriority,
       "swEgressACLIpv6RuleEnableReplaceDscp": swEgressACLIpv6RuleEnableReplaceDscp,
       "swEgressACLIpv6RuleReplaceDscp": swEgressACLIpv6RuleReplaceDscp,
       "swEgressAclIpv6RuleTimeRangeName": swEgressAclIpv6RuleTimeRangeName,
       "swEgressACLCounterTable": swEgressACLCounterTable,
       "swEgressACLCounterEntry": swEgressACLCounterEntry,
       "swEgressACLCounterProfileID": swEgressACLCounterProfileID,
       "swEgressACLCounterAccessID": swEgressACLCounterAccessID,
       "swEgressACLCounterState": swEgressACLCounterState,
       "swEgressACLCounterTotalCounter": swEgressACLCounterTotalCounter,
       "swEgressACLCounterGreenCounter": swEgressACLCounterGreenCounter,
       "swEgressACLCounterYellowCounter": swEgressACLCounterYellowCounter,
       "swEgressACLCounterRedCounter": swEgressACLCounterRedCounter,
       "swEgressAclMeteringMgmt": swEgressAclMeteringMgmt,
       "swEgressAclMeterTable": swEgressAclMeterTable,
       "swEgressAclMeterEntry": swEgressAclMeterEntry,
       "swEgressAclMeterProfileID": swEgressAclMeterProfileID,
       "swEgressAclMeterAccessID": swEgressAclMeterAccessID,
       "swEgressAclMeterRowStatus": swEgressAclMeterRowStatus,
       "swEgressAclMeterMode": swEgressAclMeterMode,
       "swEgressAclMeterTrtcmCir": swEgressAclMeterTrtcmCir,
       "swEgressAclMeterTrtcmCbs": swEgressAclMeterTrtcmCbs,
       "swEgressAclMeterTrtcmPir": swEgressAclMeterTrtcmPir,
       "swEgressAclMeterTrtcmPbs": swEgressAclMeterTrtcmPbs,
       "swEgressAclMeterTrtcmColorMode": swEgressAclMeterTrtcmColorMode,
       "swEgressAclMeterTrtcmConformState": swEgressAclMeterTrtcmConformState,
       "swEgressAclMeterTrtcmConformReplaceDscp": swEgressAclMeterTrtcmConformReplaceDscp,
       "swEgressAclMeterTrtcmConformCounterState": swEgressAclMeterTrtcmConformCounterState,
       "swEgressAclMeterTrtcmExceedState": swEgressAclMeterTrtcmExceedState,
       "swEgressAclMeterTrtcmExceedReplaceDscp": swEgressAclMeterTrtcmExceedReplaceDscp,
       "swEgressAclMeterTrtcmExceedCounterState": swEgressAclMeterTrtcmExceedCounterState,
       "swEgressAclMeterTrtcmViolateState": swEgressAclMeterTrtcmViolateState,
       "swEgressAclMeterTrtcmViolateReplaceDscp": swEgressAclMeterTrtcmViolateReplaceDscp,
       "swEgressAclMeterTrtcmViolateCounterState": swEgressAclMeterTrtcmViolateCounterState,
       "swEgressAclMeterSrtcmCir": swEgressAclMeterSrtcmCir,
       "swEgressAclMeterSrtcmCbs": swEgressAclMeterSrtcmCbs,
       "swEgressAclMeterSrtcmEbs": swEgressAclMeterSrtcmEbs,
       "swEgressAclMeterSrtcmColorMode": swEgressAclMeterSrtcmColorMode,
       "swEgressAclMeterSrtcmConformState": swEgressAclMeterSrtcmConformState,
       "swEgressAclMeterSrtcmConformReplaceDscp": swEgressAclMeterSrtcmConformReplaceDscp,
       "swEgressAclMeterSrtcmConformCounterState": swEgressAclMeterSrtcmConformCounterState,
       "swEgressAclMeterSrtcmExceedState": swEgressAclMeterSrtcmExceedState,
       "swEgressAclMeterSrtcmExceedReplaceDscp": swEgressAclMeterSrtcmExceedReplaceDscp,
       "swEgressAclMeterSrtcmExceedCounterState": swEgressAclMeterSrtcmExceedCounterState,
       "swEgressAclMeterSrtcmViolateState": swEgressAclMeterSrtcmViolateState,
       "swEgressAclMeterSrtcmViolateReplaceDscp": swEgressAclMeterSrtcmViolateReplaceDscp,
       "swEgressAclMeterSrtcmViolateCounterState": swEgressAclMeterSrtcmViolateCounterState,
       "swEgressAclRateTable": swEgressAclRateTable,
       "swEgressAclRateEntry": swEgressAclRateEntry,
       "swEgressAclRateProfileID": swEgressAclRateProfileID,
       "swEgressAclRateAccessID": swEgressAclRateAccessID,
       "swEgressAclRateRowStatus": swEgressAclRateRowStatus,
       "swEgressAclRate": swEgressAclRate,
       "swEgressAclBurstSize": swEgressAclBurstSize,
       "swEgressAclRateActionForRateExceed": swEgressAclRateActionForRateExceed,
       "swEgressAclRateRemarkDscp": swEgressAclRateRemarkDscp,
       "swEgressAclMeteringNumOfEntryInUse": swEgressAclMeteringNumOfEntryInUse}
)
