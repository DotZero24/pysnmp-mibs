# SNMP MIB module (H3C-NVGRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-NVGRE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:55 2025
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

h3cNvgre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156)
)
if mibBuilder.loadTexts:
    h3cNvgre.setRevisions(
        ("2014-03-11 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cNvgreObjects_ObjectIdentity = ObjectIdentity
h3cNvgreObjects = _H3cNvgreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1)
)
_H3cNvgreScalarGroup_ObjectIdentity = ObjectIdentity
h3cNvgreScalarGroup = _H3cNvgreScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 1)
)
_H3cNvgreNextNvgreID_Type = Unsigned32
_H3cNvgreNextNvgreID_Object = MibScalar
h3cNvgreNextNvgreID = _H3cNvgreNextNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 1, 1),
    _H3cNvgreNextNvgreID_Type()
)
h3cNvgreNextNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreNextNvgreID.setStatus("current")
_H3cNvgreConfigured_Type = Unsigned32
_H3cNvgreConfigured_Object = MibScalar
h3cNvgreConfigured = _H3cNvgreConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 1, 2),
    _H3cNvgreConfigured_Type()
)
h3cNvgreConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreConfigured.setStatus("current")
_H3cNvgreTable_Object = MibTable
h3cNvgreTable = _H3cNvgreTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2)
)
if mibBuilder.loadTexts:
    h3cNvgreTable.setStatus("current")
_H3cNvgreEntry_Object = MibTableRow
h3cNvgreEntry = _H3cNvgreEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2, 1)
)
h3cNvgreEntry.setIndexNames(
    (0, "H3C-NVGRE-MIB", "h3cNvgreID"),
)
if mibBuilder.loadTexts:
    h3cNvgreEntry.setStatus("current")
_H3cNvgreID_Type = Unsigned32
_H3cNvgreID_Object = MibTableColumn
h3cNvgreID = _H3cNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2, 1, 1),
    _H3cNvgreID_Type()
)
h3cNvgreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNvgreID.setStatus("current")
_H3cNvgreVsiIndex_Type = Unsigned32
_H3cNvgreVsiIndex_Object = MibTableColumn
h3cNvgreVsiIndex = _H3cNvgreVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2, 1, 2),
    _H3cNvgreVsiIndex_Type()
)
h3cNvgreVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNvgreVsiIndex.setStatus("current")
_H3cNvgreRemoteMacCount_Type = Unsigned32
_H3cNvgreRemoteMacCount_Object = MibTableColumn
h3cNvgreRemoteMacCount = _H3cNvgreRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2, 1, 3),
    _H3cNvgreRemoteMacCount_Type()
)
h3cNvgreRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreRemoteMacCount.setStatus("current")
_H3cNvgreRowStatus_Type = RowStatus
_H3cNvgreRowStatus_Object = MibTableColumn
h3cNvgreRowStatus = _H3cNvgreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 2, 1, 4),
    _H3cNvgreRowStatus_Type()
)
h3cNvgreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNvgreRowStatus.setStatus("current")
_H3cNvgreTunnelTable_Object = MibTable
h3cNvgreTunnelTable = _H3cNvgreTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3)
)
if mibBuilder.loadTexts:
    h3cNvgreTunnelTable.setStatus("current")
