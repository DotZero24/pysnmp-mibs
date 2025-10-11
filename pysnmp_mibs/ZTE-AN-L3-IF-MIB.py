# SNMP MIB module (ZTE-AN-L3-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-L3-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:40 2025
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnL3InterfaceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnL3InterfaceObjects_ObjectIdentity = ObjectIdentity
zxAnL3InterfaceObjects = _ZxAnL3InterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1)
)
_ZxAnL3IfTable_Object = MibTable
zxAnL3IfTable = _ZxAnL3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnL3IfTable.setStatus("current")
_ZxAnL3IfEntry_Object = MibTableRow
zxAnL3IfEntry = _ZxAnL3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1)
)
zxAnL3IfEntry.setIndexNames(
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIndex"),
)
if mibBuilder.loadTexts:
    zxAnL3IfEntry.setStatus("current")
_ZxAnL3IfIndex_Type = ZxAnIfindex
_ZxAnL3IfIndex_Object = MibTableColumn
zxAnL3IfIndex = _ZxAnL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 1),
    _ZxAnL3IfIndex_Type()
)
zxAnL3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnL3IfIndex.setStatus("current")


class _ZxAnL3IfName_Type(DisplayString):
    """Custom type zxAnL3IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnL3IfName_Type.__name__ = "DisplayString"
_ZxAnL3IfName_Object = MibTableColumn
zxAnL3IfName = _ZxAnL3IfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 2),
    _ZxAnL3IfName_Type()
)
zxAnL3IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnL3IfName.setStatus("current")
_ZxAnIfReferIndex_Type = Integer32
_ZxAnIfReferIndex_Object = MibTableColumn
zxAnIfReferIndex = _ZxAnIfReferIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 3),
    _ZxAnIfReferIndex_Type()
)
zxAnIfReferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIfReferIndex.setStatus("current")


class _ZxAnL3IfArpProxyEnable_Type(Integer32):
    """Custom type zxAnL3IfArpProxyEnable based on Integer32"""
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


_ZxAnL3IfArpProxyEnable_Type.__name__ = "Integer32"
_ZxAnL3IfArpProxyEnable_Object = MibTableColumn
zxAnL3IfArpProxyEnable = _ZxAnL3IfArpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 4),
    _ZxAnL3IfArpProxyEnable_Type()
)
zxAnL3IfArpProxyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfArpProxyEnable.setStatus("current")
_ZxAnL3IfRowStatus_Type = RowStatus
_ZxAnL3IfRowStatus_Object = MibTableColumn
zxAnL3IfRowStatus = _ZxAnL3IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 5),
    _ZxAnL3IfRowStatus_Type()
)
zxAnL3IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfRowStatus.setStatus("current")


class _ZxAnL3IfArpAgingTime_Type(Integer32):
    """Custom type zxAnL3IfArpAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )


_ZxAnL3IfArpAgingTime_Type.__name__ = "Integer32"
_ZxAnL3IfArpAgingTime_Object = MibTableColumn
zxAnL3IfArpAgingTime = _ZxAnL3IfArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 1, 1, 6),
    _ZxAnL3IfArpAgingTime_Type()
)
zxAnL3IfArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnL3IfArpAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnL3IfArpAgingTime.setUnits("second")
_ZxAnL3IfSuperVlanTable_Object = MibTable
zxAnL3IfSuperVlanTable = _ZxAnL3IfSuperVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnL3IfSuperVlanTable.setStatus("current")
_ZxAnL3IfSuperVlanEntry_Object = MibTableRow
zxAnL3IfSuperVlanEntry = _ZxAnL3IfSuperVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 2, 1)
)
zxAnL3IfSuperVlanEntry.setIndexNames(
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIndex"),
)
if mibBuilder.loadTexts:
    zxAnL3IfSuperVlanEntry.setStatus("current")


class _ZxAnL3IfSubvlanRoutingEnable_Type(Integer32):
    """Custom type zxAnL3IfSubvlanRoutingEnable based on Integer32"""
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


_ZxAnL3IfSubvlanRoutingEnable_Type.__name__ = "Integer32"
_ZxAnL3IfSubvlanRoutingEnable_Object = MibTableColumn
zxAnL3IfSubvlanRoutingEnable = _ZxAnL3IfSubvlanRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 2, 1, 1),
    _ZxAnL3IfSubvlanRoutingEnable_Type()
)
zxAnL3IfSubvlanRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnL3IfSubvlanRoutingEnable.setStatus("current")


