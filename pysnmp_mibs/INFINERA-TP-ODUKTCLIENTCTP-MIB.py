# SNMP MIB module (INFINERA-TP-ODUKTCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ODUKTCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:32 2025
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
 InfnMonitoringMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnArc",
    "InfnEnableDisable",
    "InfnMonitoringMode",
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

oduktClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24)
)
if mibBuilder.loadTexts:
    oduktClientCtpMIB.setRevisions(
        ("2009-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduktClientCtpTable_Object = MibTable
oduktClientCtpTable = _OduktClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1)
)
if mibBuilder.loadTexts:
    oduktClientCtpTable.setStatus("current")
_OduktClientCtpEntry_Object = MibTableRow
oduktClientCtpEntry = _OduktClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1)
)
oduktClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpTcmIdentifier"),
)
if mibBuilder.loadTexts:
    oduktClientCtpEntry.setStatus("current")


class _OduktClientCtpTcmIdentifier_Type(Integer32):
    """Custom type oduktClientCtpTcmIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OduktClientCtpTcmIdentifier_Type.__name__ = "Integer32"
_OduktClientCtpTcmIdentifier_Object = MibTableColumn
oduktClientCtpTcmIdentifier = _OduktClientCtpTcmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 1),
    _OduktClientCtpTcmIdentifier_Type()
)
oduktClientCtpTcmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduktClientCtpTcmIdentifier.setStatus("current")


class _OduktClientCtpSide_Type(Integer32):
    """Custom type oduktClientCtpSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fac", 1),
          ("term", 2))
    )


_OduktClientCtpSide_Type.__name__ = "Integer32"
_OduktClientCtpSide_Object = MibTableColumn
oduktClientCtpSide = _OduktClientCtpSide_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 2),
    _OduktClientCtpSide_Type()
)
oduktClientCtpSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduktClientCtpSide.setStatus("current")
_OduktClientCtpConfiguredServiceType_Type = InfnServiceType
_OduktClientCtpConfiguredServiceType_Object = MibTableColumn
oduktClientCtpConfiguredServiceType = _OduktClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 3),
    _OduktClientCtpConfiguredServiceType_Type()
)
oduktClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduktClientCtpConfiguredServiceType.setStatus("current")


class _OduktClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type oduktClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OduktClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OduktClientCtpAlarmReportControl_Object = MibTableColumn
oduktClientCtpAlarmReportControl = _OduktClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 4),
    _OduktClientCtpAlarmReportControl_Type()
)
oduktClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpAlarmReportControl.setStatus("current")
_OduktClientCtpSupportingCircuitIdList_Type = DisplayString
_OduktClientCtpSupportingCircuitIdList_Object = MibTableColumn
oduktClientCtpSupportingCircuitIdList = _OduktClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 5),
    _OduktClientCtpSupportingCircuitIdList_Type()
)
oduktClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduktClientCtpSupportingCircuitIdList.setStatus("current")
_OduktClientCtpMonitoringMode_Type = InfnMonitoringMode
_OduktClientCtpMonitoringMode_Object = MibTableColumn
oduktClientCtpMonitoringMode = _OduktClientCtpMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 6),
    _OduktClientCtpMonitoringMode_Type()
)
oduktClientCtpMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpMonitoringMode.setStatus("current")


class _OduktClientCtpDSThreshold_Type(Integer32):
    """Custom type oduktClientCtpDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduktClientCtpDSThreshold_Type.__name__ = "Integer32"
_OduktClientCtpDSThreshold_Object = MibTableColumn
oduktClientCtpDSThreshold = _OduktClientCtpDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 7),
    _OduktClientCtpDSThreshold_Type()
)
oduktClientCtpDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpDSThreshold.setStatus("current")


class _OduktClientCtpTxTTI_Type(DisplayString):
    """Custom type oduktClientCtpTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduktClientCtpTxTTI_Type.__name__ = "DisplayString"
_OduktClientCtpTxTTI_Object = MibTableColumn
oduktClientCtpTxTTI = _OduktClientCtpTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 8),
    _OduktClientCtpTxTTI_Type()
)
oduktClientCtpTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpTxTTI.setStatus("current")


