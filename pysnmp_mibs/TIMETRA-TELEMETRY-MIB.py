# SNMP MIB module (TIMETRA-TELEMETRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-TELEMETRY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:51:48 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(TDSCPNameOrEmpty,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxHigh32,
 TmnxLow32,
 TmnxOperState,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDSCPNameOrEmpty",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxHigh32",
    "TmnxLow32",
    "TmnxOperState",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraTelemetryMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 110)
)
if mibBuilder.loadTexts:
    timetraTelemetryMIBModule.setRevisions(
        ("2016-10-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxTlmtryGrpcSubMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stream", 0),
          ("once", 1))
    )



class TmnxTlmtryGrpcSubEncoding(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("json", 0),
          ("bytes", 1),
          ("proto", 2))
    )



class TmnxTlmtryGrpcSubPathMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -1),
          ("targetDefined", 0),
          ("onChange", 1),
          ("sample", 2))
    )



class TmnxTlmtryGrpcSubScalePathMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -1),
          ("once", 0),
          ("onChange", 1),
          ("sample", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxTelemetryConformance_ObjectIdentity = ObjectIdentity
tmnxTelemetryConformance = _TmnxTelemetryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110)
)
_TmnxTelemetryCompliances_ObjectIdentity = ObjectIdentity
tmnxTelemetryCompliances = _TmnxTelemetryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110, 1)
)
_TmnxTelemetryGroups_ObjectIdentity = ObjectIdentity
tmnxTelemetryGroups = _TmnxTelemetryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110, 2)
)
_TmnxTelemetryInitialGroups_ObjectIdentity = ObjectIdentity
tmnxTelemetryInitialGroups = _TmnxTelemetryInitialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110, 2, 1)
)
_TmnxTelemetryObjs_ObjectIdentity = ObjectIdentity
tmnxTelemetryObjs = _TmnxTelemetryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110)
)
_TmnxTelemetryStatsObjs_ObjectIdentity = ObjectIdentity
tmnxTelemetryStatsObjs = _TmnxTelemetryStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1)
)
_TmnxTlmtryGrpcSubscrTable_Object = MibTable
tmnxTlmtryGrpcSubscrTable = _TmnxTlmtryGrpcSubscrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrTable.setStatus("current")
_TmnxTlmtryGrpcSubscrEntry_Object = MibTableRow
tmnxTlmtryGrpcSubscrEntry = _TmnxTlmtryGrpcSubscrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1)
)
tmnxTlmtryGrpcSubscrEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubId"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrEntry.setStatus("current")
_TmnxTlmtryGrpcSubId_Type = Unsigned32
_TmnxTlmtryGrpcSubId_Object = MibTableColumn
tmnxTlmtryGrpcSubId = _TmnxTlmtryGrpcSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 1),
    _TmnxTlmtryGrpcSubId_Type()
)
tmnxTlmtryGrpcSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubId.setStatus("current")
_TmnxTlmtryGrpcSubUserName_Type = TNamedItem
_TmnxTlmtryGrpcSubUserName_Object = MibTableColumn
tmnxTlmtryGrpcSubUserName = _TmnxTlmtryGrpcSubUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 2),
    _TmnxTlmtryGrpcSubUserName_Type()
)
tmnxTlmtryGrpcSubUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubUserName.setStatus("current")
_TmnxTlmtryGrpcSubDstIpAddType_Type = InetAddressType
_TmnxTlmtryGrpcSubDstIpAddType_Object = MibTableColumn
tmnxTlmtryGrpcSubDstIpAddType = _TmnxTlmtryGrpcSubDstIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 3),
    _TmnxTlmtryGrpcSubDstIpAddType_Type()
)
tmnxTlmtryGrpcSubDstIpAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubDstIpAddType.setStatus("current")


class _TmnxTlmtryGrpcSubDstIpAddress_Type(InetAddress):
    """Custom type tmnxTlmtryGrpcSubDstIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTlmtryGrpcSubDstIpAddress_Type.__name__ = "InetAddress"
_TmnxTlmtryGrpcSubDstIpAddress_Object = MibTableColumn
tmnxTlmtryGrpcSubDstIpAddress = _TmnxTlmtryGrpcSubDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 4),
    _TmnxTlmtryGrpcSubDstIpAddress_Type()
)
tmnxTlmtryGrpcSubDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubDstIpAddress.setStatus("current")
_TmnxTlmtryGrpcSubDestPort_Type = InetPortNumber
_TmnxTlmtryGrpcSubDestPort_Object = MibTableColumn
tmnxTlmtryGrpcSubDestPort = _TmnxTlmtryGrpcSubDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 5),
    _TmnxTlmtryGrpcSubDestPort_Type()
)
tmnxTlmtryGrpcSubDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubDestPort.setStatus("current")
_TmnxTlmtryGrpcSubMode_Type = TmnxTlmtryGrpcSubMode
_TmnxTlmtryGrpcSubMode_Object = MibTableColumn
tmnxTlmtryGrpcSubMode = _TmnxTlmtryGrpcSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 6),
    _TmnxTlmtryGrpcSubMode_Type()
)
tmnxTlmtryGrpcSubMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubMode.setStatus("current")
_TmnxTlmtryGrpcSubReqQos_Type = TDSCPNameOrEmpty
_TmnxTlmtryGrpcSubReqQos_Object = MibTableColumn
tmnxTlmtryGrpcSubReqQos = _TmnxTlmtryGrpcSubReqQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 7),
    _TmnxTlmtryGrpcSubReqQos_Type()
)
tmnxTlmtryGrpcSubReqQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubReqQos.setStatus("current")
_TmnxTlmtryGrpcSubOperQos_Type = TDSCPNameOrEmpty
_TmnxTlmtryGrpcSubOperQos_Object = MibTableColumn
tmnxTlmtryGrpcSubOperQos = _TmnxTlmtryGrpcSubOperQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 8),
    _TmnxTlmtryGrpcSubOperQos_Type()
)
tmnxTlmtryGrpcSubOperQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubOperQos.setStatus("current")
_TmnxTlmtryGrpcSubEncoding_Type = TmnxTlmtryGrpcSubEncoding
_TmnxTlmtryGrpcSubEncoding_Object = MibTableColumn
tmnxTlmtryGrpcSubEncoding = _TmnxTlmtryGrpcSubEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 9),
    _TmnxTlmtryGrpcSubEncoding_Type()
)
tmnxTlmtryGrpcSubEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubEncoding.setStatus("current")
_TmnxTlmtryGrpcSubNotifCount_Type = Counter64
_TmnxTlmtryGrpcSubNotifCount_Object = MibTableColumn
tmnxTlmtryGrpcSubNotifCount = _TmnxTlmtryGrpcSubNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 1, 1, 10),
    _TmnxTlmtryGrpcSubNotifCount_Type()
)
tmnxTlmtryGrpcSubNotifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubNotifCount.setStatus("current")
_TmnxTlmtryGrpcSubscrPathTable_Object = MibTable
tmnxTlmtryGrpcSubscrPathTable = _TmnxTlmtryGrpcSubscrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrPathTable.setStatus("current")
_TmnxTlmtryGrpcSubscrPathEntry_Object = MibTableRow
tmnxTlmtryGrpcSubscrPathEntry = _TmnxTlmtryGrpcSubscrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1)
)
tmnxTlmtryGrpcSubscrPathEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubId"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrPathEntry.setStatus("current")
_TmnxTlmtryGrpcSubPathIndex_Type = Unsigned32
_TmnxTlmtryGrpcSubPathIndex_Object = MibTableColumn
tmnxTlmtryGrpcSubPathIndex = _TmnxTlmtryGrpcSubPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 1),
    _TmnxTlmtryGrpcSubPathIndex_Type()
)
tmnxTlmtryGrpcSubPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathIndex.setStatus("current")


class _TmnxTlmtryGrpcSubPathPath_Type(OctetString):
    """Custom type tmnxTlmtryGrpcSubPathPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_TmnxTlmtryGrpcSubPathPath_Type.__name__ = "OctetString"
