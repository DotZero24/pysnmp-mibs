# SNMP MIB module (MAIPU-STATICROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-STATICROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:01 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RouteMib_ObjectIdentity = ObjectIdentity
routeMib = _RouteMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81)
)
_StaticRoute_ObjectIdentity = ObjectIdentity
staticRoute = _StaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7)
)
_StaticIfRouteTable_Object = MibTable
staticIfRouteTable = _StaticIfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1)
)
if mibBuilder.loadTexts:
    staticIfRouteTable.setStatus("current")
_StaticIfRouteEntry_Object = MibTableRow
staticIfRouteEntry = _StaticIfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1)
)
staticIfRouteEntry.setIndexNames(
    (0, "MAIPU-STATICROUTE-MIB", "staticIfRouteVrfName"),
    (0, "MAIPU-STATICROUTE-MIB", "staticIfRouteDest"),
    (0, "MAIPU-STATICROUTE-MIB", "staticIfRouteMask"),
    (0, "MAIPU-STATICROUTE-MIB", "staticIfRouteIfName"),
)
if mibBuilder.loadTexts:
    staticIfRouteEntry.setStatus("current")


class _StaticIfRouteVrfName_Type(DisplayString):
    """Custom type staticIfRouteVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaticIfRouteVrfName_Type.__name__ = "DisplayString"
_StaticIfRouteVrfName_Object = MibScalar
staticIfRouteVrfName = _StaticIfRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 1),
    _StaticIfRouteVrfName_Type()
)
staticIfRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteVrfName.setStatus("current")
_StaticIfRouteDest_Type = IpAddress
_StaticIfRouteDest_Object = MibScalar
staticIfRouteDest = _StaticIfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 2),
    _StaticIfRouteDest_Type()
)
staticIfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteDest.setStatus("current")
_StaticIfRouteMask_Type = IpAddress
_StaticIfRouteMask_Object = MibScalar
staticIfRouteMask = _StaticIfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 3),
    _StaticIfRouteMask_Type()
)
staticIfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteMask.setStatus("current")


class _StaticIfRouteIfName_Type(DisplayString):
    """Custom type staticIfRouteIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_StaticIfRouteIfName_Type.__name__ = "DisplayString"
_StaticIfRouteIfName_Object = MibScalar
staticIfRouteIfName = _StaticIfRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 4),
    _StaticIfRouteIfName_Type()
)
staticIfRouteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteIfName.setStatus("current")


class _StaticIfRouteDistance_Type(Integer32):
    """Custom type staticIfRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StaticIfRouteDistance_Type.__name__ = "Integer32"
_StaticIfRouteDistance_Object = MibScalar
staticIfRouteDistance = _StaticIfRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 5),
    _StaticIfRouteDistance_Type()
)
staticIfRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteDistance.setStatus("current")
_StaticIfRouteRowStatus_Type = RowStatus
_StaticIfRouteRowStatus_Object = MibScalar
staticIfRouteRowStatus = _StaticIfRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 1, 1, 6),
    _StaticIfRouteRowStatus_Type()
)
staticIfRouteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIfRouteRowStatus.setStatus("current")
_StaticGwRouteTable_Object = MibTable
staticGwRouteTable = _StaticGwRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2)
)
if mibBuilder.loadTexts:
    staticGwRouteTable.setStatus("current")
_StaticGwRouteEntry_Object = MibTableRow
staticGwRouteEntry = _StaticGwRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1)
)
staticGwRouteEntry.setIndexNames(
    (0, "MAIPU-STATICROUTE-MIB", "staticGwRouteVrfName"),
    (0, "MAIPU-STATICROUTE-MIB", "staticGwRouteDest"),
    (0, "MAIPU-STATICROUTE-MIB", "staticGwRouteMask"),
    (0, "MAIPU-STATICROUTE-MIB", "staticGwRouteGw"),
    (0, "MAIPU-STATICROUTE-MIB", "staticGwRouteGwVrfName"),
)
if mibBuilder.loadTexts:
    staticGwRouteEntry.setStatus("current")


class _StaticGwRouteVrfName_Type(DisplayString):
    """Custom type staticGwRouteVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaticGwRouteVrfName_Type.__name__ = "DisplayString"
_StaticGwRouteVrfName_Object = MibScalar
staticGwRouteVrfName = _StaticGwRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 1),
    _StaticGwRouteVrfName_Type()
)
staticGwRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteVrfName.setStatus("current")
_StaticGwRouteDest_Type = IpAddress
_StaticGwRouteDest_Object = MibScalar
staticGwRouteDest = _StaticGwRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 2),
    _StaticGwRouteDest_Type()
)
staticGwRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteDest.setStatus("current")
_StaticGwRouteMask_Type = IpAddress
_StaticGwRouteMask_Object = MibScalar
staticGwRouteMask = _StaticGwRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 3),
    _StaticGwRouteMask_Type()
)
staticGwRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteMask.setStatus("current")
_StaticGwRouteGw_Type = IpAddress
_StaticGwRouteGw_Object = MibScalar
staticGwRouteGw = _StaticGwRouteGw_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 4),
    _StaticGwRouteGw_Type()
)
staticGwRouteGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteGw.setStatus("current")


class _StaticGwRouteGwVrfName_Type(DisplayString):
    """Custom type staticGwRouteGwVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaticGwRouteGwVrfName_Type.__name__ = "DisplayString"
_StaticGwRouteGwVrfName_Object = MibScalar
staticGwRouteGwVrfName = _StaticGwRouteGwVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 5),
    _StaticGwRouteGwVrfName_Type()
)
staticGwRouteGwVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteGwVrfName.setStatus("current")


class _StaticGwRouteDistance_Type(Integer32):
    """Custom type staticGwRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StaticGwRouteDistance_Type.__name__ = "Integer32"
_StaticGwRouteDistance_Object = MibScalar
staticGwRouteDistance = _StaticGwRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 6),
    _StaticGwRouteDistance_Type()
)
staticGwRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteDistance.setStatus("current")
_StaticGwRouteRowStatus_Type = RowStatus
_StaticGwRouteRowStatus_Object = MibScalar
staticGwRouteRowStatus = _StaticGwRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 7, 2, 1, 7),
    _StaticGwRouteRowStatus_Type()
)
staticGwRouteRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticGwRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-STATICROUTE-MIB",
    **{"routeMib": routeMib,
       "staticRoute": staticRoute,
       "staticIfRouteTable": staticIfRouteTable,
       "staticIfRouteEntry": staticIfRouteEntry,
       "staticIfRouteVrfName": staticIfRouteVrfName,
       "staticIfRouteDest": staticIfRouteDest,
       "staticIfRouteMask": staticIfRouteMask,
       "staticIfRouteIfName": staticIfRouteIfName,
       "staticIfRouteDistance": staticIfRouteDistance,
       "staticIfRouteRowStatus": staticIfRouteRowStatus,
       "staticGwRouteTable": staticGwRouteTable,
       "staticGwRouteEntry": staticGwRouteEntry,
       "staticGwRouteVrfName": staticGwRouteVrfName,
       "staticGwRouteDest": staticGwRouteDest,
       "staticGwRouteMask": staticGwRouteMask,
       "staticGwRouteGw": staticGwRouteGw,
       "staticGwRouteGwVrfName": staticGwRouteGwVrfName,
       "staticGwRouteDistance": staticGwRouteDistance,
       "staticGwRouteRowStatus": staticGwRouteRowStatus}
)
