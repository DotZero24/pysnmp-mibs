# SNMP MIB module (SUPERMICRO-OSPFMI-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFMI-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:44 2025
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

(BigMetric,
 TOSType,
 fsMIStdOspfContextId) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTDOSPF-MIB",
    "BigMetric",
    "TOSType",
    "fsMIStdOspfContextId")


# MODULE-IDENTITY

fsMIOspfTestGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147)
)
if mibBuilder.loadTexts:
    fsMIOspfTestGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIOspfBRRouteTable_Object = MibTable
fsMIOspfBRRouteTable = _FsMIOspfBRRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfBRRouteTable.setStatus("current")
_FsMIOspfBRRouteEntry_Object = MibTableRow
fsMIOspfBRRouteEntry = _FsMIOspfBRRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1)
)
fsMIOspfBRRouteEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfBRRouteIpAddr"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfBRRouteIpAddrMask"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfBRRouteIpTos"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfBRRouteIpNextHop"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfBRRouteDestType"),
)
if mibBuilder.loadTexts:
    fsMIOspfBRRouteEntry.setStatus("current")
_FsMIOspfBRRouteIpAddr_Type = IpAddress
_FsMIOspfBRRouteIpAddr_Object = MibTableColumn
fsMIOspfBRRouteIpAddr = _FsMIOspfBRRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 1),
    _FsMIOspfBRRouteIpAddr_Type()
)
fsMIOspfBRRouteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteIpAddr.setStatus("current")
_FsMIOspfBRRouteIpAddrMask_Type = IpAddress
_FsMIOspfBRRouteIpAddrMask_Object = MibTableColumn
fsMIOspfBRRouteIpAddrMask = _FsMIOspfBRRouteIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 2),
    _FsMIOspfBRRouteIpAddrMask_Type()
)
fsMIOspfBRRouteIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteIpAddrMask.setStatus("current")
_FsMIOspfBRRouteIpTos_Type = Unsigned32
_FsMIOspfBRRouteIpTos_Object = MibTableColumn
fsMIOspfBRRouteIpTos = _FsMIOspfBRRouteIpTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 3),
    _FsMIOspfBRRouteIpTos_Type()
)
fsMIOspfBRRouteIpTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteIpTos.setStatus("current")
_FsMIOspfBRRouteIpNextHop_Type = IpAddress
_FsMIOspfBRRouteIpNextHop_Object = MibTableColumn
fsMIOspfBRRouteIpNextHop = _FsMIOspfBRRouteIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 4),
    _FsMIOspfBRRouteIpNextHop_Type()
)
fsMIOspfBRRouteIpNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteIpNextHop.setStatus("current")


class _FsMIOspfBRRouteDestType_Type(Integer32):
    """Custom type fsMIOspfBRRouteDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("areaBorder", 2),
          ("asBoundary", 3))
    )


_FsMIOspfBRRouteDestType_Type.__name__ = "Integer32"
_FsMIOspfBRRouteDestType_Object = MibTableColumn
fsMIOspfBRRouteDestType = _FsMIOspfBRRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 5),
    _FsMIOspfBRRouteDestType_Type()
)
fsMIOspfBRRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteDestType.setStatus("current")


class _FsMIOspfBRRouteType_Type(Integer32):
    """Custom type fsMIOspfBRRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intraArea", 1),
          ("interArea", 2))
    )


_FsMIOspfBRRouteType_Type.__name__ = "Integer32"
_FsMIOspfBRRouteType_Object = MibTableColumn
fsMIOspfBRRouteType = _FsMIOspfBRRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 6),
    _FsMIOspfBRRouteType_Type()
)
fsMIOspfBRRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteType.setStatus("current")
_FsMIOspfBRRouteAreaId_Type = IpAddress
_FsMIOspfBRRouteAreaId_Object = MibTableColumn
fsMIOspfBRRouteAreaId = _FsMIOspfBRRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 7),
    _FsMIOspfBRRouteAreaId_Type()
)
fsMIOspfBRRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteAreaId.setStatus("current")
_FsMIOspfBRRouteCost_Type = BigMetric
_FsMIOspfBRRouteCost_Object = MibTableColumn
fsMIOspfBRRouteCost = _FsMIOspfBRRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 8),
    _FsMIOspfBRRouteCost_Type()
)
fsMIOspfBRRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteCost.setStatus("current")


