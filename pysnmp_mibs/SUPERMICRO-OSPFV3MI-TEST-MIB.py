# SNMP MIB module (SUPERMICRO-OSPFV3MI-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFV3MI-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:33 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(fsMIStdOspfv3ContextId,) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTDOSPFV3-MIB",
    "fsMIStdOspfv3ContextId")


# MODULE-IDENTITY

fsMIOspfv3TestGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100)
)
if mibBuilder.loadTexts:
    fsMIOspfv3TestGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIOspfv3TestIfTable_Object = MibTable
fsMIOspfv3TestIfTable = _FsMIOspfv3TestIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3TestIfTable.setStatus("current")
_FsMIOspfv3TestIfEntry_Object = MibTableRow
fsMIOspfv3TestIfEntry = _FsMIOspfv3TestIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 1, 1)
)
fsMIOspfv3TestIfEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3TestIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3TestIfEntry.setStatus("current")
_FsMIOspfv3TestIfIndex_Type = InterfaceIndex
_FsMIOspfv3TestIfIndex_Object = MibTableColumn
fsMIOspfv3TestIfIndex = _FsMIOspfv3TestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 1, 1, 1),
    _FsMIOspfv3TestIfIndex_Type()
)
fsMIOspfv3TestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3TestIfIndex.setStatus("current")


class _FsMIOspfv3TestDemandTraffic_Type(Integer32):
    """Custom type fsMIOspfv3TestDemandTraffic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_FsMIOspfv3TestDemandTraffic_Type.__name__ = "Integer32"
_FsMIOspfv3TestDemandTraffic_Object = MibTableColumn
fsMIOspfv3TestDemandTraffic = _FsMIOspfv3TestDemandTraffic_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 1, 1, 2),
    _FsMIOspfv3TestDemandTraffic_Type()
)
fsMIOspfv3TestDemandTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3TestDemandTraffic.setStatus("current")
_FsMIOspfv3TestIfContextId_Type = Integer32
_FsMIOspfv3TestIfContextId_Object = MibTableColumn
fsMIOspfv3TestIfContextId = _FsMIOspfv3TestIfContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 1, 1, 3),
    _FsMIOspfv3TestIfContextId_Type()
)
fsMIOspfv3TestIfContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3TestIfContextId.setStatus("current")
_FsMIOspfv3ExtRouteTable_Object = MibTable
fsMIOspfv3ExtRouteTable = _FsMIOspfv3ExtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteTable.setStatus("current")
_FsMIOspfv3ExtRouteEntry_Object = MibTableRow
fsMIOspfv3ExtRouteEntry = _FsMIOspfv3ExtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1)
)
fsMIOspfv3ExtRouteEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3ExtRouteDestType"),
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3ExtRouteDest"),
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3ExtRoutePfxLength"),
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3ExtRouteNextHopType"),
    (0, "SUPERMICRO-OSPFV3MI-TEST-MIB", "fsMIOspfv3ExtRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteEntry.setStatus("current")
_FsMIOspfv3ExtRouteDestType_Type = InetAddressType
_FsMIOspfv3ExtRouteDestType_Object = MibTableColumn
fsMIOspfv3ExtRouteDestType = _FsMIOspfv3ExtRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 1),
    _FsMIOspfv3ExtRouteDestType_Type()
)
fsMIOspfv3ExtRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteDestType.setStatus("current")


class _FsMIOspfv3ExtRouteDest_Type(InetAddress):
    """Custom type fsMIOspfv3ExtRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3ExtRouteDest_Type.__name__ = "InetAddress"
_FsMIOspfv3ExtRouteDest_Object = MibTableColumn
fsMIOspfv3ExtRouteDest = _FsMIOspfv3ExtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 2),
    _FsMIOspfv3ExtRouteDest_Type()
)
fsMIOspfv3ExtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteDest.setStatus("current")
_FsMIOspfv3ExtRoutePfxLength_Type = InetAddressPrefixLength
_FsMIOspfv3ExtRoutePfxLength_Object = MibTableColumn
fsMIOspfv3ExtRoutePfxLength = _FsMIOspfv3ExtRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 3),
    _FsMIOspfv3ExtRoutePfxLength_Type()
)
fsMIOspfv3ExtRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRoutePfxLength.setStatus("current")
_FsMIOspfv3ExtRouteNextHopType_Type = InetAddressType
_FsMIOspfv3ExtRouteNextHopType_Object = MibTableColumn
fsMIOspfv3ExtRouteNextHopType = _FsMIOspfv3ExtRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 4),
    _FsMIOspfv3ExtRouteNextHopType_Type()
)
fsMIOspfv3ExtRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteNextHopType.setStatus("current")


class _FsMIOspfv3ExtRouteNextHop_Type(InetAddress):
    """Custom type fsMIOspfv3ExtRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3ExtRouteNextHop_Type.__name__ = "InetAddress"
_FsMIOspfv3ExtRouteNextHop_Object = MibTableColumn
fsMIOspfv3ExtRouteNextHop = _FsMIOspfv3ExtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 5),
    _FsMIOspfv3ExtRouteNextHop_Type()
)
fsMIOspfv3ExtRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteNextHop.setStatus("current")
_FsMIOspfv3ExtRouteStatus_Type = RowStatus
_FsMIOspfv3ExtRouteStatus_Object = MibTableColumn
fsMIOspfv3ExtRouteStatus = _FsMIOspfv3ExtRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 24, 100, 2, 1, 6),
    _FsMIOspfv3ExtRouteStatus_Type()
)
fsMIOspfv3ExtRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtRouteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFV3MI-TEST-MIB",
    **{"fsMIOspfv3TestGroup": fsMIOspfv3TestGroup,
       "fsMIOspfv3TestIfTable": fsMIOspfv3TestIfTable,
       "fsMIOspfv3TestIfEntry": fsMIOspfv3TestIfEntry,
       "fsMIOspfv3TestIfIndex": fsMIOspfv3TestIfIndex,
       "fsMIOspfv3TestDemandTraffic": fsMIOspfv3TestDemandTraffic,
       "fsMIOspfv3TestIfContextId": fsMIOspfv3TestIfContextId,
       "fsMIOspfv3ExtRouteTable": fsMIOspfv3ExtRouteTable,
       "fsMIOspfv3ExtRouteEntry": fsMIOspfv3ExtRouteEntry,
       "fsMIOspfv3ExtRouteDestType": fsMIOspfv3ExtRouteDestType,
       "fsMIOspfv3ExtRouteDest": fsMIOspfv3ExtRouteDest,
       "fsMIOspfv3ExtRoutePfxLength": fsMIOspfv3ExtRoutePfxLength,
       "fsMIOspfv3ExtRouteNextHopType": fsMIOspfv3ExtRouteNextHopType,
       "fsMIOspfv3ExtRouteNextHop": fsMIOspfv3ExtRouteNextHop,
       "fsMIOspfv3ExtRouteStatus": fsMIOspfv3ExtRouteStatus}
)
