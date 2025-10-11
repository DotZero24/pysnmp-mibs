# SNMP MIB module (ZTE-AN-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:57 2025
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

zxAnDhcpSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnDhcpSnoopingMIBNotifs_ObjectIdentity = ObjectIdentity
zxAnDhcpSnoopingMIBNotifs = _ZxAnDhcpSnoopingMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 0)
)
_ZxAnDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
zxAnDhcpSnoopingMIBObjects = _ZxAnDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1)
)
_ZxAnDsGlobal_ObjectIdentity = ObjectIdentity
zxAnDsGlobal = _ZxAnDsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 1)
)


class _ZxAnDsGlobalEnable_Type(Integer32):
    """Custom type zxAnDsGlobalEnable based on Integer32"""
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


_ZxAnDsGlobalEnable_Type.__name__ = "Integer32"
_ZxAnDsGlobalEnable_Object = MibScalar
zxAnDsGlobalEnable = _ZxAnDsGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 1, 1),
    _ZxAnDsGlobalEnable_Type()
)
zxAnDsGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsGlobalEnable.setStatus("current")


class _ZxAnDsv6GlobalEnable_Type(Integer32):
    """Custom type zxAnDsv6GlobalEnable based on Integer32"""
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


_ZxAnDsv6GlobalEnable_Type.__name__ = "Integer32"
_ZxAnDsv6GlobalEnable_Object = MibScalar
zxAnDsv6GlobalEnable = _ZxAnDsv6GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 1, 2),
    _ZxAnDsv6GlobalEnable_Type()
)
zxAnDsv6GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsv6GlobalEnable.setStatus("current")
_ZxAnDsVlan_ObjectIdentity = ObjectIdentity
zxAnDsVlan = _ZxAnDsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2)
)
_ZxAnDsVlanTable_Object = MibTable
zxAnDsVlanTable = _ZxAnDsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnDsVlanTable.setStatus("current")
_ZxAnDsVlanEntry_Object = MibTableRow
zxAnDsVlanEntry = _ZxAnDsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2, 1, 1)
)
zxAnDsVlanEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsVlanIndex"),
)
if mibBuilder.loadTexts:
    zxAnDsVlanEntry.setStatus("current")
_ZxAnDsVlanIndex_Type = VlanId
_ZxAnDsVlanIndex_Object = MibTableColumn
zxAnDsVlanIndex = _ZxAnDsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2, 1, 1, 1),
    _ZxAnDsVlanIndex_Type()
)
zxAnDsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsVlanIndex.setStatus("current")


class _ZxAnDsVlanEnable_Type(Integer32):
    """Custom type zxAnDsVlanEnable based on Integer32"""
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


_ZxAnDsVlanEnable_Type.__name__ = "Integer32"
_ZxAnDsVlanEnable_Object = MibTableColumn
zxAnDsVlanEnable = _ZxAnDsVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2, 1, 1, 2),
    _ZxAnDsVlanEnable_Type()
)
zxAnDsVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsVlanEnable.setStatus("current")


class _ZxAnDsv6VlanEnable_Type(Integer32):
    """Custom type zxAnDsv6VlanEnable based on Integer32"""
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


_ZxAnDsv6VlanEnable_Type.__name__ = "Integer32"
_ZxAnDsv6VlanEnable_Object = MibTableColumn
zxAnDsv6VlanEnable = _ZxAnDsv6VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 2, 1, 1, 3),
    _ZxAnDsv6VlanEnable_Type()
)
zxAnDsv6VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsv6VlanEnable.setStatus("current")
_ZxAnDsBinds_ObjectIdentity = ObjectIdentity
zxAnDsBinds = _ZxAnDsBinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 3)
)
_ZxAnDsInterface_ObjectIdentity = ObjectIdentity
zxAnDsInterface = _ZxAnDsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4)
)
_ZxAnDsInterfaceTable_Object = MibTable
zxAnDsInterfaceTable = _ZxAnDsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnDsInterfaceTable.setStatus("current")
_ZxAnDsInterfaceEntry_Object = MibTableRow
zxAnDsInterfaceEntry = _ZxAnDsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4, 1, 1)
)
zxAnDsInterfaceEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    zxAnDsInterfaceEntry.setStatus("current")
_ZxAnDsInterfaceIndex_Type = ZxAnIfindex
_ZxAnDsInterfaceIndex_Object = MibTableColumn
zxAnDsInterfaceIndex = _ZxAnDsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4, 1, 1, 1),
    _ZxAnDsInterfaceIndex_Type()
)
zxAnDsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsInterfaceIndex.setStatus("current")


