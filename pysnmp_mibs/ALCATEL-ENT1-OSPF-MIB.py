# SNMP MIB module (ALCATEL-ENT1-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:36 2025
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

(routingIND1Ospf,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1Ospf")

(ospfAreaAggregateEntry,
 ospfAreaEntry,
 ospfAreaId,
 ospfExtLsdbEntry,
 ospfIfEntry,
 ospfNbrEntry,
 ospfVirtIfEntry,
 ospfVirtNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAreaAggregateEntry",
    "ospfAreaEntry",
    "ospfAreaId",
    "ospfExtLsdbEntry",
    "ospfIfEntry",
    "ospfNbrEntry",
    "ospfVirtIfEntry",
    "ospfVirtNbrEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1OSPFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaAuthenticationEncryptKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OSPFMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBObjects = _AlcatelIND1OSPFMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBObjects.setStatus("current")
_AlaProtocolOspf_ObjectIdentity = ObjectIdentity
alaProtocolOspf = _AlaProtocolOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1)
)


class _AlaOspfRedistRouteTag_Type(Integer32):
    """Custom type alaOspfRedistRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRedistRouteTag_Type.__name__ = "Integer32"
_AlaOspfRedistRouteTag_Object = MibScalar
alaOspfRedistRouteTag = _AlaOspfRedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 2),
    _AlaOspfRedistRouteTag_Type()
)
alaOspfRedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteTag.setStatus("current")


class _AlaOspfTimerSpfDelay_Type(Integer32):
    """Custom type alaOspfTimerSpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfTimerSpfDelay_Type.__name__ = "Integer32"
_AlaOspfTimerSpfDelay_Object = MibScalar
alaOspfTimerSpfDelay = _AlaOspfTimerSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 3),
    _AlaOspfTimerSpfDelay_Type()
)
alaOspfTimerSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfTimerSpfDelay.setStatus("current")


class _AlaOspfTimerSpfHold_Type(Integer32):
    """Custom type alaOspfTimerSpfHold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfTimerSpfHold_Type.__name__ = "Integer32"
_AlaOspfTimerSpfHold_Object = MibScalar
alaOspfTimerSpfHold = _AlaOspfTimerSpfHold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 4),
    _AlaOspfTimerSpfHold_Type()
)
alaOspfTimerSpfHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfTimerSpfHold.setStatus("current")
_AlaOspfRouteNumber_Type = Counter32
_AlaOspfRouteNumber_Object = MibScalar
alaOspfRouteNumber = _AlaOspfRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 7),
    _AlaOspfRouteNumber_Type()
)
alaOspfRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteNumber.setStatus("current")


class _AlaOspfMTUCheck_Type(Integer32):
    """Custom type alaOspfMTUCheck based on Integer32"""
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


_AlaOspfMTUCheck_Type.__name__ = "Integer32"
_AlaOspfMTUCheck_Object = MibScalar
alaOspfMTUCheck = _AlaOspfMTUCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 8),
    _AlaOspfMTUCheck_Type()
)
alaOspfMTUCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfMTUCheck.setStatus("current")
_AlaOspfRouteTable_Object = MibTable
alaOspfRouteTable = _AlaOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaOspfRouteTable.setStatus("current")
_AlaOspfRouteEntry_Object = MibTableRow
alaOspfRouteEntry = _AlaOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1)
)
alaOspfRouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteDest"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteMask"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteTos"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaOspfRouteEntry.setStatus("current")


class _AlaOspfRouteDest_Type(IpAddress):
    """Custom type alaOspfRouteDest based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteDest_Type.__name__ = "IpAddress"
_AlaOspfRouteDest_Object = MibTableColumn
alaOspfRouteDest = _AlaOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 1),
    _AlaOspfRouteDest_Type()
)
alaOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteDest.setStatus("current")


class _AlaOspfRouteMask_Type(IpAddress):
    """Custom type alaOspfRouteMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteMask_Type.__name__ = "IpAddress"
_AlaOspfRouteMask_Object = MibTableColumn
alaOspfRouteMask = _AlaOspfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 2),
    _AlaOspfRouteMask_Type()
)
alaOspfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMask.setStatus("current")


class _AlaOspfRouteTos_Type(Integer32):
    """Custom type alaOspfRouteTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRouteTos_Type.__name__ = "Integer32"
_AlaOspfRouteTos_Object = MibTableColumn
alaOspfRouteTos = _AlaOspfRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 3),
    _AlaOspfRouteTos_Type()
)
alaOspfRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteTos.setStatus("current")


class _AlaOspfRouteNextHop_Type(IpAddress):
    """Custom type alaOspfRouteNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteNextHop_Type.__name__ = "IpAddress"
_AlaOspfRouteNextHop_Object = MibTableColumn
alaOspfRouteNextHop = _AlaOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 4),
    _AlaOspfRouteNextHop_Type()
)
alaOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteNextHop.setStatus("current")


class _AlaOspfRouteIfIndex_Type(Integer32):
    """Custom type alaOspfRouteIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AlaOspfRouteIfIndex_Type.__name__ = "Integer32"
_AlaOspfRouteIfIndex_Object = MibTableColumn
alaOspfRouteIfIndex = _AlaOspfRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 5),
    _AlaOspfRouteIfIndex_Type()
)
alaOspfRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteIfIndex.setStatus("current")


class _AlaOspfRouteType_Type(Integer32):
    """Custom type alaOspfRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("intraArea", 1),
          ("interArea", 2),
          ("externalType1", 3),
          ("externalType2", 4),
          ("nssaExternalType1", 5),
          ("nssaExternalType2", 6))
    )


_AlaOspfRouteType_Type.__name__ = "Integer32"
_AlaOspfRouteType_Object = MibTableColumn
alaOspfRouteType = _AlaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 6),
    _AlaOspfRouteType_Type()
)
alaOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteType.setStatus("current")


class _AlaOspfRouteAge_Type(TimeTicks):
    """Custom type alaOspfRouteAge based on TimeTicks"""
    defaultValue = 0


_AlaOspfRouteAge_Type.__name__ = "TimeTicks"
_AlaOspfRouteAge_Object = MibTableColumn
alaOspfRouteAge = _AlaOspfRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 7),
    _AlaOspfRouteAge_Type()
)
alaOspfRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteAge.setStatus("current")


class _AlaOspfRouteTag_Type(Integer32):
    """Custom type alaOspfRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRouteTag_Type.__name__ = "Integer32"
_AlaOspfRouteTag_Object = MibTableColumn
alaOspfRouteTag = _AlaOspfRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 8),
    _AlaOspfRouteTag_Type()
)
alaOspfRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteTag.setStatus("current")


class _AlaOspfRouteMetric1_Type(Integer32):
    """Custom type alaOspfRouteMetric1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRouteMetric1_Type.__name__ = "Integer32"
_AlaOspfRouteMetric1_Object = MibTableColumn
alaOspfRouteMetric1 = _AlaOspfRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 9),
    _AlaOspfRouteMetric1_Type()
)
alaOspfRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMetric1.setStatus("current")


class _AlaOspfRouteMetric2_Type(Integer32):
    """Custom type alaOspfRouteMetric2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRouteMetric2_Type.__name__ = "Integer32"
_AlaOspfRouteMetric2_Object = MibTableColumn
alaOspfRouteMetric2 = _AlaOspfRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 10),
    _AlaOspfRouteMetric2_Type()
)
alaOspfRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMetric2.setStatus("current")


class _AlaOspfRouteStatus_Type(RowStatus):
    """Custom type alaOspfRouteStatus based on RowStatus"""
    defaultValue = 2


_AlaOspfRouteStatus_Type.__name__ = "RowStatus"
_AlaOspfRouteStatus_Object = MibTableColumn
alaOspfRouteStatus = _AlaOspfRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 11),
    _AlaOspfRouteStatus_Type()
)
alaOspfRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteStatus.setStatus("current")
_AlaOspfBdrRouterTable_Object = MibTable
alaOspfBdrRouterTable = _AlaOspfBdrRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterTable.setStatus("current")
_AlaOspfBdrRouterEntry_Object = MibTableRow
alaOspfBdrRouterEntry = _AlaOspfBdrRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1)
)
alaOspfBdrRouterEntry.setIndexNames(
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterAreaId"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterId"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterTos"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterNextHop"),
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterEntry.setStatus("current")


class _AlaOspfBdrRouterAreaId_Type(IpAddress):
    """Custom type alaOspfBdrRouterAreaId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterAreaId_Type.__name__ = "IpAddress"
_AlaOspfBdrRouterAreaId_Object = MibTableColumn
alaOspfBdrRouterAreaId = _AlaOspfBdrRouterAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 1),
    _AlaOspfBdrRouterAreaId_Type()
)
alaOspfBdrRouterAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterAreaId.setStatus("current")


class _AlaOspfBdrRouterId_Type(IpAddress):
    """Custom type alaOspfBdrRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterId_Type.__name__ = "IpAddress"
_AlaOspfBdrRouterId_Object = MibTableColumn
alaOspfBdrRouterId = _AlaOspfBdrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 2),
    _AlaOspfBdrRouterId_Type()
)
alaOspfBdrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterId.setStatus("current")


