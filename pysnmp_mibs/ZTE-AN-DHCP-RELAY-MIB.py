# SNMP MIB module (ZTE-AN-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:35 2025
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

zxAnDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnDhcpRelayMIBNotifs_ObjectIdentity = ObjectIdentity
zxAnDhcpRelayMIBNotifs = _ZxAnDhcpRelayMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 0)
)
_ZxAnDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
zxAnDhcpRelayMIBObjects = _ZxAnDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1)
)
_ZxAnDrGlobal_ObjectIdentity = ObjectIdentity
zxAnDrGlobal = _ZxAnDrGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1)
)


class _ZxAnDrDatabaseOper_Type(Integer32):
    """Custom type zxAnDrDatabaseOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_ZxAnDrDatabaseOper_Type.__name__ = "Integer32"
_ZxAnDrDatabaseOper_Object = MibScalar
zxAnDrDatabaseOper = _ZxAnDrDatabaseOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 1),
    _ZxAnDrDatabaseOper_Type()
)
zxAnDrDatabaseOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrDatabaseOper.setStatus("current")


class _ZxAnDrServMaxRetryTimes_Type(Integer32):
    """Custom type zxAnDrServMaxRetryTimes based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_ZxAnDrServMaxRetryTimes_Type.__name__ = "Integer32"
_ZxAnDrServMaxRetryTimes_Object = MibScalar
zxAnDrServMaxRetryTimes = _ZxAnDrServMaxRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 2),
    _ZxAnDrServMaxRetryTimes_Type()
)
zxAnDrServMaxRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrServMaxRetryTimes.setStatus("current")


class _ZxAnDrUpdateArp_Type(Integer32):
    """Custom type zxAnDrUpdateArp based on Integer32"""
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


_ZxAnDrUpdateArp_Type.__name__ = "Integer32"
_ZxAnDrUpdateArp_Object = MibScalar
zxAnDrUpdateArp = _ZxAnDrUpdateArp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 3),
    _ZxAnDrUpdateArp_Type()
)
zxAnDrUpdateArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrUpdateArp.setStatus("current")


class _ZxAnDrProxyLeaseTime_Type(Integer32):
    """Custom type zxAnDrProxyLeaseTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_ZxAnDrProxyLeaseTime_Type.__name__ = "Integer32"
_ZxAnDrProxyLeaseTime_Object = MibScalar
zxAnDrProxyLeaseTime = _ZxAnDrProxyLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 4),
    _ZxAnDrProxyLeaseTime_Type()
)
zxAnDrProxyLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrProxyLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDrProxyLeaseTime.setUnits("seconds")


class _ZxAnDrForwardMode_Type(Integer32):
    """Custom type zxAnDrForwardMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allSimultaneously", 1),
          ("roundRobin", 2))
    )


_ZxAnDrForwardMode_Type.__name__ = "Integer32"
_ZxAnDrForwardMode_Object = MibScalar
zxAnDrForwardMode = _ZxAnDrForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 5),
    _ZxAnDrForwardMode_Type()
)
zxAnDrForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrForwardMode.setStatus("current")


class _ZxAnDrCos_Type(Integer32):
    """Custom type zxAnDrCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnDrCos_Type.__name__ = "Integer32"
_ZxAnDrCos_Object = MibScalar
zxAnDrCos = _ZxAnDrCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 1, 6),
    _ZxAnDrCos_Type()
)
zxAnDrCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrCos.setStatus("current")
_ZxAnDrOption60_ObjectIdentity = ObjectIdentity
zxAnDrOption60 = _ZxAnDrOption60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2)
)
_ZxAnDrOption60Table_Object = MibTable
zxAnDrOption60Table = _ZxAnDrOption60Table_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnDrOption60Table.setStatus("current")
_ZxAnDrOption60Entry_Object = MibTableRow
zxAnDrOption60Entry = _ZxAnDrOption60Entry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1, 1)
)
zxAnDrOption60Entry.setIndexNames(
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrOption60Str"),
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrOption60Srv"),
)
if mibBuilder.loadTexts:
    zxAnDrOption60Entry.setStatus("current")


class _ZxAnDrOption60Str_Type(DisplayString):
    """Custom type zxAnDrOption60Str based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ZxAnDrOption60Str_Type.__name__ = "DisplayString"
_ZxAnDrOption60Str_Object = MibTableColumn
zxAnDrOption60Str = _ZxAnDrOption60Str_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1, 1, 1),
    _ZxAnDrOption60Str_Type()
)
zxAnDrOption60Str.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDrOption60Str.setStatus("current")
_ZxAnDrOption60Srv_Type = IpAddress
_ZxAnDrOption60Srv_Object = MibTableColumn
zxAnDrOption60Srv = _ZxAnDrOption60Srv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1, 1, 2),
    _ZxAnDrOption60Srv_Type()
)
zxAnDrOption60Srv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDrOption60Srv.setStatus("current")


