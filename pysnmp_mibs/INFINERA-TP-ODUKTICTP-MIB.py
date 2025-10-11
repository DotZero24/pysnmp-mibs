# SNMP MIB module (INFINERA-TP-ODUKTICTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ODUKTICTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:15 2025
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

oduiktClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35)
)
if mibBuilder.loadTexts:
    oduiktClientCtpMIB.setRevisions(
        ("2011-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduiktClientCtpTable_Object = MibTable
oduiktClientCtpTable = _OduiktClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1)
)
if mibBuilder.loadTexts:
    oduiktClientCtpTable.setStatus("current")
_OduiktClientCtpEntry_Object = MibTableRow
oduiktClientCtpEntry = _OduiktClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1)
)
oduiktClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpTcmIdentifier"),
)
if mibBuilder.loadTexts:
    oduiktClientCtpEntry.setStatus("current")


class _OduiktClientCtpTcmIdentifier_Type(Integer32):
    """Custom type oduiktClientCtpTcmIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OduiktClientCtpTcmIdentifier_Type.__name__ = "Integer32"
_OduiktClientCtpTcmIdentifier_Object = MibTableColumn
oduiktClientCtpTcmIdentifier = _OduiktClientCtpTcmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 1),
    _OduiktClientCtpTcmIdentifier_Type()
)
oduiktClientCtpTcmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiktClientCtpTcmIdentifier.setStatus("current")


class _OduiktClientCtpSide_Type(Integer32):
    """Custom type oduiktClientCtpSide based on Integer32"""
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


_OduiktClientCtpSide_Type.__name__ = "Integer32"
_OduiktClientCtpSide_Object = MibTableColumn
oduiktClientCtpSide = _OduiktClientCtpSide_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 2),
    _OduiktClientCtpSide_Type()
)
oduiktClientCtpSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiktClientCtpSide.setStatus("current")
_OduiktClientCtpConfiguredServiceType_Type = InfnServiceType
_OduiktClientCtpConfiguredServiceType_Object = MibTableColumn
oduiktClientCtpConfiguredServiceType = _OduiktClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 3),
    _OduiktClientCtpConfiguredServiceType_Type()
)
oduiktClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiktClientCtpConfiguredServiceType.setStatus("current")


class _OduiktClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type oduiktClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OduiktClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OduiktClientCtpAlarmReportControl_Object = MibTableColumn
oduiktClientCtpAlarmReportControl = _OduiktClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 4),
    _OduiktClientCtpAlarmReportControl_Type()
)
oduiktClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpAlarmReportControl.setStatus("current")
_OduiktClientCtpSupportingCircuitIdList_Type = DisplayString
_OduiktClientCtpSupportingCircuitIdList_Object = MibTableColumn
oduiktClientCtpSupportingCircuitIdList = _OduiktClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 5),
    _OduiktClientCtpSupportingCircuitIdList_Type()
)
oduiktClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiktClientCtpSupportingCircuitIdList.setStatus("current")
_OduiktClientCtpMonitoringMode_Type = InfnMonitoringMode
_OduiktClientCtpMonitoringMode_Object = MibTableColumn
oduiktClientCtpMonitoringMode = _OduiktClientCtpMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 6),
    _OduiktClientCtpMonitoringMode_Type()
)
oduiktClientCtpMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpMonitoringMode.setStatus("current")


class _OduiktClientCtpDSThreshold_Type(Integer32):
    """Custom type oduiktClientCtpDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduiktClientCtpDSThreshold_Type.__name__ = "Integer32"
_OduiktClientCtpDSThreshold_Object = MibTableColumn
oduiktClientCtpDSThreshold = _OduiktClientCtpDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 7),
    _OduiktClientCtpDSThreshold_Type()
)
oduiktClientCtpDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpDSThreshold.setStatus("current")


class _OduiktClientCtpTxTTI_Type(DisplayString):
    """Custom type oduiktClientCtpTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiktClientCtpTxTTI_Type.__name__ = "DisplayString"
_OduiktClientCtpTxTTI_Object = MibTableColumn
oduiktClientCtpTxTTI = _OduiktClientCtpTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 8),
    _OduiktClientCtpTxTTI_Type()
)
oduiktClientCtpTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpTxTTI.setStatus("current")


class _OduiktClientCtpExpectedSAPI_Type(DisplayString):
    """Custom type oduiktClientCtpExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiktClientCtpExpectedSAPI_Type.__name__ = "DisplayString"
