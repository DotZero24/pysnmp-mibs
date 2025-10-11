# SNMP MIB module (RAISECOM-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-MCAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:08 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

raisecomMcast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27)
)
if mibBuilder.loadTexts:
    raisecomMcast.setRevisions(
        ("2010-10-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomMcastNotifications_ObjectIdentity = ObjectIdentity
raisecomMcastNotifications = _RaisecomMcastNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 1)
)
_RaisecomMcastObjects_ObjectIdentity = ObjectIdentity
raisecomMcastObjects = _RaisecomMcastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2)
)
_RaisecomMcastScalar_ObjectIdentity = ObjectIdentity
raisecomMcastScalar = _RaisecomMcastScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 1)
)


class _RaisecomMulticastFilterEnable_Type(EnableVar):
    """Custom type raisecomMulticastFilterEnable based on EnableVar"""
    defaultValue = 2


_RaisecomMulticastFilterEnable_Type.__name__ = "EnableVar"
_RaisecomMulticastFilterEnable_Object = MibScalar
raisecomMulticastFilterEnable = _RaisecomMulticastFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 1, 1),
    _RaisecomMulticastFilterEnable_Type()
)
raisecomMulticastFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMulticastFilterEnable.setStatus("current")
_RaisecomMulticastFilterVlanlist_Type = Vlanset
_RaisecomMulticastFilterVlanlist_Object = MibScalar
raisecomMulticastFilterVlanlist = _RaisecomMulticastFilterVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 1, 2),
    _RaisecomMulticastFilterVlanlist_Type()
)
raisecomMulticastFilterVlanlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMulticastFilterVlanlist.setStatus("current")
_RaisecomMcastL2_ObjectIdentity = ObjectIdentity
raisecomMcastL2 = _RaisecomMcastL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2)
)


class _RaisecomL2MulticastMaxGroupNum_Type(Integer32):
    """Custom type raisecomL2MulticastMaxGroupNum based on Integer32"""
    defaultValue = 0


_RaisecomL2MulticastMaxGroupNum_Type.__name__ = "Integer32"
_RaisecomL2MulticastMaxGroupNum_Object = MibScalar
raisecomL2MulticastMaxGroupNum = _RaisecomL2MulticastMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 1),
    _RaisecomL2MulticastMaxGroupNum_Type()
)
raisecomL2MulticastMaxGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomL2MulticastMaxGroupNum.setStatus("current")


class _RaisecomL2MulticastCurrentGroupNum_Type(Integer32):
    """Custom type raisecomL2MulticastCurrentGroupNum based on Integer32"""
    defaultValue = 0


_RaisecomL2MulticastCurrentGroupNum_Type.__name__ = "Integer32"
_RaisecomL2MulticastCurrentGroupNum_Object = MibScalar
raisecomL2MulticastCurrentGroupNum = _RaisecomL2MulticastCurrentGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 2),
    _RaisecomL2MulticastCurrentGroupNum_Type()
)
raisecomL2MulticastCurrentGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomL2MulticastCurrentGroupNum.setStatus("current")
_RaisecomL2MulticastAddressTable_Object = MibTable
raisecomL2MulticastAddressTable = _RaisecomL2MulticastAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomL2MulticastAddressTable.setStatus("current")
_RaisecomL2MulticastAddressEntry_Object = MibTableRow
raisecomL2MulticastAddressEntry = _RaisecomL2MulticastAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1)
)
raisecomL2MulticastAddressEntry.setIndexNames(
    (0, "RAISECOM-MCAST-MIB", "raisecomL2MulticastMVlan"),
    (0, "RAISECOM-MCAST-MIB", "raisecomL2MulticastAddress"),
)
if mibBuilder.loadTexts:
    raisecomL2MulticastAddressEntry.setStatus("current")