class _FsMIOspfBRRouteInterfaceIndex_Type(Integer32):
    """Custom type fsMIOspfBRRouteInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfBRRouteInterfaceIndex_Type.__name__ = "Integer32"
_FsMIOspfBRRouteInterfaceIndex_Object = MibTableColumn
fsMIOspfBRRouteInterfaceIndex = _FsMIOspfBRRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 1, 1, 9),
    _FsMIOspfBRRouteInterfaceIndex_Type()
)
fsMIOspfBRRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfBRRouteInterfaceIndex.setStatus("current")
_FsMIOspfExtRouteTable_Object = MibTable
fsMIOspfExtRouteTable = _FsMIOspfExtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfExtRouteTable.setStatus("current")
_FsMIOspfExtRouteEntry_Object = MibTableRow
fsMIOspfExtRouteEntry = _FsMIOspfExtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1)
)
fsMIOspfExtRouteEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfExtRouteDest"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfExtRouteMask"),
    (0, "SUPERMICRO-OSPFMI-TEST-MIB", "fsMIOspfExtRouteTOS"),
)
if mibBuilder.loadTexts:
    fsMIOspfExtRouteEntry.setStatus("current")
_FsMIOspfExtRouteDest_Type = IpAddress
_FsMIOspfExtRouteDest_Object = MibTableColumn
fsMIOspfExtRouteDest = _FsMIOspfExtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 1),
    _FsMIOspfExtRouteDest_Type()
)
fsMIOspfExtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteDest.setStatus("current")
_FsMIOspfExtRouteMask_Type = IpAddress
_FsMIOspfExtRouteMask_Object = MibTableColumn
fsMIOspfExtRouteMask = _FsMIOspfExtRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 2),
    _FsMIOspfExtRouteMask_Type()
)
fsMIOspfExtRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteMask.setStatus("current")
_FsMIOspfExtRouteTOS_Type = TOSType
_FsMIOspfExtRouteTOS_Object = MibTableColumn
fsMIOspfExtRouteTOS = _FsMIOspfExtRouteTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 3),
    _FsMIOspfExtRouteTOS_Type()
)
fsMIOspfExtRouteTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteTOS.setStatus("current")
_FsMIOspfExtRouteMetric_Type = BigMetric
_FsMIOspfExtRouteMetric_Object = MibTableColumn
fsMIOspfExtRouteMetric = _FsMIOspfExtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 4),
    _FsMIOspfExtRouteMetric_Type()
)
fsMIOspfExtRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteMetric.setStatus("current")


class _FsMIOspfExtRouteMetricType_Type(Integer32):
    """Custom type fsMIOspfExtRouteMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asexttype1", 1),
          ("asexttype2", 2))
    )


_FsMIOspfExtRouteMetricType_Type.__name__ = "Integer32"
_FsMIOspfExtRouteMetricType_Object = MibTableColumn
fsMIOspfExtRouteMetricType = _FsMIOspfExtRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 5),
    _FsMIOspfExtRouteMetricType_Type()
)
fsMIOspfExtRouteMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteMetricType.setStatus("current")


class _FsMIOspfExtRouteTag_Type(Integer32):
    """Custom type fsMIOspfExtRouteTag based on Integer32"""
    defaultValue = 0


_FsMIOspfExtRouteTag_Type.__name__ = "Integer32"
_FsMIOspfExtRouteTag_Object = MibTableColumn
fsMIOspfExtRouteTag = _FsMIOspfExtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 6),
    _FsMIOspfExtRouteTag_Type()
)
fsMIOspfExtRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteTag.setStatus("current")
_FsMIOspfExtRouteFwdAdr_Type = IpAddress
_FsMIOspfExtRouteFwdAdr_Object = MibTableColumn
fsMIOspfExtRouteFwdAdr = _FsMIOspfExtRouteFwdAdr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 7),
    _FsMIOspfExtRouteFwdAdr_Type()
)
fsMIOspfExtRouteFwdAdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteFwdAdr.setStatus("current")


