# SNMP MIB module (INFINERA-TP-ODUICLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ODUICLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:03 2025
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
 InfnMonitoringMode,
 InfnOtuBitRateK,
 InfnRate,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType,
 InfnTcmList,
 InfnTsgType,
 InfnXconType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnArc",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnMonitoringMode",
    "InfnOtuBitRateK",
    "InfnRate",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType",
    "InfnTcmList",
    "InfnTsgType",
    "InfnXconType")

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

oduiClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30)
)
if mibBuilder.loadTexts:
    oduiClientCtpMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduiClientCtpTable_Object = MibTable
oduiClientCtpTable = _OduiClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1)
)
if mibBuilder.loadTexts:
    oduiClientCtpTable.setStatus("current")
_OduiClientCtpEntry_Object = MibTableRow
oduiClientCtpEntry = _OduiClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1)
)
oduiClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduiClientCtpEntry.setStatus("current")


class _OduiClientCtpServiceMode_Type(InfnServiceMode):
    """Custom type oduiClientCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_OduiClientCtpServiceMode_Type.__name__ = "InfnServiceMode"
_OduiClientCtpServiceMode_Object = MibTableColumn
oduiClientCtpServiceMode = _OduiClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 1),
    _OduiClientCtpServiceMode_Type()
)
oduiClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpServiceMode.setStatus("current")


class _OduiClientCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type oduiClientCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_OduiClientCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_OduiClientCtpServiceModeQualifier_Object = MibTableColumn
oduiClientCtpServiceModeQualifier = _OduiClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 2),
    _OduiClientCtpServiceModeQualifier_Type()
)
oduiClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpServiceModeQualifier.setStatus("current")
_OduiClientCtpFacMonitoringMode_Type = InfnMonitoringMode
_OduiClientCtpFacMonitoringMode_Object = MibTableColumn
oduiClientCtpFacMonitoringMode = _OduiClientCtpFacMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 3),
    _OduiClientCtpFacMonitoringMode_Type()
)
oduiClientCtpFacMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacMonitoringMode.setStatus("current")


class _OduiClientCtpFacTxTTI_Type(DisplayString):
    """Custom type oduiClientCtpFacTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiClientCtpFacTxTTI_Type.__name__ = "DisplayString"
_OduiClientCtpFacTxTTI_Object = MibTableColumn
oduiClientCtpFacTxTTI = _OduiClientCtpFacTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 4),
    _OduiClientCtpFacTxTTI_Type()
)
oduiClientCtpFacTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacTxTTI.setStatus("current")


class _OduiClientCtpFacExpectedSAPI_Type(DisplayString):
    """Custom type oduiClientCtpFacExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiClientCtpFacExpectedSAPI_Type.__name__ = "DisplayString"
_OduiClientCtpFacExpectedSAPI_Object = MibTableColumn
oduiClientCtpFacExpectedSAPI = _OduiClientCtpFacExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 5),
    _OduiClientCtpFacExpectedSAPI_Type()
)
oduiClientCtpFacExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacExpectedSAPI.setStatus("current")


class _OduiClientCtpFacExpectedDAPI_Type(DisplayString):
    """Custom type oduiClientCtpFacExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiClientCtpFacExpectedDAPI_Type.__name__ = "DisplayString"
_OduiClientCtpFacExpectedDAPI_Object = MibTableColumn
oduiClientCtpFacExpectedDAPI = _OduiClientCtpFacExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 6),
    _OduiClientCtpFacExpectedDAPI_Type()
)
oduiClientCtpFacExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacExpectedDAPI.setStatus("current")


class _OduiClientCtpTermTxTTI_Type(DisplayString):
    """Custom type oduiClientCtpTermTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiClientCtpTermTxTTI_Type.__name__ = "DisplayString"
_OduiClientCtpTermTxTTI_Object = MibTableColumn
oduiClientCtpTermTxTTI = _OduiClientCtpTermTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 7),
    _OduiClientCtpTermTxTTI_Type()
)
oduiClientCtpTermTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermTxTTI.setStatus("current")


class _OduiClientCtpTermExpectedSAPI_Type(DisplayString):
    """Custom type oduiClientCtpTermExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiClientCtpTermExpectedSAPI_Type.__name__ = "DisplayString"
