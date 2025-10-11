# SNMP MIB module (HUAWEI-SECURITY-STATEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-STATEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:26:57 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSecStatExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwSecStatExtMibObjects_ObjectIdentity = ObjectIdentity
hwSecStatExtMibObjects = _HwSecStatExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1)
)
_HwSecStatExtAcl_ObjectIdentity = ObjectIdentity
hwSecStatExtAcl = _HwSecStatExtAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1)
)


class _HwSecStatExtBasicAclGroupNum_Type(Integer32):
    """Custom type hwSecStatExtBasicAclGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtBasicAclGroupNum_Type.__name__ = "Integer32"
_HwSecStatExtBasicAclGroupNum_Object = MibScalar
hwSecStatExtBasicAclGroupNum = _HwSecStatExtBasicAclGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 1),
    _HwSecStatExtBasicAclGroupNum_Type()
)
hwSecStatExtBasicAclGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtBasicAclGroupNum.setStatus("current")


class _HwSecStatExtAdvanceAclGroupNum_Type(Integer32):
    """Custom type hwSecStatExtAdvanceAclGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtAdvanceAclGroupNum_Type.__name__ = "Integer32"
_HwSecStatExtAdvanceAclGroupNum_Object = MibScalar
hwSecStatExtAdvanceAclGroupNum = _HwSecStatExtAdvanceAclGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 2),
    _HwSecStatExtAdvanceAclGroupNum_Type()
)
hwSecStatExtAdvanceAclGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtAdvanceAclGroupNum.setStatus("current")


class _HwSecStatExtMacAclGroupNum_Type(Integer32):
    """Custom type hwSecStatExtMacAclGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtMacAclGroupNum_Type.__name__ = "Integer32"
_HwSecStatExtMacAclGroupNum_Object = MibScalar
hwSecStatExtMacAclGroupNum = _HwSecStatExtMacAclGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 3),
    _HwSecStatExtMacAclGroupNum_Type()
)
hwSecStatExtMacAclGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtMacAclGroupNum.setStatus("current")


class _HwSecStatExtAcl6GroupNum_Type(Integer32):
    """Custom type hwSecStatExtAcl6GroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtAcl6GroupNum_Type.__name__ = "Integer32"
_HwSecStatExtAcl6GroupNum_Object = MibScalar
hwSecStatExtAcl6GroupNum = _HwSecStatExtAcl6GroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 4),
    _HwSecStatExtAcl6GroupNum_Type()
)
hwSecStatExtAcl6GroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtAcl6GroupNum.setStatus("current")


class _HwSecStatExtBasicAclRuleNum_Type(Integer32):
    """Custom type hwSecStatExtBasicAclRuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtBasicAclRuleNum_Type.__name__ = "Integer32"
_HwSecStatExtBasicAclRuleNum_Object = MibScalar
hwSecStatExtBasicAclRuleNum = _HwSecStatExtBasicAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 5),
    _HwSecStatExtBasicAclRuleNum_Type()
)
hwSecStatExtBasicAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtBasicAclRuleNum.setStatus("current")


class _HwSecStatExtAdvanceAclRuleNum_Type(Integer32):
    """Custom type hwSecStatExtAdvanceAclRuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtAdvanceAclRuleNum_Type.__name__ = "Integer32"
_HwSecStatExtAdvanceAclRuleNum_Object = MibScalar
hwSecStatExtAdvanceAclRuleNum = _HwSecStatExtAdvanceAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 6),
    _HwSecStatExtAdvanceAclRuleNum_Type()
)
hwSecStatExtAdvanceAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtAdvanceAclRuleNum.setStatus("current")


class _HwSecStatExtMacAclRuleNum_Type(Integer32):
    """Custom type hwSecStatExtMacAclRuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtMacAclRuleNum_Type.__name__ = "Integer32"
_HwSecStatExtMacAclRuleNum_Object = MibScalar
hwSecStatExtMacAclRuleNum = _HwSecStatExtMacAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 7),
    _HwSecStatExtMacAclRuleNum_Type()
)
hwSecStatExtMacAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtMacAclRuleNum.setStatus("current")


class _HwSecStatExtAcl6RuleNum_Type(Integer32):
    """Custom type hwSecStatExtAcl6RuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtAcl6RuleNum_Type.__name__ = "Integer32"
