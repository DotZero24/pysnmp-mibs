# SNMP MIB module (ARICENT-RIP6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-RIP6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:33 2025
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

fsrip6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3)
)
if mibBuilder.loadTexts:
    fsrip6.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsrip6Scalars_ObjectIdentity = ObjectIdentity
fsrip6Scalars = _Fsrip6Scalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1)
)


class _Fsrip6RoutePreference_Type(Integer32):
    """Custom type fsrip6RoutePreference based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("bestmetric", 3))
    )


_Fsrip6RoutePreference_Type.__name__ = "Integer32"
_Fsrip6RoutePreference_Object = MibScalar
fsrip6RoutePreference = _Fsrip6RoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 1),
    _Fsrip6RoutePreference_Type()
)
fsrip6RoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RoutePreference.setStatus("current")


class _Fsrip6GlobalDebug_Type(Integer32):
    """Custom type fsrip6GlobalDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsrip6GlobalDebug_Type.__name__ = "Integer32"
_Fsrip6GlobalDebug_Object = MibScalar
fsrip6GlobalDebug = _Fsrip6GlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 2),
    _Fsrip6GlobalDebug_Type()
)
fsrip6GlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6GlobalDebug.setStatus("current")
_Fsrip6GlobalInstanceIndex_Type = Integer32
_Fsrip6GlobalInstanceIndex_Object = MibScalar
fsrip6GlobalInstanceIndex = _Fsrip6GlobalInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 3),
    _Fsrip6GlobalInstanceIndex_Type()
)
fsrip6GlobalInstanceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6GlobalInstanceIndex.setStatus("current")


class _Fsrip6PeerFilter_Type(Integer32):
    """Custom type fsrip6PeerFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_Fsrip6PeerFilter_Type.__name__ = "Integer32"
_Fsrip6PeerFilter_Object = MibScalar
fsrip6PeerFilter = _Fsrip6PeerFilter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 4),
    _Fsrip6PeerFilter_Type()
)
fsrip6PeerFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6PeerFilter.setStatus("current")


class _Fsrip6AdvFilter_Type(Integer32):
    """Custom type fsrip6AdvFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Fsrip6AdvFilter_Type.__name__ = "Integer32"
_Fsrip6AdvFilter_Object = MibScalar
fsrip6AdvFilter = _Fsrip6AdvFilter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 5),
    _Fsrip6AdvFilter_Type()
)
fsrip6AdvFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6AdvFilter.setStatus("current")


class _FsRip6RRDAdminStatus_Type(Integer32):
    """Custom type fsRip6RRDAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsRip6RRDAdminStatus_Type.__name__ = "Integer32"
_FsRip6RRDAdminStatus_Object = MibScalar
fsRip6RRDAdminStatus = _FsRip6RRDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 6),
    _FsRip6RRDAdminStatus_Type()
)
fsRip6RRDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6RRDAdminStatus.setStatus("current")
_Fsrip6RRDProtoMaskForEnable_Type = Integer32
_Fsrip6RRDProtoMaskForEnable_Object = MibScalar
fsrip6RRDProtoMaskForEnable = _Fsrip6RRDProtoMaskForEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 7),
    _Fsrip6RRDProtoMaskForEnable_Type()
)
fsrip6RRDProtoMaskForEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RRDProtoMaskForEnable.setStatus("current")
_Fsrip6RRDSrcProtoMaskForDisable_Type = Integer32
_Fsrip6RRDSrcProtoMaskForDisable_Object = MibScalar
fsrip6RRDSrcProtoMaskForDisable = _Fsrip6RRDSrcProtoMaskForDisable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 8),
    _Fsrip6RRDSrcProtoMaskForDisable_Type()
)
fsrip6RRDSrcProtoMaskForDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RRDSrcProtoMaskForDisable.setStatus("current")


class _Fsrip6RRDRouteDefMetric_Type(Integer32):
    """Custom type fsrip6RRDRouteDefMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Fsrip6RRDRouteDefMetric_Type.__name__ = "Integer32"
_Fsrip6RRDRouteDefMetric_Object = MibScalar
fsrip6RRDRouteDefMetric = _Fsrip6RRDRouteDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 9),
    _Fsrip6RRDRouteDefMetric_Type()
)
fsrip6RRDRouteDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RRDRouteDefMetric.setStatus("current")


