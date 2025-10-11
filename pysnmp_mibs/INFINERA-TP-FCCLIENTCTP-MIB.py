# SNMP MIB module (INFINERA-TP-FCCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FCCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:46 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnArc,
 InfnEnableDisable,
 InfnEqptType,
 InfnLoopbackType,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType,
 InfnTestPattern) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnArc",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnLoopbackType",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType",
    "InfnTestPattern")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fcClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26)
)
if mibBuilder.loadTexts:
    fcClientCtpMIB.setRevisions(
        ("2009-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FcClientCtpTable_Object = MibTable
fcClientCtpTable = _FcClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1)
)
if mibBuilder.loadTexts:
    fcClientCtpTable.setStatus("current")
_FcClientCtpEntry_Object = MibTableRow
fcClientCtpEntry = _FcClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1)
)
fcClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcClientCtpEntry.setStatus("current")


class _FcClientCtpScrambling_Type(InfnEnableDisable):
    """Custom type fcClientCtpScrambling based on InfnEnableDisable"""
    defaultValue = 2


_FcClientCtpScrambling_Type.__name__ = "InfnEnableDisable"
_FcClientCtpScrambling_Object = MibTableColumn
fcClientCtpScrambling = _FcClientCtpScrambling_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 1),
    _FcClientCtpScrambling_Type()
)
fcClientCtpScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpScrambling.setStatus("current")


class _FcClientCtpDeScrambling_Type(InfnEnableDisable):
    """Custom type fcClientCtpDeScrambling based on InfnEnableDisable"""
    defaultValue = 2


_FcClientCtpDeScrambling_Type.__name__ = "InfnEnableDisable"
_FcClientCtpDeScrambling_Object = MibTableColumn
fcClientCtpDeScrambling = _FcClientCtpDeScrambling_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 2),
    _FcClientCtpDeScrambling_Type()
)
fcClientCtpDeScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpDeScrambling.setStatus("current")


class _FcClientCtpTribTestSigGenMode_Type(InfnTestPattern):
    """Custom type fcClientCtpTribTestSigGenMode based on InfnTestPattern"""
    defaultValue = 1


_FcClientCtpTribTestSigGenMode_Type.__name__ = "InfnTestPattern"
_FcClientCtpTribTestSigGenMode_Object = MibTableColumn
fcClientCtpTribTestSigGenMode = _FcClientCtpTribTestSigGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 3),
    _FcClientCtpTribTestSigGenMode_Type()
)
fcClientCtpTribTestSigGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTribTestSigGenMode.setStatus("current")


class _FcClientCtpTribTestSigMonMode_Type(InfnTestPattern):
    """Custom type fcClientCtpTribTestSigMonMode based on InfnTestPattern"""
    defaultValue = 1


_FcClientCtpTribTestSigMonMode_Type.__name__ = "InfnTestPattern"
_FcClientCtpTribTestSigMonMode_Object = MibTableColumn
fcClientCtpTribTestSigMonMode = _FcClientCtpTribTestSigMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 4),
    _FcClientCtpTribTestSigMonMode_Type()
)
fcClientCtpTribTestSigMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTribTestSigMonMode.setStatus("obsolete")


class _FcClientCtpLineSigGenMode_Type(InfnTestPattern):
    """Custom type fcClientCtpLineSigGenMode based on InfnTestPattern"""
    defaultValue = 1


_FcClientCtpLineSigGenMode_Type.__name__ = "InfnTestPattern"
_FcClientCtpLineSigGenMode_Object = MibTableColumn
fcClientCtpLineSigGenMode = _FcClientCtpLineSigGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 5),
    _FcClientCtpLineSigGenMode_Type()
)
fcClientCtpLineSigGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpLineSigGenMode.setStatus("current")


class _FcClientCtpLineSigMonMode_Type(InfnTestPattern):
    """Custom type fcClientCtpLineSigMonMode based on InfnTestPattern"""
    defaultValue = 1


_FcClientCtpLineSigMonMode_Type.__name__ = "InfnTestPattern"
_FcClientCtpLineSigMonMode_Object = MibTableColumn
fcClientCtpLineSigMonMode = _FcClientCtpLineSigMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 6),
    _FcClientCtpLineSigMonMode_Type()
)
fcClientCtpLineSigMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpLineSigMonMode.setStatus("obsolete")


