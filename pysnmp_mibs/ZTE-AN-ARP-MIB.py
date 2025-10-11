# SNMP MIB module (ZTE-AN-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:22 2025
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnArpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnArpMibObjects_ObjectIdentity = ObjectIdentity
zxAnArpMibObjects = _ZxAnArpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1)
)


class _ZxAnArpAntiSpoofingGlbEnable_Type(TruthValue):
    """Custom type zxAnArpAntiSpoofingGlbEnable based on TruthValue"""
    defaultValue = 2


_ZxAnArpAntiSpoofingGlbEnable_Type.__name__ = "TruthValue"
_ZxAnArpAntiSpoofingGlbEnable_Object = MibScalar
zxAnArpAntiSpoofingGlbEnable = _ZxAnArpAntiSpoofingGlbEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 1),
    _ZxAnArpAntiSpoofingGlbEnable_Type()
)
zxAnArpAntiSpoofingGlbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingGlbEnable.setStatus("current")


class _ZxAnArpCapabilities_Type(Bits):
    """Custom type zxAnArpCapabilities based on Bits"""
    namedValues = NamedValues(
        ("mffMultiGateway", 0)
    )

_ZxAnArpCapabilities_Type.__name__ = "Bits"
_ZxAnArpCapabilities_Object = MibScalar
zxAnArpCapabilities = _ZxAnArpCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 2),
    _ZxAnArpCapabilities_Type()
)
zxAnArpCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnArpCapabilities.setStatus("current")
_ZxAnArpVlanConfTable_Object = MibTable
zxAnArpVlanConfTable = _ZxAnArpVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10)
)
if mibBuilder.loadTexts:
    zxAnArpVlanConfTable.setStatus("current")
_ZxAnArpVlanConfEntry_Object = MibTableRow
zxAnArpVlanConfEntry = _ZxAnArpVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10, 1)
)
zxAnArpVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpVlanConfStartVlan"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpVlanConfEndVlan"),
)
if mibBuilder.loadTexts:
    zxAnArpVlanConfEntry.setStatus("current")
_ZxAnArpVlanConfStartVlan_Type = Integer32
_ZxAnArpVlanConfStartVlan_Object = MibTableColumn
zxAnArpVlanConfStartVlan = _ZxAnArpVlanConfStartVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10, 1, 1),
    _ZxAnArpVlanConfStartVlan_Type()
)
zxAnArpVlanConfStartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpVlanConfStartVlan.setStatus("current")
_ZxAnArpVlanConfEndVlan_Type = Integer32
_ZxAnArpVlanConfEndVlan_Object = MibTableColumn
zxAnArpVlanConfEndVlan = _ZxAnArpVlanConfEndVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10, 1, 2),
    _ZxAnArpVlanConfEndVlan_Type()
)
zxAnArpVlanConfEndVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpVlanConfEndVlan.setStatus("current")


class _ZxAnArpVlanConfSecurityEnable_Type(Integer32):
    """Custom type zxAnArpVlanConfSecurityEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnArpVlanConfSecurityEnable_Type.__name__ = "Integer32"
_ZxAnArpVlanConfSecurityEnable_Object = MibTableColumn
zxAnArpVlanConfSecurityEnable = _ZxAnArpVlanConfSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10, 1, 3),
    _ZxAnArpVlanConfSecurityEnable_Type()
)
zxAnArpVlanConfSecurityEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpVlanConfSecurityEnable.setStatus("current")
_ZxAnArpVlanConfRowStatus_Type = RowStatus
_ZxAnArpVlanConfRowStatus_Object = MibTableColumn
zxAnArpVlanConfRowStatus = _ZxAnArpVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 10, 1, 4),
    _ZxAnArpVlanConfRowStatus_Type()
)
zxAnArpVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpVlanConfRowStatus.setStatus("current")
_ZxAnArpMapConfTable_Object = MibTable
zxAnArpMapConfTable = _ZxAnArpMapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnArpMapConfTable.setStatus("current")
_ZxAnArpMapConfEntry_Object = MibTableRow
zxAnArpMapConfEntry = _ZxAnArpMapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1)
)
zxAnArpMapConfEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMapConfIpAddr"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMapConfVlan"),
)
if mibBuilder.loadTexts:
    zxAnArpMapConfEntry.setStatus("current")
_ZxAnArpMapConfIpAddr_Type = IpAddress
_ZxAnArpMapConfIpAddr_Object = MibTableColumn
zxAnArpMapConfIpAddr = _ZxAnArpMapConfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1, 1),
    _ZxAnArpMapConfIpAddr_Type()
)
zxAnArpMapConfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMapConfIpAddr.setStatus("current")
_ZxAnArpMapConfVlan_Type = Integer32
_ZxAnArpMapConfVlan_Object = MibTableColumn
zxAnArpMapConfVlan = _ZxAnArpMapConfVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1, 2),
    _ZxAnArpMapConfVlan_Type()
)
zxAnArpMapConfVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMapConfVlan.setStatus("current")
_ZxAnArpMapConfMacAddr_Type = MacAddress
_ZxAnArpMapConfMacAddr_Object = MibTableColumn
zxAnArpMapConfMacAddr = _ZxAnArpMapConfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1, 3),
    _ZxAnArpMapConfMacAddr_Type()
)
zxAnArpMapConfMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMapConfMacAddr.setStatus("current")
_ZxAnArpMapConfIfindex_Type = ZxAnIfindex
_ZxAnArpMapConfIfindex_Object = MibTableColumn
zxAnArpMapConfIfindex = _ZxAnArpMapConfIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1, 4),
    _ZxAnArpMapConfIfindex_Type()
)
zxAnArpMapConfIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMapConfIfindex.setStatus("current")
_ZxAnArpMapConfRowStatus_Type = RowStatus
_ZxAnArpMapConfRowStatus_Object = MibTableColumn
zxAnArpMapConfRowStatus = _ZxAnArpMapConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 11, 1, 5),
    _ZxAnArpMapConfRowStatus_Type()
)
zxAnArpMapConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMapConfRowStatus.setStatus("current")
_ZxAnArpMapInfoTable_Object = MibTable
zxAnArpMapInfoTable = _ZxAnArpMapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 12)
)
if mibBuilder.loadTexts:
    zxAnArpMapInfoTable.setStatus("current")
_ZxAnArpMapInfoEntry_Object = MibTableRow
zxAnArpMapInfoEntry = _ZxAnArpMapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 12, 1)
)
zxAnArpMapInfoEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMapConfIpAddr"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMapConfVlan"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMapInfoType"),
)
if mibBuilder.loadTexts:
    zxAnArpMapInfoEntry.setStatus("current")


class _ZxAnArpMapInfoType_Type(Integer32):
    """Custom type zxAnArpMapInfoType based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("ipoas", 3),
          ("ipoad", 4),
          ("dynamic", 5))
    )