class _Fsrip6RRDRouteMapName_Type(OctetString):
    """Custom type fsrip6RRDRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fsrip6RRDRouteMapName_Type.__name__ = "OctetString"
_Fsrip6RRDRouteMapName_Object = MibScalar
fsrip6RRDRouteMapName = _Fsrip6RRDRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 10),
    _Fsrip6RRDRouteMapName_Type()
)
fsrip6RRDRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RRDRouteMapName.setStatus("current")
_Fsrip6RouteCount_Type = Integer32
_Fsrip6RouteCount_Object = MibScalar
fsrip6RouteCount = _Fsrip6RouteCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 1, 11),
    _Fsrip6RouteCount_Type()
)
fsrip6RouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RouteCount.setStatus("current")
_Fsrip6Tables_ObjectIdentity = ObjectIdentity
fsrip6Tables = _Fsrip6Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2)
)
_Fsrip6InstanceTable_Object = MibTable
fsrip6InstanceTable = _Fsrip6InstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fsrip6InstanceTable.setStatus("current")
_Fsrip6InstanceEntry_Object = MibTableRow
fsrip6InstanceEntry = _Fsrip6InstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 1, 1)
)
fsrip6InstanceEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6InstanceIndex"),
)
if mibBuilder.loadTexts:
    fsrip6InstanceEntry.setStatus("current")


class _Fsrip6InstanceIndex_Type(Integer32):
    """Custom type fsrip6InstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fsrip6InstanceIndex_Type.__name__ = "Integer32"
_Fsrip6InstanceIndex_Object = MibTableColumn
fsrip6InstanceIndex = _Fsrip6InstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 1, 1, 1),
    _Fsrip6InstanceIndex_Type()
)
fsrip6InstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6InstanceIndex.setStatus("current")


class _Fsrip6InstanceStatus_Type(Integer32):
    """Custom type fsrip6InstanceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_Fsrip6InstanceStatus_Type.__name__ = "Integer32"
_Fsrip6InstanceStatus_Object = MibTableColumn
fsrip6InstanceStatus = _Fsrip6InstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 1, 1, 2),
    _Fsrip6InstanceStatus_Type()
)
fsrip6InstanceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6InstanceStatus.setStatus("current")
_Fsrip6InstIfMapTable_Object = MibTable
fsrip6InstIfMapTable = _Fsrip6InstIfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fsrip6InstIfMapTable.setStatus("current")
_Fsrip6InstIfMapEntry_Object = MibTableRow
fsrip6InstIfMapEntry = _Fsrip6InstIfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 2, 1)
)
fsrip6InstIfMapEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6IfIndex"),
)
if mibBuilder.loadTexts:
    fsrip6InstIfMapEntry.setStatus("current")


class _Fsrip6IfIndex_Type(Integer32):
    """Custom type fsrip6IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsrip6IfIndex_Type.__name__ = "Integer32"
_Fsrip6IfIndex_Object = MibTableColumn
fsrip6IfIndex = _Fsrip6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 2, 1, 1),
    _Fsrip6IfIndex_Type()
)
fsrip6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6IfIndex.setStatus("current")
_Fsrip6InstIfMapInstId_Type = Integer32
_Fsrip6InstIfMapInstId_Object = MibTableColumn
fsrip6InstIfMapInstId = _Fsrip6InstIfMapInstId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 2, 1, 2),
    _Fsrip6InstIfMapInstId_Type()
)
fsrip6InstIfMapInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6InstIfMapInstId.setStatus("current")


class _Fsrip6InstIfMapIfAtchStatus_Type(Integer32):
    """Custom type fsrip6InstIfMapIfAtchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detached", 0),
          ("attached", 1))
    )


_Fsrip6InstIfMapIfAtchStatus_Type.__name__ = "Integer32"
_Fsrip6InstIfMapIfAtchStatus_Object = MibTableColumn
fsrip6InstIfMapIfAtchStatus = _Fsrip6InstIfMapIfAtchStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 2, 1, 3),
    _Fsrip6InstIfMapIfAtchStatus_Type()
)
fsrip6InstIfMapIfAtchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6InstIfMapIfAtchStatus.setStatus("current")
_Fsrip6RipIfTable_Object = MibTable
fsrip6RipIfTable = _Fsrip6RipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3)
)
if mibBuilder.loadTexts:
    fsrip6RipIfTable.setStatus("current")
_Fsrip6RipIfEntry_Object = MibTableRow
fsrip6RipIfEntry = _Fsrip6RipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1)
)
fsrip6RipIfEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6RipIfIndex"),
)
if mibBuilder.loadTexts:
    fsrip6RipIfEntry.setStatus("current")


class _Fsrip6RipIfIndex_Type(Integer32):
    """Custom type fsrip6RipIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsrip6RipIfIndex_Type.__name__ = "Integer32"
_Fsrip6RipIfIndex_Object = MibTableColumn
fsrip6RipIfIndex = _Fsrip6RipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 1),
    _Fsrip6RipIfIndex_Type()
)
fsrip6RipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipIfIndex.setStatus("current")


