# SNMP MIB module (DES7200-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:01 2025
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
    "DES7200-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 PositiveInteger,
 RouterID,
 Status,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "PositiveInteger",
    "RouterID",
    "Status",
    "UpToMaxAge")

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

myOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30)
)
if mibBuilder.loadTexts:
    myOspfMIB.setRevisions(
        ("2002-11-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyOspfMIBObjects_ObjectIdentity = ObjectIdentity
myOspfMIBObjects = _MyOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1)
)
_MyOspfGeneralMibsGroup_ObjectIdentity = ObjectIdentity
myOspfGeneralMibsGroup = _MyOspfGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1)
)
_MyOspfMiniLsaInterval_Type = Unsigned32
_MyOspfMiniLsaInterval_Object = MibScalar
myOspfMiniLsaInterval = _MyOspfMiniLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 1),
    _MyOspfMiniLsaInterval_Type()
)
myOspfMiniLsaInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfMiniLsaInterval.setStatus("current")
_MyOspfMiniLsaArrival_Type = Unsigned32
_MyOspfMiniLsaArrival_Object = MibScalar
myOspfMiniLsaArrival = _MyOspfMiniLsaArrival_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 2),
    _MyOspfMiniLsaArrival_Type()
)
myOspfMiniLsaArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfMiniLsaArrival.setStatus("current")
_MyOspfAreasNum_Type = Unsigned32
_MyOspfAreasNum_Object = MibScalar
myOspfAreasNum = _MyOspfAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 3),
    _MyOspfAreasNum_Type()
)
myOspfAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreasNum.setStatus("current")
_MyOspfNormalAreasNum_Type = Unsigned32
_MyOspfNormalAreasNum_Object = MibScalar
myOspfNormalAreasNum = _MyOspfNormalAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 4),
    _MyOspfNormalAreasNum_Type()
)
myOspfNormalAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNormalAreasNum.setStatus("current")
_MyOspfStubAreasNum_Type = Unsigned32
_MyOspfStubAreasNum_Object = MibScalar
myOspfStubAreasNum = _MyOspfStubAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 5),
    _MyOspfStubAreasNum_Type()
)
myOspfStubAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfStubAreasNum.setStatus("current")
_MyOspfNssaAreasNum_Type = Unsigned32
_MyOspfNssaAreasNum_Object = MibScalar
myOspfNssaAreasNum = _MyOspfNssaAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 6),
    _MyOspfNssaAreasNum_Type()
)
myOspfNssaAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNssaAreasNum.setStatus("current")


class _MyOspfSpfDelay_Type(Unsigned32):
    """Custom type myOspfSpfDelay based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyOspfSpfDelay_Type.__name__ = "Unsigned32"
_MyOspfSpfDelay_Object = MibScalar
myOspfSpfDelay = _MyOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 7),
    _MyOspfSpfDelay_Type()
)
myOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfSpfDelay.setStatus("current")


class _MyOspfSpfHoldTime_Type(Unsigned32):
    """Custom type myOspfSpfHoldTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyOspfSpfHoldTime_Type.__name__ = "Unsigned32"
_MyOspfSpfHoldTime_Object = MibScalar
myOspfSpfHoldTime = _MyOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 8),
    _MyOspfSpfHoldTime_Type()
)
myOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfSpfHoldTime.setStatus("current")


class _MyOspfAutoCostRefBandWidthRef_Type(Unsigned32):
    """Custom type myOspfAutoCostRefBandWidthRef based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyOspfAutoCostRefBandWidthRef_Type.__name__ = "Unsigned32"
_MyOspfAutoCostRefBandWidthRef_Object = MibScalar
myOspfAutoCostRefBandWidthRef = _MyOspfAutoCostRefBandWidthRef_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 9),
    _MyOspfAutoCostRefBandWidthRef_Type()
)
myOspfAutoCostRefBandWidthRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfAutoCostRefBandWidthRef.setStatus("current")


class _MyOspfLsaGroupPacing_Type(Unsigned32):
    """Custom type myOspfLsaGroupPacing based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_MyOspfLsaGroupPacing_Type.__name__ = "Unsigned32"
_MyOspfLsaGroupPacing_Object = MibScalar
myOspfLsaGroupPacing = _MyOspfLsaGroupPacing_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 10),
    _MyOspfLsaGroupPacing_Type()
)
myOspfLsaGroupPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfLsaGroupPacing.setStatus("current")


class _MyOspfInterDistance_Type(Unsigned32):
    """Custom type myOspfInterDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfInterDistance_Type.__name__ = "Unsigned32"
_MyOspfInterDistance_Object = MibScalar
myOspfInterDistance = _MyOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 11),
    _MyOspfInterDistance_Type()
)
myOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfInterDistance.setStatus("current")


class _MyOspfIntraDistance_Type(Unsigned32):
    """Custom type myOspfIntraDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfIntraDistance_Type.__name__ = "Unsigned32"
_MyOspfIntraDistance_Object = MibScalar
myOspfIntraDistance = _MyOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 12),
    _MyOspfIntraDistance_Type()
)
myOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIntraDistance.setStatus("current")


class _MyOspfExternDistance_Type(Unsigned32):
    """Custom type myOspfExternDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfExternDistance_Type.__name__ = "Unsigned32"
_MyOspfExternDistance_Object = MibScalar
myOspfExternDistance = _MyOspfExternDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 13),
    _MyOspfExternDistance_Type()
)
myOspfExternDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfExternDistance.setStatus("current")


class _MyOspfLogAdjChangeNotify_Type(EnabledStatus):
    """Custom type myOspfLogAdjChangeNotify based on EnabledStatus"""
    defaultValue = 1


_MyOspfLogAdjChangeNotify_Type.__name__ = "EnabledStatus"
_MyOspfLogAdjChangeNotify_Object = MibScalar
myOspfLogAdjChangeNotify = _MyOspfLogAdjChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 14),
    _MyOspfLogAdjChangeNotify_Type()
)
myOspfLogAdjChangeNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfLogAdjChangeNotify.setStatus("current")


class _MyOspfPassiveStatus_Type(EnabledStatus):
    """Custom type myOspfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_MyOspfPassiveStatus_Type.__name__ = "EnabledStatus"
_MyOspfPassiveStatus_Object = MibScalar
myOspfPassiveStatus = _MyOspfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 15),
    _MyOspfPassiveStatus_Type()
)
myOspfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfPassiveStatus.setStatus("current")


class _MyOspfRFC1583Compatibility_Type(EnabledStatus):
    """Custom type myOspfRFC1583Compatibility based on EnabledStatus"""
    defaultValue = 1


_MyOspfRFC1583Compatibility_Type.__name__ = "EnabledStatus"
_MyOspfRFC1583Compatibility_Object = MibScalar
myOspfRFC1583Compatibility = _MyOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 16),
    _MyOspfRFC1583Compatibility_Type()
)
myOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfRFC1583Compatibility.setStatus("current")


class _MyOspfRouteRedisDefMetricVal_Type(Unsigned32):
    """Custom type myOspfRouteRedisDefMetricVal based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_MyOspfRouteRedisDefMetricVal_Type.__name__ = "Unsigned32"
_MyOspfRouteRedisDefMetricVal_Object = MibScalar
myOspfRouteRedisDefMetricVal = _MyOspfRouteRedisDefMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 17),
    _MyOspfRouteRedisDefMetricVal_Type()
)
myOspfRouteRedisDefMetricVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfRouteRedisDefMetricVal.setStatus("current")


class _MyOspfAdminiDistance_Type(Unsigned32):
    """Custom type myOspfAdminiDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfAdminiDistance_Type.__name__ = "Unsigned32"
_MyOspfAdminiDistance_Object = MibScalar
myOspfAdminiDistance = _MyOspfAdminiDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 1, 18),
    _MyOspfAdminiDistance_Type()
)
myOspfAdminiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfAdminiDistance.setStatus("current")
_MyOspfAreaTable_Object = MibTable
myOspfAreaTable = _MyOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    myOspfAreaTable.setStatus("current")
_MyOspfAreaEntry_Object = MibTableRow
myOspfAreaEntry = _MyOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1)
)
myOspfAreaEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfAreaId"),
)
if mibBuilder.loadTexts:
    myOspfAreaEntry.setStatus("current")
_MyOspfAreaId_Type = AreaID
_MyOspfAreaId_Object = MibTableColumn
myOspfAreaId = _MyOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 1),
    _MyOspfAreaId_Type()
)
myOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaId.setStatus("current")


class _MyOspfAuthType_Type(Integer32):
    """Custom type myOspfAuthType based on Integer32"""
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


_MyOspfAuthType_Type.__name__ = "Integer32"
_MyOspfAuthType_Object = MibTableColumn
myOspfAuthType = _MyOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 2),
    _MyOspfAuthType_Type()
)
myOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfAuthType.setStatus("current")


class _MyOspfImportAsExtern_Type(Integer32):
    """Custom type myOspfImportAsExtern based on Integer32"""
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


_MyOspfImportAsExtern_Type.__name__ = "Integer32"
_MyOspfImportAsExtern_Object = MibTableColumn
myOspfImportAsExtern = _MyOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 3),
    _MyOspfImportAsExtern_Type()
)
myOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfImportAsExtern.setStatus("current")
_MyOspfSpfRuns_Type = Counter32
_MyOspfSpfRuns_Object = MibTableColumn
myOspfSpfRuns = _MyOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 4),
    _MyOspfSpfRuns_Type()
)
myOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfSpfRuns.setStatus("current")
_MyOspfAreaBdrRtrCount_Type = Gauge32
_MyOspfAreaBdrRtrCount_Object = MibTableColumn
myOspfAreaBdrRtrCount = _MyOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 5),
    _MyOspfAreaBdrRtrCount_Type()
)
myOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaBdrRtrCount.setStatus("current")
_MyOspfAsBdrRtrCount_Type = Gauge32
_MyOspfAsBdrRtrCount_Object = MibTableColumn
myOspfAsBdrRtrCount = _MyOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 6),
    _MyOspfAsBdrRtrCount_Type()
)
myOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAsBdrRtrCount.setStatus("current")
_MyOspfAreaLsaCount_Type = Gauge32
_MyOspfAreaLsaCount_Object = MibTableColumn
myOspfAreaLsaCount = _MyOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 7),
    _MyOspfAreaLsaCount_Type()
)
myOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaCount.setStatus("current")


class _MyOspfAreaLsaCksumSum_Type(Unsigned32):
    """Custom type myOspfAreaLsaCksumSum based on Unsigned32"""
    defaultValue = 0


_MyOspfAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_MyOspfAreaLsaCksumSum_Object = MibTableColumn
myOspfAreaLsaCksumSum = _MyOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 8),
    _MyOspfAreaLsaCksumSum_Type()
)
myOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaCksumSum.setStatus("current")


class _MyOspfAreaSummary_Type(Integer32):
    """Custom type myOspfAreaSummary based on Integer32"""
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


_MyOspfAreaSummary_Type.__name__ = "Integer32"
_MyOspfAreaSummary_Object = MibTableColumn
myOspfAreaSummary = _MyOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 9),
    _MyOspfAreaSummary_Type()
)
myOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfAreaSummary.setStatus("current")
_MyOspfAreaStatus_Type = RowStatus
_MyOspfAreaStatus_Object = MibTableColumn
myOspfAreaStatus = _MyOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 10),
    _MyOspfAreaStatus_Type()
)
myOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfAreaStatus.setStatus("current")
_MyOspfAreaInterfaceNum_Type = Unsigned32
_MyOspfAreaInterfaceNum_Object = MibTableColumn
myOspfAreaInterfaceNum = _MyOspfAreaInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 11),
    _MyOspfAreaInterfaceNum_Type()
)
myOspfAreaInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaInterfaceNum.setStatus("current")