_OduiktClientCtpExpectedSAPI_Object = MibTableColumn
oduiktClientCtpExpectedSAPI = _OduiktClientCtpExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 9),
    _OduiktClientCtpExpectedSAPI_Type()
)
oduiktClientCtpExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpExpectedSAPI.setStatus("current")


class _OduiktClientCtpExpectedDAPI_Type(DisplayString):
    """Custom type oduiktClientCtpExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduiktClientCtpExpectedDAPI_Type.__name__ = "DisplayString"
_OduiktClientCtpExpectedDAPI_Object = MibTableColumn
oduiktClientCtpExpectedDAPI = _OduiktClientCtpExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 10),
    _OduiktClientCtpExpectedDAPI_Type()
)
oduiktClientCtpExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpExpectedDAPI.setStatus("current")


class _OduiktClientCtpTimDetMode_Type(Integer32):
    """Custom type oduiktClientCtpTimDetMode based on Integer32"""
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


_OduiktClientCtpTimDetMode_Type.__name__ = "Integer32"
_OduiktClientCtpTimDetMode_Object = MibTableColumn
oduiktClientCtpTimDetMode = _OduiktClientCtpTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 11),
    _OduiktClientCtpTimDetMode_Type()
)
oduiktClientCtpTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpTimDetMode.setStatus("current")


class _OduiktClientCtpReceivedTTI_Type(DisplayString):
    """Custom type oduiktClientCtpReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduiktClientCtpReceivedTTI_Type.__name__ = "DisplayString"
_OduiktClientCtpReceivedTTI_Object = MibTableColumn
oduiktClientCtpReceivedTTI = _OduiktClientCtpReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 12),
    _OduiktClientCtpReceivedTTI_Type()
)
oduiktClientCtpReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiktClientCtpReceivedTTI.setStatus("current")


class _OduiktClientCtpPmHistStatsEnable_Type(Integer32):
    """Custom type oduiktClientCtpPmHistStatsEnable based on Integer32"""
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


_OduiktClientCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OduiktClientCtpPmHistStatsEnable_Object = MibTableColumn
oduiktClientCtpPmHistStatsEnable = _OduiktClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 13),
    _OduiktClientCtpPmHistStatsEnable_Type()
)
oduiktClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpPmHistStatsEnable.setStatus("current")


class _OduiktClientCtpRxEb15MinutesTce_Type(Integer32):
    """Custom type oduiktClientCtpRxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduiktClientCtpRxEb15MinutesTce_Type.__name__ = "Integer32"
_OduiktClientCtpRxEb15MinutesTce_Object = MibTableColumn
oduiktClientCtpRxEb15MinutesTce = _OduiktClientCtpRxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 14),
    _OduiktClientCtpRxEb15MinutesTce_Type()
)
oduiktClientCtpRxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxEb15MinutesTce.setStatus("current")


class _OduiktClientCtpRxEbDayTce_Type(Integer32):
    """Custom type oduiktClientCtpRxEbDayTce based on Integer32"""
    defaultValue = 15000


_OduiktClientCtpRxEbDayTce_Type.__name__ = "Integer32"
_OduiktClientCtpRxEbDayTce_Object = MibTableColumn
oduiktClientCtpRxEbDayTce = _OduiktClientCtpRxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 15),
    _OduiktClientCtpRxEbDayTce_Type()
)
oduiktClientCtpRxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxEbDayTce.setStatus("current")


class _OduiktClientCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type oduiktClientCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OduiktClientCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OduiktClientCtpRxDs15MinutesTce_Object = MibTableColumn
oduiktClientCtpRxDs15MinutesTce = _OduiktClientCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 16),
    _OduiktClientCtpRxDs15MinutesTce_Type()
)
oduiktClientCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxDs15MinutesTce.setStatus("current")


class _OduiktClientCtpRxDsDayTce_Type(Integer32):
    """Custom type oduiktClientCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OduiktClientCtpRxDsDayTce_Type.__name__ = "Integer32"