_H3cNvgreTunnelEntry_Object = MibTableRow
h3cNvgreTunnelEntry = _H3cNvgreTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3, 1)
)
h3cNvgreTunnelEntry.setIndexNames(
    (0, "H3C-NVGRE-MIB", "h3cNvgreID"),
    (0, "H3C-NVGRE-MIB", "h3cNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    h3cNvgreTunnelEntry.setStatus("current")
_H3cNvgreTunnelID_Type = Unsigned32
_H3cNvgreTunnelID_Object = MibTableColumn
h3cNvgreTunnelID = _H3cNvgreTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3, 1, 1),
    _H3cNvgreTunnelID_Type()
)
h3cNvgreTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNvgreTunnelID.setStatus("current")
_H3cNvgreTunnelRowStatus_Type = RowStatus
_H3cNvgreTunnelRowStatus_Object = MibTableColumn
h3cNvgreTunnelRowStatus = _H3cNvgreTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3, 1, 2),
    _H3cNvgreTunnelRowStatus_Type()
)
h3cNvgreTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNvgreTunnelRowStatus.setStatus("current")
_H3cNvgreTunnelOctets_Type = Counter64
_H3cNvgreTunnelOctets_Object = MibTableColumn
h3cNvgreTunnelOctets = _H3cNvgreTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3, 1, 3),
    _H3cNvgreTunnelOctets_Type()
)
h3cNvgreTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreTunnelOctets.setStatus("current")
_H3cNvgreTunnelPackets_Type = Counter64
_H3cNvgreTunnelPackets_Object = MibTableColumn
h3cNvgreTunnelPackets = _H3cNvgreTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 3, 1, 4),
    _H3cNvgreTunnelPackets_Type()
)
h3cNvgreTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreTunnelPackets.setStatus("current")
_H3cNvgreTunnelBoundTable_Object = MibTable
h3cNvgreTunnelBoundTable = _H3cNvgreTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 4)
)
if mibBuilder.loadTexts:
    h3cNvgreTunnelBoundTable.setStatus("current")
_H3cNvgreTunnelBoundEntry_Object = MibTableRow
h3cNvgreTunnelBoundEntry = _H3cNvgreTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 4, 1)
)
h3cNvgreTunnelBoundEntry.setIndexNames(
    (0, "H3C-NVGRE-MIB", "h3cNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    h3cNvgreTunnelBoundEntry.setStatus("current")
_H3cNvgreTunnelBoundNvgreNum_Type = Unsigned32
_H3cNvgreTunnelBoundNvgreNum_Object = MibTableColumn
h3cNvgreTunnelBoundNvgreNum = _H3cNvgreTunnelBoundNvgreNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 4, 1, 1),
    _H3cNvgreTunnelBoundNvgreNum_Type()
)
h3cNvgreTunnelBoundNvgreNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreTunnelBoundNvgreNum.setStatus("current")
_H3cNvgreMacTable_Object = MibTable
h3cNvgreMacTable = _H3cNvgreMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 5)
)
if mibBuilder.loadTexts:
    h3cNvgreMacTable.setStatus("current")
_H3cNvgreMacEntry_Object = MibTableRow
h3cNvgreMacEntry = _H3cNvgreMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 5, 1)
)
h3cNvgreMacEntry.setIndexNames(
    (0, "H3C-NVGRE-MIB", "h3cNvgreVsiIndex"),
    (0, "H3C-NVGRE-MIB", "h3cNvgreMacAddr"),
)
if mibBuilder.loadTexts:
    h3cNvgreMacEntry.setStatus("current")
_H3cNvgreMacAddr_Type = MacAddress
_H3cNvgreMacAddr_Object = MibTableColumn
h3cNvgreMacAddr = _H3cNvgreMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 5, 1, 1),
    _H3cNvgreMacAddr_Type()
)
h3cNvgreMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNvgreMacAddr.setStatus("current")
_H3cNvgreMacTunnelID_Type = Unsigned32
_H3cNvgreMacTunnelID_Object = MibTableColumn
h3cNvgreMacTunnelID = _H3cNvgreMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 5, 1, 2),
    _H3cNvgreMacTunnelID_Type()
)
h3cNvgreMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreMacTunnelID.setStatus("current")


