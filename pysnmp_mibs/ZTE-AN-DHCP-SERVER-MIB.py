# SNMP MIB module (ZTE-AN-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:31 2025
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

zxAnDhcpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54)
)
if mibBuilder.loadTexts:
    zxAnDhcpServerMIB.setRevisions(
        ("2006-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnDhcpServerMIBNotifs_ObjectIdentity = ObjectIdentity
zxAnDhcpServerMIBNotifs = _ZxAnDhcpServerMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 0)
)
_ZxAnDhcpServerMIBObjects_ObjectIdentity = ObjectIdentity
zxAnDhcpServerMIBObjects = _ZxAnDhcpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1)
)
_ZxAnDvGlobal_ObjectIdentity = ObjectIdentity
zxAnDvGlobal = _ZxAnDvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 1)
)
_ZxAnDvPrimaryDns_Type = IpAddress
_ZxAnDvPrimaryDns_Object = MibScalar
zxAnDvPrimaryDns = _ZxAnDvPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 1, 1),
    _ZxAnDvPrimaryDns_Type()
)
zxAnDvPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDvPrimaryDns.setStatus("current")
_ZxAnDvSecondDns_Type = IpAddress
_ZxAnDvSecondDns_Object = MibScalar
zxAnDvSecondDns = _ZxAnDvSecondDns_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 1, 2),
    _ZxAnDvSecondDns_Type()
)
zxAnDvSecondDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDvSecondDns.setStatus("current")


class _ZxAnDvLeaseTime_Type(Integer32):
    """Custom type zxAnDvLeaseTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_ZxAnDvLeaseTime_Type.__name__ = "Integer32"
_ZxAnDvLeaseTime_Object = MibScalar
zxAnDvLeaseTime = _ZxAnDvLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 1, 3),
    _ZxAnDvLeaseTime_Type()
)
zxAnDvLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDvLeaseTime.setStatus("current")


class _ZxAnDvUpdateArp_Type(Integer32):
    """Custom type zxAnDvUpdateArp based on Integer32"""
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


_ZxAnDvUpdateArp_Type.__name__ = "Integer32"
_ZxAnDvUpdateArp_Object = MibScalar
zxAnDvUpdateArp = _ZxAnDvUpdateArp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 1, 4),
    _ZxAnDvUpdateArp_Type()
)
zxAnDvUpdateArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDvUpdateArp.setStatus("current")
_ZxAnDvIpPool_ObjectIdentity = ObjectIdentity
zxAnDvIpPool = _ZxAnDvIpPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2)
)
_ZxAnDvIpPoolTable_Object = MibTable
zxAnDvIpPoolTable = _ZxAnDvIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnDvIpPoolTable.setStatus("current")
_ZxAnDvIpPoolEntry_Object = MibTableRow
zxAnDvIpPoolEntry = _ZxAnDvIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1)
)
zxAnDvIpPoolEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvIpPoolName"),
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvBeginIp"),
)
if mibBuilder.loadTexts:
    zxAnDvIpPoolEntry.setStatus("current")


class _ZxAnDvIpPoolName_Type(DisplayString):
    """Custom type zxAnDvIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnDvIpPoolName_Type.__name__ = "DisplayString"
