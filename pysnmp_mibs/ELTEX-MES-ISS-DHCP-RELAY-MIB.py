# SNMP MIB module (ELTEX-MES-ISS-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:36 2025
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

(fsMIDhcpRelaySrvAddressEntry,) = mibBuilder.importSymbols(
    "ARICENT-DHCP-RLY-MI-MIB",
    "fsMIDhcpRelaySrvAddressEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eltMesIssDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28)
)
if mibBuilder.loadTexts:
    eltMesIssDhcpRelayMIB.setRevisions(
        ("2022-06-02 00:00",
         "2021-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssDhcpRelayObjects_ObjectIdentity = ObjectIdentity
eltMesIssDhcpRelayObjects = _EltMesIssDhcpRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1)
)
_EltMesIssDhcpRelayGlobals_ObjectIdentity = ObjectIdentity
eltMesIssDhcpRelayGlobals = _EltMesIssDhcpRelayGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 1)
)
_EltMesIssDhcpRelaySrv_ObjectIdentity = ObjectIdentity
eltMesIssDhcpRelaySrv = _EltMesIssDhcpRelaySrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 2)
)
_EltMesIssMIDhcpRelaySrvAddressTable_Object = MibTable
eltMesIssMIDhcpRelaySrvAddressTable = _EltMesIssMIDhcpRelaySrvAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssMIDhcpRelaySrvAddressTable.setStatus("current")
_EltMesIssMIDhcpRelaySrvAddressEntry_Object = MibTableRow
eltMesIssMIDhcpRelaySrvAddressEntry = _EltMesIssMIDhcpRelaySrvAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssMIDhcpRelaySrvAddressEntry.setStatus("current")
_EltMesIssMIDhcpRelaySrvSrcPort_Type = InetPortNumber
_EltMesIssMIDhcpRelaySrvSrcPort_Object = MibTableColumn
eltMesIssMIDhcpRelaySrvSrcPort = _EltMesIssMIDhcpRelaySrvSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 2, 1, 1, 1),
    _EltMesIssMIDhcpRelaySrvSrcPort_Type()
)
eltMesIssMIDhcpRelaySrvSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssMIDhcpRelaySrvSrcPort.setStatus("current")
_EltMesIssMIDhcpRelaySrvDstPort_Type = InetPortNumber
_EltMesIssMIDhcpRelaySrvDstPort_Object = MibTableColumn
eltMesIssMIDhcpRelaySrvDstPort = _EltMesIssMIDhcpRelaySrvDstPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 2, 1, 1, 2),
    _EltMesIssMIDhcpRelaySrvDstPort_Type()
)
eltMesIssMIDhcpRelaySrvDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssMIDhcpRelaySrvDstPort.setStatus("current")
_EltMesIssDhcpRelayVlan_ObjectIdentity = ObjectIdentity
eltMesIssDhcpRelayVlan = _EltMesIssDhcpRelayVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 3)
)
_EltMesIssDhcpRelayVlanTable_Object = MibTable
eltMesIssDhcpRelayVlanTable = _EltMesIssDhcpRelayVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssDhcpRelayVlanTable.setStatus("current")
_EltMesIssDhcpRelayVlanEntry_Object = MibTableRow
eltMesIssDhcpRelayVlanEntry = _EltMesIssDhcpRelayVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 3, 1, 1)
)
eltMesIssDhcpRelayVlanEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DHCP-RELAY-MIB", "eltMesIssDhcpRelayVlanId"),
)
if mibBuilder.loadTexts:
    eltMesIssDhcpRelayVlanEntry.setStatus("current")
_EltMesIssDhcpRelayVlanId_Type = VlanId
_EltMesIssDhcpRelayVlanId_Object = MibTableColumn
eltMesIssDhcpRelayVlanId = _EltMesIssDhcpRelayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 3, 1, 1, 1),
    _EltMesIssDhcpRelayVlanId_Type()
)
eltMesIssDhcpRelayVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDhcpRelayVlanId.setStatus("current")


class _EltMesIssDhcpRelayVlanStatus_Type(Integer32):
    """Custom type eltMesIssDhcpRelayVlanStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EltMesIssDhcpRelayVlanStatus_Type.__name__ = "Integer32"
_EltMesIssDhcpRelayVlanStatus_Object = MibTableColumn
eltMesIssDhcpRelayVlanStatus = _EltMesIssDhcpRelayVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28, 1, 3, 1, 1, 2),
    _EltMesIssDhcpRelayVlanStatus_Type()
)
eltMesIssDhcpRelayVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpRelayVlanStatus.setStatus("current")
fsMIDhcpRelaySrvAddressEntry.registerAugmentions(
    ("ELTEX-MES-ISS-DHCP-RELAY-MIB",
     "eltMesIssMIDhcpRelaySrvAddressEntry")
)
eltMesIssMIDhcpRelaySrvAddressEntry.setIndexNames(*fsMIDhcpRelaySrvAddressEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-DHCP-RELAY-MIB",
    **{"eltMesIssDhcpRelayMIB": eltMesIssDhcpRelayMIB,
       "eltMesIssDhcpRelayObjects": eltMesIssDhcpRelayObjects,
       "eltMesIssDhcpRelayGlobals": eltMesIssDhcpRelayGlobals,
       "eltMesIssDhcpRelaySrv": eltMesIssDhcpRelaySrv,
       "eltMesIssMIDhcpRelaySrvAddressTable": eltMesIssMIDhcpRelaySrvAddressTable,
       "eltMesIssMIDhcpRelaySrvAddressEntry": eltMesIssMIDhcpRelaySrvAddressEntry,
       "eltMesIssMIDhcpRelaySrvSrcPort": eltMesIssMIDhcpRelaySrvSrcPort,
       "eltMesIssMIDhcpRelaySrvDstPort": eltMesIssMIDhcpRelaySrvDstPort,
       "eltMesIssDhcpRelayVlan": eltMesIssDhcpRelayVlan,
       "eltMesIssDhcpRelayVlanTable": eltMesIssDhcpRelayVlanTable,
       "eltMesIssDhcpRelayVlanEntry": eltMesIssDhcpRelayVlanEntry,
       "eltMesIssDhcpRelayVlanId": eltMesIssDhcpRelayVlanId,
       "eltMesIssDhcpRelayVlanStatus": eltMesIssDhcpRelayVlanStatus}
)
