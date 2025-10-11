# SNMP MIB module (QTECH-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:23 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

qtechRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20)
)
if mibBuilder.loadTexts:
    qtechRouteMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechRouteProtoType(TextualConvention, Integer32):
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

_QtechRouteMIBObjects_ObjectIdentity = ObjectIdentity
qtechRouteMIBObjects = _QtechRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1)
)
_QtechRouteServiceStatus_Type = EnabledStatus
_QtechRouteServiceStatus_Object = MibScalar
qtechRouteServiceStatus = _QtechRouteServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 1),
    _QtechRouteServiceStatus_Type()
)
qtechRouteServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRouteServiceStatus.setStatus("current")
_QtechRoutingProtoInfoTable_Object = MibTable
qtechRoutingProtoInfoTable = _QtechRoutingProtoInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoTable.setStatus("current")
_QtechRoutingProtoInfoEntry_Object = MibTableRow
qtechRoutingProtoInfoEntry = _QtechRoutingProtoInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2, 1)
)
qtechRoutingProtoInfoEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRoutingProtoInfoProtoType"),
    (0, "QTECH-ROUTE-MIB", "qtechRoutingProtoInfoGateWay"),
)
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoEntry.setStatus("current")
_QtechRoutingProtoInfoProtoType_Type = QtechRouteProtoType
_QtechRoutingProtoInfoProtoType_Object = MibTableColumn
qtechRoutingProtoInfoProtoType = _QtechRoutingProtoInfoProtoType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2, 1, 1),
    _QtechRoutingProtoInfoProtoType_Type()
)
qtechRoutingProtoInfoProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoProtoType.setStatus("current")
_QtechRoutingProtoInfoGateWay_Type = IpAddress
_QtechRoutingProtoInfoGateWay_Object = MibTableColumn
qtechRoutingProtoInfoGateWay = _QtechRoutingProtoInfoGateWay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2, 1, 2),
    _QtechRoutingProtoInfoGateWay_Type()
)
qtechRoutingProtoInfoGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoGateWay.setStatus("current")
_QtechRoutingProtoInfoDistance_Type = Unsigned32
_QtechRoutingProtoInfoDistance_Object = MibTableColumn
qtechRoutingProtoInfoDistance = _QtechRoutingProtoInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2, 1, 3),
    _QtechRoutingProtoInfoDistance_Type()
)
qtechRoutingProtoInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoDistance.setStatus("current")
_QtechRoutingProtoInfoLastUpdate_Type = TimeTicks
_QtechRoutingProtoInfoLastUpdate_Object = MibTableColumn
qtechRoutingProtoInfoLastUpdate = _QtechRoutingProtoInfoLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 2, 1, 4),
    _QtechRoutingProtoInfoLastUpdate_Type()
)
qtechRoutingProtoInfoLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoutingProtoInfoLastUpdate.setStatus("current")
_QtechDefRoutingCfgTable_Object = MibTable
qtechDefRoutingCfgTable = _QtechDefRoutingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    qtechDefRoutingCfgTable.setStatus("current")
_QtechDefRoutingCfgEntry_Object = MibTableRow
qtechDefRoutingCfgEntry = _QtechDefRoutingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1)
)
qtechDefRoutingCfgEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechDefRoutingCfgRoutingProtoType"),
)
if mibBuilder.loadTexts:
    qtechDefRoutingCfgEntry.setStatus("current")
_QtechDefRoutingCfgRoutingProtoType_Type = QtechRouteProtoType
_QtechDefRoutingCfgRoutingProtoType_Object = MibTableColumn
qtechDefRoutingCfgRoutingProtoType = _QtechDefRoutingCfgRoutingProtoType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 1),
    _QtechDefRoutingCfgRoutingProtoType_Type()
)
qtechDefRoutingCfgRoutingProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgRoutingProtoType.setStatus("current")


class _QtechDefRoutingCfgAlways_Type(TruthValue):
    """Custom type qtechDefRoutingCfgAlways based on TruthValue"""
    defaultValue = 2


_QtechDefRoutingCfgAlways_Type.__name__ = "TruthValue"
_QtechDefRoutingCfgAlways_Object = MibTableColumn
qtechDefRoutingCfgAlways = _QtechDefRoutingCfgAlways_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 2),
    _QtechDefRoutingCfgAlways_Type()
)
qtechDefRoutingCfgAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgAlways.setStatus("current")


class _QtechDefRoutingCfgMetric_Type(Unsigned32):
    """Custom type qtechDefRoutingCfgMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_QtechDefRoutingCfgMetric_Type.__name__ = "Unsigned32"
_QtechDefRoutingCfgMetric_Object = MibTableColumn
qtechDefRoutingCfgMetric = _QtechDefRoutingCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 3),
    _QtechDefRoutingCfgMetric_Type()
)
qtechDefRoutingCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgMetric.setStatus("current")


class _QtechDefRoutingCfgMetricType_Type(Integer32):
    """Custom type qtechDefRoutingCfgMetricType based on Integer32"""
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


_QtechDefRoutingCfgMetricType_Type.__name__ = "Integer32"
_QtechDefRoutingCfgMetricType_Object = MibTableColumn
qtechDefRoutingCfgMetricType = _QtechDefRoutingCfgMetricType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 4),
    _QtechDefRoutingCfgMetricType_Type()
)
qtechDefRoutingCfgMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgMetricType.setStatus("current")


class _QtechDefRoutingCfgRouteMap_Type(DisplayString):
    """Custom type qtechDefRoutingCfgRouteMap based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDefRoutingCfgRouteMap_Type.__name__ = "DisplayString"
_QtechDefRoutingCfgRouteMap_Object = MibTableColumn
qtechDefRoutingCfgRouteMap = _QtechDefRoutingCfgRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 5),
    _QtechDefRoutingCfgRouteMap_Type()
)
qtechDefRoutingCfgRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgRouteMap.setStatus("current")
_QtechDefRoutingCfgStatus_Type = RowStatus
_QtechDefRoutingCfgStatus_Object = MibTableColumn
qtechDefRoutingCfgStatus = _QtechDefRoutingCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 1, 3, 1, 6),
    _QtechDefRoutingCfgStatus_Type()
)
qtechDefRoutingCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDefRoutingCfgStatus.setStatus("current")
_QtechRouteMapMIBObjects_ObjectIdentity = ObjectIdentity
qtechRouteMapMIBObjects = _QtechRouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2)
)
_QtechRouteMapTable_Object = MibTable
qtechRouteMapTable = _QtechRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    qtechRouteMapTable.setStatus("current")
_QtechRouteMapEntry_Object = MibTableRow
qtechRouteMapEntry = _QtechRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1)
)
qtechRouteMapEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapName"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapSequenceNumber"),
)
if mibBuilder.loadTexts:
    qtechRouteMapEntry.setStatus("current")


