# SNMP MIB module (MELLANOX-XSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-XSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:41 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(mellanoxXstp,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxXstp")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mellanoxXstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1)
)
if mibBuilder.loadTexts:
    mellanoxXstpMib.setRevisions(
        ("2017-07-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxXstpNotifications_ObjectIdentity = ObjectIdentity
mellanoxXstpNotifications = _MellanoxXstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 1)
)
_MellanoxXstpObjects_ObjectIdentity = ObjectIdentity
mellanoxXstpObjects = _MellanoxXstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2)
)
_MellanoxXstpTable_Object = MibTable
mellanoxXstpTable = _MellanoxXstpTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mellanoxXstpTable.setStatus("current")
_MellanoxXstpEntry_Object = MibTableRow
mellanoxXstpEntry = _MellanoxXstpEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1)
)
mellanoxXstpEntry.setIndexNames(
    (0, "MELLANOX-XSTP-MIB", "mellanoxXstpId"),
)
if mibBuilder.loadTexts:
    mellanoxXstpEntry.setStatus("current")


class _MellanoxXstpId_Type(Unsigned32):
    """Custom type mellanoxXstpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MellanoxXstpId_Type.__name__ = "Unsigned32"
_MellanoxXstpId_Object = MibTableColumn
mellanoxXstpId = _MellanoxXstpId_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 1),
    _MellanoxXstpId_Type()
)
mellanoxXstpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mellanoxXstpId.setStatus("current")
_MellanoxXstpBridgeId_Type = BridgeId
_MellanoxXstpBridgeId_Object = MibTableColumn
mellanoxXstpBridgeId = _MellanoxXstpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 2),
    _MellanoxXstpBridgeId_Type()
)
mellanoxXstpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpBridgeId.setStatus("current")
_MellanoxXstpDesignatedRoot_Type = BridgeId
_MellanoxXstpDesignatedRoot_Object = MibTableColumn
mellanoxXstpDesignatedRoot = _MellanoxXstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 3),
    _MellanoxXstpDesignatedRoot_Type()
)
mellanoxXstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpDesignatedRoot.setStatus("current")
_MellanoxXstpRootPathCost_Type = Integer32
_MellanoxXstpRootPathCost_Object = MibTableColumn
mellanoxXstpRootPathCost = _MellanoxXstpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 4),
    _MellanoxXstpRootPathCost_Type()
)
mellanoxXstpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpRootPathCost.setStatus("current")


class _MellanoxXstpRootPort_Type(Unsigned32):
    """Custom type mellanoxXstpRootPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MellanoxXstpRootPort_Type.__name__ = "Unsigned32"
_MellanoxXstpRootPort_Object = MibTableColumn
mellanoxXstpRootPort = _MellanoxXstpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 5),
    _MellanoxXstpRootPort_Type()
)
mellanoxXstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpRootPort.setStatus("current")


class _MellanoxXstpBridgePriority_Type(Integer32):
    """Custom type mellanoxXstpBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MellanoxXstpBridgePriority_Type.__name__ = "Integer32"
_MellanoxXstpBridgePriority_Object = MibTableColumn
mellanoxXstpBridgePriority = _MellanoxXstpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 6),
    _MellanoxXstpBridgePriority_Type()
)
mellanoxXstpBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpBridgePriority.setStatus("current")


class _MellanoxXstpVids0_Type(OctetString):
    """Custom type mellanoxXstpVids0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_MellanoxXstpVids0_Type.__name__ = "OctetString"
_MellanoxXstpVids0_Object = MibTableColumn
mellanoxXstpVids0 = _MellanoxXstpVids0_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 7),
    _MellanoxXstpVids0_Type()
)
mellanoxXstpVids0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpVids0.setStatus("current")


class _MellanoxXstpVids1_Type(OctetString):
    """Custom type mellanoxXstpVids1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_MellanoxXstpVids1_Type.__name__ = "OctetString"
_MellanoxXstpVids1_Object = MibTableColumn
mellanoxXstpVids1 = _MellanoxXstpVids1_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 8),
    _MellanoxXstpVids1_Type()
)
mellanoxXstpVids1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpVids1.setStatus("current")


class _MellanoxXstpVids2_Type(OctetString):
    """Custom type mellanoxXstpVids2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_MellanoxXstpVids2_Type.__name__ = "OctetString"
_MellanoxXstpVids2_Object = MibTableColumn
mellanoxXstpVids2 = _MellanoxXstpVids2_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 9),
    _MellanoxXstpVids2_Type()
)
mellanoxXstpVids2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpVids2.setStatus("current")


