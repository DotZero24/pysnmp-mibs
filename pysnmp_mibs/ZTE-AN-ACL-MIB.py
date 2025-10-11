# SNMP MIB module (ZTE-AN-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:51 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnAclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Operator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("eq", 1),
          ("neq", 2),
          ("lt", 3),
          ("gt", 4),
          ("range", 5))
    )



# MIB Managed Objects in the order of their OIDs

_ZxAnAclObjects_ObjectIdentity = ObjectIdentity
zxAnAclObjects = _ZxAnAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1)
)
_ZxAnAclGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnAclGlobalObjects = _ZxAnAclGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 1)
)
_ZxAnAclTable_Object = MibTable
zxAnAclTable = _ZxAnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnAclTable.setStatus("current")
_ZxAnAclEntry_Object = MibTableRow
zxAnAclEntry = _ZxAnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1)
)
zxAnAclEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclEntry.setStatus("current")


class _ZxAnAclIndex_Type(Integer32):
    """Custom type zxAnAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 349),
    )


_ZxAnAclIndex_Type.__name__ = "Integer32"
_ZxAnAclIndex_Object = MibTableColumn
zxAnAclIndex = _ZxAnAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 1),
    _ZxAnAclIndex_Type()
)
zxAnAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclIndex.setStatus("current")


class _ZxAnAclRuleId_Type(Integer32):
    """Custom type zxAnAclRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxAnAclRuleId_Type.__name__ = "Integer32"
_ZxAnAclRuleId_Object = MibTableColumn
zxAnAclRuleId = _ZxAnAclRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 2),
    _ZxAnAclRuleId_Type()
)
zxAnAclRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclRuleId.setStatus("current")


class _ZxAnAclAction_Type(Integer32):
    """Custom type zxAnAclAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_ZxAnAclAction_Type.__name__ = "Integer32"
_ZxAnAclAction_Object = MibTableColumn
zxAnAclAction = _ZxAnAclAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 3),
    _ZxAnAclAction_Type()
)
zxAnAclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclAction.setStatus("current")


class _ZxAnAclProtocolType_Type(Integer32):
    """Custom type zxAnAclProtocolType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              9,
              17,
              58,
              89,
              103,
              112,
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ipInIp", 4),
          ("tcp", 6),
          ("eigr", 8),
          ("igrp", 9),
          ("udp", 17),
          ("icmpv6", 58),
          ("ospf", 89),
          ("pim", 103),
          ("vrrp", 112),
          ("ip", 255))
    )


_ZxAnAclProtocolType_Type.__name__ = "Integer32"
_ZxAnAclProtocolType_Object = MibTableColumn
zxAnAclProtocolType = _ZxAnAclProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 4),
    _ZxAnAclProtocolType_Type()
)
zxAnAclProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclProtocolType.setStatus("current")
_ZxAnAclSrcIp_Type = IpAddress
_ZxAnAclSrcIp_Object = MibTableColumn
zxAnAclSrcIp = _ZxAnAclSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 5),
    _ZxAnAclSrcIp_Type()
)
zxAnAclSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclSrcIp.setStatus("current")
_ZxAnAclSrcIpWildcardMask_Type = IpAddress
_ZxAnAclSrcIpWildcardMask_Object = MibTableColumn
zxAnAclSrcIpWildcardMask = _ZxAnAclSrcIpWildcardMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 6),
    _ZxAnAclSrcIpWildcardMask_Type()
)
zxAnAclSrcIpWildcardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclSrcIpWildcardMask.setStatus("current")
_ZxAnAclDestIp_Type = IpAddress
_ZxAnAclDestIp_Object = MibTableColumn
zxAnAclDestIp = _ZxAnAclDestIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 7),
    _ZxAnAclDestIp_Type()
)
zxAnAclDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDestIp.setStatus("current")
_ZxAnAclDestIpWildcardMask_Type = IpAddress
_ZxAnAclDestIpWildcardMask_Object = MibTableColumn
zxAnAclDestIpWildcardMask = _ZxAnAclDestIpWildcardMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 8),
    _ZxAnAclDestIpWildcardMask_Type()
)
zxAnAclDestIpWildcardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDestIpWildcardMask.setStatus("current")


class _ZxAnAclSrcPortOperator_Type(Operator):
    """Custom type zxAnAclSrcPortOperator based on Operator"""
    defaultValue = 0


_ZxAnAclSrcPortOperator_Type.__name__ = "Operator"
_ZxAnAclSrcPortOperator_Object = MibTableColumn
zxAnAclSrcPortOperator = _ZxAnAclSrcPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 9),
    _ZxAnAclSrcPortOperator_Type()
)
zxAnAclSrcPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclSrcPortOperator.setStatus("current")


class _ZxAnAclSrcPortStart_Type(Integer32):
    """Custom type zxAnAclSrcPortStart based on Integer32"""
    defaultValue = 0


_ZxAnAclSrcPortStart_Type.__name__ = "Integer32"
_ZxAnAclSrcPortStart_Object = MibTableColumn
zxAnAclSrcPortStart = _ZxAnAclSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 10),
    _ZxAnAclSrcPortStart_Type()
)
zxAnAclSrcPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclSrcPortStart.setStatus("current")


class _ZxAnAclSrcPortEnd_Type(Integer32):
    """Custom type zxAnAclSrcPortEnd based on Integer32"""
    defaultValue = 0


_ZxAnAclSrcPortEnd_Type.__name__ = "Integer32"
_ZxAnAclSrcPortEnd_Object = MibTableColumn
zxAnAclSrcPortEnd = _ZxAnAclSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 11),
    _ZxAnAclSrcPortEnd_Type()
)
zxAnAclSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclSrcPortEnd.setStatus("current")


class _ZxAnAclDestPortOperator_Type(Operator):
    """Custom type zxAnAclDestPortOperator based on Operator"""
    defaultValue = 0


_ZxAnAclDestPortOperator_Type.__name__ = "Operator"
_ZxAnAclDestPortOperator_Object = MibTableColumn
zxAnAclDestPortOperator = _ZxAnAclDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 12),
    _ZxAnAclDestPortOperator_Type()
)
zxAnAclDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDestPortOperator.setStatus("current")


class _ZxAnAclDestPortStart_Type(Integer32):
    """Custom type zxAnAclDestPortStart based on Integer32"""
    defaultValue = 0


