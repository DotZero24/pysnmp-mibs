# SNMP MIB module (RUCKUS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/RUCKUS-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:04 2025
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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


# MODULE-IDENTITY

ruckusAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45)
)
if mibBuilder.loadTexts:
    ruckusAclMIB.setRevisions(
        ("2019-08-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class AclName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class AclPolicyName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class AclType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )



class AclAction(TextualConvention, Integer32):
    status = "current"
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



class AclDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )



class AclOperator(TextualConvention, Integer32):
    status = "current"
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
        *(("eq", 1),
          ("neq", 2),
          ("lt", 3),
          ("gt", 4),
          ("range", 5),
          ("none", 6))
    )



class IpPrecedence(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("routine", 1),
          ("priority", 2),
          ("immediate", 3),
          ("flash", 4),
          ("flashOverride", 5),
          ("critical", 6),
          ("internet", 7),
          ("network", 8),
          ("other", 9))
    )



class IpTos(TextualConvention, Integer32):
    status = "current"
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
        *(("normal", 1),
          ("lowCost", 2),
          ("maxReliability", 3),
          ("maxThroughput", 4),
          ("minDelay", 5))
    )



class EtherType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_RuckusAclNotify_ObjectIdentity = ObjectIdentity
ruckusAclNotify = _RuckusAclNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 0)
)
_RuckusAclObjects_ObjectIdentity = ObjectIdentity
ruckusAclObjects = _RuckusAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1)
)
_RuckusAcls_ObjectIdentity = ObjectIdentity
ruckusAcls = _RuckusAcls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1)
)
_RuckusAclTable_Object = MibTable
ruckusAclTable = _RuckusAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusAclTable.setStatus("current")
_RuckusAclEntry_Object = MibTableRow
ruckusAclEntry = _RuckusAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1)
)
ruckusAclEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclType"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclName"),
)
if mibBuilder.loadTexts:
    ruckusAclEntry.setStatus("current")
_RuckusAclType_Type = AclType
_RuckusAclType_Object = MibTableColumn
ruckusAclType = _RuckusAclType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1, 1),
    _RuckusAclType_Type()
)
ruckusAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclType.setStatus("current")
_RuckusAclName_Type = AclName
_RuckusAclName_Object = MibTableColumn
ruckusAclName = _RuckusAclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1, 2),
    _RuckusAclName_Type()
)
ruckusAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclName.setStatus("current")
_RuckusAclAcctEnable_Type = TruthValue
_RuckusAclAcctEnable_Object = MibTableColumn
ruckusAclAcctEnable = _RuckusAclAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1, 3),
    _RuckusAclAcctEnable_Type()
)
ruckusAclAcctEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclAcctEnable.setStatus("current")
_RuckusAclStandard_Type = TruthValue
_RuckusAclStandard_Object = MibTableColumn
ruckusAclStandard = _RuckusAclStandard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1, 4),
    _RuckusAclStandard_Type()
)
ruckusAclStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAclStandard.setStatus("current")
_RuckusAclRowStatus_Type = RowStatus
_RuckusAclRowStatus_Object = MibTableColumn
ruckusAclRowStatus = _RuckusAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 1, 1, 1, 5),
    _RuckusAclRowStatus_Type()
)
ruckusAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclRowStatus.setStatus("current")
_RuckusAclFilters_ObjectIdentity = ObjectIdentity
ruckusAclFilters = _RuckusAclFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2)
)
_RuckusIpv4Filters_ObjectIdentity = ObjectIdentity
ruckusIpv4Filters = _RuckusIpv4Filters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1)
)
_RuckusIpv4AclFilterTable_Object = MibTable
ruckusIpv4AclFilterTable = _RuckusIpv4AclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterTable.setStatus("current")
_RuckusIpv4AclFilterEntry_Object = MibTableRow
ruckusIpv4AclFilterEntry = _RuckusIpv4AclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1)
)
ruckusIpv4AclFilterEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclName"),
    (0, "RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSeqNum"),
)
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterEntry.setStatus("current")
_RuckusIpv4AclFilterSeqNum_Type = Unsigned32
_RuckusIpv4AclFilterSeqNum_Object = MibTableColumn
ruckusIpv4AclFilterSeqNum = _RuckusIpv4AclFilterSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 1),
    _RuckusIpv4AclFilterSeqNum_Type()
)
ruckusIpv4AclFilterSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSeqNum.setStatus("current")
_RuckusIpv4AclFilterAction_Type = AclAction
_RuckusIpv4AclFilterAction_Object = MibTableColumn
ruckusIpv4AclFilterAction = _RuckusIpv4AclFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 2),
    _RuckusIpv4AclFilterAction_Type()
)
ruckusIpv4AclFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterAction.setStatus("current")


class _RuckusIpv4AclFilterStdProtocol_Type(Integer32):
    """Custom type ruckusIpv4AclFilterStdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              41,
              46,
              47,
              50,
              89,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("tcp", 6),
          ("udp", 17),
          ("ip6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ospf", 89),
          ("pim", 103),
          ("extended", 255))
    )


_RuckusIpv4AclFilterStdProtocol_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterStdProtocol_Object = MibTableColumn
ruckusIpv4AclFilterStdProtocol = _RuckusIpv4AclFilterStdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 3),
    _RuckusIpv4AclFilterStdProtocol_Type()
)
ruckusIpv4AclFilterStdProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterStdProtocol.setStatus("current")


class _RuckusIpv4AclFilterExtProtocol_Type(Integer32):
    """Custom type ruckusIpv4AclFilterExtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv4AclFilterExtProtocol_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterExtProtocol_Object = MibTableColumn
ruckusIpv4AclFilterExtProtocol = _RuckusIpv4AclFilterExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 4),
    _RuckusIpv4AclFilterExtProtocol_Type()
)
ruckusIpv4AclFilterExtProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterExtProtocol.setStatus("current")
_RuckusIpv4AclFilterSrcAddr_Type = InetAddressIPv4
_RuckusIpv4AclFilterSrcAddr_Object = MibTableColumn
ruckusIpv4AclFilterSrcAddr = _RuckusIpv4AclFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 5),
    _RuckusIpv4AclFilterSrcAddr_Type()
)
ruckusIpv4AclFilterSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSrcAddr.setStatus("current")
_RuckusIpv4AclFilterSrcMask_Type = InetAddressIPv4
_RuckusIpv4AclFilterSrcMask_Object = MibTableColumn
ruckusIpv4AclFilterSrcMask = _RuckusIpv4AclFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 6),
    _RuckusIpv4AclFilterSrcMask_Type()
)
ruckusIpv4AclFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSrcMask.setStatus("current")
_RuckusIpv4AclFilterSrcOperator_Type = AclOperator
_RuckusIpv4AclFilterSrcOperator_Object = MibTableColumn
ruckusIpv4AclFilterSrcOperator = _RuckusIpv4AclFilterSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 7),
    _RuckusIpv4AclFilterSrcOperator_Type()
)
ruckusIpv4AclFilterSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSrcOperator.setStatus("current")


class _RuckusIpv4AclFilterSrcPortLow_Type(Unsigned32):
    """Custom type ruckusIpv4AclFilterSrcPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv4AclFilterSrcPortLow_Type.__name__ = "Unsigned32"
_RuckusIpv4AclFilterSrcPortLow_Object = MibTableColumn
ruckusIpv4AclFilterSrcPortLow = _RuckusIpv4AclFilterSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 8),
    _RuckusIpv4AclFilterSrcPortLow_Type()
)
ruckusIpv4AclFilterSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSrcPortLow.setStatus("current")


class _RuckusIpv4AclFilterSrcPortHigh_Type(Unsigned32):
    """Custom type ruckusIpv4AclFilterSrcPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv4AclFilterSrcPortHigh_Type.__name__ = "Unsigned32"