class _QtechRouteMapName_Type(DisplayString):
    """Custom type qtechRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRouteMapName_Type.__name__ = "DisplayString"
_QtechRouteMapName_Object = MibTableColumn
qtechRouteMapName = _QtechRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 1),
    _QtechRouteMapName_Type()
)
qtechRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapName.setStatus("current")


class _QtechRouteMapSequenceNumber_Type(Unsigned32):
    """Custom type qtechRouteMapSequenceNumber based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechRouteMapSequenceNumber_Type.__name__ = "Unsigned32"
_QtechRouteMapSequenceNumber_Object = MibTableColumn
qtechRouteMapSequenceNumber = _QtechRouteMapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 2),
    _QtechRouteMapSequenceNumber_Type()
)
qtechRouteMapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapSequenceNumber.setStatus("current")


class _QtechRouteMapOperType_Type(Integer32):
    """Custom type qtechRouteMapOperType based on Integer32"""
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


_QtechRouteMapOperType_Type.__name__ = "Integer32"
_QtechRouteMapOperType_Object = MibTableColumn
qtechRouteMapOperType = _QtechRouteMapOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 3),
    _QtechRouteMapOperType_Type()
)
qtechRouteMapOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapOperType.setStatus("current")


class _QtechRouteMapMatchMetric_Type(Unsigned32):
    """Custom type qtechRouteMapMatchMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechRouteMapMatchMetric_Type.__name__ = "Unsigned32"
_QtechRouteMapMatchMetric_Object = MibTableColumn
qtechRouteMapMatchMetric = _QtechRouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 4),
    _QtechRouteMapMatchMetric_Type()
)
qtechRouteMapMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMatchMetric.setStatus("current")


class _QtechRouteMapMatchRouteType_Type(Integer32):
    """Custom type qtechRouteMapMatchRouteType based on Integer32"""
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


_QtechRouteMapMatchRouteType_Type.__name__ = "Integer32"
_QtechRouteMapMatchRouteType_Object = MibTableColumn
qtechRouteMapMatchRouteType = _QtechRouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 5),
    _QtechRouteMapMatchRouteType_Type()
)
qtechRouteMapMatchRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMatchRouteType.setStatus("current")


class _QtechRouteMapMetricValueType_Type(Integer32):
    """Custom type qtechRouteMapMetricValueType based on Integer32"""
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


_QtechRouteMapMetricValueType_Type.__name__ = "Integer32"
_QtechRouteMapMetricValueType_Object = MibTableColumn
qtechRouteMapMetricValueType = _QtechRouteMapMetricValueType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 6),
    _QtechRouteMapMetricValueType_Type()
)
qtechRouteMapMetricValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMetricValueType.setStatus("current")


class _QtechRouteMapSetMetric_Type(Unsigned32):
    """Custom type qtechRouteMapSetMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechRouteMapSetMetric_Type.__name__ = "Unsigned32"
_QtechRouteMapSetMetric_Object = MibTableColumn
qtechRouteMapSetMetric = _QtechRouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 7),
    _QtechRouteMapSetMetric_Type()
)
qtechRouteMapSetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapSetMetric.setStatus("current")


class _QtechRouteMapSetLevel_Type(Integer32):
    """Custom type qtechRouteMapSetLevel based on Integer32"""
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


_QtechRouteMapSetLevel_Type.__name__ = "Integer32"
_QtechRouteMapSetLevel_Object = MibTableColumn
qtechRouteMapSetLevel = _QtechRouteMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 8),
    _QtechRouteMapSetLevel_Type()
)
qtechRouteMapSetLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapSetLevel.setStatus("current")


class _QtechRouteMapSetMetricType_Type(Integer32):
    """Custom type qtechRouteMapSetMetricType based on Integer32"""
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


_QtechRouteMapSetMetricType_Type.__name__ = "Integer32"
_QtechRouteMapSetMetricType_Object = MibTableColumn
qtechRouteMapSetMetricType = _QtechRouteMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 9),
    _QtechRouteMapSetMetricType_Type()
)
qtechRouteMapSetMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapSetMetricType.setStatus("current")


class _QtechRouteMapSetNexthopSt_Type(ConfigStatus):
    """Custom type qtechRouteMapSetNexthopSt based on ConfigStatus"""
    defaultValue = 2


_QtechRouteMapSetNexthopSt_Type.__name__ = "ConfigStatus"
_QtechRouteMapSetNexthopSt_Object = MibTableColumn
qtechRouteMapSetNexthopSt = _QtechRouteMapSetNexthopSt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 10),
    _QtechRouteMapSetNexthopSt_Type()
)
qtechRouteMapSetNexthopSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapSetNexthopSt.setStatus("current")
_QtechRouteMapSetNexthop_Type = IpAddress
_QtechRouteMapSetNexthop_Object = MibTableColumn
qtechRouteMapSetNexthop = _QtechRouteMapSetNexthop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 11),
    _QtechRouteMapSetNexthop_Type()
)
qtechRouteMapSetNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapSetNexthop.setStatus("current")
_QtechRouteMapStatus_Type = RowStatus
_QtechRouteMapStatus_Object = MibTableColumn
qtechRouteMapStatus = _QtechRouteMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 1, 1, 12),
    _QtechRouteMapStatus_Type()
)
qtechRouteMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapStatus.setStatus("current")
_QtechRouteMapMatchIpAddressTable_Object = MibTable
qtechRouteMapMatchIpAddressTable = _QtechRouteMapMatchIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchIpAddressTable.setStatus("current")
_QtechRouteMapMatchIpAddressEntry_Object = MibTableRow
qtechRouteMapMatchIpAddressEntry = _QtechRouteMapMatchIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 2, 1)
)
qtechRouteMapMatchIpAddressEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapName"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapSequenceNumber"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapMatchType"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapMatchIpAddressAclName"),
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchIpAddressEntry.setStatus("current")