class _Fsrip6RipIfProfileIndex_Type(Integer32):
    """Custom type fsrip6RipIfProfileIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Fsrip6RipIfProfileIndex_Type.__name__ = "Integer32"
_Fsrip6RipIfProfileIndex_Object = MibTableColumn
fsrip6RipIfProfileIndex = _Fsrip6RipIfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 2),
    _Fsrip6RipIfProfileIndex_Type()
)
fsrip6RipIfProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipIfProfileIndex.setStatus("current")


class _Fsrip6RipIfCost_Type(Integer32):
    """Custom type fsrip6RipIfCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fsrip6RipIfCost_Type.__name__ = "Integer32"
_Fsrip6RipIfCost_Object = MibTableColumn
fsrip6RipIfCost = _Fsrip6RipIfCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 3),
    _Fsrip6RipIfCost_Type()
)
fsrip6RipIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipIfCost.setStatus("current")


class _Fsrip6RipIfOperStatus_Type(Integer32):
    """Custom type fsrip6RipIfOperStatus based on Integer32"""
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
        *(("enabledup", 1),
          ("enableddown", 2),
          ("disabledup", 3),
          ("disableddown", 4))
    )


_Fsrip6RipIfOperStatus_Type.__name__ = "Integer32"
_Fsrip6RipIfOperStatus_Object = MibTableColumn
fsrip6RipIfOperStatus = _Fsrip6RipIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 4),
    _Fsrip6RipIfOperStatus_Type()
)
fsrip6RipIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfOperStatus.setStatus("current")


class _Fsrip6RipIfProtocolEnable_Type(Integer32):
    """Custom type fsrip6RipIfProtocolEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Fsrip6RipIfProtocolEnable_Type.__name__ = "Integer32"
_Fsrip6RipIfProtocolEnable_Object = MibTableColumn
fsrip6RipIfProtocolEnable = _Fsrip6RipIfProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 5),
    _Fsrip6RipIfProtocolEnable_Type()
)
fsrip6RipIfProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipIfProtocolEnable.setStatus("current")
_Fsrip6RipIfInMessages_Type = Counter32
_Fsrip6RipIfInMessages_Object = MibTableColumn
fsrip6RipIfInMessages = _Fsrip6RipIfInMessages_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 6),
    _Fsrip6RipIfInMessages_Type()
)
fsrip6RipIfInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfInMessages.setStatus("current")
_Fsrip6RipIfInRequests_Type = Counter32
_Fsrip6RipIfInRequests_Object = MibTableColumn
fsrip6RipIfInRequests = _Fsrip6RipIfInRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 7),
    _Fsrip6RipIfInRequests_Type()
)
fsrip6RipIfInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfInRequests.setStatus("current")
_Fsrip6RipIfInResponses_Type = Counter32
_Fsrip6RipIfInResponses_Object = MibTableColumn
fsrip6RipIfInResponses = _Fsrip6RipIfInResponses_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 8),
    _Fsrip6RipIfInResponses_Type()
)
fsrip6RipIfInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfInResponses.setStatus("current")
_Fsrip6RipIfUnknownCmds_Type = Counter32
_Fsrip6RipIfUnknownCmds_Object = MibTableColumn
fsrip6RipIfUnknownCmds = _Fsrip6RipIfUnknownCmds_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 9),
    _Fsrip6RipIfUnknownCmds_Type()
)
fsrip6RipIfUnknownCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfUnknownCmds.setStatus("current")
_Fsrip6RipIfInOtherVer_Type = Counter32
_Fsrip6RipIfInOtherVer_Object = MibTableColumn
fsrip6RipIfInOtherVer = _Fsrip6RipIfInOtherVer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 10),
    _Fsrip6RipIfInOtherVer_Type()
)
fsrip6RipIfInOtherVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfInOtherVer.setStatus("current")
_Fsrip6RipIfInDiscards_Type = Counter32
_Fsrip6RipIfInDiscards_Object = MibTableColumn
fsrip6RipIfInDiscards = _Fsrip6RipIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 11),
    _Fsrip6RipIfInDiscards_Type()
)
fsrip6RipIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfInDiscards.setStatus("current")
_Fsrip6RipIfOutMessages_Type = Counter32
_Fsrip6RipIfOutMessages_Object = MibTableColumn
fsrip6RipIfOutMessages = _Fsrip6RipIfOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 12),
    _Fsrip6RipIfOutMessages_Type()
)
fsrip6RipIfOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfOutMessages.setStatus("current")
_Fsrip6RipIfOutRequests_Type = Counter32
_Fsrip6RipIfOutRequests_Object = MibTableColumn
fsrip6RipIfOutRequests = _Fsrip6RipIfOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 13),
    _Fsrip6RipIfOutRequests_Type()
)
fsrip6RipIfOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfOutRequests.setStatus("current")
_Fsrip6RipIfOutResponses_Type = Counter32
_Fsrip6RipIfOutResponses_Object = MibTableColumn
fsrip6RipIfOutResponses = _Fsrip6RipIfOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 14),
    _Fsrip6RipIfOutResponses_Type()
)
fsrip6RipIfOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfOutResponses.setStatus("current")
_Fsrip6RipIfOutTrigUpdates_Type = Counter32
_Fsrip6RipIfOutTrigUpdates_Object = MibTableColumn
fsrip6RipIfOutTrigUpdates = _Fsrip6RipIfOutTrigUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 15),
    _Fsrip6RipIfOutTrigUpdates_Type()
)
fsrip6RipIfOutTrigUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipIfOutTrigUpdates.setStatus("current")


class _Fsrip6RipIfDefRouteAdvt_Type(Integer32):
    """Custom type fsrip6RipIfDefRouteAdvt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Fsrip6RipIfDefRouteAdvt_Type.__name__ = "Integer32"
