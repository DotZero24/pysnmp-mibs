# SNMP MIB module (INFINERA-TP-OTUKICTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OTUKICTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:10 2025
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

(FloatTenths,
 InfnArc,
 InfnEnableDisable,
 InfnEqptType,
 InfnMonitoringMode,
 InfnOtuBitRateK,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnArc",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnMonitoringMode",
    "InfnOtuBitRateK",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType")

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

otukiCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31)
)
if mibBuilder.loadTexts:
    otukiCtpMIB.setRevisions(
        ("2009-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtukiCtpTable_Object = MibTable
otukiCtpTable = _OtukiCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1)
)
if mibBuilder.loadTexts:
    otukiCtpTable.setStatus("current")
_OtukiCtpEntry_Object = MibTableRow
otukiCtpEntry = _OtukiCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1)
)
otukiCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otukiCtpEntry.setStatus("current")


class _OtukiCtpServiceMode_Type(InfnServiceMode):
    """Custom type otukiCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_OtukiCtpServiceMode_Type.__name__ = "InfnServiceMode"
_OtukiCtpServiceMode_Object = MibTableColumn
otukiCtpServiceMode = _OtukiCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 1),
    _OtukiCtpServiceMode_Type()
)
otukiCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpServiceMode.setStatus("current")


class _OtukiCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type otukiCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_OtukiCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_OtukiCtpServiceModeQualifier_Object = MibTableColumn
otukiCtpServiceModeQualifier = _OtukiCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 2),
    _OtukiCtpServiceModeQualifier_Type()
)
otukiCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpServiceModeQualifier.setStatus("current")


class _OtukiCtpFecCorrection_Type(InfnEnableDisable):
    """Custom type otukiCtpFecCorrection based on InfnEnableDisable"""
    defaultValue = 2


_OtukiCtpFecCorrection_Type.__name__ = "InfnEnableDisable"
_OtukiCtpFecCorrection_Object = MibTableColumn
otukiCtpFecCorrection = _OtukiCtpFecCorrection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 3),
    _OtukiCtpFecCorrection_Type()
)
otukiCtpFecCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFecCorrection.setStatus("current")


class _OtukiCtpFecEnabled_Type(InfnEnableDisable):
    """Custom type otukiCtpFecEnabled based on InfnEnableDisable"""
    defaultValue = 2


_OtukiCtpFecEnabled_Type.__name__ = "InfnEnableDisable"
_OtukiCtpFecEnabled_Object = MibTableColumn
otukiCtpFecEnabled = _OtukiCtpFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 4),
    _OtukiCtpFecEnabled_Type()
)
otukiCtpFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFecEnabled.setStatus("current")


class _OtukiFecDecoderIterationCount_Type(Integer32):
    """Custom type otukiFecDecoderIterationCount based on Integer32"""
    defaultValue = 3


_OtukiFecDecoderIterationCount_Type.__name__ = "Integer32"
_OtukiFecDecoderIterationCount_Object = MibTableColumn
otukiFecDecoderIterationCount = _OtukiFecDecoderIterationCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 5),
    _OtukiFecDecoderIterationCount_Type()
)
otukiFecDecoderIterationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiFecDecoderIterationCount.setStatus("current")
_OtukpropagationDelay_Type = FloatTenths
_OtukpropagationDelay_Object = MibTableColumn
otukpropagationDelay = _OtukpropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 6),
    _OtukpropagationDelay_Type()
)
otukpropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukpropagationDelay.setStatus("current")
_OtukiBitRateK_Type = InfnOtuBitRateK
_OtukiBitRateK_Object = MibTableColumn
otukiBitRateK = _OtukiBitRateK_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 7),
    _OtukiBitRateK_Type()
)
otukiBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiBitRateK.setStatus("current")


class _OtukiCtpFacTxTTI_Type(DisplayString):
    """Custom type otukiCtpFacTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtukiCtpFacTxTTI_Type.__name__ = "DisplayString"
_OtukiCtpFacTxTTI_Object = MibTableColumn
otukiCtpFacTxTTI = _OtukiCtpFacTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 8),
    _OtukiCtpFacTxTTI_Type()
)
otukiCtpFacTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacTxTTI.setStatus("current")


