# SNMP MIB module (ALCATEL-ENT1-OSPF3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-OSPF3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:39 2025
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

(routingIND1Ospf3,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1Ospf3")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

(ospfv3AreaEntry,
 ospfv3IfEntry) = mibBuilder.importSymbols(
    "OSPFV3-MIB",
    "ospfv3AreaEntry",
    "ospfv3IfEntry")

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

alcatelIND1OSPF3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPF3MIB.setRevisions(
        ("2014-10-06 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OSPF3MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBObjects = _AlcatelIND1OSPF3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1)
)
_AlaProtocolOspf3_ObjectIdentity = ObjectIdentity
alaProtocolOspf3 = _AlaProtocolOspf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1)
)


class _AlaOspf3OrigRouteTag_Type(Unsigned32):
    """Custom type alaOspf3OrigRouteTag based on Unsigned32"""
    defaultValue = 0


_AlaOspf3OrigRouteTag_Type.__name__ = "Unsigned32"
_AlaOspf3OrigRouteTag_Object = MibScalar
alaOspf3OrigRouteTag = _AlaOspf3OrigRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 1),
    _AlaOspf3OrigRouteTag_Type()
)
alaOspf3OrigRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3OrigRouteTag.setStatus("current")


class _AlaOspf3TimerSpfDelay_Type(Integer32):
    """Custom type alaOspf3TimerSpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspf3TimerSpfDelay_Type.__name__ = "Integer32"
_AlaOspf3TimerSpfDelay_Object = MibScalar
alaOspf3TimerSpfDelay = _AlaOspf3TimerSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 2),
    _AlaOspf3TimerSpfDelay_Type()
)
alaOspf3TimerSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3TimerSpfDelay.setStatus("current")


class _AlaOspf3TimerSpfHold_Type(Integer32):
    """Custom type alaOspf3TimerSpfHold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspf3TimerSpfHold_Type.__name__ = "Integer32"
_AlaOspf3TimerSpfHold_Object = MibScalar
alaOspf3TimerSpfHold = _AlaOspf3TimerSpfHold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 3),
    _AlaOspf3TimerSpfHold_Type()
)
alaOspf3TimerSpfHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3TimerSpfHold.setStatus("current")


class _AlaOspf3RestartHelperSupport_Type(Integer32):
    """Custom type alaOspf3RestartHelperSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3RestartHelperSupport_Type.__name__ = "Integer32"
_AlaOspf3RestartHelperSupport_Object = MibScalar
alaOspf3RestartHelperSupport = _AlaOspf3RestartHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 4),
    _AlaOspf3RestartHelperSupport_Type()
)
alaOspf3RestartHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartHelperSupport.setStatus("current")


class _AlaOspf3RestartStrictLsaChecking_Type(Integer32):
    """Custom type alaOspf3RestartStrictLsaChecking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3RestartStrictLsaChecking_Type.__name__ = "Integer32"
_AlaOspf3RestartStrictLsaChecking_Object = MibScalar
alaOspf3RestartStrictLsaChecking = _AlaOspf3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 5),
    _AlaOspf3RestartStrictLsaChecking_Type()
)
alaOspf3RestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartStrictLsaChecking.setStatus("current")


class _AlaOspf3RestartInitiate_Type(Integer32):
    """Custom type alaOspf3RestartInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3RestartInitiate_Type.__name__ = "Integer32"
_AlaOspf3RestartInitiate_Object = MibScalar
alaOspf3RestartInitiate = _AlaOspf3RestartInitiate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 6),
    _AlaOspf3RestartInitiate_Type()
)
alaOspf3RestartInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartInitiate.setStatus("current")


class _AlaOspf3MTUCheck_Type(Integer32):
    """Custom type alaOspf3MTUCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3MTUCheck_Type.__name__ = "Integer32"