_RuckusIpv4AclFilterSrcPortHigh_Object = MibTableColumn
ruckusIpv4AclFilterSrcPortHigh = _RuckusIpv4AclFilterSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 9),
    _RuckusIpv4AclFilterSrcPortHigh_Type()
)
ruckusIpv4AclFilterSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterSrcPortHigh.setStatus("current")
_RuckusIpv4AclFilterDestAddr_Type = InetAddressIPv4
_RuckusIpv4AclFilterDestAddr_Object = MibTableColumn
ruckusIpv4AclFilterDestAddr = _RuckusIpv4AclFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 10),
    _RuckusIpv4AclFilterDestAddr_Type()
)
ruckusIpv4AclFilterDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDestAddr.setStatus("current")
_RuckusIpv4AclFilterDestMask_Type = InetAddressIPv4
_RuckusIpv4AclFilterDestMask_Object = MibTableColumn
ruckusIpv4AclFilterDestMask = _RuckusIpv4AclFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 11),
    _RuckusIpv4AclFilterDestMask_Type()
)
ruckusIpv4AclFilterDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDestMask.setStatus("current")
_RuckusIpv4AclFilterDestOperator_Type = AclOperator
_RuckusIpv4AclFilterDestOperator_Object = MibTableColumn
ruckusIpv4AclFilterDestOperator = _RuckusIpv4AclFilterDestOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 12),
    _RuckusIpv4AclFilterDestOperator_Type()
)
ruckusIpv4AclFilterDestOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDestOperator.setStatus("current")


class _RuckusIpv4AclFilterDestPortLow_Type(Unsigned32):
    """Custom type ruckusIpv4AclFilterDestPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv4AclFilterDestPortLow_Type.__name__ = "Unsigned32"
_RuckusIpv4AclFilterDestPortLow_Object = MibTableColumn
ruckusIpv4AclFilterDestPortLow = _RuckusIpv4AclFilterDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 13),
    _RuckusIpv4AclFilterDestPortLow_Type()
)
ruckusIpv4AclFilterDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDestPortLow.setStatus("current")


class _RuckusIpv4AclFilterDestPortHigh_Type(Unsigned32):
    """Custom type ruckusIpv4AclFilterDestPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv4AclFilterDestPortHigh_Type.__name__ = "Unsigned32"
_RuckusIpv4AclFilterDestPortHigh_Object = MibTableColumn
ruckusIpv4AclFilterDestPortHigh = _RuckusIpv4AclFilterDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 14),
    _RuckusIpv4AclFilterDestPortHigh_Type()
)
ruckusIpv4AclFilterDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDestPortHigh.setStatus("current")
_RuckusIpv4AclFilterEstablished_Type = TruthValue
_RuckusIpv4AclFilterEstablished_Object = MibTableColumn
ruckusIpv4AclFilterEstablished = _RuckusIpv4AclFilterEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 15),
    _RuckusIpv4AclFilterEstablished_Type()
)
ruckusIpv4AclFilterEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterEstablished.setStatus("current")
_RuckusIpv4AclFilterPrecedence_Type = IpPrecedence
_RuckusIpv4AclFilterPrecedence_Object = MibTableColumn
ruckusIpv4AclFilterPrecedence = _RuckusIpv4AclFilterPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 16),
    _RuckusIpv4AclFilterPrecedence_Type()
)
ruckusIpv4AclFilterPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterPrecedence.setStatus("current")
_RuckusIpv4AclFilterTos_Type = IpTos
_RuckusIpv4AclFilterTos_Object = MibTableColumn
ruckusIpv4AclFilterTos = _RuckusIpv4AclFilterTos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 17),
    _RuckusIpv4AclFilterTos_Type()
)
ruckusIpv4AclFilterTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterTos.setStatus("current")


class _RuckusIpv4AclFilterIcmpType_Type(Integer32):
    """Custom type ruckusIpv4AclFilterIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              255)
        )
    )
    namedValues = NamedValues(
        *(("echoReply", 0),
          ("destUnreachable", 3),
          ("srcQuench", 4),
          ("redirect", 5),
          ("echoReq", 8),
          ("routerAdv", 9),
          ("routerSolicit", 10),
          ("timeExceed", 11),
          ("paramProblem", 12),
          ("timestampReq", 13),
          ("timestampReply", 14),
          ("infoReq", 15),
          ("infoReply", 16),
          ("addrMaskReq", 17),
          ("addrMaskReply", 18),
          ("extended", 255))
    )


_RuckusIpv4AclFilterIcmpType_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterIcmpType_Object = MibTableColumn
ruckusIpv4AclFilterIcmpType = _RuckusIpv4AclFilterIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 18),
    _RuckusIpv4AclFilterIcmpType_Type()
)
ruckusIpv4AclFilterIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterIcmpType.setStatus("current")


class _RuckusIpv4AclFilterIcmpCode_Type(Integer32):
    """Custom type ruckusIpv4AclFilterIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv4AclFilterIcmpCode_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterIcmpCode_Object = MibTableColumn
ruckusIpv4AclFilterIcmpCode = _RuckusIpv4AclFilterIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 19),
    _RuckusIpv4AclFilterIcmpCode_Type()
)
ruckusIpv4AclFilterIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterIcmpCode.setStatus("current")


class _RuckusIpv4AclFilterExtIcmpType_Type(Integer32):
    """Custom type ruckusIpv4AclFilterExtIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv4AclFilterExtIcmpType_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterExtIcmpType_Object = MibTableColumn
ruckusIpv4AclFilterExtIcmpType = _RuckusIpv4AclFilterExtIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 20),
    _RuckusIpv4AclFilterExtIcmpType_Type()
)
ruckusIpv4AclFilterExtIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterExtIcmpType.setStatus("current")
_RuckusIpv4AclFilterPolicyName_Type = AclPolicyName
_RuckusIpv4AclFilterPolicyName_Object = MibTableColumn
ruckusIpv4AclFilterPolicyName = _RuckusIpv4AclFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 21),
    _RuckusIpv4AclFilterPolicyName_Type()
)
ruckusIpv4AclFilterPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterPolicyName.setStatus("current")


class _RuckusIpv4AclFilterDscpMatch_Type(Integer32):
    """Custom type ruckusIpv4AclFilterDscpMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuckusIpv4AclFilterDscpMatch_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterDscpMatch_Object = MibTableColumn
ruckusIpv4AclFilterDscpMatch = _RuckusIpv4AclFilterDscpMatch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 22),
    _RuckusIpv4AclFilterDscpMatch_Type()
)
ruckusIpv4AclFilterDscpMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDscpMatch.setStatus("current")


class _RuckusIpv4AclFilterDscpForce_Type(Integer32):
    """Custom type ruckusIpv4AclFilterDscpForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuckusIpv4AclFilterDscpForce_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterDscpForce_Object = MibTableColumn
ruckusIpv4AclFilterDscpForce = _RuckusIpv4AclFilterDscpForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 23),
    _RuckusIpv4AclFilterDscpForce_Type()
)
ruckusIpv4AclFilterDscpForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterDscpForce.setStatus("current")


class _RuckusIpv4AclFilterPriorityMatch_Type(Integer32):
    """Custom type ruckusIpv4AclFilterPriorityMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv4AclFilterPriorityMatch_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterPriorityMatch_Object = MibTableColumn
ruckusIpv4AclFilterPriorityMatch = _RuckusIpv4AclFilterPriorityMatch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 24),
    _RuckusIpv4AclFilterPriorityMatch_Type()
)
ruckusIpv4AclFilterPriorityMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterPriorityMatch.setStatus("current")