class _MyOspfAreaNssaIsRedistribution_Type(TruthValue):
    """Custom type myOspfAreaNssaIsRedistribution based on TruthValue"""
    defaultValue = 1


_MyOspfAreaNssaIsRedistribution_Type.__name__ = "TruthValue"
_MyOspfAreaNssaIsRedistribution_Object = MibTableColumn
myOspfAreaNssaIsRedistribution = _MyOspfAreaNssaIsRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 12),
    _MyOspfAreaNssaIsRedistribution_Type()
)
myOspfAreaNssaIsRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfAreaNssaIsRedistribution.setStatus("current")


class _MyOspfAreaNssaIsDefInfoOriginate_Type(TruthValue):
    """Custom type myOspfAreaNssaIsDefInfoOriginate based on TruthValue"""
    defaultValue = 2


_MyOspfAreaNssaIsDefInfoOriginate_Type.__name__ = "TruthValue"
_MyOspfAreaNssaIsDefInfoOriginate_Object = MibTableColumn
myOspfAreaNssaIsDefInfoOriginate = _MyOspfAreaNssaIsDefInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 2, 1, 13),
    _MyOspfAreaNssaIsDefInfoOriginate_Type()
)
myOspfAreaNssaIsDefInfoOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfAreaNssaIsDefInfoOriginate.setStatus("current")
_MyOspfAddressScopeTable_Object = MibTable
myOspfAddressScopeTable = _MyOspfAddressScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    myOspfAddressScopeTable.setStatus("current")
_MyOspfAddressScopeEntry_Object = MibTableRow
myOspfAddressScopeEntry = _MyOspfAddressScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3, 1)
)
myOspfAddressScopeEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfNetWorkAreaID"),
    (0, "DES7200-OSPF-MIB", "myOspfNetWorkAddress"),
    (0, "DES7200-OSPF-MIB", "myOspfNetWorkMask"),
)
if mibBuilder.loadTexts:
    myOspfAddressScopeEntry.setStatus("current")
_MyOspfNetWorkAreaID_Type = IpAddress
_MyOspfNetWorkAreaID_Object = MibTableColumn
myOspfNetWorkAreaID = _MyOspfNetWorkAreaID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3, 1, 1),
    _MyOspfNetWorkAreaID_Type()
)
myOspfNetWorkAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNetWorkAreaID.setStatus("current")
_MyOspfNetWorkAddress_Type = IpAddress
_MyOspfNetWorkAddress_Object = MibTableColumn
myOspfNetWorkAddress = _MyOspfNetWorkAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3, 1, 2),
    _MyOspfNetWorkAddress_Type()
)
myOspfNetWorkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNetWorkAddress.setStatus("current")
_MyOspfNetWorkMask_Type = IpAddress
_MyOspfNetWorkMask_Object = MibTableColumn
myOspfNetWorkMask = _MyOspfNetWorkMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3, 1, 3),
    _MyOspfNetWorkMask_Type()
)
myOspfNetWorkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNetWorkMask.setStatus("current")
_MyOspfNetWorkStatus_Type = RowStatus
_MyOspfNetWorkStatus_Object = MibTableColumn
myOspfNetWorkStatus = _MyOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 3, 1, 4),
    _MyOspfNetWorkStatus_Type()
)
myOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfNetWorkStatus.setStatus("current")
_MyOspfIfTable_Object = MibTable
myOspfIfTable = _MyOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    myOspfIfTable.setStatus("current")
_MyOspfIfEntry_Object = MibTableRow
myOspfIfEntry = _MyOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1)
)
myOspfIfEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfIfIpAddress"),
    (0, "DES7200-OSPF-MIB", "myOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    myOspfIfEntry.setStatus("current")
_MyOspfIfIpAddress_Type = IpAddress
_MyOspfIfIpAddress_Object = MibTableColumn
myOspfIfIpAddress = _MyOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 1),
    _MyOspfIfIpAddress_Type()
)
myOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfIpAddress.setStatus("current")
_MyOspfAddressLessIf_Type = Unsigned32
_MyOspfAddressLessIf_Object = MibTableColumn
myOspfAddressLessIf = _MyOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 2),
    _MyOspfAddressLessIf_Type()
)
myOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAddressLessIf.setStatus("current")


class _MyOspfIfAreaId_Type(AreaID):
    """Custom type myOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_MyOspfIfAreaId_Type.__name__ = "AreaID"
_MyOspfIfAreaId_Object = MibTableColumn
myOspfIfAreaId = _MyOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 3),
    _MyOspfIfAreaId_Type()
)
myOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfAreaId.setStatus("current")


class _MyOspfIfType_Type(Integer32):
    """Custom type myOspfIfType based on Integer32"""
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


_MyOspfIfType_Type.__name__ = "Integer32"
_MyOspfIfType_Object = MibTableColumn
myOspfIfType = _MyOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 4),
    _MyOspfIfType_Type()
)
myOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfType.setStatus("current")
_MyOspfIfAdminStat_Type = Status
_MyOspfIfAdminStat_Object = MibTableColumn
myOspfIfAdminStat = _MyOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 5),
    _MyOspfIfAdminStat_Type()
)
myOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfAdminStat.setStatus("current")


class _MyOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type myOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_MyOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_MyOspfIfRtrPriority_Object = MibTableColumn
myOspfIfRtrPriority = _MyOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 6),
    _MyOspfIfRtrPriority_Type()
)
myOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfRtrPriority.setStatus("current")


class _MyOspfIfTransitDelay_Type(Unsigned32):
    """Custom type myOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_MyOspfIfTransitDelay_Object = MibTableColumn
myOspfIfTransitDelay = _MyOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 7),
    _MyOspfIfTransitDelay_Type()
)
myOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfTransitDelay.setStatus("current")


class _MyOspfIfRetransInterval_Type(Unsigned32):
    """Custom type myOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_MyOspfIfRetransInterval_Object = MibTableColumn
myOspfIfRetransInterval = _MyOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 8),
    _MyOspfIfRetransInterval_Type()
)
myOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfRetransInterval.setStatus("current")


class _MyOspfIfHelloInterval_Type(HelloRange):
    """Custom type myOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_MyOspfIfHelloInterval_Type.__name__ = "HelloRange"
_MyOspfIfHelloInterval_Object = MibTableColumn
myOspfIfHelloInterval = _MyOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 9),
    _MyOspfIfHelloInterval_Type()
)
myOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfHelloInterval.setStatus("current")


class _MyOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type myOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_MyOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_MyOspfIfRtrDeadInterval_Object = MibTableColumn
myOspfIfRtrDeadInterval = _MyOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 10),
    _MyOspfIfRtrDeadInterval_Type()
)
myOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfRtrDeadInterval.setStatus("current")
_MyOspfIfPollInterval_Type = PositiveInteger
_MyOspfIfPollInterval_Object = MibTableColumn
myOspfIfPollInterval = _MyOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 11),
    _MyOspfIfPollInterval_Type()
)
myOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfPollInterval.setStatus("current")


class _MyOspfIfState_Type(Integer32):
    """Custom type myOspfIfState based on Integer32"""
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


_MyOspfIfState_Type.__name__ = "Integer32"
_MyOspfIfState_Object = MibTableColumn
myOspfIfState = _MyOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 12),
    _MyOspfIfState_Type()
)
myOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfState.setStatus("current")


class _MyOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type myOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_MyOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_MyOspfIfDesignatedRouter_Object = MibTableColumn
myOspfIfDesignatedRouter = _MyOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 13),
    _MyOspfIfDesignatedRouter_Type()
)
myOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfDesignatedRouter.setStatus("current")


class _MyOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type myOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_MyOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_MyOspfIfBackupDesignatedRouter_Object = MibTableColumn
myOspfIfBackupDesignatedRouter = _MyOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 14),
    _MyOspfIfBackupDesignatedRouter_Type()
)
myOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfBackupDesignatedRouter.setStatus("current")
_MyOspfIfEvents_Type = Counter32
_MyOspfIfEvents_Object = MibTableColumn
myOspfIfEvents = _MyOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 15),
    _MyOspfIfEvents_Type()
)
myOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfEvents.setStatus("current")


class _MyOspfIfAuthKey_Type(OctetString):
    """Custom type myOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MyOspfIfAuthKey_Type.__name__ = "OctetString"
_MyOspfIfAuthKey_Object = MibTableColumn
myOspfIfAuthKey = _MyOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 16),
    _MyOspfIfAuthKey_Type()
)
myOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfAuthKey.setStatus("current")
_MyOspfIfStatus_Type = RowStatus
_MyOspfIfStatus_Object = MibTableColumn
myOspfIfStatus = _MyOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 17),
    _MyOspfIfStatus_Type()
)
myOspfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfStatus.setStatus("current")


class _MyOspfIfMulticastForwarding_Type(Integer32):
    """Custom type myOspfIfMulticastForwarding based on Integer32"""
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


_MyOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_MyOspfIfMulticastForwarding_Object = MibTableColumn
myOspfIfMulticastForwarding = _MyOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 18),
    _MyOspfIfMulticastForwarding_Type()
)
myOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfMulticastForwarding.setStatus("current")


class _MyOspfIfDemand_Type(TruthValue):
    """Custom type myOspfIfDemand based on TruthValue"""
    defaultValue = 2


_MyOspfIfDemand_Type.__name__ = "TruthValue"
_MyOspfIfDemand_Object = MibTableColumn
myOspfIfDemand = _MyOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 19),
    _MyOspfIfDemand_Type()
)
myOspfIfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfDemand.setStatus("current")


class _MyOspfIfAuthType_Type(Integer32):
    """Custom type myOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyOspfIfAuthType_Type.__name__ = "Integer32"
_MyOspfIfAuthType_Object = MibTableColumn
myOspfIfAuthType = _MyOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 20),
    _MyOspfIfAuthType_Type()
)
myOspfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfAuthType.setStatus("current")


class _MyOspfIfDatabaseFilterAllOut_Type(EnabledStatus):
    """Custom type myOspfIfDatabaseFilterAllOut based on EnabledStatus"""
    defaultValue = 2


_MyOspfIfDatabaseFilterAllOut_Type.__name__ = "EnabledStatus"
_MyOspfIfDatabaseFilterAllOut_Object = MibTableColumn
myOspfIfDatabaseFilterAllOut = _MyOspfIfDatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 21),
    _MyOspfIfDatabaseFilterAllOut_Type()
)
myOspfIfDatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfDatabaseFilterAllOut.setStatus("current")


class _MyOspfIfDesignateRouterId_Type(IpAddress):
    """Custom type myOspfIfDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_MyOspfIfDesignateRouterId_Type.__name__ = "IpAddress"
_MyOspfIfDesignateRouterId_Object = MibTableColumn
myOspfIfDesignateRouterId = _MyOspfIfDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 22),
    _MyOspfIfDesignateRouterId_Type()
)
myOspfIfDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfDesignateRouterId.setStatus("current")


class _MyOspfIfBackupDesignateRouterId_Type(IpAddress):
    """Custom type myOspfIfBackupDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_MyOspfIfBackupDesignateRouterId_Type.__name__ = "IpAddress"