class _OduktClientCtpExpectedSAPI_Type(DisplayString):
    """Custom type oduktClientCtpExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduktClientCtpExpectedSAPI_Type.__name__ = "DisplayString"
_OduktClientCtpExpectedSAPI_Object = MibTableColumn
oduktClientCtpExpectedSAPI = _OduktClientCtpExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 9),
    _OduktClientCtpExpectedSAPI_Type()
)
oduktClientCtpExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpExpectedSAPI.setStatus("current")


class _OduktClientCtpExpectedDAPI_Type(DisplayString):
    """Custom type oduktClientCtpExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduktClientCtpExpectedDAPI_Type.__name__ = "DisplayString"
_OduktClientCtpExpectedDAPI_Object = MibTableColumn
oduktClientCtpExpectedDAPI = _OduktClientCtpExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 10),
    _OduktClientCtpExpectedDAPI_Type()
)
oduktClientCtpExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpExpectedDAPI.setStatus("current")


class _OduktClientCtpTimDetMode_Type(Integer32):
    """Custom type oduktClientCtpTimDetMode based on Integer32"""
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


_OduktClientCtpTimDetMode_Type.__name__ = "Integer32"
_OduktClientCtpTimDetMode_Object = MibTableColumn
oduktClientCtpTimDetMode = _OduktClientCtpTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 11),
    _OduktClientCtpTimDetMode_Type()
)
oduktClientCtpTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpTimDetMode.setStatus("current")


class _OduktClientCtpReceivedTTI_Type(DisplayString):
    """Custom type oduktClientCtpReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduktClientCtpReceivedTTI_Type.__name__ = "DisplayString"
_OduktClientCtpReceivedTTI_Object = MibTableColumn
oduktClientCtpReceivedTTI = _OduktClientCtpReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 12),
    _OduktClientCtpReceivedTTI_Type()
)
oduktClientCtpReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduktClientCtpReceivedTTI.setStatus("current")


class _OduktClientCtpPmHistStatsEnable_Type(Integer32):
    """Custom type oduktClientCtpPmHistStatsEnable based on Integer32"""
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


_OduktClientCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OduktClientCtpPmHistStatsEnable_Object = MibTableColumn
oduktClientCtpPmHistStatsEnable = _OduktClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 13),
    _OduktClientCtpPmHistStatsEnable_Type()
)
oduktClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpPmHistStatsEnable.setStatus("current")


class _OduktClientCtpRxEb15MinutesTce_Type(Integer32):
    """Custom type oduktClientCtpRxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduktClientCtpRxEb15MinutesTce_Type.__name__ = "Integer32"
_OduktClientCtpRxEb15MinutesTce_Object = MibTableColumn
oduktClientCtpRxEb15MinutesTce = _OduktClientCtpRxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 14),
    _OduktClientCtpRxEb15MinutesTce_Type()
)
oduktClientCtpRxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxEb15MinutesTce.setStatus("current")


class _OduktClientCtpRxEbDayTce_Type(Integer32):
    """Custom type oduktClientCtpRxEbDayTce based on Integer32"""
    defaultValue = 15000


_OduktClientCtpRxEbDayTce_Type.__name__ = "Integer32"
_OduktClientCtpRxEbDayTce_Object = MibTableColumn
oduktClientCtpRxEbDayTce = _OduktClientCtpRxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 15),
    _OduktClientCtpRxEbDayTce_Type()
)
oduktClientCtpRxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxEbDayTce.setStatus("current")


class _OduktClientCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type oduktClientCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OduktClientCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OduktClientCtpRxDs15MinutesTce_Object = MibTableColumn
oduktClientCtpRxDs15MinutesTce = _OduktClientCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 16),
    _OduktClientCtpRxDs15MinutesTce_Type()
)
oduktClientCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxDs15MinutesTce.setStatus("current")


