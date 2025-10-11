# SNMP MIB module (IGMP-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/IGMP-PROXY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:46 2025
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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsigmpproxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124)
)
if mibBuilder.loadTexts:
    fsigmpproxy.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsigmpproxyStatus_ObjectIdentity = ObjectIdentity
fsigmpproxyStatus = _FsigmpproxyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 1)
)


class _FsIgmpProxyStatus_Type(Integer32):
    """Custom type fsIgmpProxyStatus based on Integer32"""
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


_FsIgmpProxyStatus_Type.__name__ = "Integer32"
_FsIgmpProxyStatus_Object = MibScalar
fsIgmpProxyStatus = _FsIgmpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 1, 1),
    _FsIgmpProxyStatus_Type()
)
fsIgmpProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpProxyStatus.setStatus("current")
_FsigmpproxyRtr_ObjectIdentity = ObjectIdentity
fsigmpproxyRtr = _FsigmpproxyRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2)
)
_FsIgmpProxyRtrIfaceTable_Object = MibTable
fsIgmpProxyRtrIfaceTable = _FsIgmpProxyRtrIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1)
)
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceTable.setStatus("current")
_FsIgmpProxyRtrIfaceEntry_Object = MibTableRow
fsIgmpProxyRtrIfaceEntry = _FsIgmpProxyRtrIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1)
)
fsIgmpProxyRtrIfaceEntry.setIndexNames(
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyRtrIfaceIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceEntry.setStatus("current")


class _FsIgmpProxyRtrIfaceIndex_Type(Integer32):
    """Custom type fsIgmpProxyRtrIfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsIgmpProxyRtrIfaceIndex_Type.__name__ = "Integer32"
_FsIgmpProxyRtrIfaceIndex_Object = MibTableColumn
fsIgmpProxyRtrIfaceIndex = _FsIgmpProxyRtrIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 1),
    _FsIgmpProxyRtrIfaceIndex_Type()
)
fsIgmpProxyRtrIfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceIndex.setStatus("current")


class _FsIgmpProxyRtrIfaceOperVersion_Type(Integer32):
    """Custom type fsIgmpProxyRtrIfaceOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsIgmpProxyRtrIfaceOperVersion_Type.__name__ = "Integer32"
_FsIgmpProxyRtrIfaceOperVersion_Object = MibTableColumn
fsIgmpProxyRtrIfaceOperVersion = _FsIgmpProxyRtrIfaceOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 2),
    _FsIgmpProxyRtrIfaceOperVersion_Type()
)
fsIgmpProxyRtrIfaceOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceOperVersion.setStatus("current")


class _FsIgmpProxyRtrIfaceCfgOperVersion_Type(Integer32):
    """Custom type fsIgmpProxyRtrIfaceCfgOperVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsIgmpProxyRtrIfaceCfgOperVersion_Type.__name__ = "Integer32"
_FsIgmpProxyRtrIfaceCfgOperVersion_Object = MibTableColumn
fsIgmpProxyRtrIfaceCfgOperVersion = _FsIgmpProxyRtrIfaceCfgOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 3),
    _FsIgmpProxyRtrIfaceCfgOperVersion_Type()
)
fsIgmpProxyRtrIfaceCfgOperVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceCfgOperVersion.setStatus("current")


class _FsIgmpProxyRtrIfacePurgeInterval_Type(Integer32):
    """Custom type fsIgmpProxyRtrIfacePurgeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_FsIgmpProxyRtrIfacePurgeInterval_Type.__name__ = "Integer32"