class _ZxAnDsInterfaceType_Type(Integer32):
    """Custom type zxAnDsInterfaceType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_ZxAnDsInterfaceType_Type.__name__ = "Integer32"
_ZxAnDsInterfaceType_Object = MibTableColumn
zxAnDsInterfaceType = _ZxAnDsInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4, 1, 1, 2),
    _ZxAnDsInterfaceType_Type()
)
zxAnDsInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsInterfaceType.setStatus("current")


class _ZxAnDsv6InterfaceType_Type(Integer32):
    """Custom type zxAnDsv6InterfaceType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_ZxAnDsv6InterfaceType_Type.__name__ = "Integer32"
_ZxAnDsv6InterfaceType_Object = MibTableColumn
zxAnDsv6InterfaceType = _ZxAnDsv6InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 4, 1, 1, 3),
    _ZxAnDsv6InterfaceType_Type()
)
zxAnDsv6InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsv6InterfaceType.setStatus("current")
_ZxAnDsShow_ObjectIdentity = ObjectIdentity
zxAnDsShow = _ZxAnDsShow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5)
)
_ZxAnDsPortBindViewTable_Object = MibTable
zxAnDsPortBindViewTable = _ZxAnDsPortBindViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnDsPortBindViewTable.setStatus("current")
_ZxAnDsPortBindViewEntry_Object = MibTableRow
zxAnDsPortBindViewEntry = _ZxAnDsPortBindViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1)
)
zxAnDsPortBindViewEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsInterfaceIndex"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsPortBindViewMac"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsPortBindViewVlan"),
)
if mibBuilder.loadTexts:
    zxAnDsPortBindViewEntry.setStatus("current")
_ZxAnDsPortBindViewMac_Type = MacAddress
_ZxAnDsPortBindViewMac_Object = MibTableColumn
zxAnDsPortBindViewMac = _ZxAnDsPortBindViewMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 1),
    _ZxAnDsPortBindViewMac_Type()
)
zxAnDsPortBindViewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewMac.setStatus("current")


class _ZxAnDsPortBindViewVlan_Type(Integer32):
    """Custom type zxAnDsPortBindViewVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZxAnDsPortBindViewVlan_Type.__name__ = "Integer32"
_ZxAnDsPortBindViewVlan_Object = MibTableColumn
zxAnDsPortBindViewVlan = _ZxAnDsPortBindViewVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 2),
    _ZxAnDsPortBindViewVlan_Type()
)
zxAnDsPortBindViewVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewVlan.setStatus("current")
_ZxAnDsPortBindViewIp_Type = IpAddress
_ZxAnDsPortBindViewIp_Object = MibTableColumn
zxAnDsPortBindViewIp = _ZxAnDsPortBindViewIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 3),
    _ZxAnDsPortBindViewIp_Type()
)
zxAnDsPortBindViewIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewIp.setStatus("current")


class _ZxAnDsPortBindViewType_Type(Integer32):
    """Custom type zxAnDsPortBindViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_ZxAnDsPortBindViewType_Type.__name__ = "Integer32"
_ZxAnDsPortBindViewType_Object = MibTableColumn
zxAnDsPortBindViewType = _ZxAnDsPortBindViewType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 4),
    _ZxAnDsPortBindViewType_Type()
)
zxAnDsPortBindViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewType.setStatus("current")


class _ZxAnDsPortBindViewTime_Type(DisplayString):
    """Custom type zxAnDsPortBindViewTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnDsPortBindViewTime_Type.__name__ = "DisplayString"
_ZxAnDsPortBindViewTime_Object = MibTableColumn
zxAnDsPortBindViewTime = _ZxAnDsPortBindViewTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 5),
    _ZxAnDsPortBindViewTime_Type()
)
zxAnDsPortBindViewTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewTime.setStatus("current")


class _ZxAnDsPortBindViewSvlan_Type(Integer32):
    """Custom type zxAnDsPortBindViewSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZxAnDsPortBindViewSvlan_Type.__name__ = "Integer32"