class _OduktClientCtpRxDsDayTce_Type(Integer32):
    """Custom type oduktClientCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OduktClientCtpRxDsDayTce_Type.__name__ = "Integer32"
_OduktClientCtpRxDsDayTce_Object = MibTableColumn
oduktClientCtpRxDsDayTce = _OduktClientCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 17),
    _OduktClientCtpRxDsDayTce_Type()
)
oduktClientCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxDsDayTce.setStatus("current")


class _OduktClientCtpRxEbDayTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxEbDayTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxEbDayTceReporting_Object = MibTableColumn
oduktClientCtpRxEbDayTceReporting = _OduktClientCtpRxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 18),
    _OduktClientCtpRxEbDayTceReporting_Type()
)
oduktClientCtpRxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxEbDayTceReporting.setStatus("current")


class _OduktClientCtpRxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxEb15MinutesTceReporting_Object = MibTableColumn
oduktClientCtpRxEb15MinutesTceReporting = _OduktClientCtpRxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 19),
    _OduktClientCtpRxEb15MinutesTceReporting_Type()
)
oduktClientCtpRxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxEb15MinutesTceReporting.setStatus("current")


class _OduktClientCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxDsDayTceReporting_Object = MibTableColumn
oduktClientCtpRxDsDayTceReporting = _OduktClientCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 20),
    _OduktClientCtpRxDsDayTceReporting_Type()
)
oduktClientCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxDsDayTceReporting.setStatus("current")


class _OduktClientCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxDs15MinutesTceReporting_Object = MibTableColumn
oduktClientCtpRxDs15MinutesTceReporting = _OduktClientCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 21),
    _OduktClientCtpRxDs15MinutesTceReporting_Type()
)
oduktClientCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxDs15MinutesTceReporting.setStatus("current")


class _OduktClientCtpSDThreshold_Type(Integer32):
    """Custom type oduktClientCtpSDThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduktClientCtpSDThreshold_Type.__name__ = "Integer32"
_OduktClientCtpSDThreshold_Object = MibTableColumn
oduktClientCtpSDThreshold = _OduktClientCtpSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 22),
    _OduktClientCtpSDThreshold_Type()
)
oduktClientCtpSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpSDThreshold.setStatus("current")
_OduktClientCtpRxBei15MinutesTce_Type = Counter64
_OduktClientCtpRxBei15MinutesTce_Object = MibTableColumn
oduktClientCtpRxBei15MinutesTce = _OduktClientCtpRxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 23),
    _OduktClientCtpRxBei15MinutesTce_Type()
)
oduktClientCtpRxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxBei15MinutesTce.setStatus("current")
_OduktClientCtpRxBeiDayTce_Type = Counter64
_OduktClientCtpRxBeiDayTce_Object = MibTableColumn
oduktClientCtpRxBeiDayTce = _OduktClientCtpRxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 24),
    _OduktClientCtpRxBeiDayTce_Type()
)
oduktClientCtpRxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxBeiDayTce.setStatus("current")


class _OduktClientCtpRxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxBei15MinutesTceReporting_Object = MibTableColumn
oduktClientCtpRxBei15MinutesTceReporting = _OduktClientCtpRxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 25),
    _OduktClientCtpRxBei15MinutesTceReporting_Type()
)
oduktClientCtpRxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxBei15MinutesTceReporting.setStatus("current")