_Fsrip6RipIfDefRouteAdvt_Object = MibTableColumn
fsrip6RipIfDefRouteAdvt = _Fsrip6RipIfDefRouteAdvt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 3, 1, 16),
    _Fsrip6RipIfDefRouteAdvt_Type()
)
fsrip6RipIfDefRouteAdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipIfDefRouteAdvt.setStatus("current")
_Fsrip6RipProfileTable_Object = MibTable
fsrip6RipProfileTable = _Fsrip6RipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4)
)
if mibBuilder.loadTexts:
    fsrip6RipProfileTable.setStatus("current")
_Fsrip6RipProfileEntry_Object = MibTableRow
fsrip6RipProfileEntry = _Fsrip6RipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1)
)
fsrip6RipProfileEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6RipProfileIndex"),
)
if mibBuilder.loadTexts:
    fsrip6RipProfileEntry.setStatus("current")


class _Fsrip6RipProfileIndex_Type(Integer32):
    """Custom type fsrip6RipProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Fsrip6RipProfileIndex_Type.__name__ = "Integer32"
_Fsrip6RipProfileIndex_Object = MibTableColumn
fsrip6RipProfileIndex = _Fsrip6RipProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 1),
    _Fsrip6RipProfileIndex_Type()
)
fsrip6RipProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipProfileIndex.setStatus("current")


class _Fsrip6RipProfileStatus_Type(Integer32):
    """Custom type fsrip6RipProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_Fsrip6RipProfileStatus_Type.__name__ = "Integer32"
_Fsrip6RipProfileStatus_Object = MibTableColumn
fsrip6RipProfileStatus = _Fsrip6RipProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 2),
    _Fsrip6RipProfileStatus_Type()
)
fsrip6RipProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfileStatus.setStatus("current")


class _Fsrip6RipProfileHorizon_Type(Integer32):
    """Custom type fsrip6RipProfileHorizon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nohorizon", 1),
          ("splithorizon", 2),
          ("poisonreverse", 3))
    )


_Fsrip6RipProfileHorizon_Type.__name__ = "Integer32"
_Fsrip6RipProfileHorizon_Object = MibTableColumn
fsrip6RipProfileHorizon = _Fsrip6RipProfileHorizon_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 3),
    _Fsrip6RipProfileHorizon_Type()
)
fsrip6RipProfileHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfileHorizon.setStatus("current")


class _Fsrip6RipProfilePeriodicUpdTime_Type(Integer32):
    """Custom type fsrip6RipProfilePeriodicUpdTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 500),
    )


_Fsrip6RipProfilePeriodicUpdTime_Type.__name__ = "Integer32"
_Fsrip6RipProfilePeriodicUpdTime_Object = MibTableColumn
fsrip6RipProfilePeriodicUpdTime = _Fsrip6RipProfilePeriodicUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 4),
    _Fsrip6RipProfilePeriodicUpdTime_Type()
)
fsrip6RipProfilePeriodicUpdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfilePeriodicUpdTime.setStatus("current")


class _Fsrip6RipProfileTrigDelayTime_Type(Integer32):
    """Custom type fsrip6RipProfileTrigDelayTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsrip6RipProfileTrigDelayTime_Type.__name__ = "Integer32"
_Fsrip6RipProfileTrigDelayTime_Object = MibTableColumn
fsrip6RipProfileTrigDelayTime = _Fsrip6RipProfileTrigDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 5),
    _Fsrip6RipProfileTrigDelayTime_Type()
)
fsrip6RipProfileTrigDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfileTrigDelayTime.setStatus("current")


class _Fsrip6RipProfileRouteAge_Type(Integer32):
    """Custom type fsrip6RipProfileRouteAge based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 500),
    )


_Fsrip6RipProfileRouteAge_Type.__name__ = "Integer32"
_Fsrip6RipProfileRouteAge_Object = MibTableColumn
fsrip6RipProfileRouteAge = _Fsrip6RipProfileRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 6),
    _Fsrip6RipProfileRouteAge_Type()
)
fsrip6RipProfileRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfileRouteAge.setStatus("current")