class _FcClientCtpPmHistStatsEnable_Type(Integer32):
    """Custom type fcClientCtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

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


_FcClientCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_FcClientCtpPmHistStatsEnable_Object = MibTableColumn
fcClientCtpPmHistStatsEnable = _FcClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 7),
    _FcClientCtpPmHistStatsEnable_Type()
)
fcClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpPmHistStatsEnable.setStatus("current")


class _FcClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type fcClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_FcClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_FcClientCtpAlarmReportControl_Object = MibTableColumn
fcClientCtpAlarmReportControl = _FcClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 8),
    _FcClientCtpAlarmReportControl_Type()
)
fcClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpAlarmReportControl.setStatus("current")
_FcClientCtpSupportingCircuitIdList_Type = DisplayString
_FcClientCtpSupportingCircuitIdList_Object = MibTableColumn
fcClientCtpSupportingCircuitIdList = _FcClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 9),
    _FcClientCtpSupportingCircuitIdList_Type()
)
fcClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcClientCtpSupportingCircuitIdList.setStatus("current")
_FcClientCtpTamType_Type = InfnEqptType
_FcClientCtpTamType_Object = MibTableColumn
fcClientCtpTamType = _FcClientCtpTamType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 10),
    _FcClientCtpTamType_Type()
)
fcClientCtpTamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcClientCtpTamType.setStatus("obsolete")


class _FcClientCtpLoopback_Type(InfnLoopbackType):
    """Custom type fcClientCtpLoopback based on InfnLoopbackType"""
    defaultValue = 1


_FcClientCtpLoopback_Type.__name__ = "InfnLoopbackType"
_FcClientCtpLoopback_Object = MibTableColumn
fcClientCtpLoopback = _FcClientCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 11),
    _FcClientCtpLoopback_Type()
)
fcClientCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpLoopback.setStatus("current")
_FcClientCtpConfiguredServiceType_Type = InfnServiceType
_FcClientCtpConfiguredServiceType_Object = MibTableColumn
fcClientCtpConfiguredServiceType = _FcClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 12),
    _FcClientCtpConfiguredServiceType_Type()
)
fcClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcClientCtpConfiguredServiceType.setStatus("current")
_FcClientCtpRxRpi15MinutesTce_Type = Counter64
_FcClientCtpRxRpi15MinutesTce_Object = MibTableColumn
fcClientCtpRxRpi15MinutesTce = _FcClientCtpRxRpi15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 13),
    _FcClientCtpRxRpi15MinutesTce_Type()
)
fcClientCtpRxRpi15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpi15MinutesTce.setStatus("current")
_FcClientCtpRxRpiDayTce_Type = Counter64
_FcClientCtpRxRpiDayTce_Object = MibTableColumn
fcClientCtpRxRpiDayTce = _FcClientCtpRxRpiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 14),
    _FcClientCtpRxRpiDayTce_Type()
)
fcClientCtpRxRpiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpiDayTce.setStatus("current")
_FcClientCtpTxTpi15MinutesTce_Type = Counter64
_FcClientCtpTxTpi15MinutesTce_Object = MibTableColumn
fcClientCtpTxTpi15MinutesTce = _FcClientCtpTxTpi15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 15),
    _FcClientCtpTxTpi15MinutesTce_Type()
)
fcClientCtpTxTpi15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpi15MinutesTce.setStatus("current")
_FcClientCtpTxTpiDayTce_Type = Counter64
_FcClientCtpTxTpiDayTce_Object = MibTableColumn
fcClientCtpTxTpiDayTce = _FcClientCtpTxTpiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 16),
    _FcClientCtpTxTpiDayTce_Type()
)
fcClientCtpTxTpiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpiDayTce.setStatus("current")


class _FcClientCtpRxRpss15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpRxRpss15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRpss15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpRxRpss15MinutesTce_Object = MibTableColumn
fcClientCtpRxRpss15MinutesTce = _FcClientCtpRxRpss15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 17),
    _FcClientCtpRxRpss15MinutesTce_Type()
)
fcClientCtpRxRpss15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpss15MinutesTce.setStatus("current")


class _FcClientCtpRxRpssDayTce_Type(Integer32):
    """Custom type fcClientCtpRxRpssDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRpssDayTce_Type.__name__ = "Integer32"
_FcClientCtpRxRpssDayTce_Object = MibTableColumn
fcClientCtpRxRpssDayTce = _FcClientCtpRxRpssDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 18),
    _FcClientCtpRxRpssDayTce_Type()
)
fcClientCtpRxRpssDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpssDayTce.setStatus("current")


class _FcClientCtpTxTpss15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpTxTpss15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTpss15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpTxTpss15MinutesTce_Object = MibTableColumn
fcClientCtpTxTpss15MinutesTce = _FcClientCtpTxTpss15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 19),
    _FcClientCtpTxTpss15MinutesTce_Type()
)
fcClientCtpTxTpss15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpss15MinutesTce.setStatus("current")


class _FcClientCtpTxTpssDayTce_Type(Integer32):
    """Custom type fcClientCtpTxTpssDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTpssDayTce_Type.__name__ = "Integer32"
_FcClientCtpTxTpssDayTce_Object = MibTableColumn
fcClientCtpTxTpssDayTce = _FcClientCtpTxTpssDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 20),
    _FcClientCtpTxTpssDayTce_Type()
)
fcClientCtpTxTpssDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpssDayTce.setStatus("current")


class _FcClientCtpRxRps15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpRxRps15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRps15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpRxRps15MinutesTce_Object = MibTableColumn
fcClientCtpRxRps15MinutesTce = _FcClientCtpRxRps15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 21),
    _FcClientCtpRxRps15MinutesTce_Type()
)
fcClientCtpRxRps15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRps15MinutesTce.setStatus("current")


class _FcClientCtpRxRpsDayTce_Type(Integer32):
    """Custom type fcClientCtpRxRpsDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRpsDayTce_Type.__name__ = "Integer32"
_FcClientCtpRxRpsDayTce_Object = MibTableColumn
fcClientCtpRxRpsDayTce = _FcClientCtpRxRpsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 22),
    _FcClientCtpRxRpsDayTce_Type()
)
fcClientCtpRxRpsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpsDayTce.setStatus("current")


class _FcClientCtpTxTps15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpTxTps15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTps15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpTxTps15MinutesTce_Object = MibTableColumn
fcClientCtpTxTps15MinutesTce = _FcClientCtpTxTps15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 23),
    _FcClientCtpTxTps15MinutesTce_Type()
)
fcClientCtpTxTps15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTps15MinutesTce.setStatus("current")


