# SNMP MIB module (FS-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:16 2025
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

(ConfigStatus,) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 PositiveInteger,
 RouterID,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "PositiveInteger",
    "RouterID",
    "Status")

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

fsOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30)
)
if mibBuilder.loadTexts:
    fsOspfMIB.setRevisions(
        ("2002-11-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsOspfMIBObjects_ObjectIdentity = ObjectIdentity
fsOspfMIBObjects = _FsOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1)
)
_FsOspfGeneralMibsGroup_ObjectIdentity = ObjectIdentity
fsOspfGeneralMibsGroup = _FsOspfGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1)
)
_FsOspfMiniLsaInterval_Type = Unsigned32
_FsOspfMiniLsaInterval_Object = MibScalar
fsOspfMiniLsaInterval = _FsOspfMiniLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 1),
    _FsOspfMiniLsaInterval_Type()
)
fsOspfMiniLsaInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfMiniLsaInterval.setStatus("current")
_FsOspfMiniLsaArrival_Type = Unsigned32
_FsOspfMiniLsaArrival_Object = MibScalar
fsOspfMiniLsaArrival = _FsOspfMiniLsaArrival_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 2),
    _FsOspfMiniLsaArrival_Type()
)
fsOspfMiniLsaArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfMiniLsaArrival.setStatus("current")
_FsOspfAreasNum_Type = Unsigned32
_FsOspfAreasNum_Object = MibScalar
fsOspfAreasNum = _FsOspfAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 3),
    _FsOspfAreasNum_Type()
)
fsOspfAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreasNum.setStatus("current")
_FsOspfNormalAreasNum_Type = Unsigned32
_FsOspfNormalAreasNum_Object = MibScalar
fsOspfNormalAreasNum = _FsOspfNormalAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 4),
    _FsOspfNormalAreasNum_Type()
)
fsOspfNormalAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNormalAreasNum.setStatus("current")
_FsOspfStubAreasNum_Type = Unsigned32
_FsOspfStubAreasNum_Object = MibScalar
fsOspfStubAreasNum = _FsOspfStubAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 5),
    _FsOspfStubAreasNum_Type()
)
fsOspfStubAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfStubAreasNum.setStatus("current")
_FsOspfNssaAreasNum_Type = Unsigned32
_FsOspfNssaAreasNum_Object = MibScalar
fsOspfNssaAreasNum = _FsOspfNssaAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 6),
    _FsOspfNssaAreasNum_Type()
)
fsOspfNssaAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNssaAreasNum.setStatus("current")


class _FsOspfSpfDelay_Type(Unsigned32):
    """Custom type fsOspfSpfDelay based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsOspfSpfDelay_Type.__name__ = "Unsigned32"
_FsOspfSpfDelay_Object = MibScalar
fsOspfSpfDelay = _FsOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 7),
    _FsOspfSpfDelay_Type()
)
fsOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfSpfDelay.setStatus("current")


class _FsOspfSpfHoldTime_Type(Unsigned32):
    """Custom type fsOspfSpfHoldTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsOspfSpfHoldTime_Type.__name__ = "Unsigned32"
_FsOspfSpfHoldTime_Object = MibScalar
fsOspfSpfHoldTime = _FsOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 8),
    _FsOspfSpfHoldTime_Type()
)
fsOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfSpfHoldTime.setStatus("current")


class _FsOspfAutoCostRefBandWidthRef_Type(Unsigned32):
    """Custom type fsOspfAutoCostRefBandWidthRef based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsOspfAutoCostRefBandWidthRef_Type.__name__ = "Unsigned32"
_FsOspfAutoCostRefBandWidthRef_Object = MibScalar
fsOspfAutoCostRefBandWidthRef = _FsOspfAutoCostRefBandWidthRef_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 9),
    _FsOspfAutoCostRefBandWidthRef_Type()
)
fsOspfAutoCostRefBandWidthRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfAutoCostRefBandWidthRef.setStatus("current")


class _FsOspfLsaGroupPacing_Type(Unsigned32):
    """Custom type fsOspfLsaGroupPacing based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_FsOspfLsaGroupPacing_Type.__name__ = "Unsigned32"
_FsOspfLsaGroupPacing_Object = MibScalar
fsOspfLsaGroupPacing = _FsOspfLsaGroupPacing_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 10),
    _FsOspfLsaGroupPacing_Type()
)
fsOspfLsaGroupPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfLsaGroupPacing.setStatus("current")


class _FsOspfInterDistance_Type(Unsigned32):
    """Custom type fsOspfInterDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfInterDistance_Type.__name__ = "Unsigned32"
_FsOspfInterDistance_Object = MibScalar
fsOspfInterDistance = _FsOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 11),
    _FsOspfInterDistance_Type()
)
fsOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfInterDistance.setStatus("current")


class _FsOspfIntraDistance_Type(Unsigned32):
    """Custom type fsOspfIntraDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfIntraDistance_Type.__name__ = "Unsigned32"
_FsOspfIntraDistance_Object = MibScalar
fsOspfIntraDistance = _FsOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 12),
    _FsOspfIntraDistance_Type()
)
fsOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIntraDistance.setStatus("current")


class _FsOspfExternDistance_Type(Unsigned32):
    """Custom type fsOspfExternDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfExternDistance_Type.__name__ = "Unsigned32"
_FsOspfExternDistance_Object = MibScalar
fsOspfExternDistance = _FsOspfExternDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 13),
    _FsOspfExternDistance_Type()
)
fsOspfExternDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfExternDistance.setStatus("current")


class _FsOspfLogAdjChangeNotify_Type(EnabledStatus):
    """Custom type fsOspfLogAdjChangeNotify based on EnabledStatus"""
    defaultValue = 1


_FsOspfLogAdjChangeNotify_Type.__name__ = "EnabledStatus"
_FsOspfLogAdjChangeNotify_Object = MibScalar
fsOspfLogAdjChangeNotify = _FsOspfLogAdjChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 14),
    _FsOspfLogAdjChangeNotify_Type()
)
fsOspfLogAdjChangeNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfLogAdjChangeNotify.setStatus("current")


class _FsOspfPassiveStatus_Type(EnabledStatus):
    """Custom type fsOspfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_FsOspfPassiveStatus_Type.__name__ = "EnabledStatus"
_FsOspfPassiveStatus_Object = MibScalar
fsOspfPassiveStatus = _FsOspfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 15),
    _FsOspfPassiveStatus_Type()
)
fsOspfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfPassiveStatus.setStatus("current")


class _FsOspfRFC1583Compatibility_Type(EnabledStatus):
    """Custom type fsOspfRFC1583Compatibility based on EnabledStatus"""
    defaultValue = 1


_FsOspfRFC1583Compatibility_Type.__name__ = "EnabledStatus"
_FsOspfRFC1583Compatibility_Object = MibScalar
fsOspfRFC1583Compatibility = _FsOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 16),
    _FsOspfRFC1583Compatibility_Type()
)
fsOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfRFC1583Compatibility.setStatus("current")


class _FsOspfRouteRedisDefMetricVal_Type(Unsigned32):
    """Custom type fsOspfRouteRedisDefMetricVal based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FsOspfRouteRedisDefMetricVal_Type.__name__ = "Unsigned32"
_FsOspfRouteRedisDefMetricVal_Object = MibScalar
fsOspfRouteRedisDefMetricVal = _FsOspfRouteRedisDefMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 17),
    _FsOspfRouteRedisDefMetricVal_Type()
)
fsOspfRouteRedisDefMetricVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfRouteRedisDefMetricVal.setStatus("current")


class _FsOspfAdminiDistance_Type(Unsigned32):
    """Custom type fsOspfAdminiDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfAdminiDistance_Type.__name__ = "Unsigned32"
_FsOspfAdminiDistance_Object = MibScalar
fsOspfAdminiDistance = _FsOspfAdminiDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 1, 18),
    _FsOspfAdminiDistance_Type()
)
fsOspfAdminiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfAdminiDistance.setStatus("current")
_FsOspfAreaTable_Object = MibTable
fsOspfAreaTable = _FsOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    fsOspfAreaTable.setStatus("current")
_FsOspfAreaEntry_Object = MibTableRow
fsOspfAreaEntry = _FsOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1)
)
fsOspfAreaEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfAreaId"),
)
if mibBuilder.loadTexts:
    fsOspfAreaEntry.setStatus("current")
_FsOspfAreaId_Type = AreaID
_FsOspfAreaId_Object = MibTableColumn
fsOspfAreaId = _FsOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 1),
    _FsOspfAreaId_Type()
)
fsOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaId.setStatus("current")


class _FsOspfAuthType_Type(Integer32):
    """Custom type fsOspfAuthType based on Integer32"""
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
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )


_FsOspfAuthType_Type.__name__ = "Integer32"
_FsOspfAuthType_Object = MibTableColumn
fsOspfAuthType = _FsOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 2),
    _FsOspfAuthType_Type()
)
fsOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfAuthType.setStatus("current")


class _FsOspfImportAsExtern_Type(Integer32):
    """Custom type fsOspfImportAsExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_FsOspfImportAsExtern_Type.__name__ = "Integer32"
_FsOspfImportAsExtern_Object = MibTableColumn
fsOspfImportAsExtern = _FsOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 3),
    _FsOspfImportAsExtern_Type()
)
fsOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfImportAsExtern.setStatus("current")
_FsOspfSpfRuns_Type = Counter32
_FsOspfSpfRuns_Object = MibTableColumn
fsOspfSpfRuns = _FsOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 4),
    _FsOspfSpfRuns_Type()
)
fsOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfSpfRuns.setStatus("current")
_FsOspfAreaBdrRtrCount_Type = Gauge32
_FsOspfAreaBdrRtrCount_Object = MibTableColumn
fsOspfAreaBdrRtrCount = _FsOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 5),
    _FsOspfAreaBdrRtrCount_Type()
)
fsOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaBdrRtrCount.setStatus("current")
_FsOspfAsBdrRtrCount_Type = Gauge32
_FsOspfAsBdrRtrCount_Object = MibTableColumn
fsOspfAsBdrRtrCount = _FsOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 6),
    _FsOspfAsBdrRtrCount_Type()
)
fsOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAsBdrRtrCount.setStatus("current")
_FsOspfAreaLsaCount_Type = Gauge32
_FsOspfAreaLsaCount_Object = MibTableColumn
fsOspfAreaLsaCount = _FsOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 7),
    _FsOspfAreaLsaCount_Type()
)
fsOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaCount.setStatus("current")


class _FsOspfAreaLsaCksumSum_Type(Unsigned32):
    """Custom type fsOspfAreaLsaCksumSum based on Unsigned32"""
    defaultValue = 0


_FsOspfAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_FsOspfAreaLsaCksumSum_Object = MibTableColumn
fsOspfAreaLsaCksumSum = _FsOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 8),
    _FsOspfAreaLsaCksumSum_Type()
)
fsOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaCksumSum.setStatus("current")


class _FsOspfAreaSummary_Type(Integer32):
    """Custom type fsOspfAreaSummary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_FsOspfAreaSummary_Type.__name__ = "Integer32"
_FsOspfAreaSummary_Object = MibTableColumn
fsOspfAreaSummary = _FsOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 9),
    _FsOspfAreaSummary_Type()
)
fsOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfAreaSummary.setStatus("current")
_FsOspfAreaStatus_Type = RowStatus
_FsOspfAreaStatus_Object = MibTableColumn
fsOspfAreaStatus = _FsOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 10),
    _FsOspfAreaStatus_Type()
)
fsOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfAreaStatus.setStatus("current")
_FsOspfAreaInterfaceNum_Type = Unsigned32
_FsOspfAreaInterfaceNum_Object = MibTableColumn
fsOspfAreaInterfaceNum = _FsOspfAreaInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 11),
    _FsOspfAreaInterfaceNum_Type()
)
fsOspfAreaInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaInterfaceNum.setStatus("current")