class _Fsrip6RipProfileGarbageCollectTime_Type(Integer32):
    """Custom type fsrip6RipProfileGarbageCollectTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 180),
    )


_Fsrip6RipProfileGarbageCollectTime_Type.__name__ = "Integer32"
_Fsrip6RipProfileGarbageCollectTime_Object = MibTableColumn
fsrip6RipProfileGarbageCollectTime = _Fsrip6RipProfileGarbageCollectTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 4, 1, 7),
    _Fsrip6RipProfileGarbageCollectTime_Type()
)
fsrip6RipProfileGarbageCollectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipProfileGarbageCollectTime.setStatus("current")
_Fsrip6RipRouteTable_Object = MibTable
fsrip6RipRouteTable = _Fsrip6RipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5)
)
if mibBuilder.loadTexts:
    fsrip6RipRouteTable.setStatus("current")
_Fsrip6RipRouteEntry_Object = MibTableRow
fsrip6RipRouteEntry = _Fsrip6RipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1)
)
fsrip6RipRouteEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6RipRouteDest"),
    (0, "ARICENT-RIP6-MIB", "fsrip6RipRoutePfxLength"),
    (0, "ARICENT-RIP6-MIB", "fsrip6RipRouteProtocol"),
    (0, "ARICENT-RIP6-MIB", "fsrip6RipRouteIfIndex"),
)
if mibBuilder.loadTexts:
    fsrip6RipRouteEntry.setStatus("current")


class _Fsrip6RipRouteDest_Type(OctetString):
    """Custom type fsrip6RipRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Fsrip6RipRouteDest_Type.__name__ = "OctetString"
_Fsrip6RipRouteDest_Object = MibTableColumn
fsrip6RipRouteDest = _Fsrip6RipRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 1),
    _Fsrip6RipRouteDest_Type()
)
fsrip6RipRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipRouteDest.setStatus("current")


class _Fsrip6RipRoutePfxLength_Type(Integer32):
    """Custom type fsrip6RipRoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Fsrip6RipRoutePfxLength_Type.__name__ = "Integer32"
_Fsrip6RipRoutePfxLength_Object = MibTableColumn
fsrip6RipRoutePfxLength = _Fsrip6RipRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 2),
    _Fsrip6RipRoutePfxLength_Type()
)
fsrip6RipRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipRoutePfxLength.setStatus("current")


class _Fsrip6RipRouteProtocol_Type(Integer32):
    """Custom type fsrip6RipRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("ndisc", 4),
          ("rip", 5),
          ("ospf", 6),
          ("idrp", 7))
    )


_Fsrip6RipRouteProtocol_Type.__name__ = "Integer32"
_Fsrip6RipRouteProtocol_Object = MibTableColumn
fsrip6RipRouteProtocol = _Fsrip6RipRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 3),
    _Fsrip6RipRouteProtocol_Type()
)
fsrip6RipRouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipRouteProtocol.setStatus("current")


class _Fsrip6RipRouteIfIndex_Type(Integer32):
    """Custom type fsrip6RipRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsrip6RipRouteIfIndex_Type.__name__ = "Integer32"
_Fsrip6RipRouteIfIndex_Object = MibTableColumn
fsrip6RipRouteIfIndex = _Fsrip6RipRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 4),
    _Fsrip6RipRouteIfIndex_Type()
)
fsrip6RipRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipRouteIfIndex.setStatus("current")


class _Fsrip6RipRouteNextHop_Type(OctetString):
    """Custom type fsrip6RipRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Fsrip6RipRouteNextHop_Type.__name__ = "OctetString"
_Fsrip6RipRouteNextHop_Object = MibTableColumn
fsrip6RipRouteNextHop = _Fsrip6RipRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 5),
    _Fsrip6RipRouteNextHop_Type()
)
fsrip6RipRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipRouteNextHop.setStatus("current")


class _Fsrip6RipRouteMetric_Type(Integer32):
    """Custom type fsrip6RipRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Fsrip6RipRouteMetric_Type.__name__ = "Integer32"
_Fsrip6RipRouteMetric_Object = MibTableColumn
fsrip6RipRouteMetric = _Fsrip6RipRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 6),
    _Fsrip6RipRouteMetric_Type()
)
fsrip6RipRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipRouteMetric.setStatus("current")


class _Fsrip6RipRouteTag_Type(Integer32):
    """Custom type fsrip6RipRouteTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsrip6RipRouteTag_Type.__name__ = "Integer32"