_ZxAnAclDestPortStart_Type.__name__ = "Integer32"
_ZxAnAclDestPortStart_Object = MibTableColumn
zxAnAclDestPortStart = _ZxAnAclDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 13),
    _ZxAnAclDestPortStart_Type()
)
zxAnAclDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDestPortStart.setStatus("current")


class _ZxAnAclDestPortEnd_Type(Integer32):
    """Custom type zxAnAclDestPortEnd based on Integer32"""
    defaultValue = 0


_ZxAnAclDestPortEnd_Type.__name__ = "Integer32"
_ZxAnAclDestPortEnd_Object = MibTableColumn
zxAnAclDestPortEnd = _ZxAnAclDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 14),
    _ZxAnAclDestPortEnd_Type()
)
zxAnAclDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDestPortEnd.setStatus("current")
_ZxAnAclInMAC_Type = MacAddress
_ZxAnAclInMAC_Object = MibTableColumn
zxAnAclInMAC = _ZxAnAclInMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 15),
    _ZxAnAclInMAC_Type()
)
zxAnAclInMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclInMAC.setStatus("current")
_ZxAnAclInMACWildcardMask_Type = MacAddress
_ZxAnAclInMACWildcardMask_Object = MibTableColumn
zxAnAclInMACWildcardMask = _ZxAnAclInMACWildcardMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 16),
    _ZxAnAclInMACWildcardMask_Type()
)
zxAnAclInMACWildcardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclInMACWildcardMask.setStatus("current")
_ZxAnAclOutMAC_Type = MacAddress
_ZxAnAclOutMAC_Object = MibTableColumn
zxAnAclOutMAC = _ZxAnAclOutMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 17),
    _ZxAnAclOutMAC_Type()
)
zxAnAclOutMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclOutMAC.setStatus("current")
_ZxAnAclOutMACWildcardMask_Type = MacAddress
_ZxAnAclOutMACWildcardMask_Object = MibTableColumn
zxAnAclOutMACWildcardMask = _ZxAnAclOutMACWildcardMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 18),
    _ZxAnAclOutMACWildcardMask_Type()
)
zxAnAclOutMACWildcardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclOutMACWildcardMask.setStatus("current")


class _ZxAnAclEthProtocol_Type(Integer32):
    """Custom type zxAnAclEthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2048,
              2054)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2048),
          ("arp", 2054))
    )


_ZxAnAclEthProtocol_Type.__name__ = "Integer32"
_ZxAnAclEthProtocol_Object = MibTableColumn
zxAnAclEthProtocol = _ZxAnAclEthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 19),
    _ZxAnAclEthProtocol_Type()
)
zxAnAclEthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclEthProtocol.setStatus("current")
_ZxAnAclVlanID_Type = Integer32
_ZxAnAclVlanID_Object = MibTableColumn
zxAnAclVlanID = _ZxAnAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 20),
    _ZxAnAclVlanID_Type()
)
zxAnAclVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclVlanID.setStatus("current")
_ZxAnAclVlanPri_Type = Integer32
_ZxAnAclVlanPri_Object = MibTableColumn
zxAnAclVlanPri = _ZxAnAclVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 21),
    _ZxAnAclVlanPri_Type()
)
zxAnAclVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclVlanPri.setStatus("current")
_ZxAnAclInnerVlan_Type = Integer32
_ZxAnAclInnerVlan_Object = MibTableColumn
zxAnAclInnerVlan = _ZxAnAclInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 22),
    _ZxAnAclInnerVlan_Type()
)
zxAnAclInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclInnerVlan.setStatus("current")


class _ZxAnAclInnerVlanPri_Type(Integer32):
    """Custom type zxAnAclInnerVlanPri based on Integer32"""
    defaultValue = 255


_ZxAnAclInnerVlanPri_Type.__name__ = "Integer32"
_ZxAnAclInnerVlanPri_Object = MibTableColumn
zxAnAclInnerVlanPri = _ZxAnAclInnerVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 23),
    _ZxAnAclInnerVlanPri_Type()
)
zxAnAclInnerVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclInnerVlanPri.setStatus("current")
_ZxAnAclMinVlanID_Type = Integer32
_ZxAnAclMinVlanID_Object = MibTableColumn
zxAnAclMinVlanID = _ZxAnAclMinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 24),
    _ZxAnAclMinVlanID_Type()
)
zxAnAclMinVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclMinVlanID.setStatus("current")
_ZxAnAclMaxVlanID_Type = Integer32
_ZxAnAclMaxVlanID_Object = MibTableColumn
zxAnAclMaxVlanID = _ZxAnAclMaxVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 25),
    _ZxAnAclMaxVlanID_Type()
)
zxAnAclMaxVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclMaxVlanID.setStatus("current")


class _ZxAnAclDscp_Type(Integer32):
    """Custom type zxAnAclDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnAclDscp_Type.__name__ = "Integer32"
_ZxAnAclDscp_Object = MibTableColumn
zxAnAclDscp = _ZxAnAclDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 26),
    _ZxAnAclDscp_Type()
)
zxAnAclDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclDscp.setStatus("current")
_ZxAnBasicAclRowStatus_Type = RowStatus
_ZxAnBasicAclRowStatus_Object = MibTableColumn
zxAnBasicAclRowStatus = _ZxAnBasicAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 2, 1, 50),
    _ZxAnBasicAclRowStatus_Type()
)
zxAnBasicAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBasicAclRowStatus.setStatus("current")
_ZxAnAclExTable_Object = MibTable
zxAnAclExTable = _ZxAnAclExTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnAclExTable.setStatus("current")
_ZxAnAclExEntry_Object = MibTableRow
zxAnAclExEntry = _ZxAnAclExEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1)
)
zxAnAclExEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclExEntry.setStatus("current")


class _ZxAnAclExIndex_Type(Integer32):
    """Custom type zxAnAclExIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 199),
    )


_ZxAnAclExIndex_Type.__name__ = "Integer32"
_ZxAnAclExIndex_Object = MibTableColumn
zxAnAclExIndex = _ZxAnAclExIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 1),
    _ZxAnAclExIndex_Type()
)
zxAnAclExIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclExIndex.setStatus("current")


class _ZxAnAclExRuleId_Type(Integer32):
    """Custom type zxAnAclExRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxAnAclExRuleId_Type.__name__ = "Integer32"
_ZxAnAclExRuleId_Object = MibTableColumn
zxAnAclExRuleId = _ZxAnAclExRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 2),
    _ZxAnAclExRuleId_Type()
)
zxAnAclExRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclExRuleId.setStatus("current")