_RaisecomL2MulticastMVlan_Type = Integer32
_RaisecomL2MulticastMVlan_Object = MibTableColumn
raisecomL2MulticastMVlan = _RaisecomL2MulticastMVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1, 1),
    _RaisecomL2MulticastMVlan_Type()
)
raisecomL2MulticastMVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomL2MulticastMVlan.setStatus("current")
_RaisecomL2MulticastAddress_Type = MacAddress
_RaisecomL2MulticastAddress_Object = MibTableColumn
raisecomL2MulticastAddress = _RaisecomL2MulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1, 2),
    _RaisecomL2MulticastAddress_Type()
)
raisecomL2MulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomL2MulticastAddress.setStatus("current")
_RaisecomL2MulticastEgressPortlist_Type = PortList
_RaisecomL2MulticastEgressPortlist_Object = MibTableColumn
raisecomL2MulticastEgressPortlist = _RaisecomL2MulticastEgressPortlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1, 3),
    _RaisecomL2MulticastEgressPortlist_Type()
)
raisecomL2MulticastEgressPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomL2MulticastEgressPortlist.setStatus("current")
_RaisecomL2MulticastStaticPortlist_Type = PortList
_RaisecomL2MulticastStaticPortlist_Object = MibTableColumn
raisecomL2MulticastStaticPortlist = _RaisecomL2MulticastStaticPortlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1, 4),
    _RaisecomL2MulticastStaticPortlist_Type()
)
raisecomL2MulticastStaticPortlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomL2MulticastStaticPortlist.setStatus("current")
_RaisecomL2MulticastRowStatus_Type = RowStatus
_RaisecomL2MulticastRowStatus_Object = MibTableColumn
raisecomL2MulticastRowStatus = _RaisecomL2MulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 2, 3, 1, 5),
    _RaisecomL2MulticastRowStatus_Type()
)
raisecomL2MulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomL2MulticastRowStatus.setStatus("current")
_RaisecomMcastVlanCopy_ObjectIdentity = ObjectIdentity
raisecomMcastVlanCopy = _RaisecomMcastVlanCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3)
)


class _RaisecomIgmpVlanCopyMaxGroupNum_Type(Integer32):
    """Custom type raisecomIgmpVlanCopyMaxGroupNum based on Integer32"""
    defaultValue = 0


_RaisecomIgmpVlanCopyMaxGroupNum_Type.__name__ = "Integer32"
_RaisecomIgmpVlanCopyMaxGroupNum_Object = MibScalar
raisecomIgmpVlanCopyMaxGroupNum = _RaisecomIgmpVlanCopyMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 1),
    _RaisecomIgmpVlanCopyMaxGroupNum_Type()
)
raisecomIgmpVlanCopyMaxGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyMaxGroupNum.setStatus("current")


class _RaisecomIgmpVlanCopyCurrentGroupNum_Type(Integer32):
    """Custom type raisecomIgmpVlanCopyCurrentGroupNum based on Integer32"""
    defaultValue = 0


_RaisecomIgmpVlanCopyCurrentGroupNum_Type.__name__ = "Integer32"
_RaisecomIgmpVlanCopyCurrentGroupNum_Object = MibScalar
raisecomIgmpVlanCopyCurrentGroupNum = _RaisecomIgmpVlanCopyCurrentGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 2),
    _RaisecomIgmpVlanCopyCurrentGroupNum_Type()
)
raisecomIgmpVlanCopyCurrentGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyCurrentGroupNum.setStatus("current")
_RaisecomIgmpVlanCopyAddressTable_Object = MibTable
raisecomIgmpVlanCopyAddressTable = _RaisecomIgmpVlanCopyAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3)
)
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyAddressTable.setStatus("current")
_RaisecomIgmpVlanCopyAddressEntry_Object = MibTableRow
raisecomIgmpVlanCopyAddressEntry = _RaisecomIgmpVlanCopyAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1)
)
raisecomIgmpVlanCopyAddressEntry.setIndexNames(
    (0, "RAISECOM-MCAST-MIB", "raisecomIgmpVlanCopyMVlan"),
    (0, "RAISECOM-MCAST-MIB", "raisecomIgmpVlanCopyIpAddressType"),
    (0, "RAISECOM-MCAST-MIB", "raisecomIgmpVlanCopyIpAddress"),
    (0, "RAISECOM-MCAST-MIB", "raisecomIgmpVlanCopyEgressPort"),
)
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyAddressEntry.setStatus("current")
_RaisecomIgmpVlanCopyMVlan_Type = VlanIndex
_RaisecomIgmpVlanCopyMVlan_Object = MibTableColumn
raisecomIgmpVlanCopyMVlan = _RaisecomIgmpVlanCopyMVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 1),
    _RaisecomIgmpVlanCopyMVlan_Type()
)
raisecomIgmpVlanCopyMVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyMVlan.setStatus("current")
_RaisecomIgmpVlanCopyIpAddressType_Type = InetAddressType
_RaisecomIgmpVlanCopyIpAddressType_Object = MibTableColumn
raisecomIgmpVlanCopyIpAddressType = _RaisecomIgmpVlanCopyIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 2),
    _RaisecomIgmpVlanCopyIpAddressType_Type()
)
raisecomIgmpVlanCopyIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyIpAddressType.setStatus("current")