class _MellanoxXstpVids3_Type(OctetString):
    """Custom type mellanoxXstpVids3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_MellanoxXstpVids3_Type.__name__ = "OctetString"
_MellanoxXstpVids3_Object = MibTableColumn
mellanoxXstpVids3 = _MellanoxXstpVids3_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 1, 1, 10),
    _MellanoxXstpVids3_Type()
)
mellanoxXstpVids3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpVids3.setStatus("current")
_MellanoxXstpPortTable_Object = MibTable
mellanoxXstpPortTable = _MellanoxXstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mellanoxXstpPortTable.setStatus("current")
_MellanoxXstpPortEntry_Object = MibTableRow
mellanoxXstpPortEntry = _MellanoxXstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1)
)
mellanoxXstpPortEntry.setIndexNames(
    (0, "MELLANOX-XSTP-MIB", "mellanoxXstpPortMstId"),
    (0, "MELLANOX-XSTP-MIB", "mellanoxXstpPortNum"),
)
if mibBuilder.loadTexts:
    mellanoxXstpPortEntry.setStatus("current")


class _MellanoxXstpPortMstId_Type(Unsigned32):
    """Custom type mellanoxXstpPortMstId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MellanoxXstpPortMstId_Type.__name__ = "Unsigned32"
_MellanoxXstpPortMstId_Object = MibTableColumn
mellanoxXstpPortMstId = _MellanoxXstpPortMstId_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 1),
    _MellanoxXstpPortMstId_Type()
)
mellanoxXstpPortMstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mellanoxXstpPortMstId.setStatus("current")


class _MellanoxXstpPortNum_Type(Unsigned32):
    """Custom type mellanoxXstpPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MellanoxXstpPortNum_Type.__name__ = "Unsigned32"
_MellanoxXstpPortNum_Object = MibTableColumn
mellanoxXstpPortNum = _MellanoxXstpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 2),
    _MellanoxXstpPortNum_Type()
)
mellanoxXstpPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mellanoxXstpPortNum.setStatus("current")


class _MellanoxXstpPortState_Type(Integer32):
    """Custom type mellanoxXstpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("listening", 2),
          ("learning", 3),
          ("forwarding", 4),
          ("blocking", 5))
    )


_MellanoxXstpPortState_Type.__name__ = "Integer32"
_MellanoxXstpPortState_Object = MibTableColumn
mellanoxXstpPortState = _MellanoxXstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 3),
    _MellanoxXstpPortState_Type()
)
mellanoxXstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpPortState.setStatus("current")


class _MellanoxXstpPortPriority_Type(Integer32):
    """Custom type mellanoxXstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MellanoxXstpPortPriority_Type.__name__ = "Integer32"
_MellanoxXstpPortPriority_Object = MibTableColumn
mellanoxXstpPortPriority = _MellanoxXstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 4),
    _MellanoxXstpPortPriority_Type()
)
mellanoxXstpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpPortPriority.setStatus("current")


class _MellanoxXstpPortPathCost_Type(Integer32):
    """Custom type mellanoxXstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MellanoxXstpPortPathCost_Type.__name__ = "Integer32"
_MellanoxXstpPortPathCost_Object = MibTableColumn
mellanoxXstpPortPathCost = _MellanoxXstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 5),
    _MellanoxXstpPortPathCost_Type()
)
mellanoxXstpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpPortPathCost.setStatus("current")


class _MellanoxXstpPortRole_Type(Integer32):
    """Custom type mellanoxXstpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("alternate", 2),
          ("designated", 3),
          ("backup", 4),
          ("disabled", 5))
    )


_MellanoxXstpPortRole_Type.__name__ = "Integer32"
_MellanoxXstpPortRole_Object = MibTableColumn
mellanoxXstpPortRole = _MellanoxXstpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 2, 1, 6),
    _MellanoxXstpPortRole_Type()
)
mellanoxXstpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpPortRole.setStatus("current")
_MellanoxXstpVlanTable_Object = MibTable
mellanoxXstpVlanTable = _MellanoxXstpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mellanoxXstpVlanTable.setStatus("current")
_MellanoxXstpVlanEntry_Object = MibTableRow
mellanoxXstpVlanEntry = _MellanoxXstpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 3, 1)
)
mellanoxXstpVlanEntry.setIndexNames(
    (0, "MELLANOX-XSTP-MIB", "mellanoxXstpVlanId"),
)
if mibBuilder.loadTexts:
    mellanoxXstpVlanEntry.setStatus("current")


class _MellanoxXstpVlanId_Type(Unsigned32):
    """Custom type mellanoxXstpVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MellanoxXstpVlanId_Type.__name__ = "Unsigned32"