class _ZxAnAclExTos_Type(Integer32):
    """Custom type zxAnAclExTos based on Integer32"""
    defaultValue = 255


_ZxAnAclExTos_Type.__name__ = "Integer32"
_ZxAnAclExTos_Object = MibTableColumn
zxAnAclExTos = _ZxAnAclExTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 3),
    _ZxAnAclExTos_Type()
)
zxAnAclExTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExTos.setStatus("current")


class _ZxAnAclExDscp_Type(Integer32):
    """Custom type zxAnAclExDscp based on Integer32"""
    defaultValue = 255


_ZxAnAclExDscp_Type.__name__ = "Integer32"
_ZxAnAclExDscp_Object = MibTableColumn
zxAnAclExDscp = _ZxAnAclExDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 4),
    _ZxAnAclExDscp_Type()
)
zxAnAclExDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExDscp.setStatus("current")


class _ZxAnAclExAction_Type(Integer32):
    """Custom type zxAnAclExAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_ZxAnAclExAction_Type.__name__ = "Integer32"
_ZxAnAclExAction_Object = MibTableColumn
zxAnAclExAction = _ZxAnAclExAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 5),
    _ZxAnAclExAction_Type()
)
zxAnAclExAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExAction.setStatus("current")


class _ZxAnAclTtl_Type(Integer32):
    """Custom type zxAnAclTtl based on Integer32"""
    defaultValue = 65535


_ZxAnAclTtl_Type.__name__ = "Integer32"
_ZxAnAclTtl_Object = MibTableColumn
zxAnAclTtl = _ZxAnAclTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 6),
    _ZxAnAclTtl_Type()
)
zxAnAclTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclTtl.setStatus("current")
_ZxAnAclExRowStatus_Type = RowStatus
_ZxAnAclExRowStatus_Object = MibTableColumn
zxAnAclExRowStatus = _ZxAnAclExRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 3, 1, 50),
    _ZxAnAclExRowStatus_Type()
)
zxAnAclExRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExRowStatus.setStatus("current")
_ZxAnAclQosTrafficTable_Object = MibTable
zxAnAclQosTrafficTable = _ZxAnAclQosTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnAclQosTrafficTable.setStatus("current")
_ZxAnAclQosTrafficEntry_Object = MibTableRow
zxAnAclQosTrafficEntry = _ZxAnAclQosTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1)
)
zxAnAclQosTrafficEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclQosTrafficEntry.setStatus("current")


class _ZxAnAclQosTrafficLimitCir_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnAclQosTrafficLimitCir_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitCir_Object = MibTableColumn
zxAnAclQosTrafficLimitCir = _ZxAnAclQosTrafficLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 1),
    _ZxAnAclQosTrafficLimitCir_Type()
)
zxAnAclQosTrafficLimitCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitCir.setStatus("current")


class _ZxAnAclQosTrafficLimitPir_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnAclQosTrafficLimitPir_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitPir_Object = MibTableColumn
zxAnAclQosTrafficLimitPir = _ZxAnAclQosTrafficLimitPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 2),
    _ZxAnAclQosTrafficLimitPir_Type()
)
zxAnAclQosTrafficLimitPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitPir.setStatus("current")


class _ZxAnAclQosTrafficLimitCbs_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16000),
    )


_ZxAnAclQosTrafficLimitCbs_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitCbs_Object = MibTableColumn
zxAnAclQosTrafficLimitCbs = _ZxAnAclQosTrafficLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 3),
    _ZxAnAclQosTrafficLimitCbs_Type()
)
zxAnAclQosTrafficLimitCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitCbs.setStatus("current")


class _ZxAnAclQosTrafficLimitEbs_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnAclQosTrafficLimitEbs_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitEbs_Object = MibTableColumn
zxAnAclQosTrafficLimitEbs = _ZxAnAclQosTrafficLimitEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 4),
    _ZxAnAclQosTrafficLimitEbs_Type()
)
zxAnAclQosTrafficLimitEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitEbs.setStatus("current")


class _ZxAnAclQosTrafficLimitPbs_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnAclQosTrafficLimitPbs_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitPbs_Object = MibTableColumn
zxAnAclQosTrafficLimitPbs = _ZxAnAclQosTrafficLimitPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 5),
    _ZxAnAclQosTrafficLimitPbs_Type()
)
zxAnAclQosTrafficLimitPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitPbs.setStatus("current")


class _ZxAnAclQosTrafficLimitMode_Type(Integer32):
    """Custom type zxAnAclQosTrafficLimitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blind", 1),
          ("aware", 2))
    )


_ZxAnAclQosTrafficLimitMode_Type.__name__ = "Integer32"
_ZxAnAclQosTrafficLimitMode_Object = MibTableColumn
zxAnAclQosTrafficLimitMode = _ZxAnAclQosTrafficLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 6),
    _ZxAnAclQosTrafficLimitMode_Type()
)
zxAnAclQosTrafficLimitMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficLimitMode.setStatus("current")
_ZxAnAclQosTrafficRowStatus_Type = RowStatus
_ZxAnAclQosTrafficRowStatus_Object = MibTableColumn
zxAnAclQosTrafficRowStatus = _ZxAnAclQosTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 4, 1, 30),
    _ZxAnAclQosTrafficRowStatus_Type()
)
zxAnAclQosTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosTrafficRowStatus.setStatus("current")
_ZxAnAclQosPriorityMarkTable_Object = MibTable
zxAnAclQosPriorityMarkTable = _ZxAnAclQosPriorityMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnAclQosPriorityMarkTable.setStatus("current")
_ZxAnAclQosPriorityMarkEntry_Object = MibTableRow
zxAnAclQosPriorityMarkEntry = _ZxAnAclQosPriorityMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 5, 1)
)
zxAnAclQosPriorityMarkEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclExRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclQosPriorityMarkEntry.setStatus("current")


class _ZxAnAclQosPriMarkDscp_Type(Integer32):
    """Custom type zxAnAclQosPriMarkDscp based on Integer32"""
    defaultValue = 255


_ZxAnAclQosPriMarkDscp_Type.__name__ = "Integer32"
_ZxAnAclQosPriMarkDscp_Object = MibTableColumn
zxAnAclQosPriMarkDscp = _ZxAnAclQosPriMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 5, 1, 1),
    _ZxAnAclQosPriMarkDscp_Type()
)
zxAnAclQosPriMarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosPriMarkDscp.setStatus("current")