class _FsMIOspfExtRouteIfIndex_Type(Integer32):
    """Custom type fsMIOspfExtRouteIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfExtRouteIfIndex_Type.__name__ = "Integer32"
_FsMIOspfExtRouteIfIndex_Object = MibTableColumn
fsMIOspfExtRouteIfIndex = _FsMIOspfExtRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 8),
    _FsMIOspfExtRouteIfIndex_Type()
)
fsMIOspfExtRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteIfIndex.setStatus("current")
_FsMIOspfExtRouteNextHop_Type = IpAddress
_FsMIOspfExtRouteNextHop_Object = MibTableColumn
fsMIOspfExtRouteNextHop = _FsMIOspfExtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 9),
    _FsMIOspfExtRouteNextHop_Type()
)
fsMIOspfExtRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteNextHop.setStatus("current")
_FsMIOspfExtRouteStatus_Type = RowStatus
_FsMIOspfExtRouteStatus_Object = MibTableColumn
fsMIOspfExtRouteStatus = _FsMIOspfExtRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 2, 1, 10),
    _FsMIOspfExtRouteStatus_Type()
)
fsMIOspfExtRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfExtRouteStatus.setStatus("current")
_FsMIOspfGrTestGroup_ObjectIdentity = ObjectIdentity
fsMIOspfGrTestGroup = _FsMIOspfGrTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 100)
)
_FsMIOspfGrTable_Object = MibTable
fsMIOspfGrTable = _FsMIOspfGrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 100, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfGrTable.setStatus("current")
_FsMIOspfGrEntry_Object = MibTableRow
fsMIOspfGrEntry = _FsMIOspfGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 100, 2, 1)
)
fsMIOspfGrEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
)
if mibBuilder.loadTexts:
    fsMIOspfGrEntry.setStatus("current")


class _FsMIOspfGrShutdown_Type(Integer32):
    """Custom type fsMIOspfGrShutdown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unplanned", 2))
    )


_FsMIOspfGrShutdown_Type.__name__ = "Integer32"
_FsMIOspfGrShutdown_Object = MibTableColumn
fsMIOspfGrShutdown = _FsMIOspfGrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 147, 100, 2, 1, 1),
    _FsMIOspfGrShutdown_Type()
)
fsMIOspfGrShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfGrShutdown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFMI-TEST-MIB",
    **{"fsMIOspfTestGroup": fsMIOspfTestGroup,
       "fsMIOspfBRRouteTable": fsMIOspfBRRouteTable,
       "fsMIOspfBRRouteEntry": fsMIOspfBRRouteEntry,
       "fsMIOspfBRRouteIpAddr": fsMIOspfBRRouteIpAddr,
       "fsMIOspfBRRouteIpAddrMask": fsMIOspfBRRouteIpAddrMask,
       "fsMIOspfBRRouteIpTos": fsMIOspfBRRouteIpTos,
       "fsMIOspfBRRouteIpNextHop": fsMIOspfBRRouteIpNextHop,
       "fsMIOspfBRRouteDestType": fsMIOspfBRRouteDestType,
       "fsMIOspfBRRouteType": fsMIOspfBRRouteType,
       "fsMIOspfBRRouteAreaId": fsMIOspfBRRouteAreaId,
       "fsMIOspfBRRouteCost": fsMIOspfBRRouteCost,
       "fsMIOspfBRRouteInterfaceIndex": fsMIOspfBRRouteInterfaceIndex,
       "fsMIOspfExtRouteTable": fsMIOspfExtRouteTable,
       "fsMIOspfExtRouteEntry": fsMIOspfExtRouteEntry,
       "fsMIOspfExtRouteDest": fsMIOspfExtRouteDest,
       "fsMIOspfExtRouteMask": fsMIOspfExtRouteMask,
       "fsMIOspfExtRouteTOS": fsMIOspfExtRouteTOS,
       "fsMIOspfExtRouteMetric": fsMIOspfExtRouteMetric,
       "fsMIOspfExtRouteMetricType": fsMIOspfExtRouteMetricType,
       "fsMIOspfExtRouteTag": fsMIOspfExtRouteTag,
       "fsMIOspfExtRouteFwdAdr": fsMIOspfExtRouteFwdAdr,
       "fsMIOspfExtRouteIfIndex": fsMIOspfExtRouteIfIndex,
       "fsMIOspfExtRouteNextHop": fsMIOspfExtRouteNextHop,
       "fsMIOspfExtRouteStatus": fsMIOspfExtRouteStatus,
       "fsMIOspfGrTestGroup": fsMIOspfGrTestGroup,
       "fsMIOspfGrTable": fsMIOspfGrTable,
       "fsMIOspfGrEntry": fsMIOspfGrEntry,
       "fsMIOspfGrShutdown": fsMIOspfGrShutdown}
)
