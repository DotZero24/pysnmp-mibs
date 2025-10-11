# SNMP MIB module (H3C-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-VXLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:13 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cVxlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150)
)
if mibBuilder.loadTexts:
    h3cVxlan.setRevisions(
        ("2015-02-11 09:00",
         "2013-11-21 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVxlanObjects_ObjectIdentity = ObjectIdentity
h3cVxlanObjects = _H3cVxlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1)
)
_H3cVxlanScalarGroup_ObjectIdentity = ObjectIdentity
h3cVxlanScalarGroup = _H3cVxlanScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 1)
)


class _H3cVxlanLocalMacNotify_Type(TruthValue):
    """Custom type h3cVxlanLocalMacNotify based on TruthValue"""
    defaultValue = 2


_H3cVxlanLocalMacNotify_Type.__name__ = "TruthValue"
_H3cVxlanLocalMacNotify_Object = MibScalar
h3cVxlanLocalMacNotify = _H3cVxlanLocalMacNotify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 1, 1),
    _H3cVxlanLocalMacNotify_Type()
)
h3cVxlanLocalMacNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVxlanLocalMacNotify.setStatus("current")


class _H3cVxlanRemoteMacLearn_Type(TruthValue):
    """Custom type h3cVxlanRemoteMacLearn based on TruthValue"""
    defaultValue = 1


_H3cVxlanRemoteMacLearn_Type.__name__ = "TruthValue"
_H3cVxlanRemoteMacLearn_Object = MibScalar
h3cVxlanRemoteMacLearn = _H3cVxlanRemoteMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 1, 2),
    _H3cVxlanRemoteMacLearn_Type()
)
h3cVxlanRemoteMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVxlanRemoteMacLearn.setStatus("current")
_H3cVxlanNextVxlanID_Type = Unsigned32
_H3cVxlanNextVxlanID_Object = MibScalar
h3cVxlanNextVxlanID = _H3cVxlanNextVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 1, 3),
    _H3cVxlanNextVxlanID_Type()
)
h3cVxlanNextVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanNextVxlanID.setStatus("current")
_H3cVxlanConfigured_Type = Unsigned32
_H3cVxlanConfigured_Object = MibScalar
h3cVxlanConfigured = _H3cVxlanConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 1, 4),
    _H3cVxlanConfigured_Type()
)
h3cVxlanConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanConfigured.setStatus("current")
_H3cVxlanTable_Object = MibTable
h3cVxlanTable = _H3cVxlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVxlanTable.setStatus("current")
_H3cVxlanEntry_Object = MibTableRow
h3cVxlanEntry = _H3cVxlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1)
)
h3cVxlanEntry.setIndexNames(
    (0, "H3C-VXLAN-MIB", "h3cVxlanID"),
)
if mibBuilder.loadTexts:
    h3cVxlanEntry.setStatus("current")
