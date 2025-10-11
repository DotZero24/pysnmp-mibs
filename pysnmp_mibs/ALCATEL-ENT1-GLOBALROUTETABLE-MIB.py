# SNMP MIB module (ALCATEL-ENT1-GLOBALROUTETABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-GLOBALROUTETABLE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:08:52 2025
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

(routingIND1GlobalRouteTable,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1GlobalRouteTable")

(Ipv6Address,
 Ipv6IfIndex) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1GRTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GRTMIB.setRevisions(
        ("2014-02-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaGrtRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1GRTMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBObjects = _AlcatelIND1GRTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1)
)
_AlaGrtConfig_ObjectIdentity = ObjectIdentity
alaGrtConfig = _AlaGrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1)
)
_AlaGrtRouteTable_Object = MibTable
alaGrtRouteTable = _AlaGrtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaGrtRouteTable.setStatus("current")
_AlaGrtRouteEntry_Object = MibTableRow
alaGrtRouteEntry = _AlaGrtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1)
)
alaGrtRouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteDistinguisher"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteDest"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteMaskLen"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaGrtRouteEntry.setStatus("current")
_AlaGrtRouteDistinguisher_Type = AlaGrtRouteDistinguisher
_AlaGrtRouteDistinguisher_Object = MibTableColumn
alaGrtRouteDistinguisher = _AlaGrtRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 1),
    _AlaGrtRouteDistinguisher_Type()
)
alaGrtRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDistinguisher.setStatus("current")
_AlaGrtRouteDest_Type = IpAddress
_AlaGrtRouteDest_Object = MibTableColumn
alaGrtRouteDest = _AlaGrtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 2),
    _AlaGrtRouteDest_Type()
)
alaGrtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDest.setStatus("current")
_AlaGrtRouteMaskLen_Type = Unsigned32
_AlaGrtRouteMaskLen_Object = MibTableColumn
alaGrtRouteMaskLen = _AlaGrtRouteMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 3),
    _AlaGrtRouteMaskLen_Type()
)
alaGrtRouteMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteMaskLen.setStatus("current")
_AlaGrtRouteNextHop_Type = IpAddress
_AlaGrtRouteNextHop_Object = MibTableColumn
alaGrtRouteNextHop = _AlaGrtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 4),
    _AlaGrtRouteNextHop_Type()
)
alaGrtRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteNextHop.setStatus("current")
_AlaGrtRouteMetric_Type = Unsigned32
_AlaGrtRouteMetric_Object = MibTableColumn
alaGrtRouteMetric = _AlaGrtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 5),
    _AlaGrtRouteMetric_Type()
)
alaGrtRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteMetric.setStatus("current")
_AlaGrtRouteTag_Type = Unsigned32
_AlaGrtRouteTag_Object = MibTableColumn
alaGrtRouteTag = _AlaGrtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 6),
    _AlaGrtRouteTag_Type()
)
alaGrtRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteTag.setStatus("current")


class _AlaGrtRouteVrfName_Type(OctetString):
    """Custom type alaGrtRouteVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaGrtRouteVrfName_Type.__name__ = "OctetString"
_AlaGrtRouteVrfName_Object = MibTableColumn
alaGrtRouteVrfName = _AlaGrtRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 7),
    _AlaGrtRouteVrfName_Type()
)
alaGrtRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteVrfName.setStatus("current")
_AlaGrtRouteIsid_Type = Unsigned32
_AlaGrtRouteIsid_Object = MibTableColumn
alaGrtRouteIsid = _AlaGrtRouteIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 8),
    _AlaGrtRouteIsid_Type()
)
alaGrtRouteIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteIsid.setStatus("current")
_AlaGrt6RouteTable_Object = MibTable
alaGrt6RouteTable = _AlaGrt6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaGrt6RouteTable.setStatus("current")
_AlaGrt6RouteEntry_Object = MibTableRow
alaGrt6RouteEntry = _AlaGrt6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1)
)
alaGrt6RouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteDistinguisher"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteDest"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteMaskLen"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteNextHop"),
    (0, "ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteIfIndex"),
)
if mibBuilder.loadTexts:
    alaGrt6RouteEntry.setStatus("current")
_AlaGrt6RouteDistinguisher_Type = AlaGrtRouteDistinguisher
_AlaGrt6RouteDistinguisher_Object = MibTableColumn
alaGrt6RouteDistinguisher = _AlaGrt6RouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 1),
    _AlaGrt6RouteDistinguisher_Type()
)
alaGrt6RouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrt6RouteDistinguisher.setStatus("current")
_AlaGrt6RouteDest_Type = Ipv6Address
_AlaGrt6RouteDest_Object = MibTableColumn
alaGrt6RouteDest = _AlaGrt6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 2),
    _AlaGrt6RouteDest_Type()
)
alaGrt6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrt6RouteDest.setStatus("current")
_AlaGrt6RouteMaskLen_Type = Unsigned32
_AlaGrt6RouteMaskLen_Object = MibTableColumn
alaGrt6RouteMaskLen = _AlaGrt6RouteMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 3),
    _AlaGrt6RouteMaskLen_Type()
)
alaGrt6RouteMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrt6RouteMaskLen.setStatus("current")
_AlaGrt6RouteNextHop_Type = Ipv6Address
_AlaGrt6RouteNextHop_Object = MibTableColumn
alaGrt6RouteNextHop = _AlaGrt6RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 4),
    _AlaGrt6RouteNextHop_Type()
)
alaGrt6RouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrt6RouteNextHop.setStatus("current")
_AlaGrt6RouteIfIndex_Type = Ipv6IfIndex
_AlaGrt6RouteIfIndex_Object = MibTableColumn
alaGrt6RouteIfIndex = _AlaGrt6RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 5),
    _AlaGrt6RouteIfIndex_Type()
)
alaGrt6RouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrt6RouteIfIndex.setStatus("current")
_AlaGrt6RouteMetric_Type = Unsigned32
_AlaGrt6RouteMetric_Object = MibTableColumn
alaGrt6RouteMetric = _AlaGrt6RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 6),
    _AlaGrt6RouteMetric_Type()
)
alaGrt6RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrt6RouteMetric.setStatus("current")
_AlaGrt6RouteTag_Type = Unsigned32
_AlaGrt6RouteTag_Object = MibTableColumn
alaGrt6RouteTag = _AlaGrt6RouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 7),
    _AlaGrt6RouteTag_Type()
)
alaGrt6RouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrt6RouteTag.setStatus("current")


class _AlaGrt6RouteVrfName_Type(OctetString):
    """Custom type alaGrt6RouteVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaGrt6RouteVrfName_Type.__name__ = "OctetString"