_TmnxTlmtryGrpcSubPathPath_Object = MibTableColumn
tmnxTlmtryGrpcSubPathPath = _TmnxTlmtryGrpcSubPathPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 2),
    _TmnxTlmtryGrpcSubPathPath_Type()
)
tmnxTlmtryGrpcSubPathPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathPath.setStatus("current")
_TmnxTlmtryGrpcSubPathInterval_Type = CounterBasedGauge64
_TmnxTlmtryGrpcSubPathInterval_Object = MibTableColumn
tmnxTlmtryGrpcSubPathInterval = _TmnxTlmtryGrpcSubPathInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 3),
    _TmnxTlmtryGrpcSubPathInterval_Type()
)
tmnxTlmtryGrpcSubPathInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathInterval.setUnits("milliseconds")
_TmnxTlmtryGrpcSubPathFinisColCnt_Type = Counter64
_TmnxTlmtryGrpcSubPathFinisColCnt_Object = MibTableColumn
tmnxTlmtryGrpcSubPathFinisColCnt = _TmnxTlmtryGrpcSubPathFinisColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 4),
    _TmnxTlmtryGrpcSubPathFinisColCnt_Type()
)
tmnxTlmtryGrpcSubPathFinisColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathFinisColCnt.setStatus("current")
_TmnxTlmtryGrpcSubPathDeferColCnt_Type = Counter64
_TmnxTlmtryGrpcSubPathDeferColCnt_Object = MibTableColumn
tmnxTlmtryGrpcSubPathDeferColCnt = _TmnxTlmtryGrpcSubPathDeferColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 5),
    _TmnxTlmtryGrpcSubPathDeferColCnt_Type()
)
tmnxTlmtryGrpcSubPathDeferColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathDeferColCnt.setStatus("current")
_TmnxTlmtryGrpcSubPathTotColTime_Type = Counter64
_TmnxTlmtryGrpcSubPathTotColTime_Object = MibTableColumn
tmnxTlmtryGrpcSubPathTotColTime = _TmnxTlmtryGrpcSubPathTotColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 6),
    _TmnxTlmtryGrpcSubPathTotColTime_Type()
)
tmnxTlmtryGrpcSubPathTotColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathTotColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathTotColTime.setUnits("milliseconds")
_TmnxTlmtryGrpcSubPathMinColTime_Type = Counter32
_TmnxTlmtryGrpcSubPathMinColTime_Object = MibTableColumn
tmnxTlmtryGrpcSubPathMinColTime = _TmnxTlmtryGrpcSubPathMinColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 7),
    _TmnxTlmtryGrpcSubPathMinColTime_Type()
)
tmnxTlmtryGrpcSubPathMinColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathMinColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathMinColTime.setUnits("milliseconds")
_TmnxTlmtryGrpcSubPathAvgColTime_Type = Counter32
_TmnxTlmtryGrpcSubPathAvgColTime_Object = MibTableColumn
tmnxTlmtryGrpcSubPathAvgColTime = _TmnxTlmtryGrpcSubPathAvgColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 8),
    _TmnxTlmtryGrpcSubPathAvgColTime_Type()
)
tmnxTlmtryGrpcSubPathAvgColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathAvgColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathAvgColTime.setUnits("milliseconds")
_TmnxTlmtryGrpcSubPathMaxColTime_Type = Counter32
_TmnxTlmtryGrpcSubPathMaxColTime_Object = MibTableColumn
tmnxTlmtryGrpcSubPathMaxColTime = _TmnxTlmtryGrpcSubPathMaxColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 9),
    _TmnxTlmtryGrpcSubPathMaxColTime_Type()
)
tmnxTlmtryGrpcSubPathMaxColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathMaxColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathMaxColTime.setUnits("milliseconds")
_TmnxTlmtryGrpcSubPathMode_Type = TmnxTlmtryGrpcSubPathMode
_TmnxTlmtryGrpcSubPathMode_Object = MibTableColumn
tmnxTlmtryGrpcSubPathMode = _TmnxTlmtryGrpcSubPathMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 2, 1, 10),
    _TmnxTlmtryGrpcSubPathMode_Type()
)
tmnxTlmtryGrpcSubPathMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubPathMode.setStatus("current")
_TmnxTlmtryGrpcSubscrSclPathTable_Object = MibTable
tmnxTlmtryGrpcSubscrSclPathTable = _TmnxTlmtryGrpcSubscrSclPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrSclPathTable.setStatus("current")
_TmnxTlmtryGrpcSubscrSclPathEntry_Object = MibTableRow
tmnxTlmtryGrpcSubscrSclPathEntry = _TmnxTlmtryGrpcSubscrSclPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1)
)
tmnxTlmtryGrpcSubscrSclPathEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubId"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubSclPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubscrSclPathEntry.setStatus("current")
_TmnxTlmtryGrpcSubSclPathIndex_Type = Unsigned32
_TmnxTlmtryGrpcSubSclPathIndex_Object = MibTableColumn
tmnxTlmtryGrpcSubSclPathIndex = _TmnxTlmtryGrpcSubSclPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 1),
    _TmnxTlmtryGrpcSubSclPathIndex_Type()
)
tmnxTlmtryGrpcSubSclPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmtryGrpcSubSclPathIndex.setStatus("current")


class _TmnxTlmGrpcSubSclPathPath_Type(OctetString):
    """Custom type tmnxTlmGrpcSubSclPathPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_TmnxTlmGrpcSubSclPathPath_Type.__name__ = "OctetString"
_TmnxTlmGrpcSubSclPathPath_Object = MibTableColumn
tmnxTlmGrpcSubSclPathPath = _TmnxTlmGrpcSubSclPathPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 2),
    _TmnxTlmGrpcSubSclPathPath_Type()
)
tmnxTlmGrpcSubSclPathPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathPath.setStatus("current")
_TmnxTlmGrpcSubSclPathInterval_Type = CounterBasedGauge64
_TmnxTlmGrpcSubSclPathInterval_Object = MibTableColumn
tmnxTlmGrpcSubSclPathInterval = _TmnxTlmGrpcSubSclPathInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 3),
    _TmnxTlmGrpcSubSclPathInterval_Type()
)
tmnxTlmGrpcSubSclPathInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathInterval.setUnits("milliseconds")
_TmnxTlmGrpcSubSclPathFinisColCnt_Type = Counter64
_TmnxTlmGrpcSubSclPathFinisColCnt_Object = MibTableColumn
tmnxTlmGrpcSubSclPathFinisColCnt = _TmnxTlmGrpcSubSclPathFinisColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 4),
    _TmnxTlmGrpcSubSclPathFinisColCnt_Type()
)
tmnxTlmGrpcSubSclPathFinisColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathFinisColCnt.setStatus("current")
_TmnxTlmGrpcSubSclPathDeferColCnt_Type = Counter64
_TmnxTlmGrpcSubSclPathDeferColCnt_Object = MibTableColumn
tmnxTlmGrpcSubSclPathDeferColCnt = _TmnxTlmGrpcSubSclPathDeferColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 5),
    _TmnxTlmGrpcSubSclPathDeferColCnt_Type()
)
tmnxTlmGrpcSubSclPathDeferColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathDeferColCnt.setStatus("current")
_TmnxTlmGrpcSubSclPathTotColTime_Type = Counter64
_TmnxTlmGrpcSubSclPathTotColTime_Object = MibTableColumn
tmnxTlmGrpcSubSclPathTotColTime = _TmnxTlmGrpcSubSclPathTotColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 6),
    _TmnxTlmGrpcSubSclPathTotColTime_Type()
)
tmnxTlmGrpcSubSclPathTotColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathTotColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathTotColTime.setUnits("milliseconds")
_TmnxTlmGrpcSubSclPathMinColTime_Type = Counter32
_TmnxTlmGrpcSubSclPathMinColTime_Object = MibTableColumn
tmnxTlmGrpcSubSclPathMinColTime = _TmnxTlmGrpcSubSclPathMinColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 7),
    _TmnxTlmGrpcSubSclPathMinColTime_Type()
)
tmnxTlmGrpcSubSclPathMinColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathMinColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathMinColTime.setUnits("milliseconds")
_TmnxTlmGrpcSubSclPathAvgColTime_Type = Counter32
_TmnxTlmGrpcSubSclPathAvgColTime_Object = MibTableColumn
tmnxTlmGrpcSubSclPathAvgColTime = _TmnxTlmGrpcSubSclPathAvgColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 8),
    _TmnxTlmGrpcSubSclPathAvgColTime_Type()
)
tmnxTlmGrpcSubSclPathAvgColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathAvgColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathAvgColTime.setUnits("milliseconds")
_TmnxTlmGrpcSubSclPathMaxColTime_Type = Counter32
_TmnxTlmGrpcSubSclPathMaxColTime_Object = MibTableColumn
tmnxTlmGrpcSubSclPathMaxColTime = _TmnxTlmGrpcSubSclPathMaxColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 9),
    _TmnxTlmGrpcSubSclPathMaxColTime_Type()
)
tmnxTlmGrpcSubSclPathMaxColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathMaxColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathMaxColTime.setUnits("milliseconds")
_TmnxTlmGrpcSubSclPathMode_Type = TmnxTlmtryGrpcSubScalePathMode
_TmnxTlmGrpcSubSclPathMode_Object = MibTableColumn
tmnxTlmGrpcSubSclPathMode = _TmnxTlmGrpcSubSclPathMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 1, 3, 1, 10),
    _TmnxTlmGrpcSubSclPathMode_Type()
)
tmnxTlmGrpcSubSclPathMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmGrpcSubSclPathMode.setStatus("current")
_TmnxTelemetryScalarObjs_ObjectIdentity = ObjectIdentity
tmnxTelemetryScalarObjs = _TmnxTelemetryScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2)
)
_TmnxTelemetryLastChangedObjs_ObjectIdentity = ObjectIdentity
tmnxTelemetryLastChangedObjs = _TmnxTelemetryLastChangedObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1)
)
_TmnxTlmDestGrpTblLastChgd_Type = TimeStamp
_TmnxTlmDestGrpTblLastChgd_Object = MibScalar
tmnxTlmDestGrpTblLastChgd = _TmnxTlmDestGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1, 1),
    _TmnxTlmDestGrpTblLastChgd_Type()
)
tmnxTlmDestGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTblLastChgd.setStatus("current")
_TmnxTlmDestGrpDestTblLastChgd_Type = TimeStamp
_TmnxTlmDestGrpDestTblLastChgd_Object = MibScalar
tmnxTlmDestGrpDestTblLastChgd = _TmnxTlmDestGrpDestTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1, 2),
    _TmnxTlmDestGrpDestTblLastChgd_Type()
)
tmnxTlmDestGrpDestTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestTblLastChgd.setStatus("current")
_TmnxTlmSensGrpTblLastChgd_Type = TimeStamp
_TmnxTlmSensGrpTblLastChgd_Object = MibScalar
tmnxTlmSensGrpTblLastChgd = _TmnxTlmSensGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1, 3),
    _TmnxTlmSensGrpTblLastChgd_Type()
)
tmnxTlmSensGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpTblLastChgd.setStatus("current")
_TmnxTlmSensGrpPathTblLastChgd_Type = TimeStamp
_TmnxTlmSensGrpPathTblLastChgd_Object = MibScalar
tmnxTlmSensGrpPathTblLastChgd = _TmnxTlmSensGrpPathTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1, 4),
    _TmnxTlmSensGrpPathTblLastChgd_Type()
)
tmnxTlmSensGrpPathTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathTblLastChgd.setStatus("current")
_TmnxTlmPersSubTblLastChgd_Type = TimeStamp
_TmnxTlmPersSubTblLastChgd_Object = MibScalar
tmnxTlmPersSubTblLastChgd = _TmnxTlmPersSubTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 2, 1, 5),
    _TmnxTlmPersSubTblLastChgd_Type()
)
tmnxTlmPersSubTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubTblLastChgd.setStatus("current")
_TmnxTelemetryConfigObjs_ObjectIdentity = ObjectIdentity
tmnxTelemetryConfigObjs = _TmnxTelemetryConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3)
)
_TmnxTlmtryDestGroupTable_Object = MibTable
tmnxTlmtryDestGroupTable = _TmnxTlmtryDestGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxTlmtryDestGroupTable.setStatus("current")
_TmnxTlmtryDestGroupEntry_Object = MibTableRow
tmnxTlmtryDestGroupEntry = _TmnxTlmtryDestGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1)
)
tmnxTlmtryDestGroupEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpName"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryDestGroupEntry.setStatus("current")
_TmnxTlmDestGrpName_Type = TNamedItem
_TmnxTlmDestGrpName_Object = MibTableColumn
tmnxTlmDestGrpName = _TmnxTlmDestGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 1),
    _TmnxTlmDestGrpName_Type()
)
tmnxTlmDestGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpName.setStatus("current")
_TmnxTlmDestGrpLastChgd_Type = TimeStamp
_TmnxTlmDestGrpLastChgd_Object = MibTableColumn
tmnxTlmDestGrpLastChgd = _TmnxTlmDestGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 2),
    _TmnxTlmDestGrpLastChgd_Type()
)
tmnxTlmDestGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpLastChgd.setStatus("current")
_TmnxTlmDestGrpRowStatus_Type = RowStatus
_TmnxTlmDestGrpRowStatus_Object = MibTableColumn
tmnxTlmDestGrpRowStatus = _TmnxTlmDestGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 3),
    _TmnxTlmDestGrpRowStatus_Type()
)
tmnxTlmDestGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpRowStatus.setStatus("current")
_TmnxTlmDestGrpDescription_Type = TItemDescription
_TmnxTlmDestGrpDescription_Object = MibTableColumn
tmnxTlmDestGrpDescription = _TmnxTlmDestGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 4),
    _TmnxTlmDestGrpDescription_Type()
)
tmnxTlmDestGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDescription.setStatus("current")


class _TmnxTlmDestGrpTlsClientProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxTlmDestGrpTlsClientProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxTlmDestGrpTlsClientProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxTlmDestGrpTlsClientProf_Object = MibTableColumn
tmnxTlmDestGrpTlsClientProf = _TmnxTlmDestGrpTlsClientProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 5),
    _TmnxTlmDestGrpTlsClientProf_Type()
)
tmnxTlmDestGrpTlsClientProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTlsClientProf.setStatus("current")


class _TmnxTlmDestGrpAllowUnsecConn_Type(TruthValue):
    """Custom type tmnxTlmDestGrpAllowUnsecConn based on TruthValue"""
    defaultValue = 2


_TmnxTlmDestGrpAllowUnsecConn_Type.__name__ = "TruthValue"
_TmnxTlmDestGrpAllowUnsecConn_Object = MibTableColumn
tmnxTlmDestGrpAllowUnsecConn = _TmnxTlmDestGrpAllowUnsecConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 6),
    _TmnxTlmDestGrpAllowUnsecConn_Type()
)
tmnxTlmDestGrpAllowUnsecConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpAllowUnsecConn.setStatus("current")


class _TmnxTlmDestGrpTcpKaAdminState_Type(TmnxAdminState):
    """Custom type tmnxTlmDestGrpTcpKaAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxTlmDestGrpTcpKaAdminState_Type.__name__ = "TmnxAdminState"