_H3cVxlanID_Type = Unsigned32
_H3cVxlanID_Object = MibTableColumn
h3cVxlanID = _H3cVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 1),
    _H3cVxlanID_Type()
)
h3cVxlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVxlanID.setStatus("current")
_H3cVxlanAddrType_Type = InetAddressType
_H3cVxlanAddrType_Object = MibTableColumn
h3cVxlanAddrType = _H3cVxlanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 2),
    _H3cVxlanAddrType_Type()
)
h3cVxlanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanAddrType.setStatus("current")
_H3cVxlanGroupAddr_Type = InetAddress
_H3cVxlanGroupAddr_Object = MibTableColumn
h3cVxlanGroupAddr = _H3cVxlanGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 3),
    _H3cVxlanGroupAddr_Type()
)
h3cVxlanGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanGroupAddr.setStatus("current")
_H3cVxlanSourceAddr_Type = InetAddress
_H3cVxlanSourceAddr_Object = MibTableColumn
h3cVxlanSourceAddr = _H3cVxlanSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 4),
    _H3cVxlanSourceAddr_Type()
)
h3cVxlanSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanSourceAddr.setStatus("current")
_H3cVxlanVsiIndex_Type = Unsigned32
_H3cVxlanVsiIndex_Object = MibTableColumn
h3cVxlanVsiIndex = _H3cVxlanVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 5),
    _H3cVxlanVsiIndex_Type()
)
h3cVxlanVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanVsiIndex.setStatus("current")
_H3cVxlanRemoteMacCount_Type = Unsigned32
_H3cVxlanRemoteMacCount_Object = MibTableColumn
h3cVxlanRemoteMacCount = _H3cVxlanRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 6),
    _H3cVxlanRemoteMacCount_Type()
)
h3cVxlanRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanRemoteMacCount.setStatus("current")
_H3cVxlanRowStatus_Type = RowStatus
_H3cVxlanRowStatus_Object = MibTableColumn
h3cVxlanRowStatus = _H3cVxlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 2, 1, 7),
    _H3cVxlanRowStatus_Type()
)
h3cVxlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanRowStatus.setStatus("current")
_H3cVxlanTunnelTable_Object = MibTable
h3cVxlanTunnelTable = _H3cVxlanTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVxlanTunnelTable.setStatus("current")
_H3cVxlanTunnelEntry_Object = MibTableRow
h3cVxlanTunnelEntry = _H3cVxlanTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3, 1)
)
h3cVxlanTunnelEntry.setIndexNames(
    (0, "H3C-VXLAN-MIB", "h3cVxlanID"),
    (0, "H3C-VXLAN-MIB", "h3cVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    h3cVxlanTunnelEntry.setStatus("current")
_H3cVxlanTunnelID_Type = Unsigned32
_H3cVxlanTunnelID_Object = MibTableColumn
h3cVxlanTunnelID = _H3cVxlanTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3, 1, 1),
    _H3cVxlanTunnelID_Type()
)
h3cVxlanTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVxlanTunnelID.setStatus("current")
_H3cVxlanTunnelRowStatus_Type = RowStatus
_H3cVxlanTunnelRowStatus_Object = MibTableColumn
h3cVxlanTunnelRowStatus = _H3cVxlanTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3, 1, 2),
    _H3cVxlanTunnelRowStatus_Type()
)
h3cVxlanTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanTunnelRowStatus.setStatus("current")
_H3cVxlanTunnelOctets_Type = Counter64
_H3cVxlanTunnelOctets_Object = MibTableColumn
h3cVxlanTunnelOctets = _H3cVxlanTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3, 1, 3),
    _H3cVxlanTunnelOctets_Type()
)
h3cVxlanTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanTunnelOctets.setStatus("current")
_H3cVxlanTunnelPackets_Type = Counter64
_H3cVxlanTunnelPackets_Object = MibTableColumn
h3cVxlanTunnelPackets = _H3cVxlanTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 3, 1, 4),
    _H3cVxlanTunnelPackets_Type()
)
h3cVxlanTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanTunnelPackets.setStatus("current")
_H3cVxlanTunnelBoundTable_Object = MibTable
h3cVxlanTunnelBoundTable = _H3cVxlanTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 4)
)
if mibBuilder.loadTexts:
    h3cVxlanTunnelBoundTable.setStatus("current")
_H3cVxlanTunnelBoundEntry_Object = MibTableRow
h3cVxlanTunnelBoundEntry = _H3cVxlanTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 4, 1)
)
h3cVxlanTunnelBoundEntry.setIndexNames(
    (0, "H3C-VXLAN-MIB", "h3cVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    h3cVxlanTunnelBoundEntry.setStatus("current")
_H3cVxlanTunnelBoundVxlanNum_Type = Unsigned32
_H3cVxlanTunnelBoundVxlanNum_Object = MibTableColumn
h3cVxlanTunnelBoundVxlanNum = _H3cVxlanTunnelBoundVxlanNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 4, 1, 1),
    _H3cVxlanTunnelBoundVxlanNum_Type()
)
h3cVxlanTunnelBoundVxlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanTunnelBoundVxlanNum.setStatus("current")
_H3cVxlanMacTable_Object = MibTable
h3cVxlanMacTable = _H3cVxlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVxlanMacTable.setStatus("current")
_H3cVxlanMacEntry_Object = MibTableRow
h3cVxlanMacEntry = _H3cVxlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 5, 1)
)
h3cVxlanMacEntry.setIndexNames(
    (0, "H3C-VXLAN-MIB", "h3cVxlanVsiIndex"),
    (0, "H3C-VXLAN-MIB", "h3cVxlanMacAddr"),
)
if mibBuilder.loadTexts:
    h3cVxlanMacEntry.setStatus("current")
_H3cVxlanMacAddr_Type = MacAddress
_H3cVxlanMacAddr_Object = MibTableColumn
h3cVxlanMacAddr = _H3cVxlanMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 5, 1, 1),
    _H3cVxlanMacAddr_Type()
)
h3cVxlanMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVxlanMacAddr.setStatus("current")
_H3cVxlanMacTunnelID_Type = Unsigned32
_H3cVxlanMacTunnelID_Object = MibTableColumn
h3cVxlanMacTunnelID = _H3cVxlanMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 5, 1, 2),
    _H3cVxlanMacTunnelID_Type()
)
h3cVxlanMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanMacTunnelID.setStatus("current")