_AlaOspf3MTUCheck_Object = MibScalar
alaOspf3MTUCheck = _AlaOspf3MTUCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 7),
    _AlaOspf3MTUCheck_Type()
)
alaOspf3MTUCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3MTUCheck.setStatus("current")
_AlaOspf3RouteTable_Object = MibTable
alaOspf3RouteTable = _AlaOspf3RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaOspf3RouteTable.setStatus("current")
_AlaOspf3RouteEntry_Object = MibTableRow
alaOspf3RouteEntry = _AlaOspf3RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1)
)
alaOspf3RouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteDest"),
    (0, "ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RoutePfxLength"),
    (0, "ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteNextHop"),
    (0, "ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteIfIndex"),
)
if mibBuilder.loadTexts:
    alaOspf3RouteEntry.setStatus("current")
_AlaOspf3RouteDest_Type = Ipv6Address
_AlaOspf3RouteDest_Object = MibTableColumn
alaOspf3RouteDest = _AlaOspf3RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 1),
    _AlaOspf3RouteDest_Type()
)
alaOspf3RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOspf3RouteDest.setStatus("current")


class _AlaOspf3RoutePfxLength_Type(Integer32):
    """Custom type alaOspf3RoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaOspf3RoutePfxLength_Type.__name__ = "Integer32"
_AlaOspf3RoutePfxLength_Object = MibTableColumn
alaOspf3RoutePfxLength = _AlaOspf3RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 2),
    _AlaOspf3RoutePfxLength_Type()
)
alaOspf3RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOspf3RoutePfxLength.setStatus("current")
if mibBuilder.loadTexts:
    alaOspf3RoutePfxLength.setUnits("bits")
_AlaOspf3RouteNextHop_Type = Ipv6Address
_AlaOspf3RouteNextHop_Object = MibTableColumn
alaOspf3RouteNextHop = _AlaOspf3RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 3),
    _AlaOspf3RouteNextHop_Type()
)
alaOspf3RouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOspf3RouteNextHop.setStatus("current")
_AlaOspf3RouteIfIndex_Type = Ipv6IfIndexOrZero
_AlaOspf3RouteIfIndex_Object = MibTableColumn
alaOspf3RouteIfIndex = _AlaOspf3RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 4),
    _AlaOspf3RouteIfIndex_Type()
)
alaOspf3RouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOspf3RouteIfIndex.setStatus("current")


class _AlaOspf3RouteType_Type(Integer32):
    """Custom type alaOspf3RouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("other", 2))
    )


_AlaOspf3RouteType_Type.__name__ = "Integer32"
_AlaOspf3RouteType_Object = MibTableColumn
alaOspf3RouteType = _AlaOspf3RouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 5),
    _AlaOspf3RouteType_Type()
)
alaOspf3RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3RouteType.setStatus("current")


class _AlaOspf3RoutePathType_Type(Integer32):
    """Custom type alaOspf3RoutePathType based on Integer32"""
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
        *(("intraArea", 1),
          ("interArea", 2),
          ("externalType1", 3),
          ("externalType2", 4))
    )


_AlaOspf3RoutePathType_Type.__name__ = "Integer32"
_AlaOspf3RoutePathType_Object = MibTableColumn
alaOspf3RoutePathType = _AlaOspf3RoutePathType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 6),
    _AlaOspf3RoutePathType_Type()
)
alaOspf3RoutePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3RoutePathType.setStatus("current")
_AlaOspf3RouteMetric1_Type = Unsigned32
_AlaOspf3RouteMetric1_Object = MibTableColumn
alaOspf3RouteMetric1 = _AlaOspf3RouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 7),
    _AlaOspf3RouteMetric1_Type()
)
alaOspf3RouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3RouteMetric1.setStatus("current")
_AlaOspf3RouteMetric2_Type = Unsigned32
_AlaOspf3RouteMetric2_Object = MibTableColumn
alaOspf3RouteMetric2 = _AlaOspf3RouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 8),
    _AlaOspf3RouteMetric2_Type()
)
alaOspf3RouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3RouteMetric2.setStatus("current")