_ZxAnArpMapInfoType_Type.__name__ = "Integer32"
_ZxAnArpMapInfoType_Object = MibTableColumn
zxAnArpMapInfoType = _ZxAnArpMapInfoType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 12, 1, 1),
    _ZxAnArpMapInfoType_Type()
)
zxAnArpMapInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMapInfoType.setStatus("current")
_ZxAnArpMapInfoMacAddr_Type = MacAddress
_ZxAnArpMapInfoMacAddr_Object = MibTableColumn
zxAnArpMapInfoMacAddr = _ZxAnArpMapInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 12, 1, 2),
    _ZxAnArpMapInfoMacAddr_Type()
)
zxAnArpMapInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnArpMapInfoMacAddr.setStatus("current")
_ZxAnArpMapInfoIfindex_Type = ZxAnIfindex
_ZxAnArpMapInfoIfindex_Object = MibTableColumn
zxAnArpMapInfoIfindex = _ZxAnArpMapInfoIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 12, 1, 3),
    _ZxAnArpMapInfoIfindex_Type()
)
zxAnArpMapInfoIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnArpMapInfoIfindex.setStatus("current")
_ZxAnArpMffCfg_ObjectIdentity = ObjectIdentity
zxAnArpMffCfg = _ZxAnArpMffCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16)
)


class _ZxAnArpMffCfgEnable_Type(TruthValue):
    """Custom type zxAnArpMffCfgEnable based on TruthValue"""
    defaultValue = 2


_ZxAnArpMffCfgEnable_Type.__name__ = "TruthValue"
_ZxAnArpMffCfgEnable_Object = MibScalar
zxAnArpMffCfgEnable = _ZxAnArpMffCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 1),
    _ZxAnArpMffCfgEnable_Type()
)
zxAnArpMffCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnArpMffCfgEnable.setStatus("current")
_ZxAnArpMffCfgTable_Object = MibTable
zxAnArpMffCfgTable = _ZxAnArpMffCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2)
)
if mibBuilder.loadTexts:
    zxAnArpMffCfgTable.setStatus("current")
_ZxAnArpMffCfgEntry_Object = MibTableRow
zxAnArpMffCfgEntry = _ZxAnArpMffCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1)
)
zxAnArpMffCfgEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMffCfgVlan"),
)
if mibBuilder.loadTexts:
    zxAnArpMffCfgEntry.setStatus("current")


class _ZxAnArpMffCfgVlan_Type(Integer32):
    """Custom type zxAnArpMffCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpMffCfgVlan_Type.__name__ = "Integer32"
_ZxAnArpMffCfgVlan_Object = MibTableColumn
zxAnArpMffCfgVlan = _ZxAnArpMffCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1, 1),
    _ZxAnArpMffCfgVlan_Type()
)
zxAnArpMffCfgVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMffCfgVlan.setStatus("current")


class _ZxAnArpMffCfgGatewayMode_Type(Integer32):
    """Custom type zxAnArpMffCfgGatewayMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_ZxAnArpMffCfgGatewayMode_Type.__name__ = "Integer32"