class _FcClientCtpTxTpsDayTce_Type(Integer32):
    """Custom type fcClientCtpTxTpsDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTpsDayTce_Type.__name__ = "Integer32"
_FcClientCtpTxTpsDayTce_Object = MibTableColumn
fcClientCtpTxTpsDayTce = _FcClientCtpTxTpsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 24),
    _FcClientCtpTxTpsDayTce_Type()
)
fcClientCtpTxTpsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpsDayTce.setStatus("current")


class _FcClientCtpRxRpe15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpRxRpe15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRpe15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpRxRpe15MinutesTce_Object = MibTableColumn
fcClientCtpRxRpe15MinutesTce = _FcClientCtpRxRpe15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 25),
    _FcClientCtpRxRpe15MinutesTce_Type()
)
fcClientCtpRxRpe15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpe15MinutesTce.setStatus("current")


class _FcClientCtpRxRpeDayTce_Type(Integer32):
    """Custom type fcClientCtpRxRpeDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRpeDayTce_Type.__name__ = "Integer32"
_FcClientCtpRxRpeDayTce_Object = MibTableColumn
fcClientCtpRxRpeDayTce = _FcClientCtpRxRpeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 26),
    _FcClientCtpRxRpeDayTce_Type()
)
fcClientCtpRxRpeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpeDayTce.setStatus("current")


class _FcClientCtpTxTpe15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpTxTpe15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTpe15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpTxTpe15MinutesTce_Object = MibTableColumn
fcClientCtpTxTpe15MinutesTce = _FcClientCtpTxTpe15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 27),
    _FcClientCtpTxTpe15MinutesTce_Type()
)
fcClientCtpTxTpe15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpe15MinutesTce.setStatus("current")


class _FcClientCtpTxTpeDayTce_Type(Integer32):
    """Custom type fcClientCtpTxTpeDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTpeDayTce_Type.__name__ = "Integer32"
_FcClientCtpTxTpeDayTce_Object = MibTableColumn
fcClientCtpTxTpeDayTce = _FcClientCtpTxTpeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 28),
    _FcClientCtpTxTpeDayTce_Type()
)
fcClientCtpTxTpeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpeDayTce.setStatus("current")
_FcClientCtpRxRf15MinutesTce_Type = Counter64
_FcClientCtpRxRf15MinutesTce_Object = MibTableColumn
fcClientCtpRxRf15MinutesTce = _FcClientCtpRxRf15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 29),
    _FcClientCtpRxRf15MinutesTce_Type()
)
fcClientCtpRxRf15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRf15MinutesTce.setStatus("current")
_FcClientCtpRxRfDayTce_Type = Counter64
_FcClientCtpRxRfDayTce_Object = MibTableColumn
fcClientCtpRxRfDayTce = _FcClientCtpRxRfDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 30),
    _FcClientCtpRxRfDayTce_Type()
)
fcClientCtpRxRfDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRfDayTce.setStatus("current")
_FcClientCtpTxTf15MinutesTce_Type = Counter64
_FcClientCtpTxTf15MinutesTce_Object = MibTableColumn
fcClientCtpTxTf15MinutesTce = _FcClientCtpTxTf15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 31),
    _FcClientCtpTxTf15MinutesTce_Type()
)
fcClientCtpTxTf15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTf15MinutesTce.setStatus("current")
_FcClientCtpTxTfDayTce_Type = Counter64
_FcClientCtpTxTfDayTce_Object = MibTableColumn
fcClientCtpTxTfDayTce = _FcClientCtpTxTfDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 32),
    _FcClientCtpTxTfDayTce_Type()
)
fcClientCtpTxTfDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTfDayTce.setStatus("current")
_FcClientCtpRxRef15MinutesTce_Type = Counter64
_FcClientCtpRxRef15MinutesTce_Object = MibTableColumn
fcClientCtpRxRef15MinutesTce = _FcClientCtpRxRef15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 33),
    _FcClientCtpRxRef15MinutesTce_Type()
)
fcClientCtpRxRef15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRef15MinutesTce.setStatus("current")
_FcClientCtpRxRefDayTce_Type = Counter64
_FcClientCtpRxRefDayTce_Object = MibTableColumn
fcClientCtpRxRefDayTce = _FcClientCtpRxRefDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 34),
    _FcClientCtpRxRefDayTce_Type()
)
fcClientCtpRxRefDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRefDayTce.setStatus("current")
_FcClientCtpTxTef15MinutesTce_Type = Counter64
_FcClientCtpTxTef15MinutesTce_Object = MibTableColumn
fcClientCtpTxTef15MinutesTce = _FcClientCtpTxTef15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 35),
    _FcClientCtpTxTef15MinutesTce_Type()
)
fcClientCtpTxTef15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTef15MinutesTce.setStatus("current")
_FcClientCtpTxTefDayTce_Type = Counter64
_FcClientCtpTxTefDayTce_Object = MibTableColumn
fcClientCtpTxTefDayTce = _FcClientCtpTxTefDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 36),
    _FcClientCtpTxTefDayTce_Type()
)
fcClientCtpTxTefDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTefDayTce.setStatus("current")
_FcClientCtpRxRo15MinutesTce_Type = Counter64
_FcClientCtpRxRo15MinutesTce_Object = MibTableColumn
fcClientCtpRxRo15MinutesTce = _FcClientCtpRxRo15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 37),
    _FcClientCtpRxRo15MinutesTce_Type()
)
fcClientCtpRxRo15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRo15MinutesTce.setStatus("current")
_FcClientCtpRxRoDayTce_Type = Counter64
_FcClientCtpRxRoDayTce_Object = MibTableColumn
fcClientCtpRxRoDayTce = _FcClientCtpRxRoDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 38),
    _FcClientCtpRxRoDayTce_Type()
)
fcClientCtpRxRoDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRoDayTce.setStatus("current")
_FcClientCtpTxTo15MinutesTce_Type = Counter64
_FcClientCtpTxTo15MinutesTce_Object = MibTableColumn
fcClientCtpTxTo15MinutesTce = _FcClientCtpTxTo15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 39),
    _FcClientCtpTxTo15MinutesTce_Type()
)
fcClientCtpTxTo15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTo15MinutesTce.setStatus("current")
_FcClientCtpTxToDayTce_Type = Counter64
_FcClientCtpTxToDayTce_Object = MibTableColumn
fcClientCtpTxToDayTce = _FcClientCtpTxToDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 40),
    _FcClientCtpTxToDayTce_Type()
)
fcClientCtpTxToDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxToDayTce.setStatus("current")
_FcClientCtpRxREo15MinutesTce_Type = Counter64
_FcClientCtpRxREo15MinutesTce_Object = MibTableColumn
fcClientCtpRxREo15MinutesTce = _FcClientCtpRxREo15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 41),
    _FcClientCtpRxREo15MinutesTce_Type()
)
fcClientCtpRxREo15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxREo15MinutesTce.setStatus("current")
_FcClientCtpRxREoDayTce_Type = Counter64
_FcClientCtpRxREoDayTce_Object = MibTableColumn
fcClientCtpRxREoDayTce = _FcClientCtpRxREoDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 42),
    _FcClientCtpRxREoDayTce_Type()
)
fcClientCtpRxREoDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxREoDayTce.setStatus("current")
_FcClientCtpTxTEo15MinutesTce_Type = Counter64
_FcClientCtpTxTEo15MinutesTce_Object = MibTableColumn
fcClientCtpTxTEo15MinutesTce = _FcClientCtpTxTEo15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 43),
    _FcClientCtpTxTEo15MinutesTce_Type()
)
fcClientCtpTxTEo15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTEo15MinutesTce.setStatus("current")
_FcClientCtpTxTEoDayTce_Type = Counter64
_FcClientCtpTxTEoDayTce_Object = MibTableColumn
fcClientCtpTxTEoDayTce = _FcClientCtpTxTEoDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 44),
    _FcClientCtpTxTEoDayTce_Type()
)
fcClientCtpTxTEoDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTEoDayTce.setStatus("current")


class _FcClientCtpRxRFs15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpRxRFs15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRFs15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpRxRFs15MinutesTce_Object = MibTableColumn
fcClientCtpRxRFs15MinutesTce = _FcClientCtpRxRFs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 45),
    _FcClientCtpRxRFs15MinutesTce_Type()
)
fcClientCtpRxRFs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRFs15MinutesTce.setStatus("current")


class _FcClientCtpRxRFsDayTce_Type(Integer32):
    """Custom type fcClientCtpRxRFsDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpRxRFsDayTce_Type.__name__ = "Integer32"