class _RuckusIpv4AclFilterPriorityForce_Type(Integer32):
    """Custom type ruckusIpv4AclFilterPriorityForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv4AclFilterPriorityForce_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterPriorityForce_Object = MibTableColumn
ruckusIpv4AclFilterPriorityForce = _RuckusIpv4AclFilterPriorityForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 25),
    _RuckusIpv4AclFilterPriorityForce_Type()
)
ruckusIpv4AclFilterPriorityForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterPriorityForce.setStatus("current")


class _RuckusIpv4AclFilterInternalPriority_Type(Integer32):
    """Custom type ruckusIpv4AclFilterInternalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv4AclFilterInternalPriority_Type.__name__ = "Integer32"
_RuckusIpv4AclFilterInternalPriority_Object = MibTableColumn
ruckusIpv4AclFilterInternalPriority = _RuckusIpv4AclFilterInternalPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 26),
    _RuckusIpv4AclFilterInternalPriority_Type()
)
ruckusIpv4AclFilterInternalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterInternalPriority.setStatus("current")


class _RuckusIpv4AclFilterMirrorPkts_Type(TruthValue):
    """Custom type ruckusIpv4AclFilterMirrorPkts based on TruthValue"""
    defaultValue = 2


_RuckusIpv4AclFilterMirrorPkts_Type.__name__ = "TruthValue"
_RuckusIpv4AclFilterMirrorPkts_Object = MibTableColumn
ruckusIpv4AclFilterMirrorPkts = _RuckusIpv4AclFilterMirrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 27),
    _RuckusIpv4AclFilterMirrorPkts_Type()
)
ruckusIpv4AclFilterMirrorPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterMirrorPkts.setStatus("current")
_RuckusIpv4AclFilterLogEnable_Type = TruthValue
_RuckusIpv4AclFilterLogEnable_Object = MibTableColumn
ruckusIpv4AclFilterLogEnable = _RuckusIpv4AclFilterLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 28),
    _RuckusIpv4AclFilterLogEnable_Type()
)
ruckusIpv4AclFilterLogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterLogEnable.setStatus("current")


class _RuckusIpv4AclFilterComments_Type(DisplayString):
    """Custom type ruckusIpv4AclFilterComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuckusIpv4AclFilterComments_Type.__name__ = "DisplayString"
_RuckusIpv4AclFilterComments_Object = MibTableColumn
ruckusIpv4AclFilterComments = _RuckusIpv4AclFilterComments_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 29),
    _RuckusIpv4AclFilterComments_Type()
)
ruckusIpv4AclFilterComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterComments.setStatus("current")
_RuckusIpv4AclFilterRowStatus_Type = RowStatus
_RuckusIpv4AclFilterRowStatus_Object = MibTableColumn
ruckusIpv4AclFilterRowStatus = _RuckusIpv4AclFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 1, 1, 1, 30),
    _RuckusIpv4AclFilterRowStatus_Type()
)
ruckusIpv4AclFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv4AclFilterRowStatus.setStatus("current")
_RuckusIpv6Filters_ObjectIdentity = ObjectIdentity
ruckusIpv6Filters = _RuckusIpv6Filters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2)
)
_RuckusIpv6AclFilterTable_Object = MibTable
ruckusIpv6AclFilterTable = _RuckusIpv6AclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterTable.setStatus("current")
_RuckusIpv6AclFilterEntry_Object = MibTableRow
ruckusIpv6AclFilterEntry = _RuckusIpv6AclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1)
)
ruckusIpv6AclFilterEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclName"),
    (0, "RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSeqNum"),
)
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterEntry.setStatus("current")
_RuckusIpv6AclFilterSeqNum_Type = Unsigned32
_RuckusIpv6AclFilterSeqNum_Object = MibTableColumn
ruckusIpv6AclFilterSeqNum = _RuckusIpv6AclFilterSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 1),
    _RuckusIpv6AclFilterSeqNum_Type()
)
ruckusIpv6AclFilterSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSeqNum.setStatus("current")
_RuckusIpv6AclFilterAction_Type = AclAction
_RuckusIpv6AclFilterAction_Object = MibTableColumn
ruckusIpv6AclFilterAction = _RuckusIpv6AclFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 2),
    _RuckusIpv6AclFilterAction_Type()
)
ruckusIpv6AclFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterAction.setStatus("current")


class _RuckusIpv6AclFilterStdProtocol_Type(Integer32):
    """Custom type ruckusIpv6AclFilterStdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              41,
              50,
              51,
              58,
              132,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("ip6", 41),
          ("esp", 50),
          ("ahp", 51),
          ("icmp", 58),
          ("sctp", 132),
          ("extended", 255))
    )


_RuckusIpv6AclFilterStdProtocol_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterStdProtocol_Object = MibTableColumn
ruckusIpv6AclFilterStdProtocol = _RuckusIpv6AclFilterStdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 3),
    _RuckusIpv6AclFilterStdProtocol_Type()
)
ruckusIpv6AclFilterStdProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterStdProtocol.setStatus("current")


class _RuckusIpv6AclFilterExtProtocol_Type(Integer32):
    """Custom type ruckusIpv6AclFilterExtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv6AclFilterExtProtocol_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterExtProtocol_Object = MibTableColumn
ruckusIpv6AclFilterExtProtocol = _RuckusIpv6AclFilterExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 4),
    _RuckusIpv6AclFilterExtProtocol_Type()
)
ruckusIpv6AclFilterExtProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterExtProtocol.setStatus("current")
_RuckusIpv6AclFilterSrcAddr_Type = InetAddressIPv6
_RuckusIpv6AclFilterSrcAddr_Object = MibTableColumn
ruckusIpv6AclFilterSrcAddr = _RuckusIpv6AclFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 5),
    _RuckusIpv6AclFilterSrcAddr_Type()
)
ruckusIpv6AclFilterSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSrcAddr.setStatus("current")


class _RuckusIpv6AclFilterSrcPrefixLen_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterSrcPrefixLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RuckusIpv6AclFilterSrcPrefixLen_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterSrcPrefixLen_Object = MibTableColumn
ruckusIpv6AclFilterSrcPrefixLen = _RuckusIpv6AclFilterSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 6),
    _RuckusIpv6AclFilterSrcPrefixLen_Type()
)
ruckusIpv6AclFilterSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSrcPrefixLen.setStatus("current")
_RuckusIpv6AclFilterSrcOperator_Type = AclOperator
_RuckusIpv6AclFilterSrcOperator_Object = MibTableColumn
ruckusIpv6AclFilterSrcOperator = _RuckusIpv6AclFilterSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 7),
    _RuckusIpv6AclFilterSrcOperator_Type()
)
ruckusIpv6AclFilterSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSrcOperator.setStatus("current")


class _RuckusIpv6AclFilterSrcPortLow_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterSrcPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv6AclFilterSrcPortLow_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterSrcPortLow_Object = MibTableColumn
ruckusIpv6AclFilterSrcPortLow = _RuckusIpv6AclFilterSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 8),
    _RuckusIpv6AclFilterSrcPortLow_Type()
)
ruckusIpv6AclFilterSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSrcPortLow.setStatus("current")


class _RuckusIpv6AclFilterSrcPortHigh_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterSrcPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv6AclFilterSrcPortHigh_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterSrcPortHigh_Object = MibTableColumn
ruckusIpv6AclFilterSrcPortHigh = _RuckusIpv6AclFilterSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 9),
    _RuckusIpv6AclFilterSrcPortHigh_Type()
)
ruckusIpv6AclFilterSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSrcPortHigh.setStatus("current")
_RuckusIpv6AclFilterDestAddr_Type = InetAddressIPv6
_RuckusIpv6AclFilterDestAddr_Object = MibTableColumn
ruckusIpv6AclFilterDestAddr = _RuckusIpv6AclFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 10),
    _RuckusIpv6AclFilterDestAddr_Type()
)
ruckusIpv6AclFilterDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDestAddr.setStatus("current")


class _RuckusIpv6AclFilterDestPrefixLen_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterDestPrefixLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RuckusIpv6AclFilterDestPrefixLen_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterDestPrefixLen_Object = MibTableColumn
ruckusIpv6AclFilterDestPrefixLen = _RuckusIpv6AclFilterDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 11),
    _RuckusIpv6AclFilterDestPrefixLen_Type()
)
ruckusIpv6AclFilterDestPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDestPrefixLen.setStatus("current")
_RuckusIpv6AclFilterDestOperator_Type = AclOperator
_RuckusIpv6AclFilterDestOperator_Object = MibTableColumn
ruckusIpv6AclFilterDestOperator = _RuckusIpv6AclFilterDestOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 12),
    _RuckusIpv6AclFilterDestOperator_Type()
)
ruckusIpv6AclFilterDestOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDestOperator.setStatus("current")


class _RuckusIpv6AclFilterDestPortLow_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterDestPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv6AclFilterDestPortLow_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterDestPortLow_Object = MibTableColumn
ruckusIpv6AclFilterDestPortLow = _RuckusIpv6AclFilterDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 13),
    _RuckusIpv6AclFilterDestPortLow_Type()
)
ruckusIpv6AclFilterDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDestPortLow.setStatus("current")


class _RuckusIpv6AclFilterDestPortHigh_Type(Unsigned32):
    """Custom type ruckusIpv6AclFilterDestPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusIpv6AclFilterDestPortHigh_Type.__name__ = "Unsigned32"