_ZxAnArpMffCfgGatewayMode_Object = MibTableColumn
zxAnArpMffCfgGatewayMode = _ZxAnArpMffCfgGatewayMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1, 2),
    _ZxAnArpMffCfgGatewayMode_Type()
)
zxAnArpMffCfgGatewayMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffCfgGatewayMode.setStatus("deprecated")
_ZxAnArpMffCfgGatewayIp_Type = IpAddress
_ZxAnArpMffCfgGatewayIp_Object = MibTableColumn
zxAnArpMffCfgGatewayIp = _ZxAnArpMffCfgGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1, 3),
    _ZxAnArpMffCfgGatewayIp_Type()
)
zxAnArpMffCfgGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffCfgGatewayIp.setStatus("current")
_ZxAnArpMffCfgGatewayMac_Type = MacAddress
_ZxAnArpMffCfgGatewayMac_Object = MibTableColumn
zxAnArpMffCfgGatewayMac = _ZxAnArpMffCfgGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1, 4),
    _ZxAnArpMffCfgGatewayMac_Type()
)
zxAnArpMffCfgGatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffCfgGatewayMac.setStatus("current")
_ZxAnArpMffCfgRowStatus_Type = RowStatus
_ZxAnArpMffCfgRowStatus_Object = MibTableColumn
zxAnArpMffCfgRowStatus = _ZxAnArpMffCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 2, 1, 50),
    _ZxAnArpMffCfgRowStatus_Type()
)
zxAnArpMffCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffCfgRowStatus.setStatus("current")
_ZxAnArpMffMultiGatewayTable_Object = MibTable
zxAnArpMffMultiGatewayTable = _ZxAnArpMffMultiGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4)
)
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayTable.setStatus("current")
_ZxAnArpMffMultiGatewayEntry_Object = MibTableRow
zxAnArpMffMultiGatewayEntry = _ZxAnArpMffMultiGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1)
)
zxAnArpMffMultiGatewayEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMffMultiGatewayMffVid"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpMffMultiGatewayIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayEntry.setStatus("current")


class _ZxAnArpMffMultiGatewayMffVid_Type(Integer32):
    """Custom type zxAnArpMffMultiGatewayMffVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpMffMultiGatewayMffVid_Type.__name__ = "Integer32"
_ZxAnArpMffMultiGatewayMffVid_Object = MibTableColumn
zxAnArpMffMultiGatewayMffVid = _ZxAnArpMffMultiGatewayMffVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 1),
    _ZxAnArpMffMultiGatewayMffVid_Type()
)
zxAnArpMffMultiGatewayMffVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayMffVid.setStatus("current")
_ZxAnArpMffMultiGatewayIpAddr_Type = IpAddress
_ZxAnArpMffMultiGatewayIpAddr_Object = MibTableColumn
zxAnArpMffMultiGatewayIpAddr = _ZxAnArpMffMultiGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 2),
    _ZxAnArpMffMultiGatewayIpAddr_Type()
)
zxAnArpMffMultiGatewayIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayIpAddr.setStatus("current")
_ZxAnArpMffMultiGatewayIpMask_Type = IpAddress
_ZxAnArpMffMultiGatewayIpMask_Object = MibTableColumn
zxAnArpMffMultiGatewayIpMask = _ZxAnArpMffMultiGatewayIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 3),
    _ZxAnArpMffMultiGatewayIpMask_Type()
)
zxAnArpMffMultiGatewayIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayIpMask.setStatus("current")


class _ZxAnArpMffMultiGatewayMacMode_Type(Integer32):
    """Custom type zxAnArpMffMultiGatewayMacMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_ZxAnArpMffMultiGatewayMacMode_Type.__name__ = "Integer32"
_ZxAnArpMffMultiGatewayMacMode_Object = MibTableColumn
zxAnArpMffMultiGatewayMacMode = _ZxAnArpMffMultiGatewayMacMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 4),
    _ZxAnArpMffMultiGatewayMacMode_Type()
)
zxAnArpMffMultiGatewayMacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayMacMode.setStatus("current")
_ZxAnArpMffMultiGatewayMac_Type = MacAddress
_ZxAnArpMffMultiGatewayMac_Object = MibTableColumn
zxAnArpMffMultiGatewayMac = _ZxAnArpMffMultiGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 5),
    _ZxAnArpMffMultiGatewayMac_Type()
)
zxAnArpMffMultiGatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayMac.setStatus("current")
_ZxAnArpMffMultiGatewayRowStatus_Type = RowStatus
_ZxAnArpMffMultiGatewayRowStatus_Object = MibTableColumn
zxAnArpMffMultiGatewayRowStatus = _ZxAnArpMffMultiGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 16, 4, 1, 50),
    _ZxAnArpMffMultiGatewayRowStatus_Type()
)
zxAnArpMffMultiGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpMffMultiGatewayRowStatus.setStatus("current")
_ZxAnArpAntiSpoofingCfgTable_Object = MibTable
zxAnArpAntiSpoofingCfgTable = _ZxAnArpAntiSpoofingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 17)
)
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingCfgTable.setStatus("current")
_ZxAnArpAntiSpoofingCfgEntry_Object = MibTableRow
zxAnArpAntiSpoofingCfgEntry = _ZxAnArpAntiSpoofingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 17, 1)
)
zxAnArpAntiSpoofingCfgEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpAntiSpoofingVid"),
)
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingCfgEntry.setStatus("current")