class _OtukiCtpFacExpectedSAPI_Type(DisplayString):
    """Custom type otukiCtpFacExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtukiCtpFacExpectedSAPI_Type.__name__ = "DisplayString"
_OtukiCtpFacExpectedSAPI_Object = MibTableColumn
otukiCtpFacExpectedSAPI = _OtukiCtpFacExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 9),
    _OtukiCtpFacExpectedSAPI_Type()
)
otukiCtpFacExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacExpectedSAPI.setStatus("current")


class _OtukiCtpFacExpectedDAPI_Type(DisplayString):
    """Custom type otukiCtpFacExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtukiCtpFacExpectedDAPI_Type.__name__ = "DisplayString"
_OtukiCtpFacExpectedDAPI_Object = MibTableColumn
otukiCtpFacExpectedDAPI = _OtukiCtpFacExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 10),
    _OtukiCtpFacExpectedDAPI_Type()
)
otukiCtpFacExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacExpectedDAPI.setStatus("current")


class _OtukiCtpFacRxTTI_Type(DisplayString):
    """Custom type otukiCtpFacRxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtukiCtpFacRxTTI_Type.__name__ = "DisplayString"
_OtukiCtpFacRxTTI_Object = MibTableColumn
otukiCtpFacRxTTI = _OtukiCtpFacRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 11),
    _OtukiCtpFacRxTTI_Type()
)
otukiCtpFacRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpFacRxTTI.setStatus("current")


class _OtukiCtpFacPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type otukiCtpFacPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OtukiCtpFacPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OtukiCtpFacPmHistStatsEnable_Object = MibTableColumn
otukiCtpFacPmHistStatsEnable = _OtukiCtpFacPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 12),
    _OtukiCtpFacPmHistStatsEnable_Type()
)
otukiCtpFacPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacPmHistStatsEnable.setStatus("current")
_OtukiCtpFacMonitoringMode_Type = InfnMonitoringMode
_OtukiCtpFacMonitoringMode_Object = MibTableColumn
otukiCtpFacMonitoringMode = _OtukiCtpFacMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 13),
    _OtukiCtpFacMonitoringMode_Type()
)
otukiCtpFacMonitoringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpFacMonitoringMode.setStatus("current")


class _OtukiCtpFacDSThreshold_Type(Integer32):
    """Custom type otukiCtpFacDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OtukiCtpFacDSThreshold_Type.__name__ = "Integer32"
_OtukiCtpFacDSThreshold_Object = MibTableColumn
otukiCtpFacDSThreshold = _OtukiCtpFacDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 14),
    _OtukiCtpFacDSThreshold_Type()
)
otukiCtpFacDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacDSThreshold.setStatus("current")


class _OtukiCtpFacSDThreshold_Type(Integer32):
    """Custom type otukiCtpFacSDThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OtukiCtpFacSDThreshold_Type.__name__ = "Integer32"
_OtukiCtpFacSDThreshold_Object = MibTableColumn
otukiCtpFacSDThreshold = _OtukiCtpFacSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 15),
    _OtukiCtpFacSDThreshold_Type()
)
otukiCtpFacSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacSDThreshold.setStatus("current")


class _OtukiCtpFacTimDetMode_Type(Integer32):
    """Custom type otukiCtpFacTimDetMode based on Integer32"""
    defaultValue = 1

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
        *(("off", 1),
          ("sapi", 2),
          ("dapi", 3),
          ("sapidapi", 4))
    )


_OtukiCtpFacTimDetMode_Type.__name__ = "Integer32"
_OtukiCtpFacTimDetMode_Object = MibTableColumn
otukiCtpFacTimDetMode = _OtukiCtpFacTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 16),
    _OtukiCtpFacTimDetMode_Type()
)
otukiCtpFacTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpFacTimDetMode.setStatus("current")
_OtukiCtpSupportingOchList_Type = DisplayString
_OtukiCtpSupportingOchList_Object = MibTableColumn
otukiCtpSupportingOchList = _OtukiCtpSupportingOchList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 17),
    _OtukiCtpSupportingOchList_Type()
)
otukiCtpSupportingOchList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpSupportingOchList.setStatus("current")


class _OtukiCtpRxEb15MinutesTce_Type(Integer32):
    """Custom type otukiCtpRxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OtukiCtpRxEb15MinutesTce_Type.__name__ = "Integer32"