_Fsrip6RipRouteTag_Object = MibTableColumn
fsrip6RipRouteTag = _Fsrip6RipRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 7),
    _Fsrip6RipRouteTag_Type()
)
fsrip6RipRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipRouteTag.setStatus("current")
_Fsrip6RipRouteAge_Type = Integer32
_Fsrip6RipRouteAge_Object = MibTableColumn
fsrip6RipRouteAge = _Fsrip6RipRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 5, 1, 8),
    _Fsrip6RipRouteAge_Type()
)
fsrip6RipRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsrip6RipRouteAge.setStatus("current")
_Fsrip6RipPeerTable_Object = MibTable
fsrip6RipPeerTable = _Fsrip6RipPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 6)
)
if mibBuilder.loadTexts:
    fsrip6RipPeerTable.setStatus("current")
_Fsrip6RipPeerEntry_Object = MibTableRow
fsrip6RipPeerEntry = _Fsrip6RipPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 6, 1)
)
fsrip6RipPeerEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6RipPeerAddr"),
)
if mibBuilder.loadTexts:
    fsrip6RipPeerEntry.setStatus("current")


class _Fsrip6RipPeerAddr_Type(OctetString):
    """Custom type fsrip6RipPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Fsrip6RipPeerAddr_Type.__name__ = "OctetString"
_Fsrip6RipPeerAddr_Object = MibTableColumn
fsrip6RipPeerAddr = _Fsrip6RipPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 6, 1, 1),
    _Fsrip6RipPeerAddr_Type()
)
fsrip6RipPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipPeerAddr.setStatus("current")


class _Fsrip6RipPeerEntryStatus_Type(Integer32):
    """Custom type fsrip6RipPeerEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_Fsrip6RipPeerEntryStatus_Type.__name__ = "Integer32"
_Fsrip6RipPeerEntryStatus_Object = MibTableColumn
fsrip6RipPeerEntryStatus = _Fsrip6RipPeerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 6, 1, 2),
    _Fsrip6RipPeerEntryStatus_Type()
)
fsrip6RipPeerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipPeerEntryStatus.setStatus("current")
_Fsrip6RipAdvFilterTable_Object = MibTable
fsrip6RipAdvFilterTable = _Fsrip6RipAdvFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 7)
)
if mibBuilder.loadTexts:
    fsrip6RipAdvFilterTable.setStatus("current")
_Fsrip6RipAdvFilterEntry_Object = MibTableRow
fsrip6RipAdvFilterEntry = _Fsrip6RipAdvFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 7, 1)
)
fsrip6RipAdvFilterEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsrip6RipAdvFilterAddress"),
)
if mibBuilder.loadTexts:
    fsrip6RipAdvFilterEntry.setStatus("current")


class _Fsrip6RipAdvFilterAddress_Type(OctetString):
    """Custom type fsrip6RipAdvFilterAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Fsrip6RipAdvFilterAddress_Type.__name__ = "OctetString"
_Fsrip6RipAdvFilterAddress_Object = MibTableColumn
fsrip6RipAdvFilterAddress = _Fsrip6RipAdvFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 7, 1, 1),
    _Fsrip6RipAdvFilterAddress_Type()
)
fsrip6RipAdvFilterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsrip6RipAdvFilterAddress.setStatus("current")


class _Fsrip6RipAdvFilterStatus_Type(Integer32):
    """Custom type fsrip6RipAdvFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_Fsrip6RipAdvFilterStatus_Type.__name__ = "Integer32"
_Fsrip6RipAdvFilterStatus_Object = MibTableColumn
fsrip6RipAdvFilterStatus = _Fsrip6RipAdvFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 2, 7, 1, 2),
    _Fsrip6RipAdvFilterStatus_Type()
)
fsrip6RipAdvFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsrip6RipAdvFilterStatus.setStatus("current")
_Fsrip6DistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsrip6DistInOutRouteMap = _Fsrip6DistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3)
)
_FsRip6DistInOutRouteMapTable_Object = MibTable
fsRip6DistInOutRouteMapTable = _FsRip6DistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1)
)
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapTable.setStatus("current")
_FsRip6DistInOutRouteMapEntry_Object = MibTableRow
fsRip6DistInOutRouteMapEntry = _FsRip6DistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1, 1)
)
fsRip6DistInOutRouteMapEntry.setIndexNames(
    (0, "ARICENT-RIP6-MIB", "fsRip6DistInOutRouteMapName"),
    (0, "ARICENT-RIP6-MIB", "fsRip6DistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapEntry.setStatus("current")


class _FsRip6DistInOutRouteMapName_Type(DisplayString):
    """Custom type fsRip6DistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRip6DistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsRip6DistInOutRouteMapName_Object = MibTableColumn
fsRip6DistInOutRouteMapName = _FsRip6DistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1, 1, 1),
    _FsRip6DistInOutRouteMapName_Type()
)
fsRip6DistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapName.setStatus("current")


class _FsRip6DistInOutRouteMapType_Type(Integer32):
    """Custom type fsRip6DistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsRip6DistInOutRouteMapType_Type.__name__ = "Integer32"
_FsRip6DistInOutRouteMapType_Object = MibTableColumn
fsRip6DistInOutRouteMapType = _FsRip6DistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1, 1, 3),
    _FsRip6DistInOutRouteMapType_Type()
)
fsRip6DistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapType.setStatus("current")