_HwSecStatExtAcl6RuleNum_Object = MibScalar
hwSecStatExtAcl6RuleNum = _HwSecStatExtAcl6RuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 1, 8),
    _HwSecStatExtAcl6RuleNum_Type()
)
hwSecStatExtAcl6RuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtAcl6RuleNum.setStatus("current")
_HwSecStatExtRoute_ObjectIdentity = ObjectIdentity
hwSecStatExtRoute = _HwSecStatExtRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2)
)


class _HwSecStatExtStaticRouteNum_Type(Integer32):
    """Custom type hwSecStatExtStaticRouteNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtStaticRouteNum_Type.__name__ = "Integer32"
_HwSecStatExtStaticRouteNum_Object = MibScalar
hwSecStatExtStaticRouteNum = _HwSecStatExtStaticRouteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 1),
    _HwSecStatExtStaticRouteNum_Type()
)
hwSecStatExtStaticRouteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtStaticRouteNum.setStatus("current")


class _HwSecStatExtOspfNum_Type(Integer32):
    """Custom type hwSecStatExtOspfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtOspfNum_Type.__name__ = "Integer32"
_HwSecStatExtOspfNum_Object = MibScalar
hwSecStatExtOspfNum = _HwSecStatExtOspfNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 2),
    _HwSecStatExtOspfNum_Type()
)
hwSecStatExtOspfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtOspfNum.setStatus("current")


class _HwSecStatExtRipNum_Type(Integer32):
    """Custom type hwSecStatExtRipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtRipNum_Type.__name__ = "Integer32"
_HwSecStatExtRipNum_Object = MibScalar
hwSecStatExtRipNum = _HwSecStatExtRipNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 3),
    _HwSecStatExtRipNum_Type()
)
hwSecStatExtRipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtRipNum.setStatus("current")


class _HwSecStatExtIsisNum_Type(Integer32):
    """Custom type hwSecStatExtIsisNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIsisNum_Type.__name__ = "Integer32"
_HwSecStatExtIsisNum_Object = MibScalar
hwSecStatExtIsisNum = _HwSecStatExtIsisNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 4),
    _HwSecStatExtIsisNum_Type()
)
hwSecStatExtIsisNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIsisNum.setStatus("current")


class _HwSecStatExtBgpNum_Type(Integer32):
    """Custom type hwSecStatExtBgpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtBgpNum_Type.__name__ = "Integer32"
_HwSecStatExtBgpNum_Object = MibScalar
hwSecStatExtBgpNum = _HwSecStatExtBgpNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 5),
    _HwSecStatExtBgpNum_Type()
)
hwSecStatExtBgpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtBgpNum.setStatus("current")


class _HwSecStatExtIpv6StaticRouteNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6StaticRouteNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIpv6StaticRouteNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6StaticRouteNum_Object = MibScalar
hwSecStatExtIpv6StaticRouteNum = _HwSecStatExtIpv6StaticRouteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 6),
    _HwSecStatExtIpv6StaticRouteNum_Type()
)
hwSecStatExtIpv6StaticRouteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6StaticRouteNum.setStatus("current")


class _HwSecStatExtIpv6OspfNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6OspfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIpv6OspfNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6OspfNum_Object = MibScalar
hwSecStatExtIpv6OspfNum = _HwSecStatExtIpv6OspfNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 7),
    _HwSecStatExtIpv6OspfNum_Type()
)
hwSecStatExtIpv6OspfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6OspfNum.setStatus("current")


class _HwSecStatExtIpv6RipNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6RipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIpv6RipNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6RipNum_Object = MibScalar
hwSecStatExtIpv6RipNum = _HwSecStatExtIpv6RipNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 8),
    _HwSecStatExtIpv6RipNum_Type()
)
hwSecStatExtIpv6RipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6RipNum.setStatus("current")


class _HwSecStatExtIpv6IsisNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6IsisNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIpv6IsisNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6IsisNum_Object = MibScalar
hwSecStatExtIpv6IsisNum = _HwSecStatExtIpv6IsisNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 9),
    _HwSecStatExtIpv6IsisNum_Type()
)
hwSecStatExtIpv6IsisNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6IsisNum.setStatus("current")


class _HwSecStatExtIpv6BgpNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6BgpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSecStatExtIpv6BgpNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6BgpNum_Object = MibScalar
hwSecStatExtIpv6BgpNum = _HwSecStatExtIpv6BgpNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 2, 10),
    _HwSecStatExtIpv6BgpNum_Type()
)
hwSecStatExtIpv6BgpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6BgpNum.setStatus("current")
_HwSecStatExtSession_ObjectIdentity = ObjectIdentity
hwSecStatExtSession = _HwSecStatExtSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3)
)


class _HwSecStatExtSessionNum_Type(Integer32):
    """Custom type hwSecStatExtSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtSessionNum_Type.__name__ = "Integer32"