_OtukiCtpRxEb15MinutesTce_Object = MibTableColumn
otukiCtpRxEb15MinutesTce = _OtukiCtpRxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 18),
    _OtukiCtpRxEb15MinutesTce_Type()
)
otukiCtpRxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxEb15MinutesTce.setStatus("current")


class _OtukiCtpRxEbDayTce_Type(Integer32):
    """Custom type otukiCtpRxEbDayTce based on Integer32"""
    defaultValue = 15000


_OtukiCtpRxEbDayTce_Type.__name__ = "Integer32"
_OtukiCtpRxEbDayTce_Object = MibTableColumn
otukiCtpRxEbDayTce = _OtukiCtpRxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 19),
    _OtukiCtpRxEbDayTce_Type()
)
otukiCtpRxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxEbDayTce.setStatus("current")


class _OtukiCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type otukiCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OtukiCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OtukiCtpRxDs15MinutesTce_Object = MibTableColumn
otukiCtpRxDs15MinutesTce = _OtukiCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 20),
    _OtukiCtpRxDs15MinutesTce_Type()
)
otukiCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxDs15MinutesTce.setStatus("current")


class _OtukiCtpRxDsDayTce_Type(Integer32):
    """Custom type otukiCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OtukiCtpRxDsDayTce_Type.__name__ = "Integer32"
_OtukiCtpRxDsDayTce_Object = MibTableColumn
otukiCtpRxDsDayTce = _OtukiCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 21),
    _OtukiCtpRxDsDayTce_Type()
)
otukiCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxDsDayTce.setStatus("current")


class _OtukiCtpRxEbDayTceReporting_Type(TruthValue):
    """Custom type otukiCtpRxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtukiCtpRxEbDayTceReporting_Type.__name__ = "TruthValue"
_OtukiCtpRxEbDayTceReporting_Object = MibTableColumn
otukiCtpRxEbDayTceReporting = _OtukiCtpRxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 22),
    _OtukiCtpRxEbDayTceReporting_Type()
)
otukiCtpRxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxEbDayTceReporting.setStatus("current")


class _OtukiCtpRxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type otukiCtpRxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtukiCtpRxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtukiCtpRxEb15MinutesTceReporting_Object = MibTableColumn
otukiCtpRxEb15MinutesTceReporting = _OtukiCtpRxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 23),
    _OtukiCtpRxEb15MinutesTceReporting_Type()
)
otukiCtpRxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxEb15MinutesTceReporting.setStatus("current")


class _OtukiCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type otukiCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtukiCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OtukiCtpRxDsDayTceReporting_Object = MibTableColumn
otukiCtpRxDsDayTceReporting = _OtukiCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 24),
    _OtukiCtpRxDsDayTceReporting_Type()
)
otukiCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxDsDayTceReporting.setStatus("current")


class _OtukiCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type otukiCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtukiCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtukiCtpRxDs15MinutesTceReporting_Object = MibTableColumn
otukiCtpRxDs15MinutesTceReporting = _OtukiCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 25),
    _OtukiCtpRxDs15MinutesTceReporting_Type()
)
otukiCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpRxDs15MinutesTceReporting.setStatus("current")