_OduiktClientCtpRxDsDayTce_Object = MibTableColumn
oduiktClientCtpRxDsDayTce = _OduiktClientCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 17),
    _OduiktClientCtpRxDsDayTce_Type()
)
oduiktClientCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxDsDayTce.setStatus("current")


class _OduiktClientCtpRxEbDayTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxEbDayTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxEbDayTceReporting_Object = MibTableColumn
oduiktClientCtpRxEbDayTceReporting = _OduiktClientCtpRxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 18),
    _OduiktClientCtpRxEbDayTceReporting_Type()
)
oduiktClientCtpRxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxEbDayTceReporting.setStatus("current")


class _OduiktClientCtpRxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxEb15MinutesTceReporting_Object = MibTableColumn
oduiktClientCtpRxEb15MinutesTceReporting = _OduiktClientCtpRxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 19),
    _OduiktClientCtpRxEb15MinutesTceReporting_Type()
)
oduiktClientCtpRxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxEb15MinutesTceReporting.setStatus("current")


class _OduiktClientCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxDsDayTceReporting_Object = MibTableColumn
oduiktClientCtpRxDsDayTceReporting = _OduiktClientCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 20),
    _OduiktClientCtpRxDsDayTceReporting_Type()
)
oduiktClientCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxDsDayTceReporting.setStatus("current")


class _OduiktClientCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxDs15MinutesTceReporting_Object = MibTableColumn
oduiktClientCtpRxDs15MinutesTceReporting = _OduiktClientCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 21),
    _OduiktClientCtpRxDs15MinutesTceReporting_Type()
)
oduiktClientCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxDs15MinutesTceReporting.setStatus("current")


class _OduiktClientCtpSDThreshold_Type(Integer32):
    """Custom type oduiktClientCtpSDThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduiktClientCtpSDThreshold_Type.__name__ = "Integer32"
_OduiktClientCtpSDThreshold_Object = MibTableColumn
oduiktClientCtpSDThreshold = _OduiktClientCtpSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 22),
    _OduiktClientCtpSDThreshold_Type()
)
oduiktClientCtpSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpSDThreshold.setStatus("current")
_OduiktClientCtpRxBei15MinutesTce_Type = Counter64
_OduiktClientCtpRxBei15MinutesTce_Object = MibTableColumn
oduiktClientCtpRxBei15MinutesTce = _OduiktClientCtpRxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 23),
    _OduiktClientCtpRxBei15MinutesTce_Type()
)
oduiktClientCtpRxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxBei15MinutesTce.setStatus("current")
_OduiktClientCtpRxBeiDayTce_Type = Counter64
_OduiktClientCtpRxBeiDayTce_Object = MibTableColumn
oduiktClientCtpRxBeiDayTce = _OduiktClientCtpRxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 24),
    _OduiktClientCtpRxBeiDayTce_Type()
)
oduiktClientCtpRxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxBeiDayTce.setStatus("current")


class _OduiktClientCtpRxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxBei15MinutesTceReporting_Object = MibTableColumn
oduiktClientCtpRxBei15MinutesTceReporting = _OduiktClientCtpRxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 25),
    _OduiktClientCtpRxBei15MinutesTceReporting_Type()
)
oduiktClientCtpRxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxBei15MinutesTceReporting.setStatus("current")


class _OduiktClientCtpRxBeiDayTceReporting_Type(TruthValue):
    """Custom type oduiktClientCtpRxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduiktClientCtpRxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OduiktClientCtpRxBeiDayTceReporting_Object = MibTableColumn
oduiktClientCtpRxBeiDayTceReporting = _OduiktClientCtpRxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 1, 1, 26),
    _OduiktClientCtpRxBeiDayTceReporting_Type()
)
oduiktClientCtpRxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduiktClientCtpRxBeiDayTceReporting.setStatus("current")
_OduiktClientCtpConformance_ObjectIdentity = ObjectIdentity
oduiktClientCtpConformance = _OduiktClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 3)
)
_OduiktClientCtpCompliances_ObjectIdentity = ObjectIdentity
oduiktClientCtpCompliances = _OduiktClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 3, 1)
)
_OduiktClientCtpGroups_ObjectIdentity = ObjectIdentity
oduiktClientCtpGroups = _OduiktClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 3, 2)
)

# Managed Objects groups

oduiktClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 3, 2, 1)
)
oduiktClientCtpGroup.setObjects(
      *(("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpTcmIdentifier"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpSide"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpConfiguredServiceType"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpAlarmReportControl"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpMonitoringMode"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpDSThreshold"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpTxTTI"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpExpectedSAPI"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpExpectedDAPI"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpTimDetMode"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpReceivedTTI"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxEb15MinutesTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxEbDayTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxDs15MinutesTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxDsDayTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxEbDayTceReporting"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxEb15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxDsDayTceReporting"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpSDThreshold"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxBei15MinutesTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxBeiDayTce"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxBei15MinutesTceReporting"),
        ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpRxBeiDayTceReporting"))
)
if mibBuilder.loadTexts:
    oduiktClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduiktClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 35, 3, 1, 1)
)
oduiktClientCtpCompliance.setObjects(
    ("INFINERA-TP-ODUKTICTP-MIB", "oduiktClientCtpGroup")
)
if mibBuilder.loadTexts:
    oduiktClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ODUKTICTP-MIB",
    **{"oduiktClientCtpMIB": oduiktClientCtpMIB,
       "oduiktClientCtpTable": oduiktClientCtpTable,
       "oduiktClientCtpEntry": oduiktClientCtpEntry,
       "oduiktClientCtpTcmIdentifier": oduiktClientCtpTcmIdentifier,
       "oduiktClientCtpSide": oduiktClientCtpSide,
       "oduiktClientCtpConfiguredServiceType": oduiktClientCtpConfiguredServiceType,
       "oduiktClientCtpAlarmReportControl": oduiktClientCtpAlarmReportControl,
       "oduiktClientCtpSupportingCircuitIdList": oduiktClientCtpSupportingCircuitIdList,
       "oduiktClientCtpMonitoringMode": oduiktClientCtpMonitoringMode,
       "oduiktClientCtpDSThreshold": oduiktClientCtpDSThreshold,
       "oduiktClientCtpTxTTI": oduiktClientCtpTxTTI,
       "oduiktClientCtpExpectedSAPI": oduiktClientCtpExpectedSAPI,
       "oduiktClientCtpExpectedDAPI": oduiktClientCtpExpectedDAPI,
       "oduiktClientCtpTimDetMode": oduiktClientCtpTimDetMode,
       "oduiktClientCtpReceivedTTI": oduiktClientCtpReceivedTTI,
       "oduiktClientCtpPmHistStatsEnable": oduiktClientCtpPmHistStatsEnable,
       "oduiktClientCtpRxEb15MinutesTce": oduiktClientCtpRxEb15MinutesTce,
       "oduiktClientCtpRxEbDayTce": oduiktClientCtpRxEbDayTce,
       "oduiktClientCtpRxDs15MinutesTce": oduiktClientCtpRxDs15MinutesTce,
       "oduiktClientCtpRxDsDayTce": oduiktClientCtpRxDsDayTce,
       "oduiktClientCtpRxEbDayTceReporting": oduiktClientCtpRxEbDayTceReporting,
       "oduiktClientCtpRxEb15MinutesTceReporting": oduiktClientCtpRxEb15MinutesTceReporting,
       "oduiktClientCtpRxDsDayTceReporting": oduiktClientCtpRxDsDayTceReporting,
       "oduiktClientCtpRxDs15MinutesTceReporting": oduiktClientCtpRxDs15MinutesTceReporting,
       "oduiktClientCtpSDThreshold": oduiktClientCtpSDThreshold,
       "oduiktClientCtpRxBei15MinutesTce": oduiktClientCtpRxBei15MinutesTce,
       "oduiktClientCtpRxBeiDayTce": oduiktClientCtpRxBeiDayTce,
       "oduiktClientCtpRxBei15MinutesTceReporting": oduiktClientCtpRxBei15MinutesTceReporting,
       "oduiktClientCtpRxBeiDayTceReporting": oduiktClientCtpRxBeiDayTceReporting,
       "oduiktClientCtpConformance": oduiktClientCtpConformance,
       "oduiktClientCtpCompliances": oduiktClientCtpCompliances,
       "oduiktClientCtpCompliance": oduiktClientCtpCompliance,
       "oduiktClientCtpGroups": oduiktClientCtpGroups,
       "oduiktClientCtpGroup": oduiktClientCtpGroup}
)
