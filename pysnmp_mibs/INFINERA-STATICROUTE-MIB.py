# SNMP MIB module (INFINERA-STATICROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-STATICROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:12 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(infnNE,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "infnNE")

(InfnBlackHoleRouteStatus,
 InfnStaticRouteAction) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnBlackHoleRouteStatus",
    "InfnStaticRouteAction")

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

staticRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    staticRouteMIB.setRevisions(
        ("2017-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1)
)
staticRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")
_MoID_Type = DisplayString
_MoID_Object = MibTableColumn
moID = _MoID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 1),
    _MoID_Type()
)
moID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moID.setStatus("current")
_DestinationIP_Type = DisplayString
_DestinationIP_Object = MibTableColumn
destinationIP = _DestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 2),
    _DestinationIP_Type()
)
destinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationIP.setStatus("current")
_NextHop_Type = DisplayString
_NextHop_Object = MibTableColumn
nextHop = _NextHop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 3),
    _NextHop_Type()
)
nextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHop.setStatus("current")
_PrefixLength_Type = Unsigned32
_PrefixLength_Object = MibTableColumn
prefixLength = _PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 4),
    _PrefixLength_Type()
)
prefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prefixLength.setStatus("current")
_NextHopIntf_Type = DisplayString
_NextHopIntf_Object = MibTableColumn
nextHopIntf = _NextHopIntf_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 5),
    _NextHopIntf_Type()
)
nextHopIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopIntf.setStatus("current")
_Cost_Type = Unsigned32
_Cost_Object = MibTableColumn
cost = _Cost_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 6),
    _Cost_Type()
)
cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cost.setStatus("current")
_StaticRouteAction_Type = InfnStaticRouteAction
_StaticRouteAction_Object = MibTableColumn
staticRouteAction = _StaticRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 7),
    _StaticRouteAction_Type()
)
staticRouteAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteAction.setStatus("current")
_BlackHoleRoute_Type = InfnBlackHoleRouteStatus
_BlackHoleRoute_Object = MibTableColumn
blackHoleRoute = _BlackHoleRoute_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 1, 1, 8),
    _BlackHoleRoute_Type()
)
blackHoleRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blackHoleRoute.setStatus("current")
_StaticRouteConformance_ObjectIdentity = ObjectIdentity
staticRouteConformance = _StaticRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 2)
)
_StaticRouteCompliances_ObjectIdentity = ObjectIdentity
staticRouteCompliances = _StaticRouteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 2, 1)
)
_StaticRouteGroups_ObjectIdentity = ObjectIdentity
staticRouteGroups = _StaticRouteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 2, 2)
)

# Managed Objects groups

staticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 2, 2, 1)
)
staticRouteGroup.setObjects(
      *(("INFINERA-STATICROUTE-MIB", "moID"),
        ("INFINERA-STATICROUTE-MIB", "destinationIP"),
        ("INFINERA-STATICROUTE-MIB", "nextHop"),
        ("INFINERA-STATICROUTE-MIB", "prefixLength"),
        ("INFINERA-STATICROUTE-MIB", "nextHopIntf"),
        ("INFINERA-STATICROUTE-MIB", "cost"),
        ("INFINERA-STATICROUTE-MIB", "staticRouteAction"),
        ("INFINERA-STATICROUTE-MIB", "blackHoleRoute"))
)
if mibBuilder.loadTexts:
    staticRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

staticRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 5, 2, 1, 1)
)
staticRouteCompliance.setObjects(
    ("INFINERA-STATICROUTE-MIB", "staticRouteGroup")
)
if mibBuilder.loadTexts:
    staticRouteCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-STATICROUTE-MIB",
    **{"staticRouteMIB": staticRouteMIB,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "moID": moID,
       "destinationIP": destinationIP,
       "nextHop": nextHop,
       "prefixLength": prefixLength,
       "nextHopIntf": nextHopIntf,
       "cost": cost,
       "staticRouteAction": staticRouteAction,
       "blackHoleRoute": blackHoleRoute,
       "staticRouteConformance": staticRouteConformance,
       "staticRouteCompliances": staticRouteCompliances,
       "staticRouteCompliance": staticRouteCompliance,
       "staticRouteGroups": staticRouteGroups,
       "staticRouteGroup": staticRouteGroup}
)
