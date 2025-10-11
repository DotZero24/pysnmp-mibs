# SNMP MIB module (ACC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/ACC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:29 2025
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(FeatureStatus,
 RowStatus,
 TruthValue,
 rndErrorDesc,
 rndErrorSeverity,
 rsACC) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "FeatureStatus",
    "RowStatus",
    "TruthValue",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsACC")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsACCStatTable_Object = MibTable
rsACCStatTable = _RsACCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 1)
)
if mibBuilder.loadTexts:
    rsACCStatTable.setStatus("mandatory")
_RsACCStatEntry_Object = MibTableRow
rsACCStatEntry = _RsACCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 1, 1)
)
rsACCStatEntry.setIndexNames(
    (0, "ACC-MIB", "rsACCStatId"),
)
if mibBuilder.loadTexts:
    rsACCStatEntry.setStatus("mandatory")


class _RsACCStatId_Type(Integer32):
    """Custom type rsACCStatId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("received", 0),
          ("discardImmediate", 1),
          ("masterImmediate", 2),
          ("macDiscard", 3),
          ("masterNoFlow", 4),
          ("discardBrgLimit", 5),
          ("discardRtrLimit", 6),
          ("masterBrgLimit", 7),
          ("masterRtrLimit", 8),
          ("bridgeDiscard", 9),
          ("routerDiscard", 10),
          ("masterBridge", 11),
          ("masterRouter", 12),
          ("bridgeForward", 13),
          ("routerForward", 14),
          ("bindSyn", 15),
          ("ackForSyn", 16),
          ("cookieData", 17),
          ("invalidCookie", 18),
          ("cookieNotFirst", 19),
          ("bypassAcc", 20),
          ("bypassMaster", 21),
          ("bypassAccBytes", 22),
          ("bypassMasterBytes", 23),
          ("forwardImmediate", 24),
          ("toSmeSent", 25),
          ("toSmeErrors", 26),
          ("fromSmeReceived", 27),
          ("fromSmeBadConfigId", 28),
          ("fromSmeTooManyResults", 29),
          ("fromSmeHwError", 30),
          ("fromSmeTrackingError", 31),
          ("fromSmeToMaster", 32),
          ("fromSmeForward", 33),
          ("fromSmeBypass", 34),
          ("fromSmeDiscard", 35),
          ("fromSmeMatches", 36),
          ("ipFragsToMaster", 37),
          ("ipFragsDiscard", 38),
          ("httpRplyTotal", 39),
          ("httpRplyClassify", 40),
          ("httpRplyAccMarked", 41),
          ("httpRplyAccUnmarked", 42),
          ("httpRplySmeMarked", 43),
          ("debugToMaster", 44),
          ("smeBypassErr", 45),
          ("smeBypassFlow", 46),
          ("smeBypassMarked", 47),
          ("queuedPackets", 48),
          ("fromSmeBadCompileId", 49),
          ("accessListDiscard", 50),
          ("accessListBypass", 51),
          ("accessListToMaster", 52),
          ("fromSmeNFAError", 53),
          ("webCookiesDiscard", 54),
          ("webCookiesForward", 55),
          ("safeRstChallenge", 56),
          ("tcpRstChallenge", 57))
    )


_RsACCStatId_Type.__name__ = "Integer32"
_RsACCStatId_Object = MibTableColumn
rsACCStatId = _RsACCStatId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 1, 1, 1),
    _RsACCStatId_Type()
)
rsACCStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCStatId.setStatus("mandatory")
_RsACCStatValue_Type = Integer32
_RsACCStatValue_Object = MibTableColumn
rsACCStatValue = _RsACCStatValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 1, 1, 2),
    _RsACCStatValue_Type()
)
rsACCStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCStatValue.setStatus("mandatory")
_RsACCUseFlowTable_Type = FeatureStatus
_RsACCUseFlowTable_Object = MibScalar
rsACCUseFlowTable = _RsACCUseFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 2),
    _RsACCUseFlowTable_Type()
)
rsACCUseFlowTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsACCUseFlowTable.setStatus("mandatory")
_RsACCResourceTable_Object = MibTable
rsACCResourceTable = _RsACCResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3)
)
if mibBuilder.loadTexts:
    rsACCResourceTable.setStatus("mandatory")
_RsACCResourceEntry_Object = MibTableRow
rsACCResourceEntry = _RsACCResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1)
)
rsACCResourceEntry.setIndexNames(
    (0, "ACC-MIB", "rsACCCPUId"),
)
if mibBuilder.loadTexts:
    rsACCResourceEntry.setStatus("mandatory")
_RsACCInstanceId_Type = Integer32
_RsACCInstanceId_Object = MibTableColumn
rsACCInstanceId = _RsACCInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 1),
    _RsACCInstanceId_Type()
)
rsACCInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCInstanceId.setStatus("obsolete")
_RsACCId_Type = Integer32
_RsACCId_Object = MibTableColumn
rsACCId = _RsACCId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 2),
    _RsACCId_Type()
)
rsACCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCId.setStatus("obsolete")
_RsACCCPUId_Type = Integer32
_RsACCCPUId_Object = MibTableColumn
rsACCCPUId = _RsACCCPUId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 3),
    _RsACCCPUId_Type()
)
rsACCCPUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCCPUId.setStatus("mandatory")
_RsACCFlow_Type = Integer32
_RsACCFlow_Object = MibTableColumn
rsACCFlow = _RsACCFlow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 4),
    _RsACCFlow_Type()
)
rsACCFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCFlow.setStatus("mandatory")
_RsACCOther_Type = Integer32
_RsACCOther_Object = MibTableColumn
rsACCOther = _RsACCOther_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 5),
    _RsACCOther_Type()
)
rsACCOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCOther.setStatus("mandatory")
_RsACCIdle_Type = Integer32
_RsACCIdle_Object = MibTableColumn
rsACCIdle = _RsACCIdle_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 3, 1, 6),
    _RsACCIdle_Type()
)
rsACCIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCIdle.setStatus("mandatory")
_RsACCFFTRouteIgnore_Type = FeatureStatus
_RsACCFFTRouteIgnore_Object = MibScalar
rsACCFFTRouteIgnore = _RsACCFFTRouteIgnore_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 4),
    _RsACCFFTRouteIgnore_Type()
)
rsACCFFTRouteIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsACCFFTRouteIgnore.setStatus("mandatory")
_RsACCHardwareClassification_Type = FeatureStatus
_RsACCHardwareClassification_Object = MibScalar
rsACCHardwareClassification = _RsACCHardwareClassification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 5),
    _RsACCHardwareClassification_Type()
)
rsACCHardwareClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsACCHardwareClassification.setStatus("mandatory")
_RsACCSMEStatisticsTable_Object = MibTable
rsACCSMEStatisticsTable = _RsACCSMEStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6)
)
if mibBuilder.loadTexts:
    rsACCSMEStatisticsTable.setStatus("mandatory")
_RsACCSMEStatisticsEntry_Object = MibTableRow
rsACCSMEStatisticsEntry = _RsACCSMEStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1)
)
rsACCSMEStatisticsEntry.setIndexNames(
    (0, "ACC-MIB", "rsACCSMEId"),
)
if mibBuilder.loadTexts:
    rsACCSMEStatisticsEntry.setStatus("mandatory")
_RsACCSMEId_Type = Integer32
_RsACCSMEId_Object = MibTableColumn
rsACCSMEId = _RsACCSMEId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 1),
    _RsACCSMEId_Type()
)
rsACCSMEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEId.setStatus("mandatory")
_RsACCSMEResultsReceived_Type = Integer32
_RsACCSMEResultsReceived_Object = MibTableColumn
rsACCSMEResultsReceived = _RsACCSMEResultsReceived_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 2),
    _RsACCSMEResultsReceived_Type()
)
rsACCSMEResultsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEResultsReceived.setStatus("mandatory")
_RsACCSMEResultsForward_Type = Integer32
_RsACCSMEResultsForward_Object = MibTableColumn
rsACCSMEResultsForward = _RsACCSMEResultsForward_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 3),
    _RsACCSMEResultsForward_Type()
)
rsACCSMEResultsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEResultsForward.setStatus("mandatory")
_RsACCSMEResultsDiscarded_Type = Integer32
_RsACCSMEResultsDiscarded_Object = MibTableColumn
rsACCSMEResultsDiscarded = _RsACCSMEResultsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 4),
    _RsACCSMEResultsDiscarded_Type()
)
rsACCSMEResultsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEResultsDiscarded.setStatus("mandatory")
_RsACCSMEResultsNext_Type = Integer32
_RsACCSMEResultsNext_Object = MibTableColumn
rsACCSMEResultsNext = _RsACCSMEResultsNext_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 5),
    _RsACCSMEResultsNext_Type()
)
rsACCSMEResultsNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEResultsNext.setStatus("mandatory")
_RsACCSMEResultsFree_Type = Integer32
_RsACCSMEResultsFree_Object = MibTableColumn
rsACCSMEResultsFree = _RsACCSMEResultsFree_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 6),
    _RsACCSMEResultsFree_Type()
)
rsACCSMEResultsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEResultsFree.setStatus("mandatory")
_RsACCSMERequestSent_Type = Integer32
_RsACCSMERequestSent_Object = MibTableColumn
rsACCSMERequestSent = _RsACCSMERequestSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 7),
    _RsACCSMERequestSent_Type()
)
rsACCSMERequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMERequestSent.setStatus("mandatory")
_RsACCSMERequestInvalidData_Type = Integer32
_RsACCSMERequestInvalidData_Object = MibTableColumn
rsACCSMERequestInvalidData = _RsACCSMERequestInvalidData_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 8),
    _RsACCSMERequestInvalidData_Type()
)
rsACCSMERequestInvalidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMERequestInvalidData.setStatus("mandatory")
_RsACCSMERequestFailed_Type = Integer32
_RsACCSMERequestFailed_Object = MibTableColumn
rsACCSMERequestFailed = _RsACCSMERequestFailed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 9),
    _RsACCSMERequestFailed_Type()
)
rsACCSMERequestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMERequestFailed.setStatus("mandatory")
_RsACCSMEDiscard_Type = Integer32
_RsACCSMEDiscard_Object = MibTableColumn
rsACCSMEDiscard = _RsACCSMEDiscard_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 10),
    _RsACCSMEDiscard_Type()
)
rsACCSMEDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEDiscard.setStatus("mandatory")
_RsACCSMETooManyResults_Type = Integer32
_RsACCSMETooManyResults_Object = MibTableColumn
rsACCSMETooManyResults = _RsACCSMETooManyResults_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 11),
    _RsACCSMETooManyResults_Type()
)
rsACCSMETooManyResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMETooManyResults.setStatus("mandatory")
_RsACCSMEHWHWProblem_Type = Integer32
_RsACCSMEHWHWProblem_Object = MibTableColumn
rsACCSMEHWHWProblem = _RsACCSMEHWHWProblem_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 12),
    _RsACCSMEHWHWProblem_Type()
)
rsACCSMEHWHWProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEHWHWProblem.setStatus("mandatory")
_RsACCSMEFragmented_Type = Integer32
_RsACCSMEFragmented_Object = MibTableColumn
rsACCSMEFragmented = _RsACCSMEFragmented_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 6, 1, 13),
    _RsACCSMEFragmented_Type()
)
rsACCSMEFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCSMEFragmented.setStatus("mandatory")


class _RsACCSwitchMode_Type(Integer32):
    """Custom type rsACCSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 1),
          ("layer4", 2))
    )


