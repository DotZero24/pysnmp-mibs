# SNMP MIB module (ZTE-AN-NDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-NDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:48 2025
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

(InetAddress,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength")

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

(VlanId,
 ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnNdpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnNdpObjects_ObjectIdentity = ObjectIdentity
zxAnNdpObjects = _ZxAnNdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1)
)
_ZxAnNdpSnoopingObjects_ObjectIdentity = ObjectIdentity
zxAnNdpSnoopingObjects = _ZxAnNdpSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1)
)
_ZxAnNdpSnoopingBindingTable_Object = MibTable
zxAnNdpSnoopingBindingTable = _ZxAnNdpSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingTable.setStatus("current")
_ZxAnNdpSnoopingBindingEntry_Object = MibTableRow
zxAnNdpSnoopingBindingEntry = _ZxAnNdpSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1)
)
zxAnNdpSnoopingBindingEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSnoopingBindingIfIndex"),
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSnoopingBindingIp"),
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingEntry.setStatus("current")
_ZxAnNdpSnoopingBindingIfIndex_Type = ZxAnIfindex
_ZxAnNdpSnoopingBindingIfIndex_Object = MibTableColumn
zxAnNdpSnoopingBindingIfIndex = _ZxAnNdpSnoopingBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 1),
    _ZxAnNdpSnoopingBindingIfIndex_Type()
)
zxAnNdpSnoopingBindingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingIfIndex.setStatus("current")
_ZxAnNdpSnoopingBindingIp_Type = InetAddress
_ZxAnNdpSnoopingBindingIp_Object = MibTableColumn
zxAnNdpSnoopingBindingIp = _ZxAnNdpSnoopingBindingIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 2),
    _ZxAnNdpSnoopingBindingIp_Type()
)
zxAnNdpSnoopingBindingIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingIp.setStatus("current")
_ZxAnNdpSnoopingBindingMac_Type = MacAddress
_ZxAnNdpSnoopingBindingMac_Object = MibTableColumn
zxAnNdpSnoopingBindingMac = _ZxAnNdpSnoopingBindingMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 3),
    _ZxAnNdpSnoopingBindingMac_Type()
)
zxAnNdpSnoopingBindingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingMac.setStatus("current")
_ZxAnNdpSnoopingBindingBrgPort_Type = Integer32
_ZxAnNdpSnoopingBindingBrgPort_Object = MibTableColumn
zxAnNdpSnoopingBindingBrgPort = _ZxAnNdpSnoopingBindingBrgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 4),
    _ZxAnNdpSnoopingBindingBrgPort_Type()
)
zxAnNdpSnoopingBindingBrgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingBrgPort.setStatus("current")
_ZxAnNdpSnoopingBindingVlan_Type = Integer32
_ZxAnNdpSnoopingBindingVlan_Object = MibTableColumn
zxAnNdpSnoopingBindingVlan = _ZxAnNdpSnoopingBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 5),
    _ZxAnNdpSnoopingBindingVlan_Type()
)
zxAnNdpSnoopingBindingVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingVlan.setStatus("current")


class _ZxAnNdpSnoopingBindingSrcGuard_Type(Integer32):
    """Custom type zxAnNdpSnoopingBindingSrcGuard based on Integer32"""
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


_ZxAnNdpSnoopingBindingSrcGuard_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingBindingSrcGuard_Object = MibTableColumn
zxAnNdpSnoopingBindingSrcGuard = _ZxAnNdpSnoopingBindingSrcGuard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 6),
    _ZxAnNdpSnoopingBindingSrcGuard_Type()
)
zxAnNdpSnoopingBindingSrcGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingSrcGuard.setStatus("current")
_ZxAnNdpSnoopingBindingIpPfxLen_Type = InetAddressPrefixLength
_ZxAnNdpSnoopingBindingIpPfxLen_Object = MibTableColumn
zxAnNdpSnoopingBindingIpPfxLen = _ZxAnNdpSnoopingBindingIpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 7),
    _ZxAnNdpSnoopingBindingIpPfxLen_Type()
)
zxAnNdpSnoopingBindingIpPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingIpPfxLen.setStatus("current")


