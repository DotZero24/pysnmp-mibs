# SNMP MIB module (MY-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-ROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:13 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

(BigMetric,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "BigMetric")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20)
)
if mibBuilder.loadTexts:
    myRouteMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MyRouteProtoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoigrp", 11),
          ("bbnspfigp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoeigrp", 16),
          ("max", 17))
    )



# MIB Managed Objects in the order of their OIDs

_MyRouteMIBObjects_ObjectIdentity = ObjectIdentity
myRouteMIBObjects = _MyRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1)
)
_MyRouteServiceStatus_Type = EnabledStatus
_MyRouteServiceStatus_Object = MibScalar
myRouteServiceStatus = _MyRouteServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 1),
    _MyRouteServiceStatus_Type()
)
myRouteServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRouteServiceStatus.setStatus("current")
_MyRoutingProtoInfoTable_Object = MibTable
myRoutingProtoInfoTable = _MyRoutingProtoInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    myRoutingProtoInfoTable.setStatus("current")
_MyRoutingProtoInfoEntry_Object = MibTableRow
myRoutingProtoInfoEntry = _MyRoutingProtoInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1)
)
myRoutingProtoInfoEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRoutingProtoInfoProtoType"),
    (0, "MY-ROUTE-MIB", "myRoutingProtoInfoGateWay"),
)
if mibBuilder.loadTexts:
    myRoutingProtoInfoEntry.setStatus("current")
_MyRoutingProtoInfoProtoType_Type = MyRouteProtoType
_MyRoutingProtoInfoProtoType_Object = MibTableColumn
myRoutingProtoInfoProtoType = _MyRoutingProtoInfoProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 1),
    _MyRoutingProtoInfoProtoType_Type()
)
myRoutingProtoInfoProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRoutingProtoInfoProtoType.setStatus("current")
_MyRoutingProtoInfoGateWay_Type = IpAddress
_MyRoutingProtoInfoGateWay_Object = MibTableColumn
myRoutingProtoInfoGateWay = _MyRoutingProtoInfoGateWay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 2),
    _MyRoutingProtoInfoGateWay_Type()
)
myRoutingProtoInfoGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRoutingProtoInfoGateWay.setStatus("current")
_MyRoutingProtoInfoDistance_Type = Unsigned32
_MyRoutingProtoInfoDistance_Object = MibTableColumn
myRoutingProtoInfoDistance = _MyRoutingProtoInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 3),
    _MyRoutingProtoInfoDistance_Type()
)
myRoutingProtoInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRoutingProtoInfoDistance.setStatus("current")
_MyRoutingProtoInfoLastUpdate_Type = TimeTicks
_MyRoutingProtoInfoLastUpdate_Object = MibTableColumn
myRoutingProtoInfoLastUpdate = _MyRoutingProtoInfoLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 4),
    _MyRoutingProtoInfoLastUpdate_Type()
)
myRoutingProtoInfoLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRoutingProtoInfoLastUpdate.setStatus("current")
_MyDefRoutingCfgTable_Object = MibTable
myDefRoutingCfgTable = _MyDefRoutingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    myDefRoutingCfgTable.setStatus("current")
_MyDefRoutingCfgEntry_Object = MibTableRow
myDefRoutingCfgEntry = _MyDefRoutingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1)
)
myDefRoutingCfgEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myDefRoutingCfgRoutingProtoType"),
)
if mibBuilder.loadTexts:
    myDefRoutingCfgEntry.setStatus("current")
_MyDefRoutingCfgRoutingProtoType_Type = MyRouteProtoType
_MyDefRoutingCfgRoutingProtoType_Object = MibTableColumn
myDefRoutingCfgRoutingProtoType = _MyDefRoutingCfgRoutingProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 1),
    _MyDefRoutingCfgRoutingProtoType_Type()
)
myDefRoutingCfgRoutingProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDefRoutingCfgRoutingProtoType.setStatus("current")


class _MyDefRoutingCfgAlways_Type(TruthValue):
    """Custom type myDefRoutingCfgAlways based on TruthValue"""
    defaultValue = 2


_MyDefRoutingCfgAlways_Type.__name__ = "TruthValue"
_MyDefRoutingCfgAlways_Object = MibTableColumn
myDefRoutingCfgAlways = _MyDefRoutingCfgAlways_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 2),
    _MyDefRoutingCfgAlways_Type()
)
myDefRoutingCfgAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myDefRoutingCfgAlways.setStatus("current")


class _MyDefRoutingCfgMetric_Type(Unsigned32):
    """Custom type myDefRoutingCfgMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_MyDefRoutingCfgMetric_Type.__name__ = "Unsigned32"
_MyDefRoutingCfgMetric_Object = MibTableColumn
myDefRoutingCfgMetric = _MyDefRoutingCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 3),
    _MyDefRoutingCfgMetric_Type()
)
myDefRoutingCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myDefRoutingCfgMetric.setStatus("current")


class _MyDefRoutingCfgMetricType_Type(Integer32):
    """Custom type myDefRoutingCfgMetricType based on Integer32"""
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


_MyDefRoutingCfgMetricType_Type.__name__ = "Integer32"
_MyDefRoutingCfgMetricType_Object = MibTableColumn
myDefRoutingCfgMetricType = _MyDefRoutingCfgMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 4),
    _MyDefRoutingCfgMetricType_Type()
)
myDefRoutingCfgMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDefRoutingCfgMetricType.setStatus("current")


class _MyDefRoutingCfgRouteMap_Type(DisplayString):
    """Custom type myDefRoutingCfgRouteMap based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDefRoutingCfgRouteMap_Type.__name__ = "DisplayString"
_MyDefRoutingCfgRouteMap_Object = MibTableColumn
myDefRoutingCfgRouteMap = _MyDefRoutingCfgRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 5),
    _MyDefRoutingCfgRouteMap_Type()
)
myDefRoutingCfgRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myDefRoutingCfgRouteMap.setStatus("current")
_MyDefRoutingCfgStatus_Type = RowStatus
_MyDefRoutingCfgStatus_Object = MibTableColumn
myDefRoutingCfgStatus = _MyDefRoutingCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 6),
    _MyDefRoutingCfgStatus_Type()
)
myDefRoutingCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myDefRoutingCfgStatus.setStatus("current")
_MyRouteMapMIBObjects_ObjectIdentity = ObjectIdentity
myRouteMapMIBObjects = _MyRouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2)
)
_MyRouteMapTable_Object = MibTable
myRouteMapTable = _MyRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    myRouteMapTable.setStatus("current")
_MyRouteMapEntry_Object = MibTableRow
myRouteMapEntry = _MyRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1)
)
myRouteMapEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRouteMapName"),
    (0, "MY-ROUTE-MIB", "myRouteMapSequenceNumber"),
)
if mibBuilder.loadTexts:
    myRouteMapEntry.setStatus("current")