class _ZxAnDrOption60Frd_Type(Integer32):
    """Custom type zxAnDrOption60Frd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smart", 0),
          ("standard", 1),
          ("security", 2))
    )


_ZxAnDrOption60Frd_Type.__name__ = "Integer32"
_ZxAnDrOption60Frd_Object = MibTableColumn
zxAnDrOption60Frd = _ZxAnDrOption60Frd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1, 1, 3),
    _ZxAnDrOption60Frd_Type()
)
zxAnDrOption60Frd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDrOption60Frd.setStatus("current")
_ZxAnDrOption60Row_Type = RowStatus
_ZxAnDrOption60Row_Object = MibTableColumn
zxAnDrOption60Row = _ZxAnDrOption60Row_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 2, 1, 1, 4),
    _ZxAnDrOption60Row_Type()
)
zxAnDrOption60Row.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDrOption60Row.setStatus("current")
_ZxAnDrVlanInterface_ObjectIdentity = ObjectIdentity
zxAnDrVlanInterface = _ZxAnDrVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3)
)
_ZxAnDrVlanIntTable_Object = MibTable
zxAnDrVlanIntTable = _ZxAnDrVlanIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnDrVlanIntTable.setStatus("current")
_ZxAnDrVlanIntEntry_Object = MibTableRow
zxAnDrVlanIntEntry = _ZxAnDrVlanIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 1, 1)
)
zxAnDrVlanIntEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrIntIndex"),
)
if mibBuilder.loadTexts:
    zxAnDrVlanIntEntry.setStatus("current")
_ZxAnDrIntIndex_Type = ZxAnIfindex
_ZxAnDrIntIndex_Object = MibTableColumn
zxAnDrIntIndex = _ZxAnDrIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 1, 1, 1),
    _ZxAnDrIntIndex_Type()
)
zxAnDrIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDrIntIndex.setStatus("current")


class _ZxAnDrOption60Oper_Type(Integer32):
    """Custom type zxAnDrOption60Oper based on Integer32"""
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


_ZxAnDrOption60Oper_Type.__name__ = "Integer32"
_ZxAnDrOption60Oper_Object = MibTableColumn
zxAnDrOption60Oper = _ZxAnDrOption60Oper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 1, 1, 2),
    _ZxAnDrOption60Oper_Type()
)
zxAnDrOption60Oper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrOption60Oper.setStatus("current")
_ZxAnDrAgentIp_Type = IpAddress
_ZxAnDrAgentIp_Object = MibTableColumn
zxAnDrAgentIp = _ZxAnDrAgentIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 1, 1, 3),
    _ZxAnDrAgentIp_Type()
)
zxAnDrAgentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDrAgentIp.setStatus("current")
_ZxAnDrVlanIntServTable_Object = MibTable
zxAnDrVlanIntServTable = _ZxAnDrVlanIntServTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnDrVlanIntServTable.setStatus("current")
_ZxAnDrVlanIntServEntry_Object = MibTableRow
zxAnDrVlanIntServEntry = _ZxAnDrVlanIntServEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 2, 1)
)
zxAnDrVlanIntServEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrIntIndex"),
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrVlanIntServIp"),
)
if mibBuilder.loadTexts:
    zxAnDrVlanIntServEntry.setStatus("current")
_ZxAnDrVlanIntServIp_Type = IpAddress
_ZxAnDrVlanIntServIp_Object = MibTableColumn
zxAnDrVlanIntServIp = _ZxAnDrVlanIntServIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 2, 1, 1),
    _ZxAnDrVlanIntServIp_Type()
)
zxAnDrVlanIntServIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDrVlanIntServIp.setStatus("current")


class _ZxAnDrVlanIntServFrd_Type(Integer32):
    """Custom type zxAnDrVlanIntServFrd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smart", 0),
          ("standard", 1),
          ("security", 2))
    )


_ZxAnDrVlanIntServFrd_Type.__name__ = "Integer32"
_ZxAnDrVlanIntServFrd_Object = MibTableColumn
zxAnDrVlanIntServFrd = _ZxAnDrVlanIntServFrd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 2, 1, 2),
    _ZxAnDrVlanIntServFrd_Type()
)
zxAnDrVlanIntServFrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDrVlanIntServFrd.setStatus("current")
_ZxAnDrVlanIntServRow_Type = RowStatus
_ZxAnDrVlanIntServRow_Object = MibTableColumn
zxAnDrVlanIntServRow = _ZxAnDrVlanIntServRow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 3, 2, 1, 3),
    _ZxAnDrVlanIntServRow_Type()
)
zxAnDrVlanIntServRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDrVlanIntServRow.setStatus("current")
_ZxAnDrShowUsers_ObjectIdentity = ObjectIdentity
zxAnDrShowUsers = _ZxAnDrShowUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4)
)
_ZxAnDrUserViewTable_Object = MibTable
zxAnDrUserViewTable = _ZxAnDrUserViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnDrUserViewTable.setStatus("current")
_ZxAnDrUserViewEntry_Object = MibTableRow
zxAnDrUserViewEntry = _ZxAnDrUserViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1, 1)
)
zxAnDrUserViewEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrIntIndex"),
    (0, "ZTE-AN-DHCP-RELAY-MIB", "zxAnDrUserViewMac"),
)
if mibBuilder.loadTexts:
    zxAnDrUserViewEntry.setStatus("current")
