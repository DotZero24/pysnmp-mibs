# SNMP MIB module (H3C-EVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-EVPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:30 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cEvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173)
)
if mibBuilder.loadTexts:
    h3cEvpn.setRevisions(
        ("2017-10-21 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEvpnObjects_ObjectIdentity = ObjectIdentity
h3cEvpnObjects = _H3cEvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1)
)
_H3cEvpnESTable_Object = MibTable
h3cEvpnESTable = _H3cEvpnESTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEvpnESTable.setStatus("current")
_H3cEvpnESEntry_Object = MibTableRow
h3cEvpnESEntry = _H3cEvpnESEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1, 1)
)
h3cEvpnESEntry.setIndexNames(
    (0, "H3C-EVPN-MIB", "h3cEvpnESESI"),
)
if mibBuilder.loadTexts:
    h3cEvpnESEntry.setStatus("current")


class _H3cEvpnESESI_Type(OctetString):
    """Custom type h3cEvpnESESI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cEvpnESESI_Type.__name__ = "OctetString"
_H3cEvpnESESI_Object = MibTableColumn
h3cEvpnESESI = _H3cEvpnESESI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1, 1, 1),
    _H3cEvpnESESI_Type()
)
h3cEvpnESESI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvpnESESI.setStatus("current")
_H3cEvpnESIfIndex_Type = InterfaceIndex
_H3cEvpnESIfIndex_Object = MibTableColumn
h3cEvpnESIfIndex = _H3cEvpnESIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1, 1, 2),
    _H3cEvpnESIfIndex_Type()
)
h3cEvpnESIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESIfIndex.setStatus("current")


class _H3cEvpnESIfName_Type(DisplayString):
    """Custom type h3cEvpnESIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEvpnESIfName_Type.__name__ = "DisplayString"
_H3cEvpnESIfName_Object = MibTableColumn
h3cEvpnESIfName = _H3cEvpnESIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1, 1, 3),
    _H3cEvpnESIfName_Type()
)
h3cEvpnESIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESIfName.setStatus("current")
_H3cEvpnESMode_Type = Unsigned32
_H3cEvpnESMode_Object = MibTableColumn
h3cEvpnESMode = _H3cEvpnESMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 1, 1, 4),
    _H3cEvpnESMode_Type()
)
h3cEvpnESMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESMode.setStatus("current")
_H3cEvpnESMemberTable_Object = MibTable
h3cEvpnESMemberTable = _H3cEvpnESMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEvpnESMemberTable.setStatus("current")
_H3cEvpnESMemberEntry_Object = MibTableRow
h3cEvpnESMemberEntry = _H3cEvpnESMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 2, 1)
)
h3cEvpnESMemberEntry.setIndexNames(
    (0, "H3C-EVPN-MIB", "h3cEvpnESESI"),
    (0, "H3C-EVPN-MIB", "h3cEvpnESMemberIPType"),
    (0, "H3C-EVPN-MIB", "h3cEvpnESMemberIP"),
)
if mibBuilder.loadTexts:
    h3cEvpnESMemberEntry.setStatus("current")
_H3cEvpnESMemberIPType_Type = InetAddressType
_H3cEvpnESMemberIPType_Object = MibTableColumn
h3cEvpnESMemberIPType = _H3cEvpnESMemberIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 2, 1, 1),
    _H3cEvpnESMemberIPType_Type()
)
h3cEvpnESMemberIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvpnESMemberIPType.setStatus("current")
_H3cEvpnESMemberIP_Type = InetAddress
_H3cEvpnESMemberIP_Object = MibTableColumn
h3cEvpnESMemberIP = _H3cEvpnESMemberIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 2, 1, 2),
    _H3cEvpnESMemberIP_Type()
)
h3cEvpnESMemberIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvpnESMemberIP.setStatus("current")
_H3cEvpnESMemberIsSelf_Type = TruthValue
_H3cEvpnESMemberIsSelf_Object = MibTableColumn
h3cEvpnESMemberIsSelf = _H3cEvpnESMemberIsSelf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 2, 1, 3),
    _H3cEvpnESMemberIsSelf_Type()
)
h3cEvpnESMemberIsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESMemberIsSelf.setStatus("current")
_H3cEvpnESDFTable_Object = MibTable
h3cEvpnESDFTable = _H3cEvpnESDFTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3)
)
if mibBuilder.loadTexts:
    h3cEvpnESDFTable.setStatus("current")