class _ZxAnAclQosPriMarkUserPriority_Type(Integer32):
    """Custom type zxAnAclQosPriMarkUserPriority based on Integer32"""
    defaultValue = 255


_ZxAnAclQosPriMarkUserPriority_Type.__name__ = "Integer32"
_ZxAnAclQosPriMarkUserPriority_Object = MibTableColumn
zxAnAclQosPriMarkUserPriority = _ZxAnAclQosPriMarkUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 5, 1, 2),
    _ZxAnAclQosPriMarkUserPriority_Type()
)
zxAnAclQosPriMarkUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosPriMarkUserPriority.setStatus("current")
_ZxAnAclQosPriMarkRowStatus_Type = RowStatus
_ZxAnAclQosPriMarkRowStatus_Object = MibTableColumn
zxAnAclQosPriMarkRowStatus = _ZxAnAclQosPriMarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 5, 1, 30),
    _ZxAnAclQosPriMarkRowStatus_Type()
)
zxAnAclQosPriMarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosPriMarkRowStatus.setStatus("current")
_ZxAnAclQosStatisticTable_Object = MibTable
zxAnAclQosStatisticTable = _ZxAnAclQosStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnAclQosStatisticTable.setStatus("current")
_ZxAnAclQosStatisticEntry_Object = MibTableRow
zxAnAclQosStatisticEntry = _ZxAnAclQosStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 6, 1)
)
zxAnAclQosStatisticEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclQosStatisticEntry.setStatus("current")
_ZxAnAclQosStatistInPkg_Type = Counter32
_ZxAnAclQosStatistInPkg_Object = MibTableColumn
zxAnAclQosStatistInPkg = _ZxAnAclQosStatistInPkg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 6, 1, 1),
    _ZxAnAclQosStatistInPkg_Type()
)
zxAnAclQosStatistInPkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAclQosStatistInPkg.setStatus("current")
_ZxAnAclQosStatistRowStatus_Type = RowStatus
_ZxAnAclQosStatistRowStatus_Object = MibTableColumn
zxAnAclQosStatistRowStatus = _ZxAnAclQosStatistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 6, 1, 50),
    _ZxAnAclQosStatistRowStatus_Type()
)
zxAnAclQosStatistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosStatistRowStatus.setStatus("current")
_ZxAnAclQosQinqTable_Object = MibTable
zxAnAclQosQinqTable = _ZxAnAclQosQinqTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnAclQosQinqTable.setStatus("current")
_ZxAnAclQosQinqEntry_Object = MibTableRow
zxAnAclQosQinqEntry = _ZxAnAclQosQinqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 7, 1)
)
zxAnAclQosQinqEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclQosQinqEntry.setStatus("current")
_ZxAnAclQosQinqSvlan_Type = Integer32
_ZxAnAclQosQinqSvlan_Object = MibTableColumn
zxAnAclQosQinqSvlan = _ZxAnAclQosQinqSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 7, 1, 1),
    _ZxAnAclQosQinqSvlan_Type()
)
zxAnAclQosQinqSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosQinqSvlan.setStatus("current")
_ZxAnAclQosQinqCvlan_Type = Integer32
_ZxAnAclQosQinqCvlan_Object = MibTableColumn
zxAnAclQosQinqCvlan = _ZxAnAclQosQinqCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 7, 1, 2),
    _ZxAnAclQosQinqCvlan_Type()
)
zxAnAclQosQinqCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosQinqCvlan.setStatus("current")
_ZxAnAclQosQinqRowStatus_Type = RowStatus
_ZxAnAclQosQinqRowStatus_Object = MibTableColumn
zxAnAclQosQinqRowStatus = _ZxAnAclQosQinqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 7, 1, 30),
    _ZxAnAclQosQinqRowStatus_Type()
)
zxAnAclQosQinqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosQinqRowStatus.setStatus("current")
_ZxAnAclQosRedirectTable_Object = MibTable
zxAnAclQosRedirectTable = _ZxAnAclQosRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnAclQosRedirectTable.setStatus("current")
_ZxAnAclQosRedirectEntry_Object = MibTableRow
zxAnAclQosRedirectEntry = _ZxAnAclQosRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1)
)
zxAnAclQosRedirectEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnAclIndex"),
    (0, "ZTE-AN-ACL-MIB", "zxAnAclRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclQosRedirectEntry.setStatus("current")


class _ZxAnAclQosRedirectMode_Type(Integer32):
    """Custom type zxAnAclQosRedirectMode based on Integer32"""
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
        *(("cpu", 1),
          ("interface", 2),
          ("nextHop", 3))
    )


_ZxAnAclQosRedirectMode_Type.__name__ = "Integer32"
_ZxAnAclQosRedirectMode_Object = MibTableColumn
zxAnAclQosRedirectMode = _ZxAnAclQosRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1, 1),
    _ZxAnAclQosRedirectMode_Type()
)
zxAnAclQosRedirectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosRedirectMode.setStatus("current")


class _ZxAnAclQosRedirectPktLimit_Type(Integer32):
    """Custom type zxAnAclQosRedirectPktLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnAclQosRedirectPktLimit_Type.__name__ = "Integer32"
_ZxAnAclQosRedirectPktLimit_Object = MibTableColumn
zxAnAclQosRedirectPktLimit = _ZxAnAclQosRedirectPktLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1, 2),
    _ZxAnAclQosRedirectPktLimit_Type()
)
zxAnAclQosRedirectPktLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosRedirectPktLimit.setStatus("current")
_ZxAnAclQosRedirectInterface_Type = ZxAnIfindex
_ZxAnAclQosRedirectInterface_Object = MibTableColumn
zxAnAclQosRedirectInterface = _ZxAnAclQosRedirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1, 3),
    _ZxAnAclQosRedirectInterface_Type()
)
zxAnAclQosRedirectInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosRedirectInterface.setStatus("current")
_ZxAnAclQosRedirectIpAddress_Type = IpAddress
_ZxAnAclQosRedirectIpAddress_Object = MibTableColumn
zxAnAclQosRedirectIpAddress = _ZxAnAclQosRedirectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1, 4),
    _ZxAnAclQosRedirectIpAddress_Type()
)
zxAnAclQosRedirectIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosRedirectIpAddress.setStatus("current")
_ZxAnAclQosRedirectRowStatus_Type = RowStatus
_ZxAnAclQosRedirectRowStatus_Object = MibTableColumn
zxAnAclQosRedirectRowStatus = _ZxAnAclQosRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 8, 1, 30),
    _ZxAnAclQosRedirectRowStatus_Type()
)
zxAnAclQosRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclQosRedirectRowStatus.setStatus("current")
_ZxAnUniAclClassTable_Object = MibTable
zxAnUniAclClassTable = _ZxAnUniAclClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnUniAclClassTable.setStatus("current")
_ZxAnUniAclClassEntry_Object = MibTableRow
zxAnUniAclClassEntry = _ZxAnUniAclClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 11, 1)
)
zxAnUniAclClassEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnUniAclClassName"),
)
if mibBuilder.loadTexts:
    zxAnUniAclClassEntry.setStatus("current")


class _ZxAnUniAclClassName_Type(DisplayString):
    """Custom type zxAnUniAclClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnUniAclClassName_Type.__name__ = "DisplayString"
