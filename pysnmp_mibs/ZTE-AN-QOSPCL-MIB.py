# SNMP MIB module (ZTE-AN-QOSPCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-QOSPCL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:08 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnQosPclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnAclPortOperator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("eq", 1),
          ("ge", 2),
          ("le", 3),
          ("range", 7))
    )



# MIB Managed Objects in the order of their OIDs

_ZxAnQosPclObjects_ObjectIdentity = ObjectIdentity
zxAnQosPclObjects = _ZxAnQosPclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1)
)
_ZxAnQosPclGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnQosPclGlobalObjects = _ZxAnQosPclGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 1)
)


class _ZxAnQosPclCapability_Type(Bits):
    """Custom type zxAnQosPclCapability based on Bits"""
    namedValues = NamedValues(
        *(("redirectType", 0),
          ("trafficMirrorType", 1),
          ("innerPortBinding", 2),
          ("remoteMirroring", 3),
          ("ifBindAclName", 4))
    )

_ZxAnQosPclCapability_Type.__name__ = "Bits"
_ZxAnQosPclCapability_Object = MibScalar
zxAnQosPclCapability = _ZxAnQosPclCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 1, 1),
    _ZxAnQosPclCapability_Type()
)
zxAnQosPclCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosPclCapability.setStatus("current")
_ZxAnAclTable_Object = MibTable
zxAnAclTable = _ZxAnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnAclTable.setStatus("current")
_ZxAnAclEntry_Object = MibTableRow
zxAnAclEntry = _ZxAnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 2, 1)
)
zxAnAclEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
)
if mibBuilder.loadTexts:
    zxAnAclEntry.setStatus("current")


class _ZxAnAclNumber_Type(Integer32):
    """Custom type zxAnAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
        ValueRangeConstraint(600, 699),
    )


_ZxAnAclNumber_Type.__name__ = "Integer32"
_ZxAnAclNumber_Object = MibTableColumn
zxAnAclNumber = _ZxAnAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 2, 1, 1),
    _ZxAnAclNumber_Type()
)
zxAnAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclNumber.setStatus("current")


class _ZxAnAclName_Type(DisplayString):
    """Custom type zxAnAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAclName_Type.__name__ = "DisplayString"
_ZxAnAclName_Object = MibTableColumn
zxAnAclName = _ZxAnAclName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 2, 1, 2),
    _ZxAnAclName_Type()
)
zxAnAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclName.setStatus("current")
_ZxAnAclRowStatus_Type = RowStatus
_ZxAnAclRowStatus_Object = MibTableColumn
zxAnAclRowStatus = _ZxAnAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 2, 1, 30),
    _ZxAnAclRowStatus_Type()
)
zxAnAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclRowStatus.setStatus("current")
_ZxAnAclHybridRuleTable_Object = MibTable
zxAnAclHybridRuleTable = _ZxAnAclHybridRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnAclHybridRuleTable.setStatus("current")
_ZxAnAclHybridRuleEntry_Object = MibTableRow
zxAnAclHybridRuleEntry = _ZxAnAclHybridRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1)
)
zxAnAclHybridRuleEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclHybridRuleEntry.setStatus("current")


class _ZxAnAclHybridRuleId_Type(Integer32):
    """Custom type zxAnAclHybridRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxAnAclHybridRuleId_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleId_Object = MibTableColumn
zxAnAclHybridRuleId = _ZxAnAclHybridRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 1),
    _ZxAnAclHybridRuleId_Type()
)
zxAnAclHybridRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleId.setStatus("current")


class _ZxAnAclHybridRuleAccessCtrl_Type(Integer32):
    """Custom type zxAnAclHybridRuleAccessCtrl based on Integer32"""
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


_ZxAnAclHybridRuleAccessCtrl_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleAccessCtrl_Object = MibTableColumn
zxAnAclHybridRuleAccessCtrl = _ZxAnAclHybridRuleAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 2),
    _ZxAnAclHybridRuleAccessCtrl_Type()
)
zxAnAclHybridRuleAccessCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleAccessCtrl.setStatus("current")
_ZxAnAclHybridRuleSrcIpType_Type = InetAddressType
_ZxAnAclHybridRuleSrcIpType_Object = MibTableColumn
zxAnAclHybridRuleSrcIpType = _ZxAnAclHybridRuleSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 3),
    _ZxAnAclHybridRuleSrcIpType_Type()
)
zxAnAclHybridRuleSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcIpType.setStatus("current")
_ZxAnAclHybridRuleSrcIp_Type = InetAddress
_ZxAnAclHybridRuleSrcIp_Object = MibTableColumn
zxAnAclHybridRuleSrcIp = _ZxAnAclHybridRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 4),
    _ZxAnAclHybridRuleSrcIp_Type()
)
zxAnAclHybridRuleSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcIp.setStatus("current")
_ZxAnAclHybridRuleSrcIpMask_Type = InetAddress
_ZxAnAclHybridRuleSrcIpMask_Object = MibTableColumn
zxAnAclHybridRuleSrcIpMask = _ZxAnAclHybridRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 5),
    _ZxAnAclHybridRuleSrcIpMask_Type()
)
zxAnAclHybridRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcIpMask.setStatus("current")
_ZxAnAclHybridRuleDestIpType_Type = InetAddressType
_ZxAnAclHybridRuleDestIpType_Object = MibTableColumn
zxAnAclHybridRuleDestIpType = _ZxAnAclHybridRuleDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 6),
    _ZxAnAclHybridRuleDestIpType_Type()
)
zxAnAclHybridRuleDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestIpType.setStatus("current")
_ZxAnAclHybridRuleDestIp_Type = InetAddress
_ZxAnAclHybridRuleDestIp_Object = MibTableColumn
zxAnAclHybridRuleDestIp = _ZxAnAclHybridRuleDestIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 7),
    _ZxAnAclHybridRuleDestIp_Type()
)
zxAnAclHybridRuleDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestIp.setStatus("current")
_ZxAnAclHybridRuleDestIpMask_Type = InetAddress
_ZxAnAclHybridRuleDestIpMask_Object = MibTableColumn
zxAnAclHybridRuleDestIpMask = _ZxAnAclHybridRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 8),
    _ZxAnAclHybridRuleDestIpMask_Type()
)
zxAnAclHybridRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestIpMask.setStatus("current")


class _ZxAnAclHybridRuleIpProto_Type(Integer32):
    """Custom type zxAnAclHybridRuleIpProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclHybridRuleIpProto_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleIpProto_Object = MibTableColumn
zxAnAclHybridRuleIpProto = _ZxAnAclHybridRuleIpProto_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 9),
    _ZxAnAclHybridRuleIpProto_Type()
)
zxAnAclHybridRuleIpProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleIpProto.setStatus("current")


class _ZxAnAclHybridRuleEthProto_Type(Integer32):
    """Custom type zxAnAclHybridRuleEthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1537, 65535),
    )


_ZxAnAclHybridRuleEthProto_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleEthProto_Object = MibTableColumn
zxAnAclHybridRuleEthProto = _ZxAnAclHybridRuleEthProto_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 10),
    _ZxAnAclHybridRuleEthProto_Type()
)
zxAnAclHybridRuleEthProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleEthProto.setStatus("current")
_ZxAnAclHybridRuleSrcPortOper_Type = ZxAnAclPortOperator
_ZxAnAclHybridRuleSrcPortOper_Object = MibTableColumn
zxAnAclHybridRuleSrcPortOper = _ZxAnAclHybridRuleSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 11),
    _ZxAnAclHybridRuleSrcPortOper_Type()
)
zxAnAclHybridRuleSrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcPortOper.setStatus("current")


class _ZxAnAclHybridRuleStartSrcPort_Type(Integer32):
    """Custom type zxAnAclHybridRuleStartSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclHybridRuleStartSrcPort_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleStartSrcPort_Object = MibTableColumn
zxAnAclHybridRuleStartSrcPort = _ZxAnAclHybridRuleStartSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 12),
    _ZxAnAclHybridRuleStartSrcPort_Type()
)
zxAnAclHybridRuleStartSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleStartSrcPort.setStatus("current")


class _ZxAnAclHybridRuleEndSrcPort_Type(Integer32):
    """Custom type zxAnAclHybridRuleEndSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclHybridRuleEndSrcPort_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleEndSrcPort_Object = MibTableColumn
zxAnAclHybridRuleEndSrcPort = _ZxAnAclHybridRuleEndSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 13),
    _ZxAnAclHybridRuleEndSrcPort_Type()
)
zxAnAclHybridRuleEndSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleEndSrcPort.setStatus("current")
_ZxAnAclHybridRuleDestPortOper_Type = ZxAnAclPortOperator
_ZxAnAclHybridRuleDestPortOper_Object = MibTableColumn
zxAnAclHybridRuleDestPortOper = _ZxAnAclHybridRuleDestPortOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 14),
    _ZxAnAclHybridRuleDestPortOper_Type()
)
zxAnAclHybridRuleDestPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestPortOper.setStatus("current")


class _ZxAnAclHybridRuleStartDestPort_Type(Integer32):
    """Custom type zxAnAclHybridRuleStartDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclHybridRuleStartDestPort_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleStartDestPort_Object = MibTableColumn
zxAnAclHybridRuleStartDestPort = _ZxAnAclHybridRuleStartDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 15),
    _ZxAnAclHybridRuleStartDestPort_Type()
)
zxAnAclHybridRuleStartDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleStartDestPort.setStatus("current")


class _ZxAnAclHybridRuleEndDestPort_Type(Integer32):
    """Custom type zxAnAclHybridRuleEndDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclHybridRuleEndDestPort_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleEndDestPort_Object = MibTableColumn
zxAnAclHybridRuleEndDestPort = _ZxAnAclHybridRuleEndDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 16),
    _ZxAnAclHybridRuleEndDestPort_Type()
)
zxAnAclHybridRuleEndDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleEndDestPort.setStatus("current")


class _ZxAnAclHybridRulePrecedence_Type(Integer32):
    """Custom type zxAnAclHybridRulePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclHybridRulePrecedence_Type.__name__ = "Integer32"
_ZxAnAclHybridRulePrecedence_Object = MibTableColumn
zxAnAclHybridRulePrecedence = _ZxAnAclHybridRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 17),
    _ZxAnAclHybridRulePrecedence_Type()
)
zxAnAclHybridRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRulePrecedence.setStatus("current")


class _ZxAnAclHybridRuleTos_Type(Integer32):
    """Custom type zxAnAclHybridRuleTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclHybridRuleTos_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleTos_Object = MibTableColumn
zxAnAclHybridRuleTos = _ZxAnAclHybridRuleTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 18),
    _ZxAnAclHybridRuleTos_Type()
)
zxAnAclHybridRuleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleTos.setStatus("current")


class _ZxAnAclHybridRuleDscp_Type(Integer32):
    """Custom type zxAnAclHybridRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclHybridRuleDscp_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleDscp_Object = MibTableColumn
zxAnAclHybridRuleDscp = _ZxAnAclHybridRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 19),
    _ZxAnAclHybridRuleDscp_Type()
)
zxAnAclHybridRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDscp.setStatus("current")


class _ZxAnAclHybridRuleStagCos_Type(Integer32):
    """Custom type zxAnAclHybridRuleStagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclHybridRuleStagCos_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleStagCos_Object = MibTableColumn
zxAnAclHybridRuleStagCos = _ZxAnAclHybridRuleStagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 20),
    _ZxAnAclHybridRuleStagCos_Type()
)
zxAnAclHybridRuleStagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleStagCos.setStatus("current")


class _ZxAnAclHybridRuleSVid_Type(Integer32):
    """Custom type zxAnAclHybridRuleSVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnAclHybridRuleSVid_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleSVid_Object = MibTableColumn
zxAnAclHybridRuleSVid = _ZxAnAclHybridRuleSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 21),
    _ZxAnAclHybridRuleSVid_Type()
)
zxAnAclHybridRuleSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSVid.setStatus("current")


class _ZxAnAclHybridRuleCtagCos_Type(Integer32):
    """Custom type zxAnAclHybridRuleCtagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclHybridRuleCtagCos_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleCtagCos_Object = MibTableColumn
zxAnAclHybridRuleCtagCos = _ZxAnAclHybridRuleCtagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 22),
    _ZxAnAclHybridRuleCtagCos_Type()
)
zxAnAclHybridRuleCtagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleCtagCos.setStatus("current")


class _ZxAnAclHybridRuleCVid_Type(Integer32):
    """Custom type zxAnAclHybridRuleCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnAclHybridRuleCVid_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleCVid_Object = MibTableColumn