class _ZxAnNdpSnoopingBindingLeaseTime_Type(DisplayString):
    """Custom type zxAnNdpSnoopingBindingLeaseTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_ZxAnNdpSnoopingBindingLeaseTime_Type.__name__ = "DisplayString"
_ZxAnNdpSnoopingBindingLeaseTime_Object = MibTableColumn
zxAnNdpSnoopingBindingLeaseTime = _ZxAnNdpSnoopingBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 8),
    _ZxAnNdpSnoopingBindingLeaseTime_Type()
)
zxAnNdpSnoopingBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingLeaseTime.setStatus("current")
_ZxAnNdpSnoopingBindingSvlan_Type = Integer32
_ZxAnNdpSnoopingBindingSvlan_Object = MibTableColumn
zxAnNdpSnoopingBindingSvlan = _ZxAnNdpSnoopingBindingSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 2, 1, 9),
    _ZxAnNdpSnoopingBindingSvlan_Type()
)
zxAnNdpSnoopingBindingSvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingBindingSvlan.setStatus("current")
_ZxAnNdpSnoopingIfConfigTable_Object = MibTable
zxAnNdpSnoopingIfConfigTable = _ZxAnNdpSnoopingIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingIfConfigTable.setStatus("current")
_ZxAnNdpSnoopingIfConfigEntry_Object = MibTableRow
zxAnNdpSnoopingIfConfigEntry = _ZxAnNdpSnoopingIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 3, 1)
)
zxAnNdpSnoopingIfConfigEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSnoopingIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingIfConfigEntry.setStatus("current")
_ZxAnNdpSnoopingIfIndex_Type = ZxAnIfindex
_ZxAnNdpSnoopingIfIndex_Object = MibTableColumn
zxAnNdpSnoopingIfIndex = _ZxAnNdpSnoopingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 3, 1, 1),
    _ZxAnNdpSnoopingIfIndex_Type()
)
zxAnNdpSnoopingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingIfIndex.setStatus("current")


class _ZxAnNdpSnoopingIfEnable_Type(Integer32):
    """Custom type zxAnNdpSnoopingIfEnable based on Integer32"""
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


_ZxAnNdpSnoopingIfEnable_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingIfEnable_Object = MibTableColumn
zxAnNdpSnoopingIfEnable = _ZxAnNdpSnoopingIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 3, 1, 2),
    _ZxAnNdpSnoopingIfEnable_Type()
)
zxAnNdpSnoopingIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingIfEnable.setStatus("current")


class _ZxAnNdpSnoopingIfBindingLimit_Type(Integer32):
    """Custom type zxAnNdpSnoopingIfBindingLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxAnNdpSnoopingIfBindingLimit_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingIfBindingLimit_Object = MibTableColumn
zxAnNdpSnoopingIfBindingLimit = _ZxAnNdpSnoopingIfBindingLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 3, 1, 3),
    _ZxAnNdpSnoopingIfBindingLimit_Type()
)
zxAnNdpSnoopingIfBindingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingIfBindingLimit.setStatus("current")
_ZxAnNdpSnoopingVlanConfigTable_Object = MibTable
zxAnNdpSnoopingVlanConfigTable = _ZxAnNdpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingVlanConfigTable.setStatus("current")
_ZxAnNdpSnoopingVlanConfigEntry_Object = MibTableRow
zxAnNdpSnoopingVlanConfigEntry = _ZxAnNdpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 4, 1)
)
zxAnNdpSnoopingVlanConfigEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    zxAnNdpSnoopingVlanConfigEntry.setStatus("current")