_ZxAnUniAclClassName_Object = MibTableColumn
zxAnUniAclClassName = _ZxAnUniAclClassName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 11, 1, 1),
    _ZxAnUniAclClassName_Type()
)
zxAnUniAclClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUniAclClassName.setStatus("current")


class _ZxAnUniAclClassMatch_Type(DisplayString):
    """Custom type zxAnUniAclClassMatch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZxAnUniAclClassMatch_Type.__name__ = "DisplayString"
_ZxAnUniAclClassMatch_Object = MibTableColumn
zxAnUniAclClassMatch = _ZxAnUniAclClassMatch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 11, 1, 2),
    _ZxAnUniAclClassMatch_Type()
)
zxAnUniAclClassMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclClassMatch.setStatus("current")
_ZxAnUniAclClassRowStatus_Type = RowStatus
_ZxAnUniAclClassRowStatus_Object = MibTableColumn
zxAnUniAclClassRowStatus = _ZxAnUniAclClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 11, 1, 50),
    _ZxAnUniAclClassRowStatus_Type()
)
zxAnUniAclClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclClassRowStatus.setStatus("current")
_ZxAnUniAclPolicyTable_Object = MibTable
zxAnUniAclPolicyTable = _ZxAnUniAclPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 12)
)
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTable.setStatus("current")
_ZxAnUniAclPolicyEntry_Object = MibTableRow
zxAnUniAclPolicyEntry = _ZxAnUniAclPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 12, 1)
)
zxAnUniAclPolicyEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnUniAclPolicyName"),
)
if mibBuilder.loadTexts:
    zxAnUniAclPolicyEntry.setStatus("current")


class _ZxAnUniAclPolicyName_Type(DisplayString):
    """Custom type zxAnUniAclPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnUniAclPolicyName_Type.__name__ = "DisplayString"
_ZxAnUniAclPolicyName_Object = MibTableColumn
zxAnUniAclPolicyName = _ZxAnUniAclPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 12, 1, 1),
    _ZxAnUniAclPolicyName_Type()
)
zxAnUniAclPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyName.setStatus("current")
_ZxAnUniAclPolicyRowStatus_Type = RowStatus
_ZxAnUniAclPolicyRowStatus_Object = MibTableColumn
zxAnUniAclPolicyRowStatus = _ZxAnUniAclPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 12, 1, 50),
    _ZxAnUniAclPolicyRowStatus_Type()
)
zxAnUniAclPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyRowStatus.setStatus("current")
_ZxAnUniAclPolicyConfigTable_Object = MibTable
zxAnUniAclPolicyConfigTable = _ZxAnUniAclPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13)
)
if mibBuilder.loadTexts:
    zxAnUniAclPolicyConfigTable.setStatus("current")
_ZxAnUniAclPolicyConfigEntry_Object = MibTableRow
zxAnUniAclPolicyConfigEntry = _ZxAnUniAclPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1)
)
zxAnUniAclPolicyConfigEntry.setIndexNames(
    (0, "ZTE-AN-ACL-MIB", "zxAnUniAclPolicyName"),
    (0, "ZTE-AN-ACL-MIB", "zxAnUniAclClassName"),
)
if mibBuilder.loadTexts:
    zxAnUniAclPolicyConfigEntry.setStatus("current")


class _ZxAnUniAclPolicyAction_Type(Integer32):
    """Custom type zxAnUniAclPolicyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_ZxAnUniAclPolicyAction_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyAction_Object = MibTableColumn
zxAnUniAclPolicyAction = _ZxAnUniAclPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 1),
    _ZxAnUniAclPolicyAction_Type()
)
zxAnUniAclPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyAction.setStatus("current")
_ZxAnUniAclPolicyCir_Type = Integer32
_ZxAnUniAclPolicyCir_Object = MibTableColumn
zxAnUniAclPolicyCir = _ZxAnUniAclPolicyCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 2),
    _ZxAnUniAclPolicyCir_Type()
)
zxAnUniAclPolicyCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyCir.setStatus("current")
_ZxAnUniAclPolicyCbs_Type = Integer32
_ZxAnUniAclPolicyCbs_Object = MibTableColumn
zxAnUniAclPolicyCbs = _ZxAnUniAclPolicyCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 3),
    _ZxAnUniAclPolicyCbs_Type()
)
zxAnUniAclPolicyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyCbs.setStatus("current")


class _ZxAnUniAclPolicyExceedAction_Type(Integer32):
    """Custom type zxAnUniAclPolicyExceedAction based on Integer32"""
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
        *(("drop", 1),
          ("setDSCP", 2),
          ("setCos", 3))
    )


_ZxAnUniAclPolicyExceedAction_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyExceedAction_Object = MibTableColumn
zxAnUniAclPolicyExceedAction = _ZxAnUniAclPolicyExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 4),
    _ZxAnUniAclPolicyExceedAction_Type()
)
zxAnUniAclPolicyExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyExceedAction.setStatus("current")
_ZxAnUniAclPolicyExceedActValue_Type = Integer32
_ZxAnUniAclPolicyExceedActValue_Object = MibTableColumn
zxAnUniAclPolicyExceedActValue = _ZxAnUniAclPolicyExceedActValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 5),
    _ZxAnUniAclPolicyExceedActValue_Type()
)
zxAnUniAclPolicyExceedActValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyExceedActValue.setStatus("current")


class _ZxAnUniAclPolicyActionSCos_Type(Integer32):
    """Custom type zxAnUniAclPolicyActionSCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnUniAclPolicyActionSCos_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyActionSCos_Object = MibTableColumn