_OduiClientCtpTermExpectedSAPI_Object = MibTableColumn
oduiClientCtpTermExpectedSAPI = _OduiClientCtpTermExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 8),
    _OduiClientCtpTermExpectedSAPI_Type()
)
oduiClientCtpTermExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermExpectedSAPI.setStatus("current")


class _OduiClientCtpTermExpectedDAPI_Type(DisplayString):
    """Custom type oduiClientCtpTermExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiClientCtpTermExpectedDAPI_Type.__name__ = "DisplayString"
_OduiClientCtpTermExpectedDAPI_Object = MibTableColumn
oduiClientCtpTermExpectedDAPI = _OduiClientCtpTermExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 9),
    _OduiClientCtpTermExpectedDAPI_Type()
)
oduiClientCtpTermExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermExpectedDAPI.setStatus("current")


class _OduiClientCtpFacReceivedTTI_Type(DisplayString):
    """Custom type oduiClientCtpFacReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiClientCtpFacReceivedTTI_Type.__name__ = "DisplayString"
_OduiClientCtpFacReceivedTTI_Object = MibTableColumn
oduiClientCtpFacReceivedTTI = _OduiClientCtpFacReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 10),
    _OduiClientCtpFacReceivedTTI_Type()
)
oduiClientCtpFacReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpFacReceivedTTI.setStatus("current")


class _OduiClientCtpTermReceivedTTI_Type(DisplayString):
    """Custom type oduiClientCtpTermReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiClientCtpTermReceivedTTI_Type.__name__ = "DisplayString"
_OduiClientCtpTermReceivedTTI_Object = MibTableColumn
oduiClientCtpTermReceivedTTI = _OduiClientCtpTermReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 11),
    _OduiClientCtpTermReceivedTTI_Type()
)
oduiClientCtpTermReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpTermReceivedTTI.setStatus("current")


class _OduiClientCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type oduiClientCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OduiClientCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OduiClientCtpRxDs15MinutesTce_Object = MibTableColumn
oduiClientCtpRxDs15MinutesTce = _OduiClientCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 12),
    _OduiClientCtpRxDs15MinutesTce_Type()
)
oduiClientCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDs15MinutesTce.setStatus("current")


class _OduiClientCtpRxDsDayTce_Type(Integer32):
    """Custom type oduiClientCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OduiClientCtpRxDsDayTce_Type.__name__ = "Integer32"
_OduiClientCtpRxDsDayTce_Object = MibTableColumn
oduiClientCtpRxDsDayTce = _OduiClientCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 13),
    _OduiClientCtpRxDsDayTce_Type()
)
oduiClientCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsDayTce.setStatus("current")


class _OduiClientCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type oduiClientCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduiClientCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OduiClientCtpRxDsDayTceReporting_Object = MibTableColumn
oduiClientCtpRxDsDayTceReporting = _OduiClientCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 14),
    _OduiClientCtpRxDsDayTceReporting_Type()
)
oduiClientCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsDayTceReporting.setStatus("current")


class _OduiClientCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type oduiClientCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduiClientCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduiClientCtpRxDs15MinutesTceReporting_Object = MibTableColumn
oduiClientCtpRxDs15MinutesTceReporting = _OduiClientCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 15),
    _OduiClientCtpRxDs15MinutesTceReporting_Type()
)
oduiClientCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDs15MinutesTceReporting.setStatus("current")


class _OduiClientCtpFacTimDetMode_Type(Integer32):
    """Custom type oduiClientCtpFacTimDetMode based on Integer32"""
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


_OduiClientCtpFacTimDetMode_Type.__name__ = "Integer32"
_OduiClientCtpFacTimDetMode_Object = MibTableColumn
oduiClientCtpFacTimDetMode = _OduiClientCtpFacTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 16),
    _OduiClientCtpFacTimDetMode_Type()
)
oduiClientCtpFacTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacTimDetMode.setStatus("current")


