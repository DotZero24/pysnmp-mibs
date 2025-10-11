# SNMP MIB module (OCNOS-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/OCNOS-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:17 2025
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

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

(vrVrId,) = mibBuilder.importSymbols(
    "OCNOS-VR-MIB",
    "vrVrId")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

interface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 4)
)
if mibBuilder.loadTexts:
    interface.setRevisions(
        ("2018-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InterfaceNotificationsPrefix_ObjectIdentity = ObjectIdentity
interfaceNotificationsPrefix = _InterfaceNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 4, 0)
)
_InterfaceIfIndexListTable_Object = MibTable
interfaceIfIndexListTable = _InterfaceIfIndexListTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1)
)
if mibBuilder.loadTexts:
    interfaceIfIndexListTable.setStatus("current")
_InterfaceIfIndexListEntry_Object = MibTableRow
interfaceIfIndexListEntry = _InterfaceIfIndexListEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1)
)
interfaceIfIndexListEntry.setIndexNames(
    (0, "OCNOS-VR-MIB", "vrVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceIfIndexListEntry.setStatus("current")
_InterfaceIfName1_Type = OctetString
_InterfaceIfName1_Object = MibTableColumn
interfaceIfName1 = _InterfaceIfName1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 1),
    _InterfaceIfName1_Type()
)
interfaceIfName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfName1.setStatus("current")


class _InterfaceErrDisReason_Type(Bits):
    """Custom type interfaceErrDisReason based on Bits"""
    namedValues = NamedValues(
        *(("lagmismatch", 0),
          ("stpbpduguard", 1),
          ("linkflap", 2))
    )

_InterfaceErrDisReason_Type.__name__ = "Bits"
_InterfaceErrDisReason_Object = MibTableColumn
interfaceErrDisReason = _InterfaceErrDisReason_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 2),
    _InterfaceErrDisReason_Type()
)
interfaceErrDisReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceErrDisReason.setStatus("current")