_HwSecStatExtSessionNum_Object = MibScalar
hwSecStatExtSessionNum = _HwSecStatExtSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 1),
    _HwSecStatExtSessionNum_Type()
)
hwSecStatExtSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtSessionNum.setStatus("current")


class _HwSecStatExtMacAddrListNum_Type(Integer32):
    """Custom type hwSecStatExtMacAddrListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtMacAddrListNum_Type.__name__ = "Integer32"
_HwSecStatExtMacAddrListNum_Object = MibScalar
hwSecStatExtMacAddrListNum = _HwSecStatExtMacAddrListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 2),
    _HwSecStatExtMacAddrListNum_Type()
)
hwSecStatExtMacAddrListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtMacAddrListNum.setStatus("current")


class _HwSecStatExtBlackListNum_Type(Integer32):
    """Custom type hwSecStatExtBlackListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtBlackListNum_Type.__name__ = "Integer32"
_HwSecStatExtBlackListNum_Object = MibScalar
hwSecStatExtBlackListNum = _HwSecStatExtBlackListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 3),
    _HwSecStatExtBlackListNum_Type()
)
hwSecStatExtBlackListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtBlackListNum.setStatus("current")


class _HwSecStatExtNatServerNum_Type(Integer32):
    """Custom type hwSecStatExtNatServerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtNatServerNum_Type.__name__ = "Integer32"
_HwSecStatExtNatServerNum_Object = MibScalar
hwSecStatExtNatServerNum = _HwSecStatExtNatServerNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 4),
    _HwSecStatExtNatServerNum_Type()
)
hwSecStatExtNatServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtNatServerNum.setStatus("current")


class _HwSecStatExtIpMonitorListNum_Type(Integer32):
    """Custom type hwSecStatExtIpMonitorListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtIpMonitorListNum_Type.__name__ = "Integer32"
_HwSecStatExtIpMonitorListNum_Object = MibScalar
hwSecStatExtIpMonitorListNum = _HwSecStatExtIpMonitorListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 5),
    _HwSecStatExtIpMonitorListNum_Type()
)
hwSecStatExtIpMonitorListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpMonitorListNum.setStatus("current")


class _HwSecStatExtServerMapTotalNum_Type(Integer32):
    """Custom type hwSecStatExtServerMapTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtServerMapTotalNum_Type.__name__ = "Integer32"
_HwSecStatExtServerMapTotalNum_Object = MibScalar
hwSecStatExtServerMapTotalNum = _HwSecStatExtServerMapTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 6),
    _HwSecStatExtServerMapTotalNum_Type()
)
hwSecStatExtServerMapTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtServerMapTotalNum.setStatus("current")


class _HwSecStatExtServerMapDynamicNum_Type(Integer32):
    """Custom type hwSecStatExtServerMapDynamicNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtServerMapDynamicNum_Type.__name__ = "Integer32"
_HwSecStatExtServerMapDynamicNum_Object = MibScalar
hwSecStatExtServerMapDynamicNum = _HwSecStatExtServerMapDynamicNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 7),
    _HwSecStatExtServerMapDynamicNum_Type()
)
hwSecStatExtServerMapDynamicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtServerMapDynamicNum.setStatus("current")


class _HwSecStatExtWifiUserOnlineNum_Type(Integer32):
    """Custom type hwSecStatExtWifiUserOnlineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtWifiUserOnlineNum_Type.__name__ = "Integer32"
_HwSecStatExtWifiUserOnlineNum_Object = MibScalar
hwSecStatExtWifiUserOnlineNum = _HwSecStatExtWifiUserOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 8),
    _HwSecStatExtWifiUserOnlineNum_Type()
)
hwSecStatExtWifiUserOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtWifiUserOnlineNum.setStatus("current")


class _HwSecStatExt802dot1xUserOnlineNum_Type(Integer32):
    """Custom type hwSecStatExt802dot1xUserOnlineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExt802dot1xUserOnlineNum_Type.__name__ = "Integer32"