zxAnAclHybridRuleCVid = _ZxAnAclHybridRuleCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 23),
    _ZxAnAclHybridRuleCVid_Type()
)
zxAnAclHybridRuleCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleCVid.setStatus("current")
_ZxAnAclHybridRuleSrcMac_Type = MacAddress
_ZxAnAclHybridRuleSrcMac_Object = MibTableColumn
zxAnAclHybridRuleSrcMac = _ZxAnAclHybridRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 24),
    _ZxAnAclHybridRuleSrcMac_Type()
)
zxAnAclHybridRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcMac.setStatus("current")
_ZxAnAclHybridRuleSrcMacMask_Type = MacAddress
_ZxAnAclHybridRuleSrcMacMask_Object = MibTableColumn
zxAnAclHybridRuleSrcMacMask = _ZxAnAclHybridRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 25),
    _ZxAnAclHybridRuleSrcMacMask_Type()
)
zxAnAclHybridRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleSrcMacMask.setStatus("current")
_ZxAnAclHybridRuleDestMac_Type = MacAddress
_ZxAnAclHybridRuleDestMac_Object = MibTableColumn
zxAnAclHybridRuleDestMac = _ZxAnAclHybridRuleDestMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 26),
    _ZxAnAclHybridRuleDestMac_Type()
)
zxAnAclHybridRuleDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestMac.setStatus("current")
_ZxAnAclHybridRuleDestMacMask_Type = MacAddress
_ZxAnAclHybridRuleDestMacMask_Object = MibTableColumn
zxAnAclHybridRuleDestMacMask = _ZxAnAclHybridRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 27),
    _ZxAnAclHybridRuleDestMacMask_Type()
)
zxAnAclHybridRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleDestMacMask.setStatus("current")


class _ZxAnQosPclRuleTimeRangeName_Type(DisplayString):
    """Custom type zxAnQosPclRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnQosPclRuleTimeRangeName_Type.__name__ = "DisplayString"
_ZxAnQosPclRuleTimeRangeName_Object = MibTableColumn
zxAnQosPclRuleTimeRangeName = _ZxAnQosPclRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 28),
    _ZxAnQosPclRuleTimeRangeName_Type()
)
zxAnQosPclRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclRuleTimeRangeName.setStatus("current")


class _ZxAnQosPclRuleSrcAddrPfxLen_Type(InetAddressPrefixLength):
    """Custom type zxAnQosPclRuleSrcAddrPfxLen based on InetAddressPrefixLength"""
    defaultValue = 64


_ZxAnQosPclRuleSrcAddrPfxLen_Type.__name__ = "InetAddressPrefixLength"
_ZxAnQosPclRuleSrcAddrPfxLen_Object = MibTableColumn
zxAnQosPclRuleSrcAddrPfxLen = _ZxAnQosPclRuleSrcAddrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 29),
    _ZxAnQosPclRuleSrcAddrPfxLen_Type()
)
zxAnQosPclRuleSrcAddrPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclRuleSrcAddrPfxLen.setStatus("current")


class _ZxAnQosPclRuleDestAddrPfxLen_Type(InetAddressPrefixLength):
    """Custom type zxAnQosPclRuleDestAddrPfxLen based on InetAddressPrefixLength"""
    defaultValue = 64


_ZxAnQosPclRuleDestAddrPfxLen_Type.__name__ = "InetAddressPrefixLength"
_ZxAnQosPclRuleDestAddrPfxLen_Object = MibTableColumn
zxAnQosPclRuleDestAddrPfxLen = _ZxAnQosPclRuleDestAddrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 30),
    _ZxAnQosPclRuleDestAddrPfxLen_Type()
)
zxAnQosPclRuleDestAddrPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclRuleDestAddrPfxLen.setStatus("current")


class _ZxAnQosPclRuleTrafficClass_Type(Integer32):
    """Custom type zxAnQosPclRuleTrafficClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnQosPclRuleTrafficClass_Type.__name__ = "Integer32"
_ZxAnQosPclRuleTrafficClass_Object = MibTableColumn
zxAnQosPclRuleTrafficClass = _ZxAnQosPclRuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 31),
    _ZxAnQosPclRuleTrafficClass_Type()
)
zxAnQosPclRuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclRuleTrafficClass.setStatus("current")


class _ZxAnQosPclRuleFlowLabel_Type(Integer32):
    """Custom type zxAnQosPclRuleFlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(16777215, 16777215),
    )


_ZxAnQosPclRuleFlowLabel_Type.__name__ = "Integer32"
_ZxAnQosPclRuleFlowLabel_Object = MibTableColumn
zxAnQosPclRuleFlowLabel = _ZxAnQosPclRuleFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 32),
    _ZxAnQosPclRuleFlowLabel_Type()
)
zxAnQosPclRuleFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclRuleFlowLabel.setStatus("current")


class _ZxAnAclHybridRuleIcmpType_Type(Integer32):
    """Custom type zxAnAclHybridRuleIcmpType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclHybridRuleIcmpType_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleIcmpType_Object = MibTableColumn
zxAnAclHybridRuleIcmpType = _ZxAnAclHybridRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 33),
    _ZxAnAclHybridRuleIcmpType_Type()
)
zxAnAclHybridRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleIcmpType.setStatus("current")


class _ZxAnAclHybridRuleIcmpCode_Type(Integer32):
    """Custom type zxAnAclHybridRuleIcmpCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclHybridRuleIcmpCode_Type.__name__ = "Integer32"
_ZxAnAclHybridRuleIcmpCode_Object = MibTableColumn
zxAnAclHybridRuleIcmpCode = _ZxAnAclHybridRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 34),
    _ZxAnAclHybridRuleIcmpCode_Type()
)
zxAnAclHybridRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleIcmpCode.setStatus("current")
_ZxAnAclHybridRuleRowStatus_Type = RowStatus
_ZxAnAclHybridRuleRowStatus_Object = MibTableColumn
zxAnAclHybridRuleRowStatus = _ZxAnAclHybridRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 3, 1, 50),
    _ZxAnAclHybridRuleRowStatus_Type()
)
zxAnAclHybridRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclHybridRuleRowStatus.setStatus("current")
_ZxAnQosAclTrafficLimitTable_Object = MibTable
zxAnQosAclTrafficLimitTable = _ZxAnQosAclTrafficLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitTable.setStatus("current")
_ZxAnQosAclTrafficLimitEntry_Object = MibTableRow
zxAnQosAclTrafficLimitEntry = _ZxAnQosAclTrafficLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1)
)
zxAnQosAclTrafficLimitEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitEntry.setStatus("current")


class _ZxAnQosAclTrafficLimitCir_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnQosAclTrafficLimitCir_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitCir_Object = MibTableColumn
zxAnQosAclTrafficLimitCir = _ZxAnQosAclTrafficLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 1),
    _ZxAnQosAclTrafficLimitCir_Type()
)
zxAnQosAclTrafficLimitCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitCir.setStatus("current")


class _ZxAnQosAclTrafficLimitPir_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_ZxAnQosAclTrafficLimitPir_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitPir_Object = MibTableColumn
zxAnQosAclTrafficLimitPir = _ZxAnQosAclTrafficLimitPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 2),
    _ZxAnQosAclTrafficLimitPir_Type()
)
zxAnQosAclTrafficLimitPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitPir.setStatus("current")


class _ZxAnQosAclTrafficLimitCbs_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosAclTrafficLimitCbs_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitCbs_Object = MibTableColumn
zxAnQosAclTrafficLimitCbs = _ZxAnQosAclTrafficLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 3),
    _ZxAnQosAclTrafficLimitCbs_Type()
)
zxAnQosAclTrafficLimitCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitCbs.setStatus("current")


class _ZxAnQosAclTrafficLimitEbs_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosAclTrafficLimitEbs_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitEbs_Object = MibTableColumn
zxAnQosAclTrafficLimitEbs = _ZxAnQosAclTrafficLimitEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 4),
    _ZxAnQosAclTrafficLimitEbs_Type()
)
zxAnQosAclTrafficLimitEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitEbs.setStatus("current")


class _ZxAnQosAclTrafficLimitPbs_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosAclTrafficLimitPbs_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitPbs_Object = MibTableColumn
zxAnQosAclTrafficLimitPbs = _ZxAnQosAclTrafficLimitPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 5),
    _ZxAnQosAclTrafficLimitPbs_Type()
)
zxAnQosAclTrafficLimitPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitPbs.setStatus("current")


class _ZxAnQosAclTrafficLimitMode_Type(Integer32):
    """Custom type zxAnQosAclTrafficLimitMode based on Integer32"""
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


_ZxAnQosAclTrafficLimitMode_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficLimitMode_Object = MibTableColumn
zxAnQosAclTrafficLimitMode = _ZxAnQosAclTrafficLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 6),
    _ZxAnQosAclTrafficLimitMode_Type()
)
zxAnQosAclTrafficLimitMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficLimitMode.setStatus("current")
_ZxAnQosAclTrafficDropYellow_Type = TruthValue
_ZxAnQosAclTrafficDropYellow_Object = MibTableColumn
zxAnQosAclTrafficDropYellow = _ZxAnQosAclTrafficDropYellow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 7),
    _ZxAnQosAclTrafficDropYellow_Type()
)
zxAnQosAclTrafficDropYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficDropYellow.setStatus("current")
_ZxAnQosAclTrafficForwardRed_Type = TruthValue
_ZxAnQosAclTrafficForwardRed_Object = MibTableColumn
zxAnQosAclTrafficForwardRed = _ZxAnQosAclTrafficForwardRed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 8),
    _ZxAnQosAclTrafficForwardRed_Type()
)
zxAnQosAclTrafficForwardRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficForwardRed.setStatus("current")


class _ZxAnQosAclTrafficRemarkRedDp_Type(Integer32):
    """Custom type zxAnQosAclTrafficRemarkRedDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_ZxAnQosAclTrafficRemarkRedDp_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficRemarkRedDp_Object = MibTableColumn
zxAnQosAclTrafficRemarkRedDp = _ZxAnQosAclTrafficRemarkRedDp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 9),
    _ZxAnQosAclTrafficRemarkRedDp_Type()
)
zxAnQosAclTrafficRemarkRedDp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficRemarkRedDp.setStatus("current")


class _ZxAnQosAclTrafficRemarkRedDscp_Type(Integer32):
    """Custom type zxAnQosAclTrafficRemarkRedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosAclTrafficRemarkRedDscp_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficRemarkRedDscp_Object = MibTableColumn
zxAnQosAclTrafficRemarkRedDscp = _ZxAnQosAclTrafficRemarkRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 10),
    _ZxAnQosAclTrafficRemarkRedDscp_Type()
)
zxAnQosAclTrafficRemarkRedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficRemarkRedDscp.setStatus("current")


class _ZxAnQosAclTrafficRemarkYellDp_Type(Integer32):
    """Custom type zxAnQosAclTrafficRemarkYellDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_ZxAnQosAclTrafficRemarkYellDp_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficRemarkYellDp_Object = MibTableColumn
zxAnQosAclTrafficRemarkYellDp = _ZxAnQosAclTrafficRemarkYellDp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 11),
    _ZxAnQosAclTrafficRemarkYellDp_Type()
)
zxAnQosAclTrafficRemarkYellDp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficRemarkYellDp.setStatus("current")


class _ZxAnQosAclTrafficRemarkYellDscp_Type(Integer32):
    """Custom type zxAnQosAclTrafficRemarkYellDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosAclTrafficRemarkYellDscp_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficRemarkYellDscp_Object = MibTableColumn
zxAnQosAclTrafficRemarkYellDscp = _ZxAnQosAclTrafficRemarkYellDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 12),
    _ZxAnQosAclTrafficRemarkYellDscp_Type()
)
zxAnQosAclTrafficRemarkYellDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficRemarkYellDscp.setStatus("current")
_ZxAnQosAclTrafficRowStatus_Type = RowStatus
_ZxAnQosAclTrafficRowStatus_Object = MibTableColumn
zxAnQosAclTrafficRowStatus = _ZxAnQosAclTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 4, 1, 50),
    _ZxAnQosAclTrafficRowStatus_Type()
)
zxAnQosAclTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficRowStatus.setStatus("current")
_ZxAnQosAclPriorityMarkTable_Object = MibTable
zxAnQosAclPriorityMarkTable = _ZxAnQosAclPriorityMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnQosAclPriorityMarkTable.setStatus("current")
_ZxAnQosAclPriorityMarkEntry_Object = MibTableRow
zxAnQosAclPriorityMarkEntry = _ZxAnQosAclPriorityMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1)
)
zxAnQosAclPriorityMarkEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosAclPriorityMarkEntry.setStatus("current")


class _ZxAnQosAclPriMarkDscp_Type(Integer32):
    """Custom type zxAnQosAclPriMarkDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosAclPriMarkDscp_Type.__name__ = "Integer32"