class _AlaOspfBdrRouterTos_Type(Integer32):
    """Custom type alaOspfBdrRouterTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfBdrRouterTos_Type.__name__ = "Integer32"
_AlaOspfBdrRouterTos_Object = MibTableColumn
alaOspfBdrRouterTos = _AlaOspfBdrRouterTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 3),
    _AlaOspfBdrRouterTos_Type()
)
alaOspfBdrRouterTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterTos.setStatus("current")


class _AlaOspfBdrRouterNextHop_Type(IpAddress):
    """Custom type alaOspfBdrRouterNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterNextHop_Type.__name__ = "IpAddress"
_AlaOspfBdrRouterNextHop_Object = MibTableColumn
alaOspfBdrRouterNextHop = _AlaOspfBdrRouterNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 4),
    _AlaOspfBdrRouterNextHop_Type()
)
alaOspfBdrRouterNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterNextHop.setStatus("current")


class _AlaOspfBdrRouterIfIndex_Type(Integer32):
    """Custom type alaOspfBdrRouterIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfBdrRouterIfIndex_Type.__name__ = "Integer32"
_AlaOspfBdrRouterIfIndex_Object = MibTableColumn
alaOspfBdrRouterIfIndex = _AlaOspfBdrRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 5),
    _AlaOspfBdrRouterIfIndex_Type()
)
alaOspfBdrRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterIfIndex.setStatus("current")


class _AlaOspfBdrRouterType_Type(Integer32):
    """Custom type alaOspfBdrRouterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("asbr", 2),
          ("abrAsbr", 3))
    )


_AlaOspfBdrRouterType_Type.__name__ = "Integer32"
_AlaOspfBdrRouterType_Object = MibTableColumn
alaOspfBdrRouterType = _AlaOspfBdrRouterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 6),
    _AlaOspfBdrRouterType_Type()
)
alaOspfBdrRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterType.setStatus("current")


class _AlaOspfBdrRouterAge_Type(TimeTicks):
    """Custom type alaOspfBdrRouterAge based on TimeTicks"""
    defaultValue = 0


_AlaOspfBdrRouterAge_Type.__name__ = "TimeTicks"
_AlaOspfBdrRouterAge_Object = MibTableColumn
alaOspfBdrRouterAge = _AlaOspfBdrRouterAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 7),
    _AlaOspfBdrRouterAge_Type()
)
alaOspfBdrRouterAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterAge.setStatus("current")


class _AlaOspfBdrRouterMetric_Type(Integer32):
    """Custom type alaOspfBdrRouterMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfBdrRouterMetric_Type.__name__ = "Integer32"
_AlaOspfBdrRouterMetric_Object = MibTableColumn
alaOspfBdrRouterMetric = _AlaOspfBdrRouterMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 8),
    _AlaOspfBdrRouterMetric_Type()
)
alaOspfBdrRouterMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterMetric.setStatus("current")


class _AlaOspfBdrRouterStatus_Type(RowStatus):
    """Custom type alaOspfBdrRouterStatus based on RowStatus"""
    defaultValue = 2


_AlaOspfBdrRouterStatus_Type.__name__ = "RowStatus"
_AlaOspfBdrRouterStatus_Object = MibTableColumn
alaOspfBdrRouterStatus = _AlaOspfBdrRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 9),
    _AlaOspfBdrRouterStatus_Type()
)
alaOspfBdrRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterStatus.setStatus("current")
_AlaOspfIfMd5Table_Object = MibTable
alaOspfIfMd5Table = _AlaOspfIfMd5Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Table.setStatus("current")
_AlaOspfIfMd5Entry_Object = MibTableRow
alaOspfIfMd5Entry = _AlaOspfIfMd5Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1)
)
alaOspfIfMd5Entry.setIndexNames(
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5IpAddress"),
    (0, "ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyId"),
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Entry.setStatus("current")
_AlaOspfIfMd5IpAddress_Type = IpAddress
_AlaOspfIfMd5IpAddress_Object = MibTableColumn
alaOspfIfMd5IpAddress = _AlaOspfIfMd5IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 1),
    _AlaOspfIfMd5IpAddress_Type()
)
alaOspfIfMd5IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMd5IpAddress.setStatus("current")


class _AlaOspfIfMd5KeyId_Type(Integer32):
    """Custom type alaOspfIfMd5KeyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaOspfIfMd5KeyId_Type.__name__ = "Integer32"
_AlaOspfIfMd5KeyId_Object = MibTableColumn
alaOspfIfMd5KeyId = _AlaOspfIfMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 2),
    _AlaOspfIfMd5KeyId_Type()
)
alaOspfIfMd5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyId.setStatus("current")


class _AlaOspfIfMd5Key_Type(OctetString):
    """Custom type alaOspfIfMd5Key based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlaOspfIfMd5Key_Type.__name__ = "OctetString"
_AlaOspfIfMd5Key_Object = MibTableColumn
alaOspfIfMd5Key = _AlaOspfIfMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 3),
    _AlaOspfIfMd5Key_Type()
)
alaOspfIfMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5Key.setStatus("current")


class _AlaOspfIfMd5KeyStartAccept_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStartAccept based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStartAccept_Type.__name__ = "TimeTicks"
_AlaOspfIfMd5KeyStartAccept_Object = MibTableColumn
alaOspfIfMd5KeyStartAccept = _AlaOspfIfMd5KeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 4),
    _AlaOspfIfMd5KeyStartAccept_Type()
)
alaOspfIfMd5KeyStartAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStartAccept.setStatus("current")


class _AlaOspfIfMd5KeyStopAccept_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStopAccept based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStopAccept_Type.__name__ = "TimeTicks"
_AlaOspfIfMd5KeyStopAccept_Object = MibTableColumn
alaOspfIfMd5KeyStopAccept = _AlaOspfIfMd5KeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 5),
    _AlaOspfIfMd5KeyStopAccept_Type()
)
alaOspfIfMd5KeyStopAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStopAccept.setStatus("current")


class _AlaOspfIfMd5KeyStartGenerate_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStartGenerate based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStartGenerate_Type.__name__ = "TimeTicks"
_AlaOspfIfMd5KeyStartGenerate_Object = MibTableColumn
alaOspfIfMd5KeyStartGenerate = _AlaOspfIfMd5KeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 6),
    _AlaOspfIfMd5KeyStartGenerate_Type()
)
alaOspfIfMd5KeyStartGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStartGenerate.setStatus("current")


class _AlaOspfIfMd5KeyStopGenerate_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStopGenerate based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStopGenerate_Type.__name__ = "TimeTicks"
_AlaOspfIfMd5KeyStopGenerate_Object = MibTableColumn
alaOspfIfMd5KeyStopGenerate = _AlaOspfIfMd5KeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 7),
    _AlaOspfIfMd5KeyStopGenerate_Type()
)
alaOspfIfMd5KeyStopGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStopGenerate.setStatus("current")


class _AlaOspfIfMd5RowStatus_Type(RowStatus):
    """Custom type alaOspfIfMd5RowStatus based on RowStatus"""
    defaultValue = 2


_AlaOspfIfMd5RowStatus_Type.__name__ = "RowStatus"
_AlaOspfIfMd5RowStatus_Object = MibTableColumn
alaOspfIfMd5RowStatus = _AlaOspfIfMd5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 8),
    _AlaOspfIfMd5RowStatus_Type()
)
alaOspfIfMd5RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5RowStatus.setStatus("current")
_AlaOspfIfMd5EncryptKey_Type = AlaAuthenticationEncryptKey
_AlaOspfIfMd5EncryptKey_Object = MibTableColumn
alaOspfIfMd5EncryptKey = _AlaOspfIfMd5EncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 9),
    _AlaOspfIfMd5EncryptKey_Type()
)
alaOspfIfMd5EncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5EncryptKey.setStatus("current")


class _AlaOspfIfMd5AuthMode_Type(Integer32):
    """Custom type alaOspfIfMd5AuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keyedMd5", 1),
          ("hmacSha256", 2))
    )


_AlaOspfIfMd5AuthMode_Type.__name__ = "Integer32"
_AlaOspfIfMd5AuthMode_Object = MibTableColumn
alaOspfIfMd5AuthMode = _AlaOspfIfMd5AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 10),
    _AlaOspfIfMd5AuthMode_Type()
)
alaOspfIfMd5AuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfMd5AuthMode.setStatus("current")
_AlaOspfIfAugTable_Object = MibTable
alaOspfIfAugTable = _AlaOspfIfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaOspfIfAugTable.setStatus("current")
_AlaOspfIfAugEntry_Object = MibTableRow
alaOspfIfAugEntry = _AlaOspfIfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    alaOspfIfAugEntry.setStatus("current")
_AlaOspfIfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaOspfIfEncryptKey_Object = MibTableColumn
alaOspfIfEncryptKey = _AlaOspfIfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 1),
    _AlaOspfIfEncryptKey_Type()
)
alaOspfIfEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfEncryptKey.setStatus("current")
_AlaOspfIfIpMask_Type = IpAddress
_AlaOspfIfIpMask_Object = MibTableColumn
alaOspfIfIpMask = _AlaOspfIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 2),
    _AlaOspfIfIpMask_Type()
)
alaOspfIfIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfIpMask.setStatus("current")