_RsACCSwitchMode_Type.__name__ = "Integer32"
_RsACCSwitchMode_Object = MibScalar
rsACCSwitchMode = _RsACCSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 7),
    _RsACCSwitchMode_Type()
)
rsACCSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsACCSwitchMode.setStatus("mandatory")


class _RsACCTrunkMode_Type(Integer32):
    """Custom type rsACCTrunkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_RsACCTrunkMode_Type.__name__ = "Integer32"
_RsACCTrunkMode_Object = MibScalar
rsACCTrunkMode = _RsACCTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 8),
    _RsACCTrunkMode_Type()
)
rsACCTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsACCTrunkMode.setStatus("mandatory")


class _RsACCWorkingMode_Type(Integer32):
    """Custom type rsACCWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("single", 2),
          ("dual", 3))
    )


_RsACCWorkingMode_Type.__name__ = "Integer32"
_RsACCWorkingMode_Object = MibScalar
rsACCWorkingMode = _RsACCWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 9),
    _RsACCWorkingMode_Type()
)
rsACCWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsACCWorkingMode.setStatus("mandatory")
_RsSystemSmeEngineUtilizationTable_Object = MibTable
rsSystemSmeEngineUtilizationTable = _RsSystemSmeEngineUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10)
)
if mibBuilder.loadTexts:
    rsSystemSmeEngineUtilizationTable.setStatus("mandatory")
