# SNMP MIB module (RUCKUS-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/RUCKUS-VXLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:01 2025
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

ruckusVxlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49)
)
if mibBuilder.loadTexts:
    ruckusVxlanMIB.setRevisions(
        ("2021-10-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusVxlanObjects_ObjectIdentity = ObjectIdentity
ruckusVxlanObjects = _RuckusVxlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1)
)
_RuckusVxlanOverlayGateway_ObjectIdentity = ObjectIdentity
ruckusVxlanOverlayGateway = _RuckusVxlanOverlayGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1)
)
_RuckusVxlanOverlayGatewayTable_Object = MibTable
ruckusVxlanOverlayGatewayTable = _RuckusVxlanOverlayGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayTable.setStatus("current")
_RuckusVxlanOverlayGatewayEntry_Object = MibTableRow
ruckusVxlanOverlayGatewayEntry = _RuckusVxlanOverlayGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1)
)
ruckusVxlanOverlayGatewayEntry.setIndexNames(
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayName"),
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayEntry.setStatus("current")


class _RuckusVxlanOverlayGatewayName_Type(DisplayString):
    """Custom type ruckusVxlanOverlayGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuckusVxlanOverlayGatewayName_Type.__name__ = "DisplayString"
_RuckusVxlanOverlayGatewayName_Object = MibTableColumn
ruckusVxlanOverlayGatewayName = _RuckusVxlanOverlayGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 1),
    _RuckusVxlanOverlayGatewayName_Type()
)
ruckusVxlanOverlayGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayName.setStatus("current")


class _RuckusVxlanOverlayGatewayType_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("l2Extension", 1))
    )


_RuckusVxlanOverlayGatewayType_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewayType_Object = MibTableColumn
ruckusVxlanOverlayGatewayType = _RuckusVxlanOverlayGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 2),
    _RuckusVxlanOverlayGatewayType_Type()
)
ruckusVxlanOverlayGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayType.setStatus("current")
_RuckusVxlanOverlayGatewayLoopbackId_Type = Integer32
_RuckusVxlanOverlayGatewayLoopbackId_Object = MibTableColumn
ruckusVxlanOverlayGatewayLoopbackId = _RuckusVxlanOverlayGatewayLoopbackId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 3),
    _RuckusVxlanOverlayGatewayLoopbackId_Type()
)
ruckusVxlanOverlayGatewayLoopbackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayLoopbackId.setStatus("current")
_RuckusVxlanOverlayGatewayMappedVlans_Type = Integer32
_RuckusVxlanOverlayGatewayMappedVlans_Object = MibTableColumn
ruckusVxlanOverlayGatewayMappedVlans = _RuckusVxlanOverlayGatewayMappedVlans_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 4),
    _RuckusVxlanOverlayGatewayMappedVlans_Type()
)
ruckusVxlanOverlayGatewayMappedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayMappedVlans.setStatus("current")
_RuckusVxlanOverlayGatewayExtendedSites_Type = Integer32
_RuckusVxlanOverlayGatewayExtendedSites_Object = MibTableColumn
ruckusVxlanOverlayGatewayExtendedSites = _RuckusVxlanOverlayGatewayExtendedSites_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 5),
    _RuckusVxlanOverlayGatewayExtendedSites_Type()
)
ruckusVxlanOverlayGatewayExtendedSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayExtendedSites.setStatus("current")


class _RuckusVxlanOverlayGatewayRowStatus_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewayRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_RuckusVxlanOverlayGatewayRowStatus_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewayRowStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewayRowStatus = _RuckusVxlanOverlayGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 1, 1, 6),
    _RuckusVxlanOverlayGatewayRowStatus_Type()
)
ruckusVxlanOverlayGatewayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayRowStatus.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapTable_Object = MibTable
ruckusVxlanOverlayGatewayVlanMapTable = _RuckusVxlanOverlayGatewayVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapTable.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapEntry_Object = MibTableRow
ruckusVxlanOverlayGatewayVlanMapEntry = _RuckusVxlanOverlayGatewayVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1)
)
ruckusVxlanOverlayGatewayVlanMapEntry.setIndexNames(
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayVlanMapVlanId"),
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapEntry.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapVlanId_Type = Integer32
_RuckusVxlanOverlayGatewayVlanMapVlanId_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapVlanId = _RuckusVxlanOverlayGatewayVlanMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 1),
    _RuckusVxlanOverlayGatewayVlanMapVlanId_Type()
)
ruckusVxlanOverlayGatewayVlanMapVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapVlanId.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapVniId_Type = Integer32
_RuckusVxlanOverlayGatewayVlanMapVniId_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapVniId = _RuckusVxlanOverlayGatewayVlanMapVniId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 2),
    _RuckusVxlanOverlayGatewayVlanMapVniId_Type()
)
ruckusVxlanOverlayGatewayVlanMapVniId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapVniId.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapVfiId_Type = Integer32
_RuckusVxlanOverlayGatewayVlanMapVfiId_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapVfiId = _RuckusVxlanOverlayGatewayVlanMapVfiId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 3),
    _RuckusVxlanOverlayGatewayVlanMapVfiId_Type()
)
ruckusVxlanOverlayGatewayVlanMapVfiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapVfiId.setStatus("current")


class _RuckusVxlanOverlayGatewayVlanMapCrossConnect_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewayVlanMapCrossConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RuckusVxlanOverlayGatewayVlanMapCrossConnect_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewayVlanMapCrossConnect_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapCrossConnect = _RuckusVxlanOverlayGatewayVlanMapCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 4),
    _RuckusVxlanOverlayGatewayVlanMapCrossConnect_Type()
)
ruckusVxlanOverlayGatewayVlanMapCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapCrossConnect.setStatus("current")


class _RuckusVxlanOverlayGatewayVlanMapStatistics_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewayVlanMapStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RuckusVxlanOverlayGatewayVlanMapStatistics_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewayVlanMapStatistics_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapStatistics = _RuckusVxlanOverlayGatewayVlanMapStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 5),
    _RuckusVxlanOverlayGatewayVlanMapStatistics_Type()
)
ruckusVxlanOverlayGatewayVlanMapStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapStatistics.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapAccessPortCount_Type = Integer32
_RuckusVxlanOverlayGatewayVlanMapAccessPortCount_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapAccessPortCount = _RuckusVxlanOverlayGatewayVlanMapAccessPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 6),
    _RuckusVxlanOverlayGatewayVlanMapAccessPortCount_Type()
)
ruckusVxlanOverlayGatewayVlanMapAccessPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapAccessPortCount.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapExtendedSite_Type = Integer32
_RuckusVxlanOverlayGatewayVlanMapExtendedSite_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapExtendedSite = _RuckusVxlanOverlayGatewayVlanMapExtendedSite_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 7),
    _RuckusVxlanOverlayGatewayVlanMapExtendedSite_Type()
)
ruckusVxlanOverlayGatewayVlanMapExtendedSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapExtendedSite.setStatus("current")


class _RuckusVxlanOverlayGatewayVlanMapRowStatus_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewayVlanMapRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_RuckusVxlanOverlayGatewayVlanMapRowStatus_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewayVlanMapRowStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapRowStatus = _RuckusVxlanOverlayGatewayVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 8),
    _RuckusVxlanOverlayGatewayVlanMapRowStatus_Type()
)
ruckusVxlanOverlayGatewayVlanMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapRowStatus.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInUnicastPackets_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInUnicastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInUnicastPackets = _RuckusVxlanOverlayGatewayVlanMapInUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 9),
    _RuckusVxlanOverlayGatewayVlanMapInUnicastPackets_Type()
)
ruckusVxlanOverlayGatewayVlanMapInUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInUnicastPackets.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInUnicastBytes_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInUnicastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInUnicastBytes = _RuckusVxlanOverlayGatewayVlanMapInUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 10),
    _RuckusVxlanOverlayGatewayVlanMapInUnicastBytes_Type()
)
ruckusVxlanOverlayGatewayVlanMapInUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInUnicastBytes.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInMulticastPackets_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInMulticastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInMulticastPackets = _RuckusVxlanOverlayGatewayVlanMapInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 11),
    _RuckusVxlanOverlayGatewayVlanMapInMulticastPackets_Type()
)
ruckusVxlanOverlayGatewayVlanMapInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInMulticastPackets.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInMutlticastBytes_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInMutlticastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInMutlticastBytes = _RuckusVxlanOverlayGatewayVlanMapInMutlticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 12),
    _RuckusVxlanOverlayGatewayVlanMapInMutlticastBytes_Type()
)
ruckusVxlanOverlayGatewayVlanMapInMutlticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInMutlticastBytes.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInBroadcastPackets_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInBroadcastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInBroadcastPackets = _RuckusVxlanOverlayGatewayVlanMapInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 13),
    _RuckusVxlanOverlayGatewayVlanMapInBroadcastPackets_Type()
)
ruckusVxlanOverlayGatewayVlanMapInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInBroadcastPackets.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapInBroadcastBytes_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapInBroadcastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapInBroadcastBytes = _RuckusVxlanOverlayGatewayVlanMapInBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 14),
    _RuckusVxlanOverlayGatewayVlanMapInBroadcastBytes_Type()
)
ruckusVxlanOverlayGatewayVlanMapInBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapInBroadcastBytes.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapOutPackets_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapOutPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapOutPackets = _RuckusVxlanOverlayGatewayVlanMapOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 15),
    _RuckusVxlanOverlayGatewayVlanMapOutPackets_Type()
)
ruckusVxlanOverlayGatewayVlanMapOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapOutPackets.setStatus("current")
_RuckusVxlanOverlayGatewayVlanMapOutBytes_Type = Counter64
_RuckusVxlanOverlayGatewayVlanMapOutBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewayVlanMapOutBytes = _RuckusVxlanOverlayGatewayVlanMapOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 2, 1, 16),
    _RuckusVxlanOverlayGatewayVlanMapOutBytes_Type()
)
ruckusVxlanOverlayGatewayVlanMapOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewayVlanMapOutBytes.setStatus("current")
_RuckusVxlanOverlayGatewaySiteTable_Object = MibTable
ruckusVxlanOverlayGatewaySiteTable = _RuckusVxlanOverlayGatewaySiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteTable.setStatus("current")
_RuckusVxlanOverlayGatewaySiteEntry_Object = MibTableRow
ruckusVxlanOverlayGatewaySiteEntry = _RuckusVxlanOverlayGatewaySiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1)
)
ruckusVxlanOverlayGatewaySiteEntry.setIndexNames(
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewaySiteName"),
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteEntry.setStatus("current")


class _RuckusVxlanOverlayGatewaySiteName_Type(DisplayString):
    """Custom type ruckusVxlanOverlayGatewaySiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuckusVxlanOverlayGatewaySiteName_Type.__name__ = "DisplayString"
_RuckusVxlanOverlayGatewaySiteName_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteName = _RuckusVxlanOverlayGatewaySiteName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 1),
    _RuckusVxlanOverlayGatewaySiteName_Type()
)
ruckusVxlanOverlayGatewaySiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteName.setStatus("current")
_RuckusVxlanOverlayGatewaySiteIpAddress_Type = IpAddress
_RuckusVxlanOverlayGatewaySiteIpAddress_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteIpAddress = _RuckusVxlanOverlayGatewaySiteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 2),
    _RuckusVxlanOverlayGatewaySiteIpAddress_Type()
)
ruckusVxlanOverlayGatewaySiteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpAddress.setStatus("current")
_RuckusVxlanOverlayGatewaySiteStatus_Type = TruthValue
_RuckusVxlanOverlayGatewaySiteStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteStatus = _RuckusVxlanOverlayGatewaySiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 3),
    _RuckusVxlanOverlayGatewaySiteStatus_Type()
)
ruckusVxlanOverlayGatewaySiteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteStatus.setStatus("current")