class _AlaOspfIfVlanId_Type(Integer32):
    """Custom type alaOspfIfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_AlaOspfIfVlanId_Type.__name__ = "Integer32"
_AlaOspfIfVlanId_Object = MibTableColumn
alaOspfIfVlanId = _AlaOspfIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 3),
    _AlaOspfIfVlanId_Type()
)
alaOspfIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfVlanId.setStatus("current")
_AlaOspfIfDrRouterid_Type = IpAddress
_AlaOspfIfDrRouterid_Object = MibTableColumn
alaOspfIfDrRouterid = _AlaOspfIfDrRouterid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 4),
    _AlaOspfIfDrRouterid_Type()
)
alaOspfIfDrRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfDrRouterid.setStatus("current")
_AlaOspfIfBdrRouterid_Type = IpAddress
_AlaOspfIfBdrRouterid_Object = MibTableColumn
alaOspfIfBdrRouterid = _AlaOspfIfBdrRouterid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 5),
    _AlaOspfIfBdrRouterid_Type()
)
alaOspfIfBdrRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfBdrRouterid.setStatus("current")
_AlaOspfIfMTU_Type = Counter32
_AlaOspfIfMTU_Object = MibTableColumn
alaOspfIfMTU = _AlaOspfIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 6),
    _AlaOspfIfMTU_Type()
)
alaOspfIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMTU.setStatus("current")
_AlaOspfIfInitNbrs_Type = Counter32
_AlaOspfIfInitNbrs_Object = MibTableColumn
alaOspfIfInitNbrs = _AlaOspfIfInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 7),
    _AlaOspfIfInitNbrs_Type()
)
alaOspfIfInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfInitNbrs.setStatus("current")
_AlaOspfIfExchNbrs_Type = Counter32
_AlaOspfIfExchNbrs_Object = MibTableColumn
alaOspfIfExchNbrs = _AlaOspfIfExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 8),
    _AlaOspfIfExchNbrs_Type()
)
alaOspfIfExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfExchNbrs.setStatus("current")
_AlaOspfIfFullNbrs_Type = Counter32
_AlaOspfIfFullNbrs_Object = MibTableColumn
alaOspfIfFullNbrs = _AlaOspfIfFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 9),
    _AlaOspfIfFullNbrs_Type()
)
alaOspfIfFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfFullNbrs.setStatus("current")


class _AlaOspfIfLinkType_Type(Integer32):
    """Custom type alaOspfIfLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("broadcast", 1)
    )


_AlaOspfIfLinkType_Type.__name__ = "Integer32"
_AlaOspfIfLinkType_Object = MibTableColumn
alaOspfIfLinkType = _AlaOspfIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 10),
    _AlaOspfIfLinkType_Type()
)
alaOspfIfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfLinkType.setStatus("current")


class _AlaOspfIfOperStatus_Type(Integer32):
    """Custom type alaOspfIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AlaOspfIfOperStatus_Type.__name__ = "Integer32"
_AlaOspfIfOperStatus_Object = MibTableColumn
alaOspfIfOperStatus = _AlaOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 11),
    _AlaOspfIfOperStatus_Type()
)
alaOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfOperStatus.setStatus("current")
_AlaOspfIfIntfName_Type = SnmpAdminString
_AlaOspfIfIntfName_Object = MibTableColumn
alaOspfIfIntfName = _AlaOspfIfIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 12),
    _AlaOspfIfIntfName_Type()
)
alaOspfIfIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfIntfName.setStatus("current")
_AlaOspfIf2WayNbrs_Type = Counter32
_AlaOspfIf2WayNbrs_Object = MibTableColumn
alaOspfIf2WayNbrs = _AlaOspfIf2WayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 13),
    _AlaOspfIf2WayNbrs_Type()
)
alaOspfIf2WayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIf2WayNbrs.setStatus("current")


class _AlaOspfIfBfdStatus_Type(Integer32):
    """Custom type alaOspfIfBfdStatus based on Integer32"""
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


_AlaOspfIfBfdStatus_Type.__name__ = "Integer32"
_AlaOspfIfBfdStatus_Object = MibTableColumn
alaOspfIfBfdStatus = _AlaOspfIfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 14),
    _AlaOspfIfBfdStatus_Type()
)
alaOspfIfBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfBfdStatus.setStatus("current")


class _AlaOspfIfBfdDrsOnly_Type(Integer32):
    """Custom type alaOspfIfBfdDrsOnly based on Integer32"""
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


_AlaOspfIfBfdDrsOnly_Type.__name__ = "Integer32"
_AlaOspfIfBfdDrsOnly_Object = MibTableColumn
alaOspfIfBfdDrsOnly = _AlaOspfIfBfdDrsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 15),
    _AlaOspfIfBfdDrsOnly_Type()
)
alaOspfIfBfdDrsOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfBfdDrsOnly.setStatus("current")
_AlaOspfVirtIfAugTable_Object = MibTable
alaOspfVirtIfAugTable = _AlaOspfVirtIfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaOspfVirtIfAugTable.setStatus("current")
_AlaOspfVirtIfAugEntry_Object = MibTableRow
alaOspfVirtIfAugEntry = _AlaOspfVirtIfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    alaOspfVirtIfAugEntry.setStatus("current")
_AlaOspfVirtIfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaOspfVirtIfEncryptKey_Object = MibTableColumn
alaOspfVirtIfEncryptKey = _AlaOspfVirtIfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1, 1),
    _AlaOspfVirtIfEncryptKey_Type()
)
alaOspfVirtIfEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfVirtIfEncryptKey.setStatus("current")


class _AlaOspfVirtIfOperStatus_Type(Integer32):
    """Custom type alaOspfVirtIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AlaOspfVirtIfOperStatus_Type.__name__ = "Integer32"
_AlaOspfVirtIfOperStatus_Object = MibTableColumn
alaOspfVirtIfOperStatus = _AlaOspfVirtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1, 2),
    _AlaOspfVirtIfOperStatus_Type()
)
alaOspfVirtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtIfOperStatus.setStatus("current")


class _AlaOspfRestartHelperSupport_Type(Integer32):
    """Custom type alaOspfRestartHelperSupport based on Integer32"""
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


_AlaOspfRestartHelperSupport_Type.__name__ = "Integer32"
_AlaOspfRestartHelperSupport_Object = MibScalar
alaOspfRestartHelperSupport = _AlaOspfRestartHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 19),
    _AlaOspfRestartHelperSupport_Type()
)
alaOspfRestartHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartHelperSupport.setStatus("deprecated")


class _AlaOspfRestartHelperStrictLSAChecking_Type(Integer32):
    """Custom type alaOspfRestartHelperStrictLSAChecking based on Integer32"""
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


_AlaOspfRestartHelperStrictLSAChecking_Type.__name__ = "Integer32"
_AlaOspfRestartHelperStrictLSAChecking_Object = MibScalar
alaOspfRestartHelperStrictLSAChecking = _AlaOspfRestartHelperStrictLSAChecking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 20),
    _AlaOspfRestartHelperStrictLSAChecking_Type()
)
alaOspfRestartHelperStrictLSAChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartHelperStrictLSAChecking.setStatus("deprecated")


class _AlaOspfRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 1),
          ("notHelping", 2))
    )


_AlaOspfRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfRestartHelperStatus_Object = MibScalar
alaOspfRestartHelperStatus = _AlaOspfRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 21),
    _AlaOspfRestartHelperStatus_Type()
)
alaOspfRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartHelperStatus.setStatus("current")
_AlaOspfRFC1583Compatibility_Type = TruthValue
_AlaOspfRFC1583Compatibility_Object = MibScalar
alaOspfRFC1583Compatibility = _AlaOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 22),
    _AlaOspfRFC1583Compatibility_Type()
)
alaOspfRFC1583Compatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRFC1583Compatibility.setStatus("deprecated")
_AlaOspfOpaqueLsaSupport_Type = TruthValue
_AlaOspfOpaqueLsaSupport_Object = MibScalar
alaOspfOpaqueLsaSupport = _AlaOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 23),
    _AlaOspfOpaqueLsaSupport_Type()
)
alaOspfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfOpaqueLsaSupport.setStatus("current")
_AlaOspfTrafficEngineeringSupport_Type = TruthValue
_AlaOspfTrafficEngineeringSupport_Object = MibScalar
alaOspfTrafficEngineeringSupport = _AlaOspfTrafficEngineeringSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 24),
    _AlaOspfTrafficEngineeringSupport_Type()
)
alaOspfTrafficEngineeringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTrafficEngineeringSupport.setStatus("current")
_AlaOspfReferenceBandwidth_Type = Unsigned32
_AlaOspfReferenceBandwidth_Object = MibScalar
alaOspfReferenceBandwidth = _AlaOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 25),
    _AlaOspfReferenceBandwidth_Type()
)
alaOspfReferenceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfReferenceBandwidth.setStatus("deprecated")


class _AlaOspfRestartSupport_Type(Integer32):
    """Custom type alaOspfRestartSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_AlaOspfRestartSupport_Type.__name__ = "Integer32"
_AlaOspfRestartSupport_Object = MibScalar
alaOspfRestartSupport = _AlaOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 26),
    _AlaOspfRestartSupport_Type()
)
alaOspfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartSupport.setStatus("deprecated")


class _AlaOspfRestartInterval_Type(Integer32):
    """Custom type alaOspfRestartInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_AlaOspfRestartInterval_Type.__name__ = "Integer32"
_AlaOspfRestartInterval_Object = MibScalar
alaOspfRestartInterval = _AlaOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 27),
    _AlaOspfRestartInterval_Type()
)
alaOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaOspfRestartInterval.setUnits("seconds")


