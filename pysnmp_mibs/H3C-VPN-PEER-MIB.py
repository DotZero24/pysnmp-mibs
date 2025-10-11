# SNMP MIB module (H3C-VPN-PEER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-VPN-PEER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:33 2025
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

h3cVpnPeer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165)
)
if mibBuilder.loadTexts:
    h3cVpnPeer.setRevisions(
        ("2016-03-09 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVpnPeerGroup_ObjectIdentity = ObjectIdentity
h3cVpnPeerGroup = _H3cVpnPeerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1)
)
_H3cVpnPeerStat_ObjectIdentity = ObjectIdentity
h3cVpnPeerStat = _H3cVpnPeerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1)
)
_H3cVpnPeerStatTable_Object = MibTable
h3cVpnPeerStatTable = _H3cVpnPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVpnPeerStatTable.setStatus("current")
_H3cVpnPeerStatEntry_Object = MibTableRow
h3cVpnPeerStatEntry = _H3cVpnPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1)
)
h3cVpnPeerStatEntry.setIndexNames(
    (0, "H3C-VPN-PEER-MIB", "h3cVpnPeerName"),
)
if mibBuilder.loadTexts:
    h3cVpnPeerStatEntry.setStatus("current")


class _H3cVpnPeerName_Type(OctetString):
    """Custom type h3cVpnPeerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVpnPeerName_Type.__name__ = "OctetString"
_H3cVpnPeerName_Object = MibTableColumn
h3cVpnPeerName = _H3cVpnPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1, 1),
    _H3cVpnPeerName_Type()
)
h3cVpnPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVpnPeerName.setStatus("current")
_H3cVpnPeerOutPassPkts_Type = Counter64
_H3cVpnPeerOutPassPkts_Object = MibTableColumn
h3cVpnPeerOutPassPkts = _H3cVpnPeerOutPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1, 2),
    _H3cVpnPeerOutPassPkts_Type()
)
h3cVpnPeerOutPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVpnPeerOutPassPkts.setStatus("current")
_H3cVpnPeerOutPassBytes_Type = Counter64
_H3cVpnPeerOutPassBytes_Object = MibTableColumn
h3cVpnPeerOutPassBytes = _H3cVpnPeerOutPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1, 3),
    _H3cVpnPeerOutPassBytes_Type()
)
h3cVpnPeerOutPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVpnPeerOutPassBytes.setStatus("current")
_H3cVpnPeerOutDropPkts_Type = Counter64
_H3cVpnPeerOutDropPkts_Object = MibTableColumn
h3cVpnPeerOutDropPkts = _H3cVpnPeerOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1, 4),
    _H3cVpnPeerOutDropPkts_Type()
)
h3cVpnPeerOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVpnPeerOutDropPkts.setStatus("current")
_H3cVpnPeerOutDropBytes_Type = Counter64
_H3cVpnPeerOutDropBytes_Object = MibTableColumn
h3cVpnPeerOutDropBytes = _H3cVpnPeerOutDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 165, 1, 1, 1, 1, 5),
    _H3cVpnPeerOutDropBytes_Type()
)
h3cVpnPeerOutDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVpnPeerOutDropBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VPN-PEER-MIB",
    **{"h3cVpnPeer": h3cVpnPeer,
       "h3cVpnPeerGroup": h3cVpnPeerGroup,
       "h3cVpnPeerStat": h3cVpnPeerStat,
       "h3cVpnPeerStatTable": h3cVpnPeerStatTable,
       "h3cVpnPeerStatEntry": h3cVpnPeerStatEntry,
       "h3cVpnPeerName": h3cVpnPeerName,
       "h3cVpnPeerOutPassPkts": h3cVpnPeerOutPassPkts,
       "h3cVpnPeerOutPassBytes": h3cVpnPeerOutPassBytes,
       "h3cVpnPeerOutDropPkts": h3cVpnPeerOutDropPkts,
       "h3cVpnPeerOutDropBytes": h3cVpnPeerOutDropBytes}
)