class _ZxAnArpAntiSpoofingVid_Type(Integer32):
    """Custom type zxAnArpAntiSpoofingVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpAntiSpoofingVid_Type.__name__ = "Integer32"
_ZxAnArpAntiSpoofingVid_Object = MibTableColumn
zxAnArpAntiSpoofingVid = _ZxAnArpAntiSpoofingVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 17, 1, 1),
    _ZxAnArpAntiSpoofingVid_Type()
)
zxAnArpAntiSpoofingVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingVid.setStatus("current")


class _ZxAnArpAntiSpoofingDirection_Type(Integer32):
    """Custom type zxAnArpAntiSpoofingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2),
          ("all", 3))
    )


_ZxAnArpAntiSpoofingDirection_Type.__name__ = "Integer32"
_ZxAnArpAntiSpoofingDirection_Object = MibTableColumn
zxAnArpAntiSpoofingDirection = _ZxAnArpAntiSpoofingDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 17, 1, 2),
    _ZxAnArpAntiSpoofingDirection_Type()
)
zxAnArpAntiSpoofingDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingDirection.setStatus("current")
_ZxAnArpAntiSpoofingVlanRowStatus_Type = RowStatus
_ZxAnArpAntiSpoofingVlanRowStatus_Object = MibTableColumn
zxAnArpAntiSpoofingVlanRowStatus = _ZxAnArpAntiSpoofingVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 17, 1, 50),
    _ZxAnArpAntiSpoofingVlanRowStatus_Type()
)
zxAnArpAntiSpoofingVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingVlanRowStatus.setStatus("current")
_ZxAnArpGateway_ObjectIdentity = ObjectIdentity
zxAnArpGateway = _ZxAnArpGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18)
)
_ZxAnArpGatewayTable_Object = MibTable
zxAnArpGatewayTable = _ZxAnArpGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1)
)
if mibBuilder.loadTexts:
    zxAnArpGatewayTable.setStatus("current")
_ZxAnArpGatewayEntry_Object = MibTableRow
zxAnArpGatewayEntry = _ZxAnArpGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1)
)
zxAnArpGatewayEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpGatewayVlan"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpGatewayMode"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpGatewayIp"),
)
if mibBuilder.loadTexts:
    zxAnArpGatewayEntry.setStatus("current")


