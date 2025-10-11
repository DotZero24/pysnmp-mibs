# SNMP MIB module (ZYXEL-NLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-NLB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:12 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelNlb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelNlbSetup_ObjectIdentity = ObjectIdentity
zyxelNlbSetup = _ZyxelNlbSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1)
)
_ZyNlbMaxNumberOfMacForwards_Type = Integer32
_ZyNlbMaxNumberOfMacForwards_Object = MibScalar
zyNlbMaxNumberOfMacForwards = _ZyNlbMaxNumberOfMacForwards_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 1),
    _ZyNlbMaxNumberOfMacForwards_Type()
)
zyNlbMaxNumberOfMacForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyNlbMaxNumberOfMacForwards.setStatus("current")
_ZyxelNlbMacForwardTable_Object = MibTable
zyxelNlbMacForwardTable = _ZyxelNlbMacForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelNlbMacForwardTable.setStatus("current")
_ZyxelNlbMacForwardEntry_Object = MibTableRow
zyxelNlbMacForwardEntry = _ZyxelNlbMacForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1)
)
zyxelNlbMacForwardEntry.setIndexNames(
    (0, "ZYXEL-NLB-MIB", "zyNlbMacForwardVlan"),
    (0, "ZYXEL-NLB-MIB", "zyNlbMacForwardMacAddress"),
)
if mibBuilder.loadTexts:
    zyxelNlbMacForwardEntry.setStatus("current")


class _ZyNlbMacForwardVlan_Type(Integer32):
    """Custom type zyNlbMacForwardVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyNlbMacForwardVlan_Type.__name__ = "Integer32"
_ZyNlbMacForwardVlan_Object = MibTableColumn
zyNlbMacForwardVlan = _ZyNlbMacForwardVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1, 1),
    _ZyNlbMacForwardVlan_Type()
)
zyNlbMacForwardVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNlbMacForwardVlan.setStatus("current")
_ZyNlbMacForwardMacAddress_Type = MacAddress
_ZyNlbMacForwardMacAddress_Object = MibTableColumn
zyNlbMacForwardMacAddress = _ZyNlbMacForwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1, 2),
    _ZyNlbMacForwardMacAddress_Type()
)
zyNlbMacForwardMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNlbMacForwardMacAddress.setStatus("current")
_ZyNlbMacForwardEgressPorts_Type = PortList
_ZyNlbMacForwardEgressPorts_Object = MibTableColumn
zyNlbMacForwardEgressPorts = _ZyNlbMacForwardEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1, 3),
    _ZyNlbMacForwardEgressPorts_Type()
)
zyNlbMacForwardEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNlbMacForwardEgressPorts.setStatus("current")
_ZyNlbMacForwardName_Type = OctetString
_ZyNlbMacForwardName_Object = MibTableColumn
zyNlbMacForwardName = _ZyNlbMacForwardName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1, 4),
    _ZyNlbMacForwardName_Type()
)
zyNlbMacForwardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNlbMacForwardName.setStatus("current")
_ZyNlbMacForwardRowStatus_Type = RowStatus
_ZyNlbMacForwardRowStatus_Object = MibTableColumn
zyNlbMacForwardRowStatus = _ZyNlbMacForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 2, 1, 5),
    _ZyNlbMacForwardRowStatus_Type()
)
zyNlbMacForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyNlbMacForwardRowStatus.setStatus("current")
_ZyNlbMaxNumberOfIps_Type = Integer32
_ZyNlbMaxNumberOfIps_Object = MibScalar
zyNlbMaxNumberOfIps = _ZyNlbMaxNumberOfIps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 3),
    _ZyNlbMaxNumberOfIps_Type()
)
zyNlbMaxNumberOfIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyNlbMaxNumberOfIps.setStatus("current")
_ZyxelNlbIpTable_Object = MibTable
zyxelNlbIpTable = _ZyxelNlbIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelNlbIpTable.setStatus("current")
_ZyxelNlbIpEntry_Object = MibTableRow
zyxelNlbIpEntry = _ZyxelNlbIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1)
)
zyxelNlbIpEntry.setIndexNames(
    (0, "ZYXEL-NLB-MIB", "zyNlbIpInetAddressType"),
    (0, "ZYXEL-NLB-MIB", "zyNlbIpInetAddress"),
)
if mibBuilder.loadTexts:
    zyxelNlbIpEntry.setStatus("current")
_ZyNlbIpInetAddressType_Type = InetAddressType
_ZyNlbIpInetAddressType_Object = MibTableColumn
zyNlbIpInetAddressType = _ZyNlbIpInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1, 1),
    _ZyNlbIpInetAddressType_Type()
)
zyNlbIpInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNlbIpInetAddressType.setStatus("current")
_ZyNlbIpInetAddress_Type = InetAddress
_ZyNlbIpInetAddress_Object = MibTableColumn
zyNlbIpInetAddress = _ZyNlbIpInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1, 2),
    _ZyNlbIpInetAddress_Type()
)
zyNlbIpInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNlbIpInetAddress.setStatus("current")
_ZyNlbIpMacAddress_Type = MacAddress
_ZyNlbIpMacAddress_Object = MibTableColumn
zyNlbIpMacAddress = _ZyNlbIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1, 3),
    _ZyNlbIpMacAddress_Type()
)
zyNlbIpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNlbIpMacAddress.setStatus("current")
_ZyNlbIpName_Type = OctetString
_ZyNlbIpName_Object = MibTableColumn
zyNlbIpName = _ZyNlbIpName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1, 4),
    _ZyNlbIpName_Type()
)
zyNlbIpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNlbIpName.setStatus("current")
_ZyNlbIpRowStatus_Type = RowStatus
_ZyNlbIpRowStatus_Object = MibTableColumn
zyNlbIpRowStatus = _ZyNlbIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 114, 1, 4, 1, 5),
    _ZyNlbIpRowStatus_Type()
)
zyNlbIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyNlbIpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-NLB-MIB",
    **{"zyxelNlb": zyxelNlb,
       "zyxelNlbSetup": zyxelNlbSetup,
       "zyNlbMaxNumberOfMacForwards": zyNlbMaxNumberOfMacForwards,
       "zyxelNlbMacForwardTable": zyxelNlbMacForwardTable,
       "zyxelNlbMacForwardEntry": zyxelNlbMacForwardEntry,
       "zyNlbMacForwardVlan": zyNlbMacForwardVlan,
       "zyNlbMacForwardMacAddress": zyNlbMacForwardMacAddress,
       "zyNlbMacForwardEgressPorts": zyNlbMacForwardEgressPorts,
       "zyNlbMacForwardName": zyNlbMacForwardName,
       "zyNlbMacForwardRowStatus": zyNlbMacForwardRowStatus,
       "zyNlbMaxNumberOfIps": zyNlbMaxNumberOfIps,
       "zyxelNlbIpTable": zyxelNlbIpTable,
       "zyxelNlbIpEntry": zyxelNlbIpEntry,
       "zyNlbIpInetAddressType": zyNlbIpInetAddressType,
       "zyNlbIpInetAddress": zyNlbIpInetAddress,
       "zyNlbIpMacAddress": zyNlbIpMacAddress,
       "zyNlbIpName": zyNlbIpName,
       "zyNlbIpRowStatus": zyNlbIpRowStatus}
)