_ZxAnDsPortBindViewSvlan_Object = MibTableColumn
zxAnDsPortBindViewSvlan = _ZxAnDsPortBindViewSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 6),
    _ZxAnDsPortBindViewSvlan_Type()
)
zxAnDsPortBindViewSvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewSvlan.setStatus("current")
_ZxAnDsPortBindViewRowStatus_Type = RowStatus
_ZxAnDsPortBindViewRowStatus_Object = MibTableColumn
zxAnDsPortBindViewRowStatus = _ZxAnDsPortBindViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 1, 1, 20),
    _ZxAnDsPortBindViewRowStatus_Type()
)
zxAnDsPortBindViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsPortBindViewRowStatus.setStatus("current")
_ZxAnDsShowGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnDsShowGlobalObjects = _ZxAnDsShowGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 50)
)


class _ZxAnDsPortBindOnlineUserNum_Type(Integer32):
    """Custom type zxAnDsPortBindOnlineUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_ZxAnDsPortBindOnlineUserNum_Type.__name__ = "Integer32"
_ZxAnDsPortBindOnlineUserNum_Object = MibScalar
zxAnDsPortBindOnlineUserNum = _ZxAnDsPortBindOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 5, 50, 1),
    _ZxAnDsPortBindOnlineUserNum_Type()
)
zxAnDsPortBindOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsPortBindOnlineUserNum.setStatus("current")
_ZxAnDsUserInterface_ObjectIdentity = ObjectIdentity
zxAnDsUserInterface = _ZxAnDsUserInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6)
)
_ZxAnDsUserInterfaceTable_Object = MibTable
zxAnDsUserInterfaceTable = _ZxAnDsUserInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6, 1)
)
if mibBuilder.loadTexts:
    zxAnDsUserInterfaceTable.setStatus("current")
_ZxAnDsUserInterfaceEntry_Object = MibTableRow
zxAnDsUserInterfaceEntry = _ZxAnDsUserInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6, 1, 1)
)
zxAnDsUserInterfaceEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsUserInterfaceIndex"),
)
if mibBuilder.loadTexts:
    zxAnDsUserInterfaceEntry.setStatus("current")
_ZxAnDsUserInterfaceIndex_Type = ZxAnIfindex
_ZxAnDsUserInterfaceIndex_Object = MibTableColumn
zxAnDsUserInterfaceIndex = _ZxAnDsUserInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6, 1, 1, 1),
    _ZxAnDsUserInterfaceIndex_Type()
)
zxAnDsUserInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsUserInterfaceIndex.setStatus("current")


class _ZxAnDsUserInterfaceQuota_Type(Integer32):
    """Custom type zxAnDsUserInterfaceQuota based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnDsUserInterfaceQuota_Type.__name__ = "Integer32"
_ZxAnDsUserInterfaceQuota_Object = MibTableColumn
zxAnDsUserInterfaceQuota = _ZxAnDsUserInterfaceQuota_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6, 1, 1, 2),
    _ZxAnDsUserInterfaceQuota_Type()
)
zxAnDsUserInterfaceQuota.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsUserInterfaceQuota.setStatus("current")