class _FsRip6DistInOutRouteMapValue_Type(Integer32):
    """Custom type fsRip6DistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRip6DistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsRip6DistInOutRouteMapValue_Object = MibTableColumn
fsRip6DistInOutRouteMapValue = _FsRip6DistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1, 1, 4),
    _FsRip6DistInOutRouteMapValue_Type()
)
fsRip6DistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapValue.setStatus("current")
_FsRip6DistInOutRouteMapRowStatus_Type = RowStatus
_FsRip6DistInOutRouteMapRowStatus_Object = MibTableColumn
fsRip6DistInOutRouteMapRowStatus = _FsRip6DistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 3, 1, 1, 5),
    _FsRip6DistInOutRouteMapRowStatus_Type()
)
fsRip6DistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6DistInOutRouteMapRowStatus.setStatus("current")
_Fsrip6PreferenceGroup_ObjectIdentity = ObjectIdentity
fsrip6PreferenceGroup = _Fsrip6PreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3, 4)
)


class _FsRip6PreferenceValue_Type(Integer32):
    """Custom type fsRip6PreferenceValue based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRip6PreferenceValue_Type.__name__ = "Integer32"
_FsRip6PreferenceValue_Object = MibScalar
fsRip6PreferenceValue = _FsRip6PreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 4, 1),
    _FsRip6PreferenceValue_Type()
)
fsRip6PreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6PreferenceValue.setStatus("current")
_FsRip6Test_ObjectIdentity = ObjectIdentity
fsRip6Test = _FsRip6Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 3, 5)
)


class _FsRip6TestBulkUpd_Type(Integer32):
    """Custom type fsRip6TestBulkUpd based on Integer32"""
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


_FsRip6TestBulkUpd_Type.__name__ = "Integer32"
_FsRip6TestBulkUpd_Object = MibScalar
fsRip6TestBulkUpd = _FsRip6TestBulkUpd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 5, 1),
    _FsRip6TestBulkUpd_Type()
)
fsRip6TestBulkUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6TestBulkUpd.setStatus("current")


class _FsRip6TestDynamicUpd_Type(Integer32):
    """Custom type fsRip6TestDynamicUpd based on Integer32"""
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