class _AlaOspf3BfdStatus_Type(Integer32):
    """Custom type alaOspf3BfdStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3BfdStatus_Type.__name__ = "Integer32"
_AlaOspf3BfdStatus_Object = MibScalar
alaOspf3BfdStatus = _AlaOspf3BfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 9),
    _AlaOspf3BfdStatus_Type()
)
alaOspf3BfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3BfdStatus.setStatus("current")


class _AlaOspf3BfdAllInterfaceStatus_Type(Integer32):
    """Custom type alaOspf3BfdAllInterfaceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3BfdAllInterfaceStatus_Type.__name__ = "Integer32"
_AlaOspf3BfdAllInterfaceStatus_Object = MibScalar
alaOspf3BfdAllInterfaceStatus = _AlaOspf3BfdAllInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 10),
    _AlaOspf3BfdAllInterfaceStatus_Type()
)
alaOspf3BfdAllInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3BfdAllInterfaceStatus.setStatus("current")
_AlaOspf3IfAugTable_Object = MibTable
alaOspf3IfAugTable = _AlaOspf3IfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaOspf3IfAugTable.setStatus("current")
_AlaOspf3IfAugEntry_Object = MibTableRow
alaOspf3IfAugEntry = _AlaOspf3IfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaOspf3IfAugEntry.setStatus("current")


class _AlaOspf3IfBfdStatus_Type(Integer32):
    """Custom type alaOspf3IfBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3IfBfdStatus_Type.__name__ = "Integer32"
_AlaOspf3IfBfdStatus_Object = MibTableColumn
alaOspf3IfBfdStatus = _AlaOspf3IfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1, 1),
    _AlaOspf3IfBfdStatus_Type()
)
alaOspf3IfBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspf3IfBfdStatus.setStatus("current")


class _AlaOspf3IfBfdDrsOnly_Type(Integer32):
    """Custom type alaOspf3IfBfdDrsOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaOspf3IfBfdDrsOnly_Type.__name__ = "Integer32"