class _RuckusVxlanOverlayGatewaySiteRowStatus_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewaySiteRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_RuckusVxlanOverlayGatewaySiteRowStatus_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewaySiteRowStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteRowStatus = _RuckusVxlanOverlayGatewaySiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 4),
    _RuckusVxlanOverlayGatewaySiteRowStatus_Type()
)
ruckusVxlanOverlayGatewaySiteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteRowStatus.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInUnicastPackets_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInUnicastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInUnicastPackets = _RuckusVxlanOverlayGatewaySiteInUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 5),
    _RuckusVxlanOverlayGatewaySiteInUnicastPackets_Type()
)
ruckusVxlanOverlayGatewaySiteInUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInUnicastPackets.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInUnicastBytes_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInUnicastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInUnicastBytes = _RuckusVxlanOverlayGatewaySiteInUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 6),
    _RuckusVxlanOverlayGatewaySiteInUnicastBytes_Type()
)
ruckusVxlanOverlayGatewaySiteInUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInUnicastBytes.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInMulticastPackets_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInMulticastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInMulticastPackets = _RuckusVxlanOverlayGatewaySiteInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 7),
    _RuckusVxlanOverlayGatewaySiteInMulticastPackets_Type()
)
ruckusVxlanOverlayGatewaySiteInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInMulticastPackets.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInMutlticastBytes_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInMutlticastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInMutlticastBytes = _RuckusVxlanOverlayGatewaySiteInMutlticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 8),
    _RuckusVxlanOverlayGatewaySiteInMutlticastBytes_Type()
)
ruckusVxlanOverlayGatewaySiteInMutlticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInMutlticastBytes.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInBroadcastPackets_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInBroadcastPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInBroadcastPackets = _RuckusVxlanOverlayGatewaySiteInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 9),
    _RuckusVxlanOverlayGatewaySiteInBroadcastPackets_Type()
)
ruckusVxlanOverlayGatewaySiteInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInBroadcastPackets.setStatus("current")
_RuckusVxlanOverlayGatewaySiteInBroadcastBytes_Type = Counter64
_RuckusVxlanOverlayGatewaySiteInBroadcastBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteInBroadcastBytes = _RuckusVxlanOverlayGatewaySiteInBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 10),
    _RuckusVxlanOverlayGatewaySiteInBroadcastBytes_Type()
)
ruckusVxlanOverlayGatewaySiteInBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteInBroadcastBytes.setStatus("current")
_RuckusVxlanOverlayGatewaySiteOutPackets_Type = Counter64
_RuckusVxlanOverlayGatewaySiteOutPackets_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteOutPackets = _RuckusVxlanOverlayGatewaySiteOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 11),
    _RuckusVxlanOverlayGatewaySiteOutPackets_Type()
)
ruckusVxlanOverlayGatewaySiteOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteOutPackets.setStatus("current")
_RuckusVxlanOverlayGatewaySiteOutBytes_Type = Counter64
_RuckusVxlanOverlayGatewaySiteOutBytes_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteOutBytes = _RuckusVxlanOverlayGatewaySiteOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 12),
    _RuckusVxlanOverlayGatewaySiteOutBytes_Type()
)
ruckusVxlanOverlayGatewaySiteOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteOutBytes.setStatus("current")
_RuckusVxlanOverlayGatewaySiteMonitoring_Type = TruthValue
_RuckusVxlanOverlayGatewaySiteMonitoring_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteMonitoring = _RuckusVxlanOverlayGatewaySiteMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 13),
    _RuckusVxlanOverlayGatewaySiteMonitoring_Type()
)
ruckusVxlanOverlayGatewaySiteMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteMonitoring.setStatus("current")
_RuckusVxlanOverlayGatewaySiteKeepAlive_Type = Integer32
_RuckusVxlanOverlayGatewaySiteKeepAlive_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteKeepAlive = _RuckusVxlanOverlayGatewaySiteKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 14),
    _RuckusVxlanOverlayGatewaySiteKeepAlive_Type()
)
ruckusVxlanOverlayGatewaySiteKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteKeepAlive.setStatus("current")
_RuckusVxlanOverlayGatewaySiteRetry_Type = Integer32
_RuckusVxlanOverlayGatewaySiteRetry_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteRetry = _RuckusVxlanOverlayGatewaySiteRetry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 3, 1, 15),
    _RuckusVxlanOverlayGatewaySiteRetry_Type()
)
ruckusVxlanOverlayGatewaySiteRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteRetry.setStatus("current")
_RuckusVxlanOverlayGatewaySiteExtVlanTable_Object = MibTable
ruckusVxlanOverlayGatewaySiteExtVlanTable = _RuckusVxlanOverlayGatewaySiteExtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteExtVlanTable.setStatus("current")
_RuckusVxlanOverlayGatewaySiteExtVlanEntry_Object = MibTableRow
ruckusVxlanOverlayGatewaySiteExtVlanEntry = _RuckusVxlanOverlayGatewaySiteExtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 4, 1)
)
ruckusVxlanOverlayGatewaySiteExtVlanEntry.setIndexNames(
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewaySiteName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewaySiteExtVlanId"),
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteExtVlanEntry.setStatus("current")
_RuckusVxlanOverlayGatewaySiteExtVlanId_Type = Integer32
_RuckusVxlanOverlayGatewaySiteExtVlanId_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteExtVlanId = _RuckusVxlanOverlayGatewaySiteExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 4, 1, 1),
    _RuckusVxlanOverlayGatewaySiteExtVlanId_Type()
)
ruckusVxlanOverlayGatewaySiteExtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteExtVlanId.setStatus("current")


