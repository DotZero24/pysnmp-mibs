# SNMP MIB module (A3COM00xx-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/a3com/A3COM00xx-BRIDGE-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:28 2025
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

(a3ComBridgeExt,) = mibBuilder.importSymbols(
    "A3COM0004-GENERIC",
    "a3ComBridgeExt")

(MacAddress,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress",
    "Timeout",
    "dot1dBasePort")

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


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3ComDot1dExtended_ObjectIdentity = ObjectIdentity
a3ComDot1dExtended = _A3ComDot1dExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1)
)
_A3ComDot1dExtBase_ObjectIdentity = ObjectIdentity
a3ComDot1dExtBase = _A3ComDot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1)
)


class _A3ComDot1dGmrpAdminStatus_Type(Integer32):
    """Custom type a3ComDot1dGmrpAdminStatus based on Integer32"""
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


_A3ComDot1dGmrpAdminStatus_Type.__name__ = "Integer32"
_A3ComDot1dGmrpAdminStatus_Object = MibScalar
a3ComDot1dGmrpAdminStatus = _A3ComDot1dGmrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 1),
    _A3ComDot1dGmrpAdminStatus_Type()
)
a3ComDot1dGmrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDot1dGmrpAdminStatus.setStatus("mandatory")


class _A3ComDot1dGvrpAdminStatus_Type(Integer32):
    """Custom type a3ComDot1dGvrpAdminStatus based on Integer32"""
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


_A3ComDot1dGvrpAdminStatus_Type.__name__ = "Integer32"
_A3ComDot1dGvrpAdminStatus_Object = MibScalar
a3ComDot1dGvrpAdminStatus = _A3ComDot1dGvrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 2),
    _A3ComDot1dGvrpAdminStatus_Type()
)
a3ComDot1dGvrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDot1dGvrpAdminStatus.setStatus("mandatory")
_A3ComGarpJoinTime_Type = Timeout
_A3ComGarpJoinTime_Object = MibScalar
a3ComGarpJoinTime = _A3ComGarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 3),
    _A3ComGarpJoinTime_Type()
)
a3ComGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComGarpJoinTime.setStatus("mandatory")
_A3ComGarpLeaveTime_Type = Timeout
_A3ComGarpLeaveTime_Object = MibScalar
a3ComGarpLeaveTime = _A3ComGarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 4),
    _A3ComGarpLeaveTime_Type()
)
a3ComGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComGarpLeaveTime.setStatus("mandatory")
_A3ComGarpLeaveAllTime_Type = Timeout
_A3ComGarpLeaveAllTime_Object = MibScalar
a3ComGarpLeaveAllTime = _A3ComGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 5),
    _A3ComGarpLeaveAllTime_Type()
)
a3ComGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComGarpLeaveAllTime.setStatus("mandatory")


class _A3ComSingleFdbStatus_Type(Integer32):
    """Custom type a3ComSingleFdbStatus based on Integer32"""
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


_A3ComSingleFdbStatus_Type.__name__ = "Integer32"
_A3ComSingleFdbStatus_Object = MibScalar
a3ComSingleFdbStatus = _A3ComSingleFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 6),
    _A3ComSingleFdbStatus_Type()
)
a3ComSingleFdbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSingleFdbStatus.setStatus("mandatory")
_A3ComDot1dGarp_ObjectIdentity = ObjectIdentity
a3ComDot1dGarp = _A3ComDot1dGarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2)
)
_A3ComPortGarpTable_Object = MibTable
a3ComPortGarpTable = _A3ComPortGarpTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComPortGarpTable.setStatus("mandatory")
_A3ComPortGarpEntry_Object = MibTableRow
a3ComPortGarpEntry = _A3ComPortGarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1)
)
a3ComPortGarpEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    a3ComPortGarpEntry.setStatus("mandatory")


class _A3ComPortGmrpAdminStatus_Type(Integer32):
    """Custom type a3ComPortGmrpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("useDefault", 3))
    )


_A3ComPortGmrpAdminStatus_Type.__name__ = "Integer32"
_A3ComPortGmrpAdminStatus_Object = MibTableColumn
a3ComPortGmrpAdminStatus = _A3ComPortGmrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 1),
    _A3ComPortGmrpAdminStatus_Type()
)
a3ComPortGmrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortGmrpAdminStatus.setStatus("mandatory")


class _A3ComPortGmrpOperStatus_Type(Integer32):
    """Custom type a3ComPortGmrpOperStatus based on Integer32"""
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


_A3ComPortGmrpOperStatus_Type.__name__ = "Integer32"
_A3ComPortGmrpOperStatus_Object = MibTableColumn
a3ComPortGmrpOperStatus = _A3ComPortGmrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 2),
    _A3ComPortGmrpOperStatus_Type()
)
a3ComPortGmrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortGmrpOperStatus.setStatus("mandatory")


class _A3ComPortGvrpAdminStatus_Type(Integer32):
    """Custom type a3ComPortGvrpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("useDefault", 3))
    )