class _ZxAnL3IfSubvlanList_Type(OctetString):
    """Custom type zxAnL3IfSubvlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5472),
    )


_ZxAnL3IfSubvlanList_Type.__name__ = "OctetString"
_ZxAnL3IfSubvlanList_Object = MibTableColumn
zxAnL3IfSubvlanList = _ZxAnL3IfSubvlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 2, 1, 2),
    _ZxAnL3IfSubvlanList_Type()
)
zxAnL3IfSubvlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnL3IfSubvlanList.setStatus("current")
_ZxAnL3IfIpAddressTable_Object = MibTable
zxAnL3IfIpAddressTable = _ZxAnL3IfIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnL3IfIpAddressTable.setStatus("current")
_ZxAnL3IfIpAddressEntry_Object = MibTableRow
zxAnL3IfIpAddressEntry = _ZxAnL3IfIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3, 1)
)
zxAnL3IfIpAddressEntry.setIndexNames(
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIndex"),
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIpAddress"),
)
if mibBuilder.loadTexts:
    zxAnL3IfIpAddressEntry.setStatus("current")
_ZxAnL3IfIpAddress_Type = IpAddress
_ZxAnL3IfIpAddress_Object = MibTableColumn
zxAnL3IfIpAddress = _ZxAnL3IfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3, 1, 1),
    _ZxAnL3IfIpAddress_Type()
)
zxAnL3IfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnL3IfIpAddress.setStatus("current")
_ZxAnL3IfIpAddressMask_Type = IpAddress
_ZxAnL3IfIpAddressMask_Object = MibTableColumn
zxAnL3IfIpAddressMask = _ZxAnL3IfIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3, 1, 2),
    _ZxAnL3IfIpAddressMask_Type()
)
zxAnL3IfIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpAddressMask.setStatus("current")


class _ZxAnL3IfIpCategory_Type(Integer32):
    """Custom type zxAnL3IfIpCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_ZxAnL3IfIpCategory_Type.__name__ = "Integer32"
_ZxAnL3IfIpCategory_Object = MibTableColumn
zxAnL3IfIpCategory = _ZxAnL3IfIpCategory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3, 1, 3),
    _ZxAnL3IfIpCategory_Type()
)
zxAnL3IfIpCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpCategory.setStatus("current")
_ZxAnL3IfIpRowStatus_Type = RowStatus
_ZxAnL3IfIpRowStatus_Object = MibTableColumn
zxAnL3IfIpRowStatus = _ZxAnL3IfIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 3, 1, 4),
    _ZxAnL3IfIpRowStatus_Type()
)
zxAnL3IfIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpRowStatus.setStatus("current")
_ZxAnL3IfIpv6IpAddressTable_Object = MibTable
zxAnL3IfIpv6IpAddressTable = _ZxAnL3IfIpv6IpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnL3IfIpv6IpAddressTable.setStatus("current")
_ZxAnL3IfIpv6IpAddressEntry_Object = MibTableRow
zxAnL3IfIpv6IpAddressEntry = _ZxAnL3IfIpv6IpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1)
)
zxAnL3IfIpv6IpAddressEntry.setIndexNames(
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIndex"),
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIpv6IpAddress"),
)
if mibBuilder.loadTexts:
    zxAnL3IfIpv6IpAddressEntry.setStatus("current")
_ZxAnL3IfIpv6IpAddress_Type = InetAddress
_ZxAnL3IfIpv6IpAddress_Object = MibTableColumn
zxAnL3IfIpv6IpAddress = _ZxAnL3IfIpv6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 1),
    _ZxAnL3IfIpv6IpAddress_Type()
)
zxAnL3IfIpv6IpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6IpAddress.setStatus("current")
_ZxAnL3IfIpv6IpPfxLen_Type = InetAddressPrefixLength
_ZxAnL3IfIpv6IpPfxLen_Object = MibTableColumn
zxAnL3IfIpv6IpPfxLen = _ZxAnL3IfIpv6IpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 2),
    _ZxAnL3IfIpv6IpPfxLen_Type()
)
zxAnL3IfIpv6IpPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6IpPfxLen.setStatus("current")


class _ZxAnL3IfIpv6Enable_Type(Integer32):
    """Custom type zxAnL3IfIpv6Enable based on Integer32"""
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


_ZxAnL3IfIpv6Enable_Type.__name__ = "Integer32"
_ZxAnL3IfIpv6Enable_Object = MibTableColumn
zxAnL3IfIpv6Enable = _ZxAnL3IfIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 3),
    _ZxAnL3IfIpv6Enable_Type()
)
zxAnL3IfIpv6Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6Enable.setStatus("current")