class _FsOspfAreaNssaIsRedistribution_Type(TruthValue):
    """Custom type fsOspfAreaNssaIsRedistribution based on TruthValue"""
    defaultValue = 1


_FsOspfAreaNssaIsRedistribution_Type.__name__ = "TruthValue"
_FsOspfAreaNssaIsRedistribution_Object = MibTableColumn
fsOspfAreaNssaIsRedistribution = _FsOspfAreaNssaIsRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 12),
    _FsOspfAreaNssaIsRedistribution_Type()
)
fsOspfAreaNssaIsRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfAreaNssaIsRedistribution.setStatus("current")


class _FsOspfAreaNssaIsDefInfoOriginate_Type(TruthValue):
    """Custom type fsOspfAreaNssaIsDefInfoOriginate based on TruthValue"""
    defaultValue = 2


_FsOspfAreaNssaIsDefInfoOriginate_Type.__name__ = "TruthValue"
_FsOspfAreaNssaIsDefInfoOriginate_Object = MibTableColumn
fsOspfAreaNssaIsDefInfoOriginate = _FsOspfAreaNssaIsDefInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 2, 1, 13),
    _FsOspfAreaNssaIsDefInfoOriginate_Type()
)
fsOspfAreaNssaIsDefInfoOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfAreaNssaIsDefInfoOriginate.setStatus("current")
_FsOspfAddressScopeTable_Object = MibTable
fsOspfAddressScopeTable = _FsOspfAddressScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    fsOspfAddressScopeTable.setStatus("current")
_FsOspfAddressScopeEntry_Object = MibTableRow
fsOspfAddressScopeEntry = _FsOspfAddressScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3, 1)
)
fsOspfAddressScopeEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfNetWorkAreaID"),
    (0, "FS-OSPF-MIB", "fsOspfNetWorkAddress"),
    (0, "FS-OSPF-MIB", "fsOspfNetWorkMask"),
)
if mibBuilder.loadTexts:
    fsOspfAddressScopeEntry.setStatus("current")
_FsOspfNetWorkAreaID_Type = IpAddress
_FsOspfNetWorkAreaID_Object = MibTableColumn
fsOspfNetWorkAreaID = _FsOspfNetWorkAreaID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3, 1, 1),
    _FsOspfNetWorkAreaID_Type()
)
fsOspfNetWorkAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNetWorkAreaID.setStatus("current")
_FsOspfNetWorkAddress_Type = IpAddress
_FsOspfNetWorkAddress_Object = MibTableColumn
fsOspfNetWorkAddress = _FsOspfNetWorkAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3, 1, 2),
    _FsOspfNetWorkAddress_Type()
)
fsOspfNetWorkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNetWorkAddress.setStatus("current")
_FsOspfNetWorkMask_Type = IpAddress
_FsOspfNetWorkMask_Object = MibTableColumn
fsOspfNetWorkMask = _FsOspfNetWorkMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3, 1, 3),
    _FsOspfNetWorkMask_Type()
)
fsOspfNetWorkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNetWorkMask.setStatus("current")
_FsOspfNetWorkStatus_Type = RowStatus
_FsOspfNetWorkStatus_Object = MibTableColumn
fsOspfNetWorkStatus = _FsOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 3, 1, 4),
    _FsOspfNetWorkStatus_Type()
)
fsOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfNetWorkStatus.setStatus("current")
_FsOspfIfTable_Object = MibTable
fsOspfIfTable = _FsOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    fsOspfIfTable.setStatus("current")
_FsOspfIfEntry_Object = MibTableRow
fsOspfIfEntry = _FsOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1)
)
fsOspfIfEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfIfIpAddress"),
    (0, "FS-OSPF-MIB", "fsOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    fsOspfIfEntry.setStatus("current")
_FsOspfIfIpAddress_Type = IpAddress
_FsOspfIfIpAddress_Object = MibTableColumn
fsOspfIfIpAddress = _FsOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 1),
    _FsOspfIfIpAddress_Type()
)
fsOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfIpAddress.setStatus("current")
_FsOspfAddressLessIf_Type = Unsigned32
_FsOspfAddressLessIf_Object = MibTableColumn
fsOspfAddressLessIf = _FsOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 2),
    _FsOspfAddressLessIf_Type()
)
fsOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAddressLessIf.setStatus("current")


class _FsOspfIfAreaId_Type(AreaID):
    """Custom type fsOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_FsOspfIfAreaId_Type.__name__ = "AreaID"
_FsOspfIfAreaId_Object = MibTableColumn
fsOspfIfAreaId = _FsOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 3),
    _FsOspfIfAreaId_Type()
)
fsOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfAreaId.setStatus("current")


class _FsOspfIfType_Type(Integer32):
    """Custom type fsOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5),
          ("loopback", 6))
    )


_FsOspfIfType_Type.__name__ = "Integer32"
_FsOspfIfType_Object = MibTableColumn
fsOspfIfType = _FsOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 4),
    _FsOspfIfType_Type()
)
fsOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfType.setStatus("current")
_FsOspfIfAdminStat_Type = Status
_FsOspfIfAdminStat_Object = MibTableColumn
fsOspfIfAdminStat = _FsOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 5),
    _FsOspfIfAdminStat_Type()
)
fsOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfAdminStat.setStatus("current")


class _FsOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type fsOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_FsOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_FsOspfIfRtrPriority_Object = MibTableColumn
fsOspfIfRtrPriority = _FsOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 6),
    _FsOspfIfRtrPriority_Type()
)
fsOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfRtrPriority.setStatus("current")


class _FsOspfIfTransitDelay_Type(Unsigned32):
    """Custom type fsOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_FsOspfIfTransitDelay_Object = MibTableColumn
fsOspfIfTransitDelay = _FsOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 7),
    _FsOspfIfTransitDelay_Type()
)
fsOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfTransitDelay.setStatus("current")


class _FsOspfIfRetransInterval_Type(Unsigned32):
    """Custom type fsOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_FsOspfIfRetransInterval_Object = MibTableColumn
fsOspfIfRetransInterval = _FsOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 8),
    _FsOspfIfRetransInterval_Type()
)
fsOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfRetransInterval.setStatus("current")


class _FsOspfIfHelloInterval_Type(HelloRange):
    """Custom type fsOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_FsOspfIfHelloInterval_Type.__name__ = "HelloRange"
_FsOspfIfHelloInterval_Object = MibTableColumn
fsOspfIfHelloInterval = _FsOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 9),
    _FsOspfIfHelloInterval_Type()
)
fsOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfHelloInterval.setStatus("current")


class _FsOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type fsOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_FsOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_FsOspfIfRtrDeadInterval_Object = MibTableColumn
fsOspfIfRtrDeadInterval = _FsOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 10),
    _FsOspfIfRtrDeadInterval_Type()
)
fsOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfRtrDeadInterval.setStatus("current")
_FsOspfIfPollInterval_Type = PositiveInteger
_FsOspfIfPollInterval_Object = MibTableColumn
fsOspfIfPollInterval = _FsOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 11),
    _FsOspfIfPollInterval_Type()
)
fsOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfPollInterval.setStatus("current")


class _FsOspfIfState_Type(Integer32):
    """Custom type fsOspfIfState based on Integer32"""
    defaultValue = 1

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
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_FsOspfIfState_Type.__name__ = "Integer32"
_FsOspfIfState_Object = MibTableColumn
fsOspfIfState = _FsOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 12),
    _FsOspfIfState_Type()
)
fsOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfState.setStatus("current")


class _FsOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type fsOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_FsOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_FsOspfIfDesignatedRouter_Object = MibTableColumn
fsOspfIfDesignatedRouter = _FsOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 13),
    _FsOspfIfDesignatedRouter_Type()
)
fsOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfDesignatedRouter.setStatus("current")


class _FsOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type fsOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_FsOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_FsOspfIfBackupDesignatedRouter_Object = MibTableColumn
fsOspfIfBackupDesignatedRouter = _FsOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 14),
    _FsOspfIfBackupDesignatedRouter_Type()
)
fsOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfBackupDesignatedRouter.setStatus("current")
_FsOspfIfEvents_Type = Counter32
_FsOspfIfEvents_Object = MibTableColumn
fsOspfIfEvents = _FsOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 15),
    _FsOspfIfEvents_Type()
)
fsOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfEvents.setStatus("current")


class _FsOspfIfAuthKey_Type(OctetString):
    """Custom type fsOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsOspfIfAuthKey_Type.__name__ = "OctetString"
_FsOspfIfAuthKey_Object = MibTableColumn
fsOspfIfAuthKey = _FsOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 16),
    _FsOspfIfAuthKey_Type()
)
fsOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfAuthKey.setStatus("current")
_FsOspfIfStatus_Type = RowStatus
_FsOspfIfStatus_Object = MibTableColumn
fsOspfIfStatus = _FsOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 17),
    _FsOspfIfStatus_Type()
)
fsOspfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfStatus.setStatus("current")


class _FsOspfIfMulticastForwarding_Type(Integer32):
    """Custom type fsOspfIfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_FsOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_FsOspfIfMulticastForwarding_Object = MibTableColumn
fsOspfIfMulticastForwarding = _FsOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 18),
    _FsOspfIfMulticastForwarding_Type()
)
fsOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfMulticastForwarding.setStatus("current")


class _FsOspfIfDemand_Type(TruthValue):
    """Custom type fsOspfIfDemand based on TruthValue"""
    defaultValue = 2


_FsOspfIfDemand_Type.__name__ = "TruthValue"
_FsOspfIfDemand_Object = MibTableColumn
fsOspfIfDemand = _FsOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 19),
    _FsOspfIfDemand_Type()
)
fsOspfIfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfDemand.setStatus("current")


class _FsOspfIfAuthType_Type(Integer32):
    """Custom type fsOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsOspfIfAuthType_Type.__name__ = "Integer32"
_FsOspfIfAuthType_Object = MibTableColumn
fsOspfIfAuthType = _FsOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 20),
    _FsOspfIfAuthType_Type()
)
fsOspfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfAuthType.setStatus("current")


class _FsOspfIfDatabaseFilterAllOut_Type(EnabledStatus):
    """Custom type fsOspfIfDatabaseFilterAllOut based on EnabledStatus"""
    defaultValue = 2


_FsOspfIfDatabaseFilterAllOut_Type.__name__ = "EnabledStatus"
_FsOspfIfDatabaseFilterAllOut_Object = MibTableColumn
fsOspfIfDatabaseFilterAllOut = _FsOspfIfDatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 21),
    _FsOspfIfDatabaseFilterAllOut_Type()
)
fsOspfIfDatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfDatabaseFilterAllOut.setStatus("current")


class _FsOspfIfDesignateRouterId_Type(IpAddress):
    """Custom type fsOspfIfDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_FsOspfIfDesignateRouterId_Type.__name__ = "IpAddress"
_FsOspfIfDesignateRouterId_Object = MibTableColumn
fsOspfIfDesignateRouterId = _FsOspfIfDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 22),
    _FsOspfIfDesignateRouterId_Type()
)
fsOspfIfDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfDesignateRouterId.setStatus("current")


class _FsOspfIfBackupDesignateRouterId_Type(IpAddress):
    """Custom type fsOspfIfBackupDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_FsOspfIfBackupDesignateRouterId_Type.__name__ = "IpAddress"
_FsOspfIfBackupDesignateRouterId_Object = MibTableColumn
fsOspfIfBackupDesignateRouterId = _FsOspfIfBackupDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 23),
    _FsOspfIfBackupDesignateRouterId_Type()
)
fsOspfIfBackupDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfBackupDesignateRouterId.setStatus("current")
_FsOspfIfWaitInternal_Type = TimeTicks
_FsOspfIfWaitInternal_Object = MibTableColumn
fsOspfIfWaitInternal = _FsOspfIfWaitInternal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 24),
    _FsOspfIfWaitInternal_Type()
)
fsOspfIfWaitInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfWaitInternal.setStatus("current")