class _OduiClientCtpTermTimDetMode_Type(Integer32):
    """Custom type oduiClientCtpTermTimDetMode based on Integer32"""
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


_OduiClientCtpTermTimDetMode_Type.__name__ = "Integer32"
_OduiClientCtpTermTimDetMode_Object = MibTableColumn
oduiClientCtpTermTimDetMode = _OduiClientCtpTermTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 17),
    _OduiClientCtpTermTimDetMode_Type()
)
oduiClientCtpTermTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermTimDetMode.setStatus("current")
_OduiClientCtpTcmList_Type = InfnTcmList
_OduiClientCtpTcmList_Object = MibTableColumn
oduiClientCtpTcmList = _OduiClientCtpTcmList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 18),
    _OduiClientCtpTcmList_Type()
)
oduiClientCtpTcmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpTcmList.setStatus("current")
_OduiClientCtpConfiguredServiceType_Type = InfnServiceType
_OduiClientCtpConfiguredServiceType_Object = MibTableColumn
oduiClientCtpConfiguredServiceType = _OduiClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 19),
    _OduiClientCtpConfiguredServiceType_Type()
)
oduiClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpConfiguredServiceType.setStatus("current")


class _OduiClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type oduiClientCtpFacPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OduiClientCtpFacPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OduiClientCtpFacPmHistStatsEnable_Object = MibTableColumn
oduiClientCtpFacPmHistStatsEnable = _OduiClientCtpFacPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 20),
    _OduiClientCtpFacPmHistStatsEnable_Type()
)
oduiClientCtpFacPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacPmHistStatsEnable.setStatus("current")


class _OduiClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type oduiClientCtpTermPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OduiClientCtpTermPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OduiClientCtpTermPmHistStatsEnable_Object = MibTableColumn
oduiClientCtpTermPmHistStatsEnable = _OduiClientCtpTermPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 21),
    _OduiClientCtpTermPmHistStatsEnable_Type()
)
oduiClientCtpTermPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermPmHistStatsEnable.setStatus("current")


class _OduiClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type oduiClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OduiClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OduiClientCtpAlarmReportControl_Object = MibTableColumn
oduiClientCtpAlarmReportControl = _OduiClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 22),
    _OduiClientCtpAlarmReportControl_Type()
)
oduiClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpAlarmReportControl.setStatus("current")
_OduiClientCtpSupportingCircuitIdList_Type = DisplayString
_OduiClientCtpSupportingCircuitIdList_Object = MibTableColumn
oduiClientCtpSupportingCircuitIdList = _OduiClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 23),
    _OduiClientCtpSupportingCircuitIdList_Type()
)
oduiClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpSupportingCircuitIdList.setStatus("current")


class _OduiClientCtpFacDSThreshold_Type(Integer32):
    """Custom type oduiClientCtpFacDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduiClientCtpFacDSThreshold_Type.__name__ = "Integer32"
_OduiClientCtpFacDSThreshold_Object = MibTableColumn
oduiClientCtpFacDSThreshold = _OduiClientCtpFacDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 24),
    _OduiClientCtpFacDSThreshold_Type()
)
oduiClientCtpFacDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacDSThreshold.setStatus("current")


class _OduiClientCtpTermDSThreshold_Type(Integer32):
    """Custom type oduiClientCtpTermDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduiClientCtpTermDSThreshold_Type.__name__ = "Integer32"