class _RuckusVxlanOverlayGatewaySiteExtVlanRowStatus_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewaySiteExtVlanRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_RuckusVxlanOverlayGatewaySiteExtVlanRowStatus_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewaySiteExtVlanRowStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteExtVlanRowStatus = _RuckusVxlanOverlayGatewaySiteExtVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 4, 1, 2),
    _RuckusVxlanOverlayGatewaySiteExtVlanRowStatus_Type()
)
ruckusVxlanOverlayGatewaySiteExtVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteExtVlanRowStatus.setStatus("current")
_RuckusVxlanOverlayGatewaySiteIpListTable_Object = MibTable
ruckusVxlanOverlayGatewaySiteIpListTable = _RuckusVxlanOverlayGatewaySiteIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpListTable.setStatus("current")
_RuckusVxlanOverlayGatewaySiteIpListEntry_Object = MibTableRow
ruckusVxlanOverlayGatewaySiteIpListEntry = _RuckusVxlanOverlayGatewaySiteIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 5, 1)
)
ruckusVxlanOverlayGatewaySiteIpListEntry.setIndexNames(
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewayName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewaySiteName"),
    (0, "RUCKUS-VXLAN-MIB", "ruckusVxlanOverlayGatewaySiteIpListIpIndex"),
)
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpListEntry.setStatus("current")
_RuckusVxlanOverlayGatewaySiteIpListIpIndex_Type = Integer32
_RuckusVxlanOverlayGatewaySiteIpListIpIndex_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteIpListIpIndex = _RuckusVxlanOverlayGatewaySiteIpListIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 5, 1, 1),
    _RuckusVxlanOverlayGatewaySiteIpListIpIndex_Type()
)
ruckusVxlanOverlayGatewaySiteIpListIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpListIpIndex.setStatus("current")
_RuckusVxlanOverlayGatewaySiteIpListIpAddress_Type = IpAddress
_RuckusVxlanOverlayGatewaySiteIpListIpAddress_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteIpListIpAddress = _RuckusVxlanOverlayGatewaySiteIpListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 5, 1, 2),
    _RuckusVxlanOverlayGatewaySiteIpListIpAddress_Type()
)
ruckusVxlanOverlayGatewaySiteIpListIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpListIpAddress.setStatus("current")


