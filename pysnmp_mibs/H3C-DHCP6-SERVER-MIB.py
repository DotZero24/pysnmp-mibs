# SNMP MIB module (H3C-DHCP6-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DHCP6-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:46 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cDHCP6Server = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159)
)
if mibBuilder.loadTexts:
    h3cDHCP6Server.setRevisions(
        ("2014-10-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDHCP6ServerTables_ObjectIdentity = ObjectIdentity
h3cDHCP6ServerTables = _H3cDHCP6ServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1)
)
_H3cDHCPS6PoolTable_Object = MibTable
h3cDHCPS6PoolTable = _H3cDHCPS6PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolTable.setStatus("current")
_H3cDHCPS6PoolEntry_Object = MibTableRow
h3cDHCPS6PoolEntry = _H3cDHCPS6PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 1, 1)
)
h3cDHCPS6PoolEntry.setIndexNames(
    (0, "H3C-DHCP6-SERVER-MIB", "h3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolEntry.setStatus("current")


class _H3cDHCPS6PoolName_Type(OctetString):
    """Custom type h3cDHCPS6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_H3cDHCPS6PoolName_Type.__name__ = "OctetString"
_H3cDHCPS6PoolName_Object = MibTableColumn
h3cDHCPS6PoolName = _H3cDHCPS6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 1, 1, 1),
    _H3cDHCPS6PoolName_Type()
)
h3cDHCPS6PoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolName.setStatus("current")
_H3cDHCPS6PoolRowStatus_Type = RowStatus
_H3cDHCPS6PoolRowStatus_Object = MibTableColumn
h3cDHCPS6PoolRowStatus = _H3cDHCPS6PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 1, 1, 2),
    _H3cDHCPS6PoolRowStatus_Type()
)
h3cDHCPS6PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolRowStatus.setStatus("current")
_H3cDHCPS6PoolConfigTable_Object = MibTable
h3cDHCPS6PoolConfigTable = _H3cDHCPS6PoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolConfigTable.setStatus("current")
_H3cDHCPS6PoolConfigEntry_Object = MibTableRow
h3cDHCPS6PoolConfigEntry = _H3cDHCPS6PoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 2, 1)
)
h3cDHCPS6PoolConfigEntry.setIndexNames(
    (0, "H3C-DHCP6-SERVER-MIB", "h3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolConfigEntry.setStatus("current")
_H3cDHCPS6PoolPrimaryDNSIP_Type = InetAddressIPv6
_H3cDHCPS6PoolPrimaryDNSIP_Object = MibTableColumn
h3cDHCPS6PoolPrimaryDNSIP = _H3cDHCPS6PoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 2, 1, 1),
    _H3cDHCPS6PoolPrimaryDNSIP_Type()
)
h3cDHCPS6PoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolPrimaryDNSIP.setStatus("current")
_H3cDHCPS6PoolSecondDNSIP_Type = InetAddressIPv6
_H3cDHCPS6PoolSecondDNSIP_Object = MibTableColumn
h3cDHCPS6PoolSecondDNSIP = _H3cDHCPS6PoolSecondDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 2, 1, 2),
    _H3cDHCPS6PoolSecondDNSIP_Type()
)
h3cDHCPS6PoolSecondDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolSecondDNSIP.setStatus("current")
_H3cDHCPS6PoolNetworkTable_Object = MibTable
h3cDHCPS6PoolNetworkTable = _H3cDHCPS6PoolNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolNetworkTable.setStatus("current")
_H3cDHCPS6PoolNetworkEntry_Object = MibTableRow
h3cDHCPS6PoolNetworkEntry = _H3cDHCPS6PoolNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3, 1)
)
h3cDHCPS6PoolNetworkEntry.setIndexNames(
    (0, "H3C-DHCP6-SERVER-MIB", "h3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolNetworkEntry.setStatus("current")
_H3cDHCPS6PoolStartAddr_Type = InetAddressIPv6
_H3cDHCPS6PoolStartAddr_Object = MibTableColumn
h3cDHCPS6PoolStartAddr = _H3cDHCPS6PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3, 1, 1),
    _H3cDHCPS6PoolStartAddr_Type()
)
h3cDHCPS6PoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolStartAddr.setStatus("current")
_H3cDHCPS6PoolStopAddr_Type = InetAddressIPv6
_H3cDHCPS6PoolStopAddr_Object = MibTableColumn
h3cDHCPS6PoolStopAddr = _H3cDHCPS6PoolStopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3, 1, 2),
    _H3cDHCPS6PoolStopAddr_Type()
)
h3cDHCPS6PoolStopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolStopAddr.setStatus("current")


class _H3cDHCPS6PoolNetPrefixLen_Type(Integer32):
    """Custom type h3cDHCPS6PoolNetPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_H3cDHCPS6PoolNetPrefixLen_Type.__name__ = "Integer32"
_H3cDHCPS6PoolNetPrefixLen_Object = MibTableColumn
h3cDHCPS6PoolNetPrefixLen = _H3cDHCPS6PoolNetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3, 1, 3),
    _H3cDHCPS6PoolNetPrefixLen_Type()
)
h3cDHCPS6PoolNetPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolNetPrefixLen.setStatus("current")
_H3cDHCPS6PoolLeaseTime_Type = TimeTicks
_H3cDHCPS6PoolLeaseTime_Object = MibTableColumn
h3cDHCPS6PoolLeaseTime = _H3cDHCPS6PoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 3, 1, 4),
    _H3cDHCPS6PoolLeaseTime_Type()
)
h3cDHCPS6PoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolLeaseTime.setStatus("current")
_H3cDHCPS6PoolStatTable_Object = MibTable
h3cDHCPS6PoolStatTable = _H3cDHCPS6PoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolStatTable.setStatus("current")
_H3cDHCPS6PoolStatEntry_Object = MibTableRow
h3cDHCPS6PoolStatEntry = _H3cDHCPS6PoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 4, 1)
)
h3cDHCPS6PoolStatEntry.setIndexNames(
    (0, "H3C-DHCP6-SERVER-MIB", "h3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPS6PoolStatEntry.setStatus("current")
_H3cDHCPS6PoolIPPoolUsage_Type = Integer32
_H3cDHCPS6PoolIPPoolUsage_Object = MibTableColumn
h3cDHCPS6PoolIPPoolUsage = _H3cDHCPS6PoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 159, 1, 4, 1, 1),
    _H3cDHCPS6PoolIPPoolUsage_Type()
)
h3cDHCPS6PoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPS6PoolIPPoolUsage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DHCP6-SERVER-MIB",
    **{"h3cDHCP6Server": h3cDHCP6Server,
       "h3cDHCP6ServerTables": h3cDHCP6ServerTables,
       "h3cDHCPS6PoolTable": h3cDHCPS6PoolTable,
       "h3cDHCPS6PoolEntry": h3cDHCPS6PoolEntry,
       "h3cDHCPS6PoolName": h3cDHCPS6PoolName,
       "h3cDHCPS6PoolRowStatus": h3cDHCPS6PoolRowStatus,
       "h3cDHCPS6PoolConfigTable": h3cDHCPS6PoolConfigTable,
       "h3cDHCPS6PoolConfigEntry": h3cDHCPS6PoolConfigEntry,
       "h3cDHCPS6PoolPrimaryDNSIP": h3cDHCPS6PoolPrimaryDNSIP,
       "h3cDHCPS6PoolSecondDNSIP": h3cDHCPS6PoolSecondDNSIP,
       "h3cDHCPS6PoolNetworkTable": h3cDHCPS6PoolNetworkTable,
       "h3cDHCPS6PoolNetworkEntry": h3cDHCPS6PoolNetworkEntry,
       "h3cDHCPS6PoolStartAddr": h3cDHCPS6PoolStartAddr,
       "h3cDHCPS6PoolStopAddr": h3cDHCPS6PoolStopAddr,
       "h3cDHCPS6PoolNetPrefixLen": h3cDHCPS6PoolNetPrefixLen,
       "h3cDHCPS6PoolLeaseTime": h3cDHCPS6PoolLeaseTime,
       "h3cDHCPS6PoolStatTable": h3cDHCPS6PoolStatTable,
       "h3cDHCPS6PoolStatEntry": h3cDHCPS6PoolStatEntry,
       "h3cDHCPS6PoolIPPoolUsage": h3cDHCPS6PoolIPPoolUsage}
)