_RsSmeEngineUtilizationEntry_Object = MibTableRow
rsSmeEngineUtilizationEntry = _RsSmeEngineUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1)
)
rsSmeEngineUtilizationEntry.setIndexNames(
    (0, "ACC-MIB", "rsSmeUtilizationInstanceId"),
    (0, "ACC-MIB", "rsSMEEnginesUtilId"),
)
if mibBuilder.loadTexts:
    rsSmeEngineUtilizationEntry.setStatus("mandatory")
_RsSmeUtilizationInstanceId_Type = Integer32
_RsSmeUtilizationInstanceId_Object = MibTableColumn
rsSmeUtilizationInstanceId = _RsSmeUtilizationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 1),
    _RsSmeUtilizationInstanceId_Type()
)
rsSmeUtilizationInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeUtilizationInstanceId.setStatus("mandatory")
_RsSMEEnginesUtilId_Type = Integer32
_RsSMEEnginesUtilId_Object = MibTableColumn
rsSMEEnginesUtilId = _RsSMEEnginesUtilId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 2),
    _RsSMEEnginesUtilId_Type()
)
rsSMEEnginesUtilId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSMEEnginesUtilId.setStatus("mandatory")
_RsSmeNfaUtilization_Type = Integer32
_RsSmeNfaUtilization_Object = MibTableColumn
rsSmeNfaUtilization = _RsSmeNfaUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 3),
    _RsSmeNfaUtilization_Type()
)
rsSmeNfaUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaUtilization.setStatus("mandatory")
_RsSmeDfaUtilization_Type = Integer32
_RsSmeDfaUtilization_Object = MibTableColumn
rsSmeDfaUtilization = _RsSmeDfaUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 4),
    _RsSmeDfaUtilization_Type()
)
rsSmeDfaUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDfaUtilization.setStatus("mandatory")
_RsSmeDMaUtilization_Type = Integer32
_RsSmeDMaUtilization_Object = MibTableColumn
rsSmeDMaUtilization = _RsSmeDMaUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 5),
    _RsSmeDMaUtilization_Type()
)
rsSmeDMaUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDMaUtilization.setStatus("mandatory")