zxAnUniAclPolicyActionSCos = _ZxAnUniAclPolicyActionSCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 6),
    _ZxAnUniAclPolicyActionSCos_Type()
)
zxAnUniAclPolicyActionSCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionSCos.setStatus("current")


class _ZxAnUniAclPolicyActionDSCP_Type(Integer32):
    """Custom type zxAnUniAclPolicyActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnUniAclPolicyActionDSCP_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyActionDSCP_Object = MibTableColumn
zxAnUniAclPolicyActionDSCP = _ZxAnUniAclPolicyActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 7),
    _ZxAnUniAclPolicyActionDSCP_Type()
)
zxAnUniAclPolicyActionDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionDSCP.setStatus("current")


class _ZxAnUniAclPolicyActionVLAN_Type(Integer32):
    """Custom type zxAnUniAclPolicyActionVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnUniAclPolicyActionVLAN_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyActionVLAN_Object = MibTableColumn
zxAnUniAclPolicyActionVLAN = _ZxAnUniAclPolicyActionVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 8),
    _ZxAnUniAclPolicyActionVLAN_Type()
)
zxAnUniAclPolicyActionVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionVLAN.setStatus("current")
_ZxAnUniAclPolicyActionRedirectedTo_Type = Integer32
_ZxAnUniAclPolicyActionRedirectedTo_Object = MibTableColumn
zxAnUniAclPolicyActionRedirectedTo = _ZxAnUniAclPolicyActionRedirectedTo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 9),
    _ZxAnUniAclPolicyActionRedirectedTo_Type()
)
zxAnUniAclPolicyActionRedirectedTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionRedirectedTo.setStatus("current")
_ZxAnUniAclPolicyActionMirroredTo_Type = Integer32
_ZxAnUniAclPolicyActionMirroredTo_Object = MibTableColumn
zxAnUniAclPolicyActionMirroredTo = _ZxAnUniAclPolicyActionMirroredTo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 10),
    _ZxAnUniAclPolicyActionMirroredTo_Type()
)
zxAnUniAclPolicyActionMirroredTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionMirroredTo.setStatus("current")


class _ZxAnUniAclPolicyActionISStatistics_Type(Integer32):
    """Custom type zxAnUniAclPolicyActionISStatistics based on Integer32"""
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


_ZxAnUniAclPolicyActionISStatistics_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyActionISStatistics_Object = MibTableColumn
zxAnUniAclPolicyActionISStatistics = _ZxAnUniAclPolicyActionISStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 11),
    _ZxAnUniAclPolicyActionISStatistics_Type()
)
zxAnUniAclPolicyActionISStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionISStatistics.setStatus("current")


class _ZxAnUniAclPolicyActionCCos_Type(Integer32):
    """Custom type zxAnUniAclPolicyActionCCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnUniAclPolicyActionCCos_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyActionCCos_Object = MibTableColumn
zxAnUniAclPolicyActionCCos = _ZxAnUniAclPolicyActionCCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 12),
    _ZxAnUniAclPolicyActionCCos_Type()
)
zxAnUniAclPolicyActionCCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyActionCCos.setStatus("current")


class _ZxAnUniAclPolicyPir_Type(Integer32):
    """Custom type zxAnUniAclPolicyPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 128000),
    )


_ZxAnUniAclPolicyPir_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyPir_Object = MibTableColumn
zxAnUniAclPolicyPir = _ZxAnUniAclPolicyPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 13),
    _ZxAnUniAclPolicyPir_Type()
)
zxAnUniAclPolicyPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyPir.setStatus("current")


class _ZxAnUniAclPolicyPbs_Type(Integer32):
    """Custom type zxAnUniAclPolicyPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2047),
    )


_ZxAnUniAclPolicyPbs_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyPbs_Object = MibTableColumn
zxAnUniAclPolicyPbs = _ZxAnUniAclPolicyPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 14),
    _ZxAnUniAclPolicyPbs_Type()
)
zxAnUniAclPolicyPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyPbs.setStatus("current")


class _ZxAnUniAclPolicyTrtcmExceedAction_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmExceedAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-286331154,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", -286331154),
          ("dropYellow", 1),
          ("forwardRed", 2))
    )


_ZxAnUniAclPolicyTrtcmExceedAction_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmExceedAction_Object = MibTableColumn
zxAnUniAclPolicyTrtcmExceedAction = _ZxAnUniAclPolicyTrtcmExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 15),
    _ZxAnUniAclPolicyTrtcmExceedAction_Type()
)
zxAnUniAclPolicyTrtcmExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmExceedAction.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkRedDscp_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkRedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnUniAclPolicyTrtcmRemarkRedDscp_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkRedDscp_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkRedDscp = _ZxAnUniAclPolicyTrtcmRemarkRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 16),
    _ZxAnUniAclPolicyTrtcmRemarkRedDscp_Type()
)
zxAnUniAclPolicyTrtcmRemarkRedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkRedDscp.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkYellowDscp_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkYellowDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnUniAclPolicyTrtcmRemarkYellowDscp_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkYellowDscp_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkYellowDscp = _ZxAnUniAclPolicyTrtcmRemarkYellowDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 17),
    _ZxAnUniAclPolicyTrtcmRemarkYellowDscp_Type()
)
zxAnUniAclPolicyTrtcmRemarkYellowDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkYellowDscp.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkGreenDscp_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkGreenDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnUniAclPolicyTrtcmRemarkGreenDscp_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkGreenDscp_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkGreenDscp = _ZxAnUniAclPolicyTrtcmRemarkGreenDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 18),
    _ZxAnUniAclPolicyTrtcmRemarkGreenDscp_Type()
)
zxAnUniAclPolicyTrtcmRemarkGreenDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkGreenDscp.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkRedCos_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkRedCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnUniAclPolicyTrtcmRemarkRedCos_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkRedCos_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkRedCos = _ZxAnUniAclPolicyTrtcmRemarkRedCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 19),
    _ZxAnUniAclPolicyTrtcmRemarkRedCos_Type()
)
zxAnUniAclPolicyTrtcmRemarkRedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkRedCos.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkYellowCos_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkYellowCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnUniAclPolicyTrtcmRemarkYellowCos_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkYellowCos_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkYellowCos = _ZxAnUniAclPolicyTrtcmRemarkYellowCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 20),
    _ZxAnUniAclPolicyTrtcmRemarkYellowCos_Type()
)
zxAnUniAclPolicyTrtcmRemarkYellowCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkYellowCos.setStatus("current")


class _ZxAnUniAclPolicyTrtcmRemarkGreenCos_Type(Integer32):
    """Custom type zxAnUniAclPolicyTrtcmRemarkGreenCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnUniAclPolicyTrtcmRemarkGreenCos_Type.__name__ = "Integer32"