_ZxAnQosAclPriMarkDscp_Object = MibTableColumn
zxAnQosAclPriMarkDscp = _ZxAnQosAclPriMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 1),
    _ZxAnQosAclPriMarkDscp_Type()
)
zxAnQosAclPriMarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkDscp.setStatus("current")


class _ZxAnQosAclPriMarkCos_Type(Integer32):
    """Custom type zxAnQosAclPriMarkCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosAclPriMarkCos_Type.__name__ = "Integer32"
_ZxAnQosAclPriMarkCos_Object = MibTableColumn
zxAnQosAclPriMarkCos = _ZxAnQosAclPriMarkCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 2),
    _ZxAnQosAclPriMarkCos_Type()
)
zxAnQosAclPriMarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkCos.setStatus("current")


class _ZxAnQosAclPriMarkPrecedence_Type(Integer32):
    """Custom type zxAnQosAclPriMarkPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosAclPriMarkPrecedence_Type.__name__ = "Integer32"
_ZxAnQosAclPriMarkPrecedence_Object = MibTableColumn
zxAnQosAclPriMarkPrecedence = _ZxAnQosAclPriMarkPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 3),
    _ZxAnQosAclPriMarkPrecedence_Type()
)
zxAnQosAclPriMarkPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkPrecedence.setStatus("current")


class _ZxAnQosAclPriMarkLocalPrecedence_Type(Integer32):
    """Custom type zxAnQosAclPriMarkLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosAclPriMarkLocalPrecedence_Type.__name__ = "Integer32"
_ZxAnQosAclPriMarkLocalPrecedence_Object = MibTableColumn
zxAnQosAclPriMarkLocalPrecedence = _ZxAnQosAclPriMarkLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 4),
    _ZxAnQosAclPriMarkLocalPrecedence_Type()
)
zxAnQosAclPriMarkLocalPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkLocalPrecedence.setStatus("current")


class _ZxAnQosAclPriMarkDropPrecedence_Type(Integer32):
    """Custom type zxAnQosAclPriMarkDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_ZxAnQosAclPriMarkDropPrecedence_Type.__name__ = "Integer32"
_ZxAnQosAclPriMarkDropPrecedence_Object = MibTableColumn
zxAnQosAclPriMarkDropPrecedence = _ZxAnQosAclPriMarkDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 5),
    _ZxAnQosAclPriMarkDropPrecedence_Type()
)
zxAnQosAclPriMarkDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkDropPrecedence.setStatus("current")


class _ZxAnQosPclPriMarkTrafficClass_Type(Integer32):
    """Custom type zxAnQosPclPriMarkTrafficClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnQosPclPriMarkTrafficClass_Type.__name__ = "Integer32"
_ZxAnQosPclPriMarkTrafficClass_Object = MibTableColumn
zxAnQosPclPriMarkTrafficClass = _ZxAnQosPclPriMarkTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 6),
    _ZxAnQosPclPriMarkTrafficClass_Type()
)
zxAnQosPclPriMarkTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclPriMarkTrafficClass.setStatus("current")
_ZxAnQosAclPriMarkRowStatus_Type = RowStatus
_ZxAnQosAclPriMarkRowStatus_Object = MibTableColumn
zxAnQosAclPriMarkRowStatus = _ZxAnQosAclPriMarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 5, 1, 30),
    _ZxAnQosAclPriMarkRowStatus_Type()
)
zxAnQosAclPriMarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclPriMarkRowStatus.setStatus("current")
_ZxAnQosAclVlanMarkTable_Object = MibTable
zxAnQosAclVlanMarkTable = _ZxAnQosAclVlanMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnQosAclVlanMarkTable.setStatus("current")
_ZxAnQosAclVlanMarkEntry_Object = MibTableRow
zxAnQosAclVlanMarkEntry = _ZxAnQosAclVlanMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 6, 1)
)
zxAnQosAclVlanMarkEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosAclVlanMarkEntry.setStatus("current")


class _ZxAnQosAclVlanMarkVid_Type(Integer32):
    """Custom type zxAnQosAclVlanMarkVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_ZxAnQosAclVlanMarkVid_Type.__name__ = "Integer32"
_ZxAnQosAclVlanMarkVid_Object = MibTableColumn
zxAnQosAclVlanMarkVid = _ZxAnQosAclVlanMarkVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 6, 1, 1),
    _ZxAnQosAclVlanMarkVid_Type()
)
zxAnQosAclVlanMarkVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclVlanMarkVid.setStatus("current")
_ZxAnQosAclVlanMarkRowStatus_Type = RowStatus
_ZxAnQosAclVlanMarkRowStatus_Object = MibTableColumn
zxAnQosAclVlanMarkRowStatus = _ZxAnQosAclVlanMarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 6, 1, 30),
    _ZxAnQosAclVlanMarkRowStatus_Type()
)
zxAnQosAclVlanMarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclVlanMarkRowStatus.setStatus("current")
_ZxAnQosPclQinqTable_Object = MibTable
zxAnQosPclQinqTable = _ZxAnQosPclQinqTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnQosPclQinqTable.setStatus("current")
_ZxAnQosPclQinqEntry_Object = MibTableRow
zxAnQosPclQinqEntry = _ZxAnQosPclQinqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 7, 1)
)
zxAnQosPclQinqEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosPclQinqEntry.setStatus("current")


class _ZxAnQosPclQinqSvlan_Type(Integer32):
    """Custom type zxAnQosPclQinqSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_ZxAnQosPclQinqSvlan_Type.__name__ = "Integer32"
_ZxAnQosPclQinqSvlan_Object = MibTableColumn
zxAnQosPclQinqSvlan = _ZxAnQosPclQinqSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 7, 1, 1),
    _ZxAnQosPclQinqSvlan_Type()
)
zxAnQosPclQinqSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclQinqSvlan.setStatus("current")


class _ZxAnQosPclQinqCvlan_Type(Integer32):
    """Custom type zxAnQosPclQinqCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_ZxAnQosPclQinqCvlan_Type.__name__ = "Integer32"
_ZxAnQosPclQinqCvlan_Object = MibTableColumn
zxAnQosPclQinqCvlan = _ZxAnQosPclQinqCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 7, 1, 2),
    _ZxAnQosPclQinqCvlan_Type()
)
zxAnQosPclQinqCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclQinqCvlan.setStatus("current")
_ZxAnQosPclQinqRowStatus_Type = RowStatus
_ZxAnQosPclQinqRowStatus_Object = MibTableColumn
zxAnQosPclQinqRowStatus = _ZxAnQosPclQinqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 7, 1, 30),
    _ZxAnQosPclQinqRowStatus_Type()
)
zxAnQosPclQinqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclQinqRowStatus.setStatus("current")
_ZxAnQosAclRedirectTable_Object = MibTable
zxAnQosAclRedirectTable = _ZxAnQosAclRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnQosAclRedirectTable.setStatus("current")
_ZxAnQosAclRedirectEntry_Object = MibTableRow
zxAnQosAclRedirectEntry = _ZxAnQosAclRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1)
)
zxAnQosAclRedirectEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosAclRedirectEntry.setStatus("current")
_ZxAnQosAclRedirectIf_Type = Integer32
_ZxAnQosAclRedirectIf_Object = MibTableColumn
zxAnQosAclRedirectIf = _ZxAnQosAclRedirectIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1, 1),
    _ZxAnQosAclRedirectIf_Type()
)
zxAnQosAclRedirectIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclRedirectIf.setStatus("current")


class _ZxAnQosAclRedirectType_Type(Integer32):
    """Custom type zxAnQosAclRedirectType based on Integer32"""
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


_ZxAnQosAclRedirectType_Type.__name__ = "Integer32"
_ZxAnQosAclRedirectType_Object = MibTableColumn
zxAnQosAclRedirectType = _ZxAnQosAclRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1, 2),
    _ZxAnQosAclRedirectType_Type()
)
zxAnQosAclRedirectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclRedirectType.setStatus("current")


class _ZxAnQosAclRedirectNextHopIpType_Type(InetAddressType):
    """Custom type zxAnQosAclRedirectNextHopIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnQosAclRedirectNextHopIpType_Type.__name__ = "InetAddressType"
_ZxAnQosAclRedirectNextHopIpType_Object = MibTableColumn
zxAnQosAclRedirectNextHopIpType = _ZxAnQosAclRedirectNextHopIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1, 3),
    _ZxAnQosAclRedirectNextHopIpType_Type()
)
zxAnQosAclRedirectNextHopIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclRedirectNextHopIpType.setStatus("current")
_ZxAnQosAclRedirectNextHopIp_Type = InetAddress
_ZxAnQosAclRedirectNextHopIp_Object = MibTableColumn
zxAnQosAclRedirectNextHopIp = _ZxAnQosAclRedirectNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1, 4),
    _ZxAnQosAclRedirectNextHopIp_Type()
)
zxAnQosAclRedirectNextHopIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclRedirectNextHopIp.setStatus("current")
_ZxAnQosAclRedirectRowStatus_Type = RowStatus
_ZxAnQosAclRedirectRowStatus_Object = MibTableColumn
zxAnQosAclRedirectRowStatus = _ZxAnQosAclRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 8, 1, 30),
    _ZxAnQosAclRedirectRowStatus_Type()
)
zxAnQosAclRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclRedirectRowStatus.setStatus("current")
_ZxAnQosAclTrafficMirrorTable_Object = MibTable
zxAnQosAclTrafficMirrorTable = _ZxAnQosAclTrafficMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9)
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorTable.setStatus("current")
_ZxAnQosAclTrafficMirrorEntry_Object = MibTableRow
zxAnQosAclTrafficMirrorEntry = _ZxAnQosAclTrafficMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1)
)
zxAnQosAclTrafficMirrorEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorEntry.setStatus("current")
_ZxAnQosAclTrafficMirrorIf_Type = Integer32
_ZxAnQosAclTrafficMirrorIf_Object = MibTableColumn
zxAnQosAclTrafficMirrorIf = _ZxAnQosAclTrafficMirrorIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 1),
    _ZxAnQosAclTrafficMirrorIf_Type()
)
zxAnQosAclTrafficMirrorIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorIf.setStatus("current")


class _ZxAnQosAclTrafficMirrorType_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorType based on Integer32"""
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
        *(("cpu", 1),
          ("interface", 2),
          ("rspan", 3),
          ("erspan", 4))
    )


_ZxAnQosAclTrafficMirrorType_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorType_Object = MibTableColumn
zxAnQosAclTrafficMirrorType = _ZxAnQosAclTrafficMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 2),
    _ZxAnQosAclTrafficMirrorType_Type()
)
zxAnQosAclTrafficMirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorType.setStatus("current")


class _ZxAnQosAclTrafficMirrorVlanId_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_ZxAnQosAclTrafficMirrorVlanId_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorVlanId_Object = MibTableColumn
zxAnQosAclTrafficMirrorVlanId = _ZxAnQosAclTrafficMirrorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 3),
    _ZxAnQosAclTrafficMirrorVlanId_Type()
)
zxAnQosAclTrafficMirrorVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorVlanId.setStatus("current")


class _ZxAnQosAclTrafficMirrorCos_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosAclTrafficMirrorCos_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorCos_Object = MibTableColumn
zxAnQosAclTrafficMirrorCos = _ZxAnQosAclTrafficMirrorCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 4),
    _ZxAnQosAclTrafficMirrorCos_Type()
)
zxAnQosAclTrafficMirrorCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorCos.setStatus("current")


class _ZxAnQosAclTrafficMirrorTpid_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorTpid based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnQosAclTrafficMirrorTpid_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorTpid_Object = MibTableColumn
zxAnQosAclTrafficMirrorTpid = _ZxAnQosAclTrafficMirrorTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 5),
    _ZxAnQosAclTrafficMirrorTpid_Type()
)
zxAnQosAclTrafficMirrorTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorTpid.setStatus("current")


class _ZxAnQosAclTrafficMirrorDstIpType_Type(InetAddressType):
    """Custom type zxAnQosAclTrafficMirrorDstIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnQosAclTrafficMirrorDstIpType_Type.__name__ = "InetAddressType"
_ZxAnQosAclTrafficMirrorDstIpType_Object = MibTableColumn
zxAnQosAclTrafficMirrorDstIpType = _ZxAnQosAclTrafficMirrorDstIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 6),
    _ZxAnQosAclTrafficMirrorDstIpType_Type()
)
zxAnQosAclTrafficMirrorDstIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorDstIpType.setStatus("current")
_ZxAnQosAclTrafficMirrorDstIpAddr_Type = InetAddress
_ZxAnQosAclTrafficMirrorDstIpAddr_Object = MibTableColumn
zxAnQosAclTrafficMirrorDstIpAddr = _ZxAnQosAclTrafficMirrorDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 7),
    _ZxAnQosAclTrafficMirrorDstIpAddr_Type()
)
zxAnQosAclTrafficMirrorDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorDstIpAddr.setStatus("current")


class _ZxAnQosAclTrafficMirrorSrcIpType_Type(InetAddressType):
    """Custom type zxAnQosAclTrafficMirrorSrcIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnQosAclTrafficMirrorSrcIpType_Type.__name__ = "InetAddressType"