_MellanoxXstpVlanId_Object = MibTableColumn
mellanoxXstpVlanId = _MellanoxXstpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 3, 1, 1),
    _MellanoxXstpVlanId_Type()
)
mellanoxXstpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mellanoxXstpVlanId.setStatus("current")


class _MellanoxXstpVlanMstId_Type(Unsigned32):
    """Custom type mellanoxXstpVlanMstId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MellanoxXstpVlanMstId_Type.__name__ = "Unsigned32"
_MellanoxXstpVlanMstId_Object = MibTableColumn
mellanoxXstpVlanMstId = _MellanoxXstpVlanMstId_Object(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 2, 3, 1, 2),
    _MellanoxXstpVlanMstId_Type()
)
mellanoxXstpVlanMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxXstpVlanMstId.setStatus("current")

# Managed Objects groups


# Notification objects

mellanoxXstpRootBridgeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 1, 1)
)
mellanoxXstpRootBridgeChange.setObjects(
    ("MELLANOX-XSTP-MIB", "mellanoxXstpId")
)
if mibBuilder.loadTexts:
    mellanoxXstpRootBridgeChange.setStatus(
        "current"
    )

mellanoxXstpRootPortChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 1, 2)
)
mellanoxXstpRootPortChange.setObjects(
      *(("MELLANOX-XSTP-MIB", "mellanoxXstpId"),
        ("MELLANOX-XSTP-MIB", "mellanoxXstpPortNum"))
)
if mibBuilder.loadTexts:
    mellanoxXstpRootPortChange.setStatus(
        "current"
    )

mellanoxXstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 13, 1, 1, 3)
)
mellanoxXstpTopologyChange.setObjects(
      *(("MELLANOX-XSTP-MIB", "mellanoxXstpId"),
        ("MELLANOX-XSTP-MIB", "mellanoxXstpPortNum"),
        ("MELLANOX-XSTP-MIB", "mellanoxXstpPortState"))
)
if mibBuilder.loadTexts:
    mellanoxXstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-XSTP-MIB",
    **{"mellanoxXstpMib": mellanoxXstpMib,
       "mellanoxXstpNotifications": mellanoxXstpNotifications,
       "mellanoxXstpRootBridgeChange": mellanoxXstpRootBridgeChange,
       "mellanoxXstpRootPortChange": mellanoxXstpRootPortChange,
       "mellanoxXstpTopologyChange": mellanoxXstpTopologyChange,
       "mellanoxXstpObjects": mellanoxXstpObjects,
       "mellanoxXstpTable": mellanoxXstpTable,
       "mellanoxXstpEntry": mellanoxXstpEntry,
       "mellanoxXstpId": mellanoxXstpId,
       "mellanoxXstpBridgeId": mellanoxXstpBridgeId,
       "mellanoxXstpDesignatedRoot": mellanoxXstpDesignatedRoot,
       "mellanoxXstpRootPathCost": mellanoxXstpRootPathCost,
       "mellanoxXstpRootPort": mellanoxXstpRootPort,
       "mellanoxXstpBridgePriority": mellanoxXstpBridgePriority,
       "mellanoxXstpVids0": mellanoxXstpVids0,
       "mellanoxXstpVids1": mellanoxXstpVids1,
       "mellanoxXstpVids2": mellanoxXstpVids2,
       "mellanoxXstpVids3": mellanoxXstpVids3,
       "mellanoxXstpPortTable": mellanoxXstpPortTable,
       "mellanoxXstpPortEntry": mellanoxXstpPortEntry,
       "mellanoxXstpPortMstId": mellanoxXstpPortMstId,
       "mellanoxXstpPortNum": mellanoxXstpPortNum,
       "mellanoxXstpPortState": mellanoxXstpPortState,
       "mellanoxXstpPortPriority": mellanoxXstpPortPriority,
       "mellanoxXstpPortPathCost": mellanoxXstpPortPathCost,
       "mellanoxXstpPortRole": mellanoxXstpPortRole,
       "mellanoxXstpVlanTable": mellanoxXstpVlanTable,
       "mellanoxXstpVlanEntry": mellanoxXstpVlanEntry,
       "mellanoxXstpVlanId": mellanoxXstpVlanId,
       "mellanoxXstpVlanMstId": mellanoxXstpVlanMstId}
)