class _FsOspfIfPassiveStatus_Type(EnabledStatus):
    """Custom type fsOspfIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_FsOspfIfPassiveStatus_Type.__name__ = "EnabledStatus"
_FsOspfIfPassiveStatus_Object = MibTableColumn
fsOspfIfPassiveStatus = _FsOspfIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 25),
    _FsOspfIfPassiveStatus_Type()
)
fsOspfIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfPassiveStatus.setStatus("current")


class _FsOspfIfCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type fsOspfIfCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsOspfIfCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_FsOspfIfCurrentUsedMd5AuthKeyId_Object = MibTableColumn
fsOspfIfCurrentUsedMd5AuthKeyId = _FsOspfIfCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 4, 1, 26),
    _FsOspfIfCurrentUsedMd5AuthKeyId_Type()
)
fsOspfIfCurrentUsedMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfIfCurrentUsedMd5AuthKeyId.setStatus("current")
_FsOspfIfMd5AuthKeyTable_Object = MibTable
fsOspfIfMd5AuthKeyTable = _FsOspfIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5)
)
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKeyTable.setStatus("current")
_FsOspfIfMd5AuthKeyEntry_Object = MibTableRow
fsOspfIfMd5AuthKeyEntry = _FsOspfIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5, 1)
)
fsOspfIfMd5AuthKeyEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfIfMd5AuthKeyIf"),
    (0, "FS-OSPF-MIB", "fsOspfIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKeyEntry.setStatus("current")
_FsOspfIfMd5AuthKeyIf_Type = Unsigned32
_FsOspfIfMd5AuthKeyIf_Object = MibTableColumn
fsOspfIfMd5AuthKeyIf = _FsOspfIfMd5AuthKeyIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5, 1, 1),
    _FsOspfIfMd5AuthKeyIf_Type()
)
fsOspfIfMd5AuthKeyIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKeyIf.setStatus("current")


class _FsOspfIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type fsOspfIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_FsOspfIfMd5AuthKeyId_Object = MibTableColumn
fsOspfIfMd5AuthKeyId = _FsOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5, 1, 2),
    _FsOspfIfMd5AuthKeyId_Type()
)
fsOspfIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKeyId.setStatus("current")


class _FsOspfIfMd5AuthKey_Type(OctetString):
    """Custom type fsOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_FsOspfIfMd5AuthKey_Object = MibTableColumn
fsOspfIfMd5AuthKey = _FsOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5, 1, 3),
    _FsOspfIfMd5AuthKey_Type()
)
fsOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKey.setStatus("current")
_FsOspfIfMd5AuthKeySt_Type = ConfigStatus
_FsOspfIfMd5AuthKeySt_Object = MibTableColumn
fsOspfIfMd5AuthKeySt = _FsOspfIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 5, 1, 4),
    _FsOspfIfMd5AuthKeySt_Type()
)
fsOspfIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfIfMd5AuthKeySt.setStatus("current")
_FsOspfVirtTable_Object = MibTable
fsOspfVirtTable = _FsOspfVirtTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6)
)
if mibBuilder.loadTexts:
    fsOspfVirtTable.setStatus("current")
_FsOspfVirtEntry_Object = MibTableRow
fsOspfVirtEntry = _FsOspfVirtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1)
)
fsOspfVirtEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfVirtIfAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    fsOspfVirtEntry.setStatus("current")
_FsOspfVirtIfAreaId_Type = AreaID
_FsOspfVirtIfAreaId_Object = MibTableColumn
fsOspfVirtIfAreaId = _FsOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 1),
    _FsOspfVirtIfAreaId_Type()
)
fsOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfAreaId.setStatus("current")
_FsOspfVirtIfNeighbor_Type = RouterID
_FsOspfVirtIfNeighbor_Object = MibTableColumn
fsOspfVirtIfNeighbor = _FsOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 2),
    _FsOspfVirtIfNeighbor_Type()
)
fsOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfNeighbor.setStatus("current")


class _FsOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type fsOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_FsOspfVirtIfTransitDelay_Object = MibTableColumn
fsOspfVirtIfTransitDelay = _FsOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 3),
    _FsOspfVirtIfTransitDelay_Type()
)
fsOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfTransitDelay.setStatus("current")


class _FsOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type fsOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_FsOspfVirtIfRetransInterval_Object = MibTableColumn
fsOspfVirtIfRetransInterval = _FsOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 4),
    _FsOspfVirtIfRetransInterval_Type()
)
fsOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfRetransInterval.setStatus("current")


class _FsOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type fsOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_FsOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_FsOspfVirtIfHelloInterval_Object = MibTableColumn
fsOspfVirtIfHelloInterval = _FsOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 5),
    _FsOspfVirtIfHelloInterval_Type()
)
fsOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfHelloInterval.setStatus("current")


class _FsOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type fsOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_FsOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_FsOspfVirtIfRtrDeadInterval_Object = MibTableColumn
fsOspfVirtIfRtrDeadInterval = _FsOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 6),
    _FsOspfVirtIfRtrDeadInterval_Type()
)
fsOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfRtrDeadInterval.setStatus("current")


class _FsOspfVirtIfState_Type(Integer32):
    """Custom type fsOspfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_FsOspfVirtIfState_Type.__name__ = "Integer32"
_FsOspfVirtIfState_Object = MibTableColumn
fsOspfVirtIfState = _FsOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 7),
    _FsOspfVirtIfState_Type()
)
fsOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfState.setStatus("current")
_FsOspfVirtIfEvents_Type = Counter32
_FsOspfVirtIfEvents_Object = MibTableColumn
fsOspfVirtIfEvents = _FsOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 8),
    _FsOspfVirtIfEvents_Type()
)
fsOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfEvents.setStatus("current")


class _FsOspfVirtIfAuthKey_Type(OctetString):
    """Custom type fsOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_FsOspfVirtIfAuthKey_Object = MibTableColumn
fsOspfVirtIfAuthKey = _FsOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 9),
    _FsOspfVirtIfAuthKey_Type()
)
fsOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfAuthKey.setStatus("current")
_FsOspfVirtIfStatus_Type = RowStatus
_FsOspfVirtIfStatus_Object = MibTableColumn
fsOspfVirtIfStatus = _FsOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 10),
    _FsOspfVirtIfStatus_Type()
)
fsOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfStatus.setStatus("current")


class _FsOspfVirtIfAuthType_Type(Integer32):
    """Custom type fsOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsOspfVirtIfAuthType_Type.__name__ = "Integer32"
_FsOspfVirtIfAuthType_Object = MibTableColumn
fsOspfVirtIfAuthType = _FsOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 11),
    _FsOspfVirtIfAuthType_Type()
)
fsOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfAuthType.setStatus("current")
_FsOspfVirtCost_Type = Unsigned32
_FsOspfVirtCost_Object = MibTableColumn
fsOspfVirtCost = _FsOspfVirtCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 12),
    _FsOspfVirtCost_Type()
)
fsOspfVirtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtCost.setStatus("current")
_FsOspfVirtNativeIfIndex_Type = Integer32
_FsOspfVirtNativeIfIndex_Object = MibTableColumn
fsOspfVirtNativeIfIndex = _FsOspfVirtNativeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 13),
    _FsOspfVirtNativeIfIndex_Type()
)
fsOspfVirtNativeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtNativeIfIndex.setStatus("current")


class _FsOspfVirtLinkState_Type(Integer32):
    """Custom type fsOspfVirtLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsOspfVirtLinkState_Type.__name__ = "Integer32"
_FsOspfVirtLinkState_Object = MibTableColumn
fsOspfVirtLinkState = _FsOspfVirtLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 14),
    _FsOspfVirtLinkState_Type()
)
fsOspfVirtLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtLinkState.setStatus("current")
_FsOspfVirtHelloDueIn_Type = TimeTicks
_FsOspfVirtHelloDueIn_Object = MibTableColumn
fsOspfVirtHelloDueIn = _FsOspfVirtHelloDueIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 15),
    _FsOspfVirtHelloDueIn_Type()
)
fsOspfVirtHelloDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtHelloDueIn.setStatus("current")


class _FsOspfVirtCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type fsOspfVirtCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsOspfVirtCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_FsOspfVirtCurrentUsedMd5AuthKeyId_Object = MibTableColumn
fsOspfVirtCurrentUsedMd5AuthKeyId = _FsOspfVirtCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 6, 1, 16),
    _FsOspfVirtCurrentUsedMd5AuthKeyId_Type()
)
fsOspfVirtCurrentUsedMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtCurrentUsedMd5AuthKeyId.setStatus("current")
_FsOspfVirtIfMd5AuthKeyTable_Object = MibTable
fsOspfVirtIfMd5AuthKeyTable = _FsOspfVirtIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7)
)
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeyTable.setStatus("current")
_FsOspfVirtIfMd5AuthKeyEntry_Object = MibTableRow
fsOspfVirtIfMd5AuthKeyEntry = _FsOspfVirtIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1)
)
fsOspfVirtIfMd5AuthKeyEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyNeighbor"),
    (0, "FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeyEntry.setStatus("current")
_FsOspfVirtIfMd5AuthKeyAreaId_Type = AreaID
_FsOspfVirtIfMd5AuthKeyAreaId_Object = MibTableColumn
fsOspfVirtIfMd5AuthKeyAreaId = _FsOspfVirtIfMd5AuthKeyAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1, 1),
    _FsOspfVirtIfMd5AuthKeyAreaId_Type()
)
fsOspfVirtIfMd5AuthKeyAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeyAreaId.setStatus("current")
_FsOspfVirtIfMd5AuthKeyNeighbor_Type = RouterID
_FsOspfVirtIfMd5AuthKeyNeighbor_Object = MibTableColumn
fsOspfVirtIfMd5AuthKeyNeighbor = _FsOspfVirtIfMd5AuthKeyNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1, 2),
    _FsOspfVirtIfMd5AuthKeyNeighbor_Type()
)
fsOspfVirtIfMd5AuthKeyNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeyNeighbor.setStatus("current")


class _FsOspfVirtIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type fsOspfVirtIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsOspfVirtIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_FsOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
fsOspfVirtIfMd5AuthKeyId = _FsOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1, 3),
    _FsOspfVirtIfMd5AuthKeyId_Type()
)
fsOspfVirtIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeyId.setStatus("current")


class _FsOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type fsOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_FsOspfVirtIfMd5AuthKey_Object = MibTableColumn
fsOspfVirtIfMd5AuthKey = _FsOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1, 4),
    _FsOspfVirtIfMd5AuthKey_Type()
)
fsOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKey.setStatus("current")
_FsOspfVirtIfMd5AuthKeySt_Type = ConfigStatus
_FsOspfVirtIfMd5AuthKeySt_Object = MibTableColumn
fsOspfVirtIfMd5AuthKeySt = _FsOspfVirtIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 7, 1, 5),
    _FsOspfVirtIfMd5AuthKeySt_Type()
)
fsOspfVirtIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfVirtIfMd5AuthKeySt.setStatus("current")
_FsOspfLsaDetailInfoMibsGroup_ObjectIdentity = ObjectIdentity
fsOspfLsaDetailInfoMibsGroup = _FsOspfLsaDetailInfoMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8)
)
_FsOspfLsdbTable_Object = MibTable
fsOspfLsdbTable = _FsOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1)
)
if mibBuilder.loadTexts:
    fsOspfLsdbTable.setStatus("current")
_FsOspfLsdbEntry_Object = MibTableRow
fsOspfLsdbEntry = _FsOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1)
)
fsOspfLsdbEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfLsdbAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbType"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbLsid"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsOspfLsdbEntry.setStatus("current")
_FsOspfLsdbAreaId_Type = AreaID
_FsOspfLsdbAreaId_Object = MibTableColumn
fsOspfLsdbAreaId = _FsOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 1),
    _FsOspfLsdbAreaId_Type()
)
fsOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbAreaId.setStatus("current")


