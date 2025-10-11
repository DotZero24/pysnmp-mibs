# SNMP MIB module (FS-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:33 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20)
)
if mibBuilder.loadTexts:
    fsRouteMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSRouteProtoType(TextualConvention, Integer32):
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

_FsRouteMIBObjects_ObjectIdentity = ObjectIdentity
fsRouteMIBObjects = _FsRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1)
)
_FsRouteServiceStatus_Type = EnabledStatus
_FsRouteServiceStatus_Object = MibScalar
fsRouteServiceStatus = _FsRouteServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 1),
    _FsRouteServiceStatus_Type()
)
fsRouteServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteServiceStatus.setStatus("current")
_FsRoutingProtoInfoTable_Object = MibTable
fsRoutingProtoInfoTable = _FsRoutingProtoInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    fsRoutingProtoInfoTable.setStatus("current")
_FsRoutingProtoInfoEntry_Object = MibTableRow
fsRoutingProtoInfoEntry = _FsRoutingProtoInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2, 1)
)
fsRoutingProtoInfoEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRoutingProtoInfoProtoType"),
    (0, "FS-ROUTE-MIB", "fsRoutingProtoInfoGateWay"),
)
if mibBuilder.loadTexts:
    fsRoutingProtoInfoEntry.setStatus("current")
_FsRoutingProtoInfoProtoType_Type = FSRouteProtoType
_FsRoutingProtoInfoProtoType_Object = MibTableColumn
fsRoutingProtoInfoProtoType = _FsRoutingProtoInfoProtoType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2, 1, 1),
    _FsRoutingProtoInfoProtoType_Type()
)
fsRoutingProtoInfoProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoutingProtoInfoProtoType.setStatus("current")
_FsRoutingProtoInfoGateWay_Type = IpAddress
_FsRoutingProtoInfoGateWay_Object = MibTableColumn
fsRoutingProtoInfoGateWay = _FsRoutingProtoInfoGateWay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2, 1, 2),
    _FsRoutingProtoInfoGateWay_Type()
)
fsRoutingProtoInfoGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoutingProtoInfoGateWay.setStatus("current")
_FsRoutingProtoInfoDistance_Type = Unsigned32
_FsRoutingProtoInfoDistance_Object = MibTableColumn
fsRoutingProtoInfoDistance = _FsRoutingProtoInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2, 1, 3),
    _FsRoutingProtoInfoDistance_Type()
)
fsRoutingProtoInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoutingProtoInfoDistance.setStatus("current")
_FsRoutingProtoInfoLastUpdate_Type = TimeTicks
_FsRoutingProtoInfoLastUpdate_Object = MibTableColumn
fsRoutingProtoInfoLastUpdate = _FsRoutingProtoInfoLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 2, 1, 4),
    _FsRoutingProtoInfoLastUpdate_Type()
)
fsRoutingProtoInfoLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoutingProtoInfoLastUpdate.setStatus("current")
_FsDefRoutingCfgTable_Object = MibTable
fsDefRoutingCfgTable = _FsDefRoutingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    fsDefRoutingCfgTable.setStatus("current")
_FsDefRoutingCfgEntry_Object = MibTableRow
fsDefRoutingCfgEntry = _FsDefRoutingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1)
)
fsDefRoutingCfgEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsDefRoutingCfgRoutingProtoType"),
)
if mibBuilder.loadTexts:
    fsDefRoutingCfgEntry.setStatus("current")
_FsDefRoutingCfgRoutingProtoType_Type = FSRouteProtoType
_FsDefRoutingCfgRoutingProtoType_Object = MibTableColumn
fsDefRoutingCfgRoutingProtoType = _FsDefRoutingCfgRoutingProtoType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 1),
    _FsDefRoutingCfgRoutingProtoType_Type()
)
fsDefRoutingCfgRoutingProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDefRoutingCfgRoutingProtoType.setStatus("current")


class _FsDefRoutingCfgAlways_Type(TruthValue):
    """Custom type fsDefRoutingCfgAlways based on TruthValue"""
    defaultValue = 2


_FsDefRoutingCfgAlways_Type.__name__ = "TruthValue"
_FsDefRoutingCfgAlways_Object = MibTableColumn
fsDefRoutingCfgAlways = _FsDefRoutingCfgAlways_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 2),
    _FsDefRoutingCfgAlways_Type()
)
fsDefRoutingCfgAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDefRoutingCfgAlways.setStatus("current")


class _FsDefRoutingCfgMetric_Type(Unsigned32):
    """Custom type fsDefRoutingCfgMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FsDefRoutingCfgMetric_Type.__name__ = "Unsigned32"
_FsDefRoutingCfgMetric_Object = MibTableColumn
fsDefRoutingCfgMetric = _FsDefRoutingCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 3),
    _FsDefRoutingCfgMetric_Type()
)
fsDefRoutingCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDefRoutingCfgMetric.setStatus("current")


class _FsDefRoutingCfgMetricType_Type(Integer32):
    """Custom type fsDefRoutingCfgMetricType based on Integer32"""
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


_FsDefRoutingCfgMetricType_Type.__name__ = "Integer32"
_FsDefRoutingCfgMetricType_Object = MibTableColumn
fsDefRoutingCfgMetricType = _FsDefRoutingCfgMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 4),
    _FsDefRoutingCfgMetricType_Type()
)
fsDefRoutingCfgMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDefRoutingCfgMetricType.setStatus("current")


class _FsDefRoutingCfgRouteMap_Type(DisplayString):
    """Custom type fsDefRoutingCfgRouteMap based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDefRoutingCfgRouteMap_Type.__name__ = "DisplayString"
_FsDefRoutingCfgRouteMap_Object = MibTableColumn
fsDefRoutingCfgRouteMap = _FsDefRoutingCfgRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 5),
    _FsDefRoutingCfgRouteMap_Type()
)
fsDefRoutingCfgRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDefRoutingCfgRouteMap.setStatus("current")
_FsDefRoutingCfgStatus_Type = RowStatus
_FsDefRoutingCfgStatus_Object = MibTableColumn
fsDefRoutingCfgStatus = _FsDefRoutingCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 1, 3, 1, 6),
    _FsDefRoutingCfgStatus_Type()
)
fsDefRoutingCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDefRoutingCfgStatus.setStatus("current")
_FsRouteMapMIBObjects_ObjectIdentity = ObjectIdentity
fsRouteMapMIBObjects = _FsRouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2)
)
_FsRouteMapTable_Object = MibTable
fsRouteMapTable = _FsRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    fsRouteMapTable.setStatus("current")
_FsRouteMapEntry_Object = MibTableRow
fsRouteMapEntry = _FsRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1)
)
fsRouteMapEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRouteMapName"),
    (0, "FS-ROUTE-MIB", "fsRouteMapSequenceNumber"),
)
if mibBuilder.loadTexts:
    fsRouteMapEntry.setStatus("current")