class _ZxAnArpGatewayVlan_Type(Integer32):
    """Custom type zxAnArpGatewayVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpGatewayVlan_Type.__name__ = "Integer32"
_ZxAnArpGatewayVlan_Object = MibTableColumn
zxAnArpGatewayVlan = _ZxAnArpGatewayVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1, 1),
    _ZxAnArpGatewayVlan_Type()
)
zxAnArpGatewayVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpGatewayVlan.setStatus("current")


class _ZxAnArpGatewayMode_Type(Integer32):
    """Custom type zxAnArpGatewayMode based on Integer32"""
    defaultValue = 1

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
        *(("static", 1),
          ("dhcp", 2),
          ("ipoastatic", 3),
          ("ipoadynamic", 4),
          ("staticIp", 5))
    )


_ZxAnArpGatewayMode_Type.__name__ = "Integer32"
_ZxAnArpGatewayMode_Object = MibTableColumn
zxAnArpGatewayMode = _ZxAnArpGatewayMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1, 2),
    _ZxAnArpGatewayMode_Type()
)
zxAnArpGatewayMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpGatewayMode.setStatus("current")
_ZxAnArpGatewayIp_Type = IpAddress
_ZxAnArpGatewayIp_Object = MibTableColumn
zxAnArpGatewayIp = _ZxAnArpGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1, 3),
    _ZxAnArpGatewayIp_Type()
)
zxAnArpGatewayIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpGatewayIp.setStatus("current")
_ZxAnArpGatewayMacAddr_Type = MacAddress
_ZxAnArpGatewayMacAddr_Object = MibTableColumn
zxAnArpGatewayMacAddr = _ZxAnArpGatewayMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1, 4),
    _ZxAnArpGatewayMacAddr_Type()
)
zxAnArpGatewayMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpGatewayMacAddr.setStatus("current")
_ZxAnArpGatewayRowStatus_Type = RowStatus
_ZxAnArpGatewayRowStatus_Object = MibTableColumn
zxAnArpGatewayRowStatus = _ZxAnArpGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 18, 1, 1, 50),
    _ZxAnArpGatewayRowStatus_Type()
)
zxAnArpGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpGatewayRowStatus.setStatus("current")
_ZxAnArpDaiObjects_ObjectIdentity = ObjectIdentity
zxAnArpDaiObjects = _ZxAnArpDaiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19)
)
_ZxAnArpDaiIfCfgTable_Object = MibTable
zxAnArpDaiIfCfgTable = _ZxAnArpDaiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2)
)
if mibBuilder.loadTexts:
    zxAnArpDaiIfCfgTable.setStatus("current")
_ZxAnArpDaiIfCfgEntry_Object = MibTableRow
zxAnArpDaiIfCfgEntry = _ZxAnArpDaiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1)
)
zxAnArpDaiIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpRack"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpShelf"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpSlot"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpPort"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpOnu"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpIfType"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnArpDaiIfCfgEntry.setStatus("current")
_ZxAnArpRack_Type = Integer32
_ZxAnArpRack_Object = MibTableColumn
zxAnArpRack = _ZxAnArpRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 1),
    _ZxAnArpRack_Type()
)
zxAnArpRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpRack.setStatus("current")
_ZxAnArpShelf_Type = Integer32
_ZxAnArpShelf_Object = MibTableColumn
zxAnArpShelf = _ZxAnArpShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 2),
    _ZxAnArpShelf_Type()
)
zxAnArpShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpShelf.setStatus("current")
_ZxAnArpSlot_Type = Integer32
_ZxAnArpSlot_Object = MibTableColumn
zxAnArpSlot = _ZxAnArpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 3),
    _ZxAnArpSlot_Type()
)
zxAnArpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpSlot.setStatus("current")
_ZxAnArpPort_Type = Integer32
_ZxAnArpPort_Object = MibTableColumn
zxAnArpPort = _ZxAnArpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 4),
    _ZxAnArpPort_Type()
)
zxAnArpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpPort.setStatus("current")
_ZxAnArpOnu_Type = Integer32
_ZxAnArpOnu_Object = MibTableColumn
zxAnArpOnu = _ZxAnArpOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 5),
    _ZxAnArpOnu_Type()
)
zxAnArpOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpOnu.setStatus("current")


class _ZxAnArpIfType_Type(Integer32):
    """Custom type zxAnArpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("ponOnu", 3),
          ("ponVPort", 4),
          ("servicePort", 11))
    )


_ZxAnArpIfType_Type.__name__ = "Integer32"
_ZxAnArpIfType_Object = MibTableColumn
zxAnArpIfType = _ZxAnArpIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 6),
    _ZxAnArpIfType_Type()
)
zxAnArpIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpIfType.setStatus("current")
_ZxAnArpLogicalId_Type = ObjectIdentifier
_ZxAnArpLogicalId_Object = MibTableColumn
zxAnArpLogicalId = _ZxAnArpLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 7),
    _ZxAnArpLogicalId_Type()
)
zxAnArpLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpLogicalId.setStatus("current")


class _ZxAnArpAntiSpoofingIfLogEnable_Type(Integer32):
    """Custom type zxAnArpAntiSpoofingIfLogEnable based on Integer32"""
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


_ZxAnArpAntiSpoofingIfLogEnable_Type.__name__ = "Integer32"
_ZxAnArpAntiSpoofingIfLogEnable_Object = MibTableColumn
zxAnArpAntiSpoofingIfLogEnable = _ZxAnArpAntiSpoofingIfLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 19, 2, 1, 8),
    _ZxAnArpAntiSpoofingIfLogEnable_Type()
)
zxAnArpAntiSpoofingIfLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnArpAntiSpoofingIfLogEnable.setStatus("current")
_ZxAnArpReplyAgentObjects_ObjectIdentity = ObjectIdentity
zxAnArpReplyAgentObjects = _ZxAnArpReplyAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 20)
)
_ZxAnArpReplyAgentIfCfgTable_Object = MibTable
zxAnArpReplyAgentIfCfgTable = _ZxAnArpReplyAgentIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 20, 2)
)
if mibBuilder.loadTexts:
    zxAnArpReplyAgentIfCfgTable.setStatus("current")
_ZxAnArpReplyAgentIfCfgEntry_Object = MibTableRow
zxAnArpReplyAgentIfCfgEntry = _ZxAnArpReplyAgentIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 20, 2, 1)
)
zxAnArpReplyAgentIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpRack"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpShelf"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpSlot"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpPort"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpOnu"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpIfType"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnArpReplyAgentIfCfgEntry.setStatus("current")


class _ZxAnArpReplyAgentIfEnable_Type(Integer32):
    """Custom type zxAnArpReplyAgentIfEnable based on Integer32"""
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