_A3ComPortGvrpAdminStatus_Type.__name__ = "Integer32"
_A3ComPortGvrpAdminStatus_Object = MibTableColumn
a3ComPortGvrpAdminStatus = _A3ComPortGvrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 3),
    _A3ComPortGvrpAdminStatus_Type()
)
a3ComPortGvrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortGvrpAdminStatus.setStatus("mandatory")


class _A3ComPortGvrpOperStatus_Type(Integer32):
    """Custom type a3ComPortGvrpOperStatus based on Integer32"""
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


_A3ComPortGvrpOperStatus_Type.__name__ = "Integer32"
_A3ComPortGvrpOperStatus_Object = MibTableColumn
a3ComPortGvrpOperStatus = _A3ComPortGvrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 4),
    _A3ComPortGvrpOperStatus_Type()
)
a3ComPortGvrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortGvrpOperStatus.setStatus("mandatory")
_A3ComPriority_ObjectIdentity = ObjectIdentity
a3ComPriority = _A3ComPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3)
)
_A3ComBridgePriorityTable_Object = MibTable
a3ComBridgePriorityTable = _A3ComBridgePriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1)
)
if mibBuilder.loadTexts:
    a3ComBridgePriorityTable.setStatus("mandatory")
_A3ComBridgePriorityEntry_Object = MibTableRow
a3ComBridgePriorityEntry = _A3ComBridgePriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1)
)
a3ComBridgePriorityEntry.setIndexNames(
    (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComUserPriority"),
)
if mibBuilder.loadTexts:
    a3ComBridgePriorityEntry.setStatus("mandatory")


class _A3ComUserPriority_Type(Integer32):
    """Custom type a3ComUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_A3ComUserPriority_Type.__name__ = "Integer32"
_A3ComUserPriority_Object = MibTableColumn
a3ComUserPriority = _A3ComUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 1),
    _A3ComUserPriority_Type()
)
a3ComUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComUserPriority.setStatus("mandatory")


class _A3ComBridgePriority_Type(Integer32):
    """Custom type a3ComBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_A3ComBridgePriority_Type.__name__ = "Integer32"
_A3ComBridgePriority_Object = MibTableColumn
a3ComBridgePriority = _A3ComBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 2),
    _A3ComBridgePriority_Type()
)
a3ComBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBridgePriority.setStatus("mandatory")
_A3ComNeighbour_ObjectIdentity = ObjectIdentity
a3ComNeighbour = _A3ComNeighbour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4)
)
_A3ComPortNeighbourTable_Object = MibTable
a3ComPortNeighbourTable = _A3ComPortNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1)
)
if mibBuilder.loadTexts:
    a3ComPortNeighbourTable.setStatus("mandatory")
_A3ComPortNeighbourEntry_Object = MibTableRow
a3ComPortNeighbourEntry = _A3ComPortNeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1)
)
a3ComPortNeighbourEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    a3ComPortNeighbourEntry.setStatus("mandatory")


class _A3ComPortForwardUnknownVlans_Type(Integer32):
    """Custom type a3ComPortForwardUnknownVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_A3ComPortForwardUnknownVlans_Type.__name__ = "Integer32"
_A3ComPortForwardUnknownVlans_Object = MibTableColumn
a3ComPortForwardUnknownVlans = _A3ComPortForwardUnknownVlans_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1, 1),
    _A3ComPortForwardUnknownVlans_Type()
)
a3ComPortForwardUnknownVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortForwardUnknownVlans.setStatus("mandatory")
_A3ComDot1qVlan_ObjectIdentity = ObjectIdentity
a3ComDot1qVlan = _A3ComDot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2)
)
_A3ComDot1qVlanStaticTable_Object = MibTable
a3ComDot1qVlanStaticTable = _A3ComDot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComDot1qVlanStaticTable.setStatus("mandatory")
_A3ComDot1qVlanStaticEntry_Object = MibTableRow
a3ComDot1qVlanStaticEntry = _A3ComDot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1)
)
a3ComDot1qVlanStaticEntry.setIndexNames(
    (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"),
)
if mibBuilder.loadTexts:
    a3ComDot1qVlanStaticEntry.setStatus("mandatory")


class _A3ComDot1qVlanId_Type(Integer32):
    """Custom type a3ComDot1qVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_A3ComDot1qVlanId_Type.__name__ = "Integer32"
