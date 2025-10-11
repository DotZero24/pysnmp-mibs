# SNMP MIB module (RUCKUS-WIRED-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/RUCKUS-WIRED-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:00:59 2025
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

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusWiredClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43)
)
if mibBuilder.loadTexts:
    ruckusWiredClientMIB.setRevisions(
        ("2019-02-28 00:00",
         "2023-05-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_RuckusWiredClientNotify_ObjectIdentity = ObjectIdentity
ruckusWiredClientNotify = _RuckusWiredClientNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 0)
)
_RuckusWiredClientObjects_ObjectIdentity = ObjectIdentity
ruckusWiredClientObjects = _RuckusWiredClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1)
)
_RuckusWiredClients_ObjectIdentity = ObjectIdentity
ruckusWiredClients = _RuckusWiredClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1)
)
_RuckusWiredClientsTable_Object = MibTable
ruckusWiredClientsTable = _RuckusWiredClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusWiredClientsTable.setStatus("current")
_RuckusWiredClientEntry_Object = MibTableRow
ruckusWiredClientEntry = _RuckusWiredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1)
)
ruckusWiredClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientMac"),
)
if mibBuilder.loadTexts:
    ruckusWiredClientEntry.setStatus("current")
_RuckusWiredClientMac_Type = MacAddress
_RuckusWiredClientMac_Object = MibTableColumn
ruckusWiredClientMac = _RuckusWiredClientMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 1),
    _RuckusWiredClientMac_Type()
)
ruckusWiredClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientMac.setStatus("current")
_RuckusWiredClientVlan_Type = VlanId
_RuckusWiredClientVlan_Object = MibTableColumn
ruckusWiredClientVlan = _RuckusWiredClientVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 2),
    _RuckusWiredClientVlan_Type()
)
ruckusWiredClientVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientVlan.setStatus("current")


class _RuckusWiredClientType_Type(Integer32):
    """Custom type ruckusWiredClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("phone", 2),
          ("wlanAP", 3),
          ("router", 4),
          ("bridge", 5),
          ("cableDevice", 6))
    )


_RuckusWiredClientType_Type.__name__ = "Integer32"
_RuckusWiredClientType_Object = MibTableColumn
ruckusWiredClientType = _RuckusWiredClientType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 3),
    _RuckusWiredClientType_Type()
)
ruckusWiredClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientType.setStatus("current")


class _RuckusWiredClientAuthType_Type(Integer32):
    """Custom type ruckusWiredClientAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dot1x", 2),
          ("macAuth", 3),
          ("webAuth", 4))
    )


_RuckusWiredClientAuthType_Type.__name__ = "Integer32"
_RuckusWiredClientAuthType_Object = MibTableColumn
ruckusWiredClientAuthType = _RuckusWiredClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 4),
    _RuckusWiredClientAuthType_Type()
)
ruckusWiredClientAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientAuthType.setStatus("current")