_OduiClientCtpTermDSThreshold_Object = MibTableColumn
oduiClientCtpTermDSThreshold = _OduiClientCtpTermDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 25),
    _OduiClientCtpTermDSThreshold_Type()
)
oduiClientCtpTermDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermDSThreshold.setStatus("current")
_OduiClientCtpTermMonitoringMode_Type = InfnMonitoringMode
_OduiClientCtpTermMonitoringMode_Object = MibTableColumn
oduiClientCtpTermMonitoringMode = _OduiClientCtpTermMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 26),
    _OduiClientCtpTermMonitoringMode_Type()
)
oduiClientCtpTermMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTermMonitoringMode.setStatus("current")
_OduiClientCtpTSCount_Type = Integer32
_OduiClientCtpTSCount_Object = MibTableColumn
oduiClientCtpTSCount = _OduiClientCtpTSCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 28),
    _OduiClientCtpTSCount_Type()
)
oduiClientCtpTSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpTSCount.setStatus("current")
_OduiClientCtprate_Type = DisplayString
_OduiClientCtprate_Object = MibTableColumn
oduiClientCtprate = _OduiClientCtprate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 29),
    _OduiClientCtprate_Type()
)
oduiClientCtprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtprate.setStatus("current")
_OduiClientCtpTributaryPortNumber_Type = Integer32
_OduiClientCtpTributaryPortNumber_Object = MibTableColumn
oduiClientCtpTributaryPortNumber = _OduiClientCtpTributaryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 30),
    _OduiClientCtpTributaryPortNumber_Type()
)
oduiClientCtpTributaryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpTributaryPortNumber.setStatus("current")
_OduiClientCtpExpectedTPNs_Type = Integer32
_OduiClientCtpExpectedTPNs_Object = MibTableColumn
oduiClientCtpExpectedTPNs = _OduiClientCtpExpectedTPNs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 31),
    _OduiClientCtpExpectedTPNs_Type()
)
oduiClientCtpExpectedTPNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpExpectedTPNs.setStatus("current")
_OduiClientCtpDetectedTPNs_Type = Integer32
_OduiClientCtpDetectedTPNs_Object = MibTableColumn
oduiClientCtpDetectedTPNs = _OduiClientCtpDetectedTPNs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 32),
    _OduiClientCtpDetectedTPNs_Type()
)
oduiClientCtpDetectedTPNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpDetectedTPNs.setStatus("current")
_OduiClientCtpsupportingOPUTributarySlots_Type = DisplayString
_OduiClientCtpsupportingOPUTributarySlots_Object = MibTableColumn
oduiClientCtpsupportingOPUTributarySlots = _OduiClientCtpsupportingOPUTributarySlots_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 33),
    _OduiClientCtpsupportingOPUTributarySlots_Type()
)
oduiClientCtpsupportingOPUTributarySlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpsupportingOPUTributarySlots.setStatus("current")
_OduiClientCtpavailableOPUTributarySlots_Type = DisplayString
_OduiClientCtpavailableOPUTributarySlots_Object = MibTableColumn
oduiClientCtpavailableOPUTributarySlots = _OduiClientCtpavailableOPUTributarySlots_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 34),
    _OduiClientCtpavailableOPUTributarySlots_Type()
)
oduiClientCtpavailableOPUTributarySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpavailableOPUTributarySlots.setStatus("current")
_OduiClientCtpdatarate_Type = InfnRate
_OduiClientCtpdatarate_Object = MibTableColumn
oduiClientCtpdatarate = _OduiClientCtpdatarate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 35),
    _OduiClientCtpdatarate_Type()
)
oduiClientCtpdatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpdatarate.setStatus("current")
_OduiClientCtpCrossConnectType_Type = InfnXconType
_OduiClientCtpCrossConnectType_Object = MibTableColumn
oduiClientCtpCrossConnectType = _OduiClientCtpCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 36),
    _OduiClientCtpCrossConnectType_Type()
)
oduiClientCtpCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpCrossConnectType.setStatus("current")
_OduiClientCtpSupportingTP_Type = DisplayString
_OduiClientCtpSupportingTP_Object = MibTableColumn
oduiClientCtpSupportingTP = _OduiClientCtpSupportingTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 37),
    _OduiClientCtpSupportingTP_Type()
)
oduiClientCtpSupportingTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpSupportingTP.setStatus("current")
_OduiClientCtpTsg_Type = InfnTsgType
_OduiClientCtpTsg_Object = MibTableColumn
oduiClientCtpTsg = _OduiClientCtpTsg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 38),
    _OduiClientCtpTsg_Type()
)
oduiClientCtpTsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpTsg.setStatus("current")
_OduiClientCtpExpectedPayload_Type = InfnServiceType
_OduiClientCtpExpectedPayload_Object = MibTableColumn
oduiClientCtpExpectedPayload = _OduiClientCtpExpectedPayload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 39),
    _OduiClientCtpExpectedPayload_Type()
)
oduiClientCtpExpectedPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpExpectedPayload.setStatus("current")