_RuckusIpv6AclFilterDestPortHigh_Object = MibTableColumn
ruckusIpv6AclFilterDestPortHigh = _RuckusIpv6AclFilterDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 14),
    _RuckusIpv6AclFilterDestPortHigh_Type()
)
ruckusIpv6AclFilterDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDestPortHigh.setStatus("current")
_RuckusIpv6AclFilterEstablished_Type = TruthValue
_RuckusIpv6AclFilterEstablished_Object = MibTableColumn
ruckusIpv6AclFilterEstablished = _RuckusIpv6AclFilterEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 15),
    _RuckusIpv6AclFilterEstablished_Type()
)
ruckusIpv6AclFilterEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterEstablished.setStatus("current")


class _RuckusIpv6AclFilterIcmpType_Type(Integer32):
    """Custom type ruckusIpv6AclFilterIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              138,
              255)
        )
    )
    namedValues = NamedValues(
        *(("destUnreachable", 1),
          ("largePackets", 2),
          ("timeExceed", 3),
          ("paramProblem", 4),
          ("echoReq", 128),
          ("echoReply", 129),
          ("mldQueries", 130),
          ("mldReport", 131),
          ("mldReduction", 132),
          ("routerSolicit", 133),
          ("routerAdv", 134),
          ("neighborSolicit", 135),
          ("neighborAdv", 136),
          ("routerRenumbering", 138),
          ("extended", 255))
    )


_RuckusIpv6AclFilterIcmpType_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterIcmpType_Object = MibTableColumn
ruckusIpv6AclFilterIcmpType = _RuckusIpv6AclFilterIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 16),
    _RuckusIpv6AclFilterIcmpType_Type()
)
ruckusIpv6AclFilterIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterIcmpType.setStatus("current")


class _RuckusIpv6AclFilterIcmpCode_Type(Integer32):
    """Custom type ruckusIpv6AclFilterIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv6AclFilterIcmpCode_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterIcmpCode_Object = MibTableColumn
ruckusIpv6AclFilterIcmpCode = _RuckusIpv6AclFilterIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 17),
    _RuckusIpv6AclFilterIcmpCode_Type()
)
ruckusIpv6AclFilterIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterIcmpCode.setStatus("current")


class _RuckusIpv6AclFilterExtIcmpType_Type(Integer32):
    """Custom type ruckusIpv6AclFilterExtIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuckusIpv6AclFilterExtIcmpType_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterExtIcmpType_Object = MibTableColumn
ruckusIpv6AclFilterExtIcmpType = _RuckusIpv6AclFilterExtIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 18),
    _RuckusIpv6AclFilterExtIcmpType_Type()
)
ruckusIpv6AclFilterExtIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterExtIcmpType.setStatus("current")
_RuckusIpv6AclFilterPolicyName_Type = AclPolicyName
_RuckusIpv6AclFilterPolicyName_Object = MibTableColumn
ruckusIpv6AclFilterPolicyName = _RuckusIpv6AclFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 19),
    _RuckusIpv6AclFilterPolicyName_Type()
)
ruckusIpv6AclFilterPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterPolicyName.setStatus("current")


class _RuckusIpv6AclFilterDscpMatch_Type(Integer32):
    """Custom type ruckusIpv6AclFilterDscpMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuckusIpv6AclFilterDscpMatch_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterDscpMatch_Object = MibTableColumn
ruckusIpv6AclFilterDscpMatch = _RuckusIpv6AclFilterDscpMatch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 20),
    _RuckusIpv6AclFilterDscpMatch_Type()
)
ruckusIpv6AclFilterDscpMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDscpMatch.setStatus("current")


class _RuckusIpv6AclFilterDscpForce_Type(Integer32):
    """Custom type ruckusIpv6AclFilterDscpForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuckusIpv6AclFilterDscpForce_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterDscpForce_Object = MibTableColumn
ruckusIpv6AclFilterDscpForce = _RuckusIpv6AclFilterDscpForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 21),
    _RuckusIpv6AclFilterDscpForce_Type()
)
ruckusIpv6AclFilterDscpForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterDscpForce.setStatus("current")


class _RuckusIpv6AclFilterPriorityMatch_Type(Integer32):
    """Custom type ruckusIpv6AclFilterPriorityMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv6AclFilterPriorityMatch_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterPriorityMatch_Object = MibTableColumn
ruckusIpv6AclFilterPriorityMatch = _RuckusIpv6AclFilterPriorityMatch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 22),
    _RuckusIpv6AclFilterPriorityMatch_Type()
)
ruckusIpv6AclFilterPriorityMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterPriorityMatch.setStatus("current")


class _RuckusIpv6AclFilterPriorityForce_Type(Integer32):
    """Custom type ruckusIpv6AclFilterPriorityForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv6AclFilterPriorityForce_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterPriorityForce_Object = MibTableColumn
ruckusIpv6AclFilterPriorityForce = _RuckusIpv6AclFilterPriorityForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 23),
    _RuckusIpv6AclFilterPriorityForce_Type()
)
ruckusIpv6AclFilterPriorityForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterPriorityForce.setStatus("current")


class _RuckusIpv6AclFilterInternalPriority_Type(Integer32):
    """Custom type ruckusIpv6AclFilterInternalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuckusIpv6AclFilterInternalPriority_Type.__name__ = "Integer32"
_RuckusIpv6AclFilterInternalPriority_Object = MibTableColumn
ruckusIpv6AclFilterInternalPriority = _RuckusIpv6AclFilterInternalPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 24),
    _RuckusIpv6AclFilterInternalPriority_Type()
)
ruckusIpv6AclFilterInternalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterInternalPriority.setStatus("current")


class _RuckusIpv6AclFilterFragments_Type(TruthValue):
    """Custom type ruckusIpv6AclFilterFragments based on TruthValue"""
    defaultValue = 2


_RuckusIpv6AclFilterFragments_Type.__name__ = "TruthValue"
_RuckusIpv6AclFilterFragments_Object = MibTableColumn
ruckusIpv6AclFilterFragments = _RuckusIpv6AclFilterFragments_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 25),
    _RuckusIpv6AclFilterFragments_Type()
)
ruckusIpv6AclFilterFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterFragments.setStatus("current")


class _RuckusIpv6AclFilterSourceRoute_Type(TruthValue):
    """Custom type ruckusIpv6AclFilterSourceRoute based on TruthValue"""
    defaultValue = 2