class _ZxAnDsv6UserInterfaceQuota_Type(Integer32):
    """Custom type zxAnDsv6UserInterfaceQuota based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnDsv6UserInterfaceQuota_Type.__name__ = "Integer32"
_ZxAnDsv6UserInterfaceQuota_Object = MibTableColumn
zxAnDsv6UserInterfaceQuota = _ZxAnDsv6UserInterfaceQuota_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 6, 1, 1, 3),
    _ZxAnDsv6UserInterfaceQuota_Type()
)
zxAnDsv6UserInterfaceQuota.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsv6UserInterfaceQuota.setStatus("current")
_ZxAnDsv6Show_ObjectIdentity = ObjectIdentity
zxAnDsv6Show = _ZxAnDsv6Show_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7)
)
_ZxAnDsv6PortBindViewTable_Object = MibTable
zxAnDsv6PortBindViewTable = _ZxAnDsv6PortBindViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1)
)
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewTable.setStatus("current")
_ZxAnDsv6PortBindViewEntry_Object = MibTableRow
zxAnDsv6PortBindViewEntry = _ZxAnDsv6PortBindViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1)
)
zxAnDsv6PortBindViewEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsInterfaceIndex"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsv6PortBindViewMac"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsv6PortBindViewVlan"),
)
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewEntry.setStatus("current")
_ZxAnDsv6PortBindViewMac_Type = MacAddress
_ZxAnDsv6PortBindViewMac_Object = MibTableColumn
zxAnDsv6PortBindViewMac = _ZxAnDsv6PortBindViewMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 1),
    _ZxAnDsv6PortBindViewMac_Type()
)
zxAnDsv6PortBindViewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewMac.setStatus("current")


class _ZxAnDsv6PortBindViewVlan_Type(Integer32):
    """Custom type zxAnDsv6PortBindViewVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZxAnDsv6PortBindViewVlan_Type.__name__ = "Integer32"
_ZxAnDsv6PortBindViewVlan_Object = MibTableColumn
zxAnDsv6PortBindViewVlan = _ZxAnDsv6PortBindViewVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 2),
    _ZxAnDsv6PortBindViewVlan_Type()
)
zxAnDsv6PortBindViewVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewVlan.setStatus("current")
_ZxAnDsv6PortBindViewIp_Type = InetAddress
_ZxAnDsv6PortBindViewIp_Object = MibTableColumn
zxAnDsv6PortBindViewIp = _ZxAnDsv6PortBindViewIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 3),
    _ZxAnDsv6PortBindViewIp_Type()
)
zxAnDsv6PortBindViewIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewIp.setStatus("current")


class _ZxAnDsv6PortBindViewType_Type(Integer32):
    """Custom type zxAnDsv6PortBindViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_ZxAnDsv6PortBindViewType_Type.__name__ = "Integer32"
_ZxAnDsv6PortBindViewType_Object = MibTableColumn
zxAnDsv6PortBindViewType = _ZxAnDsv6PortBindViewType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 4),
    _ZxAnDsv6PortBindViewType_Type()
)
zxAnDsv6PortBindViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewType.setStatus("current")


class _ZxAnDsv6PortBindViewTime_Type(DisplayString):
    """Custom type zxAnDsv6PortBindViewTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnDsv6PortBindViewTime_Type.__name__ = "DisplayString"
_ZxAnDsv6PortBindViewTime_Object = MibTableColumn
zxAnDsv6PortBindViewTime = _ZxAnDsv6PortBindViewTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 5),
    _ZxAnDsv6PortBindViewTime_Type()
)
zxAnDsv6PortBindViewTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewTime.setStatus("current")
_ZxAnDsv6PortBindViewIpPfxLen_Type = InetAddressPrefixLength
_ZxAnDsv6PortBindViewIpPfxLen_Object = MibTableColumn
zxAnDsv6PortBindViewIpPfxLen = _ZxAnDsv6PortBindViewIpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 6),
    _ZxAnDsv6PortBindViewIpPfxLen_Type()
)
zxAnDsv6PortBindViewIpPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewIpPfxLen.setStatus("current")