_MyOspfIfBackupDesignateRouterId_Object = MibTableColumn
myOspfIfBackupDesignateRouterId = _MyOspfIfBackupDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 23),
    _MyOspfIfBackupDesignateRouterId_Type()
)
myOspfIfBackupDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfBackupDesignateRouterId.setStatus("current")
_MyOspfIfWaitInternal_Type = TimeTicks
_MyOspfIfWaitInternal_Object = MibTableColumn
myOspfIfWaitInternal = _MyOspfIfWaitInternal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 24),
    _MyOspfIfWaitInternal_Type()
)
myOspfIfWaitInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfWaitInternal.setStatus("current")


class _MyOspfIfPassiveStatus_Type(EnabledStatus):
    """Custom type myOspfIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_MyOspfIfPassiveStatus_Type.__name__ = "EnabledStatus"
_MyOspfIfPassiveStatus_Object = MibTableColumn
myOspfIfPassiveStatus = _MyOspfIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 25),
    _MyOspfIfPassiveStatus_Type()
)
myOspfIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfPassiveStatus.setStatus("current")


class _MyOspfIfCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type myOspfIfCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyOspfIfCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_MyOspfIfCurrentUsedMd5AuthKeyId_Object = MibTableColumn
myOspfIfCurrentUsedMd5AuthKeyId = _MyOspfIfCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 4, 1, 26),
    _MyOspfIfCurrentUsedMd5AuthKeyId_Type()
)
myOspfIfCurrentUsedMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfIfCurrentUsedMd5AuthKeyId.setStatus("current")
_MyOspfIfMd5AuthKeyTable_Object = MibTable
myOspfIfMd5AuthKeyTable = _MyOspfIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5)
)
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKeyTable.setStatus("current")
_MyOspfIfMd5AuthKeyEntry_Object = MibTableRow
myOspfIfMd5AuthKeyEntry = _MyOspfIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5, 1)
)
myOspfIfMd5AuthKeyEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfIfMd5AuthKeyIf"),
    (0, "DES7200-OSPF-MIB", "myOspfIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKeyEntry.setStatus("current")
_MyOspfIfMd5AuthKeyIf_Type = Unsigned32
_MyOspfIfMd5AuthKeyIf_Object = MibTableColumn
myOspfIfMd5AuthKeyIf = _MyOspfIfMd5AuthKeyIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5, 1, 1),
    _MyOspfIfMd5AuthKeyIf_Type()
)
myOspfIfMd5AuthKeyIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKeyIf.setStatus("current")


class _MyOspfIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type myOspfIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_MyOspfIfMd5AuthKeyId_Object = MibTableColumn
myOspfIfMd5AuthKeyId = _MyOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5, 1, 2),
    _MyOspfIfMd5AuthKeyId_Type()
)
myOspfIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKeyId.setStatus("current")


class _MyOspfIfMd5AuthKey_Type(OctetString):
    """Custom type myOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MyOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_MyOspfIfMd5AuthKey_Object = MibTableColumn
myOspfIfMd5AuthKey = _MyOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5, 1, 3),
    _MyOspfIfMd5AuthKey_Type()
)
myOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKey.setStatus("current")
_MyOspfIfMd5AuthKeySt_Type = ConfigStatus
_MyOspfIfMd5AuthKeySt_Object = MibTableColumn
myOspfIfMd5AuthKeySt = _MyOspfIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 5, 1, 4),
    _MyOspfIfMd5AuthKeySt_Type()
)
myOspfIfMd5AuthKeySt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfIfMd5AuthKeySt.setStatus("current")
_MyOspfVirtTable_Object = MibTable
myOspfVirtTable = _MyOspfVirtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6)
)
if mibBuilder.loadTexts:
    myOspfVirtTable.setStatus("current")
_MyOspfVirtEntry_Object = MibTableRow
myOspfVirtEntry = _MyOspfVirtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1)
)
myOspfVirtEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfVirtIfAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    myOspfVirtEntry.setStatus("current")
_MyOspfVirtIfAreaId_Type = AreaID
_MyOspfVirtIfAreaId_Object = MibTableColumn
myOspfVirtIfAreaId = _MyOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 1),
    _MyOspfVirtIfAreaId_Type()
)
myOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfAreaId.setStatus("current")
_MyOspfVirtIfNeighbor_Type = RouterID
_MyOspfVirtIfNeighbor_Object = MibTableColumn
myOspfVirtIfNeighbor = _MyOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 2),
    _MyOspfVirtIfNeighbor_Type()
)
myOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfNeighbor.setStatus("current")


class _MyOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type myOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_MyOspfVirtIfTransitDelay_Object = MibTableColumn
myOspfVirtIfTransitDelay = _MyOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 3),
    _MyOspfVirtIfTransitDelay_Type()
)
myOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfTransitDelay.setStatus("current")


class _MyOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type myOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_MyOspfVirtIfRetransInterval_Object = MibTableColumn
myOspfVirtIfRetransInterval = _MyOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 4),
    _MyOspfVirtIfRetransInterval_Type()
)
myOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfRetransInterval.setStatus("current")


class _MyOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type myOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_MyOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_MyOspfVirtIfHelloInterval_Object = MibTableColumn
myOspfVirtIfHelloInterval = _MyOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 5),
    _MyOspfVirtIfHelloInterval_Type()
)
myOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfHelloInterval.setStatus("current")


class _MyOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type myOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_MyOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_MyOspfVirtIfRtrDeadInterval_Object = MibTableColumn
myOspfVirtIfRtrDeadInterval = _MyOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 6),
    _MyOspfVirtIfRtrDeadInterval_Type()
)
myOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfRtrDeadInterval.setStatus("current")


class _MyOspfVirtIfState_Type(Integer32):
    """Custom type myOspfVirtIfState based on Integer32"""
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


_MyOspfVirtIfState_Type.__name__ = "Integer32"
_MyOspfVirtIfState_Object = MibTableColumn
myOspfVirtIfState = _MyOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 7),
    _MyOspfVirtIfState_Type()
)
myOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfState.setStatus("current")
_MyOspfVirtIfEvents_Type = Counter32
_MyOspfVirtIfEvents_Object = MibTableColumn
myOspfVirtIfEvents = _MyOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 8),
    _MyOspfVirtIfEvents_Type()
)
myOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfEvents.setStatus("current")


class _MyOspfVirtIfAuthKey_Type(OctetString):
    """Custom type myOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MyOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_MyOspfVirtIfAuthKey_Object = MibTableColumn
myOspfVirtIfAuthKey = _MyOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 9),
    _MyOspfVirtIfAuthKey_Type()
)
myOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfAuthKey.setStatus("current")
_MyOspfVirtIfStatus_Type = RowStatus
_MyOspfVirtIfStatus_Object = MibTableColumn
myOspfVirtIfStatus = _MyOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 10),
    _MyOspfVirtIfStatus_Type()
)
myOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfStatus.setStatus("current")


class _MyOspfVirtIfAuthType_Type(Integer32):
    """Custom type myOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyOspfVirtIfAuthType_Type.__name__ = "Integer32"
_MyOspfVirtIfAuthType_Object = MibTableColumn
myOspfVirtIfAuthType = _MyOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 11),
    _MyOspfVirtIfAuthType_Type()
)
myOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfAuthType.setStatus("current")
_MyOspfVirtCost_Type = Unsigned32
_MyOspfVirtCost_Object = MibTableColumn
myOspfVirtCost = _MyOspfVirtCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 12),
    _MyOspfVirtCost_Type()
)
myOspfVirtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtCost.setStatus("current")
_MyOspfVirtNativeIfIndex_Type = Integer32
_MyOspfVirtNativeIfIndex_Object = MibTableColumn
myOspfVirtNativeIfIndex = _MyOspfVirtNativeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 13),
    _MyOspfVirtNativeIfIndex_Type()
)
myOspfVirtNativeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtNativeIfIndex.setStatus("current")


class _MyOspfVirtLinkState_Type(Integer32):
    """Custom type myOspfVirtLinkState based on Integer32"""
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


_MyOspfVirtLinkState_Type.__name__ = "Integer32"
_MyOspfVirtLinkState_Object = MibTableColumn
myOspfVirtLinkState = _MyOspfVirtLinkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 14),
    _MyOspfVirtLinkState_Type()
)
myOspfVirtLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtLinkState.setStatus("current")
_MyOspfVirtHelloDueIn_Type = TimeTicks
_MyOspfVirtHelloDueIn_Object = MibTableColumn
myOspfVirtHelloDueIn = _MyOspfVirtHelloDueIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 15),
    _MyOspfVirtHelloDueIn_Type()
)
myOspfVirtHelloDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtHelloDueIn.setStatus("current")


class _MyOspfVirtCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type myOspfVirtCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyOspfVirtCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_MyOspfVirtCurrentUsedMd5AuthKeyId_Object = MibTableColumn
myOspfVirtCurrentUsedMd5AuthKeyId = _MyOspfVirtCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 6, 1, 16),
    _MyOspfVirtCurrentUsedMd5AuthKeyId_Type()
)
myOspfVirtCurrentUsedMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfVirtCurrentUsedMd5AuthKeyId.setStatus("current")
_MyOspfVirtIfMd5AuthKeyTable_Object = MibTable
myOspfVirtIfMd5AuthKeyTable = _MyOspfVirtIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7)
)
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeyTable.setStatus("current")
_MyOspfVirtIfMd5AuthKeyEntry_Object = MibTableRow
myOspfVirtIfMd5AuthKeyEntry = _MyOspfVirtIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1)
)
myOspfVirtIfMd5AuthKeyEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyNeighbor"),
    (0, "DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeyEntry.setStatus("current")
_MyOspfVirtIfMd5AuthKeyAreaId_Type = AreaID
_MyOspfVirtIfMd5AuthKeyAreaId_Object = MibTableColumn
myOspfVirtIfMd5AuthKeyAreaId = _MyOspfVirtIfMd5AuthKeyAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1, 1),
    _MyOspfVirtIfMd5AuthKeyAreaId_Type()
)
myOspfVirtIfMd5AuthKeyAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeyAreaId.setStatus("current")
_MyOspfVirtIfMd5AuthKeyNeighbor_Type = RouterID
_MyOspfVirtIfMd5AuthKeyNeighbor_Object = MibTableColumn
myOspfVirtIfMd5AuthKeyNeighbor = _MyOspfVirtIfMd5AuthKeyNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1, 2),
    _MyOspfVirtIfMd5AuthKeyNeighbor_Type()
)
myOspfVirtIfMd5AuthKeyNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeyNeighbor.setStatus("current")


class _MyOspfVirtIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type myOspfVirtIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyOspfVirtIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_MyOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
myOspfVirtIfMd5AuthKeyId = _MyOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1, 3),
    _MyOspfVirtIfMd5AuthKeyId_Type()
)
myOspfVirtIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeyId.setStatus("current")


class _MyOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type myOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MyOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_MyOspfVirtIfMd5AuthKey_Object = MibTableColumn
myOspfVirtIfMd5AuthKey = _MyOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1, 4),
    _MyOspfVirtIfMd5AuthKey_Type()
)
myOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKey.setStatus("current")
_MyOspfVirtIfMd5AuthKeySt_Type = ConfigStatus
_MyOspfVirtIfMd5AuthKeySt_Object = MibTableColumn
myOspfVirtIfMd5AuthKeySt = _MyOspfVirtIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 7, 1, 5),
    _MyOspfVirtIfMd5AuthKeySt_Type()
)
myOspfVirtIfMd5AuthKeySt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myOspfVirtIfMd5AuthKeySt.setStatus("current")
_MyOspfLsaDetailInfoMibsGroup_ObjectIdentity = ObjectIdentity
myOspfLsaDetailInfoMibsGroup = _MyOspfLsaDetailInfoMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8)
)
_MyOspfLsdbTable_Object = MibTable
myOspfLsdbTable = _MyOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1)
)
if mibBuilder.loadTexts:
    myOspfLsdbTable.setStatus("current")