_ZxAnDvIpPoolName_Object = MibTableColumn
zxAnDvIpPoolName = _ZxAnDvIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1, 1),
    _ZxAnDvIpPoolName_Type()
)
zxAnDvIpPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDvIpPoolName.setStatus("current")
_ZxAnDvBeginIp_Type = IpAddress
_ZxAnDvBeginIp_Object = MibTableColumn
zxAnDvBeginIp = _ZxAnDvBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1, 2),
    _ZxAnDvBeginIp_Type()
)
zxAnDvBeginIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDvBeginIp.setStatus("current")
_ZxAnDvEndIp_Type = IpAddress
_ZxAnDvEndIp_Object = MibTableColumn
zxAnDvEndIp = _ZxAnDvEndIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1, 3),
    _ZxAnDvEndIp_Type()
)
zxAnDvEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDvEndIp.setStatus("current")
_ZxAnDvMask_Type = IpAddress
_ZxAnDvMask_Object = MibTableColumn
zxAnDvMask = _ZxAnDvMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1, 4),
    _ZxAnDvMask_Type()
)
zxAnDvMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDvMask.setStatus("current")
_ZxAnDvRow_Type = RowStatus
_ZxAnDvRow_Object = MibTableColumn
zxAnDvRow = _ZxAnDvRow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 2, 1, 1, 5),
    _ZxAnDvRow_Type()
)
zxAnDvRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDvRow.setStatus("current")
_ZxAnDvVlanInterface_ObjectIdentity = ObjectIdentity
zxAnDvVlanInterface = _ZxAnDvVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3)
)
_ZxAnDvVlanIntTable_Object = MibTable
zxAnDvVlanIntTable = _ZxAnDvVlanIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnDvVlanIntTable.setStatus("current")
_ZxAnDvVlanIntEntry_Object = MibTableRow
zxAnDvVlanIntEntry = _ZxAnDvVlanIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 1, 1)
)
zxAnDvVlanIntEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvIntIndex"),
)
if mibBuilder.loadTexts:
    zxAnDvVlanIntEntry.setStatus("current")
_ZxAnDvIntIndex_Type = ZxAnIfindex
_ZxAnDvIntIndex_Object = MibTableColumn
zxAnDvIntIndex = _ZxAnDvIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 1, 1, 1),
    _ZxAnDvIntIndex_Type()
)
zxAnDvIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDvIntIndex.setStatus("current")


class _ZxAnDvIntIpPoolName_Type(DisplayString):
    """Custom type zxAnDvIntIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnDvIntIpPoolName_Type.__name__ = "DisplayString"
_ZxAnDvIntIpPoolName_Object = MibTableColumn
zxAnDvIntIpPoolName = _ZxAnDvIntIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 1, 1, 2),
    _ZxAnDvIntIpPoolName_Type()
)
zxAnDvIntIpPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDvIntIpPoolName.setStatus("current")
_ZxAnDvVlanIntGateWayTable_Object = MibTable
zxAnDvVlanIntGateWayTable = _ZxAnDvVlanIntGateWayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnDvVlanIntGateWayTable.setStatus("current")
_ZxAnDvVlanIntGateWayEntry_Object = MibTableRow
zxAnDvVlanIntGateWayEntry = _ZxAnDvVlanIntGateWayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 2, 1)
)
zxAnDvVlanIntGateWayEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvIntIndex"),
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvGateway"),
)
if mibBuilder.loadTexts:
    zxAnDvVlanIntGateWayEntry.setStatus("current")
_ZxAnDvGateway_Type = IpAddress
_ZxAnDvGateway_Object = MibTableColumn
zxAnDvGateway = _ZxAnDvGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 2, 1, 1),
    _ZxAnDvGateway_Type()
)
zxAnDvGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDvGateway.setStatus("current")
_ZxAnDvGatewayRow_Type = RowStatus
_ZxAnDvGatewayRow_Object = MibTableColumn
zxAnDvGatewayRow = _ZxAnDvGatewayRow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 3, 2, 1, 2),
    _ZxAnDvGatewayRow_Type()
)
zxAnDvGatewayRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDvGatewayRow.setStatus("current")
_ZxAnDvShowUsers_ObjectIdentity = ObjectIdentity
zxAnDvShowUsers = _ZxAnDvShowUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4)
)
_ZxAnDvUserViewTable_Object = MibTable
zxAnDvUserViewTable = _ZxAnDvUserViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnDvUserViewTable.setStatus("current")
_ZxAnDvUserViewEntry_Object = MibTableRow
zxAnDvUserViewEntry = _ZxAnDvUserViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1, 1)
)
zxAnDvUserViewEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvIntIndex"),
    (0, "ZTE-AN-DHCP-SERVER-MIB", "zxAnDvUserViewMac"),
)
if mibBuilder.loadTexts:
    zxAnDvUserViewEntry.setStatus("current")
_ZxAnDvUserViewMac_Type = MacAddress
_ZxAnDvUserViewMac_Object = MibTableColumn
zxAnDvUserViewMac = _ZxAnDvUserViewMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1, 1, 1),
    _ZxAnDvUserViewMac_Type()
)
zxAnDvUserViewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDvUserViewMac.setStatus("current")
_ZxAnDvUserViewIp_Type = IpAddress
_ZxAnDvUserViewIp_Object = MibTableColumn
zxAnDvUserViewIp = _ZxAnDvUserViewIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1, 1, 2),
    _ZxAnDvUserViewIp_Type()
)
zxAnDvUserViewIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDvUserViewIp.setStatus("current")


class _ZxAnDvUserViewState_Type(DisplayString):
    """Custom type zxAnDvUserViewState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ZxAnDvUserViewState_Type.__name__ = "DisplayString"