_ZxAnDrUserViewMac_Type = MacAddress
_ZxAnDrUserViewMac_Object = MibTableColumn
zxAnDrUserViewMac = _ZxAnDrUserViewMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1, 1, 1),
    _ZxAnDrUserViewMac_Type()
)
zxAnDrUserViewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDrUserViewMac.setStatus("current")
_ZxAnDrUserViewIp_Type = IpAddress
_ZxAnDrUserViewIp_Object = MibTableColumn
zxAnDrUserViewIp = _ZxAnDrUserViewIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1, 1, 2),
    _ZxAnDrUserViewIp_Type()
)
zxAnDrUserViewIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDrUserViewIp.setStatus("current")


class _ZxAnDrUserViewState_Type(DisplayString):
    """Custom type zxAnDrUserViewState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ZxAnDrUserViewState_Type.__name__ = "DisplayString"
_ZxAnDrUserViewState_Object = MibTableColumn
zxAnDrUserViewState = _ZxAnDrUserViewState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1, 1, 3),
    _ZxAnDrUserViewState_Type()
)
zxAnDrUserViewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDrUserViewState.setStatus("current")


class _ZxAnDrUserViewTime_Type(DisplayString):
    """Custom type zxAnDrUserViewTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ZxAnDrUserViewTime_Type.__name__ = "DisplayString"
_ZxAnDrUserViewTime_Object = MibTableColumn
zxAnDrUserViewTime = _ZxAnDrUserViewTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 53, 1, 4, 1, 1, 4),
    _ZxAnDrUserViewTime_Type()
)
zxAnDrUserViewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDrUserViewTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DHCP-RELAY-MIB",
    **{"zxAnDhcpRelayMIB": zxAnDhcpRelayMIB,
       "zxAnDhcpRelayMIBNotifs": zxAnDhcpRelayMIBNotifs,
       "zxAnDhcpRelayMIBObjects": zxAnDhcpRelayMIBObjects,
       "zxAnDrGlobal": zxAnDrGlobal,
       "zxAnDrDatabaseOper": zxAnDrDatabaseOper,
       "zxAnDrServMaxRetryTimes": zxAnDrServMaxRetryTimes,
       "zxAnDrUpdateArp": zxAnDrUpdateArp,
       "zxAnDrProxyLeaseTime": zxAnDrProxyLeaseTime,
       "zxAnDrForwardMode": zxAnDrForwardMode,
       "zxAnDrCos": zxAnDrCos,
       "zxAnDrOption60": zxAnDrOption60,
       "zxAnDrOption60Table": zxAnDrOption60Table,
       "zxAnDrOption60Entry": zxAnDrOption60Entry,
       "zxAnDrOption60Str": zxAnDrOption60Str,
       "zxAnDrOption60Srv": zxAnDrOption60Srv,
       "zxAnDrOption60Frd": zxAnDrOption60Frd,
       "zxAnDrOption60Row": zxAnDrOption60Row,
       "zxAnDrVlanInterface": zxAnDrVlanInterface,
       "zxAnDrVlanIntTable": zxAnDrVlanIntTable,
       "zxAnDrVlanIntEntry": zxAnDrVlanIntEntry,
       "zxAnDrIntIndex": zxAnDrIntIndex,
       "zxAnDrOption60Oper": zxAnDrOption60Oper,
       "zxAnDrAgentIp": zxAnDrAgentIp,
       "zxAnDrVlanIntServTable": zxAnDrVlanIntServTable,
       "zxAnDrVlanIntServEntry": zxAnDrVlanIntServEntry,
       "zxAnDrVlanIntServIp": zxAnDrVlanIntServIp,
       "zxAnDrVlanIntServFrd": zxAnDrVlanIntServFrd,
       "zxAnDrVlanIntServRow": zxAnDrVlanIntServRow,
       "zxAnDrShowUsers": zxAnDrShowUsers,
       "zxAnDrUserViewTable": zxAnDrUserViewTable,
       "zxAnDrUserViewEntry": zxAnDrUserViewEntry,
       "zxAnDrUserViewMac": zxAnDrUserViewMac,
       "zxAnDrUserViewIp": zxAnDrUserViewIp,
       "zxAnDrUserViewState": zxAnDrUserViewState,
       "zxAnDrUserViewTime": zxAnDrUserViewTime}
)