_MyOspfLsdbEntry_Object = MibTableRow
myOspfLsdbEntry = _MyOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1)
)
myOspfLsdbEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfLsdbAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbType"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbLsid"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    myOspfLsdbEntry.setStatus("current")
_MyOspfLsdbAreaId_Type = AreaID
_MyOspfLsdbAreaId_Object = MibTableColumn
myOspfLsdbAreaId = _MyOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 1),
    _MyOspfLsdbAreaId_Type()
)
myOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbAreaId.setStatus("current")


class _MyOspfLsdbType_Type(Integer32):
    """Custom type myOspfLsdbType based on Integer32"""
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


_MyOspfLsdbType_Type.__name__ = "Integer32"
_MyOspfLsdbType_Object = MibTableColumn
myOspfLsdbType = _MyOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 2),
    _MyOspfLsdbType_Type()
)
myOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbType.setStatus("current")
_MyOspfLsdbLsid_Type = IpAddress
_MyOspfLsdbLsid_Object = MibTableColumn
myOspfLsdbLsid = _MyOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 3),
    _MyOspfLsdbLsid_Type()
)
myOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbLsid.setStatus("current")
_MyOspfLsdbRouterId_Type = RouterID
_MyOspfLsdbRouterId_Object = MibTableColumn
myOspfLsdbRouterId = _MyOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 4),
    _MyOspfLsdbRouterId_Type()
)
myOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbRouterId.setStatus("current")
_MyOspfLsdbSequence_Type = Unsigned32
_MyOspfLsdbSequence_Object = MibTableColumn
myOspfLsdbSequence = _MyOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 5),
    _MyOspfLsdbSequence_Type()
)
myOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbSequence.setStatus("current")
_MyOspfLsdbAge_Type = Unsigned32
_MyOspfLsdbAge_Object = MibTableColumn
myOspfLsdbAge = _MyOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 6),
    _MyOspfLsdbAge_Type()
)
myOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbAge.setStatus("current")
_MyOspfLsdbChecksum_Type = Unsigned32
_MyOspfLsdbChecksum_Object = MibTableColumn
myOspfLsdbChecksum = _MyOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 7),
    _MyOspfLsdbChecksum_Type()
)
myOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbChecksum.setStatus("current")


class _MyOspfLsdbAdvertisement_Type(OctetString):
    """Custom type myOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_MyOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_MyOspfLsdbAdvertisement_Object = MibTableColumn
myOspfLsdbAdvertisement = _MyOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 8),
    _MyOspfLsdbAdvertisement_Type()
)
myOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbAdvertisement.setStatus("current")


class _MyOspfLsdbLinkNum_Type(Unsigned32):
    """Custom type myOspfLsdbLinkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MyOspfLsdbLinkNum_Type.__name__ = "Unsigned32"
_MyOspfLsdbLinkNum_Object = MibTableColumn
myOspfLsdbLinkNum = _MyOspfLsdbLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 9),
    _MyOspfLsdbLinkNum_Type()
)
myOspfLsdbLinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbLinkNum.setStatus("current")


class _MyOspfLsdbPacketLength_Type(Unsigned32):
    """Custom type myOspfLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyOspfLsdbPacketLength_Type.__name__ = "Unsigned32"
_MyOspfLsdbPacketLength_Object = MibTableColumn
myOspfLsdbPacketLength = _MyOspfLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 10),
    _MyOspfLsdbPacketLength_Type()
)
myOspfLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbPacketLength.setStatus("current")
_MyOspfSummaryLsaNetworkMask_Type = IpAddress
_MyOspfSummaryLsaNetworkMask_Object = MibTableColumn
myOspfSummaryLsaNetworkMask = _MyOspfSummaryLsaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 11),
    _MyOspfSummaryLsaNetworkMask_Type()
)
myOspfSummaryLsaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfSummaryLsaNetworkMask.setStatus("current")


class _MyOspfSummaryLsaTos0Metric_Type(Unsigned32):
    """Custom type myOspfSummaryLsaTos0Metric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyOspfSummaryLsaTos0Metric_Type.__name__ = "Unsigned32"
_MyOspfSummaryLsaTos0Metric_Object = MibTableColumn
myOspfSummaryLsaTos0Metric = _MyOspfSummaryLsaTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 12),
    _MyOspfSummaryLsaTos0Metric_Type()
)
myOspfSummaryLsaTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfSummaryLsaTos0Metric.setStatus("current")


class _MyOspfNssaLsaDetailMetricType_Type(Integer32):
    """Custom type myOspfNssaLsaDetailMetricType based on Integer32"""
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


_MyOspfNssaLsaDetailMetricType_Type.__name__ = "Integer32"
_MyOspfNssaLsaDetailMetricType_Object = MibTableColumn
myOspfNssaLsaDetailMetricType = _MyOspfNssaLsaDetailMetricType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 13),
    _MyOspfNssaLsaDetailMetricType_Type()
)
myOspfNssaLsaDetailMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNssaLsaDetailMetricType.setStatus("current")
_MyOspfNssaLsaDetailForwardAddr_Type = IpAddress
_MyOspfNssaLsaDetailForwardAddr_Object = MibTableColumn
myOspfNssaLsaDetailForwardAddr = _MyOspfNssaLsaDetailForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 14),
    _MyOspfNssaLsaDetailForwardAddr_Type()
)
myOspfNssaLsaDetailForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNssaLsaDetailForwardAddr.setStatus("current")
_MyOspfNssaLsaDetailRouteTag_Type = Unsigned32
_MyOspfNssaLsaDetailRouteTag_Object = MibTableColumn
myOspfNssaLsaDetailRouteTag = _MyOspfNssaLsaDetailRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 15),
    _MyOspfNssaLsaDetailRouteTag_Type()
)
myOspfNssaLsaDetailRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNssaLsaDetailRouteTag.setStatus("current")
_MyOspfLsdbOption_Type = Unsigned32
_MyOspfLsdbOption_Object = MibTableColumn
myOspfLsdbOption = _MyOspfLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 1, 1, 16),
    _MyOspfLsdbOption_Type()
)
myOspfLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsdbOption.setStatus("current")
_MyOspfExtLsdbTable_Object = MibTable
myOspfExtLsdbTable = _MyOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2)
)
if mibBuilder.loadTexts:
    myOspfExtLsdbTable.setStatus("current")
_MyOspfExtLsdbEntry_Object = MibTableRow
myOspfExtLsdbEntry = _MyOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1)
)
myOspfExtLsdbEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfExtLsdbType"),
    (0, "DES7200-OSPF-MIB", "myOspfExtLsdbLsid"),
    (0, "DES7200-OSPF-MIB", "myOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    myOspfExtLsdbEntry.setStatus("current")


class _MyOspfExtLsdbType_Type(Integer32):
    """Custom type myOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_MyOspfExtLsdbType_Type.__name__ = "Integer32"
_MyOspfExtLsdbType_Object = MibTableColumn
myOspfExtLsdbType = _MyOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 1),
    _MyOspfExtLsdbType_Type()
)
myOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbType.setStatus("current")
_MyOspfExtLsdbLsid_Type = IpAddress
_MyOspfExtLsdbLsid_Object = MibTableColumn
myOspfExtLsdbLsid = _MyOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 2),
    _MyOspfExtLsdbLsid_Type()
)
myOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbLsid.setStatus("current")
_MyOspfExtLsdbRouterId_Type = RouterID
_MyOspfExtLsdbRouterId_Object = MibTableColumn
myOspfExtLsdbRouterId = _MyOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 3),
    _MyOspfExtLsdbRouterId_Type()
)
myOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbRouterId.setStatus("current")
_MyOspfExtLsdbSequence_Type = Unsigned32
_MyOspfExtLsdbSequence_Object = MibTableColumn
myOspfExtLsdbSequence = _MyOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 4),
    _MyOspfExtLsdbSequence_Type()
)
myOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbSequence.setStatus("current")
_MyOspfExtLsdbAge_Type = Unsigned32
_MyOspfExtLsdbAge_Object = MibTableColumn
myOspfExtLsdbAge = _MyOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 5),
    _MyOspfExtLsdbAge_Type()
)
myOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbAge.setStatus("current")
_MyOspfExtLsdbChecksum_Type = Unsigned32
_MyOspfExtLsdbChecksum_Object = MibTableColumn
myOspfExtLsdbChecksum = _MyOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 6),
    _MyOspfExtLsdbChecksum_Type()
)
myOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbChecksum.setStatus("current")


class _MyOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type myOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_MyOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_MyOspfExtLsdbAdvertisement_Object = MibTableColumn
myOspfExtLsdbAdvertisement = _MyOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 7),
    _MyOspfExtLsdbAdvertisement_Type()
)
myOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbAdvertisement.setStatus("current")
_MyOspfExtLsdbNetworkMask_Type = IpAddress
_MyOspfExtLsdbNetworkMask_Object = MibTableColumn
myOspfExtLsdbNetworkMask = _MyOspfExtLsdbNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 8),
    _MyOspfExtLsdbNetworkMask_Type()
)
myOspfExtLsdbNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbNetworkMask.setStatus("current")
_MyOspfExtLsdbMetric_Type = Integer32
_MyOspfExtLsdbMetric_Object = MibTableColumn
myOspfExtLsdbMetric = _MyOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 9),
    _MyOspfExtLsdbMetric_Type()
)
myOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbMetric.setStatus("current")


class _MyOspfExtLsdbMetricType_Type(Integer32):
    """Custom type myOspfExtLsdbMetricType based on Integer32"""
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


_MyOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_MyOspfExtLsdbMetricType_Object = MibTableColumn
myOspfExtLsdbMetricType = _MyOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 10),
    _MyOspfExtLsdbMetricType_Type()
)
myOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbMetricType.setStatus("current")
_MyOspfExtLsdbForwardAddr_Type = IpAddress
_MyOspfExtLsdbForwardAddr_Object = MibTableColumn
myOspfExtLsdbForwardAddr = _MyOspfExtLsdbForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 11),
    _MyOspfExtLsdbForwardAddr_Type()
)
myOspfExtLsdbForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbForwardAddr.setStatus("current")
_MyOspfExtLsdbRouteTag_Type = Unsigned32
_MyOspfExtLsdbRouteTag_Object = MibTableColumn
myOspfExtLsdbRouteTag = _MyOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 12),
    _MyOspfExtLsdbRouteTag_Type()
)
myOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbRouteTag.setStatus("current")
_MyOspfExtLsdbOption_Type = Unsigned32
_MyOspfExtLsdbOption_Object = MibTableColumn
myOspfExtLsdbOption = _MyOspfExtLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 13),
    _MyOspfExtLsdbOption_Type()
)
myOspfExtLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbOption.setStatus("current")


class _MyOspfExtLsdbPacketLength_Type(Unsigned32):
    """Custom type myOspfExtLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyOspfExtLsdbPacketLength_Type.__name__ = "Unsigned32"
_MyOspfExtLsdbPacketLength_Object = MibTableColumn
myOspfExtLsdbPacketLength = _MyOspfExtLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 2, 1, 14),
    _MyOspfExtLsdbPacketLength_Type()
)
myOspfExtLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfExtLsdbPacketLength.setStatus("current")
_MyOspfRouterLsaDetailTable_Object = MibTable
myOspfRouterLsaDetailTable = _MyOspfRouterLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3)
)
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailTable.setStatus("current")
_MyOspfRouterLsaDetailEntry_Object = MibTableRow
myOspfRouterLsaDetailEntry = _MyOspfRouterLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3, 1)
)
myOspfRouterLsaDetailEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfLsdbAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbType"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbLsid"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbRouterId"),
    (0, "DES7200-OSPF-MIB", "myOspfRouterLsaDetailLinkID"),
)
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailEntry.setStatus("current")
_MyOspfRouterLsaDetailLinkID_Type = IpAddress
_MyOspfRouterLsaDetailLinkID_Object = MibTableColumn
myOspfRouterLsaDetailLinkID = _MyOspfRouterLsaDetailLinkID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3, 1, 1),
    _MyOspfRouterLsaDetailLinkID_Type()
)
myOspfRouterLsaDetailLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailLinkID.setStatus("current")