class _ZxAnNdpSnoopingVlanId_Type(Integer32):
    """Custom type zxAnNdpSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnNdpSnoopingVlanId_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingVlanId_Object = MibTableColumn
zxAnNdpSnoopingVlanId = _ZxAnNdpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 4, 1, 1),
    _ZxAnNdpSnoopingVlanId_Type()
)
zxAnNdpSnoopingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingVlanId.setStatus("current")


class _ZxAnNdpSnoopingVlanEnable_Type(Integer32):
    """Custom type zxAnNdpSnoopingVlanEnable based on Integer32"""
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


_ZxAnNdpSnoopingVlanEnable_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingVlanEnable_Object = MibTableColumn
zxAnNdpSnoopingVlanEnable = _ZxAnNdpSnoopingVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 4, 1, 2),
    _ZxAnNdpSnoopingVlanEnable_Type()
)
zxAnNdpSnoopingVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingVlanEnable.setStatus("current")
_ZxAnNdpSnoopingGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnNdpSnoopingGlobalObjects = _ZxAnNdpSnoopingGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 50)
)


class _ZxAnNdpSnoopingGlobalEnable_Type(Integer32):
    """Custom type zxAnNdpSnoopingGlobalEnable based on Integer32"""
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


_ZxAnNdpSnoopingGlobalEnable_Type.__name__ = "Integer32"
_ZxAnNdpSnoopingGlobalEnable_Object = MibScalar
zxAnNdpSnoopingGlobalEnable = _ZxAnNdpSnoopingGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 1, 50, 1),
    _ZxAnNdpSnoopingGlobalEnable_Type()
)
zxAnNdpSnoopingGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSnoopingGlobalEnable.setStatus("current")
_ZxAnNdpFilterObjects_ObjectIdentity = ObjectIdentity
zxAnNdpFilterObjects = _ZxAnNdpFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 2)
)
_ZxAnNdpFilterVlanConfTable_Object = MibTable
zxAnNdpFilterVlanConfTable = _ZxAnNdpFilterVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnNdpFilterVlanConfTable.setStatus("current")
_ZxAnNdpFilterVlanConfEntry_Object = MibTableRow
zxAnNdpFilterVlanConfEntry = _ZxAnNdpFilterVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 2, 2, 1)
)
zxAnNdpFilterVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpFilterVlanConfVid"),
)
if mibBuilder.loadTexts:
    zxAnNdpFilterVlanConfEntry.setStatus("current")


class _ZxAnNdpFilterVlanConfVid_Type(Integer32):
    """Custom type zxAnNdpFilterVlanConfVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnNdpFilterVlanConfVid_Type.__name__ = "Integer32"
_ZxAnNdpFilterVlanConfVid_Object = MibTableColumn
zxAnNdpFilterVlanConfVid = _ZxAnNdpFilterVlanConfVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 2, 2, 1, 1),
    _ZxAnNdpFilterVlanConfVid_Type()
)
zxAnNdpFilterVlanConfVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpFilterVlanConfVid.setStatus("current")
_ZxAnNdpFilterVlanConfRowStatus_Type = RowStatus
_ZxAnNdpFilterVlanConfRowStatus_Object = MibTableColumn
zxAnNdpFilterVlanConfRowStatus = _ZxAnNdpFilterVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 2, 2, 1, 50),
    _ZxAnNdpFilterVlanConfRowStatus_Type()
)
zxAnNdpFilterVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNdpFilterVlanConfRowStatus.setStatus("current")
_ZxAnNdpSlaacSnoopingObjects_ObjectIdentity = ObjectIdentity
zxAnNdpSlaacSnoopingObjects = _ZxAnNdpSlaacSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3)
)
_ZxAnNdpSlaacSnoopingBindingTable_Object = MibTable
zxAnNdpSlaacSnoopingBindingTable = _ZxAnNdpSlaacSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindingTable.setStatus("current")
_ZxAnNdpSlaacSnoopingBindingEntry_Object = MibTableRow
zxAnNdpSlaacSnoopingBindingEntry = _ZxAnNdpSlaacSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1)
)
zxAnNdpSlaacSnoopingBindingEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSnoopingBindIfIndex"),
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSnoopingBindBrgPort"),
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSnoopingBindSVid"),
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSnoopingBindMac"),
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindingEntry.setStatus("current")
_ZxAnNdpSlaacSnoopingBindIfIndex_Type = ZxAnIfindex
_ZxAnNdpSlaacSnoopingBindIfIndex_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindIfIndex = _ZxAnNdpSlaacSnoopingBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 1),
    _ZxAnNdpSlaacSnoopingBindIfIndex_Type()
)
zxAnNdpSlaacSnoopingBindIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindIfIndex.setStatus("current")
_ZxAnNdpSlaacSnoopingBindBrgPort_Type = Integer32
_ZxAnNdpSlaacSnoopingBindBrgPort_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindBrgPort = _ZxAnNdpSlaacSnoopingBindBrgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 2),
    _ZxAnNdpSlaacSnoopingBindBrgPort_Type()
)
zxAnNdpSlaacSnoopingBindBrgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindBrgPort.setStatus("current")
_ZxAnNdpSlaacSnoopingBindSVid_Type = VlanId
_ZxAnNdpSlaacSnoopingBindSVid_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindSVid = _ZxAnNdpSlaacSnoopingBindSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 3),
    _ZxAnNdpSlaacSnoopingBindSVid_Type()
)
zxAnNdpSlaacSnoopingBindSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindSVid.setStatus("current")
_ZxAnNdpSlaacSnoopingBindMac_Type = MacAddress
_ZxAnNdpSlaacSnoopingBindMac_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindMac = _ZxAnNdpSlaacSnoopingBindMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 4),
    _ZxAnNdpSlaacSnoopingBindMac_Type()
)
zxAnNdpSlaacSnoopingBindMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindMac.setStatus("current")
_ZxAnNdpSlaacSnoopingBindIp_Type = InetAddress
_ZxAnNdpSlaacSnoopingBindIp_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindIp = _ZxAnNdpSlaacSnoopingBindIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 5),
    _ZxAnNdpSlaacSnoopingBindIp_Type()
)
zxAnNdpSlaacSnoopingBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindIp.setStatus("current")
_ZxAnNdpSlaacSnoopingBindIpPfxLen_Type = InetAddressPrefixLength
_ZxAnNdpSlaacSnoopingBindIpPfxLen_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindIpPfxLen = _ZxAnNdpSlaacSnoopingBindIpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 6),
    _ZxAnNdpSlaacSnoopingBindIpPfxLen_Type()
)
zxAnNdpSlaacSnoopingBindIpPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindIpPfxLen.setStatus("current")