class _AlaOspfRestartStatus_Type(Integer32):
    """Custom type alaOspfRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_AlaOspfRestartStatus_Type.__name__ = "Integer32"
_AlaOspfRestartStatus_Object = MibScalar
alaOspfRestartStatus = _AlaOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 28),
    _AlaOspfRestartStatus_Type()
)
alaOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartStatus.setStatus("deprecated")
_AlaOspfRestartAge_Type = Unsigned32
_AlaOspfRestartAge_Object = MibScalar
alaOspfRestartAge = _AlaOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 29),
    _AlaOspfRestartAge_Type()
)
alaOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaOspfRestartAge.setUnits("seconds")


class _AlaOspfRestartExitReason_Type(Integer32):
    """Custom type alaOspfRestartExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfRestartExitReason_Type.__name__ = "Integer32"
_AlaOspfRestartExitReason_Object = MibScalar
alaOspfRestartExitReason = _AlaOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 30),
    _AlaOspfRestartExitReason_Type()
)
alaOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartExitReason.setStatus("deprecated")
_AlaOspfNbrAugTable_Object = MibTable
alaOspfNbrAugTable = _AlaOspfNbrAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31)
)
if mibBuilder.loadTexts:
    alaOspfNbrAugTable.setStatus("current")
_AlaOspfNbrAugEntry_Object = MibTableRow
alaOspfNbrAugEntry = _AlaOspfNbrAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    alaOspfNbrAugEntry.setStatus("current")


class _AlaOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_AlaOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfNbrRestartHelperStatus_Object = MibTableColumn
alaOspfNbrRestartHelperStatus = _AlaOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 1),
    _AlaOspfNbrRestartHelperStatus_Type()
)
alaOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperStatus.setStatus("deprecated")
_AlaOspfNbrRestartHelperAge_Type = Unsigned32
_AlaOspfNbrRestartHelperAge_Object = MibTableColumn
alaOspfNbrRestartHelperAge = _AlaOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 2),
    _AlaOspfNbrRestartHelperAge_Type()
)
alaOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperAge.setUnits("seconds")


class _AlaOspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type alaOspfNbrRestartHelperExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AlaOspfNbrRestartHelperExitReason_Object = MibTableColumn
alaOspfNbrRestartHelperExitReason = _AlaOspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 3),
    _AlaOspfNbrRestartHelperExitReason_Type()
)
alaOspfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperExitReason.setStatus("deprecated")
_AlaOspfNbrAreaId_Type = IpAddress
_AlaOspfNbrAreaId_Object = MibTableColumn
alaOspfNbrAreaId = _AlaOspfNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 4),
    _AlaOspfNbrAreaId_Type()
)
alaOspfNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrAreaId.setStatus("current")
_AlaOspfNbrDrAddress_Type = IpAddress
_AlaOspfNbrDrAddress_Object = MibTableColumn
alaOspfNbrDrAddress = _AlaOspfNbrDrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 5),
    _AlaOspfNbrDrAddress_Type()
)
alaOspfNbrDrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrDrAddress.setStatus("current")
_AlaOspfNbrBdrAddress_Type = IpAddress
_AlaOspfNbrBdrAddress_Object = MibTableColumn
alaOspfNbrBdrAddress = _AlaOspfNbrBdrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 6),
    _AlaOspfNbrBdrAddress_Type()
)
alaOspfNbrBdrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrBdrAddress.setStatus("current")


class _AlaOspfNbrType_Type(Integer32):
    """Custom type alaOspfNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AlaOspfNbrType_Type.__name__ = "Integer32"
_AlaOspfNbrType_Object = MibTableColumn
alaOspfNbrType = _AlaOspfNbrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 7),
    _AlaOspfNbrType_Type()
)
alaOspfNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrType.setStatus("current")


class _AlaOspfNbrMode_Type(Integer32):
    """Custom type alaOspfNbrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2),
          ("slaveHold", 3))
    )


_AlaOspfNbrMode_Type.__name__ = "Integer32"
_AlaOspfNbrMode_Object = MibTableColumn
alaOspfNbrMode = _AlaOspfNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 8),
    _AlaOspfNbrMode_Type()
)
alaOspfNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrMode.setStatus("current")
_AlaOspfNbrMd5SeqNo_Type = Counter32
_AlaOspfNbrMd5SeqNo_Object = MibTableColumn
alaOspfNbrMd5SeqNo = _AlaOspfNbrMd5SeqNo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 9),
    _AlaOspfNbrMd5SeqNo_Type()
)
alaOspfNbrMd5SeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrMd5SeqNo.setStatus("current")
_AlaOspfNbrLastHello_Type = Counter32
_AlaOspfNbrLastHello_Object = MibTableColumn
alaOspfNbrLastHello = _AlaOspfNbrLastHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 10),
    _AlaOspfNbrLastHello_Type()
)
alaOspfNbrLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrLastHello.setStatus("current")
_AlaOspfNbrPendingLSreq_Type = Counter32
_AlaOspfNbrPendingLSreq_Object = MibTableColumn
alaOspfNbrPendingLSreq = _AlaOspfNbrPendingLSreq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 11),
    _AlaOspfNbrPendingLSreq_Type()
)
alaOspfNbrPendingLSreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSreq.setStatus("current")
_AlaOspfNbrPendingLSack_Type = Counter32
_AlaOspfNbrPendingLSack_Object = MibTableColumn
alaOspfNbrPendingLSack = _AlaOspfNbrPendingLSack_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 12),
    _AlaOspfNbrPendingLSack_Type()
)
alaOspfNbrPendingLSack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSack.setStatus("current")
_AlaOspfNbrPendingLSupd_Type = Counter32
_AlaOspfNbrPendingLSupd_Object = MibTableColumn
alaOspfNbrPendingLSupd = _AlaOspfNbrPendingLSupd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 13),
    _AlaOspfNbrPendingLSupd_Type()
)
alaOspfNbrPendingLSupd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSupd.setStatus("current")
_AlaOspfVirtNbrAugTable_Object = MibTable
alaOspfVirtNbrAugTable = _AlaOspfVirtNbrAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32)
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugTable.setStatus("current")
_AlaOspfVirtNbrAugEntry_Object = MibTableRow
alaOspfVirtNbrAugEntry = _AlaOspfVirtNbrAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugEntry.setStatus("current")


class _AlaOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfVirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_AlaOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
alaOspfVirtNbrRestartHelperStatus = _AlaOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 1),
    _AlaOspfVirtNbrRestartHelperStatus_Type()
)
alaOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperStatus.setStatus("deprecated")
_AlaOspfVirtNbrRestartHelperAge_Type = Unsigned32
_AlaOspfVirtNbrRestartHelperAge_Object = MibTableColumn
alaOspfVirtNbrRestartHelperAge = _AlaOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 2),
    _AlaOspfVirtNbrRestartHelperAge_Type()
)
alaOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _AlaOspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type alaOspfVirtNbrRestartHelperExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AlaOspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
alaOspfVirtNbrRestartHelperExitReason = _AlaOspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 3),
    _AlaOspfVirtNbrRestartHelperExitReason_Type()
)
alaOspfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperExitReason.setStatus("deprecated")
_AlaOspfVirtNbrDrAddr_Type = IpAddress
_AlaOspfVirtNbrDrAddr_Object = MibTableColumn
alaOspfVirtNbrDrAddr = _AlaOspfVirtNbrDrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 4),
    _AlaOspfVirtNbrDrAddr_Type()
)
alaOspfVirtNbrDrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrDrAddr.setStatus("current")
_AlaOspfVirtNbrBdrAddr_Type = IpAddress
_AlaOspfVirtNbrBdrAddr_Object = MibTableColumn
alaOspfVirtNbrBdrAddr = _AlaOspfVirtNbrBdrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 5),
    _AlaOspfVirtNbrBdrAddr_Type()
)
alaOspfVirtNbrBdrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrBdrAddr.setStatus("current")


class _AlaOspfVirtNbrMode_Type(Integer32):
    """Custom type alaOspfVirtNbrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2),
          ("slaveHold", 3))
    )


_AlaOspfVirtNbrMode_Type.__name__ = "Integer32"
_AlaOspfVirtNbrMode_Object = MibTableColumn
alaOspfVirtNbrMode = _AlaOspfVirtNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 6),
    _AlaOspfVirtNbrMode_Type()
)
alaOspfVirtNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrMode.setStatus("current")
_AlaOspfVirtNbrMd5SeqNo_Type = Counter32
_AlaOspfVirtNbrMd5SeqNo_Object = MibTableColumn
alaOspfVirtNbrMd5SeqNo = _AlaOspfVirtNbrMd5SeqNo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 7),
    _AlaOspfVirtNbrMd5SeqNo_Type()
)
alaOspfVirtNbrMd5SeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrMd5SeqNo.setStatus("current")
_AlaOspfVirtNbrLastHello_Type = Counter32
_AlaOspfVirtNbrLastHello_Object = MibTableColumn
alaOspfVirtNbrLastHello = _AlaOspfVirtNbrLastHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 8),
    _AlaOspfVirtNbrLastHello_Type()
)
alaOspfVirtNbrLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrLastHello.setStatus("current")
_AlaOspfVirtNbrPendingLSreq_Type = Counter32
_AlaOspfVirtNbrPendingLSreq_Object = MibTableColumn
alaOspfVirtNbrPendingLSreq = _AlaOspfVirtNbrPendingLSreq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 9),
    _AlaOspfVirtNbrPendingLSreq_Type()
)
alaOspfVirtNbrPendingLSreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSreq.setStatus("current")
_AlaOspfVirtNbrPendingLSack_Type = Counter32
_AlaOspfVirtNbrPendingLSack_Object = MibTableColumn
alaOspfVirtNbrPendingLSack = _AlaOspfVirtNbrPendingLSack_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 10),
    _AlaOspfVirtNbrPendingLSack_Type()
)
alaOspfVirtNbrPendingLSack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSack.setStatus("current")
_AlaOspfVirtNbrPendingLSupd_Type = Counter32
_AlaOspfVirtNbrPendingLSupd_Object = MibTableColumn
alaOspfVirtNbrPendingLSupd = _AlaOspfVirtNbrPendingLSupd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 11),
    _AlaOspfVirtNbrPendingLSupd_Type()
)
alaOspfVirtNbrPendingLSupd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSupd.setStatus("current")


class _AlaOspfRestartInitiate_Type(Integer32):
    """Custom type alaOspfRestartInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2))
    )


