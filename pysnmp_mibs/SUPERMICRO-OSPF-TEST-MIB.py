# SNMP MIB module (SUPERMICRO-OSPF-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPF-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:01 2025
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

futOspfTestGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100)
)
if mibBuilder.loadTexts:
    futOspfTestGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BigMetric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TOSType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



# MIB Managed Objects in the order of their OIDs

_FutOspfBRRouteTable_Object = MibTable
futOspfBRRouteTable = _FutOspfBRRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1)
)
if mibBuilder.loadTexts:
    futOspfBRRouteTable.setStatus("current")
_FutOspfBRRouteEntry_Object = MibTableRow
futOspfBRRouteEntry = _FutOspfBRRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1)
)
futOspfBRRouteEntry.setIndexNames(
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfBRRouteIpAddr"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfBRRouteIpAddrMask"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfBRRouteIpTos"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfBRRouteIpNextHop"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfBRRouteDestType"),
)
if mibBuilder.loadTexts:
    futOspfBRRouteEntry.setStatus("current")
_FutOspfBRRouteIpAddr_Type = IpAddress
_FutOspfBRRouteIpAddr_Object = MibTableColumn
futOspfBRRouteIpAddr = _FutOspfBRRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 1),
    _FutOspfBRRouteIpAddr_Type()
)
futOspfBRRouteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfBRRouteIpAddr.setStatus("current")
_FutOspfBRRouteIpAddrMask_Type = IpAddress
_FutOspfBRRouteIpAddrMask_Object = MibTableColumn
futOspfBRRouteIpAddrMask = _FutOspfBRRouteIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 2),
    _FutOspfBRRouteIpAddrMask_Type()
)
futOspfBRRouteIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfBRRouteIpAddrMask.setStatus("current")
_FutOspfBRRouteIpTos_Type = Unsigned32
_FutOspfBRRouteIpTos_Object = MibTableColumn
futOspfBRRouteIpTos = _FutOspfBRRouteIpTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 3),
    _FutOspfBRRouteIpTos_Type()
)
futOspfBRRouteIpTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfBRRouteIpTos.setStatus("current")
_FutOspfBRRouteIpNextHop_Type = IpAddress
_FutOspfBRRouteIpNextHop_Object = MibTableColumn
futOspfBRRouteIpNextHop = _FutOspfBRRouteIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 4),
    _FutOspfBRRouteIpNextHop_Type()
)
futOspfBRRouteIpNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfBRRouteIpNextHop.setStatus("current")


class _FutOspfBRRouteDestType_Type(Integer32):
    """Custom type futOspfBRRouteDestType based on Integer32"""
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


_FutOspfBRRouteDestType_Type.__name__ = "Integer32"
_FutOspfBRRouteDestType_Object = MibTableColumn
futOspfBRRouteDestType = _FutOspfBRRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 5),
    _FutOspfBRRouteDestType_Type()
)
futOspfBRRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfBRRouteDestType.setStatus("current")


class _FutOspfBRRouteType_Type(Integer32):
    """Custom type futOspfBRRouteType based on Integer32"""
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


_FutOspfBRRouteType_Type.__name__ = "Integer32"
_FutOspfBRRouteType_Object = MibTableColumn
futOspfBRRouteType = _FutOspfBRRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 6),
    _FutOspfBRRouteType_Type()
)
futOspfBRRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfBRRouteType.setStatus("current")
_FutOspfBRRouteAreaId_Type = IpAddress
_FutOspfBRRouteAreaId_Object = MibTableColumn
futOspfBRRouteAreaId = _FutOspfBRRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 7),
    _FutOspfBRRouteAreaId_Type()
)
futOspfBRRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfBRRouteAreaId.setStatus("current")
_FutOspfBRRouteCost_Type = BigMetric
_FutOspfBRRouteCost_Object = MibTableColumn
futOspfBRRouteCost = _FutOspfBRRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 8),
    _FutOspfBRRouteCost_Type()
)
futOspfBRRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfBRRouteCost.setStatus("current")
_FutOspfBRRouteInterfaceIndex_Type = InterfaceIndex
_FutOspfBRRouteInterfaceIndex_Object = MibTableColumn
futOspfBRRouteInterfaceIndex = _FutOspfBRRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 1, 1, 9),
    _FutOspfBRRouteInterfaceIndex_Type()
)
futOspfBRRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfBRRouteInterfaceIndex.setStatus("current")
_FutOspfExtRouteTable_Object = MibTable
futOspfExtRouteTable = _FutOspfExtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2)
)
if mibBuilder.loadTexts:
    futOspfExtRouteTable.setStatus("current")
_FutOspfExtRouteEntry_Object = MibTableRow
futOspfExtRouteEntry = _FutOspfExtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1)
)
futOspfExtRouteEntry.setIndexNames(
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfExtRouteDest"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfExtRouteMask"),
    (0, "SUPERMICRO-OSPF-TEST-MIB", "futOspfExtRouteTOS"),
)
if mibBuilder.loadTexts:
    futOspfExtRouteEntry.setStatus("current")
_FutOspfExtRouteDest_Type = IpAddress
_FutOspfExtRouteDest_Object = MibTableColumn
futOspfExtRouteDest = _FutOspfExtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 1),
    _FutOspfExtRouteDest_Type()
)
futOspfExtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfExtRouteDest.setStatus("current")
_FutOspfExtRouteMask_Type = IpAddress
_FutOspfExtRouteMask_Object = MibTableColumn
futOspfExtRouteMask = _FutOspfExtRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 2),
    _FutOspfExtRouteMask_Type()
)
futOspfExtRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfExtRouteMask.setStatus("current")
_FutOspfExtRouteTOS_Type = TOSType
_FutOspfExtRouteTOS_Object = MibTableColumn
futOspfExtRouteTOS = _FutOspfExtRouteTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 3),
    _FutOspfExtRouteTOS_Type()
)
futOspfExtRouteTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfExtRouteTOS.setStatus("current")
_FutOspfExtRouteMetric_Type = BigMetric
_FutOspfExtRouteMetric_Object = MibTableColumn
futOspfExtRouteMetric = _FutOspfExtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 4),
    _FutOspfExtRouteMetric_Type()
)
futOspfExtRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteMetric.setStatus("current")