_ZxAnQosAclTrafficMirrorSrcIpType_Object = MibTableColumn
zxAnQosAclTrafficMirrorSrcIpType = _ZxAnQosAclTrafficMirrorSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 8),
    _ZxAnQosAclTrafficMirrorSrcIpType_Type()
)
zxAnQosAclTrafficMirrorSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorSrcIpType.setStatus("current")
_ZxAnQosAclTrafficMirrorSrcIpAddr_Type = InetAddress
_ZxAnQosAclTrafficMirrorSrcIpAddr_Object = MibTableColumn
zxAnQosAclTrafficMirrorSrcIpAddr = _ZxAnQosAclTrafficMirrorSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 9),
    _ZxAnQosAclTrafficMirrorSrcIpAddr_Type()
)
zxAnQosAclTrafficMirrorSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorSrcIpAddr.setStatus("current")


class _ZxAnQosAclTrafficMirrorTtl_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorTtl based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_ZxAnQosAclTrafficMirrorTtl_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorTtl_Object = MibTableColumn
zxAnQosAclTrafficMirrorTtl = _ZxAnQosAclTrafficMirrorTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 10),
    _ZxAnQosAclTrafficMirrorTtl_Type()
)
zxAnQosAclTrafficMirrorTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorTtl.setStatus("current")


class _ZxAnQosAclTrafficMirrorDscp_Type(Integer32):
    """Custom type zxAnQosAclTrafficMirrorDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosAclTrafficMirrorDscp_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficMirrorDscp_Object = MibTableColumn
zxAnQosAclTrafficMirrorDscp = _ZxAnQosAclTrafficMirrorDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 11),
    _ZxAnQosAclTrafficMirrorDscp_Type()
)
zxAnQosAclTrafficMirrorDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorDscp.setStatus("current")
_ZxAnQosAclTrafficMirrorRowStatus_Type = RowStatus
_ZxAnQosAclTrafficMirrorRowStatus_Object = MibTableColumn
zxAnQosAclTrafficMirrorRowStatus = _ZxAnQosAclTrafficMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 9, 1, 30),
    _ZxAnQosAclTrafficMirrorRowStatus_Type()
)
zxAnQosAclTrafficMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficMirrorRowStatus.setStatus("current")
_ZxAnQosAclTrafficStatsTable_Object = MibTable
zxAnQosAclTrafficStatsTable = _ZxAnQosAclTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10)
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsTable.setStatus("current")
_ZxAnQosAclTrafficStatsEntry_Object = MibTableRow
zxAnQosAclTrafficStatsEntry = _ZxAnQosAclTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1)
)
zxAnQosAclTrafficStatsEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclHybridRuleId"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosAclTrafficStatsPktColor"),
)
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsEntry.setStatus("current")


class _ZxAnQosAclTrafficStatsPktColor_Type(Integer32):
    """Custom type zxAnQosAclTrafficStatsPktColor based on Integer32"""
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
        *(("all", 1),
          ("red", 2),
          ("yellow", 3),
          ("green", 4))
    )


_ZxAnQosAclTrafficStatsPktColor_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficStatsPktColor_Object = MibTableColumn
zxAnQosAclTrafficStatsPktColor = _ZxAnQosAclTrafficStatsPktColor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 1),
    _ZxAnQosAclTrafficStatsPktColor_Type()
)
zxAnQosAclTrafficStatsPktColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsPktColor.setStatus("current")


class _ZxAnQosAclTrafficStatsType_Type(Integer32):
    """Custom type zxAnQosAclTrafficStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("byte", 2))
    )


_ZxAnQosAclTrafficStatsType_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficStatsType_Object = MibTableColumn
zxAnQosAclTrafficStatsType = _ZxAnQosAclTrafficStatsType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 2),
    _ZxAnQosAclTrafficStatsType_Type()
)
zxAnQosAclTrafficStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsType.setStatus("current")
_ZxAnQosAclTrafficStatsPkts_Type = Counter32
_ZxAnQosAclTrafficStatsPkts_Object = MibTableColumn
zxAnQosAclTrafficStatsPkts = _ZxAnQosAclTrafficStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 3),
    _ZxAnQosAclTrafficStatsPkts_Type()
)
zxAnQosAclTrafficStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsPkts.setStatus("current")
_ZxAnQosAclTrafficStatsOctets_Type = Counter32
_ZxAnQosAclTrafficStatsOctets_Object = MibTableColumn
zxAnQosAclTrafficStatsOctets = _ZxAnQosAclTrafficStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 4),
    _ZxAnQosAclTrafficStatsOctets_Type()
)
zxAnQosAclTrafficStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsOctets.setStatus("current")


class _ZxAnQosAclTrafficStatsReset_Type(Integer32):
    """Custom type zxAnQosAclTrafficStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("resetCounter", 3)
    )


_ZxAnQosAclTrafficStatsReset_Type.__name__ = "Integer32"
_ZxAnQosAclTrafficStatsReset_Object = MibTableColumn
zxAnQosAclTrafficStatsReset = _ZxAnQosAclTrafficStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 5),
    _ZxAnQosAclTrafficStatsReset_Type()
)
zxAnQosAclTrafficStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsReset.setStatus("current")
_ZxAnQosAclTrafficStatsRowStatus_Type = RowStatus
_ZxAnQosAclTrafficStatsRowStatus_Object = MibTableColumn
zxAnQosAclTrafficStatsRowStatus = _ZxAnQosAclTrafficStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 10, 1, 50),
    _ZxAnQosAclTrafficStatsRowStatus_Type()
)
zxAnQosAclTrafficStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosAclTrafficStatsRowStatus.setStatus("current")
_ZxAnQosPclTimeRangeTable_Object = MibTable
zxAnQosPclTimeRangeTable = _ZxAnQosPclTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnQosPclTimeRangeTable.setStatus("current")
_ZxAnQosPclTimeRangeEntry_Object = MibTableRow
zxAnQosPclTimeRangeEntry = _ZxAnQosPclTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1)
)
zxAnQosPclTimeRangeEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclTimeRangeName"),
)
if mibBuilder.loadTexts:
    zxAnQosPclTimeRangeEntry.setStatus("current")
_ZxAnQosPclTimeRangeName_Type = DisplayString
_ZxAnQosPclTimeRangeName_Object = MibTableColumn
zxAnQosPclTimeRangeName = _ZxAnQosPclTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 1),
    _ZxAnQosPclTimeRangeName_Type()
)
zxAnQosPclTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclTimeRangeName.setStatus("current")


class _ZxAnQosPclTimeRangeType_Type(Integer32):
    """Custom type zxAnQosPclTimeRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onlyonce", 1),
          ("weekly", 2))
    )


_ZxAnQosPclTimeRangeType_Type.__name__ = "Integer32"
_ZxAnQosPclTimeRangeType_Object = MibTableColumn
zxAnQosPclTimeRangeType = _ZxAnQosPclTimeRangeType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 2),
    _ZxAnQosPclTimeRangeType_Type()
)
zxAnQosPclTimeRangeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclTimeRangeType.setStatus("current")
_ZxAnQosPclOnceStartTime_Type = DisplayString
_ZxAnQosPclOnceStartTime_Object = MibTableColumn
zxAnQosPclOnceStartTime = _ZxAnQosPclOnceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 3),
    _ZxAnQosPclOnceStartTime_Type()
)
zxAnQosPclOnceStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclOnceStartTime.setStatus("current")
_ZxAnQosPclOnceEndTime_Type = DisplayString
_ZxAnQosPclOnceEndTime_Object = MibTableColumn
zxAnQosPclOnceEndTime = _ZxAnQosPclOnceEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 4),
    _ZxAnQosPclOnceEndTime_Type()
)
zxAnQosPclOnceEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclOnceEndTime.setStatus("current")


class _ZxAnQosPclWeeklyDay_Type(Bits):
    """Custom type zxAnQosPclWeeklyDay based on Bits"""
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )

_ZxAnQosPclWeeklyDay_Type.__name__ = "Bits"
_ZxAnQosPclWeeklyDay_Object = MibTableColumn
zxAnQosPclWeeklyDay = _ZxAnQosPclWeeklyDay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 5),
    _ZxAnQosPclWeeklyDay_Type()
)
zxAnQosPclWeeklyDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclWeeklyDay.setStatus("current")
_ZxAnQosPclWeeklyStartTime_Type = DisplayString
_ZxAnQosPclWeeklyStartTime_Object = MibTableColumn
zxAnQosPclWeeklyStartTime = _ZxAnQosPclWeeklyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 6),
    _ZxAnQosPclWeeklyStartTime_Type()
)
zxAnQosPclWeeklyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclWeeklyStartTime.setStatus("current")
_ZxAnQosPclWeeklyEndTime_Type = DisplayString
_ZxAnQosPclWeeklyEndTime_Object = MibTableColumn
zxAnQosPclWeeklyEndTime = _ZxAnQosPclWeeklyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 7),
    _ZxAnQosPclWeeklyEndTime_Type()
)
zxAnQosPclWeeklyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclWeeklyEndTime.setStatus("current")
_ZxAnQosPclTimeRangeRowStatus_Type = RowStatus
_ZxAnQosPclTimeRangeRowStatus_Object = MibTableColumn
zxAnQosPclTimeRangeRowStatus = _ZxAnQosPclTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 11, 1, 30),
    _ZxAnQosPclTimeRangeRowStatus_Type()
)
zxAnQosPclTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosPclTimeRangeRowStatus.setStatus("current")
_ZxAnAclIfConfTable_Object = MibTable
zxAnAclIfConfTable = _ZxAnAclIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12)
)
if mibBuilder.loadTexts:
    zxAnAclIfConfTable.setStatus("current")
_ZxAnAclIfConfEntry_Object = MibTableRow
zxAnAclIfConfEntry = _ZxAnAclIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1)
)
zxAnAclIfConfEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindRack"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindShelf"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindSlot"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindPort"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindOnu"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindVCircuitType"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindVCircuit"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclBindDirection"),
)
if mibBuilder.loadTexts:
    zxAnAclIfConfEntry.setStatus("current")
_ZxAnQosPclBindRack_Type = Integer32
_ZxAnQosPclBindRack_Object = MibTableColumn
zxAnQosPclBindRack = _ZxAnQosPclBindRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 1),
    _ZxAnQosPclBindRack_Type()
)
zxAnQosPclBindRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindRack.setStatus("current")
_ZxAnQosPclBindShelf_Type = Integer32
_ZxAnQosPclBindShelf_Object = MibTableColumn
zxAnQosPclBindShelf = _ZxAnQosPclBindShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 2),
    _ZxAnQosPclBindShelf_Type()
)
zxAnQosPclBindShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindShelf.setStatus("current")
_ZxAnQosPclBindSlot_Type = Integer32
_ZxAnQosPclBindSlot_Object = MibTableColumn
zxAnQosPclBindSlot = _ZxAnQosPclBindSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 3),
    _ZxAnQosPclBindSlot_Type()
)
zxAnQosPclBindSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindSlot.setStatus("current")
_ZxAnQosPclBindPort_Type = Integer32
_ZxAnQosPclBindPort_Object = MibTableColumn
zxAnQosPclBindPort = _ZxAnQosPclBindPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 4),
    _ZxAnQosPclBindPort_Type()
)
zxAnQosPclBindPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindPort.setStatus("current")
_ZxAnQosPclBindOnu_Type = Integer32
_ZxAnQosPclBindOnu_Object = MibTableColumn
zxAnQosPclBindOnu = _ZxAnQosPclBindOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 5),
    _ZxAnQosPclBindOnu_Type()
)
zxAnQosPclBindOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindOnu.setStatus("current")