_TmnxTlmDestGrpTcpKaAdminState_Object = MibTableColumn
tmnxTlmDestGrpTcpKaAdminState = _TmnxTlmDestGrpTcpKaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 7),
    _TmnxTlmDestGrpTcpKaAdminState_Type()
)
tmnxTlmDestGrpTcpKaAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaAdminState.setStatus("current")


class _TmnxTlmDestGrpTcpKaIdle_Type(Unsigned32):
    """Custom type tmnxTlmDestGrpTcpKaIdle based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxTlmDestGrpTcpKaIdle_Type.__name__ = "Unsigned32"
_TmnxTlmDestGrpTcpKaIdle_Object = MibTableColumn
tmnxTlmDestGrpTcpKaIdle = _TmnxTlmDestGrpTcpKaIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 8),
    _TmnxTlmDestGrpTcpKaIdle_Type()
)
tmnxTlmDestGrpTcpKaIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaIdle.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaIdle.setUnits("seconds")


class _TmnxTlmDestGrpTcpKaInterval_Type(Unsigned32):
    """Custom type tmnxTlmDestGrpTcpKaInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxTlmDestGrpTcpKaInterval_Type.__name__ = "Unsigned32"
_TmnxTlmDestGrpTcpKaInterval_Object = MibTableColumn
tmnxTlmDestGrpTcpKaInterval = _TmnxTlmDestGrpTcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 9),
    _TmnxTlmDestGrpTcpKaInterval_Type()
)
tmnxTlmDestGrpTcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaInterval.setUnits("seconds")


class _TmnxTlmDestGrpTcpKaCount_Type(Unsigned32):
    """Custom type tmnxTlmDestGrpTcpKaCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxTlmDestGrpTcpKaCount_Type.__name__ = "Unsigned32"
_TmnxTlmDestGrpTcpKaCount_Object = MibTableColumn
tmnxTlmDestGrpTcpKaCount = _TmnxTlmDestGrpTcpKaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 1, 1, 10),
    _TmnxTlmDestGrpTcpKaCount_Type()
)
tmnxTlmDestGrpTcpKaCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpTcpKaCount.setStatus("current")
_TmnxTlmtryDestGroupDestTable_Object = MibTable
tmnxTlmtryDestGroupDestTable = _TmnxTlmtryDestGroupDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxTlmtryDestGroupDestTable.setStatus("current")
_TmnxTlmtryDestGroupDestEntry_Object = MibTableRow
tmnxTlmtryDestGroupDestEntry = _TmnxTlmtryDestGroupDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1)
)
tmnxTlmtryDestGroupDestEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpName"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryDestGroupDestEntry.setStatus("current")


class _TmnxTlmDestGrpDestIndex_Type(Unsigned32):
    """Custom type tmnxTlmDestGrpDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTlmDestGrpDestIndex_Type.__name__ = "Unsigned32"
_TmnxTlmDestGrpDestIndex_Object = MibTableColumn
tmnxTlmDestGrpDestIndex = _TmnxTlmDestGrpDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 1),
    _TmnxTlmDestGrpDestIndex_Type()
)
tmnxTlmDestGrpDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestIndex.setStatus("current")
_TmnxTlmDestGrpDestAddType_Type = InetAddressType
_TmnxTlmDestGrpDestAddType_Object = MibTableColumn
tmnxTlmDestGrpDestAddType = _TmnxTlmDestGrpDestAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 2),
    _TmnxTlmDestGrpDestAddType_Type()
)
tmnxTlmDestGrpDestAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestAddType.setStatus("current")


