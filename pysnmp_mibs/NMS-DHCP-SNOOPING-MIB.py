# SNMP MIB module (NMS-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bdcom/NMS-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:05:18 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dhcpsnooping_ObjectIdentity = ObjectIdentity
dhcpsnooping = _Dhcpsnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233)
)


class _DhcpSnoopingStatus_Type(Integer32):
    """Custom type dhcpSnoopingStatus based on Integer32"""
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


_DhcpSnoopingStatus_Type.__name__ = "Integer32"
_DhcpSnoopingStatus_Object = MibScalar
dhcpSnoopingStatus = _DhcpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 1),
    _DhcpSnoopingStatus_Type()
)
dhcpSnoopingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingStatus.setStatus("mandatory")
_NmsBindingsTable_Object = MibTable
nmsBindingsTable = _NmsBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2)
)
if mibBuilder.loadTexts:
    nmsBindingsTable.setStatus("current")
_NmsBindingsEntry_Object = MibTableRow
nmsBindingsEntry = _NmsBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1)
)
nmsBindingsEntry.setIndexNames(
    (0, "NMS-DHCP-SNOOPING-MIB", "nmsBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    nmsBindingsEntry.setStatus("current")
_NmsBindingsIpAddress_Type = InetAddress
_NmsBindingsIpAddress_Object = MibTableColumn
nmsBindingsIpAddress = _NmsBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 1),
    _NmsBindingsIpAddress_Type()
)
nmsBindingsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsIpAddress.setStatus("current")
_NmsBindingsMacAddress_Type = MacAddress
_NmsBindingsMacAddress_Object = MibTableColumn
nmsBindingsMacAddress = _NmsBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 2),
    _NmsBindingsMacAddress_Type()
)
nmsBindingsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsMacAddress.setStatus("current")
_NmsBindingsVlan_Type = VlanIndex
_NmsBindingsVlan_Object = MibTableColumn
nmsBindingsVlan = _NmsBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 3),
    _NmsBindingsVlan_Type()
)
nmsBindingsVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsVlan.setStatus("current")
_NmsBindingsInterface_Type = InterfaceIndex
_NmsBindingsInterface_Object = MibTableColumn
nmsBindingsInterface = _NmsBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 4),
    _NmsBindingsInterface_Type()
)
nmsBindingsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsInterface.setStatus("current")
_NmsBindingsLeasedTime_Type = Unsigned32
_NmsBindingsLeasedTime_Object = MibTableColumn
nmsBindingsLeasedTime = _NmsBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 5),
    _NmsBindingsLeasedTime_Type()
)
nmsBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    nmsBindingsLeasedTime.setUnits("seconds")
_NmsBindingsType_Type = Unsigned32
_NmsBindingsType_Object = MibTableColumn
nmsBindingsType = _NmsBindingsType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 6),
    _NmsBindingsType_Type()
)
nmsBindingsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsType.setStatus("current")
_NmsBindingsStatus_Type = Unsigned32
_NmsBindingsStatus_Object = MibTableColumn
nmsBindingsStatus = _NmsBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 7),
    _NmsBindingsStatus_Type()
)
nmsBindingsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsBindingsStatus.setStatus("current")
_NmsBindingsrowstatus_Type = RowStatus
_NmsBindingsrowstatus_Object = MibTableColumn
nmsBindingsrowstatus = _NmsBindingsrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 2, 1, 8),
    _NmsBindingsrowstatus_Type()
)
nmsBindingsrowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsBindingsrowstatus.setStatus("mandatory")
_NmsipsourceBindingsTable_Object = MibTable
nmsipsourceBindingsTable = _NmsipsourceBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3)
)
if mibBuilder.loadTexts:
    nmsipsourceBindingsTable.setStatus("current")
_NmsipsourceBindingsEntry_Object = MibTableRow
nmsipsourceBindingsEntry = _NmsipsourceBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1)
)
nmsipsourceBindingsEntry.setIndexNames(
    (0, "NMS-DHCP-SNOOPING-MIB", "nmsipsourceBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    nmsipsourceBindingsEntry.setStatus("current")
_NmsipsourceBindingsrowstatus_Type = RowStatus
_NmsipsourceBindingsrowstatus_Object = MibTableColumn
nmsipsourceBindingsrowstatus = _NmsipsourceBindingsrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1, 1),
    _NmsipsourceBindingsrowstatus_Type()
)
nmsipsourceBindingsrowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsipsourceBindingsrowstatus.setStatus("mandatory")
_NmsipsourceBindingsIpAddress_Type = InetAddress
_NmsipsourceBindingsIpAddress_Object = MibTableColumn
nmsipsourceBindingsIpAddress = _NmsipsourceBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1, 2),
    _NmsipsourceBindingsIpAddress_Type()
)
nmsipsourceBindingsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsipsourceBindingsIpAddress.setStatus("current")
_NmsipsourceBindingsMacAddress_Type = MacAddress
_NmsipsourceBindingsMacAddress_Object = MibTableColumn
nmsipsourceBindingsMacAddress = _NmsipsourceBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1, 3),
    _NmsipsourceBindingsMacAddress_Type()
)
nmsipsourceBindingsMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsipsourceBindingsMacAddress.setStatus("current")
_NmsipsourceBindingsInterface_Type = InterfaceIndex
_NmsipsourceBindingsInterface_Object = MibTableColumn
nmsipsourceBindingsInterface = _NmsipsourceBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1, 4),
    _NmsipsourceBindingsInterface_Type()
)
nmsipsourceBindingsInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsipsourceBindingsInterface.setStatus("current")
_NmsipsourceBindingsVlanID_Type = VlanIndex
_NmsipsourceBindingsVlanID_Object = MibTableColumn
nmsipsourceBindingsVlanID = _NmsipsourceBindingsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 233, 3, 1, 5),
    _NmsipsourceBindingsVlanID_Type()
)
nmsipsourceBindingsVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsipsourceBindingsVlanID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-DHCP-SNOOPING-MIB",
    **{"dhcpsnooping": dhcpsnooping,
       "dhcpSnoopingStatus": dhcpSnoopingStatus,
       "nmsBindingsTable": nmsBindingsTable,
       "nmsBindingsEntry": nmsBindingsEntry,
       "nmsBindingsIpAddress": nmsBindingsIpAddress,
       "nmsBindingsMacAddress": nmsBindingsMacAddress,
       "nmsBindingsVlan": nmsBindingsVlan,
       "nmsBindingsInterface": nmsBindingsInterface,
       "nmsBindingsLeasedTime": nmsBindingsLeasedTime,
       "nmsBindingsType": nmsBindingsType,
       "nmsBindingsStatus": nmsBindingsStatus,
       "nmsBindingsrowstatus": nmsBindingsrowstatus,
       "nmsipsourceBindingsTable": nmsipsourceBindingsTable,
       "nmsipsourceBindingsEntry": nmsipsourceBindingsEntry,
       "nmsipsourceBindingsrowstatus": nmsipsourceBindingsrowstatus,
       "nmsipsourceBindingsIpAddress": nmsipsourceBindingsIpAddress,
       "nmsipsourceBindingsMacAddress": nmsipsourceBindingsMacAddress,
       "nmsipsourceBindingsInterface": nmsipsourceBindingsInterface,
       "nmsipsourceBindingsVlanID": nmsipsourceBindingsVlanID}
)