class _RuckusVxlanOverlayGatewaySiteIpListRowStatus_Type(Integer32):
    """Custom type ruckusVxlanOverlayGatewaySiteIpListRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_RuckusVxlanOverlayGatewaySiteIpListRowStatus_Type.__name__ = "Integer32"
_RuckusVxlanOverlayGatewaySiteIpListRowStatus_Object = MibTableColumn
ruckusVxlanOverlayGatewaySiteIpListRowStatus = _RuckusVxlanOverlayGatewaySiteIpListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 49, 1, 1, 5, 1, 3),
    _RuckusVxlanOverlayGatewaySiteIpListRowStatus_Type()
)
ruckusVxlanOverlayGatewaySiteIpListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusVxlanOverlayGatewaySiteIpListRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-VXLAN-MIB",
    **{"ruckusVxlanMIB": ruckusVxlanMIB,
       "ruckusVxlanObjects": ruckusVxlanObjects,
       "ruckusVxlanOverlayGateway": ruckusVxlanOverlayGateway,
       "ruckusVxlanOverlayGatewayTable": ruckusVxlanOverlayGatewayTable,
       "ruckusVxlanOverlayGatewayEntry": ruckusVxlanOverlayGatewayEntry,
       "ruckusVxlanOverlayGatewayName": ruckusVxlanOverlayGatewayName,
       "ruckusVxlanOverlayGatewayType": ruckusVxlanOverlayGatewayType,
       "ruckusVxlanOverlayGatewayLoopbackId": ruckusVxlanOverlayGatewayLoopbackId,
       "ruckusVxlanOverlayGatewayMappedVlans": ruckusVxlanOverlayGatewayMappedVlans,
       "ruckusVxlanOverlayGatewayExtendedSites": ruckusVxlanOverlayGatewayExtendedSites,
       "ruckusVxlanOverlayGatewayRowStatus": ruckusVxlanOverlayGatewayRowStatus,
       "ruckusVxlanOverlayGatewayVlanMapTable": ruckusVxlanOverlayGatewayVlanMapTable,
       "ruckusVxlanOverlayGatewayVlanMapEntry": ruckusVxlanOverlayGatewayVlanMapEntry,
       "ruckusVxlanOverlayGatewayVlanMapVlanId": ruckusVxlanOverlayGatewayVlanMapVlanId,
       "ruckusVxlanOverlayGatewayVlanMapVniId": ruckusVxlanOverlayGatewayVlanMapVniId,
       "ruckusVxlanOverlayGatewayVlanMapVfiId": ruckusVxlanOverlayGatewayVlanMapVfiId,
       "ruckusVxlanOverlayGatewayVlanMapCrossConnect": ruckusVxlanOverlayGatewayVlanMapCrossConnect,
       "ruckusVxlanOverlayGatewayVlanMapStatistics": ruckusVxlanOverlayGatewayVlanMapStatistics,
       "ruckusVxlanOverlayGatewayVlanMapAccessPortCount": ruckusVxlanOverlayGatewayVlanMapAccessPortCount,
       "ruckusVxlanOverlayGatewayVlanMapExtendedSite": ruckusVxlanOverlayGatewayVlanMapExtendedSite,
       "ruckusVxlanOverlayGatewayVlanMapRowStatus": ruckusVxlanOverlayGatewayVlanMapRowStatus,
       "ruckusVxlanOverlayGatewayVlanMapInUnicastPackets": ruckusVxlanOverlayGatewayVlanMapInUnicastPackets,
       "ruckusVxlanOverlayGatewayVlanMapInUnicastBytes": ruckusVxlanOverlayGatewayVlanMapInUnicastBytes,
       "ruckusVxlanOverlayGatewayVlanMapInMulticastPackets": ruckusVxlanOverlayGatewayVlanMapInMulticastPackets,
       "ruckusVxlanOverlayGatewayVlanMapInMutlticastBytes": ruckusVxlanOverlayGatewayVlanMapInMutlticastBytes,
       "ruckusVxlanOverlayGatewayVlanMapInBroadcastPackets": ruckusVxlanOverlayGatewayVlanMapInBroadcastPackets,
       "ruckusVxlanOverlayGatewayVlanMapInBroadcastBytes": ruckusVxlanOverlayGatewayVlanMapInBroadcastBytes,
       "ruckusVxlanOverlayGatewayVlanMapOutPackets": ruckusVxlanOverlayGatewayVlanMapOutPackets,
       "ruckusVxlanOverlayGatewayVlanMapOutBytes": ruckusVxlanOverlayGatewayVlanMapOutBytes,
       "ruckusVxlanOverlayGatewaySiteTable": ruckusVxlanOverlayGatewaySiteTable,
       "ruckusVxlanOverlayGatewaySiteEntry": ruckusVxlanOverlayGatewaySiteEntry,
       "ruckusVxlanOverlayGatewaySiteName": ruckusVxlanOverlayGatewaySiteName,
       "ruckusVxlanOverlayGatewaySiteIpAddress": ruckusVxlanOverlayGatewaySiteIpAddress,
       "ruckusVxlanOverlayGatewaySiteStatus": ruckusVxlanOverlayGatewaySiteStatus,
       "ruckusVxlanOverlayGatewaySiteRowStatus": ruckusVxlanOverlayGatewaySiteRowStatus,
       "ruckusVxlanOverlayGatewaySiteInUnicastPackets": ruckusVxlanOverlayGatewaySiteInUnicastPackets,
       "ruckusVxlanOverlayGatewaySiteInUnicastBytes": ruckusVxlanOverlayGatewaySiteInUnicastBytes,
       "ruckusVxlanOverlayGatewaySiteInMulticastPackets": ruckusVxlanOverlayGatewaySiteInMulticastPackets,
       "ruckusVxlanOverlayGatewaySiteInMutlticastBytes": ruckusVxlanOverlayGatewaySiteInMutlticastBytes,
       "ruckusVxlanOverlayGatewaySiteInBroadcastPackets": ruckusVxlanOverlayGatewaySiteInBroadcastPackets,
       "ruckusVxlanOverlayGatewaySiteInBroadcastBytes": ruckusVxlanOverlayGatewaySiteInBroadcastBytes,
       "ruckusVxlanOverlayGatewaySiteOutPackets": ruckusVxlanOverlayGatewaySiteOutPackets,
       "ruckusVxlanOverlayGatewaySiteOutBytes": ruckusVxlanOverlayGatewaySiteOutBytes,
       "ruckusVxlanOverlayGatewaySiteMonitoring": ruckusVxlanOverlayGatewaySiteMonitoring,
       "ruckusVxlanOverlayGatewaySiteKeepAlive": ruckusVxlanOverlayGatewaySiteKeepAlive,
       "ruckusVxlanOverlayGatewaySiteRetry": ruckusVxlanOverlayGatewaySiteRetry,
       "ruckusVxlanOverlayGatewaySiteExtVlanTable": ruckusVxlanOverlayGatewaySiteExtVlanTable,
       "ruckusVxlanOverlayGatewaySiteExtVlanEntry": ruckusVxlanOverlayGatewaySiteExtVlanEntry,
       "ruckusVxlanOverlayGatewaySiteExtVlanId": ruckusVxlanOverlayGatewaySiteExtVlanId,
       "ruckusVxlanOverlayGatewaySiteExtVlanRowStatus": ruckusVxlanOverlayGatewaySiteExtVlanRowStatus,
       "ruckusVxlanOverlayGatewaySiteIpListTable": ruckusVxlanOverlayGatewaySiteIpListTable,
       "ruckusVxlanOverlayGatewaySiteIpListEntry": ruckusVxlanOverlayGatewaySiteIpListEntry,
       "ruckusVxlanOverlayGatewaySiteIpListIpIndex": ruckusVxlanOverlayGatewaySiteIpListIpIndex,
       "ruckusVxlanOverlayGatewaySiteIpListIpAddress": ruckusVxlanOverlayGatewaySiteIpListIpAddress,
       "ruckusVxlanOverlayGatewaySiteIpListRowStatus": ruckusVxlanOverlayGatewaySiteIpListRowStatus}
)