class _H3cNvgreMacType_Type(Integer32):
    """Custom type h3cNvgreMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("selfLearned", 1),
          ("staticConfigured", 2),
          ("protocolLearned", 3))
    )


_H3cNvgreMacType_Type.__name__ = "Integer32"
_H3cNvgreMacType_Object = MibTableColumn
h3cNvgreMacType = _H3cNvgreMacType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 5, 1, 3),
    _H3cNvgreMacType_Type()
)
h3cNvgreMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNvgreMacType.setStatus("current")
_H3cNvgreStaticMacTable_Object = MibTable
h3cNvgreStaticMacTable = _H3cNvgreStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 6)
)
if mibBuilder.loadTexts:
    h3cNvgreStaticMacTable.setStatus("current")
_H3cNvgreStaticMacEntry_Object = MibTableRow
h3cNvgreStaticMacEntry = _H3cNvgreStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 6, 1)
)
h3cNvgreStaticMacEntry.setIndexNames(
    (0, "H3C-NVGRE-MIB", "h3cNvgreVsiIndex"),
    (0, "H3C-NVGRE-MIB", "h3cNvgreStaticMacAddr"),
)
if mibBuilder.loadTexts:
    h3cNvgreStaticMacEntry.setStatus("current")
_H3cNvgreStaticMacAddr_Type = MacAddress
_H3cNvgreStaticMacAddr_Object = MibTableColumn
h3cNvgreStaticMacAddr = _H3cNvgreStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 6, 1, 1),
    _H3cNvgreStaticMacAddr_Type()
)
h3cNvgreStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNvgreStaticMacAddr.setStatus("current")
_H3cNvgreStaticMacTunnelID_Type = Unsigned32
_H3cNvgreStaticMacTunnelID_Object = MibTableColumn
h3cNvgreStaticMacTunnelID = _H3cNvgreStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 6, 1, 2),
    _H3cNvgreStaticMacTunnelID_Type()
)
h3cNvgreStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNvgreStaticMacTunnelID.setStatus("current")
_H3cNvgreStaticMacRowStatus_Type = RowStatus
_H3cNvgreStaticMacRowStatus_Object = MibTableColumn
h3cNvgreStaticMacRowStatus = _H3cNvgreStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 156, 1, 6, 1, 3),
    _H3cNvgreStaticMacRowStatus_Type()
)
h3cNvgreStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNvgreStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-NVGRE-MIB",
    **{"h3cNvgre": h3cNvgre,
       "h3cNvgreObjects": h3cNvgreObjects,
       "h3cNvgreScalarGroup": h3cNvgreScalarGroup,
       "h3cNvgreNextNvgreID": h3cNvgreNextNvgreID,
       "h3cNvgreConfigured": h3cNvgreConfigured,
       "h3cNvgreTable": h3cNvgreTable,
       "h3cNvgreEntry": h3cNvgreEntry,
       "h3cNvgreID": h3cNvgreID,
       "h3cNvgreVsiIndex": h3cNvgreVsiIndex,
       "h3cNvgreRemoteMacCount": h3cNvgreRemoteMacCount,
       "h3cNvgreRowStatus": h3cNvgreRowStatus,
       "h3cNvgreTunnelTable": h3cNvgreTunnelTable,
       "h3cNvgreTunnelEntry": h3cNvgreTunnelEntry,
       "h3cNvgreTunnelID": h3cNvgreTunnelID,
       "h3cNvgreTunnelRowStatus": h3cNvgreTunnelRowStatus,
       "h3cNvgreTunnelOctets": h3cNvgreTunnelOctets,
       "h3cNvgreTunnelPackets": h3cNvgreTunnelPackets,
       "h3cNvgreTunnelBoundTable": h3cNvgreTunnelBoundTable,
       "h3cNvgreTunnelBoundEntry": h3cNvgreTunnelBoundEntry,
       "h3cNvgreTunnelBoundNvgreNum": h3cNvgreTunnelBoundNvgreNum,
       "h3cNvgreMacTable": h3cNvgreMacTable,
       "h3cNvgreMacEntry": h3cNvgreMacEntry,
       "h3cNvgreMacAddr": h3cNvgreMacAddr,
       "h3cNvgreMacTunnelID": h3cNvgreMacTunnelID,
       "h3cNvgreMacType": h3cNvgreMacType,
       "h3cNvgreStaticMacTable": h3cNvgreStaticMacTable,
       "h3cNvgreStaticMacEntry": h3cNvgreStaticMacEntry,
       "h3cNvgreStaticMacAddr": h3cNvgreStaticMacAddr,
       "h3cNvgreStaticMacTunnelID": h3cNvgreStaticMacTunnelID,
       "h3cNvgreStaticMacRowStatus": h3cNvgreStaticMacRowStatus}
)