_HwSecStatExt802dot1xUserOnlineNum_Object = MibScalar
hwSecStatExt802dot1xUserOnlineNum = _HwSecStatExt802dot1xUserOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 9),
    _HwSecStatExt802dot1xUserOnlineNum_Type()
)
hwSecStatExt802dot1xUserOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExt802dot1xUserOnlineNum.setStatus("current")


class _HwSecStatExtArplistTotalNum_Type(Integer32):
    """Custom type hwSecStatExtArplistTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtArplistTotalNum_Type.__name__ = "Integer32"
_HwSecStatExtArplistTotalNum_Object = MibScalar
hwSecStatExtArplistTotalNum = _HwSecStatExtArplistTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 10),
    _HwSecStatExtArplistTotalNum_Type()
)
hwSecStatExtArplistTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtArplistTotalNum.setStatus("current")


class _HwSecStatExtFiblistTotoleNum_Type(Integer32):
    """Custom type hwSecStatExtFiblistTotoleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtFiblistTotoleNum_Type.__name__ = "Integer32"
_HwSecStatExtFiblistTotoleNum_Object = MibScalar
hwSecStatExtFiblistTotoleNum = _HwSecStatExtFiblistTotoleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 11),
    _HwSecStatExtFiblistTotoleNum_Type()
)
hwSecStatExtFiblistTotoleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtFiblistTotoleNum.setStatus("current")


class _HwSecStatExtIpv6SessionNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6SessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtIpv6SessionNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6SessionNum_Object = MibScalar
hwSecStatExtIpv6SessionNum = _HwSecStatExtIpv6SessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 12),
    _HwSecStatExtIpv6SessionNum_Type()
)
hwSecStatExtIpv6SessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6SessionNum.setStatus("current")


class _HwSecStatExtIpv6ServerMapTotalNum_Type(Integer32):
    """Custom type hwSecStatExtIpv6ServerMapTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtIpv6ServerMapTotalNum_Type.__name__ = "Integer32"
_HwSecStatExtIpv6ServerMapTotalNum_Object = MibScalar
hwSecStatExtIpv6ServerMapTotalNum = _HwSecStatExtIpv6ServerMapTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 3, 13),
    _HwSecStatExtIpv6ServerMapTotalNum_Type()
)
hwSecStatExtIpv6ServerMapTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtIpv6ServerMapTotalNum.setStatus("current")
_HwSecStatExtTotalNum_ObjectIdentity = ObjectIdentity
hwSecStatExtTotalNum = _HwSecStatExtTotalNum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4)
)


class _HwSecStatIkeNum_Type(Integer32):
    """Custom type hwSecStatIkeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatIkeNum_Type.__name__ = "Integer32"
_HwSecStatIkeNum_Object = MibScalar
hwSecStatIkeNum = _HwSecStatIkeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 1),
    _HwSecStatIkeNum_Type()
)
hwSecStatIkeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIkeNum.setStatus("current")
_HwSecStatIpsecPacketsIn_Type = Counter64
_HwSecStatIpsecPacketsIn_Object = MibScalar
hwSecStatIpsecPacketsIn = _HwSecStatIpsecPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 2),
    _HwSecStatIpsecPacketsIn_Type()
)
hwSecStatIpsecPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIpsecPacketsIn.setStatus("current")
_HwSecStatIpsecPacketsOut_Type = Counter64
_HwSecStatIpsecPacketsOut_Object = MibScalar
hwSecStatIpsecPacketsOut = _HwSecStatIpsecPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 3),
    _HwSecStatIpsecPacketsOut_Type()
)
hwSecStatIpsecPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIpsecPacketsOut.setStatus("current")
_HwSecStatIpsecPacketsDorp_Type = Counter64
_HwSecStatIpsecPacketsDorp_Object = MibScalar
hwSecStatIpsecPacketsDorp = _HwSecStatIpsecPacketsDorp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 4),
    _HwSecStatIpsecPacketsDorp_Type()
)
hwSecStatIpsecPacketsDorp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIpsecPacketsDorp.setStatus("current")


