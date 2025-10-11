# SNMP MIB module (SUPERMICRO-OSPFV3-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFV3-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:56 2025
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


# MODULE-IDENTITY

futOspfv3TestGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301)
)
if mibBuilder.loadTexts:
    futOspfv3TestGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FutOspfv3TestIfTable_Object = MibTable
futOspfv3TestIfTable = _FutOspfv3TestIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 1)
)
if mibBuilder.loadTexts:
    futOspfv3TestIfTable.setStatus("current")
_FutOspfv3TestIfEntry_Object = MibTableRow
futOspfv3TestIfEntry = _FutOspfv3TestIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 1, 1)
)
futOspfv3TestIfEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3TestIfIndex"),
)
if mibBuilder.loadTexts:
    futOspfv3TestIfEntry.setStatus("current")
_FutOspfv3TestIfIndex_Type = InterfaceIndex
_FutOspfv3TestIfIndex_Object = MibTableColumn
futOspfv3TestIfIndex = _FutOspfv3TestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 1, 1, 1),
    _FutOspfv3TestIfIndex_Type()
)
futOspfv3TestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3TestIfIndex.setStatus("current")


class _FutOspfv3TestDemandTraffic_Type(Integer32):
    """Custom type futOspfv3TestDemandTraffic based on Integer32"""
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


_FutOspfv3TestDemandTraffic_Type.__name__ = "Integer32"
_FutOspfv3TestDemandTraffic_Object = MibTableColumn
futOspfv3TestDemandTraffic = _FutOspfv3TestDemandTraffic_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 1, 1, 2),
    _FutOspfv3TestDemandTraffic_Type()
)
futOspfv3TestDemandTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3TestDemandTraffic.setStatus("current")
_FutOspfv3ExtRouteTable_Object = MibTable
futOspfv3ExtRouteTable = _FutOspfv3ExtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2)
)
if mibBuilder.loadTexts:
    futOspfv3ExtRouteTable.setStatus("current")
_FutOspfv3ExtRouteEntry_Object = MibTableRow
futOspfv3ExtRouteEntry = _FutOspfv3ExtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1)
)
futOspfv3ExtRouteEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3ExtRouteDestType"),
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3ExtRouteDest"),
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3ExtRoutePfxLength"),
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3ExtRouteNextHopType"),
    (0, "SUPERMICRO-OSPFV3-TEST-MIB", "futOspfv3ExtRouteNextHop"),
)
if mibBuilder.loadTexts:
    futOspfv3ExtRouteEntry.setStatus("current")
_FutOspfv3ExtRouteDestType_Type = InetAddressType
_FutOspfv3ExtRouteDestType_Object = MibTableColumn
futOspfv3ExtRouteDestType = _FutOspfv3ExtRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 1),
    _FutOspfv3ExtRouteDestType_Type()
)
futOspfv3ExtRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3ExtRouteDestType.setStatus("current")


class _FutOspfv3ExtRouteDest_Type(InetAddress):
    """Custom type futOspfv3ExtRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3ExtRouteDest_Type.__name__ = "InetAddress"
_FutOspfv3ExtRouteDest_Object = MibTableColumn
futOspfv3ExtRouteDest = _FutOspfv3ExtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 2),
    _FutOspfv3ExtRouteDest_Type()
)
futOspfv3ExtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3ExtRouteDest.setStatus("current")
_FutOspfv3ExtRoutePfxLength_Type = InetAddressPrefixLength
_FutOspfv3ExtRoutePfxLength_Object = MibTableColumn
futOspfv3ExtRoutePfxLength = _FutOspfv3ExtRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 3),
    _FutOspfv3ExtRoutePfxLength_Type()
)
futOspfv3ExtRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3ExtRoutePfxLength.setStatus("current")
_FutOspfv3ExtRouteNextHopType_Type = InetAddressType
_FutOspfv3ExtRouteNextHopType_Object = MibTableColumn
futOspfv3ExtRouteNextHopType = _FutOspfv3ExtRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 4),
    _FutOspfv3ExtRouteNextHopType_Type()
)
futOspfv3ExtRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3ExtRouteNextHopType.setStatus("current")


class _FutOspfv3ExtRouteNextHop_Type(InetAddress):
    """Custom type futOspfv3ExtRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3ExtRouteNextHop_Type.__name__ = "InetAddress"
_FutOspfv3ExtRouteNextHop_Object = MibTableColumn
futOspfv3ExtRouteNextHop = _FutOspfv3ExtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 5),
    _FutOspfv3ExtRouteNextHop_Type()
)
futOspfv3ExtRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3ExtRouteNextHop.setStatus("current")
_FutOspfv3ExtRouteStatus_Type = RowStatus
_FutOspfv3ExtRouteStatus_Object = MibTableColumn
futOspfv3ExtRouteStatus = _FutOspfv3ExtRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 301, 2, 1, 6),
    _FutOspfv3ExtRouteStatus_Type()
)
futOspfv3ExtRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfv3ExtRouteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFV3-TEST-MIB",
    **{"futOspfv3TestGroup": futOspfv3TestGroup,
       "futOspfv3TestIfTable": futOspfv3TestIfTable,
       "futOspfv3TestIfEntry": futOspfv3TestIfEntry,
       "futOspfv3TestIfIndex": futOspfv3TestIfIndex,
       "futOspfv3TestDemandTraffic": futOspfv3TestDemandTraffic,
       "futOspfv3ExtRouteTable": futOspfv3ExtRouteTable,
       "futOspfv3ExtRouteEntry": futOspfv3ExtRouteEntry,
       "futOspfv3ExtRouteDestType": futOspfv3ExtRouteDestType,
       "futOspfv3ExtRouteDest": futOspfv3ExtRouteDest,
       "futOspfv3ExtRoutePfxLength": futOspfv3ExtRoutePfxLength,
       "futOspfv3ExtRouteNextHopType": futOspfv3ExtRouteNextHopType,
       "futOspfv3ExtRouteNextHop": futOspfv3ExtRouteNextHop,
       "futOspfv3ExtRouteStatus": futOspfv3ExtRouteStatus}
)
