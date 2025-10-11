# SNMP MIB module (QTECH-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:46 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus")

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

qtechOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30)
)
if mibBuilder.loadTexts:
    qtechOspfMIB.setRevisions(
        ("2002-11-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechOspfMIBObjects_ObjectIdentity = ObjectIdentity
qtechOspfMIBObjects = _QtechOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1)
)
_QtechOspfGeneralMibsGroup_ObjectIdentity = ObjectIdentity
qtechOspfGeneralMibsGroup = _QtechOspfGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1)
)
_QtechOspfMiniLsaInterval_Type = Unsigned32
_QtechOspfMiniLsaInterval_Object = MibScalar
qtechOspfMiniLsaInterval = _QtechOspfMiniLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 1),
    _QtechOspfMiniLsaInterval_Type()
)
qtechOspfMiniLsaInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfMiniLsaInterval.setStatus("current")
_QtechOspfMiniLsaArrival_Type = Unsigned32
_QtechOspfMiniLsaArrival_Object = MibScalar
qtechOspfMiniLsaArrival = _QtechOspfMiniLsaArrival_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 2),
    _QtechOspfMiniLsaArrival_Type()
)
qtechOspfMiniLsaArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfMiniLsaArrival.setStatus("current")
_QtechOspfAreasNum_Type = Unsigned32
_QtechOspfAreasNum_Object = MibScalar
qtechOspfAreasNum = _QtechOspfAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 3),
    _QtechOspfAreasNum_Type()
)
qtechOspfAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreasNum.setStatus("current")
_QtechOspfNormalAreasNum_Type = Unsigned32
_QtechOspfNormalAreasNum_Object = MibScalar
qtechOspfNormalAreasNum = _QtechOspfNormalAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 4),
    _QtechOspfNormalAreasNum_Type()
)
qtechOspfNormalAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNormalAreasNum.setStatus("current")
_QtechOspfStubAreasNum_Type = Unsigned32
_QtechOspfStubAreasNum_Object = MibScalar
qtechOspfStubAreasNum = _QtechOspfStubAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 5),
    _QtechOspfStubAreasNum_Type()
)
qtechOspfStubAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfStubAreasNum.setStatus("current")
_QtechOspfNssaAreasNum_Type = Unsigned32
_QtechOspfNssaAreasNum_Object = MibScalar
qtechOspfNssaAreasNum = _QtechOspfNssaAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 6),
    _QtechOspfNssaAreasNum_Type()
)
qtechOspfNssaAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNssaAreasNum.setStatus("current")


class _QtechOspfSpfDelay_Type(Unsigned32):
    """Custom type qtechOspfSpfDelay based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechOspfSpfDelay_Type.__name__ = "Unsigned32"
_QtechOspfSpfDelay_Object = MibScalar
qtechOspfSpfDelay = _QtechOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 7),
    _QtechOspfSpfDelay_Type()
)
qtechOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfSpfDelay.setStatus("current")


class _QtechOspfSpfHoldTime_Type(Unsigned32):
    """Custom type qtechOspfSpfHoldTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechOspfSpfHoldTime_Type.__name__ = "Unsigned32"
_QtechOspfSpfHoldTime_Object = MibScalar
qtechOspfSpfHoldTime = _QtechOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 8),
    _QtechOspfSpfHoldTime_Type()
)
qtechOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfSpfHoldTime.setStatus("current")


class _QtechOspfAutoCostRefBandWidthRef_Type(Unsigned32):
    """Custom type qtechOspfAutoCostRefBandWidthRef based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechOspfAutoCostRefBandWidthRef_Type.__name__ = "Unsigned32"
_QtechOspfAutoCostRefBandWidthRef_Object = MibScalar
qtechOspfAutoCostRefBandWidthRef = _QtechOspfAutoCostRefBandWidthRef_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 9),
    _QtechOspfAutoCostRefBandWidthRef_Type()
)
qtechOspfAutoCostRefBandWidthRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfAutoCostRefBandWidthRef.setStatus("current")


class _QtechOspfLsaGroupPacing_Type(Unsigned32):
    """Custom type qtechOspfLsaGroupPacing based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_QtechOspfLsaGroupPacing_Type.__name__ = "Unsigned32"
_QtechOspfLsaGroupPacing_Object = MibScalar
qtechOspfLsaGroupPacing = _QtechOspfLsaGroupPacing_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 10),
    _QtechOspfLsaGroupPacing_Type()
)
qtechOspfLsaGroupPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfLsaGroupPacing.setStatus("current")


class _QtechOspfInterDistance_Type(Unsigned32):
    """Custom type qtechOspfInterDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfInterDistance_Type.__name__ = "Unsigned32"
_QtechOspfInterDistance_Object = MibScalar
qtechOspfInterDistance = _QtechOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 11),
    _QtechOspfInterDistance_Type()
)
qtechOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfInterDistance.setStatus("current")


class _QtechOspfIntraDistance_Type(Unsigned32):
    """Custom type qtechOspfIntraDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfIntraDistance_Type.__name__ = "Unsigned32"
_QtechOspfIntraDistance_Object = MibScalar
qtechOspfIntraDistance = _QtechOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 12),
    _QtechOspfIntraDistance_Type()
)
qtechOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIntraDistance.setStatus("current")


class _QtechOspfExternDistance_Type(Unsigned32):
    """Custom type qtechOspfExternDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfExternDistance_Type.__name__ = "Unsigned32"
_QtechOspfExternDistance_Object = MibScalar
qtechOspfExternDistance = _QtechOspfExternDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 13),
    _QtechOspfExternDistance_Type()
)
qtechOspfExternDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfExternDistance.setStatus("current")


class _QtechOspfLogAdjChangeNotify_Type(EnabledStatus):
    """Custom type qtechOspfLogAdjChangeNotify based on EnabledStatus"""
    defaultValue = 1


_QtechOspfLogAdjChangeNotify_Type.__name__ = "EnabledStatus"
_QtechOspfLogAdjChangeNotify_Object = MibScalar
qtechOspfLogAdjChangeNotify = _QtechOspfLogAdjChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 14),
    _QtechOspfLogAdjChangeNotify_Type()
)
qtechOspfLogAdjChangeNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfLogAdjChangeNotify.setStatus("current")


class _QtechOspfPassiveStatus_Type(EnabledStatus):
    """Custom type qtechOspfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_QtechOspfPassiveStatus_Type.__name__ = "EnabledStatus"
_QtechOspfPassiveStatus_Object = MibScalar
qtechOspfPassiveStatus = _QtechOspfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 15),
    _QtechOspfPassiveStatus_Type()
)
qtechOspfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfPassiveStatus.setStatus("current")


class _QtechOspfRFC1583Compatibility_Type(EnabledStatus):
    """Custom type qtechOspfRFC1583Compatibility based on EnabledStatus"""
    defaultValue = 1


_QtechOspfRFC1583Compatibility_Type.__name__ = "EnabledStatus"
_QtechOspfRFC1583Compatibility_Object = MibScalar
qtechOspfRFC1583Compatibility = _QtechOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 16),
    _QtechOspfRFC1583Compatibility_Type()
)
qtechOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfRFC1583Compatibility.setStatus("current")


class _QtechOspfRouteRedisDefMetricVal_Type(Unsigned32):
    """Custom type qtechOspfRouteRedisDefMetricVal based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_QtechOspfRouteRedisDefMetricVal_Type.__name__ = "Unsigned32"
_QtechOspfRouteRedisDefMetricVal_Object = MibScalar
qtechOspfRouteRedisDefMetricVal = _QtechOspfRouteRedisDefMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 17),
    _QtechOspfRouteRedisDefMetricVal_Type()
)
qtechOspfRouteRedisDefMetricVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfRouteRedisDefMetricVal.setStatus("current")


class _QtechOspfAdminiDistance_Type(Unsigned32):
    """Custom type qtechOspfAdminiDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfAdminiDistance_Type.__name__ = "Unsigned32"
_QtechOspfAdminiDistance_Object = MibScalar
qtechOspfAdminiDistance = _QtechOspfAdminiDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 1, 18),
    _QtechOspfAdminiDistance_Type()
)
qtechOspfAdminiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfAdminiDistance.setStatus("current")
_QtechOspfAreaTable_Object = MibTable
qtechOspfAreaTable = _QtechOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    qtechOspfAreaTable.setStatus("current")
_QtechOspfAreaEntry_Object = MibTableRow
qtechOspfAreaEntry = _QtechOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1)
)
qtechOspfAreaEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfAreaId"),
)
if mibBuilder.loadTexts:
    qtechOspfAreaEntry.setStatus("current")
_QtechOspfAreaId_Type = AreaID
_QtechOspfAreaId_Object = MibTableColumn
qtechOspfAreaId = _QtechOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 1),
    _QtechOspfAreaId_Type()
)
qtechOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaId.setStatus("current")


class _QtechOspfAuthType_Type(Integer32):
    """Custom type qtechOspfAuthType based on Integer32"""
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


_QtechOspfAuthType_Type.__name__ = "Integer32"
_QtechOspfAuthType_Object = MibTableColumn
qtechOspfAuthType = _QtechOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 2),
    _QtechOspfAuthType_Type()
)
qtechOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfAuthType.setStatus("current")


class _QtechOspfImportAsExtern_Type(Integer32):
    """Custom type qtechOspfImportAsExtern based on Integer32"""
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


_QtechOspfImportAsExtern_Type.__name__ = "Integer32"
_QtechOspfImportAsExtern_Object = MibTableColumn
qtechOspfImportAsExtern = _QtechOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 3),
    _QtechOspfImportAsExtern_Type()
)
qtechOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfImportAsExtern.setStatus("current")
_QtechOspfSpfRuns_Type = Counter32
_QtechOspfSpfRuns_Object = MibTableColumn
qtechOspfSpfRuns = _QtechOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 4),
    _QtechOspfSpfRuns_Type()
)
qtechOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfSpfRuns.setStatus("current")
_QtechOspfAreaBdrRtrCount_Type = Gauge32
_QtechOspfAreaBdrRtrCount_Object = MibTableColumn
qtechOspfAreaBdrRtrCount = _QtechOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 5),
    _QtechOspfAreaBdrRtrCount_Type()
)
qtechOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaBdrRtrCount.setStatus("current")
_QtechOspfAsBdrRtrCount_Type = Gauge32
_QtechOspfAsBdrRtrCount_Object = MibTableColumn
qtechOspfAsBdrRtrCount = _QtechOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 6),
    _QtechOspfAsBdrRtrCount_Type()
)
qtechOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAsBdrRtrCount.setStatus("current")
_QtechOspfAreaLsaCount_Type = Gauge32
_QtechOspfAreaLsaCount_Object = MibTableColumn
qtechOspfAreaLsaCount = _QtechOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 7),
    _QtechOspfAreaLsaCount_Type()
)
qtechOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaCount.setStatus("current")


class _QtechOspfAreaLsaCksumSum_Type(Unsigned32):
    """Custom type qtechOspfAreaLsaCksumSum based on Unsigned32"""
    defaultValue = 0


_QtechOspfAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_QtechOspfAreaLsaCksumSum_Object = MibTableColumn
qtechOspfAreaLsaCksumSum = _QtechOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 8),
    _QtechOspfAreaLsaCksumSum_Type()
)
qtechOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaCksumSum.setStatus("current")


class _QtechOspfAreaSummary_Type(Integer32):
    """Custom type qtechOspfAreaSummary based on Integer32"""
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