class _HwSecStatL2tpUserTotalNum_Type(Integer32):
    """Custom type hwSecStatL2tpUserTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatL2tpUserTotalNum_Type.__name__ = "Integer32"
_HwSecStatL2tpUserTotalNum_Object = MibScalar
hwSecStatL2tpUserTotalNum = _HwSecStatL2tpUserTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 5),
    _HwSecStatL2tpUserTotalNum_Type()
)
hwSecStatL2tpUserTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatL2tpUserTotalNum.setStatus("current")


class _HwSecStatHrpPacketsSend_Type(Integer32):
    """Custom type hwSecStatHrpPacketsSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatHrpPacketsSend_Type.__name__ = "Integer32"
_HwSecStatHrpPacketsSend_Object = MibScalar
hwSecStatHrpPacketsSend = _HwSecStatHrpPacketsSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 4, 6),
    _HwSecStatHrpPacketsSend_Type()
)
hwSecStatHrpPacketsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatHrpPacketsSend.setStatus("current")
_HwSecStatExtL2tpTable_Object = MibTable
hwSecStatExtL2tpTable = _HwSecStatExtL2tpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5)
)
if mibBuilder.loadTexts:
    hwSecStatExtL2tpTable.setStatus("current")
_HwSecStatExtL2tpEntry_Object = MibTableRow
hwSecStatExtL2tpEntry = _HwSecStatExtL2tpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5, 1)
)
hwSecStatExtL2tpEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtL2tpSlotIndex"),
    (0, "HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtL2tpCpuIndex"),
)
if mibBuilder.loadTexts:
    hwSecStatExtL2tpEntry.setStatus("current")


class _HwSecStatExtL2tpSlotIndex_Type(Integer32):
    """Custom type hwSecStatExtL2tpSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwSecStatExtL2tpSlotIndex_Type.__name__ = "Integer32"
_HwSecStatExtL2tpSlotIndex_Object = MibTableColumn
hwSecStatExtL2tpSlotIndex = _HwSecStatExtL2tpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5, 1, 1),
    _HwSecStatExtL2tpSlotIndex_Type()
)
hwSecStatExtL2tpSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatExtL2tpSlotIndex.setStatus("current")


class _HwSecStatExtL2tpCpuIndex_Type(Integer32):
    """Custom type hwSecStatExtL2tpCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwSecStatExtL2tpCpuIndex_Type.__name__ = "Integer32"
_HwSecStatExtL2tpCpuIndex_Object = MibTableColumn
hwSecStatExtL2tpCpuIndex = _HwSecStatExtL2tpCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5, 1, 2),
    _HwSecStatExtL2tpCpuIndex_Type()
)
hwSecStatExtL2tpCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatExtL2tpCpuIndex.setStatus("current")


class _HwSecStatExtL2tpTunnelNum_Type(Integer32):
    """Custom type hwSecStatExtL2tpTunnelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtL2tpTunnelNum_Type.__name__ = "Integer32"
_HwSecStatExtL2tpTunnelNum_Object = MibTableColumn
hwSecStatExtL2tpTunnelNum = _HwSecStatExtL2tpTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5, 1, 3),
    _HwSecStatExtL2tpTunnelNum_Type()
)
hwSecStatExtL2tpTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtL2tpTunnelNum.setStatus("current")


class _HwSecStatExtL2tpSessionNum_Type(Integer32):
    """Custom type hwSecStatExtL2tpSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtL2tpSessionNum_Type.__name__ = "Integer32"
_HwSecStatExtL2tpSessionNum_Object = MibTableColumn
hwSecStatExtL2tpSessionNum = _HwSecStatExtL2tpSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 5, 1, 4),
    _HwSecStatExtL2tpSessionNum_Type()
)
hwSecStatExtL2tpSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtL2tpSessionNum.setStatus("current")
_HwSecStatExtVcpuTable_Object = MibTable
hwSecStatExtVcpuTable = _HwSecStatExtVcpuTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 6)
)
if mibBuilder.loadTexts:
    hwSecStatExtVcpuTable.setStatus("current")