_A3ComDot1qVlanId_Object = MibTableColumn
a3ComDot1qVlanId = _A3ComDot1qVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 1),
    _A3ComDot1qVlanId_Type()
)
a3ComDot1qVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComDot1qVlanId.setStatus("mandatory")
_A3ComDot1qVlanForbiddenPorts_Type = PortList
_A3ComDot1qVlanForbiddenPorts_Object = MibTableColumn
a3ComDot1qVlanForbiddenPorts = _A3ComDot1qVlanForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 2),
    _A3ComDot1qVlanForbiddenPorts_Type()
)
a3ComDot1qVlanForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDot1qVlanForbiddenPorts.setStatus("mandatory")
_A3ComDot1qTpGroupTable_Object = MibTable
a3ComDot1qTpGroupTable = _A3ComDot1qTpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupTable.setStatus("mandatory")
_A3ComDot1qTpGroupEntry_Object = MibTableRow
a3ComDot1qTpGroupEntry = _A3ComDot1qTpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1)
)
a3ComDot1qTpGroupEntry.setIndexNames(
    (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"),
    (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qTpGroupAddress"),
)
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupEntry.setStatus("mandatory")
_A3ComDot1qTpGroupAddress_Type = MacAddress
_A3ComDot1qTpGroupAddress_Object = MibTableColumn
a3ComDot1qTpGroupAddress = _A3ComDot1qTpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 1),
    _A3ComDot1qTpGroupAddress_Type()
)
a3ComDot1qTpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupAddress.setStatus("mandatory")
_A3ComDot1qTpGroupAllowedToGoTo_Type = PortList
_A3ComDot1qTpGroupAllowedToGoTo_Object = MibTableColumn
a3ComDot1qTpGroupAllowedToGoTo = _A3ComDot1qTpGroupAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 2),
    _A3ComDot1qTpGroupAllowedToGoTo_Type()
)
a3ComDot1qTpGroupAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupAllowedToGoTo.setStatus("mandatory")
_A3ComDot1qTpGroupGmrp_Type = PortList
_A3ComDot1qTpGroupGmrp_Object = MibTableColumn
a3ComDot1qTpGroupGmrp = _A3ComDot1qTpGroupGmrp_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 3),
    _A3ComDot1qTpGroupGmrp_Type()
)
a3ComDot1qTpGroupGmrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupGmrp.setStatus("mandatory")
_A3ComDot1qTpGroupIgmp_Type = PortList
_A3ComDot1qTpGroupIgmp_Object = MibTableColumn
a3ComDot1qTpGroupIgmp = _A3ComDot1qTpGroupIgmp_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 4),
    _A3ComDot1qTpGroupIgmp_Type()
)
a3ComDot1qTpGroupIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDot1qTpGroupIgmp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM00xx-BRIDGE-EXT-MIB",
    **{"PortList": PortList,
       "a3ComDot1dExtended": a3ComDot1dExtended,
       "a3ComDot1dExtBase": a3ComDot1dExtBase,
       "a3ComDot1dGmrpAdminStatus": a3ComDot1dGmrpAdminStatus,
       "a3ComDot1dGvrpAdminStatus": a3ComDot1dGvrpAdminStatus,
       "a3ComGarpJoinTime": a3ComGarpJoinTime,
       "a3ComGarpLeaveTime": a3ComGarpLeaveTime,
       "a3ComGarpLeaveAllTime": a3ComGarpLeaveAllTime,
       "a3ComSingleFdbStatus": a3ComSingleFdbStatus,
       "a3ComDot1dGarp": a3ComDot1dGarp,
       "a3ComPortGarpTable": a3ComPortGarpTable,
       "a3ComPortGarpEntry": a3ComPortGarpEntry,
       "a3ComPortGmrpAdminStatus": a3ComPortGmrpAdminStatus,
       "a3ComPortGmrpOperStatus": a3ComPortGmrpOperStatus,
       "a3ComPortGvrpAdminStatus": a3ComPortGvrpAdminStatus,
       "a3ComPortGvrpOperStatus": a3ComPortGvrpOperStatus,
       "a3ComPriority": a3ComPriority,
       "a3ComBridgePriorityTable": a3ComBridgePriorityTable,
       "a3ComBridgePriorityEntry": a3ComBridgePriorityEntry,
       "a3ComUserPriority": a3ComUserPriority,
       "a3ComBridgePriority": a3ComBridgePriority,
       "a3ComNeighbour": a3ComNeighbour,
       "a3ComPortNeighbourTable": a3ComPortNeighbourTable,
       "a3ComPortNeighbourEntry": a3ComPortNeighbourEntry,
       "a3ComPortForwardUnknownVlans": a3ComPortForwardUnknownVlans,
       "a3ComDot1qVlan": a3ComDot1qVlan,
       "a3ComDot1qVlanStaticTable": a3ComDot1qVlanStaticTable,
       "a3ComDot1qVlanStaticEntry": a3ComDot1qVlanStaticEntry,
       "a3ComDot1qVlanId": a3ComDot1qVlanId,
       "a3ComDot1qVlanForbiddenPorts": a3ComDot1qVlanForbiddenPorts,
       "a3ComDot1qTpGroupTable": a3ComDot1qTpGroupTable,
       "a3ComDot1qTpGroupEntry": a3ComDot1qTpGroupEntry,
       "a3ComDot1qTpGroupAddress": a3ComDot1qTpGroupAddress,
       "a3ComDot1qTpGroupAllowedToGoTo": a3ComDot1qTpGroupAllowedToGoTo,
       "a3ComDot1qTpGroupGmrp": a3ComDot1qTpGroupGmrp,
       "a3ComDot1qTpGroupIgmp": a3ComDot1qTpGroupIgmp}
)