class _TmnxTlmDestGrpDestAddress_Type(InetAddress):
    """Custom type tmnxTlmDestGrpDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxTlmDestGrpDestAddress_Type.__name__ = "InetAddress"
_TmnxTlmDestGrpDestAddress_Object = MibTableColumn
tmnxTlmDestGrpDestAddress = _TmnxTlmDestGrpDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 3),
    _TmnxTlmDestGrpDestAddress_Type()
)
tmnxTlmDestGrpDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestAddress.setStatus("current")
_TmnxTlmDestGrpDestPort_Type = InetPortNumber
_TmnxTlmDestGrpDestPort_Object = MibTableColumn
tmnxTlmDestGrpDestPort = _TmnxTlmDestGrpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 4),
    _TmnxTlmDestGrpDestPort_Type()
)
tmnxTlmDestGrpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestPort.setStatus("current")


class _TmnxTlmDestGrpDestVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxTlmDestGrpDestVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxTlmDestGrpDestVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxTlmDestGrpDestVRtrId_Object = MibTableColumn
tmnxTlmDestGrpDestVRtrId = _TmnxTlmDestGrpDestVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 5),
    _TmnxTlmDestGrpDestVRtrId_Type()
)
tmnxTlmDestGrpDestVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestVRtrId.setStatus("current")
_TmnxTlmDestGrpDestLastChgd_Type = TimeStamp
_TmnxTlmDestGrpDestLastChgd_Object = MibTableColumn
tmnxTlmDestGrpDestLastChgd = _TmnxTlmDestGrpDestLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 6),
    _TmnxTlmDestGrpDestLastChgd_Type()
)
tmnxTlmDestGrpDestLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestLastChgd.setStatus("current")
_TmnxTlmDestGrpDestRowStatus_Type = RowStatus
_TmnxTlmDestGrpDestRowStatus_Object = MibTableColumn
tmnxTlmDestGrpDestRowStatus = _TmnxTlmDestGrpDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 2, 1, 7),
    _TmnxTlmDestGrpDestRowStatus_Type()
)
tmnxTlmDestGrpDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmDestGrpDestRowStatus.setStatus("current")
_TmnxTlmtrySensGroupTable_Object = MibTable
tmnxTlmtrySensGroupTable = _TmnxTlmtrySensGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxTlmtrySensGroupTable.setStatus("current")
_TmnxTlmtrySensGroupEntry_Object = MibTableRow
tmnxTlmtrySensGroupEntry = _TmnxTlmtrySensGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3, 1)
)
tmnxTlmtrySensGroupEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpName"),
)
if mibBuilder.loadTexts:
    tmnxTlmtrySensGroupEntry.setStatus("current")
_TmnxTlmSensGrpName_Type = TNamedItem
_TmnxTlmSensGrpName_Object = MibTableColumn
tmnxTlmSensGrpName = _TmnxTlmSensGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3, 1, 1),
    _TmnxTlmSensGrpName_Type()
)
tmnxTlmSensGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpName.setStatus("current")
_TmnxTlmSensGrpLastChgd_Type = TimeStamp
_TmnxTlmSensGrpLastChgd_Object = MibTableColumn
tmnxTlmSensGrpLastChgd = _TmnxTlmSensGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3, 1, 2),
    _TmnxTlmSensGrpLastChgd_Type()
)
tmnxTlmSensGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpLastChgd.setStatus("current")
_TmnxTlmSensGrpRowStatus_Type = RowStatus
_TmnxTlmSensGrpRowStatus_Object = MibTableColumn
tmnxTlmSensGrpRowStatus = _TmnxTlmSensGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3, 1, 3),
    _TmnxTlmSensGrpRowStatus_Type()
)
tmnxTlmSensGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpRowStatus.setStatus("current")
_TmnxTlmSensGrpDescription_Type = TItemDescription
_TmnxTlmSensGrpDescription_Object = MibTableColumn
tmnxTlmSensGrpDescription = _TmnxTlmSensGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 3, 1, 4),
    _TmnxTlmSensGrpDescription_Type()
)
tmnxTlmSensGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpDescription.setStatus("current")
_TmnxTlmtrySensGroupPathTable_Object = MibTable
tmnxTlmtrySensGroupPathTable = _TmnxTlmtrySensGroupPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxTlmtrySensGroupPathTable.setStatus("current")
_TmnxTlmtrySensGroupPathEntry_Object = MibTableRow
tmnxTlmtrySensGroupPathEntry = _TmnxTlmtrySensGroupPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1)
)
tmnxTlmtrySensGroupPathEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpName"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtrySensGroupPathEntry.setStatus("current")


class _TmnxTlmSensGrpPathIndex_Type(Unsigned32):
    """Custom type tmnxTlmSensGrpPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4500),
    )


_TmnxTlmSensGrpPathIndex_Type.__name__ = "Unsigned32"
_TmnxTlmSensGrpPathIndex_Object = MibTableColumn
tmnxTlmSensGrpPathIndex = _TmnxTlmSensGrpPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1, 1),
    _TmnxTlmSensGrpPathIndex_Type()
)
tmnxTlmSensGrpPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathIndex.setStatus("current")
_TmnxTlmSensGrpPathLastChgd_Type = TimeStamp
_TmnxTlmSensGrpPathLastChgd_Object = MibTableColumn
tmnxTlmSensGrpPathLastChgd = _TmnxTlmSensGrpPathLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1, 2),
    _TmnxTlmSensGrpPathLastChgd_Type()
)
tmnxTlmSensGrpPathLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathLastChgd.setStatus("current")
_TmnxTlmSensGrpPathRowStatus_Type = RowStatus
_TmnxTlmSensGrpPathRowStatus_Object = MibTableColumn
tmnxTlmSensGrpPathRowStatus = _TmnxTlmSensGrpPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1, 3),
    _TmnxTlmSensGrpPathRowStatus_Type()
)
tmnxTlmSensGrpPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathRowStatus.setStatus("current")


class _TmnxTlmSensGrpPathPath_Type(OctetString):
    """Custom type tmnxTlmSensGrpPathPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_TmnxTlmSensGrpPathPath_Type.__name__ = "OctetString"
_TmnxTlmSensGrpPathPath_Object = MibTableColumn
tmnxTlmSensGrpPathPath = _TmnxTlmSensGrpPathPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1, 4),
    _TmnxTlmSensGrpPathPath_Type()
)
tmnxTlmSensGrpPathPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathPath.setStatus("current")


class _TmnxTlmSensGrpPathErrorReason_Type(OctetString):
    """Custom type tmnxTlmSensGrpPathErrorReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxTlmSensGrpPathErrorReason_Type.__name__ = "OctetString"
_TmnxTlmSensGrpPathErrorReason_Object = MibTableColumn
tmnxTlmSensGrpPathErrorReason = _TmnxTlmSensGrpPathErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 4, 1, 5),
    _TmnxTlmSensGrpPathErrorReason_Type()
)
tmnxTlmSensGrpPathErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmSensGrpPathErrorReason.setStatus("current")
_TmnxTlmtryPersSubscrTable_Object = MibTable
tmnxTlmtryPersSubscrTable = _TmnxTlmtryPersSubscrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrTable.setStatus("current")
_TmnxTlmtryPersSubscrEntry_Object = MibTableRow
tmnxTlmtryPersSubscrEntry = _TmnxTlmtryPersSubscrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1)
)
tmnxTlmtryPersSubscrEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubName"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrEntry.setStatus("current")
_TmnxTlmPersSubName_Type = TNamedItem
_TmnxTlmPersSubName_Object = MibTableColumn
tmnxTlmPersSubName = _TmnxTlmPersSubName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 1),
    _TmnxTlmPersSubName_Type()
)
tmnxTlmPersSubName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmPersSubName.setStatus("current")
_TmnxTlmPersSubLastChgd_Type = TimeStamp
_TmnxTlmPersSubLastChgd_Object = MibTableColumn
tmnxTlmPersSubLastChgd = _TmnxTlmPersSubLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 2),
    _TmnxTlmPersSubLastChgd_Type()
)
tmnxTlmPersSubLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubLastChgd.setStatus("current")
_TmnxTlmPersSubRowStatus_Type = RowStatus
_TmnxTlmPersSubRowStatus_Object = MibTableColumn
tmnxTlmPersSubRowStatus = _TmnxTlmPersSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 3),
    _TmnxTlmPersSubRowStatus_Type()
)
tmnxTlmPersSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubRowStatus.setStatus("current")


class _TmnxTlmPersSubAdminState_Type(TmnxAdminState):
    """Custom type tmnxTlmPersSubAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxTlmPersSubAdminState_Type.__name__ = "TmnxAdminState"
_TmnxTlmPersSubAdminState_Object = MibTableColumn
tmnxTlmPersSubAdminState = _TmnxTlmPersSubAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 4),
    _TmnxTlmPersSubAdminState_Type()
)
tmnxTlmPersSubAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubAdminState.setStatus("current")
_TmnxTlmPersSubOperState_Type = TmnxOperState
_TmnxTlmPersSubOperState_Object = MibTableColumn
tmnxTlmPersSubOperState = _TmnxTlmPersSubOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 5),
    _TmnxTlmPersSubOperState_Type()
)
tmnxTlmPersSubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubOperState.setStatus("current")


class _TmnxTlmPersSubOperDownReason_Type(OctetString):
    """Custom type tmnxTlmPersSubOperDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxTlmPersSubOperDownReason_Type.__name__ = "OctetString"
_TmnxTlmPersSubOperDownReason_Object = MibTableColumn
tmnxTlmPersSubOperDownReason = _TmnxTlmPersSubOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 6),
    _TmnxTlmPersSubOperDownReason_Type()
)
tmnxTlmPersSubOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubOperDownReason.setStatus("current")
_TmnxTlmPersSubSubscrId_Type = Unsigned32
_TmnxTlmPersSubSubscrId_Object = MibTableColumn
tmnxTlmPersSubSubscrId = _TmnxTlmPersSubSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 7),
    _TmnxTlmPersSubSubscrId_Type()
)
tmnxTlmPersSubSubscrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSubscrId.setStatus("current")
_TmnxTlmPersSubDescription_Type = TItemDescription
_TmnxTlmPersSubDescription_Object = MibTableColumn
tmnxTlmPersSubDescription = _TmnxTlmPersSubDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 8),
    _TmnxTlmPersSubDescription_Type()
)
tmnxTlmPersSubDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDescription.setStatus("current")