_FsIgmpProxyRtrIfacePurgeInterval_Object = MibTableColumn
fsIgmpProxyRtrIfacePurgeInterval = _FsIgmpProxyRtrIfacePurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 4),
    _FsIgmpProxyRtrIfacePurgeInterval_Type()
)
fsIgmpProxyRtrIfacePurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfacePurgeInterval.setStatus("current")
_FsIgmpProxyRtrIfaceUpTime_Type = TimeTicks
_FsIgmpProxyRtrIfaceUpTime_Object = MibTableColumn
fsIgmpProxyRtrIfaceUpTime = _FsIgmpProxyRtrIfaceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 5),
    _FsIgmpProxyRtrIfaceUpTime_Type()
)
fsIgmpProxyRtrIfaceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceUpTime.setStatus("current")
_FsIgmpProxyRtrIfaceExpiryTime_Type = TimeTicks
_FsIgmpProxyRtrIfaceExpiryTime_Object = MibTableColumn
fsIgmpProxyRtrIfaceExpiryTime = _FsIgmpProxyRtrIfaceExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 6),
    _FsIgmpProxyRtrIfaceExpiryTime_Type()
)
fsIgmpProxyRtrIfaceExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceExpiryTime.setStatus("current")
_FsIgmpProxyRtrIfaceRowStatus_Type = RowStatus
_FsIgmpProxyRtrIfaceRowStatus_Object = MibTableColumn
fsIgmpProxyRtrIfaceRowStatus = _FsIgmpProxyRtrIfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 2, 1, 1, 7),
    _FsIgmpProxyRtrIfaceRowStatus_Type()
)
fsIgmpProxyRtrIfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpProxyRtrIfaceRowStatus.setStatus("current")
_FsigmpproxyMRoute_ObjectIdentity = ObjectIdentity
fsigmpproxyMRoute = _FsigmpproxyMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3)
)
_FsIgmpProxyMrouteTable_Object = MibTable
fsIgmpProxyMrouteTable = _FsIgmpProxyMrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1)
)
if mibBuilder.loadTexts:
    fsIgmpProxyMrouteTable.setStatus("current")
_FsIgmpProxyMrouteEntry_Object = MibTableRow
fsIgmpProxyMrouteEntry = _FsIgmpProxyMrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1)
)
fsIgmpProxyMrouteEntry.setIndexNames(
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyMRouteSource"),
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyMRouteGroup"),
)
if mibBuilder.loadTexts:
    fsIgmpProxyMrouteEntry.setStatus("current")
_FsIgmpProxyMRouteSource_Type = IpAddress
_FsIgmpProxyMRouteSource_Object = MibTableColumn
fsIgmpProxyMRouteSource = _FsIgmpProxyMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1, 1),
    _FsIgmpProxyMRouteSource_Type()
)
fsIgmpProxyMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyMRouteSource.setStatus("current")
_FsIgmpProxyMRouteGroup_Type = IpAddress
_FsIgmpProxyMRouteGroup_Object = MibTableColumn
fsIgmpProxyMRouteGroup = _FsIgmpProxyMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1, 2),
    _FsIgmpProxyMRouteGroup_Type()
)
fsIgmpProxyMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyMRouteGroup.setStatus("current")
_FsIgmpProxyMRouteIifIndex_Type = Integer32
_FsIgmpProxyMRouteIifIndex_Object = MibTableColumn
fsIgmpProxyMRouteIifIndex = _FsIgmpProxyMRouteIifIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1, 3),
    _FsIgmpProxyMRouteIifIndex_Type()
)
fsIgmpProxyMRouteIifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyMRouteIifIndex.setStatus("current")
_FsIgmpProxyMRouteUpTime_Type = TimeTicks
_FsIgmpProxyMRouteUpTime_Object = MibTableColumn
fsIgmpProxyMRouteUpTime = _FsIgmpProxyMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1, 4),
    _FsIgmpProxyMRouteUpTime_Type()
)
fsIgmpProxyMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyMRouteUpTime.setStatus("current")
_FsIgmpProxyMRouteExpiryTime_Type = TimeTicks
_FsIgmpProxyMRouteExpiryTime_Object = MibTableColumn
fsIgmpProxyMRouteExpiryTime = _FsIgmpProxyMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 1, 1, 5),
    _FsIgmpProxyMRouteExpiryTime_Type()
)
fsIgmpProxyMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyMRouteExpiryTime.setStatus("current")
_FsIgmpProxyNextHopTable_Object = MibTable
fsIgmpProxyNextHopTable = _FsIgmpProxyNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2)
)
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopTable.setStatus("current")
_FsIgmpProxyNextHopEntry_Object = MibTableRow
fsIgmpProxyNextHopEntry = _FsIgmpProxyNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2, 1)
)
fsIgmpProxyNextHopEntry.setIndexNames(
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyNextHopSource"),
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyNextHopGroup"),
    (0, "IGMP-PROXY-MIB", "fsIgmpProxyNextHopIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopEntry.setStatus("current")
_FsIgmpProxyNextHopSource_Type = IpAddress
_FsIgmpProxyNextHopSource_Object = MibTableColumn
fsIgmpProxyNextHopSource = _FsIgmpProxyNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2, 1, 1),
    _FsIgmpProxyNextHopSource_Type()
)
fsIgmpProxyNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopSource.setStatus("current")
_FsIgmpProxyNextHopGroup_Type = IpAddress
_FsIgmpProxyNextHopGroup_Object = MibTableColumn
fsIgmpProxyNextHopGroup = _FsIgmpProxyNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2, 1, 2),
    _FsIgmpProxyNextHopGroup_Type()
)
fsIgmpProxyNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopGroup.setStatus("current")