class _MyRouteMapName_Type(DisplayString):
    """Custom type myRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyRouteMapName_Type.__name__ = "DisplayString"
_MyRouteMapName_Object = MibTableColumn
myRouteMapName = _MyRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 1),
    _MyRouteMapName_Type()
)
myRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapName.setStatus("current")


class _MyRouteMapSequenceNumber_Type(Unsigned32):
    """Custom type myRouteMapSequenceNumber based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyRouteMapSequenceNumber_Type.__name__ = "Unsigned32"
_MyRouteMapSequenceNumber_Object = MibTableColumn
myRouteMapSequenceNumber = _MyRouteMapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 2),
    _MyRouteMapSequenceNumber_Type()
)
myRouteMapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapSequenceNumber.setStatus("current")


class _MyRouteMapOperType_Type(Integer32):
    """Custom type myRouteMapOperType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_MyRouteMapOperType_Type.__name__ = "Integer32"
_MyRouteMapOperType_Object = MibTableColumn
myRouteMapOperType = _MyRouteMapOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 3),
    _MyRouteMapOperType_Type()
)
myRouteMapOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapOperType.setStatus("current")


class _MyRouteMapMatchMetric_Type(Unsigned32):
    """Custom type myRouteMapMatchMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyRouteMapMatchMetric_Type.__name__ = "Unsigned32"
_MyRouteMapMatchMetric_Object = MibTableColumn
myRouteMapMatchMetric = _MyRouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 4),
    _MyRouteMapMatchMetric_Type()
)
myRouteMapMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMatchMetric.setStatus("current")


class _MyRouteMapMatchRouteType_Type(Integer32):
    """Custom type myRouteMapMatchRouteType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notMatch", 0),
          ("internal", 1),
          ("external", 2),
          ("external-type1", 3),
          ("external-type2", 4))
    )


_MyRouteMapMatchRouteType_Type.__name__ = "Integer32"
_MyRouteMapMatchRouteType_Object = MibTableColumn
myRouteMapMatchRouteType = _MyRouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 5),
    _MyRouteMapMatchRouteType_Type()
)
myRouteMapMatchRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMatchRouteType.setStatus("current")


class _MyRouteMapMetricValueType_Type(Integer32):
    """Custom type myRouteMapMetricValueType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 0),
          ("replace", 1),
          ("add", 2),
          ("reduce", 3))
    )


_MyRouteMapMetricValueType_Type.__name__ = "Integer32"
_MyRouteMapMetricValueType_Object = MibTableColumn
myRouteMapMetricValueType = _MyRouteMapMetricValueType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 6),
    _MyRouteMapMetricValueType_Type()
)
myRouteMapMetricValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMetricValueType.setStatus("current")


class _MyRouteMapSetMetric_Type(Unsigned32):
    """Custom type myRouteMapSetMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MyRouteMapSetMetric_Type.__name__ = "Unsigned32"
_MyRouteMapSetMetric_Object = MibTableColumn
myRouteMapSetMetric = _MyRouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 7),
    _MyRouteMapSetMetric_Type()
)
myRouteMapSetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapSetMetric.setStatus("current")


class _MyRouteMapSetLevel_Type(Integer32):
    """Custom type myRouteMapSetLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("stubarea", 1),
          ("backbone", 2))
    )


_MyRouteMapSetLevel_Type.__name__ = "Integer32"
_MyRouteMapSetLevel_Object = MibTableColumn
myRouteMapSetLevel = _MyRouteMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 8),
    _MyRouteMapSetLevel_Type()
)
myRouteMapSetLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapSetLevel.setStatus("current")


class _MyRouteMapSetMetricType_Type(Integer32):
    """Custom type myRouteMapSetMetricType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 0),
          ("internal", 1),
          ("external", 2),
          ("type1", 3),
          ("type2", 4))
    )


_MyRouteMapSetMetricType_Type.__name__ = "Integer32"
_MyRouteMapSetMetricType_Object = MibTableColumn
myRouteMapSetMetricType = _MyRouteMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 9),
    _MyRouteMapSetMetricType_Type()
)
myRouteMapSetMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapSetMetricType.setStatus("current")


class _MyRouteMapSetNexthopSt_Type(ConfigStatus):
    """Custom type myRouteMapSetNexthopSt based on ConfigStatus"""
    defaultValue = 2


_MyRouteMapSetNexthopSt_Type.__name__ = "ConfigStatus"
_MyRouteMapSetNexthopSt_Object = MibTableColumn
myRouteMapSetNexthopSt = _MyRouteMapSetNexthopSt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 10),
    _MyRouteMapSetNexthopSt_Type()
)
myRouteMapSetNexthopSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRouteMapSetNexthopSt.setStatus("current")
_MyRouteMapSetNexthop_Type = IpAddress
_MyRouteMapSetNexthop_Object = MibTableColumn
myRouteMapSetNexthop = _MyRouteMapSetNexthop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 11),
    _MyRouteMapSetNexthop_Type()
)
myRouteMapSetNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapSetNexthop.setStatus("current")
_MyRouteMapStatus_Type = RowStatus
_MyRouteMapStatus_Object = MibTableColumn
myRouteMapStatus = _MyRouteMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 12),
    _MyRouteMapStatus_Type()
)
myRouteMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapStatus.setStatus("current")
_MyRouteMapMatchIpAddressTable_Object = MibTable
myRouteMapMatchIpAddressTable = _MyRouteMapMatchIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    myRouteMapMatchIpAddressTable.setStatus("current")
_MyRouteMapMatchIpAddressEntry_Object = MibTableRow
myRouteMapMatchIpAddressEntry = _MyRouteMapMatchIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1)
)
myRouteMapMatchIpAddressEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRouteMapName"),
    (0, "MY-ROUTE-MIB", "myRouteMapSequenceNumber"),
    (0, "MY-ROUTE-MIB", "myRouteMapMatchType"),
    (0, "MY-ROUTE-MIB", "myRouteMapMatchIpAddressAclName"),
)
if mibBuilder.loadTexts:
    myRouteMapMatchIpAddressEntry.setStatus("current")


class _MyRouteMapMatchType_Type(Integer32):
    """Custom type myRouteMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("nextHop", 2),
          ("source", 3))
    )