_FcClientCtpRxRFsDayTce_Object = MibTableColumn
fcClientCtpRxRFsDayTce = _FcClientCtpRxRFsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 46),
    _FcClientCtpRxRFsDayTce_Type()
)
fcClientCtpRxRFsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRFsDayTce.setStatus("current")


class _FcClientCtpTxTFs15MinutesTce_Type(Integer32):
    """Custom type fcClientCtpTxTFs15MinutesTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTFs15MinutesTce_Type.__name__ = "Integer32"
_FcClientCtpTxTFs15MinutesTce_Object = MibTableColumn
fcClientCtpTxTFs15MinutesTce = _FcClientCtpTxTFs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 47),
    _FcClientCtpTxTFs15MinutesTce_Type()
)
fcClientCtpTxTFs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTFs15MinutesTce.setStatus("current")


class _FcClientCtpTxTFsDayTce_Type(Integer32):
    """Custom type fcClientCtpTxTFsDayTce based on Integer32"""
    defaultValue = 1500


_FcClientCtpTxTFsDayTce_Type.__name__ = "Integer32"
_FcClientCtpTxTFsDayTce_Object = MibTableColumn
fcClientCtpTxTFsDayTce = _FcClientCtpTxTFsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 48),
    _FcClientCtpTxTFsDayTce_Type()
)
fcClientCtpTxTFsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTFsDayTce.setStatus("current")


class _FcClientCtpRxRpi15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpi15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpi15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpi15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRpi15MinutesTceReporting = _FcClientCtpRxRpi15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 49),
    _FcClientCtpRxRpi15MinutesTceReporting_Type()
)
fcClientCtpRxRpi15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpi15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRpiDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpiDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpiDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpiDayTceReporting_Object = MibTableColumn
fcClientCtpRxRpiDayTceReporting = _FcClientCtpRxRpiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 50),
    _FcClientCtpRxRpiDayTceReporting_Type()
)
fcClientCtpRxRpiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpiDayTceReporting.setStatus("current")


class _FcClientCtpTxTpi15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpi15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpi15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpi15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTpi15MinutesTceReporting = _FcClientCtpTxTpi15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 51),
    _FcClientCtpTxTpi15MinutesTceReporting_Type()
)
fcClientCtpTxTpi15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpi15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTpiDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpiDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpiDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpiDayTceReporting_Object = MibTableColumn
fcClientCtpTxTpiDayTceReporting = _FcClientCtpTxTpiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 52),
    _FcClientCtpTxTpiDayTceReporting_Type()
)
fcClientCtpTxTpiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpiDayTceReporting.setStatus("current")


class _FcClientCtpRxRpss15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpss15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpss15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpss15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRpss15MinutesTceReporting = _FcClientCtpRxRpss15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 53),
    _FcClientCtpRxRpss15MinutesTceReporting_Type()
)
fcClientCtpRxRpss15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpss15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRpssDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpssDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpssDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpssDayTceReporting_Object = MibTableColumn
fcClientCtpRxRpssDayTceReporting = _FcClientCtpRxRpssDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 54),
    _FcClientCtpRxRpssDayTceReporting_Type()
)
fcClientCtpRxRpssDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpssDayTceReporting.setStatus("current")


class _FcClientCtpTxTpss15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpss15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpss15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpss15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTpss15MinutesTceReporting = _FcClientCtpTxTpss15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 55),
    _FcClientCtpTxTpss15MinutesTceReporting_Type()
)
fcClientCtpTxTpss15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpss15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTpssDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpssDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpssDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpssDayTceReporting_Object = MibTableColumn
fcClientCtpTxTpssDayTceReporting = _FcClientCtpTxTpssDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 56),
    _FcClientCtpTxTpssDayTceReporting_Type()
)
fcClientCtpTxTpssDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpssDayTceReporting.setStatus("current")


class _FcClientCtpRxRps15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRps15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRps15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRps15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRps15MinutesTceReporting = _FcClientCtpRxRps15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 57),
    _FcClientCtpRxRps15MinutesTceReporting_Type()
)
fcClientCtpRxRps15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRps15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRpsDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpsDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpsDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpsDayTceReporting_Object = MibTableColumn
fcClientCtpRxRpsDayTceReporting = _FcClientCtpRxRpsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 58),
    _FcClientCtpRxRpsDayTceReporting_Type()
)
fcClientCtpRxRpsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpsDayTceReporting.setStatus("current")


class _FcClientCtpTxTps15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTps15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTps15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTps15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTps15MinutesTceReporting = _FcClientCtpTxTps15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 59),
    _FcClientCtpTxTps15MinutesTceReporting_Type()
)
fcClientCtpTxTps15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTps15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTpsDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpsDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpsDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpsDayTceReporting_Object = MibTableColumn
fcClientCtpTxTpsDayTceReporting = _FcClientCtpTxTpsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 60),
    _FcClientCtpTxTpsDayTceReporting_Type()
)
fcClientCtpTxTpsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpsDayTceReporting.setStatus("current")


class _FcClientCtpRxRpe15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpe15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpe15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpe15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRpe15MinutesTceReporting = _FcClientCtpRxRpe15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 61),
    _FcClientCtpRxRpe15MinutesTceReporting_Type()
)
fcClientCtpRxRpe15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpe15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRpeDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRpeDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRpeDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRpeDayTceReporting_Object = MibTableColumn
fcClientCtpRxRpeDayTceReporting = _FcClientCtpRxRpeDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 62),
    _FcClientCtpRxRpeDayTceReporting_Type()
)
fcClientCtpRxRpeDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRpeDayTceReporting.setStatus("current")


class _FcClientCtpTxTpe15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpe15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpe15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpe15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTpe15MinutesTceReporting = _FcClientCtpTxTpe15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 63),
    _FcClientCtpTxTpe15MinutesTceReporting_Type()
)
fcClientCtpTxTpe15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpe15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTpeDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTpeDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTpeDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTpeDayTceReporting_Object = MibTableColumn
fcClientCtpTxTpeDayTceReporting = _FcClientCtpTxTpeDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 64),
    _FcClientCtpTxTpeDayTceReporting_Type()
)
fcClientCtpTxTpeDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTpeDayTceReporting.setStatus("current")


class _FcClientCtpRxRf15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRf15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRf15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRf15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRf15MinutesTceReporting = _FcClientCtpRxRf15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 65),
    _FcClientCtpRxRf15MinutesTceReporting_Type()
)
fcClientCtpRxRf15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRf15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRfDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRfDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRfDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRfDayTceReporting_Object = MibTableColumn
fcClientCtpRxRfDayTceReporting = _FcClientCtpRxRfDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 66),
    _FcClientCtpRxRfDayTceReporting_Type()
)
fcClientCtpRxRfDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRfDayTceReporting.setStatus("current")


class _FcClientCtpTxTf15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTf15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTf15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTf15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTf15MinutesTceReporting = _FcClientCtpTxTf15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 67),
    _FcClientCtpTxTf15MinutesTceReporting_Type()
)
fcClientCtpTxTf15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTf15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTfDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTfDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTfDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTfDayTceReporting_Object = MibTableColumn
fcClientCtpTxTfDayTceReporting = _FcClientCtpTxTfDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 68),
    _FcClientCtpTxTfDayTceReporting_Type()
)
fcClientCtpTxTfDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTfDayTceReporting.setStatus("current")


class _FcClientCtpRxRef15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRef15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRef15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRef15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRef15MinutesTceReporting = _FcClientCtpRxRef15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 69),
    _FcClientCtpRxRef15MinutesTceReporting_Type()
)
fcClientCtpRxRef15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRef15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRefDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRefDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRefDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRefDayTceReporting_Object = MibTableColumn
fcClientCtpRxRefDayTceReporting = _FcClientCtpRxRefDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 70),
    _FcClientCtpRxRefDayTceReporting_Type()
)
fcClientCtpRxRefDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRefDayTceReporting.setStatus("current")


class _FcClientCtpTxTef15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTef15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTef15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTef15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTef15MinutesTceReporting = _FcClientCtpTxTef15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 71),
    _FcClientCtpTxTef15MinutesTceReporting_Type()
)
fcClientCtpTxTef15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTef15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTefDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTefDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTefDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTefDayTceReporting_Object = MibTableColumn
fcClientCtpTxTefDayTceReporting = _FcClientCtpTxTefDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 72),
    _FcClientCtpTxTefDayTceReporting_Type()
)
fcClientCtpTxTefDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTefDayTceReporting.setStatus("current")


class _FcClientCtpRxRo15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRo15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRo15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRo15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRo15MinutesTceReporting = _FcClientCtpRxRo15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 73),
    _FcClientCtpRxRo15MinutesTceReporting_Type()
)
fcClientCtpRxRo15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRo15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRoDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRoDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRoDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRoDayTceReporting_Object = MibTableColumn
fcClientCtpRxRoDayTceReporting = _FcClientCtpRxRoDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 74),
    _FcClientCtpRxRoDayTceReporting_Type()
)
fcClientCtpRxRoDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRoDayTceReporting.setStatus("current")


class _FcClientCtpTxTo15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTo15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTo15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTo15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTo15MinutesTceReporting = _FcClientCtpTxTo15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 75),
    _FcClientCtpTxTo15MinutesTceReporting_Type()
)
fcClientCtpTxTo15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTo15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxToDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxToDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxToDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxToDayTceReporting_Object = MibTableColumn
fcClientCtpTxToDayTceReporting = _FcClientCtpTxToDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 76),
    _FcClientCtpTxToDayTceReporting_Type()
)
fcClientCtpTxToDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxToDayTceReporting.setStatus("current")


class _FcClientCtpRxREo15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxREo15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxREo15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxREo15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxREo15MinutesTceReporting = _FcClientCtpRxREo15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 77),
    _FcClientCtpRxREo15MinutesTceReporting_Type()
)
fcClientCtpRxREo15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxREo15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxREoDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxREoDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxREoDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxREoDayTceReporting_Object = MibTableColumn
fcClientCtpRxREoDayTceReporting = _FcClientCtpRxREoDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 78),
    _FcClientCtpRxREoDayTceReporting_Type()
)
fcClientCtpRxREoDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxREoDayTceReporting.setStatus("current")


class _FcClientCtpTxTEo15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTEo15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTEo15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTEo15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTEo15MinutesTceReporting = _FcClientCtpTxTEo15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 79),
    _FcClientCtpTxTEo15MinutesTceReporting_Type()
)
fcClientCtpTxTEo15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTEo15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTEoDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTEoDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTEoDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTEoDayTceReporting_Object = MibTableColumn
fcClientCtpTxTEoDayTceReporting = _FcClientCtpTxTEoDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 80),
    _FcClientCtpTxTEoDayTceReporting_Type()
)
fcClientCtpTxTEoDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTEoDayTceReporting.setStatus("current")


class _FcClientCtpRxRFs15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRFs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRFs15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRFs15MinutesTceReporting_Object = MibTableColumn
fcClientCtpRxRFs15MinutesTceReporting = _FcClientCtpRxRFs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 81),
    _FcClientCtpRxRFs15MinutesTceReporting_Type()
)
fcClientCtpRxRFs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRFs15MinutesTceReporting.setStatus("current")


class _FcClientCtpRxRFsDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpRxRFsDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpRxRFsDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpRxRFsDayTceReporting_Object = MibTableColumn
fcClientCtpRxRFsDayTceReporting = _FcClientCtpRxRFsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 82),
    _FcClientCtpRxRFsDayTceReporting_Type()
)
fcClientCtpRxRFsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpRxRFsDayTceReporting.setStatus("current")


class _FcClientCtpTxTFs15MinutesTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTFs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTFs15MinutesTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTFs15MinutesTceReporting_Object = MibTableColumn
fcClientCtpTxTFs15MinutesTceReporting = _FcClientCtpTxTFs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 83),
    _FcClientCtpTxTFs15MinutesTceReporting_Type()
)
fcClientCtpTxTFs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTFs15MinutesTceReporting.setStatus("current")


class _FcClientCtpTxTFsDayTceReporting_Type(TruthValue):
    """Custom type fcClientCtpTxTFsDayTceReporting based on TruthValue"""
    defaultValue = 2


_FcClientCtpTxTFsDayTceReporting_Type.__name__ = "TruthValue"
_FcClientCtpTxTFsDayTceReporting_Object = MibTableColumn
fcClientCtpTxTFsDayTceReporting = _FcClientCtpTxTFsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 84),
    _FcClientCtpTxTFsDayTceReporting_Type()
)
fcClientCtpTxTFsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcClientCtpTxTFsDayTceReporting.setStatus("current")


class _FcClientCtpServiceMode_Type(InfnServiceMode):
    """Custom type fcClientCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_FcClientCtpServiceMode_Type.__name__ = "InfnServiceMode"