class _FsRouteMapName_Type(DisplayString):
    """Custom type fsRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRouteMapName_Type.__name__ = "DisplayString"
_FsRouteMapName_Object = MibTableColumn
fsRouteMapName = _FsRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 1),
    _FsRouteMapName_Type()
)
fsRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapName.setStatus("current")


class _FsRouteMapSequenceNumber_Type(Unsigned32):
    """Custom type fsRouteMapSequenceNumber based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRouteMapSequenceNumber_Type.__name__ = "Unsigned32"
_FsRouteMapSequenceNumber_Object = MibTableColumn
fsRouteMapSequenceNumber = _FsRouteMapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 2),
    _FsRouteMapSequenceNumber_Type()
)
fsRouteMapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapSequenceNumber.setStatus("current")


class _FsRouteMapOperType_Type(Integer32):
    """Custom type fsRouteMapOperType based on Integer32"""
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


_FsRouteMapOperType_Type.__name__ = "Integer32"
_FsRouteMapOperType_Object = MibTableColumn
fsRouteMapOperType = _FsRouteMapOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 3),
    _FsRouteMapOperType_Type()
)
fsRouteMapOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapOperType.setStatus("current")


class _FsRouteMapMatchMetric_Type(Unsigned32):
    """Custom type fsRouteMapMatchMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRouteMapMatchMetric_Type.__name__ = "Unsigned32"
_FsRouteMapMatchMetric_Object = MibTableColumn
fsRouteMapMatchMetric = _FsRouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 4),
    _FsRouteMapMatchMetric_Type()
)
fsRouteMapMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMatchMetric.setStatus("current")


class _FsRouteMapMatchRouteType_Type(Integer32):
    """Custom type fsRouteMapMatchRouteType based on Integer32"""
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


_FsRouteMapMatchRouteType_Type.__name__ = "Integer32"
_FsRouteMapMatchRouteType_Object = MibTableColumn
fsRouteMapMatchRouteType = _FsRouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 5),
    _FsRouteMapMatchRouteType_Type()
)
fsRouteMapMatchRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMatchRouteType.setStatus("current")


class _FsRouteMapMetricValueType_Type(Integer32):
    """Custom type fsRouteMapMetricValueType based on Integer32"""
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


_FsRouteMapMetricValueType_Type.__name__ = "Integer32"
_FsRouteMapMetricValueType_Object = MibTableColumn
fsRouteMapMetricValueType = _FsRouteMapMetricValueType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 6),
    _FsRouteMapMetricValueType_Type()
)
fsRouteMapMetricValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMetricValueType.setStatus("current")


class _FsRouteMapSetMetric_Type(Unsigned32):
    """Custom type fsRouteMapSetMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRouteMapSetMetric_Type.__name__ = "Unsigned32"
_FsRouteMapSetMetric_Object = MibTableColumn
fsRouteMapSetMetric = _FsRouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 7),
    _FsRouteMapSetMetric_Type()
)
fsRouteMapSetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapSetMetric.setStatus("current")


class _FsRouteMapSetLevel_Type(Integer32):
    """Custom type fsRouteMapSetLevel based on Integer32"""
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


_FsRouteMapSetLevel_Type.__name__ = "Integer32"
_FsRouteMapSetLevel_Object = MibTableColumn
fsRouteMapSetLevel = _FsRouteMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 8),
    _FsRouteMapSetLevel_Type()
)
fsRouteMapSetLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapSetLevel.setStatus("current")


class _FsRouteMapSetMetricType_Type(Integer32):
    """Custom type fsRouteMapSetMetricType based on Integer32"""
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


_FsRouteMapSetMetricType_Type.__name__ = "Integer32"
_FsRouteMapSetMetricType_Object = MibTableColumn
fsRouteMapSetMetricType = _FsRouteMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 9),
    _FsRouteMapSetMetricType_Type()
)
fsRouteMapSetMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapSetMetricType.setStatus("current")


class _FsRouteMapSetNexthopSt_Type(ConfigStatus):
    """Custom type fsRouteMapSetNexthopSt based on ConfigStatus"""
    defaultValue = 2


_FsRouteMapSetNexthopSt_Type.__name__ = "ConfigStatus"
_FsRouteMapSetNexthopSt_Object = MibTableColumn
fsRouteMapSetNexthopSt = _FsRouteMapSetNexthopSt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 10),
    _FsRouteMapSetNexthopSt_Type()
)
fsRouteMapSetNexthopSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapSetNexthopSt.setStatus("current")
_FsRouteMapSetNexthop_Type = IpAddress
_FsRouteMapSetNexthop_Object = MibTableColumn
fsRouteMapSetNexthop = _FsRouteMapSetNexthop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 11),
    _FsRouteMapSetNexthop_Type()
)
fsRouteMapSetNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapSetNexthop.setStatus("current")
_FsRouteMapStatus_Type = RowStatus
_FsRouteMapStatus_Object = MibTableColumn
fsRouteMapStatus = _FsRouteMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 1, 1, 12),
    _FsRouteMapStatus_Type()
)
fsRouteMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapStatus.setStatus("current")
_FsRouteMapMatchIpAddressTable_Object = MibTable
fsRouteMapMatchIpAddressTable = _FsRouteMapMatchIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddressTable.setStatus("current")
_FsRouteMapMatchIpAddressEntry_Object = MibTableRow
fsRouteMapMatchIpAddressEntry = _FsRouteMapMatchIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 2, 1)
)
fsRouteMapMatchIpAddressEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRouteMapName"),
    (0, "FS-ROUTE-MIB", "fsRouteMapSequenceNumber"),
    (0, "FS-ROUTE-MIB", "fsRouteMapMatchType"),
    (0, "FS-ROUTE-MIB", "fsRouteMapMatchIpAddressAclName"),
)
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddressEntry.setStatus("current")


class _FsRouteMapMatchType_Type(Integer32):
    """Custom type fsRouteMapMatchType based on Integer32"""
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