_MyRouteMapMatchType_Type.__name__ = "Integer32"
_MyRouteMapMatchType_Object = MibTableColumn
myRouteMapMatchType = _MyRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 1),
    _MyRouteMapMatchType_Type()
)
myRouteMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapMatchType.setStatus("current")


class _MyRouteMapMatchIpAddressAclName_Type(DisplayString):
    """Custom type myRouteMapMatchIpAddressAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyRouteMapMatchIpAddressAclName_Type.__name__ = "DisplayString"
_MyRouteMapMatchIpAddressAclName_Object = MibTableColumn
myRouteMapMatchIpAddressAclName = _MyRouteMapMatchIpAddressAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 2),
    _MyRouteMapMatchIpAddressAclName_Type()
)
myRouteMapMatchIpAddressAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapMatchIpAddressAclName.setStatus("current")
_MyRouteMapMatchIpAddressStatus_Type = RowStatus
_MyRouteMapMatchIpAddressStatus_Object = MibTableColumn
myRouteMapMatchIpAddressStatus = _MyRouteMapMatchIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 3),
    _MyRouteMapMatchIpAddressStatus_Type()
)
myRouteMapMatchIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMatchIpAddressStatus.setStatus("current")
_MyRouteMapMatchTagTable_Object = MibTable
myRouteMapMatchTagTable = _MyRouteMapMatchTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3)
)
if mibBuilder.loadTexts:
    myRouteMapMatchTagTable.setStatus("current")
_MyRouteMapMatchTagEntry_Object = MibTableRow
myRouteMapMatchTagEntry = _MyRouteMapMatchTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1)
)
myRouteMapMatchTagEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRouteMapName"),
    (0, "MY-ROUTE-MIB", "myRouteMapSequenceNumber"),
    (0, "MY-ROUTE-MIB", "myRouteMapMatchTagValue"),
)
if mibBuilder.loadTexts:
    myRouteMapMatchTagEntry.setStatus("current")


class _MyRouteMapMatchTagValue_Type(Unsigned32):
    """Custom type myRouteMapMatchTagValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyRouteMapMatchTagValue_Type.__name__ = "Unsigned32"
_MyRouteMapMatchTagValue_Object = MibTableColumn
myRouteMapMatchTagValue = _MyRouteMapMatchTagValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1, 1),
    _MyRouteMapMatchTagValue_Type()
)
myRouteMapMatchTagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapMatchTagValue.setStatus("current")
_MyRouteMapMatchTagStatus_Type = RowStatus
_MyRouteMapMatchTagStatus_Object = MibTableColumn
myRouteMapMatchTagStatus = _MyRouteMapMatchTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1, 2),
    _MyRouteMapMatchTagStatus_Type()
)
myRouteMapMatchTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMatchTagStatus.setStatus("current")
_MyRouteMapMatchInterfaceTable_Object = MibTable
myRouteMapMatchInterfaceTable = _MyRouteMapMatchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4)
)
if mibBuilder.loadTexts:
    myRouteMapMatchInterfaceTable.setStatus("current")
_MyRouteMapMatchInterfaceEntry_Object = MibTableRow
myRouteMapMatchInterfaceEntry = _MyRouteMapMatchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1)
)
myRouteMapMatchInterfaceEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRouteMapName"),
    (0, "MY-ROUTE-MIB", "myRouteMapSequenceNumber"),
    (0, "MY-ROUTE-MIB", "myRouteMapMatchInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    myRouteMapMatchInterfaceEntry.setStatus("current")
_MyRouteMapMatchInterfaceIfIndex_Type = IfIndex
_MyRouteMapMatchInterfaceIfIndex_Object = MibTableColumn
myRouteMapMatchInterfaceIfIndex = _MyRouteMapMatchInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1, 1),
    _MyRouteMapMatchInterfaceIfIndex_Type()
)
myRouteMapMatchInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteMapMatchInterfaceIfIndex.setStatus("current")
_MyRouteMapMatchInterfaceStatus_Type = RowStatus
_MyRouteMapMatchInterfaceStatus_Object = MibTableColumn
myRouteMapMatchInterfaceStatus = _MyRouteMapMatchInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1, 2),
    _MyRouteMapMatchInterfaceStatus_Type()
)
myRouteMapMatchInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteMapMatchInterfaceStatus.setStatus("current")
_MyRouteRedistributeMIBObjects_ObjectIdentity = ObjectIdentity
myRouteRedistributeMIBObjects = _MyRouteRedistributeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3)
)
_MyRouteRedistributeTable_Object = MibTable
myRouteRedistributeTable = _MyRouteRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    myRouteRedistributeTable.setStatus("current")
_MyRouteRedistributeEntry_Object = MibTableRow
myRouteRedistributeEntry = _MyRouteRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1)
)
myRouteRedistributeEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myRouteRedistributeProtocolCfg"),
    (0, "MY-ROUTE-MIB", "myRouteRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    myRouteRedistributeEntry.setStatus("current")
_MyRouteRedistributeProtocolCfg_Type = MyRouteProtoType
_MyRouteRedistributeProtocolCfg_Object = MibTableColumn
myRouteRedistributeProtocolCfg = _MyRouteRedistributeProtocolCfg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 1),
    _MyRouteRedistributeProtocolCfg_Type()
)
myRouteRedistributeProtocolCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteRedistributeProtocolCfg.setStatus("current")
_MyRouteRedistributeProtocol_Type = MyRouteProtoType
_MyRouteRedistributeProtocol_Object = MibTableColumn
myRouteRedistributeProtocol = _MyRouteRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 2),
    _MyRouteRedistributeProtocol_Type()
)
myRouteRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRouteRedistributeProtocol.setStatus("current")


class _MyRouteRedistributeMetricValue_Type(Unsigned32):
    """Custom type myRouteRedistributeMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_MyRouteRedistributeMetricValue_Type.__name__ = "Unsigned32"
_MyRouteRedistributeMetricValue_Object = MibTableColumn
myRouteRedistributeMetricValue = _MyRouteRedistributeMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 3),
    _MyRouteRedistributeMetricValue_Type()
)
myRouteRedistributeMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteRedistributeMetricValue.setStatus("current")


class _MyRouteRedistributeMetricType_Type(Integer32):
    """Custom type myRouteRedistributeMetricType based on Integer32"""
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


_MyRouteRedistributeMetricType_Type.__name__ = "Integer32"
_MyRouteRedistributeMetricType_Object = MibTableColumn
myRouteRedistributeMetricType = _MyRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 4),
    _MyRouteRedistributeMetricType_Type()
)
myRouteRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteRedistributeMetricType.setStatus("current")


class _MyRouteRedistributeTagValue_Type(Unsigned32):
    """Custom type myRouteRedistributeTagValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MyRouteRedistributeTagValue_Type.__name__ = "Unsigned32"