class _QtechRouteMapMatchType_Type(Integer32):
    """Custom type qtechRouteMapMatchType based on Integer32"""
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


_QtechRouteMapMatchType_Type.__name__ = "Integer32"
_QtechRouteMapMatchType_Object = MibTableColumn
qtechRouteMapMatchType = _QtechRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 2, 1, 1),
    _QtechRouteMapMatchType_Type()
)
qtechRouteMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapMatchType.setStatus("current")


class _QtechRouteMapMatchIpAddressAclName_Type(DisplayString):
    """Custom type qtechRouteMapMatchIpAddressAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRouteMapMatchIpAddressAclName_Type.__name__ = "DisplayString"
_QtechRouteMapMatchIpAddressAclName_Object = MibTableColumn
qtechRouteMapMatchIpAddressAclName = _QtechRouteMapMatchIpAddressAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 2, 1, 2),
    _QtechRouteMapMatchIpAddressAclName_Type()
)
qtechRouteMapMatchIpAddressAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapMatchIpAddressAclName.setStatus("current")
_QtechRouteMapMatchIpAddressStatus_Type = RowStatus
_QtechRouteMapMatchIpAddressStatus_Object = MibTableColumn
qtechRouteMapMatchIpAddressStatus = _QtechRouteMapMatchIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 2, 1, 3),
    _QtechRouteMapMatchIpAddressStatus_Type()
)
qtechRouteMapMatchIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMatchIpAddressStatus.setStatus("current")
_QtechRouteMapMatchTagTable_Object = MibTable
qtechRouteMapMatchTagTable = _QtechRouteMapMatchTagTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 3)
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchTagTable.setStatus("current")
_QtechRouteMapMatchTagEntry_Object = MibTableRow
qtechRouteMapMatchTagEntry = _QtechRouteMapMatchTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 3, 1)
)
qtechRouteMapMatchTagEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapName"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapSequenceNumber"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapMatchTagValue"),
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchTagEntry.setStatus("current")


class _QtechRouteMapMatchTagValue_Type(Unsigned32):
    """Custom type qtechRouteMapMatchTagValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechRouteMapMatchTagValue_Type.__name__ = "Unsigned32"
_QtechRouteMapMatchTagValue_Object = MibTableColumn
qtechRouteMapMatchTagValue = _QtechRouteMapMatchTagValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 3, 1, 1),
    _QtechRouteMapMatchTagValue_Type()
)
qtechRouteMapMatchTagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapMatchTagValue.setStatus("current")
_QtechRouteMapMatchTagStatus_Type = RowStatus
_QtechRouteMapMatchTagStatus_Object = MibTableColumn
qtechRouteMapMatchTagStatus = _QtechRouteMapMatchTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 3, 1, 2),
    _QtechRouteMapMatchTagStatus_Type()
)
qtechRouteMapMatchTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMatchTagStatus.setStatus("current")
_QtechRouteMapMatchInterfaceTable_Object = MibTable
qtechRouteMapMatchInterfaceTable = _QtechRouteMapMatchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 4)
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchInterfaceTable.setStatus("current")
_QtechRouteMapMatchInterfaceEntry_Object = MibTableRow
qtechRouteMapMatchInterfaceEntry = _QtechRouteMapMatchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 4, 1)
)
qtechRouteMapMatchInterfaceEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapName"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapSequenceNumber"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteMapMatchInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechRouteMapMatchInterfaceEntry.setStatus("current")
_QtechRouteMapMatchInterfaceIfIndex_Type = IfIndex
_QtechRouteMapMatchInterfaceIfIndex_Object = MibTableColumn
qtechRouteMapMatchInterfaceIfIndex = _QtechRouteMapMatchInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 4, 1, 1),
    _QtechRouteMapMatchInterfaceIfIndex_Type()
)
qtechRouteMapMatchInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteMapMatchInterfaceIfIndex.setStatus("current")
_QtechRouteMapMatchInterfaceStatus_Type = RowStatus
_QtechRouteMapMatchInterfaceStatus_Object = MibTableColumn
qtechRouteMapMatchInterfaceStatus = _QtechRouteMapMatchInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 2, 4, 1, 2),
    _QtechRouteMapMatchInterfaceStatus_Type()
)
qtechRouteMapMatchInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteMapMatchInterfaceStatus.setStatus("current")
_QtechRouteRedistributeMIBObjects_ObjectIdentity = ObjectIdentity
qtechRouteRedistributeMIBObjects = _QtechRouteRedistributeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3)
)
_QtechRouteRedistributeTable_Object = MibTable
qtechRouteRedistributeTable = _QtechRouteRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    qtechRouteRedistributeTable.setStatus("current")
_QtechRouteRedistributeEntry_Object = MibTableRow
qtechRouteRedistributeEntry = _QtechRouteRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1)
)
qtechRouteRedistributeEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechRouteRedistributeProtocolCfg"),
    (0, "QTECH-ROUTE-MIB", "qtechRouteRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    qtechRouteRedistributeEntry.setStatus("current")
_QtechRouteRedistributeProtocolCfg_Type = QtechRouteProtoType
_QtechRouteRedistributeProtocolCfg_Object = MibTableColumn
qtechRouteRedistributeProtocolCfg = _QtechRouteRedistributeProtocolCfg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 1),
    _QtechRouteRedistributeProtocolCfg_Type()
)
qtechRouteRedistributeProtocolCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteRedistributeProtocolCfg.setStatus("current")
_QtechRouteRedistributeProtocol_Type = QtechRouteProtoType
_QtechRouteRedistributeProtocol_Object = MibTableColumn
qtechRouteRedistributeProtocol = _QtechRouteRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 2),
    _QtechRouteRedistributeProtocol_Type()
)
qtechRouteRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRouteRedistributeProtocol.setStatus("current")