class _TmnxTlmPersSubSensGrp_Type(TNamedItemOrEmpty):
    """Custom type tmnxTlmPersSubSensGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxTlmPersSubSensGrp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxTlmPersSubSensGrp_Object = MibTableColumn
tmnxTlmPersSubSensGrp = _TmnxTlmPersSubSensGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 9),
    _TmnxTlmPersSubSensGrp_Type()
)
tmnxTlmPersSubSensGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSensGrp.setStatus("current")


class _TmnxTlmPersSubMode_Type(TmnxTlmtryGrpcSubPathMode):
    """Custom type tmnxTlmPersSubMode based on TmnxTlmtryGrpcSubPathMode"""
    defaultValue = -1


_TmnxTlmPersSubMode_Type.__name__ = "TmnxTlmtryGrpcSubPathMode"
_TmnxTlmPersSubMode_Object = MibTableColumn
tmnxTlmPersSubMode = _TmnxTlmPersSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 10),
    _TmnxTlmPersSubMode_Type()
)
tmnxTlmPersSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubMode.setStatus("current")


class _TmnxTlmPersSubSmplIntervalHi_Type(TmnxHigh32):
    """Custom type tmnxTlmPersSubSmplIntervalHi based on TmnxHigh32"""
    defaultValue = 0


_TmnxTlmPersSubSmplIntervalHi_Type.__name__ = "TmnxHigh32"
_TmnxTlmPersSubSmplIntervalHi_Object = MibTableColumn
tmnxTlmPersSubSmplIntervalHi = _TmnxTlmPersSubSmplIntervalHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 11),
    _TmnxTlmPersSubSmplIntervalHi_Type()
)
tmnxTlmPersSubSmplIntervalHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSmplIntervalHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSmplIntervalHi.setUnits("milliseconds")


class _TmnxTlmPersSubSmplIntervalLo_Type(TmnxLow32):
    """Custom type tmnxTlmPersSubSmplIntervalLo based on TmnxLow32"""
    defaultValue = 10000


_TmnxTlmPersSubSmplIntervalLo_Type.__name__ = "TmnxLow32"
_TmnxTlmPersSubSmplIntervalLo_Object = MibTableColumn
tmnxTlmPersSubSmplIntervalLo = _TmnxTlmPersSubSmplIntervalLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 12),
    _TmnxTlmPersSubSmplIntervalLo_Type()
)
tmnxTlmPersSubSmplIntervalLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSmplIntervalLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSmplIntervalLo.setUnits("milliseconds")


class _TmnxTlmPersSubDestGrp_Type(TNamedItemOrEmpty):
    """Custom type tmnxTlmPersSubDestGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxTlmPersSubDestGrp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxTlmPersSubDestGrp_Object = MibTableColumn
tmnxTlmPersSubDestGrp = _TmnxTlmPersSubDestGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 13),
    _TmnxTlmPersSubDestGrp_Type()
)
tmnxTlmPersSubDestGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestGrp.setStatus("current")


class _TmnxTlmPersSubLocalSrcAddType_Type(InetAddressType):
    """Custom type tmnxTlmPersSubLocalSrcAddType based on InetAddressType"""
    defaultValue = 0


_TmnxTlmPersSubLocalSrcAddType_Type.__name__ = "InetAddressType"
_TmnxTlmPersSubLocalSrcAddType_Object = MibTableColumn
tmnxTlmPersSubLocalSrcAddType = _TmnxTlmPersSubLocalSrcAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 14),
    _TmnxTlmPersSubLocalSrcAddType_Type()
)
tmnxTlmPersSubLocalSrcAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubLocalSrcAddType.setStatus("current")


class _TmnxTlmPersSubLocalSrcAddress_Type(InetAddress):
    """Custom type tmnxTlmPersSubLocalSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTlmPersSubLocalSrcAddress_Type.__name__ = "InetAddress"
_TmnxTlmPersSubLocalSrcAddress_Object = MibTableColumn
tmnxTlmPersSubLocalSrcAddress = _TmnxTlmPersSubLocalSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 15),
    _TmnxTlmPersSubLocalSrcAddress_Type()
)
tmnxTlmPersSubLocalSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubLocalSrcAddress.setStatus("current")


class _TmnxTlmPersSubOrigQosMarking_Type(TDSCPNameOrEmpty):
    """Custom type tmnxTlmPersSubOrigQosMarking based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TmnxTlmPersSubOrigQosMarking_Type.__name__ = "TDSCPNameOrEmpty"
_TmnxTlmPersSubOrigQosMarking_Object = MibTableColumn
tmnxTlmPersSubOrigQosMarking = _TmnxTlmPersSubOrigQosMarking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 16),
    _TmnxTlmPersSubOrigQosMarking_Type()
)
tmnxTlmPersSubOrigQosMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubOrigQosMarking.setStatus("current")


class _TmnxTlmPersSubEncoding_Type(TmnxTlmtryGrpcSubEncoding):
    """Custom type tmnxTlmPersSubEncoding based on TmnxTlmtryGrpcSubEncoding"""
    defaultValue = 0


_TmnxTlmPersSubEncoding_Type.__name__ = "TmnxTlmtryGrpcSubEncoding"
_TmnxTlmPersSubEncoding_Object = MibTableColumn
tmnxTlmPersSubEncoding = _TmnxTlmPersSubEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 5, 1, 17),
    _TmnxTlmPersSubEncoding_Type()
)
tmnxTlmPersSubEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTlmPersSubEncoding.setStatus("current")
_TmnxTlmtryPersSubscrDestTable_Object = MibTable
tmnxTlmtryPersSubscrDestTable = _TmnxTlmtryPersSubscrDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrDestTable.setStatus("current")
_TmnxTlmtryPersSubscrDestEntry_Object = MibTableRow
tmnxTlmtryPersSubscrDestEntry = _TmnxTlmtryPersSubscrDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1)
)
tmnxTlmtryPersSubscrDestEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubName"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrDestEntry.setStatus("current")


class _TmnxTlmPersSubDestIndex_Type(Unsigned32):
    """Custom type tmnxTlmPersSubDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTlmPersSubDestIndex_Type.__name__ = "Unsigned32"
_TmnxTlmPersSubDestIndex_Object = MibTableColumn
tmnxTlmPersSubDestIndex = _TmnxTlmPersSubDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 1),
    _TmnxTlmPersSubDestIndex_Type()
)
tmnxTlmPersSubDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestIndex.setStatus("current")
_TmnxTlmPersSubDestAddType_Type = InetAddressType
_TmnxTlmPersSubDestAddType_Object = MibTableColumn
tmnxTlmPersSubDestAddType = _TmnxTlmPersSubDestAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 2),
    _TmnxTlmPersSubDestAddType_Type()
)
tmnxTlmPersSubDestAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestAddType.setStatus("current")


class _TmnxTlmPersSubDestAddress_Type(InetAddress):
    """Custom type tmnxTlmPersSubDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxTlmPersSubDestAddress_Type.__name__ = "InetAddress"
_TmnxTlmPersSubDestAddress_Object = MibTableColumn
tmnxTlmPersSubDestAddress = _TmnxTlmPersSubDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 3),
    _TmnxTlmPersSubDestAddress_Type()
)
tmnxTlmPersSubDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestAddress.setStatus("current")
_TmnxTlmPersSubDestPort_Type = InetPortNumber
_TmnxTlmPersSubDestPort_Object = MibTableColumn
tmnxTlmPersSubDestPort = _TmnxTlmPersSubDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 4),
    _TmnxTlmPersSubDestPort_Type()
)
tmnxTlmPersSubDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestPort.setStatus("current")
_TmnxTlmPersSubDestOperState_Type = TmnxOperState
_TmnxTlmPersSubDestOperState_Object = MibTableColumn
tmnxTlmPersSubDestOperState = _TmnxTlmPersSubDestOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 5),
    _TmnxTlmPersSubDestOperState_Type()
)
tmnxTlmPersSubDestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestOperState.setStatus("current")