_AlaOspfRestartInitiate_Type.__name__ = "Integer32"
_AlaOspfRestartInitiate_Object = MibScalar
alaOspfRestartInitiate = _AlaOspfRestartInitiate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 33),
    _AlaOspfRestartInitiate_Type()
)
alaOspfRestartInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartInitiate.setStatus("current")
_AlaOspfAreaAugTable_Object = MibTable
alaOspfAreaAugTable = _AlaOspfAreaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35)
)
if mibBuilder.loadTexts:
    alaOspfAreaAugTable.setStatus("current")
_AlaOspfAreaAugEntry_Object = MibTableRow
alaOspfAreaAugEntry = _AlaOspfAreaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    alaOspfAreaAugEntry.setStatus("current")


class _AlaOspfAreaOperStatus_Type(Integer32):
    """Custom type alaOspfAreaOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("up", 2),
          ("down", 3))
    )


_AlaOspfAreaOperStatus_Type.__name__ = "Integer32"
_AlaOspfAreaOperStatus_Object = MibTableColumn
alaOspfAreaOperStatus = _AlaOspfAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 1),
    _AlaOspfAreaOperStatus_Type()
)
alaOspfAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaOperStatus.setStatus("current")
_AlaOspfAreaLastSpfRun_Type = Counter32
_AlaOspfAreaLastSpfRun_Object = MibTableColumn
alaOspfAreaLastSpfRun = _AlaOspfAreaLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 2),
    _AlaOspfAreaLastSpfRun_Type()
)
alaOspfAreaLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaLastSpfRun.setStatus("current")
_AlaOspfAreaActiveVlinks_Type = Counter32
_AlaOspfAreaActiveVlinks_Object = MibTableColumn
alaOspfAreaActiveVlinks = _AlaOspfAreaActiveVlinks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 3),
    _AlaOspfAreaActiveVlinks_Type()
)
alaOspfAreaActiveVlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaActiveVlinks.setStatus("current")
_AlaOspfAreaIncrSpfRuns_Type = Counter32
_AlaOspfAreaIncrSpfRuns_Object = MibTableColumn
alaOspfAreaIncrSpfRuns = _AlaOspfAreaIncrSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 4),
    _AlaOspfAreaIncrSpfRuns_Type()
)
alaOspfAreaIncrSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaIncrSpfRuns.setStatus("current")
_AlaOspfAreaInitNbrs_Type = Counter32
_AlaOspfAreaInitNbrs_Object = MibTableColumn
alaOspfAreaInitNbrs = _AlaOspfAreaInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 5),
    _AlaOspfAreaInitNbrs_Type()
)
alaOspfAreaInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaInitNbrs.setStatus("current")
_AlaOspfAreaExchNbrs_Type = Counter32
_AlaOspfAreaExchNbrs_Object = MibTableColumn
alaOspfAreaExchNbrs = _AlaOspfAreaExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 6),
    _AlaOspfAreaExchNbrs_Type()
)
alaOspfAreaExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaExchNbrs.setStatus("current")
_AlaOspfAreaFullNbrs_Type = Counter32
_AlaOspfAreaFullNbrs_Object = MibTableColumn
alaOspfAreaFullNbrs = _AlaOspfAreaFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 7),
    _AlaOspfAreaFullNbrs_Type()
)
alaOspfAreaFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaFullNbrs.setStatus("current")
_AlaOspfAreaNumIntfs_Type = Counter32
_AlaOspfAreaNumIntfs_Object = MibTableColumn
alaOspfAreaNumIntfs = _AlaOspfAreaNumIntfs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 8),
    _AlaOspfAreaNumIntfs_Type()
)
alaOspfAreaNumIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNumIntfs.setStatus("current")


class _AlaOspfAreaAttachedIntfs_Type(OctetString):
    """Custom type alaOspfAreaAttachedIntfs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2200),
    )


_AlaOspfAreaAttachedIntfs_Type.__name__ = "OctetString"
_AlaOspfAreaAttachedIntfs_Object = MibTableColumn
alaOspfAreaAttachedIntfs = _AlaOspfAreaAttachedIntfs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 9),
    _AlaOspfAreaAttachedIntfs_Type()
)
alaOspfAreaAttachedIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaAttachedIntfs.setStatus("current")
_AlaOspfArea2WayNbrs_Type = Counter32
_AlaOspfArea2WayNbrs_Object = MibTableColumn
alaOspfArea2WayNbrs = _AlaOspfArea2WayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 10),
    _AlaOspfArea2WayNbrs_Type()
)
alaOspfArea2WayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfArea2WayNbrs.setStatus("current")


class _AlaOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2),
          ("none", 3))
    )


_AlaOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorRole_Object = MibTableColumn
alaOspfAreaNssaTranslatorRole = _AlaOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 11),
    _AlaOspfAreaNssaTranslatorRole_Type()
)
alaOspfAreaNssaTranslatorRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorRole.setStatus("deprecated")


class _AlaOspfAreaNssaTranslatorStabilityInterval_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorStabilityInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaOspfAreaNssaTranslatorStabilityInterval_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
alaOspfAreaNssaTranslatorStabilityInterval = _AlaOspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 12),
    _AlaOspfAreaNssaTranslatorStabilityInterval_Type()
)
alaOspfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorStabilityInterval.setStatus("deprecated")


class _AlaOspfAreaNssaImportSetPbit_Type(Integer32):
    """Custom type alaOspfAreaNssaImportSetPbit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("propagate", 1),
          ("doNotPropagate", 2),
          ("none", 3))
    )


_AlaOspfAreaNssaImportSetPbit_Type.__name__ = "Integer32"
_AlaOspfAreaNssaImportSetPbit_Object = MibTableColumn
alaOspfAreaNssaImportSetPbit = _AlaOspfAreaNssaImportSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 13),
    _AlaOspfAreaNssaImportSetPbit_Type()
)
alaOspfAreaNssaImportSetPbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaImportSetPbit.setStatus("current")


class _AlaOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorState based on Integer32"""
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
        *(("enabled", 1),
          ("elected", 2),
          ("disabled", 3),
          ("none", 4))
    )


_AlaOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorState_Object = MibTableColumn
alaOspfAreaNssaTranslatorState = _AlaOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 14),
    _AlaOspfAreaNssaTranslatorState_Type()
)
alaOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorState.setStatus("deprecated")
_AlaOspfAreaNssaElectedTranslatorRouterId_Type = IpAddress
_AlaOspfAreaNssaElectedTranslatorRouterId_Object = MibTableColumn
alaOspfAreaNssaElectedTranslatorRouterId = _AlaOspfAreaNssaElectedTranslatorRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 15),
    _AlaOspfAreaNssaElectedTranslatorRouterId_Type()
)
alaOspfAreaNssaElectedTranslatorRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaElectedTranslatorRouterId.setStatus("current")
_AlaOspfExtLsdbAugTable_Object = MibTable
alaOspfExtLsdbAugTable = _AlaOspfExtLsdbAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36)
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugTable.setStatus("current")
_AlaOspfExtLsdbAugEntry_Object = MibTableRow
alaOspfExtLsdbAugEntry = _AlaOspfExtLsdbAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugEntry.setStatus("current")


class _AlaOspfExtLsdbProto_Type(Integer32):
    """Custom type alaOspfExtLsdbProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("static", 2),
          ("direct", 3),
          ("rip", 4),
          ("ospf", 5),
          ("isis", 6),
          ("bgp", 7))
    )


_AlaOspfExtLsdbProto_Type.__name__ = "Integer32"
_AlaOspfExtLsdbProto_Object = MibTableColumn
alaOspfExtLsdbProto = _AlaOspfExtLsdbProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 1),
    _AlaOspfExtLsdbProto_Type()
)
alaOspfExtLsdbProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbProto.setStatus("current")
_AlaOspfExtLsdbRouteTag_Type = Counter32
_AlaOspfExtLsdbRouteTag_Object = MibTableColumn
alaOspfExtLsdbRouteTag = _AlaOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 2),
    _AlaOspfExtLsdbRouteTag_Type()
)
alaOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbRouteTag.setStatus("current")
_AlaOspfExtLsdbFwdAddr_Type = IpAddress
_AlaOspfExtLsdbFwdAddr_Object = MibTableColumn
alaOspfExtLsdbFwdAddr = _AlaOspfExtLsdbFwdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 3),
    _AlaOspfExtLsdbFwdAddr_Type()
)
alaOspfExtLsdbFwdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbFwdAddr.setStatus("current")


class _AlaOspfExtLsdbMetricType_Type(Integer32):
    """Custom type alaOspfExtLsdbMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_AlaOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_AlaOspfExtLsdbMetricType_Object = MibTableColumn