_ZxAnArpReplyAgentIfEnable_Type.__name__ = "Integer32"
_ZxAnArpReplyAgentIfEnable_Object = MibTableColumn
zxAnArpReplyAgentIfEnable = _ZxAnArpReplyAgentIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 20, 2, 1, 1),
    _ZxAnArpReplyAgentIfEnable_Type()
)
zxAnArpReplyAgentIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnArpReplyAgentIfEnable.setStatus("current")
_ZxAnArpPacketLimitObjects_ObjectIdentity = ObjectIdentity
zxAnArpPacketLimitObjects = _ZxAnArpPacketLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 21)
)
_ZxAnArpPacketLimitIfCfgTable_Object = MibTable
zxAnArpPacketLimitIfCfgTable = _ZxAnArpPacketLimitIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 21, 2)
)
if mibBuilder.loadTexts:
    zxAnArpPacketLimitIfCfgTable.setStatus("current")
_ZxAnArpPacketLimitIfCfgEntry_Object = MibTableRow
zxAnArpPacketLimitIfCfgEntry = _ZxAnArpPacketLimitIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 21, 2, 1)
)
zxAnArpPacketLimitIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpRack"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpShelf"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpSlot"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpPort"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpOnu"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpIfType"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnArpPacketLimitIfCfgEntry.setStatus("current")


class _ZxAnArpBcastSuppressIfEnable_Type(Integer32):
    """Custom type zxAnArpBcastSuppressIfEnable based on Integer32"""
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


_ZxAnArpBcastSuppressIfEnable_Type.__name__ = "Integer32"
_ZxAnArpBcastSuppressIfEnable_Object = MibTableColumn
zxAnArpBcastSuppressIfEnable = _ZxAnArpBcastSuppressIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 21, 2, 1, 1),
    _ZxAnArpBcastSuppressIfEnable_Type()
)
zxAnArpBcastSuppressIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnArpBcastSuppressIfEnable.setStatus("current")
_ZxAnArpAgentObjects_ObjectIdentity = ObjectIdentity
zxAnArpAgentObjects = _ZxAnArpAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22)
)
_ZxAnArpAgentGatewayTable_Object = MibTable
zxAnArpAgentGatewayTable = _ZxAnArpAgentGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2)
)
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayTable.setStatus("current")
_ZxAnArpAgentGatewayEntry_Object = MibTableRow
zxAnArpAgentGatewayEntry = _ZxAnArpAgentGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1)
)
zxAnArpAgentGatewayEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpAgentGatewaySvid"),
    (0, "ZTE-AN-ARP-MIB", "zxAnArpAgentGatewayCvid"),
)
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayEntry.setStatus("current")


class _ZxAnArpAgentGatewaySvid_Type(Integer32):
    """Custom type zxAnArpAgentGatewaySvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpAgentGatewaySvid_Type.__name__ = "Integer32"
_ZxAnArpAgentGatewaySvid_Object = MibTableColumn
zxAnArpAgentGatewaySvid = _ZxAnArpAgentGatewaySvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 1),
    _ZxAnArpAgentGatewaySvid_Type()
)
zxAnArpAgentGatewaySvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewaySvid.setStatus("current")


class _ZxAnArpAgentGatewayCvid_Type(Integer32):
    """Custom type zxAnArpAgentGatewayCvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnArpAgentGatewayCvid_Type.__name__ = "Integer32"
_ZxAnArpAgentGatewayCvid_Object = MibTableColumn
zxAnArpAgentGatewayCvid = _ZxAnArpAgentGatewayCvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 2),
    _ZxAnArpAgentGatewayCvid_Type()
)
zxAnArpAgentGatewayCvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayCvid.setStatus("current")