class _FsOspfLsdbType_Type(Integer32):
    """Custom type fsOspfLsdbType based on Integer32"""
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
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7))
    )


_FsOspfLsdbType_Type.__name__ = "Integer32"
_FsOspfLsdbType_Object = MibTableColumn
fsOspfLsdbType = _FsOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 2),
    _FsOspfLsdbType_Type()
)
fsOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbType.setStatus("current")
_FsOspfLsdbLsid_Type = IpAddress
_FsOspfLsdbLsid_Object = MibTableColumn
fsOspfLsdbLsid = _FsOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 3),
    _FsOspfLsdbLsid_Type()
)
fsOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbLsid.setStatus("current")
_FsOspfLsdbRouterId_Type = RouterID
_FsOspfLsdbRouterId_Object = MibTableColumn
fsOspfLsdbRouterId = _FsOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 4),
    _FsOspfLsdbRouterId_Type()
)
fsOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbRouterId.setStatus("current")
_FsOspfLsdbSequence_Type = Unsigned32
_FsOspfLsdbSequence_Object = MibTableColumn
fsOspfLsdbSequence = _FsOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 5),
    _FsOspfLsdbSequence_Type()
)
fsOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbSequence.setStatus("current")
_FsOspfLsdbAge_Type = Unsigned32
_FsOspfLsdbAge_Object = MibTableColumn
fsOspfLsdbAge = _FsOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 6),
    _FsOspfLsdbAge_Type()
)
fsOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbAge.setStatus("current")
_FsOspfLsdbChecksum_Type = Unsigned32
_FsOspfLsdbChecksum_Object = MibTableColumn
fsOspfLsdbChecksum = _FsOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 7),
    _FsOspfLsdbChecksum_Type()
)
fsOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbChecksum.setStatus("current")


class _FsOspfLsdbAdvertisement_Type(OctetString):
    """Custom type fsOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_FsOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_FsOspfLsdbAdvertisement_Object = MibTableColumn
fsOspfLsdbAdvertisement = _FsOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 8),
    _FsOspfLsdbAdvertisement_Type()
)
fsOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbAdvertisement.setStatus("current")


class _FsOspfLsdbLinkNum_Type(Unsigned32):
    """Custom type fsOspfLsdbLinkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsOspfLsdbLinkNum_Type.__name__ = "Unsigned32"
_FsOspfLsdbLinkNum_Object = MibTableColumn
fsOspfLsdbLinkNum = _FsOspfLsdbLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 9),
    _FsOspfLsdbLinkNum_Type()
)
fsOspfLsdbLinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbLinkNum.setStatus("current")


class _FsOspfLsdbPacketLength_Type(Unsigned32):
    """Custom type fsOspfLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsOspfLsdbPacketLength_Type.__name__ = "Unsigned32"
_FsOspfLsdbPacketLength_Object = MibTableColumn
fsOspfLsdbPacketLength = _FsOspfLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 10),
    _FsOspfLsdbPacketLength_Type()
)
fsOspfLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbPacketLength.setStatus("current")
_FsOspfSummaryLsaNetworkMask_Type = IpAddress
_FsOspfSummaryLsaNetworkMask_Object = MibTableColumn
fsOspfSummaryLsaNetworkMask = _FsOspfSummaryLsaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 11),
    _FsOspfSummaryLsaNetworkMask_Type()
)
fsOspfSummaryLsaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfSummaryLsaNetworkMask.setStatus("current")


class _FsOspfSummaryLsaTos0Metric_Type(Unsigned32):
    """Custom type fsOspfSummaryLsaTos0Metric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsOspfSummaryLsaTos0Metric_Type.__name__ = "Unsigned32"
_FsOspfSummaryLsaTos0Metric_Object = MibTableColumn
fsOspfSummaryLsaTos0Metric = _FsOspfSummaryLsaTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 12),
    _FsOspfSummaryLsaTos0Metric_Type()
)
fsOspfSummaryLsaTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfSummaryLsaTos0Metric.setStatus("current")


class _FsOspfNssaLsaDetailMetricType_Type(Integer32):
    """Custom type fsOspfNssaLsaDetailMetricType based on Integer32"""
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


_FsOspfNssaLsaDetailMetricType_Type.__name__ = "Integer32"
_FsOspfNssaLsaDetailMetricType_Object = MibTableColumn
fsOspfNssaLsaDetailMetricType = _FsOspfNssaLsaDetailMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 13),
    _FsOspfNssaLsaDetailMetricType_Type()
)
fsOspfNssaLsaDetailMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNssaLsaDetailMetricType.setStatus("current")
_FsOspfNssaLsaDetailForwardAddr_Type = IpAddress
_FsOspfNssaLsaDetailForwardAddr_Object = MibTableColumn
fsOspfNssaLsaDetailForwardAddr = _FsOspfNssaLsaDetailForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 14),
    _FsOspfNssaLsaDetailForwardAddr_Type()
)
fsOspfNssaLsaDetailForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNssaLsaDetailForwardAddr.setStatus("current")
_FsOspfNssaLsaDetailRouteTag_Type = Unsigned32
_FsOspfNssaLsaDetailRouteTag_Object = MibTableColumn
fsOspfNssaLsaDetailRouteTag = _FsOspfNssaLsaDetailRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 15),
    _FsOspfNssaLsaDetailRouteTag_Type()
)
fsOspfNssaLsaDetailRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNssaLsaDetailRouteTag.setStatus("current")
_FsOspfLsdbOption_Type = Unsigned32
_FsOspfLsdbOption_Object = MibTableColumn
fsOspfLsdbOption = _FsOspfLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 1, 1, 16),
    _FsOspfLsdbOption_Type()
)
fsOspfLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsdbOption.setStatus("current")
_FsOspfExtLsdbTable_Object = MibTable
fsOspfExtLsdbTable = _FsOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2)
)
if mibBuilder.loadTexts:
    fsOspfExtLsdbTable.setStatus("current")
_FsOspfExtLsdbEntry_Object = MibTableRow
fsOspfExtLsdbEntry = _FsOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1)
)
fsOspfExtLsdbEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfExtLsdbType"),
    (0, "FS-OSPF-MIB", "fsOspfExtLsdbLsid"),
    (0, "FS-OSPF-MIB", "fsOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsOspfExtLsdbEntry.setStatus("current")


class _FsOspfExtLsdbType_Type(Integer32):
    """Custom type fsOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_FsOspfExtLsdbType_Type.__name__ = "Integer32"
_FsOspfExtLsdbType_Object = MibTableColumn
fsOspfExtLsdbType = _FsOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 1),
    _FsOspfExtLsdbType_Type()
)
fsOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbType.setStatus("current")
_FsOspfExtLsdbLsid_Type = IpAddress
_FsOspfExtLsdbLsid_Object = MibTableColumn
fsOspfExtLsdbLsid = _FsOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 2),
    _FsOspfExtLsdbLsid_Type()
)
fsOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbLsid.setStatus("current")
_FsOspfExtLsdbRouterId_Type = RouterID
_FsOspfExtLsdbRouterId_Object = MibTableColumn
fsOspfExtLsdbRouterId = _FsOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 3),
    _FsOspfExtLsdbRouterId_Type()
)
fsOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbRouterId.setStatus("current")
_FsOspfExtLsdbSequence_Type = Unsigned32
_FsOspfExtLsdbSequence_Object = MibTableColumn
fsOspfExtLsdbSequence = _FsOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 4),
    _FsOspfExtLsdbSequence_Type()
)
fsOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbSequence.setStatus("current")
_FsOspfExtLsdbAge_Type = Unsigned32
_FsOspfExtLsdbAge_Object = MibTableColumn
fsOspfExtLsdbAge = _FsOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 5),
    _FsOspfExtLsdbAge_Type()
)
fsOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbAge.setStatus("current")
_FsOspfExtLsdbChecksum_Type = Unsigned32
_FsOspfExtLsdbChecksum_Object = MibTableColumn
fsOspfExtLsdbChecksum = _FsOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 6),
    _FsOspfExtLsdbChecksum_Type()
)
fsOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbChecksum.setStatus("current")


class _FsOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type fsOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_FsOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_FsOspfExtLsdbAdvertisement_Object = MibTableColumn
fsOspfExtLsdbAdvertisement = _FsOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 7),
    _FsOspfExtLsdbAdvertisement_Type()
)
fsOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbAdvertisement.setStatus("current")
_FsOspfExtLsdbNetworkMask_Type = IpAddress
_FsOspfExtLsdbNetworkMask_Object = MibTableColumn
fsOspfExtLsdbNetworkMask = _FsOspfExtLsdbNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 8),
    _FsOspfExtLsdbNetworkMask_Type()
)
fsOspfExtLsdbNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbNetworkMask.setStatus("current")
_FsOspfExtLsdbMetric_Type = Integer32
_FsOspfExtLsdbMetric_Object = MibTableColumn
fsOspfExtLsdbMetric = _FsOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 9),
    _FsOspfExtLsdbMetric_Type()
)
fsOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbMetric.setStatus("current")


class _FsOspfExtLsdbMetricType_Type(Integer32):
    """Custom type fsOspfExtLsdbMetricType based on Integer32"""
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


_FsOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_FsOspfExtLsdbMetricType_Object = MibTableColumn
fsOspfExtLsdbMetricType = _FsOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 10),
    _FsOspfExtLsdbMetricType_Type()
)
fsOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbMetricType.setStatus("current")
_FsOspfExtLsdbForwardAddr_Type = IpAddress
_FsOspfExtLsdbForwardAddr_Object = MibTableColumn
fsOspfExtLsdbForwardAddr = _FsOspfExtLsdbForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 11),
    _FsOspfExtLsdbForwardAddr_Type()
)
fsOspfExtLsdbForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbForwardAddr.setStatus("current")
_FsOspfExtLsdbRouteTag_Type = Unsigned32
_FsOspfExtLsdbRouteTag_Object = MibTableColumn
fsOspfExtLsdbRouteTag = _FsOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 12),
    _FsOspfExtLsdbRouteTag_Type()
)
fsOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbRouteTag.setStatus("current")
_FsOspfExtLsdbOption_Type = Unsigned32
_FsOspfExtLsdbOption_Object = MibTableColumn
fsOspfExtLsdbOption = _FsOspfExtLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 13),
    _FsOspfExtLsdbOption_Type()
)
fsOspfExtLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbOption.setStatus("current")


class _FsOspfExtLsdbPacketLength_Type(Unsigned32):
    """Custom type fsOspfExtLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsOspfExtLsdbPacketLength_Type.__name__ = "Unsigned32"
_FsOspfExtLsdbPacketLength_Object = MibTableColumn
fsOspfExtLsdbPacketLength = _FsOspfExtLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 2, 1, 14),
    _FsOspfExtLsdbPacketLength_Type()
)
fsOspfExtLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfExtLsdbPacketLength.setStatus("current")
_FsOspfRouterLsaDetailTable_Object = MibTable
fsOspfRouterLsaDetailTable = _FsOspfRouterLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3)
)
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailTable.setStatus("current")
_FsOspfRouterLsaDetailEntry_Object = MibTableRow
fsOspfRouterLsaDetailEntry = _FsOspfRouterLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3, 1)
)
fsOspfRouterLsaDetailEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfLsdbAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbType"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbLsid"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbRouterId"),
    (0, "FS-OSPF-MIB", "fsOspfRouterLsaDetailLinkID"),
)
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailEntry.setStatus("current")
_FsOspfRouterLsaDetailLinkID_Type = IpAddress
_FsOspfRouterLsaDetailLinkID_Object = MibTableColumn
fsOspfRouterLsaDetailLinkID = _FsOspfRouterLsaDetailLinkID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3, 1, 1),
    _FsOspfRouterLsaDetailLinkID_Type()
)
fsOspfRouterLsaDetailLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailLinkID.setStatus("current")