_FsRouteMapMatchType_Type.__name__ = "Integer32"
_FsRouteMapMatchType_Object = MibTableColumn
fsRouteMapMatchType = _FsRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 2, 1, 1),
    _FsRouteMapMatchType_Type()
)
fsRouteMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapMatchType.setStatus("current")


class _FsRouteMapMatchIpAddressAclName_Type(DisplayString):
    """Custom type fsRouteMapMatchIpAddressAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRouteMapMatchIpAddressAclName_Type.__name__ = "DisplayString"
_FsRouteMapMatchIpAddressAclName_Object = MibTableColumn
fsRouteMapMatchIpAddressAclName = _FsRouteMapMatchIpAddressAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 2, 1, 2),
    _FsRouteMapMatchIpAddressAclName_Type()
)
fsRouteMapMatchIpAddressAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddressAclName.setStatus("current")
_FsRouteMapMatchIpAddressStatus_Type = RowStatus
_FsRouteMapMatchIpAddressStatus_Object = MibTableColumn
fsRouteMapMatchIpAddressStatus = _FsRouteMapMatchIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 2, 1, 3),
    _FsRouteMapMatchIpAddressStatus_Type()
)
fsRouteMapMatchIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddressStatus.setStatus("current")
_FsRouteMapMatchTagTable_Object = MibTable
fsRouteMapMatchTagTable = _FsRouteMapMatchTagTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 3)
)
if mibBuilder.loadTexts:
    fsRouteMapMatchTagTable.setStatus("current")
_FsRouteMapMatchTagEntry_Object = MibTableRow
fsRouteMapMatchTagEntry = _FsRouteMapMatchTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 3, 1)
)
fsRouteMapMatchTagEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRouteMapName"),
    (0, "FS-ROUTE-MIB", "fsRouteMapSequenceNumber"),
    (0, "FS-ROUTE-MIB", "fsRouteMapMatchTagValue"),
)
if mibBuilder.loadTexts:
    fsRouteMapMatchTagEntry.setStatus("current")


class _FsRouteMapMatchTagValue_Type(Unsigned32):
    """Custom type fsRouteMapMatchTagValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRouteMapMatchTagValue_Type.__name__ = "Unsigned32"
_FsRouteMapMatchTagValue_Object = MibTableColumn
fsRouteMapMatchTagValue = _FsRouteMapMatchTagValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 3, 1, 1),
    _FsRouteMapMatchTagValue_Type()
)
fsRouteMapMatchTagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapMatchTagValue.setStatus("current")
_FsRouteMapMatchTagStatus_Type = RowStatus
_FsRouteMapMatchTagStatus_Object = MibTableColumn
fsRouteMapMatchTagStatus = _FsRouteMapMatchTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 3, 1, 2),
    _FsRouteMapMatchTagStatus_Type()
)
fsRouteMapMatchTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMatchTagStatus.setStatus("current")
_FsRouteMapMatchInterfaceTable_Object = MibTable
fsRouteMapMatchInterfaceTable = _FsRouteMapMatchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 4)
)
if mibBuilder.loadTexts:
    fsRouteMapMatchInterfaceTable.setStatus("current")
_FsRouteMapMatchInterfaceEntry_Object = MibTableRow
fsRouteMapMatchInterfaceEntry = _FsRouteMapMatchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 4, 1)
)
fsRouteMapMatchInterfaceEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRouteMapName"),
    (0, "FS-ROUTE-MIB", "fsRouteMapSequenceNumber"),
    (0, "FS-ROUTE-MIB", "fsRouteMapMatchInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsRouteMapMatchInterfaceEntry.setStatus("current")
_FsRouteMapMatchInterfaceIfIndex_Type = IfIndex
_FsRouteMapMatchInterfaceIfIndex_Object = MibTableColumn
fsRouteMapMatchInterfaceIfIndex = _FsRouteMapMatchInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 4, 1, 1),
    _FsRouteMapMatchInterfaceIfIndex_Type()
)
fsRouteMapMatchInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteMapMatchInterfaceIfIndex.setStatus("current")
_FsRouteMapMatchInterfaceStatus_Type = RowStatus
_FsRouteMapMatchInterfaceStatus_Object = MibTableColumn
fsRouteMapMatchInterfaceStatus = _FsRouteMapMatchInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 2, 4, 1, 2),
    _FsRouteMapMatchInterfaceStatus_Type()
)
fsRouteMapMatchInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteMapMatchInterfaceStatus.setStatus("current")
_FsRouteRedistributeMIBObjects_ObjectIdentity = ObjectIdentity
fsRouteRedistributeMIBObjects = _FsRouteRedistributeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3)
)
_FsRouteRedistributeTable_Object = MibTable
fsRouteRedistributeTable = _FsRouteRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    fsRouteRedistributeTable.setStatus("current")
_FsRouteRedistributeEntry_Object = MibTableRow
fsRouteRedistributeEntry = _FsRouteRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1)
)
fsRouteRedistributeEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsRouteRedistributeProtocolCfg"),
    (0, "FS-ROUTE-MIB", "fsRouteRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    fsRouteRedistributeEntry.setStatus("current")
_FsRouteRedistributeProtocolCfg_Type = FSRouteProtoType
_FsRouteRedistributeProtocolCfg_Object = MibTableColumn
fsRouteRedistributeProtocolCfg = _FsRouteRedistributeProtocolCfg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 1),
    _FsRouteRedistributeProtocolCfg_Type()
)
fsRouteRedistributeProtocolCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteRedistributeProtocolCfg.setStatus("current")
_FsRouteRedistributeProtocol_Type = FSRouteProtoType
_FsRouteRedistributeProtocol_Object = MibTableColumn
fsRouteRedistributeProtocol = _FsRouteRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 2),
    _FsRouteRedistributeProtocol_Type()
)
fsRouteRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRouteRedistributeProtocol.setStatus("current")


class _FsRouteRedistributeMetricValue_Type(Unsigned32):
    """Custom type fsRouteRedistributeMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FsRouteRedistributeMetricValue_Type.__name__ = "Unsigned32"
_FsRouteRedistributeMetricValue_Object = MibTableColumn
fsRouteRedistributeMetricValue = _FsRouteRedistributeMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 3),
    _FsRouteRedistributeMetricValue_Type()
)
fsRouteRedistributeMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteRedistributeMetricValue.setStatus("current")


class _FsRouteRedistributeMetricType_Type(Integer32):
    """Custom type fsRouteRedistributeMetricType based on Integer32"""
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


_FsRouteRedistributeMetricType_Type.__name__ = "Integer32"
_FsRouteRedistributeMetricType_Object = MibTableColumn
fsRouteRedistributeMetricType = _FsRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 4),
    _FsRouteRedistributeMetricType_Type()
)
fsRouteRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteRedistributeMetricType.setStatus("current")


class _FsRouteRedistributeTagValue_Type(Unsigned32):
    """Custom type fsRouteRedistributeTagValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsRouteRedistributeTagValue_Type.__name__ = "Unsigned32"