_QtechOspfAreaSummary_Type.__name__ = "Integer32"
_QtechOspfAreaSummary_Object = MibTableColumn
qtechOspfAreaSummary = _QtechOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 9),
    _QtechOspfAreaSummary_Type()
)
qtechOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfAreaSummary.setStatus("current")
_QtechOspfAreaStatus_Type = RowStatus
_QtechOspfAreaStatus_Object = MibTableColumn
qtechOspfAreaStatus = _QtechOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 10),
    _QtechOspfAreaStatus_Type()
)
qtechOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfAreaStatus.setStatus("current")
_QtechOspfAreaInterfaceNum_Type = Unsigned32
_QtechOspfAreaInterfaceNum_Object = MibTableColumn
qtechOspfAreaInterfaceNum = _QtechOspfAreaInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 11),
    _QtechOspfAreaInterfaceNum_Type()
)
qtechOspfAreaInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaInterfaceNum.setStatus("current")


class _QtechOspfAreaNssaIsRedistribution_Type(TruthValue):
    """Custom type qtechOspfAreaNssaIsRedistribution based on TruthValue"""
    defaultValue = 1


_QtechOspfAreaNssaIsRedistribution_Type.__name__ = "TruthValue"
_QtechOspfAreaNssaIsRedistribution_Object = MibTableColumn
qtechOspfAreaNssaIsRedistribution = _QtechOspfAreaNssaIsRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 12),
    _QtechOspfAreaNssaIsRedistribution_Type()
)
qtechOspfAreaNssaIsRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfAreaNssaIsRedistribution.setStatus("current")


class _QtechOspfAreaNssaIsDefInfoOriginate_Type(TruthValue):
    """Custom type qtechOspfAreaNssaIsDefInfoOriginate based on TruthValue"""
    defaultValue = 2


_QtechOspfAreaNssaIsDefInfoOriginate_Type.__name__ = "TruthValue"
_QtechOspfAreaNssaIsDefInfoOriginate_Object = MibTableColumn
qtechOspfAreaNssaIsDefInfoOriginate = _QtechOspfAreaNssaIsDefInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 2, 1, 13),
    _QtechOspfAreaNssaIsDefInfoOriginate_Type()
)
qtechOspfAreaNssaIsDefInfoOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfAreaNssaIsDefInfoOriginate.setStatus("current")
_QtechOspfAddressScopeTable_Object = MibTable
qtechOspfAddressScopeTable = _QtechOspfAddressScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    qtechOspfAddressScopeTable.setStatus("current")
_QtechOspfAddressScopeEntry_Object = MibTableRow
qtechOspfAddressScopeEntry = _QtechOspfAddressScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3, 1)
)
qtechOspfAddressScopeEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfNetWorkAreaID"),
    (0, "QTECH-OSPF-MIB", "qtechOspfNetWorkAddress"),
    (0, "QTECH-OSPF-MIB", "qtechOspfNetWorkMask"),
)
if mibBuilder.loadTexts:
    qtechOspfAddressScopeEntry.setStatus("current")
_QtechOspfNetWorkAreaID_Type = IpAddress
_QtechOspfNetWorkAreaID_Object = MibTableColumn
qtechOspfNetWorkAreaID = _QtechOspfNetWorkAreaID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3, 1, 1),
    _QtechOspfNetWorkAreaID_Type()
)
qtechOspfNetWorkAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNetWorkAreaID.setStatus("current")
_QtechOspfNetWorkAddress_Type = IpAddress
_QtechOspfNetWorkAddress_Object = MibTableColumn
qtechOspfNetWorkAddress = _QtechOspfNetWorkAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3, 1, 2),
    _QtechOspfNetWorkAddress_Type()
)
qtechOspfNetWorkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNetWorkAddress.setStatus("current")
_QtechOspfNetWorkMask_Type = IpAddress
_QtechOspfNetWorkMask_Object = MibTableColumn
qtechOspfNetWorkMask = _QtechOspfNetWorkMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3, 1, 3),
    _QtechOspfNetWorkMask_Type()
)
qtechOspfNetWorkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNetWorkMask.setStatus("current")
_QtechOspfNetWorkStatus_Type = RowStatus
_QtechOspfNetWorkStatus_Object = MibTableColumn
qtechOspfNetWorkStatus = _QtechOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 3, 1, 4),
    _QtechOspfNetWorkStatus_Type()
)
qtechOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfNetWorkStatus.setStatus("current")
_QtechOspfIfTable_Object = MibTable
qtechOspfIfTable = _QtechOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    qtechOspfIfTable.setStatus("current")
_QtechOspfIfEntry_Object = MibTableRow
qtechOspfIfEntry = _QtechOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1)
)
qtechOspfIfEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfIfIpAddress"),
    (0, "QTECH-OSPF-MIB", "qtechOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    qtechOspfIfEntry.setStatus("current")
_QtechOspfIfIpAddress_Type = IpAddress
_QtechOspfIfIpAddress_Object = MibTableColumn
qtechOspfIfIpAddress = _QtechOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 1),
    _QtechOspfIfIpAddress_Type()
)
qtechOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfIpAddress.setStatus("current")
_QtechOspfAddressLessIf_Type = Unsigned32
_QtechOspfAddressLessIf_Object = MibTableColumn
qtechOspfAddressLessIf = _QtechOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 2),
    _QtechOspfAddressLessIf_Type()
)
qtechOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAddressLessIf.setStatus("current")


class _QtechOspfIfAreaId_Type(AreaID):
    """Custom type qtechOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_QtechOspfIfAreaId_Type.__name__ = "AreaID"
_QtechOspfIfAreaId_Object = MibTableColumn
qtechOspfIfAreaId = _QtechOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 3),
    _QtechOspfIfAreaId_Type()
)
qtechOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfAreaId.setStatus("current")


class _QtechOspfIfType_Type(Integer32):
    """Custom type qtechOspfIfType based on Integer32"""
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


_QtechOspfIfType_Type.__name__ = "Integer32"
_QtechOspfIfType_Object = MibTableColumn
qtechOspfIfType = _QtechOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 4),
    _QtechOspfIfType_Type()
)
qtechOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfType.setStatus("current")
_QtechOspfIfAdminStat_Type = Status
_QtechOspfIfAdminStat_Object = MibTableColumn
qtechOspfIfAdminStat = _QtechOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 5),
    _QtechOspfIfAdminStat_Type()
)
qtechOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfAdminStat.setStatus("current")


class _QtechOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type qtechOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_QtechOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_QtechOspfIfRtrPriority_Object = MibTableColumn
qtechOspfIfRtrPriority = _QtechOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 6),
    _QtechOspfIfRtrPriority_Type()
)
qtechOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfRtrPriority.setStatus("current")


class _QtechOspfIfTransitDelay_Type(Unsigned32):
    """Custom type qtechOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_QtechOspfIfTransitDelay_Object = MibTableColumn
qtechOspfIfTransitDelay = _QtechOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 7),
    _QtechOspfIfTransitDelay_Type()
)
qtechOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfTransitDelay.setStatus("current")


class _QtechOspfIfRetransInterval_Type(Unsigned32):
    """Custom type qtechOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_QtechOspfIfRetransInterval_Object = MibTableColumn
qtechOspfIfRetransInterval = _QtechOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 8),
    _QtechOspfIfRetransInterval_Type()
)
qtechOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfRetransInterval.setStatus("current")


class _QtechOspfIfHelloInterval_Type(HelloRange):
    """Custom type qtechOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_QtechOspfIfHelloInterval_Type.__name__ = "HelloRange"
_QtechOspfIfHelloInterval_Object = MibTableColumn
qtechOspfIfHelloInterval = _QtechOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 9),
    _QtechOspfIfHelloInterval_Type()
)
qtechOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfHelloInterval.setStatus("current")


class _QtechOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type qtechOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_QtechOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_QtechOspfIfRtrDeadInterval_Object = MibTableColumn
qtechOspfIfRtrDeadInterval = _QtechOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 10),
    _QtechOspfIfRtrDeadInterval_Type()
)
qtechOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfRtrDeadInterval.setStatus("current")
_QtechOspfIfPollInterval_Type = PositiveInteger
_QtechOspfIfPollInterval_Object = MibTableColumn
qtechOspfIfPollInterval = _QtechOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 11),
    _QtechOspfIfPollInterval_Type()
)
qtechOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfPollInterval.setStatus("current")


class _QtechOspfIfState_Type(Integer32):
    """Custom type qtechOspfIfState based on Integer32"""
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


_QtechOspfIfState_Type.__name__ = "Integer32"
_QtechOspfIfState_Object = MibTableColumn
qtechOspfIfState = _QtechOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 12),
    _QtechOspfIfState_Type()
)
qtechOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfState.setStatus("current")


class _QtechOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type qtechOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_QtechOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_QtechOspfIfDesignatedRouter_Object = MibTableColumn
qtechOspfIfDesignatedRouter = _QtechOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 13),
    _QtechOspfIfDesignatedRouter_Type()
)
qtechOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfDesignatedRouter.setStatus("current")


class _QtechOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type qtechOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_QtechOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_QtechOspfIfBackupDesignatedRouter_Object = MibTableColumn
qtechOspfIfBackupDesignatedRouter = _QtechOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 14),
    _QtechOspfIfBackupDesignatedRouter_Type()
)
qtechOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfBackupDesignatedRouter.setStatus("current")
_QtechOspfIfEvents_Type = Counter32
_QtechOspfIfEvents_Object = MibTableColumn
qtechOspfIfEvents = _QtechOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 15),
    _QtechOspfIfEvents_Type()
)
qtechOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfEvents.setStatus("current")


class _QtechOspfIfAuthKey_Type(OctetString):
    """Custom type qtechOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechOspfIfAuthKey_Type.__name__ = "OctetString"
_QtechOspfIfAuthKey_Object = MibTableColumn
qtechOspfIfAuthKey = _QtechOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 16),
    _QtechOspfIfAuthKey_Type()
)
qtechOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfAuthKey.setStatus("current")
_QtechOspfIfStatus_Type = RowStatus
_QtechOspfIfStatus_Object = MibTableColumn
qtechOspfIfStatus = _QtechOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 17),
    _QtechOspfIfStatus_Type()
)
qtechOspfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfStatus.setStatus("current")


class _QtechOspfIfMulticastForwarding_Type(Integer32):
    """Custom type qtechOspfIfMulticastForwarding based on Integer32"""
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


_QtechOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_QtechOspfIfMulticastForwarding_Object = MibTableColumn
qtechOspfIfMulticastForwarding = _QtechOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 18),
    _QtechOspfIfMulticastForwarding_Type()
)
qtechOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfMulticastForwarding.setStatus("current")


class _QtechOspfIfDemand_Type(TruthValue):
    """Custom type qtechOspfIfDemand based on TruthValue"""
    defaultValue = 2


_QtechOspfIfDemand_Type.__name__ = "TruthValue"
_QtechOspfIfDemand_Object = MibTableColumn
qtechOspfIfDemand = _QtechOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 19),
    _QtechOspfIfDemand_Type()
)
qtechOspfIfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfDemand.setStatus("current")


class _QtechOspfIfAuthType_Type(Integer32):
    """Custom type qtechOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechOspfIfAuthType_Type.__name__ = "Integer32"
_QtechOspfIfAuthType_Object = MibTableColumn
qtechOspfIfAuthType = _QtechOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 20),
    _QtechOspfIfAuthType_Type()
)
qtechOspfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfAuthType.setStatus("current")


class _QtechOspfIfDatabaseFilterAllOut_Type(EnabledStatus):
    """Custom type qtechOspfIfDatabaseFilterAllOut based on EnabledStatus"""
    defaultValue = 2