_ZxAnUniAclPolicyTrtcmRemarkGreenCos_Object = MibTableColumn
zxAnUniAclPolicyTrtcmRemarkGreenCos = _ZxAnUniAclPolicyTrtcmRemarkGreenCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 21),
    _ZxAnUniAclPolicyTrtcmRemarkGreenCos_Type()
)
zxAnUniAclPolicyTrtcmRemarkGreenCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyTrtcmRemarkGreenCos.setStatus("current")
_ZxAnUniAclPolicyStatus_Type = RowStatus
_ZxAnUniAclPolicyStatus_Object = MibTableColumn
zxAnUniAclPolicyStatus = _ZxAnUniAclPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 13, 1, 50),
    _ZxAnUniAclPolicyStatus_Type()
)
zxAnUniAclPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclPolicyStatus.setStatus("current")
_ZxAnUniAclBindTable_Object = MibTable
zxAnUniAclBindTable = _ZxAnUniAclBindTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 14)
)
if mibBuilder.loadTexts:
    zxAnUniAclBindTable.setStatus("current")
_ZxAnUniAclBindEntry_Object = MibTableRow
zxAnUniAclBindEntry = _ZxAnUniAclBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 14, 1)
)
zxAnUniAclBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnUniAclBindEntry.setStatus("current")


class _ZxAnUniIfAclPolicyName_Type(DisplayString):
    """Custom type zxAnUniIfAclPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnUniIfAclPolicyName_Type.__name__ = "DisplayString"
_ZxAnUniIfAclPolicyName_Object = MibTableColumn
zxAnUniIfAclPolicyName = _ZxAnUniIfAclPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 14, 1, 1),
    _ZxAnUniIfAclPolicyName_Type()
)
zxAnUniIfAclPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniIfAclPolicyName.setStatus("current")


class _ZxAnUniAclBindDir_Type(Integer32):
    """Custom type zxAnUniAclBindDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_ZxAnUniAclBindDir_Type.__name__ = "Integer32"