class _RsSmeCntTotalTime_Type(DisplayString):
    """Custom type rsSmeCntTotalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeCntTotalTime_Type.__name__ = "DisplayString"
_RsSmeCntTotalTime_Object = MibTableColumn
rsSmeCntTotalTime = _RsSmeCntTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 6),
    _RsSmeCntTotalTime_Type()
)
rsSmeCntTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeCntTotalTime.setStatus("mandatory")


class _RsSmeDfaBusy_Type(DisplayString):
    """Custom type rsSmeDfaBusy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeDfaBusy_Type.__name__ = "DisplayString"
_RsSmeDfaBusy_Object = MibTableColumn
rsSmeDfaBusy = _RsSmeDfaBusy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 7),
    _RsSmeDfaBusy_Type()
)
rsSmeDfaBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDfaBusy.setStatus("mandatory")


class _RsSmeDfaBusyDmaDataStarve_Type(DisplayString):
    """Custom type rsSmeDfaBusyDmaDataStarve based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeDfaBusyDmaDataStarve_Type.__name__ = "DisplayString"
_RsSmeDfaBusyDmaDataStarve_Object = MibTableColumn
rsSmeDfaBusyDmaDataStarve = _RsSmeDfaBusyDmaDataStarve_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 8),
    _RsSmeDfaBusyDmaDataStarve_Type()
)
rsSmeDfaBusyDmaDataStarve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDfaBusyDmaDataStarve.setStatus("mandatory")


class _RsSmeDfaBusyNfaDataStall_Type(DisplayString):
    """Custom type rsSmeDfaBusyNfaDataStall based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeDfaBusyNfaDataStall_Type.__name__ = "DisplayString"
_RsSmeDfaBusyNfaDataStall_Object = MibTableColumn
rsSmeDfaBusyNfaDataStall = _RsSmeDfaBusyNfaDataStall_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 9),
    _RsSmeDfaBusyNfaDataStall_Type()
)
rsSmeDfaBusyNfaDataStall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDfaBusyNfaDataStall.setStatus("mandatory")