_QtechOspfIfDatabaseFilterAllOut_Type.__name__ = "EnabledStatus"
_QtechOspfIfDatabaseFilterAllOut_Object = MibTableColumn
qtechOspfIfDatabaseFilterAllOut = _QtechOspfIfDatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 21),
    _QtechOspfIfDatabaseFilterAllOut_Type()
)
qtechOspfIfDatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfDatabaseFilterAllOut.setStatus("current")


class _QtechOspfIfDesignateRouterId_Type(IpAddress):
    """Custom type qtechOspfIfDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_QtechOspfIfDesignateRouterId_Type.__name__ = "IpAddress"
_QtechOspfIfDesignateRouterId_Object = MibTableColumn
qtechOspfIfDesignateRouterId = _QtechOspfIfDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 22),
    _QtechOspfIfDesignateRouterId_Type()
)
qtechOspfIfDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfDesignateRouterId.setStatus("current")


class _QtechOspfIfBackupDesignateRouterId_Type(IpAddress):
    """Custom type qtechOspfIfBackupDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_QtechOspfIfBackupDesignateRouterId_Type.__name__ = "IpAddress"
_QtechOspfIfBackupDesignateRouterId_Object = MibTableColumn
qtechOspfIfBackupDesignateRouterId = _QtechOspfIfBackupDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 23),
    _QtechOspfIfBackupDesignateRouterId_Type()
)
qtechOspfIfBackupDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfBackupDesignateRouterId.setStatus("current")
_QtechOspfIfWaitInternal_Type = TimeTicks
_QtechOspfIfWaitInternal_Object = MibTableColumn
qtechOspfIfWaitInternal = _QtechOspfIfWaitInternal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 24),
    _QtechOspfIfWaitInternal_Type()
)
qtechOspfIfWaitInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfWaitInternal.setStatus("current")


class _QtechOspfIfPassiveStatus_Type(EnabledStatus):
    """Custom type qtechOspfIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_QtechOspfIfPassiveStatus_Type.__name__ = "EnabledStatus"
_QtechOspfIfPassiveStatus_Object = MibTableColumn
qtechOspfIfPassiveStatus = _QtechOspfIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 25),
    _QtechOspfIfPassiveStatus_Type()
)
qtechOspfIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfPassiveStatus.setStatus("current")


class _QtechOspfIfCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type qtechOspfIfCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechOspfIfCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_QtechOspfIfCurrentUsedMd5AuthKeyId_Object = MibTableColumn
qtechOspfIfCurrentUsedMd5AuthKeyId = _QtechOspfIfCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 4, 1, 26),
    _QtechOspfIfCurrentUsedMd5AuthKeyId_Type()
)
qtechOspfIfCurrentUsedMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechOspfIfCurrentUsedMd5AuthKeyId.setStatus("current")
_QtechOspfIfMd5AuthKeyTable_Object = MibTable
qtechOspfIfMd5AuthKeyTable = _QtechOspfIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5)
)
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKeyTable.setStatus("current")
_QtechOspfIfMd5AuthKeyEntry_Object = MibTableRow
qtechOspfIfMd5AuthKeyEntry = _QtechOspfIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5, 1)
)
qtechOspfIfMd5AuthKeyEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKeyIf"),
    (0, "QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKeyEntry.setStatus("current")
_QtechOspfIfMd5AuthKeyIf_Type = Unsigned32
_QtechOspfIfMd5AuthKeyIf_Object = MibTableColumn
qtechOspfIfMd5AuthKeyIf = _QtechOspfIfMd5AuthKeyIf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5, 1, 1),
    _QtechOspfIfMd5AuthKeyIf_Type()
)
qtechOspfIfMd5AuthKeyIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKeyIf.setStatus("current")


class _QtechOspfIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type qtechOspfIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_QtechOspfIfMd5AuthKeyId_Object = MibTableColumn
qtechOspfIfMd5AuthKeyId = _QtechOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5, 1, 2),
    _QtechOspfIfMd5AuthKeyId_Type()
)
qtechOspfIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKeyId.setStatus("current")


class _QtechOspfIfMd5AuthKey_Type(OctetString):
    """Custom type qtechOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_QtechOspfIfMd5AuthKey_Object = MibTableColumn
qtechOspfIfMd5AuthKey = _QtechOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5, 1, 3),
    _QtechOspfIfMd5AuthKey_Type()
)
qtechOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKey.setStatus("current")
_QtechOspfIfMd5AuthKeySt_Type = ConfigStatus
_QtechOspfIfMd5AuthKeySt_Object = MibTableColumn
qtechOspfIfMd5AuthKeySt = _QtechOspfIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 5, 1, 4),
    _QtechOspfIfMd5AuthKeySt_Type()
)
qtechOspfIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfIfMd5AuthKeySt.setStatus("current")
_QtechOspfVirtTable_Object = MibTable
qtechOspfVirtTable = _QtechOspfVirtTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6)
)
if mibBuilder.loadTexts:
    qtechOspfVirtTable.setStatus("current")
_QtechOspfVirtEntry_Object = MibTableRow
qtechOspfVirtEntry = _QtechOspfVirtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1)
)
qtechOspfVirtEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfVirtIfAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    qtechOspfVirtEntry.setStatus("current")
_QtechOspfVirtIfAreaId_Type = AreaID
_QtechOspfVirtIfAreaId_Object = MibTableColumn
qtechOspfVirtIfAreaId = _QtechOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 1),
    _QtechOspfVirtIfAreaId_Type()
)
qtechOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfAreaId.setStatus("current")
_QtechOspfVirtIfNeighbor_Type = RouterID
_QtechOspfVirtIfNeighbor_Object = MibTableColumn
qtechOspfVirtIfNeighbor = _QtechOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 2),
    _QtechOspfVirtIfNeighbor_Type()
)
qtechOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfNeighbor.setStatus("current")


class _QtechOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type qtechOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_QtechOspfVirtIfTransitDelay_Object = MibTableColumn
qtechOspfVirtIfTransitDelay = _QtechOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 3),
    _QtechOspfVirtIfTransitDelay_Type()
)
qtechOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfTransitDelay.setStatus("current")


class _QtechOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type qtechOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_QtechOspfVirtIfRetransInterval_Object = MibTableColumn
qtechOspfVirtIfRetransInterval = _QtechOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 4),
    _QtechOspfVirtIfRetransInterval_Type()
)
qtechOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfRetransInterval.setStatus("current")


class _QtechOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type qtechOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_QtechOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_QtechOspfVirtIfHelloInterval_Object = MibTableColumn
qtechOspfVirtIfHelloInterval = _QtechOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 5),
    _QtechOspfVirtIfHelloInterval_Type()
)
qtechOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfHelloInterval.setStatus("current")


class _QtechOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type qtechOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_QtechOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_QtechOspfVirtIfRtrDeadInterval_Object = MibTableColumn
qtechOspfVirtIfRtrDeadInterval = _QtechOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 6),
    _QtechOspfVirtIfRtrDeadInterval_Type()
)
qtechOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfRtrDeadInterval.setStatus("current")


class _QtechOspfVirtIfState_Type(Integer32):
    """Custom type qtechOspfVirtIfState based on Integer32"""
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


_QtechOspfVirtIfState_Type.__name__ = "Integer32"
_QtechOspfVirtIfState_Object = MibTableColumn
qtechOspfVirtIfState = _QtechOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 7),
    _QtechOspfVirtIfState_Type()
)
qtechOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfState.setStatus("current")
_QtechOspfVirtIfEvents_Type = Counter32
_QtechOspfVirtIfEvents_Object = MibTableColumn
qtechOspfVirtIfEvents = _QtechOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 8),
    _QtechOspfVirtIfEvents_Type()
)
qtechOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfEvents.setStatus("current")


class _QtechOspfVirtIfAuthKey_Type(OctetString):
    """Custom type qtechOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_QtechOspfVirtIfAuthKey_Object = MibTableColumn
qtechOspfVirtIfAuthKey = _QtechOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 9),
    _QtechOspfVirtIfAuthKey_Type()
)
qtechOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfAuthKey.setStatus("current")
_QtechOspfVirtIfStatus_Type = RowStatus
_QtechOspfVirtIfStatus_Object = MibTableColumn
qtechOspfVirtIfStatus = _QtechOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 10),
    _QtechOspfVirtIfStatus_Type()
)
qtechOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfStatus.setStatus("current")


class _QtechOspfVirtIfAuthType_Type(Integer32):
    """Custom type qtechOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechOspfVirtIfAuthType_Type.__name__ = "Integer32"
_QtechOspfVirtIfAuthType_Object = MibTableColumn
qtechOspfVirtIfAuthType = _QtechOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 11),
    _QtechOspfVirtIfAuthType_Type()
)
qtechOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfAuthType.setStatus("current")
_QtechOspfVirtCost_Type = Unsigned32
_QtechOspfVirtCost_Object = MibTableColumn
qtechOspfVirtCost = _QtechOspfVirtCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 12),
    _QtechOspfVirtCost_Type()
)
qtechOspfVirtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtCost.setStatus("current")
_QtechOspfVirtNativeIfIndex_Type = Integer32
_QtechOspfVirtNativeIfIndex_Object = MibTableColumn
qtechOspfVirtNativeIfIndex = _QtechOspfVirtNativeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 13),
    _QtechOspfVirtNativeIfIndex_Type()
)
qtechOspfVirtNativeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtNativeIfIndex.setStatus("current")


class _QtechOspfVirtLinkState_Type(Integer32):
    """Custom type qtechOspfVirtLinkState based on Integer32"""
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


_QtechOspfVirtLinkState_Type.__name__ = "Integer32"
_QtechOspfVirtLinkState_Object = MibTableColumn
qtechOspfVirtLinkState = _QtechOspfVirtLinkState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 14),
    _QtechOspfVirtLinkState_Type()
)
qtechOspfVirtLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtLinkState.setStatus("current")
_QtechOspfVirtHelloDueIn_Type = TimeTicks
_QtechOspfVirtHelloDueIn_Object = MibTableColumn
qtechOspfVirtHelloDueIn = _QtechOspfVirtHelloDueIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 15),
    _QtechOspfVirtHelloDueIn_Type()
)
qtechOspfVirtHelloDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtHelloDueIn.setStatus("current")


class _QtechOspfVirtCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type qtechOspfVirtCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechOspfVirtCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_QtechOspfVirtCurrentUsedMd5AuthKeyId_Object = MibTableColumn
qtechOspfVirtCurrentUsedMd5AuthKeyId = _QtechOspfVirtCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 6, 1, 16),
    _QtechOspfVirtCurrentUsedMd5AuthKeyId_Type()
)
qtechOspfVirtCurrentUsedMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtCurrentUsedMd5AuthKeyId.setStatus("current")
_QtechOspfVirtIfMd5AuthKeyTable_Object = MibTable
qtechOspfVirtIfMd5AuthKeyTable = _QtechOspfVirtIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7)
)
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeyTable.setStatus("current")
_QtechOspfVirtIfMd5AuthKeyEntry_Object = MibTableRow
qtechOspfVirtIfMd5AuthKeyEntry = _QtechOspfVirtIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1)
)
qtechOspfVirtIfMd5AuthKeyEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyNeighbor"),
    (0, "QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeyEntry.setStatus("current")
_QtechOspfVirtIfMd5AuthKeyAreaId_Type = AreaID
_QtechOspfVirtIfMd5AuthKeyAreaId_Object = MibTableColumn
qtechOspfVirtIfMd5AuthKeyAreaId = _QtechOspfVirtIfMd5AuthKeyAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1, 1),
    _QtechOspfVirtIfMd5AuthKeyAreaId_Type()
)
qtechOspfVirtIfMd5AuthKeyAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeyAreaId.setStatus("current")
_QtechOspfVirtIfMd5AuthKeyNeighbor_Type = RouterID
_QtechOspfVirtIfMd5AuthKeyNeighbor_Object = MibTableColumn
qtechOspfVirtIfMd5AuthKeyNeighbor = _QtechOspfVirtIfMd5AuthKeyNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1, 2),
    _QtechOspfVirtIfMd5AuthKeyNeighbor_Type()
)
qtechOspfVirtIfMd5AuthKeyNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeyNeighbor.setStatus("current")