_H3cEvpnESDFEntry_Object = MibTableRow
h3cEvpnESDFEntry = _H3cEvpnESDFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1)
)
h3cEvpnESDFEntry.setIndexNames(
    (0, "H3C-EVPN-MIB", "h3cEvpnESESI"),
    (0, "H3C-EVPN-MIB", "h3cEvpnESDFVLANID"),
)
if mibBuilder.loadTexts:
    h3cEvpnESDFEntry.setStatus("current")
_H3cEvpnESDFVLANID_Type = Unsigned32
_H3cEvpnESDFVLANID_Object = MibTableColumn
h3cEvpnESDFVLANID = _H3cEvpnESDFVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 1),
    _H3cEvpnESDFVLANID_Type()
)
h3cEvpnESDFVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvpnESDFVLANID.setStatus("current")
_H3cEvpnESDFAcIfIndex_Type = InterfaceIndex
_H3cEvpnESDFAcIfIndex_Object = MibTableColumn
h3cEvpnESDFAcIfIndex = _H3cEvpnESDFAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 2),
    _H3cEvpnESDFAcIfIndex_Type()
)
h3cEvpnESDFAcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESDFAcIfIndex.setStatus("current")
_H3cEvpnESDFACEvcSrvInstId_Type = Unsigned32
_H3cEvpnESDFACEvcSrvInstId_Object = MibTableColumn
h3cEvpnESDFACEvcSrvInstId = _H3cEvpnESDFACEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 3),
    _H3cEvpnESDFACEvcSrvInstId_Type()
)
h3cEvpnESDFACEvcSrvInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESDFACEvcSrvInstId.setStatus("current")
_H3cEvpnESDFMode_Type = Unsigned32
_H3cEvpnESDFMode_Object = MibTableColumn
h3cEvpnESDFMode = _H3cEvpnESDFMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 4),
    _H3cEvpnESDFMode_Type()
)
h3cEvpnESDFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESDFMode.setStatus("current")
_H3cEvpnESDFRouterIPType_Type = InetAddressType
_H3cEvpnESDFRouterIPType_Object = MibTableColumn
h3cEvpnESDFRouterIPType = _H3cEvpnESDFRouterIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 5),
    _H3cEvpnESDFRouterIPType_Type()
)
h3cEvpnESDFRouterIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESDFRouterIPType.setStatus("current")
_H3cEvpnESDFRouterIP_Type = InetAddress
_H3cEvpnESDFRouterIP_Object = MibTableColumn
h3cEvpnESDFRouterIP = _H3cEvpnESDFRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 173, 1, 3, 1, 6),
    _H3cEvpnESDFRouterIP_Type()
)
h3cEvpnESDFRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvpnESDFRouterIP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EVPN-MIB",
    **{"h3cEvpn": h3cEvpn,
       "h3cEvpnObjects": h3cEvpnObjects,
       "h3cEvpnESTable": h3cEvpnESTable,
       "h3cEvpnESEntry": h3cEvpnESEntry,
       "h3cEvpnESESI": h3cEvpnESESI,
       "h3cEvpnESIfIndex": h3cEvpnESIfIndex,
       "h3cEvpnESIfName": h3cEvpnESIfName,
       "h3cEvpnESMode": h3cEvpnESMode,
       "h3cEvpnESMemberTable": h3cEvpnESMemberTable,
       "h3cEvpnESMemberEntry": h3cEvpnESMemberEntry,
       "h3cEvpnESMemberIPType": h3cEvpnESMemberIPType,
       "h3cEvpnESMemberIP": h3cEvpnESMemberIP,
       "h3cEvpnESMemberIsSelf": h3cEvpnESMemberIsSelf,
       "h3cEvpnESDFTable": h3cEvpnESDFTable,
       "h3cEvpnESDFEntry": h3cEvpnESDFEntry,
       "h3cEvpnESDFVLANID": h3cEvpnESDFVLANID,
       "h3cEvpnESDFAcIfIndex": h3cEvpnESDFAcIfIndex,
       "h3cEvpnESDFACEvcSrvInstId": h3cEvpnESDFACEvcSrvInstId,
       "h3cEvpnESDFMode": h3cEvpnESDFMode,
       "h3cEvpnESDFRouterIPType": h3cEvpnESDFRouterIPType,
       "h3cEvpnESDFRouterIP": h3cEvpnESDFRouterIP}
)