class _QtechRouteRedistributeMetricValue_Type(Unsigned32):
    """Custom type qtechRouteRedistributeMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_QtechRouteRedistributeMetricValue_Type.__name__ = "Unsigned32"
_QtechRouteRedistributeMetricValue_Object = MibTableColumn
qtechRouteRedistributeMetricValue = _QtechRouteRedistributeMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 3),
    _QtechRouteRedistributeMetricValue_Type()
)
qtechRouteRedistributeMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteRedistributeMetricValue.setStatus("current")


class _QtechRouteRedistributeMetricType_Type(Integer32):
    """Custom type qtechRouteRedistributeMetricType based on Integer32"""
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


_QtechRouteRedistributeMetricType_Type.__name__ = "Integer32"
_QtechRouteRedistributeMetricType_Object = MibTableColumn
qtechRouteRedistributeMetricType = _QtechRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 4),
    _QtechRouteRedistributeMetricType_Type()
)
qtechRouteRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteRedistributeMetricType.setStatus("current")


class _QtechRouteRedistributeTagValue_Type(Unsigned32):
    """Custom type qtechRouteRedistributeTagValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QtechRouteRedistributeTagValue_Type.__name__ = "Unsigned32"
_QtechRouteRedistributeTagValue_Object = MibTableColumn
qtechRouteRedistributeTagValue = _QtechRouteRedistributeTagValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 5),
    _QtechRouteRedistributeTagValue_Type()
)
qtechRouteRedistributeTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteRedistributeTagValue.setStatus("current")


class _QtechRouteRedistributeRouteMapName_Type(DisplayString):
    """Custom type qtechRouteRedistributeRouteMapName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechRouteRedistributeRouteMapName_Type.__name__ = "DisplayString"
_QtechRouteRedistributeRouteMapName_Object = MibTableColumn
qtechRouteRedistributeRouteMapName = _QtechRouteRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 6),
    _QtechRouteRedistributeRouteMapName_Type()
)
qtechRouteRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteRedistributeRouteMapName.setStatus("current")
_QtechRouteRedistributeStatus_Type = RowStatus
_QtechRouteRedistributeStatus_Object = MibTableColumn
qtechRouteRedistributeStatus = _QtechRouteRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 3, 1, 1, 7),
    _QtechRouteRedistributeStatus_Type()
)
qtechRouteRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRouteRedistributeStatus.setStatus("current")
_QtechRouteFilteringMIBObjects_ObjectIdentity = ObjectIdentity
qtechRouteFilteringMIBObjects = _QtechRouteFilteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4)
)
_QtechIpPrefixListTable_Object = MibTable
qtechIpPrefixListTable = _QtechIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    qtechIpPrefixListTable.setStatus("current")
_QtechIpPrefixListEntry_Object = MibTableRow
qtechIpPrefixListEntry = _QtechIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1)
)
qtechIpPrefixListEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechIpPrefixListName"),
    (0, "QTECH-ROUTE-MIB", "qtechIpPrefixListSequence"),
)
if mibBuilder.loadTexts:
    qtechIpPrefixListEntry.setStatus("current")


class _QtechIpPrefixListName_Type(DisplayString):
    """Custom type qtechIpPrefixListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechIpPrefixListName_Type.__name__ = "DisplayString"
_QtechIpPrefixListName_Object = MibTableColumn
qtechIpPrefixListName = _QtechIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 1),
    _QtechIpPrefixListName_Type()
)
qtechIpPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpPrefixListName.setStatus("current")


class _QtechIpPrefixListSequence_Type(Unsigned32):
    """Custom type qtechIpPrefixListSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIpPrefixListSequence_Type.__name__ = "Unsigned32"
_QtechIpPrefixListSequence_Object = MibTableColumn
qtechIpPrefixListSequence = _QtechIpPrefixListSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 2),
    _QtechIpPrefixListSequence_Type()
)
qtechIpPrefixListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpPrefixListSequence.setStatus("current")


class _QtechIpPrefixListOperMethod_Type(Integer32):
    """Custom type qtechIpPrefixListOperMethod based on Integer32"""
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


_QtechIpPrefixListOperMethod_Type.__name__ = "Integer32"
_QtechIpPrefixListOperMethod_Object = MibTableColumn
qtechIpPrefixListOperMethod = _QtechIpPrefixListOperMethod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 3),
    _QtechIpPrefixListOperMethod_Type()
)
qtechIpPrefixListOperMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListOperMethod.setStatus("current")
_QtechIpPrefixListIpAddress_Type = IpAddress
_QtechIpPrefixListIpAddress_Object = MibTableColumn
qtechIpPrefixListIpAddress = _QtechIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 4),
    _QtechIpPrefixListIpAddress_Type()
)
qtechIpPrefixListIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListIpAddress.setStatus("current")


class _QtechIpPrefixListMaskLength_Type(Unsigned32):
    """Custom type qtechIpPrefixListMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_QtechIpPrefixListMaskLength_Type.__name__ = "Unsigned32"
_QtechIpPrefixListMaskLength_Object = MibTableColumn
qtechIpPrefixListMaskLength = _QtechIpPrefixListMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 5),
    _QtechIpPrefixListMaskLength_Type()
)
qtechIpPrefixListMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListMaskLength.setStatus("current")


class _QtechIpPrefixListMinimumPrefixLength_Type(Unsigned32):
    """Custom type qtechIpPrefixListMinimumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_QtechIpPrefixListMinimumPrefixLength_Type.__name__ = "Unsigned32"
_QtechIpPrefixListMinimumPrefixLength_Object = MibTableColumn
qtechIpPrefixListMinimumPrefixLength = _QtechIpPrefixListMinimumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 6),
    _QtechIpPrefixListMinimumPrefixLength_Type()
)
qtechIpPrefixListMinimumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListMinimumPrefixLength.setStatus("current")


class _QtechIpPrefixListMaximumPrefixLength_Type(Unsigned32):
    """Custom type qtechIpPrefixListMaximumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_QtechIpPrefixListMaximumPrefixLength_Type.__name__ = "Unsigned32"
_QtechIpPrefixListMaximumPrefixLength_Object = MibTableColumn
qtechIpPrefixListMaximumPrefixLength = _QtechIpPrefixListMaximumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 7),
    _QtechIpPrefixListMaximumPrefixLength_Type()
)
qtechIpPrefixListMaximumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListMaximumPrefixLength.setStatus("current")
_QtechIpPrefixListStatus_Type = RowStatus
_QtechIpPrefixListStatus_Object = MibTableColumn
qtechIpPrefixListStatus = _QtechIpPrefixListStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 1, 1, 8),
    _QtechIpPrefixListStatus_Type()
)
qtechIpPrefixListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIpPrefixListStatus.setStatus("current")
_QtechDistributeListTable_Object = MibTable
qtechDistributeListTable = _QtechDistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2)
)
if mibBuilder.loadTexts:
    qtechDistributeListTable.setStatus("current")