class _QtechOspfVirtIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type qtechOspfVirtIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechOspfVirtIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_QtechOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
qtechOspfVirtIfMd5AuthKeyId = _QtechOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1, 3),
    _QtechOspfVirtIfMd5AuthKeyId_Type()
)
qtechOspfVirtIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeyId.setStatus("current")


class _QtechOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type qtechOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_QtechOspfVirtIfMd5AuthKey_Object = MibTableColumn
qtechOspfVirtIfMd5AuthKey = _QtechOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1, 4),
    _QtechOspfVirtIfMd5AuthKey_Type()
)
qtechOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKey.setStatus("current")
_QtechOspfVirtIfMd5AuthKeySt_Type = ConfigStatus
_QtechOspfVirtIfMd5AuthKeySt_Object = MibTableColumn
qtechOspfVirtIfMd5AuthKeySt = _QtechOspfVirtIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 7, 1, 5),
    _QtechOspfVirtIfMd5AuthKeySt_Type()
)
qtechOspfVirtIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechOspfVirtIfMd5AuthKeySt.setStatus("current")
_QtechOspfLsaDetailInfoMibsGroup_ObjectIdentity = ObjectIdentity
qtechOspfLsaDetailInfoMibsGroup = _QtechOspfLsaDetailInfoMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8)
)
_QtechOspfLsdbTable_Object = MibTable
qtechOspfLsdbTable = _QtechOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1)
)
if mibBuilder.loadTexts:
    qtechOspfLsdbTable.setStatus("current")
_QtechOspfLsdbEntry_Object = MibTableRow
qtechOspfLsdbEntry = _QtechOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1)
)
qtechOspfLsdbEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbType"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbLsid"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    qtechOspfLsdbEntry.setStatus("current")
_QtechOspfLsdbAreaId_Type = AreaID
_QtechOspfLsdbAreaId_Object = MibTableColumn
qtechOspfLsdbAreaId = _QtechOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 1),
    _QtechOspfLsdbAreaId_Type()
)
qtechOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbAreaId.setStatus("current")


class _QtechOspfLsdbType_Type(Integer32):
    """Custom type qtechOspfLsdbType based on Integer32"""
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


_QtechOspfLsdbType_Type.__name__ = "Integer32"
_QtechOspfLsdbType_Object = MibTableColumn
qtechOspfLsdbType = _QtechOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 2),
    _QtechOspfLsdbType_Type()
)
qtechOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbType.setStatus("current")
_QtechOspfLsdbLsid_Type = IpAddress
_QtechOspfLsdbLsid_Object = MibTableColumn
qtechOspfLsdbLsid = _QtechOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 3),
    _QtechOspfLsdbLsid_Type()
)
qtechOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbLsid.setStatus("current")
_QtechOspfLsdbRouterId_Type = RouterID
_QtechOspfLsdbRouterId_Object = MibTableColumn
qtechOspfLsdbRouterId = _QtechOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 4),
    _QtechOspfLsdbRouterId_Type()
)
qtechOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbRouterId.setStatus("current")
_QtechOspfLsdbSequence_Type = Unsigned32
_QtechOspfLsdbSequence_Object = MibTableColumn
qtechOspfLsdbSequence = _QtechOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 5),
    _QtechOspfLsdbSequence_Type()
)
qtechOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbSequence.setStatus("current")
_QtechOspfLsdbAge_Type = Unsigned32
_QtechOspfLsdbAge_Object = MibTableColumn
qtechOspfLsdbAge = _QtechOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 6),
    _QtechOspfLsdbAge_Type()
)
qtechOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbAge.setStatus("current")
_QtechOspfLsdbChecksum_Type = Unsigned32
_QtechOspfLsdbChecksum_Object = MibTableColumn
qtechOspfLsdbChecksum = _QtechOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 7),
    _QtechOspfLsdbChecksum_Type()
)
qtechOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbChecksum.setStatus("current")


class _QtechOspfLsdbAdvertisement_Type(OctetString):
    """Custom type qtechOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_QtechOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_QtechOspfLsdbAdvertisement_Object = MibTableColumn
qtechOspfLsdbAdvertisement = _QtechOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 8),
    _QtechOspfLsdbAdvertisement_Type()
)
qtechOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbAdvertisement.setStatus("current")


class _QtechOspfLsdbLinkNum_Type(Unsigned32):
    """Custom type qtechOspfLsdbLinkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QtechOspfLsdbLinkNum_Type.__name__ = "Unsigned32"
_QtechOspfLsdbLinkNum_Object = MibTableColumn
qtechOspfLsdbLinkNum = _QtechOspfLsdbLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 9),
    _QtechOspfLsdbLinkNum_Type()
)
qtechOspfLsdbLinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbLinkNum.setStatus("current")


class _QtechOspfLsdbPacketLength_Type(Unsigned32):
    """Custom type qtechOspfLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechOspfLsdbPacketLength_Type.__name__ = "Unsigned32"
_QtechOspfLsdbPacketLength_Object = MibTableColumn
qtechOspfLsdbPacketLength = _QtechOspfLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 10),
    _QtechOspfLsdbPacketLength_Type()
)
qtechOspfLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbPacketLength.setStatus("current")
_QtechOspfSummaryLsaNetworkMask_Type = IpAddress
_QtechOspfSummaryLsaNetworkMask_Object = MibTableColumn
qtechOspfSummaryLsaNetworkMask = _QtechOspfSummaryLsaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 11),
    _QtechOspfSummaryLsaNetworkMask_Type()
)
qtechOspfSummaryLsaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfSummaryLsaNetworkMask.setStatus("current")


class _QtechOspfSummaryLsaTos0Metric_Type(Unsigned32):
    """Custom type qtechOspfSummaryLsaTos0Metric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechOspfSummaryLsaTos0Metric_Type.__name__ = "Unsigned32"
_QtechOspfSummaryLsaTos0Metric_Object = MibTableColumn
qtechOspfSummaryLsaTos0Metric = _QtechOspfSummaryLsaTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 12),
    _QtechOspfSummaryLsaTos0Metric_Type()
)
qtechOspfSummaryLsaTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfSummaryLsaTos0Metric.setStatus("current")


class _QtechOspfNssaLsaDetailMetricType_Type(Integer32):
    """Custom type qtechOspfNssaLsaDetailMetricType based on Integer32"""
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


_QtechOspfNssaLsaDetailMetricType_Type.__name__ = "Integer32"
_QtechOspfNssaLsaDetailMetricType_Object = MibTableColumn
qtechOspfNssaLsaDetailMetricType = _QtechOspfNssaLsaDetailMetricType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 13),
    _QtechOspfNssaLsaDetailMetricType_Type()
)
qtechOspfNssaLsaDetailMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNssaLsaDetailMetricType.setStatus("current")
_QtechOspfNssaLsaDetailForwardAddr_Type = IpAddress
_QtechOspfNssaLsaDetailForwardAddr_Object = MibTableColumn
qtechOspfNssaLsaDetailForwardAddr = _QtechOspfNssaLsaDetailForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 14),
    _QtechOspfNssaLsaDetailForwardAddr_Type()
)
qtechOspfNssaLsaDetailForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNssaLsaDetailForwardAddr.setStatus("current")
_QtechOspfNssaLsaDetailRouteTag_Type = Unsigned32
_QtechOspfNssaLsaDetailRouteTag_Object = MibTableColumn
qtechOspfNssaLsaDetailRouteTag = _QtechOspfNssaLsaDetailRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 15),
    _QtechOspfNssaLsaDetailRouteTag_Type()
)
qtechOspfNssaLsaDetailRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNssaLsaDetailRouteTag.setStatus("current")
_QtechOspfLsdbOption_Type = Unsigned32
_QtechOspfLsdbOption_Object = MibTableColumn
qtechOspfLsdbOption = _QtechOspfLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 1, 1, 16),
    _QtechOspfLsdbOption_Type()
)
qtechOspfLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsdbOption.setStatus("current")
_QtechOspfExtLsdbTable_Object = MibTable
qtechOspfExtLsdbTable = _QtechOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2)
)
if mibBuilder.loadTexts:
    qtechOspfExtLsdbTable.setStatus("current")
_QtechOspfExtLsdbEntry_Object = MibTableRow
qtechOspfExtLsdbEntry = _QtechOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1)
)
qtechOspfExtLsdbEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfExtLsdbType"),
    (0, "QTECH-OSPF-MIB", "qtechOspfExtLsdbLsid"),
    (0, "QTECH-OSPF-MIB", "qtechOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    qtechOspfExtLsdbEntry.setStatus("current")


class _QtechOspfExtLsdbType_Type(Integer32):
    """Custom type qtechOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_QtechOspfExtLsdbType_Type.__name__ = "Integer32"
_QtechOspfExtLsdbType_Object = MibTableColumn
qtechOspfExtLsdbType = _QtechOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 1),
    _QtechOspfExtLsdbType_Type()
)
qtechOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbType.setStatus("current")
_QtechOspfExtLsdbLsid_Type = IpAddress
_QtechOspfExtLsdbLsid_Object = MibTableColumn
qtechOspfExtLsdbLsid = _QtechOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 2),
    _QtechOspfExtLsdbLsid_Type()
)
qtechOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbLsid.setStatus("current")
_QtechOspfExtLsdbRouterId_Type = RouterID
_QtechOspfExtLsdbRouterId_Object = MibTableColumn
qtechOspfExtLsdbRouterId = _QtechOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 3),
    _QtechOspfExtLsdbRouterId_Type()
)
qtechOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbRouterId.setStatus("current")
_QtechOspfExtLsdbSequence_Type = Unsigned32
_QtechOspfExtLsdbSequence_Object = MibTableColumn
qtechOspfExtLsdbSequence = _QtechOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 4),
    _QtechOspfExtLsdbSequence_Type()
)
qtechOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbSequence.setStatus("current")
_QtechOspfExtLsdbAge_Type = Unsigned32
_QtechOspfExtLsdbAge_Object = MibTableColumn
qtechOspfExtLsdbAge = _QtechOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 5),
    _QtechOspfExtLsdbAge_Type()
)
qtechOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbAge.setStatus("current")
_QtechOspfExtLsdbChecksum_Type = Unsigned32
_QtechOspfExtLsdbChecksum_Object = MibTableColumn
qtechOspfExtLsdbChecksum = _QtechOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 6),
    _QtechOspfExtLsdbChecksum_Type()
)
qtechOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbChecksum.setStatus("current")


class _QtechOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type qtechOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_QtechOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_QtechOspfExtLsdbAdvertisement_Object = MibTableColumn
qtechOspfExtLsdbAdvertisement = _QtechOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 7),
    _QtechOspfExtLsdbAdvertisement_Type()
)
qtechOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbAdvertisement.setStatus("current")
_QtechOspfExtLsdbNetworkMask_Type = IpAddress
_QtechOspfExtLsdbNetworkMask_Object = MibTableColumn
qtechOspfExtLsdbNetworkMask = _QtechOspfExtLsdbNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 8),
    _QtechOspfExtLsdbNetworkMask_Type()
)
qtechOspfExtLsdbNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbNetworkMask.setStatus("current")
_QtechOspfExtLsdbMetric_Type = Integer32
_QtechOspfExtLsdbMetric_Object = MibTableColumn
qtechOspfExtLsdbMetric = _QtechOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 9),
    _QtechOspfExtLsdbMetric_Type()
)
qtechOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbMetric.setStatus("current")


class _QtechOspfExtLsdbMetricType_Type(Integer32):
    """Custom type qtechOspfExtLsdbMetricType based on Integer32"""
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


_QtechOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_QtechOspfExtLsdbMetricType_Object = MibTableColumn
qtechOspfExtLsdbMetricType = _QtechOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 10),
    _QtechOspfExtLsdbMetricType_Type()
)
qtechOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbMetricType.setStatus("current")
_QtechOspfExtLsdbForwardAddr_Type = IpAddress
_QtechOspfExtLsdbForwardAddr_Object = MibTableColumn
qtechOspfExtLsdbForwardAddr = _QtechOspfExtLsdbForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 11),
    _QtechOspfExtLsdbForwardAddr_Type()
)
qtechOspfExtLsdbForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbForwardAddr.setStatus("current")
_QtechOspfExtLsdbRouteTag_Type = Unsigned32
_QtechOspfExtLsdbRouteTag_Object = MibTableColumn
qtechOspfExtLsdbRouteTag = _QtechOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 12),
    _QtechOspfExtLsdbRouteTag_Type()
)
qtechOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbRouteTag.setStatus("current")
_QtechOspfExtLsdbOption_Type = Unsigned32
_QtechOspfExtLsdbOption_Object = MibTableColumn
qtechOspfExtLsdbOption = _QtechOspfExtLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 13),
    _QtechOspfExtLsdbOption_Type()
)
qtechOspfExtLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbOption.setStatus("current")


class _QtechOspfExtLsdbPacketLength_Type(Unsigned32):
    """Custom type qtechOspfExtLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechOspfExtLsdbPacketLength_Type.__name__ = "Unsigned32"
_QtechOspfExtLsdbPacketLength_Object = MibTableColumn
qtechOspfExtLsdbPacketLength = _QtechOspfExtLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 2, 1, 14),
    _QtechOspfExtLsdbPacketLength_Type()
)
qtechOspfExtLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfExtLsdbPacketLength.setStatus("current")
_QtechOspfRouterLsaDetailTable_Object = MibTable
qtechOspfRouterLsaDetailTable = _QtechOspfRouterLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3)
)
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailTable.setStatus("current")
_QtechOspfRouterLsaDetailEntry_Object = MibTableRow
qtechOspfRouterLsaDetailEntry = _QtechOspfRouterLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3, 1)
)
qtechOspfRouterLsaDetailEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbType"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbLsid"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbRouterId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfRouterLsaDetailLinkID"),
)
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailEntry.setStatus("current")
_QtechOspfRouterLsaDetailLinkID_Type = IpAddress
_QtechOspfRouterLsaDetailLinkID_Object = MibTableColumn
qtechOspfRouterLsaDetailLinkID = _QtechOspfRouterLsaDetailLinkID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3, 1, 1),
    _QtechOspfRouterLsaDetailLinkID_Type()
)
qtechOspfRouterLsaDetailLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailLinkID.setStatus("current")