_FsRip6TestDynamicUpd_Type.__name__ = "Integer32"
_FsRip6TestDynamicUpd_Object = MibScalar
fsRip6TestDynamicUpd = _FsRip6TestDynamicUpd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 3, 5, 2),
    _FsRip6TestDynamicUpd_Type()
)
fsRip6TestDynamicUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip6TestDynamicUpd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-RIP6-MIB",
    **{"fsrip6": fsrip6,
       "fsrip6Scalars": fsrip6Scalars,
       "fsrip6RoutePreference": fsrip6RoutePreference,
       "fsrip6GlobalDebug": fsrip6GlobalDebug,
       "fsrip6GlobalInstanceIndex": fsrip6GlobalInstanceIndex,
       "fsrip6PeerFilter": fsrip6PeerFilter,
       "fsrip6AdvFilter": fsrip6AdvFilter,
       "fsRip6RRDAdminStatus": fsRip6RRDAdminStatus,
       "fsrip6RRDProtoMaskForEnable": fsrip6RRDProtoMaskForEnable,
       "fsrip6RRDSrcProtoMaskForDisable": fsrip6RRDSrcProtoMaskForDisable,
       "fsrip6RRDRouteDefMetric": fsrip6RRDRouteDefMetric,
       "fsrip6RRDRouteMapName": fsrip6RRDRouteMapName,
       "fsrip6RouteCount": fsrip6RouteCount,
       "fsrip6Tables": fsrip6Tables,
       "fsrip6InstanceTable": fsrip6InstanceTable,
       "fsrip6InstanceEntry": fsrip6InstanceEntry,
       "fsrip6InstanceIndex": fsrip6InstanceIndex,
       "fsrip6InstanceStatus": fsrip6InstanceStatus,
       "fsrip6InstIfMapTable": fsrip6InstIfMapTable,
       "fsrip6InstIfMapEntry": fsrip6InstIfMapEntry,
       "fsrip6IfIndex": fsrip6IfIndex,
       "fsrip6InstIfMapInstId": fsrip6InstIfMapInstId,
       "fsrip6InstIfMapIfAtchStatus": fsrip6InstIfMapIfAtchStatus,
       "fsrip6RipIfTable": fsrip6RipIfTable,
       "fsrip6RipIfEntry": fsrip6RipIfEntry,
       "fsrip6RipIfIndex": fsrip6RipIfIndex,
       "fsrip6RipIfProfileIndex": fsrip6RipIfProfileIndex,
       "fsrip6RipIfCost": fsrip6RipIfCost,
       "fsrip6RipIfOperStatus": fsrip6RipIfOperStatus,
       "fsrip6RipIfProtocolEnable": fsrip6RipIfProtocolEnable,
       "fsrip6RipIfInMessages": fsrip6RipIfInMessages,
       "fsrip6RipIfInRequests": fsrip6RipIfInRequests,
       "fsrip6RipIfInResponses": fsrip6RipIfInResponses,
       "fsrip6RipIfUnknownCmds": fsrip6RipIfUnknownCmds,
       "fsrip6RipIfInOtherVer": fsrip6RipIfInOtherVer,
       "fsrip6RipIfInDiscards": fsrip6RipIfInDiscards,
       "fsrip6RipIfOutMessages": fsrip6RipIfOutMessages,
       "fsrip6RipIfOutRequests": fsrip6RipIfOutRequests,
       "fsrip6RipIfOutResponses": fsrip6RipIfOutResponses,
       "fsrip6RipIfOutTrigUpdates": fsrip6RipIfOutTrigUpdates,
       "fsrip6RipIfDefRouteAdvt": fsrip6RipIfDefRouteAdvt,
       "fsrip6RipProfileTable": fsrip6RipProfileTable,
       "fsrip6RipProfileEntry": fsrip6RipProfileEntry,
       "fsrip6RipProfileIndex": fsrip6RipProfileIndex,
       "fsrip6RipProfileStatus": fsrip6RipProfileStatus,
       "fsrip6RipProfileHorizon": fsrip6RipProfileHorizon,
       "fsrip6RipProfilePeriodicUpdTime": fsrip6RipProfilePeriodicUpdTime,
       "fsrip6RipProfileTrigDelayTime": fsrip6RipProfileTrigDelayTime,
       "fsrip6RipProfileRouteAge": fsrip6RipProfileRouteAge,
       "fsrip6RipProfileGarbageCollectTime": fsrip6RipProfileGarbageCollectTime,
       "fsrip6RipRouteTable": fsrip6RipRouteTable,
       "fsrip6RipRouteEntry": fsrip6RipRouteEntry,
       "fsrip6RipRouteDest": fsrip6RipRouteDest,
       "fsrip6RipRoutePfxLength": fsrip6RipRoutePfxLength,
       "fsrip6RipRouteProtocol": fsrip6RipRouteProtocol,
       "fsrip6RipRouteIfIndex": fsrip6RipRouteIfIndex,
       "fsrip6RipRouteNextHop": fsrip6RipRouteNextHop,
       "fsrip6RipRouteMetric": fsrip6RipRouteMetric,
       "fsrip6RipRouteTag": fsrip6RipRouteTag,
       "fsrip6RipRouteAge": fsrip6RipRouteAge,
       "fsrip6RipPeerTable": fsrip6RipPeerTable,
       "fsrip6RipPeerEntry": fsrip6RipPeerEntry,
       "fsrip6RipPeerAddr": fsrip6RipPeerAddr,
       "fsrip6RipPeerEntryStatus": fsrip6RipPeerEntryStatus,
       "fsrip6RipAdvFilterTable": fsrip6RipAdvFilterTable,
       "fsrip6RipAdvFilterEntry": fsrip6RipAdvFilterEntry,
       "fsrip6RipAdvFilterAddress": fsrip6RipAdvFilterAddress,
       "fsrip6RipAdvFilterStatus": fsrip6RipAdvFilterStatus,
       "fsrip6DistInOutRouteMap": fsrip6DistInOutRouteMap,
       "fsRip6DistInOutRouteMapTable": fsRip6DistInOutRouteMapTable,
       "fsRip6DistInOutRouteMapEntry": fsRip6DistInOutRouteMapEntry,
       "fsRip6DistInOutRouteMapName": fsRip6DistInOutRouteMapName,
       "fsRip6DistInOutRouteMapType": fsRip6DistInOutRouteMapType,
       "fsRip6DistInOutRouteMapValue": fsRip6DistInOutRouteMapValue,
       "fsRip6DistInOutRouteMapRowStatus": fsRip6DistInOutRouteMapRowStatus,
       "fsrip6PreferenceGroup": fsrip6PreferenceGroup,
       "fsRip6PreferenceValue": fsRip6PreferenceValue,
       "fsRip6Test": fsRip6Test,
       "fsRip6TestBulkUpd": fsRip6TestBulkUpd,
       "fsRip6TestDynamicUpd": fsRip6TestDynamicUpd}
)