class _ZxAnNdpSlaacSnoopBindLeaseTime_Type(DisplayString):
    """Custom type zxAnNdpSlaacSnoopBindLeaseTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_ZxAnNdpSlaacSnoopBindLeaseTime_Type.__name__ = "DisplayString"
_ZxAnNdpSlaacSnoopBindLeaseTime_Object = MibTableColumn
zxAnNdpSlaacSnoopBindLeaseTime = _ZxAnNdpSlaacSnoopBindLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 7),
    _ZxAnNdpSlaacSnoopBindLeaseTime_Type()
)
zxAnNdpSlaacSnoopBindLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopBindLeaseTime.setStatus("current")


class _ZxAnNdpSlaacSnoopingBindSrcGuard_Type(Integer32):
    """Custom type zxAnNdpSlaacSnoopingBindSrcGuard based on Integer32"""
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


_ZxAnNdpSlaacSnoopingBindSrcGuard_Type.__name__ = "Integer32"
_ZxAnNdpSlaacSnoopingBindSrcGuard_Object = MibTableColumn
zxAnNdpSlaacSnoopingBindSrcGuard = _ZxAnNdpSlaacSnoopingBindSrcGuard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 2, 1, 8),
    _ZxAnNdpSlaacSnoopingBindSrcGuard_Type()
)
zxAnNdpSlaacSnoopingBindSrcGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingBindSrcGuard.setStatus("current")
_ZxAnNdpSlaacSnoopingIfConfTable_Object = MibTable
zxAnNdpSlaacSnoopingIfConfTable = _ZxAnNdpSlaacSnoopingIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingIfConfTable.setStatus("current")
_ZxAnNdpSlaacSnoopingIfConfEntry_Object = MibTableRow
zxAnNdpSlaacSnoopingIfConfEntry = _ZxAnNdpSlaacSnoopingIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 3, 1)
)
zxAnNdpSlaacSnoopingIfConfEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSnoopingIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingIfConfEntry.setStatus("current")
_ZxAnNdpSlaacSnoopingIfIndex_Type = ZxAnIfindex
_ZxAnNdpSlaacSnoopingIfIndex_Object = MibTableColumn
zxAnNdpSlaacSnoopingIfIndex = _ZxAnNdpSlaacSnoopingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 3, 1, 1),
    _ZxAnNdpSlaacSnoopingIfIndex_Type()
)
zxAnNdpSlaacSnoopingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingIfIndex.setStatus("current")


class _ZxAnNdpSlaacSnoopingIfEnable_Type(Integer32):
    """Custom type zxAnNdpSlaacSnoopingIfEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnNdpSlaacSnoopingIfEnable_Type.__name__ = "Integer32"
_ZxAnNdpSlaacSnoopingIfEnable_Object = MibTableColumn
zxAnNdpSlaacSnoopingIfEnable = _ZxAnNdpSlaacSnoopingIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 3, 1, 2),
    _ZxAnNdpSlaacSnoopingIfEnable_Type()
)
zxAnNdpSlaacSnoopingIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingIfEnable.setStatus("current")