class _RsSmeDfaMemStall_Type(DisplayString):
    """Custom type rsSmeDfaMemStall based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeDfaMemStall_Type.__name__ = "DisplayString"
_RsSmeDfaMemStall_Object = MibTableColumn
rsSmeDfaMemStall = _RsSmeDfaMemStall_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 10),
    _RsSmeDfaMemStall_Type()
)
rsSmeDfaMemStall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeDfaMemStall.setStatus("mandatory")


class _RsSmeNfaBusyReadState_Type(DisplayString):
    """Custom type rsSmeNfaBusyReadState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeNfaBusyReadState_Type.__name__ = "DisplayString"
_RsSmeNfaBusyReadState_Object = MibTableColumn
rsSmeNfaBusyReadState = _RsSmeNfaBusyReadState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 11),
    _RsSmeNfaBusyReadState_Type()
)
rsSmeNfaBusyReadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaBusyReadState.setStatus("mandatory")


class _RsSmeNfaStateProcessed_Type(DisplayString):
    """Custom type rsSmeNfaStateProcessed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeNfaStateProcessed_Type.__name__ = "DisplayString"
_RsSmeNfaStateProcessed_Object = MibTableColumn
rsSmeNfaStateProcessed = _RsSmeNfaStateProcessed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 12),
    _RsSmeNfaStateProcessed_Type()
)
rsSmeNfaStateProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaStateProcessed.setStatus("mandatory")


class _RsSmeNfaBytesProcessed_Type(DisplayString):
    """Custom type rsSmeNfaBytesProcessed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeNfaBytesProcessed_Type.__name__ = "DisplayString"
_RsSmeNfaBytesProcessed_Object = MibTableColumn
rsSmeNfaBytesProcessed = _RsSmeNfaBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 13),
    _RsSmeNfaBytesProcessed_Type()
)
rsSmeNfaBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaBytesProcessed.setStatus("mandatory")


class _RsSmeCntTotalBytes_Type(DisplayString):
    """Custom type rsSmeCntTotalBytes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeCntTotalBytes_Type.__name__ = "DisplayString"
_RsSmeCntTotalBytes_Object = MibTableColumn
rsSmeCntTotalBytes = _RsSmeCntTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 14),
    _RsSmeCntTotalBytes_Type()
)
rsSmeCntTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeCntTotalBytes.setStatus("mandatory")


class _RsSmeNfaMemStall_Type(DisplayString):
    """Custom type rsSmeNfaMemStall based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsSmeNfaMemStall_Type.__name__ = "DisplayString"
_RsSmeNfaMemStall_Object = MibTableColumn
rsSmeNfaMemStall = _RsSmeNfaMemStall_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 15),
    _RsSmeNfaMemStall_Type()
)
rsSmeNfaMemStall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaMemStall.setStatus("mandatory")
_RsSmeNfaStatesAverage_Type = Integer32
_RsSmeNfaStatesAverage_Object = MibTableColumn
rsSmeNfaStatesAverage = _RsSmeNfaStatesAverage_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 16),
    _RsSmeNfaStatesAverage_Type()
)
rsSmeNfaStatesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaStatesAverage.setStatus("mandatory")
_RsSmeNfaMemStallsPerByteProc_Type = Integer32
_RsSmeNfaMemStallsPerByteProc_Object = MibTableColumn
rsSmeNfaMemStallsPerByteProc = _RsSmeNfaMemStallsPerByteProc_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 17),
    _RsSmeNfaMemStallsPerByteProc_Type()
)
rsSmeNfaMemStallsPerByteProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaMemStallsPerByteProc.setStatus("mandatory")
_RsSmeNfaSatesWhenNfaBusy_Type = Integer32
_RsSmeNfaSatesWhenNfaBusy_Object = MibTableColumn
rsSmeNfaSatesWhenNfaBusy = _RsSmeNfaSatesWhenNfaBusy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 10, 1, 18),
    _RsSmeNfaSatesWhenNfaBusy_Type()
)
rsSmeNfaSatesWhenNfaBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSmeNfaSatesWhenNfaBusy.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsACCFlowTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 0, 1)
)
rsACCFlowTableFull.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsACCFlowTableFull.setStatus(
        ""
    )

rsACCFlowEntryExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 0, 2)
)
rsACCFlowEntryExists.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsACCFlowEntryExists.setStatus(
        ""
    )

rsACCFlowEntryNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 88, 0, 3)
)
rsACCFlowEntryNotFound.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsACCFlowEntryNotFound.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-MIB",
    **{"NetNumber": NetNumber,
       "rsACCFlowTableFull": rsACCFlowTableFull,
       "rsACCFlowEntryExists": rsACCFlowEntryExists,
       "rsACCFlowEntryNotFound": rsACCFlowEntryNotFound,
       "rsACCStatTable": rsACCStatTable,
       "rsACCStatEntry": rsACCStatEntry,
       "rsACCStatId": rsACCStatId,
       "rsACCStatValue": rsACCStatValue,
       "rsACCUseFlowTable": rsACCUseFlowTable,
       "rsACCResourceTable": rsACCResourceTable,
       "rsACCResourceEntry": rsACCResourceEntry,
       "rsACCInstanceId": rsACCInstanceId,
       "rsACCId": rsACCId,
       "rsACCCPUId": rsACCCPUId,
       "rsACCFlow": rsACCFlow,
       "rsACCOther": rsACCOther,
       "rsACCIdle": rsACCIdle,
       "rsACCFFTRouteIgnore": rsACCFFTRouteIgnore,
       "rsACCHardwareClassification": rsACCHardwareClassification,
       "rsACCSMEStatisticsTable": rsACCSMEStatisticsTable,
       "rsACCSMEStatisticsEntry": rsACCSMEStatisticsEntry,
       "rsACCSMEId": rsACCSMEId,
       "rsACCSMEResultsReceived": rsACCSMEResultsReceived,
       "rsACCSMEResultsForward": rsACCSMEResultsForward,
       "rsACCSMEResultsDiscarded": rsACCSMEResultsDiscarded,
       "rsACCSMEResultsNext": rsACCSMEResultsNext,
       "rsACCSMEResultsFree": rsACCSMEResultsFree,
       "rsACCSMERequestSent": rsACCSMERequestSent,
       "rsACCSMERequestInvalidData": rsACCSMERequestInvalidData,
       "rsACCSMERequestFailed": rsACCSMERequestFailed,
       "rsACCSMEDiscard": rsACCSMEDiscard,
       "rsACCSMETooManyResults": rsACCSMETooManyResults,
       "rsACCSMEHWHWProblem": rsACCSMEHWHWProblem,
       "rsACCSMEFragmented": rsACCSMEFragmented,
       "rsACCSwitchMode": rsACCSwitchMode,
       "rsACCTrunkMode": rsACCTrunkMode,
       "rsACCWorkingMode": rsACCWorkingMode,
       "rsSystemSmeEngineUtilizationTable": rsSystemSmeEngineUtilizationTable,
       "rsSmeEngineUtilizationEntry": rsSmeEngineUtilizationEntry,
       "rsSmeUtilizationInstanceId": rsSmeUtilizationInstanceId,
       "rsSMEEnginesUtilId": rsSMEEnginesUtilId,
       "rsSmeNfaUtilization": rsSmeNfaUtilization,
       "rsSmeDfaUtilization": rsSmeDfaUtilization,
       "rsSmeDMaUtilization": rsSmeDMaUtilization,
       "rsSmeCntTotalTime": rsSmeCntTotalTime,
       "rsSmeDfaBusy": rsSmeDfaBusy,
       "rsSmeDfaBusyDmaDataStarve": rsSmeDfaBusyDmaDataStarve,
       "rsSmeDfaBusyNfaDataStall": rsSmeDfaBusyNfaDataStall,
       "rsSmeDfaMemStall": rsSmeDfaMemStall,
       "rsSmeNfaBusyReadState": rsSmeNfaBusyReadState,
       "rsSmeNfaStateProcessed": rsSmeNfaStateProcessed,
       "rsSmeNfaBytesProcessed": rsSmeNfaBytesProcessed,
       "rsSmeCntTotalBytes": rsSmeCntTotalBytes,
       "rsSmeNfaMemStall": rsSmeNfaMemStall,
       "rsSmeNfaStatesAverage": rsSmeNfaStatesAverage,
       "rsSmeNfaMemStallsPerByteProc": rsSmeNfaMemStallsPerByteProc,
       "rsSmeNfaSatesWhenNfaBusy": rsSmeNfaSatesWhenNfaBusy}
)