class _OtukiCtpAlarmReportControl_Type(InfnArc):
    """Custom type otukiCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OtukiCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OtukiCtpAlarmReportControl_Object = MibTableColumn
otukiCtpAlarmReportControl = _OtukiCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 26),
    _OtukiCtpAlarmReportControl_Type()
)
otukiCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otukiCtpAlarmReportControl.setStatus("current")
_OtukiCtpConfiguredServiceType_Type = InfnServiceType
_OtukiCtpConfiguredServiceType_Object = MibTableColumn
otukiCtpConfiguredServiceType = _OtukiCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 1, 1, 27),
    _OtukiCtpConfiguredServiceType_Type()
)
otukiCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otukiCtpConfiguredServiceType.setStatus("current")
_OtukiCtpConformance_ObjectIdentity = ObjectIdentity
otukiCtpConformance = _OtukiCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 3)
)
_OtukiCtpCompliances_ObjectIdentity = ObjectIdentity
otukiCtpCompliances = _OtukiCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 3, 1)
)
_OtukiCtpGroups_ObjectIdentity = ObjectIdentity
otukiCtpGroups = _OtukiCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 3, 2)
)

# Managed Objects groups

otukiCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 3, 2, 1)
)
otukiCtpGroup.setObjects(
      *(("INFINERA-TP-OTUKICTP-MIB", "otukiCtpServiceMode"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpServiceModeQualifier"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFecCorrection"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFecEnabled"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiFecDecoderIterationCount"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukpropagationDelay"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiBitRateK"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacTxTTI"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacExpectedSAPI"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacExpectedDAPI"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacRxTTI"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacPmHistStatsEnable"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacMonitoringMode"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacDSThreshold"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacSDThreshold"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpFacTimDetMode"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpSupportingOchList"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxEb15MinutesTce"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxEbDayTce"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxDs15MinutesTce"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxDsDayTce"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxEbDayTceReporting"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxEb15MinutesTceReporting"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxDsDayTceReporting"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpAlarmReportControl"),
        ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpConfiguredServiceType"))
)
if mibBuilder.loadTexts:
    otukiCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otukiCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 31, 3, 1, 1)
)
otukiCtpCompliance.setObjects(
    ("INFINERA-TP-OTUKICTP-MIB", "otukiCtpGroup")
)
if mibBuilder.loadTexts:
    otukiCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OTUKICTP-MIB",
    **{"otukiCtpMIB": otukiCtpMIB,
       "otukiCtpTable": otukiCtpTable,
       "otukiCtpEntry": otukiCtpEntry,
       "otukiCtpServiceMode": otukiCtpServiceMode,
       "otukiCtpServiceModeQualifier": otukiCtpServiceModeQualifier,
       "otukiCtpFecCorrection": otukiCtpFecCorrection,
       "otukiCtpFecEnabled": otukiCtpFecEnabled,
       "otukiFecDecoderIterationCount": otukiFecDecoderIterationCount,
       "otukpropagationDelay": otukpropagationDelay,
       "otukiBitRateK": otukiBitRateK,
       "otukiCtpFacTxTTI": otukiCtpFacTxTTI,
       "otukiCtpFacExpectedSAPI": otukiCtpFacExpectedSAPI,
       "otukiCtpFacExpectedDAPI": otukiCtpFacExpectedDAPI,
       "otukiCtpFacRxTTI": otukiCtpFacRxTTI,
       "otukiCtpFacPmHistStatsEnable": otukiCtpFacPmHistStatsEnable,
       "otukiCtpFacMonitoringMode": otukiCtpFacMonitoringMode,
       "otukiCtpFacDSThreshold": otukiCtpFacDSThreshold,
       "otukiCtpFacSDThreshold": otukiCtpFacSDThreshold,
       "otukiCtpFacTimDetMode": otukiCtpFacTimDetMode,
       "otukiCtpSupportingOchList": otukiCtpSupportingOchList,
       "otukiCtpRxEb15MinutesTce": otukiCtpRxEb15MinutesTce,
       "otukiCtpRxEbDayTce": otukiCtpRxEbDayTce,
       "otukiCtpRxDs15MinutesTce": otukiCtpRxDs15MinutesTce,
       "otukiCtpRxDsDayTce": otukiCtpRxDsDayTce,
       "otukiCtpRxEbDayTceReporting": otukiCtpRxEbDayTceReporting,
       "otukiCtpRxEb15MinutesTceReporting": otukiCtpRxEb15MinutesTceReporting,
       "otukiCtpRxDsDayTceReporting": otukiCtpRxDsDayTceReporting,
       "otukiCtpRxDs15MinutesTceReporting": otukiCtpRxDs15MinutesTceReporting,
       "otukiCtpAlarmReportControl": otukiCtpAlarmReportControl,
       "otukiCtpConfiguredServiceType": otukiCtpConfiguredServiceType,
       "otukiCtpConformance": otukiCtpConformance,
       "otukiCtpCompliances": otukiCtpCompliances,
       "otukiCtpCompliance": otukiCtpCompliance,
       "otukiCtpGroups": otukiCtpGroups,
       "otukiCtpGroup": otukiCtpGroup}
)