class _ZxAnNdpSlaacSnoopingIfBindingLmt_Type(Integer32):
    """Custom type zxAnNdpSlaacSnoopingIfBindingLmt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxAnNdpSlaacSnoopingIfBindingLmt_Type.__name__ = "Integer32"
_ZxAnNdpSlaacSnoopingIfBindingLmt_Object = MibTableColumn
zxAnNdpSlaacSnoopingIfBindingLmt = _ZxAnNdpSlaacSnoopingIfBindingLmt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 3, 1, 3),
    _ZxAnNdpSlaacSnoopingIfBindingLmt_Type()
)
zxAnNdpSlaacSnoopingIfBindingLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSnoopingIfBindingLmt.setStatus("current")
_ZxAnNdpSlaacSrcGuardIfConfTable_Object = MibTable
zxAnNdpSlaacSrcGuardIfConfTable = _ZxAnNdpSlaacSrcGuardIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSrcGuardIfConfTable.setStatus("current")
_ZxAnNdpSlaacSrcGuardIfConfEntry_Object = MibTableRow
zxAnNdpSlaacSrcGuardIfConfEntry = _ZxAnNdpSlaacSrcGuardIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 4, 1)
)
zxAnNdpSlaacSrcGuardIfConfEntry.setIndexNames(
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSrcGuardIfIndex"),
    (0, "ZTE-AN-NDP-MIB", "zxAnNdpSlaacSrcGuardBrgPort"),
)
if mibBuilder.loadTexts:
    zxAnNdpSlaacSrcGuardIfConfEntry.setStatus("current")
_ZxAnNdpSlaacSrcGuardIfIndex_Type = ZxAnIfindex
_ZxAnNdpSlaacSrcGuardIfIndex_Object = MibTableColumn
zxAnNdpSlaacSrcGuardIfIndex = _ZxAnNdpSlaacSrcGuardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 4, 1, 1),
    _ZxAnNdpSlaacSrcGuardIfIndex_Type()
)
zxAnNdpSlaacSrcGuardIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSrcGuardIfIndex.setStatus("current")
_ZxAnNdpSlaacSrcGuardBrgPort_Type = Integer32
_ZxAnNdpSlaacSrcGuardBrgPort_Object = MibTableColumn
zxAnNdpSlaacSrcGuardBrgPort = _ZxAnNdpSlaacSrcGuardBrgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 4, 1, 2),
    _ZxAnNdpSlaacSrcGuardBrgPort_Type()
)
zxAnNdpSlaacSrcGuardBrgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSrcGuardBrgPort.setStatus("current")


class _ZxAnNdpSlaacSrcGuardIfEnable_Type(Integer32):
    """Custom type zxAnNdpSlaacSrcGuardIfEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnNdpSlaacSrcGuardIfEnable_Type.__name__ = "Integer32"