_AlaGrt6RouteVrfName_Object = MibTableColumn
alaGrt6RouteVrfName = _AlaGrt6RouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 2, 1, 8),
    _AlaGrt6RouteVrfName_Type()
)
alaGrt6RouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrt6RouteVrfName.setStatus("current")
_AlcatelIND1GRTMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBConformance = _AlcatelIND1GRTMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2)
)
_AlcatelIND1GRTMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBCompliances = _AlcatelIND1GRTMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1)
)
_AlcatelIND1GRTMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBGroups = _AlcatelIND1GRTMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2)
)

# Managed Objects groups

alaGrtConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2, 1)
)
alaGrtConfigMIBGroup.setObjects(
      *(("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteMetric"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteTag"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteVrfName"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtRouteIsid"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteMetric"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteTag"),
        ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrt6RouteVrfName"))
)
if mibBuilder.loadTexts:
    alaGrtConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaGrtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1, 1)
)
alaGrtCompliance.setObjects(
    ("ALCATEL-ENT1-GLOBALROUTETABLE-MIB", "alaGrtConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alaGrtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-GLOBALROUTETABLE-MIB",
    **{"AlaGrtRouteDistinguisher": AlaGrtRouteDistinguisher,
       "alcatelIND1GRTMIB": alcatelIND1GRTMIB,
       "alcatelIND1GRTMIBObjects": alcatelIND1GRTMIBObjects,
       "alaGrtConfig": alaGrtConfig,
       "alaGrtRouteTable": alaGrtRouteTable,
       "alaGrtRouteEntry": alaGrtRouteEntry,
       "alaGrtRouteDistinguisher": alaGrtRouteDistinguisher,
       "alaGrtRouteDest": alaGrtRouteDest,
       "alaGrtRouteMaskLen": alaGrtRouteMaskLen,
       "alaGrtRouteNextHop": alaGrtRouteNextHop,
       "alaGrtRouteMetric": alaGrtRouteMetric,
       "alaGrtRouteTag": alaGrtRouteTag,
       "alaGrtRouteVrfName": alaGrtRouteVrfName,
       "alaGrtRouteIsid": alaGrtRouteIsid,
       "alaGrt6RouteTable": alaGrt6RouteTable,
       "alaGrt6RouteEntry": alaGrt6RouteEntry,
       "alaGrt6RouteDistinguisher": alaGrt6RouteDistinguisher,
       "alaGrt6RouteDest": alaGrt6RouteDest,
       "alaGrt6RouteMaskLen": alaGrt6RouteMaskLen,
       "alaGrt6RouteNextHop": alaGrt6RouteNextHop,
       "alaGrt6RouteIfIndex": alaGrt6RouteIfIndex,
       "alaGrt6RouteMetric": alaGrt6RouteMetric,
       "alaGrt6RouteTag": alaGrt6RouteTag,
       "alaGrt6RouteVrfName": alaGrt6RouteVrfName,
       "alcatelIND1GRTMIBConformance": alcatelIND1GRTMIBConformance,
       "alcatelIND1GRTMIBCompliances": alcatelIND1GRTMIBCompliances,
       "alaGrtCompliance": alaGrtCompliance,
       "alcatelIND1GRTMIBGroups": alcatelIND1GRTMIBGroups,
       "alaGrtConfigMIBGroup": alaGrtConfigMIBGroup}
)