class _MyOspfRouterLsaDetailLinkType_Type(Integer32):
    """Custom type myOspfRouterLsaDetailLinkType based on Integer32"""
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


_MyOspfRouterLsaDetailLinkType_Type.__name__ = "Integer32"
_MyOspfRouterLsaDetailLinkType_Object = MibTableColumn
myOspfRouterLsaDetailLinkType = _MyOspfRouterLsaDetailLinkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3, 1, 2),
    _MyOspfRouterLsaDetailLinkType_Type()
)
myOspfRouterLsaDetailLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailLinkType.setStatus("current")
_MyOspfRouterLsaDetailLinkData_Type = IpAddress
_MyOspfRouterLsaDetailLinkData_Object = MibTableColumn
myOspfRouterLsaDetailLinkData = _MyOspfRouterLsaDetailLinkData_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3, 1, 3),
    _MyOspfRouterLsaDetailLinkData_Type()
)
myOspfRouterLsaDetailLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailLinkData.setStatus("current")
_MyOspfRouterLsaDetailTos0Metric_Type = Unsigned32
_MyOspfRouterLsaDetailTos0Metric_Object = MibTableColumn
myOspfRouterLsaDetailTos0Metric = _MyOspfRouterLsaDetailTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 3, 1, 4),
    _MyOspfRouterLsaDetailTos0Metric_Type()
)
myOspfRouterLsaDetailTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouterLsaDetailTos0Metric.setStatus("current")
_MyOspfNetWorkLsaDetailTable_Object = MibTable
myOspfNetWorkLsaDetailTable = _MyOspfNetWorkLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 4)
)
if mibBuilder.loadTexts:
    myOspfNetWorkLsaDetailTable.setStatus("current")
_MyOspfNetWorkLsaDetailEntry_Object = MibTableRow
myOspfNetWorkLsaDetailEntry = _MyOspfNetWorkLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 4, 1)
)
myOspfNetWorkLsaDetailEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfLsdbAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbType"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbLsid"),
    (0, "DES7200-OSPF-MIB", "myOspfLsdbRouterId"),
    (0, "DES7200-OSPF-MIB", "myOspfNetWorkLsaDetailAttachedRouter"),
)
if mibBuilder.loadTexts:
    myOspfNetWorkLsaDetailEntry.setStatus("current")
_MyOspfNetWorkLsaDetailAttachedRouter_Type = IpAddress
_MyOspfNetWorkLsaDetailAttachedRouter_Object = MibTableColumn
myOspfNetWorkLsaDetailAttachedRouter = _MyOspfNetWorkLsaDetailAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 4, 1, 1),
    _MyOspfNetWorkLsaDetailAttachedRouter_Type()
)
myOspfNetWorkLsaDetailAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNetWorkLsaDetailAttachedRouter.setStatus("current")
_MyOspfNetWorkLsaDetailNetworkMask_Type = IpAddress
_MyOspfNetWorkLsaDetailNetworkMask_Object = MibTableColumn
myOspfNetWorkLsaDetailNetworkMask = _MyOspfNetWorkLsaDetailNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 4, 1, 2),
    _MyOspfNetWorkLsaDetailNetworkMask_Type()
)
myOspfNetWorkLsaDetailNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNetWorkLsaDetailNetworkMask.setStatus("current")
_MyOspfAreaLsaDBSumTable_Object = MibTable
myOspfAreaLsaDBSumTable = _MyOspfAreaLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5)
)
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumTable.setStatus("current")
_MyOspfAreaLsaDBSumEntry_Object = MibTableRow
myOspfAreaLsaDBSumEntry = _MyOspfAreaLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1)
)
myOspfAreaLsaDBSumEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfAreaLsaDBSumAreaId"),
    (0, "DES7200-OSPF-MIB", "myOspfAreaLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumEntry.setStatus("current")
_MyOspfAreaLsaDBSumAreaId_Type = IpAddress
_MyOspfAreaLsaDBSumAreaId_Object = MibTableColumn
myOspfAreaLsaDBSumAreaId = _MyOspfAreaLsaDBSumAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1, 1),
    _MyOspfAreaLsaDBSumAreaId_Type()
)
myOspfAreaLsaDBSumAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumAreaId.setStatus("current")


class _MyOspfAreaLsaDBSumLsaType_Type(Integer32):
    """Custom type myOspfAreaLsaDBSumLsaType based on Integer32"""
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


_MyOspfAreaLsaDBSumLsaType_Type.__name__ = "Integer32"
_MyOspfAreaLsaDBSumLsaType_Object = MibTableColumn
myOspfAreaLsaDBSumLsaType = _MyOspfAreaLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1, 2),
    _MyOspfAreaLsaDBSumLsaType_Type()
)
myOspfAreaLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumLsaType.setStatus("current")
_MyOspfAreaLsaDBSumCounts_Type = Counter32
_MyOspfAreaLsaDBSumCounts_Object = MibTableColumn
myOspfAreaLsaDBSumCounts = _MyOspfAreaLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1, 3),
    _MyOspfAreaLsaDBSumCounts_Type()
)
myOspfAreaLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumCounts.setStatus("current")
_MyOspfAreaLsaDBSumDeletes_Type = Counter32
_MyOspfAreaLsaDBSumDeletes_Object = MibTableColumn
myOspfAreaLsaDBSumDeletes = _MyOspfAreaLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1, 4),
    _MyOspfAreaLsaDBSumDeletes_Type()
)
myOspfAreaLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumDeletes.setStatus("current")
_MyOspfAreaLsaDBSumMaxage_Type = Counter32
_MyOspfAreaLsaDBSumMaxage_Object = MibTableColumn
myOspfAreaLsaDBSumMaxage = _MyOspfAreaLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 5, 1, 5),
    _MyOspfAreaLsaDBSumMaxage_Type()
)
myOspfAreaLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfAreaLsaDBSumMaxage.setStatus("current")
_MyOspfLsaDBSumTable_Object = MibTable
myOspfLsaDBSumTable = _MyOspfLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6)
)
if mibBuilder.loadTexts:
    myOspfLsaDBSumTable.setStatus("current")
_MyOspfLsaDBSumEntry_Object = MibTableRow
myOspfLsaDBSumEntry = _MyOspfLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6, 1)
)
myOspfLsaDBSumEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    myOspfLsaDBSumEntry.setStatus("current")


class _MyOspfLsaDBSumLsaType_Type(Integer32):
    """Custom type myOspfLsaDBSumLsaType based on Integer32"""
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


_MyOspfLsaDBSumLsaType_Type.__name__ = "Integer32"
_MyOspfLsaDBSumLsaType_Object = MibTableColumn
myOspfLsaDBSumLsaType = _MyOspfLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6, 1, 1),
    _MyOspfLsaDBSumLsaType_Type()
)
myOspfLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsaDBSumLsaType.setStatus("current")
_MyOspfLsaDBSumCounts_Type = Counter32
_MyOspfLsaDBSumCounts_Object = MibTableColumn
myOspfLsaDBSumCounts = _MyOspfLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6, 1, 2),
    _MyOspfLsaDBSumCounts_Type()
)
myOspfLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsaDBSumCounts.setStatus("current")
_MyOspfLsaDBSumDeletes_Type = Counter32
_MyOspfLsaDBSumDeletes_Object = MibTableColumn
myOspfLsaDBSumDeletes = _MyOspfLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6, 1, 3),
    _MyOspfLsaDBSumDeletes_Type()
)
myOspfLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsaDBSumDeletes.setStatus("current")
_MyOspfLsaDBSumMaxage_Type = Counter32
_MyOspfLsaDBSumMaxage_Object = MibTableColumn
myOspfLsaDBSumMaxage = _MyOspfLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 8, 6, 1, 4),
    _MyOspfLsaDBSumMaxage_Type()
)
myOspfLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfLsaDBSumMaxage.setStatus("current")
_MyOspfNeighborTable_Object = MibTable
myOspfNeighborTable = _MyOspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9)
)
if mibBuilder.loadTexts:
    myOspfNeighborTable.setStatus("current")
_MyOspfNeighborEntry_Object = MibTableRow
myOspfNeighborEntry = _MyOspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1)
)
myOspfNeighborEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfNbrIpAddr"),
    (0, "DES7200-OSPF-MIB", "myOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    myOspfNeighborEntry.setStatus("current")
_MyOspfNbrIpAddr_Type = IpAddress
_MyOspfNbrIpAddr_Object = MibTableColumn
myOspfNbrIpAddr = _MyOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 1),
    _MyOspfNbrIpAddr_Type()
)
myOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrIpAddr.setStatus("current")
_MyOspfNbrAddressLessIndex_Type = Unsigned32
_MyOspfNbrAddressLessIndex_Object = MibTableColumn
myOspfNbrAddressLessIndex = _MyOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 2),
    _MyOspfNbrAddressLessIndex_Type()
)
myOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrAddressLessIndex.setStatus("current")
_MyOspfNbrRtrId_Type = RouterID
_MyOspfNbrRtrId_Object = MibTableColumn
myOspfNbrRtrId = _MyOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 3),
    _MyOspfNbrRtrId_Type()
)
myOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrRtrId.setStatus("current")
_MyOspfNbrOptions_Type = Unsigned32
_MyOspfNbrOptions_Object = MibTableColumn
myOspfNbrOptions = _MyOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 4),
    _MyOspfNbrOptions_Type()
)
myOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrOptions.setStatus("current")
_MyOspfNbrPriority_Type = DesignatedRouterPriority
_MyOspfNbrPriority_Object = MibTableColumn
myOspfNbrPriority = _MyOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 5),
    _MyOspfNbrPriority_Type()
)
myOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrPriority.setStatus("current")