class _OduktClientCtpRxBeiDayTceReporting_Type(TruthValue):
    """Custom type oduktClientCtpRxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduktClientCtpRxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OduktClientCtpRxBeiDayTceReporting_Object = MibTableColumn
oduktClientCtpRxBeiDayTceReporting = _OduktClientCtpRxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 1, 1, 26),
    _OduktClientCtpRxBeiDayTceReporting_Type()
)
oduktClientCtpRxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduktClientCtpRxBeiDayTceReporting.setStatus("current")
_OduktClientCtpConformance_ObjectIdentity = ObjectIdentity
oduktClientCtpConformance = _OduktClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 3)
)
_OduktClientCtpCompliances_ObjectIdentity = ObjectIdentity
oduktClientCtpCompliances = _OduktClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 3, 1)
)
_OduktClientCtpGroups_ObjectIdentity = ObjectIdentity
oduktClientCtpGroups = _OduktClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 3, 2)
)

# Managed Objects groups

oduktClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 3, 2, 1)
)
oduktClientCtpGroup.setObjects(
      *(("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpTcmIdentifier"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpSide"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpConfiguredServiceType"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpAlarmReportControl"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpMonitoringMode"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpDSThreshold"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpTxTTI"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpExpectedSAPI"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpExpectedDAPI"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpTimDetMode"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpReceivedTTI"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxEb15MinutesTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxEbDayTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxDs15MinutesTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxDsDayTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxEbDayTceReporting"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxEb15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxDsDayTceReporting"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpSDThreshold"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxBei15MinutesTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxBeiDayTce"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxBei15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpRxBeiDayTceReporting"))
)
if mibBuilder.loadTexts:
    oduktClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduktClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 24, 3, 1, 1)
)
oduktClientCtpCompliance.setObjects(
    ("INFINERA-TP-ODUKTCLIENTCTP-MIB", "oduktClientCtpGroup")
)
if mibBuilder.loadTexts:
    oduktClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ODUKTCLIENTCTP-MIB",
    **{"oduktClientCtpMIB": oduktClientCtpMIB,
       "oduktClientCtpTable": oduktClientCtpTable,
       "oduktClientCtpEntry": oduktClientCtpEntry,
       "oduktClientCtpTcmIdentifier": oduktClientCtpTcmIdentifier,
       "oduktClientCtpSide": oduktClientCtpSide,
       "oduktClientCtpConfiguredServiceType": oduktClientCtpConfiguredServiceType,
       "oduktClientCtpAlarmReportControl": oduktClientCtpAlarmReportControl,
       "oduktClientCtpSupportingCircuitIdList": oduktClientCtpSupportingCircuitIdList,
       "oduktClientCtpMonitoringMode": oduktClientCtpMonitoringMode,
       "oduktClientCtpDSThreshold": oduktClientCtpDSThreshold,
       "oduktClientCtpTxTTI": oduktClientCtpTxTTI,
       "oduktClientCtpExpectedSAPI": oduktClientCtpExpectedSAPI,
       "oduktClientCtpExpectedDAPI": oduktClientCtpExpectedDAPI,
       "oduktClientCtpTimDetMode": oduktClientCtpTimDetMode,
       "oduktClientCtpReceivedTTI": oduktClientCtpReceivedTTI,
       "oduktClientCtpPmHistStatsEnable": oduktClientCtpPmHistStatsEnable,
       "oduktClientCtpRxEb15MinutesTce": oduktClientCtpRxEb15MinutesTce,
       "oduktClientCtpRxEbDayTce": oduktClientCtpRxEbDayTce,
       "oduktClientCtpRxDs15MinutesTce": oduktClientCtpRxDs15MinutesTce,
       "oduktClientCtpRxDsDayTce": oduktClientCtpRxDsDayTce,
       "oduktClientCtpRxEbDayTceReporting": oduktClientCtpRxEbDayTceReporting,
       "oduktClientCtpRxEb15MinutesTceReporting": oduktClientCtpRxEb15MinutesTceReporting,
       "oduktClientCtpRxDsDayTceReporting": oduktClientCtpRxDsDayTceReporting,
       "oduktClientCtpRxDs15MinutesTceReporting": oduktClientCtpRxDs15MinutesTceReporting,
       "oduktClientCtpSDThreshold": oduktClientCtpSDThreshold,
       "oduktClientCtpRxBei15MinutesTce": oduktClientCtpRxBei15MinutesTce,
       "oduktClientCtpRxBeiDayTce": oduktClientCtpRxBeiDayTce,
       "oduktClientCtpRxBei15MinutesTceReporting": oduktClientCtpRxBei15MinutesTceReporting,
       "oduktClientCtpRxBeiDayTceReporting": oduktClientCtpRxBeiDayTceReporting,
       "oduktClientCtpConformance": oduktClientCtpConformance,
       "oduktClientCtpCompliances": oduktClientCtpCompliances,
       "oduktClientCtpCompliance": oduktClientCtpCompliance,
       "oduktClientCtpGroups": oduktClientCtpGroups,
       "oduktClientCtpGroup": oduktClientCtpGroup}
)