_ZxAnDvUserViewState_Object = MibTableColumn
zxAnDvUserViewState = _ZxAnDvUserViewState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1, 1, 3),
    _ZxAnDvUserViewState_Type()
)
zxAnDvUserViewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDvUserViewState.setStatus("current")


class _ZxAnDvUserViewTime_Type(DisplayString):
    """Custom type zxAnDvUserViewTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ZxAnDvUserViewTime_Type.__name__ = "DisplayString"
_ZxAnDvUserViewTime_Object = MibTableColumn
zxAnDvUserViewTime = _ZxAnDvUserViewTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 54, 1, 4, 1, 1, 4),
    _ZxAnDvUserViewTime_Type()
)
zxAnDvUserViewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDvUserViewTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DHCP-SERVER-MIB",
    **{"zxAnDhcpServerMIB": zxAnDhcpServerMIB,
       "zxAnDhcpServerMIBNotifs": zxAnDhcpServerMIBNotifs,
       "zxAnDhcpServerMIBObjects": zxAnDhcpServerMIBObjects,
       "zxAnDvGlobal": zxAnDvGlobal,
       "zxAnDvPrimaryDns": zxAnDvPrimaryDns,
       "zxAnDvSecondDns": zxAnDvSecondDns,
       "zxAnDvLeaseTime": zxAnDvLeaseTime,
       "zxAnDvUpdateArp": zxAnDvUpdateArp,
       "zxAnDvIpPool": zxAnDvIpPool,
       "zxAnDvIpPoolTable": zxAnDvIpPoolTable,
       "zxAnDvIpPoolEntry": zxAnDvIpPoolEntry,
       "zxAnDvIpPoolName": zxAnDvIpPoolName,
       "zxAnDvBeginIp": zxAnDvBeginIp,
       "zxAnDvEndIp": zxAnDvEndIp,
       "zxAnDvMask": zxAnDvMask,
       "zxAnDvRow": zxAnDvRow,
       "zxAnDvVlanInterface": zxAnDvVlanInterface,
       "zxAnDvVlanIntTable": zxAnDvVlanIntTable,
       "zxAnDvVlanIntEntry": zxAnDvVlanIntEntry,
       "zxAnDvIntIndex": zxAnDvIntIndex,
       "zxAnDvIntIpPoolName": zxAnDvIntIpPoolName,
       "zxAnDvVlanIntGateWayTable": zxAnDvVlanIntGateWayTable,
       "zxAnDvVlanIntGateWayEntry": zxAnDvVlanIntGateWayEntry,
       "zxAnDvGateway": zxAnDvGateway,
       "zxAnDvGatewayRow": zxAnDvGatewayRow,
       "zxAnDvShowUsers": zxAnDvShowUsers,
       "zxAnDvUserViewTable": zxAnDvUserViewTable,
       "zxAnDvUserViewEntry": zxAnDvUserViewEntry,
       "zxAnDvUserViewMac": zxAnDvUserViewMac,
       "zxAnDvUserViewIp": zxAnDvUserViewIp,
       "zxAnDvUserViewState": zxAnDvUserViewState,
       "zxAnDvUserViewTime": zxAnDvUserViewTime}
)