class _ZxAnArpAgentGatewayStatus_Type(Integer32):
    """Custom type zxAnArpAgentGatewayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_ZxAnArpAgentGatewayStatus_Type.__name__ = "Integer32"
_ZxAnArpAgentGatewayStatus_Object = MibTableColumn
zxAnArpAgentGatewayStatus = _ZxAnArpAgentGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 3),
    _ZxAnArpAgentGatewayStatus_Type()
)
zxAnArpAgentGatewayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayStatus.setStatus("current")
_ZxAnArpAgentGatewayIpAddr_Type = IpAddress
_ZxAnArpAgentGatewayIpAddr_Object = MibTableColumn
zxAnArpAgentGatewayIpAddr = _ZxAnArpAgentGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 4),
    _ZxAnArpAgentGatewayIpAddr_Type()
)
zxAnArpAgentGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayIpAddr.setStatus("current")
_ZxAnArpAgentGatewayMac_Type = MacAddress
_ZxAnArpAgentGatewayMac_Object = MibTableColumn
zxAnArpAgentGatewayMac = _ZxAnArpAgentGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 5),
    _ZxAnArpAgentGatewayMac_Type()
)
zxAnArpAgentGatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayMac.setStatus("current")
_ZxAnArpAgentGatewayRowStatus_Type = RowStatus
_ZxAnArpAgentGatewayRowStatus_Object = MibTableColumn
zxAnArpAgentGatewayRowStatus = _ZxAnArpAgentGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 22, 2, 1, 50),
    _ZxAnArpAgentGatewayRowStatus_Type()
)
zxAnArpAgentGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpAgentGatewayRowStatus.setStatus("current")
_ZxAnArpFilterObjects_ObjectIdentity = ObjectIdentity
zxAnArpFilterObjects = _ZxAnArpFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 23)
)
_ZxAnArpFilterVlanConfTable_Object = MibTable
zxAnArpFilterVlanConfTable = _ZxAnArpFilterVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 23, 2)
)
if mibBuilder.loadTexts:
    zxAnArpFilterVlanConfTable.setStatus("current")
_ZxAnArpFilterVlanConfEntry_Object = MibTableRow
zxAnArpFilterVlanConfEntry = _ZxAnArpFilterVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 23, 2, 1)
)
zxAnArpFilterVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-ARP-MIB", "zxAnArpFilterVlanConfVid"),
)
if mibBuilder.loadTexts:
    zxAnArpFilterVlanConfEntry.setStatus("current")


class _ZxAnArpFilterVlanConfVid_Type(Integer32):
    """Custom type zxAnArpFilterVlanConfVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnArpFilterVlanConfVid_Type.__name__ = "Integer32"