_FcClientCtpServiceMode_Object = MibTableColumn
fcClientCtpServiceMode = _FcClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 85),
    _FcClientCtpServiceMode_Type()
)
fcClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcClientCtpServiceMode.setStatus("current")


class _FcClientCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type fcClientCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_FcClientCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_FcClientCtpServiceModeQualifier_Object = MibTableColumn
fcClientCtpServiceModeQualifier = _FcClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 1, 1, 86),
    _FcClientCtpServiceModeQualifier_Type()
)
fcClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcClientCtpServiceModeQualifier.setStatus("current")
_FcClientCtpConformance_ObjectIdentity = ObjectIdentity
fcClientCtpConformance = _FcClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 3)
)
_FcClientCtpCompliances_ObjectIdentity = ObjectIdentity
fcClientCtpCompliances = _FcClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 3, 1)
)
_FcClientCtpGroups_ObjectIdentity = ObjectIdentity
fcClientCtpGroups = _FcClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 3, 2)
)

# Managed Objects groups

fcClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 3, 2, 1)
)
fcClientCtpGroup.setObjects(
      *(("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpScrambling"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpDeScrambling"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTribTestSigGenMode"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTribTestSigMonMode"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpLineSigGenMode"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpLineSigMonMode"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpAlarmReportControl"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTamType"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpLoopback"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpConfiguredServiceType"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpi15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpiDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpi15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpiDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpss15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpssDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpss15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpssDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpss15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpssDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpss15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpssDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRps15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpsDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTps15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpsDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpe15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpeDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpe15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpeDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRf15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRfDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTf15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTfDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRef15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRefDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTef15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTefDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRo15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRoDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTo15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxToDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxREo15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxREoDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTEo15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTEoDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRFs15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRFsDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTFs15MinutesTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTFsDayTce"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpi15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpiDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpi15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpiDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpss15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpssDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpss15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpssDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRps15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpsDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTps15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpsDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpe15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRpeDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpe15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTpeDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRf15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRfDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTf15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTfDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRef15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRefDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTef15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTefDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRo15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRoDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTo15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxToDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxREo15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxREoDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTEo15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTEoDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRFs15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpRxRFsDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTFs15MinutesTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpTxTFsDayTceReporting"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpServiceMode"),
        ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpServiceModeQualifier"))
)
if mibBuilder.loadTexts:
    fcClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 26, 3, 1, 1)
)
fcClientCtpCompliance.setObjects(
    ("INFINERA-TP-FCCLIENTCTP-MIB", "fcClientCtpGroup")
)
if mibBuilder.loadTexts:
    fcClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FCCLIENTCTP-MIB",
    **{"fcClientCtpMIB": fcClientCtpMIB,
       "fcClientCtpTable": fcClientCtpTable,
       "fcClientCtpEntry": fcClientCtpEntry,
       "fcClientCtpScrambling": fcClientCtpScrambling,
       "fcClientCtpDeScrambling": fcClientCtpDeScrambling,
       "fcClientCtpTribTestSigGenMode": fcClientCtpTribTestSigGenMode,
       "fcClientCtpTribTestSigMonMode": fcClientCtpTribTestSigMonMode,
       "fcClientCtpLineSigGenMode": fcClientCtpLineSigGenMode,
       "fcClientCtpLineSigMonMode": fcClientCtpLineSigMonMode,
       "fcClientCtpPmHistStatsEnable": fcClientCtpPmHistStatsEnable,
       "fcClientCtpAlarmReportControl": fcClientCtpAlarmReportControl,
       "fcClientCtpSupportingCircuitIdList": fcClientCtpSupportingCircuitIdList,
       "fcClientCtpTamType": fcClientCtpTamType,
       "fcClientCtpLoopback": fcClientCtpLoopback,
       "fcClientCtpConfiguredServiceType": fcClientCtpConfiguredServiceType,
       "fcClientCtpRxRpi15MinutesTce": fcClientCtpRxRpi15MinutesTce,
       "fcClientCtpRxRpiDayTce": fcClientCtpRxRpiDayTce,
       "fcClientCtpTxTpi15MinutesTce": fcClientCtpTxTpi15MinutesTce,
       "fcClientCtpTxTpiDayTce": fcClientCtpTxTpiDayTce,
       "fcClientCtpRxRpss15MinutesTce": fcClientCtpRxRpss15MinutesTce,
       "fcClientCtpRxRpssDayTce": fcClientCtpRxRpssDayTce,
       "fcClientCtpTxTpss15MinutesTce": fcClientCtpTxTpss15MinutesTce,
       "fcClientCtpTxTpssDayTce": fcClientCtpTxTpssDayTce,
       "fcClientCtpRxRps15MinutesTce": fcClientCtpRxRps15MinutesTce,
       "fcClientCtpRxRpsDayTce": fcClientCtpRxRpsDayTce,
       "fcClientCtpTxTps15MinutesTce": fcClientCtpTxTps15MinutesTce,
       "fcClientCtpTxTpsDayTce": fcClientCtpTxTpsDayTce,
       "fcClientCtpRxRpe15MinutesTce": fcClientCtpRxRpe15MinutesTce,
       "fcClientCtpRxRpeDayTce": fcClientCtpRxRpeDayTce,
       "fcClientCtpTxTpe15MinutesTce": fcClientCtpTxTpe15MinutesTce,
       "fcClientCtpTxTpeDayTce": fcClientCtpTxTpeDayTce,
       "fcClientCtpRxRf15MinutesTce": fcClientCtpRxRf15MinutesTce,
       "fcClientCtpRxRfDayTce": fcClientCtpRxRfDayTce,
       "fcClientCtpTxTf15MinutesTce": fcClientCtpTxTf15MinutesTce,
       "fcClientCtpTxTfDayTce": fcClientCtpTxTfDayTce,
       "fcClientCtpRxRef15MinutesTce": fcClientCtpRxRef15MinutesTce,
       "fcClientCtpRxRefDayTce": fcClientCtpRxRefDayTce,
       "fcClientCtpTxTef15MinutesTce": fcClientCtpTxTef15MinutesTce,
       "fcClientCtpTxTefDayTce": fcClientCtpTxTefDayTce,
       "fcClientCtpRxRo15MinutesTce": fcClientCtpRxRo15MinutesTce,
       "fcClientCtpRxRoDayTce": fcClientCtpRxRoDayTce,
       "fcClientCtpTxTo15MinutesTce": fcClientCtpTxTo15MinutesTce,
       "fcClientCtpTxToDayTce": fcClientCtpTxToDayTce,
       "fcClientCtpRxREo15MinutesTce": fcClientCtpRxREo15MinutesTce,
       "fcClientCtpRxREoDayTce": fcClientCtpRxREoDayTce,
       "fcClientCtpTxTEo15MinutesTce": fcClientCtpTxTEo15MinutesTce,
       "fcClientCtpTxTEoDayTce": fcClientCtpTxTEoDayTce,
       "fcClientCtpRxRFs15MinutesTce": fcClientCtpRxRFs15MinutesTce,
       "fcClientCtpRxRFsDayTce": fcClientCtpRxRFsDayTce,
       "fcClientCtpTxTFs15MinutesTce": fcClientCtpTxTFs15MinutesTce,
       "fcClientCtpTxTFsDayTce": fcClientCtpTxTFsDayTce,
       "fcClientCtpRxRpi15MinutesTceReporting": fcClientCtpRxRpi15MinutesTceReporting,
       "fcClientCtpRxRpiDayTceReporting": fcClientCtpRxRpiDayTceReporting,
       "fcClientCtpTxTpi15MinutesTceReporting": fcClientCtpTxTpi15MinutesTceReporting,
       "fcClientCtpTxTpiDayTceReporting": fcClientCtpTxTpiDayTceReporting,
       "fcClientCtpRxRpss15MinutesTceReporting": fcClientCtpRxRpss15MinutesTceReporting,
       "fcClientCtpRxRpssDayTceReporting": fcClientCtpRxRpssDayTceReporting,
       "fcClientCtpTxTpss15MinutesTceReporting": fcClientCtpTxTpss15MinutesTceReporting,
       "fcClientCtpTxTpssDayTceReporting": fcClientCtpTxTpssDayTceReporting,
       "fcClientCtpRxRps15MinutesTceReporting": fcClientCtpRxRps15MinutesTceReporting,
       "fcClientCtpRxRpsDayTceReporting": fcClientCtpRxRpsDayTceReporting,
       "fcClientCtpTxTps15MinutesTceReporting": fcClientCtpTxTps15MinutesTceReporting,
       "fcClientCtpTxTpsDayTceReporting": fcClientCtpTxTpsDayTceReporting,
       "fcClientCtpRxRpe15MinutesTceReporting": fcClientCtpRxRpe15MinutesTceReporting,
       "fcClientCtpRxRpeDayTceReporting": fcClientCtpRxRpeDayTceReporting,
       "fcClientCtpTxTpe15MinutesTceReporting": fcClientCtpTxTpe15MinutesTceReporting,
       "fcClientCtpTxTpeDayTceReporting": fcClientCtpTxTpeDayTceReporting,
       "fcClientCtpRxRf15MinutesTceReporting": fcClientCtpRxRf15MinutesTceReporting,
       "fcClientCtpRxRfDayTceReporting": fcClientCtpRxRfDayTceReporting,
       "fcClientCtpTxTf15MinutesTceReporting": fcClientCtpTxTf15MinutesTceReporting,
       "fcClientCtpTxTfDayTceReporting": fcClientCtpTxTfDayTceReporting,
       "fcClientCtpRxRef15MinutesTceReporting": fcClientCtpRxRef15MinutesTceReporting,
       "fcClientCtpRxRefDayTceReporting": fcClientCtpRxRefDayTceReporting,
       "fcClientCtpTxTef15MinutesTceReporting": fcClientCtpTxTef15MinutesTceReporting,
       "fcClientCtpTxTefDayTceReporting": fcClientCtpTxTefDayTceReporting,
       "fcClientCtpRxRo15MinutesTceReporting": fcClientCtpRxRo15MinutesTceReporting,
       "fcClientCtpRxRoDayTceReporting": fcClientCtpRxRoDayTceReporting,
       "fcClientCtpTxTo15MinutesTceReporting": fcClientCtpTxTo15MinutesTceReporting,
       "fcClientCtpTxToDayTceReporting": fcClientCtpTxToDayTceReporting,
       "fcClientCtpRxREo15MinutesTceReporting": fcClientCtpRxREo15MinutesTceReporting,
       "fcClientCtpRxREoDayTceReporting": fcClientCtpRxREoDayTceReporting,
       "fcClientCtpTxTEo15MinutesTceReporting": fcClientCtpTxTEo15MinutesTceReporting,
       "fcClientCtpTxTEoDayTceReporting": fcClientCtpTxTEoDayTceReporting,
       "fcClientCtpRxRFs15MinutesTceReporting": fcClientCtpRxRFs15MinutesTceReporting,
       "fcClientCtpRxRFsDayTceReporting": fcClientCtpRxRFsDayTceReporting,
       "fcClientCtpTxTFs15MinutesTceReporting": fcClientCtpTxTFs15MinutesTceReporting,
       "fcClientCtpTxTFsDayTceReporting": fcClientCtpTxTFsDayTceReporting,
       "fcClientCtpServiceMode": fcClientCtpServiceMode,
       "fcClientCtpServiceModeQualifier": fcClientCtpServiceModeQualifier,
       "fcClientCtpConformance": fcClientCtpConformance,
       "fcClientCtpCompliances": fcClientCtpCompliances,
       "fcClientCtpCompliance": fcClientCtpCompliance,
       "fcClientCtpGroups": fcClientCtpGroups,
       "fcClientCtpGroup": fcClientCtpGroup}
)