_MyRouteRedistributeTagValue_Object = MibTableColumn
myRouteRedistributeTagValue = _MyRouteRedistributeTagValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 5),
    _MyRouteRedistributeTagValue_Type()
)
myRouteRedistributeTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteRedistributeTagValue.setStatus("current")


class _MyRouteRedistributeRouteMapName_Type(DisplayString):
    """Custom type myRouteRedistributeRouteMapName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyRouteRedistributeRouteMapName_Type.__name__ = "DisplayString"
_MyRouteRedistributeRouteMapName_Object = MibTableColumn
myRouteRedistributeRouteMapName = _MyRouteRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 6),
    _MyRouteRedistributeRouteMapName_Type()
)
myRouteRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteRedistributeRouteMapName.setStatus("current")
_MyRouteRedistributeStatus_Type = RowStatus
_MyRouteRedistributeStatus_Object = MibTableColumn
myRouteRedistributeStatus = _MyRouteRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 7),
    _MyRouteRedistributeStatus_Type()
)
myRouteRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRouteRedistributeStatus.setStatus("current")
_MyRouteFilteringMIBObjects_ObjectIdentity = ObjectIdentity
myRouteFilteringMIBObjects = _MyRouteFilteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4)
)
_MyIpPrefixListTable_Object = MibTable
myIpPrefixListTable = _MyIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    myIpPrefixListTable.setStatus("current")
_MyIpPrefixListEntry_Object = MibTableRow
myIpPrefixListEntry = _MyIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1)
)
myIpPrefixListEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myIpPrefixListName"),
    (0, "MY-ROUTE-MIB", "myIpPrefixListSequence"),
)
if mibBuilder.loadTexts:
    myIpPrefixListEntry.setStatus("current")


class _MyIpPrefixListName_Type(DisplayString):
    """Custom type myIpPrefixListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyIpPrefixListName_Type.__name__ = "DisplayString"
_MyIpPrefixListName_Object = MibTableColumn
myIpPrefixListName = _MyIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 1),
    _MyIpPrefixListName_Type()
)
myIpPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIpPrefixListName.setStatus("current")


class _MyIpPrefixListSequence_Type(Unsigned32):
    """Custom type myIpPrefixListSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyIpPrefixListSequence_Type.__name__ = "Unsigned32"
_MyIpPrefixListSequence_Object = MibTableColumn
myIpPrefixListSequence = _MyIpPrefixListSequence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 2),
    _MyIpPrefixListSequence_Type()
)
myIpPrefixListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIpPrefixListSequence.setStatus("current")


class _MyIpPrefixListOperMethod_Type(Integer32):
    """Custom type myIpPrefixListOperMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_MyIpPrefixListOperMethod_Type.__name__ = "Integer32"
_MyIpPrefixListOperMethod_Object = MibTableColumn
myIpPrefixListOperMethod = _MyIpPrefixListOperMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 3),
    _MyIpPrefixListOperMethod_Type()
)
myIpPrefixListOperMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpPrefixListOperMethod.setStatus("current")
_MyIpPrefixListIpAddress_Type = IpAddress
_MyIpPrefixListIpAddress_Object = MibTableColumn
myIpPrefixListIpAddress = _MyIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 4),
    _MyIpPrefixListIpAddress_Type()
)
myIpPrefixListIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpPrefixListIpAddress.setStatus("current")


class _MyIpPrefixListMaskLength_Type(Unsigned32):
    """Custom type myIpPrefixListMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MyIpPrefixListMaskLength_Type.__name__ = "Unsigned32"
_MyIpPrefixListMaskLength_Object = MibTableColumn
myIpPrefixListMaskLength = _MyIpPrefixListMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 5),
    _MyIpPrefixListMaskLength_Type()
)
myIpPrefixListMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpPrefixListMaskLength.setStatus("current")


class _MyIpPrefixListMinimumPrefixLength_Type(Unsigned32):
    """Custom type myIpPrefixListMinimumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MyIpPrefixListMinimumPrefixLength_Type.__name__ = "Unsigned32"
_MyIpPrefixListMinimumPrefixLength_Object = MibTableColumn
myIpPrefixListMinimumPrefixLength = _MyIpPrefixListMinimumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 6),
    _MyIpPrefixListMinimumPrefixLength_Type()
)
myIpPrefixListMinimumPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpPrefixListMinimumPrefixLength.setStatus("current")


class _MyIpPrefixListMaximumPrefixLength_Type(Unsigned32):
    """Custom type myIpPrefixListMaximumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MyIpPrefixListMaximumPrefixLength_Type.__name__ = "Unsigned32"
_MyIpPrefixListMaximumPrefixLength_Object = MibTableColumn
myIpPrefixListMaximumPrefixLength = _MyIpPrefixListMaximumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 7),
    _MyIpPrefixListMaximumPrefixLength_Type()
)
myIpPrefixListMaximumPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpPrefixListMaximumPrefixLength.setStatus("current")
_MyIpPrefixListStatus_Type = RowStatus
_MyIpPrefixListStatus_Object = MibTableColumn
myIpPrefixListStatus = _MyIpPrefixListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 8),
    _MyIpPrefixListStatus_Type()
)
myIpPrefixListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myIpPrefixListStatus.setStatus("current")
_MyDistributeListTable_Object = MibTable
myDistributeListTable = _MyDistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2)
)
if mibBuilder.loadTexts:
    myDistributeListTable.setStatus("current")
_MyDistributeListEntry_Object = MibTableRow
myDistributeListEntry = _MyDistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1)
)
myDistributeListEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myDistributeListCfgProtoType"),
    (0, "MY-ROUTE-MIB", "myDistributeListIfIndex"),
    (0, "MY-ROUTE-MIB", "myDistributeListDirection"),
    (0, "MY-ROUTE-MIB", "myDistributeListFilteringProtocol"),
)
if mibBuilder.loadTexts:
    myDistributeListEntry.setStatus("current")
_MyDistributeListCfgProtoType_Type = MyRouteProtoType
_MyDistributeListCfgProtoType_Object = MibTableColumn
myDistributeListCfgProtoType = _MyDistributeListCfgProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 1),
    _MyDistributeListCfgProtoType_Type()
)
myDistributeListCfgProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDistributeListCfgProtoType.setStatus("current")
_MyDistributeListIfIndex_Type = Unsigned32
_MyDistributeListIfIndex_Object = MibTableColumn
myDistributeListIfIndex = _MyDistributeListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 2),
    _MyDistributeListIfIndex_Type()
)
myDistributeListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDistributeListIfIndex.setStatus("current")


class _MyDistributeListDirection_Type(Integer32):
    """Custom type myDistributeListDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("out", 1),
          ("in", 2))
    )