alaOspfExtLsdbMetricType = _AlaOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 4),
    _AlaOspfExtLsdbMetricType_Type()
)
alaOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMetricType.setStatus("current")
_AlaOspfExtLsdbMetric_Type = Integer32
_AlaOspfExtLsdbMetric_Object = MibTableColumn
alaOspfExtLsdbMetric = _AlaOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 5),
    _AlaOspfExtLsdbMetric_Type()
)
alaOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMetric.setStatus("current")
_AlaOspfExtLsdbLength_Type = Integer32
_AlaOspfExtLsdbLength_Object = MibTableColumn
alaOspfExtLsdbLength = _AlaOspfExtLsdbLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 6),
    _AlaOspfExtLsdbLength_Type()
)
alaOspfExtLsdbLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbLength.setStatus("current")
_AlaOspfExtLsdbMask_Type = IpAddress
_AlaOspfExtLsdbMask_Object = MibTableColumn
alaOspfExtLsdbMask = _AlaOspfExtLsdbMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 7),
    _AlaOspfExtLsdbMask_Type()
)
alaOspfExtLsdbMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMask.setStatus("current")
_AlaOspfAreaAggregateAugTable_Object = MibTable
alaOspfAreaAggregateAugTable = _AlaOspfAreaAggregateAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38)
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugTable.setStatus("current")
_AlaOspfAreaAggregateAugEntry_Object = MibTableRow
alaOspfAreaAggregateAugEntry = _AlaOspfAreaAggregateAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugEntry.setStatus("current")


class _AlaOspfAreaAggregateMetric_Type(Integer32):
    """Custom type alaOspfAreaAggregateMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfAreaAggregateMetric_Type.__name__ = "Integer32"
_AlaOspfAreaAggregateMetric_Object = MibTableColumn
alaOspfAreaAggregateMetric = _AlaOspfAreaAggregateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38, 1, 1),
    _AlaOspfAreaAggregateMetric_Type()
)
alaOspfAreaAggregateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfAreaAggregateMetric.setStatus("current")


class _AlaOspfDefaultOriginate_Type(Integer32):
    """Custom type alaOspfDefaultOriginate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("only", 2),
          ("always", 3))
    )


_AlaOspfDefaultOriginate_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginate_Object = MibScalar
alaOspfDefaultOriginate = _AlaOspfDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 39),
    _AlaOspfDefaultOriginate_Type()
)
alaOspfDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginate.setStatus("current")


class _AlaOspfDefaultOriginateMetricType_Type(Integer32):
    """Custom type alaOspfDefaultOriginateMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_AlaOspfDefaultOriginateMetricType_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginateMetricType_Object = MibScalar
alaOspfDefaultOriginateMetricType = _AlaOspfDefaultOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 40),
    _AlaOspfDefaultOriginateMetricType_Type()
)
alaOspfDefaultOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginateMetricType.setStatus("current")


class _AlaOspfDefaultOriginateMetric_Type(Integer32):
    """Custom type alaOspfDefaultOriginateMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOspfDefaultOriginateMetric_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginateMetric_Object = MibScalar
alaOspfDefaultOriginateMetric = _AlaOspfDefaultOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 41),
    _AlaOspfDefaultOriginateMetric_Type()
)
alaOspfDefaultOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginateMetric.setStatus("current")


class _AlaOspfBfdStatus_Type(Integer32):
    """Custom type alaOspfBfdStatus based on Integer32"""
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


_AlaOspfBfdStatus_Type.__name__ = "Integer32"
_AlaOspfBfdStatus_Object = MibScalar
alaOspfBfdStatus = _AlaOspfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 42),
    _AlaOspfBfdStatus_Type()
)
alaOspfBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfBfdStatus.setStatus("current")


class _AlaOspfBfdAllInterfaceStatus_Type(Integer32):
    """Custom type alaOspfBfdAllInterfaceStatus based on Integer32"""
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


_AlaOspfBfdAllInterfaceStatus_Type.__name__ = "Integer32"
_AlaOspfBfdAllInterfaceStatus_Object = MibScalar
alaOspfBfdAllInterfaceStatus = _AlaOspfBfdAllInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 43),
    _AlaOspfBfdAllInterfaceStatus_Type()
)
alaOspfBfdAllInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfBfdAllInterfaceStatus.setStatus("current")


class _AlaOspfOpaqueTransitCapability_Type(Integer32):
    """Custom type alaOspfOpaqueTransitCapability based on Integer32"""
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


_AlaOspfOpaqueTransitCapability_Type.__name__ = "Integer32"
_AlaOspfOpaqueTransitCapability_Object = MibScalar
alaOspfOpaqueTransitCapability = _AlaOspfOpaqueTransitCapability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 44),
    _AlaOspfOpaqueTransitCapability_Type()
)
alaOspfOpaqueTransitCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfOpaqueTransitCapability.setStatus("current")
_AlaOspfGeneralTable_ObjectIdentity = ObjectIdentity
alaOspfGeneralTable = _AlaOspfGeneralTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3)
)
_AlaOspfTotalSpfRuns_Type = Counter32
_AlaOspfTotalSpfRuns_Object = MibScalar
alaOspfTotalSpfRuns = _AlaOspfTotalSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 1),
    _AlaOspfTotalSpfRuns_Type()
)
alaOspfTotalSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalSpfRuns.setStatus("current")
_AlaOspfTotalIncrSpfRuns_Type = Counter32
_AlaOspfTotalIncrSpfRuns_Object = MibScalar
alaOspfTotalIncrSpfRuns = _AlaOspfTotalIncrSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 2),
    _AlaOspfTotalIncrSpfRuns_Type()
)
alaOspfTotalIncrSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalIncrSpfRuns.setStatus("current")
_AlaOspfTotalInitNbrs_Type = Counter32
_AlaOspfTotalInitNbrs_Object = MibScalar
alaOspfTotalInitNbrs = _AlaOspfTotalInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 3),
    _AlaOspfTotalInitNbrs_Type()
)
alaOspfTotalInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalInitNbrs.setStatus("current")
_AlaOspfTotalExchNbrs_Type = Counter32
_AlaOspfTotalExchNbrs_Object = MibScalar
alaOspfTotalExchNbrs = _AlaOspfTotalExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 4),
    _AlaOspfTotalExchNbrs_Type()
)
alaOspfTotalExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalExchNbrs.setStatus("current")
_AlaOspfTotalFullNbrs_Type = Counter32
_AlaOspfTotalFullNbrs_Object = MibScalar
alaOspfTotalFullNbrs = _AlaOspfTotalFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 5),
    _AlaOspfTotalFullNbrs_Type()
)
alaOspfTotalFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalFullNbrs.setStatus("current")
_AlaOspfTotalAreas_Type = Counter32
_AlaOspfTotalAreas_Object = MibScalar
alaOspfTotalAreas = _AlaOspfTotalAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 6),
    _AlaOspfTotalAreas_Type()
)
alaOspfTotalAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalAreas.setStatus("current")
_AlaOspfTotalActiveAreas_Type = Counter32
_AlaOspfTotalActiveAreas_Object = MibScalar
alaOspfTotalActiveAreas = _AlaOspfTotalActiveAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 7),
    _AlaOspfTotalActiveAreas_Type()
)
alaOspfTotalActiveAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalActiveAreas.setStatus("current")
_AlaOspfTotalTransitAreas_Type = Counter32
_AlaOspfTotalTransitAreas_Object = MibScalar
alaOspfTotalTransitAreas = _AlaOspfTotalTransitAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 8),
    _AlaOspfTotalTransitAreas_Type()
)
alaOspfTotalTransitAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalTransitAreas.setStatus("current")
_AlaOspfTotalNSSA_Type = Counter32
_AlaOspfTotalNSSA_Object = MibScalar
alaOspfTotalNSSA = _AlaOspfTotalNSSA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 9),
    _AlaOspfTotalNSSA_Type()
)
alaOspfTotalNSSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalNSSA.setStatus("current")
_AlaOspfTotal2wayNbrs_Type = Counter32
_AlaOspfTotal2wayNbrs_Object = MibScalar
alaOspfTotal2wayNbrs = _AlaOspfTotal2wayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 10),
    _AlaOspfTotal2wayNbrs_Type()
)
alaOspfTotal2wayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotal2wayNbrs.setStatus("current")
_AlcatelIND1OSPFMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBConformance = _AlcatelIND1OSPFMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBConformance.setStatus("current")
_AlcatelIND1OSPFMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBGroups = _AlcatelIND1OSPFMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBGroups.setStatus("current")
_AlcatelIND1OSPFMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBCompliances = _AlcatelIND1OSPFMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBCompliances.setStatus("current")
ospfIfEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfIfAugEntry")
)
alaOspfIfAugEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfVirtIfAugEntry")
)
alaOspfVirtIfAugEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfNbrAugEntry")
)
alaOspfNbrAugEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfVirtNbrAugEntry")
)
alaOspfVirtNbrAugEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfAreaEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfAreaAugEntry")
)
alaOspfAreaAugEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfExtLsdbEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfExtLsdbAugEntry")
)
alaOspfExtLsdbAugEntry.setIndexNames(*ospfExtLsdbEntry.getIndexNames())
ospfAreaAggregateEntry.registerAugmentions(
    ("ALCATEL-ENT1-OSPF-MIB",
     "alaOspfAreaAggregateAugEntry")
)
alaOspfAreaAggregateAugEntry.setIndexNames(*ospfAreaAggregateEntry.getIndexNames())