class _FsIgmpProxyNextHopIndex_Type(Integer32):
    """Custom type fsIgmpProxyNextHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsIgmpProxyNextHopIndex_Type.__name__ = "Integer32"
_FsIgmpProxyNextHopIndex_Object = MibTableColumn
fsIgmpProxyNextHopIndex = _FsIgmpProxyNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2, 1, 3),
    _FsIgmpProxyNextHopIndex_Type()
)
fsIgmpProxyNextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopIndex.setStatus("current")


class _FsIgmpProxyNextHopState_Type(Integer32):
    """Custom type fsIgmpProxyNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("pruned", 2))
    )


_FsIgmpProxyNextHopState_Type.__name__ = "Integer32"
_FsIgmpProxyNextHopState_Object = MibTableColumn
fsIgmpProxyNextHopState = _FsIgmpProxyNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 3, 2, 1, 4),
    _FsIgmpProxyNextHopState_Type()
)
fsIgmpProxyNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyNextHopState.setStatus("current")
_IgmpproxyTrapsControl_ObjectIdentity = ObjectIdentity
igmpproxyTrapsControl = _IgmpproxyTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 5)
)
_FsIgmpProxyQuerierIfIndex_Type = Integer32
_FsIgmpProxyQuerierIfIndex_Object = MibScalar
fsIgmpProxyQuerierIfIndex = _FsIgmpProxyQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 5, 1),
    _FsIgmpProxyQuerierIfIndex_Type()
)
fsIgmpProxyQuerierIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyQuerierIfIndex.setStatus("current")
_FsIgmpProxyQuerierAddress_Type = IpAddress
_FsIgmpProxyQuerierAddress_Object = MibScalar
fsIgmpProxyQuerierAddress = _FsIgmpProxyQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 5, 2),
    _FsIgmpProxyQuerierAddress_Type()
)
fsIgmpProxyQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyQuerierAddress.setStatus("current")
_FsigmpproxyTraps_ObjectIdentity = ObjectIdentity
fsigmpproxyTraps = _FsigmpproxyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 6)
)
_FsigmpTraps_ObjectIdentity = ObjectIdentity
fsigmpTraps = _FsigmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 6, 0)
)
_FsigmpproxyScalars_ObjectIdentity = ObjectIdentity
fsigmpproxyScalars = _FsigmpproxyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 7)
)