class _ZxAnDsv6PortBindViewSvlan_Type(Integer32):
    """Custom type zxAnDsv6PortBindViewSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZxAnDsv6PortBindViewSvlan_Type.__name__ = "Integer32"
_ZxAnDsv6PortBindViewSvlan_Object = MibTableColumn
zxAnDsv6PortBindViewSvlan = _ZxAnDsv6PortBindViewSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 7),
    _ZxAnDsv6PortBindViewSvlan_Type()
)
zxAnDsv6PortBindViewSvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewSvlan.setStatus("current")
_ZxAnDsv6PortBindViewRowStatus_Type = RowStatus
_ZxAnDsv6PortBindViewRowStatus_Object = MibTableColumn
zxAnDsv6PortBindViewRowStatus = _ZxAnDsv6PortBindViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 7, 1, 1, 20),
    _ZxAnDsv6PortBindViewRowStatus_Type()
)
zxAnDsv6PortBindViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsv6PortBindViewRowStatus.setStatus("current")
_ZxAnDsStat_ObjectIdentity = ObjectIdentity
zxAnDsStat = _ZxAnDsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8)
)
_ZxAnDhcpSnoopingIfStatTable_Object = MibTable
zxAnDhcpSnoopingIfStatTable = _ZxAnDhcpSnoopingIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1)
)
if mibBuilder.loadTexts:
    zxAnDhcpSnoopingIfStatTable.setStatus("current")
_ZxAnDhcpSnoopingIfStatEntry_Object = MibTableRow
zxAnDhcpSnoopingIfStatEntry = _ZxAnDhcpSnoopingIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1)
)
zxAnDhcpSnoopingIfStatEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatRack"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatShelf"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatSlot"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatPort"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatOnu"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatIfType"),
    (0, "ZTE-AN-DHCP-SNOOPING-MIB", "zxAnDsIfStatLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnDhcpSnoopingIfStatEntry.setStatus("current")
_ZxAnDsIfStatRack_Type = Integer32
_ZxAnDsIfStatRack_Object = MibTableColumn
zxAnDsIfStatRack = _ZxAnDsIfStatRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 1),
    _ZxAnDsIfStatRack_Type()
)
zxAnDsIfStatRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatRack.setStatus("current")
_ZxAnDsIfStatShelf_Type = Integer32
_ZxAnDsIfStatShelf_Object = MibTableColumn
zxAnDsIfStatShelf = _ZxAnDsIfStatShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 2),
    _ZxAnDsIfStatShelf_Type()
)
zxAnDsIfStatShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatShelf.setStatus("current")
_ZxAnDsIfStatSlot_Type = Integer32
_ZxAnDsIfStatSlot_Object = MibTableColumn
zxAnDsIfStatSlot = _ZxAnDsIfStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 3),
    _ZxAnDsIfStatSlot_Type()
)
zxAnDsIfStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatSlot.setStatus("current")
_ZxAnDsIfStatPort_Type = Integer32
_ZxAnDsIfStatPort_Object = MibTableColumn
zxAnDsIfStatPort = _ZxAnDsIfStatPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 4),
    _ZxAnDsIfStatPort_Type()
)
zxAnDsIfStatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatPort.setStatus("current")
_ZxAnDsIfStatOnu_Type = Integer32
_ZxAnDsIfStatOnu_Object = MibTableColumn
zxAnDsIfStatOnu = _ZxAnDsIfStatOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 5),
    _ZxAnDsIfStatOnu_Type()
)
zxAnDsIfStatOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatOnu.setStatus("current")


class _ZxAnDsIfStatIfType_Type(Integer32):
    """Custom type zxAnDsIfStatIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("ponOnu", 3),
          ("ponVPort", 4),
          ("servicePort", 11),
          ("vlan", 12))
    )