class _ZxAnQosPclBindVCircuitType_Type(Integer32):
    """Custom type zxAnQosPclBindVCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("physicalport", 1),
          ("bridgeport", 2),
          ("epononu", 3),
          ("gpononu", 4),
          ("serviceport", 11),
          ("vlan", 12),
          ("innerPort", 13))
    )


_ZxAnQosPclBindVCircuitType_Type.__name__ = "Integer32"
_ZxAnQosPclBindVCircuitType_Object = MibTableColumn
zxAnQosPclBindVCircuitType = _ZxAnQosPclBindVCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 6),
    _ZxAnQosPclBindVCircuitType_Type()
)
zxAnQosPclBindVCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindVCircuitType.setStatus("current")
_ZxAnQosPclBindVCircuit_Type = Integer32
_ZxAnQosPclBindVCircuit_Object = MibTableColumn
zxAnQosPclBindVCircuit = _ZxAnQosPclBindVCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 7),
    _ZxAnQosPclBindVCircuit_Type()
)
zxAnQosPclBindVCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindVCircuit.setStatus("current")


class _ZxAnQosPclBindDirection_Type(Integer32):
    """Custom type zxAnQosPclBindDirection based on Integer32"""
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


_ZxAnQosPclBindDirection_Type.__name__ = "Integer32"
_ZxAnQosPclBindDirection_Object = MibTableColumn
zxAnQosPclBindDirection = _ZxAnQosPclBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 8),
    _ZxAnQosPclBindDirection_Type()
)
zxAnQosPclBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclBindDirection.setStatus("current")


class _ZxAnAclIfConfAclNumber_Type(Integer32):
    """Custom type zxAnAclIfConfAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
        ValueRangeConstraint(600, 699),
    )


_ZxAnAclIfConfAclNumber_Type.__name__ = "Integer32"
_ZxAnAclIfConfAclNumber_Object = MibTableColumn
zxAnAclIfConfAclNumber = _ZxAnAclIfConfAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 9),
    _ZxAnAclIfConfAclNumber_Type()
)
zxAnAclIfConfAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclIfConfAclNumber.setStatus("current")


class _ZxAnAclIfConfAclName_Type(DisplayString):
    """Custom type zxAnAclIfConfAclName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAclIfConfAclName_Type.__name__ = "DisplayString"
_ZxAnAclIfConfAclName_Object = MibTableColumn
zxAnAclIfConfAclName = _ZxAnAclIfConfAclName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 10),
    _ZxAnAclIfConfAclName_Type()
)
zxAnAclIfConfAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclIfConfAclName.setStatus("current")
_ZxAnAclIfConfRowStatus_Type = RowStatus
_ZxAnAclIfConfRowStatus_Object = MibTableColumn
zxAnAclIfConfRowStatus = _ZxAnAclIfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 12, 1, 30),
    _ZxAnAclIfConfRowStatus_Type()
)
zxAnAclIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclIfConfRowStatus.setStatus("current")
_ZxAnQosPclGlobalBindingTable_Object = MibTable
zxAnQosPclGlobalBindingTable = _ZxAnQosPclGlobalBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 13)
)
if mibBuilder.loadTexts:
    zxAnQosPclGlobalBindingTable.setStatus("current")
_ZxAnQosPclGlobalBindingEntry_Object = MibTableRow
zxAnQosPclGlobalBindingEntry = _ZxAnQosPclGlobalBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 13, 1)
)
zxAnQosPclGlobalBindingEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnQosPclGlobalBindingType"),
)
if mibBuilder.loadTexts:
    zxAnQosPclGlobalBindingEntry.setStatus("current")


class _ZxAnQosPclGlobalBindingType_Type(Integer32):
    """Custom type zxAnQosPclGlobalBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("voip", 1)
    )


_ZxAnQosPclGlobalBindingType_Type.__name__ = "Integer32"
_ZxAnQosPclGlobalBindingType_Object = MibTableColumn
zxAnQosPclGlobalBindingType = _ZxAnQosPclGlobalBindingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 13, 1, 1),
    _ZxAnQosPclGlobalBindingType_Type()
)
zxAnQosPclGlobalBindingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosPclGlobalBindingType.setStatus("current")


class _ZxAnQosPclGlobalBindingIndex_Type(Integer32):
    """Custom type zxAnQosPclGlobalBindingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 399),
        ValueRangeConstraint(600, 699),
    )


_ZxAnQosPclGlobalBindingIndex_Type.__name__ = "Integer32"
_ZxAnQosPclGlobalBindingIndex_Object = MibTableColumn
zxAnQosPclGlobalBindingIndex = _ZxAnQosPclGlobalBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 13, 1, 2),
    _ZxAnQosPclGlobalBindingIndex_Type()
)
zxAnQosPclGlobalBindingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosPclGlobalBindingIndex.setStatus("current")
_ZxAnAclStandardRuleTable_Object = MibTable
zxAnAclStandardRuleTable = _ZxAnAclStandardRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14)
)
if mibBuilder.loadTexts:
    zxAnAclStandardRuleTable.setStatus("current")
_ZxAnAclStandardRuleEntry_Object = MibTableRow
zxAnAclStandardRuleEntry = _ZxAnAclStandardRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1)
)
zxAnAclStandardRuleEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclStdAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclStdRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclStandardRuleEntry.setStatus("current")


class _ZxAnAclStdAclNumber_Type(Integer32):
    """Custom type zxAnAclStdAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ZxAnAclStdAclNumber_Type.__name__ = "Integer32"
_ZxAnAclStdAclNumber_Object = MibTableColumn
zxAnAclStdAclNumber = _ZxAnAclStdAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 1),
    _ZxAnAclStdAclNumber_Type()
)
zxAnAclStdAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclStdAclNumber.setStatus("current")


class _ZxAnAclStdRuleId_Type(Integer32):
    """Custom type zxAnAclStdRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxAnAclStdRuleId_Type.__name__ = "Integer32"
_ZxAnAclStdRuleId_Object = MibTableColumn
zxAnAclStdRuleId = _ZxAnAclStdRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 2),
    _ZxAnAclStdRuleId_Type()
)
zxAnAclStdRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclStdRuleId.setStatus("current")


class _ZxAnAclStdRuleAccessCtrl_Type(Integer32):
    """Custom type zxAnAclStdRuleAccessCtrl based on Integer32"""
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


_ZxAnAclStdRuleAccessCtrl_Type.__name__ = "Integer32"
_ZxAnAclStdRuleAccessCtrl_Object = MibTableColumn
zxAnAclStdRuleAccessCtrl = _ZxAnAclStdRuleAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 3),
    _ZxAnAclStdRuleAccessCtrl_Type()
)
zxAnAclStdRuleAccessCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleAccessCtrl.setStatus("current")


class _ZxAnAclStdRuleSrcIpType_Type(InetAddressType):
    """Custom type zxAnAclStdRuleSrcIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnAclStdRuleSrcIpType_Type.__name__ = "InetAddressType"
_ZxAnAclStdRuleSrcIpType_Object = MibTableColumn
zxAnAclStdRuleSrcIpType = _ZxAnAclStdRuleSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 4),
    _ZxAnAclStdRuleSrcIpType_Type()
)
zxAnAclStdRuleSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleSrcIpType.setStatus("current")


class _ZxAnAclStdRuleSrcIp_Type(InetAddress):
    """Custom type zxAnAclStdRuleSrcIp based on InetAddress"""
    defaultHexValue = "00000000"


_ZxAnAclStdRuleSrcIp_Type.__name__ = "InetAddress"
_ZxAnAclStdRuleSrcIp_Object = MibTableColumn
zxAnAclStdRuleSrcIp = _ZxAnAclStdRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 5),
    _ZxAnAclStdRuleSrcIp_Type()
)
zxAnAclStdRuleSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleSrcIp.setStatus("current")


class _ZxAnAclStdRuleSrcIpMask_Type(InetAddress):
    """Custom type zxAnAclStdRuleSrcIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_ZxAnAclStdRuleSrcIpMask_Type.__name__ = "InetAddress"
_ZxAnAclStdRuleSrcIpMask_Object = MibTableColumn
zxAnAclStdRuleSrcIpMask = _ZxAnAclStdRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 6),
    _ZxAnAclStdRuleSrcIpMask_Type()
)
zxAnAclStdRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleSrcIpMask.setStatus("current")


class _ZxAnAclStdRuleTimeRangeName_Type(DisplayString):
    """Custom type zxAnAclStdRuleTimeRangeName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnAclStdRuleTimeRangeName_Type.__name__ = "DisplayString"
_ZxAnAclStdRuleTimeRangeName_Object = MibTableColumn
zxAnAclStdRuleTimeRangeName = _ZxAnAclStdRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 49),
    _ZxAnAclStdRuleTimeRangeName_Type()
)
zxAnAclStdRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleTimeRangeName.setStatus("current")
_ZxAnAclStdRuleRowStatus_Type = RowStatus
_ZxAnAclStdRuleRowStatus_Object = MibTableColumn
zxAnAclStdRuleRowStatus = _ZxAnAclStdRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 14, 1, 50),
    _ZxAnAclStdRuleRowStatus_Type()
)
zxAnAclStdRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclStdRuleRowStatus.setStatus("current")
_ZxAnAclExtendedRuleTable_Object = MibTable
zxAnAclExtendedRuleTable = _ZxAnAclExtendedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15)
)
if mibBuilder.loadTexts:
    zxAnAclExtendedRuleTable.setStatus("current")
_ZxAnAclExtendedRuleEntry_Object = MibTableRow
zxAnAclExtendedRuleEntry = _ZxAnAclExtendedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1)
)
zxAnAclExtendedRuleEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclExtAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclExtRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclExtendedRuleEntry.setStatus("current")


class _ZxAnAclExtAclNumber_Type(Integer32):
    """Custom type zxAnAclExtAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 199),
    )


_ZxAnAclExtAclNumber_Type.__name__ = "Integer32"
_ZxAnAclExtAclNumber_Object = MibTableColumn
zxAnAclExtAclNumber = _ZxAnAclExtAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 1),
    _ZxAnAclExtAclNumber_Type()
)
zxAnAclExtAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclExtAclNumber.setStatus("current")


class _ZxAnAclExtRuleId_Type(Integer32):
    """Custom type zxAnAclExtRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ZxAnAclExtRuleId_Type.__name__ = "Integer32"
_ZxAnAclExtRuleId_Object = MibTableColumn
zxAnAclExtRuleId = _ZxAnAclExtRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 2),
    _ZxAnAclExtRuleId_Type()
)
zxAnAclExtRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclExtRuleId.setStatus("current")


class _ZxAnAclExtRuleAccessCtrl_Type(Integer32):
    """Custom type zxAnAclExtRuleAccessCtrl based on Integer32"""
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


_ZxAnAclExtRuleAccessCtrl_Type.__name__ = "Integer32"
_ZxAnAclExtRuleAccessCtrl_Object = MibTableColumn
zxAnAclExtRuleAccessCtrl = _ZxAnAclExtRuleAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 3),
    _ZxAnAclExtRuleAccessCtrl_Type()
)
zxAnAclExtRuleAccessCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleAccessCtrl.setStatus("current")


class _ZxAnAclExtRuleSrcIpType_Type(InetAddressType):
    """Custom type zxAnAclExtRuleSrcIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnAclExtRuleSrcIpType_Type.__name__ = "InetAddressType"
_ZxAnAclExtRuleSrcIpType_Object = MibTableColumn
zxAnAclExtRuleSrcIpType = _ZxAnAclExtRuleSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 4),
    _ZxAnAclExtRuleSrcIpType_Type()
)
zxAnAclExtRuleSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleSrcIpType.setStatus("current")


class _ZxAnAclExtRuleSrcIp_Type(InetAddress):
    """Custom type zxAnAclExtRuleSrcIp based on InetAddress"""
    defaultHexValue = "00000000"


_ZxAnAclExtRuleSrcIp_Type.__name__ = "InetAddress"
_ZxAnAclExtRuleSrcIp_Object = MibTableColumn
zxAnAclExtRuleSrcIp = _ZxAnAclExtRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 5),
    _ZxAnAclExtRuleSrcIp_Type()
)
zxAnAclExtRuleSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleSrcIp.setStatus("current")


class _ZxAnAclExtRuleSrcIpMask_Type(InetAddress):
    """Custom type zxAnAclExtRuleSrcIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_ZxAnAclExtRuleSrcIpMask_Type.__name__ = "InetAddress"
_ZxAnAclExtRuleSrcIpMask_Object = MibTableColumn
zxAnAclExtRuleSrcIpMask = _ZxAnAclExtRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 6),
    _ZxAnAclExtRuleSrcIpMask_Type()
)
zxAnAclExtRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleSrcIpMask.setStatus("current")