_MyDistributeListDirection_Type.__name__ = "Integer32"
_MyDistributeListDirection_Object = MibTableColumn
myDistributeListDirection = _MyDistributeListDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 3),
    _MyDistributeListDirection_Type()
)
myDistributeListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDistributeListDirection.setStatus("current")
_MyDistributeListFilteringProtocol_Type = Unsigned32
_MyDistributeListFilteringProtocol_Object = MibTableColumn
myDistributeListFilteringProtocol = _MyDistributeListFilteringProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 4),
    _MyDistributeListFilteringProtocol_Type()
)
myDistributeListFilteringProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDistributeListFilteringProtocol.setStatus("current")


class _MyDistributeListFilterType_Type(Integer32):
    """Custom type myDistributeListFilterType based on Integer32"""
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
        *(("acl", 1),
          ("gateway", 2),
          ("prefix", 3),
          ("prefix-gateway", 4))
    )


_MyDistributeListFilterType_Type.__name__ = "Integer32"
_MyDistributeListFilterType_Object = MibTableColumn
myDistributeListFilterType = _MyDistributeListFilterType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 5),
    _MyDistributeListFilterType_Type()
)
myDistributeListFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDistributeListFilterType.setStatus("current")


class _MyDistributeListAclName_Type(DisplayString):
    """Custom type myDistributeListAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDistributeListAclName_Type.__name__ = "DisplayString"
_MyDistributeListAclName_Object = MibTableColumn
myDistributeListAclName = _MyDistributeListAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 6),
    _MyDistributeListAclName_Type()
)
myDistributeListAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDistributeListAclName.setStatus("current")


class _MyDistributeListGateWayIpPrefixName_Type(DisplayString):
    """Custom type myDistributeListGateWayIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDistributeListGateWayIpPrefixName_Type.__name__ = "DisplayString"
_MyDistributeListGateWayIpPrefixName_Object = MibTableColumn
myDistributeListGateWayIpPrefixName = _MyDistributeListGateWayIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 7),
    _MyDistributeListGateWayIpPrefixName_Type()
)
myDistributeListGateWayIpPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDistributeListGateWayIpPrefixName.setStatus("current")


class _MyDistributeListPrefixIpPrefixName_Type(DisplayString):
    """Custom type myDistributeListPrefixIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDistributeListPrefixIpPrefixName_Type.__name__ = "DisplayString"
_MyDistributeListPrefixIpPrefixName_Object = MibTableColumn
myDistributeListPrefixIpPrefixName = _MyDistributeListPrefixIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 8),
    _MyDistributeListPrefixIpPrefixName_Type()
)
myDistributeListPrefixIpPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDistributeListPrefixIpPrefixName.setStatus("current")
_MyDistributeListStatus_Type = RowStatus
_MyDistributeListStatus_Object = MibTableColumn
myDistributeListStatus = _MyDistributeListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 9),
    _MyDistributeListStatus_Type()
)
myDistributeListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myDistributeListStatus.setStatus("current")
_MyipCidrRouteExtendMIBObjects_ObjectIdentity = ObjectIdentity
myipCidrRouteExtendMIBObjects = _MyipCidrRouteExtendMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5)
)
_MyipCidrRouteTable_Object = MibTable
myipCidrRouteTable = _MyipCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    myipCidrRouteTable.setStatus("current")
_MyipCidrRouteEntry_Object = MibTableRow
myipCidrRouteEntry = _MyipCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1)
)
myipCidrRouteEntry.setIndexNames(
    (0, "MY-ROUTE-MIB", "myipCidrRouteDest"),
    (0, "MY-ROUTE-MIB", "myipCidrRouteMask"),
    (0, "MY-ROUTE-MIB", "myipCidrRouteTos"),
    (0, "MY-ROUTE-MIB", "myipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    myipCidrRouteEntry.setStatus("current")
_MyipCidrRouteDest_Type = IpAddress
_MyipCidrRouteDest_Object = MibTableColumn
myipCidrRouteDest = _MyipCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 1),
    _MyipCidrRouteDest_Type()
)
myipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteDest.setStatus("current")
_MyipCidrRouteMask_Type = IpAddress
_MyipCidrRouteMask_Object = MibTableColumn
myipCidrRouteMask = _MyipCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 2),
    _MyipCidrRouteMask_Type()
)
myipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteMask.setStatus("current")
_MyipCidrRouteTos_Type = Integer32
_MyipCidrRouteTos_Object = MibTableColumn
myipCidrRouteTos = _MyipCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 3),
    _MyipCidrRouteTos_Type()
)
myipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteTos.setStatus("current")
_MyipCidrRouteNextHop_Type = IpAddress
_MyipCidrRouteNextHop_Object = MibTableColumn
myipCidrRouteNextHop = _MyipCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 4),
    _MyipCidrRouteNextHop_Type()
)
myipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteNextHop.setStatus("current")


class _MyipCidrRouteIfIndex_Type(Integer32):
    """Custom type myipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_MyipCidrRouteIfIndex_Type.__name__ = "Integer32"
_MyipCidrRouteIfIndex_Object = MibTableColumn
myipCidrRouteIfIndex = _MyipCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 5),
    _MyipCidrRouteIfIndex_Type()
)
myipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteIfIndex.setStatus("current")


class _MyipCidrRouteType_Type(Integer32):
    """Custom type myipCidrRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_MyipCidrRouteType_Type.__name__ = "Integer32"
_MyipCidrRouteType_Object = MibTableColumn
myipCidrRouteType = _MyipCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 6),
    _MyipCidrRouteType_Type()
)
myipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteType.setStatus("current")


class _MyipCidrRouteProto_Type(Integer32):
    """Custom type myipCidrRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("policy", 17))
    )


_MyipCidrRouteProto_Type.__name__ = "Integer32"
_MyipCidrRouteProto_Object = MibTableColumn
myipCidrRouteProto = _MyipCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 7),
    _MyipCidrRouteProto_Type()
)
myipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteProto.setStatus("current")