_FsRouteRedistributeTagValue_Object = MibTableColumn
fsRouteRedistributeTagValue = _FsRouteRedistributeTagValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 5),
    _FsRouteRedistributeTagValue_Type()
)
fsRouteRedistributeTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteRedistributeTagValue.setStatus("current")


class _FsRouteRedistributeRouteMapName_Type(DisplayString):
    """Custom type fsRouteRedistributeRouteMapName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsRouteRedistributeRouteMapName_Type.__name__ = "DisplayString"
_FsRouteRedistributeRouteMapName_Object = MibTableColumn
fsRouteRedistributeRouteMapName = _FsRouteRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 6),
    _FsRouteRedistributeRouteMapName_Type()
)
fsRouteRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteRedistributeRouteMapName.setStatus("current")
_FsRouteRedistributeStatus_Type = RowStatus
_FsRouteRedistributeStatus_Object = MibTableColumn
fsRouteRedistributeStatus = _FsRouteRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 3, 1, 1, 7),
    _FsRouteRedistributeStatus_Type()
)
fsRouteRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRouteRedistributeStatus.setStatus("current")
_FsRouteFilteringMIBObjects_ObjectIdentity = ObjectIdentity
fsRouteFilteringMIBObjects = _FsRouteFilteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4)
)
_FsIpPrefixListTable_Object = MibTable
fsIpPrefixListTable = _FsIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    fsIpPrefixListTable.setStatus("current")
_FsIpPrefixListEntry_Object = MibTableRow
fsIpPrefixListEntry = _FsIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1)
)
fsIpPrefixListEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsIpPrefixListName"),
    (0, "FS-ROUTE-MIB", "fsIpPrefixListSequence"),
)
if mibBuilder.loadTexts:
    fsIpPrefixListEntry.setStatus("current")


class _FsIpPrefixListName_Type(DisplayString):
    """Custom type fsIpPrefixListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIpPrefixListName_Type.__name__ = "DisplayString"
_FsIpPrefixListName_Object = MibTableColumn
fsIpPrefixListName = _FsIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 1),
    _FsIpPrefixListName_Type()
)
fsIpPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpPrefixListName.setStatus("current")


class _FsIpPrefixListSequence_Type(Unsigned32):
    """Custom type fsIpPrefixListSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpPrefixListSequence_Type.__name__ = "Unsigned32"
_FsIpPrefixListSequence_Object = MibTableColumn
fsIpPrefixListSequence = _FsIpPrefixListSequence_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 2),
    _FsIpPrefixListSequence_Type()
)
fsIpPrefixListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpPrefixListSequence.setStatus("current")


class _FsIpPrefixListOperMethod_Type(Integer32):
    """Custom type fsIpPrefixListOperMethod based on Integer32"""
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


_FsIpPrefixListOperMethod_Type.__name__ = "Integer32"
_FsIpPrefixListOperMethod_Object = MibTableColumn
fsIpPrefixListOperMethod = _FsIpPrefixListOperMethod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 3),
    _FsIpPrefixListOperMethod_Type()
)
fsIpPrefixListOperMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListOperMethod.setStatus("current")
_FsIpPrefixListIpAddress_Type = IpAddress
_FsIpPrefixListIpAddress_Object = MibTableColumn
fsIpPrefixListIpAddress = _FsIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 4),
    _FsIpPrefixListIpAddress_Type()
)
fsIpPrefixListIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListIpAddress.setStatus("current")


class _FsIpPrefixListMaskLength_Type(Unsigned32):
    """Custom type fsIpPrefixListMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsIpPrefixListMaskLength_Type.__name__ = "Unsigned32"
_FsIpPrefixListMaskLength_Object = MibTableColumn
fsIpPrefixListMaskLength = _FsIpPrefixListMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 5),
    _FsIpPrefixListMaskLength_Type()
)
fsIpPrefixListMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListMaskLength.setStatus("current")


class _FsIpPrefixListMinimumPrefixLength_Type(Unsigned32):
    """Custom type fsIpPrefixListMinimumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsIpPrefixListMinimumPrefixLength_Type.__name__ = "Unsigned32"
_FsIpPrefixListMinimumPrefixLength_Object = MibTableColumn
fsIpPrefixListMinimumPrefixLength = _FsIpPrefixListMinimumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 6),
    _FsIpPrefixListMinimumPrefixLength_Type()
)
fsIpPrefixListMinimumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListMinimumPrefixLength.setStatus("current")


class _FsIpPrefixListMaximumPrefixLength_Type(Unsigned32):
    """Custom type fsIpPrefixListMaximumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsIpPrefixListMaximumPrefixLength_Type.__name__ = "Unsigned32"
_FsIpPrefixListMaximumPrefixLength_Object = MibTableColumn
fsIpPrefixListMaximumPrefixLength = _FsIpPrefixListMaximumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 7),
    _FsIpPrefixListMaximumPrefixLength_Type()
)
fsIpPrefixListMaximumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListMaximumPrefixLength.setStatus("current")
_FsIpPrefixListStatus_Type = RowStatus
_FsIpPrefixListStatus_Object = MibTableColumn
fsIpPrefixListStatus = _FsIpPrefixListStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 1, 1, 8),
    _FsIpPrefixListStatus_Type()
)
fsIpPrefixListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpPrefixListStatus.setStatus("current")
_FsDistributeListTable_Object = MibTable
fsDistributeListTable = _FsDistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2)
)
if mibBuilder.loadTexts:
    fsDistributeListTable.setStatus("current")
_FsDistributeListEntry_Object = MibTableRow
fsDistributeListEntry = _FsDistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1)
)
fsDistributeListEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsDistributeListCfgProtoType"),
    (0, "FS-ROUTE-MIB", "fsDistributeListIfIndex"),
    (0, "FS-ROUTE-MIB", "fsDistributeListDirection"),
    (0, "FS-ROUTE-MIB", "fsDistributeListFilteringProtocol"),
)
if mibBuilder.loadTexts:
    fsDistributeListEntry.setStatus("current")