class _ZxAnAclExtRuleDestIpType_Type(InetAddressType):
    """Custom type zxAnAclExtRuleDestIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnAclExtRuleDestIpType_Type.__name__ = "InetAddressType"
_ZxAnAclExtRuleDestIpType_Object = MibTableColumn
zxAnAclExtRuleDestIpType = _ZxAnAclExtRuleDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 7),
    _ZxAnAclExtRuleDestIpType_Type()
)
zxAnAclExtRuleDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleDestIpType.setStatus("current")


class _ZxAnAclExtRuleDestIp_Type(InetAddress):
    """Custom type zxAnAclExtRuleDestIp based on InetAddress"""
    defaultHexValue = "00000000"


_ZxAnAclExtRuleDestIp_Type.__name__ = "InetAddress"
_ZxAnAclExtRuleDestIp_Object = MibTableColumn
zxAnAclExtRuleDestIp = _ZxAnAclExtRuleDestIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 8),
    _ZxAnAclExtRuleDestIp_Type()
)
zxAnAclExtRuleDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleDestIp.setStatus("current")


class _ZxAnAclExtRuleDestIpMask_Type(InetAddress):
    """Custom type zxAnAclExtRuleDestIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_ZxAnAclExtRuleDestIpMask_Type.__name__ = "InetAddress"
_ZxAnAclExtRuleDestIpMask_Object = MibTableColumn
zxAnAclExtRuleDestIpMask = _ZxAnAclExtRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 9),
    _ZxAnAclExtRuleDestIpMask_Type()
)
zxAnAclExtRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleDestIpMask.setStatus("current")


class _ZxAnAclExtRuleIpProtocol_Type(Integer32):
    """Custom type zxAnAclExtRuleIpProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclExtRuleIpProtocol_Type.__name__ = "Integer32"
_ZxAnAclExtRuleIpProtocol_Object = MibTableColumn
zxAnAclExtRuleIpProtocol = _ZxAnAclExtRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 10),
    _ZxAnAclExtRuleIpProtocol_Type()
)
zxAnAclExtRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleIpProtocol.setStatus("current")


class _ZxAnAclExtRuleSrcPortOper_Type(ZxAnAclPortOperator):
    """Custom type zxAnAclExtRuleSrcPortOper based on ZxAnAclPortOperator"""
    defaultValue = 0


_ZxAnAclExtRuleSrcPortOper_Type.__name__ = "ZxAnAclPortOperator"
_ZxAnAclExtRuleSrcPortOper_Object = MibTableColumn
zxAnAclExtRuleSrcPortOper = _ZxAnAclExtRuleSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 11),
    _ZxAnAclExtRuleSrcPortOper_Type()
)
zxAnAclExtRuleSrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleSrcPortOper.setStatus("current")


class _ZxAnAclExtRuleStartSrcPort_Type(Integer32):
    """Custom type zxAnAclExtRuleStartSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclExtRuleStartSrcPort_Type.__name__ = "Integer32"
_ZxAnAclExtRuleStartSrcPort_Object = MibTableColumn
zxAnAclExtRuleStartSrcPort = _ZxAnAclExtRuleStartSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 12),
    _ZxAnAclExtRuleStartSrcPort_Type()
)
zxAnAclExtRuleStartSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleStartSrcPort.setStatus("current")


class _ZxAnAclExtRuleEndSrcPort_Type(Integer32):
    """Custom type zxAnAclExtRuleEndSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclExtRuleEndSrcPort_Type.__name__ = "Integer32"
_ZxAnAclExtRuleEndSrcPort_Object = MibTableColumn
zxAnAclExtRuleEndSrcPort = _ZxAnAclExtRuleEndSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 13),
    _ZxAnAclExtRuleEndSrcPort_Type()
)
zxAnAclExtRuleEndSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleEndSrcPort.setStatus("current")


class _ZxAnAclExtRuleDestPortOper_Type(ZxAnAclPortOperator):
    """Custom type zxAnAclExtRuleDestPortOper based on ZxAnAclPortOperator"""
    defaultValue = 0


_ZxAnAclExtRuleDestPortOper_Type.__name__ = "ZxAnAclPortOperator"
_ZxAnAclExtRuleDestPortOper_Object = MibTableColumn
zxAnAclExtRuleDestPortOper = _ZxAnAclExtRuleDestPortOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 14),
    _ZxAnAclExtRuleDestPortOper_Type()
)
zxAnAclExtRuleDestPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleDestPortOper.setStatus("current")


class _ZxAnAclExtRuleStartDestPort_Type(Integer32):
    """Custom type zxAnAclExtRuleStartDestPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclExtRuleStartDestPort_Type.__name__ = "Integer32"
_ZxAnAclExtRuleStartDestPort_Object = MibTableColumn
zxAnAclExtRuleStartDestPort = _ZxAnAclExtRuleStartDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 15),
    _ZxAnAclExtRuleStartDestPort_Type()
)
zxAnAclExtRuleStartDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleStartDestPort.setStatus("current")


class _ZxAnAclExtRuleEndDestPort_Type(Integer32):
    """Custom type zxAnAclExtRuleEndDestPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAclExtRuleEndDestPort_Type.__name__ = "Integer32"
_ZxAnAclExtRuleEndDestPort_Object = MibTableColumn
zxAnAclExtRuleEndDestPort = _ZxAnAclExtRuleEndDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 16),
    _ZxAnAclExtRuleEndDestPort_Type()
)
zxAnAclExtRuleEndDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleEndDestPort.setStatus("current")


class _ZxAnAclExtRuleTcpEstablished_Type(Integer32):
    """Custom type zxAnAclExtRuleTcpEstablished based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("establishedTcp", 1),
          ("notMatch", 2))
    )


_ZxAnAclExtRuleTcpEstablished_Type.__name__ = "Integer32"
_ZxAnAclExtRuleTcpEstablished_Object = MibTableColumn
zxAnAclExtRuleTcpEstablished = _ZxAnAclExtRuleTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 17),
    _ZxAnAclExtRuleTcpEstablished_Type()
)
zxAnAclExtRuleTcpEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleTcpEstablished.setStatus("current")


class _ZxAnAclExtRuleIcmpType_Type(Integer32):
    """Custom type zxAnAclExtRuleIcmpType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclExtRuleIcmpType_Type.__name__ = "Integer32"
_ZxAnAclExtRuleIcmpType_Object = MibTableColumn
zxAnAclExtRuleIcmpType = _ZxAnAclExtRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 18),
    _ZxAnAclExtRuleIcmpType_Type()
)
zxAnAclExtRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleIcmpType.setStatus("current")


class _ZxAnAclExtRuleIcmpCode_Type(Integer32):
    """Custom type zxAnAclExtRuleIcmpCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAclExtRuleIcmpCode_Type.__name__ = "Integer32"
_ZxAnAclExtRuleIcmpCode_Object = MibTableColumn
zxAnAclExtRuleIcmpCode = _ZxAnAclExtRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 19),
    _ZxAnAclExtRuleIcmpCode_Type()
)
zxAnAclExtRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleIcmpCode.setStatus("current")


class _ZxAnAclExtRulePrecedence_Type(Integer32):
    """Custom type zxAnAclExtRulePrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclExtRulePrecedence_Type.__name__ = "Integer32"
_ZxAnAclExtRulePrecedence_Object = MibTableColumn
zxAnAclExtRulePrecedence = _ZxAnAclExtRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 20),
    _ZxAnAclExtRulePrecedence_Type()
)
zxAnAclExtRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRulePrecedence.setStatus("current")


class _ZxAnAclExtRuleTos_Type(Integer32):
    """Custom type zxAnAclExtRuleTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclExtRuleTos_Type.__name__ = "Integer32"
_ZxAnAclExtRuleTos_Object = MibTableColumn
zxAnAclExtRuleTos = _ZxAnAclExtRuleTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 21),
    _ZxAnAclExtRuleTos_Type()
)
zxAnAclExtRuleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleTos.setStatus("current")


class _ZxAnAclExtRuleDscp_Type(Integer32):
    """Custom type zxAnAclExtRuleDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclExtRuleDscp_Type.__name__ = "Integer32"
_ZxAnAclExtRuleDscp_Object = MibTableColumn
zxAnAclExtRuleDscp = _ZxAnAclExtRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 22),
    _ZxAnAclExtRuleDscp_Type()
)
zxAnAclExtRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleDscp.setStatus("current")


class _ZxAnAclExtRuleTtl_Type(Integer32):
    """Custom type zxAnAclExtRuleTtl based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnAclExtRuleTtl_Type.__name__ = "Integer32"
_ZxAnAclExtRuleTtl_Object = MibTableColumn
zxAnAclExtRuleTtl = _ZxAnAclExtRuleTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 23),
    _ZxAnAclExtRuleTtl_Type()
)
zxAnAclExtRuleTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleTtl.setStatus("current")


class _ZxAnAclExtRuleTimeRangeName_Type(DisplayString):
    """Custom type zxAnAclExtRuleTimeRangeName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnAclExtRuleTimeRangeName_Type.__name__ = "DisplayString"
_ZxAnAclExtRuleTimeRangeName_Object = MibTableColumn
zxAnAclExtRuleTimeRangeName = _ZxAnAclExtRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 49),
    _ZxAnAclExtRuleTimeRangeName_Type()
)
zxAnAclExtRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleTimeRangeName.setStatus("current")
_ZxAnAclExtRuleRowStatus_Type = RowStatus
_ZxAnAclExtRuleRowStatus_Object = MibTableColumn
zxAnAclExtRuleRowStatus = _ZxAnAclExtRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 15, 1, 50),
    _ZxAnAclExtRuleRowStatus_Type()
)
zxAnAclExtRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclExtRuleRowStatus.setStatus("current")
_ZxAnAclLinkRuleTable_Object = MibTable
zxAnAclLinkRuleTable = _ZxAnAclLinkRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16)
)
if mibBuilder.loadTexts:
    zxAnAclLinkRuleTable.setStatus("current")
_ZxAnAclLinkRuleEntry_Object = MibTableRow
zxAnAclLinkRuleEntry = _ZxAnAclLinkRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1)
)
zxAnAclLinkRuleEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclLinkAclNumber"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclLinkRuleId"),
)
if mibBuilder.loadTexts:
    zxAnAclLinkRuleEntry.setStatus("current")


class _ZxAnAclLinkAclNumber_Type(Integer32):
    """Custom type zxAnAclLinkAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 299),
    )


_ZxAnAclLinkAclNumber_Type.__name__ = "Integer32"
_ZxAnAclLinkAclNumber_Object = MibTableColumn
zxAnAclLinkAclNumber = _ZxAnAclLinkAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 1),
    _ZxAnAclLinkAclNumber_Type()
)
zxAnAclLinkAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclLinkAclNumber.setStatus("current")


class _ZxAnAclLinkRuleId_Type(Integer32):
    """Custom type zxAnAclLinkRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnAclLinkRuleId_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleId_Object = MibTableColumn
zxAnAclLinkRuleId = _ZxAnAclLinkRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 2),
    _ZxAnAclLinkRuleId_Type()
)
zxAnAclLinkRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleId.setStatus("current")


class _ZxAnAclLinkRuleAccessCtrl_Type(Integer32):
    """Custom type zxAnAclLinkRuleAccessCtrl based on Integer32"""
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


_ZxAnAclLinkRuleAccessCtrl_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleAccessCtrl_Object = MibTableColumn
zxAnAclLinkRuleAccessCtrl = _ZxAnAclLinkRuleAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 3),
    _ZxAnAclLinkRuleAccessCtrl_Type()
)
zxAnAclLinkRuleAccessCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleAccessCtrl.setStatus("current")


class _ZxAnAclLinkRuleEthProtocol_Type(Integer32):
    """Custom type zxAnAclLinkRuleEthProtocol based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1537, 65535),
    )


_ZxAnAclLinkRuleEthProtocol_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleEthProtocol_Object = MibTableColumn
zxAnAclLinkRuleEthProtocol = _ZxAnAclLinkRuleEthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 4),
    _ZxAnAclLinkRuleEthProtocol_Type()
)
zxAnAclLinkRuleEthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleEthProtocol.setStatus("current")


class _ZxAnAclLinkRuleStagCos_Type(Integer32):
    """Custom type zxAnAclLinkRuleStagCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclLinkRuleStagCos_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleStagCos_Object = MibTableColumn
zxAnAclLinkRuleStagCos = _ZxAnAclLinkRuleStagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 5),
    _ZxAnAclLinkRuleStagCos_Type()
)
zxAnAclLinkRuleStagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleStagCos.setStatus("current")


class _ZxAnAclLinkRuleSVid_Type(Integer32):
    """Custom type zxAnAclLinkRuleSVid based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnAclLinkRuleSVid_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleSVid_Object = MibTableColumn
zxAnAclLinkRuleSVid = _ZxAnAclLinkRuleSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 6),
    _ZxAnAclLinkRuleSVid_Type()
)
zxAnAclLinkRuleSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleSVid.setStatus("current")


