# SNMP MIB module (MAIPU-POLICYROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-POLICYROUTE-MIB
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

policyRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_RouteMib_ObjectIdentity = ObjectIdentity
routeMib = _RouteMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81)
)


class _PolicyRouteLocal_Type(DisplayString):
    """Custom type policyRouteLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PolicyRouteLocal_Type.__name__ = "DisplayString"
_PolicyRouteLocal_Object = MibScalar
policyRouteLocal = _PolicyRouteLocal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 1),
    _PolicyRouteLocal_Type()
)
policyRouteLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRouteLocal.setStatus("current")
_PolicyRouteTable_Object = MibTable
policyRouteTable = _PolicyRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2)
)
if mibBuilder.loadTexts:
    policyRouteTable.setStatus("current")
_PolicyRouteEntry_Object = MibTableRow
policyRouteEntry = _PolicyRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1)
)
policyRouteEntry.setIndexNames(
    (0, "MAIPU-POLICYROUTE-MIB", "policyRouteIfindex"),
)
if mibBuilder.loadTexts:
    policyRouteEntry.setStatus("current")
_PolicyRouteIfindex_Type = Unsigned32
_PolicyRouteIfindex_Object = MibTableColumn
policyRouteIfindex = _PolicyRouteIfindex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 1),
    _PolicyRouteIfindex_Type()
)
policyRouteIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyRouteIfindex.setStatus("current")


class _PolicyRouteRoutemap_Type(DisplayString):
    """Custom type policyRouteRoutemap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PolicyRouteRoutemap_Type.__name__ = "DisplayString"
_PolicyRouteRoutemap_Object = MibTableColumn
policyRouteRoutemap = _PolicyRouteRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 2),
    _PolicyRouteRoutemap_Type()
)
policyRouteRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRouteRoutemap.setStatus("current")
_PolicyRouteCache_Type = EnabledStatus
_PolicyRouteCache_Object = MibTableColumn
policyRouteCache = _PolicyRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 3),
    _PolicyRouteCache_Type()
)
policyRouteCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRouteCache.setStatus("current")
_PolicyRouteRowStatus_Type = RowStatus
_PolicyRouteRowStatus_Object = MibTableColumn
policyRouteRowStatus = _PolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 4),
    _PolicyRouteRowStatus_Type()
)
policyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-POLICYROUTE-MIB",
    **{"EnabledStatus": EnabledStatus,
       "routeMib": routeMib,
       "policyRoute": policyRoute,
       "policyRouteLocal": policyRouteLocal,
       "policyRouteTable": policyRouteTable,
       "policyRouteEntry": policyRouteEntry,
       "policyRouteIfindex": policyRouteIfindex,
       "policyRouteRoutemap": policyRouteRoutemap,
       "policyRouteCache": policyRouteCache,
       "policyRouteRowStatus": policyRouteRowStatus}
)