_ZxAnArpFilterVlanConfVid_Object = MibTableColumn
zxAnArpFilterVlanConfVid = _ZxAnArpFilterVlanConfVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 23, 2, 1, 1),
    _ZxAnArpFilterVlanConfVid_Type()
)
zxAnArpFilterVlanConfVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnArpFilterVlanConfVid.setStatus("current")
_ZxAnArpFilterVlanConfRowStatus_Type = RowStatus
_ZxAnArpFilterVlanConfRowStatus_Object = MibTableColumn
zxAnArpFilterVlanConfRowStatus = _ZxAnArpFilterVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 34, 1, 23, 2, 1, 50),
    _ZxAnArpFilterVlanConfRowStatus_Type()
)
zxAnArpFilterVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnArpFilterVlanConfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ARP-MIB",
    **{"zxAnArpMib": zxAnArpMib,
       "zxAnArpMibObjects": zxAnArpMibObjects,
       "zxAnArpAntiSpoofingGlbEnable": zxAnArpAntiSpoofingGlbEnable,
       "zxAnArpCapabilities": zxAnArpCapabilities,
       "zxAnArpVlanConfTable": zxAnArpVlanConfTable,
       "zxAnArpVlanConfEntry": zxAnArpVlanConfEntry,
       "zxAnArpVlanConfStartVlan": zxAnArpVlanConfStartVlan,
       "zxAnArpVlanConfEndVlan": zxAnArpVlanConfEndVlan,
       "zxAnArpVlanConfSecurityEnable": zxAnArpVlanConfSecurityEnable,
       "zxAnArpVlanConfRowStatus": zxAnArpVlanConfRowStatus,
       "zxAnArpMapConfTable": zxAnArpMapConfTable,
       "zxAnArpMapConfEntry": zxAnArpMapConfEntry,
       "zxAnArpMapConfIpAddr": zxAnArpMapConfIpAddr,
       "zxAnArpMapConfVlan": zxAnArpMapConfVlan,
       "zxAnArpMapConfMacAddr": zxAnArpMapConfMacAddr,
       "zxAnArpMapConfIfindex": zxAnArpMapConfIfindex,
       "zxAnArpMapConfRowStatus": zxAnArpMapConfRowStatus,
       "zxAnArpMapInfoTable": zxAnArpMapInfoTable,
       "zxAnArpMapInfoEntry": zxAnArpMapInfoEntry,
       "zxAnArpMapInfoType": zxAnArpMapInfoType,
       "zxAnArpMapInfoMacAddr": zxAnArpMapInfoMacAddr,
       "zxAnArpMapInfoIfindex": zxAnArpMapInfoIfindex,
       "zxAnArpMffCfg": zxAnArpMffCfg,
       "zxAnArpMffCfgEnable": zxAnArpMffCfgEnable,
       "zxAnArpMffCfgTable": zxAnArpMffCfgTable,
       "zxAnArpMffCfgEntry": zxAnArpMffCfgEntry,
       "zxAnArpMffCfgVlan": zxAnArpMffCfgVlan,
       "zxAnArpMffCfgGatewayMode": zxAnArpMffCfgGatewayMode,
       "zxAnArpMffCfgGatewayIp": zxAnArpMffCfgGatewayIp,
       "zxAnArpMffCfgGatewayMac": zxAnArpMffCfgGatewayMac,
       "zxAnArpMffCfgRowStatus": zxAnArpMffCfgRowStatus,
       "zxAnArpMffMultiGatewayTable": zxAnArpMffMultiGatewayTable,
       "zxAnArpMffMultiGatewayEntry": zxAnArpMffMultiGatewayEntry,
       "zxAnArpMffMultiGatewayMffVid": zxAnArpMffMultiGatewayMffVid,
       "zxAnArpMffMultiGatewayIpAddr": zxAnArpMffMultiGatewayIpAddr,
       "zxAnArpMffMultiGatewayIpMask": zxAnArpMffMultiGatewayIpMask,
       "zxAnArpMffMultiGatewayMacMode": zxAnArpMffMultiGatewayMacMode,
       "zxAnArpMffMultiGatewayMac": zxAnArpMffMultiGatewayMac,
       "zxAnArpMffMultiGatewayRowStatus": zxAnArpMffMultiGatewayRowStatus,
       "zxAnArpAntiSpoofingCfgTable": zxAnArpAntiSpoofingCfgTable,
       "zxAnArpAntiSpoofingCfgEntry": zxAnArpAntiSpoofingCfgEntry,
       "zxAnArpAntiSpoofingVid": zxAnArpAntiSpoofingVid,
       "zxAnArpAntiSpoofingDirection": zxAnArpAntiSpoofingDirection,
       "zxAnArpAntiSpoofingVlanRowStatus": zxAnArpAntiSpoofingVlanRowStatus,
       "zxAnArpGateway": zxAnArpGateway,
       "zxAnArpGatewayTable": zxAnArpGatewayTable,
       "zxAnArpGatewayEntry": zxAnArpGatewayEntry,
       "zxAnArpGatewayVlan": zxAnArpGatewayVlan,
       "zxAnArpGatewayMode": zxAnArpGatewayMode,
       "zxAnArpGatewayIp": zxAnArpGatewayIp,
       "zxAnArpGatewayMacAddr": zxAnArpGatewayMacAddr,
       "zxAnArpGatewayRowStatus": zxAnArpGatewayRowStatus,
       "zxAnArpDaiObjects": zxAnArpDaiObjects,
       "zxAnArpDaiIfCfgTable": zxAnArpDaiIfCfgTable,
       "zxAnArpDaiIfCfgEntry": zxAnArpDaiIfCfgEntry,
       "zxAnArpRack": zxAnArpRack,
       "zxAnArpShelf": zxAnArpShelf,
       "zxAnArpSlot": zxAnArpSlot,
       "zxAnArpPort": zxAnArpPort,
       "zxAnArpOnu": zxAnArpOnu,
       "zxAnArpIfType": zxAnArpIfType,
       "zxAnArpLogicalId": zxAnArpLogicalId,
       "zxAnArpAntiSpoofingIfLogEnable": zxAnArpAntiSpoofingIfLogEnable,
       "zxAnArpReplyAgentObjects": zxAnArpReplyAgentObjects,
       "zxAnArpReplyAgentIfCfgTable": zxAnArpReplyAgentIfCfgTable,
       "zxAnArpReplyAgentIfCfgEntry": zxAnArpReplyAgentIfCfgEntry,
       "zxAnArpReplyAgentIfEnable": zxAnArpReplyAgentIfEnable,
       "zxAnArpPacketLimitObjects": zxAnArpPacketLimitObjects,
       "zxAnArpPacketLimitIfCfgTable": zxAnArpPacketLimitIfCfgTable,
       "zxAnArpPacketLimitIfCfgEntry": zxAnArpPacketLimitIfCfgEntry,
       "zxAnArpBcastSuppressIfEnable": zxAnArpBcastSuppressIfEnable,
       "zxAnArpAgentObjects": zxAnArpAgentObjects,
       "zxAnArpAgentGatewayTable": zxAnArpAgentGatewayTable,
       "zxAnArpAgentGatewayEntry": zxAnArpAgentGatewayEntry,
       "zxAnArpAgentGatewaySvid": zxAnArpAgentGatewaySvid,
       "zxAnArpAgentGatewayCvid": zxAnArpAgentGatewayCvid,
       "zxAnArpAgentGatewayStatus": zxAnArpAgentGatewayStatus,
       "zxAnArpAgentGatewayIpAddr": zxAnArpAgentGatewayIpAddr,
       "zxAnArpAgentGatewayMac": zxAnArpAgentGatewayMac,
       "zxAnArpAgentGatewayRowStatus": zxAnArpAgentGatewayRowStatus,
       "zxAnArpFilterObjects": zxAnArpFilterObjects,
       "zxAnArpFilterVlanConfTable": zxAnArpFilterVlanConfTable,
       "zxAnArpFilterVlanConfEntry": zxAnArpFilterVlanConfEntry,
       "zxAnArpFilterVlanConfVid": zxAnArpFilterVlanConfVid,
       "zxAnArpFilterVlanConfRowStatus": zxAnArpFilterVlanConfRowStatus}
)