class _H3cVxlanMacType_Type(Integer32):
    """Custom type h3cVxlanMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("selfLearned", 1),
          ("staticConfigured", 2),
          ("protocolLearned", 3),
          ("openflow", 4),
          ("ovsdb", 5))
    )


_H3cVxlanMacType_Type.__name__ = "Integer32"
_H3cVxlanMacType_Object = MibTableColumn
h3cVxlanMacType = _H3cVxlanMacType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 5, 1, 3),
    _H3cVxlanMacType_Type()
)
h3cVxlanMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVxlanMacType.setStatus("current")
_H3cVxlanStaticMacTable_Object = MibTable
h3cVxlanStaticMacTable = _H3cVxlanStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 6)
)
if mibBuilder.loadTexts:
    h3cVxlanStaticMacTable.setStatus("current")
_H3cVxlanStaticMacEntry_Object = MibTableRow
h3cVxlanStaticMacEntry = _H3cVxlanStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 6, 1)
)
h3cVxlanStaticMacEntry.setIndexNames(
    (0, "H3C-VXLAN-MIB", "h3cVxlanVsiIndex"),
    (0, "H3C-VXLAN-MIB", "h3cVxlanStaticMacAddr"),
)
if mibBuilder.loadTexts:
    h3cVxlanStaticMacEntry.setStatus("current")
_H3cVxlanStaticMacAddr_Type = MacAddress
_H3cVxlanStaticMacAddr_Object = MibTableColumn
h3cVxlanStaticMacAddr = _H3cVxlanStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 6, 1, 1),
    _H3cVxlanStaticMacAddr_Type()
)
h3cVxlanStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVxlanStaticMacAddr.setStatus("current")
_H3cVxlanStaticMacTunnelID_Type = Unsigned32
_H3cVxlanStaticMacTunnelID_Object = MibTableColumn
h3cVxlanStaticMacTunnelID = _H3cVxlanStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 6, 1, 2),
    _H3cVxlanStaticMacTunnelID_Type()
)
h3cVxlanStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanStaticMacTunnelID.setStatus("current")
_H3cVxlanStaticMacRowStatus_Type = RowStatus
_H3cVxlanStaticMacRowStatus_Object = MibTableColumn
h3cVxlanStaticMacRowStatus = _H3cVxlanStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 150, 1, 6, 1, 3),
    _H3cVxlanStaticMacRowStatus_Type()
)
h3cVxlanStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVxlanStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VXLAN-MIB",
    **{"h3cVxlan": h3cVxlan,
       "h3cVxlanObjects": h3cVxlanObjects,
       "h3cVxlanScalarGroup": h3cVxlanScalarGroup,
       "h3cVxlanLocalMacNotify": h3cVxlanLocalMacNotify,
       "h3cVxlanRemoteMacLearn": h3cVxlanRemoteMacLearn,
       "h3cVxlanNextVxlanID": h3cVxlanNextVxlanID,
       "h3cVxlanConfigured": h3cVxlanConfigured,
       "h3cVxlanTable": h3cVxlanTable,
       "h3cVxlanEntry": h3cVxlanEntry,
       "h3cVxlanID": h3cVxlanID,
       "h3cVxlanAddrType": h3cVxlanAddrType,
       "h3cVxlanGroupAddr": h3cVxlanGroupAddr,
       "h3cVxlanSourceAddr": h3cVxlanSourceAddr,
       "h3cVxlanVsiIndex": h3cVxlanVsiIndex,
       "h3cVxlanRemoteMacCount": h3cVxlanRemoteMacCount,
       "h3cVxlanRowStatus": h3cVxlanRowStatus,
       "h3cVxlanTunnelTable": h3cVxlanTunnelTable,
       "h3cVxlanTunnelEntry": h3cVxlanTunnelEntry,
       "h3cVxlanTunnelID": h3cVxlanTunnelID,
       "h3cVxlanTunnelRowStatus": h3cVxlanTunnelRowStatus,
       "h3cVxlanTunnelOctets": h3cVxlanTunnelOctets,
       "h3cVxlanTunnelPackets": h3cVxlanTunnelPackets,
       "h3cVxlanTunnelBoundTable": h3cVxlanTunnelBoundTable,
       "h3cVxlanTunnelBoundEntry": h3cVxlanTunnelBoundEntry,
       "h3cVxlanTunnelBoundVxlanNum": h3cVxlanTunnelBoundVxlanNum,
       "h3cVxlanMacTable": h3cVxlanMacTable,
       "h3cVxlanMacEntry": h3cVxlanMacEntry,
       "h3cVxlanMacAddr": h3cVxlanMacAddr,
       "h3cVxlanMacTunnelID": h3cVxlanMacTunnelID,
       "h3cVxlanMacType": h3cVxlanMacType,
       "h3cVxlanStaticMacTable": h3cVxlanStaticMacTable,
       "h3cVxlanStaticMacEntry": h3cVxlanStaticMacEntry,
       "h3cVxlanStaticMacAddr": h3cVxlanStaticMacAddr,
       "h3cVxlanStaticMacTunnelID": h3cVxlanStaticMacTunnelID,
       "h3cVxlanStaticMacRowStatus": h3cVxlanStaticMacRowStatus}
)