class _ZxAnL3IfIpv6Mtu_Type(Integer32):
    """Custom type zxAnL3IfIpv6Mtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 1500),
    )


_ZxAnL3IfIpv6Mtu_Type.__name__ = "Integer32"
_ZxAnL3IfIpv6Mtu_Object = MibTableColumn
zxAnL3IfIpv6Mtu = _ZxAnL3IfIpv6Mtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 4),
    _ZxAnL3IfIpv6Mtu_Type()
)
zxAnL3IfIpv6Mtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6Mtu.setStatus("current")


class _ZxAnL3IfIpv6DadAttemps_Type(Integer32):
    """Custom type zxAnL3IfIpv6DadAttemps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnL3IfIpv6DadAttemps_Type.__name__ = "Integer32"
_ZxAnL3IfIpv6DadAttemps_Object = MibTableColumn
zxAnL3IfIpv6DadAttemps = _ZxAnL3IfIpv6DadAttemps_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 5),
    _ZxAnL3IfIpv6DadAttemps_Type()
)
zxAnL3IfIpv6DadAttemps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6DadAttemps.setStatus("current")
_ZxAnL3IfIpv6RowStatus_Type = RowStatus
_ZxAnL3IfIpv6RowStatus_Object = MibTableColumn
zxAnL3IfIpv6RowStatus = _ZxAnL3IfIpv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 1, 4, 1, 20),
    _ZxAnL3IfIpv6RowStatus_Type()
)
zxAnL3IfIpv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfIpv6RowStatus.setStatus("current")
_ZxAnL3InterfaceTrapObjects_ObjectIdentity = ObjectIdentity
zxAnL3InterfaceTrapObjects = _ZxAnL3InterfaceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-L3-IF-MIB",
    **{"zxAnL3InterfaceMib": zxAnL3InterfaceMib,
       "zxAnL3InterfaceObjects": zxAnL3InterfaceObjects,
       "zxAnL3IfTable": zxAnL3IfTable,
       "zxAnL3IfEntry": zxAnL3IfEntry,
       "zxAnL3IfIndex": zxAnL3IfIndex,
       "zxAnL3IfName": zxAnL3IfName,
       "zxAnIfReferIndex": zxAnIfReferIndex,
       "zxAnL3IfArpProxyEnable": zxAnL3IfArpProxyEnable,
       "zxAnL3IfRowStatus": zxAnL3IfRowStatus,
       "zxAnL3IfArpAgingTime": zxAnL3IfArpAgingTime,
       "zxAnL3IfSuperVlanTable": zxAnL3IfSuperVlanTable,
       "zxAnL3IfSuperVlanEntry": zxAnL3IfSuperVlanEntry,
       "zxAnL3IfSubvlanRoutingEnable": zxAnL3IfSubvlanRoutingEnable,
       "zxAnL3IfSubvlanList": zxAnL3IfSubvlanList,
       "zxAnL3IfIpAddressTable": zxAnL3IfIpAddressTable,
       "zxAnL3IfIpAddressEntry": zxAnL3IfIpAddressEntry,
       "zxAnL3IfIpAddress": zxAnL3IfIpAddress,
       "zxAnL3IfIpAddressMask": zxAnL3IfIpAddressMask,
       "zxAnL3IfIpCategory": zxAnL3IfIpCategory,
       "zxAnL3IfIpRowStatus": zxAnL3IfIpRowStatus,
       "zxAnL3IfIpv6IpAddressTable": zxAnL3IfIpv6IpAddressTable,
       "zxAnL3IfIpv6IpAddressEntry": zxAnL3IfIpv6IpAddressEntry,
       "zxAnL3IfIpv6IpAddress": zxAnL3IfIpv6IpAddress,
       "zxAnL3IfIpv6IpPfxLen": zxAnL3IfIpv6IpPfxLen,
       "zxAnL3IfIpv6Enable": zxAnL3IfIpv6Enable,
       "zxAnL3IfIpv6Mtu": zxAnL3IfIpv6Mtu,
       "zxAnL3IfIpv6DadAttemps": zxAnL3IfIpv6DadAttemps,
       "zxAnL3IfIpv6RowStatus": zxAnL3IfIpv6RowStatus,
       "zxAnL3InterfaceTrapObjects": zxAnL3InterfaceTrapObjects}
)