class _QtechOspfRouterLsaDetailLinkType_Type(Integer32):
    """Custom type qtechOspfRouterLsaDetailLinkType based on Integer32"""
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


_QtechOspfRouterLsaDetailLinkType_Type.__name__ = "Integer32"
_QtechOspfRouterLsaDetailLinkType_Object = MibTableColumn
qtechOspfRouterLsaDetailLinkType = _QtechOspfRouterLsaDetailLinkType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3, 1, 2),
    _QtechOspfRouterLsaDetailLinkType_Type()
)
qtechOspfRouterLsaDetailLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailLinkType.setStatus("current")
_QtechOspfRouterLsaDetailLinkData_Type = IpAddress
_QtechOspfRouterLsaDetailLinkData_Object = MibTableColumn
qtechOspfRouterLsaDetailLinkData = _QtechOspfRouterLsaDetailLinkData_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3, 1, 3),
    _QtechOspfRouterLsaDetailLinkData_Type()
)
qtechOspfRouterLsaDetailLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailLinkData.setStatus("current")
_QtechOspfRouterLsaDetailTos0Metric_Type = Unsigned32
_QtechOspfRouterLsaDetailTos0Metric_Object = MibTableColumn
qtechOspfRouterLsaDetailTos0Metric = _QtechOspfRouterLsaDetailTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 3, 1, 4),
    _QtechOspfRouterLsaDetailTos0Metric_Type()
)
qtechOspfRouterLsaDetailTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouterLsaDetailTos0Metric.setStatus("current")
_QtechOspfNetWorkLsaDetailTable_Object = MibTable
qtechOspfNetWorkLsaDetailTable = _QtechOspfNetWorkLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 4)
)
if mibBuilder.loadTexts:
    qtechOspfNetWorkLsaDetailTable.setStatus("current")
_QtechOspfNetWorkLsaDetailEntry_Object = MibTableRow
qtechOspfNetWorkLsaDetailEntry = _QtechOspfNetWorkLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 4, 1)
)
qtechOspfNetWorkLsaDetailEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbType"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbLsid"),
    (0, "QTECH-OSPF-MIB", "qtechOspfLsdbRouterId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfNetWorkLsaDetailAttachedRouter"),
)
if mibBuilder.loadTexts:
    qtechOspfNetWorkLsaDetailEntry.setStatus("current")
_QtechOspfNetWorkLsaDetailAttachedRouter_Type = IpAddress
_QtechOspfNetWorkLsaDetailAttachedRouter_Object = MibTableColumn
qtechOspfNetWorkLsaDetailAttachedRouter = _QtechOspfNetWorkLsaDetailAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 4, 1, 1),
    _QtechOspfNetWorkLsaDetailAttachedRouter_Type()
)
qtechOspfNetWorkLsaDetailAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNetWorkLsaDetailAttachedRouter.setStatus("current")
_QtechOspfNetWorkLsaDetailNetworkMask_Type = IpAddress
_QtechOspfNetWorkLsaDetailNetworkMask_Object = MibTableColumn
qtechOspfNetWorkLsaDetailNetworkMask = _QtechOspfNetWorkLsaDetailNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 4, 1, 2),
    _QtechOspfNetWorkLsaDetailNetworkMask_Type()
)
qtechOspfNetWorkLsaDetailNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNetWorkLsaDetailNetworkMask.setStatus("current")
_QtechOspfAreaLsaDBSumTable_Object = MibTable
qtechOspfAreaLsaDBSumTable = _QtechOspfAreaLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5)
)
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumTable.setStatus("current")
_QtechOspfAreaLsaDBSumEntry_Object = MibTableRow
qtechOspfAreaLsaDBSumEntry = _QtechOspfAreaLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1)
)
qtechOspfAreaLsaDBSumEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumAreaId"),
    (0, "QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumEntry.setStatus("current")
_QtechOspfAreaLsaDBSumAreaId_Type = IpAddress
_QtechOspfAreaLsaDBSumAreaId_Object = MibTableColumn
qtechOspfAreaLsaDBSumAreaId = _QtechOspfAreaLsaDBSumAreaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1, 1),
    _QtechOspfAreaLsaDBSumAreaId_Type()
)
qtechOspfAreaLsaDBSumAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumAreaId.setStatus("current")


class _QtechOspfAreaLsaDBSumLsaType_Type(Integer32):
    """Custom type qtechOspfAreaLsaDBSumLsaType based on Integer32"""
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


_QtechOspfAreaLsaDBSumLsaType_Type.__name__ = "Integer32"
_QtechOspfAreaLsaDBSumLsaType_Object = MibTableColumn
qtechOspfAreaLsaDBSumLsaType = _QtechOspfAreaLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1, 2),
    _QtechOspfAreaLsaDBSumLsaType_Type()
)
qtechOspfAreaLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumLsaType.setStatus("current")
_QtechOspfAreaLsaDBSumCounts_Type = Counter32
_QtechOspfAreaLsaDBSumCounts_Object = MibTableColumn
qtechOspfAreaLsaDBSumCounts = _QtechOspfAreaLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1, 3),
    _QtechOspfAreaLsaDBSumCounts_Type()
)
qtechOspfAreaLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumCounts.setStatus("current")
_QtechOspfAreaLsaDBSumDeletes_Type = Counter32
_QtechOspfAreaLsaDBSumDeletes_Object = MibTableColumn
qtechOspfAreaLsaDBSumDeletes = _QtechOspfAreaLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1, 4),
    _QtechOspfAreaLsaDBSumDeletes_Type()
)
qtechOspfAreaLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumDeletes.setStatus("current")
_QtechOspfAreaLsaDBSumMaxage_Type = Counter32
_QtechOspfAreaLsaDBSumMaxage_Object = MibTableColumn
qtechOspfAreaLsaDBSumMaxage = _QtechOspfAreaLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 5, 1, 5),
    _QtechOspfAreaLsaDBSumMaxage_Type()
)
qtechOspfAreaLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfAreaLsaDBSumMaxage.setStatus("current")
_QtechOspfLsaDBSumTable_Object = MibTable
qtechOspfLsaDBSumTable = _QtechOspfLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6)
)
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumTable.setStatus("current")
_QtechOspfLsaDBSumEntry_Object = MibTableRow
qtechOspfLsaDBSumEntry = _QtechOspfLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6, 1)
)
qtechOspfLsaDBSumEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumEntry.setStatus("current")


class _QtechOspfLsaDBSumLsaType_Type(Integer32):
    """Custom type qtechOspfLsaDBSumLsaType based on Integer32"""
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


_QtechOspfLsaDBSumLsaType_Type.__name__ = "Integer32"
_QtechOspfLsaDBSumLsaType_Object = MibTableColumn
qtechOspfLsaDBSumLsaType = _QtechOspfLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6, 1, 1),
    _QtechOspfLsaDBSumLsaType_Type()
)
qtechOspfLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumLsaType.setStatus("current")
_QtechOspfLsaDBSumCounts_Type = Counter32
_QtechOspfLsaDBSumCounts_Object = MibTableColumn
qtechOspfLsaDBSumCounts = _QtechOspfLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6, 1, 2),
    _QtechOspfLsaDBSumCounts_Type()
)
qtechOspfLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumCounts.setStatus("current")
_QtechOspfLsaDBSumDeletes_Type = Counter32
_QtechOspfLsaDBSumDeletes_Object = MibTableColumn
qtechOspfLsaDBSumDeletes = _QtechOspfLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6, 1, 3),
    _QtechOspfLsaDBSumDeletes_Type()
)
qtechOspfLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumDeletes.setStatus("current")
_QtechOspfLsaDBSumMaxage_Type = Counter32
_QtechOspfLsaDBSumMaxage_Object = MibTableColumn
qtechOspfLsaDBSumMaxage = _QtechOspfLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 8, 6, 1, 4),
    _QtechOspfLsaDBSumMaxage_Type()
)
qtechOspfLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfLsaDBSumMaxage.setStatus("current")
_QtechOspfNeighborTable_Object = MibTable
qtechOspfNeighborTable = _QtechOspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9)
)
if mibBuilder.loadTexts:
    qtechOspfNeighborTable.setStatus("current")