_FsDistributeListCfgProtoType_Type = FSRouteProtoType
_FsDistributeListCfgProtoType_Object = MibTableColumn
fsDistributeListCfgProtoType = _FsDistributeListCfgProtoType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 1),
    _FsDistributeListCfgProtoType_Type()
)
fsDistributeListCfgProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDistributeListCfgProtoType.setStatus("current")
_FsDistributeListIfIndex_Type = Unsigned32
_FsDistributeListIfIndex_Object = MibTableColumn
fsDistributeListIfIndex = _FsDistributeListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 2),
    _FsDistributeListIfIndex_Type()
)
fsDistributeListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDistributeListIfIndex.setStatus("current")


class _FsDistributeListDirection_Type(Integer32):
    """Custom type fsDistributeListDirection based on Integer32"""
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


_FsDistributeListDirection_Type.__name__ = "Integer32"
_FsDistributeListDirection_Object = MibTableColumn
fsDistributeListDirection = _FsDistributeListDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 3),
    _FsDistributeListDirection_Type()
)
fsDistributeListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDistributeListDirection.setStatus("current")
_FsDistributeListFilteringProtocol_Type = Unsigned32
_FsDistributeListFilteringProtocol_Object = MibTableColumn
fsDistributeListFilteringProtocol = _FsDistributeListFilteringProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 4),
    _FsDistributeListFilteringProtocol_Type()
)
fsDistributeListFilteringProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDistributeListFilteringProtocol.setStatus("current")


class _FsDistributeListFilterType_Type(Integer32):
    """Custom type fsDistributeListFilterType based on Integer32"""
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


_FsDistributeListFilterType_Type.__name__ = "Integer32"
_FsDistributeListFilterType_Object = MibTableColumn
fsDistributeListFilterType = _FsDistributeListFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 5),
    _FsDistributeListFilterType_Type()
)
fsDistributeListFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDistributeListFilterType.setStatus("current")


class _FsDistributeListAclName_Type(DisplayString):
    """Custom type fsDistributeListAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDistributeListAclName_Type.__name__ = "DisplayString"
_FsDistributeListAclName_Object = MibTableColumn
fsDistributeListAclName = _FsDistributeListAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 6),
    _FsDistributeListAclName_Type()
)
fsDistributeListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDistributeListAclName.setStatus("current")


class _FsDistributeListGateWayIpPrefixName_Type(DisplayString):
    """Custom type fsDistributeListGateWayIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDistributeListGateWayIpPrefixName_Type.__name__ = "DisplayString"
_FsDistributeListGateWayIpPrefixName_Object = MibTableColumn
fsDistributeListGateWayIpPrefixName = _FsDistributeListGateWayIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 7),
    _FsDistributeListGateWayIpPrefixName_Type()
)
fsDistributeListGateWayIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDistributeListGateWayIpPrefixName.setStatus("current")


class _FsDistributeListPrefixIpPrefixName_Type(DisplayString):
    """Custom type fsDistributeListPrefixIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDistributeListPrefixIpPrefixName_Type.__name__ = "DisplayString"
_FsDistributeListPrefixIpPrefixName_Object = MibTableColumn
fsDistributeListPrefixIpPrefixName = _FsDistributeListPrefixIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 8),
    _FsDistributeListPrefixIpPrefixName_Type()
)
fsDistributeListPrefixIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDistributeListPrefixIpPrefixName.setStatus("current")
_FsDistributeListStatus_Type = RowStatus
_FsDistributeListStatus_Object = MibTableColumn
fsDistributeListStatus = _FsDistributeListStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 4, 2, 1, 9),
    _FsDistributeListStatus_Type()
)
fsDistributeListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDistributeListStatus.setStatus("current")
_FsipCidrRouteExtendMIBObjects_ObjectIdentity = ObjectIdentity
fsipCidrRouteExtendMIBObjects = _FsipCidrRouteExtendMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5)
)
_FsipCidrRouteTable_Object = MibTable
fsipCidrRouteTable = _FsipCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    fsipCidrRouteTable.setStatus("current")
_FsipCidrRouteEntry_Object = MibTableRow
fsipCidrRouteEntry = _FsipCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1)
)
fsipCidrRouteEntry.setIndexNames(
    (0, "FS-ROUTE-MIB", "fsipCidrRouteDest"),
    (0, "FS-ROUTE-MIB", "fsipCidrRouteMask"),
    (0, "FS-ROUTE-MIB", "fsipCidrRouteTos"),
    (0, "FS-ROUTE-MIB", "fsipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsipCidrRouteEntry.setStatus("current")
_FsipCidrRouteDest_Type = IpAddress
_FsipCidrRouteDest_Object = MibTableColumn
fsipCidrRouteDest = _FsipCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 1),
    _FsipCidrRouteDest_Type()
)
fsipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteDest.setStatus("current")
_FsipCidrRouteMask_Type = IpAddress
_FsipCidrRouteMask_Object = MibTableColumn
fsipCidrRouteMask = _FsipCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 2),
    _FsipCidrRouteMask_Type()
)
fsipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteMask.setStatus("current")
_FsipCidrRouteTos_Type = Integer32
_FsipCidrRouteTos_Object = MibTableColumn
fsipCidrRouteTos = _FsipCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 3),
    _FsipCidrRouteTos_Type()
)
fsipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteTos.setStatus("current")
_FsipCidrRouteNextHop_Type = IpAddress
_FsipCidrRouteNextHop_Object = MibTableColumn
fsipCidrRouteNextHop = _FsipCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 4),
    _FsipCidrRouteNextHop_Type()
)
fsipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteNextHop.setStatus("current")


class _FsipCidrRouteIfIndex_Type(Integer32):
    """Custom type fsipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_FsipCidrRouteIfIndex_Type.__name__ = "Integer32"
_FsipCidrRouteIfIndex_Object = MibTableColumn
fsipCidrRouteIfIndex = _FsipCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 5),
    _FsipCidrRouteIfIndex_Type()
)
fsipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteIfIndex.setStatus("current")


class _FsipCidrRouteType_Type(Integer32):
    """Custom type fsipCidrRouteType based on Integer32"""
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


_FsipCidrRouteType_Type.__name__ = "Integer32"
_FsipCidrRouteType_Object = MibTableColumn
fsipCidrRouteType = _FsipCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 6),
    _FsipCidrRouteType_Type()
)
fsipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteType.setStatus("current")