class _ZxAnAclLinkRuleCtagCos_Type(Integer32):
    """Custom type zxAnAclLinkRuleCtagCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnAclLinkRuleCtagCos_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleCtagCos_Object = MibTableColumn
zxAnAclLinkRuleCtagCos = _ZxAnAclLinkRuleCtagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 7),
    _ZxAnAclLinkRuleCtagCos_Type()
)
zxAnAclLinkRuleCtagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleCtagCos.setStatus("current")


class _ZxAnAclLinkRuleCVid_Type(Integer32):
    """Custom type zxAnAclLinkRuleCVid based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_ZxAnAclLinkRuleCVid_Type.__name__ = "Integer32"
_ZxAnAclLinkRuleCVid_Object = MibTableColumn
zxAnAclLinkRuleCVid = _ZxAnAclLinkRuleCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 8),
    _ZxAnAclLinkRuleCVid_Type()
)
zxAnAclLinkRuleCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleCVid.setStatus("current")


class _ZxAnAclLinkRuleSrcMac_Type(MacAddress):
    """Custom type zxAnAclLinkRuleSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_ZxAnAclLinkRuleSrcMac_Type.__name__ = "MacAddress"
_ZxAnAclLinkRuleSrcMac_Object = MibTableColumn
zxAnAclLinkRuleSrcMac = _ZxAnAclLinkRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 9),
    _ZxAnAclLinkRuleSrcMac_Type()
)
zxAnAclLinkRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleSrcMac.setStatus("current")


class _ZxAnAclLinkRuleSrcMacMask_Type(MacAddress):
    """Custom type zxAnAclLinkRuleSrcMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_ZxAnAclLinkRuleSrcMacMask_Type.__name__ = "MacAddress"
_ZxAnAclLinkRuleSrcMacMask_Object = MibTableColumn
zxAnAclLinkRuleSrcMacMask = _ZxAnAclLinkRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 10),
    _ZxAnAclLinkRuleSrcMacMask_Type()
)
zxAnAclLinkRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleSrcMacMask.setStatus("current")


class _ZxAnAclLinkRuleDestMac_Type(MacAddress):
    """Custom type zxAnAclLinkRuleDestMac based on MacAddress"""
    defaultHexValue = "000000000000"


_ZxAnAclLinkRuleDestMac_Type.__name__ = "MacAddress"
_ZxAnAclLinkRuleDestMac_Object = MibTableColumn
zxAnAclLinkRuleDestMac = _ZxAnAclLinkRuleDestMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 11),
    _ZxAnAclLinkRuleDestMac_Type()
)
zxAnAclLinkRuleDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleDestMac.setStatus("current")


class _ZxAnAclLinkRuleDestMacMask_Type(MacAddress):
    """Custom type zxAnAclLinkRuleDestMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_ZxAnAclLinkRuleDestMacMask_Type.__name__ = "MacAddress"
_ZxAnAclLinkRuleDestMacMask_Object = MibTableColumn
zxAnAclLinkRuleDestMacMask = _ZxAnAclLinkRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 12),
    _ZxAnAclLinkRuleDestMacMask_Type()
)
zxAnAclLinkRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleDestMacMask.setStatus("current")


class _ZxAnAclLinkRuleTimeRangeName_Type(DisplayString):
    """Custom type zxAnAclLinkRuleTimeRangeName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnAclLinkRuleTimeRangeName_Type.__name__ = "DisplayString"
_ZxAnAclLinkRuleTimeRangeName_Object = MibTableColumn
zxAnAclLinkRuleTimeRangeName = _ZxAnAclLinkRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 49),
    _ZxAnAclLinkRuleTimeRangeName_Type()
)
zxAnAclLinkRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleTimeRangeName.setStatus("current")
_ZxAnAclLinkRuleRowStatus_Type = RowStatus
_ZxAnAclLinkRuleRowStatus_Object = MibTableColumn
zxAnAclLinkRuleRowStatus = _ZxAnAclLinkRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 16, 1, 50),
    _ZxAnAclLinkRuleRowStatus_Type()
)
zxAnAclLinkRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclLinkRuleRowStatus.setStatus("current")
_ZxAnAclVlanConfTable_Object = MibTable
zxAnAclVlanConfTable = _ZxAnAclVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17)
)
if mibBuilder.loadTexts:
    zxAnAclVlanConfTable.setStatus("current")
_ZxAnAclVlanConfEntry_Object = MibTableRow
zxAnAclVlanConfEntry = _ZxAnAclVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1)
)
zxAnAclVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclVlanConfVid"),
    (0, "ZTE-AN-QOSPCL-MIB", "zxAnAclVlanConfDirection"),
)
if mibBuilder.loadTexts:
    zxAnAclVlanConfEntry.setStatus("current")


class _ZxAnAclVlanConfVid_Type(Integer32):
    """Custom type zxAnAclVlanConfVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnAclVlanConfVid_Type.__name__ = "Integer32"
_ZxAnAclVlanConfVid_Object = MibTableColumn
zxAnAclVlanConfVid = _ZxAnAclVlanConfVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1, 1),
    _ZxAnAclVlanConfVid_Type()
)
zxAnAclVlanConfVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclVlanConfVid.setStatus("current")


class _ZxAnAclVlanConfDirection_Type(Integer32):
    """Custom type zxAnAclVlanConfDirection based on Integer32"""
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


_ZxAnAclVlanConfDirection_Type.__name__ = "Integer32"
_ZxAnAclVlanConfDirection_Object = MibTableColumn
zxAnAclVlanConfDirection = _ZxAnAclVlanConfDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1, 2),
    _ZxAnAclVlanConfDirection_Type()
)
zxAnAclVlanConfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAclVlanConfDirection.setStatus("current")


class _ZxAnAclVlanConfAclNumber_Type(Integer32):
    """Custom type zxAnAclVlanConfAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_ZxAnAclVlanConfAclNumber_Type.__name__ = "Integer32"
_ZxAnAclVlanConfAclNumber_Object = MibTableColumn
zxAnAclVlanConfAclNumber = _ZxAnAclVlanConfAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1, 3),
    _ZxAnAclVlanConfAclNumber_Type()
)
zxAnAclVlanConfAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclVlanConfAclNumber.setStatus("current")