_AlaOspf3IfBfdDrsOnly_Object = MibTableColumn
alaOspf3IfBfdDrsOnly = _AlaOspf3IfBfdDrsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1, 2),
    _AlaOspf3IfBfdDrsOnly_Type()
)
alaOspf3IfBfdDrsOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspf3IfBfdDrsOnly.setStatus("current")
_AlaOspf3AreaAugTable_Object = MibTable
alaOspf3AreaAugTable = _AlaOspf3AreaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaOspf3AreaAugTable.setStatus("current")
_AlaOspf3AreaAugEntry_Object = MibTableRow
alaOspf3AreaAugEntry = _AlaOspf3AreaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaOspf3AreaAugEntry.setStatus("current")
_AlaOspf3AreaRouterLsaCount_Type = Gauge32
_AlaOspf3AreaRouterLsaCount_Object = MibTableColumn
alaOspf3AreaRouterLsaCount = _AlaOspf3AreaRouterLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 1),
    _AlaOspf3AreaRouterLsaCount_Type()
)
alaOspf3AreaRouterLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaRouterLsaCount.setStatus("current")
_AlaOspf3AreaNetworkLsaCount_Type = Gauge32
_AlaOspf3AreaNetworkLsaCount_Object = MibTableColumn
alaOspf3AreaNetworkLsaCount = _AlaOspf3AreaNetworkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 2),
    _AlaOspf3AreaNetworkLsaCount_Type()
)
alaOspf3AreaNetworkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaNetworkLsaCount.setStatus("current")
_AlaOspf3AreaIntraAreaPrefixLsaCount_Type = Gauge32
_AlaOspf3AreaIntraAreaPrefixLsaCount_Object = MibTableColumn
alaOspf3AreaIntraAreaPrefixLsaCount = _AlaOspf3AreaIntraAreaPrefixLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 3),
    _AlaOspf3AreaIntraAreaPrefixLsaCount_Type()
)
alaOspf3AreaIntraAreaPrefixLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaIntraAreaPrefixLsaCount.setStatus("current")
_AlaOspf3AreaInterAreaPrefixLsaCount_Type = Gauge32
_AlaOspf3AreaInterAreaPrefixLsaCount_Object = MibTableColumn
alaOspf3AreaInterAreaPrefixLsaCount = _AlaOspf3AreaInterAreaPrefixLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 4),
    _AlaOspf3AreaInterAreaPrefixLsaCount_Type()
)
alaOspf3AreaInterAreaPrefixLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaInterAreaPrefixLsaCount.setStatus("current")
_AlaOspf3AreaInterAreaRouterLsaCount_Type = Gauge32
_AlaOspf3AreaInterAreaRouterLsaCount_Object = MibTableColumn
alaOspf3AreaInterAreaRouterLsaCount = _AlaOspf3AreaInterAreaRouterLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 5),
    _AlaOspf3AreaInterAreaRouterLsaCount_Type()
)
alaOspf3AreaInterAreaRouterLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaInterAreaRouterLsaCount.setStatus("current")
_AlaOspf3AreaHostCount_Type = Gauge32
_AlaOspf3AreaHostCount_Object = MibTableColumn
alaOspf3AreaHostCount = _AlaOspf3AreaHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 6),
    _AlaOspf3AreaHostCount_Type()
)
alaOspf3AreaHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaHostCount.setStatus("current")
_AlaOspf3AreaInterfaceCount_Type = Gauge32
_AlaOspf3AreaInterfaceCount_Object = MibTableColumn
alaOspf3AreaInterfaceCount = _AlaOspf3AreaInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 7),
    _AlaOspf3AreaInterfaceCount_Type()
)
alaOspf3AreaInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaInterfaceCount.setStatus("current")
_AlaOspf3AreaSummarizationRangeCount_Type = Gauge32
_AlaOspf3AreaSummarizationRangeCount_Object = MibTableColumn
alaOspf3AreaSummarizationRangeCount = _AlaOspf3AreaSummarizationRangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 8),
    _AlaOspf3AreaSummarizationRangeCount_Type()
)
alaOspf3AreaSummarizationRangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspf3AreaSummarizationRangeCount.setStatus("current")
_AlcatelIND1OSPF3MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBConformance = _AlcatelIND1OSPF3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2)
)
_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBCompliances = _AlcatelIND1OSPF3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 1)
)
_AlcatelIND1OSPF3MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBGroups = _AlcatelIND1OSPF3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2)
)
ospfv3IfEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF3-MIB",
     "alaOspf3IfAugEntry")
)
alaOspf3IfAugEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())
ospfv3AreaEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF3-MIB",
     "alaOspf3AreaAugEntry")
)
alaOspf3AreaAugEntry.setIndexNames(*ospfv3AreaEntry.getIndexNames())

# Managed Objects groups

alaOSPF3ConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 1)
)
alaOSPF3ConfigMIBGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3OrigRouteTag"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3TimerSpfDelay"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3TimerSpfHold"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RestartHelperSupport"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RestartStrictLsaChecking"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RestartInitiate"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3MTUCheck"))
)
if mibBuilder.loadTexts:
    alaOSPF3ConfigMIBGroup.setStatus("current")

alaOspf3RouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 2)
)
alaOspf3RouteGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteType"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RoutePathType"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteMetric1"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3RouteMetric2"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3BfdStatus"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3BfdAllInterfaceStatus"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3IfBfdDrsOnly"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3IfBfdStatus"))
)
if mibBuilder.loadTexts:
    alaOspf3RouteGroup.setStatus("current")