_QtechDistributeListEntry_Object = MibTableRow
qtechDistributeListEntry = _QtechDistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1)
)
qtechDistributeListEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechDistributeListCfgProtoType"),
    (0, "QTECH-ROUTE-MIB", "qtechDistributeListIfIndex"),
    (0, "QTECH-ROUTE-MIB", "qtechDistributeListDirection"),
    (0, "QTECH-ROUTE-MIB", "qtechDistributeListFilteringProtocol"),
)
if mibBuilder.loadTexts:
    qtechDistributeListEntry.setStatus("current")
_QtechDistributeListCfgProtoType_Type = QtechRouteProtoType
_QtechDistributeListCfgProtoType_Object = MibTableColumn
qtechDistributeListCfgProtoType = _QtechDistributeListCfgProtoType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 1),
    _QtechDistributeListCfgProtoType_Type()
)
qtechDistributeListCfgProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDistributeListCfgProtoType.setStatus("current")
_QtechDistributeListIfIndex_Type = Unsigned32
_QtechDistributeListIfIndex_Object = MibTableColumn
qtechDistributeListIfIndex = _QtechDistributeListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 2),
    _QtechDistributeListIfIndex_Type()
)
qtechDistributeListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDistributeListIfIndex.setStatus("current")


class _QtechDistributeListDirection_Type(Integer32):
    """Custom type qtechDistributeListDirection based on Integer32"""
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


_QtechDistributeListDirection_Type.__name__ = "Integer32"
_QtechDistributeListDirection_Object = MibTableColumn
qtechDistributeListDirection = _QtechDistributeListDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 3),
    _QtechDistributeListDirection_Type()
)
qtechDistributeListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDistributeListDirection.setStatus("current")
_QtechDistributeListFilteringProtocol_Type = Unsigned32
_QtechDistributeListFilteringProtocol_Object = MibTableColumn
qtechDistributeListFilteringProtocol = _QtechDistributeListFilteringProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 4),
    _QtechDistributeListFilteringProtocol_Type()
)
qtechDistributeListFilteringProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDistributeListFilteringProtocol.setStatus("current")


class _QtechDistributeListFilterType_Type(Integer32):
    """Custom type qtechDistributeListFilterType based on Integer32"""
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


_QtechDistributeListFilterType_Type.__name__ = "Integer32"
_QtechDistributeListFilterType_Object = MibTableColumn
qtechDistributeListFilterType = _QtechDistributeListFilterType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 5),
    _QtechDistributeListFilterType_Type()
)
qtechDistributeListFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDistributeListFilterType.setStatus("current")


class _QtechDistributeListAclName_Type(DisplayString):
    """Custom type qtechDistributeListAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDistributeListAclName_Type.__name__ = "DisplayString"
_QtechDistributeListAclName_Object = MibTableColumn
qtechDistributeListAclName = _QtechDistributeListAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 6),
    _QtechDistributeListAclName_Type()
)
qtechDistributeListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDistributeListAclName.setStatus("current")


class _QtechDistributeListGateWayIpPrefixName_Type(DisplayString):
    """Custom type qtechDistributeListGateWayIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDistributeListGateWayIpPrefixName_Type.__name__ = "DisplayString"
_QtechDistributeListGateWayIpPrefixName_Object = MibTableColumn
qtechDistributeListGateWayIpPrefixName = _QtechDistributeListGateWayIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 7),
    _QtechDistributeListGateWayIpPrefixName_Type()
)
qtechDistributeListGateWayIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDistributeListGateWayIpPrefixName.setStatus("current")


class _QtechDistributeListPrefixIpPrefixName_Type(DisplayString):
    """Custom type qtechDistributeListPrefixIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDistributeListPrefixIpPrefixName_Type.__name__ = "DisplayString"
_QtechDistributeListPrefixIpPrefixName_Object = MibTableColumn
qtechDistributeListPrefixIpPrefixName = _QtechDistributeListPrefixIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 8),
    _QtechDistributeListPrefixIpPrefixName_Type()
)
qtechDistributeListPrefixIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDistributeListPrefixIpPrefixName.setStatus("current")
_QtechDistributeListStatus_Type = RowStatus
_QtechDistributeListStatus_Object = MibTableColumn
qtechDistributeListStatus = _QtechDistributeListStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 4, 2, 1, 9),
    _QtechDistributeListStatus_Type()
)
qtechDistributeListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDistributeListStatus.setStatus("current")
_QtechipCidrRouteExtendMIBObjects_ObjectIdentity = ObjectIdentity
qtechipCidrRouteExtendMIBObjects = _QtechipCidrRouteExtendMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5)
)
_QtechipCidrRouteTable_Object = MibTable
qtechipCidrRouteTable = _QtechipCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    qtechipCidrRouteTable.setStatus("current")
_QtechipCidrRouteEntry_Object = MibTableRow
qtechipCidrRouteEntry = _QtechipCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1)
)
qtechipCidrRouteEntry.setIndexNames(
    (0, "QTECH-ROUTE-MIB", "qtechipCidrRouteDest"),
    (0, "QTECH-ROUTE-MIB", "qtechipCidrRouteMask"),
    (0, "QTECH-ROUTE-MIB", "qtechipCidrRouteTos"),
    (0, "QTECH-ROUTE-MIB", "qtechipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    qtechipCidrRouteEntry.setStatus("current")
_QtechipCidrRouteDest_Type = IpAddress
_QtechipCidrRouteDest_Object = MibTableColumn
qtechipCidrRouteDest = _QtechipCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 1),
    _QtechipCidrRouteDest_Type()
)
qtechipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteDest.setStatus("current")
_QtechipCidrRouteMask_Type = IpAddress
_QtechipCidrRouteMask_Object = MibTableColumn
qtechipCidrRouteMask = _QtechipCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 2),
    _QtechipCidrRouteMask_Type()
)
qtechipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteMask.setStatus("current")
_QtechipCidrRouteTos_Type = Integer32
_QtechipCidrRouteTos_Object = MibTableColumn
qtechipCidrRouteTos = _QtechipCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 3),
    _QtechipCidrRouteTos_Type()
)
qtechipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteTos.setStatus("current")
_QtechipCidrRouteNextHop_Type = IpAddress
_QtechipCidrRouteNextHop_Object = MibTableColumn
qtechipCidrRouteNextHop = _QtechipCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 4),
    _QtechipCidrRouteNextHop_Type()
)
qtechipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteNextHop.setStatus("current")


class _QtechipCidrRouteIfIndex_Type(Integer32):
    """Custom type qtechipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_QtechipCidrRouteIfIndex_Type.__name__ = "Integer32"