class _FsOspfRouterLsaDetailLinkType_Type(Integer32):
    """Custom type fsOspfRouterLsaDetailLinkType based on Integer32"""
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
        *(("pointtopointConnectionToAnotherRouter", 1),
          ("connectionToaTransitNetwork", 2),
          ("connectionToaStubNetwork", 3),
          ("virtualLink", 4))
    )


_FsOspfRouterLsaDetailLinkType_Type.__name__ = "Integer32"
_FsOspfRouterLsaDetailLinkType_Object = MibTableColumn
fsOspfRouterLsaDetailLinkType = _FsOspfRouterLsaDetailLinkType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3, 1, 2),
    _FsOspfRouterLsaDetailLinkType_Type()
)
fsOspfRouterLsaDetailLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailLinkType.setStatus("current")
_FsOspfRouterLsaDetailLinkData_Type = IpAddress
_FsOspfRouterLsaDetailLinkData_Object = MibTableColumn
fsOspfRouterLsaDetailLinkData = _FsOspfRouterLsaDetailLinkData_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3, 1, 3),
    _FsOspfRouterLsaDetailLinkData_Type()
)
fsOspfRouterLsaDetailLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailLinkData.setStatus("current")
_FsOspfRouterLsaDetailTos0Metric_Type = Unsigned32
_FsOspfRouterLsaDetailTos0Metric_Object = MibTableColumn
fsOspfRouterLsaDetailTos0Metric = _FsOspfRouterLsaDetailTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 3, 1, 4),
    _FsOspfRouterLsaDetailTos0Metric_Type()
)
fsOspfRouterLsaDetailTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouterLsaDetailTos0Metric.setStatus("current")
_FsOspfNetWorkLsaDetailTable_Object = MibTable
fsOspfNetWorkLsaDetailTable = _FsOspfNetWorkLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 4)
)
if mibBuilder.loadTexts:
    fsOspfNetWorkLsaDetailTable.setStatus("current")
_FsOspfNetWorkLsaDetailEntry_Object = MibTableRow
fsOspfNetWorkLsaDetailEntry = _FsOspfNetWorkLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 4, 1)
)
fsOspfNetWorkLsaDetailEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfLsdbAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbType"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbLsid"),
    (0, "FS-OSPF-MIB", "fsOspfLsdbRouterId"),
    (0, "FS-OSPF-MIB", "fsOspfNetWorkLsaDetailAttachedRouter"),
)
if mibBuilder.loadTexts:
    fsOspfNetWorkLsaDetailEntry.setStatus("current")
_FsOspfNetWorkLsaDetailAttachedRouter_Type = IpAddress
_FsOspfNetWorkLsaDetailAttachedRouter_Object = MibTableColumn
fsOspfNetWorkLsaDetailAttachedRouter = _FsOspfNetWorkLsaDetailAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 4, 1, 1),
    _FsOspfNetWorkLsaDetailAttachedRouter_Type()
)
fsOspfNetWorkLsaDetailAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNetWorkLsaDetailAttachedRouter.setStatus("current")
_FsOspfNetWorkLsaDetailNetworkMask_Type = IpAddress
_FsOspfNetWorkLsaDetailNetworkMask_Object = MibTableColumn
fsOspfNetWorkLsaDetailNetworkMask = _FsOspfNetWorkLsaDetailNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 4, 1, 2),
    _FsOspfNetWorkLsaDetailNetworkMask_Type()
)
fsOspfNetWorkLsaDetailNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNetWorkLsaDetailNetworkMask.setStatus("current")
_FsOspfAreaLsaDBSumTable_Object = MibTable
fsOspfAreaLsaDBSumTable = _FsOspfAreaLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5)
)
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumTable.setStatus("current")
_FsOspfAreaLsaDBSumEntry_Object = MibTableRow
fsOspfAreaLsaDBSumEntry = _FsOspfAreaLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1)
)
fsOspfAreaLsaDBSumEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfAreaLsaDBSumAreaId"),
    (0, "FS-OSPF-MIB", "fsOspfAreaLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumEntry.setStatus("current")
_FsOspfAreaLsaDBSumAreaId_Type = IpAddress
_FsOspfAreaLsaDBSumAreaId_Object = MibTableColumn
fsOspfAreaLsaDBSumAreaId = _FsOspfAreaLsaDBSumAreaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1, 1),
    _FsOspfAreaLsaDBSumAreaId_Type()
)
fsOspfAreaLsaDBSumAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumAreaId.setStatus("current")


class _FsOspfAreaLsaDBSumLsaType_Type(Integer32):
    """Custom type fsOspfAreaLsaDBSumLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("nssaExternalLink", 7),
          ("subtotal", 8))
    )


_FsOspfAreaLsaDBSumLsaType_Type.__name__ = "Integer32"
_FsOspfAreaLsaDBSumLsaType_Object = MibTableColumn
fsOspfAreaLsaDBSumLsaType = _FsOspfAreaLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1, 2),
    _FsOspfAreaLsaDBSumLsaType_Type()
)
fsOspfAreaLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumLsaType.setStatus("current")
_FsOspfAreaLsaDBSumCounts_Type = Counter32
_FsOspfAreaLsaDBSumCounts_Object = MibTableColumn
fsOspfAreaLsaDBSumCounts = _FsOspfAreaLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1, 3),
    _FsOspfAreaLsaDBSumCounts_Type()
)
fsOspfAreaLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumCounts.setStatus("current")
_FsOspfAreaLsaDBSumDeletes_Type = Counter32
_FsOspfAreaLsaDBSumDeletes_Object = MibTableColumn
fsOspfAreaLsaDBSumDeletes = _FsOspfAreaLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1, 4),
    _FsOspfAreaLsaDBSumDeletes_Type()
)
fsOspfAreaLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumDeletes.setStatus("current")
_FsOspfAreaLsaDBSumMaxage_Type = Counter32
_FsOspfAreaLsaDBSumMaxage_Object = MibTableColumn
fsOspfAreaLsaDBSumMaxage = _FsOspfAreaLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 5, 1, 5),
    _FsOspfAreaLsaDBSumMaxage_Type()
)
fsOspfAreaLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfAreaLsaDBSumMaxage.setStatus("current")
_FsOspfLsaDBSumTable_Object = MibTable
fsOspfLsaDBSumTable = _FsOspfLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6)
)
if mibBuilder.loadTexts:
    fsOspfLsaDBSumTable.setStatus("current")
_FsOspfLsaDBSumEntry_Object = MibTableRow
fsOspfLsaDBSumEntry = _FsOspfLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6, 1)
)
fsOspfLsaDBSumEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    fsOspfLsaDBSumEntry.setStatus("current")


class _FsOspfLsaDBSumLsaType_Type(Integer32):
    """Custom type fsOspfLsaDBSumLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryTotalLink", 3),
          ("asSummaryTotalLink", 4),
          ("asExternalLink", 5),
          ("nssaExternalLink", 7),
          ("total", 8))
    )


_FsOspfLsaDBSumLsaType_Type.__name__ = "Integer32"
_FsOspfLsaDBSumLsaType_Object = MibTableColumn
fsOspfLsaDBSumLsaType = _FsOspfLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6, 1, 1),
    _FsOspfLsaDBSumLsaType_Type()
)
fsOspfLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsaDBSumLsaType.setStatus("current")
_FsOspfLsaDBSumCounts_Type = Counter32
_FsOspfLsaDBSumCounts_Object = MibTableColumn
fsOspfLsaDBSumCounts = _FsOspfLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6, 1, 2),
    _FsOspfLsaDBSumCounts_Type()
)
fsOspfLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsaDBSumCounts.setStatus("current")
_FsOspfLsaDBSumDeletes_Type = Counter32
_FsOspfLsaDBSumDeletes_Object = MibTableColumn
fsOspfLsaDBSumDeletes = _FsOspfLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6, 1, 3),
    _FsOspfLsaDBSumDeletes_Type()
)
fsOspfLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsaDBSumDeletes.setStatus("current")
_FsOspfLsaDBSumMaxage_Type = Counter32
_FsOspfLsaDBSumMaxage_Object = MibTableColumn
fsOspfLsaDBSumMaxage = _FsOspfLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 8, 6, 1, 4),
    _FsOspfLsaDBSumMaxage_Type()
)
fsOspfLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfLsaDBSumMaxage.setStatus("current")
_FsOspfNeighborTable_Object = MibTable
fsOspfNeighborTable = _FsOspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9)
)
if mibBuilder.loadTexts:
    fsOspfNeighborTable.setStatus("current")
_FsOspfNeighborEntry_Object = MibTableRow
fsOspfNeighborEntry = _FsOspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1)
)
fsOspfNeighborEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfNbrIpAddr"),
    (0, "FS-OSPF-MIB", "fsOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    fsOspfNeighborEntry.setStatus("current")
_FsOspfNbrIpAddr_Type = IpAddress
_FsOspfNbrIpAddr_Object = MibTableColumn
fsOspfNbrIpAddr = _FsOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 1),
    _FsOspfNbrIpAddr_Type()
)
fsOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrIpAddr.setStatus("current")
_FsOspfNbrAddressLessIndex_Type = Unsigned32
_FsOspfNbrAddressLessIndex_Object = MibTableColumn
fsOspfNbrAddressLessIndex = _FsOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 2),
    _FsOspfNbrAddressLessIndex_Type()
)
fsOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrAddressLessIndex.setStatus("current")
_FsOspfNbrRtrId_Type = RouterID
_FsOspfNbrRtrId_Object = MibTableColumn
fsOspfNbrRtrId = _FsOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 3),
    _FsOspfNbrRtrId_Type()
)
fsOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrRtrId.setStatus("current")
_FsOspfNbrOptions_Type = Unsigned32
_FsOspfNbrOptions_Object = MibTableColumn
fsOspfNbrOptions = _FsOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 4),
    _FsOspfNbrOptions_Type()
)
fsOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrOptions.setStatus("current")
_FsOspfNbrPriority_Type = DesignatedRouterPriority
_FsOspfNbrPriority_Object = MibTableColumn
fsOspfNbrPriority = _FsOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 5),
    _FsOspfNbrPriority_Type()
)
fsOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrPriority.setStatus("current")