class _FsipCidrRouteProto_Type(Integer32):
    """Custom type fsipCidrRouteProto based on Integer32"""
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


_FsipCidrRouteProto_Type.__name__ = "Integer32"
_FsipCidrRouteProto_Object = MibTableColumn
fsipCidrRouteProto = _FsipCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 7),
    _FsipCidrRouteProto_Type()
)
fsipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteProto.setStatus("current")


class _FsipCidrRouteAge_Type(Integer32):
    """Custom type fsipCidrRouteAge based on Integer32"""
    defaultValue = 0


_FsipCidrRouteAge_Type.__name__ = "Integer32"
_FsipCidrRouteAge_Object = MibTableColumn
fsipCidrRouteAge = _FsipCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 8),
    _FsipCidrRouteAge_Type()
)
fsipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrRouteAge.setStatus("current")
_FsipCidrRouteInfo_Type = ObjectIdentifier
_FsipCidrRouteInfo_Object = MibTableColumn
fsipCidrRouteInfo = _FsipCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 9),
    _FsipCidrRouteInfo_Type()
)
fsipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteInfo.setStatus("current")


class _FsipCidrRouteNextHopAS_Type(Integer32):
    """Custom type fsipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_FsipCidrRouteNextHopAS_Type.__name__ = "Integer32"
_FsipCidrRouteNextHopAS_Object = MibTableColumn
fsipCidrRouteNextHopAS = _FsipCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 10),
    _FsipCidrRouteNextHopAS_Type()
)
fsipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteNextHopAS.setStatus("current")


class _FsipCidrRouteMetric1_Type(Integer32):
    """Custom type fsipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsipCidrRouteMetric1_Type.__name__ = "Integer32"
_FsipCidrRouteMetric1_Object = MibTableColumn
fsipCidrRouteMetric1 = _FsipCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 11),
    _FsipCidrRouteMetric1_Type()
)
fsipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteMetric1.setStatus("current")


class _FsipCidrRouteMetric2_Type(Integer32):
    """Custom type fsipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_FsipCidrRouteMetric2_Type.__name__ = "Integer32"
_FsipCidrRouteMetric2_Object = MibTableColumn
fsipCidrRouteMetric2 = _FsipCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 12),
    _FsipCidrRouteMetric2_Type()
)
fsipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteMetric2.setStatus("current")


class _FsipCidrRouteMetric3_Type(Integer32):
    """Custom type fsipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_FsipCidrRouteMetric3_Type.__name__ = "Integer32"
_FsipCidrRouteMetric3_Object = MibTableColumn
fsipCidrRouteMetric3 = _FsipCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 13),
    _FsipCidrRouteMetric3_Type()
)
fsipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteMetric3.setStatus("current")


class _FsipCidrRouteMetric4_Type(Integer32):
    """Custom type fsipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_FsipCidrRouteMetric4_Type.__name__ = "Integer32"
_FsipCidrRouteMetric4_Object = MibTableColumn
fsipCidrRouteMetric4 = _FsipCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 14),
    _FsipCidrRouteMetric4_Type()
)
fsipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteMetric4.setStatus("current")


class _FsipCidrRouteMetric5_Type(Integer32):
    """Custom type fsipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_FsipCidrRouteMetric5_Type.__name__ = "Integer32"
_FsipCidrRouteMetric5_Object = MibTableColumn
fsipCidrRouteMetric5 = _FsipCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 15),
    _FsipCidrRouteMetric5_Type()
)
fsipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteMetric5.setStatus("current")
_FsipCidrRouteStatus_Type = RowStatus
_FsipCidrRouteStatus_Object = MibTableColumn
fsipCidrRouteStatus = _FsipCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 16),
    _FsipCidrRouteStatus_Type()
)
fsipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipCidrRouteStatus.setStatus("current")


class _FsipCidrOspfRouteType_Type(Integer32):
    """Custom type fsipCidrOspfRouteType based on Integer32"""
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


_FsipCidrOspfRouteType_Type.__name__ = "Integer32"
_FsipCidrOspfRouteType_Object = MibTableColumn
fsipCidrOspfRouteType = _FsipCidrOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 5, 1, 1, 17),
    _FsipCidrOspfRouteType_Type()
)
fsipCidrOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipCidrOspfRouteType.setStatus("current")
_FsRouteMIBConformance_ObjectIdentity = ObjectIdentity
fsRouteMIBConformance = _FsRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6)
)
_FsRouteMIBCompliances_ObjectIdentity = ObjectIdentity
fsRouteMIBCompliances = _FsRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 1)
)
_FsRouteMIBGroups_ObjectIdentity = ObjectIdentity
fsRouteMIBGroups = _FsRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2)
)

# Managed Objects groups

fsRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 1)
)
fsRouteMIBGroup.setObjects(
    ("FS-ROUTE-MIB", "fsRouteServiceStatus")
)
if mibBuilder.loadTexts:
    fsRouteMIBGroup.setStatus("current")

fsRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 2)
)
fsRouteInfoMIBGroup.setObjects(
      *(("FS-ROUTE-MIB", "fsRoutingProtoInfoProtoType"),
        ("FS-ROUTE-MIB", "fsRoutingProtoInfoGateWay"),
        ("FS-ROUTE-MIB", "fsRoutingProtoInfoDistance"),
        ("FS-ROUTE-MIB", "fsRoutingProtoInfoLastUpdate"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgRoutingProtoType"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgAlways"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgMetric"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgMetricType"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgRouteMap"),
        ("FS-ROUTE-MIB", "fsDefRoutingCfgStatus"))
)
if mibBuilder.loadTexts:
    fsRouteInfoMIBGroup.setStatus("current")

fsRouteMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 3)
)
fsRouteMapMIBGroup.setObjects(
      *(("FS-ROUTE-MIB", "fsRouteMapName"),
        ("FS-ROUTE-MIB", "fsRouteMapSequenceNumber"),
        ("FS-ROUTE-MIB", "fsRouteMapOperType"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchMetric"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchRouteType"),
        ("FS-ROUTE-MIB", "fsRouteMapMetricValueType"),
        ("FS-ROUTE-MIB", "fsRouteMapSetMetric"),
        ("FS-ROUTE-MIB", "fsRouteMapSetLevel"),
        ("FS-ROUTE-MIB", "fsRouteMapSetMetricType"),
        ("FS-ROUTE-MIB", "fsRouteMapSetNexthopSt"),
        ("FS-ROUTE-MIB", "fsRouteMapSetNexthopSt"),
        ("FS-ROUTE-MIB", "fsRouteMapStatus"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchIpAddressAclName"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchType"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchIpAddressStatus"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchTagValue"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchTagStatus"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchInterfaceIfIndex"),
        ("FS-ROUTE-MIB", "fsRouteMapMatchInterfaceStatus"))
)
if mibBuilder.loadTexts:
    fsRouteMapMIBGroup.setStatus("current")

fsRouteRedistributeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 4)
)
fsRouteRedistributeMIBGroup.setObjects(
      *(("FS-ROUTE-MIB", "fsRouteRedistributeProtocolCfg"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeProtocol"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeMetricValue"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeMetricType"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeTagValue"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeRouteMapName"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeStatus"))
)
if mibBuilder.loadTexts:
    fsRouteRedistributeMIBGroup.setStatus("current")

fsRouteFilteringMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 5)
)
fsRouteFilteringMibGroup.setObjects(
      *(("FS-ROUTE-MIB", "fsIpPrefixListName"),
        ("FS-ROUTE-MIB", "fsIpPrefixListSequence"),
        ("FS-ROUTE-MIB", "fsIpPrefixListOperMethod"),
        ("FS-ROUTE-MIB", "fsIpPrefixListIpAddress"),
        ("FS-ROUTE-MIB", "fsIpPrefixListMaskLength"),
        ("FS-ROUTE-MIB", "fsIpPrefixListMinimumPrefixLength"),
        ("FS-ROUTE-MIB", "fsIpPrefixListMaximumPrefixLength"),
        ("FS-ROUTE-MIB", "fsIpPrefixListStatus"),
        ("FS-ROUTE-MIB", "fsDistributeListCfgProtoType"),
        ("FS-ROUTE-MIB", "fsDistributeListIfIndex"),
        ("FS-ROUTE-MIB", "fsDistributeListFilterType"),
        ("FS-ROUTE-MIB", "fsDistributeListDirection"),
        ("FS-ROUTE-MIB", "fsDistributeListAclName"),
        ("FS-ROUTE-MIB", "fsDistributeListGateWayIpPrefixName"),
        ("FS-ROUTE-MIB", "fsDistributeListPrefixIpPrefixName"),
        ("FS-ROUTE-MIB", "fsDistributeListFilteringProtocol"),
        ("FS-ROUTE-MIB", "fsDistributeListStatus"))
)
if mibBuilder.loadTexts:
    fsRouteFilteringMibGroup.setStatus("current")

fsipCidrRouteMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 2, 6)
)
fsipCidrRouteMibGroup.setObjects(
      *(("FS-ROUTE-MIB", "fsipCidrRouteDest"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMask"),
        ("FS-ROUTE-MIB", "fsipCidrRouteTos"),
        ("FS-ROUTE-MIB", "fsipCidrRouteNextHop"),
        ("FS-ROUTE-MIB", "fsipCidrRouteIfIndex"),
        ("FS-ROUTE-MIB", "fsipCidrRouteType"),
        ("FS-ROUTE-MIB", "fsipCidrRouteProto"),
        ("FS-ROUTE-MIB", "fsipCidrRouteAge"),
        ("FS-ROUTE-MIB", "fsipCidrRouteInfo"),
        ("FS-ROUTE-MIB", "fsipCidrRouteNextHopAS"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMetric1"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMetric2"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMetric3"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMetric4"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMetric5"),
        ("FS-ROUTE-MIB", "fsipCidrRouteStatus"),
        ("FS-ROUTE-MIB", "fsipCidrOspfRouteType"))
)
if mibBuilder.loadTexts:
    fsipCidrRouteMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 20, 6, 1, 1)
)
fsRouteMIBCompliance.setObjects(
      *(("FS-ROUTE-MIB", "fsRouteMIBGroup"),
        ("FS-ROUTE-MIB", "fsRouteInfoMIBGroup"),
        ("FS-ROUTE-MIB", "fsRouteMapMIBGroup"),
        ("FS-ROUTE-MIB", "fsRouteRedistributeMIBGroup"),
        ("FS-ROUTE-MIB", "fsRouteFilteringMibGroup"),
        ("FS-ROUTE-MIB", "fsipCidrRouteMibGroup"))
)
if mibBuilder.loadTexts:
    fsRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ROUTE-MIB",
    **{"FSRouteProtoType": FSRouteProtoType,
       "fsRouteMIB": fsRouteMIB,
       "fsRouteMIBObjects": fsRouteMIBObjects,
       "fsRouteServiceStatus": fsRouteServiceStatus,
       "fsRoutingProtoInfoTable": fsRoutingProtoInfoTable,
       "fsRoutingProtoInfoEntry": fsRoutingProtoInfoEntry,
       "fsRoutingProtoInfoProtoType": fsRoutingProtoInfoProtoType,
       "fsRoutingProtoInfoGateWay": fsRoutingProtoInfoGateWay,
       "fsRoutingProtoInfoDistance": fsRoutingProtoInfoDistance,
       "fsRoutingProtoInfoLastUpdate": fsRoutingProtoInfoLastUpdate,
       "fsDefRoutingCfgTable": fsDefRoutingCfgTable,
       "fsDefRoutingCfgEntry": fsDefRoutingCfgEntry,
       "fsDefRoutingCfgRoutingProtoType": fsDefRoutingCfgRoutingProtoType,
       "fsDefRoutingCfgAlways": fsDefRoutingCfgAlways,
       "fsDefRoutingCfgMetric": fsDefRoutingCfgMetric,
       "fsDefRoutingCfgMetricType": fsDefRoutingCfgMetricType,
       "fsDefRoutingCfgRouteMap": fsDefRoutingCfgRouteMap,
       "fsDefRoutingCfgStatus": fsDefRoutingCfgStatus,
       "fsRouteMapMIBObjects": fsRouteMapMIBObjects,
       "fsRouteMapTable": fsRouteMapTable,
       "fsRouteMapEntry": fsRouteMapEntry,
       "fsRouteMapName": fsRouteMapName,
       "fsRouteMapSequenceNumber": fsRouteMapSequenceNumber,
       "fsRouteMapOperType": fsRouteMapOperType,
       "fsRouteMapMatchMetric": fsRouteMapMatchMetric,
       "fsRouteMapMatchRouteType": fsRouteMapMatchRouteType,
       "fsRouteMapMetricValueType": fsRouteMapMetricValueType,
       "fsRouteMapSetMetric": fsRouteMapSetMetric,
       "fsRouteMapSetLevel": fsRouteMapSetLevel,
       "fsRouteMapSetMetricType": fsRouteMapSetMetricType,
       "fsRouteMapSetNexthopSt": fsRouteMapSetNexthopSt,
       "fsRouteMapSetNexthop": fsRouteMapSetNexthop,
       "fsRouteMapStatus": fsRouteMapStatus,
       "fsRouteMapMatchIpAddressTable": fsRouteMapMatchIpAddressTable,
       "fsRouteMapMatchIpAddressEntry": fsRouteMapMatchIpAddressEntry,
       "fsRouteMapMatchType": fsRouteMapMatchType,
       "fsRouteMapMatchIpAddressAclName": fsRouteMapMatchIpAddressAclName,
       "fsRouteMapMatchIpAddressStatus": fsRouteMapMatchIpAddressStatus,
       "fsRouteMapMatchTagTable": fsRouteMapMatchTagTable,
       "fsRouteMapMatchTagEntry": fsRouteMapMatchTagEntry,
       "fsRouteMapMatchTagValue": fsRouteMapMatchTagValue,
       "fsRouteMapMatchTagStatus": fsRouteMapMatchTagStatus,
       "fsRouteMapMatchInterfaceTable": fsRouteMapMatchInterfaceTable,
       "fsRouteMapMatchInterfaceEntry": fsRouteMapMatchInterfaceEntry,
       "fsRouteMapMatchInterfaceIfIndex": fsRouteMapMatchInterfaceIfIndex,
       "fsRouteMapMatchInterfaceStatus": fsRouteMapMatchInterfaceStatus,
       "fsRouteRedistributeMIBObjects": fsRouteRedistributeMIBObjects,
       "fsRouteRedistributeTable": fsRouteRedistributeTable,
       "fsRouteRedistributeEntry": fsRouteRedistributeEntry,
       "fsRouteRedistributeProtocolCfg": fsRouteRedistributeProtocolCfg,
       "fsRouteRedistributeProtocol": fsRouteRedistributeProtocol,
       "fsRouteRedistributeMetricValue": fsRouteRedistributeMetricValue,
       "fsRouteRedistributeMetricType": fsRouteRedistributeMetricType,
       "fsRouteRedistributeTagValue": fsRouteRedistributeTagValue,
       "fsRouteRedistributeRouteMapName": fsRouteRedistributeRouteMapName,
       "fsRouteRedistributeStatus": fsRouteRedistributeStatus,
       "fsRouteFilteringMIBObjects": fsRouteFilteringMIBObjects,
       "fsIpPrefixListTable": fsIpPrefixListTable,
       "fsIpPrefixListEntry": fsIpPrefixListEntry,
       "fsIpPrefixListName": fsIpPrefixListName,
       "fsIpPrefixListSequence": fsIpPrefixListSequence,
       "fsIpPrefixListOperMethod": fsIpPrefixListOperMethod,
       "fsIpPrefixListIpAddress": fsIpPrefixListIpAddress,
       "fsIpPrefixListMaskLength": fsIpPrefixListMaskLength,
       "fsIpPrefixListMinimumPrefixLength": fsIpPrefixListMinimumPrefixLength,
       "fsIpPrefixListMaximumPrefixLength": fsIpPrefixListMaximumPrefixLength,
       "fsIpPrefixListStatus": fsIpPrefixListStatus,
       "fsDistributeListTable": fsDistributeListTable,
       "fsDistributeListEntry": fsDistributeListEntry,
       "fsDistributeListCfgProtoType": fsDistributeListCfgProtoType,
       "fsDistributeListIfIndex": fsDistributeListIfIndex,
       "fsDistributeListDirection": fsDistributeListDirection,
       "fsDistributeListFilteringProtocol": fsDistributeListFilteringProtocol,
       "fsDistributeListFilterType": fsDistributeListFilterType,
       "fsDistributeListAclName": fsDistributeListAclName,
       "fsDistributeListGateWayIpPrefixName": fsDistributeListGateWayIpPrefixName,
       "fsDistributeListPrefixIpPrefixName": fsDistributeListPrefixIpPrefixName,
       "fsDistributeListStatus": fsDistributeListStatus,
       "fsipCidrRouteExtendMIBObjects": fsipCidrRouteExtendMIBObjects,
       "fsipCidrRouteTable": fsipCidrRouteTable,
       "fsipCidrRouteEntry": fsipCidrRouteEntry,
       "fsipCidrRouteDest": fsipCidrRouteDest,
       "fsipCidrRouteMask": fsipCidrRouteMask,
       "fsipCidrRouteTos": fsipCidrRouteTos,
       "fsipCidrRouteNextHop": fsipCidrRouteNextHop,
       "fsipCidrRouteIfIndex": fsipCidrRouteIfIndex,
       "fsipCidrRouteType": fsipCidrRouteType,
       "fsipCidrRouteProto": fsipCidrRouteProto,
       "fsipCidrRouteAge": fsipCidrRouteAge,
       "fsipCidrRouteInfo": fsipCidrRouteInfo,
       "fsipCidrRouteNextHopAS": fsipCidrRouteNextHopAS,
       "fsipCidrRouteMetric1": fsipCidrRouteMetric1,
       "fsipCidrRouteMetric2": fsipCidrRouteMetric2,
       "fsipCidrRouteMetric3": fsipCidrRouteMetric3,
       "fsipCidrRouteMetric4": fsipCidrRouteMetric4,
       "fsipCidrRouteMetric5": fsipCidrRouteMetric5,
       "fsipCidrRouteStatus": fsipCidrRouteStatus,
       "fsipCidrOspfRouteType": fsipCidrOspfRouteType,
       "fsRouteMIBConformance": fsRouteMIBConformance,
       "fsRouteMIBCompliances": fsRouteMIBCompliances,
       "fsRouteMIBCompliance": fsRouteMIBCompliance,
       "fsRouteMIBGroups": fsRouteMIBGroups,
       "fsRouteMIBGroup": fsRouteMIBGroup,
       "fsRouteInfoMIBGroup": fsRouteInfoMIBGroup,
       "fsRouteMapMIBGroup": fsRouteMapMIBGroup,
       "fsRouteRedistributeMIBGroup": fsRouteRedistributeMIBGroup,
       "fsRouteFilteringMibGroup": fsRouteFilteringMibGroup,
       "fsipCidrRouteMibGroup": fsipCidrRouteMibGroup}
)