_ZxAnUniAclBindDir_Object = MibTableColumn
zxAnUniAclBindDir = _ZxAnUniAclBindDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 14, 1, 2),
    _ZxAnUniAclBindDir_Type()
)
zxAnUniAclBindDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclBindDir.setStatus("current")
_ZxAnUniAclBindRowStatus_Type = RowStatus
_ZxAnUniAclBindRowStatus_Object = MibTableColumn
zxAnUniAclBindRowStatus = _ZxAnUniAclBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 1, 14, 1, 50),
    _ZxAnUniAclBindRowStatus_Type()
)
zxAnUniAclBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUniAclBindRowStatus.setStatus("current")
_ZxAnAclTrapObjects_ObjectIdentity = ObjectIdentity
zxAnAclTrapObjects = _ZxAnAclTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 23, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ACL-MIB",
    **{"Operator": Operator,
       "zxAnAclMib": zxAnAclMib,
       "zxAnAclObjects": zxAnAclObjects,
       "zxAnAclGlobalObjects": zxAnAclGlobalObjects,
       "zxAnAclTable": zxAnAclTable,
       "zxAnAclEntry": zxAnAclEntry,
       "zxAnAclIndex": zxAnAclIndex,
       "zxAnAclRuleId": zxAnAclRuleId,
       "zxAnAclAction": zxAnAclAction,
       "zxAnAclProtocolType": zxAnAclProtocolType,
       "zxAnAclSrcIp": zxAnAclSrcIp,
       "zxAnAclSrcIpWildcardMask": zxAnAclSrcIpWildcardMask,
       "zxAnAclDestIp": zxAnAclDestIp,
       "zxAnAclDestIpWildcardMask": zxAnAclDestIpWildcardMask,
       "zxAnAclSrcPortOperator": zxAnAclSrcPortOperator,
       "zxAnAclSrcPortStart": zxAnAclSrcPortStart,
       "zxAnAclSrcPortEnd": zxAnAclSrcPortEnd,
       "zxAnAclDestPortOperator": zxAnAclDestPortOperator,
       "zxAnAclDestPortStart": zxAnAclDestPortStart,
       "zxAnAclDestPortEnd": zxAnAclDestPortEnd,
       "zxAnAclInMAC": zxAnAclInMAC,
       "zxAnAclInMACWildcardMask": zxAnAclInMACWildcardMask,
       "zxAnAclOutMAC": zxAnAclOutMAC,
       "zxAnAclOutMACWildcardMask": zxAnAclOutMACWildcardMask,
       "zxAnAclEthProtocol": zxAnAclEthProtocol,
       "zxAnAclVlanID": zxAnAclVlanID,
       "zxAnAclVlanPri": zxAnAclVlanPri,
       "zxAnAclInnerVlan": zxAnAclInnerVlan,
       "zxAnAclInnerVlanPri": zxAnAclInnerVlanPri,
       "zxAnAclMinVlanID": zxAnAclMinVlanID,
       "zxAnAclMaxVlanID": zxAnAclMaxVlanID,
       "zxAnAclDscp": zxAnAclDscp,
       "zxAnBasicAclRowStatus": zxAnBasicAclRowStatus,
       "zxAnAclExTable": zxAnAclExTable,
       "zxAnAclExEntry": zxAnAclExEntry,
       "zxAnAclExIndex": zxAnAclExIndex,
       "zxAnAclExRuleId": zxAnAclExRuleId,
       "zxAnAclExTos": zxAnAclExTos,
       "zxAnAclExDscp": zxAnAclExDscp,
       "zxAnAclExAction": zxAnAclExAction,
       "zxAnAclTtl": zxAnAclTtl,
       "zxAnAclExRowStatus": zxAnAclExRowStatus,
       "zxAnAclQosTrafficTable": zxAnAclQosTrafficTable,
       "zxAnAclQosTrafficEntry": zxAnAclQosTrafficEntry,
       "zxAnAclQosTrafficLimitCir": zxAnAclQosTrafficLimitCir,
       "zxAnAclQosTrafficLimitPir": zxAnAclQosTrafficLimitPir,
       "zxAnAclQosTrafficLimitCbs": zxAnAclQosTrafficLimitCbs,
       "zxAnAclQosTrafficLimitEbs": zxAnAclQosTrafficLimitEbs,
       "zxAnAclQosTrafficLimitPbs": zxAnAclQosTrafficLimitPbs,
       "zxAnAclQosTrafficLimitMode": zxAnAclQosTrafficLimitMode,
       "zxAnAclQosTrafficRowStatus": zxAnAclQosTrafficRowStatus,
       "zxAnAclQosPriorityMarkTable": zxAnAclQosPriorityMarkTable,
       "zxAnAclQosPriorityMarkEntry": zxAnAclQosPriorityMarkEntry,
       "zxAnAclQosPriMarkDscp": zxAnAclQosPriMarkDscp,
       "zxAnAclQosPriMarkUserPriority": zxAnAclQosPriMarkUserPriority,
       "zxAnAclQosPriMarkRowStatus": zxAnAclQosPriMarkRowStatus,
       "zxAnAclQosStatisticTable": zxAnAclQosStatisticTable,
       "zxAnAclQosStatisticEntry": zxAnAclQosStatisticEntry,
       "zxAnAclQosStatistInPkg": zxAnAclQosStatistInPkg,
       "zxAnAclQosStatistRowStatus": zxAnAclQosStatistRowStatus,
       "zxAnAclQosQinqTable": zxAnAclQosQinqTable,
       "zxAnAclQosQinqEntry": zxAnAclQosQinqEntry,
       "zxAnAclQosQinqSvlan": zxAnAclQosQinqSvlan,
       "zxAnAclQosQinqCvlan": zxAnAclQosQinqCvlan,
       "zxAnAclQosQinqRowStatus": zxAnAclQosQinqRowStatus,
       "zxAnAclQosRedirectTable": zxAnAclQosRedirectTable,
       "zxAnAclQosRedirectEntry": zxAnAclQosRedirectEntry,
       "zxAnAclQosRedirectMode": zxAnAclQosRedirectMode,
       "zxAnAclQosRedirectPktLimit": zxAnAclQosRedirectPktLimit,
       "zxAnAclQosRedirectInterface": zxAnAclQosRedirectInterface,
       "zxAnAclQosRedirectIpAddress": zxAnAclQosRedirectIpAddress,
       "zxAnAclQosRedirectRowStatus": zxAnAclQosRedirectRowStatus,
       "zxAnUniAclClassTable": zxAnUniAclClassTable,
       "zxAnUniAclClassEntry": zxAnUniAclClassEntry,
       "zxAnUniAclClassName": zxAnUniAclClassName,
       "zxAnUniAclClassMatch": zxAnUniAclClassMatch,
       "zxAnUniAclClassRowStatus": zxAnUniAclClassRowStatus,
       "zxAnUniAclPolicyTable": zxAnUniAclPolicyTable,
       "zxAnUniAclPolicyEntry": zxAnUniAclPolicyEntry,
       "zxAnUniAclPolicyName": zxAnUniAclPolicyName,
       "zxAnUniAclPolicyRowStatus": zxAnUniAclPolicyRowStatus,
       "zxAnUniAclPolicyConfigTable": zxAnUniAclPolicyConfigTable,
       "zxAnUniAclPolicyConfigEntry": zxAnUniAclPolicyConfigEntry,
       "zxAnUniAclPolicyAction": zxAnUniAclPolicyAction,
       "zxAnUniAclPolicyCir": zxAnUniAclPolicyCir,
       "zxAnUniAclPolicyCbs": zxAnUniAclPolicyCbs,
       "zxAnUniAclPolicyExceedAction": zxAnUniAclPolicyExceedAction,
       "zxAnUniAclPolicyExceedActValue": zxAnUniAclPolicyExceedActValue,
       "zxAnUniAclPolicyActionSCos": zxAnUniAclPolicyActionSCos,
       "zxAnUniAclPolicyActionDSCP": zxAnUniAclPolicyActionDSCP,
       "zxAnUniAclPolicyActionVLAN": zxAnUniAclPolicyActionVLAN,
       "zxAnUniAclPolicyActionRedirectedTo": zxAnUniAclPolicyActionRedirectedTo,
       "zxAnUniAclPolicyActionMirroredTo": zxAnUniAclPolicyActionMirroredTo,
       "zxAnUniAclPolicyActionISStatistics": zxAnUniAclPolicyActionISStatistics,
       "zxAnUniAclPolicyActionCCos": zxAnUniAclPolicyActionCCos,
       "zxAnUniAclPolicyPir": zxAnUniAclPolicyPir,
       "zxAnUniAclPolicyPbs": zxAnUniAclPolicyPbs,
       "zxAnUniAclPolicyTrtcmExceedAction": zxAnUniAclPolicyTrtcmExceedAction,
       "zxAnUniAclPolicyTrtcmRemarkRedDscp": zxAnUniAclPolicyTrtcmRemarkRedDscp,
       "zxAnUniAclPolicyTrtcmRemarkYellowDscp": zxAnUniAclPolicyTrtcmRemarkYellowDscp,
       "zxAnUniAclPolicyTrtcmRemarkGreenDscp": zxAnUniAclPolicyTrtcmRemarkGreenDscp,
       "zxAnUniAclPolicyTrtcmRemarkRedCos": zxAnUniAclPolicyTrtcmRemarkRedCos,
       "zxAnUniAclPolicyTrtcmRemarkYellowCos": zxAnUniAclPolicyTrtcmRemarkYellowCos,
       "zxAnUniAclPolicyTrtcmRemarkGreenCos": zxAnUniAclPolicyTrtcmRemarkGreenCos,
       "zxAnUniAclPolicyStatus": zxAnUniAclPolicyStatus,
       "zxAnUniAclBindTable": zxAnUniAclBindTable,
       "zxAnUniAclBindEntry": zxAnUniAclBindEntry,
       "zxAnUniIfAclPolicyName": zxAnUniIfAclPolicyName,
       "zxAnUniAclBindDir": zxAnUniAclBindDir,
       "zxAnUniAclBindRowStatus": zxAnUniAclBindRowStatus,
       "zxAnAclTrapObjects": zxAnAclTrapObjects}
)