class _FsOspfNbrState_Type(Integer32):
    """Custom type fsOspfNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeFS", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_FsOspfNbrState_Type.__name__ = "Integer32"
_FsOspfNbrState_Object = MibTableColumn
fsOspfNbrState = _FsOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 6),
    _FsOspfNbrState_Type()
)
fsOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrState.setStatus("current")
_FsOspfNbrEvents_Type = Counter32
_FsOspfNbrEvents_Object = MibTableColumn
fsOspfNbrEvents = _FsOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 7),
    _FsOspfNbrEvents_Type()
)
fsOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrEvents.setStatus("current")
_FsOspfNbrLsRetransQLen_Type = Gauge32
_FsOspfNbrLsRetransQLen_Object = MibTableColumn
fsOspfNbrLsRetransQLen = _FsOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 8),
    _FsOspfNbrLsRetransQLen_Type()
)
fsOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrLsRetransQLen.setStatus("current")
_FsOspfNbmaNbrStatus_Type = RowStatus
_FsOspfNbmaNbrStatus_Object = MibTableColumn
fsOspfNbmaNbrStatus = _FsOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 9),
    _FsOspfNbmaNbrStatus_Type()
)
fsOspfNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbmaNbrStatus.setStatus("current")


class _FsOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type fsOspfNbmaNbrPermanence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_FsOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_FsOspfNbmaNbrPermanence_Object = MibTableColumn
fsOspfNbmaNbrPermanence = _FsOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 10),
    _FsOspfNbmaNbrPermanence_Type()
)
fsOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbmaNbrPermanence.setStatus("current")
_FsOspfNbrHelloSuppressed_Type = TruthValue
_FsOspfNbrHelloSuppressed_Object = MibTableColumn
fsOspfNbrHelloSuppressed = _FsOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 11),
    _FsOspfNbrHelloSuppressed_Type()
)
fsOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrHelloSuppressed.setStatus("current")
_FsOspfNbrDeadTimeDueIn_Type = TimeTicks
_FsOspfNbrDeadTimeDueIn_Object = MibTableColumn
fsOspfNbrDeadTimeDueIn = _FsOspfNbrDeadTimeDueIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 12),
    _FsOspfNbrDeadTimeDueIn_Type()
)
fsOspfNbrDeadTimeDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrDeadTimeDueIn.setStatus("current")
_FsOspfNbrNeighborUpTime_Type = TimeTicks
_FsOspfNbrNeighborUpTime_Object = MibTableColumn
fsOspfNbrNeighborUpTime = _FsOspfNbrNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 13),
    _FsOspfNbrNeighborUpTime_Type()
)
fsOspfNbrNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrNeighborUpTime.setStatus("current")
_FsOspfNbrDR_Type = IpAddress
_FsOspfNbrDR_Object = MibTableColumn
fsOspfNbrDR = _FsOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 14),
    _FsOspfNbrDR_Type()
)
fsOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrDR.setStatus("current")
_FsOspfNbrBDR_Type = IpAddress
_FsOspfNbrBDR_Object = MibTableColumn
fsOspfNbrBDR = _FsOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 15),
    _FsOspfNbrBDR_Type()
)
fsOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrBDR.setStatus("current")
_FsOspfNbrArea_Type = IpAddress
_FsOspfNbrArea_Object = MibTableColumn
fsOspfNbrArea = _FsOspfNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 16),
    _FsOspfNbrArea_Type()
)
fsOspfNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrArea.setStatus("current")
_FsOspfNbrRetransmissionNum_Type = Counter32
_FsOspfNbrRetransmissionNum_Object = MibTableColumn
fsOspfNbrRetransmissionNum = _FsOspfNbrRetransmissionNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 17),
    _FsOspfNbrRetransmissionNum_Type()
)
fsOspfNbrRetransmissionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrRetransmissionNum.setStatus("current")


class _FsOspfNbrIfState_Type(Integer32):
    """Custom type fsOspfNbrIfState based on Integer32"""
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
        *(("other", 0),
          ("designatedRouter", 1),
          ("backupDesignatedRouter", 2),
          ("otherDesignatedRouter", 3))
    )


_FsOspfNbrIfState_Type.__name__ = "Integer32"
_FsOspfNbrIfState_Object = MibTableColumn
fsOspfNbrIfState = _FsOspfNbrIfState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 9, 1, 18),
    _FsOspfNbrIfState_Type()
)
fsOspfNbrIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfNbrIfState.setStatus("current")
_FsOspfRouteTable_Object = MibTable
fsOspfRouteTable = _FsOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10)
)
if mibBuilder.loadTexts:
    fsOspfRouteTable.setStatus("current")
_FsOspfRouteEntry_Object = MibTableRow
fsOspfRouteEntry = _FsOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1)
)
fsOspfRouteEntry.setIndexNames(
    (0, "FS-OSPF-MIB", "fsOspfRouteDest"),
    (0, "FS-OSPF-MIB", "fsOspfRouteArea"),
    (0, "FS-OSPF-MIB", "fsOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsOspfRouteEntry.setStatus("current")
_FsOspfRouteDest_Type = IpAddress
_FsOspfRouteDest_Object = MibTableColumn
fsOspfRouteDest = _FsOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 1),
    _FsOspfRouteDest_Type()
)
fsOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteDest.setStatus("current")
_FsOspfRouteArea_Type = IpAddress
_FsOspfRouteArea_Object = MibTableColumn
fsOspfRouteArea = _FsOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 2),
    _FsOspfRouteArea_Type()
)
fsOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteArea.setStatus("current")
_FsOspfRouteNextHop_Type = IpAddress
_FsOspfRouteNextHop_Object = MibTableColumn
fsOspfRouteNextHop = _FsOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 3),
    _FsOspfRouteNextHop_Type()
)
fsOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteNextHop.setStatus("current")
_FsOspfRouteCost_Type = Unsigned32
_FsOspfRouteCost_Object = MibTableColumn
fsOspfRouteCost = _FsOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 4),
    _FsOspfRouteCost_Type()
)
fsOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteCost.setStatus("current")


class _FsOspfRouteDRType_Type(Integer32):
    """Custom type fsOspfRouteDRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("asbr", 2),
          ("both", 3))
    )


_FsOspfRouteDRType_Type.__name__ = "Integer32"
_FsOspfRouteDRType_Object = MibTableColumn
fsOspfRouteDRType = _FsOspfRouteDRType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 5),
    _FsOspfRouteDRType_Type()
)
fsOspfRouteDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteDRType.setStatus("current")