class _MyipCidrRouteAge_Type(Integer32):
    """Custom type myipCidrRouteAge based on Integer32"""
    defaultValue = 0


_MyipCidrRouteAge_Type.__name__ = "Integer32"
_MyipCidrRouteAge_Object = MibTableColumn
myipCidrRouteAge = _MyipCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 8),
    _MyipCidrRouteAge_Type()
)
myipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrRouteAge.setStatus("current")
_MyipCidrRouteInfo_Type = ObjectIdentifier
_MyipCidrRouteInfo_Object = MibTableColumn
myipCidrRouteInfo = _MyipCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 9),
    _MyipCidrRouteInfo_Type()
)
myipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteInfo.setStatus("current")


class _MyipCidrRouteNextHopAS_Type(Integer32):
    """Custom type myipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_MyipCidrRouteNextHopAS_Type.__name__ = "Integer32"
_MyipCidrRouteNextHopAS_Object = MibTableColumn
myipCidrRouteNextHopAS = _MyipCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 10),
    _MyipCidrRouteNextHopAS_Type()
)
myipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteNextHopAS.setStatus("current")


class _MyipCidrRouteMetric1_Type(Integer32):
    """Custom type myipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_MyipCidrRouteMetric1_Type.__name__ = "Integer32"
_MyipCidrRouteMetric1_Object = MibTableColumn
myipCidrRouteMetric1 = _MyipCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 11),
    _MyipCidrRouteMetric1_Type()
)
myipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteMetric1.setStatus("current")


class _MyipCidrRouteMetric2_Type(Integer32):
    """Custom type myipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_MyipCidrRouteMetric2_Type.__name__ = "Integer32"
_MyipCidrRouteMetric2_Object = MibTableColumn
myipCidrRouteMetric2 = _MyipCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 12),
    _MyipCidrRouteMetric2_Type()
)
myipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteMetric2.setStatus("current")


class _MyipCidrRouteMetric3_Type(Integer32):
    """Custom type myipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_MyipCidrRouteMetric3_Type.__name__ = "Integer32"
_MyipCidrRouteMetric3_Object = MibTableColumn
myipCidrRouteMetric3 = _MyipCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 13),
    _MyipCidrRouteMetric3_Type()
)
myipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteMetric3.setStatus("current")


class _MyipCidrRouteMetric4_Type(Integer32):
    """Custom type myipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_MyipCidrRouteMetric4_Type.__name__ = "Integer32"
_MyipCidrRouteMetric4_Object = MibTableColumn
myipCidrRouteMetric4 = _MyipCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 14),
    _MyipCidrRouteMetric4_Type()
)
myipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteMetric4.setStatus("current")


class _MyipCidrRouteMetric5_Type(Integer32):
    """Custom type myipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_MyipCidrRouteMetric5_Type.__name__ = "Integer32"
_MyipCidrRouteMetric5_Object = MibTableColumn
myipCidrRouteMetric5 = _MyipCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 15),
    _MyipCidrRouteMetric5_Type()
)
myipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteMetric5.setStatus("current")
_MyipCidrRouteStatus_Type = RowStatus
_MyipCidrRouteStatus_Object = MibTableColumn
myipCidrRouteStatus = _MyipCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 16),
    _MyipCidrRouteStatus_Type()
)
myipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myipCidrRouteStatus.setStatus("current")