class _TmnxTlmPersSubDestOperDownReason_Type(OctetString):
    """Custom type tmnxTlmPersSubDestOperDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxTlmPersSubDestOperDownReason_Type.__name__ = "OctetString"
_TmnxTlmPersSubDestOperDownReason_Object = MibTableColumn
tmnxTlmPersSubDestOperDownReason = _TmnxTlmPersSubDestOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 6),
    _TmnxTlmPersSubDestOperDownReason_Type()
)
tmnxTlmPersSubDestOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestOperDownReason.setStatus("current")
_TmnxTlmPersSubDestOperVRtrId_Type = TmnxVRtrIDOrZero
_TmnxTlmPersSubDestOperVRtrId_Object = MibTableColumn
tmnxTlmPersSubDestOperVRtrId = _TmnxTlmPersSubDestOperVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 7),
    _TmnxTlmPersSubDestOperVRtrId_Type()
)
tmnxTlmPersSubDestOperVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestOperVRtrId.setStatus("current")
_TmnxTlmPersSubDestLastOperChange_Type = DateAndTime
_TmnxTlmPersSubDestLastOperChange_Object = MibTableColumn
tmnxTlmPersSubDestLastOperChange = _TmnxTlmPersSubDestLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 8),
    _TmnxTlmPersSubDestLastOperChange_Type()
)
tmnxTlmPersSubDestLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestLastOperChange.setStatus("current")
_TmnxTlmPersSubDestConnAttempts_Type = Counter64
_TmnxTlmPersSubDestConnAttempts_Object = MibTableColumn
tmnxTlmPersSubDestConnAttempts = _TmnxTlmPersSubDestConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 9),
    _TmnxTlmPersSubDestConnAttempts_Type()
)
tmnxTlmPersSubDestConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestConnAttempts.setStatus("current")
_TmnxTlmPersSubDestOperQos_Type = TDSCPNameOrEmpty
_TmnxTlmPersSubDestOperQos_Object = MibTableColumn
tmnxTlmPersSubDestOperQos = _TmnxTlmPersSubDestOperQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 10),
    _TmnxTlmPersSubDestOperQos_Type()
)
tmnxTlmPersSubDestOperQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestOperQos.setStatus("current")
_TmnxTlmPersSubDestNotifCnt_Type = Counter64
_TmnxTlmPersSubDestNotifCnt_Object = MibTableColumn
tmnxTlmPersSubDestNotifCnt = _TmnxTlmPersSubDestNotifCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 11),
    _TmnxTlmPersSubDestNotifCnt_Type()
)
tmnxTlmPersSubDestNotifCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestNotifCnt.setStatus("current")
_TmnxTlmPersSubDestTotalNotifCnt_Type = Counter64
_TmnxTlmPersSubDestTotalNotifCnt_Object = MibTableColumn
tmnxTlmPersSubDestTotalNotifCnt = _TmnxTlmPersSubDestTotalNotifCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 6, 1, 12),
    _TmnxTlmPersSubDestTotalNotifCnt_Type()
)
tmnxTlmPersSubDestTotalNotifCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubDestTotalNotifCnt.setStatus("current")
_TmnxTlmtryPersSubscrPathTable_Object = MibTable
tmnxTlmtryPersSubscrPathTable = _TmnxTlmtryPersSubscrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrPathTable.setStatus("current")
_TmnxTlmtryPersSubscrPathEntry_Object = MibTableRow
tmnxTlmtryPersSubscrPathEntry = _TmnxTlmtryPersSubscrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1)
)
tmnxTlmtryPersSubscrPathEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubName"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrPathEntry.setStatus("current")
_TmnxTlmPersSubPathIndex_Type = Unsigned32
_TmnxTlmPersSubPathIndex_Object = MibTableColumn
tmnxTlmPersSubPathIndex = _TmnxTlmPersSubPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 1),
    _TmnxTlmPersSubPathIndex_Type()
)
tmnxTlmPersSubPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathIndex.setStatus("current")


class _TmnxTlmPersSubPathPath_Type(OctetString):
    """Custom type tmnxTlmPersSubPathPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_TmnxTlmPersSubPathPath_Type.__name__ = "OctetString"
_TmnxTlmPersSubPathPath_Object = MibTableColumn
tmnxTlmPersSubPathPath = _TmnxTlmPersSubPathPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 2),
    _TmnxTlmPersSubPathPath_Type()
)
tmnxTlmPersSubPathPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathPath.setStatus("current")
_TmnxTlmPersSubPathFinisColCnt_Type = Counter64
_TmnxTlmPersSubPathFinisColCnt_Object = MibTableColumn
tmnxTlmPersSubPathFinisColCnt = _TmnxTlmPersSubPathFinisColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 3),
    _TmnxTlmPersSubPathFinisColCnt_Type()
)
tmnxTlmPersSubPathFinisColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathFinisColCnt.setStatus("current")
_TmnxTlmPersSubPathDeferColCnt_Type = Counter64
_TmnxTlmPersSubPathDeferColCnt_Object = MibTableColumn
tmnxTlmPersSubPathDeferColCnt = _TmnxTlmPersSubPathDeferColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 4),
    _TmnxTlmPersSubPathDeferColCnt_Type()
)
tmnxTlmPersSubPathDeferColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathDeferColCnt.setStatus("current")
_TmnxTlmPersSubPathTotColTime_Type = Counter64
_TmnxTlmPersSubPathTotColTime_Object = MibTableColumn
tmnxTlmPersSubPathTotColTime = _TmnxTlmPersSubPathTotColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 5),
    _TmnxTlmPersSubPathTotColTime_Type()
)
tmnxTlmPersSubPathTotColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathTotColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathTotColTime.setUnits("milliseconds")
_TmnxTlmPersSubPathMinColTime_Type = Counter32
_TmnxTlmPersSubPathMinColTime_Object = MibTableColumn
tmnxTlmPersSubPathMinColTime = _TmnxTlmPersSubPathMinColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 6),
    _TmnxTlmPersSubPathMinColTime_Type()
)
tmnxTlmPersSubPathMinColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathMinColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathMinColTime.setUnits("milliseconds")
_TmnxTlmPersSubPathAvgColTime_Type = Counter32
_TmnxTlmPersSubPathAvgColTime_Object = MibTableColumn
tmnxTlmPersSubPathAvgColTime = _TmnxTlmPersSubPathAvgColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 7),
    _TmnxTlmPersSubPathAvgColTime_Type()
)
tmnxTlmPersSubPathAvgColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathAvgColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathAvgColTime.setUnits("milliseconds")
_TmnxTlmPersSubPathMaxColTime_Type = Counter32
_TmnxTlmPersSubPathMaxColTime_Object = MibTableColumn
tmnxTlmPersSubPathMaxColTime = _TmnxTlmPersSubPathMaxColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 7, 1, 8),
    _TmnxTlmPersSubPathMaxColTime_Type()
)
tmnxTlmPersSubPathMaxColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathMaxColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubPathMaxColTime.setUnits("milliseconds")
_TmnxTlmtryPersSubscrSclPathTable_Object = MibTable
tmnxTlmtryPersSubscrSclPathTable = _TmnxTlmtryPersSubscrSclPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrSclPathTable.setStatus("current")
_TmnxTlmtryPersSubscrSclPathEntry_Object = MibTableRow
tmnxTlmtryPersSubscrSclPathEntry = _TmnxTlmtryPersSubscrSclPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1)
)
tmnxTlmtryPersSubscrSclPathEntry.setIndexNames(
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubName"),
    (0, "TIMETRA-TELEMETRY-MIB", "tmnxTlmtryPersSubSclPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubscrSclPathEntry.setStatus("current")
_TmnxTlmtryPersSubSclPathIndex_Type = Unsigned32
_TmnxTlmtryPersSubSclPathIndex_Object = MibTableColumn
tmnxTlmtryPersSubSclPathIndex = _TmnxTlmtryPersSubSclPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 1),
    _TmnxTlmtryPersSubSclPathIndex_Type()
)
tmnxTlmtryPersSubSclPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTlmtryPersSubSclPathIndex.setStatus("current")