_QtechOspfNeighborEntry_Object = MibTableRow
qtechOspfNeighborEntry = _QtechOspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1)
)
qtechOspfNeighborEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfNbrIpAddr"),
    (0, "QTECH-OSPF-MIB", "qtechOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    qtechOspfNeighborEntry.setStatus("current")
_QtechOspfNbrIpAddr_Type = IpAddress
_QtechOspfNbrIpAddr_Object = MibTableColumn
qtechOspfNbrIpAddr = _QtechOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 1),
    _QtechOspfNbrIpAddr_Type()
)
qtechOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrIpAddr.setStatus("current")
_QtechOspfNbrAddressLessIndex_Type = Unsigned32
_QtechOspfNbrAddressLessIndex_Object = MibTableColumn
qtechOspfNbrAddressLessIndex = _QtechOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 2),
    _QtechOspfNbrAddressLessIndex_Type()
)
qtechOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrAddressLessIndex.setStatus("current")
_QtechOspfNbrRtrId_Type = RouterID
_QtechOspfNbrRtrId_Object = MibTableColumn
qtechOspfNbrRtrId = _QtechOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 3),
    _QtechOspfNbrRtrId_Type()
)
qtechOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrRtrId.setStatus("current")
_QtechOspfNbrOptions_Type = Unsigned32
_QtechOspfNbrOptions_Object = MibTableColumn
qtechOspfNbrOptions = _QtechOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 4),
    _QtechOspfNbrOptions_Type()
)
qtechOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrOptions.setStatus("current")
_QtechOspfNbrPriority_Type = DesignatedRouterPriority
_QtechOspfNbrPriority_Object = MibTableColumn
qtechOspfNbrPriority = _QtechOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 5),
    _QtechOspfNbrPriority_Type()
)
qtechOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrPriority.setStatus("current")


class _QtechOspfNbrState_Type(Integer32):
    """Custom type qtechOspfNbrState based on Integer32"""
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
          ("exchangeQtech", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_QtechOspfNbrState_Type.__name__ = "Integer32"
_QtechOspfNbrState_Object = MibTableColumn
qtechOspfNbrState = _QtechOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 6),
    _QtechOspfNbrState_Type()
)
qtechOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrState.setStatus("current")
_QtechOspfNbrEvents_Type = Counter32
_QtechOspfNbrEvents_Object = MibTableColumn
qtechOspfNbrEvents = _QtechOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 7),
    _QtechOspfNbrEvents_Type()
)
qtechOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrEvents.setStatus("current")
_QtechOspfNbrLsRetransQLen_Type = Gauge32
_QtechOspfNbrLsRetransQLen_Object = MibTableColumn
qtechOspfNbrLsRetransQLen = _QtechOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 8),
    _QtechOspfNbrLsRetransQLen_Type()
)
qtechOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrLsRetransQLen.setStatus("current")
_QtechOspfNbmaNbrStatus_Type = RowStatus
_QtechOspfNbmaNbrStatus_Object = MibTableColumn
qtechOspfNbmaNbrStatus = _QtechOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 9),
    _QtechOspfNbmaNbrStatus_Type()
)
qtechOspfNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbmaNbrStatus.setStatus("current")