class _RaisecomIgmpVlanCopyIpAddress_Type(InetAddress):
    """Custom type raisecomIgmpVlanCopyIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RaisecomIgmpVlanCopyIpAddress_Type.__name__ = "InetAddress"
_RaisecomIgmpVlanCopyIpAddress_Object = MibTableColumn
raisecomIgmpVlanCopyIpAddress = _RaisecomIgmpVlanCopyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 3),
    _RaisecomIgmpVlanCopyIpAddress_Type()
)
raisecomIgmpVlanCopyIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyIpAddress.setStatus("current")
_RaisecomIgmpVlanCopyEgressPort_Type = Integer32
_RaisecomIgmpVlanCopyEgressPort_Object = MibTableColumn
raisecomIgmpVlanCopyEgressPort = _RaisecomIgmpVlanCopyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 4),
    _RaisecomIgmpVlanCopyEgressPort_Type()
)
raisecomIgmpVlanCopyEgressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyEgressPort.setStatus("current")
_RaisecomIgmpVlanCopyUVlanList_Type = Vlanset
_RaisecomIgmpVlanCopyUVlanList_Object = MibTableColumn
raisecomIgmpVlanCopyUVlanList = _RaisecomIgmpVlanCopyUVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 5),
    _RaisecomIgmpVlanCopyUVlanList_Type()
)
raisecomIgmpVlanCopyUVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyUVlanList.setStatus("current")
_RaisecomIgmpVlanCopyStaticFlagList_Type = Vlanset
_RaisecomIgmpVlanCopyStaticFlagList_Object = MibTableColumn
raisecomIgmpVlanCopyStaticFlagList = _RaisecomIgmpVlanCopyStaticFlagList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 6),
    _RaisecomIgmpVlanCopyStaticFlagList_Type()
)
raisecomIgmpVlanCopyStaticFlagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyStaticFlagList.setStatus("current")
_RaisecomIgmpVlanCopyRowStatus_Type = RowStatus
_RaisecomIgmpVlanCopyRowStatus_Object = MibTableColumn
raisecomIgmpVlanCopyRowStatus = _RaisecomIgmpVlanCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 2, 3, 3, 1, 7),
    _RaisecomIgmpVlanCopyRowStatus_Type()
)
raisecomIgmpVlanCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyRowStatus.setStatus("current")
_RaisecomMcastConformance_ObjectIdentity = ObjectIdentity
raisecomMcastConformance = _RaisecomMcastConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 27, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-MCAST-MIB",
    **{"raisecomMcast": raisecomMcast,
       "raisecomMcastNotifications": raisecomMcastNotifications,
       "raisecomMcastObjects": raisecomMcastObjects,
       "raisecomMcastScalar": raisecomMcastScalar,
       "raisecomMulticastFilterEnable": raisecomMulticastFilterEnable,
       "raisecomMulticastFilterVlanlist": raisecomMulticastFilterVlanlist,
       "raisecomMcastL2": raisecomMcastL2,
       "raisecomL2MulticastMaxGroupNum": raisecomL2MulticastMaxGroupNum,
       "raisecomL2MulticastCurrentGroupNum": raisecomL2MulticastCurrentGroupNum,
       "raisecomL2MulticastAddressTable": raisecomL2MulticastAddressTable,
       "raisecomL2MulticastAddressEntry": raisecomL2MulticastAddressEntry,
       "raisecomL2MulticastMVlan": raisecomL2MulticastMVlan,
       "raisecomL2MulticastAddress": raisecomL2MulticastAddress,
       "raisecomL2MulticastEgressPortlist": raisecomL2MulticastEgressPortlist,
       "raisecomL2MulticastStaticPortlist": raisecomL2MulticastStaticPortlist,
       "raisecomL2MulticastRowStatus": raisecomL2MulticastRowStatus,
       "raisecomMcastVlanCopy": raisecomMcastVlanCopy,
       "raisecomIgmpVlanCopyMaxGroupNum": raisecomIgmpVlanCopyMaxGroupNum,
       "raisecomIgmpVlanCopyCurrentGroupNum": raisecomIgmpVlanCopyCurrentGroupNum,
       "raisecomIgmpVlanCopyAddressTable": raisecomIgmpVlanCopyAddressTable,
       "raisecomIgmpVlanCopyAddressEntry": raisecomIgmpVlanCopyAddressEntry,
       "raisecomIgmpVlanCopyMVlan": raisecomIgmpVlanCopyMVlan,
       "raisecomIgmpVlanCopyIpAddressType": raisecomIgmpVlanCopyIpAddressType,
       "raisecomIgmpVlanCopyIpAddress": raisecomIgmpVlanCopyIpAddress,
       "raisecomIgmpVlanCopyEgressPort": raisecomIgmpVlanCopyEgressPort,
       "raisecomIgmpVlanCopyUVlanList": raisecomIgmpVlanCopyUVlanList,
       "raisecomIgmpVlanCopyStaticFlagList": raisecomIgmpVlanCopyStaticFlagList,
       "raisecomIgmpVlanCopyRowStatus": raisecomIgmpVlanCopyRowStatus,
       "raisecomMcastConformance": raisecomMcastConformance}
)