_HwSecStatExtVcpuEntry_Object = MibTableRow
hwSecStatExtVcpuEntry = _HwSecStatExtVcpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 6, 1)
)
hwSecStatExtVcpuEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtVcpuIndex"),
)
if mibBuilder.loadTexts:
    hwSecStatExtVcpuEntry.setStatus("current")


class _HwSecStatExtVcpuIndex_Type(Integer32):
    """Custom type hwSecStatExtVcpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwSecStatExtVcpuIndex_Type.__name__ = "Integer32"
_HwSecStatExtVcpuIndex_Object = MibTableColumn
hwSecStatExtVcpuIndex = _HwSecStatExtVcpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 6, 1, 1),
    _HwSecStatExtVcpuIndex_Type()
)
hwSecStatExtVcpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatExtVcpuIndex.setStatus("current")


class _HwSecStatExtVcpuID_Type(Integer32):
    """Custom type hwSecStatExtVcpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwSecStatExtVcpuID_Type.__name__ = "Integer32"
_HwSecStatExtVcpuID_Object = MibTableColumn
hwSecStatExtVcpuID = _HwSecStatExtVcpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 6, 1, 2),
    _HwSecStatExtVcpuID_Type()
)
hwSecStatExtVcpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtVcpuID.setStatus("current")


class _HwSecStatExtVcpuUseage_Type(Integer32):
    """Custom type hwSecStatExtVcpuUseage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtVcpuUseage_Type.__name__ = "Integer32"
_HwSecStatExtVcpuUseage_Object = MibTableColumn
hwSecStatExtVcpuUseage = _HwSecStatExtVcpuUseage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 6, 1, 3),
    _HwSecStatExtVcpuUseage_Type()
)
hwSecStatExtVcpuUseage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtVcpuUseage.setStatus("current")
_HwSecStatExtLicenseTable_Object = MibTable
hwSecStatExtLicenseTable = _HwSecStatExtLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 7)
)
if mibBuilder.loadTexts:
    hwSecStatExtLicenseTable.setStatus("current")
_HwSecStatExtLicenseEntry_Object = MibTableRow
hwSecStatExtLicenseEntry = _HwSecStatExtLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 7, 1)
)
hwSecStatExtLicenseEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtModuleIndex"),
)
if mibBuilder.loadTexts:
    hwSecStatExtLicenseEntry.setStatus("current")


class _HwSecStatExtModuleIndex_Type(Integer32):
    """Custom type hwSecStatExtModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwSecStatExtModuleIndex_Type.__name__ = "Integer32"
_HwSecStatExtModuleIndex_Object = MibTableColumn
hwSecStatExtModuleIndex = _HwSecStatExtModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 7, 1, 1),
    _HwSecStatExtModuleIndex_Type()
)
hwSecStatExtModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatExtModuleIndex.setStatus("current")


class _HwSecStatExtModuleName_Type(OctetString):
    """Custom type hwSecStatExtModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwSecStatExtModuleName_Type.__name__ = "OctetString"
_HwSecStatExtModuleName_Object = MibTableColumn
hwSecStatExtModuleName = _HwSecStatExtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 7, 1, 2),
    _HwSecStatExtModuleName_Type()
)
hwSecStatExtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtModuleName.setStatus("current")


class _HwSecStatExtModuleLicenseNum_Type(Integer32):
    """Custom type hwSecStatExtModuleLicenseNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwSecStatExtModuleLicenseNum_Type.__name__ = "Integer32"
_HwSecStatExtModuleLicenseNum_Object = MibTableColumn
hwSecStatExtModuleLicenseNum = _HwSecStatExtModuleLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 1, 7, 1, 3),
    _HwSecStatExtModuleLicenseNum_Type()
)
hwSecStatExtModuleLicenseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatExtModuleLicenseNum.setStatus("current")
_HwSecStatExtConformance_ObjectIdentity = ObjectIdentity
hwSecStatExtConformance = _HwSecStatExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2)
)
_HwSecStatExtCompliance_ObjectIdentity = ObjectIdentity
hwSecStatExtCompliance = _HwSecStatExtCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 1)
)
_HwSecStatExtMibGroups_ObjectIdentity = ObjectIdentity
hwSecStatExtMibGroups = _HwSecStatExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2)
)

# Managed Objects groups

hwSecStatExtAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 1)
)
hwSecStatExtAclGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtBasicAclGroupNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtAdvanceAclGroupNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtMacAclGroupNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtAcl6GroupNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtBasicAclRuleNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtAdvanceAclRuleNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtMacAclRuleNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtAcl6RuleNum"))
)
if mibBuilder.loadTexts:
    hwSecStatExtAclGroup.setStatus("current")

hwSecStatExtRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 2)
)
hwSecStatExtRouteGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtStaticRouteNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtOspfNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtRipNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIsisNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtBgpNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6StaticRouteNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6OspfNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6RipNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6IsisNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6BgpNum"))
)
if mibBuilder.loadTexts:
    hwSecStatExtRouteGroup.setStatus("current")

hwSecStatExtSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 3)
)
hwSecStatExtSessionGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtSessionNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtMacAddrListNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtBlackListNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtNatServerNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpMonitorListNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtServerMapTotalNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtServerMapDynamicNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtWifiUserOnlineNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExt802dot1xUserOnlineNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtArplistTotalNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6SessionNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtIpv6ServerMapTotalNum"))
)
if mibBuilder.loadTexts:
    hwSecStatExtSessionGroup.setStatus("current")

hwSecStatExtIPsecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 4)
)
hwSecStatExtIPsecGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatIkeNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatIpsecPacketsIn"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatIpsecPacketsOut"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatIpsecPacketsDorp"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatL2tpUserTotalNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatHrpPacketsSend"))
)
if mibBuilder.loadTexts:
    hwSecStatExtIPsecGroup.setStatus("current")

hwSecStatExtL2tpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 5)
)
hwSecStatExtL2tpGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtL2tpTunnelNum"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtL2tpSessionNum"))
)
if mibBuilder.loadTexts:
    hwSecStatExtL2tpGroup.setStatus("current")

hwSecStatExtVcpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 6)
)
hwSecStatExtVcpuGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtVcpuID"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtVcpuUseage"))
)
if mibBuilder.loadTexts:
    hwSecStatExtVcpuGroup.setStatus("current")

hwSecStatExtLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 38, 2, 2, 7)
)
hwSecStatExtLicenseGroup.setObjects(
      *(("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtModuleName"),
        ("HUAWEI-SECURITY-STATEXT-MIB", "hwSecStatExtModuleLicenseNum"))
)
if mibBuilder.loadTexts:
    hwSecStatExtLicenseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-STATEXT-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwSecStatExtMib": hwSecStatExtMib,
       "hwSecStatExtMibObjects": hwSecStatExtMibObjects,
       "hwSecStatExtAcl": hwSecStatExtAcl,
       "hwSecStatExtBasicAclGroupNum": hwSecStatExtBasicAclGroupNum,
       "hwSecStatExtAdvanceAclGroupNum": hwSecStatExtAdvanceAclGroupNum,
       "hwSecStatExtMacAclGroupNum": hwSecStatExtMacAclGroupNum,
       "hwSecStatExtAcl6GroupNum": hwSecStatExtAcl6GroupNum,
       "hwSecStatExtBasicAclRuleNum": hwSecStatExtBasicAclRuleNum,
       "hwSecStatExtAdvanceAclRuleNum": hwSecStatExtAdvanceAclRuleNum,
       "hwSecStatExtMacAclRuleNum": hwSecStatExtMacAclRuleNum,
       "hwSecStatExtAcl6RuleNum": hwSecStatExtAcl6RuleNum,
       "hwSecStatExtRoute": hwSecStatExtRoute,
       "hwSecStatExtStaticRouteNum": hwSecStatExtStaticRouteNum,
       "hwSecStatExtOspfNum": hwSecStatExtOspfNum,
       "hwSecStatExtRipNum": hwSecStatExtRipNum,
       "hwSecStatExtIsisNum": hwSecStatExtIsisNum,
       "hwSecStatExtBgpNum": hwSecStatExtBgpNum,
       "hwSecStatExtIpv6StaticRouteNum": hwSecStatExtIpv6StaticRouteNum,
       "hwSecStatExtIpv6OspfNum": hwSecStatExtIpv6OspfNum,
       "hwSecStatExtIpv6RipNum": hwSecStatExtIpv6RipNum,
       "hwSecStatExtIpv6IsisNum": hwSecStatExtIpv6IsisNum,
       "hwSecStatExtIpv6BgpNum": hwSecStatExtIpv6BgpNum,
       "hwSecStatExtSession": hwSecStatExtSession,
       "hwSecStatExtSessionNum": hwSecStatExtSessionNum,
       "hwSecStatExtMacAddrListNum": hwSecStatExtMacAddrListNum,
       "hwSecStatExtBlackListNum": hwSecStatExtBlackListNum,
       "hwSecStatExtNatServerNum": hwSecStatExtNatServerNum,
       "hwSecStatExtIpMonitorListNum": hwSecStatExtIpMonitorListNum,
       "hwSecStatExtServerMapTotalNum": hwSecStatExtServerMapTotalNum,
       "hwSecStatExtServerMapDynamicNum": hwSecStatExtServerMapDynamicNum,
       "hwSecStatExtWifiUserOnlineNum": hwSecStatExtWifiUserOnlineNum,
       "hwSecStatExt802dot1xUserOnlineNum": hwSecStatExt802dot1xUserOnlineNum,
       "hwSecStatExtArplistTotalNum": hwSecStatExtArplistTotalNum,
       "hwSecStatExtFiblistTotoleNum": hwSecStatExtFiblistTotoleNum,
       "hwSecStatExtIpv6SessionNum": hwSecStatExtIpv6SessionNum,
       "hwSecStatExtIpv6ServerMapTotalNum": hwSecStatExtIpv6ServerMapTotalNum,
       "hwSecStatExtTotalNum": hwSecStatExtTotalNum,
       "hwSecStatIkeNum": hwSecStatIkeNum,
       "hwSecStatIpsecPacketsIn": hwSecStatIpsecPacketsIn,
       "hwSecStatIpsecPacketsOut": hwSecStatIpsecPacketsOut,
       "hwSecStatIpsecPacketsDorp": hwSecStatIpsecPacketsDorp,
       "hwSecStatL2tpUserTotalNum": hwSecStatL2tpUserTotalNum,
       "hwSecStatHrpPacketsSend": hwSecStatHrpPacketsSend,
       "hwSecStatExtL2tpTable": hwSecStatExtL2tpTable,
       "hwSecStatExtL2tpEntry": hwSecStatExtL2tpEntry,
       "hwSecStatExtL2tpSlotIndex": hwSecStatExtL2tpSlotIndex,
       "hwSecStatExtL2tpCpuIndex": hwSecStatExtL2tpCpuIndex,
       "hwSecStatExtL2tpTunnelNum": hwSecStatExtL2tpTunnelNum,
       "hwSecStatExtL2tpSessionNum": hwSecStatExtL2tpSessionNum,
       "hwSecStatExtVcpuTable": hwSecStatExtVcpuTable,
       "hwSecStatExtVcpuEntry": hwSecStatExtVcpuEntry,
       "hwSecStatExtVcpuIndex": hwSecStatExtVcpuIndex,
       "hwSecStatExtVcpuID": hwSecStatExtVcpuID,
       "hwSecStatExtVcpuUseage": hwSecStatExtVcpuUseage,
       "hwSecStatExtLicenseTable": hwSecStatExtLicenseTable,
       "hwSecStatExtLicenseEntry": hwSecStatExtLicenseEntry,
       "hwSecStatExtModuleIndex": hwSecStatExtModuleIndex,
       "hwSecStatExtModuleName": hwSecStatExtModuleName,
       "hwSecStatExtModuleLicenseNum": hwSecStatExtModuleLicenseNum,
       "hwSecStatExtConformance": hwSecStatExtConformance,
       "hwSecStatExtCompliance": hwSecStatExtCompliance,
       "hwSecStatExtMibGroups": hwSecStatExtMibGroups,
       "hwSecStatExtAclGroup": hwSecStatExtAclGroup,
       "hwSecStatExtRouteGroup": hwSecStatExtRouteGroup,
       "hwSecStatExtSessionGroup": hwSecStatExtSessionGroup,
       "hwSecStatExtIPsecGroup": hwSecStatExtIPsecGroup,
       "hwSecStatExtL2tpGroup": hwSecStatExtL2tpGroup,
       "hwSecStatExtVcpuGroup": hwSecStatExtVcpuGroup,
       "hwSecStatExtLicenseGroup": hwSecStatExtLicenseGroup}
)