class _MyipCidrOspfRouteType_Type(Integer32):
    """Custom type myipCidrOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ospf-route", 0),
          ("ospf-ia-route", 1),
          ("ospf-n1-route", 2),
          ("ospf-n2-route", 3),
          ("ospf-e1-route", 4),
          ("ospf-e2-route", 5))
    )


_MyipCidrOspfRouteType_Type.__name__ = "Integer32"
_MyipCidrOspfRouteType_Object = MibTableColumn
myipCidrOspfRouteType = _MyipCidrOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 17),
    _MyipCidrOspfRouteType_Type()
)
myipCidrOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myipCidrOspfRouteType.setStatus("current")
_MyRouteMIBConformance_ObjectIdentity = ObjectIdentity
myRouteMIBConformance = _MyRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6)
)
_MyRouteMIBCompliances_ObjectIdentity = ObjectIdentity
myRouteMIBCompliances = _MyRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 1)
)
_MyRouteMIBGroups_ObjectIdentity = ObjectIdentity
myRouteMIBGroups = _MyRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2)
)

# Managed Objects groups

myRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 1)
)
myRouteMIBGroup.setObjects(
    ("MY-ROUTE-MIB", "myRouteServiceStatus")
)
if mibBuilder.loadTexts:
    myRouteMIBGroup.setStatus("current")

myRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 2)
)
myRouteInfoMIBGroup.setObjects(
      *(("MY-ROUTE-MIB", "myRoutingProtoInfoProtoType"),
        ("MY-ROUTE-MIB", "myRoutingProtoInfoGateWay"),
        ("MY-ROUTE-MIB", "myRoutingProtoInfoDistance"),
        ("MY-ROUTE-MIB", "myRoutingProtoInfoLastUpdate"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgRoutingProtoType"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgAlways"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgMetric"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgMetricType"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgRouteMap"),
        ("MY-ROUTE-MIB", "myDefRoutingCfgStatus"))
)
if mibBuilder.loadTexts:
    myRouteInfoMIBGroup.setStatus("current")

myRouteMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 3)
)
myRouteMapMIBGroup.setObjects(
      *(("MY-ROUTE-MIB", "myRouteMapName"),
        ("MY-ROUTE-MIB", "myRouteMapSequenceNumber"),
        ("MY-ROUTE-MIB", "myRouteMapOperType"),
        ("MY-ROUTE-MIB", "myRouteMapMatchMetric"),
        ("MY-ROUTE-MIB", "myRouteMapMatchRouteType"),
        ("MY-ROUTE-MIB", "myRouteMapMetricValueType"),
        ("MY-ROUTE-MIB", "myRouteMapSetMetric"),
        ("MY-ROUTE-MIB", "myRouteMapSetLevel"),
        ("MY-ROUTE-MIB", "myRouteMapSetMetricType"),
        ("MY-ROUTE-MIB", "myRouteMapSetNexthopSt"),
        ("MY-ROUTE-MIB", "myRouteMapSetNexthopSt"),
        ("MY-ROUTE-MIB", "myRouteMapStatus"),
        ("MY-ROUTE-MIB", "myRouteMapMatchIpAddressAclName"),
        ("MY-ROUTE-MIB", "myRouteMapMatchType"),
        ("MY-ROUTE-MIB", "myRouteMapMatchIpAddressStatus"),
        ("MY-ROUTE-MIB", "myRouteMapMatchTagValue"),
        ("MY-ROUTE-MIB", "myRouteMapMatchTagStatus"),
        ("MY-ROUTE-MIB", "myRouteMapMatchInterfaceIfIndex"),
        ("MY-ROUTE-MIB", "myRouteMapMatchInterfaceStatus"))
)
if mibBuilder.loadTexts:
    myRouteMapMIBGroup.setStatus("current")

myRouteRedistributeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 4)
)
myRouteRedistributeMIBGroup.setObjects(
      *(("MY-ROUTE-MIB", "myRouteRedistributeProtocolCfg"),
        ("MY-ROUTE-MIB", "myRouteRedistributeProtocol"),
        ("MY-ROUTE-MIB", "myRouteRedistributeMetricValue"),
        ("MY-ROUTE-MIB", "myRouteRedistributeMetricType"),
        ("MY-ROUTE-MIB", "myRouteRedistributeTagValue"),
        ("MY-ROUTE-MIB", "myRouteRedistributeRouteMapName"),
        ("MY-ROUTE-MIB", "myRouteRedistributeStatus"))
)
if mibBuilder.loadTexts:
    myRouteRedistributeMIBGroup.setStatus("current")

myRouteFilteringMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 5)
)
myRouteFilteringMibGroup.setObjects(
      *(("MY-ROUTE-MIB", "myIpPrefixListName"),
        ("MY-ROUTE-MIB", "myIpPrefixListSequence"),
        ("MY-ROUTE-MIB", "myIpPrefixListOperMethod"),
        ("MY-ROUTE-MIB", "myIpPrefixListIpAddress"),
        ("MY-ROUTE-MIB", "myIpPrefixListMaskLength"),
        ("MY-ROUTE-MIB", "myIpPrefixListMinimumPrefixLength"),
        ("MY-ROUTE-MIB", "myIpPrefixListMaximumPrefixLength"),
        ("MY-ROUTE-MIB", "myIpPrefixListStatus"),
        ("MY-ROUTE-MIB", "myDistributeListCfgProtoType"),
        ("MY-ROUTE-MIB", "myDistributeListIfIndex"),
        ("MY-ROUTE-MIB", "myDistributeListFilterType"),
        ("MY-ROUTE-MIB", "myDistributeListDirection"),
        ("MY-ROUTE-MIB", "myDistributeListAclName"),
        ("MY-ROUTE-MIB", "myDistributeListGateWayIpPrefixName"),
        ("MY-ROUTE-MIB", "myDistributeListPrefixIpPrefixName"),
        ("MY-ROUTE-MIB", "myDistributeListFilteringProtocol"),
        ("MY-ROUTE-MIB", "myDistributeListStatus"))
)
if mibBuilder.loadTexts:
    myRouteFilteringMibGroup.setStatus("current")

myipCidrRouteMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 6)
)
myipCidrRouteMibGroup.setObjects(
      *(("MY-ROUTE-MIB", "myipCidrRouteDest"),
        ("MY-ROUTE-MIB", "myipCidrRouteMask"),
        ("MY-ROUTE-MIB", "myipCidrRouteTos"),
        ("MY-ROUTE-MIB", "myipCidrRouteNextHop"),
        ("MY-ROUTE-MIB", "myipCidrRouteIfIndex"),
        ("MY-ROUTE-MIB", "myipCidrRouteType"),
        ("MY-ROUTE-MIB", "myipCidrRouteProto"),
        ("MY-ROUTE-MIB", "myipCidrRouteAge"),
        ("MY-ROUTE-MIB", "myipCidrRouteInfo"),
        ("MY-ROUTE-MIB", "myipCidrRouteNextHopAS"),
        ("MY-ROUTE-MIB", "myipCidrRouteMetric1"),
        ("MY-ROUTE-MIB", "myipCidrRouteMetric2"),
        ("MY-ROUTE-MIB", "myipCidrRouteMetric3"),
        ("MY-ROUTE-MIB", "myipCidrRouteMetric4"),
        ("MY-ROUTE-MIB", "myipCidrRouteMetric5"),
        ("MY-ROUTE-MIB", "myipCidrRouteStatus"),
        ("MY-ROUTE-MIB", "myipCidrOspfRouteType"))
)
if mibBuilder.loadTexts:
    myipCidrRouteMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 1, 1)
)
myRouteMIBCompliance.setObjects(
      *(("MY-ROUTE-MIB", "myRouteMIBGroup"),
        ("MY-ROUTE-MIB", "myRouteInfoMIBGroup"),
        ("MY-ROUTE-MIB", "myRouteMapMIBGroup"),
        ("MY-ROUTE-MIB", "myRouteRedistributeMIBGroup"),
        ("MY-ROUTE-MIB", "myRouteFilteringMibGroup"),
        ("MY-ROUTE-MIB", "myipCidrRouteMibGroup"))
)
if mibBuilder.loadTexts:
    myRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ROUTE-MIB",
    **{"MyRouteProtoType": MyRouteProtoType,
       "myRouteMIB": myRouteMIB,
       "myRouteMIBObjects": myRouteMIBObjects,
       "myRouteServiceStatus": myRouteServiceStatus,
       "myRoutingProtoInfoTable": myRoutingProtoInfoTable,
       "myRoutingProtoInfoEntry": myRoutingProtoInfoEntry,
       "myRoutingProtoInfoProtoType": myRoutingProtoInfoProtoType,
       "myRoutingProtoInfoGateWay": myRoutingProtoInfoGateWay,
       "myRoutingProtoInfoDistance": myRoutingProtoInfoDistance,
       "myRoutingProtoInfoLastUpdate": myRoutingProtoInfoLastUpdate,
       "myDefRoutingCfgTable": myDefRoutingCfgTable,
       "myDefRoutingCfgEntry": myDefRoutingCfgEntry,
       "myDefRoutingCfgRoutingProtoType": myDefRoutingCfgRoutingProtoType,
       "myDefRoutingCfgAlways": myDefRoutingCfgAlways,
       "myDefRoutingCfgMetric": myDefRoutingCfgMetric,
       "myDefRoutingCfgMetricType": myDefRoutingCfgMetricType,
       "myDefRoutingCfgRouteMap": myDefRoutingCfgRouteMap,
       "myDefRoutingCfgStatus": myDefRoutingCfgStatus,
       "myRouteMapMIBObjects": myRouteMapMIBObjects,
       "myRouteMapTable": myRouteMapTable,
       "myRouteMapEntry": myRouteMapEntry,
       "myRouteMapName": myRouteMapName,
       "myRouteMapSequenceNumber": myRouteMapSequenceNumber,
       "myRouteMapOperType": myRouteMapOperType,
       "myRouteMapMatchMetric": myRouteMapMatchMetric,
       "myRouteMapMatchRouteType": myRouteMapMatchRouteType,
       "myRouteMapMetricValueType": myRouteMapMetricValueType,
       "myRouteMapSetMetric": myRouteMapSetMetric,
       "myRouteMapSetLevel": myRouteMapSetLevel,
       "myRouteMapSetMetricType": myRouteMapSetMetricType,
       "myRouteMapSetNexthopSt": myRouteMapSetNexthopSt,
       "myRouteMapSetNexthop": myRouteMapSetNexthop,
       "myRouteMapStatus": myRouteMapStatus,
       "myRouteMapMatchIpAddressTable": myRouteMapMatchIpAddressTable,
       "myRouteMapMatchIpAddressEntry": myRouteMapMatchIpAddressEntry,
       "myRouteMapMatchType": myRouteMapMatchType,
       "myRouteMapMatchIpAddressAclName": myRouteMapMatchIpAddressAclName,
       "myRouteMapMatchIpAddressStatus": myRouteMapMatchIpAddressStatus,
       "myRouteMapMatchTagTable": myRouteMapMatchTagTable,
       "myRouteMapMatchTagEntry": myRouteMapMatchTagEntry,
       "myRouteMapMatchTagValue": myRouteMapMatchTagValue,
       "myRouteMapMatchTagStatus": myRouteMapMatchTagStatus,
       "myRouteMapMatchInterfaceTable": myRouteMapMatchInterfaceTable,
       "myRouteMapMatchInterfaceEntry": myRouteMapMatchInterfaceEntry,
       "myRouteMapMatchInterfaceIfIndex": myRouteMapMatchInterfaceIfIndex,
       "myRouteMapMatchInterfaceStatus": myRouteMapMatchInterfaceStatus,
       "myRouteRedistributeMIBObjects": myRouteRedistributeMIBObjects,
       "myRouteRedistributeTable": myRouteRedistributeTable,
       "myRouteRedistributeEntry": myRouteRedistributeEntry,
       "myRouteRedistributeProtocolCfg": myRouteRedistributeProtocolCfg,
       "myRouteRedistributeProtocol": myRouteRedistributeProtocol,
       "myRouteRedistributeMetricValue": myRouteRedistributeMetricValue,
       "myRouteRedistributeMetricType": myRouteRedistributeMetricType,
       "myRouteRedistributeTagValue": myRouteRedistributeTagValue,
       "myRouteRedistributeRouteMapName": myRouteRedistributeRouteMapName,
       "myRouteRedistributeStatus": myRouteRedistributeStatus,
       "myRouteFilteringMIBObjects": myRouteFilteringMIBObjects,
       "myIpPrefixListTable": myIpPrefixListTable,
       "myIpPrefixListEntry": myIpPrefixListEntry,
       "myIpPrefixListName": myIpPrefixListName,
       "myIpPrefixListSequence": myIpPrefixListSequence,
       "myIpPrefixListOperMethod": myIpPrefixListOperMethod,
       "myIpPrefixListIpAddress": myIpPrefixListIpAddress,
       "myIpPrefixListMaskLength": myIpPrefixListMaskLength,
       "myIpPrefixListMinimumPrefixLength": myIpPrefixListMinimumPrefixLength,
       "myIpPrefixListMaximumPrefixLength": myIpPrefixListMaximumPrefixLength,
       "myIpPrefixListStatus": myIpPrefixListStatus,
       "myDistributeListTable": myDistributeListTable,
       "myDistributeListEntry": myDistributeListEntry,
       "myDistributeListCfgProtoType": myDistributeListCfgProtoType,
       "myDistributeListIfIndex": myDistributeListIfIndex,
       "myDistributeListDirection": myDistributeListDirection,
       "myDistributeListFilteringProtocol": myDistributeListFilteringProtocol,
       "myDistributeListFilterType": myDistributeListFilterType,
       "myDistributeListAclName": myDistributeListAclName,
       "myDistributeListGateWayIpPrefixName": myDistributeListGateWayIpPrefixName,
       "myDistributeListPrefixIpPrefixName": myDistributeListPrefixIpPrefixName,
       "myDistributeListStatus": myDistributeListStatus,
       "myipCidrRouteExtendMIBObjects": myipCidrRouteExtendMIBObjects,
       "myipCidrRouteTable": myipCidrRouteTable,
       "myipCidrRouteEntry": myipCidrRouteEntry,
       "myipCidrRouteDest": myipCidrRouteDest,
       "myipCidrRouteMask": myipCidrRouteMask,
       "myipCidrRouteTos": myipCidrRouteTos,
       "myipCidrRouteNextHop": myipCidrRouteNextHop,
       "myipCidrRouteIfIndex": myipCidrRouteIfIndex,
       "myipCidrRouteType": myipCidrRouteType,
       "myipCidrRouteProto": myipCidrRouteProto,
       "myipCidrRouteAge": myipCidrRouteAge,
       "myipCidrRouteInfo": myipCidrRouteInfo,
       "myipCidrRouteNextHopAS": myipCidrRouteNextHopAS,
       "myipCidrRouteMetric1": myipCidrRouteMetric1,
       "myipCidrRouteMetric2": myipCidrRouteMetric2,
       "myipCidrRouteMetric3": myipCidrRouteMetric3,
       "myipCidrRouteMetric4": myipCidrRouteMetric4,
       "myipCidrRouteMetric5": myipCidrRouteMetric5,
       "myipCidrRouteStatus": myipCidrRouteStatus,
       "myipCidrOspfRouteType": myipCidrOspfRouteType,
       "myRouteMIBConformance": myRouteMIBConformance,
       "myRouteMIBCompliances": myRouteMIBCompliances,
       "myRouteMIBCompliance": myRouteMIBCompliance,
       "myRouteMIBGroups": myRouteMIBGroups,
       "myRouteMIBGroup": myRouteMIBGroup,
       "myRouteInfoMIBGroup": myRouteInfoMIBGroup,
       "myRouteMapMIBGroup": myRouteMapMIBGroup,
       "myRouteRedistributeMIBGroup": myRouteRedistributeMIBGroup,
       "myRouteFilteringMibGroup": myRouteFilteringMibGroup,
       "myipCidrRouteMibGroup": myipCidrRouteMibGroup}
)