_QtechipCidrRouteIfIndex_Object = MibTableColumn
qtechipCidrRouteIfIndex = _QtechipCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 5),
    _QtechipCidrRouteIfIndex_Type()
)
qtechipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteIfIndex.setStatus("current")


class _QtechipCidrRouteType_Type(Integer32):
    """Custom type qtechipCidrRouteType based on Integer32"""
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


_QtechipCidrRouteType_Type.__name__ = "Integer32"
_QtechipCidrRouteType_Object = MibTableColumn
qtechipCidrRouteType = _QtechipCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 6),
    _QtechipCidrRouteType_Type()
)
qtechipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteType.setStatus("current")


class _QtechipCidrRouteProto_Type(Integer32):
    """Custom type qtechipCidrRouteProto based on Integer32"""
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


_QtechipCidrRouteProto_Type.__name__ = "Integer32"
_QtechipCidrRouteProto_Object = MibTableColumn
qtechipCidrRouteProto = _QtechipCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 7),
    _QtechipCidrRouteProto_Type()
)
qtechipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteProto.setStatus("current")


class _QtechipCidrRouteAge_Type(Integer32):
    """Custom type qtechipCidrRouteAge based on Integer32"""
    defaultValue = 0


_QtechipCidrRouteAge_Type.__name__ = "Integer32"
_QtechipCidrRouteAge_Object = MibTableColumn
qtechipCidrRouteAge = _QtechipCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 8),
    _QtechipCidrRouteAge_Type()
)
qtechipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrRouteAge.setStatus("current")
_QtechipCidrRouteInfo_Type = ObjectIdentifier
_QtechipCidrRouteInfo_Object = MibTableColumn
qtechipCidrRouteInfo = _QtechipCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 9),
    _QtechipCidrRouteInfo_Type()
)
qtechipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteInfo.setStatus("current")


class _QtechipCidrRouteNextHopAS_Type(Integer32):
    """Custom type qtechipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_QtechipCidrRouteNextHopAS_Type.__name__ = "Integer32"
_QtechipCidrRouteNextHopAS_Object = MibTableColumn
qtechipCidrRouteNextHopAS = _QtechipCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 10),
    _QtechipCidrRouteNextHopAS_Type()
)
qtechipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteNextHopAS.setStatus("current")


class _QtechipCidrRouteMetric1_Type(Integer32):
    """Custom type qtechipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_QtechipCidrRouteMetric1_Type.__name__ = "Integer32"
_QtechipCidrRouteMetric1_Object = MibTableColumn
qtechipCidrRouteMetric1 = _QtechipCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 11),
    _QtechipCidrRouteMetric1_Type()
)
qtechipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteMetric1.setStatus("current")


class _QtechipCidrRouteMetric2_Type(Integer32):
    """Custom type qtechipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_QtechipCidrRouteMetric2_Type.__name__ = "Integer32"
_QtechipCidrRouteMetric2_Object = MibTableColumn
qtechipCidrRouteMetric2 = _QtechipCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 12),
    _QtechipCidrRouteMetric2_Type()
)
qtechipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteMetric2.setStatus("current")


class _QtechipCidrRouteMetric3_Type(Integer32):
    """Custom type qtechipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_QtechipCidrRouteMetric3_Type.__name__ = "Integer32"
_QtechipCidrRouteMetric3_Object = MibTableColumn
qtechipCidrRouteMetric3 = _QtechipCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 13),
    _QtechipCidrRouteMetric3_Type()
)
qtechipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteMetric3.setStatus("current")


class _QtechipCidrRouteMetric4_Type(Integer32):
    """Custom type qtechipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_QtechipCidrRouteMetric4_Type.__name__ = "Integer32"
_QtechipCidrRouteMetric4_Object = MibTableColumn
qtechipCidrRouteMetric4 = _QtechipCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 14),
    _QtechipCidrRouteMetric4_Type()
)
qtechipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteMetric4.setStatus("current")


class _QtechipCidrRouteMetric5_Type(Integer32):
    """Custom type qtechipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_QtechipCidrRouteMetric5_Type.__name__ = "Integer32"
_QtechipCidrRouteMetric5_Object = MibTableColumn
qtechipCidrRouteMetric5 = _QtechipCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 15),
    _QtechipCidrRouteMetric5_Type()
)
qtechipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteMetric5.setStatus("current")
_QtechipCidrRouteStatus_Type = RowStatus
_QtechipCidrRouteStatus_Object = MibTableColumn
qtechipCidrRouteStatus = _QtechipCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 16),
    _QtechipCidrRouteStatus_Type()
)
qtechipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechipCidrRouteStatus.setStatus("current")


class _QtechipCidrOspfRouteType_Type(Integer32):
    """Custom type qtechipCidrOspfRouteType based on Integer32"""
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


_QtechipCidrOspfRouteType_Type.__name__ = "Integer32"
_QtechipCidrOspfRouteType_Object = MibTableColumn
qtechipCidrOspfRouteType = _QtechipCidrOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 5, 1, 1, 17),
    _QtechipCidrOspfRouteType_Type()
)
qtechipCidrOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechipCidrOspfRouteType.setStatus("current")
_QtechRouteMIBConformance_ObjectIdentity = ObjectIdentity
qtechRouteMIBConformance = _QtechRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6)
)
_QtechRouteMIBCompliances_ObjectIdentity = ObjectIdentity
qtechRouteMIBCompliances = _QtechRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 1)
)
_QtechRouteMIBGroups_ObjectIdentity = ObjectIdentity
qtechRouteMIBGroups = _QtechRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2)
)

# Managed Objects groups

qtechRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 1)
)
qtechRouteMIBGroup.setObjects(
    ("QTECH-ROUTE-MIB", "qtechRouteServiceStatus")
)
if mibBuilder.loadTexts:
    qtechRouteMIBGroup.setStatus("current")

qtechRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 2)
)
qtechRouteInfoMIBGroup.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechRoutingProtoInfoProtoType"),
        ("QTECH-ROUTE-MIB", "qtechRoutingProtoInfoGateWay"),
        ("QTECH-ROUTE-MIB", "qtechRoutingProtoInfoDistance"),
        ("QTECH-ROUTE-MIB", "qtechRoutingProtoInfoLastUpdate"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgRoutingProtoType"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgAlways"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgMetric"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgMetricType"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgRouteMap"),
        ("QTECH-ROUTE-MIB", "qtechDefRoutingCfgStatus"))
)
if mibBuilder.loadTexts:
    qtechRouteInfoMIBGroup.setStatus("current")

qtechRouteMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 3)
)
qtechRouteMapMIBGroup.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechRouteMapName"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSequenceNumber"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapOperType"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchMetric"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchRouteType"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMetricValueType"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSetMetric"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSetLevel"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSetMetricType"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSetNexthopSt"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapSetNexthopSt"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapStatus"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchIpAddressAclName"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchType"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchIpAddressStatus"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchTagValue"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchTagStatus"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchInterfaceIfIndex"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMatchInterfaceStatus"))
)
if mibBuilder.loadTexts:
    qtechRouteMapMIBGroup.setStatus("current")

qtechRouteRedistributeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 4)
)
qtechRouteRedistributeMIBGroup.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechRouteRedistributeProtocolCfg"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeProtocol"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeMetricValue"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeMetricType"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeTagValue"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeRouteMapName"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeStatus"))
)
if mibBuilder.loadTexts:
    qtechRouteRedistributeMIBGroup.setStatus("current")

qtechRouteFilteringMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 5)
)
qtechRouteFilteringMibGroup.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechIpPrefixListName"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListSequence"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListOperMethod"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListIpAddress"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListMaskLength"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListMinimumPrefixLength"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListMaximumPrefixLength"),
        ("QTECH-ROUTE-MIB", "qtechIpPrefixListStatus"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListCfgProtoType"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListIfIndex"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListFilterType"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListDirection"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListAclName"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListGateWayIpPrefixName"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListPrefixIpPrefixName"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListFilteringProtocol"),
        ("QTECH-ROUTE-MIB", "qtechDistributeListStatus"))
)
if mibBuilder.loadTexts:
    qtechRouteFilteringMibGroup.setStatus("current")

qtechipCidrRouteMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 2, 6)
)
qtechipCidrRouteMibGroup.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechipCidrRouteDest"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMask"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteTos"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteNextHop"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteIfIndex"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteType"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteProto"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteAge"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteInfo"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteNextHopAS"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMetric1"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMetric2"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMetric3"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMetric4"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMetric5"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteStatus"),
        ("QTECH-ROUTE-MIB", "qtechipCidrOspfRouteType"))
)
if mibBuilder.loadTexts:
    qtechipCidrRouteMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 20, 6, 1, 1)
)
qtechRouteMIBCompliance.setObjects(
      *(("QTECH-ROUTE-MIB", "qtechRouteMIBGroup"),
        ("QTECH-ROUTE-MIB", "qtechRouteInfoMIBGroup"),
        ("QTECH-ROUTE-MIB", "qtechRouteMapMIBGroup"),
        ("QTECH-ROUTE-MIB", "qtechRouteRedistributeMIBGroup"),
        ("QTECH-ROUTE-MIB", "qtechRouteFilteringMibGroup"),
        ("QTECH-ROUTE-MIB", "qtechipCidrRouteMibGroup"))
)
if mibBuilder.loadTexts:
    qtechRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ROUTE-MIB",
    **{"QtechRouteProtoType": QtechRouteProtoType,
       "qtechRouteMIB": qtechRouteMIB,
       "qtechRouteMIBObjects": qtechRouteMIBObjects,
       "qtechRouteServiceStatus": qtechRouteServiceStatus,
       "qtechRoutingProtoInfoTable": qtechRoutingProtoInfoTable,
       "qtechRoutingProtoInfoEntry": qtechRoutingProtoInfoEntry,
       "qtechRoutingProtoInfoProtoType": qtechRoutingProtoInfoProtoType,
       "qtechRoutingProtoInfoGateWay": qtechRoutingProtoInfoGateWay,
       "qtechRoutingProtoInfoDistance": qtechRoutingProtoInfoDistance,
       "qtechRoutingProtoInfoLastUpdate": qtechRoutingProtoInfoLastUpdate,
       "qtechDefRoutingCfgTable": qtechDefRoutingCfgTable,
       "qtechDefRoutingCfgEntry": qtechDefRoutingCfgEntry,
       "qtechDefRoutingCfgRoutingProtoType": qtechDefRoutingCfgRoutingProtoType,
       "qtechDefRoutingCfgAlways": qtechDefRoutingCfgAlways,
       "qtechDefRoutingCfgMetric": qtechDefRoutingCfgMetric,
       "qtechDefRoutingCfgMetricType": qtechDefRoutingCfgMetricType,
       "qtechDefRoutingCfgRouteMap": qtechDefRoutingCfgRouteMap,
       "qtechDefRoutingCfgStatus": qtechDefRoutingCfgStatus,
       "qtechRouteMapMIBObjects": qtechRouteMapMIBObjects,
       "qtechRouteMapTable": qtechRouteMapTable,
       "qtechRouteMapEntry": qtechRouteMapEntry,
       "qtechRouteMapName": qtechRouteMapName,
       "qtechRouteMapSequenceNumber": qtechRouteMapSequenceNumber,
       "qtechRouteMapOperType": qtechRouteMapOperType,
       "qtechRouteMapMatchMetric": qtechRouteMapMatchMetric,
       "qtechRouteMapMatchRouteType": qtechRouteMapMatchRouteType,
       "qtechRouteMapMetricValueType": qtechRouteMapMetricValueType,
       "qtechRouteMapSetMetric": qtechRouteMapSetMetric,
       "qtechRouteMapSetLevel": qtechRouteMapSetLevel,
       "qtechRouteMapSetMetricType": qtechRouteMapSetMetricType,
       "qtechRouteMapSetNexthopSt": qtechRouteMapSetNexthopSt,
       "qtechRouteMapSetNexthop": qtechRouteMapSetNexthop,
       "qtechRouteMapStatus": qtechRouteMapStatus,
       "qtechRouteMapMatchIpAddressTable": qtechRouteMapMatchIpAddressTable,
       "qtechRouteMapMatchIpAddressEntry": qtechRouteMapMatchIpAddressEntry,
       "qtechRouteMapMatchType": qtechRouteMapMatchType,
       "qtechRouteMapMatchIpAddressAclName": qtechRouteMapMatchIpAddressAclName,
       "qtechRouteMapMatchIpAddressStatus": qtechRouteMapMatchIpAddressStatus,
       "qtechRouteMapMatchTagTable": qtechRouteMapMatchTagTable,
       "qtechRouteMapMatchTagEntry": qtechRouteMapMatchTagEntry,
       "qtechRouteMapMatchTagValue": qtechRouteMapMatchTagValue,
       "qtechRouteMapMatchTagStatus": qtechRouteMapMatchTagStatus,
       "qtechRouteMapMatchInterfaceTable": qtechRouteMapMatchInterfaceTable,
       "qtechRouteMapMatchInterfaceEntry": qtechRouteMapMatchInterfaceEntry,
       "qtechRouteMapMatchInterfaceIfIndex": qtechRouteMapMatchInterfaceIfIndex,
       "qtechRouteMapMatchInterfaceStatus": qtechRouteMapMatchInterfaceStatus,
       "qtechRouteRedistributeMIBObjects": qtechRouteRedistributeMIBObjects,
       "qtechRouteRedistributeTable": qtechRouteRedistributeTable,
       "qtechRouteRedistributeEntry": qtechRouteRedistributeEntry,
       "qtechRouteRedistributeProtocolCfg": qtechRouteRedistributeProtocolCfg,
       "qtechRouteRedistributeProtocol": qtechRouteRedistributeProtocol,
       "qtechRouteRedistributeMetricValue": qtechRouteRedistributeMetricValue,
       "qtechRouteRedistributeMetricType": qtechRouteRedistributeMetricType,
       "qtechRouteRedistributeTagValue": qtechRouteRedistributeTagValue,
       "qtechRouteRedistributeRouteMapName": qtechRouteRedistributeRouteMapName,
       "qtechRouteRedistributeStatus": qtechRouteRedistributeStatus,
       "qtechRouteFilteringMIBObjects": qtechRouteFilteringMIBObjects,
       "qtechIpPrefixListTable": qtechIpPrefixListTable,
       "qtechIpPrefixListEntry": qtechIpPrefixListEntry,
       "qtechIpPrefixListName": qtechIpPrefixListName,
       "qtechIpPrefixListSequence": qtechIpPrefixListSequence,
       "qtechIpPrefixListOperMethod": qtechIpPrefixListOperMethod,
       "qtechIpPrefixListIpAddress": qtechIpPrefixListIpAddress,
       "qtechIpPrefixListMaskLength": qtechIpPrefixListMaskLength,
       "qtechIpPrefixListMinimumPrefixLength": qtechIpPrefixListMinimumPrefixLength,
       "qtechIpPrefixListMaximumPrefixLength": qtechIpPrefixListMaximumPrefixLength,
       "qtechIpPrefixListStatus": qtechIpPrefixListStatus,
       "qtechDistributeListTable": qtechDistributeListTable,
       "qtechDistributeListEntry": qtechDistributeListEntry,
       "qtechDistributeListCfgProtoType": qtechDistributeListCfgProtoType,
       "qtechDistributeListIfIndex": qtechDistributeListIfIndex,
       "qtechDistributeListDirection": qtechDistributeListDirection,
       "qtechDistributeListFilteringProtocol": qtechDistributeListFilteringProtocol,
       "qtechDistributeListFilterType": qtechDistributeListFilterType,
       "qtechDistributeListAclName": qtechDistributeListAclName,
       "qtechDistributeListGateWayIpPrefixName": qtechDistributeListGateWayIpPrefixName,
       "qtechDistributeListPrefixIpPrefixName": qtechDistributeListPrefixIpPrefixName,
       "qtechDistributeListStatus": qtechDistributeListStatus,
       "qtechipCidrRouteExtendMIBObjects": qtechipCidrRouteExtendMIBObjects,
       "qtechipCidrRouteTable": qtechipCidrRouteTable,
       "qtechipCidrRouteEntry": qtechipCidrRouteEntry,
       "qtechipCidrRouteDest": qtechipCidrRouteDest,
       "qtechipCidrRouteMask": qtechipCidrRouteMask,
       "qtechipCidrRouteTos": qtechipCidrRouteTos,
       "qtechipCidrRouteNextHop": qtechipCidrRouteNextHop,
       "qtechipCidrRouteIfIndex": qtechipCidrRouteIfIndex,
       "qtechipCidrRouteType": qtechipCidrRouteType,
       "qtechipCidrRouteProto": qtechipCidrRouteProto,
       "qtechipCidrRouteAge": qtechipCidrRouteAge,
       "qtechipCidrRouteInfo": qtechipCidrRouteInfo,
       "qtechipCidrRouteNextHopAS": qtechipCidrRouteNextHopAS,
       "qtechipCidrRouteMetric1": qtechipCidrRouteMetric1,
       "qtechipCidrRouteMetric2": qtechipCidrRouteMetric2,
       "qtechipCidrRouteMetric3": qtechipCidrRouteMetric3,
       "qtechipCidrRouteMetric4": qtechipCidrRouteMetric4,
       "qtechipCidrRouteMetric5": qtechipCidrRouteMetric5,
       "qtechipCidrRouteStatus": qtechipCidrRouteStatus,
       "qtechipCidrOspfRouteType": qtechipCidrOspfRouteType,
       "qtechRouteMIBConformance": qtechRouteMIBConformance,
       "qtechRouteMIBCompliances": qtechRouteMIBCompliances,
       "qtechRouteMIBCompliance": qtechRouteMIBCompliance,
       "qtechRouteMIBGroups": qtechRouteMIBGroups,
       "qtechRouteMIBGroup": qtechRouteMIBGroup,
       "qtechRouteInfoMIBGroup": qtechRouteInfoMIBGroup,
       "qtechRouteMapMIBGroup": qtechRouteMapMIBGroup,
       "qtechRouteRedistributeMIBGroup": qtechRouteRedistributeMIBGroup,
       "qtechRouteFilteringMibGroup": qtechRouteFilteringMibGroup,
       "qtechipCidrRouteMibGroup": qtechipCidrRouteMibGroup}
)