class _OduiClientCtpLoopBack_Type(Integer32):
    """Custom type oduiClientCtpLoopBack based on Integer32"""
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
        *(("none", 1),
          ("terminal", 2),
          ("facility", 3))
    )


_OduiClientCtpLoopBack_Type.__name__ = "Integer32"
_OduiClientCtpLoopBack_Object = MibTableColumn
oduiClientCtpLoopBack = _OduiClientCtpLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 40),
    _OduiClientCtpLoopBack_Type()
)
oduiClientCtpLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpLoopBack.setStatus("current")


class _OduiClientCtpFacSDThreshold_Type(Integer32):
    """Custom type oduiClientCtpFacSDThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduiClientCtpFacSDThreshold_Type.__name__ = "Integer32"
_OduiClientCtpFacSDThreshold_Object = MibTableColumn
oduiClientCtpFacSDThreshold = _OduiClientCtpFacSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 41),
    _OduiClientCtpFacSDThreshold_Type()
)
oduiClientCtpFacSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpFacSDThreshold.setStatus("current")
_OduiClientCtpRxDsF15MinutesTce_Type = Integer32
_OduiClientCtpRxDsF15MinutesTce_Object = MibTableColumn
oduiClientCtpRxDsF15MinutesTce = _OduiClientCtpRxDsF15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 42),
    _OduiClientCtpRxDsF15MinutesTce_Type()
)
oduiClientCtpRxDsF15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsF15MinutesTce.setStatus("current")
_OduiClientCtpRxDsF15MinutesTceReporting_Type = TruthValue
_OduiClientCtpRxDsF15MinutesTceReporting_Object = MibTableColumn
oduiClientCtpRxDsF15MinutesTceReporting = _OduiClientCtpRxDsF15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 43),
    _OduiClientCtpRxDsF15MinutesTceReporting_Type()
)
oduiClientCtpRxDsF15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsF15MinutesTceReporting.setStatus("current")
_OduiClientCtpRxDsFDayTce_Type = Integer32
_OduiClientCtpRxDsFDayTce_Object = MibTableColumn
oduiClientCtpRxDsFDayTce = _OduiClientCtpRxDsFDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 44),
    _OduiClientCtpRxDsFDayTce_Type()
)
oduiClientCtpRxDsFDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsFDayTce.setStatus("current")
_OduiClientCtpRxDsFDayTceReporting_Type = TruthValue
_OduiClientCtpRxDsFDayTceReporting_Object = MibTableColumn
oduiClientCtpRxDsFDayTceReporting = _OduiClientCtpRxDsFDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 45),
    _OduiClientCtpRxDsFDayTceReporting_Type()
)
oduiClientCtpRxDsFDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxDsFDayTceReporting.setStatus("current")
_OduiClientCtpRxBei15MinutesTce_Type = Integer32
_OduiClientCtpRxBei15MinutesTce_Object = MibTableColumn
oduiClientCtpRxBei15MinutesTce = _OduiClientCtpRxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 46),
    _OduiClientCtpRxBei15MinutesTce_Type()
)
oduiClientCtpRxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxBei15MinutesTce.setStatus("current")
_OduiClientCtpRxBei15MinutesTceReporting_Type = TruthValue
_OduiClientCtpRxBei15MinutesTceReporting_Object = MibTableColumn
oduiClientCtpRxBei15MinutesTceReporting = _OduiClientCtpRxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 47),
    _OduiClientCtpRxBei15MinutesTceReporting_Type()
)
oduiClientCtpRxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxBei15MinutesTceReporting.setStatus("current")
_OduiClientCtpRxBeiDayTce_Type = Integer32
_OduiClientCtpRxBeiDayTce_Object = MibTableColumn
oduiClientCtpRxBeiDayTce = _OduiClientCtpRxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 48),
    _OduiClientCtpRxBeiDayTce_Type()
)
oduiClientCtpRxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxBeiDayTce.setStatus("current")
_OduiClientCtpRxBeiDayTceReporting_Type = TruthValue
_OduiClientCtpRxBeiDayTceReporting_Object = MibTableColumn
oduiClientCtpRxBeiDayTceReporting = _OduiClientCtpRxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 49),
    _OduiClientCtpRxBeiDayTceReporting_Type()
)
oduiClientCtpRxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiClientCtpRxBeiDayTceReporting.setStatus("current")
_OduiClientCtpBitRateK_Type = InfnOtuBitRateK
_OduiClientCtpBitRateK_Object = MibTableColumn
oduiClientCtpBitRateK = _OduiClientCtpBitRateK_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 1, 1, 50),
    _OduiClientCtpBitRateK_Type()
)
oduiClientCtpBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiClientCtpBitRateK.setStatus("current")
_OduiClientCtpConformance_ObjectIdentity = ObjectIdentity
oduiClientCtpConformance = _OduiClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 3)
)
_OduiClientCtpCompliances_ObjectIdentity = ObjectIdentity
oduiClientCtpCompliances = _OduiClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 3, 1)
)
_OduiClientCtpGroups_ObjectIdentity = ObjectIdentity
oduiClientCtpGroups = _OduiClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 3, 2)
)

# Managed Objects groups

oduiClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 3, 2, 1)
)
oduiClientCtpGroup.setObjects(
      *(("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpServiceMode"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacMonitoringMode"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacTxTTI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacExpectedSAPI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacExpectedDAPI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermTxTTI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermExpectedSAPI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermExpectedDAPI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacReceivedTTI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermReceivedTTI"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDs15MinutesTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsDayTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsDayTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacTimDetMode"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermTimDetMode"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTcmList"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpConfiguredServiceType"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacPmHistStatsEnable"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermPmHistStatsEnable"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpAlarmReportControl"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacDSThreshold"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermDSThreshold"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTermMonitoringMode"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTSCount"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtprate"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTributaryPortNumber"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpExpectedTPNs"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpDetectedTPNs"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpsupportingOPUTributarySlots"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpavailableOPUTributarySlots"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpdatarate"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpCrossConnectType"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpSupportingTP"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpTsg"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpExpectedPayload"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpLoopBack"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpFacSDThreshold"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsF15MinutesTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsF15MinutesTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsFDayTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxDsFDayTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxBei15MinutesTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxBei15MinutesTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxBeiDayTce"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpRxBeiDayTceReporting"),
        ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpBitRateK"))
)
if mibBuilder.loadTexts:
    oduiClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduiClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 30, 3, 1, 1)
)
oduiClientCtpCompliance.setObjects(
    ("INFINERA-TP-ODUICLIENTCTP-MIB", "oduiClientCtpGroup")
)
if mibBuilder.loadTexts:
    oduiClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ODUICLIENTCTP-MIB",
    **{"oduiClientCtpMIB": oduiClientCtpMIB,
       "oduiClientCtpTable": oduiClientCtpTable,
       "oduiClientCtpEntry": oduiClientCtpEntry,
       "oduiClientCtpServiceMode": oduiClientCtpServiceMode,
       "oduiClientCtpServiceModeQualifier": oduiClientCtpServiceModeQualifier,
       "oduiClientCtpFacMonitoringMode": oduiClientCtpFacMonitoringMode,
       "oduiClientCtpFacTxTTI": oduiClientCtpFacTxTTI,
       "oduiClientCtpFacExpectedSAPI": oduiClientCtpFacExpectedSAPI,
       "oduiClientCtpFacExpectedDAPI": oduiClientCtpFacExpectedDAPI,
       "oduiClientCtpTermTxTTI": oduiClientCtpTermTxTTI,
       "oduiClientCtpTermExpectedSAPI": oduiClientCtpTermExpectedSAPI,
       "oduiClientCtpTermExpectedDAPI": oduiClientCtpTermExpectedDAPI,
       "oduiClientCtpFacReceivedTTI": oduiClientCtpFacReceivedTTI,
       "oduiClientCtpTermReceivedTTI": oduiClientCtpTermReceivedTTI,
       "oduiClientCtpRxDs15MinutesTce": oduiClientCtpRxDs15MinutesTce,
       "oduiClientCtpRxDsDayTce": oduiClientCtpRxDsDayTce,
       "oduiClientCtpRxDsDayTceReporting": oduiClientCtpRxDsDayTceReporting,
       "oduiClientCtpRxDs15MinutesTceReporting": oduiClientCtpRxDs15MinutesTceReporting,
       "oduiClientCtpFacTimDetMode": oduiClientCtpFacTimDetMode,
       "oduiClientCtpTermTimDetMode": oduiClientCtpTermTimDetMode,
       "oduiClientCtpTcmList": oduiClientCtpTcmList,
       "oduiClientCtpConfiguredServiceType": oduiClientCtpConfiguredServiceType,
       "oduiClientCtpFacPmHistStatsEnable": oduiClientCtpFacPmHistStatsEnable,
       "oduiClientCtpTermPmHistStatsEnable": oduiClientCtpTermPmHistStatsEnable,
       "oduiClientCtpAlarmReportControl": oduiClientCtpAlarmReportControl,
       "oduiClientCtpSupportingCircuitIdList": oduiClientCtpSupportingCircuitIdList,
       "oduiClientCtpFacDSThreshold": oduiClientCtpFacDSThreshold,
       "oduiClientCtpTermDSThreshold": oduiClientCtpTermDSThreshold,
       "oduiClientCtpTermMonitoringMode": oduiClientCtpTermMonitoringMode,
       "oduiClientCtpTSCount": oduiClientCtpTSCount,
       "oduiClientCtprate": oduiClientCtprate,
       "oduiClientCtpTributaryPortNumber": oduiClientCtpTributaryPortNumber,
       "oduiClientCtpExpectedTPNs": oduiClientCtpExpectedTPNs,
       "oduiClientCtpDetectedTPNs": oduiClientCtpDetectedTPNs,
       "oduiClientCtpsupportingOPUTributarySlots": oduiClientCtpsupportingOPUTributarySlots,
       "oduiClientCtpavailableOPUTributarySlots": oduiClientCtpavailableOPUTributarySlots,
       "oduiClientCtpdatarate": oduiClientCtpdatarate,
       "oduiClientCtpCrossConnectType": oduiClientCtpCrossConnectType,
       "oduiClientCtpSupportingTP": oduiClientCtpSupportingTP,
       "oduiClientCtpTsg": oduiClientCtpTsg,
       "oduiClientCtpExpectedPayload": oduiClientCtpExpectedPayload,
       "oduiClientCtpLoopBack": oduiClientCtpLoopBack,
       "oduiClientCtpFacSDThreshold": oduiClientCtpFacSDThreshold,
       "oduiClientCtpRxDsF15MinutesTce": oduiClientCtpRxDsF15MinutesTce,
       "oduiClientCtpRxDsF15MinutesTceReporting": oduiClientCtpRxDsF15MinutesTceReporting,
       "oduiClientCtpRxDsFDayTce": oduiClientCtpRxDsFDayTce,
       "oduiClientCtpRxDsFDayTceReporting": oduiClientCtpRxDsFDayTceReporting,
       "oduiClientCtpRxBei15MinutesTce": oduiClientCtpRxBei15MinutesTce,
       "oduiClientCtpRxBei15MinutesTceReporting": oduiClientCtpRxBei15MinutesTceReporting,
       "oduiClientCtpRxBeiDayTce": oduiClientCtpRxBeiDayTce,
       "oduiClientCtpRxBeiDayTceReporting": oduiClientCtpRxBeiDayTceReporting,
       "oduiClientCtpBitRateK": oduiClientCtpBitRateK,
       "oduiClientCtpConformance": oduiClientCtpConformance,
       "oduiClientCtpCompliances": oduiClientCtpCompliances,
       "oduiClientCtpCompliance": oduiClientCtpCompliance,
       "oduiClientCtpGroups": oduiClientCtpGroups,
       "oduiClientCtpGroup": oduiClientCtpGroup}
)