class _FsOspfRouteType_Type(Integer32):
    """Custom type fsOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intral-area-route", 1),
          ("inter-area-route", 2))
    )


_FsOspfRouteType_Type.__name__ = "Integer32"
_FsOspfRouteType_Object = MibTableColumn
fsOspfRouteType = _FsOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 6),
    _FsOspfRouteType_Type()
)
fsOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteType.setStatus("current")
_FsOspfRouteSpfNo_Type = Counter32
_FsOspfRouteSpfNo_Object = MibTableColumn
fsOspfRouteSpfNo = _FsOspfRouteSpfNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 1, 10, 1, 7),
    _FsOspfRouteSpfNo_Type()
)
fsOspfRouteSpfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfRouteSpfNo.setStatus("current")
_FsOspfMIBConformance_ObjectIdentity = ObjectIdentity
fsOspfMIBConformance = _FsOspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2)
)
_FsOspfMIBCompliances_ObjectIdentity = ObjectIdentity
fsOspfMIBCompliances = _FsOspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 1)
)
_FsOspfMIBGroups_ObjectIdentity = ObjectIdentity
fsOspfMIBGroups = _FsOspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2)
)
_OspfMIBConformance_ObjectIdentity = ObjectIdentity
ospfMIBConformance = _OspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 3)
)
_OspfMIBCompliances_ObjectIdentity = ObjectIdentity
ospfMIBCompliances = _OspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 3, 1)
)

# Managed Objects groups

fsOspfBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 1)
)
fsOspfBaseMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfMiniLsaInterval"),
        ("FS-OSPF-MIB", "fsOspfMiniLsaArrival"),
        ("FS-OSPF-MIB", "fsOspfAreasNum"),
        ("FS-OSPF-MIB", "fsOspfNormalAreasNum"),
        ("FS-OSPF-MIB", "fsOspfStubAreasNum"),
        ("FS-OSPF-MIB", "fsOspfNssaAreasNum"),
        ("FS-OSPF-MIB", "fsOspfSpfDelay"),
        ("FS-OSPF-MIB", "fsOspfSpfHoldTime"),
        ("FS-OSPF-MIB", "fsOspfAutoCostRefBandWidthRef"),
        ("FS-OSPF-MIB", "fsOspfLsaGroupPacing"),
        ("FS-OSPF-MIB", "fsOspfInterDistance"),
        ("FS-OSPF-MIB", "fsOspfIntraDistance"),
        ("FS-OSPF-MIB", "fsOspfExternDistance"),
        ("FS-OSPF-MIB", "fsOspfLogAdjChangeNotify"),
        ("FS-OSPF-MIB", "fsOspfPassiveStatus"),
        ("FS-OSPF-MIB", "fsOspfRFC1583Compatibility"),
        ("FS-OSPF-MIB", "fsOspfRouteRedisDefMetricVal"))
)
if mibBuilder.loadTexts:
    fsOspfBaseMIBGroup.setStatus("current")

fsOspfAreaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 2)
)
fsOspfAreaMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfAreaId"),
        ("FS-OSPF-MIB", "fsOspfAuthType"),
        ("FS-OSPF-MIB", "fsOspfImportAsExtern"),
        ("FS-OSPF-MIB", "fsOspfSpfRuns"),
        ("FS-OSPF-MIB", "fsOspfAreaBdrRtrCount"),
        ("FS-OSPF-MIB", "fsOspfAsBdrRtrCount"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaCount"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaCksumSum"),
        ("FS-OSPF-MIB", "fsOspfAreaSummary"),
        ("FS-OSPF-MIB", "fsOspfAreaStatus"),
        ("FS-OSPF-MIB", "fsOspfAreaInterfaceNum"),
        ("FS-OSPF-MIB", "fsOspfAreaNssaIsRedistribution"),
        ("FS-OSPF-MIB", "fsOspfAreaNssaIsDefInfoOriginate"),
        ("FS-OSPF-MIB", "fsOspfNetWorkAreaID"),
        ("FS-OSPF-MIB", "fsOspfNetWorkAddress"),
        ("FS-OSPF-MIB", "fsOspfNetWorkMask"),
        ("FS-OSPF-MIB", "fsOspfNetWorkStatus"))
)
if mibBuilder.loadTexts:
    fsOspfAreaMIBGroup.setStatus("current")

fsOspfLsaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 3)
)
fsOspfLsaMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfLsdbAreaId"),
        ("FS-OSPF-MIB", "fsOspfLsdbType"),
        ("FS-OSPF-MIB", "fsOspfLsdbLsid"),
        ("FS-OSPF-MIB", "fsOspfLsdbRouterId"),
        ("FS-OSPF-MIB", "fsOspfLsdbSequence"),
        ("FS-OSPF-MIB", "fsOspfLsdbAge"),
        ("FS-OSPF-MIB", "fsOspfLsdbChecksum"),
        ("FS-OSPF-MIB", "fsOspfLsdbAdvertisement"),
        ("FS-OSPF-MIB", "fsOspfLsdbLinkNum"),
        ("FS-OSPF-MIB", "fsOspfLsdbPacketLength"),
        ("FS-OSPF-MIB", "fsOspfSummaryLsaNetworkMask"),
        ("FS-OSPF-MIB", "fsOspfSummaryLsaTos0Metric"),
        ("FS-OSPF-MIB", "fsOspfNssaLsaDetailMetricType"),
        ("FS-OSPF-MIB", "fsOspfNssaLsaDetailForwardAddr"),
        ("FS-OSPF-MIB", "fsOspfNssaLsaDetailRouteTag"),
        ("FS-OSPF-MIB", "fsOspfLsdbOption"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbType"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbLsid"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbRouterId"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbSequence"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbAge"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbChecksum"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbAdvertisement"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbNetworkMask"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbMetricType"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbForwardAddr"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbRouteTag"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbMetric"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbOption"),
        ("FS-OSPF-MIB", "fsOspfExtLsdbPacketLength"),
        ("FS-OSPF-MIB", "fsOspfRouterLsaDetailLinkID"),
        ("FS-OSPF-MIB", "fsOspfRouterLsaDetailLinkType"),
        ("FS-OSPF-MIB", "fsOspfRouterLsaDetailLinkData"),
        ("FS-OSPF-MIB", "fsOspfRouterLsaDetailTos0Metric"),
        ("FS-OSPF-MIB", "fsOspfNetWorkLsaDetailAttachedRouter"),
        ("FS-OSPF-MIB", "fsOspfNetWorkLsaDetailNetworkMask"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaDBSumAreaId"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaDBSumLsaType"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaDBSumCounts"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaDBSumDeletes"),
        ("FS-OSPF-MIB", "fsOspfAreaLsaDBSumMaxage"),
        ("FS-OSPF-MIB", "fsOspfLsaDBSumLsaType"),
        ("FS-OSPF-MIB", "fsOspfLsaDBSumCounts"),
        ("FS-OSPF-MIB", "fsOspfLsaDBSumDeletes"),
        ("FS-OSPF-MIB", "fsOspfLsaDBSumMaxage"))
)
if mibBuilder.loadTexts:
    fsOspfLsaMIBGroup.setStatus("current")

fsOspfIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 4)
)
fsOspfIfMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfIfIpAddress"),
        ("FS-OSPF-MIB", "fsOspfAddressLessIf"),
        ("FS-OSPF-MIB", "fsOspfIfAreaId"),
        ("FS-OSPF-MIB", "fsOspfIfType"),
        ("FS-OSPF-MIB", "fsOspfIfAdminStat"),
        ("FS-OSPF-MIB", "fsOspfIfRtrPriority"),
        ("FS-OSPF-MIB", "fsOspfIfTransitDelay"),
        ("FS-OSPF-MIB", "fsOspfIfRetransInterval"),
        ("FS-OSPF-MIB", "fsOspfIfHelloInterval"),
        ("FS-OSPF-MIB", "fsOspfIfRtrDeadInterval"),
        ("FS-OSPF-MIB", "fsOspfIfPollInterval"),
        ("FS-OSPF-MIB", "fsOspfIfState"),
        ("FS-OSPF-MIB", "fsOspfIfDesignatedRouter"),
        ("FS-OSPF-MIB", "fsOspfIfBackupDesignatedRouter"),
        ("FS-OSPF-MIB", "fsOspfIfEvents"),
        ("FS-OSPF-MIB", "fsOspfIfAuthType"),
        ("FS-OSPF-MIB", "fsOspfIfAuthKey"),
        ("FS-OSPF-MIB", "fsOspfIfStatus"),
        ("FS-OSPF-MIB", "fsOspfIfMulticastForwarding"),
        ("FS-OSPF-MIB", "fsOspfIfDemand"),
        ("FS-OSPF-MIB", "fsOspfIfDatabaseFilterAllOut"),
        ("FS-OSPF-MIB", "fsOspfIfDesignateRouterId"),
        ("FS-OSPF-MIB", "fsOspfIfBackupDesignateRouterId"),
        ("FS-OSPF-MIB", "fsOspfIfWaitInternal"),
        ("FS-OSPF-MIB", "fsOspfIfPassiveStatus"),
        ("FS-OSPF-MIB", "fsOspfIfCurrentUsedMd5AuthKeyId"),
        ("FS-OSPF-MIB", "fsOspfIfMd5AuthKeyIf"),
        ("FS-OSPF-MIB", "fsOspfIfMd5AuthKeyId"),
        ("FS-OSPF-MIB", "fsOspfIfMd5AuthKey"),
        ("FS-OSPF-MIB", "fsOspfIfMd5AuthKeySt"))
)
if mibBuilder.loadTexts:
    fsOspfIfMIBGroup.setStatus("current")

fsOspfVirtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 5)
)
fsOspfVirtMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfVirtIfAreaId"),
        ("FS-OSPF-MIB", "fsOspfVirtIfNeighbor"),
        ("FS-OSPF-MIB", "fsOspfVirtIfTransitDelay"),
        ("FS-OSPF-MIB", "fsOspfVirtIfRetransInterval"),
        ("FS-OSPF-MIB", "fsOspfVirtIfHelloInterval"),
        ("FS-OSPF-MIB", "fsOspfVirtIfRtrDeadInterval"),
        ("FS-OSPF-MIB", "fsOspfVirtIfState"),
        ("FS-OSPF-MIB", "fsOspfVirtIfEvents"),
        ("FS-OSPF-MIB", "fsOspfVirtIfAuthType"),
        ("FS-OSPF-MIB", "fsOspfVirtIfAuthKey"),
        ("FS-OSPF-MIB", "fsOspfVirtIfStatus"),
        ("FS-OSPF-MIB", "fsOspfVirtCost"),
        ("FS-OSPF-MIB", "fsOspfVirtNativeIfIndex"),
        ("FS-OSPF-MIB", "fsOspfVirtLinkState"),
        ("FS-OSPF-MIB", "fsOspfVirtHelloDueIn"),
        ("FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyAreaId"),
        ("FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyNeighbor"),
        ("FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeyId"),
        ("FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKey"),
        ("FS-OSPF-MIB", "fsOspfVirtIfMd5AuthKeySt"),
        ("FS-OSPF-MIB", "fsOspfVirtCurrentUsedMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    fsOspfVirtMIBGroup.setStatus("current")

fsOspfNeighborMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 6)
)
fsOspfNeighborMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfNbrIpAddr"),
        ("FS-OSPF-MIB", "fsOspfNbrAddressLessIndex"),
        ("FS-OSPF-MIB", "fsOspfNbrRtrId"),
        ("FS-OSPF-MIB", "fsOspfNbrOptions"),
        ("FS-OSPF-MIB", "fsOspfNbrPriority"),
        ("FS-OSPF-MIB", "fsOspfNbrState"),
        ("FS-OSPF-MIB", "fsOspfNbrEvents"),
        ("FS-OSPF-MIB", "fsOspfNbrLsRetransQLen"),
        ("FS-OSPF-MIB", "fsOspfNbmaNbrStatus"),
        ("FS-OSPF-MIB", "fsOspfNbmaNbrPermanence"),
        ("FS-OSPF-MIB", "fsOspfNbrHelloSuppressed"),
        ("FS-OSPF-MIB", "fsOspfNbrDeadTimeDueIn"),
        ("FS-OSPF-MIB", "fsOspfNbrNeighborUpTime"),
        ("FS-OSPF-MIB", "fsOspfNbrDR"),
        ("FS-OSPF-MIB", "fsOspfNbrBDR"),
        ("FS-OSPF-MIB", "fsOspfNbrArea"),
        ("FS-OSPF-MIB", "fsOspfNbrRetransmissionNum"))
)
if mibBuilder.loadTexts:
    fsOspfNeighborMIBGroup.setStatus("current")

fsOspfRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 2, 7)
)
fsOspfRouteInfoMIBGroup.setObjects(
      *(("FS-OSPF-MIB", "fsOspfRouteType"),
        ("FS-OSPF-MIB", "fsOspfRouteDest"),
        ("FS-OSPF-MIB", "fsOspfRouteNextHop"),
        ("FS-OSPF-MIB", "fsOspfRouteCost"),
        ("FS-OSPF-MIB", "fsOspfRouteDRType"),
        ("FS-OSPF-MIB", "fsOspfRouteArea"),
        ("FS-OSPF-MIB", "fsOspfRouteSpfNo"))
)
if mibBuilder.loadTexts:
    fsOspfRouteInfoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsOspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 2, 1, 1)
)
fsOspfMIBCompliance.setObjects(
      *(("FS-OSPF-MIB", "fsOspfBaseMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfAreaMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfLsaMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfIfMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfVirtMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfNeighborMIBGroup"),
        ("FS-OSPF-MIB", "fsOspfRouteInfoMIBGroup"))
)
if mibBuilder.loadTexts:
    fsOspfMIBCompliance.setStatus(
        "current"
    )

ospfExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ospfExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-OSPF-MIB",
    **{"fsOspfMIB": fsOspfMIB,
       "fsOspfMIBObjects": fsOspfMIBObjects,
       "fsOspfGeneralMibsGroup": fsOspfGeneralMibsGroup,
       "fsOspfMiniLsaInterval": fsOspfMiniLsaInterval,
       "fsOspfMiniLsaArrival": fsOspfMiniLsaArrival,
       "fsOspfAreasNum": fsOspfAreasNum,
       "fsOspfNormalAreasNum": fsOspfNormalAreasNum,
       "fsOspfStubAreasNum": fsOspfStubAreasNum,
       "fsOspfNssaAreasNum": fsOspfNssaAreasNum,
       "fsOspfSpfDelay": fsOspfSpfDelay,
       "fsOspfSpfHoldTime": fsOspfSpfHoldTime,
       "fsOspfAutoCostRefBandWidthRef": fsOspfAutoCostRefBandWidthRef,
       "fsOspfLsaGroupPacing": fsOspfLsaGroupPacing,
       "fsOspfInterDistance": fsOspfInterDistance,
       "fsOspfIntraDistance": fsOspfIntraDistance,
       "fsOspfExternDistance": fsOspfExternDistance,
       "fsOspfLogAdjChangeNotify": fsOspfLogAdjChangeNotify,
       "fsOspfPassiveStatus": fsOspfPassiveStatus,
       "fsOspfRFC1583Compatibility": fsOspfRFC1583Compatibility,
       "fsOspfRouteRedisDefMetricVal": fsOspfRouteRedisDefMetricVal,
       "fsOspfAdminiDistance": fsOspfAdminiDistance,
       "fsOspfAreaTable": fsOspfAreaTable,
       "fsOspfAreaEntry": fsOspfAreaEntry,
       "fsOspfAreaId": fsOspfAreaId,
       "fsOspfAuthType": fsOspfAuthType,
       "fsOspfImportAsExtern": fsOspfImportAsExtern,
       "fsOspfSpfRuns": fsOspfSpfRuns,
       "fsOspfAreaBdrRtrCount": fsOspfAreaBdrRtrCount,
       "fsOspfAsBdrRtrCount": fsOspfAsBdrRtrCount,
       "fsOspfAreaLsaCount": fsOspfAreaLsaCount,
       "fsOspfAreaLsaCksumSum": fsOspfAreaLsaCksumSum,
       "fsOspfAreaSummary": fsOspfAreaSummary,
       "fsOspfAreaStatus": fsOspfAreaStatus,
       "fsOspfAreaInterfaceNum": fsOspfAreaInterfaceNum,
       "fsOspfAreaNssaIsRedistribution": fsOspfAreaNssaIsRedistribution,
       "fsOspfAreaNssaIsDefInfoOriginate": fsOspfAreaNssaIsDefInfoOriginate,
       "fsOspfAddressScopeTable": fsOspfAddressScopeTable,
       "fsOspfAddressScopeEntry": fsOspfAddressScopeEntry,
       "fsOspfNetWorkAreaID": fsOspfNetWorkAreaID,
       "fsOspfNetWorkAddress": fsOspfNetWorkAddress,
       "fsOspfNetWorkMask": fsOspfNetWorkMask,
       "fsOspfNetWorkStatus": fsOspfNetWorkStatus,
       "fsOspfIfTable": fsOspfIfTable,
       "fsOspfIfEntry": fsOspfIfEntry,
       "fsOspfIfIpAddress": fsOspfIfIpAddress,
       "fsOspfAddressLessIf": fsOspfAddressLessIf,
       "fsOspfIfAreaId": fsOspfIfAreaId,
       "fsOspfIfType": fsOspfIfType,
       "fsOspfIfAdminStat": fsOspfIfAdminStat,
       "fsOspfIfRtrPriority": fsOspfIfRtrPriority,
       "fsOspfIfTransitDelay": fsOspfIfTransitDelay,
       "fsOspfIfRetransInterval": fsOspfIfRetransInterval,
       "fsOspfIfHelloInterval": fsOspfIfHelloInterval,
       "fsOspfIfRtrDeadInterval": fsOspfIfRtrDeadInterval,
       "fsOspfIfPollInterval": fsOspfIfPollInterval,
       "fsOspfIfState": fsOspfIfState,
       "fsOspfIfDesignatedRouter": fsOspfIfDesignatedRouter,
       "fsOspfIfBackupDesignatedRouter": fsOspfIfBackupDesignatedRouter,
       "fsOspfIfEvents": fsOspfIfEvents,
       "fsOspfIfAuthKey": fsOspfIfAuthKey,
       "fsOspfIfStatus": fsOspfIfStatus,
       "fsOspfIfMulticastForwarding": fsOspfIfMulticastForwarding,
       "fsOspfIfDemand": fsOspfIfDemand,
       "fsOspfIfAuthType": fsOspfIfAuthType,
       "fsOspfIfDatabaseFilterAllOut": fsOspfIfDatabaseFilterAllOut,
       "fsOspfIfDesignateRouterId": fsOspfIfDesignateRouterId,
       "fsOspfIfBackupDesignateRouterId": fsOspfIfBackupDesignateRouterId,
       "fsOspfIfWaitInternal": fsOspfIfWaitInternal,
       "fsOspfIfPassiveStatus": fsOspfIfPassiveStatus,
       "fsOspfIfCurrentUsedMd5AuthKeyId": fsOspfIfCurrentUsedMd5AuthKeyId,
       "fsOspfIfMd5AuthKeyTable": fsOspfIfMd5AuthKeyTable,
       "fsOspfIfMd5AuthKeyEntry": fsOspfIfMd5AuthKeyEntry,
       "fsOspfIfMd5AuthKeyIf": fsOspfIfMd5AuthKeyIf,
       "fsOspfIfMd5AuthKeyId": fsOspfIfMd5AuthKeyId,
       "fsOspfIfMd5AuthKey": fsOspfIfMd5AuthKey,
       "fsOspfIfMd5AuthKeySt": fsOspfIfMd5AuthKeySt,
       "fsOspfVirtTable": fsOspfVirtTable,
       "fsOspfVirtEntry": fsOspfVirtEntry,
       "fsOspfVirtIfAreaId": fsOspfVirtIfAreaId,
       "fsOspfVirtIfNeighbor": fsOspfVirtIfNeighbor,
       "fsOspfVirtIfTransitDelay": fsOspfVirtIfTransitDelay,
       "fsOspfVirtIfRetransInterval": fsOspfVirtIfRetransInterval,
       "fsOspfVirtIfHelloInterval": fsOspfVirtIfHelloInterval,
       "fsOspfVirtIfRtrDeadInterval": fsOspfVirtIfRtrDeadInterval,
       "fsOspfVirtIfState": fsOspfVirtIfState,
       "fsOspfVirtIfEvents": fsOspfVirtIfEvents,
       "fsOspfVirtIfAuthKey": fsOspfVirtIfAuthKey,
       "fsOspfVirtIfStatus": fsOspfVirtIfStatus,
       "fsOspfVirtIfAuthType": fsOspfVirtIfAuthType,
       "fsOspfVirtCost": fsOspfVirtCost,
       "fsOspfVirtNativeIfIndex": fsOspfVirtNativeIfIndex,
       "fsOspfVirtLinkState": fsOspfVirtLinkState,
       "fsOspfVirtHelloDueIn": fsOspfVirtHelloDueIn,
       "fsOspfVirtCurrentUsedMd5AuthKeyId": fsOspfVirtCurrentUsedMd5AuthKeyId,
       "fsOspfVirtIfMd5AuthKeyTable": fsOspfVirtIfMd5AuthKeyTable,
       "fsOspfVirtIfMd5AuthKeyEntry": fsOspfVirtIfMd5AuthKeyEntry,
       "fsOspfVirtIfMd5AuthKeyAreaId": fsOspfVirtIfMd5AuthKeyAreaId,
       "fsOspfVirtIfMd5AuthKeyNeighbor": fsOspfVirtIfMd5AuthKeyNeighbor,
       "fsOspfVirtIfMd5AuthKeyId": fsOspfVirtIfMd5AuthKeyId,
       "fsOspfVirtIfMd5AuthKey": fsOspfVirtIfMd5AuthKey,
       "fsOspfVirtIfMd5AuthKeySt": fsOspfVirtIfMd5AuthKeySt,
       "fsOspfLsaDetailInfoMibsGroup": fsOspfLsaDetailInfoMibsGroup,
       "fsOspfLsdbTable": fsOspfLsdbTable,
       "fsOspfLsdbEntry": fsOspfLsdbEntry,
       "fsOspfLsdbAreaId": fsOspfLsdbAreaId,
       "fsOspfLsdbType": fsOspfLsdbType,
       "fsOspfLsdbLsid": fsOspfLsdbLsid,
       "fsOspfLsdbRouterId": fsOspfLsdbRouterId,
       "fsOspfLsdbSequence": fsOspfLsdbSequence,
       "fsOspfLsdbAge": fsOspfLsdbAge,
       "fsOspfLsdbChecksum": fsOspfLsdbChecksum,
       "fsOspfLsdbAdvertisement": fsOspfLsdbAdvertisement,
       "fsOspfLsdbLinkNum": fsOspfLsdbLinkNum,
       "fsOspfLsdbPacketLength": fsOspfLsdbPacketLength,
       "fsOspfSummaryLsaNetworkMask": fsOspfSummaryLsaNetworkMask,
       "fsOspfSummaryLsaTos0Metric": fsOspfSummaryLsaTos0Metric,
       "fsOspfNssaLsaDetailMetricType": fsOspfNssaLsaDetailMetricType,
       "fsOspfNssaLsaDetailForwardAddr": fsOspfNssaLsaDetailForwardAddr,
       "fsOspfNssaLsaDetailRouteTag": fsOspfNssaLsaDetailRouteTag,
       "fsOspfLsdbOption": fsOspfLsdbOption,
       "fsOspfExtLsdbTable": fsOspfExtLsdbTable,
       "fsOspfExtLsdbEntry": fsOspfExtLsdbEntry,
       "fsOspfExtLsdbType": fsOspfExtLsdbType,
       "fsOspfExtLsdbLsid": fsOspfExtLsdbLsid,
       "fsOspfExtLsdbRouterId": fsOspfExtLsdbRouterId,
       "fsOspfExtLsdbSequence": fsOspfExtLsdbSequence,
       "fsOspfExtLsdbAge": fsOspfExtLsdbAge,
       "fsOspfExtLsdbChecksum": fsOspfExtLsdbChecksum,
       "fsOspfExtLsdbAdvertisement": fsOspfExtLsdbAdvertisement,
       "fsOspfExtLsdbNetworkMask": fsOspfExtLsdbNetworkMask,
       "fsOspfExtLsdbMetric": fsOspfExtLsdbMetric,
       "fsOspfExtLsdbMetricType": fsOspfExtLsdbMetricType,
       "fsOspfExtLsdbForwardAddr": fsOspfExtLsdbForwardAddr,
       "fsOspfExtLsdbRouteTag": fsOspfExtLsdbRouteTag,
       "fsOspfExtLsdbOption": fsOspfExtLsdbOption,
       "fsOspfExtLsdbPacketLength": fsOspfExtLsdbPacketLength,
       "fsOspfRouterLsaDetailTable": fsOspfRouterLsaDetailTable,
       "fsOspfRouterLsaDetailEntry": fsOspfRouterLsaDetailEntry,
       "fsOspfRouterLsaDetailLinkID": fsOspfRouterLsaDetailLinkID,
       "fsOspfRouterLsaDetailLinkType": fsOspfRouterLsaDetailLinkType,
       "fsOspfRouterLsaDetailLinkData": fsOspfRouterLsaDetailLinkData,
       "fsOspfRouterLsaDetailTos0Metric": fsOspfRouterLsaDetailTos0Metric,
       "fsOspfNetWorkLsaDetailTable": fsOspfNetWorkLsaDetailTable,
       "fsOspfNetWorkLsaDetailEntry": fsOspfNetWorkLsaDetailEntry,
       "fsOspfNetWorkLsaDetailAttachedRouter": fsOspfNetWorkLsaDetailAttachedRouter,
       "fsOspfNetWorkLsaDetailNetworkMask": fsOspfNetWorkLsaDetailNetworkMask,
       "fsOspfAreaLsaDBSumTable": fsOspfAreaLsaDBSumTable,
       "fsOspfAreaLsaDBSumEntry": fsOspfAreaLsaDBSumEntry,
       "fsOspfAreaLsaDBSumAreaId": fsOspfAreaLsaDBSumAreaId,
       "fsOspfAreaLsaDBSumLsaType": fsOspfAreaLsaDBSumLsaType,
       "fsOspfAreaLsaDBSumCounts": fsOspfAreaLsaDBSumCounts,
       "fsOspfAreaLsaDBSumDeletes": fsOspfAreaLsaDBSumDeletes,
       "fsOspfAreaLsaDBSumMaxage": fsOspfAreaLsaDBSumMaxage,
       "fsOspfLsaDBSumTable": fsOspfLsaDBSumTable,
       "fsOspfLsaDBSumEntry": fsOspfLsaDBSumEntry,
       "fsOspfLsaDBSumLsaType": fsOspfLsaDBSumLsaType,
       "fsOspfLsaDBSumCounts": fsOspfLsaDBSumCounts,
       "fsOspfLsaDBSumDeletes": fsOspfLsaDBSumDeletes,
       "fsOspfLsaDBSumMaxage": fsOspfLsaDBSumMaxage,
       "fsOspfNeighborTable": fsOspfNeighborTable,
       "fsOspfNeighborEntry": fsOspfNeighborEntry,
       "fsOspfNbrIpAddr": fsOspfNbrIpAddr,
       "fsOspfNbrAddressLessIndex": fsOspfNbrAddressLessIndex,
       "fsOspfNbrRtrId": fsOspfNbrRtrId,
       "fsOspfNbrOptions": fsOspfNbrOptions,
       "fsOspfNbrPriority": fsOspfNbrPriority,
       "fsOspfNbrState": fsOspfNbrState,
       "fsOspfNbrEvents": fsOspfNbrEvents,
       "fsOspfNbrLsRetransQLen": fsOspfNbrLsRetransQLen,
       "fsOspfNbmaNbrStatus": fsOspfNbmaNbrStatus,
       "fsOspfNbmaNbrPermanence": fsOspfNbmaNbrPermanence,
       "fsOspfNbrHelloSuppressed": fsOspfNbrHelloSuppressed,
       "fsOspfNbrDeadTimeDueIn": fsOspfNbrDeadTimeDueIn,
       "fsOspfNbrNeighborUpTime": fsOspfNbrNeighborUpTime,
       "fsOspfNbrDR": fsOspfNbrDR,
       "fsOspfNbrBDR": fsOspfNbrBDR,
       "fsOspfNbrArea": fsOspfNbrArea,
       "fsOspfNbrRetransmissionNum": fsOspfNbrRetransmissionNum,
       "fsOspfNbrIfState": fsOspfNbrIfState,
       "fsOspfRouteTable": fsOspfRouteTable,
       "fsOspfRouteEntry": fsOspfRouteEntry,
       "fsOspfRouteDest": fsOspfRouteDest,
       "fsOspfRouteArea": fsOspfRouteArea,
       "fsOspfRouteNextHop": fsOspfRouteNextHop,
       "fsOspfRouteCost": fsOspfRouteCost,
       "fsOspfRouteDRType": fsOspfRouteDRType,
       "fsOspfRouteType": fsOspfRouteType,
       "fsOspfRouteSpfNo": fsOspfRouteSpfNo,
       "fsOspfMIBConformance": fsOspfMIBConformance,
       "fsOspfMIBCompliances": fsOspfMIBCompliances,
       "fsOspfMIBCompliance": fsOspfMIBCompliance,
       "fsOspfMIBGroups": fsOspfMIBGroups,
       "fsOspfBaseMIBGroup": fsOspfBaseMIBGroup,
       "fsOspfAreaMIBGroup": fsOspfAreaMIBGroup,
       "fsOspfLsaMIBGroup": fsOspfLsaMIBGroup,
       "fsOspfIfMIBGroup": fsOspfIfMIBGroup,
       "fsOspfVirtMIBGroup": fsOspfVirtMIBGroup,
       "fsOspfNeighborMIBGroup": fsOspfNeighborMIBGroup,
       "fsOspfRouteInfoMIBGroup": fsOspfRouteInfoMIBGroup,
       "ospfMIBConformance": ospfMIBConformance,
       "ospfMIBCompliances": ospfMIBCompliances,
       "ospfExternCompliance": ospfExternCompliance}
)