# Managed Objects groups

alaOspfMiscellaneousGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 1)
)
alaOspfMiscellaneousGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfRedistRouteTag"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTimerSpfDelay"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTimerSpfHold"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteNumber"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfMTUCheck"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBfdStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBfdAllInterfaceStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartHelperSupport"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartHelperStrictLSAChecking"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartHelperStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRFC1583Compatibility"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfOpaqueLsaSupport"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTrafficEngineeringSupport"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfReferenceBandwidth"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartSupport"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartInterval"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartAge"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartExitReason"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfDefaultOriginate"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfDefaultOriginateMetricType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfDefaultOriginateMetric"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRestartInitiate"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfOpaqueTransitCapability"))
)
if mibBuilder.loadTexts:
    alaOspfMiscellaneousGroup.setStatus("current")

alaOspfRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 4)
)
alaOspfRouteGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteDest"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteMask"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteTos"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteNextHop"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteIfIndex"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteAge"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteTag"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteMetric1"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteMetric2"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteStatus"))
)
if mibBuilder.loadTexts:
    alaOspfRouteGroup.setStatus("current")

alaOspfBdrRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 5)
)
alaOspfBdrRouterGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterAreaId"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterId"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterTos"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterNextHop"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterIfIndex"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterAge"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterMetric"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterStatus"))
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterGroup.setStatus("current")

alaOspfIfMd5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 8)
)
alaOspfIfMd5Group.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5IpAddress"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyId"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5Key"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyStartAccept"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyStopAccept"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyStartGenerate"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5KeyStopGenerate"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5RowStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5EncryptKey"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5AuthMode"))
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Group.setStatus("current")

alaOspfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 9)
)
alaOspfGeneralGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalSpfRuns"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalIncrSpfRuns"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalInitNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalExchNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalFullNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalAreas"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalActiveAreas"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalTransitAreas"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotalNSSA"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfTotal2wayNbrs"))
)
if mibBuilder.loadTexts:
    alaOspfGeneralGroup.setStatus("current")

alaOspfAreaAugEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 10)
)
alaOspfAreaAugEntryGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaOperStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaLastSpfRun"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaActiveVlinks"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaIncrSpfRuns"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaInitNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaExchNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaFullNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNumIntfs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaAttachedIntfs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfArea2WayNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNssaTranslatorRole"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNssaTranslatorStabilityInterval"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNssaImportSetPbit"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNssaTranslatorState"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaNssaElectedTranslatorRouterId"))
)
if mibBuilder.loadTexts:
    alaOspfAreaAugEntryGroup.setStatus("current")

alaOspfAreaAggregateAugEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 11)
)
alaOspfAreaAggregateAugEntryGroup.setObjects(
    ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaAggregateMetric")
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugEntryGroup.setStatus("current")

alaOspfIfAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 12)
)
alaOspfIfAugGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfEncryptKey"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfIpMask"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfVlanId"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfDrRouterid"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfBdrRouterid"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMTU"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfInitNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfExchNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfFullNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfLinkType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfOperStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfIntfName"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIf2WayNbrs"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfBfdStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfBfdDrsOnly"))
)
if mibBuilder.loadTexts:
    alaOspfIfAugGroup.setStatus("current")

alaOspfExtLsdbAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 13)
)
alaOspfExtLsdbAugGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbProto"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbRouteTag"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbFwdAddr"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbMetricType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbMetric"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbLength"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbMask"))
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugGroup.setStatus("current")

alaOspfNbrAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 14)
)
alaOspfNbrAugGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrRestartHelperStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrRestartHelperAge"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrRestartHelperExitReason"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrAreaId"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrDrAddress"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrBdrAddress"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrType"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrMode"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrMd5SeqNo"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrLastHello"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrPendingLSreq"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrPendingLSack"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrPendingLSupd"))
)
if mibBuilder.loadTexts:
    alaOspfNbrAugGroup.setStatus("current")

alaOspfVirtIfAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 15)
)
alaOspfVirtIfAugGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtIfEncryptKey"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtIfOperStatus"))
)
if mibBuilder.loadTexts:
    alaOspfVirtIfAugGroup.setStatus("current")

alaOspfVirtNbrAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 16)
)
alaOspfVirtNbrAugGroup.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrRestartHelperStatus"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrRestartHelperAge"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrRestartHelperExitReason"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrDrAddr"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrBdrAddr"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrMode"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrMd5SeqNo"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrLastHello"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrPendingLSreq"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrPendingLSack"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfVirtNbrPendingLSupd"))
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1OSPFMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 2, 1)
)
alcatelIND1OSPFMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-OSPF-MIB", "alaOspfMiscellaneousGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfRouteGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfBdrRouterGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfMd5Group"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfGeneralGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaAugEntryGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfAreaAggregateAugEntryGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfIfAugGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfExtLsdbAugGroup"),
        ("ALCATEL-ENT1-OSPF-MIB", "alaOspfNbrAugGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-OSPF-MIB",
    **{"AlaAuthenticationEncryptKey": AlaAuthenticationEncryptKey,
       "alcatelIND1OSPFMIB": alcatelIND1OSPFMIB,
       "alcatelIND1OSPFMIBObjects": alcatelIND1OSPFMIBObjects,
       "alaProtocolOspf": alaProtocolOspf,
       "alaOspfRedistRouteTag": alaOspfRedistRouteTag,
       "alaOspfTimerSpfDelay": alaOspfTimerSpfDelay,
       "alaOspfTimerSpfHold": alaOspfTimerSpfHold,
       "alaOspfRouteNumber": alaOspfRouteNumber,
       "alaOspfMTUCheck": alaOspfMTUCheck,
       "alaOspfRouteTable": alaOspfRouteTable,
       "alaOspfRouteEntry": alaOspfRouteEntry,
       "alaOspfRouteDest": alaOspfRouteDest,
       "alaOspfRouteMask": alaOspfRouteMask,
       "alaOspfRouteTos": alaOspfRouteTos,
       "alaOspfRouteNextHop": alaOspfRouteNextHop,
       "alaOspfRouteIfIndex": alaOspfRouteIfIndex,
       "alaOspfRouteType": alaOspfRouteType,
       "alaOspfRouteAge": alaOspfRouteAge,
       "alaOspfRouteTag": alaOspfRouteTag,
       "alaOspfRouteMetric1": alaOspfRouteMetric1,
       "alaOspfRouteMetric2": alaOspfRouteMetric2,
       "alaOspfRouteStatus": alaOspfRouteStatus,
       "alaOspfBdrRouterTable": alaOspfBdrRouterTable,
       "alaOspfBdrRouterEntry": alaOspfBdrRouterEntry,
       "alaOspfBdrRouterAreaId": alaOspfBdrRouterAreaId,
       "alaOspfBdrRouterId": alaOspfBdrRouterId,
       "alaOspfBdrRouterTos": alaOspfBdrRouterTos,
       "alaOspfBdrRouterNextHop": alaOspfBdrRouterNextHop,
       "alaOspfBdrRouterIfIndex": alaOspfBdrRouterIfIndex,
       "alaOspfBdrRouterType": alaOspfBdrRouterType,
       "alaOspfBdrRouterAge": alaOspfBdrRouterAge,
       "alaOspfBdrRouterMetric": alaOspfBdrRouterMetric,
       "alaOspfBdrRouterStatus": alaOspfBdrRouterStatus,
       "alaOspfIfMd5Table": alaOspfIfMd5Table,
       "alaOspfIfMd5Entry": alaOspfIfMd5Entry,
       "alaOspfIfMd5IpAddress": alaOspfIfMd5IpAddress,
       "alaOspfIfMd5KeyId": alaOspfIfMd5KeyId,
       "alaOspfIfMd5Key": alaOspfIfMd5Key,
       "alaOspfIfMd5KeyStartAccept": alaOspfIfMd5KeyStartAccept,
       "alaOspfIfMd5KeyStopAccept": alaOspfIfMd5KeyStopAccept,
       "alaOspfIfMd5KeyStartGenerate": alaOspfIfMd5KeyStartGenerate,
       "alaOspfIfMd5KeyStopGenerate": alaOspfIfMd5KeyStopGenerate,
       "alaOspfIfMd5RowStatus": alaOspfIfMd5RowStatus,
       "alaOspfIfMd5EncryptKey": alaOspfIfMd5EncryptKey,
       "alaOspfIfMd5AuthMode": alaOspfIfMd5AuthMode,
       "alaOspfIfAugTable": alaOspfIfAugTable,
       "alaOspfIfAugEntry": alaOspfIfAugEntry,
       "alaOspfIfEncryptKey": alaOspfIfEncryptKey,
       "alaOspfIfIpMask": alaOspfIfIpMask,
       "alaOspfIfVlanId": alaOspfIfVlanId,
       "alaOspfIfDrRouterid": alaOspfIfDrRouterid,
       "alaOspfIfBdrRouterid": alaOspfIfBdrRouterid,
       "alaOspfIfMTU": alaOspfIfMTU,
       "alaOspfIfInitNbrs": alaOspfIfInitNbrs,
       "alaOspfIfExchNbrs": alaOspfIfExchNbrs,
       "alaOspfIfFullNbrs": alaOspfIfFullNbrs,
       "alaOspfIfLinkType": alaOspfIfLinkType,
       "alaOspfIfOperStatus": alaOspfIfOperStatus,
       "alaOspfIfIntfName": alaOspfIfIntfName,
       "alaOspfIf2WayNbrs": alaOspfIf2WayNbrs,
       "alaOspfIfBfdStatus": alaOspfIfBfdStatus,
       "alaOspfIfBfdDrsOnly": alaOspfIfBfdDrsOnly,
       "alaOspfVirtIfAugTable": alaOspfVirtIfAugTable,
       "alaOspfVirtIfAugEntry": alaOspfVirtIfAugEntry,
       "alaOspfVirtIfEncryptKey": alaOspfVirtIfEncryptKey,
       "alaOspfVirtIfOperStatus": alaOspfVirtIfOperStatus,
       "alaOspfRestartHelperSupport": alaOspfRestartHelperSupport,
       "alaOspfRestartHelperStrictLSAChecking": alaOspfRestartHelperStrictLSAChecking,
       "alaOspfRestartHelperStatus": alaOspfRestartHelperStatus,
       "alaOspfRFC1583Compatibility": alaOspfRFC1583Compatibility,
       "alaOspfOpaqueLsaSupport": alaOspfOpaqueLsaSupport,
       "alaOspfTrafficEngineeringSupport": alaOspfTrafficEngineeringSupport,
       "alaOspfReferenceBandwidth": alaOspfReferenceBandwidth,
       "alaOspfRestartSupport": alaOspfRestartSupport,
       "alaOspfRestartInterval": alaOspfRestartInterval,
       "alaOspfRestartStatus": alaOspfRestartStatus,
       "alaOspfRestartAge": alaOspfRestartAge,
       "alaOspfRestartExitReason": alaOspfRestartExitReason,
       "alaOspfNbrAugTable": alaOspfNbrAugTable,
       "alaOspfNbrAugEntry": alaOspfNbrAugEntry,
       "alaOspfNbrRestartHelperStatus": alaOspfNbrRestartHelperStatus,
       "alaOspfNbrRestartHelperAge": alaOspfNbrRestartHelperAge,
       "alaOspfNbrRestartHelperExitReason": alaOspfNbrRestartHelperExitReason,
       "alaOspfNbrAreaId": alaOspfNbrAreaId,
       "alaOspfNbrDrAddress": alaOspfNbrDrAddress,
       "alaOspfNbrBdrAddress": alaOspfNbrBdrAddress,
       "alaOspfNbrType": alaOspfNbrType,
       "alaOspfNbrMode": alaOspfNbrMode,
       "alaOspfNbrMd5SeqNo": alaOspfNbrMd5SeqNo,
       "alaOspfNbrLastHello": alaOspfNbrLastHello,
       "alaOspfNbrPendingLSreq": alaOspfNbrPendingLSreq,
       "alaOspfNbrPendingLSack": alaOspfNbrPendingLSack,
       "alaOspfNbrPendingLSupd": alaOspfNbrPendingLSupd,
       "alaOspfVirtNbrAugTable": alaOspfVirtNbrAugTable,
       "alaOspfVirtNbrAugEntry": alaOspfVirtNbrAugEntry,
       "alaOspfVirtNbrRestartHelperStatus": alaOspfVirtNbrRestartHelperStatus,
       "alaOspfVirtNbrRestartHelperAge": alaOspfVirtNbrRestartHelperAge,
       "alaOspfVirtNbrRestartHelperExitReason": alaOspfVirtNbrRestartHelperExitReason,
       "alaOspfVirtNbrDrAddr": alaOspfVirtNbrDrAddr,
       "alaOspfVirtNbrBdrAddr": alaOspfVirtNbrBdrAddr,
       "alaOspfVirtNbrMode": alaOspfVirtNbrMode,
       "alaOspfVirtNbrMd5SeqNo": alaOspfVirtNbrMd5SeqNo,
       "alaOspfVirtNbrLastHello": alaOspfVirtNbrLastHello,
       "alaOspfVirtNbrPendingLSreq": alaOspfVirtNbrPendingLSreq,
       "alaOspfVirtNbrPendingLSack": alaOspfVirtNbrPendingLSack,
       "alaOspfVirtNbrPendingLSupd": alaOspfVirtNbrPendingLSupd,
       "alaOspfRestartInitiate": alaOspfRestartInitiate,
       "alaOspfAreaAugTable": alaOspfAreaAugTable,
       "alaOspfAreaAugEntry": alaOspfAreaAugEntry,
       "alaOspfAreaOperStatus": alaOspfAreaOperStatus,
       "alaOspfAreaLastSpfRun": alaOspfAreaLastSpfRun,
       "alaOspfAreaActiveVlinks": alaOspfAreaActiveVlinks,
       "alaOspfAreaIncrSpfRuns": alaOspfAreaIncrSpfRuns,
       "alaOspfAreaInitNbrs": alaOspfAreaInitNbrs,
       "alaOspfAreaExchNbrs": alaOspfAreaExchNbrs,
       "alaOspfAreaFullNbrs": alaOspfAreaFullNbrs,
       "alaOspfAreaNumIntfs": alaOspfAreaNumIntfs,
       "alaOspfAreaAttachedIntfs": alaOspfAreaAttachedIntfs,
       "alaOspfArea2WayNbrs": alaOspfArea2WayNbrs,
       "alaOspfAreaNssaTranslatorRole": alaOspfAreaNssaTranslatorRole,
       "alaOspfAreaNssaTranslatorStabilityInterval": alaOspfAreaNssaTranslatorStabilityInterval,
       "alaOspfAreaNssaImportSetPbit": alaOspfAreaNssaImportSetPbit,
       "alaOspfAreaNssaTranslatorState": alaOspfAreaNssaTranslatorState,
       "alaOspfAreaNssaElectedTranslatorRouterId": alaOspfAreaNssaElectedTranslatorRouterId,
       "alaOspfExtLsdbAugTable": alaOspfExtLsdbAugTable,
       "alaOspfExtLsdbAugEntry": alaOspfExtLsdbAugEntry,
       "alaOspfExtLsdbProto": alaOspfExtLsdbProto,
       "alaOspfExtLsdbRouteTag": alaOspfExtLsdbRouteTag,
       "alaOspfExtLsdbFwdAddr": alaOspfExtLsdbFwdAddr,
       "alaOspfExtLsdbMetricType": alaOspfExtLsdbMetricType,
       "alaOspfExtLsdbMetric": alaOspfExtLsdbMetric,
       "alaOspfExtLsdbLength": alaOspfExtLsdbLength,
       "alaOspfExtLsdbMask": alaOspfExtLsdbMask,
       "alaOspfAreaAggregateAugTable": alaOspfAreaAggregateAugTable,
       "alaOspfAreaAggregateAugEntry": alaOspfAreaAggregateAugEntry,
       "alaOspfAreaAggregateMetric": alaOspfAreaAggregateMetric,
       "alaOspfDefaultOriginate": alaOspfDefaultOriginate,
       "alaOspfDefaultOriginateMetricType": alaOspfDefaultOriginateMetricType,
       "alaOspfDefaultOriginateMetric": alaOspfDefaultOriginateMetric,
       "alaOspfBfdStatus": alaOspfBfdStatus,
       "alaOspfBfdAllInterfaceStatus": alaOspfBfdAllInterfaceStatus,
       "alaOspfOpaqueTransitCapability": alaOspfOpaqueTransitCapability,
       "alaOspfGeneralTable": alaOspfGeneralTable,
       "alaOspfTotalSpfRuns": alaOspfTotalSpfRuns,
       "alaOspfTotalIncrSpfRuns": alaOspfTotalIncrSpfRuns,
       "alaOspfTotalInitNbrs": alaOspfTotalInitNbrs,
       "alaOspfTotalExchNbrs": alaOspfTotalExchNbrs,
       "alaOspfTotalFullNbrs": alaOspfTotalFullNbrs,
       "alaOspfTotalAreas": alaOspfTotalAreas,
       "alaOspfTotalActiveAreas": alaOspfTotalActiveAreas,
       "alaOspfTotalTransitAreas": alaOspfTotalTransitAreas,
       "alaOspfTotalNSSA": alaOspfTotalNSSA,
       "alaOspfTotal2wayNbrs": alaOspfTotal2wayNbrs,
       "alcatelIND1OSPFMIBConformance": alcatelIND1OSPFMIBConformance,
       "alcatelIND1OSPFMIBGroups": alcatelIND1OSPFMIBGroups,
       "alaOspfMiscellaneousGroup": alaOspfMiscellaneousGroup,
       "alaOspfRouteGroup": alaOspfRouteGroup,
       "alaOspfBdrRouterGroup": alaOspfBdrRouterGroup,
       "alaOspfIfMd5Group": alaOspfIfMd5Group,
       "alaOspfGeneralGroup": alaOspfGeneralGroup,
       "alaOspfAreaAugEntryGroup": alaOspfAreaAugEntryGroup,
       "alaOspfAreaAggregateAugEntryGroup": alaOspfAreaAggregateAugEntryGroup,
       "alaOspfIfAugGroup": alaOspfIfAugGroup,
       "alaOspfExtLsdbAugGroup": alaOspfExtLsdbAugGroup,
       "alaOspfNbrAugGroup": alaOspfNbrAugGroup,
       "alaOspfVirtIfAugGroup": alaOspfVirtIfAugGroup,
       "alaOspfVirtNbrAugGroup": alaOspfVirtNbrAugGroup,
       "alcatelIND1OSPFMIBCompliances": alcatelIND1OSPFMIBCompliances,
       "alcatelIND1OSPFMIBCompliance": alcatelIND1OSPFMIBCompliance}
)