class _FsIgmpProxyForwardingTblEntryCnt_Type(Integer32):
    """Custom type fsIgmpProxyForwardingTblEntryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIgmpProxyForwardingTblEntryCnt_Type.__name__ = "Integer32"
_FsIgmpProxyForwardingTblEntryCnt_Object = MibScalar
fsIgmpProxyForwardingTblEntryCnt = _FsIgmpProxyForwardingTblEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 7, 1),
    _FsIgmpProxyForwardingTblEntryCnt_Type()
)
fsIgmpProxyForwardingTblEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpProxyForwardingTblEntryCnt.setStatus("current")

# Managed Objects groups


# Notification objects

fsIgmpProxyQuerierPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 124, 6, 0, 1)
)
fsIgmpProxyQuerierPresent.setObjects(
      *(("IGMP-PROXY-MIB", "fsIgmpProxyQuerierIfIndex"),
        ("IGMP-PROXY-MIB", "fsIgmpProxyQuerierAddress"))
)
if mibBuilder.loadTexts:
    fsIgmpProxyQuerierPresent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGMP-PROXY-MIB",
    **{"fsigmpproxy": fsigmpproxy,
       "fsigmpproxyStatus": fsigmpproxyStatus,
       "fsIgmpProxyStatus": fsIgmpProxyStatus,
       "fsigmpproxyRtr": fsigmpproxyRtr,
       "fsIgmpProxyRtrIfaceTable": fsIgmpProxyRtrIfaceTable,
       "fsIgmpProxyRtrIfaceEntry": fsIgmpProxyRtrIfaceEntry,
       "fsIgmpProxyRtrIfaceIndex": fsIgmpProxyRtrIfaceIndex,
       "fsIgmpProxyRtrIfaceOperVersion": fsIgmpProxyRtrIfaceOperVersion,
       "fsIgmpProxyRtrIfaceCfgOperVersion": fsIgmpProxyRtrIfaceCfgOperVersion,
       "fsIgmpProxyRtrIfacePurgeInterval": fsIgmpProxyRtrIfacePurgeInterval,
       "fsIgmpProxyRtrIfaceUpTime": fsIgmpProxyRtrIfaceUpTime,
       "fsIgmpProxyRtrIfaceExpiryTime": fsIgmpProxyRtrIfaceExpiryTime,
       "fsIgmpProxyRtrIfaceRowStatus": fsIgmpProxyRtrIfaceRowStatus,
       "fsigmpproxyMRoute": fsigmpproxyMRoute,
       "fsIgmpProxyMrouteTable": fsIgmpProxyMrouteTable,
       "fsIgmpProxyMrouteEntry": fsIgmpProxyMrouteEntry,
       "fsIgmpProxyMRouteSource": fsIgmpProxyMRouteSource,
       "fsIgmpProxyMRouteGroup": fsIgmpProxyMRouteGroup,
       "fsIgmpProxyMRouteIifIndex": fsIgmpProxyMRouteIifIndex,
       "fsIgmpProxyMRouteUpTime": fsIgmpProxyMRouteUpTime,
       "fsIgmpProxyMRouteExpiryTime": fsIgmpProxyMRouteExpiryTime,
       "fsIgmpProxyNextHopTable": fsIgmpProxyNextHopTable,
       "fsIgmpProxyNextHopEntry": fsIgmpProxyNextHopEntry,
       "fsIgmpProxyNextHopSource": fsIgmpProxyNextHopSource,
       "fsIgmpProxyNextHopGroup": fsIgmpProxyNextHopGroup,
       "fsIgmpProxyNextHopIndex": fsIgmpProxyNextHopIndex,
       "fsIgmpProxyNextHopState": fsIgmpProxyNextHopState,
       "igmpproxyTrapsControl": igmpproxyTrapsControl,
       "fsIgmpProxyQuerierIfIndex": fsIgmpProxyQuerierIfIndex,
       "fsIgmpProxyQuerierAddress": fsIgmpProxyQuerierAddress,
       "fsigmpproxyTraps": fsigmpproxyTraps,
       "fsigmpTraps": fsigmpTraps,
       "fsIgmpProxyQuerierPresent": fsIgmpProxyQuerierPresent,
       "fsigmpproxyScalars": fsigmpproxyScalars,
       "fsIgmpProxyForwardingTblEntryCnt": fsIgmpProxyForwardingTblEntryCnt}
)