_ZxAnNdpSlaacSrcGuardIfEnable_Object = MibTableColumn
zxAnNdpSlaacSrcGuardIfEnable = _ZxAnNdpSlaacSrcGuardIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 69, 1, 3, 4, 1, 3),
    _ZxAnNdpSlaacSrcGuardIfEnable_Type()
)
zxAnNdpSlaacSrcGuardIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpSlaacSrcGuardIfEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-NDP-MIB",
    **{"zxAnNdpMib": zxAnNdpMib,
       "zxAnNdpObjects": zxAnNdpObjects,
       "zxAnNdpSnoopingObjects": zxAnNdpSnoopingObjects,
       "zxAnNdpSnoopingBindingTable": zxAnNdpSnoopingBindingTable,
       "zxAnNdpSnoopingBindingEntry": zxAnNdpSnoopingBindingEntry,
       "zxAnNdpSnoopingBindingIfIndex": zxAnNdpSnoopingBindingIfIndex,
       "zxAnNdpSnoopingBindingIp": zxAnNdpSnoopingBindingIp,
       "zxAnNdpSnoopingBindingMac": zxAnNdpSnoopingBindingMac,
       "zxAnNdpSnoopingBindingBrgPort": zxAnNdpSnoopingBindingBrgPort,
       "zxAnNdpSnoopingBindingVlan": zxAnNdpSnoopingBindingVlan,
       "zxAnNdpSnoopingBindingSrcGuard": zxAnNdpSnoopingBindingSrcGuard,
       "zxAnNdpSnoopingBindingIpPfxLen": zxAnNdpSnoopingBindingIpPfxLen,
       "zxAnNdpSnoopingBindingLeaseTime": zxAnNdpSnoopingBindingLeaseTime,
       "zxAnNdpSnoopingBindingSvlan": zxAnNdpSnoopingBindingSvlan,
       "zxAnNdpSnoopingIfConfigTable": zxAnNdpSnoopingIfConfigTable,
       "zxAnNdpSnoopingIfConfigEntry": zxAnNdpSnoopingIfConfigEntry,
       "zxAnNdpSnoopingIfIndex": zxAnNdpSnoopingIfIndex,
       "zxAnNdpSnoopingIfEnable": zxAnNdpSnoopingIfEnable,
       "zxAnNdpSnoopingIfBindingLimit": zxAnNdpSnoopingIfBindingLimit,
       "zxAnNdpSnoopingVlanConfigTable": zxAnNdpSnoopingVlanConfigTable,
       "zxAnNdpSnoopingVlanConfigEntry": zxAnNdpSnoopingVlanConfigEntry,
       "zxAnNdpSnoopingVlanId": zxAnNdpSnoopingVlanId,
       "zxAnNdpSnoopingVlanEnable": zxAnNdpSnoopingVlanEnable,
       "zxAnNdpSnoopingGlobalObjects": zxAnNdpSnoopingGlobalObjects,
       "zxAnNdpSnoopingGlobalEnable": zxAnNdpSnoopingGlobalEnable,
       "zxAnNdpFilterObjects": zxAnNdpFilterObjects,
       "zxAnNdpFilterVlanConfTable": zxAnNdpFilterVlanConfTable,
       "zxAnNdpFilterVlanConfEntry": zxAnNdpFilterVlanConfEntry,
       "zxAnNdpFilterVlanConfVid": zxAnNdpFilterVlanConfVid,
       "zxAnNdpFilterVlanConfRowStatus": zxAnNdpFilterVlanConfRowStatus,
       "zxAnNdpSlaacSnoopingObjects": zxAnNdpSlaacSnoopingObjects,
       "zxAnNdpSlaacSnoopingBindingTable": zxAnNdpSlaacSnoopingBindingTable,
       "zxAnNdpSlaacSnoopingBindingEntry": zxAnNdpSlaacSnoopingBindingEntry,
       "zxAnNdpSlaacSnoopingBindIfIndex": zxAnNdpSlaacSnoopingBindIfIndex,
       "zxAnNdpSlaacSnoopingBindBrgPort": zxAnNdpSlaacSnoopingBindBrgPort,
       "zxAnNdpSlaacSnoopingBindSVid": zxAnNdpSlaacSnoopingBindSVid,
       "zxAnNdpSlaacSnoopingBindMac": zxAnNdpSlaacSnoopingBindMac,
       "zxAnNdpSlaacSnoopingBindIp": zxAnNdpSlaacSnoopingBindIp,
       "zxAnNdpSlaacSnoopingBindIpPfxLen": zxAnNdpSlaacSnoopingBindIpPfxLen,
       "zxAnNdpSlaacSnoopBindLeaseTime": zxAnNdpSlaacSnoopBindLeaseTime,
       "zxAnNdpSlaacSnoopingBindSrcGuard": zxAnNdpSlaacSnoopingBindSrcGuard,
       "zxAnNdpSlaacSnoopingIfConfTable": zxAnNdpSlaacSnoopingIfConfTable,
       "zxAnNdpSlaacSnoopingIfConfEntry": zxAnNdpSlaacSnoopingIfConfEntry,
       "zxAnNdpSlaacSnoopingIfIndex": zxAnNdpSlaacSnoopingIfIndex,
       "zxAnNdpSlaacSnoopingIfEnable": zxAnNdpSlaacSnoopingIfEnable,
       "zxAnNdpSlaacSnoopingIfBindingLmt": zxAnNdpSlaacSnoopingIfBindingLmt,
       "zxAnNdpSlaacSrcGuardIfConfTable": zxAnNdpSlaacSrcGuardIfConfTable,
       "zxAnNdpSlaacSrcGuardIfConfEntry": zxAnNdpSlaacSrcGuardIfConfEntry,
       "zxAnNdpSlaacSrcGuardIfIndex": zxAnNdpSlaacSrcGuardIfIndex,
       "zxAnNdpSlaacSrcGuardBrgPort": zxAnNdpSlaacSrcGuardBrgPort,
       "zxAnNdpSlaacSrcGuardIfEnable": zxAnNdpSlaacSrcGuardIfEnable}
)