_RuckusIpv6AclFilterSourceRoute_Type.__name__ = "TruthValue"
_RuckusIpv6AclFilterSourceRoute_Object = MibTableColumn
ruckusIpv6AclFilterSourceRoute = _RuckusIpv6AclFilterSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 26),
    _RuckusIpv6AclFilterSourceRoute_Type()
)
ruckusIpv6AclFilterSourceRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterSourceRoute.setStatus("current")


class _RuckusIpv6AclFilterMirrorPkts_Type(TruthValue):
    """Custom type ruckusIpv6AclFilterMirrorPkts based on TruthValue"""
    defaultValue = 2


_RuckusIpv6AclFilterMirrorPkts_Type.__name__ = "TruthValue"
_RuckusIpv6AclFilterMirrorPkts_Object = MibTableColumn
ruckusIpv6AclFilterMirrorPkts = _RuckusIpv6AclFilterMirrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 27),
    _RuckusIpv6AclFilterMirrorPkts_Type()
)
ruckusIpv6AclFilterMirrorPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterMirrorPkts.setStatus("current")
_RuckusIpv6AclFilterLogEnable_Type = TruthValue
_RuckusIpv6AclFilterLogEnable_Object = MibTableColumn
ruckusIpv6AclFilterLogEnable = _RuckusIpv6AclFilterLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 28),
    _RuckusIpv6AclFilterLogEnable_Type()
)
ruckusIpv6AclFilterLogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterLogEnable.setStatus("current")


class _RuckusIpv6AclFilterComments_Type(DisplayString):
    """Custom type ruckusIpv6AclFilterComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuckusIpv6AclFilterComments_Type.__name__ = "DisplayString"
_RuckusIpv6AclFilterComments_Object = MibTableColumn
ruckusIpv6AclFilterComments = _RuckusIpv6AclFilterComments_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 29),
    _RuckusIpv6AclFilterComments_Type()
)
ruckusIpv6AclFilterComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterComments.setStatus("current")
_RuckusIpv6AclFilterRowStatus_Type = RowStatus
_RuckusIpv6AclFilterRowStatus_Object = MibTableColumn
ruckusIpv6AclFilterRowStatus = _RuckusIpv6AclFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 2, 1, 1, 30),
    _RuckusIpv6AclFilterRowStatus_Type()
)
ruckusIpv6AclFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusIpv6AclFilterRowStatus.setStatus("current")
_RuckusMacFilters_ObjectIdentity = ObjectIdentity
ruckusMacFilters = _RuckusMacFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3)
)
_RuckusMacAclFilterTable_Object = MibTable
ruckusMacAclFilterTable = _RuckusMacAclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusMacAclFilterTable.setStatus("current")
_RuckusMacAclFilterEntry_Object = MibTableRow
ruckusMacAclFilterEntry = _RuckusMacAclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1)
)
ruckusMacAclFilterEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclName"),
    (0, "RUCKUS-ACL-MIB", "ruckusMacAclFilterSeqNum"),
)
if mibBuilder.loadTexts:
    ruckusMacAclFilterEntry.setStatus("current")
_RuckusMacAclFilterSeqNum_Type = Unsigned32
_RuckusMacAclFilterSeqNum_Object = MibTableColumn
ruckusMacAclFilterSeqNum = _RuckusMacAclFilterSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 1),
    _RuckusMacAclFilterSeqNum_Type()
)
ruckusMacAclFilterSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusMacAclFilterSeqNum.setStatus("current")
_RuckusMacAclFilterAction_Type = AclAction
_RuckusMacAclFilterAction_Object = MibTableColumn
ruckusMacAclFilterAction = _RuckusMacAclFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 2),
    _RuckusMacAclFilterAction_Type()
)
ruckusMacAclFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterAction.setStatus("current")


class _RuckusMacAclFilterSrcAddr_Type(MacAddress):
    """Custom type ruckusMacAclFilterSrcAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_RuckusMacAclFilterSrcAddr_Type.__name__ = "MacAddress"
_RuckusMacAclFilterSrcAddr_Object = MibTableColumn
ruckusMacAclFilterSrcAddr = _RuckusMacAclFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 3),
    _RuckusMacAclFilterSrcAddr_Type()
)
ruckusMacAclFilterSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterSrcAddr.setStatus("current")


class _RuckusMacAclFilterSrcMask_Type(MacAddress):
    """Custom type ruckusMacAclFilterSrcMask based on MacAddress"""
    defaultHexValue = "000000000000"


_RuckusMacAclFilterSrcMask_Type.__name__ = "MacAddress"
_RuckusMacAclFilterSrcMask_Object = MibTableColumn
ruckusMacAclFilterSrcMask = _RuckusMacAclFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 4),
    _RuckusMacAclFilterSrcMask_Type()
)
ruckusMacAclFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterSrcMask.setStatus("current")