class _RuckusWiredClientStatus_Type(Integer32):
    """Custom type ruckusWiredClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("allowed", 2),
          ("blocked", 3),
          ("restricted", 4),
          ("critical", 5),
          ("guest", 6))
    )


_RuckusWiredClientStatus_Type.__name__ = "Integer32"
_RuckusWiredClientStatus_Object = MibTableColumn
ruckusWiredClientStatus = _RuckusWiredClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 5),
    _RuckusWiredClientStatus_Type()
)
ruckusWiredClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientStatus.setStatus("current")
_RuckusWiredClientDescr_Type = SnmpAdminString
_RuckusWiredClientDescr_Object = MibTableColumn
ruckusWiredClientDescr = _RuckusWiredClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 6),
    _RuckusWiredClientDescr_Type()
)
ruckusWiredClientDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientDescr.setStatus("current")
_RuckusWiredClientUserName_Type = SnmpAdminString
_RuckusWiredClientUserName_Object = MibTableColumn
ruckusWiredClientUserName = _RuckusWiredClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 7),
    _RuckusWiredClientUserName_Type()
)
ruckusWiredClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientUserName.setStatus("current")
_RuckusWiredClientV4Addr_Type = InetAddressIPv4
_RuckusWiredClientV4Addr_Object = MibTableColumn
ruckusWiredClientV4Addr = _RuckusWiredClientV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 8),
    _RuckusWiredClientV4Addr_Type()
)
ruckusWiredClientV4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientV4Addr.setStatus("current")
_RuckusWiredClientV6Addr_Type = InetAddressIPv6
_RuckusWiredClientV6Addr_Object = MibTableColumn
ruckusWiredClientV6Addr = _RuckusWiredClientV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 9),
    _RuckusWiredClientV6Addr_Type()
)
ruckusWiredClientV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientV6Addr.setStatus("current")
_RuckusWiredClientUpTime_Type = TimeTicks
_RuckusWiredClientUpTime_Object = MibTableColumn
ruckusWiredClientUpTime = _RuckusWiredClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 10),
    _RuckusWiredClientUpTime_Type()
)
ruckusWiredClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientUpTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWiredClientUpTime.setUnits("centi-seconds")
_RuckusWiredClientTxPkts_Type = Counter64
_RuckusWiredClientTxPkts_Object = MibTableColumn
ruckusWiredClientTxPkts = _RuckusWiredClientTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 11),
    _RuckusWiredClientTxPkts_Type()
)
ruckusWiredClientTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientTxPkts.setStatus("current")
_RuckusWiredClientRxPkts_Type = Counter64
_RuckusWiredClientRxPkts_Object = MibTableColumn
ruckusWiredClientRxPkts = _RuckusWiredClientRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 12),
    _RuckusWiredClientRxPkts_Type()
)
ruckusWiredClientRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientRxPkts.setStatus("current")
_RuckusWiredClientTxOctets_Type = Counter64
_RuckusWiredClientTxOctets_Object = MibTableColumn
ruckusWiredClientTxOctets = _RuckusWiredClientTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 13),
    _RuckusWiredClientTxOctets_Type()
)
ruckusWiredClientTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientTxOctets.setStatus("current")
_RuckusWiredClientRxOctets_Type = Counter64
_RuckusWiredClientRxOctets_Object = MibTableColumn
ruckusWiredClientRxOctets = _RuckusWiredClientRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 14),
    _RuckusWiredClientRxOctets_Type()
)
ruckusWiredClientRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWiredClientRxOctets.setStatus("current")
_RuckusDhcpClientHostName_Type = SnmpAdminString
_RuckusDhcpClientHostName_Object = MibTableColumn
ruckusDhcpClientHostName = _RuckusDhcpClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 15),
    _RuckusDhcpClientHostName_Type()
)
ruckusDhcpClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDhcpClientHostName.setStatus("current")
_RuckusDhcpClientDeviceTypeName_Type = SnmpAdminString
_RuckusDhcpClientDeviceTypeName_Object = MibTableColumn
ruckusDhcpClientDeviceTypeName = _RuckusDhcpClientDeviceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 16),
    _RuckusDhcpClientDeviceTypeName_Type()
)
ruckusDhcpClientDeviceTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDhcpClientDeviceTypeName.setStatus("current")
_RuckusDhcpClientOsVendorName_Type = SnmpAdminString
_RuckusDhcpClientOsVendorName_Object = MibTableColumn
ruckusDhcpClientOsVendorName = _RuckusDhcpClientOsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 17),
    _RuckusDhcpClientOsVendorName_Type()
)
ruckusDhcpClientOsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDhcpClientOsVendorName.setStatus("current")
_RuckusDhcpClientModelName_Type = SnmpAdminString
_RuckusDhcpClientModelName_Object = MibTableColumn
ruckusDhcpClientModelName = _RuckusDhcpClientModelName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 1, 1, 1, 1, 18),
    _RuckusDhcpClientModelName_Type()
)
ruckusDhcpClientModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDhcpClientModelName.setStatus("current")
_RuckusWiredClientConformance_ObjectIdentity = ObjectIdentity
ruckusWiredClientConformance = _RuckusWiredClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 2)
)
_RuckusWiredClientMIBCompliances_ObjectIdentity = ObjectIdentity
ruckusWiredClientMIBCompliances = _RuckusWiredClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 2, 1)
)
_RuckusWiredClientMIBGroups_ObjectIdentity = ObjectIdentity
ruckusWiredClientMIBGroups = _RuckusWiredClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 2, 2)
)

# Managed Objects groups

ruckusWiredClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 2, 2, 1)
)
ruckusWiredClientGroup.setObjects(
      *(("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientMac"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientVlan"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientType"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientAuthType"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientStatus"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientDescr"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientUserName"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientV4Addr"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientV6Addr"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientUpTime"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientTxPkts"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientRxPkts"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientTxOctets"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientRxOctets"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusDhcpClientHostName"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusDhcpClientDeviceTypeName"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusDhcpClientOsVendorName"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusDhcpClientModelName"))
)
if mibBuilder.loadTexts:
    ruckusWiredClientGroup.setStatus("current")


# Notification objects

ruckusWiredClientConnectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 0, 1)
)
ruckusWiredClientConnectedNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientMac"))
)
if mibBuilder.loadTexts:
    ruckusWiredClientConnectedNotify.setStatus(
        "current"
    )

ruckusWiredClientDisconnectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 0, 2)
)
ruckusWiredClientDisconnectedNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientMac"))
)
if mibBuilder.loadTexts:
    ruckusWiredClientDisconnectedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruckusWiredClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 43, 2, 1, 1)
)
ruckusWiredClientCompliance.setObjects(
    ("RUCKUS-WIRED-CLIENT-MIB", "ruckusWiredClientGroup")
)
if mibBuilder.loadTexts:
    ruckusWiredClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-WIRED-CLIENT-MIB",
    **{"VlanId": VlanId,
       "ruckusWiredClientMIB": ruckusWiredClientMIB,
       "ruckusWiredClientNotify": ruckusWiredClientNotify,
       "ruckusWiredClientConnectedNotify": ruckusWiredClientConnectedNotify,
       "ruckusWiredClientDisconnectedNotify": ruckusWiredClientDisconnectedNotify,
       "ruckusWiredClientObjects": ruckusWiredClientObjects,
       "ruckusWiredClients": ruckusWiredClients,
       "ruckusWiredClientsTable": ruckusWiredClientsTable,
       "ruckusWiredClientEntry": ruckusWiredClientEntry,
       "ruckusWiredClientMac": ruckusWiredClientMac,
       "ruckusWiredClientVlan": ruckusWiredClientVlan,
       "ruckusWiredClientType": ruckusWiredClientType,
       "ruckusWiredClientAuthType": ruckusWiredClientAuthType,
       "ruckusWiredClientStatus": ruckusWiredClientStatus,
       "ruckusWiredClientDescr": ruckusWiredClientDescr,
       "ruckusWiredClientUserName": ruckusWiredClientUserName,
       "ruckusWiredClientV4Addr": ruckusWiredClientV4Addr,
       "ruckusWiredClientV6Addr": ruckusWiredClientV6Addr,
       "ruckusWiredClientUpTime": ruckusWiredClientUpTime,
       "ruckusWiredClientTxPkts": ruckusWiredClientTxPkts,
       "ruckusWiredClientRxPkts": ruckusWiredClientRxPkts,
       "ruckusWiredClientTxOctets": ruckusWiredClientTxOctets,
       "ruckusWiredClientRxOctets": ruckusWiredClientRxOctets,
       "ruckusDhcpClientHostName": ruckusDhcpClientHostName,
       "ruckusDhcpClientDeviceTypeName": ruckusDhcpClientDeviceTypeName,
       "ruckusDhcpClientOsVendorName": ruckusDhcpClientOsVendorName,
       "ruckusDhcpClientModelName": ruckusDhcpClientModelName,
       "ruckusWiredClientConformance": ruckusWiredClientConformance,
       "ruckusWiredClientMIBCompliances": ruckusWiredClientMIBCompliances,
       "ruckusWiredClientCompliance": ruckusWiredClientCompliance,
       "ruckusWiredClientMIBGroups": ruckusWiredClientMIBGroups,
       "ruckusWiredClientGroup": ruckusWiredClientGroup}
)