class _QtechOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type qtechOspfNbmaNbrPermanence based on Integer32"""
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


_QtechOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_QtechOspfNbmaNbrPermanence_Object = MibTableColumn
qtechOspfNbmaNbrPermanence = _QtechOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 10),
    _QtechOspfNbmaNbrPermanence_Type()
)
qtechOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbmaNbrPermanence.setStatus("current")
_QtechOspfNbrHelloSuppressed_Type = TruthValue
_QtechOspfNbrHelloSuppressed_Object = MibTableColumn
qtechOspfNbrHelloSuppressed = _QtechOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 11),
    _QtechOspfNbrHelloSuppressed_Type()
)
qtechOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrHelloSuppressed.setStatus("current")
_QtechOspfNbrDeadTimeDueIn_Type = TimeTicks
_QtechOspfNbrDeadTimeDueIn_Object = MibTableColumn
qtechOspfNbrDeadTimeDueIn = _QtechOspfNbrDeadTimeDueIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 12),
    _QtechOspfNbrDeadTimeDueIn_Type()
)
qtechOspfNbrDeadTimeDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrDeadTimeDueIn.setStatus("current")
_QtechOspfNbrNeighborUpTime_Type = TimeTicks
_QtechOspfNbrNeighborUpTime_Object = MibTableColumn
qtechOspfNbrNeighborUpTime = _QtechOspfNbrNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 13),
    _QtechOspfNbrNeighborUpTime_Type()
)
qtechOspfNbrNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrNeighborUpTime.setStatus("current")
_QtechOspfNbrDR_Type = IpAddress
_QtechOspfNbrDR_Object = MibTableColumn
qtechOspfNbrDR = _QtechOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 14),
    _QtechOspfNbrDR_Type()
)
qtechOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrDR.setStatus("current")
_QtechOspfNbrBDR_Type = IpAddress
_QtechOspfNbrBDR_Object = MibTableColumn
qtechOspfNbrBDR = _QtechOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 15),
    _QtechOspfNbrBDR_Type()
)
qtechOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrBDR.setStatus("current")
_QtechOspfNbrArea_Type = IpAddress
_QtechOspfNbrArea_Object = MibTableColumn
qtechOspfNbrArea = _QtechOspfNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 16),
    _QtechOspfNbrArea_Type()
)
qtechOspfNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrArea.setStatus("current")
_QtechOspfNbrRetransmissionNum_Type = Counter32
_QtechOspfNbrRetransmissionNum_Object = MibTableColumn
qtechOspfNbrRetransmissionNum = _QtechOspfNbrRetransmissionNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 17),
    _QtechOspfNbrRetransmissionNum_Type()
)
qtechOspfNbrRetransmissionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrRetransmissionNum.setStatus("current")


class _QtechOspfNbrIfState_Type(Integer32):
    """Custom type qtechOspfNbrIfState based on Integer32"""
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


_QtechOspfNbrIfState_Type.__name__ = "Integer32"
_QtechOspfNbrIfState_Object = MibTableColumn
qtechOspfNbrIfState = _QtechOspfNbrIfState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 9, 1, 18),
    _QtechOspfNbrIfState_Type()
)
qtechOspfNbrIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfNbrIfState.setStatus("current")
_QtechOspfRouteTable_Object = MibTable
qtechOspfRouteTable = _QtechOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10)
)
if mibBuilder.loadTexts:
    qtechOspfRouteTable.setStatus("current")
_QtechOspfRouteEntry_Object = MibTableRow
qtechOspfRouteEntry = _QtechOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1)
)
qtechOspfRouteEntry.setIndexNames(
    (0, "QTECH-OSPF-MIB", "qtechOspfRouteDest"),
    (0, "QTECH-OSPF-MIB", "qtechOspfRouteArea"),
    (0, "QTECH-OSPF-MIB", "qtechOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    qtechOspfRouteEntry.setStatus("current")
_QtechOspfRouteDest_Type = IpAddress
_QtechOspfRouteDest_Object = MibTableColumn
qtechOspfRouteDest = _QtechOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 1),
    _QtechOspfRouteDest_Type()
)
qtechOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteDest.setStatus("current")
_QtechOspfRouteArea_Type = IpAddress
_QtechOspfRouteArea_Object = MibTableColumn
qtechOspfRouteArea = _QtechOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 2),
    _QtechOspfRouteArea_Type()
)
qtechOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteArea.setStatus("current")
_QtechOspfRouteNextHop_Type = IpAddress
_QtechOspfRouteNextHop_Object = MibTableColumn
qtechOspfRouteNextHop = _QtechOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 3),
    _QtechOspfRouteNextHop_Type()
)
qtechOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteNextHop.setStatus("current")
_QtechOspfRouteCost_Type = Unsigned32
_QtechOspfRouteCost_Object = MibTableColumn
qtechOspfRouteCost = _QtechOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 4),
    _QtechOspfRouteCost_Type()
)
qtechOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteCost.setStatus("current")


class _QtechOspfRouteDRType_Type(Integer32):
    """Custom type qtechOspfRouteDRType based on Integer32"""
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


_QtechOspfRouteDRType_Type.__name__ = "Integer32"
_QtechOspfRouteDRType_Object = MibTableColumn
qtechOspfRouteDRType = _QtechOspfRouteDRType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 5),
    _QtechOspfRouteDRType_Type()
)
qtechOspfRouteDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteDRType.setStatus("current")


class _QtechOspfRouteType_Type(Integer32):
    """Custom type qtechOspfRouteType based on Integer32"""
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


_QtechOspfRouteType_Type.__name__ = "Integer32"
_QtechOspfRouteType_Object = MibTableColumn
qtechOspfRouteType = _QtechOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 6),
    _QtechOspfRouteType_Type()
)
qtechOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteType.setStatus("current")
_QtechOspfRouteSpfNo_Type = Counter32
_QtechOspfRouteSpfNo_Object = MibTableColumn
qtechOspfRouteSpfNo = _QtechOspfRouteSpfNo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 1, 10, 1, 7),
    _QtechOspfRouteSpfNo_Type()
)
qtechOspfRouteSpfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOspfRouteSpfNo.setStatus("current")
_QtechOspfMIBConformance_ObjectIdentity = ObjectIdentity
qtechOspfMIBConformance = _QtechOspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2)
)
_QtechOspfMIBCompliances_ObjectIdentity = ObjectIdentity
qtechOspfMIBCompliances = _QtechOspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 1)
)
_QtechOspfMIBGroups_ObjectIdentity = ObjectIdentity
qtechOspfMIBGroups = _QtechOspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2)
)
_OspfMIBConformance_ObjectIdentity = ObjectIdentity
ospfMIBConformance = _OspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 3)
)
_OspfMIBCompliances_ObjectIdentity = ObjectIdentity
ospfMIBCompliances = _OspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 3, 1)
)

# Managed Objects groups

qtechOspfBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 1)
)
qtechOspfBaseMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfMiniLsaInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfMiniLsaArrival"),
        ("QTECH-OSPF-MIB", "qtechOspfAreasNum"),
        ("QTECH-OSPF-MIB", "qtechOspfNormalAreasNum"),
        ("QTECH-OSPF-MIB", "qtechOspfStubAreasNum"),
        ("QTECH-OSPF-MIB", "qtechOspfNssaAreasNum"),
        ("QTECH-OSPF-MIB", "qtechOspfSpfDelay"),
        ("QTECH-OSPF-MIB", "qtechOspfSpfHoldTime"),
        ("QTECH-OSPF-MIB", "qtechOspfAutoCostRefBandWidthRef"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaGroupPacing"),
        ("QTECH-OSPF-MIB", "qtechOspfInterDistance"),
        ("QTECH-OSPF-MIB", "qtechOspfIntraDistance"),
        ("QTECH-OSPF-MIB", "qtechOspfExternDistance"),
        ("QTECH-OSPF-MIB", "qtechOspfLogAdjChangeNotify"),
        ("QTECH-OSPF-MIB", "qtechOspfPassiveStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfRFC1583Compatibility"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteRedisDefMetricVal"))
)
if mibBuilder.loadTexts:
    qtechOspfBaseMIBGroup.setStatus("current")

qtechOspfAreaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 2)
)
qtechOspfAreaMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfAuthType"),
        ("QTECH-OSPF-MIB", "qtechOspfImportAsExtern"),
        ("QTECH-OSPF-MIB", "qtechOspfSpfRuns"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaBdrRtrCount"),
        ("QTECH-OSPF-MIB", "qtechOspfAsBdrRtrCount"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaCount"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaCksumSum"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaSummary"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaInterfaceNum"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaNssaIsRedistribution"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaNssaIsDefInfoOriginate"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkAreaID"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkAddress"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkMask"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkStatus"))
)
if mibBuilder.loadTexts:
    qtechOspfAreaMIBGroup.setStatus("current")

qtechOspfLsaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 3)
)
qtechOspfLsaMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfLsdbAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbType"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbLsid"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbRouterId"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbSequence"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbAge"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbChecksum"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbAdvertisement"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbLinkNum"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbPacketLength"),
        ("QTECH-OSPF-MIB", "qtechOspfSummaryLsaNetworkMask"),
        ("QTECH-OSPF-MIB", "qtechOspfSummaryLsaTos0Metric"),
        ("QTECH-OSPF-MIB", "qtechOspfNssaLsaDetailMetricType"),
        ("QTECH-OSPF-MIB", "qtechOspfNssaLsaDetailForwardAddr"),
        ("QTECH-OSPF-MIB", "qtechOspfNssaLsaDetailRouteTag"),
        ("QTECH-OSPF-MIB", "qtechOspfLsdbOption"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbType"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbLsid"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbRouterId"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbSequence"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbAge"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbChecksum"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbAdvertisement"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbNetworkMask"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbMetricType"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbForwardAddr"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbRouteTag"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbMetric"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbOption"),
        ("QTECH-OSPF-MIB", "qtechOspfExtLsdbPacketLength"),
        ("QTECH-OSPF-MIB", "qtechOspfRouterLsaDetailLinkID"),
        ("QTECH-OSPF-MIB", "qtechOspfRouterLsaDetailLinkType"),
        ("QTECH-OSPF-MIB", "qtechOspfRouterLsaDetailLinkData"),
        ("QTECH-OSPF-MIB", "qtechOspfRouterLsaDetailTos0Metric"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkLsaDetailAttachedRouter"),
        ("QTECH-OSPF-MIB", "qtechOspfNetWorkLsaDetailNetworkMask"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumLsaType"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumCounts"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumDeletes"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaLsaDBSumMaxage"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaDBSumLsaType"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaDBSumCounts"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaDBSumDeletes"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaDBSumMaxage"))
)
if mibBuilder.loadTexts:
    qtechOspfLsaMIBGroup.setStatus("current")

qtechOspfIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 4)
)
qtechOspfIfMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfIfIpAddress"),
        ("QTECH-OSPF-MIB", "qtechOspfAddressLessIf"),
        ("QTECH-OSPF-MIB", "qtechOspfIfAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfIfType"),
        ("QTECH-OSPF-MIB", "qtechOspfIfAdminStat"),
        ("QTECH-OSPF-MIB", "qtechOspfIfRtrPriority"),
        ("QTECH-OSPF-MIB", "qtechOspfIfTransitDelay"),
        ("QTECH-OSPF-MIB", "qtechOspfIfRetransInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfIfHelloInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfIfRtrDeadInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfIfPollInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfIfState"),
        ("QTECH-OSPF-MIB", "qtechOspfIfDesignatedRouter"),
        ("QTECH-OSPF-MIB", "qtechOspfIfBackupDesignatedRouter"),
        ("QTECH-OSPF-MIB", "qtechOspfIfEvents"),
        ("QTECH-OSPF-MIB", "qtechOspfIfAuthType"),
        ("QTECH-OSPF-MIB", "qtechOspfIfAuthKey"),
        ("QTECH-OSPF-MIB", "qtechOspfIfStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMulticastForwarding"),
        ("QTECH-OSPF-MIB", "qtechOspfIfDemand"),
        ("QTECH-OSPF-MIB", "qtechOspfIfDatabaseFilterAllOut"),
        ("QTECH-OSPF-MIB", "qtechOspfIfDesignateRouterId"),
        ("QTECH-OSPF-MIB", "qtechOspfIfBackupDesignateRouterId"),
        ("QTECH-OSPF-MIB", "qtechOspfIfWaitInternal"),
        ("QTECH-OSPF-MIB", "qtechOspfIfPassiveStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfIfCurrentUsedMd5AuthKeyId"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKeyIf"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKeyId"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKey"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMd5AuthKeySt"))
)
if mibBuilder.loadTexts:
    qtechOspfIfMIBGroup.setStatus("current")

qtechOspfVirtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 5)
)
qtechOspfVirtMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfVirtIfAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfNeighbor"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfTransitDelay"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfRetransInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfHelloInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfRtrDeadInterval"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfState"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfEvents"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfAuthType"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfAuthKey"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtCost"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtNativeIfIndex"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtLinkState"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtHelloDueIn"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyAreaId"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyNeighbor"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeyId"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKey"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtIfMd5AuthKeySt"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtCurrentUsedMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    qtechOspfVirtMIBGroup.setStatus("current")

qtechOspfNeighborMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 6)
)
qtechOspfNeighborMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfNbrIpAddr"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrAddressLessIndex"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrRtrId"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrOptions"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrPriority"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrState"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrEvents"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrLsRetransQLen"),
        ("QTECH-OSPF-MIB", "qtechOspfNbmaNbrStatus"),
        ("QTECH-OSPF-MIB", "qtechOspfNbmaNbrPermanence"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrHelloSuppressed"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrDeadTimeDueIn"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrNeighborUpTime"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrDR"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrBDR"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrArea"),
        ("QTECH-OSPF-MIB", "qtechOspfNbrRetransmissionNum"))
)
if mibBuilder.loadTexts:
    qtechOspfNeighborMIBGroup.setStatus("current")

qtechOspfRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 2, 7)
)
qtechOspfRouteInfoMIBGroup.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfRouteType"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteDest"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteNextHop"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteCost"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteDRType"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteArea"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteSpfNo"))
)
if mibBuilder.loadTexts:
    qtechOspfRouteInfoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechOspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 2, 1, 1)
)
qtechOspfMIBCompliance.setObjects(
      *(("QTECH-OSPF-MIB", "qtechOspfBaseMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfAreaMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfLsaMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfIfMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfVirtMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfNeighborMIBGroup"),
        ("QTECH-OSPF-MIB", "qtechOspfRouteInfoMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechOspfMIBCompliance.setStatus(
        "current"
    )

ospfExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ospfExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-OSPF-MIB",
    **{"qtechOspfMIB": qtechOspfMIB,
       "qtechOspfMIBObjects": qtechOspfMIBObjects,
       "qtechOspfGeneralMibsGroup": qtechOspfGeneralMibsGroup,
       "qtechOspfMiniLsaInterval": qtechOspfMiniLsaInterval,
       "qtechOspfMiniLsaArrival": qtechOspfMiniLsaArrival,
       "qtechOspfAreasNum": qtechOspfAreasNum,
       "qtechOspfNormalAreasNum": qtechOspfNormalAreasNum,
       "qtechOspfStubAreasNum": qtechOspfStubAreasNum,
       "qtechOspfNssaAreasNum": qtechOspfNssaAreasNum,
       "qtechOspfSpfDelay": qtechOspfSpfDelay,
       "qtechOspfSpfHoldTime": qtechOspfSpfHoldTime,
       "qtechOspfAutoCostRefBandWidthRef": qtechOspfAutoCostRefBandWidthRef,
       "qtechOspfLsaGroupPacing": qtechOspfLsaGroupPacing,
       "qtechOspfInterDistance": qtechOspfInterDistance,
       "qtechOspfIntraDistance": qtechOspfIntraDistance,
       "qtechOspfExternDistance": qtechOspfExternDistance,
       "qtechOspfLogAdjChangeNotify": qtechOspfLogAdjChangeNotify,
       "qtechOspfPassiveStatus": qtechOspfPassiveStatus,
       "qtechOspfRFC1583Compatibility": qtechOspfRFC1583Compatibility,
       "qtechOspfRouteRedisDefMetricVal": qtechOspfRouteRedisDefMetricVal,
       "qtechOspfAdminiDistance": qtechOspfAdminiDistance,
       "qtechOspfAreaTable": qtechOspfAreaTable,
       "qtechOspfAreaEntry": qtechOspfAreaEntry,
       "qtechOspfAreaId": qtechOspfAreaId,
       "qtechOspfAuthType": qtechOspfAuthType,
       "qtechOspfImportAsExtern": qtechOspfImportAsExtern,
       "qtechOspfSpfRuns": qtechOspfSpfRuns,
       "qtechOspfAreaBdrRtrCount": qtechOspfAreaBdrRtrCount,
       "qtechOspfAsBdrRtrCount": qtechOspfAsBdrRtrCount,
       "qtechOspfAreaLsaCount": qtechOspfAreaLsaCount,
       "qtechOspfAreaLsaCksumSum": qtechOspfAreaLsaCksumSum,
       "qtechOspfAreaSummary": qtechOspfAreaSummary,
       "qtechOspfAreaStatus": qtechOspfAreaStatus,
       "qtechOspfAreaInterfaceNum": qtechOspfAreaInterfaceNum,
       "qtechOspfAreaNssaIsRedistribution": qtechOspfAreaNssaIsRedistribution,
       "qtechOspfAreaNssaIsDefInfoOriginate": qtechOspfAreaNssaIsDefInfoOriginate,
       "qtechOspfAddressScopeTable": qtechOspfAddressScopeTable,
       "qtechOspfAddressScopeEntry": qtechOspfAddressScopeEntry,
       "qtechOspfNetWorkAreaID": qtechOspfNetWorkAreaID,
       "qtechOspfNetWorkAddress": qtechOspfNetWorkAddress,
       "qtechOspfNetWorkMask": qtechOspfNetWorkMask,
       "qtechOspfNetWorkStatus": qtechOspfNetWorkStatus,
       "qtechOspfIfTable": qtechOspfIfTable,
       "qtechOspfIfEntry": qtechOspfIfEntry,
       "qtechOspfIfIpAddress": qtechOspfIfIpAddress,
       "qtechOspfAddressLessIf": qtechOspfAddressLessIf,
       "qtechOspfIfAreaId": qtechOspfIfAreaId,
       "qtechOspfIfType": qtechOspfIfType,
       "qtechOspfIfAdminStat": qtechOspfIfAdminStat,
       "qtechOspfIfRtrPriority": qtechOspfIfRtrPriority,
       "qtechOspfIfTransitDelay": qtechOspfIfTransitDelay,
       "qtechOspfIfRetransInterval": qtechOspfIfRetransInterval,
       "qtechOspfIfHelloInterval": qtechOspfIfHelloInterval,
       "qtechOspfIfRtrDeadInterval": qtechOspfIfRtrDeadInterval,
       "qtechOspfIfPollInterval": qtechOspfIfPollInterval,
       "qtechOspfIfState": qtechOspfIfState,
       "qtechOspfIfDesignatedRouter": qtechOspfIfDesignatedRouter,
       "qtechOspfIfBackupDesignatedRouter": qtechOspfIfBackupDesignatedRouter,
       "qtechOspfIfEvents": qtechOspfIfEvents,
       "qtechOspfIfAuthKey": qtechOspfIfAuthKey,
       "qtechOspfIfStatus": qtechOspfIfStatus,
       "qtechOspfIfMulticastForwarding": qtechOspfIfMulticastForwarding,
       "qtechOspfIfDemand": qtechOspfIfDemand,
       "qtechOspfIfAuthType": qtechOspfIfAuthType,
       "qtechOspfIfDatabaseFilterAllOut": qtechOspfIfDatabaseFilterAllOut,
       "qtechOspfIfDesignateRouterId": qtechOspfIfDesignateRouterId,
       "qtechOspfIfBackupDesignateRouterId": qtechOspfIfBackupDesignateRouterId,
       "qtechOspfIfWaitInternal": qtechOspfIfWaitInternal,
       "qtechOspfIfPassiveStatus": qtechOspfIfPassiveStatus,
       "qtechOspfIfCurrentUsedMd5AuthKeyId": qtechOspfIfCurrentUsedMd5AuthKeyId,
       "qtechOspfIfMd5AuthKeyTable": qtechOspfIfMd5AuthKeyTable,
       "qtechOspfIfMd5AuthKeyEntry": qtechOspfIfMd5AuthKeyEntry,
       "qtechOspfIfMd5AuthKeyIf": qtechOspfIfMd5AuthKeyIf,
       "qtechOspfIfMd5AuthKeyId": qtechOspfIfMd5AuthKeyId,
       "qtechOspfIfMd5AuthKey": qtechOspfIfMd5AuthKey,
       "qtechOspfIfMd5AuthKeySt": qtechOspfIfMd5AuthKeySt,
       "qtechOspfVirtTable": qtechOspfVirtTable,
       "qtechOspfVirtEntry": qtechOspfVirtEntry,
       "qtechOspfVirtIfAreaId": qtechOspfVirtIfAreaId,
       "qtechOspfVirtIfNeighbor": qtechOspfVirtIfNeighbor,
       "qtechOspfVirtIfTransitDelay": qtechOspfVirtIfTransitDelay,
       "qtechOspfVirtIfRetransInterval": qtechOspfVirtIfRetransInterval,
       "qtechOspfVirtIfHelloInterval": qtechOspfVirtIfHelloInterval,
       "qtechOspfVirtIfRtrDeadInterval": qtechOspfVirtIfRtrDeadInterval,
       "qtechOspfVirtIfState": qtechOspfVirtIfState,
       "qtechOspfVirtIfEvents": qtechOspfVirtIfEvents,
       "qtechOspfVirtIfAuthKey": qtechOspfVirtIfAuthKey,
       "qtechOspfVirtIfStatus": qtechOspfVirtIfStatus,
       "qtechOspfVirtIfAuthType": qtechOspfVirtIfAuthType,
       "qtechOspfVirtCost": qtechOspfVirtCost,
       "qtechOspfVirtNativeIfIndex": qtechOspfVirtNativeIfIndex,
       "qtechOspfVirtLinkState": qtechOspfVirtLinkState,
       "qtechOspfVirtHelloDueIn": qtechOspfVirtHelloDueIn,
       "qtechOspfVirtCurrentUsedMd5AuthKeyId": qtechOspfVirtCurrentUsedMd5AuthKeyId,
       "qtechOspfVirtIfMd5AuthKeyTable": qtechOspfVirtIfMd5AuthKeyTable,
       "qtechOspfVirtIfMd5AuthKeyEntry": qtechOspfVirtIfMd5AuthKeyEntry,
       "qtechOspfVirtIfMd5AuthKeyAreaId": qtechOspfVirtIfMd5AuthKeyAreaId,
       "qtechOspfVirtIfMd5AuthKeyNeighbor": qtechOspfVirtIfMd5AuthKeyNeighbor,
       "qtechOspfVirtIfMd5AuthKeyId": qtechOspfVirtIfMd5AuthKeyId,
       "qtechOspfVirtIfMd5AuthKey": qtechOspfVirtIfMd5AuthKey,
       "qtechOspfVirtIfMd5AuthKeySt": qtechOspfVirtIfMd5AuthKeySt,
       "qtechOspfLsaDetailInfoMibsGroup": qtechOspfLsaDetailInfoMibsGroup,
       "qtechOspfLsdbTable": qtechOspfLsdbTable,
       "qtechOspfLsdbEntry": qtechOspfLsdbEntry,
       "qtechOspfLsdbAreaId": qtechOspfLsdbAreaId,
       "qtechOspfLsdbType": qtechOspfLsdbType,
       "qtechOspfLsdbLsid": qtechOspfLsdbLsid,
       "qtechOspfLsdbRouterId": qtechOspfLsdbRouterId,
       "qtechOspfLsdbSequence": qtechOspfLsdbSequence,
       "qtechOspfLsdbAge": qtechOspfLsdbAge,
       "qtechOspfLsdbChecksum": qtechOspfLsdbChecksum,
       "qtechOspfLsdbAdvertisement": qtechOspfLsdbAdvertisement,
       "qtechOspfLsdbLinkNum": qtechOspfLsdbLinkNum,
       "qtechOspfLsdbPacketLength": qtechOspfLsdbPacketLength,
       "qtechOspfSummaryLsaNetworkMask": qtechOspfSummaryLsaNetworkMask,
       "qtechOspfSummaryLsaTos0Metric": qtechOspfSummaryLsaTos0Metric,
       "qtechOspfNssaLsaDetailMetricType": qtechOspfNssaLsaDetailMetricType,
       "qtechOspfNssaLsaDetailForwardAddr": qtechOspfNssaLsaDetailForwardAddr,
       "qtechOspfNssaLsaDetailRouteTag": qtechOspfNssaLsaDetailRouteTag,
       "qtechOspfLsdbOption": qtechOspfLsdbOption,
       "qtechOspfExtLsdbTable": qtechOspfExtLsdbTable,
       "qtechOspfExtLsdbEntry": qtechOspfExtLsdbEntry,
       "qtechOspfExtLsdbType": qtechOspfExtLsdbType,
       "qtechOspfExtLsdbLsid": qtechOspfExtLsdbLsid,
       "qtechOspfExtLsdbRouterId": qtechOspfExtLsdbRouterId,
       "qtechOspfExtLsdbSequence": qtechOspfExtLsdbSequence,
       "qtechOspfExtLsdbAge": qtechOspfExtLsdbAge,
       "qtechOspfExtLsdbChecksum": qtechOspfExtLsdbChecksum,
       "qtechOspfExtLsdbAdvertisement": qtechOspfExtLsdbAdvertisement,
       "qtechOspfExtLsdbNetworkMask": qtechOspfExtLsdbNetworkMask,
       "qtechOspfExtLsdbMetric": qtechOspfExtLsdbMetric,
       "qtechOspfExtLsdbMetricType": qtechOspfExtLsdbMetricType,
       "qtechOspfExtLsdbForwardAddr": qtechOspfExtLsdbForwardAddr,
       "qtechOspfExtLsdbRouteTag": qtechOspfExtLsdbRouteTag,
       "qtechOspfExtLsdbOption": qtechOspfExtLsdbOption,
       "qtechOspfExtLsdbPacketLength": qtechOspfExtLsdbPacketLength,
       "qtechOspfRouterLsaDetailTable": qtechOspfRouterLsaDetailTable,
       "qtechOspfRouterLsaDetailEntry": qtechOspfRouterLsaDetailEntry,
       "qtechOspfRouterLsaDetailLinkID": qtechOspfRouterLsaDetailLinkID,
       "qtechOspfRouterLsaDetailLinkType": qtechOspfRouterLsaDetailLinkType,
       "qtechOspfRouterLsaDetailLinkData": qtechOspfRouterLsaDetailLinkData,
       "qtechOspfRouterLsaDetailTos0Metric": qtechOspfRouterLsaDetailTos0Metric,
       "qtechOspfNetWorkLsaDetailTable": qtechOspfNetWorkLsaDetailTable,
       "qtechOspfNetWorkLsaDetailEntry": qtechOspfNetWorkLsaDetailEntry,
       "qtechOspfNetWorkLsaDetailAttachedRouter": qtechOspfNetWorkLsaDetailAttachedRouter,
       "qtechOspfNetWorkLsaDetailNetworkMask": qtechOspfNetWorkLsaDetailNetworkMask,
       "qtechOspfAreaLsaDBSumTable": qtechOspfAreaLsaDBSumTable,
       "qtechOspfAreaLsaDBSumEntry": qtechOspfAreaLsaDBSumEntry,
       "qtechOspfAreaLsaDBSumAreaId": qtechOspfAreaLsaDBSumAreaId,
       "qtechOspfAreaLsaDBSumLsaType": qtechOspfAreaLsaDBSumLsaType,
       "qtechOspfAreaLsaDBSumCounts": qtechOspfAreaLsaDBSumCounts,
       "qtechOspfAreaLsaDBSumDeletes": qtechOspfAreaLsaDBSumDeletes,
       "qtechOspfAreaLsaDBSumMaxage": qtechOspfAreaLsaDBSumMaxage,
       "qtechOspfLsaDBSumTable": qtechOspfLsaDBSumTable,
       "qtechOspfLsaDBSumEntry": qtechOspfLsaDBSumEntry,
       "qtechOspfLsaDBSumLsaType": qtechOspfLsaDBSumLsaType,
       "qtechOspfLsaDBSumCounts": qtechOspfLsaDBSumCounts,
       "qtechOspfLsaDBSumDeletes": qtechOspfLsaDBSumDeletes,
       "qtechOspfLsaDBSumMaxage": qtechOspfLsaDBSumMaxage,
       "qtechOspfNeighborTable": qtechOspfNeighborTable,
       "qtechOspfNeighborEntry": qtechOspfNeighborEntry,
       "qtechOspfNbrIpAddr": qtechOspfNbrIpAddr,
       "qtechOspfNbrAddressLessIndex": qtechOspfNbrAddressLessIndex,
       "qtechOspfNbrRtrId": qtechOspfNbrRtrId,
       "qtechOspfNbrOptions": qtechOspfNbrOptions,
       "qtechOspfNbrPriority": qtechOspfNbrPriority,
       "qtechOspfNbrState": qtechOspfNbrState,
       "qtechOspfNbrEvents": qtechOspfNbrEvents,
       "qtechOspfNbrLsRetransQLen": qtechOspfNbrLsRetransQLen,
       "qtechOspfNbmaNbrStatus": qtechOspfNbmaNbrStatus,
       "qtechOspfNbmaNbrPermanence": qtechOspfNbmaNbrPermanence,
       "qtechOspfNbrHelloSuppressed": qtechOspfNbrHelloSuppressed,
       "qtechOspfNbrDeadTimeDueIn": qtechOspfNbrDeadTimeDueIn,
       "qtechOspfNbrNeighborUpTime": qtechOspfNbrNeighborUpTime,
       "qtechOspfNbrDR": qtechOspfNbrDR,
       "qtechOspfNbrBDR": qtechOspfNbrBDR,
       "qtechOspfNbrArea": qtechOspfNbrArea,
       "qtechOspfNbrRetransmissionNum": qtechOspfNbrRetransmissionNum,
       "qtechOspfNbrIfState": qtechOspfNbrIfState,
       "qtechOspfRouteTable": qtechOspfRouteTable,
       "qtechOspfRouteEntry": qtechOspfRouteEntry,
       "qtechOspfRouteDest": qtechOspfRouteDest,
       "qtechOspfRouteArea": qtechOspfRouteArea,
       "qtechOspfRouteNextHop": qtechOspfRouteNextHop,
       "qtechOspfRouteCost": qtechOspfRouteCost,
       "qtechOspfRouteDRType": qtechOspfRouteDRType,
       "qtechOspfRouteType": qtechOspfRouteType,
       "qtechOspfRouteSpfNo": qtechOspfRouteSpfNo,
       "qtechOspfMIBConformance": qtechOspfMIBConformance,
       "qtechOspfMIBCompliances": qtechOspfMIBCompliances,
       "qtechOspfMIBCompliance": qtechOspfMIBCompliance,
       "qtechOspfMIBGroups": qtechOspfMIBGroups,
       "qtechOspfBaseMIBGroup": qtechOspfBaseMIBGroup,
       "qtechOspfAreaMIBGroup": qtechOspfAreaMIBGroup,
       "qtechOspfLsaMIBGroup": qtechOspfLsaMIBGroup,
       "qtechOspfIfMIBGroup": qtechOspfIfMIBGroup,
       "qtechOspfVirtMIBGroup": qtechOspfVirtMIBGroup,
       "qtechOspfNeighborMIBGroup": qtechOspfNeighborMIBGroup,
       "qtechOspfRouteInfoMIBGroup": qtechOspfRouteInfoMIBGroup,
       "ospfMIBConformance": ospfMIBConformance,
       "ospfMIBCompliances": ospfMIBCompliances,
       "ospfExternCompliance": ospfExternCompliance}
)