class _ZxAnAclVlanConfAclName_Type(DisplayString):
    """Custom type zxAnAclVlanConfAclName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAclVlanConfAclName_Type.__name__ = "DisplayString"
_ZxAnAclVlanConfAclName_Object = MibTableColumn
zxAnAclVlanConfAclName = _ZxAnAclVlanConfAclName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1, 4),
    _ZxAnAclVlanConfAclName_Type()
)
zxAnAclVlanConfAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclVlanConfAclName.setStatus("current")
_ZxAnAclVlanConfRowStatus_Type = RowStatus
_ZxAnAclVlanConfRowStatus_Object = MibTableColumn
zxAnAclVlanConfRowStatus = _ZxAnAclVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 1, 17, 1, 50),
    _ZxAnAclVlanConfRowStatus_Type()
)
zxAnAclVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAclVlanConfRowStatus.setStatus("current")
_ZxAnQosPclTrapObjects_ObjectIdentity = ObjectIdentity
zxAnQosPclTrapObjects = _ZxAnQosPclTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-QOSPCL-MIB",
    **{"ZxAnAclPortOperator": ZxAnAclPortOperator,
       "zxAnQosPclMib": zxAnQosPclMib,
       "zxAnQosPclObjects": zxAnQosPclObjects,
       "zxAnQosPclGlobalObjects": zxAnQosPclGlobalObjects,
       "zxAnQosPclCapability": zxAnQosPclCapability,
       "zxAnAclTable": zxAnAclTable,
       "zxAnAclEntry": zxAnAclEntry,
       "zxAnAclNumber": zxAnAclNumber,
       "zxAnAclName": zxAnAclName,
       "zxAnAclRowStatus": zxAnAclRowStatus,
       "zxAnAclHybridRuleTable": zxAnAclHybridRuleTable,
       "zxAnAclHybridRuleEntry": zxAnAclHybridRuleEntry,
       "zxAnAclHybridRuleId": zxAnAclHybridRuleId,
       "zxAnAclHybridRuleAccessCtrl": zxAnAclHybridRuleAccessCtrl,
       "zxAnAclHybridRuleSrcIpType": zxAnAclHybridRuleSrcIpType,
       "zxAnAclHybridRuleSrcIp": zxAnAclHybridRuleSrcIp,
       "zxAnAclHybridRuleSrcIpMask": zxAnAclHybridRuleSrcIpMask,
       "zxAnAclHybridRuleDestIpType": zxAnAclHybridRuleDestIpType,
       "zxAnAclHybridRuleDestIp": zxAnAclHybridRuleDestIp,
       "zxAnAclHybridRuleDestIpMask": zxAnAclHybridRuleDestIpMask,
       "zxAnAclHybridRuleIpProto": zxAnAclHybridRuleIpProto,
       "zxAnAclHybridRuleEthProto": zxAnAclHybridRuleEthProto,
       "zxAnAclHybridRuleSrcPortOper": zxAnAclHybridRuleSrcPortOper,
       "zxAnAclHybridRuleStartSrcPort": zxAnAclHybridRuleStartSrcPort,
       "zxAnAclHybridRuleEndSrcPort": zxAnAclHybridRuleEndSrcPort,
       "zxAnAclHybridRuleDestPortOper": zxAnAclHybridRuleDestPortOper,
       "zxAnAclHybridRuleStartDestPort": zxAnAclHybridRuleStartDestPort,
       "zxAnAclHybridRuleEndDestPort": zxAnAclHybridRuleEndDestPort,
       "zxAnAclHybridRulePrecedence": zxAnAclHybridRulePrecedence,
       "zxAnAclHybridRuleTos": zxAnAclHybridRuleTos,
       "zxAnAclHybridRuleDscp": zxAnAclHybridRuleDscp,
       "zxAnAclHybridRuleStagCos": zxAnAclHybridRuleStagCos,
       "zxAnAclHybridRuleSVid": zxAnAclHybridRuleSVid,
       "zxAnAclHybridRuleCtagCos": zxAnAclHybridRuleCtagCos,
       "zxAnAclHybridRuleCVid": zxAnAclHybridRuleCVid,
       "zxAnAclHybridRuleSrcMac": zxAnAclHybridRuleSrcMac,
       "zxAnAclHybridRuleSrcMacMask": zxAnAclHybridRuleSrcMacMask,
       "zxAnAclHybridRuleDestMac": zxAnAclHybridRuleDestMac,
       "zxAnAclHybridRuleDestMacMask": zxAnAclHybridRuleDestMacMask,
       "zxAnQosPclRuleTimeRangeName": zxAnQosPclRuleTimeRangeName,
       "zxAnQosPclRuleSrcAddrPfxLen": zxAnQosPclRuleSrcAddrPfxLen,
       "zxAnQosPclRuleDestAddrPfxLen": zxAnQosPclRuleDestAddrPfxLen,
       "zxAnQosPclRuleTrafficClass": zxAnQosPclRuleTrafficClass,
       "zxAnQosPclRuleFlowLabel": zxAnQosPclRuleFlowLabel,
       "zxAnAclHybridRuleIcmpType": zxAnAclHybridRuleIcmpType,
       "zxAnAclHybridRuleIcmpCode": zxAnAclHybridRuleIcmpCode,
       "zxAnAclHybridRuleRowStatus": zxAnAclHybridRuleRowStatus,
       "zxAnQosAclTrafficLimitTable": zxAnQosAclTrafficLimitTable,
       "zxAnQosAclTrafficLimitEntry": zxAnQosAclTrafficLimitEntry,
       "zxAnQosAclTrafficLimitCir": zxAnQosAclTrafficLimitCir,
       "zxAnQosAclTrafficLimitPir": zxAnQosAclTrafficLimitPir,
       "zxAnQosAclTrafficLimitCbs": zxAnQosAclTrafficLimitCbs,
       "zxAnQosAclTrafficLimitEbs": zxAnQosAclTrafficLimitEbs,
       "zxAnQosAclTrafficLimitPbs": zxAnQosAclTrafficLimitPbs,
       "zxAnQosAclTrafficLimitMode": zxAnQosAclTrafficLimitMode,
       "zxAnQosAclTrafficDropYellow": zxAnQosAclTrafficDropYellow,
       "zxAnQosAclTrafficForwardRed": zxAnQosAclTrafficForwardRed,
       "zxAnQosAclTrafficRemarkRedDp": zxAnQosAclTrafficRemarkRedDp,
       "zxAnQosAclTrafficRemarkRedDscp": zxAnQosAclTrafficRemarkRedDscp,
       "zxAnQosAclTrafficRemarkYellDp": zxAnQosAclTrafficRemarkYellDp,
       "zxAnQosAclTrafficRemarkYellDscp": zxAnQosAclTrafficRemarkYellDscp,
       "zxAnQosAclTrafficRowStatus": zxAnQosAclTrafficRowStatus,
       "zxAnQosAclPriorityMarkTable": zxAnQosAclPriorityMarkTable,
       "zxAnQosAclPriorityMarkEntry": zxAnQosAclPriorityMarkEntry,
       "zxAnQosAclPriMarkDscp": zxAnQosAclPriMarkDscp,
       "zxAnQosAclPriMarkCos": zxAnQosAclPriMarkCos,
       "zxAnQosAclPriMarkPrecedence": zxAnQosAclPriMarkPrecedence,
       "zxAnQosAclPriMarkLocalPrecedence": zxAnQosAclPriMarkLocalPrecedence,
       "zxAnQosAclPriMarkDropPrecedence": zxAnQosAclPriMarkDropPrecedence,
       "zxAnQosPclPriMarkTrafficClass": zxAnQosPclPriMarkTrafficClass,
       "zxAnQosAclPriMarkRowStatus": zxAnQosAclPriMarkRowStatus,
       "zxAnQosAclVlanMarkTable": zxAnQosAclVlanMarkTable,
       "zxAnQosAclVlanMarkEntry": zxAnQosAclVlanMarkEntry,
       "zxAnQosAclVlanMarkVid": zxAnQosAclVlanMarkVid,
       "zxAnQosAclVlanMarkRowStatus": zxAnQosAclVlanMarkRowStatus,
       "zxAnQosPclQinqTable": zxAnQosPclQinqTable,
       "zxAnQosPclQinqEntry": zxAnQosPclQinqEntry,
       "zxAnQosPclQinqSvlan": zxAnQosPclQinqSvlan,
       "zxAnQosPclQinqCvlan": zxAnQosPclQinqCvlan,
       "zxAnQosPclQinqRowStatus": zxAnQosPclQinqRowStatus,
       "zxAnQosAclRedirectTable": zxAnQosAclRedirectTable,
       "zxAnQosAclRedirectEntry": zxAnQosAclRedirectEntry,
       "zxAnQosAclRedirectIf": zxAnQosAclRedirectIf,
       "zxAnQosAclRedirectType": zxAnQosAclRedirectType,
       "zxAnQosAclRedirectNextHopIpType": zxAnQosAclRedirectNextHopIpType,
       "zxAnQosAclRedirectNextHopIp": zxAnQosAclRedirectNextHopIp,
       "zxAnQosAclRedirectRowStatus": zxAnQosAclRedirectRowStatus,
       "zxAnQosAclTrafficMirrorTable": zxAnQosAclTrafficMirrorTable,
       "zxAnQosAclTrafficMirrorEntry": zxAnQosAclTrafficMirrorEntry,
       "zxAnQosAclTrafficMirrorIf": zxAnQosAclTrafficMirrorIf,
       "zxAnQosAclTrafficMirrorType": zxAnQosAclTrafficMirrorType,
       "zxAnQosAclTrafficMirrorVlanId": zxAnQosAclTrafficMirrorVlanId,
       "zxAnQosAclTrafficMirrorCos": zxAnQosAclTrafficMirrorCos,
       "zxAnQosAclTrafficMirrorTpid": zxAnQosAclTrafficMirrorTpid,
       "zxAnQosAclTrafficMirrorDstIpType": zxAnQosAclTrafficMirrorDstIpType,
       "zxAnQosAclTrafficMirrorDstIpAddr": zxAnQosAclTrafficMirrorDstIpAddr,
       "zxAnQosAclTrafficMirrorSrcIpType": zxAnQosAclTrafficMirrorSrcIpType,
       "zxAnQosAclTrafficMirrorSrcIpAddr": zxAnQosAclTrafficMirrorSrcIpAddr,
       "zxAnQosAclTrafficMirrorTtl": zxAnQosAclTrafficMirrorTtl,
       "zxAnQosAclTrafficMirrorDscp": zxAnQosAclTrafficMirrorDscp,
       "zxAnQosAclTrafficMirrorRowStatus": zxAnQosAclTrafficMirrorRowStatus,
       "zxAnQosAclTrafficStatsTable": zxAnQosAclTrafficStatsTable,
       "zxAnQosAclTrafficStatsEntry": zxAnQosAclTrafficStatsEntry,
       "zxAnQosAclTrafficStatsPktColor": zxAnQosAclTrafficStatsPktColor,
       "zxAnQosAclTrafficStatsType": zxAnQosAclTrafficStatsType,
       "zxAnQosAclTrafficStatsPkts": zxAnQosAclTrafficStatsPkts,
       "zxAnQosAclTrafficStatsOctets": zxAnQosAclTrafficStatsOctets,
       "zxAnQosAclTrafficStatsReset": zxAnQosAclTrafficStatsReset,
       "zxAnQosAclTrafficStatsRowStatus": zxAnQosAclTrafficStatsRowStatus,
       "zxAnQosPclTimeRangeTable": zxAnQosPclTimeRangeTable,
       "zxAnQosPclTimeRangeEntry": zxAnQosPclTimeRangeEntry,
       "zxAnQosPclTimeRangeName": zxAnQosPclTimeRangeName,
       "zxAnQosPclTimeRangeType": zxAnQosPclTimeRangeType,
       "zxAnQosPclOnceStartTime": zxAnQosPclOnceStartTime,
       "zxAnQosPclOnceEndTime": zxAnQosPclOnceEndTime,
       "zxAnQosPclWeeklyDay": zxAnQosPclWeeklyDay,
       "zxAnQosPclWeeklyStartTime": zxAnQosPclWeeklyStartTime,
       "zxAnQosPclWeeklyEndTime": zxAnQosPclWeeklyEndTime,
       "zxAnQosPclTimeRangeRowStatus": zxAnQosPclTimeRangeRowStatus,
       "zxAnAclIfConfTable": zxAnAclIfConfTable,
       "zxAnAclIfConfEntry": zxAnAclIfConfEntry,
       "zxAnQosPclBindRack": zxAnQosPclBindRack,
       "zxAnQosPclBindShelf": zxAnQosPclBindShelf,
       "zxAnQosPclBindSlot": zxAnQosPclBindSlot,
       "zxAnQosPclBindPort": zxAnQosPclBindPort,
       "zxAnQosPclBindOnu": zxAnQosPclBindOnu,
       "zxAnQosPclBindVCircuitType": zxAnQosPclBindVCircuitType,
       "zxAnQosPclBindVCircuit": zxAnQosPclBindVCircuit,
       "zxAnQosPclBindDirection": zxAnQosPclBindDirection,
       "zxAnAclIfConfAclNumber": zxAnAclIfConfAclNumber,
       "zxAnAclIfConfAclName": zxAnAclIfConfAclName,
       "zxAnAclIfConfRowStatus": zxAnAclIfConfRowStatus,
       "zxAnQosPclGlobalBindingTable": zxAnQosPclGlobalBindingTable,
       "zxAnQosPclGlobalBindingEntry": zxAnQosPclGlobalBindingEntry,
       "zxAnQosPclGlobalBindingType": zxAnQosPclGlobalBindingType,
       "zxAnQosPclGlobalBindingIndex": zxAnQosPclGlobalBindingIndex,
       "zxAnAclStandardRuleTable": zxAnAclStandardRuleTable,
       "zxAnAclStandardRuleEntry": zxAnAclStandardRuleEntry,
       "zxAnAclStdAclNumber": zxAnAclStdAclNumber,
       "zxAnAclStdRuleId": zxAnAclStdRuleId,
       "zxAnAclStdRuleAccessCtrl": zxAnAclStdRuleAccessCtrl,
       "zxAnAclStdRuleSrcIpType": zxAnAclStdRuleSrcIpType,
       "zxAnAclStdRuleSrcIp": zxAnAclStdRuleSrcIp,
       "zxAnAclStdRuleSrcIpMask": zxAnAclStdRuleSrcIpMask,
       "zxAnAclStdRuleTimeRangeName": zxAnAclStdRuleTimeRangeName,
       "zxAnAclStdRuleRowStatus": zxAnAclStdRuleRowStatus,
       "zxAnAclExtendedRuleTable": zxAnAclExtendedRuleTable,
       "zxAnAclExtendedRuleEntry": zxAnAclExtendedRuleEntry,
       "zxAnAclExtAclNumber": zxAnAclExtAclNumber,
       "zxAnAclExtRuleId": zxAnAclExtRuleId,
       "zxAnAclExtRuleAccessCtrl": zxAnAclExtRuleAccessCtrl,
       "zxAnAclExtRuleSrcIpType": zxAnAclExtRuleSrcIpType,
       "zxAnAclExtRuleSrcIp": zxAnAclExtRuleSrcIp,
       "zxAnAclExtRuleSrcIpMask": zxAnAclExtRuleSrcIpMask,
       "zxAnAclExtRuleDestIpType": zxAnAclExtRuleDestIpType,
       "zxAnAclExtRuleDestIp": zxAnAclExtRuleDestIp,
       "zxAnAclExtRuleDestIpMask": zxAnAclExtRuleDestIpMask,
       "zxAnAclExtRuleIpProtocol": zxAnAclExtRuleIpProtocol,
       "zxAnAclExtRuleSrcPortOper": zxAnAclExtRuleSrcPortOper,
       "zxAnAclExtRuleStartSrcPort": zxAnAclExtRuleStartSrcPort,
       "zxAnAclExtRuleEndSrcPort": zxAnAclExtRuleEndSrcPort,
       "zxAnAclExtRuleDestPortOper": zxAnAclExtRuleDestPortOper,
       "zxAnAclExtRuleStartDestPort": zxAnAclExtRuleStartDestPort,
       "zxAnAclExtRuleEndDestPort": zxAnAclExtRuleEndDestPort,
       "zxAnAclExtRuleTcpEstablished": zxAnAclExtRuleTcpEstablished,
       "zxAnAclExtRuleIcmpType": zxAnAclExtRuleIcmpType,
       "zxAnAclExtRuleIcmpCode": zxAnAclExtRuleIcmpCode,
       "zxAnAclExtRulePrecedence": zxAnAclExtRulePrecedence,
       "zxAnAclExtRuleTos": zxAnAclExtRuleTos,
       "zxAnAclExtRuleDscp": zxAnAclExtRuleDscp,
       "zxAnAclExtRuleTtl": zxAnAclExtRuleTtl,
       "zxAnAclExtRuleTimeRangeName": zxAnAclExtRuleTimeRangeName,
       "zxAnAclExtRuleRowStatus": zxAnAclExtRuleRowStatus,
       "zxAnAclLinkRuleTable": zxAnAclLinkRuleTable,
       "zxAnAclLinkRuleEntry": zxAnAclLinkRuleEntry,
       "zxAnAclLinkAclNumber": zxAnAclLinkAclNumber,
       "zxAnAclLinkRuleId": zxAnAclLinkRuleId,
       "zxAnAclLinkRuleAccessCtrl": zxAnAclLinkRuleAccessCtrl,
       "zxAnAclLinkRuleEthProtocol": zxAnAclLinkRuleEthProtocol,
       "zxAnAclLinkRuleStagCos": zxAnAclLinkRuleStagCos,
       "zxAnAclLinkRuleSVid": zxAnAclLinkRuleSVid,
       "zxAnAclLinkRuleCtagCos": zxAnAclLinkRuleCtagCos,
       "zxAnAclLinkRuleCVid": zxAnAclLinkRuleCVid,
       "zxAnAclLinkRuleSrcMac": zxAnAclLinkRuleSrcMac,
       "zxAnAclLinkRuleSrcMacMask": zxAnAclLinkRuleSrcMacMask,
       "zxAnAclLinkRuleDestMac": zxAnAclLinkRuleDestMac,
       "zxAnAclLinkRuleDestMacMask": zxAnAclLinkRuleDestMacMask,
       "zxAnAclLinkRuleTimeRangeName": zxAnAclLinkRuleTimeRangeName,
       "zxAnAclLinkRuleRowStatus": zxAnAclLinkRuleRowStatus,
       "zxAnAclVlanConfTable": zxAnAclVlanConfTable,
       "zxAnAclVlanConfEntry": zxAnAclVlanConfEntry,
       "zxAnAclVlanConfVid": zxAnAclVlanConfVid,
       "zxAnAclVlanConfDirection": zxAnAclVlanConfDirection,
       "zxAnAclVlanConfAclNumber": zxAnAclVlanConfAclNumber,
       "zxAnAclVlanConfAclName": zxAnAclVlanConfAclName,
       "zxAnAclVlanConfRowStatus": zxAnAclVlanConfRowStatus,
       "zxAnQosPclTrapObjects": zxAnQosPclTrapObjects}
)
