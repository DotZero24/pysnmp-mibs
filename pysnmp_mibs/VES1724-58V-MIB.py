# SNMP MIB module (VES1724-58V-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/VES1724-58V-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:38 2025
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
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(xdsl2LConfProfProfileName,
 xdsl2LineAlarmConfProfileName,
 xdsl2LineBand,
 xdsl2SCStatusBand,
 xdsl2SCStatusDirection) = mibBuilder.importSymbols(
    "VDSL2-LINE-MIB",
    "xdsl2LConfProfProfileName",
    "xdsl2LineAlarmConfProfileName",
    "xdsl2LineBand",
    "xdsl2SCStatusBand",
    "xdsl2SCStatusDirection")


# MODULE-IDENTITY

ves1724_58v = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Xdsl2Unit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xtuc", 1),
          ("xtur", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_VesSeries_ObjectIdentity = ObjectIdentity
vesSeries = _VesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12)
)
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1)
)
_AclMaxNumOfAclPerSystem_Type = Integer32
_AclMaxNumOfAclPerSystem_Object = MibScalar
aclMaxNumOfAclPerSystem = _AclMaxNumOfAclPerSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 1),
    _AclMaxNumOfAclPerSystem_Type()
)
aclMaxNumOfAclPerSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMaxNumOfAclPerSystem.setStatus("current")
_AclSystemTable_Object = MibTable
aclSystemTable = _AclSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 2)
)
if mibBuilder.loadTexts:
    aclSystemTable.setStatus("current")
_AclSystemEntry_Object = MibTableRow
aclSystemEntry = _AclSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 2, 1)
)
aclSystemEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "aclSystemProfileName"),
)
if mibBuilder.loadTexts:
    aclSystemEntry.setStatus("current")


class _AclSystemProfileName_Type(DisplayString):
    """Custom type aclSystemProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclSystemProfileName_Type.__name__ = "DisplayString"
_AclSystemProfileName_Object = MibTableColumn
aclSystemProfileName = _AclSystemProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 2, 1, 1),
    _AclSystemProfileName_Type()
)
aclSystemProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSystemProfileName.setStatus("current")
_AclSystemRowStaus_Type = RowStatus
_AclSystemRowStaus_Object = MibTableColumn
aclSystemRowStaus = _AclSystemRowStaus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 2, 1, 2),
    _AclSystemRowStaus_Type()
)
aclSystemRowStaus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclSystemRowStaus.setStatus("current")
_AclMaxNumOfAclPerPort_Type = Integer32
_AclMaxNumOfAclPerPort_Object = MibScalar
aclMaxNumOfAclPerPort = _AclMaxNumOfAclPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 3),
    _AclMaxNumOfAclPerPort_Type()
)
aclMaxNumOfAclPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMaxNumOfAclPerPort.setStatus("current")
_AclPortTable_Object = MibTable
aclPortTable = _AclPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 4)
)
if mibBuilder.loadTexts:
    aclPortTable.setStatus("current")
_AclPortEntry_Object = MibTableRow
aclPortEntry = _AclPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 4, 1)
)
aclPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "VES1724-58V-MIB", "aclPortProfileName"),
)
if mibBuilder.loadTexts:
    aclPortEntry.setStatus("current")


class _AclPortProfileName_Type(DisplayString):
    """Custom type aclPortProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclPortProfileName_Type.__name__ = "DisplayString"
_AclPortProfileName_Object = MibTableColumn
aclPortProfileName = _AclPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 4, 1, 1),
    _AclPortProfileName_Type()
)
aclPortProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortProfileName.setStatus("current")
_AclPortRowStatus_Type = RowStatus
_AclPortRowStatus_Object = MibTableColumn
aclPortRowStatus = _AclPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 4, 1, 2),
    _AclPortRowStatus_Type()
)
aclPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPortRowStatus.setStatus("current")
_AclMaxNumOfAclProfiles_Type = Integer32
_AclMaxNumOfAclProfiles_Object = MibScalar
aclMaxNumOfAclProfiles = _AclMaxNumOfAclProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 5),
    _AclMaxNumOfAclProfiles_Type()
)
aclMaxNumOfAclProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMaxNumOfAclProfiles.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1)
)
aclProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "aclProfileName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")


class _AclProfileName_Type(DisplayString):
    """Custom type aclProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclProfileName_Type.__name__ = "DisplayString"
_AclProfileName_Object = MibTableColumn
aclProfileName = _AclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 1),
    _AclProfileName_Type()
)
aclProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileName.setStatus("current")


class _AclProfileActionMask_Type(Bits):
    """Custom type aclProfileActionMask based on Bits"""
    namedValues = NamedValues(
        *(("drop", 0),
          ("rateLimit", 1),
          ("changeInnerPbit", 2),
          ("changeOuterPbit", 3),
          ("changeDscp", 4),
          ("changeTrafficClass", 5),
          ("changeQos", 6))
    )

_AclProfileActionMask_Type.__name__ = "Bits"
_AclProfileActionMask_Object = MibTableColumn
aclProfileActionMask = _AclProfileActionMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 2),
    _AclProfileActionMask_Type()
)
aclProfileActionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionMask.setStatus("current")


class _AclProfileFieldMask_Type(Bits):
    """Custom type aclProfileFieldMask based on Bits"""
    namedValues = NamedValues(
        *(("etherType", 0),
          ("sourceMac", 1),
          ("destMac", 2),
          ("sourceOui", 3),
          ("destOui", 4),
          ("innerVlan", 5),
          ("outerVlan", 6),
          ("innerPbit", 7),
          ("outerPbit", 8),
          ("sourceIpRange", 9),
          ("destIpRange", 10),
          ("sourceIp", 11),
          ("destIp", 12),
          ("protocol", 13),
          ("ipPrecedence", 14),
          ("dscp", 15),
          ("sourceIpv6", 16),
          ("destIpv6", 17),
          ("nextHeader", 18),
          ("trafficClass", 19),
          ("sourceL4PortRange", 20),
          ("destL4PortRange", 21),
          ("sourceL4Port", 22),
          ("destL4Port", 23))
    )

_AclProfileFieldMask_Type.__name__ = "Bits"
_AclProfileFieldMask_Object = MibTableColumn
aclProfileFieldMask = _AclProfileFieldMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 3),
    _AclProfileFieldMask_Type()
)
aclProfileFieldMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileFieldMask.setStatus("current")


class _AclProfileRuleEtype_Type(Integer32):
    """Custom type aclProfileRuleEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleEtype_Type.__name__ = "Integer32"
_AclProfileRuleEtype_Object = MibTableColumn
aclProfileRuleEtype = _AclProfileRuleEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 4),
    _AclProfileRuleEtype_Type()
)
aclProfileRuleEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleEtype.setStatus("current")
_AclProfileRuleSrcMac_Type = PhysAddress
_AclProfileRuleSrcMac_Object = MibTableColumn
aclProfileRuleSrcMac = _AclProfileRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 5),
    _AclProfileRuleSrcMac_Type()
)
aclProfileRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcMac.setStatus("current")
_AclProfileRuleDestMac_Type = PhysAddress
_AclProfileRuleDestMac_Object = MibTableColumn
aclProfileRuleDestMac = _AclProfileRuleDestMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 6),
    _AclProfileRuleDestMac_Type()
)
aclProfileRuleDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestMac.setStatus("current")
_AclProfileRuleSrcOui_Type = OctetString
_AclProfileRuleSrcOui_Object = MibTableColumn
aclProfileRuleSrcOui = _AclProfileRuleSrcOui_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 7),
    _AclProfileRuleSrcOui_Type()
)
aclProfileRuleSrcOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcOui.setStatus("current")
_AclProfileRuleDestOui_Type = OctetString
_AclProfileRuleDestOui_Object = MibTableColumn
aclProfileRuleDestOui = _AclProfileRuleDestOui_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 8),
    _AclProfileRuleDestOui_Type()
)
aclProfileRuleDestOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestOui.setStatus("current")


class _AclProfileRuleInnerVlan_Type(VlanIndex):
    """Custom type aclProfileRuleInnerVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclProfileRuleInnerVlan_Type.__name__ = "VlanIndex"
_AclProfileRuleInnerVlan_Object = MibTableColumn
aclProfileRuleInnerVlan = _AclProfileRuleInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 9),
    _AclProfileRuleInnerVlan_Type()
)
aclProfileRuleInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleInnerVlan.setStatus("current")


class _AclProfileRuleOuterVlan_Type(VlanIndex):
    """Custom type aclProfileRuleOuterVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclProfileRuleOuterVlan_Type.__name__ = "VlanIndex"
_AclProfileRuleOuterVlan_Object = MibTableColumn
aclProfileRuleOuterVlan = _AclProfileRuleOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 10),
    _AclProfileRuleOuterVlan_Type()
)
aclProfileRuleOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleOuterVlan.setStatus("current")


class _AclProfileRuleInnerPbit_Type(Integer32):
    """Custom type aclProfileRuleInnerPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRuleInnerPbit_Type.__name__ = "Integer32"
_AclProfileRuleInnerPbit_Object = MibTableColumn
aclProfileRuleInnerPbit = _AclProfileRuleInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 11),
    _AclProfileRuleInnerPbit_Type()
)
aclProfileRuleInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleInnerPbit.setStatus("current")


class _AclProfileRuleOuterPbit_Type(Integer32):
    """Custom type aclProfileRuleOuterPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRuleOuterPbit_Type.__name__ = "Integer32"
_AclProfileRuleOuterPbit_Object = MibTableColumn
aclProfileRuleOuterPbit = _AclProfileRuleOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 12),
    _AclProfileRuleOuterPbit_Type()
)
aclProfileRuleOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleOuterPbit.setStatus("current")
_AclProfileRuleSrcIpRange_Type = IpAddress
_AclProfileRuleSrcIpRange_Object = MibTableColumn
aclProfileRuleSrcIpRange = _AclProfileRuleSrcIpRange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 13),
    _AclProfileRuleSrcIpRange_Type()
)
aclProfileRuleSrcIpRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIpRange.setStatus("current")


class _AclProfileRuleSrcIpMask_Type(Integer32):
    """Custom type aclProfileRuleSrcIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_AclProfileRuleSrcIpMask_Type.__name__ = "Integer32"
_AclProfileRuleSrcIpMask_Object = MibTableColumn
aclProfileRuleSrcIpMask = _AclProfileRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 14),
    _AclProfileRuleSrcIpMask_Type()
)
aclProfileRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIpMask.setStatus("current")
_AclProfileRuleDestIpRange_Type = IpAddress
_AclProfileRuleDestIpRange_Object = MibTableColumn
aclProfileRuleDestIpRange = _AclProfileRuleDestIpRange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 15),
    _AclProfileRuleDestIpRange_Type()
)
aclProfileRuleDestIpRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestIpRange.setStatus("current")


class _AclProfileRuleDestIpMask_Type(Integer32):
    """Custom type aclProfileRuleDestIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_AclProfileRuleDestIpMask_Type.__name__ = "Integer32"
_AclProfileRuleDestIpMask_Object = MibTableColumn
aclProfileRuleDestIpMask = _AclProfileRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 16),
    _AclProfileRuleDestIpMask_Type()
)
aclProfileRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestIpMask.setStatus("current")
_AclProfileRuleSrcIp_Type = IpAddress
_AclProfileRuleSrcIp_Object = MibTableColumn
aclProfileRuleSrcIp = _AclProfileRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 17),
    _AclProfileRuleSrcIp_Type()
)
aclProfileRuleSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIp.setStatus("current")
_AclProfileRuleDestIp_Type = IpAddress
_AclProfileRuleDestIp_Object = MibTableColumn
aclProfileRuleDestIp = _AclProfileRuleDestIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 18),
    _AclProfileRuleDestIp_Type()
)
aclProfileRuleDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestIp.setStatus("current")


class _AclProfileRuleProtocol_Type(Integer32):
    """Custom type aclProfileRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleProtocol_Type.__name__ = "Integer32"
_AclProfileRuleProtocol_Object = MibTableColumn
aclProfileRuleProtocol = _AclProfileRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 19),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")


class _AclProfileRuleIpPrecedence_Type(Integer32):
    """Custom type aclProfileRuleIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRuleIpPrecedence_Type.__name__ = "Integer32"
_AclProfileRuleIpPrecedence_Object = MibTableColumn
aclProfileRuleIpPrecedence = _AclProfileRuleIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 20),
    _AclProfileRuleIpPrecedence_Type()
)
aclProfileRuleIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleIpPrecedence.setStatus("current")


class _AclProfileRuleDscp_Type(Integer32):
    """Custom type aclProfileRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclProfileRuleDscp_Type.__name__ = "Integer32"
_AclProfileRuleDscp_Object = MibTableColumn
aclProfileRuleDscp = _AclProfileRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 21),
    _AclProfileRuleDscp_Type()
)
aclProfileRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDscp.setStatus("current")
_AclProfileRuleSrcIpv6_Type = InetAddress
_AclProfileRuleSrcIpv6_Object = MibTableColumn
aclProfileRuleSrcIpv6 = _AclProfileRuleSrcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 22),
    _AclProfileRuleSrcIpv6_Type()
)
aclProfileRuleSrcIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIpv6.setStatus("current")
_AclProfileRuleDestIpv6_Type = InetAddress
_AclProfileRuleDestIpv6_Object = MibTableColumn
aclProfileRuleDestIpv6 = _AclProfileRuleDestIpv6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 23),
    _AclProfileRuleDestIpv6_Type()
)
aclProfileRuleDestIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestIpv6.setStatus("current")


class _AclProfileRuleNextHeader_Type(Integer32):
    """Custom type aclProfileRuleNextHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclProfileRuleNextHeader_Type.__name__ = "Integer32"
_AclProfileRuleNextHeader_Object = MibTableColumn
aclProfileRuleNextHeader = _AclProfileRuleNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 24),
    _AclProfileRuleNextHeader_Type()
)
aclProfileRuleNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleNextHeader.setStatus("current")


class _AclProfileRuleTrafficClass_Type(Integer32):
    """Custom type aclProfileRuleTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleTrafficClass_Type.__name__ = "Integer32"
_AclProfileRuleTrafficClass_Object = MibTableColumn
aclProfileRuleTrafficClass = _AclProfileRuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 25),
    _AclProfileRuleTrafficClass_Type()
)
aclProfileRuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleTrafficClass.setStatus("current")


class _AclProfileRuleSrcL4StartPort_Type(Integer32):
    """Custom type aclProfileRuleSrcL4StartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcL4StartPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcL4StartPort_Object = MibTableColumn
aclProfileRuleSrcL4StartPort = _AclProfileRuleSrcL4StartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 26),
    _AclProfileRuleSrcL4StartPort_Type()
)
aclProfileRuleSrcL4StartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcL4StartPort.setStatus("current")


class _AclProfileRuleSrcL4EndPort_Type(Integer32):
    """Custom type aclProfileRuleSrcL4EndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcL4EndPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcL4EndPort_Object = MibTableColumn
aclProfileRuleSrcL4EndPort = _AclProfileRuleSrcL4EndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 27),
    _AclProfileRuleSrcL4EndPort_Type()
)
aclProfileRuleSrcL4EndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcL4EndPort.setStatus("current")


class _AclProfileRuleDestL4StartPort_Type(Integer32):
    """Custom type aclProfileRuleDestL4StartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestL4StartPort_Type.__name__ = "Integer32"
_AclProfileRuleDestL4StartPort_Object = MibTableColumn
aclProfileRuleDestL4StartPort = _AclProfileRuleDestL4StartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 28),
    _AclProfileRuleDestL4StartPort_Type()
)
aclProfileRuleDestL4StartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestL4StartPort.setStatus("current")


class _AclProfileRuleDestL4EndPort_Type(Integer32):
    """Custom type aclProfileRuleDestL4EndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestL4EndPort_Type.__name__ = "Integer32"
_AclProfileRuleDestL4EndPort_Object = MibTableColumn
aclProfileRuleDestL4EndPort = _AclProfileRuleDestL4EndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 29),
    _AclProfileRuleDestL4EndPort_Type()
)
aclProfileRuleDestL4EndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestL4EndPort.setStatus("current")


class _AclProfileRuleSrcL4Port_Type(Integer32):
    """Custom type aclProfileRuleSrcL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcL4Port_Type.__name__ = "Integer32"
_AclProfileRuleSrcL4Port_Object = MibTableColumn
aclProfileRuleSrcL4Port = _AclProfileRuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 30),
    _AclProfileRuleSrcL4Port_Type()
)
aclProfileRuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSrcL4Port.setStatus("current")


class _AclProfileRuleDestL4Port_Type(Integer32):
    """Custom type aclProfileRuleDestL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestL4Port_Type.__name__ = "Integer32"
_AclProfileRuleDestL4Port_Object = MibTableColumn
aclProfileRuleDestL4Port = _AclProfileRuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 31),
    _AclProfileRuleDestL4Port_Type()
)
aclProfileRuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDestL4Port.setStatus("current")


class _AclProfileActionRate_Type(Integer32):
    """Custom type aclProfileActionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_AclProfileActionRate_Type.__name__ = "Integer32"
_AclProfileActionRate_Object = MibTableColumn
aclProfileActionRate = _AclProfileActionRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 32),
    _AclProfileActionRate_Type()
)
aclProfileActionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionRate.setStatus("current")
if mibBuilder.loadTexts:
    aclProfileActionRate.setUnits("kbps")


class _AclProfileActionInnerPbit_Type(Integer32):
    """Custom type aclProfileActionInnerPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionInnerPbit_Type.__name__ = "Integer32"
_AclProfileActionInnerPbit_Object = MibTableColumn
aclProfileActionInnerPbit = _AclProfileActionInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 33),
    _AclProfileActionInnerPbit_Type()
)
aclProfileActionInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionInnerPbit.setStatus("current")


class _AclProfileActionOuterPbit_Type(Integer32):
    """Custom type aclProfileActionOuterPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionOuterPbit_Type.__name__ = "Integer32"
_AclProfileActionOuterPbit_Object = MibTableColumn
aclProfileActionOuterPbit = _AclProfileActionOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 34),
    _AclProfileActionOuterPbit_Type()
)
aclProfileActionOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionOuterPbit.setStatus("current")


class _AclProfileActionDscp_Type(Integer32):
    """Custom type aclProfileActionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclProfileActionDscp_Type.__name__ = "Integer32"
_AclProfileActionDscp_Object = MibTableColumn
aclProfileActionDscp = _AclProfileActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 35),
    _AclProfileActionDscp_Type()
)
aclProfileActionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionDscp.setStatus("current")


class _AclProfileActionTrafficClass_Type(Integer32):
    """Custom type aclProfileActionTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileActionTrafficClass_Type.__name__ = "Integer32"
_AclProfileActionTrafficClass_Object = MibTableColumn
aclProfileActionTrafficClass = _AclProfileActionTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 36),
    _AclProfileActionTrafficClass_Type()
)
aclProfileActionTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionTrafficClass.setStatus("current")


class _AclProfileActionQos_Type(Integer32):
    """Custom type aclProfileActionQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionQos_Type.__name__ = "Integer32"
_AclProfileActionQos_Object = MibTableColumn
aclProfileActionQos = _AclProfileActionQos_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 37),
    _AclProfileActionQos_Type()
)
aclProfileActionQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileActionQos.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 38),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_AclProfilePriority_Type = OctetString
_AclProfilePriority_Object = MibTableColumn
aclProfilePriority = _AclProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 6, 1, 39),
    _AclProfilePriority_Type()
)
aclProfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfilePriority.setStatus("current")
_AclMulticast_ObjectIdentity = ObjectIdentity
aclMulticast = _AclMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 7)
)


class _AclUnsolicited_Type(Integer32):
    """Custom type aclUnsolicited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropMulticastTraffic", 1),
          ("noDropMulticastTraffic", 2))
    )


_AclUnsolicited_Type.__name__ = "Integer32"
_AclUnsolicited_Object = MibScalar
aclUnsolicited = _AclUnsolicited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 7, 1),
    _AclUnsolicited_Type()
)
aclUnsolicited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUnsolicited.setStatus("current")


class _AclUpstream_Type(Integer32):
    """Custom type aclUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropMulticastTraffic", 1),
          ("noDropMulticastTraffic", 2))
    )


_AclUpstream_Type.__name__ = "Integer32"
_AclUpstream_Object = MibScalar
aclUpstream = _AclUpstream_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 7, 2),
    _AclUpstream_Type()
)
aclUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUpstream.setStatus("current")
_AclStormControl_ObjectIdentity = ObjectIdentity
aclStormControl = _AclStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 8)
)


class _AclBroadcast_Type(Integer32):
    """Custom type aclBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100000),
    )


_AclBroadcast_Type.__name__ = "Integer32"
_AclBroadcast_Object = MibScalar
aclBroadcast = _AclBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 8, 1),
    _AclBroadcast_Type()
)
aclBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclBroadcast.setStatus("current")


class _AclDlf_Type(Integer32):
    """Custom type aclDlf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100000),
    )


_AclDlf_Type.__name__ = "Integer32"
_AclDlf_Object = MibScalar
aclDlf = _AclDlf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 8, 2),
    _AclDlf_Type()
)
aclDlf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclDlf.setStatus("current")
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20)
)


class _Dot1xEnable_Type(Integer32):
    """Custom type dot1xEnable based on Integer32"""
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


_Dot1xEnable_Type.__name__ = "Integer32"
_Dot1xEnable_Object = MibScalar
dot1xEnable = _Dot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 1),
    _Dot1xEnable_Type()
)
dot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xEnable.setStatus("current")


class _Dot1xAuthMethod_Type(Integer32):
    """Custom type dot1xAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userprofile", 1),
          ("radius", 2))
    )


_Dot1xAuthMethod_Type.__name__ = "Integer32"
_Dot1xAuthMethod_Object = MibScalar
dot1xAuthMethod = _Dot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 2),
    _Dot1xAuthMethod_Type()
)
dot1xAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthMethod.setStatus("current")
_Dot1xRadiusServerTable_Object = MibTable
dot1xRadiusServerTable = _Dot1xRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3)
)
if mibBuilder.loadTexts:
    dot1xRadiusServerTable.setStatus("current")
_Dot1xRadiusServerEntry_Object = MibTableRow
dot1xRadiusServerEntry = _Dot1xRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3, 1)
)
dot1xRadiusServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dot1xRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    dot1xRadiusServerEntry.setStatus("current")
_Dot1xRadiusServerIndex_Type = Integer32
_Dot1xRadiusServerIndex_Object = MibTableColumn
dot1xRadiusServerIndex = _Dot1xRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3, 1, 1),
    _Dot1xRadiusServerIndex_Type()
)
dot1xRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusServerIndex.setStatus("current")
_Dot1xRadiusServerIp_Type = IpAddress
_Dot1xRadiusServerIp_Object = MibTableColumn
dot1xRadiusServerIp = _Dot1xRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3, 1, 2),
    _Dot1xRadiusServerIp_Type()
)
dot1xRadiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xRadiusServerIp.setStatus("current")


class _Dot1xRadiusServerPort_Type(Integer32):
    """Custom type dot1xRadiusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xRadiusServerPort_Type.__name__ = "Integer32"
_Dot1xRadiusServerPort_Object = MibTableColumn
dot1xRadiusServerPort = _Dot1xRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3, 1, 3),
    _Dot1xRadiusServerPort_Type()
)
dot1xRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xRadiusServerPort.setStatus("current")


class _Dot1xRadiusServerSecret_Type(DisplayString):
    """Custom type dot1xRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Dot1xRadiusServerSecret_Type.__name__ = "DisplayString"
_Dot1xRadiusServerSecret_Object = MibTableColumn
dot1xRadiusServerSecret = _Dot1xRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 3, 1, 4),
    _Dot1xRadiusServerSecret_Type()
)
dot1xRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xRadiusServerSecret.setStatus("current")
_Dot1xPortTable_Object = MibTable
dot1xPortTable = _Dot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4)
)
if mibBuilder.loadTexts:
    dot1xPortTable.setStatus("current")
_Dot1xPortEntry_Object = MibTableRow
dot1xPortEntry = _Dot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4, 1)
)
dot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot1xPortEntry.setStatus("current")


class _Dot1xPortRadiusServerIndex_Type(Integer32):
    """Custom type dot1xPortRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot1xPortRadiusServerIndex_Type.__name__ = "Integer32"
_Dot1xPortRadiusServerIndex_Object = MibTableColumn
dot1xPortRadiusServerIndex = _Dot1xPortRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4, 1, 1),
    _Dot1xPortRadiusServerIndex_Type()
)
dot1xPortRadiusServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortRadiusServerIndex.setStatus("current")


class _Dot1xPortEnable_Type(Integer32):
    """Custom type dot1xPortEnable based on Integer32"""
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


_Dot1xPortEnable_Type.__name__ = "Integer32"
_Dot1xPortEnable_Object = MibTableColumn
dot1xPortEnable = _Dot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4, 1, 2),
    _Dot1xPortEnable_Type()
)
dot1xPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortEnable.setStatus("current")


class _Dot1xPortCircuitIDEnable_Type(Integer32):
    """Custom type dot1xPortCircuitIDEnable based on Integer32"""
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


_Dot1xPortCircuitIDEnable_Type.__name__ = "Integer32"
_Dot1xPortCircuitIDEnable_Object = MibTableColumn
dot1xPortCircuitIDEnable = _Dot1xPortCircuitIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4, 1, 3),
    _Dot1xPortCircuitIDEnable_Type()
)
dot1xPortCircuitIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortCircuitIDEnable.setStatus("current")


class _Dot1xPortCircuitIDInfo_Type(DisplayString):
    """Custom type dot1xPortCircuitIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Dot1xPortCircuitIDInfo_Type.__name__ = "DisplayString"
_Dot1xPortCircuitIDInfo_Object = MibTableColumn
dot1xPortCircuitIDInfo = _Dot1xPortCircuitIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 4, 1, 4),
    _Dot1xPortCircuitIDInfo_Type()
)
dot1xPortCircuitIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xPortCircuitIDInfo.setStatus("current")
_Dot1xUserProfileTable_Object = MibTable
dot1xUserProfileTable = _Dot1xUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 5)
)
if mibBuilder.loadTexts:
    dot1xUserProfileTable.setStatus("current")
_Dot1xUserProfileEntry_Object = MibTableRow
dot1xUserProfileEntry = _Dot1xUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 5, 1)
)
dot1xUserProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "dot1xUserProfileName"),
)
if mibBuilder.loadTexts:
    dot1xUserProfileEntry.setStatus("current")


class _Dot1xUserProfileName_Type(DisplayString):
    """Custom type dot1xUserProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Dot1xUserProfileName_Type.__name__ = "DisplayString"
_Dot1xUserProfileName_Object = MibTableColumn
dot1xUserProfileName = _Dot1xUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 5, 1, 1),
    _Dot1xUserProfileName_Type()
)
dot1xUserProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xUserProfileName.setStatus("current")


class _Dot1xUserProfilePassword_Type(DisplayString):
    """Custom type dot1xUserProfilePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 95),
    )


_Dot1xUserProfilePassword_Type.__name__ = "DisplayString"
_Dot1xUserProfilePassword_Object = MibTableColumn
dot1xUserProfilePassword = _Dot1xUserProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 5, 1, 2),
    _Dot1xUserProfilePassword_Type()
)
dot1xUserProfilePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xUserProfilePassword.setStatus("current")
_Dot1xUserProfileRowStatus_Type = RowStatus
_Dot1xUserProfileRowStatus_Object = MibTableColumn
dot1xUserProfileRowStatus = _Dot1xUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 5, 1, 3),
    _Dot1xUserProfileRowStatus_Type()
)
dot1xUserProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xUserProfileRowStatus.setStatus("current")
_Dot1xStatsPortTable_Object = MibTable
dot1xStatsPortTable = _Dot1xStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 6)
)
if mibBuilder.loadTexts:
    dot1xStatsPortTable.setStatus("current")
_Dot1xStatsPortEntry_Object = MibTableRow
dot1xStatsPortEntry = _Dot1xStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 6, 1)
)
dot1xStatsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot1xStatsPortEntry.setStatus("current")
_Dot1xStatsPortReAuthCount_Type = Integer32
_Dot1xStatsPortReAuthCount_Object = MibTableColumn
dot1xStatsPortReAuthCount = _Dot1xStatsPortReAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 20, 6, 1, 1),
    _Dot1xStatsPortReAuthCount_Type()
)
dot1xStatsPortReAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xStatsPortReAuthCount.setStatus("current")
_AclFieldPriorityTable_Object = MibTable
aclFieldPriorityTable = _AclFieldPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 21)
)
if mibBuilder.loadTexts:
    aclFieldPriorityTable.setStatus("current")
_AclFieldPriorityEntry_Object = MibTableRow
aclFieldPriorityEntry = _AclFieldPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 21, 1)
)
aclFieldPriorityEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "aclFieldPriorityIndex"),
)
if mibBuilder.loadTexts:
    aclFieldPriorityEntry.setStatus("current")


class _AclFieldPriorityIndex_Type(Integer32):
    """Custom type aclFieldPriorityIndex based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("sourceMac", 1),
          ("destMac", 2),
          ("sourceOui", 3),
          ("destOui", 4),
          ("sourceIpAddress", 5),
          ("sourceIpRange", 6),
          ("destIpAddress", 7),
          ("destIpRange", 8),
          ("sourceIpv6", 9),
          ("destIpv6", 10),
          ("sourceL4Port", 11),
          ("sourceL4PortRange", 12),
          ("destL4Port", 13),
          ("destL4PortRange", 14),
          ("outerVlan", 15),
          ("innerVlan", 16),
          ("outerPbit", 17),
          ("innerPbit", 18),
          ("etherType", 19),
          ("nextHeader", 20),
          ("trafficClass", 21),
          ("ipPrecedence", 22),
          ("dscp", 23),
          ("protocol", 24))
    )


_AclFieldPriorityIndex_Type.__name__ = "Integer32"
_AclFieldPriorityIndex_Object = MibTableColumn
aclFieldPriorityIndex = _AclFieldPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 21, 1, 1),
    _AclFieldPriorityIndex_Type()
)
aclFieldPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclFieldPriorityIndex.setStatus("current")
_AclFieldPriorityValue_Type = OctetString
_AclFieldPriorityValue_Object = MibTableColumn
aclFieldPriorityValue = _AclFieldPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 21, 1, 2),
    _AclFieldPriorityValue_Type()
)
aclFieldPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclFieldPriorityValue.setStatus("current")
_AclPacketTypeFilterTable_Object = MibTable
aclPacketTypeFilterTable = _AclPacketTypeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 22)
)
if mibBuilder.loadTexts:
    aclPacketTypeFilterTable.setStatus("current")
_AclPacketTypeFilterEntry_Object = MibTableRow
aclPacketTypeFilterEntry = _AclPacketTypeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 22, 1)
)
aclPacketTypeFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "aclPacketTypeFilterVlanId"),
)
if mibBuilder.loadTexts:
    aclPacketTypeFilterEntry.setStatus("current")


class _AclPacketTypeFilterVlanId_Type(VlanIndex):
    """Custom type aclPacketTypeFilterVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclPacketTypeFilterVlanId_Type.__name__ = "VlanIndex"
_AclPacketTypeFilterVlanId_Object = MibTableColumn
aclPacketTypeFilterVlanId = _AclPacketTypeFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 22, 1, 1),
    _AclPacketTypeFilterVlanId_Type()
)
aclPacketTypeFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPacketTypeFilterVlanId.setStatus("current")


class _AclPacketTypeFilterActionMask_Type(Bits):
    """Custom type aclPacketTypeFilterActionMask based on Bits"""
    namedValues = NamedValues(
        *(("dropIgmp", 0),
          ("dropEapol", 1),
          ("dropDhcp", 2),
          ("dropNetBios", 3),
          ("dropArp", 4),
          ("dropIp", 5),
          ("dropPppoe", 6),
          ("pppoeOnly", 7))
    )

_AclPacketTypeFilterActionMask_Type.__name__ = "Bits"
_AclPacketTypeFilterActionMask_Object = MibTableColumn
aclPacketTypeFilterActionMask = _AclPacketTypeFilterActionMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 22, 1, 2),
    _AclPacketTypeFilterActionMask_Type()
)
aclPacketTypeFilterActionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPacketTypeFilterActionMask.setStatus("current")
_AclPacketTypeFilterRowStatus_Type = RowStatus
_AclPacketTypeFilterRowStatus_Object = MibTableColumn
aclPacketTypeFilterRowStatus = _AclPacketTypeFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 1, 22, 1, 3),
    _AclPacketTypeFilterRowStatus_Type()
)
aclPacketTypeFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPacketTypeFilterRowStatus.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2)
)
_AlarmOps_ObjectIdentity = ObjectIdentity
alarmOps = _AlarmOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1)
)
_CurAlarmClearTargetTrapOid_Type = ObjectIdentifier
_CurAlarmClearTargetTrapOid_Object = MibScalar
curAlarmClearTargetTrapOid = _CurAlarmClearTargetTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1, 1),
    _CurAlarmClearTargetTrapOid_Type()
)
curAlarmClearTargetTrapOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curAlarmClearTargetTrapOid.setStatus("current")
_CurAlarmClearTargetIndex1_Type = Integer32
_CurAlarmClearTargetIndex1_Object = MibScalar
curAlarmClearTargetIndex1 = _CurAlarmClearTargetIndex1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1, 2),
    _CurAlarmClearTargetIndex1_Type()
)
curAlarmClearTargetIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curAlarmClearTargetIndex1.setStatus("current")
_CurAlarmClearTargetIndex2_Type = Integer32
_CurAlarmClearTargetIndex2_Object = MibScalar
curAlarmClearTargetIndex2 = _CurAlarmClearTargetIndex2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1, 3),
    _CurAlarmClearTargetIndex2_Type()
)
curAlarmClearTargetIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curAlarmClearTargetIndex2.setStatus("current")
_CurAlarmClearTargetIndex3_Type = Integer32
_CurAlarmClearTargetIndex3_Object = MibScalar
curAlarmClearTargetIndex3 = _CurAlarmClearTargetIndex3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1, 4),
    _CurAlarmClearTargetIndex3_Type()
)
curAlarmClearTargetIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curAlarmClearTargetIndex3.setStatus("current")


class _AlarmOperation_Type(Integer32):
    """Custom type alarmOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearOneCurrAlarm", 1),
          ("clearAllCurrAlarm", 2),
          ("clearAllHistoricalAlarm", 3))
    )


_AlarmOperation_Type.__name__ = "Integer32"
_AlarmOperation_Object = MibScalar
alarmOperation = _AlarmOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 1, 5),
    _AlarmOperation_Type()
)
alarmOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOperation.setStatus("current")
_CurrAlarmTable_Object = MibTable
currAlarmTable = _CurrAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2)
)
if mibBuilder.loadTexts:
    currAlarmTable.setStatus("current")
_CurrAlarmEntry_Object = MibTableRow
currAlarmEntry = _CurrAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1)
)
currAlarmEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "currAlarmIndex"),
)
if mibBuilder.loadTexts:
    currAlarmEntry.setStatus("current")
_CurrAlarmIndex_Type = Integer32
_CurrAlarmIndex_Object = MibTableColumn
currAlarmIndex = _CurrAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 1),
    _CurrAlarmIndex_Type()
)
currAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmIndex.setStatus("current")
_CurrAlarmCondId_Type = Integer32
_CurrAlarmCondId_Object = MibTableColumn
currAlarmCondId = _CurrAlarmCondId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 2),
    _CurrAlarmCondId_Type()
)
currAlarmCondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmCondId.setStatus("current")
_CurrAlarmOccurTime_Type = TimeTicks
_CurrAlarmOccurTime_Object = MibTableColumn
currAlarmOccurTime = _CurrAlarmOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 3),
    _CurrAlarmOccurTime_Type()
)
currAlarmOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmOccurTime.setStatus("current")
_CurrAlarmTrapOid_Type = ObjectIdentifier
_CurrAlarmTrapOid_Object = MibTableColumn
currAlarmTrapOid = _CurrAlarmTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 4),
    _CurrAlarmTrapOid_Type()
)
currAlarmTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmTrapOid.setStatus("current")
_CurrAlarmParam1_Type = Integer32
_CurrAlarmParam1_Object = MibTableColumn
currAlarmParam1 = _CurrAlarmParam1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 5),
    _CurrAlarmParam1_Type()
)
currAlarmParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam1.setStatus("current")
_CurrAlarmParam2_Type = Integer32
_CurrAlarmParam2_Object = MibTableColumn
currAlarmParam2 = _CurrAlarmParam2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 6),
    _CurrAlarmParam2_Type()
)
currAlarmParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam2.setStatus("current")
_CurrAlarmParam3_Type = Integer32
_CurrAlarmParam3_Object = MibTableColumn
currAlarmParam3 = _CurrAlarmParam3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 7),
    _CurrAlarmParam3_Type()
)
currAlarmParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam3.setStatus("current")
_CurrAlarmParam4_Type = Integer32
_CurrAlarmParam4_Object = MibTableColumn
currAlarmParam4 = _CurrAlarmParam4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 8),
    _CurrAlarmParam4_Type()
)
currAlarmParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam4.setStatus("current")
_CurrAlarmParam5_Type = Integer32
_CurrAlarmParam5_Object = MibTableColumn
currAlarmParam5 = _CurrAlarmParam5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 9),
    _CurrAlarmParam5_Type()
)
currAlarmParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam5.setStatus("current")
_CurrAlarmParam6_Type = Integer32
_CurrAlarmParam6_Object = MibTableColumn
currAlarmParam6 = _CurrAlarmParam6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 10),
    _CurrAlarmParam6_Type()
)
currAlarmParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam6.setStatus("current")
_CurrAlarmParam7_Type = Integer32
_CurrAlarmParam7_Object = MibTableColumn
currAlarmParam7 = _CurrAlarmParam7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 11),
    _CurrAlarmParam7_Type()
)
currAlarmParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam7.setStatus("current")
_CurrAlarmParam8_Type = Integer32
_CurrAlarmParam8_Object = MibTableColumn
currAlarmParam8 = _CurrAlarmParam8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 12),
    _CurrAlarmParam8_Type()
)
currAlarmParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam8.setStatus("current")
_CurrAlarmParam9_Type = DisplayString
_CurrAlarmParam9_Object = MibTableColumn
currAlarmParam9 = _CurrAlarmParam9_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 13),
    _CurrAlarmParam9_Type()
)
currAlarmParam9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmParam9.setStatus("current")
_CurrAlarmTimeDescr_Type = DisplayString
_CurrAlarmTimeDescr_Object = MibTableColumn
currAlarmTimeDescr = _CurrAlarmTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 14),
    _CurrAlarmTimeDescr_Type()
)
currAlarmTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmTimeDescr.setStatus("current")


class _CurrAlarmSeverity_Type(Integer32):
    """Custom type currAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_CurrAlarmSeverity_Type.__name__ = "Integer32"
_CurrAlarmSeverity_Object = MibTableColumn
currAlarmSeverity = _CurrAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 15),
    _CurrAlarmSeverity_Type()
)
currAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmSeverity.setStatus("current")
_CurrAlarmDescr_Type = DisplayString
_CurrAlarmDescr_Object = MibTableColumn
currAlarmDescr = _CurrAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 2, 1, 16),
    _CurrAlarmDescr_Type()
)
currAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currAlarmDescr.setStatus("current")
_HistAlarmTable_Object = MibTable
histAlarmTable = _HistAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3)
)
if mibBuilder.loadTexts:
    histAlarmTable.setStatus("current")
_HistAlarmEntry_Object = MibTableRow
histAlarmEntry = _HistAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1)
)
histAlarmEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "histAlarmIndex"),
)
if mibBuilder.loadTexts:
    histAlarmEntry.setStatus("current")
_HistAlarmIndex_Type = Integer32
_HistAlarmIndex_Object = MibTableColumn
histAlarmIndex = _HistAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 1),
    _HistAlarmIndex_Type()
)
histAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmIndex.setStatus("current")
_HistAlarmCondId_Type = Integer32
_HistAlarmCondId_Object = MibTableColumn
histAlarmCondId = _HistAlarmCondId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 2),
    _HistAlarmCondId_Type()
)
histAlarmCondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmCondId.setStatus("current")
_HistAlarmOccurTime_Type = TimeTicks
_HistAlarmOccurTime_Object = MibTableColumn
histAlarmOccurTime = _HistAlarmOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 3),
    _HistAlarmOccurTime_Type()
)
histAlarmOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmOccurTime.setStatus("current")
_HistAlarmTrapOid_Type = ObjectIdentifier
_HistAlarmTrapOid_Object = MibTableColumn
histAlarmTrapOid = _HistAlarmTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 4),
    _HistAlarmTrapOid_Type()
)
histAlarmTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmTrapOid.setStatus("current")
_HistAlarmParam1_Type = Integer32
_HistAlarmParam1_Object = MibTableColumn
histAlarmParam1 = _HistAlarmParam1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 5),
    _HistAlarmParam1_Type()
)
histAlarmParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam1.setStatus("current")
_HistAlarmParam2_Type = Integer32
_HistAlarmParam2_Object = MibTableColumn
histAlarmParam2 = _HistAlarmParam2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 6),
    _HistAlarmParam2_Type()
)
histAlarmParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam2.setStatus("current")
_HistAlarmParam3_Type = Integer32
_HistAlarmParam3_Object = MibTableColumn
histAlarmParam3 = _HistAlarmParam3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 7),
    _HistAlarmParam3_Type()
)
histAlarmParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam3.setStatus("current")
_HistAlarmParam4_Type = Integer32
_HistAlarmParam4_Object = MibTableColumn
histAlarmParam4 = _HistAlarmParam4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 8),
    _HistAlarmParam4_Type()
)
histAlarmParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam4.setStatus("current")
_HistAlarmParam5_Type = Integer32
_HistAlarmParam5_Object = MibTableColumn
histAlarmParam5 = _HistAlarmParam5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 9),
    _HistAlarmParam5_Type()
)
histAlarmParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam5.setStatus("current")
_HistAlarmParam6_Type = Integer32
_HistAlarmParam6_Object = MibTableColumn
histAlarmParam6 = _HistAlarmParam6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 10),
    _HistAlarmParam6_Type()
)
histAlarmParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam6.setStatus("current")
_HistAlarmParam7_Type = Integer32
_HistAlarmParam7_Object = MibTableColumn
histAlarmParam7 = _HistAlarmParam7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 11),
    _HistAlarmParam7_Type()
)
histAlarmParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam7.setStatus("current")
_HistAlarmParam8_Type = Integer32
_HistAlarmParam8_Object = MibTableColumn
histAlarmParam8 = _HistAlarmParam8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 12),
    _HistAlarmParam8_Type()
)
histAlarmParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam8.setStatus("current")
_HistAlarmParam9_Type = DisplayString
_HistAlarmParam9_Object = MibTableColumn
histAlarmParam9 = _HistAlarmParam9_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 13),
    _HistAlarmParam9_Type()
)
histAlarmParam9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmParam9.setStatus("current")
_HistAlarmTimeDescr_Type = DisplayString
_HistAlarmTimeDescr_Object = MibTableColumn
histAlarmTimeDescr = _HistAlarmTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 14),
    _HistAlarmTimeDescr_Type()
)
histAlarmTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmTimeDescr.setStatus("current")


class _HistAlarmSeverity_Type(Integer32):
    """Custom type histAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("event", 5))
    )


_HistAlarmSeverity_Type.__name__ = "Integer32"
_HistAlarmSeverity_Object = MibTableColumn
histAlarmSeverity = _HistAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 15),
    _HistAlarmSeverity_Type()
)
histAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmSeverity.setStatus("current")
_HistAlarmDescr_Type = DisplayString
_HistAlarmDescr_Object = MibTableColumn
histAlarmDescr = _HistAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 3, 1, 16),
    _HistAlarmDescr_Type()
)
histAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histAlarmDescr.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4, 1)
)
alarmConfEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "alarmConfTrapOid"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfTrapOid_Type = ObjectIdentifier
_AlarmConfTrapOid_Object = MibTableColumn
alarmConfTrapOid = _AlarmConfTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4, 1, 1),
    _AlarmConfTrapOid_Type()
)
alarmConfTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConfTrapOid.setStatus("current")


class _AlarmConfSeverity_Type(Integer32):
    """Custom type alarmConfSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("event", 5))
    )


_AlarmConfSeverity_Type.__name__ = "Integer32"
_AlarmConfSeverity_Object = MibTableColumn
alarmConfSeverity = _AlarmConfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4, 1, 2),
    _AlarmConfSeverity_Type()
)
alarmConfSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfSeverity.setStatus("current")


class _AlarmConfLogFacility_Type(Integer32):
    """Custom type alarmConfLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_AlarmConfLogFacility_Type.__name__ = "Integer32"
_AlarmConfLogFacility_Object = MibTableColumn
alarmConfLogFacility = _AlarmConfLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4, 1, 3),
    _AlarmConfLogFacility_Type()
)
alarmConfLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfLogFacility.setStatus("current")


class _AlarmConfTarget_Type(Integer32):
    """Custom type alarmConfTarget based on Integer32"""
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
        *(("snmp", 1),
          ("syslog", 2),
          ("all", 3),
          ("none", 4))
    )


_AlarmConfTarget_Type.__name__ = "Integer32"
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 4, 1, 4),
    _AlarmConfTarget_Type()
)
alarmConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfTarget.setStatus("current")


class _AlarmSeveritySystem_Type(Integer32):
    """Custom type alarmSeveritySystem based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_AlarmSeveritySystem_Type.__name__ = "Integer32"
_AlarmSeveritySystem_Object = MibScalar
alarmSeveritySystem = _AlarmSeveritySystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 5),
    _AlarmSeveritySystem_Type()
)
alarmSeveritySystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeveritySystem.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 6)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 6, 1)
)
alarmSeverityPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alarmSeverityPortEntry.setStatus("current")


class _AlarmSeverityPortThresh_Type(Integer32):
    """Custom type alarmSeverityPortThresh based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_AlarmSeverityPortThresh_Type.__name__ = "Integer32"
_AlarmSeverityPortThresh_Object = MibTableColumn
alarmSeverityPortThresh = _AlarmSeverityPortThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 6, 1, 1),
    _AlarmSeverityPortThresh_Type()
)
alarmSeverityPortThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeverityPortThresh.setStatus("current")
_AlarmControl_ObjectIdentity = ObjectIdentity
alarmControl = _AlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 7)
)


class _SysAlarmSuppressEnable_Type(Integer32):
    """Custom type sysAlarmSuppressEnable based on Integer32"""
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


_SysAlarmSuppressEnable_Type.__name__ = "Integer32"
_SysAlarmSuppressEnable_Object = MibScalar
sysAlarmSuppressEnable = _SysAlarmSuppressEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 7, 1),
    _SysAlarmSuppressEnable_Type()
)
sysAlarmSuppressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmSuppressEnable.setStatus("current")
_ExternalAlarmTable_Object = MibTable
externalAlarmTable = _ExternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 8)
)
if mibBuilder.loadTexts:
    externalAlarmTable.setStatus("current")
_ExternalAlarmEntry_Object = MibTableRow
externalAlarmEntry = _ExternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 8, 1)
)
externalAlarmEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "externalAlarmIndex"),
)
if mibBuilder.loadTexts:
    externalAlarmEntry.setStatus("current")


class _ExternalAlarmIndex_Type(Integer32):
    """Custom type externalAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ExternalAlarmIndex_Type.__name__ = "Integer32"
_ExternalAlarmIndex_Object = MibTableColumn
externalAlarmIndex = _ExternalAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 8, 1, 1),
    _ExternalAlarmIndex_Type()
)
externalAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAlarmIndex.setStatus("current")


class _ExternalAlarmName_Type(DisplayString):
    """Custom type externalAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExternalAlarmName_Type.__name__ = "DisplayString"
_ExternalAlarmName_Object = MibTableColumn
externalAlarmName = _ExternalAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 2, 8, 1, 2),
    _ExternalAlarmName_Type()
)
externalAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAlarmName.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3)
)
_DhcpL2agTable_Object = MibTable
dhcpL2agTable = _DhcpL2agTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpL2agTable.setStatus("current")
_DhcpL2agEntry_Object = MibTableRow
dhcpL2agEntry = _DhcpL2agEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1)
)
dhcpL2agEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dhcpL2agVlanId"),
)
if mibBuilder.loadTexts:
    dhcpL2agEntry.setStatus("current")


class _DhcpL2agVlanId_Type(VlanIndex):
    """Custom type dhcpL2agVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_DhcpL2agVlanId_Type.__name__ = "VlanIndex"
_DhcpL2agVlanId_Object = MibTableColumn
dhcpL2agVlanId = _DhcpL2agVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 1),
    _DhcpL2agVlanId_Type()
)
dhcpL2agVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpL2agVlanId.setStatus("current")


class _DhcpL2agMode_Type(Integer32):
    """Custom type dhcpL2agMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpTransparent", 1),
          ("dhcpL2Agent", 2))
    )


_DhcpL2agMode_Type.__name__ = "Integer32"
_DhcpL2agMode_Object = MibTableColumn
dhcpL2agMode = _DhcpL2agMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 2),
    _DhcpL2agMode_Type()
)
dhcpL2agMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agMode.setStatus("current")


class _DhcpL2agLdraEnable_Type(Integer32):
    """Custom type dhcpL2agLdraEnable based on Integer32"""
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


_DhcpL2agLdraEnable_Type.__name__ = "Integer32"
_DhcpL2agLdraEnable_Object = MibTableColumn
dhcpL2agLdraEnable = _DhcpL2agLdraEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 3),
    _DhcpL2agLdraEnable_Type()
)
dhcpL2agLdraEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agLdraEnable.setStatus("current")


class _DhcpL2agOpt18CircuitIDEnable_Type(Integer32):
    """Custom type dhcpL2agOpt18CircuitIDEnable based on Integer32"""
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


_DhcpL2agOpt18CircuitIDEnable_Type.__name__ = "Integer32"
_DhcpL2agOpt18CircuitIDEnable_Object = MibTableColumn
dhcpL2agOpt18CircuitIDEnable = _DhcpL2agOpt18CircuitIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 4),
    _DhcpL2agOpt18CircuitIDEnable_Type()
)
dhcpL2agOpt18CircuitIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt18CircuitIDEnable.setStatus("current")


class _DhcpL2agOpt18CircuitIDInfo_Type(DisplayString):
    """Custom type dhcpL2agOpt18CircuitIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpL2agOpt18CircuitIDInfo_Type.__name__ = "DisplayString"
_DhcpL2agOpt18CircuitIDInfo_Object = MibTableColumn
dhcpL2agOpt18CircuitIDInfo = _DhcpL2agOpt18CircuitIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 5),
    _DhcpL2agOpt18CircuitIDInfo_Type()
)
dhcpL2agOpt18CircuitIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt18CircuitIDInfo.setStatus("current")


class _DhcpL2agOpt37RemoteIDEnable_Type(Integer32):
    """Custom type dhcpL2agOpt37RemoteIDEnable based on Integer32"""
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


_DhcpL2agOpt37RemoteIDEnable_Type.__name__ = "Integer32"
_DhcpL2agOpt37RemoteIDEnable_Object = MibTableColumn
dhcpL2agOpt37RemoteIDEnable = _DhcpL2agOpt37RemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 6),
    _DhcpL2agOpt37RemoteIDEnable_Type()
)
dhcpL2agOpt37RemoteIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt37RemoteIDEnable.setStatus("current")


class _DhcpL2agOpt37RemoteIDInfo_Type(DisplayString):
    """Custom type dhcpL2agOpt37RemoteIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpL2agOpt37RemoteIDInfo_Type.__name__ = "DisplayString"
_DhcpL2agOpt37RemoteIDInfo_Object = MibTableColumn
dhcpL2agOpt37RemoteIDInfo = _DhcpL2agOpt37RemoteIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 7),
    _DhcpL2agOpt37RemoteIDInfo_Type()
)
dhcpL2agOpt37RemoteIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt37RemoteIDInfo.setStatus("current")


class _DhcpL2agOpt82CircuitIDEnable_Type(Integer32):
    """Custom type dhcpL2agOpt82CircuitIDEnable based on Integer32"""
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


_DhcpL2agOpt82CircuitIDEnable_Type.__name__ = "Integer32"
_DhcpL2agOpt82CircuitIDEnable_Object = MibTableColumn
dhcpL2agOpt82CircuitIDEnable = _DhcpL2agOpt82CircuitIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 8),
    _DhcpL2agOpt82CircuitIDEnable_Type()
)
dhcpL2agOpt82CircuitIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt82CircuitIDEnable.setStatus("current")


class _DhcpL2agOpt82CircuitIDInfo_Type(DisplayString):
    """Custom type dhcpL2agOpt82CircuitIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpL2agOpt82CircuitIDInfo_Type.__name__ = "DisplayString"
_DhcpL2agOpt82CircuitIDInfo_Object = MibTableColumn
dhcpL2agOpt82CircuitIDInfo = _DhcpL2agOpt82CircuitIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 9),
    _DhcpL2agOpt82CircuitIDInfo_Type()
)
dhcpL2agOpt82CircuitIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt82CircuitIDInfo.setStatus("current")


class _DhcpL2agOpt82RemoteIDEnable_Type(Integer32):
    """Custom type dhcpL2agOpt82RemoteIDEnable based on Integer32"""
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


_DhcpL2agOpt82RemoteIDEnable_Type.__name__ = "Integer32"
_DhcpL2agOpt82RemoteIDEnable_Object = MibTableColumn
dhcpL2agOpt82RemoteIDEnable = _DhcpL2agOpt82RemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 10),
    _DhcpL2agOpt82RemoteIDEnable_Type()
)
dhcpL2agOpt82RemoteIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt82RemoteIDEnable.setStatus("current")


class _DhcpL2agOpt82RemoteIDInfo_Type(DisplayString):
    """Custom type dhcpL2agOpt82RemoteIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpL2agOpt82RemoteIDInfo_Type.__name__ = "DisplayString"
_DhcpL2agOpt82RemoteIDInfo_Object = MibTableColumn
dhcpL2agOpt82RemoteIDInfo = _DhcpL2agOpt82RemoteIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 11),
    _DhcpL2agOpt82RemoteIDInfo_Type()
)
dhcpL2agOpt82RemoteIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agOpt82RemoteIDInfo.setStatus("current")
_DhcpL2agRowStatus_Type = RowStatus
_DhcpL2agRowStatus_Object = MibTableColumn
dhcpL2agRowStatus = _DhcpL2agRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 1, 1, 12),
    _DhcpL2agRowStatus_Type()
)
dhcpL2agRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2agRowStatus.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 1, 1)
)
dhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortEntry.setStatus("current")


class _DhcpSnoopPortIpMacBindingEnable_Type(Integer32):
    """Custom type dhcpSnoopPortIpMacBindingEnable based on Integer32"""
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


_DhcpSnoopPortIpMacBindingEnable_Type.__name__ = "Integer32"
_DhcpSnoopPortIpMacBindingEnable_Object = MibTableColumn
dhcpSnoopPortIpMacBindingEnable = _DhcpSnoopPortIpMacBindingEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 1, 1, 1),
    _DhcpSnoopPortIpMacBindingEnable_Type()
)
dhcpSnoopPortIpMacBindingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortIpMacBindingEnable.setStatus("current")


class _DhcpSnoopPortMaxLeaseCount_Type(Integer32):
    """Custom type dhcpSnoopPortMaxLeaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DhcpSnoopPortMaxLeaseCount_Type.__name__ = "Integer32"
_DhcpSnoopPortMaxLeaseCount_Object = MibTableColumn
dhcpSnoopPortMaxLeaseCount = _DhcpSnoopPortMaxLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 1, 1, 2),
    _DhcpSnoopPortMaxLeaseCount_Type()
)
dhcpSnoopPortMaxLeaseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortMaxLeaseCount.setStatus("current")
_DhcpSnoopPortDbFlush_Type = Integer32
_DhcpSnoopPortDbFlush_Object = MibTableColumn
dhcpSnoopPortDbFlush = _DhcpSnoopPortDbFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 1, 1, 3),
    _DhcpSnoopPortDbFlush_Type()
)
dhcpSnoopPortDbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortDbFlush.setStatus("current")


class _DhcpSnoopOverflowMode_Type(Integer32):
    """Custom type dhcpSnoopOverflowMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denynewlease", 1),
          ("removeoldestlease", 2))
    )


_DhcpSnoopOverflowMode_Type.__name__ = "Integer32"
_DhcpSnoopOverflowMode_Object = MibScalar
dhcpSnoopOverflowMode = _DhcpSnoopOverflowMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 2),
    _DhcpSnoopOverflowMode_Type()
)
dhcpSnoopOverflowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOverflowMode.setStatus("current")
_DhcpSnoopDbTable_Object = MibTable
dhcpSnoopDbTable = _DhcpSnoopDbTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3)
)
if mibBuilder.loadTexts:
    dhcpSnoopDbTable.setStatus("current")
_DhcpSnoopDbEntry_Object = MibTableRow
dhcpSnoopDbEntry = _DhcpSnoopDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3, 1)
)
dhcpSnoopDbEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "dhcpSnoopDbIpType"),
    (1, "VES1724-58V-MIB", "dhcpSnoopDbIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopDbEntry.setStatus("current")


class _DhcpSnoopDbIpType_Type(InetAddressType):
    """Custom type dhcpSnoopDbIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_DhcpSnoopDbIpType_Type.__name__ = "InetAddressType"
_DhcpSnoopDbIpType_Object = MibTableColumn
dhcpSnoopDbIpType = _DhcpSnoopDbIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3, 1, 1),
    _DhcpSnoopDbIpType_Type()
)
dhcpSnoopDbIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopDbIpType.setStatus("current")
_DhcpSnoopDbIp_Type = InetAddress
_DhcpSnoopDbIp_Object = MibTableColumn
dhcpSnoopDbIp = _DhcpSnoopDbIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3, 1, 2),
    _DhcpSnoopDbIp_Type()
)
dhcpSnoopDbIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopDbIp.setStatus("current")


class _DhcpSnoopDbVid_Type(VlanIndex):
    """Custom type dhcpSnoopDbVid based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_DhcpSnoopDbVid_Type.__name__ = "VlanIndex"
_DhcpSnoopDbVid_Object = MibTableColumn
dhcpSnoopDbVid = _DhcpSnoopDbVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3, 1, 3),
    _DhcpSnoopDbVid_Type()
)
dhcpSnoopDbVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopDbVid.setStatus("current")
_DhcpSnoopDbMac_Type = PhysAddress
_DhcpSnoopDbMac_Object = MibTableColumn
dhcpSnoopDbMac = _DhcpSnoopDbMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 3, 1, 4),
    _DhcpSnoopDbMac_Type()
)
dhcpSnoopDbMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopDbMac.setStatus("current")
_DhcpSnoopStatsTable_Object = MibTable
dhcpSnoopStatsTable = _DhcpSnoopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpSnoopStatsTable.setStatus("current")
_DhcpSnoopStatsEntry_Object = MibTableRow
dhcpSnoopStatsEntry = _DhcpSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1)
)
dhcpSnoopStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopStatsEntry.setStatus("current")
_DhcpSnoopStatsOverFlow_Type = Counter32
_DhcpSnoopStatsOverFlow_Object = MibTableColumn
dhcpSnoopStatsOverFlow = _DhcpSnoopStatsOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 1),
    _DhcpSnoopStatsOverFlow_Type()
)
dhcpSnoopStatsOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsOverFlow.setStatus("current")
_DhcpSnoopStatsV4Discover_Type = Counter32
_DhcpSnoopStatsV4Discover_Object = MibTableColumn
dhcpSnoopStatsV4Discover = _DhcpSnoopStatsV4Discover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 2),
    _DhcpSnoopStatsV4Discover_Type()
)
dhcpSnoopStatsV4Discover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV4Discover.setStatus("current")
_DhcpSnoopStatsV4Offer_Type = Counter32
_DhcpSnoopStatsV4Offer_Object = MibTableColumn
dhcpSnoopStatsV4Offer = _DhcpSnoopStatsV4Offer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 3),
    _DhcpSnoopStatsV4Offer_Type()
)
dhcpSnoopStatsV4Offer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV4Offer.setStatus("current")
_DhcpSnoopStatsV4Request_Type = Counter32
_DhcpSnoopStatsV4Request_Object = MibTableColumn
dhcpSnoopStatsV4Request = _DhcpSnoopStatsV4Request_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 4),
    _DhcpSnoopStatsV4Request_Type()
)
dhcpSnoopStatsV4Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV4Request.setStatus("current")
_DhcpSnoopStatsV4Ack_Type = Counter32
_DhcpSnoopStatsV4Ack_Object = MibTableColumn
dhcpSnoopStatsV4Ack = _DhcpSnoopStatsV4Ack_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 5),
    _DhcpSnoopStatsV4Ack_Type()
)
dhcpSnoopStatsV4Ack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV4Ack.setStatus("current")
_DhcpSnoopStatsV4Release_Type = Counter32
_DhcpSnoopStatsV4Release_Object = MibTableColumn
dhcpSnoopStatsV4Release = _DhcpSnoopStatsV4Release_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 6),
    _DhcpSnoopStatsV4Release_Type()
)
dhcpSnoopStatsV4Release.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV4Release.setStatus("current")
_DhcpSnoopStatsV6Solicit_Type = Counter32
_DhcpSnoopStatsV6Solicit_Object = MibTableColumn
dhcpSnoopStatsV6Solicit = _DhcpSnoopStatsV6Solicit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 7),
    _DhcpSnoopStatsV6Solicit_Type()
)
dhcpSnoopStatsV6Solicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Solicit.setStatus("current")
_DhcpSnoopStatsV6Advertise_Type = Counter32
_DhcpSnoopStatsV6Advertise_Object = MibTableColumn
dhcpSnoopStatsV6Advertise = _DhcpSnoopStatsV6Advertise_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 8),
    _DhcpSnoopStatsV6Advertise_Type()
)
dhcpSnoopStatsV6Advertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Advertise.setStatus("current")
_DhcpSnoopStatsV6Request_Type = Counter32
_DhcpSnoopStatsV6Request_Object = MibTableColumn
dhcpSnoopStatsV6Request = _DhcpSnoopStatsV6Request_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 9),
    _DhcpSnoopStatsV6Request_Type()
)
dhcpSnoopStatsV6Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Request.setStatus("current")
_DhcpSnoopStatsV6Reply_Type = Counter32
_DhcpSnoopStatsV6Reply_Object = MibTableColumn
dhcpSnoopStatsV6Reply = _DhcpSnoopStatsV6Reply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 10),
    _DhcpSnoopStatsV6Reply_Type()
)
dhcpSnoopStatsV6Reply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Reply.setStatus("current")
_DhcpSnoopStatsV6Renew_Type = Counter32
_DhcpSnoopStatsV6Renew_Object = MibTableColumn
dhcpSnoopStatsV6Renew = _DhcpSnoopStatsV6Renew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 11),
    _DhcpSnoopStatsV6Renew_Type()
)
dhcpSnoopStatsV6Renew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Renew.setStatus("current")
_DhcpSnoopStatsV6Rebind_Type = Counter32
_DhcpSnoopStatsV6Rebind_Object = MibTableColumn
dhcpSnoopStatsV6Rebind = _DhcpSnoopStatsV6Rebind_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 12),
    _DhcpSnoopStatsV6Rebind_Type()
)
dhcpSnoopStatsV6Rebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Rebind.setStatus("current")
_DhcpSnoopStatsV6Release_Type = Counter32
_DhcpSnoopStatsV6Release_Object = MibTableColumn
dhcpSnoopStatsV6Release = _DhcpSnoopStatsV6Release_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 13),
    _DhcpSnoopStatsV6Release_Type()
)
dhcpSnoopStatsV6Release.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6Release.setStatus("current")
_DhcpSnoopStatsV6RelayForward_Type = Counter32
_DhcpSnoopStatsV6RelayForward_Object = MibTableColumn
dhcpSnoopStatsV6RelayForward = _DhcpSnoopStatsV6RelayForward_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 14),
    _DhcpSnoopStatsV6RelayForward_Type()
)
dhcpSnoopStatsV6RelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6RelayForward.setStatus("current")
_DhcpSnoopStatsV6RelayReply_Type = Counter32
_DhcpSnoopStatsV6RelayReply_Object = MibTableColumn
dhcpSnoopStatsV6RelayReply = _DhcpSnoopStatsV6RelayReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 15),
    _DhcpSnoopStatsV6RelayReply_Type()
)
dhcpSnoopStatsV6RelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopStatsV6RelayReply.setStatus("current")
_DhcpSnoopStatsClear_Type = Integer32
_DhcpSnoopStatsClear_Object = MibTableColumn
dhcpSnoopStatsClear = _DhcpSnoopStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 2, 4, 1, 16),
    _DhcpSnoopStatsClear_Type()
)
dhcpSnoopStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopStatsClear.setStatus("current")
_DhcpTest_ObjectIdentity = ObjectIdentity
dhcpTest = _DhcpTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4)
)
_DhcpTestPort_Type = Integer32
_DhcpTestPort_Object = MibScalar
dhcpTestPort = _DhcpTestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 1),
    _DhcpTestPort_Type()
)
dhcpTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestPort.setStatus("current")


class _DhcpTestChannel_Type(Integer32):
    """Custom type dhcpTestChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptm", 1),
          ("atm", 2))
    )


_DhcpTestChannel_Type.__name__ = "Integer32"
_DhcpTestChannel_Object = MibScalar
dhcpTestChannel = _DhcpTestChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 2),
    _DhcpTestChannel_Type()
)
dhcpTestChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestChannel.setStatus("current")


class _DhcpTestUniVlanMode_Type(Integer32):
    """Custom type dhcpTestUniVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2))
    )


_DhcpTestUniVlanMode_Type.__name__ = "Integer32"
_DhcpTestUniVlanMode_Object = MibScalar
dhcpTestUniVlanMode = _DhcpTestUniVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 3),
    _DhcpTestUniVlanMode_Type()
)
dhcpTestUniVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestUniVlanMode.setStatus("current")


class _DhcpTestUniVlan_Type(VlanIndex):
    """Custom type dhcpTestUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_DhcpTestUniVlan_Type.__name__ = "VlanIndex"
_DhcpTestUniVlan_Object = MibScalar
dhcpTestUniVlan = _DhcpTestUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 4),
    _DhcpTestUniVlan_Type()
)
dhcpTestUniVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestUniVlan.setStatus("current")


class _DhcpTestType_Type(Integer32):
    """Custom type dhcpTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v6", 2))
    )


_DhcpTestType_Type.__name__ = "Integer32"
_DhcpTestType_Object = MibScalar
dhcpTestType = _DhcpTestType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 5),
    _DhcpTestType_Type()
)
dhcpTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestType.setStatus("current")
_DhcpTestOps_Type = Integer32
_DhcpTestOps_Object = MibScalar
dhcpTestOps = _DhcpTestOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 6),
    _DhcpTestOps_Type()
)
dhcpTestOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTestOps.setStatus("current")
_DhcpTestStatus_Type = DisplayString
_DhcpTestStatus_Object = MibScalar
dhcpTestStatus = _DhcpTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 3, 4, 7),
    _DhcpTestStatus_Type()
)
dhcpTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpTestStatus.setStatus("current")
_Ge_ObjectIdentity = ObjectIdentity
ge = _Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4)
)
_GeConfTable_Object = MibTable
geConfTable = _GeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1)
)
if mibBuilder.loadTexts:
    geConfTable.setStatus("current")
_GeConfEntry_Object = MibTableRow
geConfEntry = _GeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1)
)
geConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    geConfEntry.setStatus("current")


class _GeConfName_Type(DisplayString):
    """Custom type geConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GeConfName_Type.__name__ = "DisplayString"
_GeConfName_Object = MibTableColumn
geConfName = _GeConfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 1),
    _GeConfName_Type()
)
geConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geConfName.setStatus("current")


class _GeConfSpeedDuplex_Type(Integer32):
    """Custom type geConfSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("halfx10", 2),
          ("fullx10", 3),
          ("halfx100", 4),
          ("fullx100", 5),
          ("fullx1000", 6),
          ("fiberx1000", 7))
    )


_GeConfSpeedDuplex_Type.__name__ = "Integer32"
_GeConfSpeedDuplex_Object = MibTableColumn
geConfSpeedDuplex = _GeConfSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 2),
    _GeConfSpeedDuplex_Type()
)
geConfSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geConfSpeedDuplex.setStatus("current")


class _GeConfAlarmProf_Type(DisplayString):
    """Custom type geConfAlarmProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GeConfAlarmProf_Type.__name__ = "DisplayString"
_GeConfAlarmProf_Object = MibTableColumn
geConfAlarmProf = _GeConfAlarmProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 3),
    _GeConfAlarmProf_Type()
)
geConfAlarmProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geConfAlarmProf.setStatus("current")


class _GeLinkStatus_Type(Integer32):
    """Custom type geLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("linkdown", 1),
          ("halfx10", 2),
          ("fullx10", 3),
          ("halfx100", 4),
          ("fullx100", 5),
          ("fullx1000", 6),
          ("fiberx1000", 7))
    )


_GeLinkStatus_Type.__name__ = "Integer32"
_GeLinkStatus_Object = MibTableColumn
geLinkStatus = _GeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 4),
    _GeLinkStatus_Type()
)
geLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geLinkStatus.setStatus("current")
_GeUtilTxCurrentPercent_Type = Unsigned32
_GeUtilTxCurrentPercent_Object = MibTableColumn
geUtilTxCurrentPercent = _GeUtilTxCurrentPercent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 5),
    _GeUtilTxCurrentPercent_Type()
)
geUtilTxCurrentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geUtilTxCurrentPercent.setStatus("current")
_GeUtilTxCurrentSpeed_Type = Unsigned32
_GeUtilTxCurrentSpeed_Object = MibTableColumn
geUtilTxCurrentSpeed = _GeUtilTxCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 6),
    _GeUtilTxCurrentSpeed_Type()
)
geUtilTxCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geUtilTxCurrentSpeed.setStatus("current")
_GeUtilRxCurrentPercent_Type = Unsigned32
_GeUtilRxCurrentPercent_Object = MibTableColumn
geUtilRxCurrentPercent = _GeUtilRxCurrentPercent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 7),
    _GeUtilRxCurrentPercent_Type()
)
geUtilRxCurrentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geUtilRxCurrentPercent.setStatus("current")
_GeUtilRxCurrentSpeed_Type = Unsigned32
_GeUtilRxCurrentSpeed_Object = MibTableColumn
geUtilRxCurrentSpeed = _GeUtilRxCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 8),
    _GeUtilRxCurrentSpeed_Type()
)
geUtilRxCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geUtilRxCurrentSpeed.setStatus("current")


class _GeUtilTxIssueLvl1Threshold_Type(Unsigned32):
    """Custom type geUtilTxIssueLvl1Threshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeUtilTxIssueLvl1Threshold_Type.__name__ = "Unsigned32"
_GeUtilTxIssueLvl1Threshold_Object = MibTableColumn
geUtilTxIssueLvl1Threshold = _GeUtilTxIssueLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 9),
    _GeUtilTxIssueLvl1Threshold_Type()
)
geUtilTxIssueLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geUtilTxIssueLvl1Threshold.setStatus("current")


class _GeUtilTxIssueLvl2Threshold_Type(Unsigned32):
    """Custom type geUtilTxIssueLvl2Threshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeUtilTxIssueLvl2Threshold_Type.__name__ = "Unsigned32"
_GeUtilTxIssueLvl2Threshold_Object = MibTableColumn
geUtilTxIssueLvl2Threshold = _GeUtilTxIssueLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 10),
    _GeUtilTxIssueLvl2Threshold_Type()
)
geUtilTxIssueLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geUtilTxIssueLvl2Threshold.setStatus("current")


class _GeUtilRxIssueLvl1Threshold_Type(Unsigned32):
    """Custom type geUtilRxIssueLvl1Threshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeUtilRxIssueLvl1Threshold_Type.__name__ = "Unsigned32"
_GeUtilRxIssueLvl1Threshold_Object = MibTableColumn
geUtilRxIssueLvl1Threshold = _GeUtilRxIssueLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 11),
    _GeUtilRxIssueLvl1Threshold_Type()
)
geUtilRxIssueLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geUtilRxIssueLvl1Threshold.setStatus("current")


class _GeUtilRxIssueLvl2Threshold_Type(Unsigned32):
    """Custom type geUtilRxIssueLvl2Threshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeUtilRxIssueLvl2Threshold_Type.__name__ = "Unsigned32"
_GeUtilRxIssueLvl2Threshold_Object = MibTableColumn
geUtilRxIssueLvl2Threshold = _GeUtilRxIssueLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 12),
    _GeUtilRxIssueLvl2Threshold_Type()
)
geUtilRxIssueLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geUtilRxIssueLvl2Threshold.setStatus("current")


class _GeUtilSampleSeconds_Type(Unsigned32):
    """Custom type geUtilSampleSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_GeUtilSampleSeconds_Type.__name__ = "Unsigned32"
_GeUtilSampleSeconds_Object = MibTableColumn
geUtilSampleSeconds = _GeUtilSampleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 1, 1, 13),
    _GeUtilSampleSeconds_Type()
)
geUtilSampleSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geUtilSampleSeconds.setStatus("current")
_GeOps_ObjectIdentity = ObjectIdentity
geOps = _GeOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 2)
)
_GeTarget_Type = PortList
_GeTarget_Object = MibScalar
geTarget = _GeTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 2, 1),
    _GeTarget_Type()
)
geTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geTarget.setStatus("current")


class _GeOperation_Type(Integer32):
    """Custom type geOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clearCurrPerformance", 2),
          ("clearCurr15MinPerformance", 3),
          ("clearHist15MinPerformance", 4),
          ("clearCurr1DayPerformance", 5),
          ("clearHist1DayPerformance", 6))
    )


_GeOperation_Type.__name__ = "Integer32"
_GeOperation_Object = MibScalar
geOperation = _GeOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 2, 2),
    _GeOperation_Type()
)
geOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geOperation.setStatus("current")
_GeDdmiTable_Object = MibTable
geDdmiTable = _GeDdmiTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3)
)
if mibBuilder.loadTexts:
    geDdmiTable.setStatus("current")
_GeDdmiEntry_Object = MibTableRow
geDdmiEntry = _GeDdmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1)
)
geDdmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    geDdmiEntry.setStatus("current")
_GeDdmiTemp_Type = Integer32
_GeDdmiTemp_Object = MibTableColumn
geDdmiTemp = _GeDdmiTemp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1, 1),
    _GeDdmiTemp_Type()
)
geDdmiTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDdmiTemp.setStatus("current")
_GeDdmiVolt_Type = Integer32
_GeDdmiVolt_Object = MibTableColumn
geDdmiVolt = _GeDdmiVolt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1, 2),
    _GeDdmiVolt_Type()
)
geDdmiVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDdmiVolt.setStatus("current")
_GeDdmiTxCurr_Type = Integer32
_GeDdmiTxCurr_Object = MibTableColumn
geDdmiTxCurr = _GeDdmiTxCurr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1, 3),
    _GeDdmiTxCurr_Type()
)
geDdmiTxCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDdmiTxCurr.setStatus("current")
_GeDdmiTxPower_Type = Integer32
_GeDdmiTxPower_Object = MibTableColumn
geDdmiTxPower = _GeDdmiTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1, 4),
    _GeDdmiTxPower_Type()
)
geDdmiTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDdmiTxPower.setStatus("current")
_GeDdmiRxPower_Type = Integer32
_GeDdmiRxPower_Object = MibTableColumn
geDdmiRxPower = _GeDdmiRxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 3, 1, 5),
    _GeDdmiRxPower_Type()
)
geDdmiRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDdmiRxPower.setStatus("current")
_GeSfpInfoTable_Object = MibTable
geSfpInfoTable = _GeSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4)
)
if mibBuilder.loadTexts:
    geSfpInfoTable.setStatus("current")
_GeSfpInfoEntry_Object = MibTableRow
geSfpInfoEntry = _GeSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1)
)
geSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    geSfpInfoEntry.setStatus("current")


class _GeSfpInfoVendor_Type(DisplayString):
    """Custom type geSfpInfoVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GeSfpInfoVendor_Type.__name__ = "DisplayString"
_GeSfpInfoVendor_Object = MibTableColumn
geSfpInfoVendor = _GeSfpInfoVendor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1, 1),
    _GeSfpInfoVendor_Type()
)
geSfpInfoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geSfpInfoVendor.setStatus("current")
_GeSfpInfoVendorPn_Type = DisplayString
_GeSfpInfoVendorPn_Object = MibTableColumn
geSfpInfoVendorPn = _GeSfpInfoVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1, 2),
    _GeSfpInfoVendorPn_Type()
)
geSfpInfoVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geSfpInfoVendorPn.setStatus("current")
_GeSfpInfoVendorRev_Type = DisplayString
_GeSfpInfoVendorRev_Object = MibTableColumn
geSfpInfoVendorRev = _GeSfpInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1, 3),
    _GeSfpInfoVendorRev_Type()
)
geSfpInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geSfpInfoVendorRev.setStatus("current")
_GeSfpInfoVendorSn_Type = DisplayString
_GeSfpInfoVendorSn_Object = MibTableColumn
geSfpInfoVendorSn = _GeSfpInfoVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1, 4),
    _GeSfpInfoVendorSn_Type()
)
geSfpInfoVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geSfpInfoVendorSn.setStatus("current")
_GeSfpInfoDateCode_Type = DisplayString
_GeSfpInfoDateCode_Object = MibTableColumn
geSfpInfoDateCode = _GeSfpInfoDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 4, 4, 1, 5),
    _GeSfpInfoDateCode_Type()
)
geSfpInfoDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geSfpInfoDateCode.setStatus("current")
_Hwmonitor_ObjectIdentity = ObjectIdentity
hwmonitor = _Hwmonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5)
)
_FanConfTable_Object = MibTable
fanConfTable = _FanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 1)
)
if mibBuilder.loadTexts:
    fanConfTable.setStatus("current")
_FanConfEntry_Object = MibTableRow
fanConfEntry = _FanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 1, 1)
)
fanConfEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "fanConfIndex"),
)
if mibBuilder.loadTexts:
    fanConfEntry.setStatus("current")


class _FanConfIndex_Type(Integer32):
    """Custom type fanConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FanConfIndex_Type.__name__ = "Integer32"
_FanConfIndex_Object = MibTableColumn
fanConfIndex = _FanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 1, 1, 1),
    _FanConfIndex_Type()
)
fanConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConfIndex.setStatus("current")


class _FanConfHighThreshold_Type(Integer32):
    """Custom type fanConfHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_FanConfHighThreshold_Type.__name__ = "Integer32"
_FanConfHighThreshold_Object = MibTableColumn
fanConfHighThreshold = _FanConfHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 1, 1, 2),
    _FanConfHighThreshold_Type()
)
fanConfHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanConfHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fanConfHighThreshold.setUnits("RPM")


class _FanConfLowThreshold_Type(Integer32):
    """Custom type fanConfLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_FanConfLowThreshold_Type.__name__ = "Integer32"
_FanConfLowThreshold_Object = MibTableColumn
fanConfLowThreshold = _FanConfLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 1, 1, 3),
    _FanConfLowThreshold_Type()
)
fanConfLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanConfLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fanConfLowThreshold.setUnits("RPM")
_TemperatureConfTable_Object = MibTable
temperatureConfTable = _TemperatureConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 2)
)
if mibBuilder.loadTexts:
    temperatureConfTable.setStatus("current")
_TemperatureConfEntry_Object = MibTableRow
temperatureConfEntry = _TemperatureConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 2, 1)
)
temperatureConfEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
    (0, "VES1724-58V-MIB", "temperatureConfIndex"),
)
if mibBuilder.loadTexts:
    temperatureConfEntry.setStatus("current")


class _TemperatureConfIndex_Type(Integer32):
    """Custom type temperatureConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TemperatureConfIndex_Type.__name__ = "Integer32"
_TemperatureConfIndex_Object = MibTableColumn
temperatureConfIndex = _TemperatureConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 2, 1, 1),
    _TemperatureConfIndex_Type()
)
temperatureConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConfIndex.setStatus("current")


class _TemperatureConfHighThreshold_Type(Integer32):
    """Custom type temperatureConfHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 120),
    )


_TemperatureConfHighThreshold_Type.__name__ = "Integer32"
_TemperatureConfHighThreshold_Object = MibTableColumn
temperatureConfHighThreshold = _TemperatureConfHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 2, 1, 2),
    _TemperatureConfHighThreshold_Type()
)
temperatureConfHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureConfHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    temperatureConfHighThreshold.setUnits("degree Celsius")


class _TemperatureConfLowThreshold_Type(Integer32):
    """Custom type temperatureConfLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 120),
    )


_TemperatureConfLowThreshold_Type.__name__ = "Integer32"
_TemperatureConfLowThreshold_Object = MibTableColumn
temperatureConfLowThreshold = _TemperatureConfLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 2, 1, 3),
    _TemperatureConfLowThreshold_Type()
)
temperatureConfLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureConfLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    temperatureConfLowThreshold.setUnits("degree Celsius")
_VoltageConfTable_Object = MibTable
voltageConfTable = _VoltageConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 3)
)
if mibBuilder.loadTexts:
    voltageConfTable.setStatus("current")
_VoltageConfEntry_Object = MibTableRow
voltageConfEntry = _VoltageConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 3, 1)
)
voltageConfEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
    (0, "VES1724-58V-MIB", "voltageConfIndex"),
)
if mibBuilder.loadTexts:
    voltageConfEntry.setStatus("current")


class _VoltageConfIndex_Type(Integer32):
    """Custom type voltageConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VoltageConfIndex_Type.__name__ = "Integer32"
_VoltageConfIndex_Object = MibTableColumn
voltageConfIndex = _VoltageConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 3, 1, 1),
    _VoltageConfIndex_Type()
)
voltageConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageConfIndex.setStatus("current")


class _VoltageConfHighThreshold_Type(Integer32):
    """Custom type voltageConfHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_VoltageConfHighThreshold_Type.__name__ = "Integer32"
_VoltageConfHighThreshold_Object = MibTableColumn
voltageConfHighThreshold = _VoltageConfHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 3, 1, 2),
    _VoltageConfHighThreshold_Type()
)
voltageConfHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageConfHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    voltageConfHighThreshold.setUnits("mV")


class _VoltageConfLowThreshold_Type(Integer32):
    """Custom type voltageConfLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_VoltageConfLowThreshold_Type.__name__ = "Integer32"
_VoltageConfLowThreshold_Object = MibTableColumn
voltageConfLowThreshold = _VoltageConfLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 3, 1, 3),
    _VoltageConfLowThreshold_Type()
)
voltageConfLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageConfLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    voltageConfLowThreshold.setUnits("mV")
_FanStatsTable_Object = MibTable
fanStatsTable = _FanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4)
)
if mibBuilder.loadTexts:
    fanStatsTable.setStatus("current")
_FanStatsEntry_Object = MibTableRow
fanStatsEntry = _FanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1)
)
fanStatsEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "fanConfIndex"),
)
if mibBuilder.loadTexts:
    fanStatsEntry.setStatus("current")
_FanRpmCurValue_Type = Integer32
_FanRpmCurValue_Object = MibTableColumn
fanRpmCurValue = _FanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1, 1),
    _FanRpmCurValue_Type()
)
fanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmCurValue.setStatus("current")
_FanRpmMaxValue_Type = Integer32
_FanRpmMaxValue_Object = MibTableColumn
fanRpmMaxValue = _FanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1, 2),
    _FanRpmMaxValue_Type()
)
fanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setStatus("current")
_FanRpmMinValue_Type = Integer32
_FanRpmMinValue_Object = MibTableColumn
fanRpmMinValue = _FanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1, 3),
    _FanRpmMinValue_Type()
)
fanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinValue.setStatus("current")
_FanRpmAvgValue_Type = Integer32
_FanRpmAvgValue_Object = MibTableColumn
fanRpmAvgValue = _FanRpmAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1, 4),
    _FanRpmAvgValue_Type()
)
fanRpmAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmAvgValue.setStatus("current")
_FanRpmDescr_Type = DisplayString
_FanRpmDescr_Object = MibTableColumn
fanRpmDescr = _FanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 4, 1, 5),
    _FanRpmDescr_Type()
)
fanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmDescr.setStatus("current")
_TemperatureStatsTable_Object = MibTable
temperatureStatsTable = _TemperatureStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5)
)
if mibBuilder.loadTexts:
    temperatureStatsTable.setStatus("current")
_TemperatureStatsEntry_Object = MibTableRow
temperatureStatsEntry = _TemperatureStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1)
)
temperatureStatsEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
    (0, "VES1724-58V-MIB", "temperatureConfIndex"),
)
if mibBuilder.loadTexts:
    temperatureStatsEntry.setStatus("current")
_TemperatureCurValue_Type = Integer32
_TemperatureCurValue_Object = MibTableColumn
temperatureCurValue = _TemperatureCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1, 1),
    _TemperatureCurValue_Type()
)
temperatureCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCurValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCurValue.setUnits("Celsius")
_TemperatureMaxValue_Type = Integer32
_TemperatureMaxValue_Object = MibTableColumn
temperatureMaxValue = _TemperatureMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1, 2),
    _TemperatureMaxValue_Type()
)
temperatureMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMaxValue.setUnits("Celsius")
_TemperatureMinValue_Type = Integer32
_TemperatureMinValue_Object = MibTableColumn
temperatureMinValue = _TemperatureMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1, 3),
    _TemperatureMinValue_Type()
)
temperatureMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMinValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMinValue.setUnits("Celsius")
_TemperatureAvgValue_Type = Integer32
_TemperatureAvgValue_Object = MibTableColumn
temperatureAvgValue = _TemperatureAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1, 4),
    _TemperatureAvgValue_Type()
)
temperatureAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureAvgValue.setUnits("Celsius")
_TemperatureDescr_Type = DisplayString
_TemperatureDescr_Object = MibTableColumn
temperatureDescr = _TemperatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 5, 1, 5),
    _TemperatureDescr_Type()
)
temperatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDescr.setStatus("current")
_VoltageStatsTable_Object = MibTable
voltageStatsTable = _VoltageStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6)
)
if mibBuilder.loadTexts:
    voltageStatsTable.setStatus("current")
_VoltageStatsEntry_Object = MibTableRow
voltageStatsEntry = _VoltageStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1)
)
voltageStatsEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
    (0, "VES1724-58V-MIB", "voltageConfIndex"),
)
if mibBuilder.loadTexts:
    voltageStatsEntry.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 1),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageCurValue.setUnits("milli-voltage")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 2),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMaxValue.setUnits("milli-voltage")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 3),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageMinValue.setUnits("milli-voltage")
_VoltageAvgValue_Type = Integer32
_VoltageAvgValue_Object = MibTableColumn
voltageAvgValue = _VoltageAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 4),
    _VoltageAvgValue_Type()
)
voltageAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageAvgValue.setUnits("milli-voltage")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageNominalValue.setUnits("milli-voltage")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 6, 1, 6),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")


class _BatterySaving_Type(Bits):
    """Custom type batterySaving based on Bits"""
    namedValues = NamedValues(
        *(("input1", 0),
          ("input2", 1),
          ("input3", 2),
          ("input4", 3))
    )

_BatterySaving_Type.__name__ = "Bits"
_BatterySaving_Object = MibScalar
batterySaving = _BatterySaving_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 7),
    _BatterySaving_Type()
)
batterySaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batterySaving.setStatus("current")
_ExternalBattery_ObjectIdentity = ObjectIdentity
externalBattery = _ExternalBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8)
)
_ExternalBatteryStats_ObjectIdentity = ObjectIdentity
externalBatteryStats = _ExternalBatteryStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 1)
)
_ExternalBatteryStatsTemperature_Type = Integer32
_ExternalBatteryStatsTemperature_Object = MibScalar
externalBatteryStatsTemperature = _ExternalBatteryStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 1, 1),
    _ExternalBatteryStatsTemperature_Type()
)
externalBatteryStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBatteryStatsTemperature.setStatus("current")
_ExternalBatteryStatsVoltage_Type = Integer32
_ExternalBatteryStatsVoltage_Object = MibScalar
externalBatteryStatsVoltage = _ExternalBatteryStatsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 1, 2),
    _ExternalBatteryStatsVoltage_Type()
)
externalBatteryStatsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBatteryStatsVoltage.setStatus("current")
_ExternalBatteryConf_ObjectIdentity = ObjectIdentity
externalBatteryConf = _ExternalBatteryConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2)
)


class _ExternalBatteryConfTempHighThreshold_Type(Integer32):
    """Custom type externalBatteryConfTempHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 50),
    )


_ExternalBatteryConfTempHighThreshold_Type.__name__ = "Integer32"
_ExternalBatteryConfTempHighThreshold_Object = MibScalar
externalBatteryConfTempHighThreshold = _ExternalBatteryConfTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2, 1),
    _ExternalBatteryConfTempHighThreshold_Type()
)
externalBatteryConfTempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalBatteryConfTempHighThreshold.setStatus("current")


class _ExternalBatteryConfTempLowThreshold_Type(Integer32):
    """Custom type externalBatteryConfTempLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 50),
    )


_ExternalBatteryConfTempLowThreshold_Type.__name__ = "Integer32"
_ExternalBatteryConfTempLowThreshold_Object = MibScalar
externalBatteryConfTempLowThreshold = _ExternalBatteryConfTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2, 2),
    _ExternalBatteryConfTempLowThreshold_Type()
)
externalBatteryConfTempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalBatteryConfTempLowThreshold.setStatus("current")
_ExternalBatteryConfDcCriticThreshold_Type = Integer32
_ExternalBatteryConfDcCriticThreshold_Object = MibScalar
externalBatteryConfDcCriticThreshold = _ExternalBatteryConfDcCriticThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2, 3),
    _ExternalBatteryConfDcCriticThreshold_Type()
)
externalBatteryConfDcCriticThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBatteryConfDcCriticThreshold.setStatus("current")
_ExternalBatteryConfDcLowThreshold_Type = Integer32
_ExternalBatteryConfDcLowThreshold_Object = MibScalar
externalBatteryConfDcLowThreshold = _ExternalBatteryConfDcLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2, 4),
    _ExternalBatteryConfDcLowThreshold_Type()
)
externalBatteryConfDcLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBatteryConfDcLowThreshold.setStatus("current")
_ExternalBatteryConfDcErrThreshold_Type = Integer32
_ExternalBatteryConfDcErrThreshold_Object = MibScalar
externalBatteryConfDcErrThreshold = _ExternalBatteryConfDcErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 5, 8, 2, 5),
    _ExternalBatteryConfDcErrThreshold_Type()
)
externalBatteryConfDcErrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBatteryConfDcErrThreshold.setStatus("current")
_Igmpmld_ObjectIdentity = ObjectIdentity
igmpmld = _Igmpmld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6)
)


class _IgmpmldMode_Type(Integer32):
    """Custom type igmpmldMode based on Integer32"""
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
        *(("disable", 0),
          ("transparent", 1),
          ("snooping", 2),
          ("proxy", 3),
          ("proxyReport", 4))
    )


_IgmpmldMode_Type.__name__ = "Integer32"
_IgmpmldMode_Object = MibScalar
igmpmldMode = _IgmpmldMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 1),
    _IgmpmldMode_Type()
)
igmpmldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldMode.setStatus("current")


class _IgmpmldVersion_Type(Integer32):
    """Custom type igmpmldVersion based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 1),
          ("igmpv3", 2),
          ("mldv1", 3),
          ("mldv2", 4),
          ("igmpv2AndMldv1", 5),
          ("igmpv2AndMldv2", 6),
          ("igmpv3AndMldv1", 7),
          ("igmpv3AndMldv2", 8))
    )


_IgmpmldVersion_Type.__name__ = "Integer32"
_IgmpmldVersion_Object = MibScalar
igmpmldVersion = _IgmpmldVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 2),
    _IgmpmldVersion_Type()
)
igmpmldVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldVersion.setStatus("current")


class _IgmpmldLeaveMode_Type(Integer32):
    """Custom type igmpmldLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastLeave", 1),
          ("lastMemberQuery", 2))
    )


_IgmpmldLeaveMode_Type.__name__ = "Integer32"
_IgmpmldLeaveMode_Object = MibScalar
igmpmldLeaveMode = _IgmpmldLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 3),
    _IgmpmldLeaveMode_Type()
)
igmpmldLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldLeaveMode.setStatus("current")


class _IgmpmldLastMemberQueryInterval_Type(Integer32):
    """Custom type igmpmldLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_IgmpmldLastMemberQueryInterval_Type.__name__ = "Integer32"
_IgmpmldLastMemberQueryInterval_Object = MibScalar
igmpmldLastMemberQueryInterval = _IgmpmldLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 4),
    _IgmpmldLastMemberQueryInterval_Type()
)
igmpmldLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldLastMemberQueryInterval.setUnits("ms")


class _IgmpmldLastMemberQueryRobustness_Type(Integer32):
    """Custom type igmpmldLastMemberQueryRobustness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpmldLastMemberQueryRobustness_Type.__name__ = "Integer32"
_IgmpmldLastMemberQueryRobustness_Object = MibScalar
igmpmldLastMemberQueryRobustness = _IgmpmldLastMemberQueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 5),
    _IgmpmldLastMemberQueryRobustness_Type()
)
igmpmldLastMemberQueryRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldLastMemberQueryRobustness.setStatus("current")


class _IgmpmldGeneralQueryInterval_Type(Integer32):
    """Custom type igmpmldGeneralQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IgmpmldGeneralQueryInterval_Type.__name__ = "Integer32"
_IgmpmldGeneralQueryInterval_Object = MibScalar
igmpmldGeneralQueryInterval = _IgmpmldGeneralQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 6),
    _IgmpmldGeneralQueryInterval_Type()
)
igmpmldGeneralQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldGeneralQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGeneralQueryInterval.setUnits("seconds")


class _IgmpmldGeneralQueryRobustness_Type(Integer32):
    """Custom type igmpmldGeneralQueryRobustness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpmldGeneralQueryRobustness_Type.__name__ = "Integer32"
_IgmpmldGeneralQueryRobustness_Object = MibScalar
igmpmldGeneralQueryRobustness = _IgmpmldGeneralQueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 7),
    _IgmpmldGeneralQueryRobustness_Type()
)
igmpmldGeneralQueryRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldGeneralQueryRobustness.setStatus("current")


class _IgmpmldGeneralQueryMaxRespTime_Type(Integer32):
    """Custom type igmpmldGeneralQueryMaxRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IgmpmldGeneralQueryMaxRespTime_Type.__name__ = "Integer32"
_IgmpmldGeneralQueryMaxRespTime_Object = MibScalar
igmpmldGeneralQueryMaxRespTime = _IgmpmldGeneralQueryMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 8),
    _IgmpmldGeneralQueryMaxRespTime_Type()
)
igmpmldGeneralQueryMaxRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldGeneralQueryMaxRespTime.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGeneralQueryMaxRespTime.setUnits("seconds")
_IgmpmldConfPortTable_Object = MibTable
igmpmldConfPortTable = _IgmpmldConfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9)
)
if mibBuilder.loadTexts:
    igmpmldConfPortTable.setStatus("current")
_IgmpmldConfPortEntry_Object = MibTableRow
igmpmldConfPortEntry = _IgmpmldConfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9, 1)
)
igmpmldConfPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpmldConfPortEntry.setStatus("current")


class _IgmpmldConfPortMaxGroupCount_Type(Integer32):
    """Custom type igmpmldConfPortMaxGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IgmpmldConfPortMaxGroupCount_Type.__name__ = "Integer32"
_IgmpmldConfPortMaxGroupCount_Object = MibTableColumn
igmpmldConfPortMaxGroupCount = _IgmpmldConfPortMaxGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9, 1, 1),
    _IgmpmldConfPortMaxGroupCount_Type()
)
igmpmldConfPortMaxGroupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldConfPortMaxGroupCount.setStatus("current")


class _IgmpmldConfPortPrivilegeEnable_Type(Integer32):
    """Custom type igmpmldConfPortPrivilegeEnable based on Integer32"""
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


_IgmpmldConfPortPrivilegeEnable_Type.__name__ = "Integer32"
_IgmpmldConfPortPrivilegeEnable_Object = MibTableColumn
igmpmldConfPortPrivilegeEnable = _IgmpmldConfPortPrivilegeEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9, 1, 2),
    _IgmpmldConfPortPrivilegeEnable_Type()
)
igmpmldConfPortPrivilegeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldConfPortPrivilegeEnable.setStatus("current")


class _IgmpmldConfPortCacEnable_Type(Integer32):
    """Custom type igmpmldConfPortCacEnable based on Integer32"""
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


_IgmpmldConfPortCacEnable_Type.__name__ = "Integer32"
_IgmpmldConfPortCacEnable_Object = MibTableColumn
igmpmldConfPortCacEnable = _IgmpmldConfPortCacEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9, 1, 3),
    _IgmpmldConfPortCacEnable_Type()
)
igmpmldConfPortCacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldConfPortCacEnable.setStatus("current")


class _IgmpmldConfPortCacMaxBandwidth_Type(Integer32):
    """Custom type igmpmldConfPortCacMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IgmpmldConfPortCacMaxBandwidth_Type.__name__ = "Integer32"
_IgmpmldConfPortCacMaxBandwidth_Object = MibTableColumn
igmpmldConfPortCacMaxBandwidth = _IgmpmldConfPortCacMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 9, 1, 4),
    _IgmpmldConfPortCacMaxBandwidth_Type()
)
igmpmldConfPortCacMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldConfPortCacMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldConfPortCacMaxBandwidth.setUnits("Mbps")
_GroupPrivilege_ObjectIdentity = ObjectIdentity
groupPrivilege = _GroupPrivilege_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10)
)
_IgmpmldMaxNumOfGroupPrivilegeProfiles_Type = Integer32
_IgmpmldMaxNumOfGroupPrivilegeProfiles_Object = MibScalar
igmpmldMaxNumOfGroupPrivilegeProfiles = _IgmpmldMaxNumOfGroupPrivilegeProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 1),
    _IgmpmldMaxNumOfGroupPrivilegeProfiles_Type()
)
igmpmldMaxNumOfGroupPrivilegeProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMaxNumOfGroupPrivilegeProfiles.setStatus("current")
_IgmpmldGroupPrivilegeProfileTable_Object = MibTable
igmpmldGroupPrivilegeProfileTable = _IgmpmldGroupPrivilegeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2)
)
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileTable.setStatus("current")
_IgmpmldGroupPrivilegeProfileEntry_Object = MibTableRow
igmpmldGroupPrivilegeProfileEntry = _IgmpmldGroupPrivilegeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1)
)
igmpmldGroupPrivilegeProfileEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "igmpmldGroupPrivilegeProfileName"),
    (0, "VES1724-58V-MIB", "igmpmldGroupPrivilegeProfileIndex"),
)
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileEntry.setStatus("current")


class _IgmpmldGroupPrivilegeProfileName_Type(DisplayString):
    """Custom type igmpmldGroupPrivilegeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpmldGroupPrivilegeProfileName_Type.__name__ = "DisplayString"
_IgmpmldGroupPrivilegeProfileName_Object = MibTableColumn
igmpmldGroupPrivilegeProfileName = _IgmpmldGroupPrivilegeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 1),
    _IgmpmldGroupPrivilegeProfileName_Type()
)
igmpmldGroupPrivilegeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileName.setStatus("current")


class _IgmpmldGroupPrivilegeProfileIndex_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IgmpmldGroupPrivilegeProfileIndex_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfileIndex_Object = MibTableColumn
igmpmldGroupPrivilegeProfileIndex = _IgmpmldGroupPrivilegeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 2),
    _IgmpmldGroupPrivilegeProfileIndex_Type()
)
igmpmldGroupPrivilegeProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileIndex.setStatus("current")


class _IgmpmldGroupPrivilegeProfileAddressType_Type(InetAddressType):
    """Custom type igmpmldGroupPrivilegeProfileAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_IgmpmldGroupPrivilegeProfileAddressType_Type.__name__ = "InetAddressType"
_IgmpmldGroupPrivilegeProfileAddressType_Object = MibTableColumn
igmpmldGroupPrivilegeProfileAddressType = _IgmpmldGroupPrivilegeProfileAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 3),
    _IgmpmldGroupPrivilegeProfileAddressType_Type()
)
igmpmldGroupPrivilegeProfileAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileAddressType.setStatus("current")
_IgmpmldGroupPrivilegeProfileStartIp_Type = InetAddress
_IgmpmldGroupPrivilegeProfileStartIp_Object = MibTableColumn
igmpmldGroupPrivilegeProfileStartIp = _IgmpmldGroupPrivilegeProfileStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 4),
    _IgmpmldGroupPrivilegeProfileStartIp_Type()
)
igmpmldGroupPrivilegeProfileStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileStartIp.setStatus("current")
_IgmpmldGroupPrivilegeProfileEndIp_Type = InetAddress
_IgmpmldGroupPrivilegeProfileEndIp_Object = MibTableColumn
igmpmldGroupPrivilegeProfileEndIp = _IgmpmldGroupPrivilegeProfileEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 5),
    _IgmpmldGroupPrivilegeProfileEndIp_Type()
)
igmpmldGroupPrivilegeProfileEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileEndIp.setStatus("current")


class _IgmpmldGroupPrivilegeProfilePrivilege_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfilePrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forbid", 0),
          ("permit", 1),
          ("preview", 2))
    )


_IgmpmldGroupPrivilegeProfilePrivilege_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfilePrivilege_Object = MibTableColumn
igmpmldGroupPrivilegeProfilePrivilege = _IgmpmldGroupPrivilegeProfilePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 6),
    _IgmpmldGroupPrivilegeProfilePrivilege_Type()
)
igmpmldGroupPrivilegeProfilePrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilege.setStatus("current")


class _IgmpmldGroupPrivilegeProfilePrivilegePreviewLength_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfilePrivilegePreviewLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IgmpmldGroupPrivilegeProfilePrivilegePreviewLength_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfilePrivilegePreviewLength_Object = MibTableColumn
igmpmldGroupPrivilegeProfilePrivilegePreviewLength = _IgmpmldGroupPrivilegeProfilePrivilegePreviewLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 7),
    _IgmpmldGroupPrivilegeProfilePrivilegePreviewLength_Type()
)
igmpmldGroupPrivilegeProfilePrivilegePreviewLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewLength.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewLength.setUnits("seconds")


class _IgmpmldGroupPrivilegeProfilePrivilegePreviewInterval_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfilePrivilegePreviewInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IgmpmldGroupPrivilegeProfilePrivilegePreviewInterval_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfilePrivilegePreviewInterval_Object = MibTableColumn
igmpmldGroupPrivilegeProfilePrivilegePreviewInterval = _IgmpmldGroupPrivilegeProfilePrivilegePreviewInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 8),
    _IgmpmldGroupPrivilegeProfilePrivilegePreviewInterval_Type()
)
igmpmldGroupPrivilegeProfilePrivilegePreviewInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewInterval.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewInterval.setUnits("seconds")


class _IgmpmldGroupPrivilegeProfilePrivilegePreviewCount_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfilePrivilegePreviewCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IgmpmldGroupPrivilegeProfilePrivilegePreviewCount_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfilePrivilegePreviewCount_Object = MibTableColumn
igmpmldGroupPrivilegeProfilePrivilegePreviewCount = _IgmpmldGroupPrivilegeProfilePrivilegePreviewCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 9),
    _IgmpmldGroupPrivilegeProfilePrivilegePreviewCount_Type()
)
igmpmldGroupPrivilegeProfilePrivilegePreviewCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewCount.setStatus("current")


class _IgmpmldGroupPrivilegeProfilePrivilegePreviewReset_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfilePrivilegePreviewReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_IgmpmldGroupPrivilegeProfilePrivilegePreviewReset_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfilePrivilegePreviewReset_Object = MibTableColumn
igmpmldGroupPrivilegeProfilePrivilegePreviewReset = _IgmpmldGroupPrivilegeProfilePrivilegePreviewReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 10),
    _IgmpmldGroupPrivilegeProfilePrivilegePreviewReset_Type()
)
igmpmldGroupPrivilegeProfilePrivilegePreviewReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewReset.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfilePrivilegePreviewReset.setUnits("seconds")


class _IgmpmldGroupPrivilegeProfileCacBandwidth_Type(Integer32):
    """Custom type igmpmldGroupPrivilegeProfileCacBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IgmpmldGroupPrivilegeProfileCacBandwidth_Type.__name__ = "Integer32"
_IgmpmldGroupPrivilegeProfileCacBandwidth_Object = MibTableColumn
igmpmldGroupPrivilegeProfileCacBandwidth = _IgmpmldGroupPrivilegeProfileCacBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 11),
    _IgmpmldGroupPrivilegeProfileCacBandwidth_Type()
)
igmpmldGroupPrivilegeProfileCacBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileCacBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileCacBandwidth.setUnits("Mbps")
_IgmpmldGroupPrivilegeProfileRowStatus_Type = RowStatus
_IgmpmldGroupPrivilegeProfileRowStatus_Object = MibTableColumn
igmpmldGroupPrivilegeProfileRowStatus = _IgmpmldGroupPrivilegeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 2, 1, 12),
    _IgmpmldGroupPrivilegeProfileRowStatus_Type()
)
igmpmldGroupPrivilegeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegeProfileRowStatus.setStatus("current")
_IgmpmldGroupPrivilegePortTable_Object = MibTable
igmpmldGroupPrivilegePortTable = _IgmpmldGroupPrivilegePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 3)
)
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegePortTable.setStatus("current")
_IgmpmldGroupPrivilegePortEntry_Object = MibTableRow
igmpmldGroupPrivilegePortEntry = _IgmpmldGroupPrivilegePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 3, 1)
)
igmpmldGroupPrivilegePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "VES1724-58V-MIB", "igmpmldGroupPrivilegeProfileName"),
)
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegePortEntry.setStatus("current")
_IgmpmldGroupPrivilegePortEntryRowStatus_Type = RowStatus
_IgmpmldGroupPrivilegePortEntryRowStatus_Object = MibTableColumn
igmpmldGroupPrivilegePortEntryRowStatus = _IgmpmldGroupPrivilegePortEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 10, 3, 1, 1),
    _IgmpmldGroupPrivilegePortEntryRowStatus_Type()
)
igmpmldGroupPrivilegePortEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldGroupPrivilegePortEntryRowStatus.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11)
)
_IgmpmldMaxNumOfMvlan_Type = Integer32
_IgmpmldMaxNumOfMvlan_Object = MibScalar
igmpmldMaxNumOfMvlan = _IgmpmldMaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 1),
    _IgmpmldMaxNumOfMvlan_Type()
)
igmpmldMaxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMaxNumOfMvlan.setStatus("current")
_IgmpmldMvlanTable_Object = MibTable
igmpmldMvlanTable = _IgmpmldMvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 2)
)
if mibBuilder.loadTexts:
    igmpmldMvlanTable.setStatus("current")
_IgmpmldMvlanEntry_Object = MibTableRow
igmpmldMvlanEntry = _IgmpmldMvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 2, 1)
)
igmpmldMvlanEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "igmpmldMvlanId"),
)
if mibBuilder.loadTexts:
    igmpmldMvlanEntry.setStatus("current")


class _IgmpmldMvlanId_Type(VlanIndex):
    """Custom type igmpmldMvlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_IgmpmldMvlanId_Type.__name__ = "VlanIndex"
_IgmpmldMvlanId_Object = MibTableColumn
igmpmldMvlanId = _IgmpmldMvlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 2, 1, 1),
    _IgmpmldMvlanId_Type()
)
igmpmldMvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanId.setStatus("current")
_IgmpmldMvlanRowStatus_Type = RowStatus
_IgmpmldMvlanRowStatus_Object = MibTableColumn
igmpmldMvlanRowStatus = _IgmpmldMvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 2, 1, 2),
    _IgmpmldMvlanRowStatus_Type()
)
igmpmldMvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanRowStatus.setStatus("current")


class _IgmpmldMvlanTr101fw_Type(Integer32):
    """Custom type igmpmldMvlanTr101fw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IgmpmldMvlanTr101fw_Type.__name__ = "Integer32"
_IgmpmldMvlanTr101fw_Object = MibTableColumn
igmpmldMvlanTr101fw = _IgmpmldMvlanTr101fw_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 2, 1, 3),
    _IgmpmldMvlanTr101fw_Type()
)
igmpmldMvlanTr101fw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanTr101fw.setStatus("current")
_IgmpmldMvlanPortTable_Object = MibTable
igmpmldMvlanPortTable = _IgmpmldMvlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 3)
)
if mibBuilder.loadTexts:
    igmpmldMvlanPortTable.setStatus("current")
_IgmpmldMvlanPortEntry_Object = MibTableRow
igmpmldMvlanPortEntry = _IgmpmldMvlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 3, 1)
)
igmpmldMvlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "igmpmldMvlanId"),
)
if mibBuilder.loadTexts:
    igmpmldMvlanPortEntry.setStatus("current")


class _IgmpmldMvlanPortEgressType_Type(Integer32):
    """Custom type igmpmldMvlanPortEgressType based on Integer32"""
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
        *(("untag", 1),
          ("tag", 2),
          ("replaceByUniVlan", 3),
          ("transparent", 4))
    )


_IgmpmldMvlanPortEgressType_Type.__name__ = "Integer32"
_IgmpmldMvlanPortEgressType_Object = MibTableColumn
igmpmldMvlanPortEgressType = _IgmpmldMvlanPortEgressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 3, 1, 1),
    _IgmpmldMvlanPortEgressType_Type()
)
igmpmldMvlanPortEgressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanPortEgressType.setStatus("current")


class _IgmpmldMvlanPortUniVlan_Type(VlanIndex):
    """Custom type igmpmldMvlanPortUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_IgmpmldMvlanPortUniVlan_Type.__name__ = "VlanIndex"
_IgmpmldMvlanPortUniVlan_Object = MibTableColumn
igmpmldMvlanPortUniVlan = _IgmpmldMvlanPortUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 3, 1, 2),
    _IgmpmldMvlanPortUniVlan_Type()
)
igmpmldMvlanPortUniVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanPortUniVlan.setStatus("current")
_IgmpmldMvlanPortRowStatus_Type = RowStatus
_IgmpmldMvlanPortRowStatus_Object = MibTableColumn
igmpmldMvlanPortRowStatus = _IgmpmldMvlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 3, 1, 3),
    _IgmpmldMvlanPortRowStatus_Type()
)
igmpmldMvlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanPortRowStatus.setStatus("current")
_IgmpmldMvlanMapTable_Object = MibTable
igmpmldMvlanMapTable = _IgmpmldMvlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4)
)
if mibBuilder.loadTexts:
    igmpmldMvlanMapTable.setStatus("current")
_IgmpmldMvlanMapEntry_Object = MibTableRow
igmpmldMvlanMapEntry = _IgmpmldMvlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4, 1)
)
igmpmldMvlanMapEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "igmpmldMvlanId"),
    (0, "VES1724-58V-MIB", "igmpmldMvlanMapIndex"),
)
if mibBuilder.loadTexts:
    igmpmldMvlanMapEntry.setStatus("current")


class _IgmpmldMvlanMapIndex_Type(Integer32):
    """Custom type igmpmldMvlanMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IgmpmldMvlanMapIndex_Type.__name__ = "Integer32"
_IgmpmldMvlanMapIndex_Object = MibTableColumn
igmpmldMvlanMapIndex = _IgmpmldMvlanMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4, 1, 1),
    _IgmpmldMvlanMapIndex_Type()
)
igmpmldMvlanMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanMapIndex.setStatus("current")
_IgmpmldMvlanMapStartIp_Type = InetAddress
_IgmpmldMvlanMapStartIp_Object = MibTableColumn
igmpmldMvlanMapStartIp = _IgmpmldMvlanMapStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4, 1, 2),
    _IgmpmldMvlanMapStartIp_Type()
)
igmpmldMvlanMapStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanMapStartIp.setStatus("current")
_IgmpmldMvlanMapEndIp_Type = InetAddress
_IgmpmldMvlanMapEndIp_Object = MibTableColumn
igmpmldMvlanMapEndIp = _IgmpmldMvlanMapEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4, 1, 3),
    _IgmpmldMvlanMapEndIp_Type()
)
igmpmldMvlanMapEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanMapEndIp.setStatus("current")
_IgmpmldMvlanMapRowStatus_Type = RowStatus
_IgmpmldMvlanMapRowStatus_Object = MibTableColumn
igmpmldMvlanMapRowStatus = _IgmpmldMvlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 11, 4, 1, 4),
    _IgmpmldMvlanMapRowStatus_Type()
)
igmpmldMvlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpmldMvlanMapRowStatus.setStatus("current")
_Group_ObjectIdentity = ObjectIdentity
group = _Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12)
)
_IgmpmldMvlanGroupTable_Object = MibTable
igmpmldMvlanGroupTable = _IgmpmldMvlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3)
)
if mibBuilder.loadTexts:
    igmpmldMvlanGroupTable.setStatus("current")
_IgmpmldMvlanGroupEntry_Object = MibTableRow
igmpmldMvlanGroupEntry = _IgmpmldMvlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1)
)
igmpmldMvlanGroupEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "igmpmldMvlanGroupId"),
    (0, "VES1724-58V-MIB", "igmpmldMvlanGroupAddressType"),
    (1, "VES1724-58V-MIB", "igmpmldMvlanGroupAddress"),
)
if mibBuilder.loadTexts:
    igmpmldMvlanGroupEntry.setStatus("current")


class _IgmpmldMvlanGroupId_Type(VlanIndex):
    """Custom type igmpmldMvlanGroupId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_IgmpmldMvlanGroupId_Type.__name__ = "VlanIndex"
_IgmpmldMvlanGroupId_Object = MibTableColumn
igmpmldMvlanGroupId = _IgmpmldMvlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 1),
    _IgmpmldMvlanGroupId_Type()
)
igmpmldMvlanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupId.setStatus("current")


class _IgmpmldMvlanGroupAddressType_Type(InetAddressType):
    """Custom type igmpmldMvlanGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_IgmpmldMvlanGroupAddressType_Type.__name__ = "InetAddressType"
_IgmpmldMvlanGroupAddressType_Object = MibTableColumn
igmpmldMvlanGroupAddressType = _IgmpmldMvlanGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 2),
    _IgmpmldMvlanGroupAddressType_Type()
)
igmpmldMvlanGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupAddressType.setStatus("current")
_IgmpmldMvlanGroupAddress_Type = InetAddress
_IgmpmldMvlanGroupAddress_Object = MibTableColumn
igmpmldMvlanGroupAddress = _IgmpmldMvlanGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 3),
    _IgmpmldMvlanGroupAddress_Type()
)
igmpmldMvlanGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupAddress.setStatus("current")
_IgmpmldMvlanGroupNumberOfMembers_Type = Integer32
_IgmpmldMvlanGroupNumberOfMembers_Object = MibTableColumn
igmpmldMvlanGroupNumberOfMembers = _IgmpmldMvlanGroupNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 4),
    _IgmpmldMvlanGroupNumberOfMembers_Type()
)
igmpmldMvlanGroupNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupNumberOfMembers.setStatus("current")
_IgmpmldMvlanGroupNumberOfNewJoinedMembers_Type = Counter32
_IgmpmldMvlanGroupNumberOfNewJoinedMembers_Object = MibTableColumn
igmpmldMvlanGroupNumberOfNewJoinedMembers = _IgmpmldMvlanGroupNumberOfNewJoinedMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 5),
    _IgmpmldMvlanGroupNumberOfNewJoinedMembers_Type()
)
igmpmldMvlanGroupNumberOfNewJoinedMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupNumberOfNewJoinedMembers.setStatus("current")
_IgmpmldMvlanGroupNumberOfLeftMembers_Type = Counter32
_IgmpmldMvlanGroupNumberOfLeftMembers_Object = MibTableColumn
igmpmldMvlanGroupNumberOfLeftMembers = _IgmpmldMvlanGroupNumberOfLeftMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 3, 1, 6),
    _IgmpmldMvlanGroupNumberOfLeftMembers_Type()
)
igmpmldMvlanGroupNumberOfLeftMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupNumberOfLeftMembers.setStatus("current")
_IgmpmldMvlanGroupPortTable_Object = MibTable
igmpmldMvlanGroupPortTable = _IgmpmldMvlanGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4)
)
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortTable.setStatus("current")
_IgmpmldMvlanGroupPortEntry_Object = MibTableRow
igmpmldMvlanGroupPortEntry = _IgmpmldMvlanGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4, 1)
)
igmpmldMvlanGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "igmpmldMvlanGroupId"),
    (0, "VES1724-58V-MIB", "igmpmldMvlanGroupAddressType"),
    (1, "VES1724-58V-MIB", "igmpmldMvlanGroupAddress"),
)
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortEntry.setStatus("current")
_IgmpmldMvlanGroupCreateTime_Type = DisplayString
_IgmpmldMvlanGroupCreateTime_Object = MibTableColumn
igmpmldMvlanGroupCreateTime = _IgmpmldMvlanGroupCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4, 1, 1),
    _IgmpmldMvlanGroupCreateTime_Type()
)
igmpmldMvlanGroupCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupCreateTime.setStatus("current")


class _IgmpmldMvlanGroupPortBandwidth_Type(Integer32):
    """Custom type igmpmldMvlanGroupPortBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IgmpmldMvlanGroupPortBandwidth_Type.__name__ = "Integer32"
_IgmpmldMvlanGroupPortBandwidth_Object = MibTableColumn
igmpmldMvlanGroupPortBandwidth = _IgmpmldMvlanGroupPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4, 1, 2),
    _IgmpmldMvlanGroupPortBandwidth_Type()
)
igmpmldMvlanGroupPortBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortBandwidth.setUnits("Mbps")


class _IgmpmldMvlanGroupPortPrivilege_Type(Integer32):
    """Custom type igmpmldMvlanGroupPortPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forbid", 0),
          ("preview", 1),
          ("permit", 2))
    )


_IgmpmldMvlanGroupPortPrivilege_Type.__name__ = "Integer32"
_IgmpmldMvlanGroupPortPrivilege_Object = MibTableColumn
igmpmldMvlanGroupPortPrivilege = _IgmpmldMvlanGroupPortPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4, 1, 3),
    _IgmpmldMvlanGroupPortPrivilege_Type()
)
igmpmldMvlanGroupPortPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortPrivilege.setStatus("current")


class _IgmpmldMvlanGroupPortState_Type(Integer32):
    """Custom type igmpmldMvlanGroupPortState based on Integer32"""
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
        *(("null", 0),
          ("active", 1),
          ("lastMemberQuery", 2),
          ("preview", 3),
          ("previewLastMemberQuery", 4),
          ("previewForbid", 5))
    )


_IgmpmldMvlanGroupPortState_Type.__name__ = "Integer32"
_IgmpmldMvlanGroupPortState_Object = MibTableColumn
igmpmldMvlanGroupPortState = _IgmpmldMvlanGroupPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 12, 4, 1, 4),
    _IgmpmldMvlanGroupPortState_Type()
)
igmpmldMvlanGroupPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldMvlanGroupPortState.setStatus("current")
_IgmpmldStatistics_ObjectIdentity = ObjectIdentity
igmpmldStatistics = _IgmpmldStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13)
)
_IgmpmldStatisticsRxQuery_Type = Counter32
_IgmpmldStatisticsRxQuery_Object = MibScalar
igmpmldStatisticsRxQuery = _IgmpmldStatisticsRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 1),
    _IgmpmldStatisticsRxQuery_Type()
)
igmpmldStatisticsRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsRxQuery.setStatus("current")
_IgmpmldStatisticstTxQuery_Type = Counter32
_IgmpmldStatisticstTxQuery_Object = MibScalar
igmpmldStatisticstTxQuery = _IgmpmldStatisticstTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 2),
    _IgmpmldStatisticstTxQuery_Type()
)
igmpmldStatisticstTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticstTxQuery.setStatus("current")
_IgmpmldStatisticsRxReport_Type = Counter32
_IgmpmldStatisticsRxReport_Object = MibScalar
igmpmldStatisticsRxReport = _IgmpmldStatisticsRxReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 3),
    _IgmpmldStatisticsRxReport_Type()
)
igmpmldStatisticsRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsRxReport.setStatus("current")
_IgmpmldStatisticsTxReport_Type = Counter32
_IgmpmldStatisticsTxReport_Object = MibScalar
igmpmldStatisticsTxReport = _IgmpmldStatisticsTxReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 4),
    _IgmpmldStatisticsTxReport_Type()
)
igmpmldStatisticsTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsTxReport.setStatus("current")
_IgmpmldStatisticsPortTable_Object = MibTable
igmpmldStatisticsPortTable = _IgmpmldStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5)
)
if mibBuilder.loadTexts:
    igmpmldStatisticsPortTable.setStatus("current")
_IgmpmldStatisticsPortEntry_Object = MibTableRow
igmpmldStatisticsPortEntry = _IgmpmldStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1)
)
igmpmldStatisticsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpmldStatisticsPortEntry.setStatus("current")
_IgmpmldStatisticsPortChannelCreateSuccess_Type = Counter32
_IgmpmldStatisticsPortChannelCreateSuccess_Object = MibTableColumn
igmpmldStatisticsPortChannelCreateSuccess = _IgmpmldStatisticsPortChannelCreateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 1),
    _IgmpmldStatisticsPortChannelCreateSuccess_Type()
)
igmpmldStatisticsPortChannelCreateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortChannelCreateSuccess.setStatus("current")
_IgmpmldStatisticsPortChannelCreateFail_Type = Counter32
_IgmpmldStatisticsPortChannelCreateFail_Object = MibTableColumn
igmpmldStatisticsPortChannelCreateFail = _IgmpmldStatisticsPortChannelCreateFail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 2),
    _IgmpmldStatisticsPortChannelCreateFail_Type()
)
igmpmldStatisticsPortChannelCreateFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortChannelCreateFail.setStatus("current")
_IgmpmldStatisticsPortChannelRemoveLeave_Type = Counter32
_IgmpmldStatisticsPortChannelRemoveLeave_Object = MibTableColumn
igmpmldStatisticsPortChannelRemoveLeave = _IgmpmldStatisticsPortChannelRemoveLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 3),
    _IgmpmldStatisticsPortChannelRemoveLeave_Type()
)
igmpmldStatisticsPortChannelRemoveLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortChannelRemoveLeave.setStatus("current")
_IgmpmldStatisticsPortChannelRemoveTimeout_Type = Counter32
_IgmpmldStatisticsPortChannelRemoveTimeout_Object = MibTableColumn
igmpmldStatisticsPortChannelRemoveTimeout = _IgmpmldStatisticsPortChannelRemoveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 4),
    _IgmpmldStatisticsPortChannelRemoveTimeout_Type()
)
igmpmldStatisticsPortChannelRemoveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortChannelRemoveTimeout.setStatus("current")
_IgmpmldStatisticsPortQueryRx_Type = Counter32
_IgmpmldStatisticsPortQueryRx_Object = MibTableColumn
igmpmldStatisticsPortQueryRx = _IgmpmldStatisticsPortQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 5),
    _IgmpmldStatisticsPortQueryRx_Type()
)
igmpmldStatisticsPortQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortQueryRx.setStatus("current")
_IgmpmldStatisticsPortQueryTx_Type = Counter32
_IgmpmldStatisticsPortQueryTx_Object = MibTableColumn
igmpmldStatisticsPortQueryTx = _IgmpmldStatisticsPortQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 6),
    _IgmpmldStatisticsPortQueryTx_Type()
)
igmpmldStatisticsPortQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortQueryTx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryIgmpv2Tx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryIgmpv2Tx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryIgmpv2Tx = _IgmpmldStatisticsPortGeneralQueryIgmpv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 7),
    _IgmpmldStatisticsPortGeneralQueryIgmpv2Tx_Type()
)
igmpmldStatisticsPortGeneralQueryIgmpv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryIgmpv2Tx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryIgmpv3Tx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryIgmpv3Tx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryIgmpv3Tx = _IgmpmldStatisticsPortGeneralQueryIgmpv3Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 8),
    _IgmpmldStatisticsPortGeneralQueryIgmpv3Tx_Type()
)
igmpmldStatisticsPortGeneralQueryIgmpv3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryIgmpv3Tx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryMldv1Tx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryMldv1Tx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryMldv1Tx = _IgmpmldStatisticsPortGeneralQueryMldv1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 9),
    _IgmpmldStatisticsPortGeneralQueryMldv1Tx_Type()
)
igmpmldStatisticsPortGeneralQueryMldv1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryMldv1Tx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryMldv2Tx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryMldv2Tx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryMldv2Tx = _IgmpmldStatisticsPortGeneralQueryMldv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 10),
    _IgmpmldStatisticsPortGeneralQueryMldv2Tx_Type()
)
igmpmldStatisticsPortGeneralQueryMldv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryMldv2Tx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryIgmpv2Tx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryIgmpv2Tx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryIgmpv2Tx = _IgmpmldStatisticsPortSpecificQueryIgmpv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 11),
    _IgmpmldStatisticsPortSpecificQueryIgmpv2Tx_Type()
)
igmpmldStatisticsPortSpecificQueryIgmpv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryIgmpv2Tx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryIgmpv3Tx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryIgmpv3Tx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryIgmpv3Tx = _IgmpmldStatisticsPortSpecificQueryIgmpv3Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 12),
    _IgmpmldStatisticsPortSpecificQueryIgmpv3Tx_Type()
)
igmpmldStatisticsPortSpecificQueryIgmpv3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryIgmpv3Tx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryMldv1Tx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryMldv1Tx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryMldv1Tx = _IgmpmldStatisticsPortSpecificQueryMldv1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 14),
    _IgmpmldStatisticsPortSpecificQueryMldv1Tx_Type()
)
igmpmldStatisticsPortSpecificQueryMldv1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryMldv1Tx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryMldv2Tx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryMldv2Tx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryMldv2Tx = _IgmpmldStatisticsPortSpecificQueryMldv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 15),
    _IgmpmldStatisticsPortSpecificQueryMldv2Tx_Type()
)
igmpmldStatisticsPortSpecificQueryMldv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryMldv2Tx.setStatus("current")
_IgmpmldStatisticsPortReportRx_Type = Counter32
_IgmpmldStatisticsPortReportRx_Object = MibTableColumn
igmpmldStatisticsPortReportRx = _IgmpmldStatisticsPortReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 16),
    _IgmpmldStatisticsPortReportRx_Type()
)
igmpmldStatisticsPortReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportRx.setStatus("current")
_IgmpmldStatisticsPortReportTx_Type = Counter32
_IgmpmldStatisticsPortReportTx_Object = MibTableColumn
igmpmldStatisticsPortReportTx = _IgmpmldStatisticsPortReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 17),
    _IgmpmldStatisticsPortReportTx_Type()
)
igmpmldStatisticsPortReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportTx.setStatus("current")
_IgmpmldStatisticsPortReportJoinIgmpv2Rx_Type = Counter32
_IgmpmldStatisticsPortReportJoinIgmpv2Rx_Object = MibTableColumn
igmpmldStatisticsPortReportJoinIgmpv2Rx = _IgmpmldStatisticsPortReportJoinIgmpv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 18),
    _IgmpmldStatisticsPortReportJoinIgmpv2Rx_Type()
)
igmpmldStatisticsPortReportJoinIgmpv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportJoinIgmpv2Rx.setStatus("current")
_IgmpmldStatisticsPortReportLeaveIgmpv2Rx_Type = Counter32
_IgmpmldStatisticsPortReportLeaveIgmpv2Rx_Object = MibTableColumn
igmpmldStatisticsPortReportLeaveIgmpv2Rx = _IgmpmldStatisticsPortReportLeaveIgmpv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 19),
    _IgmpmldStatisticsPortReportLeaveIgmpv2Rx_Type()
)
igmpmldStatisticsPortReportLeaveIgmpv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportLeaveIgmpv2Rx.setStatus("current")
_IgmpmldStatisticsPortReportDropIgmp_Type = Counter32
_IgmpmldStatisticsPortReportDropIgmp_Object = MibTableColumn
igmpmldStatisticsPortReportDropIgmp = _IgmpmldStatisticsPortReportDropIgmp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 20),
    _IgmpmldStatisticsPortReportDropIgmp_Type()
)
igmpmldStatisticsPortReportDropIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportDropIgmp.setStatus("current")


class _IgmpmldStatisticsPortCompatibleMode_Type(Integer32):
    """Custom type igmpmldStatisticsPortCompatibleMode based on Integer32"""
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
        *(("none", 0),
          ("igmpOnly", 1),
          ("mldOnly", 2),
          ("igmpAndMld", 3))
    )


_IgmpmldStatisticsPortCompatibleMode_Type.__name__ = "Integer32"
_IgmpmldStatisticsPortCompatibleMode_Object = MibTableColumn
igmpmldStatisticsPortCompatibleMode = _IgmpmldStatisticsPortCompatibleMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 21),
    _IgmpmldStatisticsPortCompatibleMode_Type()
)
igmpmldStatisticsPortCompatibleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortCompatibleMode.setStatus("current")
_IgmpmldStatisticsPortReportJoinMldv1Rx_Type = Counter32
_IgmpmldStatisticsPortReportJoinMldv1Rx_Object = MibTableColumn
igmpmldStatisticsPortReportJoinMldv1Rx = _IgmpmldStatisticsPortReportJoinMldv1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 22),
    _IgmpmldStatisticsPortReportJoinMldv1Rx_Type()
)
igmpmldStatisticsPortReportJoinMldv1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportJoinMldv1Rx.setStatus("current")
_IgmpmldStatisticsPortReportLeaveMldv1Rx_Type = Counter32
_IgmpmldStatisticsPortReportLeaveMldv1Rx_Object = MibTableColumn
igmpmldStatisticsPortReportLeaveMldv1Rx = _IgmpmldStatisticsPortReportLeaveMldv1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 23),
    _IgmpmldStatisticsPortReportLeaveMldv1Rx_Type()
)
igmpmldStatisticsPortReportLeaveMldv1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportLeaveMldv1Rx.setStatus("current")
_IgmpmldStatisticsPortReportDropMld_Type = Counter32
_IgmpmldStatisticsPortReportDropMld_Object = MibTableColumn
igmpmldStatisticsPortReportDropMld = _IgmpmldStatisticsPortReportDropMld_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 24),
    _IgmpmldStatisticsPortReportDropMld_Type()
)
igmpmldStatisticsPortReportDropMld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportDropMld.setStatus("current")
_IgmpmldStatisticsPortReportIgmpv3Rx_Type = Counter32
_IgmpmldStatisticsPortReportIgmpv3Rx_Object = MibTableColumn
igmpmldStatisticsPortReportIgmpv3Rx = _IgmpmldStatisticsPortReportIgmpv3Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 25),
    _IgmpmldStatisticsPortReportIgmpv3Rx_Type()
)
igmpmldStatisticsPortReportIgmpv3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportIgmpv3Rx.setStatus("current")
_IgmpmldStatisticsPortReportMldv2Rx_Type = Counter32
_IgmpmldStatisticsPortReportMldv2Rx_Object = MibTableColumn
igmpmldStatisticsPortReportMldv2Rx = _IgmpmldStatisticsPortReportMldv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 26),
    _IgmpmldStatisticsPortReportMldv2Rx_Type()
)
igmpmldStatisticsPortReportMldv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportMldv2Rx.setStatus("current")
_IgmpmldStatisticsPortQueryDropIgmp_Type = Counter32
_IgmpmldStatisticsPortQueryDropIgmp_Object = MibTableColumn
igmpmldStatisticsPortQueryDropIgmp = _IgmpmldStatisticsPortQueryDropIgmp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 27),
    _IgmpmldStatisticsPortQueryDropIgmp_Type()
)
igmpmldStatisticsPortQueryDropIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortQueryDropIgmp.setStatus("current")
_IgmpmldStatisticsPortQueryDropMld_Type = Counter32
_IgmpmldStatisticsPortQueryDropMld_Object = MibTableColumn
igmpmldStatisticsPortQueryDropMld = _IgmpmldStatisticsPortQueryDropMld_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 28),
    _IgmpmldStatisticsPortQueryDropMld_Type()
)
igmpmldStatisticsPortQueryDropMld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortQueryDropMld.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryIgmpv2Rx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryIgmpv2Rx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryIgmpv2Rx = _IgmpmldStatisticsPortGeneralQueryIgmpv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 29),
    _IgmpmldStatisticsPortGeneralQueryIgmpv2Rx_Type()
)
igmpmldStatisticsPortGeneralQueryIgmpv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryIgmpv2Rx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryIgmpv3Rx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryIgmpv3Rx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryIgmpv3Rx = _IgmpmldStatisticsPortGeneralQueryIgmpv3Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 30),
    _IgmpmldStatisticsPortGeneralQueryIgmpv3Rx_Type()
)
igmpmldStatisticsPortGeneralQueryIgmpv3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryIgmpv3Rx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryMldv1Rx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryMldv1Rx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryMldv1Rx = _IgmpmldStatisticsPortGeneralQueryMldv1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 31),
    _IgmpmldStatisticsPortGeneralQueryMldv1Rx_Type()
)
igmpmldStatisticsPortGeneralQueryMldv1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryMldv1Rx.setStatus("current")
_IgmpmldStatisticsPortGeneralQueryMldv2Rx_Type = Counter32
_IgmpmldStatisticsPortGeneralQueryMldv2Rx_Object = MibTableColumn
igmpmldStatisticsPortGeneralQueryMldv2Rx = _IgmpmldStatisticsPortGeneralQueryMldv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 32),
    _IgmpmldStatisticsPortGeneralQueryMldv2Rx_Type()
)
igmpmldStatisticsPortGeneralQueryMldv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortGeneralQueryMldv2Rx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryIgmpv2Rx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryIgmpv2Rx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryIgmpv2Rx = _IgmpmldStatisticsPortSpecificQueryIgmpv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 33),
    _IgmpmldStatisticsPortSpecificQueryIgmpv2Rx_Type()
)
igmpmldStatisticsPortSpecificQueryIgmpv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryIgmpv2Rx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryIgmpv3Rx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryIgmpv3Rx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryIgmpv3Rx = _IgmpmldStatisticsPortSpecificQueryIgmpv3Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 34),
    _IgmpmldStatisticsPortSpecificQueryIgmpv3Rx_Type()
)
igmpmldStatisticsPortSpecificQueryIgmpv3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryIgmpv3Rx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryMldv1Rx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryMldv1Rx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryMldv1Rx = _IgmpmldStatisticsPortSpecificQueryMldv1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 35),
    _IgmpmldStatisticsPortSpecificQueryMldv1Rx_Type()
)
igmpmldStatisticsPortSpecificQueryMldv1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryMldv1Rx.setStatus("current")
_IgmpmldStatisticsPortSpecificQueryMldv2Rx_Type = Counter32
_IgmpmldStatisticsPortSpecificQueryMldv2Rx_Object = MibTableColumn
igmpmldStatisticsPortSpecificQueryMldv2Rx = _IgmpmldStatisticsPortSpecificQueryMldv2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 36),
    _IgmpmldStatisticsPortSpecificQueryMldv2Rx_Type()
)
igmpmldStatisticsPortSpecificQueryMldv2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortSpecificQueryMldv2Rx.setStatus("current")
_IgmpmldStatisticsPortReportJoinIgmpv2Tx_Type = Counter32
_IgmpmldStatisticsPortReportJoinIgmpv2Tx_Object = MibTableColumn
igmpmldStatisticsPortReportJoinIgmpv2Tx = _IgmpmldStatisticsPortReportJoinIgmpv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 37),
    _IgmpmldStatisticsPortReportJoinIgmpv2Tx_Type()
)
igmpmldStatisticsPortReportJoinIgmpv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportJoinIgmpv2Tx.setStatus("current")
_IgmpmldStatisticsPortReportLeaveIgmpv2Tx_Type = Counter32
_IgmpmldStatisticsPortReportLeaveIgmpv2Tx_Object = MibTableColumn
igmpmldStatisticsPortReportLeaveIgmpv2Tx = _IgmpmldStatisticsPortReportLeaveIgmpv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 38),
    _IgmpmldStatisticsPortReportLeaveIgmpv2Tx_Type()
)
igmpmldStatisticsPortReportLeaveIgmpv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportLeaveIgmpv2Tx.setStatus("current")
_IgmpmldStatisticsPortReportJoinMldv1Tx_Type = Counter32
_IgmpmldStatisticsPortReportJoinMldv1Tx_Object = MibTableColumn
igmpmldStatisticsPortReportJoinMldv1Tx = _IgmpmldStatisticsPortReportJoinMldv1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 39),
    _IgmpmldStatisticsPortReportJoinMldv1Tx_Type()
)
igmpmldStatisticsPortReportJoinMldv1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportJoinMldv1Tx.setStatus("current")
_IgmpmldStatisticsPortReportLeaveMldv1Tx_Type = Counter32
_IgmpmldStatisticsPortReportLeaveMldv1Tx_Object = MibTableColumn
igmpmldStatisticsPortReportLeaveMldv1Tx = _IgmpmldStatisticsPortReportLeaveMldv1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 40),
    _IgmpmldStatisticsPortReportLeaveMldv1Tx_Type()
)
igmpmldStatisticsPortReportLeaveMldv1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportLeaveMldv1Tx.setStatus("current")
_IgmpmldStatisticsPortReportIgmpv3Tx_Type = Counter32
_IgmpmldStatisticsPortReportIgmpv3Tx_Object = MibTableColumn
igmpmldStatisticsPortReportIgmpv3Tx = _IgmpmldStatisticsPortReportIgmpv3Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 41),
    _IgmpmldStatisticsPortReportIgmpv3Tx_Type()
)
igmpmldStatisticsPortReportIgmpv3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportIgmpv3Tx.setStatus("current")
_IgmpmldStatisticsPortReportMldv2Tx_Type = Counter32
_IgmpmldStatisticsPortReportMldv2Tx_Object = MibTableColumn
igmpmldStatisticsPortReportMldv2Tx = _IgmpmldStatisticsPortReportMldv2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 13, 5, 1, 42),
    _IgmpmldStatisticsPortReportMldv2Tx_Type()
)
igmpmldStatisticsPortReportMldv2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldStatisticsPortReportMldv2Tx.setStatus("current")
_IgmpmldLogs_ObjectIdentity = ObjectIdentity
igmpmldLogs = _IgmpmldLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14)
)
_IgmpmldLogsPortTable_Object = MibTable
igmpmldLogsPortTable = _IgmpmldLogsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1)
)
if mibBuilder.loadTexts:
    igmpmldLogsPortTable.setStatus("current")
_IgmpmldLogsPortEntry_Object = MibTableRow
igmpmldLogsPortEntry = _IgmpmldLogsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1)
)
igmpmldLogsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "igmpmldLogsPortTime"),
    (0, "VES1724-58V-MIB", "igmpmldLogsPortSerialNo"),
)
if mibBuilder.loadTexts:
    igmpmldLogsPortEntry.setStatus("current")
_IgmpmldLogsPortTime_Type = Unsigned32
_IgmpmldLogsPortTime_Object = MibTableColumn
igmpmldLogsPortTime = _IgmpmldLogsPortTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1, 1),
    _IgmpmldLogsPortTime_Type()
)
igmpmldLogsPortTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldLogsPortTime.setStatus("current")
_IgmpmldLogsPortSerialNo_Type = Integer32
_IgmpmldLogsPortSerialNo_Object = MibTableColumn
igmpmldLogsPortSerialNo = _IgmpmldLogsPortSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1, 2),
    _IgmpmldLogsPortSerialNo_Type()
)
igmpmldLogsPortSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldLogsPortSerialNo.setStatus("current")


class _IgmpmldLogsPortEvent_Type(Integer32):
    """Custom type igmpmldLogsPortEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("join", 0),
          ("leave", 1),
          ("drop", 2))
    )


_IgmpmldLogsPortEvent_Type.__name__ = "Integer32"
_IgmpmldLogsPortEvent_Object = MibTableColumn
igmpmldLogsPortEvent = _IgmpmldLogsPortEvent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1, 3),
    _IgmpmldLogsPortEvent_Type()
)
igmpmldLogsPortEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldLogsPortEvent.setStatus("current")


class _IgmpmldLogsPortGroupAddressType_Type(InetAddressType):
    """Custom type igmpmldLogsPortGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_IgmpmldLogsPortGroupAddressType_Type.__name__ = "InetAddressType"
_IgmpmldLogsPortGroupAddressType_Object = MibTableColumn
igmpmldLogsPortGroupAddressType = _IgmpmldLogsPortGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1, 4),
    _IgmpmldLogsPortGroupAddressType_Type()
)
igmpmldLogsPortGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldLogsPortGroupAddressType.setStatus("current")
_IgmpmldLogsPortGroupAddress_Type = InetAddress
_IgmpmldLogsPortGroupAddress_Object = MibTableColumn
igmpmldLogsPortGroupAddress = _IgmpmldLogsPortGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 14, 1, 1, 5),
    _IgmpmldLogsPortGroupAddress_Type()
)
igmpmldLogsPortGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpmldLogsPortGroupAddress.setStatus("current")
_IgmpmldOps_ObjectIdentity = ObjectIdentity
igmpmldOps = _IgmpmldOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 15)
)
_IgmpmldTarget_Type = PortList
_IgmpmldTarget_Object = MibScalar
igmpmldTarget = _IgmpmldTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 15, 1),
    _IgmpmldTarget_Type()
)
igmpmldTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldTarget.setStatus("current")


class _IgmpmldOperation_Type(Integer32):
    """Custom type igmpmldOperation based on Integer32"""
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
        *(("clearIGMPMLDPacketStatistics", 1),
          ("clearIGMPMLDPacketStatisticsOnSpecifiedUNIPorts", 2),
          ("clearIGMPMLDLogOnSpecifiedUNIPorts", 3),
          ("clearIGMPMLDPacketStatisticsOnSpecifiedNNIPorts", 4))
    )


_IgmpmldOperation_Type.__name__ = "Integer32"
_IgmpmldOperation_Object = MibScalar
igmpmldOperation = _IgmpmldOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 15, 2),
    _IgmpmldOperation_Type()
)
igmpmldOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldOperation.setStatus("current")


class _IgmpmldPbit_Type(Integer32):
    """Custom type igmpmldPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IgmpmldPbit_Type.__name__ = "Integer32"
_IgmpmldPbit_Object = MibScalar
igmpmldPbit = _IgmpmldPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 16),
    _IgmpmldPbit_Type()
)
igmpmldPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpmldPbit.setStatus("current")
_IgmpmldTest_ObjectIdentity = ObjectIdentity
igmpmldTest = _IgmpmldTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 6, 17)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7)
)
_IpArp_ObjectIdentity = ObjectIdentity
ipArp = _IpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1)
)


class _IpArpOps_Type(Integer32):
    """Custom type ipArpOps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("flushTheARPxTableEntries", 1)
    )


_IpArpOps_Type.__name__ = "Integer32"
_IpArpOps_Object = MibScalar
ipArpOps = _IpArpOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 1),
    _IpArpOps_Type()
)
ipArpOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipArpOps.setStatus("current")
_IpArpTable_Object = MibTable
ipArpTable = _IpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ipArpTable.setStatus("current")
_IpArpEntry_Object = MibTableRow
ipArpEntry = _IpArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 2, 1)
)
ipArpEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipAddress"),
)
if mibBuilder.loadTexts:
    ipArpEntry.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 2, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_MacAddress_Type = PhysAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 2, 1, 2),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_IpInterface_Type = DisplayString
_IpInterface_Object = MibTableColumn
ipInterface = _IpInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 1, 2, 1, 3),
    _IpInterface_Type()
)
ipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterface.setStatus("current")
_IpInband_ObjectIdentity = ObjectIdentity
ipInband = _IpInband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2)
)
_IpInbandAddress_Type = IpAddress
_IpInbandAddress_Object = MibScalar
ipInbandAddress = _IpInbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 1),
    _IpInbandAddress_Type()
)
ipInbandAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandAddress.setStatus("current")


class _IpInbandNetmask_Type(Integer32):
    """Custom type ipInbandNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IpInbandNetmask_Type.__name__ = "Integer32"
_IpInbandNetmask_Object = MibScalar
ipInbandNetmask = _IpInbandNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 2),
    _IpInbandNetmask_Type()
)
ipInbandNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandNetmask.setStatus("current")


class _IpInbandMgmtVlan_Type(VlanIndex):
    """Custom type ipInbandMgmtVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_IpInbandMgmtVlan_Type.__name__ = "VlanIndex"
_IpInbandMgmtVlan_Object = MibScalar
ipInbandMgmtVlan = _IpInbandMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 3),
    _IpInbandMgmtVlan_Type()
)
ipInbandMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandMgmtVlan.setStatus("current")
_IpInbandGateway_Type = IpAddress
_IpInbandGateway_Object = MibScalar
ipInbandGateway = _IpInbandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 4),
    _IpInbandGateway_Type()
)
ipInbandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandGateway.setStatus("current")
_Ipv6InbandAddress_Type = InetAddress
_Ipv6InbandAddress_Object = MibScalar
ipv6InbandAddress = _Ipv6InbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 5),
    _Ipv6InbandAddress_Type()
)
ipv6InbandAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6InbandAddress.setStatus("current")


class _Ipv6InbandNetmask_Type(Integer32):
    """Custom type ipv6InbandNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ipv6InbandNetmask_Type.__name__ = "Integer32"
_Ipv6InbandNetmask_Object = MibScalar
ipv6InbandNetmask = _Ipv6InbandNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 6),
    _Ipv6InbandNetmask_Type()
)
ipv6InbandNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6InbandNetmask.setStatus("current")
_Ipv6InbandGateway_Type = InetAddress
_Ipv6InbandGateway_Object = MibScalar
ipv6InbandGateway = _Ipv6InbandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 7),
    _Ipv6InbandGateway_Type()
)
ipv6InbandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6InbandGateway.setStatus("current")


class _IpInbandDhcpBootpEnable_Type(Integer32):
    """Custom type ipInbandDhcpBootpEnable based on Integer32"""
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


_IpInbandDhcpBootpEnable_Type.__name__ = "Integer32"
_IpInbandDhcpBootpEnable_Object = MibScalar
ipInbandDhcpBootpEnable = _IpInbandDhcpBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 8),
    _IpInbandDhcpBootpEnable_Type()
)
ipInbandDhcpBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandDhcpBootpEnable.setStatus("current")


class _IpInbandDhcpOperation_Type(Integer32):
    """Custom type ipInbandDhcpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 1),
          ("renew", 2))
    )


_IpInbandDhcpOperation_Type.__name__ = "Integer32"
_IpInbandDhcpOperation_Object = MibScalar
ipInbandDhcpOperation = _IpInbandDhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 9),
    _IpInbandDhcpOperation_Type()
)
ipInbandDhcpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandDhcpOperation.setStatus("current")


class _IpInbandMgmtPbit_Type(Integer32):
    """Custom type ipInbandMgmtPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpInbandMgmtPbit_Type.__name__ = "Integer32"
_IpInbandMgmtPbit_Object = MibScalar
ipInbandMgmtPbit = _IpInbandMgmtPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 10),
    _IpInbandMgmtPbit_Type()
)
ipInbandMgmtPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInbandMgmtPbit.setStatus("current")
_Ipv6InbandLinkLocalAddress_Type = InetAddress
_Ipv6InbandLinkLocalAddress_Object = MibScalar
ipv6InbandLinkLocalAddress = _Ipv6InbandLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 2, 11),
    _Ipv6InbandLinkLocalAddress_Type()
)
ipv6InbandLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InbandLinkLocalAddress.setStatus("current")
_IpOutband_ObjectIdentity = ObjectIdentity
ipOutband = _IpOutband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3)
)
_IpOutbandAddress_Type = IpAddress
_IpOutbandAddress_Object = MibScalar
ipOutbandAddress = _IpOutbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3, 1),
    _IpOutbandAddress_Type()
)
ipOutbandAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipOutbandAddress.setStatus("current")


class _IpOutbandNetmask_Type(Integer32):
    """Custom type ipOutbandNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IpOutbandNetmask_Type.__name__ = "Integer32"
_IpOutbandNetmask_Object = MibScalar
ipOutbandNetmask = _IpOutbandNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3, 2),
    _IpOutbandNetmask_Type()
)
ipOutbandNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipOutbandNetmask.setStatus("current")
_Ipv6OutbandAddress_Type = InetAddress
_Ipv6OutbandAddress_Object = MibScalar
ipv6OutbandAddress = _Ipv6OutbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3, 3),
    _Ipv6OutbandAddress_Type()
)
ipv6OutbandAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6OutbandAddress.setStatus("current")


class _Ipv6OutbandNetmask_Type(Integer32):
    """Custom type ipv6OutbandNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ipv6OutbandNetmask_Type.__name__ = "Integer32"
_Ipv6OutbandNetmask_Object = MibScalar
ipv6OutbandNetmask = _Ipv6OutbandNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3, 4),
    _Ipv6OutbandNetmask_Type()
)
ipv6OutbandNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6OutbandNetmask.setStatus("current")
_Ipv6OutbandLinkLocalAddress_Type = InetAddress
_Ipv6OutbandLinkLocalAddress_Object = MibScalar
ipv6OutbandLinkLocalAddress = _Ipv6OutbandLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 3, 5),
    _Ipv6OutbandLinkLocalAddress_Type()
)
ipv6OutbandLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6OutbandLinkLocalAddress.setStatus("current")


class _Ipv6DefaultMgmt_Type(Integer32):
    """Custom type ipv6DefaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outband", 2))
    )


_Ipv6DefaultMgmt_Type.__name__ = "Integer32"
_Ipv6DefaultMgmt_Object = MibScalar
ipv6DefaultMgmt = _Ipv6DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 4),
    _Ipv6DefaultMgmt_Type()
)
ipv6DefaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultMgmt.setStatus("current")
_IpRoute_ObjectIdentity = ObjectIdentity
ipRoute = _IpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5)
)
_IpMaxNumOfStaticRoutes_Type = Integer32
_IpMaxNumOfStaticRoutes_Object = MibScalar
ipMaxNumOfStaticRoutes = _IpMaxNumOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 1),
    _IpMaxNumOfStaticRoutes_Type()
)
ipMaxNumOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMaxNumOfStaticRoutes.setStatus("current")
_IpStaticRouteTable_Object = MibTable
ipStaticRouteTable = _IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2)
)
if mibBuilder.loadTexts:
    ipStaticRouteTable.setStatus("current")
_IpStaticRouteEntry_Object = MibTableRow
ipStaticRouteEntry = _IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1)
)
ipStaticRouteEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipStaticRouteDest"),
    (0, "VES1724-58V-MIB", "ipStaticRouteMask"),
)
if mibBuilder.loadTexts:
    ipStaticRouteEntry.setStatus("current")
_IpStaticRouteDest_Type = IpAddress
_IpStaticRouteDest_Object = MibTableColumn
ipStaticRouteDest = _IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1, 1),
    _IpStaticRouteDest_Type()
)
ipStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteDest.setStatus("current")


class _IpStaticRouteMask_Type(Integer32):
    """Custom type ipStaticRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpStaticRouteMask_Type.__name__ = "Integer32"
_IpStaticRouteMask_Object = MibTableColumn
ipStaticRouteMask = _IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1, 2),
    _IpStaticRouteMask_Type()
)
ipStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteMask.setStatus("current")
_IpStaticRouteNextHop_Type = IpAddress
_IpStaticRouteNextHop_Object = MibTableColumn
ipStaticRouteNextHop = _IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1, 3),
    _IpStaticRouteNextHop_Type()
)
ipStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStaticRouteNextHop.setStatus("current")
_IpStaticRouteRowStatus_Type = RowStatus
_IpStaticRouteRowStatus_Object = MibTableColumn
ipStaticRouteRowStatus = _IpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1, 4),
    _IpStaticRouteRowStatus_Type()
)
ipStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStaticRouteRowStatus.setStatus("current")
_IpStaticRouteIfName_Type = DisplayString
_IpStaticRouteIfName_Object = MibTableColumn
ipStaticRouteIfName = _IpStaticRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 2, 1, 5),
    _IpStaticRouteIfName_Type()
)
ipStaticRouteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteIfName.setStatus("current")
_IpRouteTable_Object = MibTable
ipRouteTable = _IpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3)
)
if mibBuilder.loadTexts:
    ipRouteTable.setStatus("current")
_IpRouteEntry_Object = MibTableRow
ipRouteEntry = _IpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3, 1)
)
ipRouteEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipRouteDest"),
    (0, "VES1724-58V-MIB", "ipRouteMask"),
)
if mibBuilder.loadTexts:
    ipRouteEntry.setStatus("current")
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibTableColumn
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3, 1, 1),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("current")


class _IpRouteMask_Type(Integer32):
    """Custom type ipRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpRouteMask_Type.__name__ = "Integer32"
_IpRouteMask_Object = MibTableColumn
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3, 1, 2),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("current")
_IpRouteNextHop_Type = IpAddress
_IpRouteNextHop_Object = MibTableColumn
ipRouteNextHop = _IpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3, 1, 3),
    _IpRouteNextHop_Type()
)
ipRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteNextHop.setStatus("current")
_IpRouteIfName_Type = DisplayString
_IpRouteIfName_Object = MibTableColumn
ipRouteIfName = _IpRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 3, 1, 4),
    _IpRouteIfName_Type()
)
ipRouteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteIfName.setStatus("current")
_Ipv6DefaultRouterInbandTable_Object = MibTable
ipv6DefaultRouterInbandTable = _Ipv6DefaultRouterInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4)
)
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandTable.setStatus("current")
_Ipv6DefaultRouterInbandEntry_Object = MibTableRow
ipv6DefaultRouterInbandEntry = _Ipv6DefaultRouterInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1)
)
ipv6DefaultRouterInbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6DefaultRouterInbandAddress"),
)
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandEntry.setStatus("current")
_Ipv6DefaultRouterInbandAddress_Type = InetAddress
_Ipv6DefaultRouterInbandAddress_Object = MibTableColumn
ipv6DefaultRouterInbandAddress = _Ipv6DefaultRouterInbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1, 1),
    _Ipv6DefaultRouterInbandAddress_Type()
)
ipv6DefaultRouterInbandAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandAddress.setStatus("current")
_Ipv6DefaultRouterInbandPreference_Type = DisplayString
_Ipv6DefaultRouterInbandPreference_Object = MibTableColumn
ipv6DefaultRouterInbandPreference = _Ipv6DefaultRouterInbandPreference_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1, 2),
    _Ipv6DefaultRouterInbandPreference_Type()
)
ipv6DefaultRouterInbandPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandPreference.setStatus("current")
_Ipv6DefaultRouterInbandLifetime_Type = Integer32
_Ipv6DefaultRouterInbandLifetime_Object = MibTableColumn
ipv6DefaultRouterInbandLifetime = _Ipv6DefaultRouterInbandLifetime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1, 3),
    _Ipv6DefaultRouterInbandLifetime_Type()
)
ipv6DefaultRouterInbandLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandLifetime.setStatus("current")
_Ipv6DefaultRouterInbandExpire_Type = DisplayString
_Ipv6DefaultRouterInbandExpire_Object = MibTableColumn
ipv6DefaultRouterInbandExpire = _Ipv6DefaultRouterInbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1, 4),
    _Ipv6DefaultRouterInbandExpire_Type()
)
ipv6DefaultRouterInbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandExpire.setStatus("current")
_Ipv6DefaultRouterInbandFlag_Type = DisplayString
_Ipv6DefaultRouterInbandFlag_Object = MibTableColumn
ipv6DefaultRouterInbandFlag = _Ipv6DefaultRouterInbandFlag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 4, 1, 5),
    _Ipv6DefaultRouterInbandFlag_Type()
)
ipv6DefaultRouterInbandFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterInbandFlag.setStatus("current")
_Ipv6DefaultRouterOutbandTable_Object = MibTable
ipv6DefaultRouterOutbandTable = _Ipv6DefaultRouterOutbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5)
)
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandTable.setStatus("current")
_Ipv6DefaultRouterOutbandEntry_Object = MibTableRow
ipv6DefaultRouterOutbandEntry = _Ipv6DefaultRouterOutbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1)
)
ipv6DefaultRouterOutbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6DefaultRouterOutbandAddress"),
)
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandEntry.setStatus("current")
_Ipv6DefaultRouterOutbandAddress_Type = InetAddress
_Ipv6DefaultRouterOutbandAddress_Object = MibTableColumn
ipv6DefaultRouterOutbandAddress = _Ipv6DefaultRouterOutbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1, 1),
    _Ipv6DefaultRouterOutbandAddress_Type()
)
ipv6DefaultRouterOutbandAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandAddress.setStatus("current")
_Ipv6DefaultRouterOutbandPreference_Type = DisplayString
_Ipv6DefaultRouterOutbandPreference_Object = MibTableColumn
ipv6DefaultRouterOutbandPreference = _Ipv6DefaultRouterOutbandPreference_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1, 2),
    _Ipv6DefaultRouterOutbandPreference_Type()
)
ipv6DefaultRouterOutbandPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandPreference.setStatus("current")
_Ipv6DefaultRouterOutbandLifetime_Type = Integer32
_Ipv6DefaultRouterOutbandLifetime_Object = MibTableColumn
ipv6DefaultRouterOutbandLifetime = _Ipv6DefaultRouterOutbandLifetime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1, 3),
    _Ipv6DefaultRouterOutbandLifetime_Type()
)
ipv6DefaultRouterOutbandLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandLifetime.setStatus("current")
_Ipv6DefaultRouterOutbandExpire_Type = DisplayString
_Ipv6DefaultRouterOutbandExpire_Object = MibTableColumn
ipv6DefaultRouterOutbandExpire = _Ipv6DefaultRouterOutbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1, 4),
    _Ipv6DefaultRouterOutbandExpire_Type()
)
ipv6DefaultRouterOutbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandExpire.setStatus("current")
_Ipv6DefaultRouterOutbandFlag_Type = DisplayString
_Ipv6DefaultRouterOutbandFlag_Object = MibTableColumn
ipv6DefaultRouterOutbandFlag = _Ipv6DefaultRouterOutbandFlag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 5, 1, 5),
    _Ipv6DefaultRouterOutbandFlag_Type()
)
ipv6DefaultRouterOutbandFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouterOutbandFlag.setStatus("current")
_Ipv6RouteInbandTable_Object = MibTable
ipv6RouteInbandTable = _Ipv6RouteInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 6)
)
if mibBuilder.loadTexts:
    ipv6RouteInbandTable.setStatus("current")
_Ipv6RouteInbandEntry_Object = MibTableRow
ipv6RouteInbandEntry = _Ipv6RouteInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 6, 1)
)
ipv6RouteInbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6RouteInbandAddress"),
    (0, "VES1724-58V-MIB", "ipv6RouteInbandMask"),
)
if mibBuilder.loadTexts:
    ipv6RouteInbandEntry.setStatus("current")
_Ipv6RouteInbandAddress_Type = InetAddress
_Ipv6RouteInbandAddress_Object = MibTableColumn
ipv6RouteInbandAddress = _Ipv6RouteInbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 6, 1, 1),
    _Ipv6RouteInbandAddress_Type()
)
ipv6RouteInbandAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteInbandAddress.setStatus("current")
_Ipv6RouteInbandMask_Type = Integer32
_Ipv6RouteInbandMask_Object = MibTableColumn
ipv6RouteInbandMask = _Ipv6RouteInbandMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 6, 1, 2),
    _Ipv6RouteInbandMask_Type()
)
ipv6RouteInbandMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteInbandMask.setStatus("current")
_Ipv6RouteInbandName_Type = DisplayString
_Ipv6RouteInbandName_Object = MibTableColumn
ipv6RouteInbandName = _Ipv6RouteInbandName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 6, 1, 3),
    _Ipv6RouteInbandName_Type()
)
ipv6RouteInbandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteInbandName.setStatus("current")
_Ipv6RouteOutbandTable_Object = MibTable
ipv6RouteOutbandTable = _Ipv6RouteOutbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 7)
)
if mibBuilder.loadTexts:
    ipv6RouteOutbandTable.setStatus("current")
_Ipv6RouteOutbandEntry_Object = MibTableRow
ipv6RouteOutbandEntry = _Ipv6RouteOutbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 7, 1)
)
ipv6RouteOutbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6RouteOutbandAddress"),
)
if mibBuilder.loadTexts:
    ipv6RouteOutbandEntry.setStatus("current")
_Ipv6RouteOutbandAddress_Type = InetAddress
_Ipv6RouteOutbandAddress_Object = MibTableColumn
ipv6RouteOutbandAddress = _Ipv6RouteOutbandAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 7, 1, 1),
    _Ipv6RouteOutbandAddress_Type()
)
ipv6RouteOutbandAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteOutbandAddress.setStatus("current")
_Ipv6RouteOutbandMask_Type = Integer32
_Ipv6RouteOutbandMask_Object = MibTableColumn
ipv6RouteOutbandMask = _Ipv6RouteOutbandMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 7, 1, 2),
    _Ipv6RouteOutbandMask_Type()
)
ipv6RouteOutbandMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteOutbandMask.setStatus("current")
_Ipv6RouteOutbandName_Type = DisplayString
_Ipv6RouteOutbandName_Object = MibTableColumn
ipv6RouteOutbandName = _Ipv6RouteOutbandName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 5, 7, 1, 3),
    _Ipv6RouteOutbandName_Type()
)
ipv6RouteOutbandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteOutbandName.setStatus("current")
_IpStatistic_ObjectIdentity = ObjectIdentity
ipStatistic = _IpStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6)
)
_IpInOctetCount_Type = Counter32
_IpInOctetCount_Object = MibScalar
ipInOctetCount = _IpInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 1),
    _IpInOctetCount_Type()
)
ipInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInOctetCount.setStatus("current")
_IpInUnicastCount_Type = Counter32
_IpInUnicastCount_Object = MibScalar
ipInUnicastCount = _IpInUnicastCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 2),
    _IpInUnicastCount_Type()
)
ipInUnicastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInUnicastCount.setStatus("current")
_IpInMulticastCount_Type = Counter32
_IpInMulticastCount_Object = MibScalar
ipInMulticastCount = _IpInMulticastCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 3),
    _IpInMulticastCount_Type()
)
ipInMulticastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInMulticastCount.setStatus("current")
_IpInDiscardCount_Type = Counter32
_IpInDiscardCount_Object = MibScalar
ipInDiscardCount = _IpInDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 4),
    _IpInDiscardCount_Type()
)
ipInDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDiscardCount.setStatus("current")
_IpInErrorCount_Type = Counter32
_IpInErrorCount_Object = MibScalar
ipInErrorCount = _IpInErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 5),
    _IpInErrorCount_Type()
)
ipInErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInErrorCount.setStatus("current")
_IpInUnknowProtocolCount_Type = Counter32
_IpInUnknowProtocolCount_Object = MibScalar
ipInUnknowProtocolCount = _IpInUnknowProtocolCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 6),
    _IpInUnknowProtocolCount_Type()
)
ipInUnknowProtocolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInUnknowProtocolCount.setStatus("current")
_IpOutOctetCount_Type = Counter32
_IpOutOctetCount_Object = MibScalar
ipOutOctetCount = _IpOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 7),
    _IpOutOctetCount_Type()
)
ipOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutOctetCount.setStatus("current")
_IpOutUnicastCount_Type = Counter32
_IpOutUnicastCount_Object = MibScalar
ipOutUnicastCount = _IpOutUnicastCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 8),
    _IpOutUnicastCount_Type()
)
ipOutUnicastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutUnicastCount.setStatus("current")
_IpOutMulticastCount_Type = Counter32
_IpOutMulticastCount_Object = MibScalar
ipOutMulticastCount = _IpOutMulticastCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 9),
    _IpOutMulticastCount_Type()
)
ipOutMulticastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutMulticastCount.setStatus("current")
_IpOutDiscardCount_Type = Counter32
_IpOutDiscardCount_Object = MibScalar
ipOutDiscardCount = _IpOutDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 10),
    _IpOutDiscardCount_Type()
)
ipOutDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutDiscardCount.setStatus("current")
_IpOutErrorCount_Type = Counter32
_IpOutErrorCount_Object = MibScalar
ipOutErrorCount = _IpOutErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 6, 11),
    _IpOutErrorCount_Type()
)
ipOutErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutErrorCount.setStatus("current")
_Ipv6Destination_ObjectIdentity = ObjectIdentity
ipv6Destination = _Ipv6Destination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7)
)
_Ipv6DestInbandTable_Object = MibTable
ipv6DestInbandTable = _Ipv6DestInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 1)
)
if mibBuilder.loadTexts:
    ipv6DestInbandTable.setStatus("current")
_Ipv6DestInbandEntry_Object = MibTableRow
ipv6DestInbandEntry = _Ipv6DestInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 1, 1)
)
ipv6DestInbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6DestInbandDestAddress"),
)
if mibBuilder.loadTexts:
    ipv6DestInbandEntry.setStatus("current")
_Ipv6DestInbandDestAddress_Type = InetAddress
_Ipv6DestInbandDestAddress_Object = MibTableColumn
ipv6DestInbandDestAddress = _Ipv6DestInbandDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 1, 1, 1),
    _Ipv6DestInbandDestAddress_Type()
)
ipv6DestInbandDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DestInbandDestAddress.setStatus("current")
_Ipv6DestInbandNextHopAddress_Type = InetAddress
_Ipv6DestInbandNextHopAddress_Object = MibTableColumn
ipv6DestInbandNextHopAddress = _Ipv6DestInbandNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 1, 1, 2),
    _Ipv6DestInbandNextHopAddress_Type()
)
ipv6DestInbandNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DestInbandNextHopAddress.setStatus("current")
_Ipv6DestOutbandTable_Object = MibTable
ipv6DestOutbandTable = _Ipv6DestOutbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 2)
)
if mibBuilder.loadTexts:
    ipv6DestOutbandTable.setStatus("current")
_Ipv6DestOutbandEntry_Object = MibTableRow
ipv6DestOutbandEntry = _Ipv6DestOutbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 2, 1)
)
ipv6DestOutbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6DestOutbandDestAddress"),
)
if mibBuilder.loadTexts:
    ipv6DestOutbandEntry.setStatus("current")
_Ipv6DestOutbandDestAddress_Type = InetAddress
_Ipv6DestOutbandDestAddress_Object = MibTableColumn
ipv6DestOutbandDestAddress = _Ipv6DestOutbandDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 2, 1, 1),
    _Ipv6DestOutbandDestAddress_Type()
)
ipv6DestOutbandDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DestOutbandDestAddress.setStatus("current")
_Ipv6DestOutbandNextHopAddress_Type = InetAddress
_Ipv6DestOutbandNextHopAddress_Object = MibTableColumn
ipv6DestOutbandNextHopAddress = _Ipv6DestOutbandNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 7, 2, 1, 2),
    _Ipv6DestOutbandNextHopAddress_Type()
)
ipv6DestOutbandNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DestOutbandNextHopAddress.setStatus("current")
_Ipv6Neighbor_ObjectIdentity = ObjectIdentity
ipv6Neighbor = _Ipv6Neighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8)
)
_Ipv6NeighborInbandTable_Object = MibTable
ipv6NeighborInbandTable = _Ipv6NeighborInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1)
)
if mibBuilder.loadTexts:
    ipv6NeighborInbandTable.setStatus("current")
_Ipv6NeighborInbandEntry_Object = MibTableRow
ipv6NeighborInbandEntry = _Ipv6NeighborInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1, 1)
)
ipv6NeighborInbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6NeighborInbandNeighbor"),
)
if mibBuilder.loadTexts:
    ipv6NeighborInbandEntry.setStatus("current")
_Ipv6NeighborInbandNeighbor_Type = InetAddress
_Ipv6NeighborInbandNeighbor_Object = MibTableColumn
ipv6NeighborInbandNeighbor = _Ipv6NeighborInbandNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1, 1, 1),
    _Ipv6NeighborInbandNeighbor_Type()
)
ipv6NeighborInbandNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborInbandNeighbor.setStatus("current")


class _Ipv6NeighborInbandLinklayerAddress_Type(PhysAddress):
    """Custom type ipv6NeighborInbandLinklayerAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Ipv6NeighborInbandLinklayerAddress_Type.__name__ = "PhysAddress"
_Ipv6NeighborInbandLinklayerAddress_Object = MibTableColumn
ipv6NeighborInbandLinklayerAddress = _Ipv6NeighborInbandLinklayerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1, 1, 2),
    _Ipv6NeighborInbandLinklayerAddress_Type()
)
ipv6NeighborInbandLinklayerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborInbandLinklayerAddress.setStatus("current")
_Ipv6NeighborInbandExpire_Type = DisplayString
_Ipv6NeighborInbandExpire_Object = MibTableColumn
ipv6NeighborInbandExpire = _Ipv6NeighborInbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1, 1, 3),
    _Ipv6NeighborInbandExpire_Type()
)
ipv6NeighborInbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborInbandExpire.setStatus("current")
_Ipv6NeighborInbandFlags_Type = DisplayString
_Ipv6NeighborInbandFlags_Object = MibTableColumn
ipv6NeighborInbandFlags = _Ipv6NeighborInbandFlags_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 1, 1, 4),
    _Ipv6NeighborInbandFlags_Type()
)
ipv6NeighborInbandFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborInbandFlags.setStatus("current")
_Ipv6NeighborOutbandTable_Object = MibTable
ipv6NeighborOutbandTable = _Ipv6NeighborOutbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2)
)
if mibBuilder.loadTexts:
    ipv6NeighborOutbandTable.setStatus("current")
_Ipv6NeighborOutbandEntry_Object = MibTableRow
ipv6NeighborOutbandEntry = _Ipv6NeighborOutbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2, 1)
)
ipv6NeighborOutbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6NeighborOutbandNeighbor"),
)
if mibBuilder.loadTexts:
    ipv6NeighborOutbandEntry.setStatus("current")
_Ipv6NeighborOutbandNeighbor_Type = InetAddress
_Ipv6NeighborOutbandNeighbor_Object = MibTableColumn
ipv6NeighborOutbandNeighbor = _Ipv6NeighborOutbandNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2, 1, 1),
    _Ipv6NeighborOutbandNeighbor_Type()
)
ipv6NeighborOutbandNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborOutbandNeighbor.setStatus("current")


class _Ipv6NeighborOutbandLinklayerAddress_Type(PhysAddress):
    """Custom type ipv6NeighborOutbandLinklayerAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Ipv6NeighborOutbandLinklayerAddress_Type.__name__ = "PhysAddress"
_Ipv6NeighborOutbandLinklayerAddress_Object = MibTableColumn
ipv6NeighborOutbandLinklayerAddress = _Ipv6NeighborOutbandLinklayerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2, 1, 2),
    _Ipv6NeighborOutbandLinklayerAddress_Type()
)
ipv6NeighborOutbandLinklayerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborOutbandLinklayerAddress.setStatus("current")
_Ipv6NeighborOutbandExpire_Type = DisplayString
_Ipv6NeighborOutbandExpire_Object = MibTableColumn
ipv6NeighborOutbandExpire = _Ipv6NeighborOutbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2, 1, 3),
    _Ipv6NeighborOutbandExpire_Type()
)
ipv6NeighborOutbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborOutbandExpire.setStatus("current")
_Ipv6NeighborOutbandFlags_Type = DisplayString
_Ipv6NeighborOutbandFlags_Object = MibTableColumn
ipv6NeighborOutbandFlags = _Ipv6NeighborOutbandFlags_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 8, 2, 1, 4),
    _Ipv6NeighborOutbandFlags_Type()
)
ipv6NeighborOutbandFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborOutbandFlags.setStatus("current")
_Ipv6Prefix_ObjectIdentity = ObjectIdentity
ipv6Prefix = _Ipv6Prefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9)
)
_Ipv6PrefixInbandTable_Object = MibTable
ipv6PrefixInbandTable = _Ipv6PrefixInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1)
)
if mibBuilder.loadTexts:
    ipv6PrefixInbandTable.setStatus("current")
_Ipv6PrefixInbandEntry_Object = MibTableRow
ipv6PrefixInbandEntry = _Ipv6PrefixInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1)
)
ipv6PrefixInbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6PrefixInbandPrefix"),
    (0, "VES1724-58V-MIB", "ipv6PrefixInbandPrefixLength"),
)
if mibBuilder.loadTexts:
    ipv6PrefixInbandEntry.setStatus("current")
_Ipv6PrefixInbandPrefix_Type = InetAddress
_Ipv6PrefixInbandPrefix_Object = MibTableColumn
ipv6PrefixInbandPrefix = _Ipv6PrefixInbandPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 1),
    _Ipv6PrefixInbandPrefix_Type()
)
ipv6PrefixInbandPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandPrefix.setStatus("current")
_Ipv6PrefixInbandPrefixLength_Type = Integer32
_Ipv6PrefixInbandPrefixLength_Object = MibTableColumn
ipv6PrefixInbandPrefixLength = _Ipv6PrefixInbandPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 2),
    _Ipv6PrefixInbandPrefixLength_Type()
)
ipv6PrefixInbandPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandPrefixLength.setStatus("current")
_Ipv6PrefixInbandVLtime_Type = DisplayString
_Ipv6PrefixInbandVLtime_Object = MibTableColumn
ipv6PrefixInbandVLtime = _Ipv6PrefixInbandVLtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 3),
    _Ipv6PrefixInbandVLtime_Type()
)
ipv6PrefixInbandVLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandVLtime.setStatus("current")
_Ipv6PrefixInbandPLtime_Type = DisplayString
_Ipv6PrefixInbandPLtime_Object = MibTableColumn
ipv6PrefixInbandPLtime = _Ipv6PrefixInbandPLtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 4),
    _Ipv6PrefixInbandPLtime_Type()
)
ipv6PrefixInbandPLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandPLtime.setStatus("current")
_Ipv6PrefixInbandExpire_Type = DisplayString
_Ipv6PrefixInbandExpire_Object = MibTableColumn
ipv6PrefixInbandExpire = _Ipv6PrefixInbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 5),
    _Ipv6PrefixInbandExpire_Type()
)
ipv6PrefixInbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandExpire.setStatus("current")


class _Ipv6PrefixInbandOnlink_Type(Integer32):
    """Custom type ipv6PrefixInbandOnlink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ipv6PrefixInbandOnlink_Type.__name__ = "Integer32"
_Ipv6PrefixInbandOnlink_Object = MibTableColumn
ipv6PrefixInbandOnlink = _Ipv6PrefixInbandOnlink_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 6),
    _Ipv6PrefixInbandOnlink_Type()
)
ipv6PrefixInbandOnlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandOnlink.setStatus("current")


class _Ipv6PrefixInbandAutonomous_Type(Integer32):
    """Custom type ipv6PrefixInbandAutonomous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ipv6PrefixInbandAutonomous_Type.__name__ = "Integer32"
_Ipv6PrefixInbandAutonomous_Object = MibTableColumn
ipv6PrefixInbandAutonomous = _Ipv6PrefixInbandAutonomous_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 1, 1, 7),
    _Ipv6PrefixInbandAutonomous_Type()
)
ipv6PrefixInbandAutonomous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixInbandAutonomous.setStatus("current")
_Ipv6PrefixOutbandTable_Object = MibTable
ipv6PrefixOutbandTable = _Ipv6PrefixOutbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2)
)
if mibBuilder.loadTexts:
    ipv6PrefixOutbandTable.setStatus("current")
_Ipv6PrefixOutbandEntry_Object = MibTableRow
ipv6PrefixOutbandEntry = _Ipv6PrefixOutbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1)
)
ipv6PrefixOutbandEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "ipv6PrefixOutbandPrefix"),
    (0, "VES1724-58V-MIB", "ipv6PrefixOutbandPrefixLength"),
)
if mibBuilder.loadTexts:
    ipv6PrefixOutbandEntry.setStatus("current")
_Ipv6PrefixOutbandPrefix_Type = InetAddress
_Ipv6PrefixOutbandPrefix_Object = MibTableColumn
ipv6PrefixOutbandPrefix = _Ipv6PrefixOutbandPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 1),
    _Ipv6PrefixOutbandPrefix_Type()
)
ipv6PrefixOutbandPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandPrefix.setStatus("current")
_Ipv6PrefixOutbandPrefixLength_Type = Integer32
_Ipv6PrefixOutbandPrefixLength_Object = MibTableColumn
ipv6PrefixOutbandPrefixLength = _Ipv6PrefixOutbandPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 2),
    _Ipv6PrefixOutbandPrefixLength_Type()
)
ipv6PrefixOutbandPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandPrefixLength.setStatus("current")
_Ipv6PrefixOutbandVLtime_Type = DisplayString
_Ipv6PrefixOutbandVLtime_Object = MibTableColumn
ipv6PrefixOutbandVLtime = _Ipv6PrefixOutbandVLtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 3),
    _Ipv6PrefixOutbandVLtime_Type()
)
ipv6PrefixOutbandVLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandVLtime.setStatus("current")
_Ipv6PrefixOutbandPLtime_Type = DisplayString
_Ipv6PrefixOutbandPLtime_Object = MibTableColumn
ipv6PrefixOutbandPLtime = _Ipv6PrefixOutbandPLtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 4),
    _Ipv6PrefixOutbandPLtime_Type()
)
ipv6PrefixOutbandPLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandPLtime.setStatus("current")
_Ipv6PrefixOutbandExpire_Type = DisplayString
_Ipv6PrefixOutbandExpire_Object = MibTableColumn
ipv6PrefixOutbandExpire = _Ipv6PrefixOutbandExpire_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 5),
    _Ipv6PrefixOutbandExpire_Type()
)
ipv6PrefixOutbandExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandExpire.setStatus("current")


class _Ipv6PrefixOutbandOnlink_Type(Integer32):
    """Custom type ipv6PrefixOutbandOnlink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ipv6PrefixOutbandOnlink_Type.__name__ = "Integer32"
_Ipv6PrefixOutbandOnlink_Object = MibTableColumn
ipv6PrefixOutbandOnlink = _Ipv6PrefixOutbandOnlink_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 6),
    _Ipv6PrefixOutbandOnlink_Type()
)
ipv6PrefixOutbandOnlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandOnlink.setStatus("current")


class _Ipv6PrefixOutbandAutonomous_Type(Integer32):
    """Custom type ipv6PrefixOutbandAutonomous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ipv6PrefixOutbandAutonomous_Type.__name__ = "Integer32"
_Ipv6PrefixOutbandAutonomous_Object = MibTableColumn
ipv6PrefixOutbandAutonomous = _Ipv6PrefixOutbandAutonomous_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 7, 9, 2, 1, 7),
    _Ipv6PrefixOutbandAutonomous_Type()
)
ipv6PrefixOutbandAutonomous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PrefixOutbandAutonomous.setStatus("current")
_Lcm_ObjectIdentity = ObjectIdentity
lcm = _Lcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8)
)
_SlotModuleTable_Object = MibTable
slotModuleTable = _SlotModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1)
)
if mibBuilder.loadTexts:
    slotModuleTable.setStatus("current")
_SlotModuleEntry_Object = MibTableRow
slotModuleEntry = _SlotModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1)
)
slotModuleEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
)
if mibBuilder.loadTexts:
    slotModuleEntry.setStatus("current")
_SlotModuleIdVes1724_58v_Type = Integer32
_SlotModuleIdVes1724_58v_Object = MibTableColumn
slotModuleIdVes1724_58v = _SlotModuleIdVes1724_58v_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 1),
    _SlotModuleIdVes1724_58v_Type()
)
slotModuleIdVes1724_58v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleIdVes1724_58v.setStatus("current")


class _SlotModuleRealType_Type(Integer32):
    """Custom type slotModuleRealType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("msc", 1),
          ("alc", 2),
          ("vlc", 3),
          ("vop", 4),
          ("unknown", 8))
    )


_SlotModuleRealType_Type.__name__ = "Integer32"
_SlotModuleRealType_Object = MibTableColumn
slotModuleRealType = _SlotModuleRealType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 2),
    _SlotModuleRealType_Type()
)
slotModuleRealType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleRealType.setStatus("current")
_SlotModuleDescr_Type = DisplayString
_SlotModuleDescr_Object = MibTableColumn
slotModuleDescr = _SlotModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 4),
    _SlotModuleDescr_Type()
)
slotModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleDescr.setStatus("current")


class _SlotModuleStatus_Type(Integer32):
    """Custom type slotModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("init", 1),
          ("provisioning", 2),
          ("active", 3),
          ("failure", 4),
          ("disabled", 5),
          ("unknown", 6))
    )


_SlotModuleStatus_Type.__name__ = "Integer32"
_SlotModuleStatus_Object = MibTableColumn
slotModuleStatus = _SlotModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 5),
    _SlotModuleStatus_Type()
)
slotModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleStatus.setStatus("current")


class _SlotModuleAlarmStatus_Type(Integer32):
    """Custom type slotModuleAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hasAlarm", 1),
          ("noAlarm", 2))
    )


_SlotModuleAlarmStatus_Type.__name__ = "Integer32"
_SlotModuleAlarmStatus_Object = MibTableColumn
slotModuleAlarmStatus = _SlotModuleAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 6),
    _SlotModuleAlarmStatus_Type()
)
slotModuleAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleAlarmStatus.setStatus("current")
_SlotModuleHWVersion_Type = DisplayString
_SlotModuleHWVersion_Object = MibTableColumn
slotModuleHWVersion = _SlotModuleHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 7),
    _SlotModuleHWVersion_Type()
)
slotModuleHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleHWVersion.setStatus("current")
_SlotModuleSerialNumber_Type = DisplayString
_SlotModuleSerialNumber_Object = MibTableColumn
slotModuleSerialNumber = _SlotModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 8),
    _SlotModuleSerialNumber_Type()
)
slotModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleSerialNumber.setStatus("current")
_SlotModuleCleiCode_Type = DisplayString
_SlotModuleCleiCode_Object = MibTableColumn
slotModuleCleiCode = _SlotModuleCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 9),
    _SlotModuleCleiCode_Type()
)
slotModuleCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleCleiCode.setStatus("current")
_SlotModuleUpTime_Type = Integer32
_SlotModuleUpTime_Object = MibTableColumn
slotModuleUpTime = _SlotModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 8, 1, 1, 10),
    _SlotModuleUpTime_Type()
)
slotModuleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleUpTime.setStatus("current")
_Login_ObjectIdentity = ObjectIdentity
login = _Login_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9)
)
_LoginMaxNumOfUsers_Type = Integer32
_LoginMaxNumOfUsers_Object = MibScalar
loginMaxNumOfUsers = _LoginMaxNumOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 1),
    _LoginMaxNumOfUsers_Type()
)
loginMaxNumOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginMaxNumOfUsers.setStatus("current")
_LoginUserTable_Object = MibTable
loginUserTable = _LoginUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2)
)
if mibBuilder.loadTexts:
    loginUserTable.setStatus("current")
_LoginUserEntry_Object = MibTableRow
loginUserEntry = _LoginUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2, 1)
)
loginUserEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "loginUserName"),
)
if mibBuilder.loadTexts:
    loginUserEntry.setStatus("current")


class _LoginUserName_Type(DisplayString):
    """Custom type loginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LoginUserName_Type.__name__ = "DisplayString"
_LoginUserName_Object = MibTableColumn
loginUserName = _LoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2, 1, 1),
    _LoginUserName_Type()
)
loginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserName.setStatus("current")


class _LoginUserPassword_Type(DisplayString):
    """Custom type loginUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 95),
    )


_LoginUserPassword_Type.__name__ = "DisplayString"
_LoginUserPassword_Object = MibTableColumn
loginUserPassword = _LoginUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2, 1, 2),
    _LoginUserPassword_Type()
)
loginUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loginUserPassword.setStatus("current")


class _LoginUserPrivilege_Type(Integer32):
    """Custom type loginUserPrivilege based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_LoginUserPrivilege_Type.__name__ = "Integer32"
_LoginUserPrivilege_Object = MibTableColumn
loginUserPrivilege = _LoginUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2, 1, 3),
    _LoginUserPrivilege_Type()
)
loginUserPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loginUserPrivilege.setStatus("current")
_LoginUserRowStatus_Type = RowStatus
_LoginUserRowStatus_Object = MibTableColumn
loginUserRowStatus = _LoginUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 9, 2, 1, 4),
    _LoginUserRowStatus_Type()
)
loginUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loginUserRowStatus.setStatus("current")
_Loopguard_ObjectIdentity = ObjectIdentity
loopguard = _Loopguard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10)
)
_LoopguardConfPortTable_Object = MibTable
loopguardConfPortTable = _LoopguardConfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1)
)
if mibBuilder.loadTexts:
    loopguardConfPortTable.setStatus("current")
_LoopguardConfPortEntry_Object = MibTableRow
loopguardConfPortEntry = _LoopguardConfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1)
)
loopguardConfPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    loopguardConfPortEntry.setStatus("current")


class _LoopguardConfPortEnable_Type(Integer32):
    """Custom type loopguardConfPortEnable based on Integer32"""
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


_LoopguardConfPortEnable_Type.__name__ = "Integer32"
_LoopguardConfPortEnable_Object = MibTableColumn
loopguardConfPortEnable = _LoopguardConfPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1, 1),
    _LoopguardConfPortEnable_Type()
)
loopguardConfPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardConfPortEnable.setStatus("current")


class _LoopguardConfPortPolicy_Type(Integer32):
    """Custom type loopguardConfPortPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix", 1),
          ("dynamic", 2))
    )


_LoopguardConfPortPolicy_Type.__name__ = "Integer32"
_LoopguardConfPortPolicy_Object = MibTableColumn
loopguardConfPortPolicy = _LoopguardConfPortPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1, 2),
    _LoopguardConfPortPolicy_Type()
)
loopguardConfPortPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardConfPortPolicy.setStatus("current")


class _LoopguardConfPortRecoverTime_Type(Integer32):
    """Custom type loopguardConfPortRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_LoopguardConfPortRecoverTime_Type.__name__ = "Integer32"
_LoopguardConfPortRecoverTime_Object = MibTableColumn
loopguardConfPortRecoverTime = _LoopguardConfPortRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1, 3),
    _LoopguardConfPortRecoverTime_Type()
)
loopguardConfPortRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardConfPortRecoverTime.setStatus("current")
if mibBuilder.loadTexts:
    loopguardConfPortRecoverTime.setUnits("seconds")


class _LoopguardConfPortUniVlan_Type(VlanIndex):
    """Custom type loopguardConfPortUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_LoopguardConfPortUniVlan_Type.__name__ = "VlanIndex"
_LoopguardConfPortUniVlan_Object = MibTableColumn
loopguardConfPortUniVlan = _LoopguardConfPortUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1, 4),
    _LoopguardConfPortUniVlan_Type()
)
loopguardConfPortUniVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardConfPortUniVlan.setStatus("current")


class _LoopguardConfPortPbit_Type(Integer32):
    """Custom type loopguardConfPortPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LoopguardConfPortPbit_Type.__name__ = "Integer32"
_LoopguardConfPortPbit_Object = MibTableColumn
loopguardConfPortPbit = _LoopguardConfPortPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 1, 1, 5),
    _LoopguardConfPortPbit_Type()
)
loopguardConfPortPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardConfPortPbit.setStatus("current")


class _LoopguardStatsSysStatus_Type(Integer32):
    """Custom type loopguardStatsSysStatus based on Integer32"""
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


_LoopguardStatsSysStatus_Type.__name__ = "Integer32"
_LoopguardStatsSysStatus_Object = MibScalar
loopguardStatsSysStatus = _LoopguardStatsSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 2),
    _LoopguardStatsSysStatus_Type()
)
loopguardStatsSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsSysStatus.setStatus("current")
_LoopguardStatsPortTable_Object = MibTable
loopguardStatsPortTable = _LoopguardStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3)
)
if mibBuilder.loadTexts:
    loopguardStatsPortTable.setStatus("current")
_LoopguardStatsPortEntry_Object = MibTableRow
loopguardStatsPortEntry = _LoopguardStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1)
)
loopguardStatsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    loopguardStatsPortEntry.setStatus("current")


class _LoopguardStatsPortLinkedState_Type(Integer32):
    """Custom type loopguardStatsPortLinkedState based on Integer32"""
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


_LoopguardStatsPortLinkedState_Type.__name__ = "Integer32"
_LoopguardStatsPortLinkedState_Object = MibTableColumn
loopguardStatsPortLinkedState = _LoopguardStatsPortLinkedState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 1),
    _LoopguardStatsPortLinkedState_Type()
)
loopguardStatsPortLinkedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsPortLinkedState.setStatus("current")
_LoopguardStatsPortTxPkts_Type = Counter32
_LoopguardStatsPortTxPkts_Object = MibTableColumn
loopguardStatsPortTxPkts = _LoopguardStatsPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 2),
    _LoopguardStatsPortTxPkts_Type()
)
loopguardStatsPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsPortTxPkts.setStatus("current")
_LoopguardStatsPortRxPkts_Type = Counter32
_LoopguardStatsPortRxPkts_Object = MibTableColumn
loopguardStatsPortRxPkts = _LoopguardStatsPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 3),
    _LoopguardStatsPortRxPkts_Type()
)
loopguardStatsPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsPortRxPkts.setStatus("current")
_LoopguardStatsPortBadPkts_Type = Counter32
_LoopguardStatsPortBadPkts_Object = MibTableColumn
loopguardStatsPortBadPkts = _LoopguardStatsPortBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 4),
    _LoopguardStatsPortBadPkts_Type()
)
loopguardStatsPortBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsPortBadPkts.setStatus("current")
_LoopguardStatsPortShutdownTime_Type = DisplayString
_LoopguardStatsPortShutdownTime_Object = MibTableColumn
loopguardStatsPortShutdownTime = _LoopguardStatsPortShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 5),
    _LoopguardStatsPortShutdownTime_Type()
)
loopguardStatsPortShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardStatsPortShutdownTime.setStatus("current")


class _LoopguardStatsPortOperation_Type(Integer32):
    """Custom type loopguardStatsPortOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearLoopguardStatistics", 1)
    )


_LoopguardStatsPortOperation_Type.__name__ = "Integer32"
_LoopguardStatsPortOperation_Object = MibTableColumn
loopguardStatsPortOperation = _LoopguardStatsPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 10, 3, 1, 6),
    _LoopguardStatsPortOperation_Type()
)
loopguardStatsPortOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardStatsPortOperation.setStatus("current")
_Interworking_ObjectIdentity = ObjectIdentity
interworking = _Interworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11)
)
_Atmvc_ObjectIdentity = ObjectIdentity
atmvc = _Atmvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1)
)
_AtmMaxNumOfVcPerPort_Type = Integer32
_AtmMaxNumOfVcPerPort_Object = MibScalar
atmMaxNumOfVcPerPort = _AtmMaxNumOfVcPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 1),
    _AtmMaxNumOfVcPerPort_Type()
)
atmMaxNumOfVcPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMaxNumOfVcPerPort.setStatus("current")
_AtmvcTable_Object = MibTable
atmvcTable = _AtmvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2)
)
if mibBuilder.loadTexts:
    atmvcTable.setStatus("current")
_AtmvcEntry_Object = MibTableRow
atmvcEntry = _AtmvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1)
)
atmvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    atmvcEntry.setStatus("current")


class _AtmvcVpi_Type(Integer32):
    """Custom type atmvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmvcVpi_Type.__name__ = "Integer32"
_AtmvcVpi_Object = MibTableColumn
atmvcVpi = _AtmvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 1),
    _AtmvcVpi_Type()
)
atmvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmvcVpi.setStatus("current")


class _AtmvcVci_Type(Integer32):
    """Custom type atmvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_AtmvcVci_Type.__name__ = "Integer32"
_AtmvcVci_Object = MibTableColumn
atmvcVci = _AtmvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 2),
    _AtmvcVci_Type()
)
atmvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmvcVci.setStatus("current")


class _AtmvcPriority_Type(Integer32):
    """Custom type atmvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtmvcPriority_Type.__name__ = "Integer32"
_AtmvcPriority_Object = MibTableColumn
atmvcPriority = _AtmvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 3),
    _AtmvcPriority_Type()
)
atmvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcPriority.setStatus("current")


class _AtmvcEncap_Type(Integer32):
    """Custom type atmvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_AtmvcEncap_Type.__name__ = "Integer32"
_AtmvcEncap_Object = MibTableColumn
atmvcEncap = _AtmvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 4),
    _AtmvcEncap_Type()
)
atmvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcEncap.setStatus("current")
_AtmvcRowStatus_Type = RowStatus
_AtmvcRowStatus_Object = MibTableColumn
atmvcRowStatus = _AtmvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 7),
    _AtmvcRowStatus_Type()
)
atmvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcRowStatus.setStatus("current")


class _AtmvcMvlan_Type(Integer32):
    """Custom type atmvcMvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("join", 1),
          ("nojoin", 2))
    )


_AtmvcMvlan_Type.__name__ = "Integer32"
_AtmvcMvlan_Object = MibTableColumn
atmvcMvlan = _AtmvcMvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 8),
    _AtmvcMvlan_Type()
)
atmvcMvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcMvlan.setStatus("current")


class _AtmvcPvid_Type(Integer32):
    """Custom type atmvcPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AtmvcPvid_Type.__name__ = "Integer32"
_AtmvcPvid_Object = MibTableColumn
atmvcPvid = _AtmvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 9),
    _AtmvcPvid_Type()
)
atmvcPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcPvid.setStatus("current")


class _AtmvcPbit_Type(Integer32):
    """Custom type atmvcPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtmvcPbit_Type.__name__ = "Integer32"
_AtmvcPbit_Object = MibTableColumn
atmvcPbit = _AtmvcPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 10),
    _AtmvcPbit_Type()
)
atmvcPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcPbit.setStatus("current")


class _AtmvcVlanTrunk_Type(Integer32):
    """Custom type atmvcVlanTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("join", 1),
          ("nojoin", 2))
    )


_AtmvcVlanTrunk_Type.__name__ = "Integer32"
_AtmvcVlanTrunk_Object = MibTableColumn
atmvcVlanTrunk = _AtmvcVlanTrunk_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 2, 1, 11),
    _AtmvcVlanTrunk_Type()
)
atmvcVlanTrunk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmvcVlanTrunk.setStatus("current")
_AtmOamF5Table_Object = MibTable
atmOamF5Table = _AtmOamF5Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 3)
)
if mibBuilder.loadTexts:
    atmOamF5Table.setStatus("current")
_AtmOamF5Entry_Object = MibTableRow
atmOamF5Entry = _AtmOamF5Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 3, 1)
)
atmOamF5Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    atmOamF5Entry.setStatus("current")


class _AtmOamF5Test_Type(Integer32):
    """Custom type atmOamF5Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("test", 2))
    )


_AtmOamF5Test_Type.__name__ = "Integer32"
_AtmOamF5Test_Object = MibTableColumn
atmOamF5Test = _AtmOamF5Test_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 3, 1, 1),
    _AtmOamF5Test_Type()
)
atmOamF5Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamF5Test.setStatus("current")


class _AtmOamF5TestResult_Type(Integer32):
    """Custom type atmOamF5TestResult based on Integer32"""
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
          ("ongoing", 2),
          ("successful", 3),
          ("failed", 4))
    )


_AtmOamF5TestResult_Type.__name__ = "Integer32"
_AtmOamF5TestResult_Object = MibTableColumn
atmOamF5TestResult = _AtmOamF5TestResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 1, 3, 1, 2),
    _AtmOamF5TestResult_Type()
)
atmOamF5TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamF5TestResult.setStatus("current")
_PortIsolation_ObjectIdentity = ObjectIdentity
portIsolation = _PortIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2)
)


class _PortIsolationEnable_Type(Integer32):
    """Custom type portIsolationEnable based on Integer32"""
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


_PortIsolationEnable_Type.__name__ = "Integer32"
_PortIsolationEnable_Object = MibScalar
portIsolationEnable = _PortIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2, 1),
    _PortIsolationEnable_Type()
)
portIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIsolationEnable.setStatus("current")
_PortIsolationVlanTable_Object = MibTable
portIsolationVlanTable = _PortIsolationVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2, 2)
)
if mibBuilder.loadTexts:
    portIsolationVlanTable.setStatus("current")
_PortIsolationVlanEntry_Object = MibTableRow
portIsolationVlanEntry = _PortIsolationVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2, 2, 1)
)
portIsolationVlanEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "portIsolationVlanVid"),
)
if mibBuilder.loadTexts:
    portIsolationVlanEntry.setStatus("current")


class _PortIsolationVlanVid_Type(VlanIndex):
    """Custom type portIsolationVlanVid based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_PortIsolationVlanVid_Type.__name__ = "VlanIndex"
_PortIsolationVlanVid_Object = MibTableColumn
portIsolationVlanVid = _PortIsolationVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2, 2, 1, 1),
    _PortIsolationVlanVid_Type()
)
portIsolationVlanVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIsolationVlanVid.setStatus("current")
_PortIsolationVlanRowStatus_Type = RowStatus
_PortIsolationVlanRowStatus_Object = MibTableColumn
portIsolationVlanRowStatus = _PortIsolationVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 2, 2, 1, 2),
    _PortIsolationVlanRowStatus_Type()
)
portIsolationVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portIsolationVlanRowStatus.setStatus("current")
_VlanGlobal_ObjectIdentity = ObjectIdentity
vlanGlobal = _VlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 3)
)


class _VlanStagTpid_Type(Unsigned32):
    """Custom type vlanStagTpid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 65535),
    )


_VlanStagTpid_Type.__name__ = "Unsigned32"
_VlanStagTpid_Object = MibScalar
vlanStagTpid = _VlanStagTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 3, 1),
    _VlanStagTpid_Type()
)
vlanStagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStagTpid.setStatus("current")


class _VlanSingleTagMode_Type(Integer32):
    """Custom type vlanSingleTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stag", 1),
          ("ctag", 2))
    )


_VlanSingleTagMode_Type.__name__ = "Integer32"
_VlanSingleTagMode_Object = MibScalar
vlanSingleTagMode = _VlanSingleTagMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 3, 2),
    _VlanSingleTagMode_Type()
)
vlanSingleTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSingleTagMode.setStatus("current")
_VlanUplink_ObjectIdentity = ObjectIdentity
vlanUplink = _VlanUplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4)
)
_VlanUplinkTable_Object = MibTable
vlanUplinkTable = _VlanUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 1)
)
if mibBuilder.loadTexts:
    vlanUplinkTable.setStatus("current")
_VlanUplinkEntry_Object = MibTableRow
vlanUplinkEntry = _VlanUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 1, 1)
)
vlanUplinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "vlanUplinkVlanId"),
)
if mibBuilder.loadTexts:
    vlanUplinkEntry.setStatus("current")


class _VlanUplinkVlanId_Type(VlanIndex):
    """Custom type vlanUplinkVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanUplinkVlanId_Type.__name__ = "VlanIndex"
_VlanUplinkVlanId_Object = MibTableColumn
vlanUplinkVlanId = _VlanUplinkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 1, 1, 1),
    _VlanUplinkVlanId_Type()
)
vlanUplinkVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanUplinkVlanId.setStatus("current")
_VlanUplinkRowStatus_Type = RowStatus
_VlanUplinkRowStatus_Object = MibTableColumn
vlanUplinkRowStatus = _VlanUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 1, 1, 2),
    _VlanUplinkRowStatus_Type()
)
vlanUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanUplinkRowStatus.setStatus("current")
_VlanUplinkJoinAllTable_Object = MibTable
vlanUplinkJoinAllTable = _VlanUplinkJoinAllTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 2)
)
if mibBuilder.loadTexts:
    vlanUplinkJoinAllTable.setStatus("current")
_VlanUplinkJoinAllEntry_Object = MibTableRow
vlanUplinkJoinAllEntry = _VlanUplinkJoinAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 2, 1)
)
vlanUplinkJoinAllEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanUplinkJoinAllEntry.setStatus("current")


class _VlanUplinkJoinAllEnable_Type(Integer32):
    """Custom type vlanUplinkJoinAllEnable based on Integer32"""
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


_VlanUplinkJoinAllEnable_Type.__name__ = "Integer32"
_VlanUplinkJoinAllEnable_Object = MibTableColumn
vlanUplinkJoinAllEnable = _VlanUplinkJoinAllEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 2, 1, 2),
    _VlanUplinkJoinAllEnable_Type()
)
vlanUplinkJoinAllEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanUplinkJoinAllEnable.setStatus("current")
_VlanUplinkMaxNumOfUntagPerPort_Type = Integer32
_VlanUplinkMaxNumOfUntagPerPort_Object = MibScalar
vlanUplinkMaxNumOfUntagPerPort = _VlanUplinkMaxNumOfUntagPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 3),
    _VlanUplinkMaxNumOfUntagPerPort_Type()
)
vlanUplinkMaxNumOfUntagPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanUplinkMaxNumOfUntagPerPort.setStatus("current")
_VlanUplinkUntagTable_Object = MibTable
vlanUplinkUntagTable = _VlanUplinkUntagTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 4)
)
if mibBuilder.loadTexts:
    vlanUplinkUntagTable.setStatus("current")
_VlanUplinkUntagEntry_Object = MibTableRow
vlanUplinkUntagEntry = _VlanUplinkUntagEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 4, 1)
)
vlanUplinkUntagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "vlanUplinkUntagVlanId"),
)
if mibBuilder.loadTexts:
    vlanUplinkUntagEntry.setStatus("current")


class _VlanUplinkUntagVlanId_Type(Integer32):
    """Custom type vlanUplinkUntagVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanUplinkUntagVlanId_Type.__name__ = "Integer32"
_VlanUplinkUntagVlanId_Object = MibTableColumn
vlanUplinkUntagVlanId = _VlanUplinkUntagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 4, 1, 1),
    _VlanUplinkUntagVlanId_Type()
)
vlanUplinkUntagVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanUplinkUntagVlanId.setStatus("current")


class _VlanUplinkUntagVlanPbit_Type(Integer32):
    """Custom type vlanUplinkUntagVlanPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanUplinkUntagVlanPbit_Type.__name__ = "Integer32"
_VlanUplinkUntagVlanPbit_Object = MibTableColumn
vlanUplinkUntagVlanPbit = _VlanUplinkUntagVlanPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 4, 1, 2),
    _VlanUplinkUntagVlanPbit_Type()
)
vlanUplinkUntagVlanPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanUplinkUntagVlanPbit.setStatus("current")
_VlanUplinkUntagRowStatus_Type = RowStatus
_VlanUplinkUntagRowStatus_Object = MibTableColumn
vlanUplinkUntagRowStatus = _VlanUplinkUntagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 4, 4, 1, 3),
    _VlanUplinkUntagRowStatus_Type()
)
vlanUplinkUntagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanUplinkUntagRowStatus.setStatus("current")
_VlanTransparent_ObjectIdentity = ObjectIdentity
vlanTransparent = _VlanTransparent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5)
)
_VlanTransparentPortTable_Object = MibTable
vlanTransparentPortTable = _VlanTransparentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTransparentPortTable.setStatus("current")
_VlanTransparentPortEntry_Object = MibTableRow
vlanTransparentPortEntry = _VlanTransparentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 1, 1)
)
vlanTransparentPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanTransparentPortEntry.setStatus("current")
_VlanTransparentPortRowStatus_Type = RowStatus
_VlanTransparentPortRowStatus_Object = MibTableColumn
vlanTransparentPortRowStatus = _VlanTransparentPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 1, 1, 1),
    _VlanTransparentPortRowStatus_Type()
)
vlanTransparentPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTransparentPortRowStatus.setStatus("current")
_VlanTransparentVcTable_Object = MibTable
vlanTransparentVcTable = _VlanTransparentVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 2)
)
if mibBuilder.loadTexts:
    vlanTransparentVcTable.setStatus("current")
_VlanTransparentVcEntry_Object = MibTableRow
vlanTransparentVcEntry = _VlanTransparentVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 2, 1)
)
vlanTransparentVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    vlanTransparentVcEntry.setStatus("current")
_VlanTransparentVcRowStatus_Type = RowStatus
_VlanTransparentVcRowStatus_Object = MibTableColumn
vlanTransparentVcRowStatus = _VlanTransparentVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 5, 2, 1, 1),
    _VlanTransparentVcRowStatus_Type()
)
vlanTransparentVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTransparentVcRowStatus.setStatus("current")
_VlanTrunk_ObjectIdentity = ObjectIdentity
vlanTrunk = _VlanTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6)
)
_VlanTrunkUntagPortTable_Object = MibTable
vlanTrunkUntagPortTable = _VlanTrunkUntagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkUntagPortTable.setStatus("current")
_VlanTrunkUntagPortEntry_Object = MibTableRow
vlanTrunkUntagPortEntry = _VlanTrunkUntagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1)
)
vlanTrunkUntagPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanTrunkUntagPortEntry.setStatus("current")


class _VlanTrunkUntagPortMode_Type(Integer32):
    """Custom type vlanTrunkUntagPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkUntagPortMode_Type.__name__ = "Integer32"
_VlanTrunkUntagPortMode_Object = MibTableColumn
vlanTrunkUntagPortMode = _VlanTrunkUntagPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 1),
    _VlanTrunkUntagPortMode_Type()
)
vlanTrunkUntagPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortMode.setStatus("current")


class _VlanTrunkUntagPortNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagPortNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagPortNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagPortNniSvlan_Object = MibTableColumn
vlanTrunkUntagPortNniSvlan = _VlanTrunkUntagPortNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 2),
    _VlanTrunkUntagPortNniSvlan_Type()
)
vlanTrunkUntagPortNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortNniSvlan.setStatus("current")


class _VlanTrunkUntagPortNniSpbit_Type(Integer32):
    """Custom type vlanTrunkUntagPortNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagPortNniSpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagPortNniSpbit_Object = MibTableColumn
vlanTrunkUntagPortNniSpbit = _VlanTrunkUntagPortNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 3),
    _VlanTrunkUntagPortNniSpbit_Type()
)
vlanTrunkUntagPortNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortNniSpbit.setStatus("current")


class _VlanTrunkUntagPortNniCvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagPortNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagPortNniCvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagPortNniCvlan_Object = MibTableColumn
vlanTrunkUntagPortNniCvlan = _VlanTrunkUntagPortNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 4),
    _VlanTrunkUntagPortNniCvlan_Type()
)
vlanTrunkUntagPortNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortNniCvlan.setStatus("current")


class _VlanTrunkUntagPortNniCpbit_Type(Integer32):
    """Custom type vlanTrunkUntagPortNniCpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagPortNniCpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagPortNniCpbit_Object = MibTableColumn
vlanTrunkUntagPortNniCpbit = _VlanTrunkUntagPortNniCpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 5),
    _VlanTrunkUntagPortNniCpbit_Type()
)
vlanTrunkUntagPortNniCpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortNniCpbit.setStatus("current")
_VlanTrunkUntagPortRowStatus_Type = RowStatus
_VlanTrunkUntagPortRowStatus_Object = MibTableColumn
vlanTrunkUntagPortRowStatus = _VlanTrunkUntagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 1, 1, 6),
    _VlanTrunkUntagPortRowStatus_Type()
)
vlanTrunkUntagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagPortRowStatus.setStatus("current")
_VlanTrunkUntagEtypePortTable_Object = MibTable
vlanTrunkUntagEtypePortTable = _VlanTrunkUntagEtypePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2)
)
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortTable.setStatus("current")
_VlanTrunkUntagEtypePortEntry_Object = MibTableRow
vlanTrunkUntagEtypePortEntry = _VlanTrunkUntagEtypePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1)
)
vlanTrunkUntagEtypePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "vlanTrunkUntagEtypePortEtype"),
)
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortEntry.setStatus("current")


class _VlanTrunkUntagEtypePortEtype_Type(Unsigned32):
    """Custom type vlanTrunkUntagEtypePortEtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanTrunkUntagEtypePortEtype_Type.__name__ = "Unsigned32"
_VlanTrunkUntagEtypePortEtype_Object = MibTableColumn
vlanTrunkUntagEtypePortEtype = _VlanTrunkUntagEtypePortEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 1),
    _VlanTrunkUntagEtypePortEtype_Type()
)
vlanTrunkUntagEtypePortEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortEtype.setStatus("current")


class _VlanTrunkUntagEtypePortMode_Type(Integer32):
    """Custom type vlanTrunkUntagEtypePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkUntagEtypePortMode_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypePortMode_Object = MibTableColumn
vlanTrunkUntagEtypePortMode = _VlanTrunkUntagEtypePortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 2),
    _VlanTrunkUntagEtypePortMode_Type()
)
vlanTrunkUntagEtypePortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortMode.setStatus("current")


class _VlanTrunkUntagEtypePortNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagEtypePortNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagEtypePortNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagEtypePortNniSvlan_Object = MibTableColumn
vlanTrunkUntagEtypePortNniSvlan = _VlanTrunkUntagEtypePortNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 3),
    _VlanTrunkUntagEtypePortNniSvlan_Type()
)
vlanTrunkUntagEtypePortNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortNniSvlan.setStatus("current")


class _VlanTrunkUntagEtypePortNniSpbit_Type(Integer32):
    """Custom type vlanTrunkUntagEtypePortNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagEtypePortNniSpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypePortNniSpbit_Object = MibTableColumn
vlanTrunkUntagEtypePortNniSpbit = _VlanTrunkUntagEtypePortNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 4),
    _VlanTrunkUntagEtypePortNniSpbit_Type()
)
vlanTrunkUntagEtypePortNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortNniSpbit.setStatus("current")


class _VlanTrunkUntagEtypePortNniCvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagEtypePortNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagEtypePortNniCvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagEtypePortNniCvlan_Object = MibTableColumn
vlanTrunkUntagEtypePortNniCvlan = _VlanTrunkUntagEtypePortNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 5),
    _VlanTrunkUntagEtypePortNniCvlan_Type()
)
vlanTrunkUntagEtypePortNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortNniCvlan.setStatus("current")


class _VlanTrunkUntagEtypePortNniCpbit_Type(Integer32):
    """Custom type vlanTrunkUntagEtypePortNniCpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagEtypePortNniCpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypePortNniCpbit_Object = MibTableColumn
vlanTrunkUntagEtypePortNniCpbit = _VlanTrunkUntagEtypePortNniCpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 6),
    _VlanTrunkUntagEtypePortNniCpbit_Type()
)
vlanTrunkUntagEtypePortNniCpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortNniCpbit.setStatus("current")
_VlanTrunkUntagEtypePortRowStatus_Type = RowStatus
_VlanTrunkUntagEtypePortRowStatus_Object = MibTableColumn
vlanTrunkUntagEtypePortRowStatus = _VlanTrunkUntagEtypePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 2, 1, 7),
    _VlanTrunkUntagEtypePortRowStatus_Type()
)
vlanTrunkUntagEtypePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypePortRowStatus.setStatus("current")
_VlanTrunkTagPortTable_Object = MibTable
vlanTrunkTagPortTable = _VlanTrunkTagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3)
)
if mibBuilder.loadTexts:
    vlanTrunkTagPortTable.setStatus("current")
_VlanTrunkTagPortEntry_Object = MibTableRow
vlanTrunkTagPortEntry = _VlanTrunkTagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3, 1)
)
vlanTrunkTagPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "vlanTrunkTagPortUniNniVlan"),
)
if mibBuilder.loadTexts:
    vlanTrunkTagPortEntry.setStatus("current")


class _VlanTrunkTagPortUniNniVlan_Type(VlanIndex):
    """Custom type vlanTrunkTagPortUniNniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkTagPortUniNniVlan_Type.__name__ = "VlanIndex"
_VlanTrunkTagPortUniNniVlan_Object = MibTableColumn
vlanTrunkTagPortUniNniVlan = _VlanTrunkTagPortUniNniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3, 1, 1),
    _VlanTrunkTagPortUniNniVlan_Type()
)
vlanTrunkTagPortUniNniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkTagPortUniNniVlan.setStatus("current")


class _VlanTrunkTagPortMode_Type(Integer32):
    """Custom type vlanTrunkTagPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkTagPortMode_Type.__name__ = "Integer32"
_VlanTrunkTagPortMode_Object = MibTableColumn
vlanTrunkTagPortMode = _VlanTrunkTagPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3, 1, 2),
    _VlanTrunkTagPortMode_Type()
)
vlanTrunkTagPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagPortMode.setStatus("current")


class _VlanTrunkTagPortNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkTagPortNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkTagPortNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkTagPortNniSvlan_Object = MibTableColumn
vlanTrunkTagPortNniSvlan = _VlanTrunkTagPortNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3, 1, 3),
    _VlanTrunkTagPortNniSvlan_Type()
)
vlanTrunkTagPortNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagPortNniSvlan.setStatus("current")
_VlanTrunkTagPortRowStatus_Type = RowStatus
_VlanTrunkTagPortRowStatus_Object = MibTableColumn
vlanTrunkTagPortRowStatus = _VlanTrunkTagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 3, 1, 4),
    _VlanTrunkTagPortRowStatus_Type()
)
vlanTrunkTagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagPortRowStatus.setStatus("current")
_VlanTrunkUntagVcTable_Object = MibTable
vlanTrunkUntagVcTable = _VlanTrunkUntagVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4)
)
if mibBuilder.loadTexts:
    vlanTrunkUntagVcTable.setStatus("current")
_VlanTrunkUntagVcEntry_Object = MibTableRow
vlanTrunkUntagVcEntry = _VlanTrunkUntagVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1)
)
vlanTrunkUntagVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    vlanTrunkUntagVcEntry.setStatus("current")


class _VlanTrunkUntagVcMode_Type(Integer32):
    """Custom type vlanTrunkUntagVcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkUntagVcMode_Type.__name__ = "Integer32"
_VlanTrunkUntagVcMode_Object = MibTableColumn
vlanTrunkUntagVcMode = _VlanTrunkUntagVcMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 1),
    _VlanTrunkUntagVcMode_Type()
)
vlanTrunkUntagVcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcMode.setStatus("current")


class _VlanTrunkUntagVcNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagVcNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagVcNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagVcNniSvlan_Object = MibTableColumn
vlanTrunkUntagVcNniSvlan = _VlanTrunkUntagVcNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 2),
    _VlanTrunkUntagVcNniSvlan_Type()
)
vlanTrunkUntagVcNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcNniSvlan.setStatus("current")


class _VlanTrunkUntagVcNniSpbit_Type(Integer32):
    """Custom type vlanTrunkUntagVcNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagVcNniSpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagVcNniSpbit_Object = MibTableColumn
vlanTrunkUntagVcNniSpbit = _VlanTrunkUntagVcNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 3),
    _VlanTrunkUntagVcNniSpbit_Type()
)
vlanTrunkUntagVcNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcNniSpbit.setStatus("current")


class _VlanTrunkUntagVcNniCvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagVcNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagVcNniCvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagVcNniCvlan_Object = MibTableColumn
vlanTrunkUntagVcNniCvlan = _VlanTrunkUntagVcNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 4),
    _VlanTrunkUntagVcNniCvlan_Type()
)
vlanTrunkUntagVcNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcNniCvlan.setStatus("current")


class _VlanTrunkUntagVcNniCpbit_Type(Integer32):
    """Custom type vlanTrunkUntagVcNniCpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagVcNniCpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagVcNniCpbit_Object = MibTableColumn
vlanTrunkUntagVcNniCpbit = _VlanTrunkUntagVcNniCpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 5),
    _VlanTrunkUntagVcNniCpbit_Type()
)
vlanTrunkUntagVcNniCpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcNniCpbit.setStatus("current")
_VlanTrunkUntagVcRowStatus_Type = RowStatus
_VlanTrunkUntagVcRowStatus_Object = MibTableColumn
vlanTrunkUntagVcRowStatus = _VlanTrunkUntagVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 4, 1, 6),
    _VlanTrunkUntagVcRowStatus_Type()
)
vlanTrunkUntagVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagVcRowStatus.setStatus("current")
_VlanTrunkUntagEtypeVcTable_Object = MibTable
vlanTrunkUntagEtypeVcTable = _VlanTrunkUntagEtypeVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5)
)
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcTable.setStatus("current")
_VlanTrunkUntagEtypeVcEntry_Object = MibTableRow
vlanTrunkUntagEtypeVcEntry = _VlanTrunkUntagEtypeVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1)
)
vlanTrunkUntagEtypeVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
    (0, "VES1724-58V-MIB", "vlanTrunkUntagEtypeVcEtype"),
)
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcEntry.setStatus("current")


class _VlanTrunkUntagEtypeVcEtype_Type(Unsigned32):
    """Custom type vlanTrunkUntagEtypeVcEtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanTrunkUntagEtypeVcEtype_Type.__name__ = "Unsigned32"
_VlanTrunkUntagEtypeVcEtype_Object = MibTableColumn
vlanTrunkUntagEtypeVcEtype = _VlanTrunkUntagEtypeVcEtype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 1),
    _VlanTrunkUntagEtypeVcEtype_Type()
)
vlanTrunkUntagEtypeVcEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcEtype.setStatus("current")


class _VlanTrunkUntagEtypeVcMode_Type(Integer32):
    """Custom type vlanTrunkUntagEtypeVcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkUntagEtypeVcMode_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypeVcMode_Object = MibTableColumn
vlanTrunkUntagEtypeVcMode = _VlanTrunkUntagEtypeVcMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 2),
    _VlanTrunkUntagEtypeVcMode_Type()
)
vlanTrunkUntagEtypeVcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcMode.setStatus("current")


class _VlanTrunkUntagEtypeVcNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagEtypeVcNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagEtypeVcNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagEtypeVcNniSvlan_Object = MibTableColumn
vlanTrunkUntagEtypeVcNniSvlan = _VlanTrunkUntagEtypeVcNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 3),
    _VlanTrunkUntagEtypeVcNniSvlan_Type()
)
vlanTrunkUntagEtypeVcNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcNniSvlan.setStatus("current")


class _VlanTrunkUntagEtypeVcNniSpbit_Type(Integer32):
    """Custom type vlanTrunkUntagEtypeVcNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagEtypeVcNniSpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypeVcNniSpbit_Object = MibTableColumn
vlanTrunkUntagEtypeVcNniSpbit = _VlanTrunkUntagEtypeVcNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 4),
    _VlanTrunkUntagEtypeVcNniSpbit_Type()
)
vlanTrunkUntagEtypeVcNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcNniSpbit.setStatus("current")


class _VlanTrunkUntagEtypeVcNniCvlan_Type(VlanIndex):
    """Custom type vlanTrunkUntagEtypeVcNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkUntagEtypeVcNniCvlan_Type.__name__ = "VlanIndex"
_VlanTrunkUntagEtypeVcNniCvlan_Object = MibTableColumn
vlanTrunkUntagEtypeVcNniCvlan = _VlanTrunkUntagEtypeVcNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 5),
    _VlanTrunkUntagEtypeVcNniCvlan_Type()
)
vlanTrunkUntagEtypeVcNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcNniCvlan.setStatus("current")


class _VlanTrunkUntagEtypeVcNniCpbit_Type(Integer32):
    """Custom type vlanTrunkUntagEtypeVcNniCpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTrunkUntagEtypeVcNniCpbit_Type.__name__ = "Integer32"
_VlanTrunkUntagEtypeVcNniCpbit_Object = MibTableColumn
vlanTrunkUntagEtypeVcNniCpbit = _VlanTrunkUntagEtypeVcNniCpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 6),
    _VlanTrunkUntagEtypeVcNniCpbit_Type()
)
vlanTrunkUntagEtypeVcNniCpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcNniCpbit.setStatus("current")
_VlanTrunkUntagEtypeVcRowStatus_Type = RowStatus
_VlanTrunkUntagEtypeVcRowStatus_Object = MibTableColumn
vlanTrunkUntagEtypeVcRowStatus = _VlanTrunkUntagEtypeVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 5, 1, 7),
    _VlanTrunkUntagEtypeVcRowStatus_Type()
)
vlanTrunkUntagEtypeVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkUntagEtypeVcRowStatus.setStatus("current")
_VlanTrunkTagVcTable_Object = MibTable
vlanTrunkTagVcTable = _VlanTrunkTagVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6)
)
if mibBuilder.loadTexts:
    vlanTrunkTagVcTable.setStatus("current")
_VlanTrunkTagVcEntry_Object = MibTableRow
vlanTrunkTagVcEntry = _VlanTrunkTagVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6, 1)
)
vlanTrunkTagVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
    (0, "VES1724-58V-MIB", "vlanTrunkTagVcUniNniVlan"),
)
if mibBuilder.loadTexts:
    vlanTrunkTagVcEntry.setStatus("current")


class _VlanTrunkTagVcUniNniVlan_Type(VlanIndex):
    """Custom type vlanTrunkTagVcUniNniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkTagVcUniNniVlan_Type.__name__ = "VlanIndex"
_VlanTrunkTagVcUniNniVlan_Object = MibTableColumn
vlanTrunkTagVcUniNniVlan = _VlanTrunkTagVcUniNniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6, 1, 1),
    _VlanTrunkTagVcUniNniVlan_Type()
)
vlanTrunkTagVcUniNniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkTagVcUniNniVlan.setStatus("current")


class _VlanTrunkTagVcMode_Type(Integer32):
    """Custom type vlanTrunkTagVcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTrunkTagVcMode_Type.__name__ = "Integer32"
_VlanTrunkTagVcMode_Object = MibTableColumn
vlanTrunkTagVcMode = _VlanTrunkTagVcMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6, 1, 2),
    _VlanTrunkTagVcMode_Type()
)
vlanTrunkTagVcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagVcMode.setStatus("current")


class _VlanTrunkTagVcNniSvlan_Type(VlanIndex):
    """Custom type vlanTrunkTagVcNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTrunkTagVcNniSvlan_Type.__name__ = "VlanIndex"
_VlanTrunkTagVcNniSvlan_Object = MibTableColumn
vlanTrunkTagVcNniSvlan = _VlanTrunkTagVcNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6, 1, 3),
    _VlanTrunkTagVcNniSvlan_Type()
)
vlanTrunkTagVcNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagVcNniSvlan.setStatus("current")
_VlanTrunkTagVcRowStatus_Type = RowStatus
_VlanTrunkTagVcRowStatus_Object = MibTableColumn
vlanTrunkTagVcRowStatus = _VlanTrunkTagVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 6, 6, 1, 4),
    _VlanTrunkTagVcRowStatus_Type()
)
vlanTrunkTagVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkTagVcRowStatus.setStatus("current")
_VlanTranslation_ObjectIdentity = ObjectIdentity
vlanTranslation = _VlanTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7)
)
_VlanTranslationPortTable_Object = MibTable
vlanTranslationPortTable = _VlanTranslationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1)
)
if mibBuilder.loadTexts:
    vlanTranslationPortTable.setStatus("current")
_VlanTranslationPortEntry_Object = MibTableRow
vlanTranslationPortEntry = _VlanTranslationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1)
)
vlanTranslationPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "vlanTranslationPortUniVlan"),
)
if mibBuilder.loadTexts:
    vlanTranslationPortEntry.setStatus("current")


class _VlanTranslationPortUniVlan_Type(VlanIndex):
    """Custom type vlanTranslationPortUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationPortUniVlan_Type.__name__ = "VlanIndex"
_VlanTranslationPortUniVlan_Object = MibTableColumn
vlanTranslationPortUniVlan = _VlanTranslationPortUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1, 1),
    _VlanTranslationPortUniVlan_Type()
)
vlanTranslationPortUniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationPortUniVlan.setStatus("current")


class _VlanTranslationPortMode_Type(Integer32):
    """Custom type vlanTranslationPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTranslationPortMode_Type.__name__ = "Integer32"
_VlanTranslationPortMode_Object = MibTableColumn
vlanTranslationPortMode = _VlanTranslationPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1, 2),
    _VlanTranslationPortMode_Type()
)
vlanTranslationPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationPortMode.setStatus("current")


class _VlanTranslationPortNniSvlan_Type(VlanIndex):
    """Custom type vlanTranslationPortNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationPortNniSvlan_Type.__name__ = "VlanIndex"
_VlanTranslationPortNniSvlan_Object = MibTableColumn
vlanTranslationPortNniSvlan = _VlanTranslationPortNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1, 3),
    _VlanTranslationPortNniSvlan_Type()
)
vlanTranslationPortNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationPortNniSvlan.setStatus("current")


class _VlanTranslationPortNniCvlan_Type(VlanIndex):
    """Custom type vlanTranslationPortNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationPortNniCvlan_Type.__name__ = "VlanIndex"
_VlanTranslationPortNniCvlan_Object = MibTableColumn
vlanTranslationPortNniCvlan = _VlanTranslationPortNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1, 4),
    _VlanTranslationPortNniCvlan_Type()
)
vlanTranslationPortNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationPortNniCvlan.setStatus("current")
_VlanTranslationPortRowStatus_Type = RowStatus
_VlanTranslationPortRowStatus_Object = MibTableColumn
vlanTranslationPortRowStatus = _VlanTranslationPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 1, 1, 5),
    _VlanTranslationPortRowStatus_Type()
)
vlanTranslationPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationPortRowStatus.setStatus("current")
_VlanTranslationVcTable_Object = MibTable
vlanTranslationVcTable = _VlanTranslationVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2)
)
if mibBuilder.loadTexts:
    vlanTranslationVcTable.setStatus("current")
_VlanTranslationVcEntry_Object = MibTableRow
vlanTranslationVcEntry = _VlanTranslationVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1)
)
vlanTranslationVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
    (0, "VES1724-58V-MIB", "vlanTranslationVcUniVlan"),
)
if mibBuilder.loadTexts:
    vlanTranslationVcEntry.setStatus("current")


class _VlanTranslationVcUniVlan_Type(VlanIndex):
    """Custom type vlanTranslationVcUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationVcUniVlan_Type.__name__ = "VlanIndex"
_VlanTranslationVcUniVlan_Object = MibTableColumn
vlanTranslationVcUniVlan = _VlanTranslationVcUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1, 1),
    _VlanTranslationVcUniVlan_Type()
)
vlanTranslationVcUniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationVcUniVlan.setStatus("current")


class _VlanTranslationVcMode_Type(Integer32):
    """Custom type vlanTranslationVcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2))
    )


_VlanTranslationVcMode_Type.__name__ = "Integer32"
_VlanTranslationVcMode_Object = MibTableColumn
vlanTranslationVcMode = _VlanTranslationVcMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1, 2),
    _VlanTranslationVcMode_Type()
)
vlanTranslationVcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationVcMode.setStatus("current")


class _VlanTranslationVcNniSvlan_Type(VlanIndex):
    """Custom type vlanTranslationVcNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationVcNniSvlan_Type.__name__ = "VlanIndex"
_VlanTranslationVcNniSvlan_Object = MibTableColumn
vlanTranslationVcNniSvlan = _VlanTranslationVcNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1, 3),
    _VlanTranslationVcNniSvlan_Type()
)
vlanTranslationVcNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationVcNniSvlan.setStatus("current")


class _VlanTranslationVcNniCvlan_Type(VlanIndex):
    """Custom type vlanTranslationVcNniCvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTranslationVcNniCvlan_Type.__name__ = "VlanIndex"
_VlanTranslationVcNniCvlan_Object = MibTableColumn
vlanTranslationVcNniCvlan = _VlanTranslationVcNniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1, 4),
    _VlanTranslationVcNniCvlan_Type()
)
vlanTranslationVcNniCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationVcNniCvlan.setStatus("current")
_VlanTranslationVcRowStatus_Type = RowStatus
_VlanTranslationVcRowStatus_Object = MibTableColumn
vlanTranslationVcRowStatus = _VlanTranslationVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 7, 2, 1, 5),
    _VlanTranslationVcRowStatus_Type()
)
vlanTranslationVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationVcRowStatus.setStatus("current")
_VlanTls_ObjectIdentity = ObjectIdentity
vlanTls = _VlanTls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8)
)
_VlanTlsPortTable_Object = MibTable
vlanTlsPortTable = _VlanTlsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1)
)
if mibBuilder.loadTexts:
    vlanTlsPortTable.setStatus("current")
_VlanTlsPortEntry_Object = MibTableRow
vlanTlsPortEntry = _VlanTlsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1, 1)
)
vlanTlsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanTlsPortEntry.setStatus("current")


class _VlanTlsPortNniSvlan_Type(VlanIndex):
    """Custom type vlanTlsPortNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTlsPortNniSvlan_Type.__name__ = "VlanIndex"
_VlanTlsPortNniSvlan_Object = MibTableColumn
vlanTlsPortNniSvlan = _VlanTlsPortNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1, 1, 1),
    _VlanTlsPortNniSvlan_Type()
)
vlanTlsPortNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsPortNniSvlan.setStatus("current")


class _VlanTlsPortNniSpbit_Type(Integer32):
    """Custom type vlanTlsPortNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTlsPortNniSpbit_Type.__name__ = "Integer32"
_VlanTlsPortNniSpbit_Object = MibTableColumn
vlanTlsPortNniSpbit = _VlanTlsPortNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1, 1, 2),
    _VlanTlsPortNniSpbit_Type()
)
vlanTlsPortNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsPortNniSpbit.setStatus("current")


class _VlanTlsPortNniForceSpbit_Type(Integer32):
    """Custom type vlanTlsPortNniForceSpbit based on Integer32"""
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


_VlanTlsPortNniForceSpbit_Type.__name__ = "Integer32"
_VlanTlsPortNniForceSpbit_Object = MibTableColumn
vlanTlsPortNniForceSpbit = _VlanTlsPortNniForceSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1, 1, 3),
    _VlanTlsPortNniForceSpbit_Type()
)
vlanTlsPortNniForceSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsPortNniForceSpbit.setStatus("current")
_VlanTlsPortRowStatus_Type = RowStatus
_VlanTlsPortRowStatus_Object = MibTableColumn
vlanTlsPortRowStatus = _VlanTlsPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 1, 1, 4),
    _VlanTlsPortRowStatus_Type()
)
vlanTlsPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsPortRowStatus.setStatus("current")
_VlanTlsVcTable_Object = MibTable
vlanTlsVcTable = _VlanTlsVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2)
)
if mibBuilder.loadTexts:
    vlanTlsVcTable.setStatus("current")
_VlanTlsVcEntry_Object = MibTableRow
vlanTlsVcEntry = _VlanTlsVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2, 1)
)
vlanTlsVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    vlanTlsVcEntry.setStatus("current")


class _VlanTlsVcNniSvlan_Type(VlanIndex):
    """Custom type vlanTlsVcNniSvlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VlanTlsVcNniSvlan_Type.__name__ = "VlanIndex"
_VlanTlsVcNniSvlan_Object = MibTableColumn
vlanTlsVcNniSvlan = _VlanTlsVcNniSvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2, 1, 1),
    _VlanTlsVcNniSvlan_Type()
)
vlanTlsVcNniSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsVcNniSvlan.setStatus("current")


class _VlanTlsVcNniSpbit_Type(Integer32):
    """Custom type vlanTlsVcNniSpbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTlsVcNniSpbit_Type.__name__ = "Integer32"
_VlanTlsVcNniSpbit_Object = MibTableColumn
vlanTlsVcNniSpbit = _VlanTlsVcNniSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2, 1, 2),
    _VlanTlsVcNniSpbit_Type()
)
vlanTlsVcNniSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsVcNniSpbit.setStatus("current")


class _VlanTlsVcNniForceSpbit_Type(Integer32):
    """Custom type vlanTlsVcNniForceSpbit based on Integer32"""
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


_VlanTlsVcNniForceSpbit_Type.__name__ = "Integer32"
_VlanTlsVcNniForceSpbit_Object = MibTableColumn
vlanTlsVcNniForceSpbit = _VlanTlsVcNniForceSpbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2, 1, 3),
    _VlanTlsVcNniForceSpbit_Type()
)
vlanTlsVcNniForceSpbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsVcNniForceSpbit.setStatus("current")
_VlanTlsVcRowStatus_Type = RowStatus
_VlanTlsVcRowStatus_Object = MibTableColumn
vlanTlsVcRowStatus = _VlanTlsVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 8, 2, 1, 4),
    _VlanTlsVcRowStatus_Type()
)
vlanTlsVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTlsVcRowStatus.setStatus("current")
_Fdb_ObjectIdentity = ObjectIdentity
fdb = _Fdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9)
)


class _FdbAgingTime_Type(Integer32):
    """Custom type fdbAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_FdbAgingTime_Type.__name__ = "Integer32"
_FdbAgingTime_Object = MibScalar
fdbAgingTime = _FdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 1),
    _FdbAgingTime_Type()
)
fdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    fdbAgingTime.setUnits("second")
_FdbOps_ObjectIdentity = ObjectIdentity
fdbOps = _FdbOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 2)
)
_FdbTarget_Type = PortList
_FdbTarget_Object = MibScalar
fdbTarget = _FdbTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 2, 1),
    _FdbTarget_Type()
)
fdbTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbTarget.setStatus("current")


class _FdbOperation_Type(Integer32):
    """Custom type fdbOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushFDBxAddressTable", 1),
          ("flushFDBAddressTableForSpecifiedUNIxPorts", 2))
    )


_FdbOperation_Type.__name__ = "Integer32"
_FdbOperation_Object = MibScalar
fdbOperation = _FdbOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 2, 2),
    _FdbOperation_Type()
)
fdbOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbOperation.setStatus("current")
_FdbPortConfTable_Object = MibTable
fdbPortConfTable = _FdbPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 3)
)
if mibBuilder.loadTexts:
    fdbPortConfTable.setStatus("current")
_FdbPortConfEntry_Object = MibTableRow
fdbPortConfEntry = _FdbPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 3, 1)
)
fdbPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdbPortConfEntry.setStatus("current")


class _FdbPortConfMaxNumOfMacEntries_Type(Integer32):
    """Custom type fdbPortConfMaxNumOfMacEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FdbPortConfMaxNumOfMacEntries_Type.__name__ = "Integer32"
_FdbPortConfMaxNumOfMacEntries_Object = MibTableColumn
fdbPortConfMaxNumOfMacEntries = _FdbPortConfMaxNumOfMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 3, 1, 1),
    _FdbPortConfMaxNumOfMacEntries_Type()
)
fdbPortConfMaxNumOfMacEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbPortConfMaxNumOfMacEntries.setStatus("current")


class _FdbPortConfMacMode_Type(Integer32):
    """Custom type fdbPortConfMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicAndStaticMac", 1),
          ("staticMacOnly", 2))
    )


_FdbPortConfMacMode_Type.__name__ = "Integer32"
_FdbPortConfMacMode_Object = MibTableColumn
fdbPortConfMacMode = _FdbPortConfMacMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 3, 1, 2),
    _FdbPortConfMacMode_Type()
)
fdbPortConfMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbPortConfMacMode.setStatus("current")
_FdbPortUniVlanConfTable_Object = MibTable
fdbPortUniVlanConfTable = _FdbPortUniVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 5)
)
if mibBuilder.loadTexts:
    fdbPortUniVlanConfTable.setStatus("current")
_FdbPortUniVlanConfEntry_Object = MibTableRow
fdbPortUniVlanConfEntry = _FdbPortUniVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 5, 1)
)
fdbPortUniVlanConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "fdbPortVlanConfUniVlan"),
)
if mibBuilder.loadTexts:
    fdbPortUniVlanConfEntry.setStatus("current")


class _FdbPortVlanConfUniVlan_Type(VlanIndex):
    """Custom type fdbPortVlanConfUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_FdbPortVlanConfUniVlan_Type.__name__ = "VlanIndex"
_FdbPortVlanConfUniVlan_Object = MibTableColumn
fdbPortVlanConfUniVlan = _FdbPortVlanConfUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 5, 1, 1),
    _FdbPortVlanConfUniVlan_Type()
)
fdbPortVlanConfUniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbPortVlanConfUniVlan.setStatus("current")


class _FdbPortVlanConfMaxNumOfMacEntries_Type(Integer32):
    """Custom type fdbPortVlanConfMaxNumOfMacEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FdbPortVlanConfMaxNumOfMacEntries_Type.__name__ = "Integer32"
_FdbPortVlanConfMaxNumOfMacEntries_Object = MibTableColumn
fdbPortVlanConfMaxNumOfMacEntries = _FdbPortVlanConfMaxNumOfMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 5, 1, 2),
    _FdbPortVlanConfMaxNumOfMacEntries_Type()
)
fdbPortVlanConfMaxNumOfMacEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbPortVlanConfMaxNumOfMacEntries.setStatus("current")
_FdbPortVlanConfRowStatus_Type = RowStatus
_FdbPortVlanConfRowStatus_Object = MibTableColumn
fdbPortVlanConfRowStatus = _FdbPortVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 5, 1, 3),
    _FdbPortVlanConfRowStatus_Type()
)
fdbPortVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbPortVlanConfRowStatus.setStatus("current")
_FdbStaticMacTable_Object = MibTable
fdbStaticMacTable = _FdbStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6)
)
if mibBuilder.loadTexts:
    fdbStaticMacTable.setStatus("current")
_FdbStaticMacEntry_Object = MibTableRow
fdbStaticMacEntry = _FdbStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6, 1)
)
fdbStaticMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "fdbStaticMacMode"),
    (0, "VES1724-58V-MIB", "fdbStaticMacPhysAddress"),
    (0, "VES1724-58V-MIB", "fdbStaticMacVlanId"),
)
if mibBuilder.loadTexts:
    fdbStaticMacEntry.setStatus("current")


class _FdbStaticMacMode_Type(Integer32):
    """Custom type fdbStaticMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("svl", 1),
          ("ivl", 2))
    )


_FdbStaticMacMode_Type.__name__ = "Integer32"
_FdbStaticMacMode_Object = MibTableColumn
fdbStaticMacMode = _FdbStaticMacMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6, 1, 1),
    _FdbStaticMacMode_Type()
)
fdbStaticMacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStaticMacMode.setStatus("current")


class _FdbStaticMacVlanId_Type(VlanIndex):
    """Custom type fdbStaticMacVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_FdbStaticMacVlanId_Type.__name__ = "VlanIndex"
_FdbStaticMacVlanId_Object = MibTableColumn
fdbStaticMacVlanId = _FdbStaticMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6, 1, 2),
    _FdbStaticMacVlanId_Type()
)
fdbStaticMacVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStaticMacVlanId.setStatus("current")


class _FdbStaticMacPhysAddress_Type(PhysAddress):
    """Custom type fdbStaticMacPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FdbStaticMacPhysAddress_Type.__name__ = "PhysAddress"
_FdbStaticMacPhysAddress_Object = MibTableColumn
fdbStaticMacPhysAddress = _FdbStaticMacPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6, 1, 3),
    _FdbStaticMacPhysAddress_Type()
)
fdbStaticMacPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStaticMacPhysAddress.setStatus("current")
_FdbStaticMacRowStatus_Type = RowStatus
_FdbStaticMacRowStatus_Object = MibTableColumn
fdbStaticMacRowStatus = _FdbStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 6, 1, 4),
    _FdbStaticMacRowStatus_Type()
)
fdbStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbStaticMacRowStatus.setStatus("current")
_FdbMacLearningVlanTable_Object = MibTable
fdbMacLearningVlanTable = _FdbMacLearningVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7)
)
if mibBuilder.loadTexts:
    fdbMacLearningVlanTable.setStatus("current")
_FdbMacLearningVlanEntry_Object = MibTableRow
fdbMacLearningVlanEntry = _FdbMacLearningVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1)
)
fdbMacLearningVlanEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "fdbMacLearningVlanMode"),
    (0, "VES1724-58V-MIB", "fdbMacLearningVlanNniSVlan"),
    (0, "VES1724-58V-MIB", "fdbMacLearningVlanNniCVlan"),
    (0, "VES1724-58V-MIB", "fdbMacLearningVlanPhysAddress"),
)
if mibBuilder.loadTexts:
    fdbMacLearningVlanEntry.setStatus("current")


class _FdbMacLearningVlanMode_Type(Integer32):
    """Custom type fdbMacLearningVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sVlan", 1),
          ("sPlusCxVlan", 2),
          ("untag", 3))
    )


_FdbMacLearningVlanMode_Type.__name__ = "Integer32"
_FdbMacLearningVlanMode_Object = MibTableColumn
fdbMacLearningVlanMode = _FdbMacLearningVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 1),
    _FdbMacLearningVlanMode_Type()
)
fdbMacLearningVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanMode.setStatus("current")


class _FdbMacLearningVlanNniSVlan_Type(VlanIndex):
    """Custom type fdbMacLearningVlanNniSVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_FdbMacLearningVlanNniSVlan_Type.__name__ = "VlanIndex"
_FdbMacLearningVlanNniSVlan_Object = MibTableColumn
fdbMacLearningVlanNniSVlan = _FdbMacLearningVlanNniSVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 2),
    _FdbMacLearningVlanNniSVlan_Type()
)
fdbMacLearningVlanNniSVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanNniSVlan.setStatus("current")


class _FdbMacLearningVlanNniCVlan_Type(VlanIndex):
    """Custom type fdbMacLearningVlanNniCVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_FdbMacLearningVlanNniCVlan_Type.__name__ = "VlanIndex"
_FdbMacLearningVlanNniCVlan_Object = MibTableColumn
fdbMacLearningVlanNniCVlan = _FdbMacLearningVlanNniCVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 3),
    _FdbMacLearningVlanNniCVlan_Type()
)
fdbMacLearningVlanNniCVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanNniCVlan.setStatus("current")


class _FdbMacLearningVlanPhysAddress_Type(PhysAddress):
    """Custom type fdbMacLearningVlanPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FdbMacLearningVlanPhysAddress_Type.__name__ = "PhysAddress"
_FdbMacLearningVlanPhysAddress_Object = MibTableColumn
fdbMacLearningVlanPhysAddress = _FdbMacLearningVlanPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 4),
    _FdbMacLearningVlanPhysAddress_Type()
)
fdbMacLearningVlanPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanPhysAddress.setStatus("current")


class _FdbMacLearningVlanUniVlan_Type(VlanIndex):
    """Custom type fdbMacLearningVlanUniVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_FdbMacLearningVlanUniVlan_Type.__name__ = "VlanIndex"
_FdbMacLearningVlanUniVlan_Object = MibTableColumn
fdbMacLearningVlanUniVlan = _FdbMacLearningVlanUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 5),
    _FdbMacLearningVlanUniVlan_Type()
)
fdbMacLearningVlanUniVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanUniVlan.setStatus("current")
_FdbMacLearningVlanPort_Type = Integer32
_FdbMacLearningVlanPort_Object = MibTableColumn
fdbMacLearningVlanPort = _FdbMacLearningVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 6),
    _FdbMacLearningVlanPort_Type()
)
fdbMacLearningVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanPort.setStatus("current")


class _FdbMacLearningVlanType_Type(Integer32):
    """Custom type fdbMacLearningVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("staic", 2))
    )


_FdbMacLearningVlanType_Type.__name__ = "Integer32"
_FdbMacLearningVlanType_Object = MibTableColumn
fdbMacLearningVlanType = _FdbMacLearningVlanType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 7, 1, 7),
    _FdbMacLearningVlanType_Type()
)
fdbMacLearningVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacLearningVlanType.setStatus("current")


class _FdbAntiSpoofing_Type(Integer32):
    """Custom type fdbAntiSpoofing based on Integer32"""
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


_FdbAntiSpoofing_Type.__name__ = "Integer32"
_FdbAntiSpoofing_Object = MibScalar
fdbAntiSpoofing = _FdbAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 8),
    _FdbAntiSpoofing_Type()
)
fdbAntiSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAntiSpoofing.setStatus("current")


class _FdbSpoofingAction_Type(Integer32):
    """Custom type fdbSpoofingAction based on Integer32"""
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


_FdbSpoofingAction_Type.__name__ = "Integer32"
_FdbSpoofingAction_Object = MibScalar
fdbSpoofingAction = _FdbSpoofingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 9, 9),
    _FdbSpoofingAction_Type()
)
fdbSpoofingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbSpoofingAction.setStatus("current")


class _Mtu_Type(Integer32):
    """Custom type mtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2000),
    )


_Mtu_Type.__name__ = "Integer32"
_Mtu_Object = MibScalar
mtu = _Mtu_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 10),
    _Mtu_Type()
)
mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtu.setStatus("current")
_Mirror_ObjectIdentity = ObjectIdentity
mirror = _Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11)
)
_MirrorPortTable_Object = MibTable
mirrorPortTable = _MirrorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1)
)
if mibBuilder.loadTexts:
    mirrorPortTable.setStatus("current")
_MirrorPortEntry_Object = MibTableRow
mirrorPortEntry = _MirrorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1)
)
mirrorPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mirrorPortEntry.setStatus("current")
_MirrorPortDestPort_Type = Integer32
_MirrorPortDestPort_Object = MibTableColumn
mirrorPortDestPort = _MirrorPortDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1, 1),
    _MirrorPortDestPort_Type()
)
mirrorPortDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorPortDestPort.setStatus("current")


class _MirrorPortDestPortVpi_Type(Integer32):
    """Custom type mirrorPortDestPortVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MirrorPortDestPortVpi_Type.__name__ = "Integer32"
_MirrorPortDestPortVpi_Object = MibTableColumn
mirrorPortDestPortVpi = _MirrorPortDestPortVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1, 2),
    _MirrorPortDestPortVpi_Type()
)
mirrorPortDestPortVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorPortDestPortVpi.setStatus("current")


class _MirrorPortDestPortVci_Type(Integer32):
    """Custom type mirrorPortDestPortVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_MirrorPortDestPortVci_Type.__name__ = "Integer32"
_MirrorPortDestPortVci_Object = MibTableColumn
mirrorPortDestPortVci = _MirrorPortDestPortVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1, 3),
    _MirrorPortDestPortVci_Type()
)
mirrorPortDestPortVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorPortDestPortVci.setStatus("current")


class _MirrorPortDirection_Type(Integer32):
    """Custom type mirrorPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1),
          ("both", 2))
    )


_MirrorPortDirection_Type.__name__ = "Integer32"
_MirrorPortDirection_Object = MibTableColumn
mirrorPortDirection = _MirrorPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1, 4),
    _MirrorPortDirection_Type()
)
mirrorPortDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorPortDirection.setStatus("current")
_MirrorPortRowStatus_Type = RowStatus
_MirrorPortRowStatus_Object = MibTableColumn
mirrorPortRowStatus = _MirrorPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 1, 1, 5),
    _MirrorPortRowStatus_Type()
)
mirrorPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorPortRowStatus.setStatus("current")
_MirrorVcTable_Object = MibTable
mirrorVcTable = _MirrorVcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2)
)
if mibBuilder.loadTexts:
    mirrorVcTable.setStatus("current")
_MirrorVcEntry_Object = MibTableRow
mirrorVcEntry = _MirrorVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1)
)
mirrorVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    mirrorVcEntry.setStatus("current")
_MirrorVcDestPort_Type = Integer32
_MirrorVcDestPort_Object = MibTableColumn
mirrorVcDestPort = _MirrorVcDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1, 1),
    _MirrorVcDestPort_Type()
)
mirrorVcDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorVcDestPort.setStatus("current")


class _MirrorVcDestPortVpi_Type(Integer32):
    """Custom type mirrorVcDestPortVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MirrorVcDestPortVpi_Type.__name__ = "Integer32"
_MirrorVcDestPortVpi_Object = MibTableColumn
mirrorVcDestPortVpi = _MirrorVcDestPortVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1, 2),
    _MirrorVcDestPortVpi_Type()
)
mirrorVcDestPortVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorVcDestPortVpi.setStatus("current")


class _MirrorVcDestPortVci_Type(Integer32):
    """Custom type mirrorVcDestPortVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_MirrorVcDestPortVci_Type.__name__ = "Integer32"
_MirrorVcDestPortVci_Object = MibTableColumn
mirrorVcDestPortVci = _MirrorVcDestPortVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1, 3),
    _MirrorVcDestPortVci_Type()
)
mirrorVcDestPortVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorVcDestPortVci.setStatus("current")


class _MirrorVcDirection_Type(Integer32):
    """Custom type mirrorVcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1),
          ("both", 2))
    )


_MirrorVcDirection_Type.__name__ = "Integer32"
_MirrorVcDirection_Object = MibTableColumn
mirrorVcDirection = _MirrorVcDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1, 4),
    _MirrorVcDirection_Type()
)
mirrorVcDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorVcDirection.setStatus("current")
_MirrorVcRowStatus_Type = RowStatus
_MirrorVcRowStatus_Object = MibTableColumn
mirrorVcRowStatus = _MirrorVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 11, 11, 2, 1, 5),
    _MirrorVcRowStatus_Type()
)
mirrorVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorVcRowStatus.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1)
)
pppoeAgentEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "pppoeAgentVlanId"),
)
if mibBuilder.loadTexts:
    pppoeAgentEntry.setStatus("current")


class _PppoeAgentVlanId_Type(VlanIndex):
    """Custom type pppoeAgentVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_PppoeAgentVlanId_Type.__name__ = "VlanIndex"
_PppoeAgentVlanId_Object = MibTableColumn
pppoeAgentVlanId = _PppoeAgentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 1),
    _PppoeAgentVlanId_Type()
)
pppoeAgentVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeAgentVlanId.setStatus("current")


class _PppoeAgentMode_Type(Integer32):
    """Custom type pppoeAgentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pppoeTransparent", 1),
          ("pppoeIA", 2))
    )


_PppoeAgentMode_Type.__name__ = "Integer32"
_PppoeAgentMode_Object = MibTableColumn
pppoeAgentMode = _PppoeAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 2),
    _PppoeAgentMode_Type()
)
pppoeAgentMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentMode.setStatus("current")


class _PppoeAgentCircuitIDEnable_Type(Integer32):
    """Custom type pppoeAgentCircuitIDEnable based on Integer32"""
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


_PppoeAgentCircuitIDEnable_Type.__name__ = "Integer32"
_PppoeAgentCircuitIDEnable_Object = MibTableColumn
pppoeAgentCircuitIDEnable = _PppoeAgentCircuitIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 3),
    _PppoeAgentCircuitIDEnable_Type()
)
pppoeAgentCircuitIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentCircuitIDEnable.setStatus("current")


class _PppoeAgentCircuitIDInfo_Type(DisplayString):
    """Custom type pppoeAgentCircuitIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PppoeAgentCircuitIDInfo_Type.__name__ = "DisplayString"
_PppoeAgentCircuitIDInfo_Object = MibTableColumn
pppoeAgentCircuitIDInfo = _PppoeAgentCircuitIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 4),
    _PppoeAgentCircuitIDInfo_Type()
)
pppoeAgentCircuitIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentCircuitIDInfo.setStatus("current")


class _PppoeAgentRemoteIDEnable_Type(Integer32):
    """Custom type pppoeAgentRemoteIDEnable based on Integer32"""
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


_PppoeAgentRemoteIDEnable_Type.__name__ = "Integer32"
_PppoeAgentRemoteIDEnable_Object = MibTableColumn
pppoeAgentRemoteIDEnable = _PppoeAgentRemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 5),
    _PppoeAgentRemoteIDEnable_Type()
)
pppoeAgentRemoteIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRemoteIDEnable.setStatus("current")


class _PppoeAgentRemoteIDInfo_Type(DisplayString):
    """Custom type pppoeAgentRemoteIDInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PppoeAgentRemoteIDInfo_Type.__name__ = "DisplayString"
_PppoeAgentRemoteIDInfo_Object = MibTableColumn
pppoeAgentRemoteIDInfo = _PppoeAgentRemoteIDInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 6),
    _PppoeAgentRemoteIDInfo_Type()
)
pppoeAgentRemoteIDInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRemoteIDInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 1, 1, 7),
    _PppoeAgentRowStatus_Type()
)
pppoeAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRowStatus.setStatus("current")
_PppoeTest_ObjectIdentity = ObjectIdentity
pppoeTest = _PppoeTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2)
)
_PppoeTestPort_Type = Integer32
_PppoeTestPort_Object = MibScalar
pppoeTestPort = _PppoeTestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 1),
    _PppoeTestPort_Type()
)
pppoeTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTestPort.setStatus("current")


class _PppoeTestVlanMode_Type(Integer32):
    """Custom type pppoeTestVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("singletag", 2),
          ("doubletag", 3))
    )


_PppoeTestVlanMode_Type.__name__ = "Integer32"
_PppoeTestVlanMode_Object = MibScalar
pppoeTestVlanMode = _PppoeTestVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 2),
    _PppoeTestVlanMode_Type()
)
pppoeTestVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTestVlanMode.setStatus("current")


class _PppoeTestSvid_Type(VlanIndex):
    """Custom type pppoeTestSvid based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_PppoeTestSvid_Type.__name__ = "VlanIndex"
_PppoeTestSvid_Object = MibScalar
pppoeTestSvid = _PppoeTestSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 3),
    _PppoeTestSvid_Type()
)
pppoeTestSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTestSvid.setStatus("current")


class _PppoeTestCvid_Type(VlanIndex):
    """Custom type pppoeTestCvid based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_PppoeTestCvid_Type.__name__ = "VlanIndex"
_PppoeTestCvid_Object = MibScalar
pppoeTestCvid = _PppoeTestCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 4),
    _PppoeTestCvid_Type()
)
pppoeTestCvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTestCvid.setStatus("current")
_PppoeTestOps_Type = Integer32
_PppoeTestOps_Object = MibScalar
pppoeTestOps = _PppoeTestOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 5),
    _PppoeTestOps_Type()
)
pppoeTestOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTestOps.setStatus("current")
_PppoeTestStatus_Type = DisplayString
_PppoeTestStatus_Object = MibScalar
pppoeTestStatus = _PppoeTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 12, 2, 6),
    _PppoeTestStatus_Type()
)
pppoeTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTestStatus.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13)
)


class _QosAtmVcShapingEnable_Type(Integer32):
    """Custom type qosAtmVcShapingEnable based on Integer32"""
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


_QosAtmVcShapingEnable_Type.__name__ = "Integer32"
_QosAtmVcShapingEnable_Object = MibScalar
qosAtmVcShapingEnable = _QosAtmVcShapingEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 1),
    _QosAtmVcShapingEnable_Type()
)
qosAtmVcShapingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosAtmVcShapingEnable.setStatus("current")
_QosMaxNumOfShapingProfiles_Type = Integer32
_QosMaxNumOfShapingProfiles_Object = MibScalar
qosMaxNumOfShapingProfiles = _QosMaxNumOfShapingProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 2),
    _QosMaxNumOfShapingProfiles_Type()
)
qosMaxNumOfShapingProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMaxNumOfShapingProfiles.setStatus("current")
_QosShapingProfileTable_Object = MibTable
qosShapingProfileTable = _QosShapingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3)
)
if mibBuilder.loadTexts:
    qosShapingProfileTable.setStatus("current")
_QosShapingProfileEntry_Object = MibTableRow
qosShapingProfileEntry = _QosShapingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1)
)
qosShapingProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "qosShapingProfileName"),
)
if mibBuilder.loadTexts:
    qosShapingProfileEntry.setStatus("current")


class _QosShapingProfileName_Type(DisplayString):
    """Custom type qosShapingProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosShapingProfileName_Type.__name__ = "DisplayString"
_QosShapingProfileName_Object = MibTableColumn
qosShapingProfileName = _QosShapingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 1),
    _QosShapingProfileName_Type()
)
qosShapingProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosShapingProfileName.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileName.setUnits("kbps")


class _QosShapingProfileQueue7MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue7MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue7MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue7MaxRate_Object = MibTableColumn
qosShapingProfileQueue7MaxRate = _QosShapingProfileQueue7MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 2),
    _QosShapingProfileQueue7MaxRate_Type()
)
qosShapingProfileQueue7MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue7MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue7MaxRate.setUnits("kbps")


class _QosShapingProfileQueue6MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue6MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue6MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue6MaxRate_Object = MibTableColumn
qosShapingProfileQueue6MaxRate = _QosShapingProfileQueue6MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 3),
    _QosShapingProfileQueue6MaxRate_Type()
)
qosShapingProfileQueue6MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue6MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue6MaxRate.setUnits("kbps")


class _QosShapingProfileQueue5MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue5MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue5MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue5MaxRate_Object = MibTableColumn
qosShapingProfileQueue5MaxRate = _QosShapingProfileQueue5MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 4),
    _QosShapingProfileQueue5MaxRate_Type()
)
qosShapingProfileQueue5MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue5MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue5MaxRate.setUnits("kbps")


class _QosShapingProfileQueue4MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue4MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue4MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue4MaxRate_Object = MibTableColumn
qosShapingProfileQueue4MaxRate = _QosShapingProfileQueue4MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 5),
    _QosShapingProfileQueue4MaxRate_Type()
)
qosShapingProfileQueue4MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue4MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue4MaxRate.setUnits("kbps")


class _QosShapingProfileQueue3MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue3MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue3MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue3MaxRate_Object = MibTableColumn
qosShapingProfileQueue3MaxRate = _QosShapingProfileQueue3MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 6),
    _QosShapingProfileQueue3MaxRate_Type()
)
qosShapingProfileQueue3MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue3MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue3MaxRate.setUnits("kbps")


class _QosShapingProfileQueue2MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue2MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue2MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue2MaxRate_Object = MibTableColumn
qosShapingProfileQueue2MaxRate = _QosShapingProfileQueue2MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 7),
    _QosShapingProfileQueue2MaxRate_Type()
)
qosShapingProfileQueue2MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue2MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue2MaxRate.setUnits("kbps")


class _QosShapingProfileQueue1MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue1MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue1MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue1MaxRate_Object = MibTableColumn
qosShapingProfileQueue1MaxRate = _QosShapingProfileQueue1MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 8),
    _QosShapingProfileQueue1MaxRate_Type()
)
qosShapingProfileQueue1MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue1MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue1MaxRate.setUnits("kbps")


class _QosShapingProfileQueue0MaxRate_Type(Integer32):
    """Custom type qosShapingProfileQueue0MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosShapingProfileQueue0MaxRate_Type.__name__ = "Integer32"
_QosShapingProfileQueue0MaxRate_Object = MibTableColumn
qosShapingProfileQueue0MaxRate = _QosShapingProfileQueue0MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 9),
    _QosShapingProfileQueue0MaxRate_Type()
)
qosShapingProfileQueue0MaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue0MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosShapingProfileQueue0MaxRate.setUnits("kbps")


class _QosShapingProfileQueue7Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue7Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue7Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue7Depth_Object = MibTableColumn
qosShapingProfileQueue7Depth = _QosShapingProfileQueue7Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 10),
    _QosShapingProfileQueue7Depth_Type()
)
qosShapingProfileQueue7Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue7Depth.setStatus("current")


class _QosShapingProfileQueue6Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue6Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue6Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue6Depth_Object = MibTableColumn
qosShapingProfileQueue6Depth = _QosShapingProfileQueue6Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 11),
    _QosShapingProfileQueue6Depth_Type()
)
qosShapingProfileQueue6Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue6Depth.setStatus("current")


class _QosShapingProfileQueue5Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue5Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue5Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue5Depth_Object = MibTableColumn
qosShapingProfileQueue5Depth = _QosShapingProfileQueue5Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 12),
    _QosShapingProfileQueue5Depth_Type()
)
qosShapingProfileQueue5Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue5Depth.setStatus("current")


class _QosShapingProfileQueue4Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue4Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue4Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue4Depth_Object = MibTableColumn
qosShapingProfileQueue4Depth = _QosShapingProfileQueue4Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 13),
    _QosShapingProfileQueue4Depth_Type()
)
qosShapingProfileQueue4Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue4Depth.setStatus("current")


class _QosShapingProfileQueue3Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue3Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue3Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue3Depth_Object = MibTableColumn
qosShapingProfileQueue3Depth = _QosShapingProfileQueue3Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 14),
    _QosShapingProfileQueue3Depth_Type()
)
qosShapingProfileQueue3Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue3Depth.setStatus("current")


class _QosShapingProfileQueue2Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue2Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue2Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue2Depth_Object = MibTableColumn
qosShapingProfileQueue2Depth = _QosShapingProfileQueue2Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 15),
    _QosShapingProfileQueue2Depth_Type()
)
qosShapingProfileQueue2Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue2Depth.setStatus("current")


class _QosShapingProfileQueue1Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue1Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue1Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue1Depth_Object = MibTableColumn
qosShapingProfileQueue1Depth = _QosShapingProfileQueue1Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 16),
    _QosShapingProfileQueue1Depth_Type()
)
qosShapingProfileQueue1Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue1Depth.setStatus("current")


class _QosShapingProfileQueue0Depth_Type(Integer32):
    """Custom type qosShapingProfileQueue0Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosShapingProfileQueue0Depth_Type.__name__ = "Integer32"
_QosShapingProfileQueue0Depth_Object = MibTableColumn
qosShapingProfileQueue0Depth = _QosShapingProfileQueue0Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 17),
    _QosShapingProfileQueue0Depth_Type()
)
qosShapingProfileQueue0Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileQueue0Depth.setStatus("current")
_QosShapingProfileRowStatus_Type = RowStatus
_QosShapingProfileRowStatus_Object = MibTableColumn
qosShapingProfileRowStatus = _QosShapingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 3, 1, 18),
    _QosShapingProfileRowStatus_Type()
)
qosShapingProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosShapingProfileRowStatus.setStatus("current")
_QosMaxNumOfVcShapingProfiles_Type = Integer32
_QosMaxNumOfVcShapingProfiles_Object = MibScalar
qosMaxNumOfVcShapingProfiles = _QosMaxNumOfVcShapingProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 6),
    _QosMaxNumOfVcShapingProfiles_Type()
)
qosMaxNumOfVcShapingProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMaxNumOfVcShapingProfiles.setStatus("current")
_QosVcShapingProfileTable_Object = MibTable
qosVcShapingProfileTable = _QosVcShapingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7)
)
if mibBuilder.loadTexts:
    qosVcShapingProfileTable.setStatus("current")
_QosVcShapingProfileEntry_Object = MibTableRow
qosVcShapingProfileEntry = _QosVcShapingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7, 1)
)
qosVcShapingProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "qosVcShapingProfileName"),
)
if mibBuilder.loadTexts:
    qosVcShapingProfileEntry.setStatus("current")


class _QosVcShapingProfileName_Type(DisplayString):
    """Custom type qosVcShapingProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosVcShapingProfileName_Type.__name__ = "DisplayString"
_QosVcShapingProfileName_Object = MibTableColumn
qosVcShapingProfileName = _QosVcShapingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7, 1, 1),
    _QosVcShapingProfileName_Type()
)
qosVcShapingProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosVcShapingProfileName.setStatus("current")


class _QosVcShapingProfileMaxRate_Type(Integer32):
    """Custom type qosVcShapingProfileMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosVcShapingProfileMaxRate_Type.__name__ = "Integer32"
_QosVcShapingProfileMaxRate_Object = MibTableColumn
qosVcShapingProfileMaxRate = _QosVcShapingProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7, 1, 2),
    _QosVcShapingProfileMaxRate_Type()
)
qosVcShapingProfileMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVcShapingProfileMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosVcShapingProfileMaxRate.setUnits("kbps")


class _QosVcShapingProfileQueueDepth_Type(Integer32):
    """Custom type qosVcShapingProfileQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosVcShapingProfileQueueDepth_Type.__name__ = "Integer32"
_QosVcShapingProfileQueueDepth_Object = MibTableColumn
qosVcShapingProfileQueueDepth = _QosVcShapingProfileQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7, 1, 3),
    _QosVcShapingProfileQueueDepth_Type()
)
qosVcShapingProfileQueueDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVcShapingProfileQueueDepth.setStatus("current")
_QosVcShapingProfileRowStatus_Type = RowStatus
_QosVcShapingProfileRowStatus_Object = MibTableColumn
qosVcShapingProfileRowStatus = _QosVcShapingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 7, 1, 4),
    _QosVcShapingProfileRowStatus_Type()
)
qosVcShapingProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVcShapingProfileRowStatus.setStatus("current")
_QosPortConfTable_Object = MibTable
qosPortConfTable = _QosPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8)
)
if mibBuilder.loadTexts:
    qosPortConfTable.setStatus("current")
_QosPortConfEntry_Object = MibTableRow
qosPortConfEntry = _QosPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8, 1)
)
qosPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosPortConfEntry.setStatus("current")


class _QosPortConfShapingProfile_Type(DisplayString):
    """Custom type qosPortConfShapingProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosPortConfShapingProfile_Type.__name__ = "DisplayString"
_QosPortConfShapingProfile_Object = MibTableColumn
qosPortConfShapingProfile = _QosPortConfShapingProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8, 1, 1),
    _QosPortConfShapingProfile_Type()
)
qosPortConfShapingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortConfShapingProfile.setStatus("current")


class _QosPortConfAlgorithm_Type(Integer32):
    """Custom type qosPortConfAlgorithm based on Integer32"""
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
        *(("sp", 1),
          ("wfq", 2),
          ("spWfq", 3),
          ("shaping", 4))
    )


_QosPortConfAlgorithm_Type.__name__ = "Integer32"
_QosPortConfAlgorithm_Object = MibTableColumn
qosPortConfAlgorithm = _QosPortConfAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8, 1, 3),
    _QosPortConfAlgorithm_Type()
)
qosPortConfAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortConfAlgorithm.setStatus("current")


class _QosPortConfMaxRate_Type(Integer32):
    """Custom type qosPortConfMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 100000),
    )


_QosPortConfMaxRate_Type.__name__ = "Integer32"
_QosPortConfMaxRate_Object = MibTableColumn
qosPortConfMaxRate = _QosPortConfMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8, 1, 4),
    _QosPortConfMaxRate_Type()
)
qosPortConfMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortConfMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    qosPortConfMaxRate.setUnits("kbps")


class _QosPortConfWeightProfile_Type(DisplayString):
    """Custom type qosPortConfWeightProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosPortConfWeightProfile_Type.__name__ = "DisplayString"
_QosPortConfWeightProfile_Object = MibTableColumn
qosPortConfWeightProfile = _QosPortConfWeightProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 8, 1, 5),
    _QosPortConfWeightProfile_Type()
)
qosPortConfWeightProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortConfWeightProfile.setStatus("current")
_QosVcConfTable_Object = MibTable
qosVcConfTable = _QosVcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 9)
)
if mibBuilder.loadTexts:
    qosVcConfTable.setStatus("current")
_QosVcConfEntry_Object = MibTableRow
qosVcConfEntry = _QosVcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 9, 1)
)
qosVcConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "atmvcVpi"),
    (0, "VES1724-58V-MIB", "atmvcVci"),
)
if mibBuilder.loadTexts:
    qosVcConfEntry.setStatus("current")


class _QosVcConfShapingProfile_Type(DisplayString):
    """Custom type qosVcConfShapingProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosVcConfShapingProfile_Type.__name__ = "DisplayString"
_QosVcConfShapingProfile_Object = MibTableColumn
qosVcConfShapingProfile = _QosVcConfShapingProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 9, 1, 1),
    _QosVcConfShapingProfile_Type()
)
qosVcConfShapingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVcConfShapingProfile.setStatus("current")
_QueueMapping_ObjectIdentity = ObjectIdentity
queueMapping = _QueueMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10)
)


class _QueueMappingPbit7QueueId_Type(Integer32):
    """Custom type queueMappingPbit7QueueId based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit7QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit7QueueId_Object = MibScalar
queueMappingPbit7QueueId = _QueueMappingPbit7QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 1),
    _QueueMappingPbit7QueueId_Type()
)
queueMappingPbit7QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit7QueueId.setStatus("current")


class _QueueMappingPbit6QueueId_Type(Integer32):
    """Custom type queueMappingPbit6QueueId based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit6QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit6QueueId_Object = MibScalar
queueMappingPbit6QueueId = _QueueMappingPbit6QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 2),
    _QueueMappingPbit6QueueId_Type()
)
queueMappingPbit6QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit6QueueId.setStatus("current")


class _QueueMappingPbit5QueueId_Type(Integer32):
    """Custom type queueMappingPbit5QueueId based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit5QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit5QueueId_Object = MibScalar
queueMappingPbit5QueueId = _QueueMappingPbit5QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 3),
    _QueueMappingPbit5QueueId_Type()
)
queueMappingPbit5QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit5QueueId.setStatus("current")


class _QueueMappingPbit4QueueId_Type(Integer32):
    """Custom type queueMappingPbit4QueueId based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit4QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit4QueueId_Object = MibScalar
queueMappingPbit4QueueId = _QueueMappingPbit4QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 4),
    _QueueMappingPbit4QueueId_Type()
)
queueMappingPbit4QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit4QueueId.setStatus("current")


class _QueueMappingPbit3QueueId_Type(Integer32):
    """Custom type queueMappingPbit3QueueId based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit3QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit3QueueId_Object = MibScalar
queueMappingPbit3QueueId = _QueueMappingPbit3QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 5),
    _QueueMappingPbit3QueueId_Type()
)
queueMappingPbit3QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit3QueueId.setStatus("current")


class _QueueMappingPbit2QueueId_Type(Integer32):
    """Custom type queueMappingPbit2QueueId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit2QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit2QueueId_Object = MibScalar
queueMappingPbit2QueueId = _QueueMappingPbit2QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 6),
    _QueueMappingPbit2QueueId_Type()
)
queueMappingPbit2QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit2QueueId.setStatus("current")


class _QueueMappingPbit1QueueId_Type(Integer32):
    """Custom type queueMappingPbit1QueueId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit1QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit1QueueId_Object = MibScalar
queueMappingPbit1QueueId = _QueueMappingPbit1QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 7),
    _QueueMappingPbit1QueueId_Type()
)
queueMappingPbit1QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit1QueueId.setStatus("current")


class _QueueMappingPbit0QueueId_Type(Integer32):
    """Custom type queueMappingPbit0QueueId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueMappingPbit0QueueId_Type.__name__ = "Integer32"
_QueueMappingPbit0QueueId_Object = MibScalar
queueMappingPbit0QueueId = _QueueMappingPbit0QueueId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 10, 8),
    _QueueMappingPbit0QueueId_Type()
)
queueMappingPbit0QueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMappingPbit0QueueId.setStatus("current")
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 1, 1, 1),
    _DscpSrcCodePoint_Type()
)
dscpSrcCodePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpSrcCodePoint.setStatus("current")


class _DscpMapPriority_Type(Integer32):
    """Custom type dscpMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DscpMapPriority_Type.__name__ = "Integer32"
_DscpMapPriority_Object = MibTableColumn
dscpMapPriority = _DscpMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 1, 1, 2),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 2, 1)
)
dscpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dscpPortEntry.setStatus("current")


class _DscpStatusEnable_Type(Integer32):
    """Custom type dscpStatusEnable based on Integer32"""
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


_DscpStatusEnable_Type.__name__ = "Integer32"
_DscpStatusEnable_Object = MibTableColumn
dscpStatusEnable = _DscpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 11, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_QosMaxNumOfWeightProfiles_Type = Integer32
_QosMaxNumOfWeightProfiles_Object = MibScalar
qosMaxNumOfWeightProfiles = _QosMaxNumOfWeightProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 12),
    _QosMaxNumOfWeightProfiles_Type()
)
qosMaxNumOfWeightProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMaxNumOfWeightProfiles.setStatus("current")
_QosWeightProfileTable_Object = MibTable
qosWeightProfileTable = _QosWeightProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13)
)
if mibBuilder.loadTexts:
    qosWeightProfileTable.setStatus("current")
_QosWeightProfileEntry_Object = MibTableRow
qosWeightProfileEntry = _QosWeightProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1)
)
qosWeightProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "qosWeightProfileName"),
)
if mibBuilder.loadTexts:
    qosWeightProfileEntry.setStatus("current")


class _QosWeightProfileName_Type(DisplayString):
    """Custom type qosWeightProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QosWeightProfileName_Type.__name__ = "DisplayString"
_QosWeightProfileName_Object = MibTableColumn
qosWeightProfileName = _QosWeightProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 1),
    _QosWeightProfileName_Type()
)
qosWeightProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWeightProfileName.setStatus("current")


class _QosWeightProfileQueue7Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue7Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue7Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue7Weight_Object = MibTableColumn
qosWeightProfileQueue7Weight = _QosWeightProfileQueue7Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 2),
    _QosWeightProfileQueue7Weight_Type()
)
qosWeightProfileQueue7Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue7Weight.setStatus("current")


class _QosWeightProfileQueue6Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue6Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue6Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue6Weight_Object = MibTableColumn
qosWeightProfileQueue6Weight = _QosWeightProfileQueue6Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 3),
    _QosWeightProfileQueue6Weight_Type()
)
qosWeightProfileQueue6Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue6Weight.setStatus("current")


class _QosWeightProfileQueue5Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue5Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue5Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue5Weight_Object = MibTableColumn
qosWeightProfileQueue5Weight = _QosWeightProfileQueue5Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 4),
    _QosWeightProfileQueue5Weight_Type()
)
qosWeightProfileQueue5Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue5Weight.setStatus("current")


class _QosWeightProfileQueue4Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue4Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue4Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue4Weight_Object = MibTableColumn
qosWeightProfileQueue4Weight = _QosWeightProfileQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 5),
    _QosWeightProfileQueue4Weight_Type()
)
qosWeightProfileQueue4Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue4Weight.setStatus("current")


class _QosWeightProfileQueue3Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue3Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue3Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue3Weight_Object = MibTableColumn
qosWeightProfileQueue3Weight = _QosWeightProfileQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 6),
    _QosWeightProfileQueue3Weight_Type()
)
qosWeightProfileQueue3Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue3Weight.setStatus("current")


class _QosWeightProfileQueue2Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue2Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue2Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue2Weight_Object = MibTableColumn
qosWeightProfileQueue2Weight = _QosWeightProfileQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 7),
    _QosWeightProfileQueue2Weight_Type()
)
qosWeightProfileQueue2Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue2Weight.setStatus("current")


class _QosWeightProfileQueue1Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue1Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue1Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue1Weight_Object = MibTableColumn
qosWeightProfileQueue1Weight = _QosWeightProfileQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 8),
    _QosWeightProfileQueue1Weight_Type()
)
qosWeightProfileQueue1Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue1Weight.setStatus("current")


class _QosWeightProfileQueue0Weight_Type(Integer32):
    """Custom type qosWeightProfileQueue0Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_QosWeightProfileQueue0Weight_Type.__name__ = "Integer32"
_QosWeightProfileQueue0Weight_Object = MibTableColumn
qosWeightProfileQueue0Weight = _QosWeightProfileQueue0Weight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 9),
    _QosWeightProfileQueue0Weight_Type()
)
qosWeightProfileQueue0Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue0Weight.setStatus("current")


class _QosWeightProfileQueue7Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue7Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue7Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue7Depth_Object = MibTableColumn
qosWeightProfileQueue7Depth = _QosWeightProfileQueue7Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 10),
    _QosWeightProfileQueue7Depth_Type()
)
qosWeightProfileQueue7Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue7Depth.setStatus("current")


class _QosWeightProfileQueue6Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue6Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue6Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue6Depth_Object = MibTableColumn
qosWeightProfileQueue6Depth = _QosWeightProfileQueue6Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 11),
    _QosWeightProfileQueue6Depth_Type()
)
qosWeightProfileQueue6Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue6Depth.setStatus("current")


class _QosWeightProfileQueue5Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue5Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue5Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue5Depth_Object = MibTableColumn
qosWeightProfileQueue5Depth = _QosWeightProfileQueue5Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 12),
    _QosWeightProfileQueue5Depth_Type()
)
qosWeightProfileQueue5Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue5Depth.setStatus("current")


class _QosWeightProfileQueue4Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue4Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue4Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue4Depth_Object = MibTableColumn
qosWeightProfileQueue4Depth = _QosWeightProfileQueue4Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 13),
    _QosWeightProfileQueue4Depth_Type()
)
qosWeightProfileQueue4Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue4Depth.setStatus("current")


class _QosWeightProfileQueue3Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue3Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue3Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue3Depth_Object = MibTableColumn
qosWeightProfileQueue3Depth = _QosWeightProfileQueue3Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 14),
    _QosWeightProfileQueue3Depth_Type()
)
qosWeightProfileQueue3Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue3Depth.setStatus("current")


class _QosWeightProfileQueue2Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue2Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue2Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue2Depth_Object = MibTableColumn
qosWeightProfileQueue2Depth = _QosWeightProfileQueue2Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 15),
    _QosWeightProfileQueue2Depth_Type()
)
qosWeightProfileQueue2Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue2Depth.setStatus("current")


class _QosWeightProfileQueue1Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue1Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue1Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue1Depth_Object = MibTableColumn
qosWeightProfileQueue1Depth = _QosWeightProfileQueue1Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 16),
    _QosWeightProfileQueue1Depth_Type()
)
qosWeightProfileQueue1Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue1Depth.setStatus("current")


class _QosWeightProfileQueue0Depth_Type(Integer32):
    """Custom type qosWeightProfileQueue0Depth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_QosWeightProfileQueue0Depth_Type.__name__ = "Integer32"
_QosWeightProfileQueue0Depth_Object = MibTableColumn
qosWeightProfileQueue0Depth = _QosWeightProfileQueue0Depth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 17),
    _QosWeightProfileQueue0Depth_Type()
)
qosWeightProfileQueue0Depth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileQueue0Depth.setStatus("current")
_QosWeightProfileRowStatus_Type = RowStatus
_QosWeightProfileRowStatus_Object = MibTableColumn
qosWeightProfileRowStatus = _QosWeightProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 13, 13, 1, 18),
    _QosWeightProfileRowStatus_Type()
)
qosWeightProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWeightProfileRowStatus.setStatus("current")
_Service_ObjectIdentity = ObjectIdentity
service = _Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14)
)
_SecuredClientIpTable_Object = MibTable
securedClientIpTable = _SecuredClientIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2)
)
if mibBuilder.loadTexts:
    securedClientIpTable.setStatus("current")
_SecuredClientIpEntry_Object = MibTableRow
securedClientIpEntry = _SecuredClientIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1)
)
securedClientIpEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "securedClientIpIndex"),
)
if mibBuilder.loadTexts:
    securedClientIpEntry.setStatus("current")


class _SecuredClientIpIndex_Type(Integer32):
    """Custom type securedClientIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SecuredClientIpIndex_Type.__name__ = "Integer32"
_SecuredClientIpIndex_Object = MibTableColumn
securedClientIpIndex = _SecuredClientIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1, 1),
    _SecuredClientIpIndex_Type()
)
securedClientIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIpIndex.setStatus("current")
_SecuredClientIpStartIpAddress_Type = IpAddress
_SecuredClientIpStartIpAddress_Object = MibTableColumn
securedClientIpStartIpAddress = _SecuredClientIpStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1, 2),
    _SecuredClientIpStartIpAddress_Type()
)
securedClientIpStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpStartIpAddress.setStatus("current")
_SecuredClientIpEndIpAddress_Type = IpAddress
_SecuredClientIpEndIpAddress_Object = MibTableColumn
securedClientIpEndIpAddress = _SecuredClientIpEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1, 3),
    _SecuredClientIpEndIpAddress_Type()
)
securedClientIpEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpEndIpAddress.setStatus("current")


class _SecuredClientIpService_Type(Bits):
    """Custom type securedClientIpService based on Bits"""
    namedValues = NamedValues(
        *(("icmp", 0),
          ("telnet", 1),
          ("ftp", 2),
          ("snmp", 3),
          ("http", 4),
          ("ssh", 5),
          ("https", 6),
          ("voip", 7))
    )

_SecuredClientIpService_Type.__name__ = "Bits"
_SecuredClientIpService_Object = MibTableColumn
securedClientIpService = _SecuredClientIpService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1, 4),
    _SecuredClientIpService_Type()
)
securedClientIpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpService.setStatus("current")


class _SecuredClientIpEnable_Type(Integer32):
    """Custom type securedClientIpEnable based on Integer32"""
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


_SecuredClientIpEnable_Type.__name__ = "Integer32"
_SecuredClientIpEnable_Object = MibTableColumn
securedClientIpEnable = _SecuredClientIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 2, 1, 5),
    _SecuredClientIpEnable_Type()
)
securedClientIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpEnable.setStatus("current")
_SecuredClientIpv6Table_Object = MibTable
securedClientIpv6Table = _SecuredClientIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3)
)
if mibBuilder.loadTexts:
    securedClientIpv6Table.setStatus("current")
_SecuredClientIpv6Entry_Object = MibTableRow
securedClientIpv6Entry = _SecuredClientIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1)
)
securedClientIpv6Entry.setIndexNames(
    (0, "VES1724-58V-MIB", "securedClientIpv6Index"),
)
if mibBuilder.loadTexts:
    securedClientIpv6Entry.setStatus("current")


class _SecuredClientIpv6Index_Type(Integer32):
    """Custom type securedClientIpv6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SecuredClientIpv6Index_Type.__name__ = "Integer32"
_SecuredClientIpv6Index_Object = MibTableColumn
securedClientIpv6Index = _SecuredClientIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1, 1),
    _SecuredClientIpv6Index_Type()
)
securedClientIpv6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIpv6Index.setStatus("current")
_SecuredClientIpv6IpAddress_Type = InetAddressIPv6
_SecuredClientIpv6IpAddress_Object = MibTableColumn
securedClientIpv6IpAddress = _SecuredClientIpv6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1, 2),
    _SecuredClientIpv6IpAddress_Type()
)
securedClientIpv6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpv6IpAddress.setStatus("current")


class _SecuredClientIpv6IpMask_Type(Integer32):
    """Custom type securedClientIpv6IpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SecuredClientIpv6IpMask_Type.__name__ = "Integer32"
_SecuredClientIpv6IpMask_Object = MibTableColumn
securedClientIpv6IpMask = _SecuredClientIpv6IpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1, 3),
    _SecuredClientIpv6IpMask_Type()
)
securedClientIpv6IpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpv6IpMask.setStatus("current")


class _SecuredClientIpv6Service_Type(Bits):
    """Custom type securedClientIpv6Service based on Bits"""
    namedValues = NamedValues(
        *(("icmp", 0),
          ("telnet", 1),
          ("ftp", 2),
          ("snmp", 3),
          ("http", 4),
          ("https", 6))
    )

_SecuredClientIpv6Service_Type.__name__ = "Bits"
_SecuredClientIpv6Service_Object = MibTableColumn
securedClientIpv6Service = _SecuredClientIpv6Service_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1, 4),
    _SecuredClientIpv6Service_Type()
)
securedClientIpv6Service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpv6Service.setStatus("current")


class _SecuredClientIpv6Enable_Type(Integer32):
    """Custom type securedClientIpv6Enable based on Integer32"""
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


_SecuredClientIpv6Enable_Type.__name__ = "Integer32"
_SecuredClientIpv6Enable_Object = MibTableColumn
securedClientIpv6Enable = _SecuredClientIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 14, 3, 1, 5),
    _SecuredClientIpv6Enable_Type()
)
securedClientIpv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpv6Enable.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15)
)
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("current")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "snmpTrapDestIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("current")


class _SnmpTrapDestIndex_Type(Integer32):
    """Custom type snmpTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnmpTrapDestIndex_Type.__name__ = "Integer32"
_SnmpTrapDestIndex_Object = MibTableColumn
snmpTrapDestIndex = _SnmpTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 1),
    _SnmpTrapDestIndex_Type()
)
snmpTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestIndex.setStatus("current")


class _SnmpTrapDestIpAddressType_Type(InetAddressType):
    """Custom type snmpTrapDestIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_SnmpTrapDestIpAddressType_Type.__name__ = "InetAddressType"
_SnmpTrapDestIpAddressType_Object = MibTableColumn
snmpTrapDestIpAddressType = _SnmpTrapDestIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 2),
    _SnmpTrapDestIpAddressType_Type()
)
snmpTrapDestIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestIpAddressType.setStatus("current")
_SnmpTrapDestIpAddress_Type = InetAddress
_SnmpTrapDestIpAddress_Object = MibTableColumn
snmpTrapDestIpAddress = _SnmpTrapDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 3),
    _SnmpTrapDestIpAddress_Type()
)
snmpTrapDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestIpAddress.setStatus("current")


class _SnmpTrapDestUdpPort_Type(Integer32):
    """Custom type snmpTrapDestUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpTrapDestUdpPort_Type.__name__ = "Integer32"
_SnmpTrapDestUdpPort_Object = MibTableColumn
snmpTrapDestUdpPort = _SnmpTrapDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 4),
    _SnmpTrapDestUdpPort_Type()
)
snmpTrapDestUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestUdpPort.setStatus("current")


class _SnmpTrapDestVersion_Type(Integer32):
    """Custom type snmpTrapDestVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpTrapDestVersion_Type.__name__ = "Integer32"
_SnmpTrapDestVersion_Object = MibTableColumn
snmpTrapDestVersion = _SnmpTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 5),
    _SnmpTrapDestVersion_Type()
)
snmpTrapDestVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestVersion.setStatus("current")


class _SnmpTrapDestUserName_Type(DisplayString):
    """Custom type snmpTrapDestUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpTrapDestUserName_Type.__name__ = "DisplayString"
_SnmpTrapDestUserName_Object = MibTableColumn
snmpTrapDestUserName = _SnmpTrapDestUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 1, 1, 6),
    _SnmpTrapDestUserName_Type()
)
snmpTrapDestUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestUserName.setStatus("current")


class _SnmpGetCommunity_Type(DisplayString):
    """Custom type snmpGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpGetCommunity_Type.__name__ = "DisplayString"
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 2),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("current")


class _SnmpSetCommunity_Type(DisplayString):
    """Custom type snmpSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 95),
    )


_SnmpSetCommunity_Type.__name__ = "DisplayString"
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 3),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("current")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5, 1)
)
snmpUserEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "snmpUserName"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")


class _SnmpUserName_Type(DisplayString):
    """Custom type snmpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpUserName_Type.__name__ = "DisplayString"
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserSecurityLevel_Type(Integer32):
    """Custom type snmpUserSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 1),
          ("auth", 2),
          ("priv", 3))
    )


_SnmpUserSecurityLevel_Type.__name__ = "Integer32"
_SnmpUserSecurityLevel_Object = MibTableColumn
snmpUserSecurityLevel = _SnmpUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5, 1, 2),
    _SnmpUserSecurityLevel_Type()
)
snmpUserSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserSecurityLevel.setStatus("current")


class _SnmpUserAuthProtocol_Type(Integer32):
    """Custom type snmpUserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_SnmpUserAuthProtocol_Type.__name__ = "Integer32"
_SnmpUserAuthProtocol_Object = MibTableColumn
snmpUserAuthProtocol = _SnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5, 1, 3),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocol.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("aes", 2))
    )


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 5, 1, 4),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 1),
          ("v3", 2),
          ("v3v2c", 3))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 15, 6),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16)
)
_SysBootupFwVersion_Type = DisplayString
_SysBootupFwVersion_Object = MibScalar
sysBootupFwVersion = _SysBootupFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 1),
    _SysBootupFwVersion_Type()
)
sysBootupFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootupFwVersion.setStatus("current")
_SysImage1FwVersion_Type = DisplayString
_SysImage1FwVersion_Object = MibScalar
sysImage1FwVersion = _SysImage1FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 2),
    _SysImage1FwVersion_Type()
)
sysImage1FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage1FwVersion.setStatus("current")
_SysImage2FwVersion_Type = DisplayString
_SysImage2FwVersion_Object = MibScalar
sysImage2FwVersion = _SysImage2FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 3),
    _SysImage2FwVersion_Type()
)
sysImage2FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage2FwVersion.setStatus("current")


class _SysBootupImage_Type(Integer32):
    """Custom type sysBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ras0", 1),
          ("ras1", 2))
    )


_SysBootupImage_Type.__name__ = "Integer32"
_SysBootupImage_Object = MibScalar
sysBootupImage = _SysBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 4),
    _SysBootupImage_Type()
)
sysBootupImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootupImage.setStatus("current")


class _SysBootupConfig_Type(Integer32):
    """Custom type sysBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysBootupConfig_Type.__name__ = "Integer32"
_SysBootupConfig_Object = MibScalar
sysBootupConfig = _SysBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 5),
    _SysBootupConfig_Type()
)
sysBootupConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootupConfig.setStatus("current")
_SysOps_ObjectIdentity = ObjectIdentity
sysOps = _SysOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 6)
)
_SysTarget_Type = PortList
_SysTarget_Object = MibScalar
sysTarget = _SysTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 6, 1),
    _SysTarget_Type()
)
sysTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTarget.setStatus("current")


class _SysOperation_Type(Integer32):
    """Custom type sysOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sysReset", 1),
          ("saveConfigToBootConfig", 2),
          ("loadFactoryDefault", 5),
          ("loadFactoryDefaultByPort", 6),
          ("loadFactoryDefaultInterfaceSystem", 7),
          ("configCopyByPort", 8))
    )


_SysOperation_Type.__name__ = "Integer32"
_SysOperation_Object = MibScalar
sysOperation = _SysOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 6, 2),
    _SysOperation_Type()
)
sysOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOperation.setStatus("current")
_SysSource_Type = PortList
_SysSource_Object = MibScalar
sysSource = _SysSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 6, 3),
    _SysSource_Type()
)
sysSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSource.setStatus("current")
_SysAttributeSelect_Type = PortList
_SysAttributeSelect_Object = MibScalar
sysAttributeSelect = _SysAttributeSelect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 6, 4),
    _SysAttributeSelect_Type()
)
sysAttributeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAttributeSelect.setStatus("current")
_SysTimeSetup_ObjectIdentity = ObjectIdentity
sysTimeSetup = _SysTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7)
)


class _SysTimeServerMode_Type(Integer32):
    """Custom type sysTimeServerMode based on Integer32"""
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
          ("daytime", 2),
          ("time", 3),
          ("ntp", 4))
    )


_SysTimeServerMode_Type.__name__ = "Integer32"
_SysTimeServerMode_Object = MibScalar
sysTimeServerMode = _SysTimeServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 1),
    _SysTimeServerMode_Type()
)
sysTimeServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerMode.setStatus("current")


class _SysTimeServerIPType_Type(InetAddressType):
    """Custom type sysTimeServerIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_SysTimeServerIPType_Type.__name__ = "InetAddressType"
_SysTimeServerIPType_Object = MibScalar
sysTimeServerIPType = _SysTimeServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 2),
    _SysTimeServerIPType_Type()
)
sysTimeServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerIPType.setStatus("current")
_SysTimeServerIP_Type = InetAddress
_SysTimeServerIP_Object = MibScalar
sysTimeServerIP = _SysTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 3),
    _SysTimeServerIP_Type()
)
sysTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerIP.setStatus("current")
_SysTimeSystemTime_Type = DisplayString
_SysTimeSystemTime_Object = MibScalar
sysTimeSystemTime = _SysTimeSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 4),
    _SysTimeSystemTime_Type()
)
sysTimeSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSystemTime.setStatus("current")
_SysTimeSystemDate_Type = DisplayString
_SysTimeSystemDate_Object = MibScalar
sysTimeSystemDate = _SysTimeSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 5),
    _SysTimeSystemDate_Type()
)
sysTimeSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSystemDate.setStatus("current")


class _SysTimeSystemTimeZone_Type(Integer32):
    """Custom type sysTimeSystemTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              11,
              13,
              17,
              21,
              25,
              29,
              31,
              33,
              35,
              37,
              41,
              45,
              49,
              53,
              57,
              61,
              63,
              65,
              67,
              69,
              71,
              72,
              73,
              75,
              77,
              81,
              83,
              84,
              85,
              87,
              89,
              91,
              93,
              97,
              100,
              101,
              105)
        )
    )
    namedValues = NamedValues(
        *(("utcMinus1200", 1),
          ("utcMinus1100", 5),
          ("utcMinus1000", 9),
          ("utcMinus0930", 11),
          ("utcMinus0900", 13),
          ("utcMinus0800", 17),
          ("utcMinus0700", 21),
          ("utcMinus0600", 25),
          ("utcMinus0500", 29),
          ("utcMinus0430", 31),
          ("utcMinus0400", 33),
          ("utcMinus0330", 35),
          ("utcMinus0300", 37),
          ("utcMinus0200", 41),
          ("utcMinus0100", 45),
          ("utc0000", 49),
          ("utcPlus0100", 53),
          ("utcPlus0200", 57),
          ("utcPlus0300", 61),
          ("utcPlus0330", 63),
          ("utcPlus0400", 65),
          ("utcPlus0430", 67),
          ("utcPlus0500", 69),
          ("utcPlus0530", 71),
          ("utcPlus0545", 72),
          ("utcPlus0600", 73),
          ("utcPlus0630", 75),
          ("utcPlus0700", 77),
          ("utcPlus0800", 81),
          ("utcPlus0830", 83),
          ("utcPlus0845", 84),
          ("utcPlus0900", 85),
          ("utcPlus0930", 87),
          ("utcPlus1000", 89),
          ("utcPlus1030", 91),
          ("utcPlus1100", 93),
          ("utcPlus1200", 97),
          ("utcPlus1245", 100),
          ("utcPlus1300", 101),
          ("utcPlus1400", 105))
    )


_SysTimeSystemTimeZone_Type.__name__ = "Integer32"
_SysTimeSystemTimeZone_Object = MibScalar
sysTimeSystemTimeZone = _SysTimeSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 6),
    _SysTimeSystemTimeZone_Type()
)
sysTimeSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSystemTimeZone.setStatus("current")


class _SysTimeServerSynchronize_Type(Integer32):
    """Custom type sysTimeServerSynchronize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("synchronize", 1)
    )


_SysTimeServerSynchronize_Type.__name__ = "Integer32"
_SysTimeServerSynchronize_Object = MibScalar
sysTimeServerSynchronize = _SysTimeServerSynchronize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 7),
    _SysTimeServerSynchronize_Type()
)
sysTimeServerSynchronize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerSynchronize.setStatus("current")


class _SysTimeDaylightSaveEnable_Type(Integer32):
    """Custom type sysTimeDaylightSaveEnable based on Integer32"""
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


_SysTimeDaylightSaveEnable_Type.__name__ = "Integer32"
_SysTimeDaylightSaveEnable_Object = MibScalar
sysTimeDaylightSaveEnable = _SysTimeDaylightSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 8),
    _SysTimeDaylightSaveEnable_Type()
)
sysTimeDaylightSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveEnable.setStatus("current")


class _SysTimeDaylightSaveStartDateWeek_Type(Integer32):
    """Custom type sysTimeDaylightSaveStartDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysTimeDaylightSaveStartDateWeek_Type.__name__ = "Integer32"
_SysTimeDaylightSaveStartDateWeek_Object = MibScalar
sysTimeDaylightSaveStartDateWeek = _SysTimeDaylightSaveStartDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 9),
    _SysTimeDaylightSaveStartDateWeek_Type()
)
sysTimeDaylightSaveStartDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveStartDateWeek.setStatus("current")


class _SysTimeDaylightSaveStartDateDay_Type(Integer32):
    """Custom type sysTimeDaylightSaveStartDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_SysTimeDaylightSaveStartDateDay_Type.__name__ = "Integer32"
_SysTimeDaylightSaveStartDateDay_Object = MibScalar
sysTimeDaylightSaveStartDateDay = _SysTimeDaylightSaveStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 10),
    _SysTimeDaylightSaveStartDateDay_Type()
)
sysTimeDaylightSaveStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveStartDateDay.setStatus("current")


class _SysTimeDaylightSaveStartDateMonth_Type(Integer32):
    """Custom type sysTimeDaylightSaveStartDateMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SysTimeDaylightSaveStartDateMonth_Type.__name__ = "Integer32"
_SysTimeDaylightSaveStartDateMonth_Object = MibScalar
sysTimeDaylightSaveStartDateMonth = _SysTimeDaylightSaveStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 11),
    _SysTimeDaylightSaveStartDateMonth_Type()
)
sysTimeDaylightSaveStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveStartDateMonth.setStatus("current")


class _SysTimeDaylightSaveStartDateClock_Type(Integer32):
    """Custom type sysTimeDaylightSaveStartDateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SysTimeDaylightSaveStartDateClock_Type.__name__ = "Integer32"
_SysTimeDaylightSaveStartDateClock_Object = MibScalar
sysTimeDaylightSaveStartDateClock = _SysTimeDaylightSaveStartDateClock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 12),
    _SysTimeDaylightSaveStartDateClock_Type()
)
sysTimeDaylightSaveStartDateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveStartDateClock.setStatus("current")


class _SysTimeDaylightSaveEndDateWeek_Type(Integer32):
    """Custom type sysTimeDaylightSaveEndDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysTimeDaylightSaveEndDateWeek_Type.__name__ = "Integer32"
_SysTimeDaylightSaveEndDateWeek_Object = MibScalar
sysTimeDaylightSaveEndDateWeek = _SysTimeDaylightSaveEndDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 13),
    _SysTimeDaylightSaveEndDateWeek_Type()
)
sysTimeDaylightSaveEndDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveEndDateWeek.setStatus("current")


class _SysTimeDaylightSaveEndDateDay_Type(Integer32):
    """Custom type sysTimeDaylightSaveEndDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_SysTimeDaylightSaveEndDateDay_Type.__name__ = "Integer32"
_SysTimeDaylightSaveEndDateDay_Object = MibScalar
sysTimeDaylightSaveEndDateDay = _SysTimeDaylightSaveEndDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 14),
    _SysTimeDaylightSaveEndDateDay_Type()
)
sysTimeDaylightSaveEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveEndDateDay.setStatus("current")


class _SysTimeDaylightSaveEndDateMonth_Type(Integer32):
    """Custom type sysTimeDaylightSaveEndDateMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SysTimeDaylightSaveEndDateMonth_Type.__name__ = "Integer32"
_SysTimeDaylightSaveEndDateMonth_Object = MibScalar
sysTimeDaylightSaveEndDateMonth = _SysTimeDaylightSaveEndDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 15),
    _SysTimeDaylightSaveEndDateMonth_Type()
)
sysTimeDaylightSaveEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveEndDateMonth.setStatus("current")


class _SysTimeDaylightSaveEndDateClock_Type(Integer32):
    """Custom type sysTimeDaylightSaveEndDateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SysTimeDaylightSaveEndDateClock_Type.__name__ = "Integer32"
_SysTimeDaylightSaveEndDateClock_Object = MibScalar
sysTimeDaylightSaveEndDateClock = _SysTimeDaylightSaveEndDateClock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 16),
    _SysTimeDaylightSaveEndDateClock_Type()
)
sysTimeDaylightSaveEndDateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDaylightSaveEndDateClock.setStatus("current")


class _SysTimeServerLastSynchronizeStatus_Type(Integer32):
    """Custom type sysTimeServerLastSynchronizeStatus based on Integer32"""
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
        *(("idle", 1),
          ("successfully", 2),
          ("failed", 3),
          ("ongoing", 4))
    )


_SysTimeServerLastSynchronizeStatus_Type.__name__ = "Integer32"
_SysTimeServerLastSynchronizeStatus_Object = MibScalar
sysTimeServerLastSynchronizeStatus = _SysTimeServerLastSynchronizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 17),
    _SysTimeServerLastSynchronizeStatus_Type()
)
sysTimeServerLastSynchronizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeServerLastSynchronizeStatus.setStatus("current")
_SysTimeServerLastSynchronizeTime_Type = DisplayString
_SysTimeServerLastSynchronizeTime_Object = MibScalar
sysTimeServerLastSynchronizeTime = _SysTimeServerLastSynchronizeTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 7, 18),
    _SysTimeServerLastSynchronizeTime_Type()
)
sysTimeServerLastSynchronizeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeServerLastSynchronizeTime.setStatus("current")
_SysPmSync_ObjectIdentity = ObjectIdentity
sysPmSync = _SysPmSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 9)
)
_SysPmSyncUrl_Type = DisplayString
_SysPmSyncUrl_Object = MibScalar
sysPmSyncUrl = _SysPmSyncUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 9, 1),
    _SysPmSyncUrl_Type()
)
sysPmSyncUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPmSyncUrl.setStatus("current")


class _SysPmSyncEnable_Type(Integer32):
    """Custom type sysPmSyncEnable based on Integer32"""
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


_SysPmSyncEnable_Type.__name__ = "Integer32"
_SysPmSyncEnable_Object = MibScalar
sysPmSyncEnable = _SysPmSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 9, 2),
    _SysPmSyncEnable_Type()
)
sysPmSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPmSyncEnable.setStatus("current")


class _SysPmSyncDelay_Type(Integer32):
    """Custom type sysPmSyncDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 899),
    )


_SysPmSyncDelay_Type.__name__ = "Integer32"
_SysPmSyncDelay_Object = MibScalar
sysPmSyncDelay = _SysPmSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 9, 3),
    _SysPmSyncDelay_Type()
)
sysPmSyncDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPmSyncDelay.setStatus("current")


class _SysPmSyncStatus_Type(Integer32):
    """Custom type sysPmSyncStatus based on Integer32"""
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
        *(("idle", 1),
          ("uploaded", 2),
          ("uploading", 3),
          ("uploadingTimeout", 4),
          ("uploadingSuccessfully", 5))
    )


_SysPmSyncStatus_Type.__name__ = "Integer32"
_SysPmSyncStatus_Object = MibScalar
sysPmSyncStatus = _SysPmSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 9, 4),
    _SysPmSyncStatus_Type()
)
sysPmSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPmSyncStatus.setStatus("current")


class _SysNniType_Type(Integer32):
    """Custom type sysNniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ge", 1),
          ("gpon", 2))
    )


_SysNniType_Type.__name__ = "Integer32"
_SysNniType_Object = MibScalar
sysNniType = _SysNniType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 11),
    _SysNniType_Type()
)
sysNniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNniType.setStatus("current")
_Aaa_ObjectIdentity = ObjectIdentity
aaa = _Aaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14)
)
_Authen_ObjectIdentity = ObjectIdentity
authen = _Authen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1)
)


class _LoginMethod1_Type(Integer32):
    """Custom type loginMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_LoginMethod1_Type.__name__ = "Integer32"
_LoginMethod1_Object = MibScalar
loginMethod1 = _LoginMethod1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 1),
    _LoginMethod1_Type()
)
loginMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginMethod1.setStatus("current")


class _LoginMethod2_Type(Integer32):
    """Custom type loginMethod2 based on Integer32"""
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
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_LoginMethod2_Type.__name__ = "Integer32"
_LoginMethod2_Object = MibScalar
loginMethod2 = _LoginMethod2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 2),
    _LoginMethod2_Type()
)
loginMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginMethod2.setStatus("current")


class _LoginMethod3_Type(Integer32):
    """Custom type loginMethod3 based on Integer32"""
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
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_LoginMethod3_Type.__name__ = "Integer32"
_LoginMethod3_Object = MibScalar
loginMethod3 = _LoginMethod3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 3),
    _LoginMethod3_Type()
)
loginMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginMethod3.setStatus("current")


class _EnableMethod1_Type(Integer32):
    """Custom type enableMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("tacacsplus", 2),
          ("radius", 3))
    )


_EnableMethod1_Type.__name__ = "Integer32"
_EnableMethod1_Object = MibScalar
enableMethod1 = _EnableMethod1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 4),
    _EnableMethod1_Type()
)
enableMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableMethod1.setStatus("current")


class _EnableMethod2_Type(Integer32):
    """Custom type enableMethod2 based on Integer32"""
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
        *(("none", 0),
          ("enable", 1),
          ("tacacsplus", 2),
          ("radius", 3))
    )


_EnableMethod2_Type.__name__ = "Integer32"
_EnableMethod2_Object = MibScalar
enableMethod2 = _EnableMethod2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 5),
    _EnableMethod2_Type()
)
enableMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableMethod2.setStatus("current")


class _EnableMethod3_Type(Integer32):
    """Custom type enableMethod3 based on Integer32"""
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
        *(("none", 0),
          ("enable", 1),
          ("tacacsplus", 2),
          ("radius", 3))
    )


_EnableMethod3_Type.__name__ = "Integer32"
_EnableMethod3_Object = MibScalar
enableMethod3 = _EnableMethod3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 1, 6),
    _EnableMethod3_Type()
)
enableMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableMethod3.setStatus("current")
_Acct_ObjectIdentity = ObjectIdentity
acct = _Acct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2)
)


class _SystemMethod_Type(Integer32):
    """Custom type systemMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("radius", 1),
          ("tacacsplus", 2))
    )


_SystemMethod_Type.__name__ = "Integer32"
_SystemMethod_Object = MibScalar
systemMethod = _SystemMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 1),
    _SystemMethod_Type()
)
systemMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemMethod.setStatus("current")


class _ExecMethod_Type(Integer32):
    """Custom type execMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("radius", 1),
          ("tacacsplus", 2))
    )


_ExecMethod_Type.__name__ = "Integer32"
_ExecMethod_Object = MibScalar
execMethod = _ExecMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 2),
    _ExecMethod_Type()
)
execMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    execMethod.setStatus("current")


class _ExecMode_Type(Integer32):
    """Custom type execMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start_stop", 1),
          ("stop_only", 2))
    )


_ExecMode_Type.__name__ = "Integer32"
_ExecMode_Object = MibScalar
execMode = _ExecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 3),
    _ExecMode_Type()
)
execMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    execMode.setStatus("current")


class _CommandsPrivilege_Type(Integer32):
    """Custom type commandsPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CommandsPrivilege_Type.__name__ = "Integer32"
_CommandsPrivilege_Object = MibScalar
commandsPrivilege = _CommandsPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 4),
    _CommandsPrivilege_Type()
)
commandsPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandsPrivilege.setStatus("current")


class _UpdatePeriod_Type(Integer32):
    """Custom type updatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UpdatePeriod_Type.__name__ = "Integer32"
_UpdatePeriod_Object = MibScalar
updatePeriod = _UpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 5),
    _UpdatePeriod_Type()
)
updatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updatePeriod.setStatus("current")


class _CommandsMethod_Type(Integer32):
    """Custom type commandsMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("tacacsplus", 0)
    )


_CommandsMethod_Type.__name__ = "Integer32"
_CommandsMethod_Object = MibScalar
commandsMethod = _CommandsMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 2, 6),
    _CommandsMethod_Type()
)
commandsMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandsMethod.setStatus("current")
_Author_ObjectIdentity = ObjectIdentity
author = _Author_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 3)
)
_AuthorPrivModeTable_Object = MibTable
authorPrivModeTable = _AuthorPrivModeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 3, 1)
)
if mibBuilder.loadTexts:
    authorPrivModeTable.setStatus("current")
_AuthorPrivModeEntry_Object = MibTableRow
authorPrivModeEntry = _AuthorPrivModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 3, 1, 1)
)
authorPrivModeEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "authorPrivilege"),
)
if mibBuilder.loadTexts:
    authorPrivModeEntry.setStatus("current")


class _AuthorPrivilege_Type(Integer32):
    """Custom type authorPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_AuthorPrivilege_Type.__name__ = "Integer32"
_AuthorPrivilege_Object = MibTableColumn
authorPrivilege = _AuthorPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 3, 1, 1, 1),
    _AuthorPrivilege_Type()
)
authorPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorPrivilege.setStatus("current")


class _AuthorMode_Type(Integer32):
    """Custom type authorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("tacacsplus", 1),
          ("tacacsplus_then_local", 2))
    )


_AuthorMode_Type.__name__ = "Integer32"
_AuthorMode_Object = MibTableColumn
authorMode = _AuthorMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 3, 1, 1, 2),
    _AuthorMode_Type()
)
authorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorMode.setStatus("current")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4)
)
_RadiusAuthen_ObjectIdentity = ObjectIdentity
radiusAuthen = _RadiusAuthen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1)
)


class _RadiusAuthenRedundantMode_Type(Integer32):
    """Custom type radiusAuthenRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index_priority", 1),
          ("round_robin", 2))
    )


_RadiusAuthenRedundantMode_Type.__name__ = "Integer32"
_RadiusAuthenRedundantMode_Object = MibScalar
radiusAuthenRedundantMode = _RadiusAuthenRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 1),
    _RadiusAuthenRedundantMode_Type()
)
radiusAuthenRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthenRedundantMode.setStatus("current")


class _RadiusAuthenTimeoutPeriod_Type(Integer32):
    """Custom type radiusAuthenTimeoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RadiusAuthenTimeoutPeriod_Type.__name__ = "Integer32"
_RadiusAuthenTimeoutPeriod_Object = MibScalar
radiusAuthenTimeoutPeriod = _RadiusAuthenTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 2),
    _RadiusAuthenTimeoutPeriod_Type()
)
radiusAuthenTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthenTimeoutPeriod.setStatus("current")
_RadiusAuthenServerTable_Object = MibTable
radiusAuthenServerTable = _RadiusAuthenServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthenServerTable.setStatus("current")
_RadiusAuthenServerEntry_Object = MibTableRow
radiusAuthenServerEntry = _RadiusAuthenServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3, 1)
)
radiusAuthenServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "radiusAuthenServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthenServerEntry.setStatus("current")


class _RadiusAuthenServerIndex_Type(Integer32):
    """Custom type radiusAuthenServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RadiusAuthenServerIndex_Type.__name__ = "Integer32"
_RadiusAuthenServerIndex_Object = MibTableColumn
radiusAuthenServerIndex = _RadiusAuthenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3, 1, 1),
    _RadiusAuthenServerIndex_Type()
)
radiusAuthenServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthenServerIndex.setStatus("current")
_RadiusAuthenServerIP_Type = IpAddress
_RadiusAuthenServerIP_Object = MibTableColumn
radiusAuthenServerIP = _RadiusAuthenServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3, 1, 2),
    _RadiusAuthenServerIP_Type()
)
radiusAuthenServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthenServerIP.setStatus("current")
_RadiusAuthenServerPort_Type = Integer32
_RadiusAuthenServerPort_Object = MibTableColumn
radiusAuthenServerPort = _RadiusAuthenServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3, 1, 3),
    _RadiusAuthenServerPort_Type()
)
radiusAuthenServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthenServerPort.setStatus("current")
_RadiusAuthenServerSecret_Type = DisplayString
_RadiusAuthenServerSecret_Object = MibTableColumn
radiusAuthenServerSecret = _RadiusAuthenServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 1, 3, 1, 4),
    _RadiusAuthenServerSecret_Type()
)
radiusAuthenServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthenServerSecret.setStatus("current")
_RadiusAcct_ObjectIdentity = ObjectIdentity
radiusAcct = _RadiusAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2)
)


class _RadiusAcctRedundantMode_Type(Integer32):
    """Custom type radiusAcctRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index_priority", 1),
          ("round_robin", 2))
    )


_RadiusAcctRedundantMode_Type.__name__ = "Integer32"
_RadiusAcctRedundantMode_Object = MibScalar
radiusAcctRedundantMode = _RadiusAcctRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 1),
    _RadiusAcctRedundantMode_Type()
)
radiusAcctRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctRedundantMode.setStatus("current")


class _RadiusAcctTimeoutPeriod_Type(Integer32):
    """Custom type radiusAcctTimeoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RadiusAcctTimeoutPeriod_Type.__name__ = "Integer32"
_RadiusAcctTimeoutPeriod_Object = MibScalar
radiusAcctTimeoutPeriod = _RadiusAcctTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 2),
    _RadiusAcctTimeoutPeriod_Type()
)
radiusAcctTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctTimeoutPeriod.setStatus("current")
_RadiusAcctServerTable_Object = MibTable
radiusAcctServerTable = _RadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3)
)
if mibBuilder.loadTexts:
    radiusAcctServerTable.setStatus("current")
_RadiusAcctServerEntry_Object = MibTableRow
radiusAcctServerEntry = _RadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3, 1)
)
radiusAcctServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "radiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctServerEntry.setStatus("current")


class _RadiusAcctServerIndex_Type(Integer32):
    """Custom type radiusAcctServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RadiusAcctServerIndex_Type.__name__ = "Integer32"
_RadiusAcctServerIndex_Object = MibTableColumn
radiusAcctServerIndex = _RadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3, 1, 1),
    _RadiusAcctServerIndex_Type()
)
radiusAcctServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctServerIndex.setStatus("current")
_RadiusAcctServerIP_Type = IpAddress
_RadiusAcctServerIP_Object = MibTableColumn
radiusAcctServerIP = _RadiusAcctServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3, 1, 2),
    _RadiusAcctServerIP_Type()
)
radiusAcctServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIP.setStatus("current")
_RadiusAcctServerPort_Type = Integer32
_RadiusAcctServerPort_Object = MibTableColumn
radiusAcctServerPort = _RadiusAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3, 1, 3),
    _RadiusAcctServerPort_Type()
)
radiusAcctServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerPort.setStatus("current")
_RadiusAcctServerSecret_Type = DisplayString
_RadiusAcctServerSecret_Object = MibTableColumn
radiusAcctServerSecret = _RadiusAcctServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 4, 2, 3, 1, 4),
    _RadiusAcctServerSecret_Type()
)
radiusAcctServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerSecret.setStatus("current")
_Tacacsplus_ObjectIdentity = ObjectIdentity
tacacsplus = _Tacacsplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5)
)
_TacacsplusAuthen_ObjectIdentity = ObjectIdentity
tacacsplusAuthen = _TacacsplusAuthen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1)
)


class _TacacsplusAuthenRedundantMode_Type(Integer32):
    """Custom type tacacsplusAuthenRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index_priority", 1),
          ("round_robin", 2))
    )


_TacacsplusAuthenRedundantMode_Type.__name__ = "Integer32"
_TacacsplusAuthenRedundantMode_Object = MibScalar
tacacsplusAuthenRedundantMode = _TacacsplusAuthenRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 1),
    _TacacsplusAuthenRedundantMode_Type()
)
tacacsplusAuthenRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthenRedundantMode.setStatus("current")


class _TacacsplusAuthenTimeoutPeriod_Type(Integer32):
    """Custom type tacacsplusAuthenTimeoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TacacsplusAuthenTimeoutPeriod_Type.__name__ = "Integer32"
_TacacsplusAuthenTimeoutPeriod_Object = MibScalar
tacacsplusAuthenTimeoutPeriod = _TacacsplusAuthenTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 2),
    _TacacsplusAuthenTimeoutPeriod_Type()
)
tacacsplusAuthenTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthenTimeoutPeriod.setStatus("current")
_TacacsplusAuthenServerTable_Object = MibTable
tacacsplusAuthenServerTable = _TacacsplusAuthenServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tacacsplusAuthenServerTable.setStatus("current")
_TacacsplusAuthenServerEntry_Object = MibTableRow
tacacsplusAuthenServerEntry = _TacacsplusAuthenServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3, 1)
)
tacacsplusAuthenServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "tacscsplusAuthenServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsplusAuthenServerEntry.setStatus("current")


class _TacscsplusAuthenServerIndex_Type(Integer32):
    """Custom type tacscsplusAuthenServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TacscsplusAuthenServerIndex_Type.__name__ = "Integer32"
_TacscsplusAuthenServerIndex_Object = MibTableColumn
tacscsplusAuthenServerIndex = _TacscsplusAuthenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3, 1, 1),
    _TacscsplusAuthenServerIndex_Type()
)
tacscsplusAuthenServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacscsplusAuthenServerIndex.setStatus("current")
_TacscsplusAuthenServerIP_Type = IpAddress
_TacscsplusAuthenServerIP_Object = MibTableColumn
tacscsplusAuthenServerIP = _TacscsplusAuthenServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3, 1, 2),
    _TacscsplusAuthenServerIP_Type()
)
tacscsplusAuthenServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacscsplusAuthenServerIP.setStatus("current")
_TacscsplusAuthenServerPort_Type = Integer32
_TacscsplusAuthenServerPort_Object = MibTableColumn
tacscsplusAuthenServerPort = _TacscsplusAuthenServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3, 1, 3),
    _TacscsplusAuthenServerPort_Type()
)
tacscsplusAuthenServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacscsplusAuthenServerPort.setStatus("current")
_TacscsplusAuthenServerSecret_Type = DisplayString
_TacscsplusAuthenServerSecret_Object = MibTableColumn
tacscsplusAuthenServerSecret = _TacscsplusAuthenServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 1, 3, 1, 4),
    _TacscsplusAuthenServerSecret_Type()
)
tacscsplusAuthenServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacscsplusAuthenServerSecret.setStatus("current")
_TacacsplusAcct_ObjectIdentity = ObjectIdentity
tacacsplusAcct = _TacacsplusAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2)
)


class _TacacsplusAcctRedundantMode_Type(Integer32):
    """Custom type tacacsplusAcctRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index_priority", 1),
          ("round_robin", 2))
    )


_TacacsplusAcctRedundantMode_Type.__name__ = "Integer32"
_TacacsplusAcctRedundantMode_Object = MibScalar
tacacsplusAcctRedundantMode = _TacacsplusAcctRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 1),
    _TacacsplusAcctRedundantMode_Type()
)
tacacsplusAcctRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAcctRedundantMode.setStatus("current")


class _TacacsplusAcctTimeoutPeriod_Type(Integer32):
    """Custom type tacacsplusAcctTimeoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TacacsplusAcctTimeoutPeriod_Type.__name__ = "Integer32"
_TacacsplusAcctTimeoutPeriod_Object = MibScalar
tacacsplusAcctTimeoutPeriod = _TacacsplusAcctTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 2),
    _TacacsplusAcctTimeoutPeriod_Type()
)
tacacsplusAcctTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAcctTimeoutPeriod.setStatus("current")
_TacacsplusAcctServerTable_Object = MibTable
tacacsplusAcctServerTable = _TacacsplusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3)
)
if mibBuilder.loadTexts:
    tacacsplusAcctServerTable.setStatus("current")
_TacacsplusAcctServerEntry_Object = MibTableRow
tacacsplusAcctServerEntry = _TacacsplusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3, 1)
)
tacacsplusAcctServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "tacacsplusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsplusAcctServerEntry.setStatus("current")


class _TacacsplusAcctServerIndex_Type(Integer32):
    """Custom type tacacsplusAcctServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TacacsplusAcctServerIndex_Type.__name__ = "Integer32"
_TacacsplusAcctServerIndex_Object = MibTableColumn
tacacsplusAcctServerIndex = _TacacsplusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3, 1, 1),
    _TacacsplusAcctServerIndex_Type()
)
tacacsplusAcctServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsplusAcctServerIndex.setStatus("current")
_TacacsplusAcctServerIP_Type = IpAddress
_TacacsplusAcctServerIP_Object = MibTableColumn
tacacsplusAcctServerIP = _TacacsplusAcctServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3, 1, 2),
    _TacacsplusAcctServerIP_Type()
)
tacacsplusAcctServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAcctServerIP.setStatus("current")
_TacacsplusAcctServerPort_Type = Integer32
_TacacsplusAcctServerPort_Object = MibTableColumn
tacacsplusAcctServerPort = _TacacsplusAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3, 1, 3),
    _TacacsplusAcctServerPort_Type()
)
tacacsplusAcctServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAcctServerPort.setStatus("current")
_TacacsplusAcctServerSecret_Type = DisplayString
_TacacsplusAcctServerSecret_Object = MibTableColumn
tacacsplusAcctServerSecret = _TacacsplusAcctServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 2, 3, 1, 4),
    _TacacsplusAcctServerSecret_Type()
)
tacacsplusAcctServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAcctServerSecret.setStatus("current")
_TacacsplusAuthor_ObjectIdentity = ObjectIdentity
tacacsplusAuthor = _TacacsplusAuthor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3)
)


class _TacacsplusAuthorRedundantMode_Type(Integer32):
    """Custom type tacacsplusAuthorRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index_priority", 1),
          ("round_robin", 2))
    )


_TacacsplusAuthorRedundantMode_Type.__name__ = "Integer32"
_TacacsplusAuthorRedundantMode_Object = MibScalar
tacacsplusAuthorRedundantMode = _TacacsplusAuthorRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 1),
    _TacacsplusAuthorRedundantMode_Type()
)
tacacsplusAuthorRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthorRedundantMode.setStatus("current")


class _TacacsplusAuthorTimeoutPeriod_Type(Integer32):
    """Custom type tacacsplusAuthorTimeoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TacacsplusAuthorTimeoutPeriod_Type.__name__ = "Integer32"
_TacacsplusAuthorTimeoutPeriod_Object = MibScalar
tacacsplusAuthorTimeoutPeriod = _TacacsplusAuthorTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 2),
    _TacacsplusAuthorTimeoutPeriod_Type()
)
tacacsplusAuthorTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthorTimeoutPeriod.setStatus("current")
_TacacsplusAuthorServerTable_Object = MibTable
tacacsplusAuthorServerTable = _TacacsplusAuthorServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3)
)
if mibBuilder.loadTexts:
    tacacsplusAuthorServerTable.setStatus("current")
_TacacsplusAuthorServerEntry_Object = MibTableRow
tacacsplusAuthorServerEntry = _TacacsplusAuthorServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3, 1)
)
tacacsplusAuthorServerEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "tacacsplusAuthorServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsplusAuthorServerEntry.setStatus("current")


class _TacacsplusAuthorServerIndex_Type(Integer32):
    """Custom type tacacsplusAuthorServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TacacsplusAuthorServerIndex_Type.__name__ = "Integer32"
_TacacsplusAuthorServerIndex_Object = MibTableColumn
tacacsplusAuthorServerIndex = _TacacsplusAuthorServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3, 1, 1),
    _TacacsplusAuthorServerIndex_Type()
)
tacacsplusAuthorServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsplusAuthorServerIndex.setStatus("current")
_TacacsplusAuthorServerIP_Type = IpAddress
_TacacsplusAuthorServerIP_Object = MibTableColumn
tacacsplusAuthorServerIP = _TacacsplusAuthorServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3, 1, 2),
    _TacacsplusAuthorServerIP_Type()
)
tacacsplusAuthorServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthorServerIP.setStatus("current")
_TacacsplusAuthorServerPort_Type = Integer32
_TacacsplusAuthorServerPort_Object = MibTableColumn
tacacsplusAuthorServerPort = _TacacsplusAuthorServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3, 1, 3),
    _TacacsplusAuthorServerPort_Type()
)
tacacsplusAuthorServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthorServerPort.setStatus("current")
_TacacsplusAuthorServerSecret_Type = DisplayString
_TacacsplusAuthorServerSecret_Object = MibTableColumn
tacacsplusAuthorServerSecret = _TacacsplusAuthorServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 14, 5, 3, 3, 1, 4),
    _TacacsplusAuthorServerSecret_Type()
)
tacacsplusAuthorServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsplusAuthorServerSecret.setStatus("current")


class _SysPowerSource_Type(Integer32):
    """Custom type sysPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_SysPowerSource_Type.__name__ = "Integer32"
_SysPowerSource_Object = MibScalar
sysPowerSource = _SysPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 15),
    _SysPowerSource_Type()
)
sysPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPowerSource.setStatus("current")


class _SysLoginMessage_Type(DisplayString):
    """Custom type sysLoginMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SysLoginMessage_Type.__name__ = "DisplayString"
_SysLoginMessage_Object = MibScalar
sysLoginMessage = _SysLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 17),
    _SysLoginMessage_Type()
)
sysLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginMessage.setStatus("current")
_SysConfiglog_ObjectIdentity = ObjectIdentity
sysConfiglog = _SysConfiglog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 19)
)
_SysConfigLastChangeTime_Type = DisplayString
_SysConfigLastChangeTime_Object = MibScalar
sysConfigLastChangeTime = _SysConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 19, 1),
    _SysConfigLastChangeTime_Type()
)
sysConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigLastChangeTime.setStatus("current")
_SysConfigLastChangeSession_Type = DisplayString
_SysConfigLastChangeSession_Object = MibScalar
sysConfigLastChangeSession = _SysConfigLastChangeSession_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 19, 2),
    _SysConfigLastChangeSession_Type()
)
sysConfigLastChangeSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigLastChangeSession.setStatus("current")
_SysConfigLastChangeUser_Type = DisplayString
_SysConfigLastChangeUser_Object = MibScalar
sysConfigLastChangeUser = _SysConfigLastChangeUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 19, 3),
    _SysConfigLastChangeUser_Type()
)
sysConfigLastChangeUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigLastChangeUser.setStatus("current")
_SysConfigLastChangeLocation_Type = DisplayString
_SysConfigLastChangeLocation_Object = MibScalar
sysConfigLastChangeLocation = _SysConfigLastChangeLocation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 19, 4),
    _SysConfigLastChangeLocation_Type()
)
sysConfigLastChangeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigLastChangeLocation.setStatus("current")
_SysReboot_ObjectIdentity = ObjectIdentity
sysReboot = _SysReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 20)
)


class _SysRebootAction_Type(Integer32):
    """Custom type sysRebootAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Commit", 1),
          ("Cancel", 2))
    )


_SysRebootAction_Type.__name__ = "Integer32"
_SysRebootAction_Object = MibScalar
sysRebootAction = _SysRebootAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 20, 1),
    _SysRebootAction_Type()
)
sysRebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRebootAction.setStatus("current")
_SysRebootTimer_Type = Integer32
_SysRebootTimer_Object = MibScalar
sysRebootTimer = _SysRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 16, 20, 2),
    _SysRebootTimer_Type()
)
sysRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRebootTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysRebootTimer.setUnits("sec")
_Vdsl_ObjectIdentity = ObjectIdentity
vdsl = _Vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17)
)
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pe_0_dot_4_mm", 1),
          ("pe_0_dot_5_mm", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")


class _SeltLoopTerminal_Type(Integer32):
    """Custom type seltLoopTerminal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("short", 2))
    )


_SeltLoopTerminal_Type.__name__ = "Integer32"
_SeltLoopTerminal_Object = MibScalar
seltLoopTerminal = _SeltLoopTerminal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 7),
    _SeltLoopTerminal_Type()
)
seltLoopTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopTerminal.setStatus("current")
_SeltAttenuation180khz_Type = DisplayString
_SeltAttenuation180khz_Object = MibScalar
seltAttenuation180khz = _SeltAttenuation180khz_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 8),
    _SeltAttenuation180khz_Type()
)
seltAttenuation180khz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltAttenuation180khz.setStatus("current")
if mibBuilder.loadTexts:
    seltAttenuation180khz.setUnits("dB")
_SeltAttenuation300khz_Type = DisplayString
_SeltAttenuation300khz_Object = MibScalar
seltAttenuation300khz = _SeltAttenuation300khz_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 1, 9),
    _SeltAttenuation300khz_Type()
)
seltAttenuation300khz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltAttenuation300khz.setStatus("current")
if mibBuilder.loadTexts:
    seltAttenuation300khz.setUnits("dB")
_VdslOps_ObjectIdentity = ObjectIdentity
vdslOps = _VdslOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 2)
)
_VdslTarget_Type = PortList
_VdslTarget_Object = MibScalar
vdslTarget = _VdslTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 2, 1),
    _VdslTarget_Type()
)
vdslTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslTarget.setStatus("current")


class _VdslOperation_Type(Integer32):
    """Custom type vdslOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("clearCurrPerformance", 2),
          ("clearCurr15MinPerformance", 3),
          ("clearHist15MinPerformance", 4),
          ("clearCurr1DayPerformance", 5),
          ("clearHist1DayPerformance", 6),
          ("clearCurrStatPerformance", 7),
          ("clearCurr15MinStatPerformance", 8),
          ("clearHist15MinStatPerformance", 9),
          ("clearCurr1DayStatPerformance", 10),
          ("clearHist1DayStatPerformance", 11))
    )


_VdslOperation_Type.__name__ = "Integer32"
_VdslOperation_Object = MibScalar
vdslOperation = _VdslOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 2, 2),
    _VdslOperation_Type()
)
vdslOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslOperation.setStatus("current")
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 3)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 3, 1)
)
subrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subrPortEntry.setStatus("current")


class _SubrPortName_Type(DisplayString):
    """Custom type subrPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SubrPortName_Type.__name__ = "DisplayString"
_SubrPortName_Object = MibTableColumn
subrPortName = _SubrPortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 3, 1, 1),
    _SubrPortName_Type()
)
subrPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortName.setStatus("current")


class _SubrPortAlarmProf_Type(DisplayString):
    """Custom type subrPortAlarmProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SubrPortAlarmProf_Type.__name__ = "DisplayString"
_SubrPortAlarmProf_Object = MibTableColumn
subrPortAlarmProf = _SubrPortAlarmProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 3, 1, 2),
    _SubrPortAlarmProf_Type()
)
subrPortAlarmProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortAlarmProf.setStatus("current")
_Vdsl2Profile_ObjectIdentity = ObjectIdentity
vdsl2Profile = _Vdsl2Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4)
)
_Vdsl2LineConfProfileExtendedTable_Object = MibTable
vdsl2LineConfProfileExtendedTable = _Vdsl2LineConfProfileExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1)
)
if mibBuilder.loadTexts:
    vdsl2LineConfProfileExtendedTable.setStatus("current")
_Vdsl2LineConfProfileExtendedEntry_Object = MibTableRow
vdsl2LineConfProfileExtendedEntry = _Vdsl2LineConfProfileExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1)
)
vdsl2LineConfProfileExtendedEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfProfileName"),
)
if mibBuilder.loadTexts:
    vdsl2LineConfProfileExtendedEntry.setStatus("current")


class _Vdsl2LineConfProfileDpboEPsdID_Type(Integer32):
    """Custom type vdsl2LineConfProfileDpboEPsdID based on Integer32"""
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
        *(("psd_co", 1),
          ("psd_flat", 2),
          ("psd_cab_ansi", 3),
          ("psd_cab_etsi", 4),
          ("psd_exch_etsi", 5),
          ("psd_exch_ansi", 6))
    )


_Vdsl2LineConfProfileDpboEPsdID_Type.__name__ = "Integer32"
_Vdsl2LineConfProfileDpboEPsdID_Object = MibTableColumn
vdsl2LineConfProfileDpboEPsdID = _Vdsl2LineConfProfileDpboEPsdID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1, 1),
    _Vdsl2LineConfProfileDpboEPsdID_Type()
)
vdsl2LineConfProfileDpboEPsdID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineConfProfileDpboEPsdID.setStatus("current")


class _Vdsl2LineConfProfileBitSwapDs_Type(Integer32):
    """Custom type vdsl2LineConfProfileBitSwapDs based on Integer32"""
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


_Vdsl2LineConfProfileBitSwapDs_Type.__name__ = "Integer32"
_Vdsl2LineConfProfileBitSwapDs_Object = MibTableColumn
vdsl2LineConfProfileBitSwapDs = _Vdsl2LineConfProfileBitSwapDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1, 2),
    _Vdsl2LineConfProfileBitSwapDs_Type()
)
vdsl2LineConfProfileBitSwapDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineConfProfileBitSwapDs.setStatus("current")


class _Vdsl2LineConfProfileBitSwapUs_Type(Integer32):
    """Custom type vdsl2LineConfProfileBitSwapUs based on Integer32"""
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


_Vdsl2LineConfProfileBitSwapUs_Type.__name__ = "Integer32"
_Vdsl2LineConfProfileBitSwapUs_Object = MibTableColumn
vdsl2LineConfProfileBitSwapUs = _Vdsl2LineConfProfileBitSwapUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1, 3),
    _Vdsl2LineConfProfileBitSwapUs_Type()
)
vdsl2LineConfProfileBitSwapUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineConfProfileBitSwapUs.setStatus("current")


class _Vdsl2LineConfProfileTransmissionType_Type(Bits):
    """Custom type vdsl2LineConfProfileTransmissionType based on Bits"""
    namedValues = NamedValues(
        *(("vdsl2", 0),
          ("adsl2plus", 1),
          ("adsl2", 2),
          ("gdmt", 3),
          ("t1413", 4),
          ("glite", 5),
          ("annexM", 6),
          ("annexL", 7),
          ("annexJ", 8),
          ("annexI", 9))
    )

_Vdsl2LineConfProfileTransmissionType_Type.__name__ = "Bits"
_Vdsl2LineConfProfileTransmissionType_Object = MibTableColumn
vdsl2LineConfProfileTransmissionType = _Vdsl2LineConfProfileTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1, 4),
    _Vdsl2LineConfProfileTransmissionType_Type()
)
vdsl2LineConfProfileTransmissionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineConfProfileTransmissionType.setStatus("current")
_Vdsl2LineConfProfileProfileName_Type = DisplayString
_Vdsl2LineConfProfileProfileName_Object = MibTableColumn
vdsl2LineConfProfileProfileName = _Vdsl2LineConfProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 1, 1, 5),
    _Vdsl2LineConfProfileProfileName_Type()
)
vdsl2LineConfProfileProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsl2LineConfProfileProfileName.setStatus("current")
_Vdsl2LineAlarmConfProfileExtendedTable_Object = MibTable
vdsl2LineAlarmConfProfileExtendedTable = _Vdsl2LineAlarmConfProfileExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2)
)
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileExtendedTable.setStatus("current")
_Vdsl2LineAlarmConfProfileExtendedEntry_Object = MibTableRow
vdsl2LineAlarmConfProfileExtendedEntry = _Vdsl2LineAlarmConfProfileExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2, 1)
)
vdsl2LineAlarmConfProfileExtendedEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileExtendedEntry.setStatus("current")
_Vdsl2LineAlarmConfProfileXtucThresh15MinLofs_Type = Unsigned32
_Vdsl2LineAlarmConfProfileXtucThresh15MinLofs_Object = MibTableColumn
vdsl2LineAlarmConfProfileXtucThresh15MinLofs = _Vdsl2LineAlarmConfProfileXtucThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2, 1, 1),
    _Vdsl2LineAlarmConfProfileXtucThresh15MinLofs_Type()
)
vdsl2LineAlarmConfProfileXtucThresh15MinLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileXtucThresh15MinLofs.setStatus("current")
_Vdsl2LineAlarmConfProfileXturThresh15MinLofs_Type = Unsigned32
_Vdsl2LineAlarmConfProfileXturThresh15MinLofs_Object = MibTableColumn
vdsl2LineAlarmConfProfileXturThresh15MinLofs = _Vdsl2LineAlarmConfProfileXturThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2, 1, 2),
    _Vdsl2LineAlarmConfProfileXturThresh15MinLofs_Type()
)
vdsl2LineAlarmConfProfileXturThresh15MinLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileXturThresh15MinLofs.setStatus("current")
_Vdsl2LineAlarmConfProfileXturThresh15MinLprs_Type = Unsigned32
_Vdsl2LineAlarmConfProfileXturThresh15MinLprs_Object = MibTableColumn
vdsl2LineAlarmConfProfileXturThresh15MinLprs = _Vdsl2LineAlarmConfProfileXturThresh15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2, 1, 3),
    _Vdsl2LineAlarmConfProfileXturThresh15MinLprs_Type()
)
vdsl2LineAlarmConfProfileXturThresh15MinLprs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileXturThresh15MinLprs.setStatus("current")
_Vdsl2LineAlarmConfProfileProfileName_Type = DisplayString
_Vdsl2LineAlarmConfProfileProfileName_Object = MibTableColumn
vdsl2LineAlarmConfProfileProfileName = _Vdsl2LineAlarmConfProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 2, 1, 4),
    _Vdsl2LineAlarmConfProfileProfileName_Type()
)
vdsl2LineAlarmConfProfileProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsl2LineAlarmConfProfileProfileName.setStatus("current")
_Vdsl2ChanConfProfileExtendedTable_Object = MibTable
vdsl2ChanConfProfileExtendedTable = _Vdsl2ChanConfProfileExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 3)
)
if mibBuilder.loadTexts:
    vdsl2ChanConfProfileExtendedTable.setStatus("current")
_Vdsl2ChanConfProfileExtendedEntry_Object = MibTableRow
vdsl2ChanConfProfileExtendedEntry = _Vdsl2ChanConfProfileExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 3, 1)
)
vdsl2ChanConfProfileExtendedEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "vdsl2ChanConfProfileProfileName"),
)
if mibBuilder.loadTexts:
    vdsl2ChanConfProfileExtendedEntry.setStatus("current")


class _Vdsl2ChanConfProfilePhyRDs_Type(Integer32):
    """Custom type vdsl2ChanConfProfilePhyRDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("auto", 3))
    )


_Vdsl2ChanConfProfilePhyRDs_Type.__name__ = "Integer32"
_Vdsl2ChanConfProfilePhyRDs_Object = MibTableColumn
vdsl2ChanConfProfilePhyRDs = _Vdsl2ChanConfProfilePhyRDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 3, 1, 1),
    _Vdsl2ChanConfProfilePhyRDs_Type()
)
vdsl2ChanConfProfilePhyRDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2ChanConfProfilePhyRDs.setStatus("current")


class _Vdsl2ChanConfProfilePhyRUs_Type(Integer32):
    """Custom type vdsl2ChanConfProfilePhyRUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("auto", 3))
    )


_Vdsl2ChanConfProfilePhyRUs_Type.__name__ = "Integer32"
_Vdsl2ChanConfProfilePhyRUs_Object = MibTableColumn
vdsl2ChanConfProfilePhyRUs = _Vdsl2ChanConfProfilePhyRUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 3, 1, 2),
    _Vdsl2ChanConfProfilePhyRUs_Type()
)
vdsl2ChanConfProfilePhyRUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsl2ChanConfProfilePhyRUs.setStatus("current")
_Vdsl2ChanConfProfileProfileName_Type = DisplayString
_Vdsl2ChanConfProfileProfileName_Object = MibTableColumn
vdsl2ChanConfProfileProfileName = _Vdsl2ChanConfProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 4, 3, 1, 3),
    _Vdsl2ChanConfProfileProfileName_Type()
)
vdsl2ChanConfProfileProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsl2ChanConfProfileProfileName.setStatus("current")
_Vdsl2Stats_ObjectIdentity = ObjectIdentity
vdsl2Stats = _Vdsl2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5)
)
_Xdsl2LineBandExtendedTable_Object = MibTable
xdsl2LineBandExtendedTable = _Xdsl2LineBandExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineBandExtendedTable.setStatus("current")
_Xdsl2LineBandExtendedEntry_Object = MibTableRow
xdsl2LineBandExtendedEntry = _Xdsl2LineBandExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 1, 1)
)
xdsl2LineBandExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineBand"),
)
if mibBuilder.loadTexts:
    xdsl2LineBandExtendedEntry.setStatus("current")
_Xdsl2LineBandTxPower_Type = Integer32
_Xdsl2LineBandTxPower_Object = MibTableColumn
xdsl2LineBandTxPower = _Xdsl2LineBandTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 1, 1, 1),
    _Xdsl2LineBandTxPower_Type()
)
xdsl2LineBandTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandTxPower.setStatus("current")
_Xdsl2PMExtended_ObjectIdentity = ObjectIdentity
xdsl2PMExtended = _Xdsl2PMExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2)
)
_Xdsl2PMLineExtended_ObjectIdentity = ObjectIdentity
xdsl2PMLineExtended = _Xdsl2PMLineExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1)
)
_Xdsl2PMLineCurrExtendedTable_Object = MibTable
xdsl2PMLineCurrExtendedTable = _Xdsl2PMLineCurrExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrExtendedTable.setStatus("current")
_Xdsl2PMLineCurrExtendedEntry_Object = MibTableRow
xdsl2PMLineCurrExtendedEntry = _Xdsl2PMLineCurrExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 1, 1)
)
xdsl2PMLineCurrExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMLCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrExtendedEntry.setStatus("current")
_Xdsl2PMLCurrUnit_Type = Xdsl2Unit
_Xdsl2PMLCurrUnit_Object = MibTableColumn
xdsl2PMLCurrUnit = _Xdsl2PMLCurrUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 1, 1, 1),
    _Xdsl2PMLCurrUnit_Type()
)
xdsl2PMLCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLCurrUnit.setStatus("current")
_Xdsl2PMLCurr15MLofs_Type = Counter32
_Xdsl2PMLCurr15MLofs_Object = MibTableColumn
xdsl2PMLCurr15MLofs = _Xdsl2PMLCurr15MLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 1, 1, 2),
    _Xdsl2PMLCurr15MLofs_Type()
)
xdsl2PMLCurr15MLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLofs.setUnits("seconds")
_Xdsl2PMLCurr1DayLofs_Type = Counter32
_Xdsl2PMLCurr1DayLofs_Object = MibTableColumn
xdsl2PMLCurr1DayLofs = _Xdsl2PMLCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 1, 1, 3),
    _Xdsl2PMLCurr1DayLofs_Type()
)
xdsl2PMLCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLofs.setUnits("seconds")
_Xdsl2PMLineInitCurrExtendedTable_Object = MibTable
xdsl2PMLineInitCurrExtendedTable = _Xdsl2PMLineInitCurrExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrExtendedTable.setStatus("current")
_Xdsl2PMLineInitCurrExtendedEntry_Object = MibTableRow
xdsl2PMLineInitCurrExtendedEntry = _Xdsl2PMLineInitCurrExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1)
)
xdsl2PMLineInitCurrExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrExtendedEntry.setStatus("current")
_Xdsl2PMLInitCurr15MLols_Type = Counter32
_Xdsl2PMLInitCurr15MLols_Object = MibTableColumn
xdsl2PMLInitCurr15MLols = _Xdsl2PMLInitCurr15MLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 1),
    _Xdsl2PMLInitCurr15MLols_Type()
)
xdsl2PMLInitCurr15MLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLols.setUnits("seconds")
_Xdsl2PMLInitCurr15MLol_Type = Unsigned32
_Xdsl2PMLInitCurr15MLol_Object = MibTableColumn
xdsl2PMLInitCurr15MLol = _Xdsl2PMLInitCurr15MLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 2),
    _Xdsl2PMLInitCurr15MLol_Type()
)
xdsl2PMLInitCurr15MLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLol.setStatus("current")
_Xdsl2PMLInitCurr15MLprs_Type = Counter32
_Xdsl2PMLInitCurr15MLprs_Object = MibTableColumn
xdsl2PMLInitCurr15MLprs = _Xdsl2PMLInitCurr15MLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 3),
    _Xdsl2PMLInitCurr15MLprs_Type()
)
xdsl2PMLInitCurr15MLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLprs.setUnits("seconds")
_Xdsl2PMLInitCurr15MLpr_Type = Unsigned32
_Xdsl2PMLInitCurr15MLpr_Object = MibTableColumn
xdsl2PMLInitCurr15MLpr = _Xdsl2PMLInitCurr15MLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 4),
    _Xdsl2PMLInitCurr15MLpr_Type()
)
xdsl2PMLInitCurr15MLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MLpr.setStatus("current")
_Xdsl2PMLInitCurr1DayLols_Type = Counter32
_Xdsl2PMLInitCurr1DayLols_Object = MibTableColumn
xdsl2PMLInitCurr1DayLols = _Xdsl2PMLInitCurr1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 5),
    _Xdsl2PMLInitCurr1DayLols_Type()
)
xdsl2PMLInitCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLols.setUnits("seconds")
_Xdsl2PMLInitCurr1DayLol_Type = Unsigned32
_Xdsl2PMLInitCurr1DayLol_Object = MibTableColumn
xdsl2PMLInitCurr1DayLol = _Xdsl2PMLInitCurr1DayLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 6),
    _Xdsl2PMLInitCurr1DayLol_Type()
)
xdsl2PMLInitCurr1DayLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLol.setStatus("current")
_Xdsl2PMLInitCurr1DayLprs_Type = Counter32
_Xdsl2PMLInitCurr1DayLprs_Object = MibTableColumn
xdsl2PMLInitCurr1DayLprs = _Xdsl2PMLInitCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 7),
    _Xdsl2PMLInitCurr1DayLprs_Type()
)
xdsl2PMLInitCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLprs.setUnits("seconds")
_Xdsl2PMLInitCurr1DayLpr_Type = Unsigned32
_Xdsl2PMLInitCurr1DayLpr_Object = MibTableColumn
xdsl2PMLInitCurr1DayLpr = _Xdsl2PMLInitCurr1DayLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 2, 1, 8),
    _Xdsl2PMLInitCurr1DayLpr_Type()
)
xdsl2PMLInitCurr1DayLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayLpr.setStatus("current")
_Xdsl2PMLineHist15MinExtendedTable_Object = MibTable
xdsl2PMLineHist15MinExtendedTable = _Xdsl2PMLineHist15MinExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinExtendedTable.setStatus("current")
_Xdsl2PMLineHist15MinExtendedEntry_Object = MibTableRow
xdsl2PMLineHist15MinExtendedEntry = _Xdsl2PMLineHist15MinExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 3, 1)
)
xdsl2PMLineHist15MinExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist15MUnit"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinExtendedEntry.setStatus("current")
_Xdsl2PMLHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMLHist15MUnit_Object = MibTableColumn
xdsl2PMLHist15MUnit = _Xdsl2PMLHist15MUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 3, 1, 1),
    _Xdsl2PMLHist15MUnit_Type()
)
xdsl2PMLHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUnit.setStatus("current")


class _Xdsl2PMLHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist15MInterval_Object = MibTableColumn
xdsl2PMLHist15MInterval = _Xdsl2PMLHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 3, 1, 2),
    _Xdsl2PMLHist15MInterval_Type()
)
xdsl2PMLHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInterval.setStatus("current")
_Xdsl2PMLHist15MLofs_Type = Counter32
_Xdsl2PMLHist15MLofs_Object = MibTableColumn
xdsl2PMLHist15MLofs = _Xdsl2PMLHist15MLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 3, 1, 3),
    _Xdsl2PMLHist15MLofs_Type()
)
xdsl2PMLHist15MLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLofs.setUnits("seconds")
_Xdsl2PMLineHist1DayExtendedTable_Object = MibTable
xdsl2PMLineHist1DayExtendedTable = _Xdsl2PMLineHist1DayExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayExtendedTable.setStatus("current")
_Xdsl2PMLineHist1DayExtendedEntry_Object = MibTableRow
xdsl2PMLineHist1DayExtendedEntry = _Xdsl2PMLineHist1DayExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 4, 1)
)
xdsl2PMLineHist1DayExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist1DUnit"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayExtendedEntry.setStatus("current")
_Xdsl2PMLHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMLHist1DUnit_Object = MibTableColumn
xdsl2PMLHist1DUnit = _Xdsl2PMLHist1DUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 4, 1, 1),
    _Xdsl2PMLHist1DUnit_Type()
)
xdsl2PMLHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUnit.setStatus("current")


class _Xdsl2PMLHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist1DInterval_Object = MibTableColumn
xdsl2PMLHist1DInterval = _Xdsl2PMLHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 4, 1, 2),
    _Xdsl2PMLHist1DInterval_Type()
)
xdsl2PMLHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInterval.setStatus("current")
_Xdsl2PMLHist1DLofs_Type = Counter32
_Xdsl2PMLHist1DLofs_Object = MibTableColumn
xdsl2PMLHist1DLofs = _Xdsl2PMLHist1DLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 4, 1, 3),
    _Xdsl2PMLHist1DLofs_Type()
)
xdsl2PMLHist1DLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLofs.setUnits("seconds")
_Xdsl2PMLineInitHist15MinExtendedTable_Object = MibTable
xdsl2PMLineInitHist15MinExtendedTable = _Xdsl2PMLineInitHist15MinExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinExtendedTable.setStatus("current")
_Xdsl2PMLineInitHist15MinExtendedEntry_Object = MibTableRow
xdsl2PMLineInitHist15MinExtendedEntry = _Xdsl2PMLineInitHist15MinExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1)
)
xdsl2PMLineInitHist15MinExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinExtendedEntry.setStatus("current")


class _Xdsl2PMLInitHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLInitHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist15MInterval_Object = MibTableColumn
xdsl2PMLInitHist15MInterval = _Xdsl2PMLInitHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1, 1),
    _Xdsl2PMLInitHist15MInterval_Type()
)
xdsl2PMLInitHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MInterval.setStatus("current")
_Xdsl2PMLInitHist15MLols_Type = Counter32
_Xdsl2PMLInitHist15MLols_Object = MibTableColumn
xdsl2PMLInitHist15MLols = _Xdsl2PMLInitHist15MLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1, 2),
    _Xdsl2PMLInitHist15MLols_Type()
)
xdsl2PMLInitHist15MLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLols.setUnits("seconds")
_Xdsl2PMLInitHist15MLol_Type = Unsigned32
_Xdsl2PMLInitHist15MLol_Object = MibTableColumn
xdsl2PMLInitHist15MLol = _Xdsl2PMLInitHist15MLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1, 3),
    _Xdsl2PMLInitHist15MLol_Type()
)
xdsl2PMLInitHist15MLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLol.setStatus("current")
_Xdsl2PMLInitHist15MLprs_Type = Counter32
_Xdsl2PMLInitHist15MLprs_Object = MibTableColumn
xdsl2PMLInitHist15MLprs = _Xdsl2PMLInitHist15MLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1, 4),
    _Xdsl2PMLInitHist15MLprs_Type()
)
xdsl2PMLInitHist15MLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLprs.setUnits("seconds")
_Xdsl2PMLInitHist15MLpr_Type = Unsigned32
_Xdsl2PMLInitHist15MLpr_Object = MibTableColumn
xdsl2PMLInitHist15MLpr = _Xdsl2PMLInitHist15MLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 5, 1, 5),
    _Xdsl2PMLInitHist15MLpr_Type()
)
xdsl2PMLInitHist15MLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MLpr.setStatus("current")
_Xdsl2PMLineInitHist1DayExtendedTable_Object = MibTable
xdsl2PMLineInitHist1DayExtendedTable = _Xdsl2PMLineInitHist1DayExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayExtendedTable.setStatus("current")
_Xdsl2PMLineInitHist1DayExtendedEntry_Object = MibTableRow
xdsl2PMLineInitHist1DayExtendedEntry = _Xdsl2PMLineInitHist1DayExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1)
)
xdsl2PMLineInitHist1DayExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayExtendedEntry.setStatus("current")


class _Xdsl2PMLInitHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLInitHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist1DInterval_Object = MibTableColumn
xdsl2PMLInitHist1DInterval = _Xdsl2PMLInitHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1, 1),
    _Xdsl2PMLInitHist1DInterval_Type()
)
xdsl2PMLInitHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DInterval.setStatus("current")
_Xdsl2PMLInitHist1DLols_Type = Counter32
_Xdsl2PMLInitHist1DLols_Object = MibTableColumn
xdsl2PMLInitHist1DLols = _Xdsl2PMLInitHist1DLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1, 2),
    _Xdsl2PMLInitHist1DLols_Type()
)
xdsl2PMLInitHist1DLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLols.setUnits("seconds")
_Xdsl2PMLInitHist1DLol_Type = Unsigned32
_Xdsl2PMLInitHist1DLol_Object = MibTableColumn
xdsl2PMLInitHist1DLol = _Xdsl2PMLInitHist1DLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1, 3),
    _Xdsl2PMLInitHist1DLol_Type()
)
xdsl2PMLInitHist1DLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLol.setStatus("current")
_Xdsl2PMLInitHist1DLprs_Type = Counter32
_Xdsl2PMLInitHist1DLprs_Object = MibTableColumn
xdsl2PMLInitHist1DLprs = _Xdsl2PMLInitHist1DLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1, 4),
    _Xdsl2PMLInitHist1DLprs_Type()
)
xdsl2PMLInitHist1DLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLprs.setUnits("seconds")
_Xdsl2PMLInitHist1DLpr_Type = Unsigned32
_Xdsl2PMLInitHist1DLpr_Object = MibTableColumn
xdsl2PMLInitHist1DLpr = _Xdsl2PMLInitHist1DLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 1, 6, 1, 5),
    _Xdsl2PMLInitHist1DLpr_Type()
)
xdsl2PMLInitHist1DLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DLpr.setStatus("current")
_Xdsl2PMChannelExtended_ObjectIdentity = ObjectIdentity
xdsl2PMChannelExtended = _Xdsl2PMChannelExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2)
)
_Xdsl2PMChCurrExtendedTable_Object = MibTable
xdsl2PMChCurrExtendedTable = _Xdsl2PMChCurrExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrExtendedTable.setStatus("current")
_Xdsl2PMChCurrExtendedEntry_Object = MibTableRow
xdsl2PMChCurrExtendedEntry = _Xdsl2PMChCurrExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 1, 1)
)
xdsl2PMChCurrExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMChCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrExtendedEntry.setStatus("current")
_Xdsl2PMChCurrUnit_Type = Xdsl2Unit
_Xdsl2PMChCurrUnit_Object = MibTableColumn
xdsl2PMChCurrUnit = _Xdsl2PMChCurrUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 1, 1, 1),
    _Xdsl2PMChCurrUnit_Type()
)
xdsl2PMChCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChCurrUnit.setStatus("current")
_Xdsl2PMChCurr15MUncorrectBlocks_Type = Unsigned32
_Xdsl2PMChCurr15MUncorrectBlocks_Object = MibTableColumn
xdsl2PMChCurr15MUncorrectBlocks = _Xdsl2PMChCurr15MUncorrectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 1, 1, 2),
    _Xdsl2PMChCurr15MUncorrectBlocks_Type()
)
xdsl2PMChCurr15MUncorrectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MUncorrectBlocks.setStatus("current")
_Xdsl2PMChCurr1DayUncorrectBlocks_Type = Unsigned32
_Xdsl2PMChCurr1DayUncorrectBlocks_Object = MibTableColumn
xdsl2PMChCurr1DayUncorrectBlocks = _Xdsl2PMChCurr1DayUncorrectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 1, 1, 3),
    _Xdsl2PMChCurr1DayUncorrectBlocks_Type()
)
xdsl2PMChCurr1DayUncorrectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayUncorrectBlocks.setStatus("current")
_Xdsl2PMChHist15MinExtendedTable_Object = MibTable
xdsl2PMChHist15MinExtendedTable = _Xdsl2PMChHist15MinExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinExtendedTable.setStatus("current")
_Xdsl2PMChHist15MinExtendedEntry_Object = MibTableRow
xdsl2PMChHist15MinExtendedEntry = _Xdsl2PMChHist15MinExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 2, 1)
)
xdsl2PMChHist15MinExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMChHist15MUnit"),
    (0, "VES1724-58V-MIB", "xdsl2PMChHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinExtendedEntry.setStatus("current")
_Xdsl2PMChHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMChHist15MUnit_Object = MibTableColumn
xdsl2PMChHist15MUnit = _Xdsl2PMChHist15MUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 2, 1, 1),
    _Xdsl2PMChHist15MUnit_Type()
)
xdsl2PMChHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MUnit.setStatus("current")


class _Xdsl2PMChHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMChHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist15MInterval_Object = MibTableColumn
xdsl2PMChHist15MInterval = _Xdsl2PMChHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 2, 1, 2),
    _Xdsl2PMChHist15MInterval_Type()
)
xdsl2PMChHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MInterval.setStatus("current")
_Xdsl2PMChHist15MUncorrectBlocks_Type = Unsigned32
_Xdsl2PMChHist15MUncorrectBlocks_Object = MibTableColumn
xdsl2PMChHist15MUncorrectBlocks = _Xdsl2PMChHist15MUncorrectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 2, 1, 3),
    _Xdsl2PMChHist15MUncorrectBlocks_Type()
)
xdsl2PMChHist15MUncorrectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MUncorrectBlocks.setStatus("current")
_Xdsl2PMChHist1DExtendedTable_Object = MibTable
xdsl2PMChHist1DExtendedTable = _Xdsl2PMChHist1DExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DExtendedTable.setStatus("current")
_Xdsl2PMChHist1DExtendedEntry_Object = MibTableRow
xdsl2PMChHist1DExtendedEntry = _Xdsl2PMChHist1DExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 3, 1)
)
xdsl2PMChHist1DExtendedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "xdsl2PMChHist1DUnit"),
    (0, "VES1724-58V-MIB", "xdsl2PMChHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DExtendedEntry.setStatus("current")
_Xdsl2PMChHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMChHist1DUnit_Object = MibTableColumn
xdsl2PMChHist1DUnit = _Xdsl2PMChHist1DUnit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 3, 1, 1),
    _Xdsl2PMChHist1DUnit_Type()
)
xdsl2PMChHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DUnit.setStatus("current")


class _Xdsl2PMChHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMChHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist1DInterval_Object = MibTableColumn
xdsl2PMChHist1DInterval = _Xdsl2PMChHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 3, 1, 2),
    _Xdsl2PMChHist1DInterval_Type()
)
xdsl2PMChHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DInterval.setStatus("current")
_Xdsl2PMChHist1DUncorrectBlocks_Type = Unsigned32
_Xdsl2PMChHist1DUncorrectBlocks_Object = MibTableColumn
xdsl2PMChHist1DUncorrectBlocks = _Xdsl2PMChHist1DUncorrectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 2, 2, 3, 1, 3),
    _Xdsl2PMChHist1DUncorrectBlocks_Type()
)
xdsl2PMChHist1DUncorrectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DUncorrectBlocks.setStatus("current")
_Xdsl2LineStatusTable_Object = MibTable
xdsl2LineStatusTable = _Xdsl2LineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3)
)
if mibBuilder.loadTexts:
    xdsl2LineStatusTable.setStatus("current")
_Xdsl2LineStatusEntry_Object = MibTableRow
xdsl2LineStatusEntry = _Xdsl2LineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1)
)
xdsl2LineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2LineStatusEntry.setStatus("current")


class _Xdsl2LineStatus_Type(Integer32):
    """Custom type xdsl2LineStatus based on Integer32"""
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
        *(("inactive", 1),
          ("training", 2),
          ("linkUp", 3),
          ("linkDown", 4))
    )


_Xdsl2LineStatus_Type.__name__ = "Integer32"
_Xdsl2LineStatus_Object = MibTableColumn
xdsl2LineStatus = _Xdsl2LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1, 1),
    _Xdsl2LineStatus_Type()
)
xdsl2LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatus.setStatus("current")


class _Xdsl2LineProtocol_Type(Integer32):
    """Custom type xdsl2LineProtocol based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vdsl8a", 2),
          ("vdsl8b", 3),
          ("vdsl8c", 4),
          ("vdsl8d", 5),
          ("vdsl12a", 6),
          ("vdsl12b", 7),
          ("vdsl17a", 8),
          ("gdmt", 9),
          ("glite", 10),
          ("adsl2", 11),
          ("adsl2plus", 12),
          ("t1413", 13))
    )


_Xdsl2LineProtocol_Type.__name__ = "Integer32"
_Xdsl2LineProtocol_Object = MibTableColumn
xdsl2LineProtocol = _Xdsl2LineProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1, 2),
    _Xdsl2LineProtocol_Type()
)
xdsl2LineProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineProtocol.setStatus("current")
_Xdsl2LineUptime_Type = Integer32
_Xdsl2LineUptime_Object = MibTableColumn
xdsl2LineUptime = _Xdsl2LineUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1, 3),
    _Xdsl2LineUptime_Type()
)
xdsl2LineUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineUptime.setStatus("current")
_Xdsl2LineTxRate_Type = Integer32
_Xdsl2LineTxRate_Object = MibTableColumn
xdsl2LineTxRate = _Xdsl2LineTxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1, 4),
    _Xdsl2LineTxRate_Type()
)
xdsl2LineTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineTxRate.setStatus("current")
_Xdsl2LineRxRate_Type = Integer32
_Xdsl2LineRxRate_Object = MibTableColumn
xdsl2LineRxRate = _Xdsl2LineRxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 5, 3, 1, 5),
    _Xdsl2LineRxRate_Type()
)
xdsl2LineRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineRxRate.setStatus("current")
_Ldm_ObjectIdentity = ObjectIdentity
ldm = _Ldm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8)
)
_Xdsl2ExtendedStatus_ObjectIdentity = ObjectIdentity
xdsl2ExtendedStatus = _Xdsl2ExtendedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1)
)
_Xdsl2ExtendedSCStatusTable_Object = MibTable
xdsl2ExtendedSCStatusTable = _Xdsl2ExtendedSCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtendedSCStatusTable.setStatus("current")
_Xdsl2ExtendedSCStatusEntry_Object = MibTableRow
xdsl2ExtendedSCStatusEntry = _Xdsl2ExtendedSCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 1, 1)
)
xdsl2ExtendedSCStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
)
if mibBuilder.loadTexts:
    xdsl2ExtendedSCStatusEntry.setStatus("current")


class _Xdsl2SCStatusActAtp_Type(Integer32):
    """Custom type xdsl2SCStatusActAtp based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusActAtp_Type.__name__ = "Integer32"
_Xdsl2SCStatusActAtp_Object = MibTableColumn
xdsl2SCStatusActAtp = _Xdsl2SCStatusActAtp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 1, 1, 1),
    _Xdsl2SCStatusActAtp_Type()
)
xdsl2SCStatusActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusActAtp.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusActAtp.setUnits("0.1 dBm")
_Xdsl2ExtendedSCStatusBandTable_Object = MibTable
xdsl2ExtendedSCStatusBandTable = _Xdsl2ExtendedSCStatusBandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2ExtendedSCStatusBandTable.setStatus("current")
_Xdsl2ExtendedSCStatusBandEntry_Object = MibTableRow
xdsl2ExtendedSCStatusBandEntry = _Xdsl2ExtendedSCStatusBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 2, 1)
)
xdsl2ExtendedSCStatusBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusBand"),
)
if mibBuilder.loadTexts:
    xdsl2ExtendedSCStatusBandEntry.setStatus("current")


class _Xdsl2SCStatusBandSnrMargin_Type(Integer32):
    """Custom type xdsl2SCStatusBandSnrMargin based on Integer32"""
    defaultValue = 2147483646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandSnrMargin_Type.__name__ = "Integer32"
_Xdsl2SCStatusBandSnrMargin_Object = MibTableColumn
xdsl2SCStatusBandSnrMargin = _Xdsl2SCStatusBandSnrMargin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 8, 1, 2, 1, 1),
    _Xdsl2SCStatusBandSnrMargin_Type()
)
xdsl2SCStatusBandSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSnrMargin.setUnits("0.1 dB")
_ForcePortSettingTable_Object = MibTable
forcePortSettingTable = _ForcePortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9)
)
if mibBuilder.loadTexts:
    forcePortSettingTable.setStatus("current")
_ForcePortSettingEntry_Object = MibTableRow
forcePortSettingEntry = _ForcePortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1)
)
forcePortSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    forcePortSettingEntry.setStatus("current")


class _ForcePortTransType_Type(Integer32):
    """Custom type forcePortTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("profile", 0),
          ("auto", 1),
          ("vdsl2", 2),
          ("adsl2plus", 3),
          ("adsl2", 4),
          ("gdmt", 5),
          ("glite", 6),
          ("t1413", 7))
    )


_ForcePortTransType_Type.__name__ = "Integer32"
_ForcePortTransType_Object = MibTableColumn
forcePortTransType = _ForcePortTransType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 1),
    _ForcePortTransType_Type()
)
forcePortTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortTransType.setStatus("current")


class _ForcePortAnnexM_Type(Integer32):
    """Custom type forcePortAnnexM based on Integer32"""
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


_ForcePortAnnexM_Type.__name__ = "Integer32"
_ForcePortAnnexM_Object = MibTableColumn
forcePortAnnexM = _ForcePortAnnexM_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 2),
    _ForcePortAnnexM_Type()
)
forcePortAnnexM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortAnnexM.setStatus("current")


class _ForcePortAnnexL_Type(Integer32):
    """Custom type forcePortAnnexL based on Integer32"""
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


_ForcePortAnnexL_Type.__name__ = "Integer32"
_ForcePortAnnexL_Object = MibTableColumn
forcePortAnnexL = _ForcePortAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 3),
    _ForcePortAnnexL_Type()
)
forcePortAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortAnnexL.setStatus("current")


class _ForcePortAnnexI_Type(Integer32):
    """Custom type forcePortAnnexI based on Integer32"""
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


_ForcePortAnnexI_Type.__name__ = "Integer32"
_ForcePortAnnexI_Object = MibTableColumn
forcePortAnnexI = _ForcePortAnnexI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 4),
    _ForcePortAnnexI_Type()
)
forcePortAnnexI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortAnnexI.setStatus("current")


class _ForcePortAnnexJ_Type(Integer32):
    """Custom type forcePortAnnexJ based on Integer32"""
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


_ForcePortAnnexJ_Type.__name__ = "Integer32"
_ForcePortAnnexJ_Object = MibTableColumn
forcePortAnnexJ = _ForcePortAnnexJ_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 5),
    _ForcePortAnnexJ_Type()
)
forcePortAnnexJ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortAnnexJ.setStatus("current")


class _ForcePortPmMode_Type(Integer32):
    """Custom type forcePortPmMode based on Integer32"""
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
        *(("disable", 0),
          ("allowL3", 1),
          ("allowL2", 2),
          ("allowBoth", 3))
    )


_ForcePortPmMode_Type.__name__ = "Integer32"
_ForcePortPmMode_Object = MibTableColumn
forcePortPmMode = _ForcePortPmMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 6),
    _ForcePortPmMode_Type()
)
forcePortPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortPmMode.setStatus("current")


class _ForcePortL0Time_Type(Integer32):
    """Custom type forcePortL0Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ForcePortL0Time_Type.__name__ = "Integer32"
_ForcePortL0Time_Object = MibTableColumn
forcePortL0Time = _ForcePortL0Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 7),
    _ForcePortL0Time_Type()
)
forcePortL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortL0Time.setStatus("current")


class _ForcePortL2Time_Type(Integer32):
    """Custom type forcePortL2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ForcePortL2Time_Type.__name__ = "Integer32"
_ForcePortL2Time_Object = MibTableColumn
forcePortL2Time = _ForcePortL2Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 8),
    _ForcePortL2Time_Type()
)
forcePortL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortL2Time.setStatus("current")


class _ForcePortL2PwrDnStep_Type(Integer32):
    """Custom type forcePortL2PwrDnStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ForcePortL2PwrDnStep_Type.__name__ = "Integer32"
_ForcePortL2PwrDnStep_Object = MibTableColumn
forcePortL2PwrDnStep = _ForcePortL2PwrDnStep_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 9),
    _ForcePortL2PwrDnStep_Type()
)
forcePortL2PwrDnStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortL2PwrDnStep.setStatus("current")


class _ForcePortL2PwrDnMax_Type(Integer32):
    """Custom type forcePortL2PwrDnMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ForcePortL2PwrDnMax_Type.__name__ = "Integer32"
_ForcePortL2PwrDnMax_Object = MibTableColumn
forcePortL2PwrDnMax = _ForcePortL2PwrDnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 10),
    _ForcePortL2PwrDnMax_Type()
)
forcePortL2PwrDnMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortL2PwrDnMax.setStatus("current")


class _ForcePortTxPwrMode_Type(Integer32):
    """Custom type forcePortTxPwrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix", 0),
          ("power", 1),
          ("rate", 2))
    )


_ForcePortTxPwrMode_Type.__name__ = "Integer32"
_ForcePortTxPwrMode_Object = MibTableColumn
forcePortTxPwrMode = _ForcePortTxPwrMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 11),
    _ForcePortTxPwrMode_Type()
)
forcePortTxPwrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortTxPwrMode.setStatus("current")


class _ForcePortMinInpDs_Type(Integer32):
    """Custom type forcePortMinInpDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ForcePortMinInpDs_Type.__name__ = "Integer32"
_ForcePortMinInpDs_Object = MibTableColumn
forcePortMinInpDs = _ForcePortMinInpDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 12),
    _ForcePortMinInpDs_Type()
)
forcePortMinInpDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortMinInpDs.setStatus("current")


class _ForcePortMinInpUs_Type(Integer32):
    """Custom type forcePortMinInpUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ForcePortMinInpUs_Type.__name__ = "Integer32"
_ForcePortMinInpUs_Object = MibTableColumn
forcePortMinInpUs = _ForcePortMinInpUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 13),
    _ForcePortMinInpUs_Type()
)
forcePortMinInpUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortMinInpUs.setStatus("current")


class _ForcePortMaxUsTxPwr_Type(Integer32):
    """Custom type forcePortMaxUsTxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_ForcePortMaxUsTxPwr_Type.__name__ = "Integer32"
_ForcePortMaxUsTxPwr_Object = MibTableColumn
forcePortMaxUsTxPwr = _ForcePortMaxUsTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 14),
    _ForcePortMaxUsTxPwr_Type()
)
forcePortMaxUsTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortMaxUsTxPwr.setStatus("current")


class _ForcePortMaxDsTxPwr_Type(Integer32):
    """Custom type forcePortMaxDsTxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_ForcePortMaxDsTxPwr_Type.__name__ = "Integer32"
_ForcePortMaxDsTxPwr_Object = MibTableColumn
forcePortMaxDsTxPwr = _ForcePortMaxDsTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 15),
    _ForcePortMaxDsTxPwr_Type()
)
forcePortMaxDsTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortMaxDsTxPwr.setStatus("current")


class _ForcePortMaxUsRxPwr_Type(Integer32):
    """Custom type forcePortMaxUsRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_ForcePortMaxUsRxPwr_Type.__name__ = "Integer32"
_ForcePortMaxUsRxPwr_Object = MibTableColumn
forcePortMaxUsRxPwr = _ForcePortMaxUsRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 9, 1, 16),
    _ForcePortMaxUsRxPwr_Type()
)
forcePortMaxUsRxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcePortMaxUsRxPwr.setStatus("current")
_XdslBonding_ObjectIdentity = ObjectIdentity
xdslBonding = _XdslBonding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10)
)
_XdslBondingConfigTable_Object = MibTable
xdslBondingConfigTable = _XdslBondingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1)
)
if mibBuilder.loadTexts:
    xdslBondingConfigTable.setStatus("current")
_XdslBondingConfigEntry_Object = MibTableRow
xdslBondingConfigEntry = _XdslBondingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1)
)
xdslBondingConfigEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "xdslBondingConfigName"),
)
if mibBuilder.loadTexts:
    xdslBondingConfigEntry.setStatus("current")


class _XdslBondingConfigName_Type(DisplayString):
    """Custom type xdslBondingConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XdslBondingConfigName_Type.__name__ = "DisplayString"
_XdslBondingConfigName_Object = MibTableColumn
xdslBondingConfigName = _XdslBondingConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 1),
    _XdslBondingConfigName_Type()
)
xdslBondingConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingConfigName.setStatus("current")


class _XdslBondingConfigActive_Type(Integer32):
    """Custom type xdslBondingConfigActive based on Integer32"""
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


_XdslBondingConfigActive_Type.__name__ = "Integer32"
_XdslBondingConfigActive_Object = MibTableColumn
xdslBondingConfigActive = _XdslBondingConfigActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 2),
    _XdslBondingConfigActive_Type()
)
xdslBondingConfigActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigActive.setStatus("current")
_XdslBondingConfigMemberPort_Type = PortList
_XdslBondingConfigMemberPort_Object = MibTableColumn
xdslBondingConfigMemberPort = _XdslBondingConfigMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 3),
    _XdslBondingConfigMemberPort_Type()
)
xdslBondingConfigMemberPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigMemberPort.setStatus("current")


class _XdslBondingConfigMode_Type(Integer32):
    """Custom type xdslBondingConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 0),
          ("ptm", 1),
          ("auto", 2))
    )


_XdslBondingConfigMode_Type.__name__ = "Integer32"
_XdslBondingConfigMode_Object = MibTableColumn
xdslBondingConfigMode = _XdslBondingConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 4),
    _XdslBondingConfigMode_Type()
)
xdslBondingConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigMode.setStatus("current")


class _XdslBongingConfigLineTemp_Type(DisplayString):
    """Custom type xdslBongingConfigLineTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XdslBongingConfigLineTemp_Type.__name__ = "DisplayString"
_XdslBongingConfigLineTemp_Object = MibTableColumn
xdslBongingConfigLineTemp = _XdslBongingConfigLineTemp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 5),
    _XdslBongingConfigLineTemp_Type()
)
xdslBongingConfigLineTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBongingConfigLineTemp.setStatus("current")


class _XdslBondingConfigFallbackTemp_Type(DisplayString):
    """Custom type xdslBondingConfigFallbackTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XdslBondingConfigFallbackTemp_Type.__name__ = "DisplayString"
_XdslBondingConfigFallbackTemp_Object = MibTableColumn
xdslBondingConfigFallbackTemp = _XdslBondingConfigFallbackTemp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 6),
    _XdslBondingConfigFallbackTemp_Type()
)
xdslBondingConfigFallbackTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigFallbackTemp.setStatus("current")
_XdslBondingConfigRowStatus_Type = RowStatus
_XdslBondingConfigRowStatus_Object = MibTableColumn
xdslBondingConfigRowStatus = _XdslBondingConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 1, 1, 7),
    _XdslBondingConfigRowStatus_Type()
)
xdslBondingConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigRowStatus.setStatus("current")
_XdslBondingStatusTable_Object = MibTable
xdslBondingStatusTable = _XdslBondingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2)
)
if mibBuilder.loadTexts:
    xdslBondingStatusTable.setStatus("current")
_XdslBondingStatusEntry_Object = MibTableRow
xdslBondingStatusEntry = _XdslBondingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1)
)
xdslBondingStatusEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "xdslBondingStatusName"),
)
if mibBuilder.loadTexts:
    xdslBondingStatusEntry.setStatus("current")
_XdslBondingStatusName_Type = DisplayString
_XdslBondingStatusName_Object = MibTableColumn
xdslBondingStatusName = _XdslBondingStatusName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 1),
    _XdslBondingStatusName_Type()
)
xdslBondingStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusName.setStatus("current")


class _XdslBondingStatusActive_Type(Integer32):
    """Custom type xdslBondingStatusActive based on Integer32"""
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


_XdslBondingStatusActive_Type.__name__ = "Integer32"
_XdslBondingStatusActive_Object = MibTableColumn
xdslBondingStatusActive = _XdslBondingStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 2),
    _XdslBondingStatusActive_Type()
)
xdslBondingStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusActive.setStatus("current")
_XdslBondingStatusMemberPort_Type = DisplayString
_XdslBondingStatusMemberPort_Object = MibTableColumn
xdslBondingStatusMemberPort = _XdslBondingStatusMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 3),
    _XdslBondingStatusMemberPort_Type()
)
xdslBondingStatusMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusMemberPort.setStatus("current")
_XdslBondingStatusActivePort_Type = DisplayString
_XdslBondingStatusActivePort_Object = MibTableColumn
xdslBondingStatusActivePort = _XdslBondingStatusActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 4),
    _XdslBondingStatusActivePort_Type()
)
xdslBondingStatusActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusActivePort.setStatus("current")
_XdslBondingStatusMainPort_Type = DisplayString
_XdslBondingStatusMainPort_Object = MibTableColumn
xdslBondingStatusMainPort = _XdslBondingStatusMainPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 5),
    _XdslBondingStatusMainPort_Type()
)
xdslBondingStatusMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusMainPort.setStatus("current")


class _XdslBondingStatusTransferMode_Type(Integer32):
    """Custom type xdslBondingStatusTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 0),
          ("ptm", 1),
          ("none", 2))
    )


_XdslBondingStatusTransferMode_Type.__name__ = "Integer32"
_XdslBondingStatusTransferMode_Object = MibTableColumn
xdslBondingStatusTransferMode = _XdslBondingStatusTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 6),
    _XdslBondingStatusTransferMode_Type()
)
xdslBondingStatusTransferMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusTransferMode.setStatus("current")
_XdslBondingStatusRateUs_Type = Integer32
_XdslBondingStatusRateUs_Object = MibTableColumn
xdslBondingStatusRateUs = _XdslBondingStatusRateUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 7),
    _XdslBondingStatusRateUs_Type()
)
xdslBondingStatusRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusRateUs.setStatus("current")
_XdslBondingStatusRateDs_Type = Integer32
_XdslBondingStatusRateDs_Object = MibTableColumn
xdslBondingStatusRateDs = _XdslBondingStatusRateDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 2, 1, 8),
    _XdslBondingStatusRateDs_Type()
)
xdslBondingStatusRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusRateDs.setStatus("current")
_XdslBondingCounterOps_ObjectIdentity = ObjectIdentity
xdslBondingCounterOps = _XdslBondingCounterOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 3)
)
_XdslBondingCounterTarget_Type = DisplayString
_XdslBondingCounterTarget_Object = MibScalar
xdslBondingCounterTarget = _XdslBondingCounterTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 3, 1),
    _XdslBondingCounterTarget_Type()
)
xdslBondingCounterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslBondingCounterTarget.setStatus("current")


class _XdslBondingCounterOperation_Type(Integer32):
    """Custom type xdslBondingCounterOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCurrentCounter", 1),
          ("clear15MinCounter", 2),
          ("clear1DayCounter", 3))
    )


_XdslBondingCounterOperation_Type.__name__ = "Integer32"
_XdslBondingCounterOperation_Object = MibScalar
xdslBondingCounterOperation = _XdslBondingCounterOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 17, 10, 3, 2),
    _XdslBondingCounterOperation_Type()
)
xdslBondingCounterOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslBondingCounterOperation.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18)
)
_Mlt_ObjectIdentity = ObjectIdentity
mlt = _Mlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1)
)


class _MltTarget_Type(DisplayString):
    """Custom type mltTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MltTarget_Type.__name__ = "DisplayString"
_MltTarget_Object = MibScalar
mltTarget = _MltTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 1),
    _MltTarget_Type()
)
mltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTarget.setStatus("current")


class _MltOption_Type(Bits):
    """Custom type mltOption based on Bits"""
    namedValues = NamedValues(
        *(("vac", 0),
          ("vdc", 1),
          ("rload", 2),
          ("riso", 3),
          ("cap", 4),
          ("ren", 5),
          ("ring", 6),
          ("metering", 7),
          ("dialtone", 8),
          ("digit", 9),
          ("roh", 10),
          ("loop", 11),
          ("rrev", 12))
    )

_MltOption_Type.__name__ = "Bits"
_MltOption_Object = MibScalar
mltOption = _MltOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 2),
    _MltOption_Type()
)
mltOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOption.setStatus("current")


class _MltForce_Type(Integer32):
    """Custom type mltForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("notForce", 2))
    )


_MltForce_Type.__name__ = "Integer32"
_MltForce_Object = MibScalar
mltForce = _MltForce_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 3),
    _MltForce_Type()
)
mltForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltForce.setStatus("current")


class _MltOps_Type(Integer32):
    """Custom type mltOps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mltDone", 0),
          ("mltStart", 1),
          ("mltClear", 2))
    )


_MltOps_Type.__name__ = "Integer32"
_MltOps_Object = MibScalar
mltOps = _MltOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 4),
    _MltOps_Type()
)
mltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOps.setStatus("current")
_MltResultTable_Object = MibTable
mltResultTable = _MltResultTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5)
)
if mibBuilder.loadTexts:
    mltResultTable.setStatus("current")
_MltResultEntry_Object = MibTableRow
mltResultEntry = _MltResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1)
)
mltResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mltResultEntry.setStatus("current")
_MltVacTip_Type = Integer32
_MltVacTip_Object = MibTableColumn
mltVacTip = _MltVacTip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 1),
    _MltVacTip_Type()
)
mltVacTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVacTip.setUnits("0.1 rms")
_MltVacRing_Type = Integer32
_MltVacRing_Object = MibTableColumn
mltVacRing = _MltVacRing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 2),
    _MltVacRing_Type()
)
mltVacRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVacRing.setUnits("0.1 rms")
_MltVacDiff_Type = Integer32
_MltVacDiff_Object = MibTableColumn
mltVacDiff = _MltVacDiff_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 3),
    _MltVacDiff_Type()
)
mltVacDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVacDiff.setUnits("0.1 rms")
_MltVdcTip_Type = Integer32
_MltVdcTip_Object = MibTableColumn
mltVdcTip = _MltVdcTip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 4),
    _MltVdcTip_Type()
)
mltVdcTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcTip.setUnits("0.1 volt")
_MltVdcRing_Type = Integer32
_MltVdcRing_Object = MibTableColumn
mltVdcRing = _MltVdcRing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 5),
    _MltVdcRing_Type()
)
mltVdcRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcRing.setUnits("0.1 volt")
_MltVdcDiff_Type = Integer32
_MltVdcDiff_Object = MibTableColumn
mltVdcDiff = _MltVdcDiff_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 6),
    _MltVdcDiff_Type()
)
mltVdcDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcDiff.setUnits("0.1 volt")
_MltRLoop_Type = Integer32
_MltRLoop_Object = MibTableColumn
mltRLoop = _MltRLoop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 7),
    _MltRLoop_Type()
)
mltRLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRLoop.setStatus("current")
if mibBuilder.loadTexts:
    mltRLoop.setUnits("0.1 ohm")
_MltRtg_Type = Integer32
_MltRtg_Object = MibTableColumn
mltRtg = _MltRtg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 8),
    _MltRtg_Type()
)
mltRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtg.setStatus("current")
if mibBuilder.loadTexts:
    mltRtg.setUnits("0.1 ohm")
_MltRrg_Type = Integer32
_MltRrg_Object = MibTableColumn
mltRrg = _MltRrg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 9),
    _MltRrg_Type()
)
mltRrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRrg.setStatus("current")
if mibBuilder.loadTexts:
    mltRrg.setUnits("0.1 ohm")
_MltRtr_Type = Integer32
_MltRtr_Object = MibTableColumn
mltRtr = _MltRtr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 10),
    _MltRtr_Type()
)
mltRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtr.setStatus("current")
if mibBuilder.loadTexts:
    mltRtr.setUnits("0.1 ohm")
_MltCtg_Type = Integer32
_MltCtg_Object = MibTableColumn
mltCtg = _MltCtg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 11),
    _MltCtg_Type()
)
mltCtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtg.setStatus("current")
if mibBuilder.loadTexts:
    mltCtg.setUnits("10^-10 F")
_MltCrg_Type = Integer32
_MltCrg_Object = MibTableColumn
mltCrg = _MltCrg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 12),
    _MltCrg_Type()
)
mltCrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCrg.setStatus("current")
if mibBuilder.loadTexts:
    mltCrg.setUnits("10^-10 F")
_MltCtr_Type = Integer32
_MltCtr_Object = MibTableColumn
mltCtr = _MltCtr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 13),
    _MltCtr_Type()
)
mltCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtr.setStatus("current")
if mibBuilder.loadTexts:
    mltCtr.setUnits("10^-10 F")
_MltRen_Type = Integer32
_MltRen_Object = MibTableColumn
mltRen = _MltRen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 14),
    _MltRen_Type()
)
mltRen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRen.setStatus("current")
if mibBuilder.loadTexts:
    mltRen.setUnits("0.1 ren")
_MltVRing_Type = Integer32
_MltVRing_Object = MibTableColumn
mltVRing = _MltVRing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 15),
    _MltVRing_Type()
)
mltVRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVRing.setUnits("0.1 volt")
_MltVMetering_Type = Integer32
_MltVMetering_Object = MibTableColumn
mltVMetering = _MltVMetering_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 16),
    _MltVMetering_Type()
)
mltVMetering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVMetering.setStatus("current")
if mibBuilder.loadTexts:
    mltVMetering.setUnits("0.1 vpeak")


class _MltDialToneDetected_Type(Integer32):
    """Custom type mltDialToneDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_MltDialToneDetected_Type.__name__ = "Integer32"
_MltDialToneDetected_Object = MibTableColumn
mltDialToneDetected = _MltDialToneDetected_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 17),
    _MltDialToneDetected_Type()
)
mltDialToneDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDetected.setStatus("current")
_MltDetectedDtmfCount_Type = Integer32
_MltDetectedDtmfCount_Object = MibTableColumn
mltDetectedDtmfCount = _MltDetectedDtmfCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 18),
    _MltDetectedDtmfCount_Type()
)
mltDetectedDtmfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDetectedDtmfCount.setStatus("current")
_MltDialToneDelay_Type = Integer32
_MltDialToneDelay_Object = MibTableColumn
mltDialToneDelay = _MltDialToneDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 19),
    _MltDialToneDelay_Type()
)
mltDialToneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDelay.setStatus("current")
if mibBuilder.loadTexts:
    mltDialToneDelay.setUnits("0.001 sec")


class _MltReceiverOffHook_Type(Integer32):
    """Custom type mltReceiverOffHook based on Integer32"""
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
        *(("onhook", 1),
          ("offhook", 2),
          ("short", 3),
          ("open", 4))
    )


_MltReceiverOffHook_Type.__name__ = "Integer32"
_MltReceiverOffHook_Object = MibTableColumn
mltReceiverOffHook = _MltReceiverOffHook_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 20),
    _MltReceiverOffHook_Type()
)
mltReceiverOffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltReceiverOffHook.setStatus("current")
_MltLoopRload_Type = Integer32
_MltLoopRload_Object = MibTableColumn
mltLoopRload = _MltLoopRload_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 21),
    _MltLoopRload_Type()
)
mltLoopRload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopRload.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopRload.setUnits("1 ohm")
_MltLoopIMetallic_Type = Integer32
_MltLoopIMetallic_Object = MibTableColumn
mltLoopIMetallic = _MltLoopIMetallic_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 22),
    _MltLoopIMetallic_Type()
)
mltLoopIMetallic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopIMetallic.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopIMetallic.setUnits("10^-6 amp")
_MltLoopVAB_Type = Integer32
_MltLoopVAB_Object = MibTableColumn
mltLoopVAB = _MltLoopVAB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 23),
    _MltLoopVAB_Type()
)
mltLoopVAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopVAB.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopVAB.setUnits("0.001 volt")
_MltLoopVBL_Type = Integer32
_MltLoopVBL_Object = MibTableColumn
mltLoopVBL = _MltLoopVBL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 24),
    _MltLoopVBL_Type()
)
mltLoopVBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopVBL.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopVBL.setUnits("0.001 volt")
_MltLoopVBH_Type = Integer32
_MltLoopVBH_Object = MibTableColumn
mltLoopVBH = _MltLoopVBH_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 25),
    _MltLoopVBH_Type()
)
mltLoopVBH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopVBH.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopVBH.setUnits("0.001 volt")
_MltRrev_Type = Integer32
_MltRrev_Object = MibTableColumn
mltRrev = _MltRrev_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 26),
    _MltRrev_Type()
)
mltRrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRrev.setStatus("current")
if mibBuilder.loadTexts:
    mltRrev.setUnits("1 ohm")


class _MltDetectedDtmfDigit_Type(DisplayString):
    """Custom type mltDetectedDtmfDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MltDetectedDtmfDigit_Type.__name__ = "DisplayString"
_MltDetectedDtmfDigit_Object = MibTableColumn
mltDetectedDtmfDigit = _MltDetectedDtmfDigit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 5, 1, 27),
    _MltDetectedDtmfDigit_Type()
)
mltDetectedDtmfDigit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDetectedDtmfDigit.setStatus("current")


class _MltOpsErrMsg_Type(DisplayString):
    """Custom type mltOpsErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MltOpsErrMsg_Type.__name__ = "DisplayString"
_MltOpsErrMsg_Object = MibScalar
mltOpsErrMsg = _MltOpsErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 6),
    _MltOpsErrMsg_Type()
)
mltOpsErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltOpsErrMsg.setStatus("current")


class _MltTargetType_Type(Integer32):
    """Custom type mltTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mltPort", 0),
          ("mltTel", 2),
          ("mltAccount", 3),
          ("mltTerminateId", 4))
    )


_MltTargetType_Type.__name__ = "Integer32"
_MltTargetType_Object = MibScalar
mltTargetType = _MltTargetType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 1, 7),
    _MltTargetType_Type()
)
mltTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTargetType.setStatus("current")
_H248_ObjectIdentity = ObjectIdentity
h248 = _H248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2)
)
_H248DigitMapTimeout_ObjectIdentity = ObjectIdentity
h248DigitMapTimeout = _H248DigitMapTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 1)
)


class _H248DigitStartTimeout_Type(Integer32):
    """Custom type h248DigitStartTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_H248DigitStartTimeout_Type.__name__ = "Integer32"
_H248DigitStartTimeout_Object = MibScalar
h248DigitStartTimeout = _H248DigitStartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 1, 1),
    _H248DigitStartTimeout_Type()
)
h248DigitStartTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248DigitStartTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h248DigitStartTimeout.setUnits("second")


class _H248DigitShortTimeout_Type(Integer32):
    """Custom type h248DigitShortTimeout based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_H248DigitShortTimeout_Type.__name__ = "Integer32"
_H248DigitShortTimeout_Object = MibScalar
h248DigitShortTimeout = _H248DigitShortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 1, 2),
    _H248DigitShortTimeout_Type()
)
h248DigitShortTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248DigitShortTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h248DigitShortTimeout.setUnits("second")


class _H248DigitLongTimeout_Type(Integer32):
    """Custom type h248DigitLongTimeout based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_H248DigitLongTimeout_Type.__name__ = "Integer32"
_H248DigitLongTimeout_Object = MibScalar
h248DigitLongTimeout = _H248DigitLongTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 1, 3),
    _H248DigitLongTimeout_Type()
)
h248DigitLongTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248DigitLongTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h248DigitLongTimeout.setUnits("second")


class _H248Dscp_Type(Integer32):
    """Custom type h248Dscp based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H248Dscp_Type.__name__ = "Integer32"
_H248Dscp_Object = MibScalar
h248Dscp = _H248Dscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 2),
    _H248Dscp_Type()
)
h248Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Dscp.setStatus("current")


class _H248Encode_Type(Integer32):
    """Custom type h248Encode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_H248Encode_Type.__name__ = "Integer32"
_H248Encode_Object = MibScalar
h248Encode = _H248Encode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 3),
    _H248Encode_Type()
)
h248Encode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Encode.setStatus("current")


class _H248InactivityTimer_Type(Integer32):
    """Custom type h248InactivityTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H248InactivityTimer_Type.__name__ = "Integer32"
_H248InactivityTimer_Object = MibScalar
h248InactivityTimer = _H248InactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 4),
    _H248InactivityTimer_Type()
)
h248InactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248InactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    h248InactivityTimer.setUnits("10 milliseconds")
_H248Mg_ObjectIdentity = ObjectIdentity
h248Mg = _H248Mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 5)
)


class _H248MgEnable_Type(Integer32):
    """Custom type h248MgEnable based on Integer32"""
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


_H248MgEnable_Type.__name__ = "Integer32"
_H248MgEnable_Object = MibScalar
h248MgEnable = _H248MgEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 5, 1),
    _H248MgEnable_Type()
)
h248MgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgEnable.setStatus("current")


class _H248MgName_Type(DisplayString):
    """Custom type h248MgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H248MgName_Type.__name__ = "DisplayString"
_H248MgName_Object = MibScalar
h248MgName = _H248MgName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 5, 2),
    _H248MgName_Type()
)
h248MgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgName.setStatus("current")


class _H248MgPort_Type(Integer32):
    """Custom type h248MgPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248MgPort_Type.__name__ = "Integer32"
_H248MgPort_Object = MibScalar
h248MgPort = _H248MgPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 5, 3),
    _H248MgPort_Type()
)
h248MgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgPort.setStatus("current")


class _H248MgState_Type(Integer32):
    """Custom type h248MgState based on Integer32"""
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
        *(("disabled", 1),
          ("registering", 2),
          ("registered", 3),
          ("unregistering", 4),
          ("unregistered", 5),
          ("inactivity_timeout", 6),
          ("activity_back", 7),
          ("disconnected", 8),
          ("disabled_by_mgc", 9),
          ("unknown", 10))
    )


_H248MgState_Type.__name__ = "Integer32"
_H248MgState_Object = MibScalar
h248MgState = _H248MgState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 5, 4),
    _H248MgState_Type()
)
h248MgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h248MgState.setStatus("current")
_H248Mgc_ObjectIdentity = ObjectIdentity
h248Mgc = _H248Mgc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6)
)


class _H248MgcIpDn_Type(DisplayString):
    """Custom type h248MgcIpDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H248MgcIpDn_Type.__name__ = "DisplayString"
_H248MgcIpDn_Object = MibScalar
h248MgcIpDn = _H248MgcIpDn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6, 1),
    _H248MgcIpDn_Type()
)
h248MgcIpDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgcIpDn.setStatus("current")


class _H248MgcPort_Type(Integer32):
    """Custom type h248MgcPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248MgcPort_Type.__name__ = "Integer32"
_H248MgcPort_Object = MibScalar
h248MgcPort = _H248MgcPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6, 2),
    _H248MgcPort_Type()
)
h248MgcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgcPort.setStatus("current")


class _H248Mgc2Enable_Type(Integer32):
    """Custom type h248Mgc2Enable based on Integer32"""
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


_H248Mgc2Enable_Type.__name__ = "Integer32"
_H248Mgc2Enable_Object = MibScalar
h248Mgc2Enable = _H248Mgc2Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6, 3),
    _H248Mgc2Enable_Type()
)
h248Mgc2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Mgc2Enable.setStatus("current")


class _H248Mgc2IpDn_Type(DisplayString):
    """Custom type h248Mgc2IpDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H248Mgc2IpDn_Type.__name__ = "DisplayString"
_H248Mgc2IpDn_Object = MibScalar
h248Mgc2IpDn = _H248Mgc2IpDn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6, 4),
    _H248Mgc2IpDn_Type()
)
h248Mgc2IpDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Mgc2IpDn.setStatus("current")


class _H248Mgc2Port_Type(Integer32):
    """Custom type h248Mgc2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248Mgc2Port_Type.__name__ = "Integer32"
_H248Mgc2Port_Object = MibScalar
h248Mgc2Port = _H248Mgc2Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 6, 5),
    _H248Mgc2Port_Type()
)
h248Mgc2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Mgc2Port.setStatus("current")
_H248RetransmitTime_ObjectIdentity = ObjectIdentity
h248RetransmitTime = _H248RetransmitTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 8)
)


class _H248RetransmitInitTime_Type(Integer32):
    """Custom type h248RetransmitInitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 20000),
    )


_H248RetransmitInitTime_Type.__name__ = "Integer32"
_H248RetransmitInitTime_Object = MibScalar
h248RetransmitInitTime = _H248RetransmitInitTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 8, 1),
    _H248RetransmitInitTime_Type()
)
h248RetransmitInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RetransmitInitTime.setStatus("current")
if mibBuilder.loadTexts:
    h248RetransmitInitTime.setUnits("millisecond")


class _H248RetransmitMinTime_Type(Integer32):
    """Custom type h248RetransmitMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_H248RetransmitMinTime_Type.__name__ = "Integer32"
_H248RetransmitMinTime_Object = MibScalar
h248RetransmitMinTime = _H248RetransmitMinTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 8, 2),
    _H248RetransmitMinTime_Type()
)
h248RetransmitMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RetransmitMinTime.setStatus("current")
if mibBuilder.loadTexts:
    h248RetransmitMinTime.setUnits("millisecond")


class _H248RetransmitMaxTime_Type(Integer32):
    """Custom type h248RetransmitMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_H248RetransmitMaxTime_Type.__name__ = "Integer32"
_H248RetransmitMaxTime_Object = MibScalar
h248RetransmitMaxTime = _H248RetransmitMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 8, 3),
    _H248RetransmitMaxTime_Type()
)
h248RetransmitMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RetransmitMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    h248RetransmitMaxTime.setUnits("millisecond")


class _H248RetransmitWindow_Type(Integer32):
    """Custom type h248RetransmitWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_H248RetransmitWindow_Type.__name__ = "Integer32"
_H248RetransmitWindow_Object = MibScalar
h248RetransmitWindow = _H248RetransmitWindow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 8, 4),
    _H248RetransmitWindow_Type()
)
h248RetransmitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RetransmitWindow.setStatus("current")
if mibBuilder.loadTexts:
    h248RetransmitWindow.setUnits("millisecond")
_H248Rfc2833_ObjectIdentity = ObjectIdentity
h248Rfc2833 = _H248Rfc2833_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 9)
)


class _H248Rfc2833Enable_Type(Integer32):
    """Custom type h248Rfc2833Enable based on Integer32"""
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


_H248Rfc2833Enable_Type.__name__ = "Integer32"
_H248Rfc2833Enable_Object = MibScalar
h248Rfc2833Enable = _H248Rfc2833Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 9, 1),
    _H248Rfc2833Enable_Type()
)
h248Rfc2833Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Rfc2833Enable.setStatus("current")


class _H248Rfc2833Ptype_Type(Integer32):
    """Custom type h248Rfc2833Ptype based on Integer32"""
    defaultValue = 101

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_H248Rfc2833Ptype_Type.__name__ = "Integer32"
_H248Rfc2833Ptype_Object = MibScalar
h248Rfc2833Ptype = _H248Rfc2833Ptype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 9, 2),
    _H248Rfc2833Ptype_Type()
)
h248Rfc2833Ptype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Rfc2833Ptype.setStatus("current")


class _H248RtpStartPort_Type(Integer32):
    """Custom type h248RtpStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 64000),
    )


_H248RtpStartPort_Type.__name__ = "Integer32"
_H248RtpStartPort_Object = MibScalar
h248RtpStartPort = _H248RtpStartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 10),
    _H248RtpStartPort_Type()
)
h248RtpStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpStartPort.setStatus("current")


class _H248RtpEndPort_Type(Integer32):
    """Custom type h248RtpEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 65000),
    )


_H248RtpEndPort_Type.__name__ = "Integer32"
_H248RtpEndPort_Object = MibScalar
h248RtpEndPort = _H248RtpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 11),
    _H248RtpEndPort_Type()
)
h248RtpEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpEndPort.setStatus("current")


class _H248SoftSwitch_Type(Integer32):
    """Custom type h248SoftSwitch based on Integer32"""
    defaultValue = 1

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
        *(("defval", 1),
          ("zxss10xSs", 2),
          ("huaweiSs3000", 3),
          ("aluSs5020", 4),
          ("nsn", 5),
          ("iskratel", 6))
    )


_H248SoftSwitch_Type.__name__ = "Integer32"
_H248SoftSwitch_Object = MibScalar
h248SoftSwitch = _H248SoftSwitch_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 12),
    _H248SoftSwitch_Type()
)
h248SoftSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248SoftSwitch.setStatus("current")


class _H248T38Enable_Type(Integer32):
    """Custom type h248T38Enable based on Integer32"""
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


_H248T38Enable_Type.__name__ = "Integer32"
_H248T38Enable_Object = MibScalar
h248T38Enable = _H248T38Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 13),
    _H248T38Enable_Type()
)
h248T38Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248T38Enable.setStatus("current")


class _H248Transport_Type(Integer32):
    """Custom type h248Transport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_H248Transport_Type.__name__ = "Integer32"
_H248Transport_Object = MibScalar
h248Transport = _H248Transport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 14),
    _H248Transport_Type()
)
h248Transport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248Transport.setStatus("current")


class _H248VbdEnable_Type(Integer32):
    """Custom type h248VbdEnable based on Integer32"""
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


_H248VbdEnable_Type.__name__ = "Integer32"
_H248VbdEnable_Object = MibScalar
h248VbdEnable = _H248VbdEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 15),
    _H248VbdEnable_Type()
)
h248VbdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248VbdEnable.setStatus("current")
_H248RtpTerminatetId_ObjectIdentity = ObjectIdentity
h248RtpTerminatetId = _H248RtpTerminatetId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 16)
)


class _H248RtpTerminateIdPrefix_Type(DisplayString):
    """Custom type h248RtpTerminateIdPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H248RtpTerminateIdPrefix_Type.__name__ = "DisplayString"
_H248RtpTerminateIdPrefix_Object = MibScalar
h248RtpTerminateIdPrefix = _H248RtpTerminateIdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 16, 1),
    _H248RtpTerminateIdPrefix_Type()
)
h248RtpTerminateIdPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTerminateIdPrefix.setStatus("current")


class _H248RtpTerminateIdSuffixStartNumber_Type(DisplayString):
    """Custom type h248RtpTerminateIdSuffixStartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_H248RtpTerminateIdSuffixStartNumber_Type.__name__ = "DisplayString"
_H248RtpTerminateIdSuffixStartNumber_Object = MibScalar
h248RtpTerminateIdSuffixStartNumber = _H248RtpTerminateIdSuffixStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 16, 2),
    _H248RtpTerminateIdSuffixStartNumber_Type()
)
h248RtpTerminateIdSuffixStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTerminateIdSuffixStartNumber.setStatus("current")


class _H248RtpTerminateIdSuffixLen_Type(Integer32):
    """Custom type h248RtpTerminateIdSuffixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H248RtpTerminateIdSuffixLen_Type.__name__ = "Integer32"
_H248RtpTerminateIdSuffixLen_Object = MibScalar
h248RtpTerminateIdSuffixLen = _H248RtpTerminateIdSuffixLen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 16, 3),
    _H248RtpTerminateIdSuffixLen_Type()
)
h248RtpTerminateIdSuffixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTerminateIdSuffixLen.setStatus("current")


class _H248ForceVerEnable_Type(Integer32):
    """Custom type h248ForceVerEnable based on Integer32"""
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


_H248ForceVerEnable_Type.__name__ = "Integer32"
_H248ForceVerEnable_Object = MibScalar
h248ForceVerEnable = _H248ForceVerEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 17),
    _H248ForceVerEnable_Type()
)
h248ForceVerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248ForceVerEnable.setStatus("current")


class _H248RegisterRetry_Type(Integer32):
    """Custom type h248RegisterRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_H248RegisterRetry_Type.__name__ = "Integer32"
_H248RegisterRetry_Object = MibScalar
h248RegisterRetry = _H248RegisterRetry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 2, 18),
    _H248RegisterRetry_Type()
)
h248RegisterRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RegisterRetry.setStatus("current")
_VoipIp_ObjectIdentity = ObjectIdentity
voipIp = _VoipIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3)
)
_VoipIpAddress_Type = IpAddress
_VoipIpAddress_Object = MibScalar
voipIpAddress = _VoipIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 1),
    _VoipIpAddress_Type()
)
voipIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpAddress.setStatus("current")


class _VoipIpNetmask_Type(Integer32):
    """Custom type voipIpNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VoipIpNetmask_Type.__name__ = "Integer32"
_VoipIpNetmask_Object = MibScalar
voipIpNetmask = _VoipIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 2),
    _VoipIpNetmask_Type()
)
voipIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpNetmask.setStatus("current")


class _VoipIpVlanId_Type(VlanIndex):
    """Custom type voipIpVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VoipIpVlanId_Type.__name__ = "VlanIndex"
_VoipIpVlanId_Object = MibScalar
voipIpVlanId = _VoipIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 3),
    _VoipIpVlanId_Type()
)
voipIpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpVlanId.setStatus("current")
_VoipIpDefaultGateway_Type = IpAddress
_VoipIpDefaultGateway_Object = MibScalar
voipIpDefaultGateway = _VoipIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 4),
    _VoipIpDefaultGateway_Type()
)
voipIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDefaultGateway.setStatus("current")
_VoipIpDns_Type = IpAddress
_VoipIpDns_Object = MibScalar
voipIpDns = _VoipIpDns_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 5),
    _VoipIpDns_Type()
)
voipIpDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDns.setStatus("current")


class _VoipIpDhcpBootpEnable_Type(Integer32):
    """Custom type voipIpDhcpBootpEnable based on Integer32"""
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


_VoipIpDhcpBootpEnable_Type.__name__ = "Integer32"
_VoipIpDhcpBootpEnable_Object = MibScalar
voipIpDhcpBootpEnable = _VoipIpDhcpBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 6),
    _VoipIpDhcpBootpEnable_Type()
)
voipIpDhcpBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDhcpBootpEnable.setStatus("current")


class _VoipIpDhcpOperation_Type(Integer32):
    """Custom type voipIpDhcpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 1),
          ("renew", 2))
    )


_VoipIpDhcpOperation_Type.__name__ = "Integer32"
_VoipIpDhcpOperation_Object = MibScalar
voipIpDhcpOperation = _VoipIpDhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 7),
    _VoipIpDhcpOperation_Type()
)
voipIpDhcpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDhcpOperation.setStatus("current")


class _VoipIpPbit_Type(Integer32):
    """Custom type voipIpPbit based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VoipIpPbit_Type.__name__ = "Integer32"
_VoipIpPbit_Object = MibScalar
voipIpPbit = _VoipIpPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 8),
    _VoipIpPbit_Type()
)
voipIpPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpPbit.setStatus("current")
_VoipIpDns2_Type = IpAddress
_VoipIpDns2_Object = MibScalar
voipIpDns2 = _VoipIpDns2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 9),
    _VoipIpDns2_Type()
)
voipIpDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDns2.setStatus("current")
_VoipIpDns3_Type = IpAddress
_VoipIpDns3_Object = MibScalar
voipIpDns3 = _VoipIpDns3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 3, 10),
    _VoipIpDns3_Type()
)
voipIpDns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpDns3.setStatus("current")
_VoipPots_ObjectIdentity = ObjectIdentity
voipPots = _VoipPots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4)
)


class _VoipPotsHookFlashTimeEnable_Type(Integer32):
    """Custom type voipPotsHookFlashTimeEnable based on Integer32"""
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


_VoipPotsHookFlashTimeEnable_Type.__name__ = "Integer32"
_VoipPotsHookFlashTimeEnable_Object = MibScalar
voipPotsHookFlashTimeEnable = _VoipPotsHookFlashTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 1),
    _VoipPotsHookFlashTimeEnable_Type()
)
voipPotsHookFlashTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsHookFlashTimeEnable.setStatus("current")


class _VoipPotsHookFlashMaxTime_Type(Integer32):
    """Custom type voipPotsHookFlashMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1500),
    )


_VoipPotsHookFlashMaxTime_Type.__name__ = "Integer32"
_VoipPotsHookFlashMaxTime_Object = MibScalar
voipPotsHookFlashMaxTime = _VoipPotsHookFlashMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 2),
    _VoipPotsHookFlashMaxTime_Type()
)
voipPotsHookFlashMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsHookFlashMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    voipPotsHookFlashMaxTime.setUnits("millisecond")


class _VoipPotsHookFlashMinTime_Type(Integer32):
    """Custom type voipPotsHookFlashMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1500),
    )


_VoipPotsHookFlashMinTime_Type.__name__ = "Integer32"
_VoipPotsHookFlashMinTime_Object = MibScalar
voipPotsHookFlashMinTime = _VoipPotsHookFlashMinTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 3),
    _VoipPotsHookFlashMinTime_Type()
)
voipPotsHookFlashMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsHookFlashMinTime.setStatus("current")
if mibBuilder.loadTexts:
    voipPotsHookFlashMinTime.setUnits("millisecond")


class _VoipPotsOffHookTimeEnable_Type(Integer32):
    """Custom type voipPotsOffHookTimeEnable based on Integer32"""
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


_VoipPotsOffHookTimeEnable_Type.__name__ = "Integer32"
_VoipPotsOffHookTimeEnable_Object = MibScalar
voipPotsOffHookTimeEnable = _VoipPotsOffHookTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 4),
    _VoipPotsOffHookTimeEnable_Type()
)
voipPotsOffHookTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsOffHookTimeEnable.setStatus("current")


class _VoipPotsOffHookTime_Type(Integer32):
    """Custom type voipPotsOffHookTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VoipPotsOffHookTime_Type.__name__ = "Integer32"
_VoipPotsOffHookTime_Object = MibScalar
voipPotsOffHookTime = _VoipPotsOffHookTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 5),
    _VoipPotsOffHookTime_Type()
)
voipPotsOffHookTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsOffHookTime.setStatus("current")
if mibBuilder.loadTexts:
    voipPotsOffHookTime.setUnits("millisecond")
_VoipPotsRingTable_Object = MibTable
voipPotsRingTable = _VoipPotsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6)
)
if mibBuilder.loadTexts:
    voipPotsRingTable.setStatus("current")
_VoipPotsRingEntry_Object = MibTableRow
voipPotsRingEntry = _VoipPotsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1)
)
voipPotsRingEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "voipPotsRingIndex"),
)
if mibBuilder.loadTexts:
    voipPotsRingEntry.setStatus("current")
_VoipPotsRingIndex_Type = Integer32
_VoipPotsRingIndex_Object = MibTableColumn
voipPotsRingIndex = _VoipPotsRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 1),
    _VoipPotsRingIndex_Type()
)
voipPotsRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPotsRingIndex.setStatus("current")
_VoipPotsRingName_Type = DisplayString
_VoipPotsRingName_Object = MibTableColumn
voipPotsRingName = _VoipPotsRingName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 2),
    _VoipPotsRingName_Type()
)
voipPotsRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingName.setStatus("current")
_VoipPotsRingOn1_Type = Integer32
_VoipPotsRingOn1_Object = MibTableColumn
voipPotsRingOn1 = _VoipPotsRingOn1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 3),
    _VoipPotsRingOn1_Type()
)
voipPotsRingOn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOn1.setStatus("current")
_VoipPotsRingOff1_Type = Integer32
_VoipPotsRingOff1_Object = MibTableColumn
voipPotsRingOff1 = _VoipPotsRingOff1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 4),
    _VoipPotsRingOff1_Type()
)
voipPotsRingOff1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOff1.setStatus("current")
_VoipPotsRingOn2_Type = Integer32
_VoipPotsRingOn2_Object = MibTableColumn
voipPotsRingOn2 = _VoipPotsRingOn2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 5),
    _VoipPotsRingOn2_Type()
)
voipPotsRingOn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOn2.setStatus("current")
_VoipPotsRingOff2_Type = Integer32
_VoipPotsRingOff2_Object = MibTableColumn
voipPotsRingOff2 = _VoipPotsRingOff2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 6),
    _VoipPotsRingOff2_Type()
)
voipPotsRingOff2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOff2.setStatus("current")
_VoipPotsRingOn3_Type = Integer32
_VoipPotsRingOn3_Object = MibTableColumn
voipPotsRingOn3 = _VoipPotsRingOn3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 7),
    _VoipPotsRingOn3_Type()
)
voipPotsRingOn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOn3.setStatus("current")
_VoipPotsRingOff3_Type = Integer32
_VoipPotsRingOff3_Object = MibTableColumn
voipPotsRingOff3 = _VoipPotsRingOff3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 8),
    _VoipPotsRingOff3_Type()
)
voipPotsRingOff3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingOff3.setStatus("current")


class _VoipPotsRingSetDefault_Type(Integer32):
    """Custom type voipPotsRingSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("name", 1),
          ("pattern", 2))
    )


_VoipPotsRingSetDefault_Type.__name__ = "Integer32"
_VoipPotsRingSetDefault_Object = MibTableColumn
voipPotsRingSetDefault = _VoipPotsRingSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 4, 6, 1, 9),
    _VoipPotsRingSetDefault_Type()
)
voipPotsRingSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPotsRingSetDefault.setStatus("current")
_VoipCountryCode_Type = Integer32
_VoipCountryCode_Object = MibScalar
voipCountryCode = _VoipCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 5),
    _VoipCountryCode_Type()
)
voipCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipCountryCode.setStatus("current")
_VoipMaxNumOfDspProfiles_Type = Integer32
_VoipMaxNumOfDspProfiles_Object = MibScalar
voipMaxNumOfDspProfiles = _VoipMaxNumOfDspProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 6),
    _VoipMaxNumOfDspProfiles_Type()
)
voipMaxNumOfDspProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipMaxNumOfDspProfiles.setStatus("current")
_VoipDspProfileTable_Object = MibTable
voipDspProfileTable = _VoipDspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7)
)
if mibBuilder.loadTexts:
    voipDspProfileTable.setStatus("current")
_VoipDspProfileEntry_Object = MibTableRow
voipDspProfileEntry = _VoipDspProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1)
)
voipDspProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "voipDspProfileName"),
)
if mibBuilder.loadTexts:
    voipDspProfileEntry.setStatus("current")


class _VoipDspProfileName_Type(DisplayString):
    """Custom type voipDspProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipDspProfileName_Type.__name__ = "DisplayString"
_VoipDspProfileName_Object = MibTableColumn
voipDspProfileName = _VoipDspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 1),
    _VoipDspProfileName_Type()
)
voipDspProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDspProfileName.setStatus("current")
_VoipDspProfileCodec_Type = OctetString
_VoipDspProfileCodec_Object = MibTableColumn
voipDspProfileCodec = _VoipDspProfileCodec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 2),
    _VoipDspProfileCodec_Type()
)
voipDspProfileCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileCodec.setStatus("current")


class _VoipDspProfileDscp_Type(Integer32):
    """Custom type voipDspProfileDscp based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VoipDspProfileDscp_Type.__name__ = "Integer32"
_VoipDspProfileDscp_Object = MibTableColumn
voipDspProfileDscp = _VoipDspProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 3),
    _VoipDspProfileDscp_Type()
)
voipDspProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileDscp.setStatus("current")


class _VoipDspProfileEchoTail_Type(Integer32):
    """Custom type voipDspProfileEchoTail based on Integer32"""
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
        *(("echotailx8ms", 1),
          ("echotailx16ms", 2),
          ("echotailx32ms", 3),
          ("echotailx128ms", 4))
    )


_VoipDspProfileEchoTail_Type.__name__ = "Integer32"
_VoipDspProfileEchoTail_Object = MibTableColumn
voipDspProfileEchoTail = _VoipDspProfileEchoTail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 4),
    _VoipDspProfileEchoTail_Type()
)
voipDspProfileEchoTail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileEchoTail.setStatus("current")


class _VoipDspProfileEchoCancelEnable_Type(Integer32):
    """Custom type voipDspProfileEchoCancelEnable based on Integer32"""
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


_VoipDspProfileEchoCancelEnable_Type.__name__ = "Integer32"
_VoipDspProfileEchoCancelEnable_Object = MibTableColumn
voipDspProfileEchoCancelEnable = _VoipDspProfileEchoCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 5),
    _VoipDspProfileEchoCancelEnable_Type()
)
voipDspProfileEchoCancelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileEchoCancelEnable.setStatus("current")


class _VoipDspProfileG711Vpi_Type(Integer32):
    """Custom type voipDspProfileG711Vpi based on Integer32"""
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
        *(("intervalx10ms", 1),
          ("intervalx20ms", 2),
          ("intervalx30ms", 3),
          ("intervalx40ms", 4))
    )


_VoipDspProfileG711Vpi_Type.__name__ = "Integer32"
_VoipDspProfileG711Vpi_Object = MibTableColumn
voipDspProfileG711Vpi = _VoipDspProfileG711Vpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 6),
    _VoipDspProfileG711Vpi_Type()
)
voipDspProfileG711Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileG711Vpi.setStatus("current")


class _VoipDspProfileG723Vpi_Type(Integer32):
    """Custom type voipDspProfileG723Vpi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intervalx30ms", 1),
          ("intervalx60ms", 2))
    )


_VoipDspProfileG723Vpi_Type.__name__ = "Integer32"
_VoipDspProfileG723Vpi_Object = MibTableColumn
voipDspProfileG723Vpi = _VoipDspProfileG723Vpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 7),
    _VoipDspProfileG723Vpi_Type()
)
voipDspProfileG723Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileG723Vpi.setStatus("current")


class _VoipDspProfileG726Vpi_Type(Integer32):
    """Custom type voipDspProfileG726Vpi based on Integer32"""
    defaultValue = 2

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
        *(("intervalx10ms", 1),
          ("intervalx20ms", 2),
          ("intervalx30ms", 3),
          ("intervalx40ms", 4))
    )


_VoipDspProfileG726Vpi_Type.__name__ = "Integer32"
_VoipDspProfileG726Vpi_Object = MibTableColumn
voipDspProfileG726Vpi = _VoipDspProfileG726Vpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 8),
    _VoipDspProfileG726Vpi_Type()
)
voipDspProfileG726Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileG726Vpi.setStatus("current")


class _VoipDspProfileG729Vpi_Type(Integer32):
    """Custom type voipDspProfileG729Vpi based on Integer32"""
    defaultValue = 2

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
        *(("intervalx10ms", 1),
          ("intervalx20ms", 2),
          ("intervalx30ms", 3),
          ("intervalx40ms", 4),
          ("intervalx50ms", 5),
          ("intervalx60ms", 6))
    )


_VoipDspProfileG729Vpi_Type.__name__ = "Integer32"
_VoipDspProfileG729Vpi_Object = MibTableColumn
voipDspProfileG729Vpi = _VoipDspProfileG729Vpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 9),
    _VoipDspProfileG729Vpi_Type()
)
voipDspProfileG729Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileG729Vpi.setStatus("current")


class _VoipDspProfilePbit_Type(Integer32):
    """Custom type voipDspProfilePbit based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VoipDspProfilePbit_Type.__name__ = "Integer32"
_VoipDspProfilePbit_Object = MibTableColumn
voipDspProfilePbit = _VoipDspProfilePbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 10),
    _VoipDspProfilePbit_Type()
)
voipDspProfilePbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfilePbit.setStatus("current")


class _VoipDspProfilePlayBufferMinDelay_Type(Integer32):
    """Custom type voipDspProfilePlayBufferMinDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_VoipDspProfilePlayBufferMinDelay_Type.__name__ = "Integer32"
_VoipDspProfilePlayBufferMinDelay_Object = MibTableColumn
voipDspProfilePlayBufferMinDelay = _VoipDspProfilePlayBufferMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 11),
    _VoipDspProfilePlayBufferMinDelay_Type()
)
voipDspProfilePlayBufferMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfilePlayBufferMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    voipDspProfilePlayBufferMinDelay.setUnits("millisecond")


class _VoipDspProfilePlayBufferMaxDelay_Type(Integer32):
    """Custom type voipDspProfilePlayBufferMaxDelay based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_VoipDspProfilePlayBufferMaxDelay_Type.__name__ = "Integer32"
_VoipDspProfilePlayBufferMaxDelay_Object = MibTableColumn
voipDspProfilePlayBufferMaxDelay = _VoipDspProfilePlayBufferMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 12),
    _VoipDspProfilePlayBufferMaxDelay_Type()
)
voipDspProfilePlayBufferMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfilePlayBufferMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    voipDspProfilePlayBufferMaxDelay.setUnits("millisecond")


class _VoipDspProfileVadEnable_Type(Integer32):
    """Custom type voipDspProfileVadEnable based on Integer32"""
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


_VoipDspProfileVadEnable_Type.__name__ = "Integer32"
_VoipDspProfileVadEnable_Object = MibTableColumn
voipDspProfileVadEnable = _VoipDspProfileVadEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 13),
    _VoipDspProfileVadEnable_Type()
)
voipDspProfileVadEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileVadEnable.setStatus("current")
_VoipDspProfileRowStatus_Type = RowStatus
_VoipDspProfileRowStatus_Object = MibTableColumn
voipDspProfileRowStatus = _VoipDspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 7, 1, 14),
    _VoipDspProfileRowStatus_Type()
)
voipDspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipDspProfileRowStatus.setStatus("current")
_VoipPortConfTable_Object = MibTable
voipPortConfTable = _VoipPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8)
)
if mibBuilder.loadTexts:
    voipPortConfTable.setStatus("current")
_VoipPortConfEntry_Object = MibTableRow
voipPortConfEntry = _VoipPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1)
)
voipPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortConfEntry.setStatus("current")


class _VoipPortConfPortEnable_Type(Integer32):
    """Custom type voipPortConfPortEnable based on Integer32"""
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


_VoipPortConfPortEnable_Type.__name__ = "Integer32"
_VoipPortConfPortEnable_Object = MibTableColumn
voipPortConfPortEnable = _VoipPortConfPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 1),
    _VoipPortConfPortEnable_Type()
)
voipPortConfPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPortEnable.setStatus("current")


class _VoipPortConfDspProfile_Type(DisplayString):
    """Custom type voipPortConfDspProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoipPortConfDspProfile_Type.__name__ = "DisplayString"
_VoipPortConfDspProfile_Object = MibTableColumn
voipPortConfDspProfile = _VoipPortConfDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 2),
    _VoipPortConfDspProfile_Type()
)
voipPortConfDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfDspProfile.setStatus("current")


class _VoipPortConfVbdDspProfile_Type(DisplayString):
    """Custom type voipPortConfVbdDspProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoipPortConfVbdDspProfile_Type.__name__ = "DisplayString"
_VoipPortConfVbdDspProfile_Object = MibTableColumn
voipPortConfVbdDspProfile = _VoipPortConfVbdDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 3),
    _VoipPortConfVbdDspProfile_Type()
)
voipPortConfVbdDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfVbdDspProfile.setStatus("current")


class _VoipPortConfVbdDspProfileEnable_Type(Integer32):
    """Custom type voipPortConfVbdDspProfileEnable based on Integer32"""
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


_VoipPortConfVbdDspProfileEnable_Type.__name__ = "Integer32"
_VoipPortConfVbdDspProfileEnable_Object = MibTableColumn
voipPortConfVbdDspProfileEnable = _VoipPortConfVbdDspProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 4),
    _VoipPortConfVbdDspProfileEnable_Type()
)
voipPortConfVbdDspProfileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfVbdDspProfileEnable.setStatus("current")


class _VoipPortConfPotsBattery_Type(Integer32):
    """Custom type voipPortConfPotsBattery based on Integer32"""
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
          ("high", 2),
          ("boost", 3))
    )


_VoipPortConfPotsBattery_Type.__name__ = "Integer32"
_VoipPortConfPotsBattery_Object = MibTableColumn
voipPortConfPotsBattery = _VoipPortConfPotsBattery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 5),
    _VoipPortConfPotsBattery_Type()
)
voipPortConfPotsBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsBattery.setStatus("current")


class _VoipPortConfPotsTxGain_Type(Integer32):
    """Custom type voipPortConfPotsTxGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_VoipPortConfPotsTxGain_Type.__name__ = "Integer32"
_VoipPortConfPotsTxGain_Object = MibTableColumn
voipPortConfPotsTxGain = _VoipPortConfPotsTxGain_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 6),
    _VoipPortConfPotsTxGain_Type()
)
voipPortConfPotsTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsTxGain.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsTxGain.setUnits("1dB")


class _VoipPortConfPotsRxGain_Type(Integer32):
    """Custom type voipPortConfPotsRxGain based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_VoipPortConfPotsRxGain_Type.__name__ = "Integer32"
_VoipPortConfPotsRxGain_Object = MibTableColumn
voipPortConfPotsRxGain = _VoipPortConfPotsRxGain_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 7),
    _VoipPortConfPotsRxGain_Type()
)
voipPortConfPotsRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsRxGain.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsRxGain.setUnits("1dB")


class _VoipPortConfVoiceTxGain_Type(Integer32):
    """Custom type voipPortConfVoiceTxGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_VoipPortConfVoiceTxGain_Type.__name__ = "Integer32"
_VoipPortConfVoiceTxGain_Object = MibTableColumn
voipPortConfVoiceTxGain = _VoipPortConfVoiceTxGain_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 8),
    _VoipPortConfVoiceTxGain_Type()
)
voipPortConfVoiceTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfVoiceTxGain.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfVoiceTxGain.setUnits("1dB")


class _VoipPortConfVoiceRxGain_Type(Integer32):
    """Custom type voipPortConfVoiceRxGain based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_VoipPortConfVoiceRxGain_Type.__name__ = "Integer32"
_VoipPortConfVoiceRxGain_Object = MibTableColumn
voipPortConfVoiceRxGain = _VoipPortConfVoiceRxGain_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 9),
    _VoipPortConfVoiceRxGain_Type()
)
voipPortConfVoiceRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfVoiceRxGain.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfVoiceRxGain.setUnits("1dB")


class _VoipPortConfPotsImpedance_Type(Integer32):
    """Custom type voipPortConfPotsImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("impedancex600ohm", 0),
          ("impedancex600ohmx1000nf", 1),
          ("impedancex220ohmx820ohmx120nf", 2),
          ("impedancex270ohmx750ohmx150nf", 3),
          ("impedancex300ohmx1000ohmx220nf", 4),
          ("impedancex370ohmx620ohmx310nf", 5),
          ("impedancex220ohmx680ohmx100nf", 6),
          ("impedancex220ohmx820ohmx115nf", 7),
          ("impedancex900ohm", 8),
          ("impedancex200ohmx680ohmx100nf", 9),
          ("impedancex900ohmx2160nf", 10))
    )


_VoipPortConfPotsImpedance_Type.__name__ = "Integer32"
_VoipPortConfPotsImpedance_Object = MibTableColumn
voipPortConfPotsImpedance = _VoipPortConfPotsImpedance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 10),
    _VoipPortConfPotsImpedance_Type()
)
voipPortConfPotsImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsImpedance.setStatus("current")


class _VoipPortConfPotsImpedanceEnable_Type(Integer32):
    """Custom type voipPortConfPotsImpedanceEnable based on Integer32"""
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


_VoipPortConfPotsImpedanceEnable_Type.__name__ = "Integer32"
_VoipPortConfPotsImpedanceEnable_Object = MibTableColumn
voipPortConfPotsImpedanceEnable = _VoipPortConfPotsImpedanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 11),
    _VoipPortConfPotsImpedanceEnable_Type()
)
voipPortConfPotsImpedanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsImpedanceEnable.setStatus("current")


class _VoipPortConfH248TerminateId_Type(DisplayString):
    """Custom type voipPortConfH248TerminateId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoipPortConfH248TerminateId_Type.__name__ = "DisplayString"
_VoipPortConfH248TerminateId_Object = MibTableColumn
voipPortConfH248TerminateId = _VoipPortConfH248TerminateId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 12),
    _VoipPortConfH248TerminateId_Type()
)
voipPortConfH248TerminateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfH248TerminateId.setStatus("current")


class _VoipPortConfPmThreshProfile_Type(DisplayString):
    """Custom type voipPortConfPmThreshProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoipPortConfPmThreshProfile_Type.__name__ = "DisplayString"
_VoipPortConfPmThreshProfile_Object = MibTableColumn
voipPortConfPmThreshProfile = _VoipPortConfPmThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 13),
    _VoipPortConfPmThreshProfile_Type()
)
voipPortConfPmThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPmThreshProfile.setStatus("current")


class _VoipPortConfPotsTax_Type(Integer32):
    """Custom type voipPortConfPotsTax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tax_disable", 0),
          ("tax_12kHz", 1),
          ("tax_16kHz", 2),
          ("tax_reversal_12kHz", 3),
          ("tax_reversal_16kHz", 4),
          ("tax_reversal_steady", 5),
          ("tax_reversal_pulse", 6))
    )


_VoipPortConfPotsTax_Type.__name__ = "Integer32"
_VoipPortConfPotsTax_Object = MibTableColumn
voipPortConfPotsTax = _VoipPortConfPotsTax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 14),
    _VoipPortConfPotsTax_Type()
)
voipPortConfPotsTax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsTax.setStatus("current")


class _VoipPortConfPotsLoopCurrent_Type(Integer32):
    """Custom type voipPortConfPotsLoopCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_VoipPortConfPotsLoopCurrent_Type.__name__ = "Integer32"
_VoipPortConfPotsLoopCurrent_Object = MibTableColumn
voipPortConfPotsLoopCurrent = _VoipPortConfPotsLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 16),
    _VoipPortConfPotsLoopCurrent_Type()
)
voipPortConfPotsLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsLoopCurrent.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsLoopCurrent.setUnits("mA")


class _VoipPortConfTel_Type(DisplayString):
    """Custom type voipPortConfTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VoipPortConfTel_Type.__name__ = "DisplayString"
_VoipPortConfTel_Object = MibTableColumn
voipPortConfTel = _VoipPortConfTel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 17),
    _VoipPortConfTel_Type()
)
voipPortConfTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfTel.setStatus("current")


class _VoipPortConfName_Type(DisplayString):
    """Custom type voipPortConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_VoipPortConfName_Type.__name__ = "DisplayString"
_VoipPortConfName_Object = MibTableColumn
voipPortConfName = _VoipPortConfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 18),
    _VoipPortConfName_Type()
)
voipPortConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfName.setStatus("current")


class _VoipPortConfSipCallSvcProfile_Type(DisplayString):
    """Custom type voipPortConfSipCallSvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipPortConfSipCallSvcProfile_Type.__name__ = "DisplayString"
_VoipPortConfSipCallSvcProfile_Object = MibTableColumn
voipPortConfSipCallSvcProfile = _VoipPortConfSipCallSvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 20),
    _VoipPortConfSipCallSvcProfile_Type()
)
voipPortConfSipCallSvcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfSipCallSvcProfile.setStatus("current")


class _VoipPortConfHotline_Type(Integer32):
    """Custom type voipPortConfHotline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_VoipPortConfHotline_Type.__name__ = "Integer32"
_VoipPortConfHotline_Object = MibTableColumn
voipPortConfHotline = _VoipPortConfHotline_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 22),
    _VoipPortConfHotline_Type()
)
voipPortConfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfHotline.setStatus("current")


class _VoipPortConfHotlineTel_Type(DisplayString):
    """Custom type voipPortConfHotlineTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoipPortConfHotlineTel_Type.__name__ = "DisplayString"
_VoipPortConfHotlineTel_Object = MibTableColumn
voipPortConfHotlineTel = _VoipPortConfHotlineTel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 23),
    _VoipPortConfHotlineTel_Type()
)
voipPortConfHotlineTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfHotlineTel.setStatus("current")


class _VoipPortConfHotlineTimeout_Type(Integer32):
    """Custom type voipPortConfHotlineTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VoipPortConfHotlineTimeout_Type.__name__ = "Integer32"
_VoipPortConfHotlineTimeout_Object = MibTableColumn
voipPortConfHotlineTimeout = _VoipPortConfHotlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 24),
    _VoipPortConfHotlineTimeout_Type()
)
voipPortConfHotlineTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfHotlineTimeout.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfHotlineTimeout.setUnits("seconds")


class _VoipPortConfAccount_Type(DisplayString):
    """Custom type voipPortConfAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoipPortConfAccount_Type.__name__ = "DisplayString"
_VoipPortConfAccount_Object = MibTableColumn
voipPortConfAccount = _VoipPortConfAccount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 25),
    _VoipPortConfAccount_Type()
)
voipPortConfAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfAccount.setStatus("current")


class _VoipPortConfSipProfile_Type(DisplayString):
    """Custom type voipPortConfSipProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipPortConfSipProfile_Type.__name__ = "DisplayString"
_VoipPortConfSipProfile_Object = MibTableColumn
voipPortConfSipProfile = _VoipPortConfSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 26),
    _VoipPortConfSipProfile_Type()
)
voipPortConfSipProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfSipProfile.setStatus("current")


class _VoipPortConfPassword_Type(DisplayString):
    """Custom type voipPortConfPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_VoipPortConfPassword_Type.__name__ = "DisplayString"
_VoipPortConfPassword_Object = MibTableColumn
voipPortConfPassword = _VoipPortConfPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 27),
    _VoipPortConfPassword_Type()
)
voipPortConfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPassword.setStatus("current")
_VoipPortConfPotsLoopResistance_Type = Integer32
_VoipPortConfPotsLoopResistance_Object = MibTableColumn
voipPortConfPotsLoopResistance = _VoipPortConfPotsLoopResistance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 28),
    _VoipPortConfPotsLoopResistance_Type()
)
voipPortConfPotsLoopResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsLoopResistance.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsLoopResistance.setUnits("ohm")


class _VoipPortConfPotsCidAsType_Type(Integer32):
    """Custom type voipPortConfPotsCidAsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("defval", 0),
          ("cid-during-ring", 1),
          ("dtas-cid-before-ring", 2),
          ("rpas-cid-before-ring", 3),
          ("lr-dtas-cid-before-ring", 4),
          ("lr-cid-before-ring", 5),
          ("cid-before-ring", 6))
    )


_VoipPortConfPotsCidAsType_Type.__name__ = "Integer32"
_VoipPortConfPotsCidAsType_Object = MibTableColumn
voipPortConfPotsCidAsType = _VoipPortConfPotsCidAsType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 29),
    _VoipPortConfPotsCidAsType_Type()
)
voipPortConfPotsCidAsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsCidAsType.setStatus("current")


class _VoipPortConfPotsCidPayloadType_Type(Integer32):
    """Custom type voipPortConfPotsCidPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("defval", 0),
          ("mdmf", 1),
          ("sdmf", 2),
          ("etsi-mdmf", 3),
          ("etsi-sdmf", 4),
          ("dtmf", 5),
          ("uk-mdmf", 6),
          ("uk-sdmf", 7),
          ("japanese-mdmf", 8))
    )


_VoipPortConfPotsCidPayloadType_Type.__name__ = "Integer32"
_VoipPortConfPotsCidPayloadType_Object = MibTableColumn
voipPortConfPotsCidPayloadType = _VoipPortConfPotsCidPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 30),
    _VoipPortConfPotsCidPayloadType_Type()
)
voipPortConfPotsCidPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsCidPayloadType.setStatus("current")


class _VoipPortConfPotsVmwiFormat_Type(Integer32):
    """Custom type voipPortConfPotsVmwiFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("FSK", 0),
          ("Voltage", 2))
    )


_VoipPortConfPotsVmwiFormat_Type.__name__ = "Integer32"
_VoipPortConfPotsVmwiFormat_Object = MibTableColumn
voipPortConfPotsVmwiFormat = _VoipPortConfPotsVmwiFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 41),
    _VoipPortConfPotsVmwiFormat_Type()
)
voipPortConfPotsVmwiFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsVmwiFormat.setStatus("current")


class _VoipPortConfPotsHookFlashMaxTime_Type(Integer32):
    """Custom type voipPortConfPotsHookFlashMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1500),
    )


_VoipPortConfPotsHookFlashMaxTime_Type.__name__ = "Integer32"
_VoipPortConfPotsHookFlashMaxTime_Object = MibTableColumn
voipPortConfPotsHookFlashMaxTime = _VoipPortConfPotsHookFlashMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 42),
    _VoipPortConfPotsHookFlashMaxTime_Type()
)
voipPortConfPotsHookFlashMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsHookFlashMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsHookFlashMaxTime.setUnits("millisecond")


class _VoipPortConfPotsHookFlashMinTime_Type(Integer32):
    """Custom type voipPortConfPotsHookFlashMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1500),
    )


_VoipPortConfPotsHookFlashMinTime_Type.__name__ = "Integer32"
_VoipPortConfPotsHookFlashMinTime_Object = MibTableColumn
voipPortConfPotsHookFlashMinTime = _VoipPortConfPotsHookFlashMinTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 8, 1, 43),
    _VoipPortConfPotsHookFlashMinTime_Type()
)
voipPortConfPotsHookFlashMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortConfPotsHookFlashMinTime.setStatus("current")
if mibBuilder.loadTexts:
    voipPortConfPotsHookFlashMinTime.setUnits("millisecond")
_VoipPortStatisticTable_Object = MibTable
voipPortStatisticTable = _VoipPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9)
)
if mibBuilder.loadTexts:
    voipPortStatisticTable.setStatus("current")
_VoipPortStatisticEntry_Object = MibTableRow
voipPortStatisticEntry = _VoipPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1)
)
voipPortStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortStatisticEntry.setStatus("current")
_VoipPortStatisticCurrCallTime_Type = Counter32
_VoipPortStatisticCurrCallTime_Object = MibTableColumn
voipPortStatisticCurrCallTime = _VoipPortStatisticCurrCallTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 1),
    _VoipPortStatisticCurrCallTime_Type()
)
voipPortStatisticCurrCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticCurrCallTime.setStatus("current")
_VoipPortStatisticTotalCallTime_Type = Counter64
_VoipPortStatisticTotalCallTime_Object = MibTableColumn
voipPortStatisticTotalCallTime = _VoipPortStatisticTotalCallTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 2),
    _VoipPortStatisticTotalCallTime_Type()
)
voipPortStatisticTotalCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTotalCallTime.setStatus("current")
_VoipPortStatisticCallTimes_Type = Counter32
_VoipPortStatisticCallTimes_Object = MibTableColumn
voipPortStatisticCallTimes = _VoipPortStatisticCallTimes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 3),
    _VoipPortStatisticCallTimes_Type()
)
voipPortStatisticCallTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticCallTimes.setStatus("current")
_VoipPortStatisticTxRate_Type = Counter32
_VoipPortStatisticTxRate_Object = MibTableColumn
voipPortStatisticTxRate = _VoipPortStatisticTxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 4),
    _VoipPortStatisticTxRate_Type()
)
voipPortStatisticTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTxRate.setStatus("current")
_VoipPortStatisticRxRate_Type = Counter32
_VoipPortStatisticRxRate_Object = MibTableColumn
voipPortStatisticRxRate = _VoipPortStatisticRxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 5),
    _VoipPortStatisticRxRate_Type()
)
voipPortStatisticRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticRxRate.setStatus("current")
_VoipPortStatisticTxPktCnt_Type = Counter64
_VoipPortStatisticTxPktCnt_Object = MibTableColumn
voipPortStatisticTxPktCnt = _VoipPortStatisticTxPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 6),
    _VoipPortStatisticTxPktCnt_Type()
)
voipPortStatisticTxPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTxPktCnt.setStatus("current")
_VoipPortStatisticRxPktCnt_Type = Counter64
_VoipPortStatisticRxPktCnt_Object = MibTableColumn
voipPortStatisticRxPktCnt = _VoipPortStatisticRxPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 7),
    _VoipPortStatisticRxPktCnt_Type()
)
voipPortStatisticRxPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticRxPktCnt.setStatus("current")
_VoipPortStatisticTxFracLost_Type = Counter32
_VoipPortStatisticTxFracLost_Object = MibTableColumn
voipPortStatisticTxFracLost = _VoipPortStatisticTxFracLost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 8),
    _VoipPortStatisticTxFracLost_Type()
)
voipPortStatisticTxFracLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTxFracLost.setStatus("current")
_VoipPortStatisticRxFracLost_Type = Counter32
_VoipPortStatisticRxFracLost_Object = MibTableColumn
voipPortStatisticRxFracLost = _VoipPortStatisticRxFracLost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 9),
    _VoipPortStatisticRxFracLost_Type()
)
voipPortStatisticRxFracLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticRxFracLost.setStatus("current")
_VoipPortStatisticTxJitter_Type = Counter64
_VoipPortStatisticTxJitter_Object = MibTableColumn
voipPortStatisticTxJitter = _VoipPortStatisticTxJitter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 10),
    _VoipPortStatisticTxJitter_Type()
)
voipPortStatisticTxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTxJitter.setStatus("current")
_VoipPortStatisticRxJitter_Type = Counter64
_VoipPortStatisticRxJitter_Object = MibTableColumn
voipPortStatisticRxJitter = _VoipPortStatisticRxJitter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 11),
    _VoipPortStatisticRxJitter_Type()
)
voipPortStatisticRxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticRxJitter.setStatus("current")
_VoipPortStatisticTxAvgDelay_Type = Counter64
_VoipPortStatisticTxAvgDelay_Object = MibTableColumn
voipPortStatisticTxAvgDelay = _VoipPortStatisticTxAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 12),
    _VoipPortStatisticTxAvgDelay_Type()
)
voipPortStatisticTxAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticTxAvgDelay.setStatus("current")
_VoipPortStatisticRxAvgDelay_Type = Counter64
_VoipPortStatisticRxAvgDelay_Object = MibTableColumn
voipPortStatisticRxAvgDelay = _VoipPortStatisticRxAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 9, 1, 13),
    _VoipPortStatisticRxAvgDelay_Type()
)
voipPortStatisticRxAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortStatisticRxAvgDelay.setStatus("current")
_VoipPortLineStatusTable_Object = MibTable
voipPortLineStatusTable = _VoipPortLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 10)
)
if mibBuilder.loadTexts:
    voipPortLineStatusTable.setStatus("current")
_VoipPortLineStatusEntry_Object = MibTableRow
voipPortLineStatusEntry = _VoipPortLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 10, 1)
)
voipPortLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortLineStatusEntry.setStatus("current")


class _VoipPortLineStatusPhoneStatus_Type(Integer32):
    """Custom type voipPortLineStatusPhoneStatus based on Integer32"""
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
        *(("disabled", 1),
          ("onHook", 2),
          ("offHook", 3),
          ("ringing", 4),
          ("testing", 5),
          ("powerCutDown", 6),
          ("fault", 7),
          ("bad", 8),
          ("uninitialized", 9),
          ("unknown", 10))
    )


_VoipPortLineStatusPhoneStatus_Type.__name__ = "Integer32"
_VoipPortLineStatusPhoneStatus_Object = MibTableColumn
voipPortLineStatusPhoneStatus = _VoipPortLineStatusPhoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 10, 1, 1),
    _VoipPortLineStatusPhoneStatus_Type()
)
voipPortLineStatusPhoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineStatusPhoneStatus.setStatus("current")


class _VoipPortLineStatusServiceStatus_Type(Integer32):
    """Custom type voipPortLineStatusServiceStatus based on Integer32"""
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
        *(("disabled", 1),
          ("outOfService", 2),
          ("idle", 3),
          ("waitingForDialing", 4),
          ("dialingOut", 5),
          ("ringing", 6),
          ("conversationCaller", 7),
          ("conversationCallee", 8),
          ("faxOrModemCaller", 9),
          ("faxOrModemCallee", 10),
          ("waitingForOnHook", 11),
          ("dialingTimeout", 12),
          ("alertingOffHook", 13),
          ("powerCutDown", 14))
    )


_VoipPortLineStatusServiceStatus_Type.__name__ = "Integer32"
_VoipPortLineStatusServiceStatus_Object = MibTableColumn
voipPortLineStatusServiceStatus = _VoipPortLineStatusServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 10, 1, 2),
    _VoipPortLineStatusServiceStatus_Type()
)
voipPortLineStatusServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineStatusServiceStatus.setStatus("current")
_VoipPortLineInfoTable_Object = MibTable
voipPortLineInfoTable = _VoipPortLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11)
)
if mibBuilder.loadTexts:
    voipPortLineInfoTable.setStatus("current")
_VoipPortLineInfoEntry_Object = MibTableRow
voipPortLineInfoEntry = _VoipPortLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1)
)
voipPortLineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortLineInfoEntry.setStatus("current")


class _VoipPortLineInfoRtpTxCodecType_Type(Integer32):
    """Custom type voipPortLineInfoRtpTxCodecType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711mu", 2),
          ("g723", 3),
          ("g726x16", 4),
          ("g726x24", 5),
          ("g726x32", 6),
          ("g726x40", 7),
          ("g729ab", 8),
          ("t38", 9),
          ("g711aVbd", 10),
          ("g711muVbd", 11))
    )


_VoipPortLineInfoRtpTxCodecType_Type.__name__ = "Integer32"
_VoipPortLineInfoRtpTxCodecType_Object = MibTableColumn
voipPortLineInfoRtpTxCodecType = _VoipPortLineInfoRtpTxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 1),
    _VoipPortLineInfoRtpTxCodecType_Type()
)
voipPortLineInfoRtpTxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpTxCodecType.setStatus("current")


class _VoipPortLineInfoRtpRxCodecType_Type(Integer32):
    """Custom type voipPortLineInfoRtpRxCodecType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711mu", 2),
          ("g723", 3),
          ("g726x16", 4),
          ("g726x24", 5),
          ("g726x32", 6),
          ("g726x40", 7),
          ("g729ab", 8),
          ("t38", 9),
          ("g711aVbd", 10),
          ("g711muVbd", 11))
    )


_VoipPortLineInfoRtpRxCodecType_Type.__name__ = "Integer32"
_VoipPortLineInfoRtpRxCodecType_Object = MibTableColumn
voipPortLineInfoRtpRxCodecType = _VoipPortLineInfoRtpRxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 2),
    _VoipPortLineInfoRtpRxCodecType_Type()
)
voipPortLineInfoRtpRxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpRxCodecType.setStatus("current")
_VoipPortLineInfoRtpTxPt_Type = Integer32
_VoipPortLineInfoRtpTxPt_Object = MibTableColumn
voipPortLineInfoRtpTxPt = _VoipPortLineInfoRtpTxPt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 3),
    _VoipPortLineInfoRtpTxPt_Type()
)
voipPortLineInfoRtpTxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpTxPt.setStatus("current")
_VoipPortLineInfoRtpRxPt_Type = Integer32
_VoipPortLineInfoRtpRxPt_Object = MibTableColumn
voipPortLineInfoRtpRxPt = _VoipPortLineInfoRtpRxPt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 4),
    _VoipPortLineInfoRtpRxPt_Type()
)
voipPortLineInfoRtpRxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpRxPt.setStatus("current")
_VoipPortLineInfoRtpLocalIp_Type = IpAddress
_VoipPortLineInfoRtpLocalIp_Object = MibTableColumn
voipPortLineInfoRtpLocalIp = _VoipPortLineInfoRtpLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 5),
    _VoipPortLineInfoRtpLocalIp_Type()
)
voipPortLineInfoRtpLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpLocalIp.setStatus("current")
_VoipPortLineInfoRtpRemoteIp_Type = IpAddress
_VoipPortLineInfoRtpRemoteIp_Object = MibTableColumn
voipPortLineInfoRtpRemoteIp = _VoipPortLineInfoRtpRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 6),
    _VoipPortLineInfoRtpRemoteIp_Type()
)
voipPortLineInfoRtpRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpRemoteIp.setStatus("current")
_VoipPortLineInfoRtpLocalPort_Type = Integer32
_VoipPortLineInfoRtpLocalPort_Object = MibTableColumn
voipPortLineInfoRtpLocalPort = _VoipPortLineInfoRtpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 7),
    _VoipPortLineInfoRtpLocalPort_Type()
)
voipPortLineInfoRtpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpLocalPort.setStatus("current")
_VoipPortLineInfoRtpRemotePort_Type = Integer32
_VoipPortLineInfoRtpRemotePort_Object = MibTableColumn
voipPortLineInfoRtpRemotePort = _VoipPortLineInfoRtpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 11, 1, 8),
    _VoipPortLineInfoRtpRemotePort_Type()
)
voipPortLineInfoRtpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortLineInfoRtpRemotePort.setStatus("current")
_VoipOps_ObjectIdentity = ObjectIdentity
voipOps = _VoipOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 12)
)
_VoipTarget_Type = PortList
_VoipTarget_Object = MibScalar
voipTarget = _VoipTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 12, 1),
    _VoipTarget_Type()
)
voipTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTarget.setStatus("current")


class _VoipClearOperation_Type(Integer32):
    """Custom type voipClearOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clearControlPacketStastistics", 1),
          ("clearPortCallStatistics", 2),
          ("clearCurrPerformance", 4),
          ("clearCurr15MinPerformance", 5),
          ("clearHist15MinPerformance", 6),
          ("clearCurr1DayPerformance", 7),
          ("clearHist1DayPerformance", 8),
          ("clearSipControlPacketStatistics", 9))
    )


_VoipClearOperation_Type.__name__ = "Integer32"
_VoipClearOperation_Object = MibScalar
voipClearOperation = _VoipClearOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 12, 2),
    _VoipClearOperation_Type()
)
voipClearOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipClearOperation.setStatus("current")
_VoipRtpIp_ObjectIdentity = ObjectIdentity
voipRtpIp = _VoipRtpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13)
)
_VoipRtpIpAddress_Type = IpAddress
_VoipRtpIpAddress_Object = MibScalar
voipRtpIpAddress = _VoipRtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 1),
    _VoipRtpIpAddress_Type()
)
voipRtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpAddress.setStatus("current")


class _VoipRtpIpNetmask_Type(Integer32):
    """Custom type voipRtpIpNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VoipRtpIpNetmask_Type.__name__ = "Integer32"
_VoipRtpIpNetmask_Object = MibScalar
voipRtpIpNetmask = _VoipRtpIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 2),
    _VoipRtpIpNetmask_Type()
)
voipRtpIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpNetmask.setStatus("current")


class _VoipRtpIpVlanId_Type(VlanIndex):
    """Custom type voipRtpIpVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_VoipRtpIpVlanId_Type.__name__ = "VlanIndex"
_VoipRtpIpVlanId_Object = MibScalar
voipRtpIpVlanId = _VoipRtpIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 3),
    _VoipRtpIpVlanId_Type()
)
voipRtpIpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpVlanId.setStatus("current")
_VoipRtpIpDefaultGateway_Type = IpAddress
_VoipRtpIpDefaultGateway_Object = MibScalar
voipRtpIpDefaultGateway = _VoipRtpIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 4),
    _VoipRtpIpDefaultGateway_Type()
)
voipRtpIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpDefaultGateway.setStatus("current")


class _VoipRtpIpDhcpBootpEnable_Type(Integer32):
    """Custom type voipRtpIpDhcpBootpEnable based on Integer32"""
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


_VoipRtpIpDhcpBootpEnable_Type.__name__ = "Integer32"
_VoipRtpIpDhcpBootpEnable_Object = MibScalar
voipRtpIpDhcpBootpEnable = _VoipRtpIpDhcpBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 6),
    _VoipRtpIpDhcpBootpEnable_Type()
)
voipRtpIpDhcpBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpDhcpBootpEnable.setStatus("current")


class _VoipRtpIpDhcpOperation_Type(Integer32):
    """Custom type voipRtpIpDhcpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 1),
          ("renew", 2))
    )


_VoipRtpIpDhcpOperation_Type.__name__ = "Integer32"
_VoipRtpIpDhcpOperation_Object = MibScalar
voipRtpIpDhcpOperation = _VoipRtpIpDhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 7),
    _VoipRtpIpDhcpOperation_Type()
)
voipRtpIpDhcpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpDhcpOperation.setStatus("current")


class _VoipRtpIpOperation_Type(Integer32):
    """Custom type voipRtpIpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("removeAllRtpIpSettings", 1)
    )


_VoipRtpIpOperation_Type.__name__ = "Integer32"
_VoipRtpIpOperation_Object = MibScalar
voipRtpIpOperation = _VoipRtpIpOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 8),
    _VoipRtpIpOperation_Type()
)
voipRtpIpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpOperation.setStatus("current")


class _VoipRtpIpPbit_Type(Integer32):
    """Custom type voipRtpIpPbit based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VoipRtpIpPbit_Type.__name__ = "Integer32"
_VoipRtpIpPbit_Object = MibScalar
voipRtpIpPbit = _VoipRtpIpPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 13, 9),
    _VoipRtpIpPbit_Type()
)
voipRtpIpPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRtpIpPbit.setStatus("current")
_VoipH248Statistic_ObjectIdentity = ObjectIdentity
voipH248Statistic = _VoipH248Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14)
)
_VoipH248StatisticMsgSent_Type = Counter64
_VoipH248StatisticMsgSent_Object = MibScalar
voipH248StatisticMsgSent = _VoipH248StatisticMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 1),
    _VoipH248StatisticMsgSent_Type()
)
voipH248StatisticMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticMsgSent.setStatus("current")
_VoipH248StatisticMsgRecv_Type = Counter64
_VoipH248StatisticMsgRecv_Object = MibScalar
voipH248StatisticMsgRecv = _VoipH248StatisticMsgRecv_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 2),
    _VoipH248StatisticMsgRecv_Type()
)
voipH248StatisticMsgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticMsgRecv.setStatus("current")
_VoipH248StatisticMsgLost_Type = Counter32
_VoipH248StatisticMsgLost_Object = MibScalar
voipH248StatisticMsgLost = _VoipH248StatisticMsgLost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 3),
    _VoipH248StatisticMsgLost_Type()
)
voipH248StatisticMsgLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticMsgLost.setStatus("current")
_VoipH248StatisticMsgResent_Type = Counter32
_VoipH248StatisticMsgResent_Object = MibScalar
voipH248StatisticMsgResent = _VoipH248StatisticMsgResent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 4),
    _VoipH248StatisticMsgResent_Type()
)
voipH248StatisticMsgResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticMsgResent.setStatus("current")
_VoipH248StatisticErrorMsg_Type = Counter32
_VoipH248StatisticErrorMsg_Object = MibScalar
voipH248StatisticErrorMsg = _VoipH248StatisticErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 5),
    _VoipH248StatisticErrorMsg_Type()
)
voipH248StatisticErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticErrorMsg.setStatus("current")
_VoipH248StatisticUnIdentifiedMsg_Type = Counter32
_VoipH248StatisticUnIdentifiedMsg_Object = MibScalar
voipH248StatisticUnIdentifiedMsg = _VoipH248StatisticUnIdentifiedMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 14, 6),
    _VoipH248StatisticUnIdentifiedMsg_Type()
)
voipH248StatisticUnIdentifiedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatisticUnIdentifiedMsg.setStatus("current")
_Sip_ObjectIdentity = ObjectIdentity
sip = _Sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20)
)
_MaxNumOfSipProfiles_Type = Integer32
_MaxNumOfSipProfiles_Object = MibScalar
maxNumOfSipProfiles = _MaxNumOfSipProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 1),
    _MaxNumOfSipProfiles_Type()
)
maxNumOfSipProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipProfiles.setStatus("current")
_SipProfileTable_Object = MibTable
sipProfileTable = _SipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2)
)
if mibBuilder.loadTexts:
    sipProfileTable.setStatus("current")
_SipProfileEntry_Object = MibTableRow
sipProfileEntry = _SipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1)
)
sipProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "sipProfileName"),
)
if mibBuilder.loadTexts:
    sipProfileEntry.setStatus("current")


class _SipProfileName_Type(DisplayString):
    """Custom type sipProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipProfileName_Type.__name__ = "DisplayString"
_SipProfileName_Object = MibTableColumn
sipProfileName = _SipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 1),
    _SipProfileName_Type()
)
sipProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProfileName.setStatus("current")
_SipProfileSipSvr_Type = DisplayString
_SipProfileSipSvr_Object = MibTableColumn
sipProfileSipSvr = _SipProfileSipSvr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 2),
    _SipProfileSipSvr_Type()
)
sipProfileSipSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipSvr.setStatus("current")
_SipProfileRegSvr_Type = DisplayString
_SipProfileRegSvr_Object = MibTableColumn
sipProfileRegSvr = _SipProfileRegSvr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 3),
    _SipProfileRegSvr_Type()
)
sipProfileRegSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvr.setStatus("current")
_SipProfileProxySvr_Type = DisplayString
_SipProfileProxySvr_Object = MibTableColumn
sipProfileProxySvr = _SipProfileProxySvr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 4),
    _SipProfileProxySvr_Type()
)
sipProfileProxySvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvr.setStatus("current")


class _SipProfileSipPort_Type(Integer32):
    """Custom type sipProfileSipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileSipPort_Type.__name__ = "Integer32"
_SipProfileSipPort_Object = MibTableColumn
sipProfileSipPort = _SipProfileSipPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 5),
    _SipProfileSipPort_Type()
)
sipProfileSipPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipPort.setStatus("current")


class _SipProfileRegSvrPort_Type(Integer32):
    """Custom type sipProfileRegSvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileRegSvrPort_Type.__name__ = "Integer32"
_SipProfileRegSvrPort_Object = MibTableColumn
sipProfileRegSvrPort = _SipProfileRegSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 6),
    _SipProfileRegSvrPort_Type()
)
sipProfileRegSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvrPort.setStatus("current")


class _SipProfileProxySvrPort_Type(Integer32):
    """Custom type sipProfileProxySvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileProxySvrPort_Type.__name__ = "Integer32"
_SipProfileProxySvrPort_Object = MibTableColumn
sipProfileProxySvrPort = _SipProfileProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 7),
    _SipProfileProxySvrPort_Type()
)
sipProfileProxySvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvrPort.setStatus("current")


class _SipProfileUriType_Type(Integer32):
    """Custom type sipProfileUriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use_sip_uri", 1),
          ("use_tel_uri", 2))
    )


_SipProfileUriType_Type.__name__ = "Integer32"
_SipProfileUriType_Object = MibTableColumn
sipProfileUriType = _SipProfileUriType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 8),
    _SipProfileUriType_Type()
)
sipProfileUriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileUriType.setStatus("current")


class _SipProfileDscp_Type(Integer32):
    """Custom type sipProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SipProfileDscp_Type.__name__ = "Integer32"
_SipProfileDscp_Object = MibTableColumn
sipProfileDscp = _SipProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 10),
    _SipProfileDscp_Type()
)
sipProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileDscp.setStatus("current")


class _SipProfileKeepAlive_Type(Integer32):
    """Custom type sipProfileKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfileKeepAlive_Type.__name__ = "Integer32"
_SipProfileKeepAlive_Object = MibTableColumn
sipProfileKeepAlive = _SipProfileKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 11),
    _SipProfileKeepAlive_Type()
)
sipProfileKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileKeepAlive.setStatus("current")


class _SipProfilePrack_Type(Integer32):
    """Custom type sipProfilePrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfilePrack_Type.__name__ = "Integer32"
_SipProfilePrack_Object = MibTableColumn
sipProfilePrack = _SipProfilePrack_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 13),
    _SipProfilePrack_Type()
)
sipProfilePrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfilePrack.setStatus("current")
_SipProfileRowStatus_Type = RowStatus
_SipProfileRowStatus_Object = MibTableColumn
sipProfileRowStatus = _SipProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 14),
    _SipProfileRowStatus_Type()
)
sipProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRowStatus.setStatus("current")
_SipProfileRtpStartPort_Type = Integer32
_SipProfileRtpStartPort_Object = MibTableColumn
sipProfileRtpStartPort = _SipProfileRtpStartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 20),
    _SipProfileRtpStartPort_Type()
)
sipProfileRtpStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRtpStartPort.setStatus("current")
_SipProfileRtpEndPort_Type = Integer32
_SipProfileRtpEndPort_Object = MibTableColumn
sipProfileRtpEndPort = _SipProfileRtpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 21),
    _SipProfileRtpEndPort_Type()
)
sipProfileRtpEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRtpEndPort.setStatus("current")


class _SipProfileSwitchType_Type(Integer32):
    """Custom type sipProfileSwitchType based on Integer32"""
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
        *(("nsn", 1),
          ("alu", 2),
          ("hua", 3),
          ("isk", 4),
          ("zte", 5))
    )


_SipProfileSwitchType_Type.__name__ = "Integer32"
_SipProfileSwitchType_Object = MibTableColumn
sipProfileSwitchType = _SipProfileSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 27),
    _SipProfileSwitchType_Type()
)
sipProfileSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSwitchType.setStatus("current")
_SipProfileKeepAliveTimeOut_Type = Integer32
_SipProfileKeepAliveTimeOut_Object = MibTableColumn
sipProfileKeepAliveTimeOut = _SipProfileKeepAliveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 28),
    _SipProfileKeepAliveTimeOut_Type()
)
sipProfileKeepAliveTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileKeepAliveTimeOut.setStatus("current")


class _SipProfileFailRetry_Type(Integer32):
    """Custom type sipProfileFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 900),
    )


_SipProfileFailRetry_Type.__name__ = "Integer32"
_SipProfileFailRetry_Object = MibTableColumn
sipProfileFailRetry = _SipProfileFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 29),
    _SipProfileFailRetry_Type()
)
sipProfileFailRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileFailRetry.setStatus("current")


class _SipProfileRegTime_Type(Integer32):
    """Custom type sipProfileRegTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 65535),
    )


_SipProfileRegTime_Type.__name__ = "Integer32"
_SipProfileRegTime_Object = MibTableColumn
sipProfileRegTime = _SipProfileRegTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 30),
    _SipProfileRegTime_Type()
)
sipProfileRegTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegTime.setStatus("current")
if mibBuilder.loadTexts:
    sipProfileRegTime.setUnits("seconds")


class _SipProfileRegistration_Type(Integer32):
    """Custom type sipProfileRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfileRegistration_Type.__name__ = "Integer32"
_SipProfileRegistration_Object = MibTableColumn
sipProfileRegistration = _SipProfileRegistration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 31),
    _SipProfileRegistration_Type()
)
sipProfileRegistration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegistration.setStatus("current")


class _SipProfileDnsSvr_Type(Integer32):
    """Custom type sipProfileDnsSvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfileDnsSvr_Type.__name__ = "Integer32"
_SipProfileDnsSvr_Object = MibTableColumn
sipProfileDnsSvr = _SipProfileDnsSvr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 32),
    _SipProfileDnsSvr_Type()
)
sipProfileDnsSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileDnsSvr.setStatus("current")


class _SipProfileDualSvr_Type(Integer32):
    """Custom type sipProfileDualSvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfileDualSvr_Type.__name__ = "Integer32"
_SipProfileDualSvr_Object = MibTableColumn
sipProfileDualSvr = _SipProfileDualSvr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 33),
    _SipProfileDualSvr_Type()
)
sipProfileDualSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileDualSvr.setStatus("current")
_SipProfileSipSvr2_Type = DisplayString
_SipProfileSipSvr2_Object = MibTableColumn
sipProfileSipSvr2 = _SipProfileSipSvr2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 34),
    _SipProfileSipSvr2_Type()
)
sipProfileSipSvr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipSvr2.setStatus("current")
_SipProfileRegSvr2_Type = DisplayString
_SipProfileRegSvr2_Object = MibTableColumn
sipProfileRegSvr2 = _SipProfileRegSvr2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 35),
    _SipProfileRegSvr2_Type()
)
sipProfileRegSvr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvr2.setStatus("current")
_SipProfileProxySvr2_Type = DisplayString
_SipProfileProxySvr2_Object = MibTableColumn
sipProfileProxySvr2 = _SipProfileProxySvr2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 36),
    _SipProfileProxySvr2_Type()
)
sipProfileProxySvr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvr2.setStatus("current")


class _SipProfileSipPort2_Type(Integer32):
    """Custom type sipProfileSipPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileSipPort2_Type.__name__ = "Integer32"
_SipProfileSipPort2_Object = MibTableColumn
sipProfileSipPort2 = _SipProfileSipPort2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 37),
    _SipProfileSipPort2_Type()
)
sipProfileSipPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipPort2.setStatus("current")


class _SipProfileRegSvrPort2_Type(Integer32):
    """Custom type sipProfileRegSvrPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileRegSvrPort2_Type.__name__ = "Integer32"
_SipProfileRegSvrPort2_Object = MibTableColumn
sipProfileRegSvrPort2 = _SipProfileRegSvrPort2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 38),
    _SipProfileRegSvrPort2_Type()
)
sipProfileRegSvrPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvrPort2.setStatus("current")


class _SipProfileProxySvrPort2_Type(Integer32):
    """Custom type sipProfileProxySvrPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileProxySvrPort2_Type.__name__ = "Integer32"
_SipProfileProxySvrPort2_Object = MibTableColumn
sipProfileProxySvrPort2 = _SipProfileProxySvrPort2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 2, 1, 39),
    _SipProfileProxySvrPort2_Type()
)
sipProfileProxySvrPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvrPort2.setStatus("current")
_MaxNumOfSipCallSvcProfiles_Type = Integer32
_MaxNumOfSipCallSvcProfiles_Object = MibScalar
maxNumOfSipCallSvcProfiles = _MaxNumOfSipCallSvcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 3),
    _MaxNumOfSipCallSvcProfiles_Type()
)
maxNumOfSipCallSvcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipCallSvcProfiles.setStatus("current")
_SipCallSvcProfileTable_Object = MibTable
sipCallSvcProfileTable = _SipCallSvcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4)
)
if mibBuilder.loadTexts:
    sipCallSvcProfileTable.setStatus("current")
_SipCallSvcProfileEntry_Object = MibTableRow
sipCallSvcProfileEntry = _SipCallSvcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1)
)
sipCallSvcProfileEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "sipCallSvcProfileName"),
)
if mibBuilder.loadTexts:
    sipCallSvcProfileEntry.setStatus("current")


class _SipCallSvcProfileName_Type(DisplayString):
    """Custom type sipCallSvcProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipCallSvcProfileName_Type.__name__ = "DisplayString"
_SipCallSvcProfileName_Object = MibTableColumn
sipCallSvcProfileName = _SipCallSvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 1),
    _SipCallSvcProfileName_Type()
)
sipCallSvcProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCallSvcProfileName.setStatus("current")


class _SipCallSvcProfileDialPlanOn_Type(Integer32):
    """Custom type sipCallSvcProfileDialPlanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipCallSvcProfileDialPlanOn_Type.__name__ = "Integer32"
_SipCallSvcProfileDialPlanOn_Object = MibTableColumn
sipCallSvcProfileDialPlanOn = _SipCallSvcProfileDialPlanOn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 4),
    _SipCallSvcProfileDialPlanOn_Type()
)
sipCallSvcProfileDialPlanOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDialPlanOn.setStatus("current")


class _SipCallSvcProfileDialPlanCc_Type(DisplayString):
    """Custom type sipCallSvcProfileDialPlanCc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SipCallSvcProfileDialPlanCc_Type.__name__ = "DisplayString"
_SipCallSvcProfileDialPlanCc_Object = MibTableColumn
sipCallSvcProfileDialPlanCc = _SipCallSvcProfileDialPlanCc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 5),
    _SipCallSvcProfileDialPlanCc_Type()
)
sipCallSvcProfileDialPlanCc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDialPlanCc.setStatus("current")


class _SipCallSvcProfileDialPlanNdc_Type(DisplayString):
    """Custom type sipCallSvcProfileDialPlanNdc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SipCallSvcProfileDialPlanNdc_Type.__name__ = "DisplayString"
_SipCallSvcProfileDialPlanNdc_Object = MibTableColumn
sipCallSvcProfileDialPlanNdc = _SipCallSvcProfileDialPlanNdc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 6),
    _SipCallSvcProfileDialPlanNdc_Type()
)
sipCallSvcProfileDialPlanNdc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDialPlanNdc.setStatus("current")


class _SipCallSvcProfileDialPlanTable_Type(DisplayString):
    """Custom type sipCallSvcProfileDialPlanTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipCallSvcProfileDialPlanTable_Type.__name__ = "DisplayString"
_SipCallSvcProfileDialPlanTable_Object = MibTableColumn
sipCallSvcProfileDialPlanTable = _SipCallSvcProfileDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 7),
    _SipCallSvcProfileDialPlanTable_Type()
)
sipCallSvcProfileDialPlanTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDialPlanTable.setStatus("current")
_SipCallSvcProfileStateMask_Type = Integer32
_SipCallSvcProfileStateMask_Object = MibTableColumn
sipCallSvcProfileStateMask = _SipCallSvcProfileStateMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 8),
    _SipCallSvcProfileStateMask_Type()
)
sipCallSvcProfileStateMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileStateMask.setStatus("current")


class _SipCallSvcProfileDtmf_Type(Integer32):
    """Custom type sipCallSvcProfileDtmf based on Integer32"""
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
        *(("bypass", 1),
          ("rfc2833", 2),
          ("sipinfo", 3),
          ("rfc2833like", 4),
          ("plaintext", 5))
    )


_SipCallSvcProfileDtmf_Type.__name__ = "Integer32"
_SipCallSvcProfileDtmf_Object = MibTableColumn
sipCallSvcProfileDtmf = _SipCallSvcProfileDtmf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 9),
    _SipCallSvcProfileDtmf_Type()
)
sipCallSvcProfileDtmf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDtmf.setStatus("current")


class _SipCallSvcProfileDtmfRfc2833PayloadType_Type(Integer32):
    """Custom type sipCallSvcProfileDtmfRfc2833PayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_SipCallSvcProfileDtmfRfc2833PayloadType_Type.__name__ = "Integer32"
_SipCallSvcProfileDtmfRfc2833PayloadType_Object = MibTableColumn
sipCallSvcProfileDtmfRfc2833PayloadType = _SipCallSvcProfileDtmfRfc2833PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 10),
    _SipCallSvcProfileDtmfRfc2833PayloadType_Type()
)
sipCallSvcProfileDtmfRfc2833PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDtmfRfc2833PayloadType.setStatus("current")


class _SipCallSvcProfileFax_Type(Integer32):
    """Custom type sipCallSvcProfileFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("t38", 2),
          ("g711mu", 3))
    )


_SipCallSvcProfileFax_Type.__name__ = "Integer32"
_SipCallSvcProfileFax_Object = MibTableColumn
sipCallSvcProfileFax = _SipCallSvcProfileFax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 11),
    _SipCallSvcProfileFax_Type()
)
sipCallSvcProfileFax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFax.setStatus("current")
_SipCallSvcProfileRowStatus_Type = RowStatus
_SipCallSvcProfileRowStatus_Object = MibTableColumn
sipCallSvcProfileRowStatus = _SipCallSvcProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 12),
    _SipCallSvcProfileRowStatus_Type()
)
sipCallSvcProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileRowStatus.setStatus("current")


class _SipCallSvcProfileKeypattern_Type(DisplayString):
    """Custom type sipCallSvcProfileKeypattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipCallSvcProfileKeypattern_Type.__name__ = "DisplayString"
_SipCallSvcProfileKeypattern_Object = MibTableColumn
sipCallSvcProfileKeypattern = _SipCallSvcProfileKeypattern_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 13),
    _SipCallSvcProfileKeypattern_Type()
)
sipCallSvcProfileKeypattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileKeypattern.setStatus("current")


class _SipCallSvcProfileFlash_Type(Integer32):
    """Custom type sipCallSvcProfileFlash based on Integer32"""
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
        *(("invite", 1),
          ("rfc2833", 2),
          ("rfc2833like", 3),
          ("sipinfo1", 4),
          ("sipinfo2", 5),
          ("sipinfo3", 6),
          ("sipinfo4", 7),
          ("sipinfo5", 8),
          ("sipinfo6", 9))
    )


_SipCallSvcProfileFlash_Type.__name__ = "Integer32"
_SipCallSvcProfileFlash_Object = MibTableColumn
sipCallSvcProfileFlash = _SipCallSvcProfileFlash_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 15),
    _SipCallSvcProfileFlash_Type()
)
sipCallSvcProfileFlash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlash.setStatus("current")
_SipCallSvcProfileFlashPattern_Type = DisplayString
_SipCallSvcProfileFlashPattern_Object = MibTableColumn
sipCallSvcProfileFlashPattern = _SipCallSvcProfileFlashPattern_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 16),
    _SipCallSvcProfileFlashPattern_Type()
)
sipCallSvcProfileFlashPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlashPattern.setStatus("current")
_SipCallSvcProfileFirstDigit_Type = Integer32
_SipCallSvcProfileFirstDigit_Object = MibTableColumn
sipCallSvcProfileFirstDigit = _SipCallSvcProfileFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 18),
    _SipCallSvcProfileFirstDigit_Type()
)
sipCallSvcProfileFirstDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFirstDigit.setStatus("current")
_SipCallSvcProfileInterDigit_Type = Integer32
_SipCallSvcProfileInterDigit_Object = MibTableColumn
sipCallSvcProfileInterDigit = _SipCallSvcProfileInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 19),
    _SipCallSvcProfileInterDigit_Type()
)
sipCallSvcProfileInterDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileInterDigit.setStatus("current")


class _SipCallSvcProfileCentrex_Type(Integer32):
    """Custom type sipCallSvcProfileCentrex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipCallSvcProfileCentrex_Type.__name__ = "Integer32"
_SipCallSvcProfileCentrex_Object = MibTableColumn
sipCallSvcProfileCentrex = _SipCallSvcProfileCentrex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 4, 1, 20),
    _SipCallSvcProfileCentrex_Type()
)
sipCallSvcProfileCentrex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileCentrex.setStatus("current")
_MaxNumOfSipDialPlan_Type = Integer32
_MaxNumOfSipDialPlan_Object = MibScalar
maxNumOfSipDialPlan = _MaxNumOfSipDialPlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 8),
    _MaxNumOfSipDialPlan_Type()
)
maxNumOfSipDialPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipDialPlan.setStatus("current")
_MaxNumOfSipKeyPattern_Type = Integer32
_MaxNumOfSipKeyPattern_Object = MibScalar
maxNumOfSipKeyPattern = _MaxNumOfSipKeyPattern_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 12),
    _MaxNumOfSipKeyPattern_Type()
)
maxNumOfSipKeyPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipKeyPattern.setStatus("current")
_SipDialPlanTable_Object = MibTable
sipDialPlanTable = _SipDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 18)
)
if mibBuilder.loadTexts:
    sipDialPlanTable.setStatus("current")
_SipDialPlanEntry_Object = MibTableRow
sipDialPlanEntry = _SipDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 18, 1)
)
sipDialPlanEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "sipDialPlanName"),
)
if mibBuilder.loadTexts:
    sipDialPlanEntry.setStatus("current")


class _SipDialPlanName_Type(DisplayString):
    """Custom type sipDialPlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipDialPlanName_Type.__name__ = "DisplayString"
_SipDialPlanName_Object = MibTableColumn
sipDialPlanName = _SipDialPlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 18, 1, 1),
    _SipDialPlanName_Type()
)
sipDialPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDialPlanName.setStatus("current")
_SipDialPlanRowStatus_Type = RowStatus
_SipDialPlanRowStatus_Object = MibTableColumn
sipDialPlanRowStatus = _SipDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 18, 1, 2),
    _SipDialPlanRowStatus_Type()
)
sipDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipDialPlanRowStatus.setStatus("current")
_SipDialPlanContentTable_Object = MibTable
sipDialPlanContentTable = _SipDialPlanContentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 19)
)
if mibBuilder.loadTexts:
    sipDialPlanContentTable.setStatus("current")
_SipDialPlanContentEntry_Object = MibTableRow
sipDialPlanContentEntry = _SipDialPlanContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 19, 1)
)
sipDialPlanContentEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "sipDialPlanName"),
    (0, "VES1724-58V-MIB", "sipDialPlanIndex"),
)
if mibBuilder.loadTexts:
    sipDialPlanContentEntry.setStatus("current")


class _SipDialPlanIndex_Type(Integer32):
    """Custom type sipDialPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SipDialPlanIndex_Type.__name__ = "Integer32"
_SipDialPlanIndex_Object = MibTableColumn
sipDialPlanIndex = _SipDialPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 19, 1, 1),
    _SipDialPlanIndex_Type()
)
sipDialPlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDialPlanIndex.setStatus("current")


class _SipDialPlanPattern_Type(DisplayString):
    """Custom type sipDialPlanPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_SipDialPlanPattern_Type.__name__ = "DisplayString"
_SipDialPlanPattern_Object = MibTableColumn
sipDialPlanPattern = _SipDialPlanPattern_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 19, 1, 2),
    _SipDialPlanPattern_Type()
)
sipDialPlanPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDialPlanPattern.setStatus("current")


class _SipDialPlanRule_Type(DisplayString):
    """Custom type sipDialPlanRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_SipDialPlanRule_Type.__name__ = "DisplayString"
_SipDialPlanRule_Object = MibTableColumn
sipDialPlanRule = _SipDialPlanRule_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 19, 1, 3),
    _SipDialPlanRule_Type()
)
sipDialPlanRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDialPlanRule.setStatus("current")
_SipKeyPatternTable_Object = MibTable
sipKeyPatternTable = _SipKeyPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 20)
)
if mibBuilder.loadTexts:
    sipKeyPatternTable.setStatus("current")
_SipKeyPatternEntry_Object = MibTableRow
sipKeyPatternEntry = _SipKeyPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 20, 1)
)
sipKeyPatternEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "sipKeyPatternName"),
)
if mibBuilder.loadTexts:
    sipKeyPatternEntry.setStatus("current")


class _SipKeyPatternName_Type(DisplayString):
    """Custom type sipKeyPatternName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipKeyPatternName_Type.__name__ = "DisplayString"
_SipKeyPatternName_Object = MibTableColumn
sipKeyPatternName = _SipKeyPatternName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 20, 1, 1),
    _SipKeyPatternName_Type()
)
sipKeyPatternName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipKeyPatternName.setStatus("current")
_SipKeyPatternRowStatus_Type = RowStatus
_SipKeyPatternRowStatus_Object = MibTableColumn
sipKeyPatternRowStatus = _SipKeyPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 20, 1, 2),
    _SipKeyPatternRowStatus_Type()
)
sipKeyPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipKeyPatternRowStatus.setStatus("current")
_SipKeyPatternContentTable_Object = MibTable
sipKeyPatternContentTable = _SipKeyPatternContentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 21)
)
if mibBuilder.loadTexts:
    sipKeyPatternContentTable.setStatus("current")
_SipKeyPatternContentEntry_Object = MibTableRow
sipKeyPatternContentEntry = _SipKeyPatternContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 21, 1)
)
sipKeyPatternContentEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "sipKeyPatternName"),
    (0, "VES1724-58V-MIB", "sipKeyPatternServiceType"),
)
if mibBuilder.loadTexts:
    sipKeyPatternContentEntry.setStatus("current")


class _SipKeyPatternServiceType_Type(Integer32):
    """Custom type sipKeyPatternServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("clir", 8),
          ("dndoff", 9),
          ("dndon", 10))
    )


_SipKeyPatternServiceType_Type.__name__ = "Integer32"
_SipKeyPatternServiceType_Object = MibTableColumn
sipKeyPatternServiceType = _SipKeyPatternServiceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 21, 1, 1),
    _SipKeyPatternServiceType_Type()
)
sipKeyPatternServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipKeyPatternServiceType.setStatus("current")


class _SipKeyPatternPattern_Type(DisplayString):
    """Custom type sipKeyPatternPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SipKeyPatternPattern_Type.__name__ = "DisplayString"
_SipKeyPatternPattern_Object = MibTableColumn
sipKeyPatternPattern = _SipKeyPatternPattern_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 20, 21, 1, 2),
    _SipKeyPatternPattern_Type()
)
sipKeyPatternPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeyPatternPattern.setStatus("current")
_VoipSIPStatistic_ObjectIdentity = ObjectIdentity
voipSIPStatistic = _VoipSIPStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21)
)
_VoipSIPStatisticMsgSent_Type = Counter64
_VoipSIPStatisticMsgSent_Object = MibScalar
voipSIPStatisticMsgSent = _VoipSIPStatisticMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 1),
    _VoipSIPStatisticMsgSent_Type()
)
voipSIPStatisticMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticMsgSent.setStatus("current")
_VoipSIPStatisticMsgRecv_Type = Counter64
_VoipSIPStatisticMsgRecv_Object = MibScalar
voipSIPStatisticMsgRecv = _VoipSIPStatisticMsgRecv_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 2),
    _VoipSIPStatisticMsgRecv_Type()
)
voipSIPStatisticMsgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticMsgRecv.setStatus("current")
_VoipSIPStatisticMsgLost_Type = Counter32
_VoipSIPStatisticMsgLost_Object = MibScalar
voipSIPStatisticMsgLost = _VoipSIPStatisticMsgLost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 3),
    _VoipSIPStatisticMsgLost_Type()
)
voipSIPStatisticMsgLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticMsgLost.setStatus("current")
_VoipSIPStatisticMsgResent_Type = Counter32
_VoipSIPStatisticMsgResent_Object = MibScalar
voipSIPStatisticMsgResent = _VoipSIPStatisticMsgResent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 4),
    _VoipSIPStatisticMsgResent_Type()
)
voipSIPStatisticMsgResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticMsgResent.setStatus("current")
_VoipSIPStatisticErrorMsg_Type = Counter32
_VoipSIPStatisticErrorMsg_Object = MibScalar
voipSIPStatisticErrorMsg = _VoipSIPStatisticErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 5),
    _VoipSIPStatisticErrorMsg_Type()
)
voipSIPStatisticErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticErrorMsg.setStatus("current")
_VoipSIPStatisticUnIdentifiedMsg_Type = Counter32
_VoipSIPStatisticUnIdentifiedMsg_Object = MibScalar
voipSIPStatisticUnIdentifiedMsg = _VoipSIPStatisticUnIdentifiedMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 21, 6),
    _VoipSIPStatisticUnIdentifiedMsg_Type()
)
voipSIPStatisticUnIdentifiedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipSIPStatisticUnIdentifiedMsg.setStatus("current")


class _VoipProtocolMode_Type(Integer32):
    """Custom type voipProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("h248", 2))
    )


_VoipProtocolMode_Type.__name__ = "Integer32"
_VoipProtocolMode_Object = MibScalar
voipProtocolMode = _VoipProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 18, 22),
    _VoipProtocolMode_Type()
)
voipProtocolMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipProtocolMode.setStatus("current")
_Coa_ObjectIdentity = ObjectIdentity
coa = _Coa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20)
)


class _CoaConfIssueThreshold_Type(Unsigned32):
    """Custom type coaConfIssueThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoaConfIssueThreshold_Type.__name__ = "Unsigned32"
_CoaConfIssueThreshold_Object = MibScalar
coaConfIssueThreshold = _CoaConfIssueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 1),
    _CoaConfIssueThreshold_Type()
)
coaConfIssueThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coaConfIssueThreshold.setStatus("current")


class _CoaConfClearThreshold_Type(Unsigned32):
    """Custom type coaConfClearThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoaConfClearThreshold_Type.__name__ = "Unsigned32"
_CoaConfClearThreshold_Object = MibScalar
coaConfClearThreshold = _CoaConfClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 2),
    _CoaConfClearThreshold_Type()
)
coaConfClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coaConfClearThreshold.setStatus("current")


class _CoaConfSampleSeconds_Type(Unsigned32):
    """Custom type coaConfSampleSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CoaConfSampleSeconds_Type.__name__ = "Unsigned32"
_CoaConfSampleSeconds_Object = MibScalar
coaConfSampleSeconds = _CoaConfSampleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 3),
    _CoaConfSampleSeconds_Type()
)
coaConfSampleSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coaConfSampleSeconds.setStatus("current")


class _CoaConfAnalyticMethod_Type(Integer32):
    """Custom type coaConfAnalyticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 1),
          ("average", 2))
    )


_CoaConfAnalyticMethod_Type.__name__ = "Integer32"
_CoaConfAnalyticMethod_Object = MibScalar
coaConfAnalyticMethod = _CoaConfAnalyticMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 4),
    _CoaConfAnalyticMethod_Type()
)
coaConfAnalyticMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coaConfAnalyticMethod.setStatus("current")
_CpuUtilizationTable_Object = MibTable
cpuUtilizationTable = _CpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 5)
)
if mibBuilder.loadTexts:
    cpuUtilizationTable.setStatus("current")
_CpuUtilizationEntry_Object = MibTableRow
cpuUtilizationEntry = _CpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 5, 1)
)
cpuUtilizationEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "cpuSecondIndex"),
)
if mibBuilder.loadTexts:
    cpuUtilizationEntry.setStatus("current")
_CpuSecondIndex_Type = Integer32
_CpuSecondIndex_Object = MibTableColumn
cpuSecondIndex = _CpuSecondIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 5, 1, 1),
    _CpuSecondIndex_Type()
)
cpuSecondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSecondIndex.setStatus("current")
_CpuValue_Type = Integer32
_CpuValue_Object = MibTableColumn
cpuValue = _CpuValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 20, 5, 1, 2),
    _CpuValue_Type()
)
cpuValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuValue.setStatus("current")
if mibBuilder.loadTexts:
    cpuValue.setUnits("0.01 Percent")
_Pm_ObjectIdentity = ObjectIdentity
pm = _Pm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22)
)
_GePmCurr15minTable_Object = MibTable
gePmCurr15minTable = _GePmCurr15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1)
)
if mibBuilder.loadTexts:
    gePmCurr15minTable.setStatus("current")
_GePmCurr15minEntry_Object = MibTableRow
gePmCurr15minEntry = _GePmCurr15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1)
)
gePmCurr15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gePmCurr15minEntry.setStatus("current")
_GePmCurr15minElapsed_Type = Integer32
_GePmCurr15minElapsed_Object = MibTableColumn
gePmCurr15minElapsed = _GePmCurr15minElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 1),
    _GePmCurr15minElapsed_Type()
)
gePmCurr15minElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minElapsed.setStatus("current")
_GePmCurr15minTxOctets_Type = Counter64
_GePmCurr15minTxOctets_Object = MibTableColumn
gePmCurr15minTxOctets = _GePmCurr15minTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 2),
    _GePmCurr15minTxOctets_Type()
)
gePmCurr15minTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minTxOctets.setStatus("current")
_GePmCurr15minTxPkts_Type = Counter64
_GePmCurr15minTxPkts_Object = MibTableColumn
gePmCurr15minTxPkts = _GePmCurr15minTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 3),
    _GePmCurr15minTxPkts_Type()
)
gePmCurr15minTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minTxPkts.setStatus("current")
_GePmCurr15minTxBroadcastPkts_Type = Counter64
_GePmCurr15minTxBroadcastPkts_Object = MibTableColumn
gePmCurr15minTxBroadcastPkts = _GePmCurr15minTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 4),
    _GePmCurr15minTxBroadcastPkts_Type()
)
gePmCurr15minTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minTxBroadcastPkts.setStatus("current")
_GePmCurr15minTxMulticastPkts_Type = Counter64
_GePmCurr15minTxMulticastPkts_Object = MibTableColumn
gePmCurr15minTxMulticastPkts = _GePmCurr15minTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 5),
    _GePmCurr15minTxMulticastPkts_Type()
)
gePmCurr15minTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minTxMulticastPkts.setStatus("current")
_GePmCurr15minRxOctets_Type = Counter64
_GePmCurr15minRxOctets_Object = MibTableColumn
gePmCurr15minRxOctets = _GePmCurr15minRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 6),
    _GePmCurr15minRxOctets_Type()
)
gePmCurr15minRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxOctets.setStatus("current")
_GePmCurr15minRxPkts_Type = Counter64
_GePmCurr15minRxPkts_Object = MibTableColumn
gePmCurr15minRxPkts = _GePmCurr15minRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 7),
    _GePmCurr15minRxPkts_Type()
)
gePmCurr15minRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxPkts.setStatus("current")
_GePmCurr15minRxBroadcastPkts_Type = Counter64
_GePmCurr15minRxBroadcastPkts_Object = MibTableColumn
gePmCurr15minRxBroadcastPkts = _GePmCurr15minRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 8),
    _GePmCurr15minRxBroadcastPkts_Type()
)
gePmCurr15minRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxBroadcastPkts.setStatus("current")
_GePmCurr15minRxMulticastPkts_Type = Counter64
_GePmCurr15minRxMulticastPkts_Object = MibTableColumn
gePmCurr15minRxMulticastPkts = _GePmCurr15minRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 9),
    _GePmCurr15minRxMulticastPkts_Type()
)
gePmCurr15minRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxMulticastPkts.setStatus("current")
_GePmCurr15minRxCRCAlignErrors_Type = Counter64
_GePmCurr15minRxCRCAlignErrors_Object = MibTableColumn
gePmCurr15minRxCRCAlignErrors = _GePmCurr15minRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 10),
    _GePmCurr15minRxCRCAlignErrors_Type()
)
gePmCurr15minRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxCRCAlignErrors.setStatus("current")
_GePmCurr15minRxUndersizePkts_Type = Counter64
_GePmCurr15minRxUndersizePkts_Object = MibTableColumn
gePmCurr15minRxUndersizePkts = _GePmCurr15minRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 11),
    _GePmCurr15minRxUndersizePkts_Type()
)
gePmCurr15minRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxUndersizePkts.setStatus("current")
_GePmCurr15minRxOversizePkts_Type = Counter64
_GePmCurr15minRxOversizePkts_Object = MibTableColumn
gePmCurr15minRxOversizePkts = _GePmCurr15minRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 12),
    _GePmCurr15minRxOversizePkts_Type()
)
gePmCurr15minRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxOversizePkts.setStatus("current")
_GePmCurr15minRxFragments_Type = Counter64
_GePmCurr15minRxFragments_Object = MibTableColumn
gePmCurr15minRxFragments = _GePmCurr15minRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 13),
    _GePmCurr15minRxFragments_Type()
)
gePmCurr15minRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minRxFragments.setStatus("current")
_GePmCurr15minCollisions_Type = Counter64
_GePmCurr15minCollisions_Object = MibTableColumn
gePmCurr15minCollisions = _GePmCurr15minCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 14),
    _GePmCurr15minCollisions_Type()
)
gePmCurr15minCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minCollisions.setStatus("current")
_GePmCurr15minPkts64Octets_Type = Counter64
_GePmCurr15minPkts64Octets_Object = MibTableColumn
gePmCurr15minPkts64Octets = _GePmCurr15minPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 15),
    _GePmCurr15minPkts64Octets_Type()
)
gePmCurr15minPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts64Octets.setStatus("current")
_GePmCurr15minPkts65to127Octets_Type = Counter64
_GePmCurr15minPkts65to127Octets_Object = MibTableColumn
gePmCurr15minPkts65to127Octets = _GePmCurr15minPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 16),
    _GePmCurr15minPkts65to127Octets_Type()
)
gePmCurr15minPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts65to127Octets.setStatus("current")
_GePmCurr15minPkts128to255Octets_Type = Counter64
_GePmCurr15minPkts128to255Octets_Object = MibTableColumn
gePmCurr15minPkts128to255Octets = _GePmCurr15minPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 17),
    _GePmCurr15minPkts128to255Octets_Type()
)
gePmCurr15minPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts128to255Octets.setStatus("current")
_GePmCurr15minPkts256to511Octets_Type = Counter64
_GePmCurr15minPkts256to511Octets_Object = MibTableColumn
gePmCurr15minPkts256to511Octets = _GePmCurr15minPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 18),
    _GePmCurr15minPkts256to511Octets_Type()
)
gePmCurr15minPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts256to511Octets.setStatus("current")
_GePmCurr15minPkts512to1023Octets_Type = Counter64
_GePmCurr15minPkts512to1023Octets_Object = MibTableColumn
gePmCurr15minPkts512to1023Octets = _GePmCurr15minPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 19),
    _GePmCurr15minPkts512to1023Octets_Type()
)
gePmCurr15minPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts512to1023Octets.setStatus("current")
_GePmCurr15minPkts1024to1518Octets_Type = Counter64
_GePmCurr15minPkts1024to1518Octets_Object = MibTableColumn
gePmCurr15minPkts1024to1518Octets = _GePmCurr15minPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 20),
    _GePmCurr15minPkts1024to1518Octets_Type()
)
gePmCurr15minPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts1024to1518Octets.setStatus("current")
_GePmCurr15minPkts1519to1522Octets_Type = Counter64
_GePmCurr15minPkts1519to1522Octets_Object = MibTableColumn
gePmCurr15minPkts1519to1522Octets = _GePmCurr15minPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 1, 1, 21),
    _GePmCurr15minPkts1519to1522Octets_Type()
)
gePmCurr15minPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr15minPkts1519to1522Octets.setStatus("current")
_GePmHist15minTable_Object = MibTable
gePmHist15minTable = _GePmHist15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2)
)
if mibBuilder.loadTexts:
    gePmHist15minTable.setStatus("current")
_GePmHist15minEntry_Object = MibTableRow
gePmHist15minEntry = _GePmHist15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1)
)
gePmHist15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "gePmHist15minIndex"),
)
if mibBuilder.loadTexts:
    gePmHist15minEntry.setStatus("current")


class _GePmHist15minIndex_Type(Integer32):
    """Custom type gePmHist15minIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GePmHist15minIndex_Type.__name__ = "Integer32"
_GePmHist15minIndex_Object = MibTableColumn
gePmHist15minIndex = _GePmHist15minIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 1),
    _GePmHist15minIndex_Type()
)
gePmHist15minIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minIndex.setStatus("current")
_GePmHist15minElapsed_Type = Integer32
_GePmHist15minElapsed_Object = MibTableColumn
gePmHist15minElapsed = _GePmHist15minElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 2),
    _GePmHist15minElapsed_Type()
)
gePmHist15minElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minElapsed.setStatus("current")
_GePmHist15minTxOctets_Type = Counter64
_GePmHist15minTxOctets_Object = MibTableColumn
gePmHist15minTxOctets = _GePmHist15minTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 3),
    _GePmHist15minTxOctets_Type()
)
gePmHist15minTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minTxOctets.setStatus("current")
_GePmHist15minTxPkts_Type = Counter64
_GePmHist15minTxPkts_Object = MibTableColumn
gePmHist15minTxPkts = _GePmHist15minTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 4),
    _GePmHist15minTxPkts_Type()
)
gePmHist15minTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minTxPkts.setStatus("current")
_GePmHist15minTxBroadcastPkts_Type = Counter64
_GePmHist15minTxBroadcastPkts_Object = MibTableColumn
gePmHist15minTxBroadcastPkts = _GePmHist15minTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 5),
    _GePmHist15minTxBroadcastPkts_Type()
)
gePmHist15minTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minTxBroadcastPkts.setStatus("current")
_GePmHist15minTxMulticastPkts_Type = Counter64
_GePmHist15minTxMulticastPkts_Object = MibTableColumn
gePmHist15minTxMulticastPkts = _GePmHist15minTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 6),
    _GePmHist15minTxMulticastPkts_Type()
)
gePmHist15minTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minTxMulticastPkts.setStatus("current")
_GePmHist15minRxOctets_Type = Counter64
_GePmHist15minRxOctets_Object = MibTableColumn
gePmHist15minRxOctets = _GePmHist15minRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 7),
    _GePmHist15minRxOctets_Type()
)
gePmHist15minRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxOctets.setStatus("current")
_GePmHist15minRxPkts_Type = Counter64
_GePmHist15minRxPkts_Object = MibTableColumn
gePmHist15minRxPkts = _GePmHist15minRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 8),
    _GePmHist15minRxPkts_Type()
)
gePmHist15minRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxPkts.setStatus("current")
_GePmHist15minRxBroadcastPkts_Type = Counter64
_GePmHist15minRxBroadcastPkts_Object = MibTableColumn
gePmHist15minRxBroadcastPkts = _GePmHist15minRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 9),
    _GePmHist15minRxBroadcastPkts_Type()
)
gePmHist15minRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxBroadcastPkts.setStatus("current")
_GePmHist15minRxMulticastPkts_Type = Counter64
_GePmHist15minRxMulticastPkts_Object = MibTableColumn
gePmHist15minRxMulticastPkts = _GePmHist15minRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 10),
    _GePmHist15minRxMulticastPkts_Type()
)
gePmHist15minRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxMulticastPkts.setStatus("current")
_GePmHist15minRxCRCAlignErrors_Type = Counter64
_GePmHist15minRxCRCAlignErrors_Object = MibTableColumn
gePmHist15minRxCRCAlignErrors = _GePmHist15minRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 11),
    _GePmHist15minRxCRCAlignErrors_Type()
)
gePmHist15minRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxCRCAlignErrors.setStatus("current")
_GePmHist15minRxUndersizePkts_Type = Counter64
_GePmHist15minRxUndersizePkts_Object = MibTableColumn
gePmHist15minRxUndersizePkts = _GePmHist15minRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 12),
    _GePmHist15minRxUndersizePkts_Type()
)
gePmHist15minRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxUndersizePkts.setStatus("current")
_GePmHist15minRxOversizePkts_Type = Counter64
_GePmHist15minRxOversizePkts_Object = MibTableColumn
gePmHist15minRxOversizePkts = _GePmHist15minRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 13),
    _GePmHist15minRxOversizePkts_Type()
)
gePmHist15minRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxOversizePkts.setStatus("current")
_GePmHist15minRxFragments_Type = Counter64
_GePmHist15minRxFragments_Object = MibTableColumn
gePmHist15minRxFragments = _GePmHist15minRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 14),
    _GePmHist15minRxFragments_Type()
)
gePmHist15minRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minRxFragments.setStatus("current")
_GePmHist15minCollisions_Type = Counter64
_GePmHist15minCollisions_Object = MibTableColumn
gePmHist15minCollisions = _GePmHist15minCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 15),
    _GePmHist15minCollisions_Type()
)
gePmHist15minCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minCollisions.setStatus("current")
_GePmHist15minPkts64Octets_Type = Counter64
_GePmHist15minPkts64Octets_Object = MibTableColumn
gePmHist15minPkts64Octets = _GePmHist15minPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 16),
    _GePmHist15minPkts64Octets_Type()
)
gePmHist15minPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts64Octets.setStatus("current")
_GePmHist15minPkts65to127Octets_Type = Counter64
_GePmHist15minPkts65to127Octets_Object = MibTableColumn
gePmHist15minPkts65to127Octets = _GePmHist15minPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 17),
    _GePmHist15minPkts65to127Octets_Type()
)
gePmHist15minPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts65to127Octets.setStatus("current")
_GePmHist15minPkts128to255Octets_Type = Counter64
_GePmHist15minPkts128to255Octets_Object = MibTableColumn
gePmHist15minPkts128to255Octets = _GePmHist15minPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 18),
    _GePmHist15minPkts128to255Octets_Type()
)
gePmHist15minPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts128to255Octets.setStatus("current")
_GePmHist15minPkts256to511Octets_Type = Counter64
_GePmHist15minPkts256to511Octets_Object = MibTableColumn
gePmHist15minPkts256to511Octets = _GePmHist15minPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 19),
    _GePmHist15minPkts256to511Octets_Type()
)
gePmHist15minPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts256to511Octets.setStatus("current")
_GePmHist15minPkts512to1023Octets_Type = Counter64
_GePmHist15minPkts512to1023Octets_Object = MibTableColumn
gePmHist15minPkts512to1023Octets = _GePmHist15minPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 20),
    _GePmHist15minPkts512to1023Octets_Type()
)
gePmHist15minPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts512to1023Octets.setStatus("current")
_GePmHist15minPkts1024to1518Octets_Type = Counter64
_GePmHist15minPkts1024to1518Octets_Object = MibTableColumn
gePmHist15minPkts1024to1518Octets = _GePmHist15minPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 21),
    _GePmHist15minPkts1024to1518Octets_Type()
)
gePmHist15minPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts1024to1518Octets.setStatus("current")
_GePmHist15minPkts1519to1522Octets_Type = Counter64
_GePmHist15minPkts1519to1522Octets_Object = MibTableColumn
gePmHist15minPkts1519to1522Octets = _GePmHist15minPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 22),
    _GePmHist15minPkts1519to1522Octets_Type()
)
gePmHist15minPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minPkts1519to1522Octets.setStatus("current")
_GePmHist15minStartTime_Type = DisplayString
_GePmHist15minStartTime_Object = MibTableColumn
gePmHist15minStartTime = _GePmHist15minStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 23),
    _GePmHist15minStartTime_Type()
)
gePmHist15minStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minStartTime.setStatus("current")
_GePmHist15minEndTime_Type = DisplayString
_GePmHist15minEndTime_Object = MibTableColumn
gePmHist15minEndTime = _GePmHist15minEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 2, 1, 24),
    _GePmHist15minEndTime_Type()
)
gePmHist15minEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist15minEndTime.setStatus("current")
_GePmCurr1dayTable_Object = MibTable
gePmCurr1dayTable = _GePmCurr1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3)
)
if mibBuilder.loadTexts:
    gePmCurr1dayTable.setStatus("current")
_GePmCurr1dayEntry_Object = MibTableRow
gePmCurr1dayEntry = _GePmCurr1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1)
)
gePmCurr1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gePmCurr1dayEntry.setStatus("current")
_GePmCurr1dayElapsed_Type = Integer32
_GePmCurr1dayElapsed_Object = MibTableColumn
gePmCurr1dayElapsed = _GePmCurr1dayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 1),
    _GePmCurr1dayElapsed_Type()
)
gePmCurr1dayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayElapsed.setStatus("current")
_GePmCurr1dayTxOctets_Type = Counter64
_GePmCurr1dayTxOctets_Object = MibTableColumn
gePmCurr1dayTxOctets = _GePmCurr1dayTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 2),
    _GePmCurr1dayTxOctets_Type()
)
gePmCurr1dayTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayTxOctets.setStatus("current")
_GePmCurr1dayTxPkts_Type = Counter64
_GePmCurr1dayTxPkts_Object = MibTableColumn
gePmCurr1dayTxPkts = _GePmCurr1dayTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 3),
    _GePmCurr1dayTxPkts_Type()
)
gePmCurr1dayTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayTxPkts.setStatus("current")
_GePmCurr1dayTxBroadcastPkts_Type = Counter64
_GePmCurr1dayTxBroadcastPkts_Object = MibTableColumn
gePmCurr1dayTxBroadcastPkts = _GePmCurr1dayTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 4),
    _GePmCurr1dayTxBroadcastPkts_Type()
)
gePmCurr1dayTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayTxBroadcastPkts.setStatus("current")
_GePmCurr1dayTxMulticastPkts_Type = Counter64
_GePmCurr1dayTxMulticastPkts_Object = MibTableColumn
gePmCurr1dayTxMulticastPkts = _GePmCurr1dayTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 5),
    _GePmCurr1dayTxMulticastPkts_Type()
)
gePmCurr1dayTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayTxMulticastPkts.setStatus("current")
_GePmCurr1dayRxOctets_Type = Counter64
_GePmCurr1dayRxOctets_Object = MibTableColumn
gePmCurr1dayRxOctets = _GePmCurr1dayRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 6),
    _GePmCurr1dayRxOctets_Type()
)
gePmCurr1dayRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxOctets.setStatus("current")
_GePmCurr1dayRxPkts_Type = Counter64
_GePmCurr1dayRxPkts_Object = MibTableColumn
gePmCurr1dayRxPkts = _GePmCurr1dayRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 7),
    _GePmCurr1dayRxPkts_Type()
)
gePmCurr1dayRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxPkts.setStatus("current")
_GePmCurr1dayRxBroadcastPkts_Type = Counter64
_GePmCurr1dayRxBroadcastPkts_Object = MibTableColumn
gePmCurr1dayRxBroadcastPkts = _GePmCurr1dayRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 8),
    _GePmCurr1dayRxBroadcastPkts_Type()
)
gePmCurr1dayRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxBroadcastPkts.setStatus("current")
_GePmCurr1dayRxMulticastPkts_Type = Counter64
_GePmCurr1dayRxMulticastPkts_Object = MibTableColumn
gePmCurr1dayRxMulticastPkts = _GePmCurr1dayRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 9),
    _GePmCurr1dayRxMulticastPkts_Type()
)
gePmCurr1dayRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxMulticastPkts.setStatus("current")
_GePmCurr1dayRxCRCAlignErrors_Type = Counter64
_GePmCurr1dayRxCRCAlignErrors_Object = MibTableColumn
gePmCurr1dayRxCRCAlignErrors = _GePmCurr1dayRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 10),
    _GePmCurr1dayRxCRCAlignErrors_Type()
)
gePmCurr1dayRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxCRCAlignErrors.setStatus("current")
_GePmCurr1dayRxUndersizePkts_Type = Counter64
_GePmCurr1dayRxUndersizePkts_Object = MibTableColumn
gePmCurr1dayRxUndersizePkts = _GePmCurr1dayRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 11),
    _GePmCurr1dayRxUndersizePkts_Type()
)
gePmCurr1dayRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxUndersizePkts.setStatus("current")
_GePmCurr1dayRxOversizePkts_Type = Counter64
_GePmCurr1dayRxOversizePkts_Object = MibTableColumn
gePmCurr1dayRxOversizePkts = _GePmCurr1dayRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 12),
    _GePmCurr1dayRxOversizePkts_Type()
)
gePmCurr1dayRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxOversizePkts.setStatus("current")
_GePmCurr1dayRxFragments_Type = Counter64
_GePmCurr1dayRxFragments_Object = MibTableColumn
gePmCurr1dayRxFragments = _GePmCurr1dayRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 13),
    _GePmCurr1dayRxFragments_Type()
)
gePmCurr1dayRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayRxFragments.setStatus("current")
_GePmCurr1dayCollisions_Type = Counter64
_GePmCurr1dayCollisions_Object = MibTableColumn
gePmCurr1dayCollisions = _GePmCurr1dayCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 14),
    _GePmCurr1dayCollisions_Type()
)
gePmCurr1dayCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayCollisions.setStatus("current")
_GePmCurr1dayPkts64Octets_Type = Counter64
_GePmCurr1dayPkts64Octets_Object = MibTableColumn
gePmCurr1dayPkts64Octets = _GePmCurr1dayPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 15),
    _GePmCurr1dayPkts64Octets_Type()
)
gePmCurr1dayPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts64Octets.setStatus("current")
_GePmCurr1dayPkts65to127Octets_Type = Counter64
_GePmCurr1dayPkts65to127Octets_Object = MibTableColumn
gePmCurr1dayPkts65to127Octets = _GePmCurr1dayPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 16),
    _GePmCurr1dayPkts65to127Octets_Type()
)
gePmCurr1dayPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts65to127Octets.setStatus("current")
_GePmCurr1dayPkts128to255Octets_Type = Counter64
_GePmCurr1dayPkts128to255Octets_Object = MibTableColumn
gePmCurr1dayPkts128to255Octets = _GePmCurr1dayPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 17),
    _GePmCurr1dayPkts128to255Octets_Type()
)
gePmCurr1dayPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts128to255Octets.setStatus("current")
_GePmCurr1dayPkts256to511Octets_Type = Counter64
_GePmCurr1dayPkts256to511Octets_Object = MibTableColumn
gePmCurr1dayPkts256to511Octets = _GePmCurr1dayPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 18),
    _GePmCurr1dayPkts256to511Octets_Type()
)
gePmCurr1dayPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts256to511Octets.setStatus("current")
_GePmCurr1dayPkts512to1023Octets_Type = Counter64
_GePmCurr1dayPkts512to1023Octets_Object = MibTableColumn
gePmCurr1dayPkts512to1023Octets = _GePmCurr1dayPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 19),
    _GePmCurr1dayPkts512to1023Octets_Type()
)
gePmCurr1dayPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts512to1023Octets.setStatus("current")
_GePmCurr1dayPkts1024to1518Octets_Type = Counter64
_GePmCurr1dayPkts1024to1518Octets_Object = MibTableColumn
gePmCurr1dayPkts1024to1518Octets = _GePmCurr1dayPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 20),
    _GePmCurr1dayPkts1024to1518Octets_Type()
)
gePmCurr1dayPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts1024to1518Octets.setStatus("current")
_GePmCurr1dayPkts1519to1522Octets_Type = Counter64
_GePmCurr1dayPkts1519to1522Octets_Object = MibTableColumn
gePmCurr1dayPkts1519to1522Octets = _GePmCurr1dayPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 3, 1, 21),
    _GePmCurr1dayPkts1519to1522Octets_Type()
)
gePmCurr1dayPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurr1dayPkts1519to1522Octets.setStatus("current")
_GePmHist1dayTable_Object = MibTable
gePmHist1dayTable = _GePmHist1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4)
)
if mibBuilder.loadTexts:
    gePmHist1dayTable.setStatus("current")
_GePmHist1dayEntry_Object = MibTableRow
gePmHist1dayEntry = _GePmHist1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1)
)
gePmHist1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "gePmHist1dayIndex"),
)
if mibBuilder.loadTexts:
    gePmHist1dayEntry.setStatus("current")


class _GePmHist1dayIndex_Type(Integer32):
    """Custom type gePmHist1dayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GePmHist1dayIndex_Type.__name__ = "Integer32"
_GePmHist1dayIndex_Object = MibTableColumn
gePmHist1dayIndex = _GePmHist1dayIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 1),
    _GePmHist1dayIndex_Type()
)
gePmHist1dayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayIndex.setStatus("current")
_GePmHist1dayStartTime_Type = DisplayString
_GePmHist1dayStartTime_Object = MibTableColumn
gePmHist1dayStartTime = _GePmHist1dayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 2),
    _GePmHist1dayStartTime_Type()
)
gePmHist1dayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayStartTime.setStatus("current")
_GePmHist1dayEndTime_Type = DisplayString
_GePmHist1dayEndTime_Object = MibTableColumn
gePmHist1dayEndTime = _GePmHist1dayEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 3),
    _GePmHist1dayEndTime_Type()
)
gePmHist1dayEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayEndTime.setStatus("current")
_GePmHist1dayTxOctets_Type = Counter64
_GePmHist1dayTxOctets_Object = MibTableColumn
gePmHist1dayTxOctets = _GePmHist1dayTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 4),
    _GePmHist1dayTxOctets_Type()
)
gePmHist1dayTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayTxOctets.setStatus("current")
_GePmHist1dayTxPkts_Type = Counter64
_GePmHist1dayTxPkts_Object = MibTableColumn
gePmHist1dayTxPkts = _GePmHist1dayTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 5),
    _GePmHist1dayTxPkts_Type()
)
gePmHist1dayTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayTxPkts.setStatus("current")
_GePmHist1dayTxBroadcastPkts_Type = Counter64
_GePmHist1dayTxBroadcastPkts_Object = MibTableColumn
gePmHist1dayTxBroadcastPkts = _GePmHist1dayTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 6),
    _GePmHist1dayTxBroadcastPkts_Type()
)
gePmHist1dayTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayTxBroadcastPkts.setStatus("current")
_GePmHist1dayTxMulticastPkts_Type = Counter64
_GePmHist1dayTxMulticastPkts_Object = MibTableColumn
gePmHist1dayTxMulticastPkts = _GePmHist1dayTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 7),
    _GePmHist1dayTxMulticastPkts_Type()
)
gePmHist1dayTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayTxMulticastPkts.setStatus("current")
_GePmHist1dayRxOctets_Type = Counter64
_GePmHist1dayRxOctets_Object = MibTableColumn
gePmHist1dayRxOctets = _GePmHist1dayRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 8),
    _GePmHist1dayRxOctets_Type()
)
gePmHist1dayRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxOctets.setStatus("current")
_GePmHist1dayRxPkts_Type = Counter64
_GePmHist1dayRxPkts_Object = MibTableColumn
gePmHist1dayRxPkts = _GePmHist1dayRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 9),
    _GePmHist1dayRxPkts_Type()
)
gePmHist1dayRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxPkts.setStatus("current")
_GePmHist1dayRxBroadcastPkts_Type = Counter64
_GePmHist1dayRxBroadcastPkts_Object = MibTableColumn
gePmHist1dayRxBroadcastPkts = _GePmHist1dayRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 10),
    _GePmHist1dayRxBroadcastPkts_Type()
)
gePmHist1dayRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxBroadcastPkts.setStatus("current")
_GePmHist1dayRxMulticastPkts_Type = Counter64
_GePmHist1dayRxMulticastPkts_Object = MibTableColumn
gePmHist1dayRxMulticastPkts = _GePmHist1dayRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 11),
    _GePmHist1dayRxMulticastPkts_Type()
)
gePmHist1dayRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxMulticastPkts.setStatus("current")
_GePmHist1dayRxCRCAlignErrors_Type = Counter64
_GePmHist1dayRxCRCAlignErrors_Object = MibTableColumn
gePmHist1dayRxCRCAlignErrors = _GePmHist1dayRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 12),
    _GePmHist1dayRxCRCAlignErrors_Type()
)
gePmHist1dayRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxCRCAlignErrors.setStatus("current")
_GePmHist1dayRxUndersizePkts_Type = Counter64
_GePmHist1dayRxUndersizePkts_Object = MibTableColumn
gePmHist1dayRxUndersizePkts = _GePmHist1dayRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 13),
    _GePmHist1dayRxUndersizePkts_Type()
)
gePmHist1dayRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxUndersizePkts.setStatus("current")
_GePmHist1dayRxOversizePkts_Type = Counter64
_GePmHist1dayRxOversizePkts_Object = MibTableColumn
gePmHist1dayRxOversizePkts = _GePmHist1dayRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 14),
    _GePmHist1dayRxOversizePkts_Type()
)
gePmHist1dayRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxOversizePkts.setStatus("current")
_GePmHist1dayRxFragments_Type = Counter64
_GePmHist1dayRxFragments_Object = MibTableColumn
gePmHist1dayRxFragments = _GePmHist1dayRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 15),
    _GePmHist1dayRxFragments_Type()
)
gePmHist1dayRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayRxFragments.setStatus("current")
_GePmHist1dayCollisions_Type = Counter64
_GePmHist1dayCollisions_Object = MibTableColumn
gePmHist1dayCollisions = _GePmHist1dayCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 16),
    _GePmHist1dayCollisions_Type()
)
gePmHist1dayCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayCollisions.setStatus("current")
_GePmHist1dayPkts64Octets_Type = Counter64
_GePmHist1dayPkts64Octets_Object = MibTableColumn
gePmHist1dayPkts64Octets = _GePmHist1dayPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 17),
    _GePmHist1dayPkts64Octets_Type()
)
gePmHist1dayPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts64Octets.setStatus("current")
_GePmHist1dayPkts65to127Octets_Type = Counter64
_GePmHist1dayPkts65to127Octets_Object = MibTableColumn
gePmHist1dayPkts65to127Octets = _GePmHist1dayPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 18),
    _GePmHist1dayPkts65to127Octets_Type()
)
gePmHist1dayPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts65to127Octets.setStatus("current")
_GePmHist1dayPkts128to255Octets_Type = Counter64
_GePmHist1dayPkts128to255Octets_Object = MibTableColumn
gePmHist1dayPkts128to255Octets = _GePmHist1dayPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 19),
    _GePmHist1dayPkts128to255Octets_Type()
)
gePmHist1dayPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts128to255Octets.setStatus("current")
_GePmHist1dayPkts256to511Octets_Type = Counter64
_GePmHist1dayPkts256to511Octets_Object = MibTableColumn
gePmHist1dayPkts256to511Octets = _GePmHist1dayPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 20),
    _GePmHist1dayPkts256to511Octets_Type()
)
gePmHist1dayPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts256to511Octets.setStatus("current")
_GePmHist1dayPkts512to1023Octets_Type = Counter64
_GePmHist1dayPkts512to1023Octets_Object = MibTableColumn
gePmHist1dayPkts512to1023Octets = _GePmHist1dayPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 21),
    _GePmHist1dayPkts512to1023Octets_Type()
)
gePmHist1dayPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts512to1023Octets.setStatus("current")
_GePmHist1dayPkts1024to1518Octets_Type = Counter64
_GePmHist1dayPkts1024to1518Octets_Object = MibTableColumn
gePmHist1dayPkts1024to1518Octets = _GePmHist1dayPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 22),
    _GePmHist1dayPkts1024to1518Octets_Type()
)
gePmHist1dayPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts1024to1518Octets.setStatus("current")
_GePmHist1dayPkts1519to1522Octets_Type = Counter64
_GePmHist1dayPkts1519to1522Octets_Object = MibTableColumn
gePmHist1dayPkts1519to1522Octets = _GePmHist1dayPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 4, 1, 23),
    _GePmHist1dayPkts1519to1522Octets_Type()
)
gePmHist1dayPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmHist1dayPkts1519to1522Octets.setStatus("current")
_GePmThreshProfTable_Object = MibTable
gePmThreshProfTable = _GePmThreshProfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5)
)
if mibBuilder.loadTexts:
    gePmThreshProfTable.setStatus("current")
_GePmThreshProfEntry_Object = MibTableRow
gePmThreshProfEntry = _GePmThreshProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1)
)
gePmThreshProfEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "gePmThreshProfName"),
)
if mibBuilder.loadTexts:
    gePmThreshProfEntry.setStatus("current")
_GePmThreshProfName_Type = DisplayString
_GePmThreshProfName_Object = MibTableColumn
gePmThreshProfName = _GePmThreshProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 1),
    _GePmThreshProfName_Type()
)
gePmThreshProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmThreshProfName.setStatus("current")


class _GePmThreshProfTxOctets_Type(DisplayString):
    """Custom type gePmThreshProfTxOctets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfTxOctets_Type.__name__ = "DisplayString"
_GePmThreshProfTxOctets_Object = MibTableColumn
gePmThreshProfTxOctets = _GePmThreshProfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 2),
    _GePmThreshProfTxOctets_Type()
)
gePmThreshProfTxOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfTxOctets.setStatus("current")


class _GePmThreshProfTxPkts_Type(DisplayString):
    """Custom type gePmThreshProfTxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfTxPkts_Type.__name__ = "DisplayString"
_GePmThreshProfTxPkts_Object = MibTableColumn
gePmThreshProfTxPkts = _GePmThreshProfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 3),
    _GePmThreshProfTxPkts_Type()
)
gePmThreshProfTxPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfTxPkts.setStatus("current")


class _GePmThreshProfTxBroadcastPkts_Type(DisplayString):
    """Custom type gePmThreshProfTxBroadcastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfTxBroadcastPkts_Type.__name__ = "DisplayString"
_GePmThreshProfTxBroadcastPkts_Object = MibTableColumn
gePmThreshProfTxBroadcastPkts = _GePmThreshProfTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 4),
    _GePmThreshProfTxBroadcastPkts_Type()
)
gePmThreshProfTxBroadcastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfTxBroadcastPkts.setStatus("current")


class _GePmThreshProfTxMulticastPkts_Type(DisplayString):
    """Custom type gePmThreshProfTxMulticastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfTxMulticastPkts_Type.__name__ = "DisplayString"
_GePmThreshProfTxMulticastPkts_Object = MibTableColumn
gePmThreshProfTxMulticastPkts = _GePmThreshProfTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 5),
    _GePmThreshProfTxMulticastPkts_Type()
)
gePmThreshProfTxMulticastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfTxMulticastPkts.setStatus("current")


class _GePmThreshProfRxOctets_Type(DisplayString):
    """Custom type gePmThreshProfRxOctets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxOctets_Type.__name__ = "DisplayString"
_GePmThreshProfRxOctets_Object = MibTableColumn
gePmThreshProfRxOctets = _GePmThreshProfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 6),
    _GePmThreshProfRxOctets_Type()
)
gePmThreshProfRxOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxOctets.setStatus("current")


class _GePmThreshProfRxPkts_Type(DisplayString):
    """Custom type gePmThreshProfRxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxPkts_Type.__name__ = "DisplayString"
_GePmThreshProfRxPkts_Object = MibTableColumn
gePmThreshProfRxPkts = _GePmThreshProfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 7),
    _GePmThreshProfRxPkts_Type()
)
gePmThreshProfRxPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxPkts.setStatus("current")


class _GePmThreshProfRxBroadcastPkts_Type(DisplayString):
    """Custom type gePmThreshProfRxBroadcastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxBroadcastPkts_Type.__name__ = "DisplayString"
_GePmThreshProfRxBroadcastPkts_Object = MibTableColumn
gePmThreshProfRxBroadcastPkts = _GePmThreshProfRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 8),
    _GePmThreshProfRxBroadcastPkts_Type()
)
gePmThreshProfRxBroadcastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxBroadcastPkts.setStatus("current")


class _GePmThreshProfRxMulticastPkts_Type(DisplayString):
    """Custom type gePmThreshProfRxMulticastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxMulticastPkts_Type.__name__ = "DisplayString"
_GePmThreshProfRxMulticastPkts_Object = MibTableColumn
gePmThreshProfRxMulticastPkts = _GePmThreshProfRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 9),
    _GePmThreshProfRxMulticastPkts_Type()
)
gePmThreshProfRxMulticastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxMulticastPkts.setStatus("current")


class _GePmThreshProfRxCRCAlignErrors_Type(DisplayString):
    """Custom type gePmThreshProfRxCRCAlignErrors based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxCRCAlignErrors_Type.__name__ = "DisplayString"
_GePmThreshProfRxCRCAlignErrors_Object = MibTableColumn
gePmThreshProfRxCRCAlignErrors = _GePmThreshProfRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 10),
    _GePmThreshProfRxCRCAlignErrors_Type()
)
gePmThreshProfRxCRCAlignErrors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxCRCAlignErrors.setStatus("current")


class _GePmThreshProfRxUndersizePkts_Type(DisplayString):
    """Custom type gePmThreshProfRxUndersizePkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxUndersizePkts_Type.__name__ = "DisplayString"
_GePmThreshProfRxUndersizePkts_Object = MibTableColumn
gePmThreshProfRxUndersizePkts = _GePmThreshProfRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 11),
    _GePmThreshProfRxUndersizePkts_Type()
)
gePmThreshProfRxUndersizePkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxUndersizePkts.setStatus("current")


class _GePmThreshProfRxOversizePkts_Type(DisplayString):
    """Custom type gePmThreshProfRxOversizePkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxOversizePkts_Type.__name__ = "DisplayString"
_GePmThreshProfRxOversizePkts_Object = MibTableColumn
gePmThreshProfRxOversizePkts = _GePmThreshProfRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 12),
    _GePmThreshProfRxOversizePkts_Type()
)
gePmThreshProfRxOversizePkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxOversizePkts.setStatus("current")


class _GePmThreshProfRxFragments_Type(DisplayString):
    """Custom type gePmThreshProfRxFragments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfRxFragments_Type.__name__ = "DisplayString"
_GePmThreshProfRxFragments_Object = MibTableColumn
gePmThreshProfRxFragments = _GePmThreshProfRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 13),
    _GePmThreshProfRxFragments_Type()
)
gePmThreshProfRxFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRxFragments.setStatus("current")


class _GePmThreshProfCollisions_Type(DisplayString):
    """Custom type gePmThreshProfCollisions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfCollisions_Type.__name__ = "DisplayString"
_GePmThreshProfCollisions_Object = MibTableColumn
gePmThreshProfCollisions = _GePmThreshProfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 14),
    _GePmThreshProfCollisions_Type()
)
gePmThreshProfCollisions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfCollisions.setStatus("current")


class _GePmThreshProfPkts64Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts64Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts64Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts64Octets_Object = MibTableColumn
gePmThreshProfPkts64Octets = _GePmThreshProfPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 15),
    _GePmThreshProfPkts64Octets_Type()
)
gePmThreshProfPkts64Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts64Octets.setStatus("current")


class _GePmThreshProfPkts65to127Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts65to127Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts65to127Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts65to127Octets_Object = MibTableColumn
gePmThreshProfPkts65to127Octets = _GePmThreshProfPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 16),
    _GePmThreshProfPkts65to127Octets_Type()
)
gePmThreshProfPkts65to127Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts65to127Octets.setStatus("current")


class _GePmThreshProfPkts128to255Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts128to255Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts128to255Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts128to255Octets_Object = MibTableColumn
gePmThreshProfPkts128to255Octets = _GePmThreshProfPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 17),
    _GePmThreshProfPkts128to255Octets_Type()
)
gePmThreshProfPkts128to255Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts128to255Octets.setStatus("current")


class _GePmThreshProfPkts256to511Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts256to511Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts256to511Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts256to511Octets_Object = MibTableColumn
gePmThreshProfPkts256to511Octets = _GePmThreshProfPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 18),
    _GePmThreshProfPkts256to511Octets_Type()
)
gePmThreshProfPkts256to511Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts256to511Octets.setStatus("current")


class _GePmThreshProfPkts512to1023Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts512to1023Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts512to1023Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts512to1023Octets_Object = MibTableColumn
gePmThreshProfPkts512to1023Octets = _GePmThreshProfPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 19),
    _GePmThreshProfPkts512to1023Octets_Type()
)
gePmThreshProfPkts512to1023Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts512to1023Octets.setStatus("current")


class _GePmThreshProfPkts1024to1518Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts1024to1518Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts1024to1518Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts1024to1518Octets_Object = MibTableColumn
gePmThreshProfPkts1024to1518Octets = _GePmThreshProfPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 20),
    _GePmThreshProfPkts1024to1518Octets_Type()
)
gePmThreshProfPkts1024to1518Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts1024to1518Octets.setStatus("current")


class _GePmThreshProfPkts1519to1522Octets_Type(DisplayString):
    """Custom type gePmThreshProfPkts1519to1522Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GePmThreshProfPkts1519to1522Octets_Type.__name__ = "DisplayString"
_GePmThreshProfPkts1519to1522Octets_Object = MibTableColumn
gePmThreshProfPkts1519to1522Octets = _GePmThreshProfPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 21),
    _GePmThreshProfPkts1519to1522Octets_Type()
)
gePmThreshProfPkts1519to1522Octets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfPkts1519to1522Octets.setStatus("current")
_GePmThreshProfRowStatus_Type = RowStatus
_GePmThreshProfRowStatus_Object = MibTableColumn
gePmThreshProfRowStatus = _GePmThreshProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 5, 1, 22),
    _GePmThreshProfRowStatus_Type()
)
gePmThreshProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gePmThreshProfRowStatus.setStatus("current")
_FxsPmCurr15minTable_Object = MibTable
fxsPmCurr15minTable = _FxsPmCurr15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11)
)
if mibBuilder.loadTexts:
    fxsPmCurr15minTable.setStatus("current")
_FxsPmCurr15minEntry_Object = MibTableRow
fxsPmCurr15minEntry = _FxsPmCurr15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1)
)
fxsPmCurr15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxsPmCurr15minEntry.setStatus("current")
_FxsPmCurr15minElapsed_Type = Integer32
_FxsPmCurr15minElapsed_Object = MibTableColumn
fxsPmCurr15minElapsed = _FxsPmCurr15minElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 1),
    _FxsPmCurr15minElapsed_Type()
)
fxsPmCurr15minElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minElapsed.setStatus("current")
_FxsPmCurr15minRtpElapsedTime_Type = Integer32
_FxsPmCurr15minRtpElapsedTime_Object = MibTableColumn
fxsPmCurr15minRtpElapsedTime = _FxsPmCurr15minRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 2),
    _FxsPmCurr15minRtpElapsedTime_Type()
)
fxsPmCurr15minRtpElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpElapsedTime.setStatus("current")
_FxsPmCurr15minRtpTxBytes_Type = Counter64
_FxsPmCurr15minRtpTxBytes_Object = MibTableColumn
fxsPmCurr15minRtpTxBytes = _FxsPmCurr15minRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 3),
    _FxsPmCurr15minRtpTxBytes_Type()
)
fxsPmCurr15minRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpTxBytes.setStatus("current")
_FxsPmCurr15minRtpRxBytes_Type = Counter64
_FxsPmCurr15minRtpRxBytes_Object = MibTableColumn
fxsPmCurr15minRtpRxBytes = _FxsPmCurr15minRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 4),
    _FxsPmCurr15minRtpRxBytes_Type()
)
fxsPmCurr15minRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpRxBytes.setStatus("current")
_FxsPmCurr15minRtpTxPackets_Type = Counter64
_FxsPmCurr15minRtpTxPackets_Object = MibTableColumn
fxsPmCurr15minRtpTxPackets = _FxsPmCurr15minRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 5),
    _FxsPmCurr15minRtpTxPackets_Type()
)
fxsPmCurr15minRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpTxPackets.setStatus("current")
_FxsPmCurr15minRtpRxPackets_Type = Counter64
_FxsPmCurr15minRtpRxPackets_Object = MibTableColumn
fxsPmCurr15minRtpRxPackets = _FxsPmCurr15minRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 6),
    _FxsPmCurr15minRtpRxPackets_Type()
)
fxsPmCurr15minRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpRxPackets.setStatus("current")
_FxsPmCurr15minRtpTxLostPackets_Type = Counter64
_FxsPmCurr15minRtpTxLostPackets_Object = MibTableColumn
fxsPmCurr15minRtpTxLostPackets = _FxsPmCurr15minRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 7),
    _FxsPmCurr15minRtpTxLostPackets_Type()
)
fxsPmCurr15minRtpTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpTxLostPackets.setStatus("current")
_FxsPmCurr15minRtpRxLostPackets_Type = Counter64
_FxsPmCurr15minRtpRxLostPackets_Object = MibTableColumn
fxsPmCurr15minRtpRxLostPackets = _FxsPmCurr15minRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 11, 1, 8),
    _FxsPmCurr15minRtpRxLostPackets_Type()
)
fxsPmCurr15minRtpRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr15minRtpRxLostPackets.setStatus("current")
_FxsPmHist15minTable_Object = MibTable
fxsPmHist15minTable = _FxsPmHist15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12)
)
if mibBuilder.loadTexts:
    fxsPmHist15minTable.setStatus("current")
_FxsPmHist15minEntry_Object = MibTableRow
fxsPmHist15minEntry = _FxsPmHist15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1)
)
fxsPmHist15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "fxsPmHist15minIndex"),
)
if mibBuilder.loadTexts:
    fxsPmHist15minEntry.setStatus("current")


class _FxsPmHist15minIndex_Type(Integer32):
    """Custom type fxsPmHist15minIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FxsPmHist15minIndex_Type.__name__ = "Integer32"
_FxsPmHist15minIndex_Object = MibTableColumn
fxsPmHist15minIndex = _FxsPmHist15minIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 1),
    _FxsPmHist15minIndex_Type()
)
fxsPmHist15minIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minIndex.setStatus("current")
_FxsPmHist15minStartTime_Type = DisplayString
_FxsPmHist15minStartTime_Object = MibTableColumn
fxsPmHist15minStartTime = _FxsPmHist15minStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 2),
    _FxsPmHist15minStartTime_Type()
)
fxsPmHist15minStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minStartTime.setStatus("current")
_FxsPmHist15minEndTime_Type = DisplayString
_FxsPmHist15minEndTime_Object = MibTableColumn
fxsPmHist15minEndTime = _FxsPmHist15minEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 3),
    _FxsPmHist15minEndTime_Type()
)
fxsPmHist15minEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minEndTime.setStatus("current")
_FxsPmHist15minRtpElapsedTime_Type = Integer32
_FxsPmHist15minRtpElapsedTime_Object = MibTableColumn
fxsPmHist15minRtpElapsedTime = _FxsPmHist15minRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 4),
    _FxsPmHist15minRtpElapsedTime_Type()
)
fxsPmHist15minRtpElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpElapsedTime.setStatus("current")
_FxsPmHist15minRtpTxBytes_Type = Counter64
_FxsPmHist15minRtpTxBytes_Object = MibTableColumn
fxsPmHist15minRtpTxBytes = _FxsPmHist15minRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 5),
    _FxsPmHist15minRtpTxBytes_Type()
)
fxsPmHist15minRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpTxBytes.setStatus("current")
_FxsPmHist15minRtpRxBytes_Type = Counter64
_FxsPmHist15minRtpRxBytes_Object = MibTableColumn
fxsPmHist15minRtpRxBytes = _FxsPmHist15minRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 6),
    _FxsPmHist15minRtpRxBytes_Type()
)
fxsPmHist15minRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpRxBytes.setStatus("current")
_FxsPmHist15minRtpTxPackets_Type = Counter64
_FxsPmHist15minRtpTxPackets_Object = MibTableColumn
fxsPmHist15minRtpTxPackets = _FxsPmHist15minRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 7),
    _FxsPmHist15minRtpTxPackets_Type()
)
fxsPmHist15minRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpTxPackets.setStatus("current")
_FxsPmHist15minRtpRxPackets_Type = Counter64
_FxsPmHist15minRtpRxPackets_Object = MibTableColumn
fxsPmHist15minRtpRxPackets = _FxsPmHist15minRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 8),
    _FxsPmHist15minRtpRxPackets_Type()
)
fxsPmHist15minRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpRxPackets.setStatus("current")
_FxsPmHist15minRtpTxLostPackets_Type = Counter64
_FxsPmHist15minRtpTxLostPackets_Object = MibTableColumn
fxsPmHist15minRtpTxLostPackets = _FxsPmHist15minRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 9),
    _FxsPmHist15minRtpTxLostPackets_Type()
)
fxsPmHist15minRtpTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpTxLostPackets.setStatus("current")
_FxsPmHist15minRtpRxLostPackets_Type = Counter64
_FxsPmHist15minRtpRxLostPackets_Object = MibTableColumn
fxsPmHist15minRtpRxLostPackets = _FxsPmHist15minRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 12, 1, 10),
    _FxsPmHist15minRtpRxLostPackets_Type()
)
fxsPmHist15minRtpRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist15minRtpRxLostPackets.setStatus("current")
_FxsPmCurr1dayTable_Object = MibTable
fxsPmCurr1dayTable = _FxsPmCurr1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13)
)
if mibBuilder.loadTexts:
    fxsPmCurr1dayTable.setStatus("current")
_FxsPmCurr1dayEntry_Object = MibTableRow
fxsPmCurr1dayEntry = _FxsPmCurr1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1)
)
fxsPmCurr1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxsPmCurr1dayEntry.setStatus("current")
_FxsPmCurr1dayElapsed_Type = Integer32
_FxsPmCurr1dayElapsed_Object = MibTableColumn
fxsPmCurr1dayElapsed = _FxsPmCurr1dayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 1),
    _FxsPmCurr1dayElapsed_Type()
)
fxsPmCurr1dayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayElapsed.setStatus("current")
_FxsPmCurr1dayRtpElapsedTime_Type = Integer32
_FxsPmCurr1dayRtpElapsedTime_Object = MibTableColumn
fxsPmCurr1dayRtpElapsedTime = _FxsPmCurr1dayRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 2),
    _FxsPmCurr1dayRtpElapsedTime_Type()
)
fxsPmCurr1dayRtpElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpElapsedTime.setStatus("current")
_FxsPmCurr1dayRtpTxBytes_Type = Counter64
_FxsPmCurr1dayRtpTxBytes_Object = MibTableColumn
fxsPmCurr1dayRtpTxBytes = _FxsPmCurr1dayRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 3),
    _FxsPmCurr1dayRtpTxBytes_Type()
)
fxsPmCurr1dayRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpTxBytes.setStatus("current")
_FxsPmCurr1dayRtpRxBytes_Type = Counter64
_FxsPmCurr1dayRtpRxBytes_Object = MibTableColumn
fxsPmCurr1dayRtpRxBytes = _FxsPmCurr1dayRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 4),
    _FxsPmCurr1dayRtpRxBytes_Type()
)
fxsPmCurr1dayRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpRxBytes.setStatus("current")
_FxsPmCurr1dayRtpTxPackets_Type = Counter64
_FxsPmCurr1dayRtpTxPackets_Object = MibTableColumn
fxsPmCurr1dayRtpTxPackets = _FxsPmCurr1dayRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 5),
    _FxsPmCurr1dayRtpTxPackets_Type()
)
fxsPmCurr1dayRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpTxPackets.setStatus("current")
_FxsPmCurr1dayRtpRxPackets_Type = Counter64
_FxsPmCurr1dayRtpRxPackets_Object = MibTableColumn
fxsPmCurr1dayRtpRxPackets = _FxsPmCurr1dayRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 6),
    _FxsPmCurr1dayRtpRxPackets_Type()
)
fxsPmCurr1dayRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpRxPackets.setStatus("current")
_FxsPmCurr1dayRtpTxLostPackets_Type = Counter64
_FxsPmCurr1dayRtpTxLostPackets_Object = MibTableColumn
fxsPmCurr1dayRtpTxLostPackets = _FxsPmCurr1dayRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 7),
    _FxsPmCurr1dayRtpTxLostPackets_Type()
)
fxsPmCurr1dayRtpTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpTxLostPackets.setStatus("current")
_FxsPmCurr1dayRtpRxLostPackets_Type = Counter64
_FxsPmCurr1dayRtpRxLostPackets_Object = MibTableColumn
fxsPmCurr1dayRtpRxLostPackets = _FxsPmCurr1dayRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 13, 1, 8),
    _FxsPmCurr1dayRtpRxLostPackets_Type()
)
fxsPmCurr1dayRtpRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurr1dayRtpRxLostPackets.setStatus("current")
_FxsPmHist1dayTable_Object = MibTable
fxsPmHist1dayTable = _FxsPmHist1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14)
)
if mibBuilder.loadTexts:
    fxsPmHist1dayTable.setStatus("current")
_FxsPmHist1dayEntry_Object = MibTableRow
fxsPmHist1dayEntry = _FxsPmHist1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1)
)
fxsPmHist1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "fxsPmHist1dayIndex"),
)
if mibBuilder.loadTexts:
    fxsPmHist1dayEntry.setStatus("current")


class _FxsPmHist1dayIndex_Type(Integer32):
    """Custom type fxsPmHist1dayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FxsPmHist1dayIndex_Type.__name__ = "Integer32"
_FxsPmHist1dayIndex_Object = MibTableColumn
fxsPmHist1dayIndex = _FxsPmHist1dayIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 1),
    _FxsPmHist1dayIndex_Type()
)
fxsPmHist1dayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayIndex.setStatus("current")
_FxsPmHist1dayStartTime_Type = DisplayString
_FxsPmHist1dayStartTime_Object = MibTableColumn
fxsPmHist1dayStartTime = _FxsPmHist1dayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 2),
    _FxsPmHist1dayStartTime_Type()
)
fxsPmHist1dayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayStartTime.setStatus("current")
_FxsPmHist1dayEndTime_Type = DisplayString
_FxsPmHist1dayEndTime_Object = MibTableColumn
fxsPmHist1dayEndTime = _FxsPmHist1dayEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 3),
    _FxsPmHist1dayEndTime_Type()
)
fxsPmHist1dayEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayEndTime.setStatus("current")
_FxsPmHist1dayRtpElapsedTime_Type = Integer32
_FxsPmHist1dayRtpElapsedTime_Object = MibTableColumn
fxsPmHist1dayRtpElapsedTime = _FxsPmHist1dayRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 4),
    _FxsPmHist1dayRtpElapsedTime_Type()
)
fxsPmHist1dayRtpElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpElapsedTime.setStatus("current")
_FxsPmHist1dayRtpTxBytes_Type = Counter64
_FxsPmHist1dayRtpTxBytes_Object = MibTableColumn
fxsPmHist1dayRtpTxBytes = _FxsPmHist1dayRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 5),
    _FxsPmHist1dayRtpTxBytes_Type()
)
fxsPmHist1dayRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpTxBytes.setStatus("current")
_FxsPmHist1dayRtpRxBytes_Type = Counter64
_FxsPmHist1dayRtpRxBytes_Object = MibTableColumn
fxsPmHist1dayRtpRxBytes = _FxsPmHist1dayRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 6),
    _FxsPmHist1dayRtpRxBytes_Type()
)
fxsPmHist1dayRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpRxBytes.setStatus("current")
_FxsPmHist1dayRtpTxPackets_Type = Counter64
_FxsPmHist1dayRtpTxPackets_Object = MibTableColumn
fxsPmHist1dayRtpTxPackets = _FxsPmHist1dayRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 7),
    _FxsPmHist1dayRtpTxPackets_Type()
)
fxsPmHist1dayRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpTxPackets.setStatus("current")
_FxsPmHist1dayRtpRxPackets_Type = Counter64
_FxsPmHist1dayRtpRxPackets_Object = MibTableColumn
fxsPmHist1dayRtpRxPackets = _FxsPmHist1dayRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 8),
    _FxsPmHist1dayRtpRxPackets_Type()
)
fxsPmHist1dayRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpRxPackets.setStatus("current")
_FxsPmHist1dayRtpTxLostPackets_Type = Counter64
_FxsPmHist1dayRtpTxLostPackets_Object = MibTableColumn
fxsPmHist1dayRtpTxLostPackets = _FxsPmHist1dayRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 9),
    _FxsPmHist1dayRtpTxLostPackets_Type()
)
fxsPmHist1dayRtpTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpTxLostPackets.setStatus("current")
_FxsPmHist1dayRtpRxLostPackets_Type = Counter64
_FxsPmHist1dayRtpRxLostPackets_Object = MibTableColumn
fxsPmHist1dayRtpRxLostPackets = _FxsPmHist1dayRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 14, 1, 10),
    _FxsPmHist1dayRtpRxLostPackets_Type()
)
fxsPmHist1dayRtpRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmHist1dayRtpRxLostPackets.setStatus("current")
_FxsPmThreshProfTable_Object = MibTable
fxsPmThreshProfTable = _FxsPmThreshProfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15)
)
if mibBuilder.loadTexts:
    fxsPmThreshProfTable.setStatus("current")
_FxsPmThreshProfEntry_Object = MibTableRow
fxsPmThreshProfEntry = _FxsPmThreshProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1)
)
fxsPmThreshProfEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "fxsPmThreshProfName"),
)
if mibBuilder.loadTexts:
    fxsPmThreshProfEntry.setStatus("current")
_FxsPmThreshProfName_Type = DisplayString
_FxsPmThreshProfName_Object = MibTableColumn
fxsPmThreshProfName = _FxsPmThreshProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 1),
    _FxsPmThreshProfName_Type()
)
fxsPmThreshProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmThreshProfName.setStatus("current")


class _FxsPmThreshProfRtpElapsedTime_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpElapsedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpElapsedTime_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpElapsedTime_Object = MibTableColumn
fxsPmThreshProfRtpElapsedTime = _FxsPmThreshProfRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 2),
    _FxsPmThreshProfRtpElapsedTime_Type()
)
fxsPmThreshProfRtpElapsedTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpElapsedTime.setStatus("current")


class _FxsPmThreshProfRtpTxBytes_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpTxBytes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpTxBytes_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpTxBytes_Object = MibTableColumn
fxsPmThreshProfRtpTxBytes = _FxsPmThreshProfRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 3),
    _FxsPmThreshProfRtpTxBytes_Type()
)
fxsPmThreshProfRtpTxBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpTxBytes.setStatus("current")


class _FxsPmThreshProfRtpRxBytes_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpRxBytes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpRxBytes_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpRxBytes_Object = MibTableColumn
fxsPmThreshProfRtpRxBytes = _FxsPmThreshProfRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 4),
    _FxsPmThreshProfRtpRxBytes_Type()
)
fxsPmThreshProfRtpRxBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpRxBytes.setStatus("current")


class _FxsPmThreshProfRtpTxPackets_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpTxPackets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpTxPackets_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpTxPackets_Object = MibTableColumn
fxsPmThreshProfRtpTxPackets = _FxsPmThreshProfRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 5),
    _FxsPmThreshProfRtpTxPackets_Type()
)
fxsPmThreshProfRtpTxPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpTxPackets.setStatus("current")


class _FxsPmThreshProfRtpRxPackets_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpRxPackets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpRxPackets_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpRxPackets_Object = MibTableColumn
fxsPmThreshProfRtpRxPackets = _FxsPmThreshProfRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 6),
    _FxsPmThreshProfRtpRxPackets_Type()
)
fxsPmThreshProfRtpRxPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpRxPackets.setStatus("current")


class _FxsPmThreshProfRtpTxLostPackets_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpTxLostPackets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpTxLostPackets_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpTxLostPackets_Object = MibTableColumn
fxsPmThreshProfRtpTxLostPackets = _FxsPmThreshProfRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 7),
    _FxsPmThreshProfRtpTxLostPackets_Type()
)
fxsPmThreshProfRtpTxLostPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpTxLostPackets.setStatus("current")


class _FxsPmThreshProfRtpRxLostPackets_Type(DisplayString):
    """Custom type fxsPmThreshProfRtpRxLostPackets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FxsPmThreshProfRtpRxLostPackets_Type.__name__ = "DisplayString"
_FxsPmThreshProfRtpRxLostPackets_Object = MibTableColumn
fxsPmThreshProfRtpRxLostPackets = _FxsPmThreshProfRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 8),
    _FxsPmThreshProfRtpRxLostPackets_Type()
)
fxsPmThreshProfRtpRxLostPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRtpRxLostPackets.setStatus("current")
_FxsPmThreshProfRowStatus_Type = RowStatus
_FxsPmThreshProfRowStatus_Object = MibTableColumn
fxsPmThreshProfRowStatus = _FxsPmThreshProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 15, 1, 9),
    _FxsPmThreshProfRowStatus_Type()
)
fxsPmThreshProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPmThreshProfRowStatus.setStatus("current")
_GePmCurrStatisticTable_Object = MibTable
gePmCurrStatisticTable = _GePmCurrStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16)
)
if mibBuilder.loadTexts:
    gePmCurrStatisticTable.setStatus("current")
_GePmCurrStatisticEntry_Object = MibTableRow
gePmCurrStatisticEntry = _GePmCurrStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1)
)
gePmCurrStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gePmCurrStatisticEntry.setStatus("current")
_GePmCurrStatisticTxOctets_Type = Counter64
_GePmCurrStatisticTxOctets_Object = MibTableColumn
gePmCurrStatisticTxOctets = _GePmCurrStatisticTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 1),
    _GePmCurrStatisticTxOctets_Type()
)
gePmCurrStatisticTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticTxOctets.setStatus("current")
_GePmCurrStatisticTxPkts_Type = Counter64
_GePmCurrStatisticTxPkts_Object = MibTableColumn
gePmCurrStatisticTxPkts = _GePmCurrStatisticTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 2),
    _GePmCurrStatisticTxPkts_Type()
)
gePmCurrStatisticTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticTxPkts.setStatus("current")
_GePmCurrStatisticTxBroadcastPkts_Type = Counter64
_GePmCurrStatisticTxBroadcastPkts_Object = MibTableColumn
gePmCurrStatisticTxBroadcastPkts = _GePmCurrStatisticTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 3),
    _GePmCurrStatisticTxBroadcastPkts_Type()
)
gePmCurrStatisticTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticTxBroadcastPkts.setStatus("current")
_GePmCurrStatisticTxMulticastPkts_Type = Counter64
_GePmCurrStatisticTxMulticastPkts_Object = MibTableColumn
gePmCurrStatisticTxMulticastPkts = _GePmCurrStatisticTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 4),
    _GePmCurrStatisticTxMulticastPkts_Type()
)
gePmCurrStatisticTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticTxMulticastPkts.setStatus("current")
_GePmCurrStatisticRxOctets_Type = Counter64
_GePmCurrStatisticRxOctets_Object = MibTableColumn
gePmCurrStatisticRxOctets = _GePmCurrStatisticRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 5),
    _GePmCurrStatisticRxOctets_Type()
)
gePmCurrStatisticRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxOctets.setStatus("current")
_GePmCurrStatisticRxPkts_Type = Counter64
_GePmCurrStatisticRxPkts_Object = MibTableColumn
gePmCurrStatisticRxPkts = _GePmCurrStatisticRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 6),
    _GePmCurrStatisticRxPkts_Type()
)
gePmCurrStatisticRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxPkts.setStatus("current")
_GePmCurrStatisticRxBroadcastPkts_Type = Counter64
_GePmCurrStatisticRxBroadcastPkts_Object = MibTableColumn
gePmCurrStatisticRxBroadcastPkts = _GePmCurrStatisticRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 7),
    _GePmCurrStatisticRxBroadcastPkts_Type()
)
gePmCurrStatisticRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxBroadcastPkts.setStatus("current")
_GePmCurrStatisticRxMulticastPkts_Type = Counter64
_GePmCurrStatisticRxMulticastPkts_Object = MibTableColumn
gePmCurrStatisticRxMulticastPkts = _GePmCurrStatisticRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 8),
    _GePmCurrStatisticRxMulticastPkts_Type()
)
gePmCurrStatisticRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxMulticastPkts.setStatus("current")
_GePmCurrStatisticRxCRCAlignErrors_Type = Counter64
_GePmCurrStatisticRxCRCAlignErrors_Object = MibTableColumn
gePmCurrStatisticRxCRCAlignErrors = _GePmCurrStatisticRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 9),
    _GePmCurrStatisticRxCRCAlignErrors_Type()
)
gePmCurrStatisticRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxCRCAlignErrors.setStatus("current")
_GePmCurrStatisticRxUndersizePkts_Type = Counter64
_GePmCurrStatisticRxUndersizePkts_Object = MibTableColumn
gePmCurrStatisticRxUndersizePkts = _GePmCurrStatisticRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 10),
    _GePmCurrStatisticRxUndersizePkts_Type()
)
gePmCurrStatisticRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxUndersizePkts.setStatus("current")
_GePmCurrStatisticRxOversizePkts_Type = Counter64
_GePmCurrStatisticRxOversizePkts_Object = MibTableColumn
gePmCurrStatisticRxOversizePkts = _GePmCurrStatisticRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 11),
    _GePmCurrStatisticRxOversizePkts_Type()
)
gePmCurrStatisticRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxOversizePkts.setStatus("current")
_GePmCurrStatisticRxFragments_Type = Counter64
_GePmCurrStatisticRxFragments_Object = MibTableColumn
gePmCurrStatisticRxFragments = _GePmCurrStatisticRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 12),
    _GePmCurrStatisticRxFragments_Type()
)
gePmCurrStatisticRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticRxFragments.setStatus("current")
_GePmCurrStatisticCollisions_Type = Counter64
_GePmCurrStatisticCollisions_Object = MibTableColumn
gePmCurrStatisticCollisions = _GePmCurrStatisticCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 13),
    _GePmCurrStatisticCollisions_Type()
)
gePmCurrStatisticCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticCollisions.setStatus("current")
_GePmCurrStatisticPkts64Octets_Type = Counter64
_GePmCurrStatisticPkts64Octets_Object = MibTableColumn
gePmCurrStatisticPkts64Octets = _GePmCurrStatisticPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 14),
    _GePmCurrStatisticPkts64Octets_Type()
)
gePmCurrStatisticPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts64Octets.setStatus("current")
_GePmCurrStatisticPkts65to127Octets_Type = Counter64
_GePmCurrStatisticPkts65to127Octets_Object = MibTableColumn
gePmCurrStatisticPkts65to127Octets = _GePmCurrStatisticPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 15),
    _GePmCurrStatisticPkts65to127Octets_Type()
)
gePmCurrStatisticPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts65to127Octets.setStatus("current")
_GePmCurrStatisticPkts128to255Octets_Type = Counter64
_GePmCurrStatisticPkts128to255Octets_Object = MibTableColumn
gePmCurrStatisticPkts128to255Octets = _GePmCurrStatisticPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 16),
    _GePmCurrStatisticPkts128to255Octets_Type()
)
gePmCurrStatisticPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts128to255Octets.setStatus("current")
_GePmCurrStatisticPkts256to511Octets_Type = Counter64
_GePmCurrStatisticPkts256to511Octets_Object = MibTableColumn
gePmCurrStatisticPkts256to511Octets = _GePmCurrStatisticPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 17),
    _GePmCurrStatisticPkts256to511Octets_Type()
)
gePmCurrStatisticPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts256to511Octets.setStatus("current")
_GePmCurrStatisticPkts512to1023Octets_Type = Counter64
_GePmCurrStatisticPkts512to1023Octets_Object = MibTableColumn
gePmCurrStatisticPkts512to1023Octets = _GePmCurrStatisticPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 18),
    _GePmCurrStatisticPkts512to1023Octets_Type()
)
gePmCurrStatisticPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts512to1023Octets.setStatus("current")
_GePmCurrStatisticPkts1024to1518Octets_Type = Counter64
_GePmCurrStatisticPkts1024to1518Octets_Object = MibTableColumn
gePmCurrStatisticPkts1024to1518Octets = _GePmCurrStatisticPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 19),
    _GePmCurrStatisticPkts1024to1518Octets_Type()
)
gePmCurrStatisticPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts1024to1518Octets.setStatus("current")
_GePmCurrStatisticPkts1519to1522Octets_Type = Counter64
_GePmCurrStatisticPkts1519to1522Octets_Object = MibTableColumn
gePmCurrStatisticPkts1519to1522Octets = _GePmCurrStatisticPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 20),
    _GePmCurrStatisticPkts1519to1522Octets_Type()
)
gePmCurrStatisticPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticPkts1519to1522Octets.setStatus("current")
_GePmCurrStatisticTimestamp_Type = Unsigned32
_GePmCurrStatisticTimestamp_Object = MibTableColumn
gePmCurrStatisticTimestamp = _GePmCurrStatisticTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 16, 1, 21),
    _GePmCurrStatisticTimestamp_Type()
)
gePmCurrStatisticTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePmCurrStatisticTimestamp.setStatus("current")
_FxsPmCurrStatisticTable_Object = MibTable
fxsPmCurrStatisticTable = _FxsPmCurrStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18)
)
if mibBuilder.loadTexts:
    fxsPmCurrStatisticTable.setStatus("current")
_FxsPmCurrStatisticEntry_Object = MibTableRow
fxsPmCurrStatisticEntry = _FxsPmCurrStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1)
)
fxsPmCurrStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxsPmCurrStatisticEntry.setStatus("current")
_FxsPmCurrStatisticRtpElapsedTime_Type = Integer32
_FxsPmCurrStatisticRtpElapsedTime_Object = MibTableColumn
fxsPmCurrStatisticRtpElapsedTime = _FxsPmCurrStatisticRtpElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 1),
    _FxsPmCurrStatisticRtpElapsedTime_Type()
)
fxsPmCurrStatisticRtpElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpElapsedTime.setStatus("current")
_FxsPmCurrStatisticRtpTxBytes_Type = Counter64
_FxsPmCurrStatisticRtpTxBytes_Object = MibTableColumn
fxsPmCurrStatisticRtpTxBytes = _FxsPmCurrStatisticRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 2),
    _FxsPmCurrStatisticRtpTxBytes_Type()
)
fxsPmCurrStatisticRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpTxBytes.setStatus("current")
_FxsPmCurrStatisticRtpRxBytes_Type = Counter64
_FxsPmCurrStatisticRtpRxBytes_Object = MibTableColumn
fxsPmCurrStatisticRtpRxBytes = _FxsPmCurrStatisticRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 3),
    _FxsPmCurrStatisticRtpRxBytes_Type()
)
fxsPmCurrStatisticRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpRxBytes.setStatus("current")
_FxsPmCurrStatisticRtpTxPackets_Type = Counter64
_FxsPmCurrStatisticRtpTxPackets_Object = MibTableColumn
fxsPmCurrStatisticRtpTxPackets = _FxsPmCurrStatisticRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 4),
    _FxsPmCurrStatisticRtpTxPackets_Type()
)
fxsPmCurrStatisticRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpTxPackets.setStatus("current")
_FxsPmCurrStatisticRtpRxPackets_Type = Counter64
_FxsPmCurrStatisticRtpRxPackets_Object = MibTableColumn
fxsPmCurrStatisticRtpRxPackets = _FxsPmCurrStatisticRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 5),
    _FxsPmCurrStatisticRtpRxPackets_Type()
)
fxsPmCurrStatisticRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpRxPackets.setStatus("current")
_FxsPmCurrStatisticRtpTxLostPackets_Type = Counter64
_FxsPmCurrStatisticRtpTxLostPackets_Object = MibTableColumn
fxsPmCurrStatisticRtpTxLostPackets = _FxsPmCurrStatisticRtpTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 6),
    _FxsPmCurrStatisticRtpTxLostPackets_Type()
)
fxsPmCurrStatisticRtpTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpTxLostPackets.setStatus("current")
_FxsPmCurrStatisticRtpRxLostPackets_Type = Counter64
_FxsPmCurrStatisticRtpRxLostPackets_Object = MibTableColumn
fxsPmCurrStatisticRtpRxLostPackets = _FxsPmCurrStatisticRtpRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 7),
    _FxsPmCurrStatisticRtpRxLostPackets_Type()
)
fxsPmCurrStatisticRtpRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticRtpRxLostPackets.setStatus("current")
_FxsPmCurrStatisticTimestamp_Type = Unsigned32
_FxsPmCurrStatisticTimestamp_Object = MibTableColumn
fxsPmCurrStatisticTimestamp = _FxsPmCurrStatisticTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 18, 1, 8),
    _FxsPmCurrStatisticTimestamp_Type()
)
fxsPmCurrStatisticTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPmCurrStatisticTimestamp.setStatus("current")
_DslPmCurr15minTable_Object = MibTable
dslPmCurr15minTable = _DslPmCurr15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19)
)
if mibBuilder.loadTexts:
    dslPmCurr15minTable.setStatus("current")
_DslPmCurr15minEntry_Object = MibTableRow
dslPmCurr15minEntry = _DslPmCurr15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1)
)
dslPmCurr15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dslPmCurr15minEntry.setStatus("current")
_DslPmCurr15minElapsed_Type = Integer32
_DslPmCurr15minElapsed_Object = MibTableColumn
dslPmCurr15minElapsed = _DslPmCurr15minElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 1),
    _DslPmCurr15minElapsed_Type()
)
dslPmCurr15minElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minElapsed.setStatus("current")
_DslPmCurr15minTxOctets_Type = Counter64
_DslPmCurr15minTxOctets_Object = MibTableColumn
dslPmCurr15minTxOctets = _DslPmCurr15minTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 2),
    _DslPmCurr15minTxOctets_Type()
)
dslPmCurr15minTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxOctets.setStatus("current")
_DslPmCurr15minTxPkts_Type = Counter64
_DslPmCurr15minTxPkts_Object = MibTableColumn
dslPmCurr15minTxPkts = _DslPmCurr15minTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 3),
    _DslPmCurr15minTxPkts_Type()
)
dslPmCurr15minTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxPkts.setStatus("current")
_DslPmCurr15minTxUnicastPkts_Type = Counter64
_DslPmCurr15minTxUnicastPkts_Object = MibTableColumn
dslPmCurr15minTxUnicastPkts = _DslPmCurr15minTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 4),
    _DslPmCurr15minTxUnicastPkts_Type()
)
dslPmCurr15minTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxUnicastPkts.setStatus("current")
_DslPmCurr15minTxBroadcastPkts_Type = Counter64
_DslPmCurr15minTxBroadcastPkts_Object = MibTableColumn
dslPmCurr15minTxBroadcastPkts = _DslPmCurr15minTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 5),
    _DslPmCurr15minTxBroadcastPkts_Type()
)
dslPmCurr15minTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxBroadcastPkts.setStatus("current")
_DslPmCurr15minTxMulticastPkts_Type = Counter64
_DslPmCurr15minTxMulticastPkts_Object = MibTableColumn
dslPmCurr15minTxMulticastPkts = _DslPmCurr15minTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 6),
    _DslPmCurr15minTxMulticastPkts_Type()
)
dslPmCurr15minTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxMulticastPkts.setStatus("current")
_DslPmCurr15minTxDiscardPkts_Type = Counter64
_DslPmCurr15minTxDiscardPkts_Object = MibTableColumn
dslPmCurr15minTxDiscardPkts = _DslPmCurr15minTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 7),
    _DslPmCurr15minTxDiscardPkts_Type()
)
dslPmCurr15minTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minTxDiscardPkts.setStatus("current")
_DslPmCurr15minRxOctets_Type = Counter64
_DslPmCurr15minRxOctets_Object = MibTableColumn
dslPmCurr15minRxOctets = _DslPmCurr15minRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 8),
    _DslPmCurr15minRxOctets_Type()
)
dslPmCurr15minRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxOctets.setStatus("current")
_DslPmCurr15minRxPkts_Type = Counter64
_DslPmCurr15minRxPkts_Object = MibTableColumn
dslPmCurr15minRxPkts = _DslPmCurr15minRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 9),
    _DslPmCurr15minRxPkts_Type()
)
dslPmCurr15minRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxPkts.setStatus("current")
_DslPmCurr15minRxUnicastPkts_Type = Counter64
_DslPmCurr15minRxUnicastPkts_Object = MibTableColumn
dslPmCurr15minRxUnicastPkts = _DslPmCurr15minRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 10),
    _DslPmCurr15minRxUnicastPkts_Type()
)
dslPmCurr15minRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxUnicastPkts.setStatus("current")
_DslPmCurr15minRxBroadcastPkts_Type = Counter64
_DslPmCurr15minRxBroadcastPkts_Object = MibTableColumn
dslPmCurr15minRxBroadcastPkts = _DslPmCurr15minRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 11),
    _DslPmCurr15minRxBroadcastPkts_Type()
)
dslPmCurr15minRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxBroadcastPkts.setStatus("current")
_DslPmCurr15minRxMulticastPkts_Type = Counter64
_DslPmCurr15minRxMulticastPkts_Object = MibTableColumn
dslPmCurr15minRxMulticastPkts = _DslPmCurr15minRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 12),
    _DslPmCurr15minRxMulticastPkts_Type()
)
dslPmCurr15minRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxMulticastPkts.setStatus("current")
_DslPmCurr15minRxDiscardPkts_Type = Counter64
_DslPmCurr15minRxDiscardPkts_Object = MibTableColumn
dslPmCurr15minRxDiscardPkts = _DslPmCurr15minRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 19, 1, 13),
    _DslPmCurr15minRxDiscardPkts_Type()
)
dslPmCurr15minRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr15minRxDiscardPkts.setStatus("current")
_DslPmHist15minTable_Object = MibTable
dslPmHist15minTable = _DslPmHist15minTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20)
)
if mibBuilder.loadTexts:
    dslPmHist15minTable.setStatus("current")
_DslPmHist15minEntry_Object = MibTableRow
dslPmHist15minEntry = _DslPmHist15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1)
)
dslPmHist15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "dslPmHist15minIndex"),
)
if mibBuilder.loadTexts:
    dslPmHist15minEntry.setStatus("current")


class _DslPmHist15minIndex_Type(Integer32):
    """Custom type dslPmHist15minIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DslPmHist15minIndex_Type.__name__ = "Integer32"
_DslPmHist15minIndex_Object = MibTableColumn
dslPmHist15minIndex = _DslPmHist15minIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 1),
    _DslPmHist15minIndex_Type()
)
dslPmHist15minIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minIndex.setStatus("current")
_DslPmHist15minElapsed_Type = Integer32
_DslPmHist15minElapsed_Object = MibTableColumn
dslPmHist15minElapsed = _DslPmHist15minElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 2),
    _DslPmHist15minElapsed_Type()
)
dslPmHist15minElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minElapsed.setStatus("current")
_DslPmHist15minStartTime_Type = DisplayString
_DslPmHist15minStartTime_Object = MibTableColumn
dslPmHist15minStartTime = _DslPmHist15minStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 3),
    _DslPmHist15minStartTime_Type()
)
dslPmHist15minStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minStartTime.setStatus("current")
_DslPmHist15minEndTime_Type = DisplayString
_DslPmHist15minEndTime_Object = MibTableColumn
dslPmHist15minEndTime = _DslPmHist15minEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 4),
    _DslPmHist15minEndTime_Type()
)
dslPmHist15minEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minEndTime.setStatus("current")
_DslPmHist15minTxOctets_Type = Counter64
_DslPmHist15minTxOctets_Object = MibTableColumn
dslPmHist15minTxOctets = _DslPmHist15minTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 5),
    _DslPmHist15minTxOctets_Type()
)
dslPmHist15minTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxOctets.setStatus("current")
_DslPmHist15minTxPkts_Type = Counter64
_DslPmHist15minTxPkts_Object = MibTableColumn
dslPmHist15minTxPkts = _DslPmHist15minTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 6),
    _DslPmHist15minTxPkts_Type()
)
dslPmHist15minTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxPkts.setStatus("current")
_DslPmHist15minTxUnicastPkts_Type = Counter64
_DslPmHist15minTxUnicastPkts_Object = MibTableColumn
dslPmHist15minTxUnicastPkts = _DslPmHist15minTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 7),
    _DslPmHist15minTxUnicastPkts_Type()
)
dslPmHist15minTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxUnicastPkts.setStatus("current")
_DslPmHist15minTxBroadcastPkts_Type = Counter64
_DslPmHist15minTxBroadcastPkts_Object = MibTableColumn
dslPmHist15minTxBroadcastPkts = _DslPmHist15minTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 8),
    _DslPmHist15minTxBroadcastPkts_Type()
)
dslPmHist15minTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxBroadcastPkts.setStatus("current")
_DslPmHist15minTxMulticastPkts_Type = Counter64
_DslPmHist15minTxMulticastPkts_Object = MibTableColumn
dslPmHist15minTxMulticastPkts = _DslPmHist15minTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 9),
    _DslPmHist15minTxMulticastPkts_Type()
)
dslPmHist15minTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxMulticastPkts.setStatus("current")
_DslPmHist15minTxDiscardPkts_Type = Counter64
_DslPmHist15minTxDiscardPkts_Object = MibTableColumn
dslPmHist15minTxDiscardPkts = _DslPmHist15minTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 10),
    _DslPmHist15minTxDiscardPkts_Type()
)
dslPmHist15minTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minTxDiscardPkts.setStatus("current")
_DslPmHist15minRxOctets_Type = Counter64
_DslPmHist15minRxOctets_Object = MibTableColumn
dslPmHist15minRxOctets = _DslPmHist15minRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 11),
    _DslPmHist15minRxOctets_Type()
)
dslPmHist15minRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxOctets.setStatus("current")
_DslPmHist15minRxPkts_Type = Counter64
_DslPmHist15minRxPkts_Object = MibTableColumn
dslPmHist15minRxPkts = _DslPmHist15minRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 12),
    _DslPmHist15minRxPkts_Type()
)
dslPmHist15minRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxPkts.setStatus("current")
_DslPmHist15minRxUnicastPkts_Type = Counter64
_DslPmHist15minRxUnicastPkts_Object = MibTableColumn
dslPmHist15minRxUnicastPkts = _DslPmHist15minRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 13),
    _DslPmHist15minRxUnicastPkts_Type()
)
dslPmHist15minRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxUnicastPkts.setStatus("current")
_DslPmHist15minRxBroadcastPkts_Type = Counter64
_DslPmHist15minRxBroadcastPkts_Object = MibTableColumn
dslPmHist15minRxBroadcastPkts = _DslPmHist15minRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 14),
    _DslPmHist15minRxBroadcastPkts_Type()
)
dslPmHist15minRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxBroadcastPkts.setStatus("current")
_DslPmHist15minRxMulticastPkts_Type = Counter64
_DslPmHist15minRxMulticastPkts_Object = MibTableColumn
dslPmHist15minRxMulticastPkts = _DslPmHist15minRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 15),
    _DslPmHist15minRxMulticastPkts_Type()
)
dslPmHist15minRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxMulticastPkts.setStatus("current")
_DslPmHist15minRxDiscardPkts_Type = Counter64
_DslPmHist15minRxDiscardPkts_Object = MibTableColumn
dslPmHist15minRxDiscardPkts = _DslPmHist15minRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 20, 1, 16),
    _DslPmHist15minRxDiscardPkts_Type()
)
dslPmHist15minRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist15minRxDiscardPkts.setStatus("current")
_DslPmCurr1dayTable_Object = MibTable
dslPmCurr1dayTable = _DslPmCurr1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21)
)
if mibBuilder.loadTexts:
    dslPmCurr1dayTable.setStatus("current")
_DslPmCurr1dayEntry_Object = MibTableRow
dslPmCurr1dayEntry = _DslPmCurr1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1)
)
dslPmCurr1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dslPmCurr1dayEntry.setStatus("current")
_DslPmCurr1dayElapsed_Type = Integer32
_DslPmCurr1dayElapsed_Object = MibTableColumn
dslPmCurr1dayElapsed = _DslPmCurr1dayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 1),
    _DslPmCurr1dayElapsed_Type()
)
dslPmCurr1dayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayElapsed.setStatus("current")
_DslPmCurr1dayTxOctets_Type = Counter64
_DslPmCurr1dayTxOctets_Object = MibTableColumn
dslPmCurr1dayTxOctets = _DslPmCurr1dayTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 2),
    _DslPmCurr1dayTxOctets_Type()
)
dslPmCurr1dayTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxOctets.setStatus("current")
_DslPmCurr1dayTxPkts_Type = Counter64
_DslPmCurr1dayTxPkts_Object = MibTableColumn
dslPmCurr1dayTxPkts = _DslPmCurr1dayTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 3),
    _DslPmCurr1dayTxPkts_Type()
)
dslPmCurr1dayTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxPkts.setStatus("current")
_DslPmCurr1dayTxUnicastPkts_Type = Counter64
_DslPmCurr1dayTxUnicastPkts_Object = MibTableColumn
dslPmCurr1dayTxUnicastPkts = _DslPmCurr1dayTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 4),
    _DslPmCurr1dayTxUnicastPkts_Type()
)
dslPmCurr1dayTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxUnicastPkts.setStatus("current")
_DslPmCurr1dayTxBroadcastPkts_Type = Counter64
_DslPmCurr1dayTxBroadcastPkts_Object = MibTableColumn
dslPmCurr1dayTxBroadcastPkts = _DslPmCurr1dayTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 5),
    _DslPmCurr1dayTxBroadcastPkts_Type()
)
dslPmCurr1dayTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxBroadcastPkts.setStatus("current")
_DslPmCurr1dayTxMulticastPkts_Type = Counter64
_DslPmCurr1dayTxMulticastPkts_Object = MibTableColumn
dslPmCurr1dayTxMulticastPkts = _DslPmCurr1dayTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 6),
    _DslPmCurr1dayTxMulticastPkts_Type()
)
dslPmCurr1dayTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxMulticastPkts.setStatus("current")
_DslPmCurr1dayTxDiscardPkts_Type = Counter64
_DslPmCurr1dayTxDiscardPkts_Object = MibTableColumn
dslPmCurr1dayTxDiscardPkts = _DslPmCurr1dayTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 7),
    _DslPmCurr1dayTxDiscardPkts_Type()
)
dslPmCurr1dayTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayTxDiscardPkts.setStatus("current")
_DslPmCurr1dayRxOctets_Type = Counter64
_DslPmCurr1dayRxOctets_Object = MibTableColumn
dslPmCurr1dayRxOctets = _DslPmCurr1dayRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 8),
    _DslPmCurr1dayRxOctets_Type()
)
dslPmCurr1dayRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxOctets.setStatus("current")
_DslPmCurr1dayRxPkts_Type = Counter64
_DslPmCurr1dayRxPkts_Object = MibTableColumn
dslPmCurr1dayRxPkts = _DslPmCurr1dayRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 9),
    _DslPmCurr1dayRxPkts_Type()
)
dslPmCurr1dayRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxPkts.setStatus("current")
_DslPmCurr1dayRxUnicastPkts_Type = Counter64
_DslPmCurr1dayRxUnicastPkts_Object = MibTableColumn
dslPmCurr1dayRxUnicastPkts = _DslPmCurr1dayRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 10),
    _DslPmCurr1dayRxUnicastPkts_Type()
)
dslPmCurr1dayRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxUnicastPkts.setStatus("current")
_DslPmCurr1dayRxBroadcastPkts_Type = Counter64
_DslPmCurr1dayRxBroadcastPkts_Object = MibTableColumn
dslPmCurr1dayRxBroadcastPkts = _DslPmCurr1dayRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 11),
    _DslPmCurr1dayRxBroadcastPkts_Type()
)
dslPmCurr1dayRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxBroadcastPkts.setStatus("current")
_DslPmCurr1dayRxMulticastPkts_Type = Counter64
_DslPmCurr1dayRxMulticastPkts_Object = MibTableColumn
dslPmCurr1dayRxMulticastPkts = _DslPmCurr1dayRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 12),
    _DslPmCurr1dayRxMulticastPkts_Type()
)
dslPmCurr1dayRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxMulticastPkts.setStatus("current")
_DslPmCurr1dayRxDiscardPkts_Type = Counter64
_DslPmCurr1dayRxDiscardPkts_Object = MibTableColumn
dslPmCurr1dayRxDiscardPkts = _DslPmCurr1dayRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 21, 1, 13),
    _DslPmCurr1dayRxDiscardPkts_Type()
)
dslPmCurr1dayRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurr1dayRxDiscardPkts.setStatus("current")
_DslPmHist1dayTable_Object = MibTable
dslPmHist1dayTable = _DslPmHist1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22)
)
if mibBuilder.loadTexts:
    dslPmHist1dayTable.setStatus("current")
_DslPmHist1dayEntry_Object = MibTableRow
dslPmHist1dayEntry = _DslPmHist1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1)
)
dslPmHist1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "dslPmHist1dayIndex"),
)
if mibBuilder.loadTexts:
    dslPmHist1dayEntry.setStatus("current")


class _DslPmHist1dayIndex_Type(Integer32):
    """Custom type dslPmHist1dayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DslPmHist1dayIndex_Type.__name__ = "Integer32"
_DslPmHist1dayIndex_Object = MibTableColumn
dslPmHist1dayIndex = _DslPmHist1dayIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 1),
    _DslPmHist1dayIndex_Type()
)
dslPmHist1dayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayIndex.setStatus("current")
_DslPmHist1dayStartTime_Type = DisplayString
_DslPmHist1dayStartTime_Object = MibTableColumn
dslPmHist1dayStartTime = _DslPmHist1dayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 2),
    _DslPmHist1dayStartTime_Type()
)
dslPmHist1dayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayStartTime.setStatus("current")
_DslPmHist1dayEndTime_Type = DisplayString
_DslPmHist1dayEndTime_Object = MibTableColumn
dslPmHist1dayEndTime = _DslPmHist1dayEndTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 3),
    _DslPmHist1dayEndTime_Type()
)
dslPmHist1dayEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayEndTime.setStatus("current")
_DslPmHist1dayTxOctets_Type = Counter64
_DslPmHist1dayTxOctets_Object = MibTableColumn
dslPmHist1dayTxOctets = _DslPmHist1dayTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 4),
    _DslPmHist1dayTxOctets_Type()
)
dslPmHist1dayTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxOctets.setStatus("current")
_DslPmHist1dayTxPkts_Type = Counter64
_DslPmHist1dayTxPkts_Object = MibTableColumn
dslPmHist1dayTxPkts = _DslPmHist1dayTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 5),
    _DslPmHist1dayTxPkts_Type()
)
dslPmHist1dayTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxPkts.setStatus("current")
_DslPmHist1dayTxUnicastPkts_Type = Counter64
_DslPmHist1dayTxUnicastPkts_Object = MibTableColumn
dslPmHist1dayTxUnicastPkts = _DslPmHist1dayTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 6),
    _DslPmHist1dayTxUnicastPkts_Type()
)
dslPmHist1dayTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxUnicastPkts.setStatus("current")
_DslPmHist1dayTxBroadcastPkts_Type = Counter64
_DslPmHist1dayTxBroadcastPkts_Object = MibTableColumn
dslPmHist1dayTxBroadcastPkts = _DslPmHist1dayTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 7),
    _DslPmHist1dayTxBroadcastPkts_Type()
)
dslPmHist1dayTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxBroadcastPkts.setStatus("current")
_DslPmHist1dayTxMulticastPkts_Type = Counter64
_DslPmHist1dayTxMulticastPkts_Object = MibTableColumn
dslPmHist1dayTxMulticastPkts = _DslPmHist1dayTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 8),
    _DslPmHist1dayTxMulticastPkts_Type()
)
dslPmHist1dayTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxMulticastPkts.setStatus("current")
_DslPmHist1dayTxDiscardPkts_Type = Counter64
_DslPmHist1dayTxDiscardPkts_Object = MibTableColumn
dslPmHist1dayTxDiscardPkts = _DslPmHist1dayTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 9),
    _DslPmHist1dayTxDiscardPkts_Type()
)
dslPmHist1dayTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayTxDiscardPkts.setStatus("current")
_DslPmHist1dayRxOctets_Type = Counter64
_DslPmHist1dayRxOctets_Object = MibTableColumn
dslPmHist1dayRxOctets = _DslPmHist1dayRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 10),
    _DslPmHist1dayRxOctets_Type()
)
dslPmHist1dayRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxOctets.setStatus("current")
_DslPmHist1dayRxPkts_Type = Counter64
_DslPmHist1dayRxPkts_Object = MibTableColumn
dslPmHist1dayRxPkts = _DslPmHist1dayRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 11),
    _DslPmHist1dayRxPkts_Type()
)
dslPmHist1dayRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxPkts.setStatus("current")
_DslPmHist1dayRxUnicastPkts_Type = Counter64
_DslPmHist1dayRxUnicastPkts_Object = MibTableColumn
dslPmHist1dayRxUnicastPkts = _DslPmHist1dayRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 12),
    _DslPmHist1dayRxUnicastPkts_Type()
)
dslPmHist1dayRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxUnicastPkts.setStatus("current")
_DslPmHist1dayRxBroadcastPkts_Type = Counter64
_DslPmHist1dayRxBroadcastPkts_Object = MibTableColumn
dslPmHist1dayRxBroadcastPkts = _DslPmHist1dayRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 13),
    _DslPmHist1dayRxBroadcastPkts_Type()
)
dslPmHist1dayRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxBroadcastPkts.setStatus("current")
_DslPmHist1dayRxMulticastPkts_Type = Counter64
_DslPmHist1dayRxMulticastPkts_Object = MibTableColumn
dslPmHist1dayRxMulticastPkts = _DslPmHist1dayRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 14),
    _DslPmHist1dayRxMulticastPkts_Type()
)
dslPmHist1dayRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxMulticastPkts.setStatus("current")
_DslPmHist1dayRxDiscardPkts_Type = Counter64
_DslPmHist1dayRxDiscardPkts_Object = MibTableColumn
dslPmHist1dayRxDiscardPkts = _DslPmHist1dayRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 22, 1, 15),
    _DslPmHist1dayRxDiscardPkts_Type()
)
dslPmHist1dayRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmHist1dayRxDiscardPkts.setStatus("current")
_DslPmThreshProfTable_Object = MibTable
dslPmThreshProfTable = _DslPmThreshProfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23)
)
if mibBuilder.loadTexts:
    dslPmThreshProfTable.setStatus("current")
_DslPmThreshProfEntry_Object = MibTableRow
dslPmThreshProfEntry = _DslPmThreshProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1)
)
dslPmThreshProfEntry.setIndexNames(
    (1, "VES1724-58V-MIB", "dslPmThreshProfName"),
)
if mibBuilder.loadTexts:
    dslPmThreshProfEntry.setStatus("current")
_DslPmThreshProfName_Type = DisplayString
_DslPmThreshProfName_Object = MibTableColumn
dslPmThreshProfName = _DslPmThreshProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 1),
    _DslPmThreshProfName_Type()
)
dslPmThreshProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmThreshProfName.setStatus("current")


class _DslPmThreshProfTxOctets_Type(DisplayString):
    """Custom type dslPmThreshProfTxOctets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxOctets_Type.__name__ = "DisplayString"
_DslPmThreshProfTxOctets_Object = MibTableColumn
dslPmThreshProfTxOctets = _DslPmThreshProfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 2),
    _DslPmThreshProfTxOctets_Type()
)
dslPmThreshProfTxOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxOctets.setStatus("current")


class _DslPmThreshProfTxPkts_Type(DisplayString):
    """Custom type dslPmThreshProfTxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfTxPkts_Object = MibTableColumn
dslPmThreshProfTxPkts = _DslPmThreshProfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 3),
    _DslPmThreshProfTxPkts_Type()
)
dslPmThreshProfTxPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxPkts.setStatus("current")


class _DslPmThreshProfTxUnicastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfTxUnicastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxUnicastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfTxUnicastPkts_Object = MibTableColumn
dslPmThreshProfTxUnicastPkts = _DslPmThreshProfTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 4),
    _DslPmThreshProfTxUnicastPkts_Type()
)
dslPmThreshProfTxUnicastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxUnicastPkts.setStatus("current")


class _DslPmThreshProfTxBroadcastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfTxBroadcastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxBroadcastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfTxBroadcastPkts_Object = MibTableColumn
dslPmThreshProfTxBroadcastPkts = _DslPmThreshProfTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 5),
    _DslPmThreshProfTxBroadcastPkts_Type()
)
dslPmThreshProfTxBroadcastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxBroadcastPkts.setStatus("current")


class _DslPmThreshProfTxMulticastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfTxMulticastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxMulticastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfTxMulticastPkts_Object = MibTableColumn
dslPmThreshProfTxMulticastPkts = _DslPmThreshProfTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 6),
    _DslPmThreshProfTxMulticastPkts_Type()
)
dslPmThreshProfTxMulticastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxMulticastPkts.setStatus("current")


class _DslPmThreshProfTxDiscardPkts_Type(DisplayString):
    """Custom type dslPmThreshProfTxDiscardPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfTxDiscardPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfTxDiscardPkts_Object = MibTableColumn
dslPmThreshProfTxDiscardPkts = _DslPmThreshProfTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 7),
    _DslPmThreshProfTxDiscardPkts_Type()
)
dslPmThreshProfTxDiscardPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfTxDiscardPkts.setStatus("current")


class _DslPmThreshProfRxOctets_Type(DisplayString):
    """Custom type dslPmThreshProfRxOctets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxOctets_Type.__name__ = "DisplayString"
_DslPmThreshProfRxOctets_Object = MibTableColumn
dslPmThreshProfRxOctets = _DslPmThreshProfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 8),
    _DslPmThreshProfRxOctets_Type()
)
dslPmThreshProfRxOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxOctets.setStatus("current")


class _DslPmThreshProfRxPkts_Type(DisplayString):
    """Custom type dslPmThreshProfRxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfRxPkts_Object = MibTableColumn
dslPmThreshProfRxPkts = _DslPmThreshProfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 9),
    _DslPmThreshProfRxPkts_Type()
)
dslPmThreshProfRxPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxPkts.setStatus("current")


class _DslPmThreshProfRxUnicastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfRxUnicastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxUnicastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfRxUnicastPkts_Object = MibTableColumn
dslPmThreshProfRxUnicastPkts = _DslPmThreshProfRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 10),
    _DslPmThreshProfRxUnicastPkts_Type()
)
dslPmThreshProfRxUnicastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxUnicastPkts.setStatus("current")


class _DslPmThreshProfRxBroadcastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfRxBroadcastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxBroadcastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfRxBroadcastPkts_Object = MibTableColumn
dslPmThreshProfRxBroadcastPkts = _DslPmThreshProfRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 11),
    _DslPmThreshProfRxBroadcastPkts_Type()
)
dslPmThreshProfRxBroadcastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxBroadcastPkts.setStatus("current")


class _DslPmThreshProfRxMulticastPkts_Type(DisplayString):
    """Custom type dslPmThreshProfRxMulticastPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxMulticastPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfRxMulticastPkts_Object = MibTableColumn
dslPmThreshProfRxMulticastPkts = _DslPmThreshProfRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 12),
    _DslPmThreshProfRxMulticastPkts_Type()
)
dslPmThreshProfRxMulticastPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxMulticastPkts.setStatus("current")


class _DslPmThreshProfRxDiscardPkts_Type(DisplayString):
    """Custom type dslPmThreshProfRxDiscardPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DslPmThreshProfRxDiscardPkts_Type.__name__ = "DisplayString"
_DslPmThreshProfRxDiscardPkts_Object = MibTableColumn
dslPmThreshProfRxDiscardPkts = _DslPmThreshProfRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 13),
    _DslPmThreshProfRxDiscardPkts_Type()
)
dslPmThreshProfRxDiscardPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRxDiscardPkts.setStatus("current")
_DslPmThreshProfRowStatus_Type = RowStatus
_DslPmThreshProfRowStatus_Object = MibTableColumn
dslPmThreshProfRowStatus = _DslPmThreshProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 23, 1, 14),
    _DslPmThreshProfRowStatus_Type()
)
dslPmThreshProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dslPmThreshProfRowStatus.setStatus("current")
_DslPmCurrStatisticTable_Object = MibTable
dslPmCurrStatisticTable = _DslPmCurrStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24)
)
if mibBuilder.loadTexts:
    dslPmCurrStatisticTable.setStatus("current")
_DslPmCurrStatisticEntry_Object = MibTableRow
dslPmCurrStatisticEntry = _DslPmCurrStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1)
)
dslPmCurrStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dslPmCurrStatisticEntry.setStatus("current")
_DslPmCurrStatisticTxOctets_Type = Counter64
_DslPmCurrStatisticTxOctets_Object = MibTableColumn
dslPmCurrStatisticTxOctets = _DslPmCurrStatisticTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 1),
    _DslPmCurrStatisticTxOctets_Type()
)
dslPmCurrStatisticTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxOctets.setStatus("current")
_DslPmCurrStatisticTxPkts_Type = Counter64
_DslPmCurrStatisticTxPkts_Object = MibTableColumn
dslPmCurrStatisticTxPkts = _DslPmCurrStatisticTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 2),
    _DslPmCurrStatisticTxPkts_Type()
)
dslPmCurrStatisticTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxPkts.setStatus("current")
_DslPmCurrStatisticTxUnicastPkts_Type = Counter64
_DslPmCurrStatisticTxUnicastPkts_Object = MibTableColumn
dslPmCurrStatisticTxUnicastPkts = _DslPmCurrStatisticTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 3),
    _DslPmCurrStatisticTxUnicastPkts_Type()
)
dslPmCurrStatisticTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxUnicastPkts.setStatus("current")
_DslPmCurrStatisticTxBroadcastPkts_Type = Counter64
_DslPmCurrStatisticTxBroadcastPkts_Object = MibTableColumn
dslPmCurrStatisticTxBroadcastPkts = _DslPmCurrStatisticTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 4),
    _DslPmCurrStatisticTxBroadcastPkts_Type()
)
dslPmCurrStatisticTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxBroadcastPkts.setStatus("current")
_DslPmCurrStatisticTxMulticastPkts_Type = Counter64
_DslPmCurrStatisticTxMulticastPkts_Object = MibTableColumn
dslPmCurrStatisticTxMulticastPkts = _DslPmCurrStatisticTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 5),
    _DslPmCurrStatisticTxMulticastPkts_Type()
)
dslPmCurrStatisticTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxMulticastPkts.setStatus("current")
_DslPmCurrStatisticTxDiscard_Type = Counter64
_DslPmCurrStatisticTxDiscard_Object = MibTableColumn
dslPmCurrStatisticTxDiscard = _DslPmCurrStatisticTxDiscard_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 6),
    _DslPmCurrStatisticTxDiscard_Type()
)
dslPmCurrStatisticTxDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTxDiscard.setStatus("current")
_DslPmCurrStatisticRxOctets_Type = Counter64
_DslPmCurrStatisticRxOctets_Object = MibTableColumn
dslPmCurrStatisticRxOctets = _DslPmCurrStatisticRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 7),
    _DslPmCurrStatisticRxOctets_Type()
)
dslPmCurrStatisticRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxOctets.setStatus("current")
_DslPmCurrStatisticRxPkts_Type = Counter64
_DslPmCurrStatisticRxPkts_Object = MibTableColumn
dslPmCurrStatisticRxPkts = _DslPmCurrStatisticRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 8),
    _DslPmCurrStatisticRxPkts_Type()
)
dslPmCurrStatisticRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxPkts.setStatus("current")
_DslPmCurrStatisticRxUnicastPkts_Type = Counter64
_DslPmCurrStatisticRxUnicastPkts_Object = MibTableColumn
dslPmCurrStatisticRxUnicastPkts = _DslPmCurrStatisticRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 9),
    _DslPmCurrStatisticRxUnicastPkts_Type()
)
dslPmCurrStatisticRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxUnicastPkts.setStatus("current")
_DslPmCurrStatisticRxBroadcastPkts_Type = Counter64
_DslPmCurrStatisticRxBroadcastPkts_Object = MibTableColumn
dslPmCurrStatisticRxBroadcastPkts = _DslPmCurrStatisticRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 10),
    _DslPmCurrStatisticRxBroadcastPkts_Type()
)
dslPmCurrStatisticRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxBroadcastPkts.setStatus("current")
_DslPmCurrStatisticRxMulticastPkts_Type = Counter64
_DslPmCurrStatisticRxMulticastPkts_Object = MibTableColumn
dslPmCurrStatisticRxMulticastPkts = _DslPmCurrStatisticRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 11),
    _DslPmCurrStatisticRxMulticastPkts_Type()
)
dslPmCurrStatisticRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxMulticastPkts.setStatus("current")
_DslPmCurrStatisticRxDiscard_Type = Counter64
_DslPmCurrStatisticRxDiscard_Object = MibTableColumn
dslPmCurrStatisticRxDiscard = _DslPmCurrStatisticRxDiscard_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 12),
    _DslPmCurrStatisticRxDiscard_Type()
)
dslPmCurrStatisticRxDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticRxDiscard.setStatus("current")
_DslPmCurrStatisticTimestamp_Type = Unsigned32
_DslPmCurrStatisticTimestamp_Object = MibTableColumn
dslPmCurrStatisticTimestamp = _DslPmCurrStatisticTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 24, 1, 13),
    _DslPmCurrStatisticTimestamp_Type()
)
dslPmCurrStatisticTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslPmCurrStatisticTimestamp.setStatus("current")
_DslBondingCurrCountersTable_Object = MibTable
dslBondingCurrCountersTable = _DslBondingCurrCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25)
)
if mibBuilder.loadTexts:
    dslBondingCurrCountersTable.setStatus("current")
_DslBondingCurrCountersEntry_Object = MibTableRow
dslBondingCurrCountersEntry = _DslBondingCurrCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1)
)
dslBondingCurrCountersEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dslBondingCurrCountersGroupName"),
)
if mibBuilder.loadTexts:
    dslBondingCurrCountersEntry.setStatus("current")
_DslBondingCurrCountersGroupName_Type = DisplayString
_DslBondingCurrCountersGroupName_Object = MibTableColumn
dslBondingCurrCountersGroupName = _DslBondingCurrCountersGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 1),
    _DslBondingCurrCountersGroupName_Type()
)
dslBondingCurrCountersGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersGroupName.setStatus("current")
_DslBondingCurrCountersPtmRxPackets_Type = Counter64
_DslBondingCurrCountersPtmRxPackets_Object = MibTableColumn
dslBondingCurrCountersPtmRxPackets = _DslBondingCurrCountersPtmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 2),
    _DslBondingCurrCountersPtmRxPackets_Type()
)
dslBondingCurrCountersPtmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxPackets.setStatus("current")
_DslBondingCurrCountersPtmNumFlushRequests_Type = Counter64
_DslBondingCurrCountersPtmNumFlushRequests_Object = MibTableColumn
dslBondingCurrCountersPtmNumFlushRequests = _DslBondingCurrCountersPtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 3),
    _DslBondingCurrCountersPtmNumFlushRequests_Type()
)
dslBondingCurrCountersPtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmNumFlushRequests.setStatus("current")
_DslBondingCurrCountersPtmNumTimeouts_Type = Counter64
_DslBondingCurrCountersPtmNumTimeouts_Object = MibTableColumn
dslBondingCurrCountersPtmNumTimeouts = _DslBondingCurrCountersPtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 4),
    _DslBondingCurrCountersPtmNumTimeouts_Type()
)
dslBondingCurrCountersPtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmNumTimeouts.setStatus("current")
_DslBondingCurrCountersPtmNumDirectSidResets_Type = Counter64
_DslBondingCurrCountersPtmNumDirectSidResets_Object = MibTableColumn
dslBondingCurrCountersPtmNumDirectSidResets = _DslBondingCurrCountersPtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 5),
    _DslBondingCurrCountersPtmNumDirectSidResets_Type()
)
dslBondingCurrCountersPtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmNumDirectSidResets.setStatus("current")
_DslBondingCurrCountersPtmRxSmallFragments_Type = Counter64
_DslBondingCurrCountersPtmRxSmallFragments_Object = MibTableColumn
dslBondingCurrCountersPtmRxSmallFragments = _DslBondingCurrCountersPtmRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 6),
    _DslBondingCurrCountersPtmRxSmallFragments_Type()
)
dslBondingCurrCountersPtmRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxSmallFragments.setStatus("current")
_DslBondingCurrCountersPtmRxLargeFragments_Type = Counter64
_DslBondingCurrCountersPtmRxLargeFragments_Object = MibTableColumn
dslBondingCurrCountersPtmRxLargeFragments = _DslBondingCurrCountersPtmRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 7),
    _DslBondingCurrCountersPtmRxLargeFragments_Type()
)
dslBondingCurrCountersPtmRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxLargeFragments.setStatus("current")
_DslBondingCurrCountersPtmRxBadFragments_Type = Counter64
_DslBondingCurrCountersPtmRxBadFragments_Object = MibTableColumn
dslBondingCurrCountersPtmRxBadFragments = _DslBondingCurrCountersPtmRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 8),
    _DslBondingCurrCountersPtmRxBadFragments_Type()
)
dslBondingCurrCountersPtmRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxBadFragments.setStatus("current")
_DslBondingCurrCountersPtmRxLostFragments_Type = Counter64
_DslBondingCurrCountersPtmRxLostFragments_Object = MibTableColumn
dslBondingCurrCountersPtmRxLostFragments = _DslBondingCurrCountersPtmRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 9),
    _DslBondingCurrCountersPtmRxLostFragments_Type()
)
dslBondingCurrCountersPtmRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxLostFragments.setStatus("current")
_DslBondingCurrCountersPtmRxLostStarts_Type = Counter64
_DslBondingCurrCountersPtmRxLostStarts_Object = MibTableColumn
dslBondingCurrCountersPtmRxLostStarts = _DslBondingCurrCountersPtmRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 10),
    _DslBondingCurrCountersPtmRxLostStarts_Type()
)
dslBondingCurrCountersPtmRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxLostStarts.setStatus("current")
_DslBondingCurrCountersPtmRxLostEnds_Type = Counter64
_DslBondingCurrCountersPtmRxLostEnds_Object = MibTableColumn
dslBondingCurrCountersPtmRxLostEnds = _DslBondingCurrCountersPtmRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 11),
    _DslBondingCurrCountersPtmRxLostEnds_Type()
)
dslBondingCurrCountersPtmRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmRxLostEnds.setStatus("current")
_DslBondingCurrCountersPtmTxPackets_Type = Counter64
_DslBondingCurrCountersPtmTxPackets_Object = MibTableColumn
dslBondingCurrCountersPtmTxPackets = _DslBondingCurrCountersPtmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 12),
    _DslBondingCurrCountersPtmTxPackets_Type()
)
dslBondingCurrCountersPtmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersPtmTxPackets.setStatus("current")
_DslBondingCurrCountersAtmTxCells_Type = Counter64
_DslBondingCurrCountersAtmTxCells_Object = MibTableColumn
dslBondingCurrCountersAtmTxCells = _DslBondingCurrCountersAtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 13),
    _DslBondingCurrCountersAtmTxCells_Type()
)
dslBondingCurrCountersAtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmTxCells.setStatus("current")
_DslBondingCurrCountersAtmRxCells_Type = Counter64
_DslBondingCurrCountersAtmRxCells_Object = MibTableColumn
dslBondingCurrCountersAtmRxCells = _DslBondingCurrCountersAtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 14),
    _DslBondingCurrCountersAtmRxCells_Type()
)
dslBondingCurrCountersAtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmRxCells.setStatus("current")
_DslBondingCurrCountersAtmNumFlushRequests_Type = Counter64
_DslBondingCurrCountersAtmNumFlushRequests_Object = MibTableColumn
dslBondingCurrCountersAtmNumFlushRequests = _DslBondingCurrCountersAtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 15),
    _DslBondingCurrCountersAtmNumFlushRequests_Type()
)
dslBondingCurrCountersAtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmNumFlushRequests.setStatus("current")
_DslBondingCurrCountersAtmNumTimeouts_Type = Counter64
_DslBondingCurrCountersAtmNumTimeouts_Object = MibTableColumn
dslBondingCurrCountersAtmNumTimeouts = _DslBondingCurrCountersAtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 16),
    _DslBondingCurrCountersAtmNumTimeouts_Type()
)
dslBondingCurrCountersAtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmNumTimeouts.setStatus("current")
_DslBondingCurrCountersAtmNumDirectSidResets_Type = Counter64
_DslBondingCurrCountersAtmNumDirectSidResets_Object = MibTableColumn
dslBondingCurrCountersAtmNumDirectSidResets = _DslBondingCurrCountersAtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 17),
    _DslBondingCurrCountersAtmNumDirectSidResets_Type()
)
dslBondingCurrCountersAtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmNumDirectSidResets.setStatus("current")
_DslBondingCurrCountersAtmNumDiscards_Type = Counter64
_DslBondingCurrCountersAtmNumDiscards_Object = MibTableColumn
dslBondingCurrCountersAtmNumDiscards = _DslBondingCurrCountersAtmNumDiscards_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 25, 1, 18),
    _DslBondingCurrCountersAtmNumDiscards_Type()
)
dslBondingCurrCountersAtmNumDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBondingCurrCountersAtmNumDiscards.setStatus("current")
_DslBonding15minCountersTable_Object = MibTable
dslBonding15minCountersTable = _DslBonding15minCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26)
)
if mibBuilder.loadTexts:
    dslBonding15minCountersTable.setStatus("current")
_DslBonding15minCountersEntry_Object = MibTableRow
dslBonding15minCountersEntry = _DslBonding15minCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1)
)
dslBonding15minCountersEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dslBonding15minCountersGroupName"),
)
if mibBuilder.loadTexts:
    dslBonding15minCountersEntry.setStatus("current")
_DslBonding15minCountersGroupName_Type = DisplayString
_DslBonding15minCountersGroupName_Object = MibTableColumn
dslBonding15minCountersGroupName = _DslBonding15minCountersGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 1),
    _DslBonding15minCountersGroupName_Type()
)
dslBonding15minCountersGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersGroupName.setStatus("current")
_DslBonding15minCountersElapsed_Type = Integer32
_DslBonding15minCountersElapsed_Object = MibTableColumn
dslBonding15minCountersElapsed = _DslBonding15minCountersElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 2),
    _DslBonding15minCountersElapsed_Type()
)
dslBonding15minCountersElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersElapsed.setStatus("current")
_DslBonding15minCountersPtmRxPackets_Type = Counter64
_DslBonding15minCountersPtmRxPackets_Object = MibTableColumn
dslBonding15minCountersPtmRxPackets = _DslBonding15minCountersPtmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 3),
    _DslBonding15minCountersPtmRxPackets_Type()
)
dslBonding15minCountersPtmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxPackets.setStatus("current")
_DslBonding15minCountersPtmNumFlushRequests_Type = Counter64
_DslBonding15minCountersPtmNumFlushRequests_Object = MibTableColumn
dslBonding15minCountersPtmNumFlushRequests = _DslBonding15minCountersPtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 4),
    _DslBonding15minCountersPtmNumFlushRequests_Type()
)
dslBonding15minCountersPtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmNumFlushRequests.setStatus("current")
_DslBonding15minCountersPtmNumTimeouts_Type = Counter64
_DslBonding15minCountersPtmNumTimeouts_Object = MibTableColumn
dslBonding15minCountersPtmNumTimeouts = _DslBonding15minCountersPtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 5),
    _DslBonding15minCountersPtmNumTimeouts_Type()
)
dslBonding15minCountersPtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmNumTimeouts.setStatus("current")
_DslBonding15minCountersPtmNumDirectSidResets_Type = Counter64
_DslBonding15minCountersPtmNumDirectSidResets_Object = MibTableColumn
dslBonding15minCountersPtmNumDirectSidResets = _DslBonding15minCountersPtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 6),
    _DslBonding15minCountersPtmNumDirectSidResets_Type()
)
dslBonding15minCountersPtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmNumDirectSidResets.setStatus("current")
_DslBonding15minCountersPtmRxSmallFragments_Type = Counter64
_DslBonding15minCountersPtmRxSmallFragments_Object = MibTableColumn
dslBonding15minCountersPtmRxSmallFragments = _DslBonding15minCountersPtmRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 7),
    _DslBonding15minCountersPtmRxSmallFragments_Type()
)
dslBonding15minCountersPtmRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxSmallFragments.setStatus("current")
_DslBonding15minCountersPtmRxLargeFragments_Type = Counter64
_DslBonding15minCountersPtmRxLargeFragments_Object = MibTableColumn
dslBonding15minCountersPtmRxLargeFragments = _DslBonding15minCountersPtmRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 8),
    _DslBonding15minCountersPtmRxLargeFragments_Type()
)
dslBonding15minCountersPtmRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxLargeFragments.setStatus("current")
_DslBonding15minCountersPtmRxBadFragments_Type = Counter64
_DslBonding15minCountersPtmRxBadFragments_Object = MibTableColumn
dslBonding15minCountersPtmRxBadFragments = _DslBonding15minCountersPtmRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 9),
    _DslBonding15minCountersPtmRxBadFragments_Type()
)
dslBonding15minCountersPtmRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxBadFragments.setStatus("current")
_DslBonding15minCountersPtmRxLostFragments_Type = Counter64
_DslBonding15minCountersPtmRxLostFragments_Object = MibTableColumn
dslBonding15minCountersPtmRxLostFragments = _DslBonding15minCountersPtmRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 10),
    _DslBonding15minCountersPtmRxLostFragments_Type()
)
dslBonding15minCountersPtmRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxLostFragments.setStatus("current")
_DslBonding15minCountersPtmRxLostStarts_Type = Counter64
_DslBonding15minCountersPtmRxLostStarts_Object = MibTableColumn
dslBonding15minCountersPtmRxLostStarts = _DslBonding15minCountersPtmRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 11),
    _DslBonding15minCountersPtmRxLostStarts_Type()
)
dslBonding15minCountersPtmRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxLostStarts.setStatus("current")
_DslBonding15minCountersPtmRxLostEnds_Type = Counter64
_DslBonding15minCountersPtmRxLostEnds_Object = MibTableColumn
dslBonding15minCountersPtmRxLostEnds = _DslBonding15minCountersPtmRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 12),
    _DslBonding15minCountersPtmRxLostEnds_Type()
)
dslBonding15minCountersPtmRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmRxLostEnds.setStatus("current")
_DslBonding15minCountersPtmTxPackets_Type = Counter64
_DslBonding15minCountersPtmTxPackets_Object = MibTableColumn
dslBonding15minCountersPtmTxPackets = _DslBonding15minCountersPtmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 13),
    _DslBonding15minCountersPtmTxPackets_Type()
)
dslBonding15minCountersPtmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersPtmTxPackets.setStatus("current")
_DslBonding15minCountersAtmTxCells_Type = Counter64
_DslBonding15minCountersAtmTxCells_Object = MibTableColumn
dslBonding15minCountersAtmTxCells = _DslBonding15minCountersAtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 14),
    _DslBonding15minCountersAtmTxCells_Type()
)
dslBonding15minCountersAtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmTxCells.setStatus("current")
_DslBonding15minCountersAtmRxCells_Type = Counter64
_DslBonding15minCountersAtmRxCells_Object = MibTableColumn
dslBonding15minCountersAtmRxCells = _DslBonding15minCountersAtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 15),
    _DslBonding15minCountersAtmRxCells_Type()
)
dslBonding15minCountersAtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmRxCells.setStatus("current")
_DslBonding15minCountersAtmNumFlushRequests_Type = Counter64
_DslBonding15minCountersAtmNumFlushRequests_Object = MibTableColumn
dslBonding15minCountersAtmNumFlushRequests = _DslBonding15minCountersAtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 16),
    _DslBonding15minCountersAtmNumFlushRequests_Type()
)
dslBonding15minCountersAtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmNumFlushRequests.setStatus("current")
_DslBonding15minCountersAtmNumTimeouts_Type = Counter64
_DslBonding15minCountersAtmNumTimeouts_Object = MibTableColumn
dslBonding15minCountersAtmNumTimeouts = _DslBonding15minCountersAtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 17),
    _DslBonding15minCountersAtmNumTimeouts_Type()
)
dslBonding15minCountersAtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmNumTimeouts.setStatus("current")
_DslBonding15minCountersAtmNumDirectSidResets_Type = Counter64
_DslBonding15minCountersAtmNumDirectSidResets_Object = MibTableColumn
dslBonding15minCountersAtmNumDirectSidResets = _DslBonding15minCountersAtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 18),
    _DslBonding15minCountersAtmNumDirectSidResets_Type()
)
dslBonding15minCountersAtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmNumDirectSidResets.setStatus("current")
_DslBonding15minCountersAtmNumDiscards_Type = Counter64
_DslBonding15minCountersAtmNumDiscards_Object = MibTableColumn
dslBonding15minCountersAtmNumDiscards = _DslBonding15minCountersAtmNumDiscards_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 26, 1, 19),
    _DslBonding15minCountersAtmNumDiscards_Type()
)
dslBonding15minCountersAtmNumDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding15minCountersAtmNumDiscards.setStatus("current")
_DslBonding1dayCountersTable_Object = MibTable
dslBonding1dayCountersTable = _DslBonding1dayCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27)
)
if mibBuilder.loadTexts:
    dslBonding1dayCountersTable.setStatus("current")
_DslBonding1dayCountersEntry_Object = MibTableRow
dslBonding1dayCountersEntry = _DslBonding1dayCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1)
)
dslBonding1dayCountersEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dslBonding1dayCountersGroupName"),
)
if mibBuilder.loadTexts:
    dslBonding1dayCountersEntry.setStatus("current")
_DslBonding1dayCountersGroupName_Type = DisplayString
_DslBonding1dayCountersGroupName_Object = MibTableColumn
dslBonding1dayCountersGroupName = _DslBonding1dayCountersGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 1),
    _DslBonding1dayCountersGroupName_Type()
)
dslBonding1dayCountersGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersGroupName.setStatus("current")
_DslBonding1dayCountersElapsed_Type = Integer32
_DslBonding1dayCountersElapsed_Object = MibTableColumn
dslBonding1dayCountersElapsed = _DslBonding1dayCountersElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 2),
    _DslBonding1dayCountersElapsed_Type()
)
dslBonding1dayCountersElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersElapsed.setStatus("current")
_DslBonding1dayCountersPtmRxPackets_Type = Counter64
_DslBonding1dayCountersPtmRxPackets_Object = MibTableColumn
dslBonding1dayCountersPtmRxPackets = _DslBonding1dayCountersPtmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 3),
    _DslBonding1dayCountersPtmRxPackets_Type()
)
dslBonding1dayCountersPtmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxPackets.setStatus("current")
_DslBonding1dayCountersPtmNumFlushRequests_Type = Counter64
_DslBonding1dayCountersPtmNumFlushRequests_Object = MibTableColumn
dslBonding1dayCountersPtmNumFlushRequests = _DslBonding1dayCountersPtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 4),
    _DslBonding1dayCountersPtmNumFlushRequests_Type()
)
dslBonding1dayCountersPtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmNumFlushRequests.setStatus("current")
_DslBonding1dayCountersPtmNumTimeouts_Type = Counter64
_DslBonding1dayCountersPtmNumTimeouts_Object = MibTableColumn
dslBonding1dayCountersPtmNumTimeouts = _DslBonding1dayCountersPtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 5),
    _DslBonding1dayCountersPtmNumTimeouts_Type()
)
dslBonding1dayCountersPtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmNumTimeouts.setStatus("current")
_DslBonding1dayCountersPtmNumDirectSidResets_Type = Counter64
_DslBonding1dayCountersPtmNumDirectSidResets_Object = MibTableColumn
dslBonding1dayCountersPtmNumDirectSidResets = _DslBonding1dayCountersPtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 6),
    _DslBonding1dayCountersPtmNumDirectSidResets_Type()
)
dslBonding1dayCountersPtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmNumDirectSidResets.setStatus("current")
_DslBonding1dayCountersPtmRxSmallFragments_Type = Counter64
_DslBonding1dayCountersPtmRxSmallFragments_Object = MibTableColumn
dslBonding1dayCountersPtmRxSmallFragments = _DslBonding1dayCountersPtmRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 7),
    _DslBonding1dayCountersPtmRxSmallFragments_Type()
)
dslBonding1dayCountersPtmRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxSmallFragments.setStatus("current")
_DslBonding1dayCountersPtmRxLargeFragments_Type = Counter64
_DslBonding1dayCountersPtmRxLargeFragments_Object = MibTableColumn
dslBonding1dayCountersPtmRxLargeFragments = _DslBonding1dayCountersPtmRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 8),
    _DslBonding1dayCountersPtmRxLargeFragments_Type()
)
dslBonding1dayCountersPtmRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxLargeFragments.setStatus("current")
_DslBonding1dayCountersPtmRxBadFragments_Type = Counter64
_DslBonding1dayCountersPtmRxBadFragments_Object = MibTableColumn
dslBonding1dayCountersPtmRxBadFragments = _DslBonding1dayCountersPtmRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 9),
    _DslBonding1dayCountersPtmRxBadFragments_Type()
)
dslBonding1dayCountersPtmRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxBadFragments.setStatus("current")
_DslBonding1dayCountersPtmRxLostFragments_Type = Counter64
_DslBonding1dayCountersPtmRxLostFragments_Object = MibTableColumn
dslBonding1dayCountersPtmRxLostFragments = _DslBonding1dayCountersPtmRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 10),
    _DslBonding1dayCountersPtmRxLostFragments_Type()
)
dslBonding1dayCountersPtmRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxLostFragments.setStatus("current")
_DslBonding1dayCountersPtmRxLostStarts_Type = Counter64
_DslBonding1dayCountersPtmRxLostStarts_Object = MibTableColumn
dslBonding1dayCountersPtmRxLostStarts = _DslBonding1dayCountersPtmRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 11),
    _DslBonding1dayCountersPtmRxLostStarts_Type()
)
dslBonding1dayCountersPtmRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxLostStarts.setStatus("current")
_DslBonding1dayCountersPtmRxLostEnds_Type = Counter64
_DslBonding1dayCountersPtmRxLostEnds_Object = MibTableColumn
dslBonding1dayCountersPtmRxLostEnds = _DslBonding1dayCountersPtmRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 12),
    _DslBonding1dayCountersPtmRxLostEnds_Type()
)
dslBonding1dayCountersPtmRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmRxLostEnds.setStatus("current")
_DslBonding1dayCountersPtmTxPackets_Type = Counter64
_DslBonding1dayCountersPtmTxPackets_Object = MibTableColumn
dslBonding1dayCountersPtmTxPackets = _DslBonding1dayCountersPtmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 13),
    _DslBonding1dayCountersPtmTxPackets_Type()
)
dslBonding1dayCountersPtmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersPtmTxPackets.setStatus("current")
_DslBonding1dayCountersAtmTxCells_Type = Counter64
_DslBonding1dayCountersAtmTxCells_Object = MibTableColumn
dslBonding1dayCountersAtmTxCells = _DslBonding1dayCountersAtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 14),
    _DslBonding1dayCountersAtmTxCells_Type()
)
dslBonding1dayCountersAtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmTxCells.setStatus("current")
_DslBonding1dayCountersAtmRxCells_Type = Counter64
_DslBonding1dayCountersAtmRxCells_Object = MibTableColumn
dslBonding1dayCountersAtmRxCells = _DslBonding1dayCountersAtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 15),
    _DslBonding1dayCountersAtmRxCells_Type()
)
dslBonding1dayCountersAtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmRxCells.setStatus("current")
_DslBonding1dayCountersAtmNumFlushRequests_Type = Counter64
_DslBonding1dayCountersAtmNumFlushRequests_Object = MibTableColumn
dslBonding1dayCountersAtmNumFlushRequests = _DslBonding1dayCountersAtmNumFlushRequests_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 16),
    _DslBonding1dayCountersAtmNumFlushRequests_Type()
)
dslBonding1dayCountersAtmNumFlushRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmNumFlushRequests.setStatus("current")
_DslBonding1dayCountersAtmNumTimeouts_Type = Counter64
_DslBonding1dayCountersAtmNumTimeouts_Object = MibTableColumn
dslBonding1dayCountersAtmNumTimeouts = _DslBonding1dayCountersAtmNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 17),
    _DslBonding1dayCountersAtmNumTimeouts_Type()
)
dslBonding1dayCountersAtmNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmNumTimeouts.setStatus("current")
_DslBonding1dayCountersAtmNumDirectSidResets_Type = Counter64
_DslBonding1dayCountersAtmNumDirectSidResets_Object = MibTableColumn
dslBonding1dayCountersAtmNumDirectSidResets = _DslBonding1dayCountersAtmNumDirectSidResets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 18),
    _DslBonding1dayCountersAtmNumDirectSidResets_Type()
)
dslBonding1dayCountersAtmNumDirectSidResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmNumDirectSidResets.setStatus("current")
_DslBonding1dayCountersAtmNumDiscards_Type = Counter64
_DslBonding1dayCountersAtmNumDiscards_Object = MibTableColumn
dslBonding1dayCountersAtmNumDiscards = _DslBonding1dayCountersAtmNumDiscards_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 22, 27, 1, 19),
    _DslBonding1dayCountersAtmNumDiscards_Type()
)
dslBonding1dayCountersAtmNumDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslBonding1dayCountersAtmNumDiscards.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26)
)


class _SyslogEnable_Type(Integer32):
    """Custom type syslogEnable based on Integer32"""
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


_SyslogEnable_Type.__name__ = "Integer32"
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 1),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("current")
_SyslogServerIpTable_Object = MibTable
syslogServerIpTable = _SyslogServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 2)
)
if mibBuilder.loadTexts:
    syslogServerIpTable.setStatus("current")
_SyslogServerIpEntry_Object = MibTableRow
syslogServerIpEntry = _SyslogServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 2, 1)
)
syslogServerIpEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "syslogServerIpIndex"),
)
if mibBuilder.loadTexts:
    syslogServerIpEntry.setStatus("current")


class _SyslogServerIpIndex_Type(Integer32):
    """Custom type syslogServerIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SyslogServerIpIndex_Type.__name__ = "Integer32"
_SyslogServerIpIndex_Object = MibTableColumn
syslogServerIpIndex = _SyslogServerIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 2, 1, 1),
    _SyslogServerIpIndex_Type()
)
syslogServerIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServerIpIndex.setStatus("current")


class _SyslogServerIpAddressType_Type(InetAddressType):
    """Custom type syslogServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_SyslogServerIpAddressType_Type.__name__ = "InetAddressType"
_SyslogServerIpAddressType_Object = MibTableColumn
syslogServerIpAddressType = _SyslogServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 2, 1, 2),
    _SyslogServerIpAddressType_Type()
)
syslogServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIpAddressType.setStatus("current")
_SyslogServerIpAddress_Type = InetAddress
_SyslogServerIpAddress_Object = MibTableColumn
syslogServerIpAddress = _SyslogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 26, 2, 1, 3),
    _SyslogServerIpAddress_Type()
)
syslogServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIpAddress.setStatus("current")
_Dot3ad_ObjectIdentity = ObjectIdentity
dot3ad = _Dot3ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27)
)
_Dot3adTable_Object = MibTable
dot3adTable = _Dot3adTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1)
)
if mibBuilder.loadTexts:
    dot3adTable.setStatus("current")
_Dot3adEntry_Object = MibTableRow
dot3adEntry = _Dot3adEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1, 1)
)
dot3adEntry.setIndexNames(
    (0, "VES1724-58V-MIB", "dot3adGroupId"),
)
if mibBuilder.loadTexts:
    dot3adEntry.setStatus("current")
_Dot3adGroupId_Type = Integer32
_Dot3adGroupId_Object = MibTableColumn
dot3adGroupId = _Dot3adGroupId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1, 1, 1),
    _Dot3adGroupId_Type()
)
dot3adGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adGroupId.setStatus("current")


class _Dot3adEnable_Type(Integer32):
    """Custom type dot3adEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("enableWithLacp", 2),
          ("disable", 3))
    )


_Dot3adEnable_Type.__name__ = "Integer32"
_Dot3adEnable_Object = MibTableColumn
dot3adEnable = _Dot3adEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1, 1, 2),
    _Dot3adEnable_Type()
)
dot3adEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adEnable.setStatus("current")
_Dot3adGroupName_Type = DisplayString
_Dot3adGroupName_Object = MibTableColumn
dot3adGroupName = _Dot3adGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1, 1, 3),
    _Dot3adGroupName_Type()
)
dot3adGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adGroupName.setStatus("current")
_Dot3adGroupPortList_Type = PortList
_Dot3adGroupPortList_Object = MibTableColumn
dot3adGroupPortList = _Dot3adGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 1, 1, 4),
    _Dot3adGroupPortList_Type()
)
dot3adGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adGroupPortList.setStatus("current")


class _LacpPriority_Type(Integer32):
    """Custom type lacpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LacpPriority_Type.__name__ = "Integer32"
_LacpPriority_Object = MibScalar
lacpPriority = _LacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 2),
    _LacpPriority_Type()
)
lacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPriority.setStatus("current")


class _LacpTimeout_Type(Integer32):
    """Custom type lacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shorttimeout", 1),
          ("longtimeout", 2))
    )


_LacpTimeout_Type.__name__ = "Integer32"
_LacpTimeout_Object = MibScalar
lacpTimeout = _LacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 3),
    _LacpTimeout_Type()
)
lacpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpTimeout.setStatus("current")
_Dot3adStatus_ObjectIdentity = ObjectIdentity
dot3adStatus = _Dot3adStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4)
)


class _Actor_Type(PhysAddress):
    """Custom type actor based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Actor_Type.__name__ = "PhysAddress"
_Actor_Object = MibScalar
actor = _Actor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 1),
    _Actor_Type()
)
actor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actor.setStatus("current")
_ActorPriority_Type = Integer32
_ActorPriority_Object = MibScalar
actorPriority = _ActorPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 2),
    _ActorPriority_Type()
)
actorPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorPriority.setStatus("current")
_ActorKey_Type = Integer32
_ActorKey_Object = MibScalar
actorKey = _ActorKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 3),
    _ActorKey_Type()
)
actorKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorKey.setStatus("current")


class _Partner_Type(PhysAddress):
    """Custom type partner based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Partner_Type.__name__ = "PhysAddress"
_Partner_Object = MibScalar
partner = _Partner_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 4),
    _Partner_Type()
)
partner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partner.setStatus("current")
_PartnerPriority_Type = Integer32
_PartnerPriority_Object = MibScalar
partnerPriority = _PartnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 5),
    _PartnerPriority_Type()
)
partnerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerPriority.setStatus("current")
_PartnerKey_Type = Integer32
_PartnerKey_Object = MibScalar
partnerKey = _PartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 6),
    _PartnerKey_Type()
)
partnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerKey.setStatus("current")


class _Links_Type(DisplayString):
    """Custom type links based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Links_Type.__name__ = "DisplayString"
_Links_Object = MibScalar
links = _Links_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 7),
    _Links_Type()
)
links.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    links.setStatus("current")


class _Syncs_Type(DisplayString):
    """Custom type syncs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Syncs_Type.__name__ = "DisplayString"
_Syncs_Object = MibScalar
syncs = _Syncs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 4, 8),
    _Syncs_Type()
)
syncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncs.setStatus("current")
_Dot3adStatistic_ObjectIdentity = ObjectIdentity
dot3adStatistic = _Dot3adStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5)
)
_Dot3adStatisticTxUtilization_Type = Unsigned32
_Dot3adStatisticTxUtilization_Object = MibScalar
dot3adStatisticTxUtilization = _Dot3adStatisticTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 1),
    _Dot3adStatisticTxUtilization_Type()
)
dot3adStatisticTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticTxUtilization.setStatus("current")
_Dot3adStatisticTxSpeed_Type = Unsigned32
_Dot3adStatisticTxSpeed_Object = MibScalar
dot3adStatisticTxSpeed = _Dot3adStatisticTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 2),
    _Dot3adStatisticTxSpeed_Type()
)
dot3adStatisticTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticTxSpeed.setStatus("current")
_Dot3adStatisticRxUtilization_Type = Unsigned32
_Dot3adStatisticRxUtilization_Object = MibScalar
dot3adStatisticRxUtilization = _Dot3adStatisticRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 3),
    _Dot3adStatisticRxUtilization_Type()
)
dot3adStatisticRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxUtilization.setStatus("current")
_Dot3adStatisticRxSpeed_Type = Unsigned32
_Dot3adStatisticRxSpeed_Object = MibScalar
dot3adStatisticRxSpeed = _Dot3adStatisticRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 4),
    _Dot3adStatisticRxSpeed_Type()
)
dot3adStatisticRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxSpeed.setStatus("current")
_Dot3adStatisticsTxOctet_Type = Counter64
_Dot3adStatisticsTxOctet_Object = MibScalar
dot3adStatisticsTxOctet = _Dot3adStatisticsTxOctet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 5),
    _Dot3adStatisticsTxOctet_Type()
)
dot3adStatisticsTxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticsTxOctet.setStatus("current")
_Dot3adStatisticTxPkts_Type = Counter64
_Dot3adStatisticTxPkts_Object = MibScalar
dot3adStatisticTxPkts = _Dot3adStatisticTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 6),
    _Dot3adStatisticTxPkts_Type()
)
dot3adStatisticTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticTxPkts.setStatus("current")
_Dot3adStatisticTxBroadcastPkts_Type = Counter64
_Dot3adStatisticTxBroadcastPkts_Object = MibScalar
dot3adStatisticTxBroadcastPkts = _Dot3adStatisticTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 7),
    _Dot3adStatisticTxBroadcastPkts_Type()
)
dot3adStatisticTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticTxBroadcastPkts.setStatus("current")
_Dot3adStatisticTxMulticastPkts_Type = Counter64
_Dot3adStatisticTxMulticastPkts_Object = MibScalar
dot3adStatisticTxMulticastPkts = _Dot3adStatisticTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 8),
    _Dot3adStatisticTxMulticastPkts_Type()
)
dot3adStatisticTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticTxMulticastPkts.setStatus("current")
_Dot3adStatisticRxOctets_Type = Counter64
_Dot3adStatisticRxOctets_Object = MibScalar
dot3adStatisticRxOctets = _Dot3adStatisticRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 9),
    _Dot3adStatisticRxOctets_Type()
)
dot3adStatisticRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxOctets.setStatus("current")
_Dot3adStatisticRxPkts_Type = Counter64
_Dot3adStatisticRxPkts_Object = MibScalar
dot3adStatisticRxPkts = _Dot3adStatisticRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 10),
    _Dot3adStatisticRxPkts_Type()
)
dot3adStatisticRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxPkts.setStatus("current")
_Dot3adStatisticRxBroadcastPkts_Type = Counter64
_Dot3adStatisticRxBroadcastPkts_Object = MibScalar
dot3adStatisticRxBroadcastPkts = _Dot3adStatisticRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 11),
    _Dot3adStatisticRxBroadcastPkts_Type()
)
dot3adStatisticRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxBroadcastPkts.setStatus("current")
_Dot3adStatisticRxMulticastPkts_Type = Counter64
_Dot3adStatisticRxMulticastPkts_Object = MibScalar
dot3adStatisticRxMulticastPkts = _Dot3adStatisticRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 12),
    _Dot3adStatisticRxMulticastPkts_Type()
)
dot3adStatisticRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxMulticastPkts.setStatus("current")
_Dot3adStatisticRxCRCAlignErrors_Type = Counter64
_Dot3adStatisticRxCRCAlignErrors_Object = MibScalar
dot3adStatisticRxCRCAlignErrors = _Dot3adStatisticRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 13),
    _Dot3adStatisticRxCRCAlignErrors_Type()
)
dot3adStatisticRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxCRCAlignErrors.setStatus("current")
_Dot3adStatisticRxUndersizePkts_Type = Counter64
_Dot3adStatisticRxUndersizePkts_Object = MibScalar
dot3adStatisticRxUndersizePkts = _Dot3adStatisticRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 14),
    _Dot3adStatisticRxUndersizePkts_Type()
)
dot3adStatisticRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxUndersizePkts.setStatus("current")
_Dot3adStatisticRxOversizePkts_Type = Counter64
_Dot3adStatisticRxOversizePkts_Object = MibScalar
dot3adStatisticRxOversizePkts = _Dot3adStatisticRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 15),
    _Dot3adStatisticRxOversizePkts_Type()
)
dot3adStatisticRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxOversizePkts.setStatus("current")
_Dot3adStatisticRxFragments_Type = Counter64
_Dot3adStatisticRxFragments_Object = MibScalar
dot3adStatisticRxFragments = _Dot3adStatisticRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 16),
    _Dot3adStatisticRxFragments_Type()
)
dot3adStatisticRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticRxFragments.setStatus("current")
_Dot3adStatisticCollisions_Type = Counter64
_Dot3adStatisticCollisions_Object = MibScalar
dot3adStatisticCollisions = _Dot3adStatisticCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 17),
    _Dot3adStatisticCollisions_Type()
)
dot3adStatisticCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticCollisions.setStatus("current")
_Dot3adStatisticPkts64Octets_Type = Counter64
_Dot3adStatisticPkts64Octets_Object = MibScalar
dot3adStatisticPkts64Octets = _Dot3adStatisticPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 18),
    _Dot3adStatisticPkts64Octets_Type()
)
dot3adStatisticPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts64Octets.setStatus("current")
_Dot3adStatisticPkts65to127Octets_Type = Counter64
_Dot3adStatisticPkts65to127Octets_Object = MibScalar
dot3adStatisticPkts65to127Octets = _Dot3adStatisticPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 19),
    _Dot3adStatisticPkts65to127Octets_Type()
)
dot3adStatisticPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts65to127Octets.setStatus("current")
_Dot3adStatisticPkts128to255Octets_Type = Counter64
_Dot3adStatisticPkts128to255Octets_Object = MibScalar
dot3adStatisticPkts128to255Octets = _Dot3adStatisticPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 20),
    _Dot3adStatisticPkts128to255Octets_Type()
)
dot3adStatisticPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts128to255Octets.setStatus("current")
_Dot3adStatisticPkts256to511Octets_Type = Counter64
_Dot3adStatisticPkts256to511Octets_Object = MibScalar
dot3adStatisticPkts256to511Octets = _Dot3adStatisticPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 21),
    _Dot3adStatisticPkts256to511Octets_Type()
)
dot3adStatisticPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts256to511Octets.setStatus("current")
_Dot3adStatisticPkts512to1023Octets_Type = Counter64
_Dot3adStatisticPkts512to1023Octets_Object = MibScalar
dot3adStatisticPkts512to1023Octets = _Dot3adStatisticPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 22),
    _Dot3adStatisticPkts512to1023Octets_Type()
)
dot3adStatisticPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts512to1023Octets.setStatus("current")
_Dot3adStatisticPkts1024to1518Octets_Type = Counter64
_Dot3adStatisticPkts1024to1518Octets_Object = MibScalar
dot3adStatisticPkts1024to1518Octets = _Dot3adStatisticPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 23),
    _Dot3adStatisticPkts1024to1518Octets_Type()
)
dot3adStatisticPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts1024to1518Octets.setStatus("current")
_Dot3adStatisticPkts1519to1522Octets_Type = Counter64
_Dot3adStatisticPkts1519to1522Octets_Object = MibScalar
dot3adStatisticPkts1519to1522Octets = _Dot3adStatisticPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 24),
    _Dot3adStatisticPkts1519to1522Octets_Type()
)
dot3adStatisticPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adStatisticPkts1519to1522Octets.setStatus("current")


class _Dot3adStatisticOperation_Type(Integer32):
    """Custom type dot3adStatisticOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Dot3adStatisticOperation_Type.__name__ = "Integer32"
_Dot3adStatisticOperation_Object = MibScalar
dot3adStatisticOperation = _Dot3adStatisticOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 5, 25),
    _Dot3adStatisticOperation_Type()
)
dot3adStatisticOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adStatisticOperation.setStatus("current")


class _LoadDistribution_Type(Integer32):
    """Custom type loadDistribution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("src-mac", 1),
          ("dst-mac", 2),
          ("src-dst-mac", 3),
          ("src-ip", 4),
          ("dst-ip", 5),
          ("src-dst-ip", 6),
          ("src-dst-ipmac", 7))
    )


_LoadDistribution_Type.__name__ = "Integer32"
_LoadDistribution_Object = MibScalar
loadDistribution = _LoadDistribution_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 27, 6),
    _LoadDistribution_Type()
)
loadDistribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadDistribution.setStatus("current")
_Daisychain_ObjectIdentity = ObjectIdentity
daisychain = _Daisychain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 29)
)
_DaisychainTable_Object = MibTable
daisychainTable = _DaisychainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 29, 1)
)
if mibBuilder.loadTexts:
    daisychainTable.setStatus("current")
_DaisychainEntry_Object = MibTableRow
daisychainEntry = _DaisychainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 29, 1, 1)
)
daisychainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    daisychainEntry.setStatus("current")


class _DaisychainMode_Type(Integer32):
    """Custom type daisychainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("daisychain", 2))
    )


_DaisychainMode_Type.__name__ = "Integer32"
_DaisychainMode_Object = MibTableColumn
daisychainMode = _DaisychainMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 29, 1, 1, 1),
    _DaisychainMode_Type()
)
daisychainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daisychainMode.setStatus("current")
_Smcast_ObjectIdentity = ObjectIdentity
smcast = _Smcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31)
)
_MaxNumberOfSmcastPortGroups_Type = Integer32
_MaxNumberOfSmcastPortGroups_Object = MibScalar
maxNumberOfSmcastPortGroups = _MaxNumberOfSmcastPortGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 1),
    _MaxNumberOfSmcastPortGroups_Type()
)
maxNumberOfSmcastPortGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfSmcastPortGroups.setStatus("current")
_SmcastPortTagGroupTable_Object = MibTable
smcastPortTagGroupTable = _SmcastPortTagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 2)
)
if mibBuilder.loadTexts:
    smcastPortTagGroupTable.setStatus("current")
_SmcastPortTagGroupEntry_Object = MibTableRow
smcastPortTagGroupEntry = _SmcastPortTagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 2, 1)
)
smcastPortTagGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "smcastPortTagGroupVid"),
    (0, "VES1724-58V-MIB", "smcastPortTagGroupMac"),
)
if mibBuilder.loadTexts:
    smcastPortTagGroupEntry.setStatus("current")


class _SmcastPortTagGroupVid_Type(VlanIndex):
    """Custom type smcastPortTagGroupVid based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_SmcastPortTagGroupVid_Type.__name__ = "VlanIndex"
_SmcastPortTagGroupVid_Object = MibTableColumn
smcastPortTagGroupVid = _SmcastPortTagGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 2, 1, 1),
    _SmcastPortTagGroupVid_Type()
)
smcastPortTagGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcastPortTagGroupVid.setStatus("current")


class _SmcastPortTagGroupMac_Type(PhysAddress):
    """Custom type smcastPortTagGroupMac based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SmcastPortTagGroupMac_Type.__name__ = "PhysAddress"
_SmcastPortTagGroupMac_Object = MibTableColumn
smcastPortTagGroupMac = _SmcastPortTagGroupMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 2, 1, 2),
    _SmcastPortTagGroupMac_Type()
)
smcastPortTagGroupMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcastPortTagGroupMac.setStatus("current")
_SmcastPortTagGroupRowStatus_Type = RowStatus
_SmcastPortTagGroupRowStatus_Object = MibTableColumn
smcastPortTagGroupRowStatus = _SmcastPortTagGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 2, 1, 3),
    _SmcastPortTagGroupRowStatus_Type()
)
smcastPortTagGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smcastPortTagGroupRowStatus.setStatus("current")
_SmcastPortUntagGroupTable_Object = MibTable
smcastPortUntagGroupTable = _SmcastPortUntagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 3)
)
if mibBuilder.loadTexts:
    smcastPortUntagGroupTable.setStatus("current")
_SmcastPortUntagGroupEntry_Object = MibTableRow
smcastPortUntagGroupEntry = _SmcastPortUntagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 3, 1)
)
smcastPortUntagGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VES1724-58V-MIB", "smcastPortUntagGroupMac"),
)
if mibBuilder.loadTexts:
    smcastPortUntagGroupEntry.setStatus("current")


class _SmcastPortUntagGroupMac_Type(PhysAddress):
    """Custom type smcastPortUntagGroupMac based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SmcastPortUntagGroupMac_Type.__name__ = "PhysAddress"
_SmcastPortUntagGroupMac_Object = MibTableColumn
smcastPortUntagGroupMac = _SmcastPortUntagGroupMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 3, 1, 1),
    _SmcastPortUntagGroupMac_Type()
)
smcastPortUntagGroupMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcastPortUntagGroupMac.setStatus("current")
_SmcastPortUntagGroupRowStatus_Type = RowStatus
_SmcastPortUntagGroupRowStatus_Object = MibTableColumn
smcastPortUntagGroupRowStatus = _SmcastPortUntagGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 31, 3, 1, 2),
    _SmcastPortUntagGroupRowStatus_Type()
)
smcastPortUntagGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smcastPortUntagGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VES1724-58V-MIB",
    **{"Xdsl2Unit": Xdsl2Unit,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "vesSeries": vesSeries,
       "ves1724-58v": ves1724_58v,
       "acl": acl,
       "aclMaxNumOfAclPerSystem": aclMaxNumOfAclPerSystem,
       "aclSystemTable": aclSystemTable,
       "aclSystemEntry": aclSystemEntry,
       "aclSystemProfileName": aclSystemProfileName,
       "aclSystemRowStaus": aclSystemRowStaus,
       "aclMaxNumOfAclPerPort": aclMaxNumOfAclPerPort,
       "aclPortTable": aclPortTable,
       "aclPortEntry": aclPortEntry,
       "aclPortProfileName": aclPortProfileName,
       "aclPortRowStatus": aclPortRowStatus,
       "aclMaxNumOfAclProfiles": aclMaxNumOfAclProfiles,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileName": aclProfileName,
       "aclProfileActionMask": aclProfileActionMask,
       "aclProfileFieldMask": aclProfileFieldMask,
       "aclProfileRuleEtype": aclProfileRuleEtype,
       "aclProfileRuleSrcMac": aclProfileRuleSrcMac,
       "aclProfileRuleDestMac": aclProfileRuleDestMac,
       "aclProfileRuleSrcOui": aclProfileRuleSrcOui,
       "aclProfileRuleDestOui": aclProfileRuleDestOui,
       "aclProfileRuleInnerVlan": aclProfileRuleInnerVlan,
       "aclProfileRuleOuterVlan": aclProfileRuleOuterVlan,
       "aclProfileRuleInnerPbit": aclProfileRuleInnerPbit,
       "aclProfileRuleOuterPbit": aclProfileRuleOuterPbit,
       "aclProfileRuleSrcIpRange": aclProfileRuleSrcIpRange,
       "aclProfileRuleSrcIpMask": aclProfileRuleSrcIpMask,
       "aclProfileRuleDestIpRange": aclProfileRuleDestIpRange,
       "aclProfileRuleDestIpMask": aclProfileRuleDestIpMask,
       "aclProfileRuleSrcIp": aclProfileRuleSrcIp,
       "aclProfileRuleDestIp": aclProfileRuleDestIp,
       "aclProfileRuleProtocol": aclProfileRuleProtocol,
       "aclProfileRuleIpPrecedence": aclProfileRuleIpPrecedence,
       "aclProfileRuleDscp": aclProfileRuleDscp,
       "aclProfileRuleSrcIpv6": aclProfileRuleSrcIpv6,
       "aclProfileRuleDestIpv6": aclProfileRuleDestIpv6,
       "aclProfileRuleNextHeader": aclProfileRuleNextHeader,
       "aclProfileRuleTrafficClass": aclProfileRuleTrafficClass,
       "aclProfileRuleSrcL4StartPort": aclProfileRuleSrcL4StartPort,
       "aclProfileRuleSrcL4EndPort": aclProfileRuleSrcL4EndPort,
       "aclProfileRuleDestL4StartPort": aclProfileRuleDestL4StartPort,
       "aclProfileRuleDestL4EndPort": aclProfileRuleDestL4EndPort,
       "aclProfileRuleSrcL4Port": aclProfileRuleSrcL4Port,
       "aclProfileRuleDestL4Port": aclProfileRuleDestL4Port,
       "aclProfileActionRate": aclProfileActionRate,
       "aclProfileActionInnerPbit": aclProfileActionInnerPbit,
       "aclProfileActionOuterPbit": aclProfileActionOuterPbit,
       "aclProfileActionDscp": aclProfileActionDscp,
       "aclProfileActionTrafficClass": aclProfileActionTrafficClass,
       "aclProfileActionQos": aclProfileActionQos,
       "aclProfileRowStatus": aclProfileRowStatus,
       "aclProfilePriority": aclProfilePriority,
       "aclMulticast": aclMulticast,
       "aclUnsolicited": aclUnsolicited,
       "aclUpstream": aclUpstream,
       "aclStormControl": aclStormControl,
       "aclBroadcast": aclBroadcast,
       "aclDlf": aclDlf,
       "dot1x": dot1x,
       "dot1xEnable": dot1xEnable,
       "dot1xAuthMethod": dot1xAuthMethod,
       "dot1xRadiusServerTable": dot1xRadiusServerTable,
       "dot1xRadiusServerEntry": dot1xRadiusServerEntry,
       "dot1xRadiusServerIndex": dot1xRadiusServerIndex,
       "dot1xRadiusServerIp": dot1xRadiusServerIp,
       "dot1xRadiusServerPort": dot1xRadiusServerPort,
       "dot1xRadiusServerSecret": dot1xRadiusServerSecret,
       "dot1xPortTable": dot1xPortTable,
       "dot1xPortEntry": dot1xPortEntry,
       "dot1xPortRadiusServerIndex": dot1xPortRadiusServerIndex,
       "dot1xPortEnable": dot1xPortEnable,
       "dot1xPortCircuitIDEnable": dot1xPortCircuitIDEnable,
       "dot1xPortCircuitIDInfo": dot1xPortCircuitIDInfo,
       "dot1xUserProfileTable": dot1xUserProfileTable,
       "dot1xUserProfileEntry": dot1xUserProfileEntry,
       "dot1xUserProfileName": dot1xUserProfileName,
       "dot1xUserProfilePassword": dot1xUserProfilePassword,
       "dot1xUserProfileRowStatus": dot1xUserProfileRowStatus,
       "dot1xStatsPortTable": dot1xStatsPortTable,
       "dot1xStatsPortEntry": dot1xStatsPortEntry,
       "dot1xStatsPortReAuthCount": dot1xStatsPortReAuthCount,
       "aclFieldPriorityTable": aclFieldPriorityTable,
       "aclFieldPriorityEntry": aclFieldPriorityEntry,
       "aclFieldPriorityIndex": aclFieldPriorityIndex,
       "aclFieldPriorityValue": aclFieldPriorityValue,
       "aclPacketTypeFilterTable": aclPacketTypeFilterTable,
       "aclPacketTypeFilterEntry": aclPacketTypeFilterEntry,
       "aclPacketTypeFilterVlanId": aclPacketTypeFilterVlanId,
       "aclPacketTypeFilterActionMask": aclPacketTypeFilterActionMask,
       "aclPacketTypeFilterRowStatus": aclPacketTypeFilterRowStatus,
       "alarm": alarm,
       "alarmOps": alarmOps,
       "curAlarmClearTargetTrapOid": curAlarmClearTargetTrapOid,
       "curAlarmClearTargetIndex1": curAlarmClearTargetIndex1,
       "curAlarmClearTargetIndex2": curAlarmClearTargetIndex2,
       "curAlarmClearTargetIndex3": curAlarmClearTargetIndex3,
       "alarmOperation": alarmOperation,
       "currAlarmTable": currAlarmTable,
       "currAlarmEntry": currAlarmEntry,
       "currAlarmIndex": currAlarmIndex,
       "currAlarmCondId": currAlarmCondId,
       "currAlarmOccurTime": currAlarmOccurTime,
       "currAlarmTrapOid": currAlarmTrapOid,
       "currAlarmParam1": currAlarmParam1,
       "currAlarmParam2": currAlarmParam2,
       "currAlarmParam3": currAlarmParam3,
       "currAlarmParam4": currAlarmParam4,
       "currAlarmParam5": currAlarmParam5,
       "currAlarmParam6": currAlarmParam6,
       "currAlarmParam7": currAlarmParam7,
       "currAlarmParam8": currAlarmParam8,
       "currAlarmParam9": currAlarmParam9,
       "currAlarmTimeDescr": currAlarmTimeDescr,
       "currAlarmSeverity": currAlarmSeverity,
       "currAlarmDescr": currAlarmDescr,
       "histAlarmTable": histAlarmTable,
       "histAlarmEntry": histAlarmEntry,
       "histAlarmIndex": histAlarmIndex,
       "histAlarmCondId": histAlarmCondId,
       "histAlarmOccurTime": histAlarmOccurTime,
       "histAlarmTrapOid": histAlarmTrapOid,
       "histAlarmParam1": histAlarmParam1,
       "histAlarmParam2": histAlarmParam2,
       "histAlarmParam3": histAlarmParam3,
       "histAlarmParam4": histAlarmParam4,
       "histAlarmParam5": histAlarmParam5,
       "histAlarmParam6": histAlarmParam6,
       "histAlarmParam7": histAlarmParam7,
       "histAlarmParam8": histAlarmParam8,
       "histAlarmParam9": histAlarmParam9,
       "histAlarmTimeDescr": histAlarmTimeDescr,
       "histAlarmSeverity": histAlarmSeverity,
       "histAlarmDescr": histAlarmDescr,
       "alarmConfTable": alarmConfTable,
       "alarmConfEntry": alarmConfEntry,
       "alarmConfTrapOid": alarmConfTrapOid,
       "alarmConfSeverity": alarmConfSeverity,
       "alarmConfLogFacility": alarmConfLogFacility,
       "alarmConfTarget": alarmConfTarget,
       "alarmSeveritySystem": alarmSeveritySystem,
       "alarmSeverityPortTable": alarmSeverityPortTable,
       "alarmSeverityPortEntry": alarmSeverityPortEntry,
       "alarmSeverityPortThresh": alarmSeverityPortThresh,
       "alarmControl": alarmControl,
       "sysAlarmSuppressEnable": sysAlarmSuppressEnable,
       "externalAlarmTable": externalAlarmTable,
       "externalAlarmEntry": externalAlarmEntry,
       "externalAlarmIndex": externalAlarmIndex,
       "externalAlarmName": externalAlarmName,
       "dhcp": dhcp,
       "dhcpL2agTable": dhcpL2agTable,
       "dhcpL2agEntry": dhcpL2agEntry,
       "dhcpL2agVlanId": dhcpL2agVlanId,
       "dhcpL2agMode": dhcpL2agMode,
       "dhcpL2agLdraEnable": dhcpL2agLdraEnable,
       "dhcpL2agOpt18CircuitIDEnable": dhcpL2agOpt18CircuitIDEnable,
       "dhcpL2agOpt18CircuitIDInfo": dhcpL2agOpt18CircuitIDInfo,
       "dhcpL2agOpt37RemoteIDEnable": dhcpL2agOpt37RemoteIDEnable,
       "dhcpL2agOpt37RemoteIDInfo": dhcpL2agOpt37RemoteIDInfo,
       "dhcpL2agOpt82CircuitIDEnable": dhcpL2agOpt82CircuitIDEnable,
       "dhcpL2agOpt82CircuitIDInfo": dhcpL2agOpt82CircuitIDInfo,
       "dhcpL2agOpt82RemoteIDEnable": dhcpL2agOpt82RemoteIDEnable,
       "dhcpL2agOpt82RemoteIDInfo": dhcpL2agOpt82RemoteIDInfo,
       "dhcpL2agRowStatus": dhcpL2agRowStatus,
       "dhcpSnoop": dhcpSnoop,
       "dhcpSnoopPortTable": dhcpSnoopPortTable,
       "dhcpSnoopPortEntry": dhcpSnoopPortEntry,
       "dhcpSnoopPortIpMacBindingEnable": dhcpSnoopPortIpMacBindingEnable,
       "dhcpSnoopPortMaxLeaseCount": dhcpSnoopPortMaxLeaseCount,
       "dhcpSnoopPortDbFlush": dhcpSnoopPortDbFlush,
       "dhcpSnoopOverflowMode": dhcpSnoopOverflowMode,
       "dhcpSnoopDbTable": dhcpSnoopDbTable,
       "dhcpSnoopDbEntry": dhcpSnoopDbEntry,
       "dhcpSnoopDbIpType": dhcpSnoopDbIpType,
       "dhcpSnoopDbIp": dhcpSnoopDbIp,
       "dhcpSnoopDbVid": dhcpSnoopDbVid,
       "dhcpSnoopDbMac": dhcpSnoopDbMac,
       "dhcpSnoopStatsTable": dhcpSnoopStatsTable,
       "dhcpSnoopStatsEntry": dhcpSnoopStatsEntry,
       "dhcpSnoopStatsOverFlow": dhcpSnoopStatsOverFlow,
       "dhcpSnoopStatsV4Discover": dhcpSnoopStatsV4Discover,
       "dhcpSnoopStatsV4Offer": dhcpSnoopStatsV4Offer,
       "dhcpSnoopStatsV4Request": dhcpSnoopStatsV4Request,
       "dhcpSnoopStatsV4Ack": dhcpSnoopStatsV4Ack,
       "dhcpSnoopStatsV4Release": dhcpSnoopStatsV4Release,
       "dhcpSnoopStatsV6Solicit": dhcpSnoopStatsV6Solicit,
       "dhcpSnoopStatsV6Advertise": dhcpSnoopStatsV6Advertise,
       "dhcpSnoopStatsV6Request": dhcpSnoopStatsV6Request,
       "dhcpSnoopStatsV6Reply": dhcpSnoopStatsV6Reply,
       "dhcpSnoopStatsV6Renew": dhcpSnoopStatsV6Renew,
       "dhcpSnoopStatsV6Rebind": dhcpSnoopStatsV6Rebind,
       "dhcpSnoopStatsV6Release": dhcpSnoopStatsV6Release,
       "dhcpSnoopStatsV6RelayForward": dhcpSnoopStatsV6RelayForward,
       "dhcpSnoopStatsV6RelayReply": dhcpSnoopStatsV6RelayReply,
       "dhcpSnoopStatsClear": dhcpSnoopStatsClear,
       "dhcpTest": dhcpTest,
       "dhcpTestPort": dhcpTestPort,
       "dhcpTestChannel": dhcpTestChannel,
       "dhcpTestUniVlanMode": dhcpTestUniVlanMode,
       "dhcpTestUniVlan": dhcpTestUniVlan,
       "dhcpTestType": dhcpTestType,
       "dhcpTestOps": dhcpTestOps,
       "dhcpTestStatus": dhcpTestStatus,
       "ge": ge,
       "geConfTable": geConfTable,
       "geConfEntry": geConfEntry,
       "geConfName": geConfName,
       "geConfSpeedDuplex": geConfSpeedDuplex,
       "geConfAlarmProf": geConfAlarmProf,
       "geLinkStatus": geLinkStatus,
       "geUtilTxCurrentPercent": geUtilTxCurrentPercent,
       "geUtilTxCurrentSpeed": geUtilTxCurrentSpeed,
       "geUtilRxCurrentPercent": geUtilRxCurrentPercent,
       "geUtilRxCurrentSpeed": geUtilRxCurrentSpeed,
       "geUtilTxIssueLvl1Threshold": geUtilTxIssueLvl1Threshold,
       "geUtilTxIssueLvl2Threshold": geUtilTxIssueLvl2Threshold,
       "geUtilRxIssueLvl1Threshold": geUtilRxIssueLvl1Threshold,
       "geUtilRxIssueLvl2Threshold": geUtilRxIssueLvl2Threshold,
       "geUtilSampleSeconds": geUtilSampleSeconds,
       "geOps": geOps,
       "geTarget": geTarget,
       "geOperation": geOperation,
       "geDdmiTable": geDdmiTable,
       "geDdmiEntry": geDdmiEntry,
       "geDdmiTemp": geDdmiTemp,
       "geDdmiVolt": geDdmiVolt,
       "geDdmiTxCurr": geDdmiTxCurr,
       "geDdmiTxPower": geDdmiTxPower,
       "geDdmiRxPower": geDdmiRxPower,
       "geSfpInfoTable": geSfpInfoTable,
       "geSfpInfoEntry": geSfpInfoEntry,
       "geSfpInfoVendor": geSfpInfoVendor,
       "geSfpInfoVendorPn": geSfpInfoVendorPn,
       "geSfpInfoVendorRev": geSfpInfoVendorRev,
       "geSfpInfoVendorSn": geSfpInfoVendorSn,
       "geSfpInfoDateCode": geSfpInfoDateCode,
       "hwmonitor": hwmonitor,
       "fanConfTable": fanConfTable,
       "fanConfEntry": fanConfEntry,
       "fanConfIndex": fanConfIndex,
       "fanConfHighThreshold": fanConfHighThreshold,
       "fanConfLowThreshold": fanConfLowThreshold,
       "temperatureConfTable": temperatureConfTable,
       "temperatureConfEntry": temperatureConfEntry,
       "temperatureConfIndex": temperatureConfIndex,
       "temperatureConfHighThreshold": temperatureConfHighThreshold,
       "temperatureConfLowThreshold": temperatureConfLowThreshold,
       "voltageConfTable": voltageConfTable,
       "voltageConfEntry": voltageConfEntry,
       "voltageConfIndex": voltageConfIndex,
       "voltageConfHighThreshold": voltageConfHighThreshold,
       "voltageConfLowThreshold": voltageConfLowThreshold,
       "fanStatsTable": fanStatsTable,
       "fanStatsEntry": fanStatsEntry,
       "fanRpmCurValue": fanRpmCurValue,
       "fanRpmMaxValue": fanRpmMaxValue,
       "fanRpmMinValue": fanRpmMinValue,
       "fanRpmAvgValue": fanRpmAvgValue,
       "fanRpmDescr": fanRpmDescr,
       "temperatureStatsTable": temperatureStatsTable,
       "temperatureStatsEntry": temperatureStatsEntry,
       "temperatureCurValue": temperatureCurValue,
       "temperatureMaxValue": temperatureMaxValue,
       "temperatureMinValue": temperatureMinValue,
       "temperatureAvgValue": temperatureAvgValue,
       "temperatureDescr": temperatureDescr,
       "voltageStatsTable": voltageStatsTable,
       "voltageStatsEntry": voltageStatsEntry,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageAvgValue": voltageAvgValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageDescr": voltageDescr,
       "batterySaving": batterySaving,
       "externalBattery": externalBattery,
       "externalBatteryStats": externalBatteryStats,
       "externalBatteryStatsTemperature": externalBatteryStatsTemperature,
       "externalBatteryStatsVoltage": externalBatteryStatsVoltage,
       "externalBatteryConf": externalBatteryConf,
       "externalBatteryConfTempHighThreshold": externalBatteryConfTempHighThreshold,
       "externalBatteryConfTempLowThreshold": externalBatteryConfTempLowThreshold,
       "externalBatteryConfDcCriticThreshold": externalBatteryConfDcCriticThreshold,
       "externalBatteryConfDcLowThreshold": externalBatteryConfDcLowThreshold,
       "externalBatteryConfDcErrThreshold": externalBatteryConfDcErrThreshold,
       "igmpmld": igmpmld,
       "igmpmldMode": igmpmldMode,
       "igmpmldVersion": igmpmldVersion,
       "igmpmldLeaveMode": igmpmldLeaveMode,
       "igmpmldLastMemberQueryInterval": igmpmldLastMemberQueryInterval,
       "igmpmldLastMemberQueryRobustness": igmpmldLastMemberQueryRobustness,
       "igmpmldGeneralQueryInterval": igmpmldGeneralQueryInterval,
       "igmpmldGeneralQueryRobustness": igmpmldGeneralQueryRobustness,
       "igmpmldGeneralQueryMaxRespTime": igmpmldGeneralQueryMaxRespTime,
       "igmpmldConfPortTable": igmpmldConfPortTable,
       "igmpmldConfPortEntry": igmpmldConfPortEntry,
       "igmpmldConfPortMaxGroupCount": igmpmldConfPortMaxGroupCount,
       "igmpmldConfPortPrivilegeEnable": igmpmldConfPortPrivilegeEnable,
       "igmpmldConfPortCacEnable": igmpmldConfPortCacEnable,
       "igmpmldConfPortCacMaxBandwidth": igmpmldConfPortCacMaxBandwidth,
       "groupPrivilege": groupPrivilege,
       "igmpmldMaxNumOfGroupPrivilegeProfiles": igmpmldMaxNumOfGroupPrivilegeProfiles,
       "igmpmldGroupPrivilegeProfileTable": igmpmldGroupPrivilegeProfileTable,
       "igmpmldGroupPrivilegeProfileEntry": igmpmldGroupPrivilegeProfileEntry,
       "igmpmldGroupPrivilegeProfileName": igmpmldGroupPrivilegeProfileName,
       "igmpmldGroupPrivilegeProfileIndex": igmpmldGroupPrivilegeProfileIndex,
       "igmpmldGroupPrivilegeProfileAddressType": igmpmldGroupPrivilegeProfileAddressType,
       "igmpmldGroupPrivilegeProfileStartIp": igmpmldGroupPrivilegeProfileStartIp,
       "igmpmldGroupPrivilegeProfileEndIp": igmpmldGroupPrivilegeProfileEndIp,
       "igmpmldGroupPrivilegeProfilePrivilege": igmpmldGroupPrivilegeProfilePrivilege,
       "igmpmldGroupPrivilegeProfilePrivilegePreviewLength": igmpmldGroupPrivilegeProfilePrivilegePreviewLength,
       "igmpmldGroupPrivilegeProfilePrivilegePreviewInterval": igmpmldGroupPrivilegeProfilePrivilegePreviewInterval,
       "igmpmldGroupPrivilegeProfilePrivilegePreviewCount": igmpmldGroupPrivilegeProfilePrivilegePreviewCount,
       "igmpmldGroupPrivilegeProfilePrivilegePreviewReset": igmpmldGroupPrivilegeProfilePrivilegePreviewReset,
       "igmpmldGroupPrivilegeProfileCacBandwidth": igmpmldGroupPrivilegeProfileCacBandwidth,
       "igmpmldGroupPrivilegeProfileRowStatus": igmpmldGroupPrivilegeProfileRowStatus,
       "igmpmldGroupPrivilegePortTable": igmpmldGroupPrivilegePortTable,
       "igmpmldGroupPrivilegePortEntry": igmpmldGroupPrivilegePortEntry,
       "igmpmldGroupPrivilegePortEntryRowStatus": igmpmldGroupPrivilegePortEntryRowStatus,
       "mvlan": mvlan,
       "igmpmldMaxNumOfMvlan": igmpmldMaxNumOfMvlan,
       "igmpmldMvlanTable": igmpmldMvlanTable,
       "igmpmldMvlanEntry": igmpmldMvlanEntry,
       "igmpmldMvlanId": igmpmldMvlanId,
       "igmpmldMvlanRowStatus": igmpmldMvlanRowStatus,
       "igmpmldMvlanTr101fw": igmpmldMvlanTr101fw,
       "igmpmldMvlanPortTable": igmpmldMvlanPortTable,
       "igmpmldMvlanPortEntry": igmpmldMvlanPortEntry,
       "igmpmldMvlanPortEgressType": igmpmldMvlanPortEgressType,
       "igmpmldMvlanPortUniVlan": igmpmldMvlanPortUniVlan,
       "igmpmldMvlanPortRowStatus": igmpmldMvlanPortRowStatus,
       "igmpmldMvlanMapTable": igmpmldMvlanMapTable,
       "igmpmldMvlanMapEntry": igmpmldMvlanMapEntry,
       "igmpmldMvlanMapIndex": igmpmldMvlanMapIndex,
       "igmpmldMvlanMapStartIp": igmpmldMvlanMapStartIp,
       "igmpmldMvlanMapEndIp": igmpmldMvlanMapEndIp,
       "igmpmldMvlanMapRowStatus": igmpmldMvlanMapRowStatus,
       "group": group,
       "igmpmldMvlanGroupTable": igmpmldMvlanGroupTable,
       "igmpmldMvlanGroupEntry": igmpmldMvlanGroupEntry,
       "igmpmldMvlanGroupId": igmpmldMvlanGroupId,
       "igmpmldMvlanGroupAddressType": igmpmldMvlanGroupAddressType,
       "igmpmldMvlanGroupAddress": igmpmldMvlanGroupAddress,
       "igmpmldMvlanGroupNumberOfMembers": igmpmldMvlanGroupNumberOfMembers,
       "igmpmldMvlanGroupNumberOfNewJoinedMembers": igmpmldMvlanGroupNumberOfNewJoinedMembers,
       "igmpmldMvlanGroupNumberOfLeftMembers": igmpmldMvlanGroupNumberOfLeftMembers,
       "igmpmldMvlanGroupPortTable": igmpmldMvlanGroupPortTable,
       "igmpmldMvlanGroupPortEntry": igmpmldMvlanGroupPortEntry,
       "igmpmldMvlanGroupCreateTime": igmpmldMvlanGroupCreateTime,
       "igmpmldMvlanGroupPortBandwidth": igmpmldMvlanGroupPortBandwidth,
       "igmpmldMvlanGroupPortPrivilege": igmpmldMvlanGroupPortPrivilege,
       "igmpmldMvlanGroupPortState": igmpmldMvlanGroupPortState,
       "igmpmldStatistics": igmpmldStatistics,
       "igmpmldStatisticsRxQuery": igmpmldStatisticsRxQuery,
       "igmpmldStatisticstTxQuery": igmpmldStatisticstTxQuery,
       "igmpmldStatisticsRxReport": igmpmldStatisticsRxReport,
       "igmpmldStatisticsTxReport": igmpmldStatisticsTxReport,
       "igmpmldStatisticsPortTable": igmpmldStatisticsPortTable,
       "igmpmldStatisticsPortEntry": igmpmldStatisticsPortEntry,
       "igmpmldStatisticsPortChannelCreateSuccess": igmpmldStatisticsPortChannelCreateSuccess,
       "igmpmldStatisticsPortChannelCreateFail": igmpmldStatisticsPortChannelCreateFail,
       "igmpmldStatisticsPortChannelRemoveLeave": igmpmldStatisticsPortChannelRemoveLeave,
       "igmpmldStatisticsPortChannelRemoveTimeout": igmpmldStatisticsPortChannelRemoveTimeout,
       "igmpmldStatisticsPortQueryRx": igmpmldStatisticsPortQueryRx,
       "igmpmldStatisticsPortQueryTx": igmpmldStatisticsPortQueryTx,
       "igmpmldStatisticsPortGeneralQueryIgmpv2Tx": igmpmldStatisticsPortGeneralQueryIgmpv2Tx,
       "igmpmldStatisticsPortGeneralQueryIgmpv3Tx": igmpmldStatisticsPortGeneralQueryIgmpv3Tx,
       "igmpmldStatisticsPortGeneralQueryMldv1Tx": igmpmldStatisticsPortGeneralQueryMldv1Tx,
       "igmpmldStatisticsPortGeneralQueryMldv2Tx": igmpmldStatisticsPortGeneralQueryMldv2Tx,
       "igmpmldStatisticsPortSpecificQueryIgmpv2Tx": igmpmldStatisticsPortSpecificQueryIgmpv2Tx,
       "igmpmldStatisticsPortSpecificQueryIgmpv3Tx": igmpmldStatisticsPortSpecificQueryIgmpv3Tx,
       "igmpmldStatisticsPortSpecificQueryMldv1Tx": igmpmldStatisticsPortSpecificQueryMldv1Tx,
       "igmpmldStatisticsPortSpecificQueryMldv2Tx": igmpmldStatisticsPortSpecificQueryMldv2Tx,
       "igmpmldStatisticsPortReportRx": igmpmldStatisticsPortReportRx,
       "igmpmldStatisticsPortReportTx": igmpmldStatisticsPortReportTx,
       "igmpmldStatisticsPortReportJoinIgmpv2Rx": igmpmldStatisticsPortReportJoinIgmpv2Rx,
       "igmpmldStatisticsPortReportLeaveIgmpv2Rx": igmpmldStatisticsPortReportLeaveIgmpv2Rx,
       "igmpmldStatisticsPortReportDropIgmp": igmpmldStatisticsPortReportDropIgmp,
       "igmpmldStatisticsPortCompatibleMode": igmpmldStatisticsPortCompatibleMode,
       "igmpmldStatisticsPortReportJoinMldv1Rx": igmpmldStatisticsPortReportJoinMldv1Rx,
       "igmpmldStatisticsPortReportLeaveMldv1Rx": igmpmldStatisticsPortReportLeaveMldv1Rx,
       "igmpmldStatisticsPortReportDropMld": igmpmldStatisticsPortReportDropMld,
       "igmpmldStatisticsPortReportIgmpv3Rx": igmpmldStatisticsPortReportIgmpv3Rx,
       "igmpmldStatisticsPortReportMldv2Rx": igmpmldStatisticsPortReportMldv2Rx,
       "igmpmldStatisticsPortQueryDropIgmp": igmpmldStatisticsPortQueryDropIgmp,
       "igmpmldStatisticsPortQueryDropMld": igmpmldStatisticsPortQueryDropMld,
       "igmpmldStatisticsPortGeneralQueryIgmpv2Rx": igmpmldStatisticsPortGeneralQueryIgmpv2Rx,
       "igmpmldStatisticsPortGeneralQueryIgmpv3Rx": igmpmldStatisticsPortGeneralQueryIgmpv3Rx,
       "igmpmldStatisticsPortGeneralQueryMldv1Rx": igmpmldStatisticsPortGeneralQueryMldv1Rx,
       "igmpmldStatisticsPortGeneralQueryMldv2Rx": igmpmldStatisticsPortGeneralQueryMldv2Rx,
       "igmpmldStatisticsPortSpecificQueryIgmpv2Rx": igmpmldStatisticsPortSpecificQueryIgmpv2Rx,
       "igmpmldStatisticsPortSpecificQueryIgmpv3Rx": igmpmldStatisticsPortSpecificQueryIgmpv3Rx,
       "igmpmldStatisticsPortSpecificQueryMldv1Rx": igmpmldStatisticsPortSpecificQueryMldv1Rx,
       "igmpmldStatisticsPortSpecificQueryMldv2Rx": igmpmldStatisticsPortSpecificQueryMldv2Rx,
       "igmpmldStatisticsPortReportJoinIgmpv2Tx": igmpmldStatisticsPortReportJoinIgmpv2Tx,
       "igmpmldStatisticsPortReportLeaveIgmpv2Tx": igmpmldStatisticsPortReportLeaveIgmpv2Tx,
       "igmpmldStatisticsPortReportJoinMldv1Tx": igmpmldStatisticsPortReportJoinMldv1Tx,
       "igmpmldStatisticsPortReportLeaveMldv1Tx": igmpmldStatisticsPortReportLeaveMldv1Tx,
       "igmpmldStatisticsPortReportIgmpv3Tx": igmpmldStatisticsPortReportIgmpv3Tx,
       "igmpmldStatisticsPortReportMldv2Tx": igmpmldStatisticsPortReportMldv2Tx,
       "igmpmldLogs": igmpmldLogs,
       "igmpmldLogsPortTable": igmpmldLogsPortTable,
       "igmpmldLogsPortEntry": igmpmldLogsPortEntry,
       "igmpmldLogsPortTime": igmpmldLogsPortTime,
       "igmpmldLogsPortSerialNo": igmpmldLogsPortSerialNo,
       "igmpmldLogsPortEvent": igmpmldLogsPortEvent,
       "igmpmldLogsPortGroupAddressType": igmpmldLogsPortGroupAddressType,
       "igmpmldLogsPortGroupAddress": igmpmldLogsPortGroupAddress,
       "igmpmldOps": igmpmldOps,
       "igmpmldTarget": igmpmldTarget,
       "igmpmldOperation": igmpmldOperation,
       "igmpmldPbit": igmpmldPbit,
       "igmpmldTest": igmpmldTest,
       "ip": ip,
       "ipArp": ipArp,
       "ipArpOps": ipArpOps,
       "ipArpTable": ipArpTable,
       "ipArpEntry": ipArpEntry,
       "ipAddress": ipAddress,
       "macAddress": macAddress,
       "ipInterface": ipInterface,
       "ipInband": ipInband,
       "ipInbandAddress": ipInbandAddress,
       "ipInbandNetmask": ipInbandNetmask,
       "ipInbandMgmtVlan": ipInbandMgmtVlan,
       "ipInbandGateway": ipInbandGateway,
       "ipv6InbandAddress": ipv6InbandAddress,
       "ipv6InbandNetmask": ipv6InbandNetmask,
       "ipv6InbandGateway": ipv6InbandGateway,
       "ipInbandDhcpBootpEnable": ipInbandDhcpBootpEnable,
       "ipInbandDhcpOperation": ipInbandDhcpOperation,
       "ipInbandMgmtPbit": ipInbandMgmtPbit,
       "ipv6InbandLinkLocalAddress": ipv6InbandLinkLocalAddress,
       "ipOutband": ipOutband,
       "ipOutbandAddress": ipOutbandAddress,
       "ipOutbandNetmask": ipOutbandNetmask,
       "ipv6OutbandAddress": ipv6OutbandAddress,
       "ipv6OutbandNetmask": ipv6OutbandNetmask,
       "ipv6OutbandLinkLocalAddress": ipv6OutbandLinkLocalAddress,
       "ipv6DefaultMgmt": ipv6DefaultMgmt,
       "ipRoute": ipRoute,
       "ipMaxNumOfStaticRoutes": ipMaxNumOfStaticRoutes,
       "ipStaticRouteTable": ipStaticRouteTable,
       "ipStaticRouteEntry": ipStaticRouteEntry,
       "ipStaticRouteDest": ipStaticRouteDest,
       "ipStaticRouteMask": ipStaticRouteMask,
       "ipStaticRouteNextHop": ipStaticRouteNextHop,
       "ipStaticRouteRowStatus": ipStaticRouteRowStatus,
       "ipStaticRouteIfName": ipStaticRouteIfName,
       "ipRouteTable": ipRouteTable,
       "ipRouteEntry": ipRouteEntry,
       "ipRouteDest": ipRouteDest,
       "ipRouteMask": ipRouteMask,
       "ipRouteNextHop": ipRouteNextHop,
       "ipRouteIfName": ipRouteIfName,
       "ipv6DefaultRouterInbandTable": ipv6DefaultRouterInbandTable,
       "ipv6DefaultRouterInbandEntry": ipv6DefaultRouterInbandEntry,
       "ipv6DefaultRouterInbandAddress": ipv6DefaultRouterInbandAddress,
       "ipv6DefaultRouterInbandPreference": ipv6DefaultRouterInbandPreference,
       "ipv6DefaultRouterInbandLifetime": ipv6DefaultRouterInbandLifetime,
       "ipv6DefaultRouterInbandExpire": ipv6DefaultRouterInbandExpire,
       "ipv6DefaultRouterInbandFlag": ipv6DefaultRouterInbandFlag,
       "ipv6DefaultRouterOutbandTable": ipv6DefaultRouterOutbandTable,
       "ipv6DefaultRouterOutbandEntry": ipv6DefaultRouterOutbandEntry,
       "ipv6DefaultRouterOutbandAddress": ipv6DefaultRouterOutbandAddress,
       "ipv6DefaultRouterOutbandPreference": ipv6DefaultRouterOutbandPreference,
       "ipv6DefaultRouterOutbandLifetime": ipv6DefaultRouterOutbandLifetime,
       "ipv6DefaultRouterOutbandExpire": ipv6DefaultRouterOutbandExpire,
       "ipv6DefaultRouterOutbandFlag": ipv6DefaultRouterOutbandFlag,
       "ipv6RouteInbandTable": ipv6RouteInbandTable,
       "ipv6RouteInbandEntry": ipv6RouteInbandEntry,
       "ipv6RouteInbandAddress": ipv6RouteInbandAddress,
       "ipv6RouteInbandMask": ipv6RouteInbandMask,
       "ipv6RouteInbandName": ipv6RouteInbandName,
       "ipv6RouteOutbandTable": ipv6RouteOutbandTable,
       "ipv6RouteOutbandEntry": ipv6RouteOutbandEntry,
       "ipv6RouteOutbandAddress": ipv6RouteOutbandAddress,
       "ipv6RouteOutbandMask": ipv6RouteOutbandMask,
       "ipv6RouteOutbandName": ipv6RouteOutbandName,
       "ipStatistic": ipStatistic,
       "ipInOctetCount": ipInOctetCount,
       "ipInUnicastCount": ipInUnicastCount,
       "ipInMulticastCount": ipInMulticastCount,
       "ipInDiscardCount": ipInDiscardCount,
       "ipInErrorCount": ipInErrorCount,
       "ipInUnknowProtocolCount": ipInUnknowProtocolCount,
       "ipOutOctetCount": ipOutOctetCount,
       "ipOutUnicastCount": ipOutUnicastCount,
       "ipOutMulticastCount": ipOutMulticastCount,
       "ipOutDiscardCount": ipOutDiscardCount,
       "ipOutErrorCount": ipOutErrorCount,
       "ipv6Destination": ipv6Destination,
       "ipv6DestInbandTable": ipv6DestInbandTable,
       "ipv6DestInbandEntry": ipv6DestInbandEntry,
       "ipv6DestInbandDestAddress": ipv6DestInbandDestAddress,
       "ipv6DestInbandNextHopAddress": ipv6DestInbandNextHopAddress,
       "ipv6DestOutbandTable": ipv6DestOutbandTable,
       "ipv6DestOutbandEntry": ipv6DestOutbandEntry,
       "ipv6DestOutbandDestAddress": ipv6DestOutbandDestAddress,
       "ipv6DestOutbandNextHopAddress": ipv6DestOutbandNextHopAddress,
       "ipv6Neighbor": ipv6Neighbor,
       "ipv6NeighborInbandTable": ipv6NeighborInbandTable,
       "ipv6NeighborInbandEntry": ipv6NeighborInbandEntry,
       "ipv6NeighborInbandNeighbor": ipv6NeighborInbandNeighbor,
       "ipv6NeighborInbandLinklayerAddress": ipv6NeighborInbandLinklayerAddress,
       "ipv6NeighborInbandExpire": ipv6NeighborInbandExpire,
       "ipv6NeighborInbandFlags": ipv6NeighborInbandFlags,
       "ipv6NeighborOutbandTable": ipv6NeighborOutbandTable,
       "ipv6NeighborOutbandEntry": ipv6NeighborOutbandEntry,
       "ipv6NeighborOutbandNeighbor": ipv6NeighborOutbandNeighbor,
       "ipv6NeighborOutbandLinklayerAddress": ipv6NeighborOutbandLinklayerAddress,
       "ipv6NeighborOutbandExpire": ipv6NeighborOutbandExpire,
       "ipv6NeighborOutbandFlags": ipv6NeighborOutbandFlags,
       "ipv6Prefix": ipv6Prefix,
       "ipv6PrefixInbandTable": ipv6PrefixInbandTable,
       "ipv6PrefixInbandEntry": ipv6PrefixInbandEntry,
       "ipv6PrefixInbandPrefix": ipv6PrefixInbandPrefix,
       "ipv6PrefixInbandPrefixLength": ipv6PrefixInbandPrefixLength,
       "ipv6PrefixInbandVLtime": ipv6PrefixInbandVLtime,
       "ipv6PrefixInbandPLtime": ipv6PrefixInbandPLtime,
       "ipv6PrefixInbandExpire": ipv6PrefixInbandExpire,
       "ipv6PrefixInbandOnlink": ipv6PrefixInbandOnlink,
       "ipv6PrefixInbandAutonomous": ipv6PrefixInbandAutonomous,
       "ipv6PrefixOutbandTable": ipv6PrefixOutbandTable,
       "ipv6PrefixOutbandEntry": ipv6PrefixOutbandEntry,
       "ipv6PrefixOutbandPrefix": ipv6PrefixOutbandPrefix,
       "ipv6PrefixOutbandPrefixLength": ipv6PrefixOutbandPrefixLength,
       "ipv6PrefixOutbandVLtime": ipv6PrefixOutbandVLtime,
       "ipv6PrefixOutbandPLtime": ipv6PrefixOutbandPLtime,
       "ipv6PrefixOutbandExpire": ipv6PrefixOutbandExpire,
       "ipv6PrefixOutbandOnlink": ipv6PrefixOutbandOnlink,
       "ipv6PrefixOutbandAutonomous": ipv6PrefixOutbandAutonomous,
       "lcm": lcm,
       "slotModuleTable": slotModuleTable,
       "slotModuleEntry": slotModuleEntry,
       "slotModuleIdVes1724-58v": slotModuleIdVes1724_58v,
       "slotModuleRealType": slotModuleRealType,
       "slotModuleDescr": slotModuleDescr,
       "slotModuleStatus": slotModuleStatus,
       "slotModuleAlarmStatus": slotModuleAlarmStatus,
       "slotModuleHWVersion": slotModuleHWVersion,
       "slotModuleSerialNumber": slotModuleSerialNumber,
       "slotModuleCleiCode": slotModuleCleiCode,
       "slotModuleUpTime": slotModuleUpTime,
       "login": login,
       "loginMaxNumOfUsers": loginMaxNumOfUsers,
       "loginUserTable": loginUserTable,
       "loginUserEntry": loginUserEntry,
       "loginUserName": loginUserName,
       "loginUserPassword": loginUserPassword,
       "loginUserPrivilege": loginUserPrivilege,
       "loginUserRowStatus": loginUserRowStatus,
       "loopguard": loopguard,
       "loopguardConfPortTable": loopguardConfPortTable,
       "loopguardConfPortEntry": loopguardConfPortEntry,
       "loopguardConfPortEnable": loopguardConfPortEnable,
       "loopguardConfPortPolicy": loopguardConfPortPolicy,
       "loopguardConfPortRecoverTime": loopguardConfPortRecoverTime,
       "loopguardConfPortUniVlan": loopguardConfPortUniVlan,
       "loopguardConfPortPbit": loopguardConfPortPbit,
       "loopguardStatsSysStatus": loopguardStatsSysStatus,
       "loopguardStatsPortTable": loopguardStatsPortTable,
       "loopguardStatsPortEntry": loopguardStatsPortEntry,
       "loopguardStatsPortLinkedState": loopguardStatsPortLinkedState,
       "loopguardStatsPortTxPkts": loopguardStatsPortTxPkts,
       "loopguardStatsPortRxPkts": loopguardStatsPortRxPkts,
       "loopguardStatsPortBadPkts": loopguardStatsPortBadPkts,
       "loopguardStatsPortShutdownTime": loopguardStatsPortShutdownTime,
       "loopguardStatsPortOperation": loopguardStatsPortOperation,
       "interworking": interworking,
       "atmvc": atmvc,
       "atmMaxNumOfVcPerPort": atmMaxNumOfVcPerPort,
       "atmvcTable": atmvcTable,
       "atmvcEntry": atmvcEntry,
       "atmvcVpi": atmvcVpi,
       "atmvcVci": atmvcVci,
       "atmvcPriority": atmvcPriority,
       "atmvcEncap": atmvcEncap,
       "atmvcRowStatus": atmvcRowStatus,
       "atmvcMvlan": atmvcMvlan,
       "atmvcPvid": atmvcPvid,
       "atmvcPbit": atmvcPbit,
       "atmvcVlanTrunk": atmvcVlanTrunk,
       "atmOamF5Table": atmOamF5Table,
       "atmOamF5Entry": atmOamF5Entry,
       "atmOamF5Test": atmOamF5Test,
       "atmOamF5TestResult": atmOamF5TestResult,
       "portIsolation": portIsolation,
       "portIsolationEnable": portIsolationEnable,
       "portIsolationVlanTable": portIsolationVlanTable,
       "portIsolationVlanEntry": portIsolationVlanEntry,
       "portIsolationVlanVid": portIsolationVlanVid,
       "portIsolationVlanRowStatus": portIsolationVlanRowStatus,
       "vlanGlobal": vlanGlobal,
       "vlanStagTpid": vlanStagTpid,
       "vlanSingleTagMode": vlanSingleTagMode,
       "vlanUplink": vlanUplink,
       "vlanUplinkTable": vlanUplinkTable,
       "vlanUplinkEntry": vlanUplinkEntry,
       "vlanUplinkVlanId": vlanUplinkVlanId,
       "vlanUplinkRowStatus": vlanUplinkRowStatus,
       "vlanUplinkJoinAllTable": vlanUplinkJoinAllTable,
       "vlanUplinkJoinAllEntry": vlanUplinkJoinAllEntry,
       "vlanUplinkJoinAllEnable": vlanUplinkJoinAllEnable,
       "vlanUplinkMaxNumOfUntagPerPort": vlanUplinkMaxNumOfUntagPerPort,
       "vlanUplinkUntagTable": vlanUplinkUntagTable,
       "vlanUplinkUntagEntry": vlanUplinkUntagEntry,
       "vlanUplinkUntagVlanId": vlanUplinkUntagVlanId,
       "vlanUplinkUntagVlanPbit": vlanUplinkUntagVlanPbit,
       "vlanUplinkUntagRowStatus": vlanUplinkUntagRowStatus,
       "vlanTransparent": vlanTransparent,
       "vlanTransparentPortTable": vlanTransparentPortTable,
       "vlanTransparentPortEntry": vlanTransparentPortEntry,
       "vlanTransparentPortRowStatus": vlanTransparentPortRowStatus,
       "vlanTransparentVcTable": vlanTransparentVcTable,
       "vlanTransparentVcEntry": vlanTransparentVcEntry,
       "vlanTransparentVcRowStatus": vlanTransparentVcRowStatus,
       "vlanTrunk": vlanTrunk,
       "vlanTrunkUntagPortTable": vlanTrunkUntagPortTable,
       "vlanTrunkUntagPortEntry": vlanTrunkUntagPortEntry,
       "vlanTrunkUntagPortMode": vlanTrunkUntagPortMode,
       "vlanTrunkUntagPortNniSvlan": vlanTrunkUntagPortNniSvlan,
       "vlanTrunkUntagPortNniSpbit": vlanTrunkUntagPortNniSpbit,
       "vlanTrunkUntagPortNniCvlan": vlanTrunkUntagPortNniCvlan,
       "vlanTrunkUntagPortNniCpbit": vlanTrunkUntagPortNniCpbit,
       "vlanTrunkUntagPortRowStatus": vlanTrunkUntagPortRowStatus,
       "vlanTrunkUntagEtypePortTable": vlanTrunkUntagEtypePortTable,
       "vlanTrunkUntagEtypePortEntry": vlanTrunkUntagEtypePortEntry,
       "vlanTrunkUntagEtypePortEtype": vlanTrunkUntagEtypePortEtype,
       "vlanTrunkUntagEtypePortMode": vlanTrunkUntagEtypePortMode,
       "vlanTrunkUntagEtypePortNniSvlan": vlanTrunkUntagEtypePortNniSvlan,
       "vlanTrunkUntagEtypePortNniSpbit": vlanTrunkUntagEtypePortNniSpbit,
       "vlanTrunkUntagEtypePortNniCvlan": vlanTrunkUntagEtypePortNniCvlan,
       "vlanTrunkUntagEtypePortNniCpbit": vlanTrunkUntagEtypePortNniCpbit,
       "vlanTrunkUntagEtypePortRowStatus": vlanTrunkUntagEtypePortRowStatus,
       "vlanTrunkTagPortTable": vlanTrunkTagPortTable,
       "vlanTrunkTagPortEntry": vlanTrunkTagPortEntry,
       "vlanTrunkTagPortUniNniVlan": vlanTrunkTagPortUniNniVlan,
       "vlanTrunkTagPortMode": vlanTrunkTagPortMode,
       "vlanTrunkTagPortNniSvlan": vlanTrunkTagPortNniSvlan,
       "vlanTrunkTagPortRowStatus": vlanTrunkTagPortRowStatus,
       "vlanTrunkUntagVcTable": vlanTrunkUntagVcTable,
       "vlanTrunkUntagVcEntry": vlanTrunkUntagVcEntry,
       "vlanTrunkUntagVcMode": vlanTrunkUntagVcMode,
       "vlanTrunkUntagVcNniSvlan": vlanTrunkUntagVcNniSvlan,
       "vlanTrunkUntagVcNniSpbit": vlanTrunkUntagVcNniSpbit,
       "vlanTrunkUntagVcNniCvlan": vlanTrunkUntagVcNniCvlan,
       "vlanTrunkUntagVcNniCpbit": vlanTrunkUntagVcNniCpbit,
       "vlanTrunkUntagVcRowStatus": vlanTrunkUntagVcRowStatus,
       "vlanTrunkUntagEtypeVcTable": vlanTrunkUntagEtypeVcTable,
       "vlanTrunkUntagEtypeVcEntry": vlanTrunkUntagEtypeVcEntry,
       "vlanTrunkUntagEtypeVcEtype": vlanTrunkUntagEtypeVcEtype,
       "vlanTrunkUntagEtypeVcMode": vlanTrunkUntagEtypeVcMode,
       "vlanTrunkUntagEtypeVcNniSvlan": vlanTrunkUntagEtypeVcNniSvlan,
       "vlanTrunkUntagEtypeVcNniSpbit": vlanTrunkUntagEtypeVcNniSpbit,
       "vlanTrunkUntagEtypeVcNniCvlan": vlanTrunkUntagEtypeVcNniCvlan,
       "vlanTrunkUntagEtypeVcNniCpbit": vlanTrunkUntagEtypeVcNniCpbit,
       "vlanTrunkUntagEtypeVcRowStatus": vlanTrunkUntagEtypeVcRowStatus,
       "vlanTrunkTagVcTable": vlanTrunkTagVcTable,
       "vlanTrunkTagVcEntry": vlanTrunkTagVcEntry,
       "vlanTrunkTagVcUniNniVlan": vlanTrunkTagVcUniNniVlan,
       "vlanTrunkTagVcMode": vlanTrunkTagVcMode,
       "vlanTrunkTagVcNniSvlan": vlanTrunkTagVcNniSvlan,
       "vlanTrunkTagVcRowStatus": vlanTrunkTagVcRowStatus,
       "vlanTranslation": vlanTranslation,
       "vlanTranslationPortTable": vlanTranslationPortTable,
       "vlanTranslationPortEntry": vlanTranslationPortEntry,
       "vlanTranslationPortUniVlan": vlanTranslationPortUniVlan,
       "vlanTranslationPortMode": vlanTranslationPortMode,
       "vlanTranslationPortNniSvlan": vlanTranslationPortNniSvlan,
       "vlanTranslationPortNniCvlan": vlanTranslationPortNniCvlan,
       "vlanTranslationPortRowStatus": vlanTranslationPortRowStatus,
       "vlanTranslationVcTable": vlanTranslationVcTable,
       "vlanTranslationVcEntry": vlanTranslationVcEntry,
       "vlanTranslationVcUniVlan": vlanTranslationVcUniVlan,
       "vlanTranslationVcMode": vlanTranslationVcMode,
       "vlanTranslationVcNniSvlan": vlanTranslationVcNniSvlan,
       "vlanTranslationVcNniCvlan": vlanTranslationVcNniCvlan,
       "vlanTranslationVcRowStatus": vlanTranslationVcRowStatus,
       "vlanTls": vlanTls,
       "vlanTlsPortTable": vlanTlsPortTable,
       "vlanTlsPortEntry": vlanTlsPortEntry,
       "vlanTlsPortNniSvlan": vlanTlsPortNniSvlan,
       "vlanTlsPortNniSpbit": vlanTlsPortNniSpbit,
       "vlanTlsPortNniForceSpbit": vlanTlsPortNniForceSpbit,
       "vlanTlsPortRowStatus": vlanTlsPortRowStatus,
       "vlanTlsVcTable": vlanTlsVcTable,
       "vlanTlsVcEntry": vlanTlsVcEntry,
       "vlanTlsVcNniSvlan": vlanTlsVcNniSvlan,
       "vlanTlsVcNniSpbit": vlanTlsVcNniSpbit,
       "vlanTlsVcNniForceSpbit": vlanTlsVcNniForceSpbit,
       "vlanTlsVcRowStatus": vlanTlsVcRowStatus,
       "fdb": fdb,
       "fdbAgingTime": fdbAgingTime,
       "fdbOps": fdbOps,
       "fdbTarget": fdbTarget,
       "fdbOperation": fdbOperation,
       "fdbPortConfTable": fdbPortConfTable,
       "fdbPortConfEntry": fdbPortConfEntry,
       "fdbPortConfMaxNumOfMacEntries": fdbPortConfMaxNumOfMacEntries,
       "fdbPortConfMacMode": fdbPortConfMacMode,
       "fdbPortUniVlanConfTable": fdbPortUniVlanConfTable,
       "fdbPortUniVlanConfEntry": fdbPortUniVlanConfEntry,
       "fdbPortVlanConfUniVlan": fdbPortVlanConfUniVlan,
       "fdbPortVlanConfMaxNumOfMacEntries": fdbPortVlanConfMaxNumOfMacEntries,
       "fdbPortVlanConfRowStatus": fdbPortVlanConfRowStatus,
       "fdbStaticMacTable": fdbStaticMacTable,
       "fdbStaticMacEntry": fdbStaticMacEntry,
       "fdbStaticMacMode": fdbStaticMacMode,
       "fdbStaticMacVlanId": fdbStaticMacVlanId,
       "fdbStaticMacPhysAddress": fdbStaticMacPhysAddress,
       "fdbStaticMacRowStatus": fdbStaticMacRowStatus,
       "fdbMacLearningVlanTable": fdbMacLearningVlanTable,
       "fdbMacLearningVlanEntry": fdbMacLearningVlanEntry,
       "fdbMacLearningVlanMode": fdbMacLearningVlanMode,
       "fdbMacLearningVlanNniSVlan": fdbMacLearningVlanNniSVlan,
       "fdbMacLearningVlanNniCVlan": fdbMacLearningVlanNniCVlan,
       "fdbMacLearningVlanPhysAddress": fdbMacLearningVlanPhysAddress,
       "fdbMacLearningVlanUniVlan": fdbMacLearningVlanUniVlan,
       "fdbMacLearningVlanPort": fdbMacLearningVlanPort,
       "fdbMacLearningVlanType": fdbMacLearningVlanType,
       "fdbAntiSpoofing": fdbAntiSpoofing,
       "fdbSpoofingAction": fdbSpoofingAction,
       "mtu": mtu,
       "mirror": mirror,
       "mirrorPortTable": mirrorPortTable,
       "mirrorPortEntry": mirrorPortEntry,
       "mirrorPortDestPort": mirrorPortDestPort,
       "mirrorPortDestPortVpi": mirrorPortDestPortVpi,
       "mirrorPortDestPortVci": mirrorPortDestPortVci,
       "mirrorPortDirection": mirrorPortDirection,
       "mirrorPortRowStatus": mirrorPortRowStatus,
       "mirrorVcTable": mirrorVcTable,
       "mirrorVcEntry": mirrorVcEntry,
       "mirrorVcDestPort": mirrorVcDestPort,
       "mirrorVcDestPortVpi": mirrorVcDestPortVpi,
       "mirrorVcDestPortVci": mirrorVcDestPortVci,
       "mirrorVcDirection": mirrorVcDirection,
       "mirrorVcRowStatus": mirrorVcRowStatus,
       "pppoe": pppoe,
       "pppoeAgentTable": pppoeAgentTable,
       "pppoeAgentEntry": pppoeAgentEntry,
       "pppoeAgentVlanId": pppoeAgentVlanId,
       "pppoeAgentMode": pppoeAgentMode,
       "pppoeAgentCircuitIDEnable": pppoeAgentCircuitIDEnable,
       "pppoeAgentCircuitIDInfo": pppoeAgentCircuitIDInfo,
       "pppoeAgentRemoteIDEnable": pppoeAgentRemoteIDEnable,
       "pppoeAgentRemoteIDInfo": pppoeAgentRemoteIDInfo,
       "pppoeAgentRowStatus": pppoeAgentRowStatus,
       "pppoeTest": pppoeTest,
       "pppoeTestPort": pppoeTestPort,
       "pppoeTestVlanMode": pppoeTestVlanMode,
       "pppoeTestSvid": pppoeTestSvid,
       "pppoeTestCvid": pppoeTestCvid,
       "pppoeTestOps": pppoeTestOps,
       "pppoeTestStatus": pppoeTestStatus,
       "qos": qos,
       "qosAtmVcShapingEnable": qosAtmVcShapingEnable,
       "qosMaxNumOfShapingProfiles": qosMaxNumOfShapingProfiles,
       "qosShapingProfileTable": qosShapingProfileTable,
       "qosShapingProfileEntry": qosShapingProfileEntry,
       "qosShapingProfileName": qosShapingProfileName,
       "qosShapingProfileQueue7MaxRate": qosShapingProfileQueue7MaxRate,
       "qosShapingProfileQueue6MaxRate": qosShapingProfileQueue6MaxRate,
       "qosShapingProfileQueue5MaxRate": qosShapingProfileQueue5MaxRate,
       "qosShapingProfileQueue4MaxRate": qosShapingProfileQueue4MaxRate,
       "qosShapingProfileQueue3MaxRate": qosShapingProfileQueue3MaxRate,
       "qosShapingProfileQueue2MaxRate": qosShapingProfileQueue2MaxRate,
       "qosShapingProfileQueue1MaxRate": qosShapingProfileQueue1MaxRate,
       "qosShapingProfileQueue0MaxRate": qosShapingProfileQueue0MaxRate,
       "qosShapingProfileQueue7Depth": qosShapingProfileQueue7Depth,
       "qosShapingProfileQueue6Depth": qosShapingProfileQueue6Depth,
       "qosShapingProfileQueue5Depth": qosShapingProfileQueue5Depth,
       "qosShapingProfileQueue4Depth": qosShapingProfileQueue4Depth,
       "qosShapingProfileQueue3Depth": qosShapingProfileQueue3Depth,
       "qosShapingProfileQueue2Depth": qosShapingProfileQueue2Depth,
       "qosShapingProfileQueue1Depth": qosShapingProfileQueue1Depth,
       "qosShapingProfileQueue0Depth": qosShapingProfileQueue0Depth,
       "qosShapingProfileRowStatus": qosShapingProfileRowStatus,
       "qosMaxNumOfVcShapingProfiles": qosMaxNumOfVcShapingProfiles,
       "qosVcShapingProfileTable": qosVcShapingProfileTable,
       "qosVcShapingProfileEntry": qosVcShapingProfileEntry,
       "qosVcShapingProfileName": qosVcShapingProfileName,
       "qosVcShapingProfileMaxRate": qosVcShapingProfileMaxRate,
       "qosVcShapingProfileQueueDepth": qosVcShapingProfileQueueDepth,
       "qosVcShapingProfileRowStatus": qosVcShapingProfileRowStatus,
       "qosPortConfTable": qosPortConfTable,
       "qosPortConfEntry": qosPortConfEntry,
       "qosPortConfShapingProfile": qosPortConfShapingProfile,
       "qosPortConfAlgorithm": qosPortConfAlgorithm,
       "qosPortConfMaxRate": qosPortConfMaxRate,
       "qosPortConfWeightProfile": qosPortConfWeightProfile,
       "qosVcConfTable": qosVcConfTable,
       "qosVcConfEntry": qosVcConfEntry,
       "qosVcConfShapingProfile": qosVcConfShapingProfile,
       "queueMapping": queueMapping,
       "queueMappingPbit7QueueId": queueMappingPbit7QueueId,
       "queueMappingPbit6QueueId": queueMappingPbit6QueueId,
       "queueMappingPbit5QueueId": queueMappingPbit5QueueId,
       "queueMappingPbit4QueueId": queueMappingPbit4QueueId,
       "queueMappingPbit3QueueId": queueMappingPbit3QueueId,
       "queueMappingPbit2QueueId": queueMappingPbit2QueueId,
       "queueMappingPbit1QueueId": queueMappingPbit1QueueId,
       "queueMappingPbit0QueueId": queueMappingPbit0QueueId,
       "dscp": dscp,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpSrcCodePoint": dscpSrcCodePoint,
       "dscpMapPriority": dscpMapPriority,
       "dscpPortTable": dscpPortTable,
       "dscpPortEntry": dscpPortEntry,
       "dscpStatusEnable": dscpStatusEnable,
       "qosMaxNumOfWeightProfiles": qosMaxNumOfWeightProfiles,
       "qosWeightProfileTable": qosWeightProfileTable,
       "qosWeightProfileEntry": qosWeightProfileEntry,
       "qosWeightProfileName": qosWeightProfileName,
       "qosWeightProfileQueue7Weight": qosWeightProfileQueue7Weight,
       "qosWeightProfileQueue6Weight": qosWeightProfileQueue6Weight,
       "qosWeightProfileQueue5Weight": qosWeightProfileQueue5Weight,
       "qosWeightProfileQueue4Weight": qosWeightProfileQueue4Weight,
       "qosWeightProfileQueue3Weight": qosWeightProfileQueue3Weight,
       "qosWeightProfileQueue2Weight": qosWeightProfileQueue2Weight,
       "qosWeightProfileQueue1Weight": qosWeightProfileQueue1Weight,
       "qosWeightProfileQueue0Weight": qosWeightProfileQueue0Weight,
       "qosWeightProfileQueue7Depth": qosWeightProfileQueue7Depth,
       "qosWeightProfileQueue6Depth": qosWeightProfileQueue6Depth,
       "qosWeightProfileQueue5Depth": qosWeightProfileQueue5Depth,
       "qosWeightProfileQueue4Depth": qosWeightProfileQueue4Depth,
       "qosWeightProfileQueue3Depth": qosWeightProfileQueue3Depth,
       "qosWeightProfileQueue2Depth": qosWeightProfileQueue2Depth,
       "qosWeightProfileQueue1Depth": qosWeightProfileQueue1Depth,
       "qosWeightProfileQueue0Depth": qosWeightProfileQueue0Depth,
       "qosWeightProfileRowStatus": qosWeightProfileRowStatus,
       "service": service,
       "securedClientIpTable": securedClientIpTable,
       "securedClientIpEntry": securedClientIpEntry,
       "securedClientIpIndex": securedClientIpIndex,
       "securedClientIpStartIpAddress": securedClientIpStartIpAddress,
       "securedClientIpEndIpAddress": securedClientIpEndIpAddress,
       "securedClientIpService": securedClientIpService,
       "securedClientIpEnable": securedClientIpEnable,
       "securedClientIpv6Table": securedClientIpv6Table,
       "securedClientIpv6Entry": securedClientIpv6Entry,
       "securedClientIpv6Index": securedClientIpv6Index,
       "securedClientIpv6IpAddress": securedClientIpv6IpAddress,
       "securedClientIpv6IpMask": securedClientIpv6IpMask,
       "securedClientIpv6Service": securedClientIpv6Service,
       "securedClientIpv6Enable": securedClientIpv6Enable,
       "snmp": snmp,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "snmpTrapDestIndex": snmpTrapDestIndex,
       "snmpTrapDestIpAddressType": snmpTrapDestIpAddressType,
       "snmpTrapDestIpAddress": snmpTrapDestIpAddress,
       "snmpTrapDestUdpPort": snmpTrapDestUdpPort,
       "snmpTrapDestVersion": snmpTrapDestVersion,
       "snmpTrapDestUserName": snmpTrapDestUserName,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserSecurityLevel": snmpUserSecurityLevel,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpVersion": snmpVersion,
       "sys": sys,
       "sysBootupFwVersion": sysBootupFwVersion,
       "sysImage1FwVersion": sysImage1FwVersion,
       "sysImage2FwVersion": sysImage2FwVersion,
       "sysBootupImage": sysBootupImage,
       "sysBootupConfig": sysBootupConfig,
       "sysOps": sysOps,
       "sysTarget": sysTarget,
       "sysOperation": sysOperation,
       "sysSource": sysSource,
       "sysAttributeSelect": sysAttributeSelect,
       "sysTimeSetup": sysTimeSetup,
       "sysTimeServerMode": sysTimeServerMode,
       "sysTimeServerIPType": sysTimeServerIPType,
       "sysTimeServerIP": sysTimeServerIP,
       "sysTimeSystemTime": sysTimeSystemTime,
       "sysTimeSystemDate": sysTimeSystemDate,
       "sysTimeSystemTimeZone": sysTimeSystemTimeZone,
       "sysTimeServerSynchronize": sysTimeServerSynchronize,
       "sysTimeDaylightSaveEnable": sysTimeDaylightSaveEnable,
       "sysTimeDaylightSaveStartDateWeek": sysTimeDaylightSaveStartDateWeek,
       "sysTimeDaylightSaveStartDateDay": sysTimeDaylightSaveStartDateDay,
       "sysTimeDaylightSaveStartDateMonth": sysTimeDaylightSaveStartDateMonth,
       "sysTimeDaylightSaveStartDateClock": sysTimeDaylightSaveStartDateClock,
       "sysTimeDaylightSaveEndDateWeek": sysTimeDaylightSaveEndDateWeek,
       "sysTimeDaylightSaveEndDateDay": sysTimeDaylightSaveEndDateDay,
       "sysTimeDaylightSaveEndDateMonth": sysTimeDaylightSaveEndDateMonth,
       "sysTimeDaylightSaveEndDateClock": sysTimeDaylightSaveEndDateClock,
       "sysTimeServerLastSynchronizeStatus": sysTimeServerLastSynchronizeStatus,
       "sysTimeServerLastSynchronizeTime": sysTimeServerLastSynchronizeTime,
       "sysPmSync": sysPmSync,
       "sysPmSyncUrl": sysPmSyncUrl,
       "sysPmSyncEnable": sysPmSyncEnable,
       "sysPmSyncDelay": sysPmSyncDelay,
       "sysPmSyncStatus": sysPmSyncStatus,
       "sysNniType": sysNniType,
       "aaa": aaa,
       "authen": authen,
       "loginMethod1": loginMethod1,
       "loginMethod2": loginMethod2,
       "loginMethod3": loginMethod3,
       "enableMethod1": enableMethod1,
       "enableMethod2": enableMethod2,
       "enableMethod3": enableMethod3,
       "acct": acct,
       "systemMethod": systemMethod,
       "execMethod": execMethod,
       "execMode": execMode,
       "commandsPrivilege": commandsPrivilege,
       "updatePeriod": updatePeriod,
       "commandsMethod": commandsMethod,
       "author": author,
       "authorPrivModeTable": authorPrivModeTable,
       "authorPrivModeEntry": authorPrivModeEntry,
       "authorPrivilege": authorPrivilege,
       "authorMode": authorMode,
       "radius": radius,
       "radiusAuthen": radiusAuthen,
       "radiusAuthenRedundantMode": radiusAuthenRedundantMode,
       "radiusAuthenTimeoutPeriod": radiusAuthenTimeoutPeriod,
       "radiusAuthenServerTable": radiusAuthenServerTable,
       "radiusAuthenServerEntry": radiusAuthenServerEntry,
       "radiusAuthenServerIndex": radiusAuthenServerIndex,
       "radiusAuthenServerIP": radiusAuthenServerIP,
       "radiusAuthenServerPort": radiusAuthenServerPort,
       "radiusAuthenServerSecret": radiusAuthenServerSecret,
       "radiusAcct": radiusAcct,
       "radiusAcctRedundantMode": radiusAcctRedundantMode,
       "radiusAcctTimeoutPeriod": radiusAcctTimeoutPeriod,
       "radiusAcctServerTable": radiusAcctServerTable,
       "radiusAcctServerEntry": radiusAcctServerEntry,
       "radiusAcctServerIndex": radiusAcctServerIndex,
       "radiusAcctServerIP": radiusAcctServerIP,
       "radiusAcctServerPort": radiusAcctServerPort,
       "radiusAcctServerSecret": radiusAcctServerSecret,
       "tacacsplus": tacacsplus,
       "tacacsplusAuthen": tacacsplusAuthen,
       "tacacsplusAuthenRedundantMode": tacacsplusAuthenRedundantMode,
       "tacacsplusAuthenTimeoutPeriod": tacacsplusAuthenTimeoutPeriod,
       "tacacsplusAuthenServerTable": tacacsplusAuthenServerTable,
       "tacacsplusAuthenServerEntry": tacacsplusAuthenServerEntry,
       "tacscsplusAuthenServerIndex": tacscsplusAuthenServerIndex,
       "tacscsplusAuthenServerIP": tacscsplusAuthenServerIP,
       "tacscsplusAuthenServerPort": tacscsplusAuthenServerPort,
       "tacscsplusAuthenServerSecret": tacscsplusAuthenServerSecret,
       "tacacsplusAcct": tacacsplusAcct,
       "tacacsplusAcctRedundantMode": tacacsplusAcctRedundantMode,
       "tacacsplusAcctTimeoutPeriod": tacacsplusAcctTimeoutPeriod,
       "tacacsplusAcctServerTable": tacacsplusAcctServerTable,
       "tacacsplusAcctServerEntry": tacacsplusAcctServerEntry,
       "tacacsplusAcctServerIndex": tacacsplusAcctServerIndex,
       "tacacsplusAcctServerIP": tacacsplusAcctServerIP,
       "tacacsplusAcctServerPort": tacacsplusAcctServerPort,
       "tacacsplusAcctServerSecret": tacacsplusAcctServerSecret,
       "tacacsplusAuthor": tacacsplusAuthor,
       "tacacsplusAuthorRedundantMode": tacacsplusAuthorRedundantMode,
       "tacacsplusAuthorTimeoutPeriod": tacacsplusAuthorTimeoutPeriod,
       "tacacsplusAuthorServerTable": tacacsplusAuthorServerTable,
       "tacacsplusAuthorServerEntry": tacacsplusAuthorServerEntry,
       "tacacsplusAuthorServerIndex": tacacsplusAuthorServerIndex,
       "tacacsplusAuthorServerIP": tacacsplusAuthorServerIP,
       "tacacsplusAuthorServerPort": tacacsplusAuthorServerPort,
       "tacacsplusAuthorServerSecret": tacacsplusAuthorServerSecret,
       "sysPowerSource": sysPowerSource,
       "sysLoginMessage": sysLoginMessage,
       "sysConfiglog": sysConfiglog,
       "sysConfigLastChangeTime": sysConfigLastChangeTime,
       "sysConfigLastChangeSession": sysConfigLastChangeSession,
       "sysConfigLastChangeUser": sysConfigLastChangeUser,
       "sysConfigLastChangeLocation": sysConfigLastChangeLocation,
       "sysReboot": sysReboot,
       "sysRebootAction": sysRebootAction,
       "sysRebootTimer": sysRebootTimer,
       "vdsl": vdsl,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter,
       "seltLoopTerminal": seltLoopTerminal,
       "seltAttenuation180khz": seltAttenuation180khz,
       "seltAttenuation300khz": seltAttenuation300khz,
       "vdslOps": vdslOps,
       "vdslTarget": vdslTarget,
       "vdslOperation": vdslOperation,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortAlarmProf": subrPortAlarmProf,
       "vdsl2Profile": vdsl2Profile,
       "vdsl2LineConfProfileExtendedTable": vdsl2LineConfProfileExtendedTable,
       "vdsl2LineConfProfileExtendedEntry": vdsl2LineConfProfileExtendedEntry,
       "vdsl2LineConfProfileDpboEPsdID": vdsl2LineConfProfileDpboEPsdID,
       "vdsl2LineConfProfileBitSwapDs": vdsl2LineConfProfileBitSwapDs,
       "vdsl2LineConfProfileBitSwapUs": vdsl2LineConfProfileBitSwapUs,
       "vdsl2LineConfProfileTransmissionType": vdsl2LineConfProfileTransmissionType,
       "vdsl2LineConfProfileProfileName": vdsl2LineConfProfileProfileName,
       "vdsl2LineAlarmConfProfileExtendedTable": vdsl2LineAlarmConfProfileExtendedTable,
       "vdsl2LineAlarmConfProfileExtendedEntry": vdsl2LineAlarmConfProfileExtendedEntry,
       "vdsl2LineAlarmConfProfileXtucThresh15MinLofs": vdsl2LineAlarmConfProfileXtucThresh15MinLofs,
       "vdsl2LineAlarmConfProfileXturThresh15MinLofs": vdsl2LineAlarmConfProfileXturThresh15MinLofs,
       "vdsl2LineAlarmConfProfileXturThresh15MinLprs": vdsl2LineAlarmConfProfileXturThresh15MinLprs,
       "vdsl2LineAlarmConfProfileProfileName": vdsl2LineAlarmConfProfileProfileName,
       "vdsl2ChanConfProfileExtendedTable": vdsl2ChanConfProfileExtendedTable,
       "vdsl2ChanConfProfileExtendedEntry": vdsl2ChanConfProfileExtendedEntry,
       "vdsl2ChanConfProfilePhyRDs": vdsl2ChanConfProfilePhyRDs,
       "vdsl2ChanConfProfilePhyRUs": vdsl2ChanConfProfilePhyRUs,
       "vdsl2ChanConfProfileProfileName": vdsl2ChanConfProfileProfileName,
       "vdsl2Stats": vdsl2Stats,
       "xdsl2LineBandExtendedTable": xdsl2LineBandExtendedTable,
       "xdsl2LineBandExtendedEntry": xdsl2LineBandExtendedEntry,
       "xdsl2LineBandTxPower": xdsl2LineBandTxPower,
       "xdsl2PMExtended": xdsl2PMExtended,
       "xdsl2PMLineExtended": xdsl2PMLineExtended,
       "xdsl2PMLineCurrExtendedTable": xdsl2PMLineCurrExtendedTable,
       "xdsl2PMLineCurrExtendedEntry": xdsl2PMLineCurrExtendedEntry,
       "xdsl2PMLCurrUnit": xdsl2PMLCurrUnit,
       "xdsl2PMLCurr15MLofs": xdsl2PMLCurr15MLofs,
       "xdsl2PMLCurr1DayLofs": xdsl2PMLCurr1DayLofs,
       "xdsl2PMLineInitCurrExtendedTable": xdsl2PMLineInitCurrExtendedTable,
       "xdsl2PMLineInitCurrExtendedEntry": xdsl2PMLineInitCurrExtendedEntry,
       "xdsl2PMLInitCurr15MLols": xdsl2PMLInitCurr15MLols,
       "xdsl2PMLInitCurr15MLol": xdsl2PMLInitCurr15MLol,
       "xdsl2PMLInitCurr15MLprs": xdsl2PMLInitCurr15MLprs,
       "xdsl2PMLInitCurr15MLpr": xdsl2PMLInitCurr15MLpr,
       "xdsl2PMLInitCurr1DayLols": xdsl2PMLInitCurr1DayLols,
       "xdsl2PMLInitCurr1DayLol": xdsl2PMLInitCurr1DayLol,
       "xdsl2PMLInitCurr1DayLprs": xdsl2PMLInitCurr1DayLprs,
       "xdsl2PMLInitCurr1DayLpr": xdsl2PMLInitCurr1DayLpr,
       "xdsl2PMLineHist15MinExtendedTable": xdsl2PMLineHist15MinExtendedTable,
       "xdsl2PMLineHist15MinExtendedEntry": xdsl2PMLineHist15MinExtendedEntry,
       "xdsl2PMLHist15MUnit": xdsl2PMLHist15MUnit,
       "xdsl2PMLHist15MInterval": xdsl2PMLHist15MInterval,
       "xdsl2PMLHist15MLofs": xdsl2PMLHist15MLofs,
       "xdsl2PMLineHist1DayExtendedTable": xdsl2PMLineHist1DayExtendedTable,
       "xdsl2PMLineHist1DayExtendedEntry": xdsl2PMLineHist1DayExtendedEntry,
       "xdsl2PMLHist1DUnit": xdsl2PMLHist1DUnit,
       "xdsl2PMLHist1DInterval": xdsl2PMLHist1DInterval,
       "xdsl2PMLHist1DLofs": xdsl2PMLHist1DLofs,
       "xdsl2PMLineInitHist15MinExtendedTable": xdsl2PMLineInitHist15MinExtendedTable,
       "xdsl2PMLineInitHist15MinExtendedEntry": xdsl2PMLineInitHist15MinExtendedEntry,
       "xdsl2PMLInitHist15MInterval": xdsl2PMLInitHist15MInterval,
       "xdsl2PMLInitHist15MLols": xdsl2PMLInitHist15MLols,
       "xdsl2PMLInitHist15MLol": xdsl2PMLInitHist15MLol,
       "xdsl2PMLInitHist15MLprs": xdsl2PMLInitHist15MLprs,
       "xdsl2PMLInitHist15MLpr": xdsl2PMLInitHist15MLpr,
       "xdsl2PMLineInitHist1DayExtendedTable": xdsl2PMLineInitHist1DayExtendedTable,
       "xdsl2PMLineInitHist1DayExtendedEntry": xdsl2PMLineInitHist1DayExtendedEntry,
       "xdsl2PMLInitHist1DInterval": xdsl2PMLInitHist1DInterval,
       "xdsl2PMLInitHist1DLols": xdsl2PMLInitHist1DLols,
       "xdsl2PMLInitHist1DLol": xdsl2PMLInitHist1DLol,
       "xdsl2PMLInitHist1DLprs": xdsl2PMLInitHist1DLprs,
       "xdsl2PMLInitHist1DLpr": xdsl2PMLInitHist1DLpr,
       "xdsl2PMChannelExtended": xdsl2PMChannelExtended,
       "xdsl2PMChCurrExtendedTable": xdsl2PMChCurrExtendedTable,
       "xdsl2PMChCurrExtendedEntry": xdsl2PMChCurrExtendedEntry,
       "xdsl2PMChCurrUnit": xdsl2PMChCurrUnit,
       "xdsl2PMChCurr15MUncorrectBlocks": xdsl2PMChCurr15MUncorrectBlocks,
       "xdsl2PMChCurr1DayUncorrectBlocks": xdsl2PMChCurr1DayUncorrectBlocks,
       "xdsl2PMChHist15MinExtendedTable": xdsl2PMChHist15MinExtendedTable,
       "xdsl2PMChHist15MinExtendedEntry": xdsl2PMChHist15MinExtendedEntry,
       "xdsl2PMChHist15MUnit": xdsl2PMChHist15MUnit,
       "xdsl2PMChHist15MInterval": xdsl2PMChHist15MInterval,
       "xdsl2PMChHist15MUncorrectBlocks": xdsl2PMChHist15MUncorrectBlocks,
       "xdsl2PMChHist1DExtendedTable": xdsl2PMChHist1DExtendedTable,
       "xdsl2PMChHist1DExtendedEntry": xdsl2PMChHist1DExtendedEntry,
       "xdsl2PMChHist1DUnit": xdsl2PMChHist1DUnit,
       "xdsl2PMChHist1DInterval": xdsl2PMChHist1DInterval,
       "xdsl2PMChHist1DUncorrectBlocks": xdsl2PMChHist1DUncorrectBlocks,
       "xdsl2LineStatusTable": xdsl2LineStatusTable,
       "xdsl2LineStatusEntry": xdsl2LineStatusEntry,
       "xdsl2LineStatus": xdsl2LineStatus,
       "xdsl2LineProtocol": xdsl2LineProtocol,
       "xdsl2LineUptime": xdsl2LineUptime,
       "xdsl2LineTxRate": xdsl2LineTxRate,
       "xdsl2LineRxRate": xdsl2LineRxRate,
       "ldm": ldm,
       "xdsl2ExtendedStatus": xdsl2ExtendedStatus,
       "xdsl2ExtendedSCStatusTable": xdsl2ExtendedSCStatusTable,
       "xdsl2ExtendedSCStatusEntry": xdsl2ExtendedSCStatusEntry,
       "xdsl2SCStatusActAtp": xdsl2SCStatusActAtp,
       "xdsl2ExtendedSCStatusBandTable": xdsl2ExtendedSCStatusBandTable,
       "xdsl2ExtendedSCStatusBandEntry": xdsl2ExtendedSCStatusBandEntry,
       "xdsl2SCStatusBandSnrMargin": xdsl2SCStatusBandSnrMargin,
       "forcePortSettingTable": forcePortSettingTable,
       "forcePortSettingEntry": forcePortSettingEntry,
       "forcePortTransType": forcePortTransType,
       "forcePortAnnexM": forcePortAnnexM,
       "forcePortAnnexL": forcePortAnnexL,
       "forcePortAnnexI": forcePortAnnexI,
       "forcePortAnnexJ": forcePortAnnexJ,
       "forcePortPmMode": forcePortPmMode,
       "forcePortL0Time": forcePortL0Time,
       "forcePortL2Time": forcePortL2Time,
       "forcePortL2PwrDnStep": forcePortL2PwrDnStep,
       "forcePortL2PwrDnMax": forcePortL2PwrDnMax,
       "forcePortTxPwrMode": forcePortTxPwrMode,
       "forcePortMinInpDs": forcePortMinInpDs,
       "forcePortMinInpUs": forcePortMinInpUs,
       "forcePortMaxUsTxPwr": forcePortMaxUsTxPwr,
       "forcePortMaxDsTxPwr": forcePortMaxDsTxPwr,
       "forcePortMaxUsRxPwr": forcePortMaxUsRxPwr,
       "xdslBonding": xdslBonding,
       "xdslBondingConfigTable": xdslBondingConfigTable,
       "xdslBondingConfigEntry": xdslBondingConfigEntry,
       "xdslBondingConfigName": xdslBondingConfigName,
       "xdslBondingConfigActive": xdslBondingConfigActive,
       "xdslBondingConfigMemberPort": xdslBondingConfigMemberPort,
       "xdslBondingConfigMode": xdslBondingConfigMode,
       "xdslBongingConfigLineTemp": xdslBongingConfigLineTemp,
       "xdslBondingConfigFallbackTemp": xdslBondingConfigFallbackTemp,
       "xdslBondingConfigRowStatus": xdslBondingConfigRowStatus,
       "xdslBondingStatusTable": xdslBondingStatusTable,
       "xdslBondingStatusEntry": xdslBondingStatusEntry,
       "xdslBondingStatusName": xdslBondingStatusName,
       "xdslBondingStatusActive": xdslBondingStatusActive,
       "xdslBondingStatusMemberPort": xdslBondingStatusMemberPort,
       "xdslBondingStatusActivePort": xdslBondingStatusActivePort,
       "xdslBondingStatusMainPort": xdslBondingStatusMainPort,
       "xdslBondingStatusTransferMode": xdslBondingStatusTransferMode,
       "xdslBondingStatusRateUs": xdslBondingStatusRateUs,
       "xdslBondingStatusRateDs": xdslBondingStatusRateDs,
       "xdslBondingCounterOps": xdslBondingCounterOps,
       "xdslBondingCounterTarget": xdslBondingCounterTarget,
       "xdslBondingCounterOperation": xdslBondingCounterOperation,
       "voip": voip,
       "mlt": mlt,
       "mltTarget": mltTarget,
       "mltOption": mltOption,
       "mltForce": mltForce,
       "mltOps": mltOps,
       "mltResultTable": mltResultTable,
       "mltResultEntry": mltResultEntry,
       "mltVacTip": mltVacTip,
       "mltVacRing": mltVacRing,
       "mltVacDiff": mltVacDiff,
       "mltVdcTip": mltVdcTip,
       "mltVdcRing": mltVdcRing,
       "mltVdcDiff": mltVdcDiff,
       "mltRLoop": mltRLoop,
       "mltRtg": mltRtg,
       "mltRrg": mltRrg,
       "mltRtr": mltRtr,
       "mltCtg": mltCtg,
       "mltCrg": mltCrg,
       "mltCtr": mltCtr,
       "mltRen": mltRen,
       "mltVRing": mltVRing,
       "mltVMetering": mltVMetering,
       "mltDialToneDetected": mltDialToneDetected,
       "mltDetectedDtmfCount": mltDetectedDtmfCount,
       "mltDialToneDelay": mltDialToneDelay,
       "mltReceiverOffHook": mltReceiverOffHook,
       "mltLoopRload": mltLoopRload,
       "mltLoopIMetallic": mltLoopIMetallic,
       "mltLoopVAB": mltLoopVAB,
       "mltLoopVBL": mltLoopVBL,
       "mltLoopVBH": mltLoopVBH,
       "mltRrev": mltRrev,
       "mltDetectedDtmfDigit": mltDetectedDtmfDigit,
       "mltOpsErrMsg": mltOpsErrMsg,
       "mltTargetType": mltTargetType,
       "h248": h248,
       "h248DigitMapTimeout": h248DigitMapTimeout,
       "h248DigitStartTimeout": h248DigitStartTimeout,
       "h248DigitShortTimeout": h248DigitShortTimeout,
       "h248DigitLongTimeout": h248DigitLongTimeout,
       "h248Dscp": h248Dscp,
       "h248Encode": h248Encode,
       "h248InactivityTimer": h248InactivityTimer,
       "h248Mg": h248Mg,
       "h248MgEnable": h248MgEnable,
       "h248MgName": h248MgName,
       "h248MgPort": h248MgPort,
       "h248MgState": h248MgState,
       "h248Mgc": h248Mgc,
       "h248MgcIpDn": h248MgcIpDn,
       "h248MgcPort": h248MgcPort,
       "h248Mgc2Enable": h248Mgc2Enable,
       "h248Mgc2IpDn": h248Mgc2IpDn,
       "h248Mgc2Port": h248Mgc2Port,
       "h248RetransmitTime": h248RetransmitTime,
       "h248RetransmitInitTime": h248RetransmitInitTime,
       "h248RetransmitMinTime": h248RetransmitMinTime,
       "h248RetransmitMaxTime": h248RetransmitMaxTime,
       "h248RetransmitWindow": h248RetransmitWindow,
       "h248Rfc2833": h248Rfc2833,
       "h248Rfc2833Enable": h248Rfc2833Enable,
       "h248Rfc2833Ptype": h248Rfc2833Ptype,
       "h248RtpStartPort": h248RtpStartPort,
       "h248RtpEndPort": h248RtpEndPort,
       "h248SoftSwitch": h248SoftSwitch,
       "h248T38Enable": h248T38Enable,
       "h248Transport": h248Transport,
       "h248VbdEnable": h248VbdEnable,
       "h248RtpTerminatetId": h248RtpTerminatetId,
       "h248RtpTerminateIdPrefix": h248RtpTerminateIdPrefix,
       "h248RtpTerminateIdSuffixStartNumber": h248RtpTerminateIdSuffixStartNumber,
       "h248RtpTerminateIdSuffixLen": h248RtpTerminateIdSuffixLen,
       "h248ForceVerEnable": h248ForceVerEnable,
       "h248RegisterRetry": h248RegisterRetry,
       "voipIp": voipIp,
       "voipIpAddress": voipIpAddress,
       "voipIpNetmask": voipIpNetmask,
       "voipIpVlanId": voipIpVlanId,
       "voipIpDefaultGateway": voipIpDefaultGateway,
       "voipIpDns": voipIpDns,
       "voipIpDhcpBootpEnable": voipIpDhcpBootpEnable,
       "voipIpDhcpOperation": voipIpDhcpOperation,
       "voipIpPbit": voipIpPbit,
       "voipIpDns2": voipIpDns2,
       "voipIpDns3": voipIpDns3,
       "voipPots": voipPots,
       "voipPotsHookFlashTimeEnable": voipPotsHookFlashTimeEnable,
       "voipPotsHookFlashMaxTime": voipPotsHookFlashMaxTime,
       "voipPotsHookFlashMinTime": voipPotsHookFlashMinTime,
       "voipPotsOffHookTimeEnable": voipPotsOffHookTimeEnable,
       "voipPotsOffHookTime": voipPotsOffHookTime,
       "voipPotsRingTable": voipPotsRingTable,
       "voipPotsRingEntry": voipPotsRingEntry,
       "voipPotsRingIndex": voipPotsRingIndex,
       "voipPotsRingName": voipPotsRingName,
       "voipPotsRingOn1": voipPotsRingOn1,
       "voipPotsRingOff1": voipPotsRingOff1,
       "voipPotsRingOn2": voipPotsRingOn2,
       "voipPotsRingOff2": voipPotsRingOff2,
       "voipPotsRingOn3": voipPotsRingOn3,
       "voipPotsRingOff3": voipPotsRingOff3,
       "voipPotsRingSetDefault": voipPotsRingSetDefault,
       "voipCountryCode": voipCountryCode,
       "voipMaxNumOfDspProfiles": voipMaxNumOfDspProfiles,
       "voipDspProfileTable": voipDspProfileTable,
       "voipDspProfileEntry": voipDspProfileEntry,
       "voipDspProfileName": voipDspProfileName,
       "voipDspProfileCodec": voipDspProfileCodec,
       "voipDspProfileDscp": voipDspProfileDscp,
       "voipDspProfileEchoTail": voipDspProfileEchoTail,
       "voipDspProfileEchoCancelEnable": voipDspProfileEchoCancelEnable,
       "voipDspProfileG711Vpi": voipDspProfileG711Vpi,
       "voipDspProfileG723Vpi": voipDspProfileG723Vpi,
       "voipDspProfileG726Vpi": voipDspProfileG726Vpi,
       "voipDspProfileG729Vpi": voipDspProfileG729Vpi,
       "voipDspProfilePbit": voipDspProfilePbit,
       "voipDspProfilePlayBufferMinDelay": voipDspProfilePlayBufferMinDelay,
       "voipDspProfilePlayBufferMaxDelay": voipDspProfilePlayBufferMaxDelay,
       "voipDspProfileVadEnable": voipDspProfileVadEnable,
       "voipDspProfileRowStatus": voipDspProfileRowStatus,
       "voipPortConfTable": voipPortConfTable,
       "voipPortConfEntry": voipPortConfEntry,
       "voipPortConfPortEnable": voipPortConfPortEnable,
       "voipPortConfDspProfile": voipPortConfDspProfile,
       "voipPortConfVbdDspProfile": voipPortConfVbdDspProfile,
       "voipPortConfVbdDspProfileEnable": voipPortConfVbdDspProfileEnable,
       "voipPortConfPotsBattery": voipPortConfPotsBattery,
       "voipPortConfPotsTxGain": voipPortConfPotsTxGain,
       "voipPortConfPotsRxGain": voipPortConfPotsRxGain,
       "voipPortConfVoiceTxGain": voipPortConfVoiceTxGain,
       "voipPortConfVoiceRxGain": voipPortConfVoiceRxGain,
       "voipPortConfPotsImpedance": voipPortConfPotsImpedance,
       "voipPortConfPotsImpedanceEnable": voipPortConfPotsImpedanceEnable,
       "voipPortConfH248TerminateId": voipPortConfH248TerminateId,
       "voipPortConfPmThreshProfile": voipPortConfPmThreshProfile,
       "voipPortConfPotsTax": voipPortConfPotsTax,
       "voipPortConfPotsLoopCurrent": voipPortConfPotsLoopCurrent,
       "voipPortConfTel": voipPortConfTel,
       "voipPortConfName": voipPortConfName,
       "voipPortConfSipCallSvcProfile": voipPortConfSipCallSvcProfile,
       "voipPortConfHotline": voipPortConfHotline,
       "voipPortConfHotlineTel": voipPortConfHotlineTel,
       "voipPortConfHotlineTimeout": voipPortConfHotlineTimeout,
       "voipPortConfAccount": voipPortConfAccount,
       "voipPortConfSipProfile": voipPortConfSipProfile,
       "voipPortConfPassword": voipPortConfPassword,
       "voipPortConfPotsLoopResistance": voipPortConfPotsLoopResistance,
       "voipPortConfPotsCidAsType": voipPortConfPotsCidAsType,
       "voipPortConfPotsCidPayloadType": voipPortConfPotsCidPayloadType,
       "voipPortConfPotsVmwiFormat": voipPortConfPotsVmwiFormat,
       "voipPortConfPotsHookFlashMaxTime": voipPortConfPotsHookFlashMaxTime,
       "voipPortConfPotsHookFlashMinTime": voipPortConfPotsHookFlashMinTime,
       "voipPortStatisticTable": voipPortStatisticTable,
       "voipPortStatisticEntry": voipPortStatisticEntry,
       "voipPortStatisticCurrCallTime": voipPortStatisticCurrCallTime,
       "voipPortStatisticTotalCallTime": voipPortStatisticTotalCallTime,
       "voipPortStatisticCallTimes": voipPortStatisticCallTimes,
       "voipPortStatisticTxRate": voipPortStatisticTxRate,
       "voipPortStatisticRxRate": voipPortStatisticRxRate,
       "voipPortStatisticTxPktCnt": voipPortStatisticTxPktCnt,
       "voipPortStatisticRxPktCnt": voipPortStatisticRxPktCnt,
       "voipPortStatisticTxFracLost": voipPortStatisticTxFracLost,
       "voipPortStatisticRxFracLost": voipPortStatisticRxFracLost,
       "voipPortStatisticTxJitter": voipPortStatisticTxJitter,
       "voipPortStatisticRxJitter": voipPortStatisticRxJitter,
       "voipPortStatisticTxAvgDelay": voipPortStatisticTxAvgDelay,
       "voipPortStatisticRxAvgDelay": voipPortStatisticRxAvgDelay,
       "voipPortLineStatusTable": voipPortLineStatusTable,
       "voipPortLineStatusEntry": voipPortLineStatusEntry,
       "voipPortLineStatusPhoneStatus": voipPortLineStatusPhoneStatus,
       "voipPortLineStatusServiceStatus": voipPortLineStatusServiceStatus,
       "voipPortLineInfoTable": voipPortLineInfoTable,
       "voipPortLineInfoEntry": voipPortLineInfoEntry,
       "voipPortLineInfoRtpTxCodecType": voipPortLineInfoRtpTxCodecType,
       "voipPortLineInfoRtpRxCodecType": voipPortLineInfoRtpRxCodecType,
       "voipPortLineInfoRtpTxPt": voipPortLineInfoRtpTxPt,
       "voipPortLineInfoRtpRxPt": voipPortLineInfoRtpRxPt,
       "voipPortLineInfoRtpLocalIp": voipPortLineInfoRtpLocalIp,
       "voipPortLineInfoRtpRemoteIp": voipPortLineInfoRtpRemoteIp,
       "voipPortLineInfoRtpLocalPort": voipPortLineInfoRtpLocalPort,
       "voipPortLineInfoRtpRemotePort": voipPortLineInfoRtpRemotePort,
       "voipOps": voipOps,
       "voipTarget": voipTarget,
       "voipClearOperation": voipClearOperation,
       "voipRtpIp": voipRtpIp,
       "voipRtpIpAddress": voipRtpIpAddress,
       "voipRtpIpNetmask": voipRtpIpNetmask,
       "voipRtpIpVlanId": voipRtpIpVlanId,
       "voipRtpIpDefaultGateway": voipRtpIpDefaultGateway,
       "voipRtpIpDhcpBootpEnable": voipRtpIpDhcpBootpEnable,
       "voipRtpIpDhcpOperation": voipRtpIpDhcpOperation,
       "voipRtpIpOperation": voipRtpIpOperation,
       "voipRtpIpPbit": voipRtpIpPbit,
       "voipH248Statistic": voipH248Statistic,
       "voipH248StatisticMsgSent": voipH248StatisticMsgSent,
       "voipH248StatisticMsgRecv": voipH248StatisticMsgRecv,
       "voipH248StatisticMsgLost": voipH248StatisticMsgLost,
       "voipH248StatisticMsgResent": voipH248StatisticMsgResent,
       "voipH248StatisticErrorMsg": voipH248StatisticErrorMsg,
       "voipH248StatisticUnIdentifiedMsg": voipH248StatisticUnIdentifiedMsg,
       "sip": sip,
       "maxNumOfSipProfiles": maxNumOfSipProfiles,
       "sipProfileTable": sipProfileTable,
       "sipProfileEntry": sipProfileEntry,
       "sipProfileName": sipProfileName,
       "sipProfileSipSvr": sipProfileSipSvr,
       "sipProfileRegSvr": sipProfileRegSvr,
       "sipProfileProxySvr": sipProfileProxySvr,
       "sipProfileSipPort": sipProfileSipPort,
       "sipProfileRegSvrPort": sipProfileRegSvrPort,
       "sipProfileProxySvrPort": sipProfileProxySvrPort,
       "sipProfileUriType": sipProfileUriType,
       "sipProfileDscp": sipProfileDscp,
       "sipProfileKeepAlive": sipProfileKeepAlive,
       "sipProfilePrack": sipProfilePrack,
       "sipProfileRowStatus": sipProfileRowStatus,
       "sipProfileRtpStartPort": sipProfileRtpStartPort,
       "sipProfileRtpEndPort": sipProfileRtpEndPort,
       "sipProfileSwitchType": sipProfileSwitchType,
       "sipProfileKeepAliveTimeOut": sipProfileKeepAliveTimeOut,
       "sipProfileFailRetry": sipProfileFailRetry,
       "sipProfileRegTime": sipProfileRegTime,
       "sipProfileRegistration": sipProfileRegistration,
       "sipProfileDnsSvr": sipProfileDnsSvr,
       "sipProfileDualSvr": sipProfileDualSvr,
       "sipProfileSipSvr2": sipProfileSipSvr2,
       "sipProfileRegSvr2": sipProfileRegSvr2,
       "sipProfileProxySvr2": sipProfileProxySvr2,
       "sipProfileSipPort2": sipProfileSipPort2,
       "sipProfileRegSvrPort2": sipProfileRegSvrPort2,
       "sipProfileProxySvrPort2": sipProfileProxySvrPort2,
       "maxNumOfSipCallSvcProfiles": maxNumOfSipCallSvcProfiles,
       "sipCallSvcProfileTable": sipCallSvcProfileTable,
       "sipCallSvcProfileEntry": sipCallSvcProfileEntry,
       "sipCallSvcProfileName": sipCallSvcProfileName,
       "sipCallSvcProfileDialPlanOn": sipCallSvcProfileDialPlanOn,
       "sipCallSvcProfileDialPlanCc": sipCallSvcProfileDialPlanCc,
       "sipCallSvcProfileDialPlanNdc": sipCallSvcProfileDialPlanNdc,
       "sipCallSvcProfileDialPlanTable": sipCallSvcProfileDialPlanTable,
       "sipCallSvcProfileStateMask": sipCallSvcProfileStateMask,
       "sipCallSvcProfileDtmf": sipCallSvcProfileDtmf,
       "sipCallSvcProfileDtmfRfc2833PayloadType": sipCallSvcProfileDtmfRfc2833PayloadType,
       "sipCallSvcProfileFax": sipCallSvcProfileFax,
       "sipCallSvcProfileRowStatus": sipCallSvcProfileRowStatus,
       "sipCallSvcProfileKeypattern": sipCallSvcProfileKeypattern,
       "sipCallSvcProfileFlash": sipCallSvcProfileFlash,
       "sipCallSvcProfileFlashPattern": sipCallSvcProfileFlashPattern,
       "sipCallSvcProfileFirstDigit": sipCallSvcProfileFirstDigit,
       "sipCallSvcProfileInterDigit": sipCallSvcProfileInterDigit,
       "sipCallSvcProfileCentrex": sipCallSvcProfileCentrex,
       "maxNumOfSipDialPlan": maxNumOfSipDialPlan,
       "maxNumOfSipKeyPattern": maxNumOfSipKeyPattern,
       "sipDialPlanTable": sipDialPlanTable,
       "sipDialPlanEntry": sipDialPlanEntry,
       "sipDialPlanName": sipDialPlanName,
       "sipDialPlanRowStatus": sipDialPlanRowStatus,
       "sipDialPlanContentTable": sipDialPlanContentTable,
       "sipDialPlanContentEntry": sipDialPlanContentEntry,
       "sipDialPlanIndex": sipDialPlanIndex,
       "sipDialPlanPattern": sipDialPlanPattern,
       "sipDialPlanRule": sipDialPlanRule,
       "sipKeyPatternTable": sipKeyPatternTable,
       "sipKeyPatternEntry": sipKeyPatternEntry,
       "sipKeyPatternName": sipKeyPatternName,
       "sipKeyPatternRowStatus": sipKeyPatternRowStatus,
       "sipKeyPatternContentTable": sipKeyPatternContentTable,
       "sipKeyPatternContentEntry": sipKeyPatternContentEntry,
       "sipKeyPatternServiceType": sipKeyPatternServiceType,
       "sipKeyPatternPattern": sipKeyPatternPattern,
       "voipSIPStatistic": voipSIPStatistic,
       "voipSIPStatisticMsgSent": voipSIPStatisticMsgSent,
       "voipSIPStatisticMsgRecv": voipSIPStatisticMsgRecv,
       "voipSIPStatisticMsgLost": voipSIPStatisticMsgLost,
       "voipSIPStatisticMsgResent": voipSIPStatisticMsgResent,
       "voipSIPStatisticErrorMsg": voipSIPStatisticErrorMsg,
       "voipSIPStatisticUnIdentifiedMsg": voipSIPStatisticUnIdentifiedMsg,
       "voipProtocolMode": voipProtocolMode,
       "coa": coa,
       "coaConfIssueThreshold": coaConfIssueThreshold,
       "coaConfClearThreshold": coaConfClearThreshold,
       "coaConfSampleSeconds": coaConfSampleSeconds,
       "coaConfAnalyticMethod": coaConfAnalyticMethod,
       "cpuUtilizationTable": cpuUtilizationTable,
       "cpuUtilizationEntry": cpuUtilizationEntry,
       "cpuSecondIndex": cpuSecondIndex,
       "cpuValue": cpuValue,
       "pm": pm,
       "gePmCurr15minTable": gePmCurr15minTable,
       "gePmCurr15minEntry": gePmCurr15minEntry,
       "gePmCurr15minElapsed": gePmCurr15minElapsed,
       "gePmCurr15minTxOctets": gePmCurr15minTxOctets,
       "gePmCurr15minTxPkts": gePmCurr15minTxPkts,
       "gePmCurr15minTxBroadcastPkts": gePmCurr15minTxBroadcastPkts,
       "gePmCurr15minTxMulticastPkts": gePmCurr15minTxMulticastPkts,
       "gePmCurr15minRxOctets": gePmCurr15minRxOctets,
       "gePmCurr15minRxPkts": gePmCurr15minRxPkts,
       "gePmCurr15minRxBroadcastPkts": gePmCurr15minRxBroadcastPkts,
       "gePmCurr15minRxMulticastPkts": gePmCurr15minRxMulticastPkts,
       "gePmCurr15minRxCRCAlignErrors": gePmCurr15minRxCRCAlignErrors,
       "gePmCurr15minRxUndersizePkts": gePmCurr15minRxUndersizePkts,
       "gePmCurr15minRxOversizePkts": gePmCurr15minRxOversizePkts,
       "gePmCurr15minRxFragments": gePmCurr15minRxFragments,
       "gePmCurr15minCollisions": gePmCurr15minCollisions,
       "gePmCurr15minPkts64Octets": gePmCurr15minPkts64Octets,
       "gePmCurr15minPkts65to127Octets": gePmCurr15minPkts65to127Octets,
       "gePmCurr15minPkts128to255Octets": gePmCurr15minPkts128to255Octets,
       "gePmCurr15minPkts256to511Octets": gePmCurr15minPkts256to511Octets,
       "gePmCurr15minPkts512to1023Octets": gePmCurr15minPkts512to1023Octets,
       "gePmCurr15minPkts1024to1518Octets": gePmCurr15minPkts1024to1518Octets,
       "gePmCurr15minPkts1519to1522Octets": gePmCurr15minPkts1519to1522Octets,
       "gePmHist15minTable": gePmHist15minTable,
       "gePmHist15minEntry": gePmHist15minEntry,
       "gePmHist15minIndex": gePmHist15minIndex,
       "gePmHist15minElapsed": gePmHist15minElapsed,
       "gePmHist15minTxOctets": gePmHist15minTxOctets,
       "gePmHist15minTxPkts": gePmHist15minTxPkts,
       "gePmHist15minTxBroadcastPkts": gePmHist15minTxBroadcastPkts,
       "gePmHist15minTxMulticastPkts": gePmHist15minTxMulticastPkts,
       "gePmHist15minRxOctets": gePmHist15minRxOctets,
       "gePmHist15minRxPkts": gePmHist15minRxPkts,
       "gePmHist15minRxBroadcastPkts": gePmHist15minRxBroadcastPkts,
       "gePmHist15minRxMulticastPkts": gePmHist15minRxMulticastPkts,
       "gePmHist15minRxCRCAlignErrors": gePmHist15minRxCRCAlignErrors,
       "gePmHist15minRxUndersizePkts": gePmHist15minRxUndersizePkts,
       "gePmHist15minRxOversizePkts": gePmHist15minRxOversizePkts,
       "gePmHist15minRxFragments": gePmHist15minRxFragments,
       "gePmHist15minCollisions": gePmHist15minCollisions,
       "gePmHist15minPkts64Octets": gePmHist15minPkts64Octets,
       "gePmHist15minPkts65to127Octets": gePmHist15minPkts65to127Octets,
       "gePmHist15minPkts128to255Octets": gePmHist15minPkts128to255Octets,
       "gePmHist15minPkts256to511Octets": gePmHist15minPkts256to511Octets,
       "gePmHist15minPkts512to1023Octets": gePmHist15minPkts512to1023Octets,
       "gePmHist15minPkts1024to1518Octets": gePmHist15minPkts1024to1518Octets,
       "gePmHist15minPkts1519to1522Octets": gePmHist15minPkts1519to1522Octets,
       "gePmHist15minStartTime": gePmHist15minStartTime,
       "gePmHist15minEndTime": gePmHist15minEndTime,
       "gePmCurr1dayTable": gePmCurr1dayTable,
       "gePmCurr1dayEntry": gePmCurr1dayEntry,
       "gePmCurr1dayElapsed": gePmCurr1dayElapsed,
       "gePmCurr1dayTxOctets": gePmCurr1dayTxOctets,
       "gePmCurr1dayTxPkts": gePmCurr1dayTxPkts,
       "gePmCurr1dayTxBroadcastPkts": gePmCurr1dayTxBroadcastPkts,
       "gePmCurr1dayTxMulticastPkts": gePmCurr1dayTxMulticastPkts,
       "gePmCurr1dayRxOctets": gePmCurr1dayRxOctets,
       "gePmCurr1dayRxPkts": gePmCurr1dayRxPkts,
       "gePmCurr1dayRxBroadcastPkts": gePmCurr1dayRxBroadcastPkts,
       "gePmCurr1dayRxMulticastPkts": gePmCurr1dayRxMulticastPkts,
       "gePmCurr1dayRxCRCAlignErrors": gePmCurr1dayRxCRCAlignErrors,
       "gePmCurr1dayRxUndersizePkts": gePmCurr1dayRxUndersizePkts,
       "gePmCurr1dayRxOversizePkts": gePmCurr1dayRxOversizePkts,
       "gePmCurr1dayRxFragments": gePmCurr1dayRxFragments,
       "gePmCurr1dayCollisions": gePmCurr1dayCollisions,
       "gePmCurr1dayPkts64Octets": gePmCurr1dayPkts64Octets,
       "gePmCurr1dayPkts65to127Octets": gePmCurr1dayPkts65to127Octets,
       "gePmCurr1dayPkts128to255Octets": gePmCurr1dayPkts128to255Octets,
       "gePmCurr1dayPkts256to511Octets": gePmCurr1dayPkts256to511Octets,
       "gePmCurr1dayPkts512to1023Octets": gePmCurr1dayPkts512to1023Octets,
       "gePmCurr1dayPkts1024to1518Octets": gePmCurr1dayPkts1024to1518Octets,
       "gePmCurr1dayPkts1519to1522Octets": gePmCurr1dayPkts1519to1522Octets,
       "gePmHist1dayTable": gePmHist1dayTable,
       "gePmHist1dayEntry": gePmHist1dayEntry,
       "gePmHist1dayIndex": gePmHist1dayIndex,
       "gePmHist1dayStartTime": gePmHist1dayStartTime,
       "gePmHist1dayEndTime": gePmHist1dayEndTime,
       "gePmHist1dayTxOctets": gePmHist1dayTxOctets,
       "gePmHist1dayTxPkts": gePmHist1dayTxPkts,
       "gePmHist1dayTxBroadcastPkts": gePmHist1dayTxBroadcastPkts,
       "gePmHist1dayTxMulticastPkts": gePmHist1dayTxMulticastPkts,
       "gePmHist1dayRxOctets": gePmHist1dayRxOctets,
       "gePmHist1dayRxPkts": gePmHist1dayRxPkts,
       "gePmHist1dayRxBroadcastPkts": gePmHist1dayRxBroadcastPkts,
       "gePmHist1dayRxMulticastPkts": gePmHist1dayRxMulticastPkts,
       "gePmHist1dayRxCRCAlignErrors": gePmHist1dayRxCRCAlignErrors,
       "gePmHist1dayRxUndersizePkts": gePmHist1dayRxUndersizePkts,
       "gePmHist1dayRxOversizePkts": gePmHist1dayRxOversizePkts,
       "gePmHist1dayRxFragments": gePmHist1dayRxFragments,
       "gePmHist1dayCollisions": gePmHist1dayCollisions,
       "gePmHist1dayPkts64Octets": gePmHist1dayPkts64Octets,
       "gePmHist1dayPkts65to127Octets": gePmHist1dayPkts65to127Octets,
       "gePmHist1dayPkts128to255Octets": gePmHist1dayPkts128to255Octets,
       "gePmHist1dayPkts256to511Octets": gePmHist1dayPkts256to511Octets,
       "gePmHist1dayPkts512to1023Octets": gePmHist1dayPkts512to1023Octets,
       "gePmHist1dayPkts1024to1518Octets": gePmHist1dayPkts1024to1518Octets,
       "gePmHist1dayPkts1519to1522Octets": gePmHist1dayPkts1519to1522Octets,
       "gePmThreshProfTable": gePmThreshProfTable,
       "gePmThreshProfEntry": gePmThreshProfEntry,
       "gePmThreshProfName": gePmThreshProfName,
       "gePmThreshProfTxOctets": gePmThreshProfTxOctets,
       "gePmThreshProfTxPkts": gePmThreshProfTxPkts,
       "gePmThreshProfTxBroadcastPkts": gePmThreshProfTxBroadcastPkts,
       "gePmThreshProfTxMulticastPkts": gePmThreshProfTxMulticastPkts,
       "gePmThreshProfRxOctets": gePmThreshProfRxOctets,
       "gePmThreshProfRxPkts": gePmThreshProfRxPkts,
       "gePmThreshProfRxBroadcastPkts": gePmThreshProfRxBroadcastPkts,
       "gePmThreshProfRxMulticastPkts": gePmThreshProfRxMulticastPkts,
       "gePmThreshProfRxCRCAlignErrors": gePmThreshProfRxCRCAlignErrors,
       "gePmThreshProfRxUndersizePkts": gePmThreshProfRxUndersizePkts,
       "gePmThreshProfRxOversizePkts": gePmThreshProfRxOversizePkts,
       "gePmThreshProfRxFragments": gePmThreshProfRxFragments,
       "gePmThreshProfCollisions": gePmThreshProfCollisions,
       "gePmThreshProfPkts64Octets": gePmThreshProfPkts64Octets,
       "gePmThreshProfPkts65to127Octets": gePmThreshProfPkts65to127Octets,
       "gePmThreshProfPkts128to255Octets": gePmThreshProfPkts128to255Octets,
       "gePmThreshProfPkts256to511Octets": gePmThreshProfPkts256to511Octets,
       "gePmThreshProfPkts512to1023Octets": gePmThreshProfPkts512to1023Octets,
       "gePmThreshProfPkts1024to1518Octets": gePmThreshProfPkts1024to1518Octets,
       "gePmThreshProfPkts1519to1522Octets": gePmThreshProfPkts1519to1522Octets,
       "gePmThreshProfRowStatus": gePmThreshProfRowStatus,
       "fxsPmCurr15minTable": fxsPmCurr15minTable,
       "fxsPmCurr15minEntry": fxsPmCurr15minEntry,
       "fxsPmCurr15minElapsed": fxsPmCurr15minElapsed,
       "fxsPmCurr15minRtpElapsedTime": fxsPmCurr15minRtpElapsedTime,
       "fxsPmCurr15minRtpTxBytes": fxsPmCurr15minRtpTxBytes,
       "fxsPmCurr15minRtpRxBytes": fxsPmCurr15minRtpRxBytes,
       "fxsPmCurr15minRtpTxPackets": fxsPmCurr15minRtpTxPackets,
       "fxsPmCurr15minRtpRxPackets": fxsPmCurr15minRtpRxPackets,
       "fxsPmCurr15minRtpTxLostPackets": fxsPmCurr15minRtpTxLostPackets,
       "fxsPmCurr15minRtpRxLostPackets": fxsPmCurr15minRtpRxLostPackets,
       "fxsPmHist15minTable": fxsPmHist15minTable,
       "fxsPmHist15minEntry": fxsPmHist15minEntry,
       "fxsPmHist15minIndex": fxsPmHist15minIndex,
       "fxsPmHist15minStartTime": fxsPmHist15minStartTime,
       "fxsPmHist15minEndTime": fxsPmHist15minEndTime,
       "fxsPmHist15minRtpElapsedTime": fxsPmHist15minRtpElapsedTime,
       "fxsPmHist15minRtpTxBytes": fxsPmHist15minRtpTxBytes,
       "fxsPmHist15minRtpRxBytes": fxsPmHist15minRtpRxBytes,
       "fxsPmHist15minRtpTxPackets": fxsPmHist15minRtpTxPackets,
       "fxsPmHist15minRtpRxPackets": fxsPmHist15minRtpRxPackets,
       "fxsPmHist15minRtpTxLostPackets": fxsPmHist15minRtpTxLostPackets,
       "fxsPmHist15minRtpRxLostPackets": fxsPmHist15minRtpRxLostPackets,
       "fxsPmCurr1dayTable": fxsPmCurr1dayTable,
       "fxsPmCurr1dayEntry": fxsPmCurr1dayEntry,
       "fxsPmCurr1dayElapsed": fxsPmCurr1dayElapsed,
       "fxsPmCurr1dayRtpElapsedTime": fxsPmCurr1dayRtpElapsedTime,
       "fxsPmCurr1dayRtpTxBytes": fxsPmCurr1dayRtpTxBytes,
       "fxsPmCurr1dayRtpRxBytes": fxsPmCurr1dayRtpRxBytes,
       "fxsPmCurr1dayRtpTxPackets": fxsPmCurr1dayRtpTxPackets,
       "fxsPmCurr1dayRtpRxPackets": fxsPmCurr1dayRtpRxPackets,
       "fxsPmCurr1dayRtpTxLostPackets": fxsPmCurr1dayRtpTxLostPackets,
       "fxsPmCurr1dayRtpRxLostPackets": fxsPmCurr1dayRtpRxLostPackets,
       "fxsPmHist1dayTable": fxsPmHist1dayTable,
       "fxsPmHist1dayEntry": fxsPmHist1dayEntry,
       "fxsPmHist1dayIndex": fxsPmHist1dayIndex,
       "fxsPmHist1dayStartTime": fxsPmHist1dayStartTime,
       "fxsPmHist1dayEndTime": fxsPmHist1dayEndTime,
       "fxsPmHist1dayRtpElapsedTime": fxsPmHist1dayRtpElapsedTime,
       "fxsPmHist1dayRtpTxBytes": fxsPmHist1dayRtpTxBytes,
       "fxsPmHist1dayRtpRxBytes": fxsPmHist1dayRtpRxBytes,
       "fxsPmHist1dayRtpTxPackets": fxsPmHist1dayRtpTxPackets,
       "fxsPmHist1dayRtpRxPackets": fxsPmHist1dayRtpRxPackets,
       "fxsPmHist1dayRtpTxLostPackets": fxsPmHist1dayRtpTxLostPackets,
       "fxsPmHist1dayRtpRxLostPackets": fxsPmHist1dayRtpRxLostPackets,
       "fxsPmThreshProfTable": fxsPmThreshProfTable,
       "fxsPmThreshProfEntry": fxsPmThreshProfEntry,
       "fxsPmThreshProfName": fxsPmThreshProfName,
       "fxsPmThreshProfRtpElapsedTime": fxsPmThreshProfRtpElapsedTime,
       "fxsPmThreshProfRtpTxBytes": fxsPmThreshProfRtpTxBytes,
       "fxsPmThreshProfRtpRxBytes": fxsPmThreshProfRtpRxBytes,
       "fxsPmThreshProfRtpTxPackets": fxsPmThreshProfRtpTxPackets,
       "fxsPmThreshProfRtpRxPackets": fxsPmThreshProfRtpRxPackets,
       "fxsPmThreshProfRtpTxLostPackets": fxsPmThreshProfRtpTxLostPackets,
       "fxsPmThreshProfRtpRxLostPackets": fxsPmThreshProfRtpRxLostPackets,
       "fxsPmThreshProfRowStatus": fxsPmThreshProfRowStatus,
       "gePmCurrStatisticTable": gePmCurrStatisticTable,
       "gePmCurrStatisticEntry": gePmCurrStatisticEntry,
       "gePmCurrStatisticTxOctets": gePmCurrStatisticTxOctets,
       "gePmCurrStatisticTxPkts": gePmCurrStatisticTxPkts,
       "gePmCurrStatisticTxBroadcastPkts": gePmCurrStatisticTxBroadcastPkts,
       "gePmCurrStatisticTxMulticastPkts": gePmCurrStatisticTxMulticastPkts,
       "gePmCurrStatisticRxOctets": gePmCurrStatisticRxOctets,
       "gePmCurrStatisticRxPkts": gePmCurrStatisticRxPkts,
       "gePmCurrStatisticRxBroadcastPkts": gePmCurrStatisticRxBroadcastPkts,
       "gePmCurrStatisticRxMulticastPkts": gePmCurrStatisticRxMulticastPkts,
       "gePmCurrStatisticRxCRCAlignErrors": gePmCurrStatisticRxCRCAlignErrors,
       "gePmCurrStatisticRxUndersizePkts": gePmCurrStatisticRxUndersizePkts,
       "gePmCurrStatisticRxOversizePkts": gePmCurrStatisticRxOversizePkts,
       "gePmCurrStatisticRxFragments": gePmCurrStatisticRxFragments,
       "gePmCurrStatisticCollisions": gePmCurrStatisticCollisions,
       "gePmCurrStatisticPkts64Octets": gePmCurrStatisticPkts64Octets,
       "gePmCurrStatisticPkts65to127Octets": gePmCurrStatisticPkts65to127Octets,
       "gePmCurrStatisticPkts128to255Octets": gePmCurrStatisticPkts128to255Octets,
       "gePmCurrStatisticPkts256to511Octets": gePmCurrStatisticPkts256to511Octets,
       "gePmCurrStatisticPkts512to1023Octets": gePmCurrStatisticPkts512to1023Octets,
       "gePmCurrStatisticPkts1024to1518Octets": gePmCurrStatisticPkts1024to1518Octets,
       "gePmCurrStatisticPkts1519to1522Octets": gePmCurrStatisticPkts1519to1522Octets,
       "gePmCurrStatisticTimestamp": gePmCurrStatisticTimestamp,
       "fxsPmCurrStatisticTable": fxsPmCurrStatisticTable,
       "fxsPmCurrStatisticEntry": fxsPmCurrStatisticEntry,
       "fxsPmCurrStatisticRtpElapsedTime": fxsPmCurrStatisticRtpElapsedTime,
       "fxsPmCurrStatisticRtpTxBytes": fxsPmCurrStatisticRtpTxBytes,
       "fxsPmCurrStatisticRtpRxBytes": fxsPmCurrStatisticRtpRxBytes,
       "fxsPmCurrStatisticRtpTxPackets": fxsPmCurrStatisticRtpTxPackets,
       "fxsPmCurrStatisticRtpRxPackets": fxsPmCurrStatisticRtpRxPackets,
       "fxsPmCurrStatisticRtpTxLostPackets": fxsPmCurrStatisticRtpTxLostPackets,
       "fxsPmCurrStatisticRtpRxLostPackets": fxsPmCurrStatisticRtpRxLostPackets,
       "fxsPmCurrStatisticTimestamp": fxsPmCurrStatisticTimestamp,
       "dslPmCurr15minTable": dslPmCurr15minTable,
       "dslPmCurr15minEntry": dslPmCurr15minEntry,
       "dslPmCurr15minElapsed": dslPmCurr15minElapsed,
       "dslPmCurr15minTxOctets": dslPmCurr15minTxOctets,
       "dslPmCurr15minTxPkts": dslPmCurr15minTxPkts,
       "dslPmCurr15minTxUnicastPkts": dslPmCurr15minTxUnicastPkts,
       "dslPmCurr15minTxBroadcastPkts": dslPmCurr15minTxBroadcastPkts,
       "dslPmCurr15minTxMulticastPkts": dslPmCurr15minTxMulticastPkts,
       "dslPmCurr15minTxDiscardPkts": dslPmCurr15minTxDiscardPkts,
       "dslPmCurr15minRxOctets": dslPmCurr15minRxOctets,
       "dslPmCurr15minRxPkts": dslPmCurr15minRxPkts,
       "dslPmCurr15minRxUnicastPkts": dslPmCurr15minRxUnicastPkts,
       "dslPmCurr15minRxBroadcastPkts": dslPmCurr15minRxBroadcastPkts,
       "dslPmCurr15minRxMulticastPkts": dslPmCurr15minRxMulticastPkts,
       "dslPmCurr15minRxDiscardPkts": dslPmCurr15minRxDiscardPkts,
       "dslPmHist15minTable": dslPmHist15minTable,
       "dslPmHist15minEntry": dslPmHist15minEntry,
       "dslPmHist15minIndex": dslPmHist15minIndex,
       "dslPmHist15minElapsed": dslPmHist15minElapsed,
       "dslPmHist15minStartTime": dslPmHist15minStartTime,
       "dslPmHist15minEndTime": dslPmHist15minEndTime,
       "dslPmHist15minTxOctets": dslPmHist15minTxOctets,
       "dslPmHist15minTxPkts": dslPmHist15minTxPkts,
       "dslPmHist15minTxUnicastPkts": dslPmHist15minTxUnicastPkts,
       "dslPmHist15minTxBroadcastPkts": dslPmHist15minTxBroadcastPkts,
       "dslPmHist15minTxMulticastPkts": dslPmHist15minTxMulticastPkts,
       "dslPmHist15minTxDiscardPkts": dslPmHist15minTxDiscardPkts,
       "dslPmHist15minRxOctets": dslPmHist15minRxOctets,
       "dslPmHist15minRxPkts": dslPmHist15minRxPkts,
       "dslPmHist15minRxUnicastPkts": dslPmHist15minRxUnicastPkts,
       "dslPmHist15minRxBroadcastPkts": dslPmHist15minRxBroadcastPkts,
       "dslPmHist15minRxMulticastPkts": dslPmHist15minRxMulticastPkts,
       "dslPmHist15minRxDiscardPkts": dslPmHist15minRxDiscardPkts,
       "dslPmCurr1dayTable": dslPmCurr1dayTable,
       "dslPmCurr1dayEntry": dslPmCurr1dayEntry,
       "dslPmCurr1dayElapsed": dslPmCurr1dayElapsed,
       "dslPmCurr1dayTxOctets": dslPmCurr1dayTxOctets,
       "dslPmCurr1dayTxPkts": dslPmCurr1dayTxPkts,
       "dslPmCurr1dayTxUnicastPkts": dslPmCurr1dayTxUnicastPkts,
       "dslPmCurr1dayTxBroadcastPkts": dslPmCurr1dayTxBroadcastPkts,
       "dslPmCurr1dayTxMulticastPkts": dslPmCurr1dayTxMulticastPkts,
       "dslPmCurr1dayTxDiscardPkts": dslPmCurr1dayTxDiscardPkts,
       "dslPmCurr1dayRxOctets": dslPmCurr1dayRxOctets,
       "dslPmCurr1dayRxPkts": dslPmCurr1dayRxPkts,
       "dslPmCurr1dayRxUnicastPkts": dslPmCurr1dayRxUnicastPkts,
       "dslPmCurr1dayRxBroadcastPkts": dslPmCurr1dayRxBroadcastPkts,
       "dslPmCurr1dayRxMulticastPkts": dslPmCurr1dayRxMulticastPkts,
       "dslPmCurr1dayRxDiscardPkts": dslPmCurr1dayRxDiscardPkts,
       "dslPmHist1dayTable": dslPmHist1dayTable,
       "dslPmHist1dayEntry": dslPmHist1dayEntry,
       "dslPmHist1dayIndex": dslPmHist1dayIndex,
       "dslPmHist1dayStartTime": dslPmHist1dayStartTime,
       "dslPmHist1dayEndTime": dslPmHist1dayEndTime,
       "dslPmHist1dayTxOctets": dslPmHist1dayTxOctets,
       "dslPmHist1dayTxPkts": dslPmHist1dayTxPkts,
       "dslPmHist1dayTxUnicastPkts": dslPmHist1dayTxUnicastPkts,
       "dslPmHist1dayTxBroadcastPkts": dslPmHist1dayTxBroadcastPkts,
       "dslPmHist1dayTxMulticastPkts": dslPmHist1dayTxMulticastPkts,
       "dslPmHist1dayTxDiscardPkts": dslPmHist1dayTxDiscardPkts,
       "dslPmHist1dayRxOctets": dslPmHist1dayRxOctets,
       "dslPmHist1dayRxPkts": dslPmHist1dayRxPkts,
       "dslPmHist1dayRxUnicastPkts": dslPmHist1dayRxUnicastPkts,
       "dslPmHist1dayRxBroadcastPkts": dslPmHist1dayRxBroadcastPkts,
       "dslPmHist1dayRxMulticastPkts": dslPmHist1dayRxMulticastPkts,
       "dslPmHist1dayRxDiscardPkts": dslPmHist1dayRxDiscardPkts,
       "dslPmThreshProfTable": dslPmThreshProfTable,
       "dslPmThreshProfEntry": dslPmThreshProfEntry,
       "dslPmThreshProfName": dslPmThreshProfName,
       "dslPmThreshProfTxOctets": dslPmThreshProfTxOctets,
       "dslPmThreshProfTxPkts": dslPmThreshProfTxPkts,
       "dslPmThreshProfTxUnicastPkts": dslPmThreshProfTxUnicastPkts,
       "dslPmThreshProfTxBroadcastPkts": dslPmThreshProfTxBroadcastPkts,
       "dslPmThreshProfTxMulticastPkts": dslPmThreshProfTxMulticastPkts,
       "dslPmThreshProfTxDiscardPkts": dslPmThreshProfTxDiscardPkts,
       "dslPmThreshProfRxOctets": dslPmThreshProfRxOctets,
       "dslPmThreshProfRxPkts": dslPmThreshProfRxPkts,
       "dslPmThreshProfRxUnicastPkts": dslPmThreshProfRxUnicastPkts,
       "dslPmThreshProfRxBroadcastPkts": dslPmThreshProfRxBroadcastPkts,
       "dslPmThreshProfRxMulticastPkts": dslPmThreshProfRxMulticastPkts,
       "dslPmThreshProfRxDiscardPkts": dslPmThreshProfRxDiscardPkts,
       "dslPmThreshProfRowStatus": dslPmThreshProfRowStatus,
       "dslPmCurrStatisticTable": dslPmCurrStatisticTable,
       "dslPmCurrStatisticEntry": dslPmCurrStatisticEntry,
       "dslPmCurrStatisticTxOctets": dslPmCurrStatisticTxOctets,
       "dslPmCurrStatisticTxPkts": dslPmCurrStatisticTxPkts,
       "dslPmCurrStatisticTxUnicastPkts": dslPmCurrStatisticTxUnicastPkts,
       "dslPmCurrStatisticTxBroadcastPkts": dslPmCurrStatisticTxBroadcastPkts,
       "dslPmCurrStatisticTxMulticastPkts": dslPmCurrStatisticTxMulticastPkts,
       "dslPmCurrStatisticTxDiscard": dslPmCurrStatisticTxDiscard,
       "dslPmCurrStatisticRxOctets": dslPmCurrStatisticRxOctets,
       "dslPmCurrStatisticRxPkts": dslPmCurrStatisticRxPkts,
       "dslPmCurrStatisticRxUnicastPkts": dslPmCurrStatisticRxUnicastPkts,
       "dslPmCurrStatisticRxBroadcastPkts": dslPmCurrStatisticRxBroadcastPkts,
       "dslPmCurrStatisticRxMulticastPkts": dslPmCurrStatisticRxMulticastPkts,
       "dslPmCurrStatisticRxDiscard": dslPmCurrStatisticRxDiscard,
       "dslPmCurrStatisticTimestamp": dslPmCurrStatisticTimestamp,
       "dslBondingCurrCountersTable": dslBondingCurrCountersTable,
       "dslBondingCurrCountersEntry": dslBondingCurrCountersEntry,
       "dslBondingCurrCountersGroupName": dslBondingCurrCountersGroupName,
       "dslBondingCurrCountersPtmRxPackets": dslBondingCurrCountersPtmRxPackets,
       "dslBondingCurrCountersPtmNumFlushRequests": dslBondingCurrCountersPtmNumFlushRequests,
       "dslBondingCurrCountersPtmNumTimeouts": dslBondingCurrCountersPtmNumTimeouts,
       "dslBondingCurrCountersPtmNumDirectSidResets": dslBondingCurrCountersPtmNumDirectSidResets,
       "dslBondingCurrCountersPtmRxSmallFragments": dslBondingCurrCountersPtmRxSmallFragments,
       "dslBondingCurrCountersPtmRxLargeFragments": dslBondingCurrCountersPtmRxLargeFragments,
       "dslBondingCurrCountersPtmRxBadFragments": dslBondingCurrCountersPtmRxBadFragments,
       "dslBondingCurrCountersPtmRxLostFragments": dslBondingCurrCountersPtmRxLostFragments,
       "dslBondingCurrCountersPtmRxLostStarts": dslBondingCurrCountersPtmRxLostStarts,
       "dslBondingCurrCountersPtmRxLostEnds": dslBondingCurrCountersPtmRxLostEnds,
       "dslBondingCurrCountersPtmTxPackets": dslBondingCurrCountersPtmTxPackets,
       "dslBondingCurrCountersAtmTxCells": dslBondingCurrCountersAtmTxCells,
       "dslBondingCurrCountersAtmRxCells": dslBondingCurrCountersAtmRxCells,
       "dslBondingCurrCountersAtmNumFlushRequests": dslBondingCurrCountersAtmNumFlushRequests,
       "dslBondingCurrCountersAtmNumTimeouts": dslBondingCurrCountersAtmNumTimeouts,
       "dslBondingCurrCountersAtmNumDirectSidResets": dslBondingCurrCountersAtmNumDirectSidResets,
       "dslBondingCurrCountersAtmNumDiscards": dslBondingCurrCountersAtmNumDiscards,
       "dslBonding15minCountersTable": dslBonding15minCountersTable,
       "dslBonding15minCountersEntry": dslBonding15minCountersEntry,
       "dslBonding15minCountersGroupName": dslBonding15minCountersGroupName,
       "dslBonding15minCountersElapsed": dslBonding15minCountersElapsed,
       "dslBonding15minCountersPtmRxPackets": dslBonding15minCountersPtmRxPackets,
       "dslBonding15minCountersPtmNumFlushRequests": dslBonding15minCountersPtmNumFlushRequests,
       "dslBonding15minCountersPtmNumTimeouts": dslBonding15minCountersPtmNumTimeouts,
       "dslBonding15minCountersPtmNumDirectSidResets": dslBonding15minCountersPtmNumDirectSidResets,
       "dslBonding15minCountersPtmRxSmallFragments": dslBonding15minCountersPtmRxSmallFragments,
       "dslBonding15minCountersPtmRxLargeFragments": dslBonding15minCountersPtmRxLargeFragments,
       "dslBonding15minCountersPtmRxBadFragments": dslBonding15minCountersPtmRxBadFragments,
       "dslBonding15minCountersPtmRxLostFragments": dslBonding15minCountersPtmRxLostFragments,
       "dslBonding15minCountersPtmRxLostStarts": dslBonding15minCountersPtmRxLostStarts,
       "dslBonding15minCountersPtmRxLostEnds": dslBonding15minCountersPtmRxLostEnds,
       "dslBonding15minCountersPtmTxPackets": dslBonding15minCountersPtmTxPackets,
       "dslBonding15minCountersAtmTxCells": dslBonding15minCountersAtmTxCells,
       "dslBonding15minCountersAtmRxCells": dslBonding15minCountersAtmRxCells,
       "dslBonding15minCountersAtmNumFlushRequests": dslBonding15minCountersAtmNumFlushRequests,
       "dslBonding15minCountersAtmNumTimeouts": dslBonding15minCountersAtmNumTimeouts,
       "dslBonding15minCountersAtmNumDirectSidResets": dslBonding15minCountersAtmNumDirectSidResets,
       "dslBonding15minCountersAtmNumDiscards": dslBonding15minCountersAtmNumDiscards,
       "dslBonding1dayCountersTable": dslBonding1dayCountersTable,
       "dslBonding1dayCountersEntry": dslBonding1dayCountersEntry,
       "dslBonding1dayCountersGroupName": dslBonding1dayCountersGroupName,
       "dslBonding1dayCountersElapsed": dslBonding1dayCountersElapsed,
       "dslBonding1dayCountersPtmRxPackets": dslBonding1dayCountersPtmRxPackets,
       "dslBonding1dayCountersPtmNumFlushRequests": dslBonding1dayCountersPtmNumFlushRequests,
       "dslBonding1dayCountersPtmNumTimeouts": dslBonding1dayCountersPtmNumTimeouts,
       "dslBonding1dayCountersPtmNumDirectSidResets": dslBonding1dayCountersPtmNumDirectSidResets,
       "dslBonding1dayCountersPtmRxSmallFragments": dslBonding1dayCountersPtmRxSmallFragments,
       "dslBonding1dayCountersPtmRxLargeFragments": dslBonding1dayCountersPtmRxLargeFragments,
       "dslBonding1dayCountersPtmRxBadFragments": dslBonding1dayCountersPtmRxBadFragments,
       "dslBonding1dayCountersPtmRxLostFragments": dslBonding1dayCountersPtmRxLostFragments,
       "dslBonding1dayCountersPtmRxLostStarts": dslBonding1dayCountersPtmRxLostStarts,
       "dslBonding1dayCountersPtmRxLostEnds": dslBonding1dayCountersPtmRxLostEnds,
       "dslBonding1dayCountersPtmTxPackets": dslBonding1dayCountersPtmTxPackets,
       "dslBonding1dayCountersAtmTxCells": dslBonding1dayCountersAtmTxCells,
       "dslBonding1dayCountersAtmRxCells": dslBonding1dayCountersAtmRxCells,
       "dslBonding1dayCountersAtmNumFlushRequests": dslBonding1dayCountersAtmNumFlushRequests,
       "dslBonding1dayCountersAtmNumTimeouts": dslBonding1dayCountersAtmNumTimeouts,
       "dslBonding1dayCountersAtmNumDirectSidResets": dslBonding1dayCountersAtmNumDirectSidResets,
       "dslBonding1dayCountersAtmNumDiscards": dslBonding1dayCountersAtmNumDiscards,
       "syslog": syslog,
       "syslogEnable": syslogEnable,
       "syslogServerIpTable": syslogServerIpTable,
       "syslogServerIpEntry": syslogServerIpEntry,
       "syslogServerIpIndex": syslogServerIpIndex,
       "syslogServerIpAddressType": syslogServerIpAddressType,
       "syslogServerIpAddress": syslogServerIpAddress,
       "dot3ad": dot3ad,
       "dot3adTable": dot3adTable,
       "dot3adEntry": dot3adEntry,
       "dot3adGroupId": dot3adGroupId,
       "dot3adEnable": dot3adEnable,
       "dot3adGroupName": dot3adGroupName,
       "dot3adGroupPortList": dot3adGroupPortList,
       "lacpPriority": lacpPriority,
       "lacpTimeout": lacpTimeout,
       "dot3adStatus": dot3adStatus,
       "actor": actor,
       "actorPriority": actorPriority,
       "actorKey": actorKey,
       "partner": partner,
       "partnerPriority": partnerPriority,
       "partnerKey": partnerKey,
       "links": links,
       "syncs": syncs,
       "dot3adStatistic": dot3adStatistic,
       "dot3adStatisticTxUtilization": dot3adStatisticTxUtilization,
       "dot3adStatisticTxSpeed": dot3adStatisticTxSpeed,
       "dot3adStatisticRxUtilization": dot3adStatisticRxUtilization,
       "dot3adStatisticRxSpeed": dot3adStatisticRxSpeed,
       "dot3adStatisticsTxOctet": dot3adStatisticsTxOctet,
       "dot3adStatisticTxPkts": dot3adStatisticTxPkts,
       "dot3adStatisticTxBroadcastPkts": dot3adStatisticTxBroadcastPkts,
       "dot3adStatisticTxMulticastPkts": dot3adStatisticTxMulticastPkts,
       "dot3adStatisticRxOctets": dot3adStatisticRxOctets,
       "dot3adStatisticRxPkts": dot3adStatisticRxPkts,
       "dot3adStatisticRxBroadcastPkts": dot3adStatisticRxBroadcastPkts,
       "dot3adStatisticRxMulticastPkts": dot3adStatisticRxMulticastPkts,
       "dot3adStatisticRxCRCAlignErrors": dot3adStatisticRxCRCAlignErrors,
       "dot3adStatisticRxUndersizePkts": dot3adStatisticRxUndersizePkts,
       "dot3adStatisticRxOversizePkts": dot3adStatisticRxOversizePkts,
       "dot3adStatisticRxFragments": dot3adStatisticRxFragments,
       "dot3adStatisticCollisions": dot3adStatisticCollisions,
       "dot3adStatisticPkts64Octets": dot3adStatisticPkts64Octets,
       "dot3adStatisticPkts65to127Octets": dot3adStatisticPkts65to127Octets,
       "dot3adStatisticPkts128to255Octets": dot3adStatisticPkts128to255Octets,
       "dot3adStatisticPkts256to511Octets": dot3adStatisticPkts256to511Octets,
       "dot3adStatisticPkts512to1023Octets": dot3adStatisticPkts512to1023Octets,
       "dot3adStatisticPkts1024to1518Octets": dot3adStatisticPkts1024to1518Octets,
       "dot3adStatisticPkts1519to1522Octets": dot3adStatisticPkts1519to1522Octets,
       "dot3adStatisticOperation": dot3adStatisticOperation,
       "loadDistribution": loadDistribution,
       "daisychain": daisychain,
       "daisychainTable": daisychainTable,
       "daisychainEntry": daisychainEntry,
       "daisychainMode": daisychainMode,
       "smcast": smcast,
       "maxNumberOfSmcastPortGroups": maxNumberOfSmcastPortGroups,
       "smcastPortTagGroupTable": smcastPortTagGroupTable,
       "smcastPortTagGroupEntry": smcastPortTagGroupEntry,
       "smcastPortTagGroupVid": smcastPortTagGroupVid,
       "smcastPortTagGroupMac": smcastPortTagGroupMac,
       "smcastPortTagGroupRowStatus": smcastPortTagGroupRowStatus,
       "smcastPortUntagGroupTable": smcastPortUntagGroupTable,
       "smcastPortUntagGroupEntry": smcastPortUntagGroupEntry,
       "smcastPortUntagGroupMac": smcastPortUntagGroupMac,
       "smcastPortUntagGroupRowStatus": smcastPortUntagGroupRowStatus}
)