alaOspf3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 3)
)
alaOspf3AreaGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaRouterLsaCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaNetworkLsaCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaIntraAreaPrefixLsaCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaInterAreaPrefixLsaCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaInterAreaRouterLsaCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaHostCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaInterfaceCount"),
        ("ALCATEL-ENT1-OSPF3-MIB", "alaOspf3AreaSummarizationRangeCount"))
)
if mibBuilder.loadTexts:
    alaOspf3AreaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1OSPF3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 1, 1)
)
alcatelIND1OSPF3MIBCompliance.setObjects(
    ("ALCATEL-ENT1-OSPF3-MIB", "alaOSPF3ConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1OSPF3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-OSPF3-MIB",
    **{"alcatelIND1OSPF3MIB": alcatelIND1OSPF3MIB,
       "alcatelIND1OSPF3MIBObjects": alcatelIND1OSPF3MIBObjects,
       "alaProtocolOspf3": alaProtocolOspf3,
       "alaOspf3OrigRouteTag": alaOspf3OrigRouteTag,
       "alaOspf3TimerSpfDelay": alaOspf3TimerSpfDelay,
       "alaOspf3TimerSpfHold": alaOspf3TimerSpfHold,
       "alaOspf3RestartHelperSupport": alaOspf3RestartHelperSupport,
       "alaOspf3RestartStrictLsaChecking": alaOspf3RestartStrictLsaChecking,
       "alaOspf3RestartInitiate": alaOspf3RestartInitiate,
       "alaOspf3MTUCheck": alaOspf3MTUCheck,
       "alaOspf3RouteTable": alaOspf3RouteTable,
       "alaOspf3RouteEntry": alaOspf3RouteEntry,
       "alaOspf3RouteDest": alaOspf3RouteDest,
       "alaOspf3RoutePfxLength": alaOspf3RoutePfxLength,
       "alaOspf3RouteNextHop": alaOspf3RouteNextHop,
       "alaOspf3RouteIfIndex": alaOspf3RouteIfIndex,
       "alaOspf3RouteType": alaOspf3RouteType,
       "alaOspf3RoutePathType": alaOspf3RoutePathType,
       "alaOspf3RouteMetric1": alaOspf3RouteMetric1,
       "alaOspf3RouteMetric2": alaOspf3RouteMetric2,
       "alaOspf3BfdStatus": alaOspf3BfdStatus,
       "alaOspf3BfdAllInterfaceStatus": alaOspf3BfdAllInterfaceStatus,
       "alaOspf3IfAugTable": alaOspf3IfAugTable,
       "alaOspf3IfAugEntry": alaOspf3IfAugEntry,
       "alaOspf3IfBfdStatus": alaOspf3IfBfdStatus,
       "alaOspf3IfBfdDrsOnly": alaOspf3IfBfdDrsOnly,
       "alaOspf3AreaAugTable": alaOspf3AreaAugTable,
       "alaOspf3AreaAugEntry": alaOspf3AreaAugEntry,
       "alaOspf3AreaRouterLsaCount": alaOspf3AreaRouterLsaCount,
       "alaOspf3AreaNetworkLsaCount": alaOspf3AreaNetworkLsaCount,
       "alaOspf3AreaIntraAreaPrefixLsaCount": alaOspf3AreaIntraAreaPrefixLsaCount,
       "alaOspf3AreaInterAreaPrefixLsaCount": alaOspf3AreaInterAreaPrefixLsaCount,
       "alaOspf3AreaInterAreaRouterLsaCount": alaOspf3AreaInterAreaRouterLsaCount,
       "alaOspf3AreaHostCount": alaOspf3AreaHostCount,
       "alaOspf3AreaInterfaceCount": alaOspf3AreaInterfaceCount,
       "alaOspf3AreaSummarizationRangeCount": alaOspf3AreaSummarizationRangeCount,
       "alcatelIND1OSPF3MIBConformance": alcatelIND1OSPF3MIBConformance,
       "alcatelIND1OSPF3MIBCompliances": alcatelIND1OSPF3MIBCompliances,
       "alcatelIND1OSPF3MIBCompliance": alcatelIND1OSPF3MIBCompliance,
       "alcatelIND1OSPF3MIBGroups": alcatelIND1OSPF3MIBGroups,
       "alaOSPF3ConfigMIBGroup": alaOSPF3ConfigMIBGroup,
       "alaOspf3RouteGroup": alaOspf3RouteGroup,
       "alaOspf3AreaGroup": alaOspf3AreaGroup}
)