class _FutOspfExtRouteMetricType_Type(Integer32):
    """Custom type futOspfExtRouteMetricType based on Integer32"""
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


_FutOspfExtRouteMetricType_Type.__name__ = "Integer32"
_FutOspfExtRouteMetricType_Object = MibTableColumn
futOspfExtRouteMetricType = _FutOspfExtRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 5),
    _FutOspfExtRouteMetricType_Type()
)
futOspfExtRouteMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteMetricType.setStatus("current")


class _FutOspfExtRouteTag_Type(Integer32):
    """Custom type futOspfExtRouteTag based on Integer32"""
    defaultValue = 0


_FutOspfExtRouteTag_Type.__name__ = "Integer32"
_FutOspfExtRouteTag_Object = MibTableColumn
futOspfExtRouteTag = _FutOspfExtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 6),
    _FutOspfExtRouteTag_Type()
)
futOspfExtRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteTag.setStatus("current")
_FutOspfExtRouteFwdAdr_Type = IpAddress
_FutOspfExtRouteFwdAdr_Object = MibTableColumn
futOspfExtRouteFwdAdr = _FutOspfExtRouteFwdAdr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 7),
    _FutOspfExtRouteFwdAdr_Type()
)
futOspfExtRouteFwdAdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteFwdAdr.setStatus("current")


class _FutOspfExtRouteIfIndex_Type(InterfaceIndex):
    """Custom type futOspfExtRouteIfIndex based on InterfaceIndex"""
    defaultValue = 0

    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfExtRouteIfIndex_Type.__name__ = "InterfaceIndex"
_FutOspfExtRouteIfIndex_Object = MibTableColumn
futOspfExtRouteIfIndex = _FutOspfExtRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 8),
    _FutOspfExtRouteIfIndex_Type()
)
futOspfExtRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteIfIndex.setStatus("current")
_FutOspfExtRouteNextHop_Type = IpAddress
_FutOspfExtRouteNextHop_Object = MibTableColumn
futOspfExtRouteNextHop = _FutOspfExtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 9),
    _FutOspfExtRouteNextHop_Type()
)
futOspfExtRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteNextHop.setStatus("current")
_FutOspfExtRouteStatus_Type = RowStatus
_FutOspfExtRouteStatus_Object = MibTableColumn
futOspfExtRouteStatus = _FutOspfExtRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 2, 1, 10),
    _FutOspfExtRouteStatus_Type()
)
futOspfExtRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfExtRouteStatus.setStatus("current")
_FutOspfGrTestGroup_ObjectIdentity = ObjectIdentity
futOspfGrTestGroup = _FutOspfGrTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 100)
)


class _FutOspfGrShutdown_Type(Integer32):
    """Custom type futOspfGrShutdown based on Integer32"""
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


_FutOspfGrShutdown_Type.__name__ = "Integer32"
_FutOspfGrShutdown_Object = MibScalar
futOspfGrShutdown = _FutOspfGrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 10, 100, 100, 1),
    _FutOspfGrShutdown_Type()
)
futOspfGrShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfGrShutdown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPF-TEST-MIB",
    **{"BigMetric": BigMetric,
       "InterfaceIndex": InterfaceIndex,
       "TOSType": TOSType,
       "futOspfTestGroup": futOspfTestGroup,
       "futOspfBRRouteTable": futOspfBRRouteTable,
       "futOspfBRRouteEntry": futOspfBRRouteEntry,
       "futOspfBRRouteIpAddr": futOspfBRRouteIpAddr,
       "futOspfBRRouteIpAddrMask": futOspfBRRouteIpAddrMask,
       "futOspfBRRouteIpTos": futOspfBRRouteIpTos,
       "futOspfBRRouteIpNextHop": futOspfBRRouteIpNextHop,
       "futOspfBRRouteDestType": futOspfBRRouteDestType,
       "futOspfBRRouteType": futOspfBRRouteType,
       "futOspfBRRouteAreaId": futOspfBRRouteAreaId,
       "futOspfBRRouteCost": futOspfBRRouteCost,
       "futOspfBRRouteInterfaceIndex": futOspfBRRouteInterfaceIndex,
       "futOspfExtRouteTable": futOspfExtRouteTable,
       "futOspfExtRouteEntry": futOspfExtRouteEntry,
       "futOspfExtRouteDest": futOspfExtRouteDest,
       "futOspfExtRouteMask": futOspfExtRouteMask,
       "futOspfExtRouteTOS": futOspfExtRouteTOS,
       "futOspfExtRouteMetric": futOspfExtRouteMetric,
       "futOspfExtRouteMetricType": futOspfExtRouteMetricType,
       "futOspfExtRouteTag": futOspfExtRouteTag,
       "futOspfExtRouteFwdAdr": futOspfExtRouteFwdAdr,
       "futOspfExtRouteIfIndex": futOspfExtRouteIfIndex,
       "futOspfExtRouteNextHop": futOspfExtRouteNextHop,
       "futOspfExtRouteStatus": futOspfExtRouteStatus,
       "futOspfGrTestGroup": futOspfGrTestGroup,
       "futOspfGrShutdown": futOspfGrShutdown}
)