_ZxAnDsIfStatIfType_Type.__name__ = "Integer32"
_ZxAnDsIfStatIfType_Object = MibTableColumn
zxAnDsIfStatIfType = _ZxAnDsIfStatIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 6),
    _ZxAnDsIfStatIfType_Type()
)
zxAnDsIfStatIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatIfType.setStatus("current")
_ZxAnDsIfStatLogicalId_Type = ObjectIdentifier
_ZxAnDsIfStatLogicalId_Object = MibTableColumn
zxAnDsIfStatLogicalId = _ZxAnDsIfStatLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 7),
    _ZxAnDsIfStatLogicalId_Type()
)
zxAnDsIfStatLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsIfStatLogicalId.setStatus("current")
_ZxAnDsIfStatDiscoverPackets_Type = Counter32
_ZxAnDsIfStatDiscoverPackets_Object = MibTableColumn
zxAnDsIfStatDiscoverPackets = _ZxAnDsIfStatDiscoverPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 8),
    _ZxAnDsIfStatDiscoverPackets_Type()
)
zxAnDsIfStatDiscoverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatDiscoverPackets.setStatus("current")
_ZxAnDsIfStatOfferPackets_Type = Counter32
_ZxAnDsIfStatOfferPackets_Object = MibTableColumn
zxAnDsIfStatOfferPackets = _ZxAnDsIfStatOfferPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 9),
    _ZxAnDsIfStatOfferPackets_Type()
)
zxAnDsIfStatOfferPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatOfferPackets.setStatus("current")
_ZxAnDsIfStatRequestPackets_Type = Counter32
_ZxAnDsIfStatRequestPackets_Object = MibTableColumn
zxAnDsIfStatRequestPackets = _ZxAnDsIfStatRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 10),
    _ZxAnDsIfStatRequestPackets_Type()
)
zxAnDsIfStatRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatRequestPackets.setStatus("current")
_ZxAnDsIfStatAckPackets_Type = Counter32
_ZxAnDsIfStatAckPackets_Object = MibTableColumn
zxAnDsIfStatAckPackets = _ZxAnDsIfStatAckPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 11),
    _ZxAnDsIfStatAckPackets_Type()
)
zxAnDsIfStatAckPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatAckPackets.setStatus("current")
_ZxAnDsIfStatNackPackets_Type = Counter32
_ZxAnDsIfStatNackPackets_Object = MibTableColumn
zxAnDsIfStatNackPackets = _ZxAnDsIfStatNackPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 12),
    _ZxAnDsIfStatNackPackets_Type()
)
zxAnDsIfStatNackPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatNackPackets.setStatus("current")
_ZxAnDsIfStatReleasePackets_Type = Counter32
_ZxAnDsIfStatReleasePackets_Object = MibTableColumn
zxAnDsIfStatReleasePackets = _ZxAnDsIfStatReleasePackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 13),
    _ZxAnDsIfStatReleasePackets_Type()
)
zxAnDsIfStatReleasePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatReleasePackets.setStatus("current")
_ZxAnDsIfStatDeclinePackets_Type = Counter32
_ZxAnDsIfStatDeclinePackets_Object = MibTableColumn
zxAnDsIfStatDeclinePackets = _ZxAnDsIfStatDeclinePackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 14),
    _ZxAnDsIfStatDeclinePackets_Type()
)
zxAnDsIfStatDeclinePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatDeclinePackets.setStatus("current")
_ZxAnDsIfStatInformPackets_Type = Counter32
_ZxAnDsIfStatInformPackets_Object = MibTableColumn
zxAnDsIfStatInformPackets = _ZxAnDsIfStatInformPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 51, 1, 8, 1, 1, 15),
    _ZxAnDsIfStatInformPackets_Type()
)
zxAnDsIfStatInformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsIfStatInformPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DHCP-SNOOPING-MIB",
    **{"zxAnDhcpSnoopingMib": zxAnDhcpSnoopingMib,
       "zxAnDhcpSnoopingMIBNotifs": zxAnDhcpSnoopingMIBNotifs,
       "zxAnDhcpSnoopingMIBObjects": zxAnDhcpSnoopingMIBObjects,
       "zxAnDsGlobal": zxAnDsGlobal,
       "zxAnDsGlobalEnable": zxAnDsGlobalEnable,
       "zxAnDsv6GlobalEnable": zxAnDsv6GlobalEnable,
       "zxAnDsVlan": zxAnDsVlan,
       "zxAnDsVlanTable": zxAnDsVlanTable,
       "zxAnDsVlanEntry": zxAnDsVlanEntry,
       "zxAnDsVlanIndex": zxAnDsVlanIndex,
       "zxAnDsVlanEnable": zxAnDsVlanEnable,
       "zxAnDsv6VlanEnable": zxAnDsv6VlanEnable,
       "zxAnDsBinds": zxAnDsBinds,
       "zxAnDsInterface": zxAnDsInterface,
       "zxAnDsInterfaceTable": zxAnDsInterfaceTable,
       "zxAnDsInterfaceEntry": zxAnDsInterfaceEntry,
       "zxAnDsInterfaceIndex": zxAnDsInterfaceIndex,
       "zxAnDsInterfaceType": zxAnDsInterfaceType,
       "zxAnDsv6InterfaceType": zxAnDsv6InterfaceType,
       "zxAnDsShow": zxAnDsShow,
       "zxAnDsPortBindViewTable": zxAnDsPortBindViewTable,
       "zxAnDsPortBindViewEntry": zxAnDsPortBindViewEntry,
       "zxAnDsPortBindViewMac": zxAnDsPortBindViewMac,
       "zxAnDsPortBindViewVlan": zxAnDsPortBindViewVlan,
       "zxAnDsPortBindViewIp": zxAnDsPortBindViewIp,
       "zxAnDsPortBindViewType": zxAnDsPortBindViewType,
       "zxAnDsPortBindViewTime": zxAnDsPortBindViewTime,
       "zxAnDsPortBindViewSvlan": zxAnDsPortBindViewSvlan,
       "zxAnDsPortBindViewRowStatus": zxAnDsPortBindViewRowStatus,
       "zxAnDsShowGlobalObjects": zxAnDsShowGlobalObjects,
       "zxAnDsPortBindOnlineUserNum": zxAnDsPortBindOnlineUserNum,
       "zxAnDsUserInterface": zxAnDsUserInterface,
       "zxAnDsUserInterfaceTable": zxAnDsUserInterfaceTable,
       "zxAnDsUserInterfaceEntry": zxAnDsUserInterfaceEntry,
       "zxAnDsUserInterfaceIndex": zxAnDsUserInterfaceIndex,
       "zxAnDsUserInterfaceQuota": zxAnDsUserInterfaceQuota,
       "zxAnDsv6UserInterfaceQuota": zxAnDsv6UserInterfaceQuota,
       "zxAnDsv6Show": zxAnDsv6Show,
       "zxAnDsv6PortBindViewTable": zxAnDsv6PortBindViewTable,
       "zxAnDsv6PortBindViewEntry": zxAnDsv6PortBindViewEntry,
       "zxAnDsv6PortBindViewMac": zxAnDsv6PortBindViewMac,
       "zxAnDsv6PortBindViewVlan": zxAnDsv6PortBindViewVlan,
       "zxAnDsv6PortBindViewIp": zxAnDsv6PortBindViewIp,
       "zxAnDsv6PortBindViewType": zxAnDsv6PortBindViewType,
       "zxAnDsv6PortBindViewTime": zxAnDsv6PortBindViewTime,
       "zxAnDsv6PortBindViewIpPfxLen": zxAnDsv6PortBindViewIpPfxLen,
       "zxAnDsv6PortBindViewSvlan": zxAnDsv6PortBindViewSvlan,
       "zxAnDsv6PortBindViewRowStatus": zxAnDsv6PortBindViewRowStatus,
       "zxAnDsStat": zxAnDsStat,
       "zxAnDhcpSnoopingIfStatTable": zxAnDhcpSnoopingIfStatTable,
       "zxAnDhcpSnoopingIfStatEntry": zxAnDhcpSnoopingIfStatEntry,
       "zxAnDsIfStatRack": zxAnDsIfStatRack,
       "zxAnDsIfStatShelf": zxAnDsIfStatShelf,
       "zxAnDsIfStatSlot": zxAnDsIfStatSlot,
       "zxAnDsIfStatPort": zxAnDsIfStatPort,
       "zxAnDsIfStatOnu": zxAnDsIfStatOnu,
       "zxAnDsIfStatIfType": zxAnDsIfStatIfType,
       "zxAnDsIfStatLogicalId": zxAnDsIfStatLogicalId,
       "zxAnDsIfStatDiscoverPackets": zxAnDsIfStatDiscoverPackets,
       "zxAnDsIfStatOfferPackets": zxAnDsIfStatOfferPackets,
       "zxAnDsIfStatRequestPackets": zxAnDsIfStatRequestPackets,
       "zxAnDsIfStatAckPackets": zxAnDsIfStatAckPackets,
       "zxAnDsIfStatNackPackets": zxAnDsIfStatNackPackets,
       "zxAnDsIfStatReleasePackets": zxAnDsIfStatReleasePackets,
       "zxAnDsIfStatDeclinePackets": zxAnDsIfStatDeclinePackets,
       "zxAnDsIfStatInformPackets": zxAnDsIfStatInformPackets}
)