class _TmnxTlmPersSubSclPathPath_Type(OctetString):
    """Custom type tmnxTlmPersSubSclPathPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_TmnxTlmPersSubSclPathPath_Type.__name__ = "OctetString"
_TmnxTlmPersSubSclPathPath_Object = MibTableColumn
tmnxTlmPersSubSclPathPath = _TmnxTlmPersSubSclPathPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 2),
    _TmnxTlmPersSubSclPathPath_Type()
)
tmnxTlmPersSubSclPathPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathPath.setStatus("current")
_TmnxTlmPersSubSclPathFinisColCnt_Type = Counter64
_TmnxTlmPersSubSclPathFinisColCnt_Object = MibTableColumn
tmnxTlmPersSubSclPathFinisColCnt = _TmnxTlmPersSubSclPathFinisColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 3),
    _TmnxTlmPersSubSclPathFinisColCnt_Type()
)
tmnxTlmPersSubSclPathFinisColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathFinisColCnt.setStatus("current")
_TmnxTlmPersSubSclPathDeferColCnt_Type = Counter64
_TmnxTlmPersSubSclPathDeferColCnt_Object = MibTableColumn
tmnxTlmPersSubSclPathDeferColCnt = _TmnxTlmPersSubSclPathDeferColCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 4),
    _TmnxTlmPersSubSclPathDeferColCnt_Type()
)
tmnxTlmPersSubSclPathDeferColCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathDeferColCnt.setStatus("current")
_TmnxTlmPersSubSclPathTotColTime_Type = Counter64
_TmnxTlmPersSubSclPathTotColTime_Object = MibTableColumn
tmnxTlmPersSubSclPathTotColTime = _TmnxTlmPersSubSclPathTotColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 5),
    _TmnxTlmPersSubSclPathTotColTime_Type()
)
tmnxTlmPersSubSclPathTotColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathTotColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathTotColTime.setUnits("milliseconds")
_TmnxTlmPersSubSclPathMinColTime_Type = Counter32
_TmnxTlmPersSubSclPathMinColTime_Object = MibTableColumn
tmnxTlmPersSubSclPathMinColTime = _TmnxTlmPersSubSclPathMinColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 6),
    _TmnxTlmPersSubSclPathMinColTime_Type()
)
tmnxTlmPersSubSclPathMinColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathMinColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathMinColTime.setUnits("milliseconds")
_TmnxTlmPersSubSclPathAvgColTime_Type = Counter32
_TmnxTlmPersSubSclPathAvgColTime_Object = MibTableColumn
tmnxTlmPersSubSclPathAvgColTime = _TmnxTlmPersSubSclPathAvgColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 7),
    _TmnxTlmPersSubSclPathAvgColTime_Type()
)
tmnxTlmPersSubSclPathAvgColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathAvgColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathAvgColTime.setUnits("milliseconds")
_TmnxTlmPersSubSclPathMaxColTime_Type = Counter32
_TmnxTlmPersSubSclPathMaxColTime_Object = MibTableColumn
tmnxTlmPersSubSclPathMaxColTime = _TmnxTlmPersSubSclPathMaxColTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 110, 3, 8, 1, 8),
    _TmnxTlmPersSubSclPathMaxColTime_Type()
)
tmnxTlmPersSubSclPathMaxColTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathMaxColTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTlmPersSubSclPathMaxColTime.setUnits("milliseconds")

# Managed Objects groups

tmnxTelemetryStateV15Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110, 2, 1, 1)
)
tmnxTelemetryStateV15Group.setObjects(
      *(("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubUserName"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubDstIpAddType"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubDstIpAddress"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubDestPort"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubMode"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubReqQos"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubOperQos"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubEncoding"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubNotifCount"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathPath"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathInterval"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathFinisColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathDeferColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathTotColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathMinColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathAvgColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathMaxColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmtryGrpcSubPathMode"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathPath"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathInterval"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathFinisColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathDeferColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathTotColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathMinColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathAvgColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathMaxColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmGrpcSubSclPathMode"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTblLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpRowStatus"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDescription"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTlsClientProf"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpAllowUnsecConn"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTcpKaAdminState"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTcpKaIdle"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTcpKaInterval"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpTcpKaCount"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestTblLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestRowStatus"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestAddType"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestAddress"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestPort"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmDestGrpDestVRtrId"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpTblLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpRowStatus"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpDescription"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathTblLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathRowStatus"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathPath"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmSensGrpPathErrorReason"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubTblLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubLastChgd"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubRowStatus"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubAdminState"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubOperState"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubOperDownReason"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSubscrId"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDescription"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSensGrp"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubMode"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSmplIntervalHi"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSmplIntervalLo"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestGrp"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubLocalSrcAddType"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubLocalSrcAddress"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubOrigQosMarking"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubEncoding"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestOperState"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestOperDownReason"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestOperVRtrId"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestLastOperChange"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestConnAttempts"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestAddType"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestAddress"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestPort"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestOperQos"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestNotifCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubDestTotalNotifCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathPath"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathFinisColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathDeferColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathTotColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathMinColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathAvgColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubPathMaxColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathPath"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathFinisColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathDeferColCnt"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathTotColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathMinColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathAvgColTime"),
        ("TIMETRA-TELEMETRY-MIB", "tmnxTlmPersSubSclPathMaxColTime"))
)
if mibBuilder.loadTexts:
    tmnxTelemetryStateV15Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxTelemetryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 110, 1, 1)
)
tmnxTelemetryCompliance.setObjects(
    ("TIMETRA-TELEMETRY-MIB", "tmnxTelemetryStateV15Group")
)
if mibBuilder.loadTexts:
    tmnxTelemetryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TELEMETRY-MIB",
    **{"TmnxTlmtryGrpcSubMode": TmnxTlmtryGrpcSubMode,
       "TmnxTlmtryGrpcSubEncoding": TmnxTlmtryGrpcSubEncoding,
       "TmnxTlmtryGrpcSubPathMode": TmnxTlmtryGrpcSubPathMode,
       "TmnxTlmtryGrpcSubScalePathMode": TmnxTlmtryGrpcSubScalePathMode,
       "timetraTelemetryMIBModule": timetraTelemetryMIBModule,
       "tmnxTelemetryConformance": tmnxTelemetryConformance,
       "tmnxTelemetryCompliances": tmnxTelemetryCompliances,
       "tmnxTelemetryCompliance": tmnxTelemetryCompliance,
       "tmnxTelemetryGroups": tmnxTelemetryGroups,
       "tmnxTelemetryInitialGroups": tmnxTelemetryInitialGroups,
       "tmnxTelemetryStateV15Group": tmnxTelemetryStateV15Group,
       "tmnxTelemetryObjs": tmnxTelemetryObjs,
       "tmnxTelemetryStatsObjs": tmnxTelemetryStatsObjs,
       "tmnxTlmtryGrpcSubscrTable": tmnxTlmtryGrpcSubscrTable,
       "tmnxTlmtryGrpcSubscrEntry": tmnxTlmtryGrpcSubscrEntry,
       "tmnxTlmtryGrpcSubId": tmnxTlmtryGrpcSubId,
       "tmnxTlmtryGrpcSubUserName": tmnxTlmtryGrpcSubUserName,
       "tmnxTlmtryGrpcSubDstIpAddType": tmnxTlmtryGrpcSubDstIpAddType,
       "tmnxTlmtryGrpcSubDstIpAddress": tmnxTlmtryGrpcSubDstIpAddress,
       "tmnxTlmtryGrpcSubDestPort": tmnxTlmtryGrpcSubDestPort,
       "tmnxTlmtryGrpcSubMode": tmnxTlmtryGrpcSubMode,
       "tmnxTlmtryGrpcSubReqQos": tmnxTlmtryGrpcSubReqQos,
       "tmnxTlmtryGrpcSubOperQos": tmnxTlmtryGrpcSubOperQos,
       "tmnxTlmtryGrpcSubEncoding": tmnxTlmtryGrpcSubEncoding,
       "tmnxTlmtryGrpcSubNotifCount": tmnxTlmtryGrpcSubNotifCount,
       "tmnxTlmtryGrpcSubscrPathTable": tmnxTlmtryGrpcSubscrPathTable,
       "tmnxTlmtryGrpcSubscrPathEntry": tmnxTlmtryGrpcSubscrPathEntry,
       "tmnxTlmtryGrpcSubPathIndex": tmnxTlmtryGrpcSubPathIndex,
       "tmnxTlmtryGrpcSubPathPath": tmnxTlmtryGrpcSubPathPath,
       "tmnxTlmtryGrpcSubPathInterval": tmnxTlmtryGrpcSubPathInterval,
       "tmnxTlmtryGrpcSubPathFinisColCnt": tmnxTlmtryGrpcSubPathFinisColCnt,
       "tmnxTlmtryGrpcSubPathDeferColCnt": tmnxTlmtryGrpcSubPathDeferColCnt,
       "tmnxTlmtryGrpcSubPathTotColTime": tmnxTlmtryGrpcSubPathTotColTime,
       "tmnxTlmtryGrpcSubPathMinColTime": tmnxTlmtryGrpcSubPathMinColTime,
       "tmnxTlmtryGrpcSubPathAvgColTime": tmnxTlmtryGrpcSubPathAvgColTime,
       "tmnxTlmtryGrpcSubPathMaxColTime": tmnxTlmtryGrpcSubPathMaxColTime,
       "tmnxTlmtryGrpcSubPathMode": tmnxTlmtryGrpcSubPathMode,
       "tmnxTlmtryGrpcSubscrSclPathTable": tmnxTlmtryGrpcSubscrSclPathTable,
       "tmnxTlmtryGrpcSubscrSclPathEntry": tmnxTlmtryGrpcSubscrSclPathEntry,
       "tmnxTlmtryGrpcSubSclPathIndex": tmnxTlmtryGrpcSubSclPathIndex,
       "tmnxTlmGrpcSubSclPathPath": tmnxTlmGrpcSubSclPathPath,
       "tmnxTlmGrpcSubSclPathInterval": tmnxTlmGrpcSubSclPathInterval,
       "tmnxTlmGrpcSubSclPathFinisColCnt": tmnxTlmGrpcSubSclPathFinisColCnt,
       "tmnxTlmGrpcSubSclPathDeferColCnt": tmnxTlmGrpcSubSclPathDeferColCnt,
       "tmnxTlmGrpcSubSclPathTotColTime": tmnxTlmGrpcSubSclPathTotColTime,
       "tmnxTlmGrpcSubSclPathMinColTime": tmnxTlmGrpcSubSclPathMinColTime,
       "tmnxTlmGrpcSubSclPathAvgColTime": tmnxTlmGrpcSubSclPathAvgColTime,
       "tmnxTlmGrpcSubSclPathMaxColTime": tmnxTlmGrpcSubSclPathMaxColTime,
       "tmnxTlmGrpcSubSclPathMode": tmnxTlmGrpcSubSclPathMode,
       "tmnxTelemetryScalarObjs": tmnxTelemetryScalarObjs,
       "tmnxTelemetryLastChangedObjs": tmnxTelemetryLastChangedObjs,
       "tmnxTlmDestGrpTblLastChgd": tmnxTlmDestGrpTblLastChgd,
       "tmnxTlmDestGrpDestTblLastChgd": tmnxTlmDestGrpDestTblLastChgd,
       "tmnxTlmSensGrpTblLastChgd": tmnxTlmSensGrpTblLastChgd,
       "tmnxTlmSensGrpPathTblLastChgd": tmnxTlmSensGrpPathTblLastChgd,
       "tmnxTlmPersSubTblLastChgd": tmnxTlmPersSubTblLastChgd,
       "tmnxTelemetryConfigObjs": tmnxTelemetryConfigObjs,
       "tmnxTlmtryDestGroupTable": tmnxTlmtryDestGroupTable,
       "tmnxTlmtryDestGroupEntry": tmnxTlmtryDestGroupEntry,
       "tmnxTlmDestGrpName": tmnxTlmDestGrpName,
       "tmnxTlmDestGrpLastChgd": tmnxTlmDestGrpLastChgd,
       "tmnxTlmDestGrpRowStatus": tmnxTlmDestGrpRowStatus,
       "tmnxTlmDestGrpDescription": tmnxTlmDestGrpDescription,
       "tmnxTlmDestGrpTlsClientProf": tmnxTlmDestGrpTlsClientProf,
       "tmnxTlmDestGrpAllowUnsecConn": tmnxTlmDestGrpAllowUnsecConn,
       "tmnxTlmDestGrpTcpKaAdminState": tmnxTlmDestGrpTcpKaAdminState,
       "tmnxTlmDestGrpTcpKaIdle": tmnxTlmDestGrpTcpKaIdle,
       "tmnxTlmDestGrpTcpKaInterval": tmnxTlmDestGrpTcpKaInterval,
       "tmnxTlmDestGrpTcpKaCount": tmnxTlmDestGrpTcpKaCount,
       "tmnxTlmtryDestGroupDestTable": tmnxTlmtryDestGroupDestTable,
       "tmnxTlmtryDestGroupDestEntry": tmnxTlmtryDestGroupDestEntry,
       "tmnxTlmDestGrpDestIndex": tmnxTlmDestGrpDestIndex,
       "tmnxTlmDestGrpDestAddType": tmnxTlmDestGrpDestAddType,
       "tmnxTlmDestGrpDestAddress": tmnxTlmDestGrpDestAddress,
       "tmnxTlmDestGrpDestPort": tmnxTlmDestGrpDestPort,
       "tmnxTlmDestGrpDestVRtrId": tmnxTlmDestGrpDestVRtrId,
       "tmnxTlmDestGrpDestLastChgd": tmnxTlmDestGrpDestLastChgd,
       "tmnxTlmDestGrpDestRowStatus": tmnxTlmDestGrpDestRowStatus,
       "tmnxTlmtrySensGroupTable": tmnxTlmtrySensGroupTable,
       "tmnxTlmtrySensGroupEntry": tmnxTlmtrySensGroupEntry,
       "tmnxTlmSensGrpName": tmnxTlmSensGrpName,
       "tmnxTlmSensGrpLastChgd": tmnxTlmSensGrpLastChgd,
       "tmnxTlmSensGrpRowStatus": tmnxTlmSensGrpRowStatus,
       "tmnxTlmSensGrpDescription": tmnxTlmSensGrpDescription,
       "tmnxTlmtrySensGroupPathTable": tmnxTlmtrySensGroupPathTable,
       "tmnxTlmtrySensGroupPathEntry": tmnxTlmtrySensGroupPathEntry,
       "tmnxTlmSensGrpPathIndex": tmnxTlmSensGrpPathIndex,
       "tmnxTlmSensGrpPathLastChgd": tmnxTlmSensGrpPathLastChgd,
       "tmnxTlmSensGrpPathRowStatus": tmnxTlmSensGrpPathRowStatus,
       "tmnxTlmSensGrpPathPath": tmnxTlmSensGrpPathPath,
       "tmnxTlmSensGrpPathErrorReason": tmnxTlmSensGrpPathErrorReason,
       "tmnxTlmtryPersSubscrTable": tmnxTlmtryPersSubscrTable,
       "tmnxTlmtryPersSubscrEntry": tmnxTlmtryPersSubscrEntry,
       "tmnxTlmPersSubName": tmnxTlmPersSubName,
       "tmnxTlmPersSubLastChgd": tmnxTlmPersSubLastChgd,
       "tmnxTlmPersSubRowStatus": tmnxTlmPersSubRowStatus,
       "tmnxTlmPersSubAdminState": tmnxTlmPersSubAdminState,
       "tmnxTlmPersSubOperState": tmnxTlmPersSubOperState,
       "tmnxTlmPersSubOperDownReason": tmnxTlmPersSubOperDownReason,
       "tmnxTlmPersSubSubscrId": tmnxTlmPersSubSubscrId,
       "tmnxTlmPersSubDescription": tmnxTlmPersSubDescription,
       "tmnxTlmPersSubSensGrp": tmnxTlmPersSubSensGrp,
       "tmnxTlmPersSubMode": tmnxTlmPersSubMode,
       "tmnxTlmPersSubSmplIntervalHi": tmnxTlmPersSubSmplIntervalHi,
       "tmnxTlmPersSubSmplIntervalLo": tmnxTlmPersSubSmplIntervalLo,
       "tmnxTlmPersSubDestGrp": tmnxTlmPersSubDestGrp,
       "tmnxTlmPersSubLocalSrcAddType": tmnxTlmPersSubLocalSrcAddType,
       "tmnxTlmPersSubLocalSrcAddress": tmnxTlmPersSubLocalSrcAddress,
       "tmnxTlmPersSubOrigQosMarking": tmnxTlmPersSubOrigQosMarking,
       "tmnxTlmPersSubEncoding": tmnxTlmPersSubEncoding,
       "tmnxTlmtryPersSubscrDestTable": tmnxTlmtryPersSubscrDestTable,
       "tmnxTlmtryPersSubscrDestEntry": tmnxTlmtryPersSubscrDestEntry,
       "tmnxTlmPersSubDestIndex": tmnxTlmPersSubDestIndex,
       "tmnxTlmPersSubDestAddType": tmnxTlmPersSubDestAddType,
       "tmnxTlmPersSubDestAddress": tmnxTlmPersSubDestAddress,
       "tmnxTlmPersSubDestPort": tmnxTlmPersSubDestPort,
       "tmnxTlmPersSubDestOperState": tmnxTlmPersSubDestOperState,
       "tmnxTlmPersSubDestOperDownReason": tmnxTlmPersSubDestOperDownReason,
       "tmnxTlmPersSubDestOperVRtrId": tmnxTlmPersSubDestOperVRtrId,
       "tmnxTlmPersSubDestLastOperChange": tmnxTlmPersSubDestLastOperChange,
       "tmnxTlmPersSubDestConnAttempts": tmnxTlmPersSubDestConnAttempts,
       "tmnxTlmPersSubDestOperQos": tmnxTlmPersSubDestOperQos,
       "tmnxTlmPersSubDestNotifCnt": tmnxTlmPersSubDestNotifCnt,
       "tmnxTlmPersSubDestTotalNotifCnt": tmnxTlmPersSubDestTotalNotifCnt,
       "tmnxTlmtryPersSubscrPathTable": tmnxTlmtryPersSubscrPathTable,
       "tmnxTlmtryPersSubscrPathEntry": tmnxTlmtryPersSubscrPathEntry,
       "tmnxTlmPersSubPathIndex": tmnxTlmPersSubPathIndex,
       "tmnxTlmPersSubPathPath": tmnxTlmPersSubPathPath,
       "tmnxTlmPersSubPathFinisColCnt": tmnxTlmPersSubPathFinisColCnt,
       "tmnxTlmPersSubPathDeferColCnt": tmnxTlmPersSubPathDeferColCnt,
       "tmnxTlmPersSubPathTotColTime": tmnxTlmPersSubPathTotColTime,
       "tmnxTlmPersSubPathMinColTime": tmnxTlmPersSubPathMinColTime,
       "tmnxTlmPersSubPathAvgColTime": tmnxTlmPersSubPathAvgColTime,
       "tmnxTlmPersSubPathMaxColTime": tmnxTlmPersSubPathMaxColTime,
       "tmnxTlmtryPersSubscrSclPathTable": tmnxTlmtryPersSubscrSclPathTable,
       "tmnxTlmtryPersSubscrSclPathEntry": tmnxTlmtryPersSubscrSclPathEntry,
       "tmnxTlmtryPersSubSclPathIndex": tmnxTlmtryPersSubSclPathIndex,
       "tmnxTlmPersSubSclPathPath": tmnxTlmPersSubSclPathPath,
       "tmnxTlmPersSubSclPathFinisColCnt": tmnxTlmPersSubSclPathFinisColCnt,
       "tmnxTlmPersSubSclPathDeferColCnt": tmnxTlmPersSubSclPathDeferColCnt,
       "tmnxTlmPersSubSclPathTotColTime": tmnxTlmPersSubSclPathTotColTime,
       "tmnxTlmPersSubSclPathMinColTime": tmnxTlmPersSubSclPathMinColTime,
       "tmnxTlmPersSubSclPathAvgColTime": tmnxTlmPersSubSclPathAvgColTime,
       "tmnxTlmPersSubSclPathMaxColTime": tmnxTlmPersSubSclPathMaxColTime}
)