class _RuckusMacAclFilterDestAddr_Type(MacAddress):
    """Custom type ruckusMacAclFilterDestAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_RuckusMacAclFilterDestAddr_Type.__name__ = "MacAddress"
_RuckusMacAclFilterDestAddr_Object = MibTableColumn
ruckusMacAclFilterDestAddr = _RuckusMacAclFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 5),
    _RuckusMacAclFilterDestAddr_Type()
)
ruckusMacAclFilterDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterDestAddr.setStatus("current")


class _RuckusMacAclFilterDestMask_Type(MacAddress):
    """Custom type ruckusMacAclFilterDestMask based on MacAddress"""
    defaultHexValue = "000000000000"


_RuckusMacAclFilterDestMask_Type.__name__ = "MacAddress"
_RuckusMacAclFilterDestMask_Object = MibTableColumn
ruckusMacAclFilterDestMask = _RuckusMacAclFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 6),
    _RuckusMacAclFilterDestMask_Type()
)
ruckusMacAclFilterDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterDestMask.setStatus("current")


class _RuckusMacAclFilterEtherType_Type(Integer32):
    """Custom type ruckusMacAclFilterEtherType based on Integer32"""
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
        *(("arp", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("extended", 4))
    )


_RuckusMacAclFilterEtherType_Type.__name__ = "Integer32"
_RuckusMacAclFilterEtherType_Object = MibTableColumn
ruckusMacAclFilterEtherType = _RuckusMacAclFilterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 7),
    _RuckusMacAclFilterEtherType_Type()
)
ruckusMacAclFilterEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterEtherType.setStatus("current")
_RuckusMacAclFilterExtEtherType_Type = EtherType
_RuckusMacAclFilterExtEtherType_Object = MibTableColumn
ruckusMacAclFilterExtEtherType = _RuckusMacAclFilterExtEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 8),
    _RuckusMacAclFilterExtEtherType_Type()
)
ruckusMacAclFilterExtEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterExtEtherType.setStatus("current")


class _RuckusMacAclFilterMirrorPkts_Type(TruthValue):
    """Custom type ruckusMacAclFilterMirrorPkts based on TruthValue"""
    defaultValue = 2


_RuckusMacAclFilterMirrorPkts_Type.__name__ = "TruthValue"
_RuckusMacAclFilterMirrorPkts_Object = MibTableColumn
ruckusMacAclFilterMirrorPkts = _RuckusMacAclFilterMirrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 9),
    _RuckusMacAclFilterMirrorPkts_Type()
)
ruckusMacAclFilterMirrorPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterMirrorPkts.setStatus("current")
_RuckusMacAclFilterLogEnable_Type = TruthValue
_RuckusMacAclFilterLogEnable_Object = MibTableColumn
ruckusMacAclFilterLogEnable = _RuckusMacAclFilterLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 10),
    _RuckusMacAclFilterLogEnable_Type()
)
ruckusMacAclFilterLogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterLogEnable.setStatus("current")
_RuckusMacAclFilterRowStatus_Type = RowStatus
_RuckusMacAclFilterRowStatus_Object = MibTableColumn
ruckusMacAclFilterRowStatus = _RuckusMacAclFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 2, 3, 1, 1, 11),
    _RuckusMacAclFilterRowStatus_Type()
)
ruckusMacAclFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusMacAclFilterRowStatus.setStatus("current")
_RuckusAclBindings_ObjectIdentity = ObjectIdentity
ruckusAclBindings = _RuckusAclBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3)
)
_RuckusAclIfBindTable_Object = MibTable
ruckusAclIfBindTable = _RuckusAclIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusAclIfBindTable.setStatus("current")
_RuckusAclIfBindEntry_Object = MibTableRow
ruckusAclIfBindEntry = _RuckusAclIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1)
)
ruckusAclIfBindEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclIfBindPort"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclIfBindType"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclIfBindDirection"),
)
if mibBuilder.loadTexts:
    ruckusAclIfBindEntry.setStatus("current")
_RuckusAclIfBindPort_Type = InterfaceIndex
_RuckusAclIfBindPort_Object = MibTableColumn
ruckusAclIfBindPort = _RuckusAclIfBindPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 1),
    _RuckusAclIfBindPort_Type()
)
ruckusAclIfBindPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclIfBindPort.setStatus("current")
_RuckusAclIfBindType_Type = AclType
_RuckusAclIfBindType_Object = MibTableColumn
ruckusAclIfBindType = _RuckusAclIfBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 2),
    _RuckusAclIfBindType_Type()
)
ruckusAclIfBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclIfBindType.setStatus("current")
_RuckusAclIfBindDirection_Type = AclDirection
_RuckusAclIfBindDirection_Object = MibTableColumn
ruckusAclIfBindDirection = _RuckusAclIfBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 3),
    _RuckusAclIfBindDirection_Type()
)
ruckusAclIfBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclIfBindDirection.setStatus("current")
_RuckusAclIfBindName_Type = AclName
_RuckusAclIfBindName_Object = MibTableColumn
ruckusAclIfBindName = _RuckusAclIfBindName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 4),
    _RuckusAclIfBindName_Type()
)
ruckusAclIfBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclIfBindName.setStatus("current")


class _RuckusAclIfBindLog_Type(TruthValue):
    """Custom type ruckusAclIfBindLog based on TruthValue"""
    defaultValue = 2


_RuckusAclIfBindLog_Type.__name__ = "TruthValue"
_RuckusAclIfBindLog_Object = MibTableColumn
ruckusAclIfBindLog = _RuckusAclIfBindLog_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 5),
    _RuckusAclIfBindLog_Type()
)
ruckusAclIfBindLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclIfBindLog.setStatus("current")
_RuckusAclIfBindRowStatus_Type = RowStatus
_RuckusAclIfBindRowStatus_Object = MibTableColumn
ruckusAclIfBindRowStatus = _RuckusAclIfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 1, 1, 6),
    _RuckusAclIfBindRowStatus_Type()
)
ruckusAclIfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclIfBindRowStatus.setStatus("current")
_RuckusAclVlanBindTable_Object = MibTable
ruckusAclVlanBindTable = _RuckusAclVlanBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruckusAclVlanBindTable.setStatus("current")
_RuckusAclVlanBindEntry_Object = MibTableRow
ruckusAclVlanBindEntry = _RuckusAclVlanBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1)
)
ruckusAclVlanBindEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclVlanBindId"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclVlanBindType"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclVlanBindDirection"),
)
if mibBuilder.loadTexts:
    ruckusAclVlanBindEntry.setStatus("current")
_RuckusAclVlanBindId_Type = VlanId
_RuckusAclVlanBindId_Object = MibTableColumn
ruckusAclVlanBindId = _RuckusAclVlanBindId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 1),
    _RuckusAclVlanBindId_Type()
)
ruckusAclVlanBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVlanBindId.setStatus("current")
_RuckusAclVlanBindType_Type = AclType
_RuckusAclVlanBindType_Object = MibTableColumn
ruckusAclVlanBindType = _RuckusAclVlanBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 2),
    _RuckusAclVlanBindType_Type()
)
ruckusAclVlanBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVlanBindType.setStatus("current")
_RuckusAclVlanBindDirection_Type = AclDirection
_RuckusAclVlanBindDirection_Object = MibTableColumn
ruckusAclVlanBindDirection = _RuckusAclVlanBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 3),
    _RuckusAclVlanBindDirection_Type()
)
ruckusAclVlanBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVlanBindDirection.setStatus("current")
_RuckusAclVlanBindName_Type = AclName
_RuckusAclVlanBindName_Object = MibTableColumn
ruckusAclVlanBindName = _RuckusAclVlanBindName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 4),
    _RuckusAclVlanBindName_Type()
)
ruckusAclVlanBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVlanBindName.setStatus("current")


class _RuckusAclVlanBindLog_Type(TruthValue):
    """Custom type ruckusAclVlanBindLog based on TruthValue"""
    defaultValue = 2


_RuckusAclVlanBindLog_Type.__name__ = "TruthValue"
_RuckusAclVlanBindLog_Object = MibTableColumn
ruckusAclVlanBindLog = _RuckusAclVlanBindLog_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 5),
    _RuckusAclVlanBindLog_Type()
)
ruckusAclVlanBindLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVlanBindLog.setStatus("current")
_RuckusAclVlanBindRowStatus_Type = RowStatus
_RuckusAclVlanBindRowStatus_Object = MibTableColumn
ruckusAclVlanBindRowStatus = _RuckusAclVlanBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 2, 1, 6),
    _RuckusAclVlanBindRowStatus_Type()
)
ruckusAclVlanBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVlanBindRowStatus.setStatus("current")
_RuckusAclVPortBindTable_Object = MibTable
ruckusAclVPortBindTable = _RuckusAclVPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ruckusAclVPortBindTable.setStatus("current")
_RuckusAclVPortBindEntry_Object = MibTableRow
ruckusAclVPortBindEntry = _RuckusAclVPortBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1)
)
ruckusAclVPortBindEntry.setIndexNames(
    (0, "RUCKUS-ACL-MIB", "ruckusAclVPortBindId"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclVPortBindPort"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclVPortBindType"),
    (0, "RUCKUS-ACL-MIB", "ruckusAclVPortBindDirection"),
)
if mibBuilder.loadTexts:
    ruckusAclVPortBindEntry.setStatus("current")
_RuckusAclVPortBindId_Type = VlanId
_RuckusAclVPortBindId_Object = MibTableColumn
ruckusAclVPortBindId = _RuckusAclVPortBindId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 1),
    _RuckusAclVPortBindId_Type()
)
ruckusAclVPortBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVPortBindId.setStatus("current")
_RuckusAclVPortBindPort_Type = InterfaceIndex
_RuckusAclVPortBindPort_Object = MibTableColumn
ruckusAclVPortBindPort = _RuckusAclVPortBindPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 2),
    _RuckusAclVPortBindPort_Type()
)
ruckusAclVPortBindPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVPortBindPort.setStatus("current")
_RuckusAclVPortBindType_Type = AclType
_RuckusAclVPortBindType_Object = MibTableColumn
ruckusAclVPortBindType = _RuckusAclVPortBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 3),
    _RuckusAclVPortBindType_Type()
)
ruckusAclVPortBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVPortBindType.setStatus("current")
_RuckusAclVPortBindDirection_Type = AclDirection
_RuckusAclVPortBindDirection_Object = MibTableColumn
ruckusAclVPortBindDirection = _RuckusAclVPortBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 4),
    _RuckusAclVPortBindDirection_Type()
)
ruckusAclVPortBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAclVPortBindDirection.setStatus("current")
_RuckusAclVPortBindName_Type = AclName
_RuckusAclVPortBindName_Object = MibTableColumn
ruckusAclVPortBindName = _RuckusAclVPortBindName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 5),
    _RuckusAclVPortBindName_Type()
)
ruckusAclVPortBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVPortBindName.setStatus("current")


class _RuckusAclVPortBindLog_Type(TruthValue):
    """Custom type ruckusAclVPortBindLog based on TruthValue"""
    defaultValue = 2


_RuckusAclVPortBindLog_Type.__name__ = "TruthValue"
_RuckusAclVPortBindLog_Object = MibTableColumn
ruckusAclVPortBindLog = _RuckusAclVPortBindLog_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 6),
    _RuckusAclVPortBindLog_Type()
)
ruckusAclVPortBindLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVPortBindLog.setStatus("current")
_RuckusAclVPortBindRowStatus_Type = RowStatus
_RuckusAclVPortBindRowStatus_Object = MibTableColumn
ruckusAclVPortBindRowStatus = _RuckusAclVPortBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 1, 3, 3, 1, 7),
    _RuckusAclVPortBindRowStatus_Type()
)
ruckusAclVPortBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusAclVPortBindRowStatus.setStatus("current")
_RuckusAclConformance_ObjectIdentity = ObjectIdentity
ruckusAclConformance = _RuckusAclConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 2)
)
_RuckusAclCompliances_ObjectIdentity = ObjectIdentity
ruckusAclCompliances = _RuckusAclCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 2, 1)
)
_RuckusAclGroups_ObjectIdentity = ObjectIdentity
ruckusAclGroups = _RuckusAclGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 2, 2)
)

# Managed Objects groups

ruckusAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 2, 2, 1)
)
ruckusAclGroup.setObjects(
      *(("RUCKUS-ACL-MIB", "ruckusAclAcctEnable"),
        ("RUCKUS-ACL-MIB", "ruckusAclRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterAction"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterStdProtocol"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterExtProtocol"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSrcAddr"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSrcMask"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSrcOperator"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSrcPortLow"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterSrcPortHigh"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDestAddr"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDestMask"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDestOperator"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDestPortLow"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDestPortHigh"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterEstablished"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterPrecedence"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterTos"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterIcmpType"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterIcmpCode"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterPolicyName"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDscpMatch"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterDscpForce"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterPriorityMatch"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterPriorityForce"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterInternalPriority"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterMirrorPkts"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterLogEnable"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterComments"),
        ("RUCKUS-ACL-MIB", "ruckusIpv4AclFilterRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterAction"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterStdProtocol"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterExtProtocol"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSrcAddr"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSrcPrefixLen"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSrcOperator"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSrcPortLow"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSrcPortHigh"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDestAddr"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDestPrefixLen"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDestOperator"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDestPortLow"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDestPortHigh"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterEstablished"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterIcmpType"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterIcmpCode"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterPolicyName"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDscpMatch"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterDscpForce"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterPriorityMatch"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterPriorityForce"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterInternalPriority"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterFragments"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterSourceRoute"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterMirrorPkts"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterLogEnable"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterComments"),
        ("RUCKUS-ACL-MIB", "ruckusIpv6AclFilterRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterAction"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterSrcAddr"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterSrcMask"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterDestAddr"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterDestMask"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterEtherType"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterExtEtherType"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterMirrorPkts"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterLogEnable"),
        ("RUCKUS-ACL-MIB", "ruckusMacAclFilterRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusAclIfBindName"),
        ("RUCKUS-ACL-MIB", "ruckusAclIfBindLog"),
        ("RUCKUS-ACL-MIB", "ruckusAclIfBindRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusAclVlanBindName"),
        ("RUCKUS-ACL-MIB", "ruckusAclVlanBindLog"),
        ("RUCKUS-ACL-MIB", "ruckusAclVlanBindRowStatus"),
        ("RUCKUS-ACL-MIB", "ruckusAclVPortBindName"),
        ("RUCKUS-ACL-MIB", "ruckusAclVPortBindLog"),
        ("RUCKUS-ACL-MIB", "ruckusAclVPortBindRowStatus"))
)
if mibBuilder.loadTexts:
    ruckusAclGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruckusAclCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 45, 2, 1, 1)
)
ruckusAclCompliance.setObjects(
    ("RUCKUS-ACL-MIB", "ruckusAclGroup")
)
if mibBuilder.loadTexts:
    ruckusAclCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ACL-MIB",
    **{"VlanId": VlanId,
       "AclName": AclName,
       "AclPolicyName": AclPolicyName,
       "AclType": AclType,
       "AclAction": AclAction,
       "AclDirection": AclDirection,
       "AclOperator": AclOperator,
       "IpPrecedence": IpPrecedence,
       "IpTos": IpTos,
       "EtherType": EtherType,
       "ruckusAclMIB": ruckusAclMIB,
       "ruckusAclNotify": ruckusAclNotify,
       "ruckusAclObjects": ruckusAclObjects,
       "ruckusAcls": ruckusAcls,
       "ruckusAclTable": ruckusAclTable,
       "ruckusAclEntry": ruckusAclEntry,
       "ruckusAclType": ruckusAclType,
       "ruckusAclName": ruckusAclName,
       "ruckusAclAcctEnable": ruckusAclAcctEnable,
       "ruckusAclStandard": ruckusAclStandard,
       "ruckusAclRowStatus": ruckusAclRowStatus,
       "ruckusAclFilters": ruckusAclFilters,
       "ruckusIpv4Filters": ruckusIpv4Filters,
       "ruckusIpv4AclFilterTable": ruckusIpv4AclFilterTable,
       "ruckusIpv4AclFilterEntry": ruckusIpv4AclFilterEntry,
       "ruckusIpv4AclFilterSeqNum": ruckusIpv4AclFilterSeqNum,
       "ruckusIpv4AclFilterAction": ruckusIpv4AclFilterAction,
       "ruckusIpv4AclFilterStdProtocol": ruckusIpv4AclFilterStdProtocol,
       "ruckusIpv4AclFilterExtProtocol": ruckusIpv4AclFilterExtProtocol,
       "ruckusIpv4AclFilterSrcAddr": ruckusIpv4AclFilterSrcAddr,
       "ruckusIpv4AclFilterSrcMask": ruckusIpv4AclFilterSrcMask,
       "ruckusIpv4AclFilterSrcOperator": ruckusIpv4AclFilterSrcOperator,
       "ruckusIpv4AclFilterSrcPortLow": ruckusIpv4AclFilterSrcPortLow,
       "ruckusIpv4AclFilterSrcPortHigh": ruckusIpv4AclFilterSrcPortHigh,
       "ruckusIpv4AclFilterDestAddr": ruckusIpv4AclFilterDestAddr,
       "ruckusIpv4AclFilterDestMask": ruckusIpv4AclFilterDestMask,
       "ruckusIpv4AclFilterDestOperator": ruckusIpv4AclFilterDestOperator,
       "ruckusIpv4AclFilterDestPortLow": ruckusIpv4AclFilterDestPortLow,
       "ruckusIpv4AclFilterDestPortHigh": ruckusIpv4AclFilterDestPortHigh,
       "ruckusIpv4AclFilterEstablished": ruckusIpv4AclFilterEstablished,
       "ruckusIpv4AclFilterPrecedence": ruckusIpv4AclFilterPrecedence,
       "ruckusIpv4AclFilterTos": ruckusIpv4AclFilterTos,
       "ruckusIpv4AclFilterIcmpType": ruckusIpv4AclFilterIcmpType,
       "ruckusIpv4AclFilterIcmpCode": ruckusIpv4AclFilterIcmpCode,
       "ruckusIpv4AclFilterExtIcmpType": ruckusIpv4AclFilterExtIcmpType,
       "ruckusIpv4AclFilterPolicyName": ruckusIpv4AclFilterPolicyName,
       "ruckusIpv4AclFilterDscpMatch": ruckusIpv4AclFilterDscpMatch,
       "ruckusIpv4AclFilterDscpForce": ruckusIpv4AclFilterDscpForce,
       "ruckusIpv4AclFilterPriorityMatch": ruckusIpv4AclFilterPriorityMatch,
       "ruckusIpv4AclFilterPriorityForce": ruckusIpv4AclFilterPriorityForce,
       "ruckusIpv4AclFilterInternalPriority": ruckusIpv4AclFilterInternalPriority,
       "ruckusIpv4AclFilterMirrorPkts": ruckusIpv4AclFilterMirrorPkts,
       "ruckusIpv4AclFilterLogEnable": ruckusIpv4AclFilterLogEnable,
       "ruckusIpv4AclFilterComments": ruckusIpv4AclFilterComments,
       "ruckusIpv4AclFilterRowStatus": ruckusIpv4AclFilterRowStatus,
       "ruckusIpv6Filters": ruckusIpv6Filters,
       "ruckusIpv6AclFilterTable": ruckusIpv6AclFilterTable,
       "ruckusIpv6AclFilterEntry": ruckusIpv6AclFilterEntry,
       "ruckusIpv6AclFilterSeqNum": ruckusIpv6AclFilterSeqNum,
       "ruckusIpv6AclFilterAction": ruckusIpv6AclFilterAction,
       "ruckusIpv6AclFilterStdProtocol": ruckusIpv6AclFilterStdProtocol,
       "ruckusIpv6AclFilterExtProtocol": ruckusIpv6AclFilterExtProtocol,
       "ruckusIpv6AclFilterSrcAddr": ruckusIpv6AclFilterSrcAddr,
       "ruckusIpv6AclFilterSrcPrefixLen": ruckusIpv6AclFilterSrcPrefixLen,
       "ruckusIpv6AclFilterSrcOperator": ruckusIpv6AclFilterSrcOperator,
       "ruckusIpv6AclFilterSrcPortLow": ruckusIpv6AclFilterSrcPortLow,
       "ruckusIpv6AclFilterSrcPortHigh": ruckusIpv6AclFilterSrcPortHigh,
       "ruckusIpv6AclFilterDestAddr": ruckusIpv6AclFilterDestAddr,
       "ruckusIpv6AclFilterDestPrefixLen": ruckusIpv6AclFilterDestPrefixLen,
       "ruckusIpv6AclFilterDestOperator": ruckusIpv6AclFilterDestOperator,
       "ruckusIpv6AclFilterDestPortLow": ruckusIpv6AclFilterDestPortLow,
       "ruckusIpv6AclFilterDestPortHigh": ruckusIpv6AclFilterDestPortHigh,
       "ruckusIpv6AclFilterEstablished": ruckusIpv6AclFilterEstablished,
       "ruckusIpv6AclFilterIcmpType": ruckusIpv6AclFilterIcmpType,
       "ruckusIpv6AclFilterIcmpCode": ruckusIpv6AclFilterIcmpCode,
       "ruckusIpv6AclFilterExtIcmpType": ruckusIpv6AclFilterExtIcmpType,
       "ruckusIpv6AclFilterPolicyName": ruckusIpv6AclFilterPolicyName,
       "ruckusIpv6AclFilterDscpMatch": ruckusIpv6AclFilterDscpMatch,
       "ruckusIpv6AclFilterDscpForce": ruckusIpv6AclFilterDscpForce,
       "ruckusIpv6AclFilterPriorityMatch": ruckusIpv6AclFilterPriorityMatch,
       "ruckusIpv6AclFilterPriorityForce": ruckusIpv6AclFilterPriorityForce,
       "ruckusIpv6AclFilterInternalPriority": ruckusIpv6AclFilterInternalPriority,
       "ruckusIpv6AclFilterFragments": ruckusIpv6AclFilterFragments,
       "ruckusIpv6AclFilterSourceRoute": ruckusIpv6AclFilterSourceRoute,
       "ruckusIpv6AclFilterMirrorPkts": ruckusIpv6AclFilterMirrorPkts,
       "ruckusIpv6AclFilterLogEnable": ruckusIpv6AclFilterLogEnable,
       "ruckusIpv6AclFilterComments": ruckusIpv6AclFilterComments,
       "ruckusIpv6AclFilterRowStatus": ruckusIpv6AclFilterRowStatus,
       "ruckusMacFilters": ruckusMacFilters,
       "ruckusMacAclFilterTable": ruckusMacAclFilterTable,
       "ruckusMacAclFilterEntry": ruckusMacAclFilterEntry,
       "ruckusMacAclFilterSeqNum": ruckusMacAclFilterSeqNum,
       "ruckusMacAclFilterAction": ruckusMacAclFilterAction,
       "ruckusMacAclFilterSrcAddr": ruckusMacAclFilterSrcAddr,
       "ruckusMacAclFilterSrcMask": ruckusMacAclFilterSrcMask,
       "ruckusMacAclFilterDestAddr": ruckusMacAclFilterDestAddr,
       "ruckusMacAclFilterDestMask": ruckusMacAclFilterDestMask,
       "ruckusMacAclFilterEtherType": ruckusMacAclFilterEtherType,
       "ruckusMacAclFilterExtEtherType": ruckusMacAclFilterExtEtherType,
       "ruckusMacAclFilterMirrorPkts": ruckusMacAclFilterMirrorPkts,
       "ruckusMacAclFilterLogEnable": ruckusMacAclFilterLogEnable,
       "ruckusMacAclFilterRowStatus": ruckusMacAclFilterRowStatus,
       "ruckusAclBindings": ruckusAclBindings,
       "ruckusAclIfBindTable": ruckusAclIfBindTable,
       "ruckusAclIfBindEntry": ruckusAclIfBindEntry,
       "ruckusAclIfBindPort": ruckusAclIfBindPort,
       "ruckusAclIfBindType": ruckusAclIfBindType,
       "ruckusAclIfBindDirection": ruckusAclIfBindDirection,
       "ruckusAclIfBindName": ruckusAclIfBindName,
       "ruckusAclIfBindLog": ruckusAclIfBindLog,
       "ruckusAclIfBindRowStatus": ruckusAclIfBindRowStatus,
       "ruckusAclVlanBindTable": ruckusAclVlanBindTable,
       "ruckusAclVlanBindEntry": ruckusAclVlanBindEntry,
       "ruckusAclVlanBindId": ruckusAclVlanBindId,
       "ruckusAclVlanBindType": ruckusAclVlanBindType,
       "ruckusAclVlanBindDirection": ruckusAclVlanBindDirection,
       "ruckusAclVlanBindName": ruckusAclVlanBindName,
       "ruckusAclVlanBindLog": ruckusAclVlanBindLog,
       "ruckusAclVlanBindRowStatus": ruckusAclVlanBindRowStatus,
       "ruckusAclVPortBindTable": ruckusAclVPortBindTable,
       "ruckusAclVPortBindEntry": ruckusAclVPortBindEntry,
       "ruckusAclVPortBindId": ruckusAclVPortBindId,
       "ruckusAclVPortBindPort": ruckusAclVPortBindPort,
       "ruckusAclVPortBindType": ruckusAclVPortBindType,
       "ruckusAclVPortBindDirection": ruckusAclVPortBindDirection,
       "ruckusAclVPortBindName": ruckusAclVPortBindName,
       "ruckusAclVPortBindLog": ruckusAclVPortBindLog,
       "ruckusAclVPortBindRowStatus": ruckusAclVPortBindRowStatus,
       "ruckusAclConformance": ruckusAclConformance,
       "ruckusAclCompliances": ruckusAclCompliances,
       "ruckusAclCompliance": ruckusAclCompliance,
       "ruckusAclGroups": ruckusAclGroups,
       "ruckusAclGroup": ruckusAclGroup}
)