class _MyOspfNbrState_Type(Integer32):
    """Custom type myOspfNbrState based on Integer32"""
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
          ("exchangeMy", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_MyOspfNbrState_Type.__name__ = "Integer32"
_MyOspfNbrState_Object = MibTableColumn
myOspfNbrState = _MyOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 6),
    _MyOspfNbrState_Type()
)
myOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrState.setStatus("current")
_MyOspfNbrEvents_Type = Counter32
_MyOspfNbrEvents_Object = MibTableColumn
myOspfNbrEvents = _MyOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 7),
    _MyOspfNbrEvents_Type()
)
myOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrEvents.setStatus("current")
_MyOspfNbrLsRetransQLen_Type = Gauge32
_MyOspfNbrLsRetransQLen_Object = MibTableColumn
myOspfNbrLsRetransQLen = _MyOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 8),
    _MyOspfNbrLsRetransQLen_Type()
)
myOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrLsRetransQLen.setStatus("current")
_MyOspfNbmaNbrStatus_Type = RowStatus
_MyOspfNbmaNbrStatus_Object = MibTableColumn
myOspfNbmaNbrStatus = _MyOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 9),
    _MyOspfNbmaNbrStatus_Type()
)
myOspfNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbmaNbrStatus.setStatus("current")


class _MyOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type myOspfNbmaNbrPermanence based on Integer32"""
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


_MyOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_MyOspfNbmaNbrPermanence_Object = MibTableColumn
myOspfNbmaNbrPermanence = _MyOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 10),
    _MyOspfNbmaNbrPermanence_Type()
)
myOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbmaNbrPermanence.setStatus("current")
_MyOspfNbrHelloSuppressed_Type = TruthValue
_MyOspfNbrHelloSuppressed_Object = MibTableColumn
myOspfNbrHelloSuppressed = _MyOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 11),
    _MyOspfNbrHelloSuppressed_Type()
)
myOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrHelloSuppressed.setStatus("current")
_MyOspfNbrDeadTimeDueIn_Type = TimeTicks
_MyOspfNbrDeadTimeDueIn_Object = MibTableColumn
myOspfNbrDeadTimeDueIn = _MyOspfNbrDeadTimeDueIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 12),
    _MyOspfNbrDeadTimeDueIn_Type()
)
myOspfNbrDeadTimeDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrDeadTimeDueIn.setStatus("current")
_MyOspfNbrNeighborUpTime_Type = TimeTicks
_MyOspfNbrNeighborUpTime_Object = MibTableColumn
myOspfNbrNeighborUpTime = _MyOspfNbrNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 13),
    _MyOspfNbrNeighborUpTime_Type()
)
myOspfNbrNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrNeighborUpTime.setStatus("current")
_MyOspfNbrDR_Type = IpAddress
_MyOspfNbrDR_Object = MibTableColumn
myOspfNbrDR = _MyOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 14),
    _MyOspfNbrDR_Type()
)
myOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrDR.setStatus("current")
_MyOspfNbrBDR_Type = IpAddress
_MyOspfNbrBDR_Object = MibTableColumn
myOspfNbrBDR = _MyOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 15),
    _MyOspfNbrBDR_Type()
)
myOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrBDR.setStatus("current")
_MyOspfNbrArea_Type = IpAddress
_MyOspfNbrArea_Object = MibTableColumn
myOspfNbrArea = _MyOspfNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 16),
    _MyOspfNbrArea_Type()
)
myOspfNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrArea.setStatus("current")
_MyOspfNbrRetransmissionNum_Type = Counter32
_MyOspfNbrRetransmissionNum_Object = MibTableColumn
myOspfNbrRetransmissionNum = _MyOspfNbrRetransmissionNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 17),
    _MyOspfNbrRetransmissionNum_Type()
)
myOspfNbrRetransmissionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrRetransmissionNum.setStatus("current")


class _MyOspfNbrIfState_Type(Integer32):
    """Custom type myOspfNbrIfState based on Integer32"""
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


_MyOspfNbrIfState_Type.__name__ = "Integer32"
_MyOspfNbrIfState_Object = MibTableColumn
myOspfNbrIfState = _MyOspfNbrIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 9, 1, 18),
    _MyOspfNbrIfState_Type()
)
myOspfNbrIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfNbrIfState.setStatus("current")
_MyOspfRouteTable_Object = MibTable
myOspfRouteTable = _MyOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10)
)
if mibBuilder.loadTexts:
    myOspfRouteTable.setStatus("current")
_MyOspfRouteEntry_Object = MibTableRow
myOspfRouteEntry = _MyOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1)
)
myOspfRouteEntry.setIndexNames(
    (0, "DES7200-OSPF-MIB", "myOspfRouteDest"),
    (0, "DES7200-OSPF-MIB", "myOspfRouteArea"),
    (0, "DES7200-OSPF-MIB", "myOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    myOspfRouteEntry.setStatus("current")
_MyOspfRouteDest_Type = IpAddress
_MyOspfRouteDest_Object = MibTableColumn
myOspfRouteDest = _MyOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 1),
    _MyOspfRouteDest_Type()
)
myOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteDest.setStatus("current")
_MyOspfRouteArea_Type = IpAddress
_MyOspfRouteArea_Object = MibTableColumn
myOspfRouteArea = _MyOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 2),
    _MyOspfRouteArea_Type()
)
myOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteArea.setStatus("current")
_MyOspfRouteNextHop_Type = IpAddress
_MyOspfRouteNextHop_Object = MibTableColumn
myOspfRouteNextHop = _MyOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 3),
    _MyOspfRouteNextHop_Type()
)
myOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteNextHop.setStatus("current")
_MyOspfRouteCost_Type = Unsigned32
_MyOspfRouteCost_Object = MibTableColumn
myOspfRouteCost = _MyOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 4),
    _MyOspfRouteCost_Type()
)
myOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteCost.setStatus("current")


class _MyOspfRouteDRType_Type(Integer32):
    """Custom type myOspfRouteDRType based on Integer32"""
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


_MyOspfRouteDRType_Type.__name__ = "Integer32"
_MyOspfRouteDRType_Object = MibTableColumn
myOspfRouteDRType = _MyOspfRouteDRType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 5),
    _MyOspfRouteDRType_Type()
)
myOspfRouteDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteDRType.setStatus("current")


class _MyOspfRouteType_Type(Integer32):
    """Custom type myOspfRouteType based on Integer32"""
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


_MyOspfRouteType_Type.__name__ = "Integer32"
_MyOspfRouteType_Object = MibTableColumn
myOspfRouteType = _MyOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 6),
    _MyOspfRouteType_Type()
)
myOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteType.setStatus("current")
_MyOspfRouteSpfNo_Type = Counter32
_MyOspfRouteSpfNo_Object = MibTableColumn
myOspfRouteSpfNo = _MyOspfRouteSpfNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 1, 10, 1, 7),
    _MyOspfRouteSpfNo_Type()
)
myOspfRouteSpfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myOspfRouteSpfNo.setStatus("current")
_MyOspfMIBConformance_ObjectIdentity = ObjectIdentity
myOspfMIBConformance = _MyOspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2)
)
_MyOspfMIBCompliances_ObjectIdentity = ObjectIdentity
myOspfMIBCompliances = _MyOspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 1)
)
_MyOspfMIBGroups_ObjectIdentity = ObjectIdentity
myOspfMIBGroups = _MyOspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2)
)
_OspfMIBConformance_ObjectIdentity = ObjectIdentity
ospfMIBConformance = _OspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 3)
)
_OspfMIBCompliances_ObjectIdentity = ObjectIdentity
ospfMIBCompliances = _OspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 3, 1)
)

# Managed Objects groups

myOspfBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 1)
)
myOspfBaseMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfMiniLsaInterval"),
        ("DES7200-OSPF-MIB", "myOspfMiniLsaArrival"),
        ("DES7200-OSPF-MIB", "myOspfAreasNum"),
        ("DES7200-OSPF-MIB", "myOspfNormalAreasNum"),
        ("DES7200-OSPF-MIB", "myOspfStubAreasNum"),
        ("DES7200-OSPF-MIB", "myOspfNssaAreasNum"),
        ("DES7200-OSPF-MIB", "myOspfSpfDelay"),
        ("DES7200-OSPF-MIB", "myOspfSpfHoldTime"),
        ("DES7200-OSPF-MIB", "myOspfAutoCostRefBandWidthRef"),
        ("DES7200-OSPF-MIB", "myOspfLsaGroupPacing"),
        ("DES7200-OSPF-MIB", "myOspfInterDistance"),
        ("DES7200-OSPF-MIB", "myOspfIntraDistance"),
        ("DES7200-OSPF-MIB", "myOspfExternDistance"),
        ("DES7200-OSPF-MIB", "myOspfLogAdjChangeNotify"),
        ("DES7200-OSPF-MIB", "myOspfPassiveStatus"),
        ("DES7200-OSPF-MIB", "myOspfRFC1583Compatibility"),
        ("DES7200-OSPF-MIB", "myOspfRouteRedisDefMetricVal"))
)
if mibBuilder.loadTexts:
    myOspfBaseMIBGroup.setStatus("current")

myOspfAreaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 2)
)
myOspfAreaMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfAreaId"),
        ("DES7200-OSPF-MIB", "myOspfAuthType"),
        ("DES7200-OSPF-MIB", "myOspfImportAsExtern"),
        ("DES7200-OSPF-MIB", "myOspfSpfRuns"),
        ("DES7200-OSPF-MIB", "myOspfAreaBdrRtrCount"),
        ("DES7200-OSPF-MIB", "myOspfAsBdrRtrCount"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaCount"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaCksumSum"),
        ("DES7200-OSPF-MIB", "myOspfAreaSummary"),
        ("DES7200-OSPF-MIB", "myOspfAreaStatus"),
        ("DES7200-OSPF-MIB", "myOspfAreaInterfaceNum"),
        ("DES7200-OSPF-MIB", "myOspfAreaNssaIsRedistribution"),
        ("DES7200-OSPF-MIB", "myOspfAreaNssaIsDefInfoOriginate"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkAreaID"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkAddress"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkMask"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkStatus"))
)
if mibBuilder.loadTexts:
    myOspfAreaMIBGroup.setStatus("current")

myOspfLsaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 3)
)
myOspfLsaMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfLsdbAreaId"),
        ("DES7200-OSPF-MIB", "myOspfLsdbType"),
        ("DES7200-OSPF-MIB", "myOspfLsdbLsid"),
        ("DES7200-OSPF-MIB", "myOspfLsdbRouterId"),
        ("DES7200-OSPF-MIB", "myOspfLsdbSequence"),
        ("DES7200-OSPF-MIB", "myOspfLsdbAge"),
        ("DES7200-OSPF-MIB", "myOspfLsdbChecksum"),
        ("DES7200-OSPF-MIB", "myOspfLsdbAdvertisement"),
        ("DES7200-OSPF-MIB", "myOspfLsdbLinkNum"),
        ("DES7200-OSPF-MIB", "myOspfLsdbPacketLength"),
        ("DES7200-OSPF-MIB", "myOspfSummaryLsaNetworkMask"),
        ("DES7200-OSPF-MIB", "myOspfSummaryLsaTos0Metric"),
        ("DES7200-OSPF-MIB", "myOspfNssaLsaDetailMetricType"),
        ("DES7200-OSPF-MIB", "myOspfNssaLsaDetailForwardAddr"),
        ("DES7200-OSPF-MIB", "myOspfNssaLsaDetailRouteTag"),
        ("DES7200-OSPF-MIB", "myOspfLsdbOption"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbType"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbLsid"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbRouterId"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbSequence"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbAge"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbChecksum"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbAdvertisement"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbNetworkMask"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbMetricType"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbForwardAddr"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbRouteTag"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbMetric"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbOption"),
        ("DES7200-OSPF-MIB", "myOspfExtLsdbPacketLength"),
        ("DES7200-OSPF-MIB", "myOspfRouterLsaDetailLinkID"),
        ("DES7200-OSPF-MIB", "myOspfRouterLsaDetailLinkType"),
        ("DES7200-OSPF-MIB", "myOspfRouterLsaDetailLinkData"),
        ("DES7200-OSPF-MIB", "myOspfRouterLsaDetailTos0Metric"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkLsaDetailAttachedRouter"),
        ("DES7200-OSPF-MIB", "myOspfNetWorkLsaDetailNetworkMask"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaDBSumAreaId"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaDBSumLsaType"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaDBSumCounts"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaDBSumDeletes"),
        ("DES7200-OSPF-MIB", "myOspfAreaLsaDBSumMaxage"),
        ("DES7200-OSPF-MIB", "myOspfLsaDBSumLsaType"),
        ("DES7200-OSPF-MIB", "myOspfLsaDBSumCounts"),
        ("DES7200-OSPF-MIB", "myOspfLsaDBSumDeletes"),
        ("DES7200-OSPF-MIB", "myOspfLsaDBSumMaxage"))
)
if mibBuilder.loadTexts:
    myOspfLsaMIBGroup.setStatus("current")

myOspfIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 4)
)
myOspfIfMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfIfIpAddress"),
        ("DES7200-OSPF-MIB", "myOspfAddressLessIf"),
        ("DES7200-OSPF-MIB", "myOspfIfAreaId"),
        ("DES7200-OSPF-MIB", "myOspfIfType"),
        ("DES7200-OSPF-MIB", "myOspfIfAdminStat"),
        ("DES7200-OSPF-MIB", "myOspfIfRtrPriority"),
        ("DES7200-OSPF-MIB", "myOspfIfTransitDelay"),
        ("DES7200-OSPF-MIB", "myOspfIfRetransInterval"),
        ("DES7200-OSPF-MIB", "myOspfIfHelloInterval"),
        ("DES7200-OSPF-MIB", "myOspfIfRtrDeadInterval"),
        ("DES7200-OSPF-MIB", "myOspfIfPollInterval"),
        ("DES7200-OSPF-MIB", "myOspfIfState"),
        ("DES7200-OSPF-MIB", "myOspfIfDesignatedRouter"),
        ("DES7200-OSPF-MIB", "myOspfIfBackupDesignatedRouter"),
        ("DES7200-OSPF-MIB", "myOspfIfEvents"),
        ("DES7200-OSPF-MIB", "myOspfIfAuthType"),
        ("DES7200-OSPF-MIB", "myOspfIfAuthKey"),
        ("DES7200-OSPF-MIB", "myOspfIfStatus"),
        ("DES7200-OSPF-MIB", "myOspfIfMulticastForwarding"),
        ("DES7200-OSPF-MIB", "myOspfIfDemand"),
        ("DES7200-OSPF-MIB", "myOspfIfDatabaseFilterAllOut"),
        ("DES7200-OSPF-MIB", "myOspfIfDesignateRouterId"),
        ("DES7200-OSPF-MIB", "myOspfIfBackupDesignateRouterId"),
        ("DES7200-OSPF-MIB", "myOspfIfWaitInternal"),
        ("DES7200-OSPF-MIB", "myOspfIfPassiveStatus"),
        ("DES7200-OSPF-MIB", "myOspfIfCurrentUsedMd5AuthKeyId"),
        ("DES7200-OSPF-MIB", "myOspfIfMd5AuthKeyIf"),
        ("DES7200-OSPF-MIB", "myOspfIfMd5AuthKeyId"),
        ("DES7200-OSPF-MIB", "myOspfIfMd5AuthKey"),
        ("DES7200-OSPF-MIB", "myOspfIfMd5AuthKeySt"))
)
if mibBuilder.loadTexts:
    myOspfIfMIBGroup.setStatus("current")

myOspfVirtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 5)
)
myOspfVirtMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfVirtIfAreaId"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfNeighbor"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfTransitDelay"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfRetransInterval"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfHelloInterval"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfRtrDeadInterval"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfState"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfEvents"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfAuthType"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfAuthKey"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfStatus"),
        ("DES7200-OSPF-MIB", "myOspfVirtCost"),
        ("DES7200-OSPF-MIB", "myOspfVirtNativeIfIndex"),
        ("DES7200-OSPF-MIB", "myOspfVirtLinkState"),
        ("DES7200-OSPF-MIB", "myOspfVirtHelloDueIn"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyAreaId"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyNeighbor"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeyId"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKey"),
        ("DES7200-OSPF-MIB", "myOspfVirtIfMd5AuthKeySt"),
        ("DES7200-OSPF-MIB", "myOspfVirtCurrentUsedMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    myOspfVirtMIBGroup.setStatus("current")

myOspfNeighborMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 6)
)
myOspfNeighborMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfNbrIpAddr"),
        ("DES7200-OSPF-MIB", "myOspfNbrAddressLessIndex"),
        ("DES7200-OSPF-MIB", "myOspfNbrRtrId"),
        ("DES7200-OSPF-MIB", "myOspfNbrOptions"),
        ("DES7200-OSPF-MIB", "myOspfNbrPriority"),
        ("DES7200-OSPF-MIB", "myOspfNbrState"),
        ("DES7200-OSPF-MIB", "myOspfNbrEvents"),
        ("DES7200-OSPF-MIB", "myOspfNbrLsRetransQLen"),
        ("DES7200-OSPF-MIB", "myOspfNbmaNbrStatus"),
        ("DES7200-OSPF-MIB", "myOspfNbmaNbrPermanence"),
        ("DES7200-OSPF-MIB", "myOspfNbrHelloSuppressed"),
        ("DES7200-OSPF-MIB", "myOspfNbrDeadTimeDueIn"),
        ("DES7200-OSPF-MIB", "myOspfNbrNeighborUpTime"),
        ("DES7200-OSPF-MIB", "myOspfNbrDR"),
        ("DES7200-OSPF-MIB", "myOspfNbrBDR"),
        ("DES7200-OSPF-MIB", "myOspfNbrArea"),
        ("DES7200-OSPF-MIB", "myOspfNbrRetransmissionNum"))
)
if mibBuilder.loadTexts:
    myOspfNeighborMIBGroup.setStatus("current")

myOspfRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 2, 7)
)
myOspfRouteInfoMIBGroup.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfRouteType"),
        ("DES7200-OSPF-MIB", "myOspfRouteDest"),
        ("DES7200-OSPF-MIB", "myOspfRouteNextHop"),
        ("DES7200-OSPF-MIB", "myOspfRouteCost"),
        ("DES7200-OSPF-MIB", "myOspfRouteDRType"),
        ("DES7200-OSPF-MIB", "myOspfRouteArea"),
        ("DES7200-OSPF-MIB", "myOspfRouteSpfNo"))
)
if mibBuilder.loadTexts:
    myOspfRouteInfoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myOspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 2, 1, 1)
)
myOspfMIBCompliance.setObjects(
      *(("DES7200-OSPF-MIB", "myOspfBaseMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfAreaMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfLsaMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfIfMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfVirtMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfNeighborMIBGroup"),
        ("DES7200-OSPF-MIB", "myOspfRouteInfoMIBGroup"))
)
if mibBuilder.loadTexts:
    myOspfMIBCompliance.setStatus(
        "current"
    )

ospfExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ospfExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-OSPF-MIB",
    **{"myOspfMIB": myOspfMIB,
       "myOspfMIBObjects": myOspfMIBObjects,
       "myOspfGeneralMibsGroup": myOspfGeneralMibsGroup,
       "myOspfMiniLsaInterval": myOspfMiniLsaInterval,
       "myOspfMiniLsaArrival": myOspfMiniLsaArrival,
       "myOspfAreasNum": myOspfAreasNum,
       "myOspfNormalAreasNum": myOspfNormalAreasNum,
       "myOspfStubAreasNum": myOspfStubAreasNum,
       "myOspfNssaAreasNum": myOspfNssaAreasNum,
       "myOspfSpfDelay": myOspfSpfDelay,
       "myOspfSpfHoldTime": myOspfSpfHoldTime,
       "myOspfAutoCostRefBandWidthRef": myOspfAutoCostRefBandWidthRef,
       "myOspfLsaGroupPacing": myOspfLsaGroupPacing,
       "myOspfInterDistance": myOspfInterDistance,
       "myOspfIntraDistance": myOspfIntraDistance,
       "myOspfExternDistance": myOspfExternDistance,
       "myOspfLogAdjChangeNotify": myOspfLogAdjChangeNotify,
       "myOspfPassiveStatus": myOspfPassiveStatus,
       "myOspfRFC1583Compatibility": myOspfRFC1583Compatibility,
       "myOspfRouteRedisDefMetricVal": myOspfRouteRedisDefMetricVal,
       "myOspfAdminiDistance": myOspfAdminiDistance,
       "myOspfAreaTable": myOspfAreaTable,
       "myOspfAreaEntry": myOspfAreaEntry,
       "myOspfAreaId": myOspfAreaId,
       "myOspfAuthType": myOspfAuthType,
       "myOspfImportAsExtern": myOspfImportAsExtern,
       "myOspfSpfRuns": myOspfSpfRuns,
       "myOspfAreaBdrRtrCount": myOspfAreaBdrRtrCount,
       "myOspfAsBdrRtrCount": myOspfAsBdrRtrCount,
       "myOspfAreaLsaCount": myOspfAreaLsaCount,
       "myOspfAreaLsaCksumSum": myOspfAreaLsaCksumSum,
       "myOspfAreaSummary": myOspfAreaSummary,
       "myOspfAreaStatus": myOspfAreaStatus,
       "myOspfAreaInterfaceNum": myOspfAreaInterfaceNum,
       "myOspfAreaNssaIsRedistribution": myOspfAreaNssaIsRedistribution,
       "myOspfAreaNssaIsDefInfoOriginate": myOspfAreaNssaIsDefInfoOriginate,
       "myOspfAddressScopeTable": myOspfAddressScopeTable,
       "myOspfAddressScopeEntry": myOspfAddressScopeEntry,
       "myOspfNetWorkAreaID": myOspfNetWorkAreaID,
       "myOspfNetWorkAddress": myOspfNetWorkAddress,
       "myOspfNetWorkMask": myOspfNetWorkMask,
       "myOspfNetWorkStatus": myOspfNetWorkStatus,
       "myOspfIfTable": myOspfIfTable,
       "myOspfIfEntry": myOspfIfEntry,
       "myOspfIfIpAddress": myOspfIfIpAddress,
       "myOspfAddressLessIf": myOspfAddressLessIf,
       "myOspfIfAreaId": myOspfIfAreaId,
       "myOspfIfType": myOspfIfType,
       "myOspfIfAdminStat": myOspfIfAdminStat,
       "myOspfIfRtrPriority": myOspfIfRtrPriority,
       "myOspfIfTransitDelay": myOspfIfTransitDelay,
       "myOspfIfRetransInterval": myOspfIfRetransInterval,
       "myOspfIfHelloInterval": myOspfIfHelloInterval,
       "myOspfIfRtrDeadInterval": myOspfIfRtrDeadInterval,
       "myOspfIfPollInterval": myOspfIfPollInterval,
       "myOspfIfState": myOspfIfState,
       "myOspfIfDesignatedRouter": myOspfIfDesignatedRouter,
       "myOspfIfBackupDesignatedRouter": myOspfIfBackupDesignatedRouter,
       "myOspfIfEvents": myOspfIfEvents,
       "myOspfIfAuthKey": myOspfIfAuthKey,
       "myOspfIfStatus": myOspfIfStatus,
       "myOspfIfMulticastForwarding": myOspfIfMulticastForwarding,
       "myOspfIfDemand": myOspfIfDemand,
       "myOspfIfAuthType": myOspfIfAuthType,
       "myOspfIfDatabaseFilterAllOut": myOspfIfDatabaseFilterAllOut,
       "myOspfIfDesignateRouterId": myOspfIfDesignateRouterId,
       "myOspfIfBackupDesignateRouterId": myOspfIfBackupDesignateRouterId,
       "myOspfIfWaitInternal": myOspfIfWaitInternal,
       "myOspfIfPassiveStatus": myOspfIfPassiveStatus,
       "myOspfIfCurrentUsedMd5AuthKeyId": myOspfIfCurrentUsedMd5AuthKeyId,
       "myOspfIfMd5AuthKeyTable": myOspfIfMd5AuthKeyTable,
       "myOspfIfMd5AuthKeyEntry": myOspfIfMd5AuthKeyEntry,
       "myOspfIfMd5AuthKeyIf": myOspfIfMd5AuthKeyIf,
       "myOspfIfMd5AuthKeyId": myOspfIfMd5AuthKeyId,
       "myOspfIfMd5AuthKey": myOspfIfMd5AuthKey,
       "myOspfIfMd5AuthKeySt": myOspfIfMd5AuthKeySt,
       "myOspfVirtTable": myOspfVirtTable,
       "myOspfVirtEntry": myOspfVirtEntry,
       "myOspfVirtIfAreaId": myOspfVirtIfAreaId,
       "myOspfVirtIfNeighbor": myOspfVirtIfNeighbor,
       "myOspfVirtIfTransitDelay": myOspfVirtIfTransitDelay,
       "myOspfVirtIfRetransInterval": myOspfVirtIfRetransInterval,
       "myOspfVirtIfHelloInterval": myOspfVirtIfHelloInterval,
       "myOspfVirtIfRtrDeadInterval": myOspfVirtIfRtrDeadInterval,
       "myOspfVirtIfState": myOspfVirtIfState,
       "myOspfVirtIfEvents": myOspfVirtIfEvents,
       "myOspfVirtIfAuthKey": myOspfVirtIfAuthKey,
       "myOspfVirtIfStatus": myOspfVirtIfStatus,
       "myOspfVirtIfAuthType": myOspfVirtIfAuthType,
       "myOspfVirtCost": myOspfVirtCost,
       "myOspfVirtNativeIfIndex": myOspfVirtNativeIfIndex,
       "myOspfVirtLinkState": myOspfVirtLinkState,
       "myOspfVirtHelloDueIn": myOspfVirtHelloDueIn,
       "myOspfVirtCurrentUsedMd5AuthKeyId": myOspfVirtCurrentUsedMd5AuthKeyId,
       "myOspfVirtIfMd5AuthKeyTable": myOspfVirtIfMd5AuthKeyTable,
       "myOspfVirtIfMd5AuthKeyEntry": myOspfVirtIfMd5AuthKeyEntry,
       "myOspfVirtIfMd5AuthKeyAreaId": myOspfVirtIfMd5AuthKeyAreaId,
       "myOspfVirtIfMd5AuthKeyNeighbor": myOspfVirtIfMd5AuthKeyNeighbor,
       "myOspfVirtIfMd5AuthKeyId": myOspfVirtIfMd5AuthKeyId,
       "myOspfVirtIfMd5AuthKey": myOspfVirtIfMd5AuthKey,
       "myOspfVirtIfMd5AuthKeySt": myOspfVirtIfMd5AuthKeySt,
       "myOspfLsaDetailInfoMibsGroup": myOspfLsaDetailInfoMibsGroup,
       "myOspfLsdbTable": myOspfLsdbTable,
       "myOspfLsdbEntry": myOspfLsdbEntry,
       "myOspfLsdbAreaId": myOspfLsdbAreaId,
       "myOspfLsdbType": myOspfLsdbType,
       "myOspfLsdbLsid": myOspfLsdbLsid,
       "myOspfLsdbRouterId": myOspfLsdbRouterId,
       "myOspfLsdbSequence": myOspfLsdbSequence,
       "myOspfLsdbAge": myOspfLsdbAge,
       "myOspfLsdbChecksum": myOspfLsdbChecksum,
       "myOspfLsdbAdvertisement": myOspfLsdbAdvertisement,
       "myOspfLsdbLinkNum": myOspfLsdbLinkNum,
       "myOspfLsdbPacketLength": myOspfLsdbPacketLength,
       "myOspfSummaryLsaNetworkMask": myOspfSummaryLsaNetworkMask,
       "myOspfSummaryLsaTos0Metric": myOspfSummaryLsaTos0Metric,
       "myOspfNssaLsaDetailMetricType": myOspfNssaLsaDetailMetricType,
       "myOspfNssaLsaDetailForwardAddr": myOspfNssaLsaDetailForwardAddr,
       "myOspfNssaLsaDetailRouteTag": myOspfNssaLsaDetailRouteTag,
       "myOspfLsdbOption": myOspfLsdbOption,
       "myOspfExtLsdbTable": myOspfExtLsdbTable,
       "myOspfExtLsdbEntry": myOspfExtLsdbEntry,
       "myOspfExtLsdbType": myOspfExtLsdbType,
       "myOspfExtLsdbLsid": myOspfExtLsdbLsid,
       "myOspfExtLsdbRouterId": myOspfExtLsdbRouterId,
       "myOspfExtLsdbSequence": myOspfExtLsdbSequence,
       "myOspfExtLsdbAge": myOspfExtLsdbAge,
       "myOspfExtLsdbChecksum": myOspfExtLsdbChecksum,
       "myOspfExtLsdbAdvertisement": myOspfExtLsdbAdvertisement,
       "myOspfExtLsdbNetworkMask": myOspfExtLsdbNetworkMask,
       "myOspfExtLsdbMetric": myOspfExtLsdbMetric,
       "myOspfExtLsdbMetricType": myOspfExtLsdbMetricType,
       "myOspfExtLsdbForwardAddr": myOspfExtLsdbForwardAddr,
       "myOspfExtLsdbRouteTag": myOspfExtLsdbRouteTag,
       "myOspfExtLsdbOption": myOspfExtLsdbOption,
       "myOspfExtLsdbPacketLength": myOspfExtLsdbPacketLength,
       "myOspfRouterLsaDetailTable": myOspfRouterLsaDetailTable,
       "myOspfRouterLsaDetailEntry": myOspfRouterLsaDetailEntry,
       "myOspfRouterLsaDetailLinkID": myOspfRouterLsaDetailLinkID,
       "myOspfRouterLsaDetailLinkType": myOspfRouterLsaDetailLinkType,
       "myOspfRouterLsaDetailLinkData": myOspfRouterLsaDetailLinkData,
       "myOspfRouterLsaDetailTos0Metric": myOspfRouterLsaDetailTos0Metric,
       "myOspfNetWorkLsaDetailTable": myOspfNetWorkLsaDetailTable,
       "myOspfNetWorkLsaDetailEntry": myOspfNetWorkLsaDetailEntry,
       "myOspfNetWorkLsaDetailAttachedRouter": myOspfNetWorkLsaDetailAttachedRouter,
       "myOspfNetWorkLsaDetailNetworkMask": myOspfNetWorkLsaDetailNetworkMask,
       "myOspfAreaLsaDBSumTable": myOspfAreaLsaDBSumTable,
       "myOspfAreaLsaDBSumEntry": myOspfAreaLsaDBSumEntry,
       "myOspfAreaLsaDBSumAreaId": myOspfAreaLsaDBSumAreaId,
       "myOspfAreaLsaDBSumLsaType": myOspfAreaLsaDBSumLsaType,
       "myOspfAreaLsaDBSumCounts": myOspfAreaLsaDBSumCounts,
       "myOspfAreaLsaDBSumDeletes": myOspfAreaLsaDBSumDeletes,
       "myOspfAreaLsaDBSumMaxage": myOspfAreaLsaDBSumMaxage,
       "myOspfLsaDBSumTable": myOspfLsaDBSumTable,
       "myOspfLsaDBSumEntry": myOspfLsaDBSumEntry,
       "myOspfLsaDBSumLsaType": myOspfLsaDBSumLsaType,
       "myOspfLsaDBSumCounts": myOspfLsaDBSumCounts,
       "myOspfLsaDBSumDeletes": myOspfLsaDBSumDeletes,
       "myOspfLsaDBSumMaxage": myOspfLsaDBSumMaxage,
       "myOspfNeighborTable": myOspfNeighborTable,
       "myOspfNeighborEntry": myOspfNeighborEntry,
       "myOspfNbrIpAddr": myOspfNbrIpAddr,
       "myOspfNbrAddressLessIndex": myOspfNbrAddressLessIndex,
       "myOspfNbrRtrId": myOspfNbrRtrId,
       "myOspfNbrOptions": myOspfNbrOptions,
       "myOspfNbrPriority": myOspfNbrPriority,
       "myOspfNbrState": myOspfNbrState,
       "myOspfNbrEvents": myOspfNbrEvents,
       "myOspfNbrLsRetransQLen": myOspfNbrLsRetransQLen,
       "myOspfNbmaNbrStatus": myOspfNbmaNbrStatus,
       "myOspfNbmaNbrPermanence": myOspfNbmaNbrPermanence,
       "myOspfNbrHelloSuppressed": myOspfNbrHelloSuppressed,
       "myOspfNbrDeadTimeDueIn": myOspfNbrDeadTimeDueIn,
       "myOspfNbrNeighborUpTime": myOspfNbrNeighborUpTime,
       "myOspfNbrDR": myOspfNbrDR,
       "myOspfNbrBDR": myOspfNbrBDR,
       "myOspfNbrArea": myOspfNbrArea,
       "myOspfNbrRetransmissionNum": myOspfNbrRetransmissionNum,
       "myOspfNbrIfState": myOspfNbrIfState,
       "myOspfRouteTable": myOspfRouteTable,
       "myOspfRouteEntry": myOspfRouteEntry,
       "myOspfRouteDest": myOspfRouteDest,
       "myOspfRouteArea": myOspfRouteArea,
       "myOspfRouteNextHop": myOspfRouteNextHop,
       "myOspfRouteCost": myOspfRouteCost,
       "myOspfRouteDRType": myOspfRouteDRType,
       "myOspfRouteType": myOspfRouteType,
       "myOspfRouteSpfNo": myOspfRouteSpfNo,
       "myOspfMIBConformance": myOspfMIBConformance,
       "myOspfMIBCompliances": myOspfMIBCompliances,
       "myOspfMIBCompliance": myOspfMIBCompliance,
       "myOspfMIBGroups": myOspfMIBGroups,
       "myOspfBaseMIBGroup": myOspfBaseMIBGroup,
       "myOspfAreaMIBGroup": myOspfAreaMIBGroup,
       "myOspfLsaMIBGroup": myOspfLsaMIBGroup,
       "myOspfIfMIBGroup": myOspfIfMIBGroup,
       "myOspfVirtMIBGroup": myOspfVirtMIBGroup,
       "myOspfNeighborMIBGroup": myOspfNeighborMIBGroup,
       "myOspfRouteInfoMIBGroup": myOspfRouteInfoMIBGroup,
       "ospfMIBConformance": ospfMIBConformance,
       "ospfMIBCompliances": ospfMIBCompliances,
       "ospfExternCompliance": ospfExternCompliance}
)