class _InterfaceAggDownMinLink_Type(Integer32):
    """Custom type interfaceAggDownMinLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_InterfaceAggDownMinLink_Type.__name__ = "Integer32"
_InterfaceAggDownMinLink_Object = MibTableColumn
interfaceAggDownMinLink = _InterfaceAggDownMinLink_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 3),
    _InterfaceAggDownMinLink_Type()
)
interfaceAggDownMinLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAggDownMinLink.setStatus("current")
_InterfaceArpDiscardPackets_Type = Counter64
_InterfaceArpDiscardPackets_Object = MibTableColumn
interfaceArpDiscardPackets = _InterfaceArpDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 4),
    _InterfaceArpDiscardPackets_Type()
)
interfaceArpDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceArpDiscardPackets.setStatus("current")
_InterfaceTxArpDiscardPackets_Type = Counter64
_InterfaceTxArpDiscardPackets_Object = MibTableColumn
interfaceTxArpDiscardPackets = _InterfaceTxArpDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 5),
    _InterfaceTxArpDiscardPackets_Type()
)
interfaceTxArpDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpDiscardPackets.setStatus("current")
_InterfaceRxArpRequestPackets_Type = Counter64
_InterfaceRxArpRequestPackets_Object = MibTableColumn
interfaceRxArpRequestPackets = _InterfaceRxArpRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 6),
    _InterfaceRxArpRequestPackets_Type()
)
interfaceRxArpRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpRequestPackets.setStatus("current")
_InterfaceRxArpReplyPackets_Type = Counter64
_InterfaceRxArpReplyPackets_Object = MibTableColumn
interfaceRxArpReplyPackets = _InterfaceRxArpReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 7),
    _InterfaceRxArpReplyPackets_Type()
)
interfaceRxArpReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpReplyPackets.setStatus("current")
_InterfaceTxArpRequestPackets_Type = Counter64
_InterfaceTxArpRequestPackets_Object = MibTableColumn
interfaceTxArpRequestPackets = _InterfaceTxArpRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 8),
    _InterfaceTxArpRequestPackets_Type()
)
interfaceTxArpRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpRequestPackets.setStatus("current")
_InterfaceTxArpReplyPackets_Type = Counter64
_InterfaceTxArpReplyPackets_Object = MibTableColumn
interfaceTxArpReplyPackets = _InterfaceTxArpReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 9),
    _InterfaceTxArpReplyPackets_Type()
)
interfaceTxArpReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpReplyPackets.setStatus("current")
_InterfaceNdDiscardPackets_Type = Counter64
_InterfaceNdDiscardPackets_Object = MibTableColumn
interfaceNdDiscardPackets = _InterfaceNdDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 10),
    _InterfaceNdDiscardPackets_Type()
)
interfaceNdDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNdDiscardPackets.setStatus("current")
_InterfaceTxNdDiscardPackets_Type = Counter64
_InterfaceTxNdDiscardPackets_Object = MibTableColumn
interfaceTxNdDiscardPackets = _InterfaceTxNdDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 11),
    _InterfaceTxNdDiscardPackets_Type()
)
interfaceTxNdDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxNdDiscardPackets.setStatus("current")
_InterfaceRxNDRequestPackets_Type = Counter64
_InterfaceRxNDRequestPackets_Object = MibTableColumn
interfaceRxNDRequestPackets = _InterfaceRxNDRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 12),
    _InterfaceRxNDRequestPackets_Type()
)
interfaceRxNDRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxNDRequestPackets.setStatus("current")
_InterfaceRxNDReplyPackets_Type = Counter64
_InterfaceRxNDReplyPackets_Object = MibTableColumn
interfaceRxNDReplyPackets = _InterfaceRxNDReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 13),
    _InterfaceRxNDReplyPackets_Type()
)
interfaceRxNDReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxNDReplyPackets.setStatus("current")
_InterfaceTxNDRequestPackets_Type = Counter64
_InterfaceTxNDRequestPackets_Object = MibTableColumn
interfaceTxNDRequestPackets = _InterfaceTxNDRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 14),
    _InterfaceTxNDRequestPackets_Type()
)
interfaceTxNDRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxNDRequestPackets.setStatus("current")
_InterfaceTxNDReplyPackets_Type = Counter64
_InterfaceTxNDReplyPackets_Object = MibTableColumn
interfaceTxNDReplyPackets = _InterfaceTxNDReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 36673, 4, 1, 1, 15),
    _InterfaceTxNDReplyPackets_Type()
)
interfaceTxNDReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxNDReplyPackets.setStatus("current")

# Managed Objects groups


# Notification objects

interfaceErrdisNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 4, 0, 1)
)
interfaceErrdisNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("OCNOS-VR-MIB", "vrVrId"),
        ("OCNOS-INTERFACE-MIB", "interfaceErrDisReason"))
)
if mibBuilder.loadTexts:
    interfaceErrdisNotif.setStatus(
        "current"
    )

aggMinLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 4, 0, 2)
)
aggMinLink.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("OCNOS-VR-MIB", "vrVrId"),
        ("OCNOS-INTERFACE-MIB", "interfaceAggDownMinLink"))
)
if mibBuilder.loadTexts:
    aggMinLink.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCNOS-INTERFACE-MIB",
    **{"interface": interface,
       "interfaceNotificationsPrefix": interfaceNotificationsPrefix,
       "interfaceErrdisNotif": interfaceErrdisNotif,
       "aggMinLink": aggMinLink,
       "interfaceIfIndexListTable": interfaceIfIndexListTable,
       "interfaceIfIndexListEntry": interfaceIfIndexListEntry,
       "interfaceIfName1": interfaceIfName1,
       "interfaceErrDisReason": interfaceErrDisReason,
       "interfaceAggDownMinLink": interfaceAggDownMinLink,
       "interfaceArpDiscardPackets": interfaceArpDiscardPackets,
       "interfaceTxArpDiscardPackets": interfaceTxArpDiscardPackets,
       "interfaceRxArpRequestPackets": interfaceRxArpRequestPackets,
       "interfaceRxArpReplyPackets": interfaceRxArpReplyPackets,
       "interfaceTxArpRequestPackets": interfaceTxArpRequestPackets,
       "interfaceTxArpReplyPackets": interfaceTxArpReplyPackets,
       "interfaceNdDiscardPackets": interfaceNdDiscardPackets,
       "interfaceTxNdDiscardPackets": interfaceTxNdDiscardPackets,
       "interfaceRxNDRequestPackets": interfaceRxNDRequestPackets,
       "interfaceRxNDReplyPackets": interfaceRxNDReplyPackets,
       "interfaceTxNDRequestPackets": interfaceTxNDRequestPackets,
       "interfaceTxNDReplyPackets": interfaceTxNDReplyPackets}
)
