# SNMP MIB module (ZTE-AN-PERF-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PERF-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:55 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnPerfMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPerfMgmtObjects_ObjectIdentity = ObjectIdentity
zxAnPerfMgmtObjects = _ZxAnPerfMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1)
)
_ZxAnPmCtrlTable_Object = MibTable
zxAnPmCtrlTable = _ZxAnPmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnPmCtrlTable.setStatus("current")
_ZxAnPmCtrlEntry_Object = MibTableRow
zxAnPmCtrlEntry = _ZxAnPmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1)
)
zxAnPmCtrlEntry.setIndexNames(
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlIndex"),
)
if mibBuilder.loadTexts:
    zxAnPmCtrlEntry.setStatus("current")
_ZxAnPmCtrlIndex_Type = Integer32
_ZxAnPmCtrlIndex_Object = MibTableColumn
zxAnPmCtrlIndex = _ZxAnPmCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 1),
    _ZxAnPmCtrlIndex_Type()
)
zxAnPmCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmCtrlIndex.setStatus("current")
_ZxAnPmCtrlDesc_Type = DisplayString
_ZxAnPmCtrlDesc_Object = MibTableColumn
zxAnPmCtrlDesc = _ZxAnPmCtrlDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 2),
    _ZxAnPmCtrlDesc_Type()
)
zxAnPmCtrlDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlDesc.setStatus("current")
_ZxAnPmCtrlMetric_Type = ObjectIdentifier
_ZxAnPmCtrlMetric_Object = MibTableColumn
zxAnPmCtrlMetric = _ZxAnPmCtrlMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 3),
    _ZxAnPmCtrlMetric_Type()
)
zxAnPmCtrlMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlMetric.setStatus("current")
_ZxAnPmCtrlMetricInstIndex_Type = ObjectIdentifier
_ZxAnPmCtrlMetricInstIndex_Object = MibTableColumn
zxAnPmCtrlMetricInstIndex = _ZxAnPmCtrlMetricInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 4),
    _ZxAnPmCtrlMetricInstIndex_Type()
)
zxAnPmCtrlMetricInstIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlMetricInstIndex.setStatus("current")


class _ZxAnPmCtrlAdminStatus_Type(Integer32):
    """Custom type zxAnPmCtrlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("resetCounter", 3))
    )


_ZxAnPmCtrlAdminStatus_Type.__name__ = "Integer32"
_ZxAnPmCtrlAdminStatus_Object = MibTableColumn
zxAnPmCtrlAdminStatus = _ZxAnPmCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 5),
    _ZxAnPmCtrlAdminStatus_Type()
)
zxAnPmCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlAdminStatus.setStatus("current")


class _ZxAnPmCtrlBucketsRequested_Type(Integer32):
    """Custom type zxAnPmCtrlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnPmCtrlBucketsRequested_Type.__name__ = "Integer32"
_ZxAnPmCtrlBucketsRequested_Object = MibTableColumn
zxAnPmCtrlBucketsRequested = _ZxAnPmCtrlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 6),
    _ZxAnPmCtrlBucketsRequested_Type()
)
zxAnPmCtrlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlBucketsRequested.setStatus("current")


class _ZxAnPmCtrlBucketsGranted_Type(Integer32):
    """Custom type zxAnPmCtrlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnPmCtrlBucketsGranted_Type.__name__ = "Integer32"
_ZxAnPmCtrlBucketsGranted_Object = MibTableColumn
zxAnPmCtrlBucketsGranted = _ZxAnPmCtrlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 7),
    _ZxAnPmCtrlBucketsGranted_Type()
)
zxAnPmCtrlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPmCtrlBucketsGranted.setStatus("current")


class _ZxAnPmCtrlSamplingInterval_Type(Integer32):
    """Custom type zxAnPmCtrlSamplingInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ZxAnPmCtrlSamplingInterval_Type.__name__ = "Integer32"
_ZxAnPmCtrlSamplingInterval_Object = MibTableColumn
zxAnPmCtrlSamplingInterval = _ZxAnPmCtrlSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 8),
    _ZxAnPmCtrlSamplingInterval_Type()
)
zxAnPmCtrlSamplingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPmCtrlSamplingInterval.setUnits("Seconds")
_ZxAnPmCtrlRowStatus_Type = RowStatus
_ZxAnPmCtrlRowStatus_Object = MibTableColumn
zxAnPmCtrlRowStatus = _ZxAnPmCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 9),
    _ZxAnPmCtrlRowStatus_Type()
)
zxAnPmCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlRowStatus.setStatus("current")


class _ZxAnPmCtrlSamplingType_Type(Integer32):
    """Custom type zxAnPmCtrlSamplingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_ZxAnPmCtrlSamplingType_Type.__name__ = "Integer32"
_ZxAnPmCtrlSamplingType_Object = MibTableColumn
zxAnPmCtrlSamplingType = _ZxAnPmCtrlSamplingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 10),
    _ZxAnPmCtrlSamplingType_Type()
)
zxAnPmCtrlSamplingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlSamplingType.setStatus("current")


class _ZxAnPmCtrlStatisticalInterval_Type(Integer32):
    """Custom type zxAnPmCtrlStatisticalInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ZxAnPmCtrlStatisticalInterval_Type.__name__ = "Integer32"
_ZxAnPmCtrlStatisticalInterval_Object = MibTableColumn
zxAnPmCtrlStatisticalInterval = _ZxAnPmCtrlStatisticalInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 1, 1, 11),
    _ZxAnPmCtrlStatisticalInterval_Type()
)
zxAnPmCtrlStatisticalInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmCtrlStatisticalInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPmCtrlStatisticalInterval.setUnits("Minutes")
_ZxAnPmSpareIndex_Type = Integer32
_ZxAnPmSpareIndex_Object = MibScalar
zxAnPmSpareIndex = _ZxAnPmSpareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 2),
    _ZxAnPmSpareIndex_Type()
)
zxAnPmSpareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPmSpareIndex.setStatus("current")
_ZxAnPmHisTable_Object = MibTable
zxAnPmHisTable = _ZxAnPmHisTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 31)
)
if mibBuilder.loadTexts:
    zxAnPmHisTable.setStatus("current")
_ZxAnPmHisEntry_Object = MibTableRow
zxAnPmHisEntry = _ZxAnPmHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 31, 1)
)
zxAnPmHisEntry.setIndexNames(
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisMetric"),
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisMetricInstIndex"),
)
if mibBuilder.loadTexts:
    zxAnPmHisEntry.setStatus("current")
_ZxAnPmHisMetric_Type = ObjectIdentifier
_ZxAnPmHisMetric_Object = MibTableColumn
zxAnPmHisMetric = _ZxAnPmHisMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 31, 1, 1),
    _ZxAnPmHisMetric_Type()
)
zxAnPmHisMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmHisMetric.setStatus("current")
_ZxAnPmHisMetricInstIndex_Type = ObjectIdentifier
_ZxAnPmHisMetricInstIndex_Object = MibTableColumn
zxAnPmHisMetricInstIndex = _ZxAnPmHisMetricInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 31, 1, 2),
    _ZxAnPmHisMetricInstIndex_Type()
)
zxAnPmHisMetricInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmHisMetricInstIndex.setStatus("current")
_ZxAnPmHisStatisticalValue_Type = Counter64
_ZxAnPmHisStatisticalValue_Object = MibTableColumn
zxAnPmHisStatisticalValue = _ZxAnPmHisStatisticalValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 31, 1, 3),
    _ZxAnPmHisStatisticalValue_Type()
)
zxAnPmHisStatisticalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPmHisStatisticalValue.setStatus("current")
_ZxAnPmThresholdTable_Object = MibTable
zxAnPmThresholdTable = _ZxAnPmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32)
)
if mibBuilder.loadTexts:
    zxAnPmThresholdTable.setStatus("current")
_ZxAnPmThresholdEntry_Object = MibTableRow
zxAnPmThresholdEntry = _ZxAnPmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1)
)
zxAnPmThresholdEntry.setIndexNames(
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetricInstIndex"),
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetric"),
)
if mibBuilder.loadTexts:
    zxAnPmThresholdEntry.setStatus("current")
_ZxAnPmThresholdMetricInstIndex_Type = ObjectIdentifier
_ZxAnPmThresholdMetricInstIndex_Object = MibTableColumn
zxAnPmThresholdMetricInstIndex = _ZxAnPmThresholdMetricInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 1),
    _ZxAnPmThresholdMetricInstIndex_Type()
)
zxAnPmThresholdMetricInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmThresholdMetricInstIndex.setStatus("current")
_ZxAnPmThresholdMetric_Type = ObjectIdentifier
_ZxAnPmThresholdMetric_Object = MibTableColumn
zxAnPmThresholdMetric = _ZxAnPmThresholdMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 2),
    _ZxAnPmThresholdMetric_Type()
)
zxAnPmThresholdMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmThresholdMetric.setStatus("current")


class _ZxAnPmEventTrapEnable_Type(Integer32):
    """Custom type zxAnPmEventTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnPmEventTrapEnable_Type.__name__ = "Integer32"
_ZxAnPmEventTrapEnable_Object = MibTableColumn
zxAnPmEventTrapEnable = _ZxAnPmEventTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 3),
    _ZxAnPmEventTrapEnable_Type()
)
zxAnPmEventTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmEventTrapEnable.setStatus("current")
_ZxAnPmRisingWarningThreshold_Type = Counter64
_ZxAnPmRisingWarningThreshold_Object = MibTableColumn
zxAnPmRisingWarningThreshold = _ZxAnPmRisingWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 4),
    _ZxAnPmRisingWarningThreshold_Type()
)
zxAnPmRisingWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmRisingWarningThreshold.setStatus("current")
_ZxAnPmRisingAlarmThreshold_Type = Counter64
_ZxAnPmRisingAlarmThreshold_Object = MibTableColumn
zxAnPmRisingAlarmThreshold = _ZxAnPmRisingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 5),
    _ZxAnPmRisingAlarmThreshold_Type()
)
zxAnPmRisingAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmRisingAlarmThreshold.setStatus("current")
_ZxAnPmFallingWarningThreshold_Type = Counter64
_ZxAnPmFallingWarningThreshold_Object = MibTableColumn
zxAnPmFallingWarningThreshold = _ZxAnPmFallingWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 6),
    _ZxAnPmFallingWarningThreshold_Type()
)
zxAnPmFallingWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmFallingWarningThreshold.setStatus("current")
_ZxAnPmFallingAlarmThreshold_Type = Counter64
_ZxAnPmFallingAlarmThreshold_Object = MibTableColumn
zxAnPmFallingAlarmThreshold = _ZxAnPmFallingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 7),
    _ZxAnPmFallingAlarmThreshold_Type()
)
zxAnPmFallingAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmFallingAlarmThreshold.setStatus("current")
_ZxAnPmThresholdRowStatus_Type = RowStatus
_ZxAnPmThresholdRowStatus_Object = MibTableColumn
zxAnPmThresholdRowStatus = _ZxAnPmThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 1, 32, 1, 31),
    _ZxAnPmThresholdRowStatus_Type()
)
zxAnPmThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmThresholdRowStatus.setStatus("current")
_ZxAnPerfLogMgmtObjects_ObjectIdentity = ObjectIdentity
zxAnPerfLogMgmtObjects = _ZxAnPerfLogMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2)
)


class _ZxAnPmLogAdminStatus_Type(Integer32):
    """Custom type zxAnPmLogAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnPmLogAdminStatus_Type.__name__ = "Integer32"
_ZxAnPmLogAdminStatus_Object = MibScalar
zxAnPmLogAdminStatus = _ZxAnPmLogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 1),
    _ZxAnPmLogAdminStatus_Type()
)
zxAnPmLogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogAdminStatus.setStatus("current")
_ZxAnPmLogMaxRecordRows_Type = Integer32
_ZxAnPmLogMaxRecordRows_Object = MibScalar
zxAnPmLogMaxRecordRows = _ZxAnPmLogMaxRecordRows_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 2),
    _ZxAnPmLogMaxRecordRows_Type()
)
zxAnPmLogMaxRecordRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogMaxRecordRows.setStatus("current")


class _ZxAnPmLogManualReportAction_Type(Integer32):
    """Custom type zxAnPmLogManualReportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("report", 1)
    )


_ZxAnPmLogManualReportAction_Type.__name__ = "Integer32"
_ZxAnPmLogManualReportAction_Object = MibScalar
zxAnPmLogManualReportAction = _ZxAnPmLogManualReportAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 3),
    _ZxAnPmLogManualReportAction_Type()
)
zxAnPmLogManualReportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogManualReportAction.setStatus("current")
_ZxAnPmLogManualReportStatus_Type = TruthValue
_ZxAnPmLogManualReportStatus_Object = MibScalar
zxAnPmLogManualReportStatus = _ZxAnPmLogManualReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 4),
    _ZxAnPmLogManualReportStatus_Type()
)
zxAnPmLogManualReportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPmLogManualReportStatus.setStatus("current")
_ZxAnPmLogAutoReportMetric_Type = TruthValue
_ZxAnPmLogAutoReportMetric_Object = MibScalar
zxAnPmLogAutoReportMetric = _ZxAnPmLogAutoReportMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 5),
    _ZxAnPmLogAutoReportMetric_Type()
)
zxAnPmLogAutoReportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogAutoReportMetric.setStatus("current")
_ZxAnPmLogAutoReportInterval_Type = Integer32
_ZxAnPmLogAutoReportInterval_Object = MibScalar
zxAnPmLogAutoReportInterval = _ZxAnPmLogAutoReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 6),
    _ZxAnPmLogAutoReportInterval_Type()
)
zxAnPmLogAutoReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogAutoReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPmLogAutoReportInterval.setUnits("Minute")
_ZxAnPmLogReportFtpHost_Type = DisplayString
_ZxAnPmLogReportFtpHost_Object = MibScalar
zxAnPmLogReportFtpHost = _ZxAnPmLogReportFtpHost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 7),
    _ZxAnPmLogReportFtpHost_Type()
)
zxAnPmLogReportFtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogReportFtpHost.setStatus("current")
_ZxAnPmLogReportFtpPath_Type = DisplayString
_ZxAnPmLogReportFtpPath_Object = MibScalar
zxAnPmLogReportFtpPath = _ZxAnPmLogReportFtpPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 8),
    _ZxAnPmLogReportFtpPath_Type()
)
zxAnPmLogReportFtpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogReportFtpPath.setStatus("current")
_ZxAnPmLogReportFtpUser_Type = DisplayString
_ZxAnPmLogReportFtpUser_Object = MibScalar
zxAnPmLogReportFtpUser = _ZxAnPmLogReportFtpUser_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 9),
    _ZxAnPmLogReportFtpUser_Type()
)
zxAnPmLogReportFtpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogReportFtpUser.setStatus("current")
_ZxAnPmLogReportFtpPassword_Type = DisplayString
_ZxAnPmLogReportFtpPassword_Object = MibScalar
zxAnPmLogReportFtpPassword = _ZxAnPmLogReportFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 10),
    _ZxAnPmLogReportFtpPassword_Type()
)
zxAnPmLogReportFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPmLogReportFtpPassword.setStatus("current")
_ZxAnPmLogCtrlTable_Object = MibTable
zxAnPmLogCtrlTable = _ZxAnPmLogCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31)
)
if mibBuilder.loadTexts:
    zxAnPmLogCtrlTable.setStatus("current")
_ZxAnPmLogCtrlEntry_Object = MibTableRow
zxAnPmLogCtrlEntry = _ZxAnPmLogCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31, 1)
)
zxAnPmLogCtrlEntry.setIndexNames(
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmLogCtrlMetric"),
    (0, "ZTE-AN-PERF-MGMT-MIB", "zxAnPmLogCtrlMetricInstIndex"),
)
if mibBuilder.loadTexts:
    zxAnPmLogCtrlEntry.setStatus("current")
_ZxAnPmLogCtrlMetric_Type = ObjectIdentifier
_ZxAnPmLogCtrlMetric_Object = MibTableColumn
zxAnPmLogCtrlMetric = _ZxAnPmLogCtrlMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31, 1, 1),
    _ZxAnPmLogCtrlMetric_Type()
)
zxAnPmLogCtrlMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmLogCtrlMetric.setStatus("current")
_ZxAnPmLogCtrlMetricInstIndex_Type = ObjectIdentifier
_ZxAnPmLogCtrlMetricInstIndex_Object = MibTableColumn
zxAnPmLogCtrlMetricInstIndex = _ZxAnPmLogCtrlMetricInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31, 1, 2),
    _ZxAnPmLogCtrlMetricInstIndex_Type()
)
zxAnPmLogCtrlMetricInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPmLogCtrlMetricInstIndex.setStatus("current")


class _ZxAnPmLoggingMetricAdminStatus_Type(Integer32):
    """Custom type zxAnPmLoggingMetricAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnPmLoggingMetricAdminStatus_Type.__name__ = "Integer32"
_ZxAnPmLoggingMetricAdminStatus_Object = MibTableColumn
zxAnPmLoggingMetricAdminStatus = _ZxAnPmLoggingMetricAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31, 1, 3),
    _ZxAnPmLoggingMetricAdminStatus_Type()
)
zxAnPmLoggingMetricAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmLoggingMetricAdminStatus.setStatus("current")
_ZxAnPmLogCtrlRowStatus_Type = RowStatus
_ZxAnPmLogCtrlRowStatus_Object = MibTableColumn
zxAnPmLogCtrlRowStatus = _ZxAnPmLogCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 2, 31, 1, 31),
    _ZxAnPmLogCtrlRowStatus_Type()
)
zxAnPmLogCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPmLogCtrlRowStatus.setStatus("current")
_ZxAnPerfFileMgmtObjects_ObjectIdentity = ObjectIdentity
zxAnPerfFileMgmtObjects = _ZxAnPerfFileMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 3)
)
_ZxAnPerfRetrievalControlObjects_ObjectIdentity = ObjectIdentity
zxAnPerfRetrievalControlObjects = _ZxAnPerfRetrievalControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 3, 1)
)


class _ZxAnPerfRetrievalTimeGranularity_Type(Integer32):
    """Custom type zxAnPerfRetrievalTimeGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("for15Minutes", 1),
          ("for24Hours", 2))
    )


_ZxAnPerfRetrievalTimeGranularity_Type.__name__ = "Integer32"
_ZxAnPerfRetrievalTimeGranularity_Object = MibScalar
zxAnPerfRetrievalTimeGranularity = _ZxAnPerfRetrievalTimeGranularity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 3, 1, 1),
    _ZxAnPerfRetrievalTimeGranularity_Type()
)
zxAnPerfRetrievalTimeGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPerfRetrievalTimeGranularity.setStatus("current")


class _ZxAnPerfRetrievalStartTime_Type(DisplayString):
    """Custom type zxAnPerfRetrievalStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnPerfRetrievalStartTime_Type.__name__ = "DisplayString"
_ZxAnPerfRetrievalStartTime_Object = MibScalar
zxAnPerfRetrievalStartTime = _ZxAnPerfRetrievalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 3, 1, 2),
    _ZxAnPerfRetrievalStartTime_Type()
)
zxAnPerfRetrievalStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPerfRetrievalStartTime.setStatus("current")


class _ZxAnPerfRetrievalEndTime_Type(DisplayString):
    """Custom type zxAnPerfRetrievalEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnPerfRetrievalEndTime_Type.__name__ = "DisplayString"
_ZxAnPerfRetrievalEndTime_Object = MibScalar
zxAnPerfRetrievalEndTime = _ZxAnPerfRetrievalEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 3, 1, 3),
    _ZxAnPerfRetrievalEndTime_Type()
)
zxAnPerfRetrievalEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPerfRetrievalEndTime.setStatus("current")
_ZxAnPerfMgmtTrapObjects_ObjectIdentity = ObjectIdentity
zxAnPerfMgmtTrapObjects = _ZxAnPerfMgmtTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 100)
)

# Managed Objects groups


# Notification objects

zxAnPmMetricOverWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 100, 1)
)
zxAnPmMetricOverWarning.setObjects(
      *(("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetricInstIndex"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetric"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisStatisticalValue"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlStatisticalInterval"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlSamplingType"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmRisingWarningThreshold"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPmMetricOverWarning.setStatus(
        "current"
    )

zxAnPmMetricOverWarningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 100, 2)
)
zxAnPmMetricOverWarningRestore.setObjects(
      *(("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetricInstIndex"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetric"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisStatisticalValue"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlStatisticalInterval"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlSamplingType"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmRisingWarningThreshold"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPmMetricOverWarningRestore.setStatus(
        "current"
    )

zxAnPmMetricOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 100, 3)
)
zxAnPmMetricOverAlarm.setObjects(
      *(("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetricInstIndex"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetric"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisStatisticalValue"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlStatisticalInterval"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlSamplingType"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmRisingAlarmThreshold"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPmMetricOverAlarm.setStatus(
        "current"
    )

zxAnPmMetricOverAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 189, 100, 4)
)
zxAnPmMetricOverAlarmRestore.setObjects(
      *(("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetricInstIndex"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmThresholdMetric"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmHisStatisticalValue"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlStatisticalInterval"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmCtrlSamplingType"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmRisingAlarmThreshold"),
        ("ZTE-AN-PERF-MGMT-MIB", "zxAnPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPmMetricOverAlarmRestore.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PERF-MGMT-MIB",
    **{"zxAnPerfMgmtMib": zxAnPerfMgmtMib,
       "zxAnPerfMgmtObjects": zxAnPerfMgmtObjects,
       "zxAnPmCtrlTable": zxAnPmCtrlTable,
       "zxAnPmCtrlEntry": zxAnPmCtrlEntry,
       "zxAnPmCtrlIndex": zxAnPmCtrlIndex,
       "zxAnPmCtrlDesc": zxAnPmCtrlDesc,
       "zxAnPmCtrlMetric": zxAnPmCtrlMetric,
       "zxAnPmCtrlMetricInstIndex": zxAnPmCtrlMetricInstIndex,
       "zxAnPmCtrlAdminStatus": zxAnPmCtrlAdminStatus,
       "zxAnPmCtrlBucketsRequested": zxAnPmCtrlBucketsRequested,
       "zxAnPmCtrlBucketsGranted": zxAnPmCtrlBucketsGranted,
       "zxAnPmCtrlSamplingInterval": zxAnPmCtrlSamplingInterval,
       "zxAnPmCtrlRowStatus": zxAnPmCtrlRowStatus,
       "zxAnPmCtrlSamplingType": zxAnPmCtrlSamplingType,
       "zxAnPmCtrlStatisticalInterval": zxAnPmCtrlStatisticalInterval,
       "zxAnPmSpareIndex": zxAnPmSpareIndex,
       "zxAnPmHisTable": zxAnPmHisTable,
       "zxAnPmHisEntry": zxAnPmHisEntry,
       "zxAnPmHisMetric": zxAnPmHisMetric,
       "zxAnPmHisMetricInstIndex": zxAnPmHisMetricInstIndex,
       "zxAnPmHisStatisticalValue": zxAnPmHisStatisticalValue,
       "zxAnPmThresholdTable": zxAnPmThresholdTable,
       "zxAnPmThresholdEntry": zxAnPmThresholdEntry,
       "zxAnPmThresholdMetricInstIndex": zxAnPmThresholdMetricInstIndex,
       "zxAnPmThresholdMetric": zxAnPmThresholdMetric,
       "zxAnPmEventTrapEnable": zxAnPmEventTrapEnable,
       "zxAnPmRisingWarningThreshold": zxAnPmRisingWarningThreshold,
       "zxAnPmRisingAlarmThreshold": zxAnPmRisingAlarmThreshold,
       "zxAnPmFallingWarningThreshold": zxAnPmFallingWarningThreshold,
       "zxAnPmFallingAlarmThreshold": zxAnPmFallingAlarmThreshold,
       "zxAnPmThresholdRowStatus": zxAnPmThresholdRowStatus,
       "zxAnPerfLogMgmtObjects": zxAnPerfLogMgmtObjects,
       "zxAnPmLogAdminStatus": zxAnPmLogAdminStatus,
       "zxAnPmLogMaxRecordRows": zxAnPmLogMaxRecordRows,
       "zxAnPmLogManualReportAction": zxAnPmLogManualReportAction,
       "zxAnPmLogManualReportStatus": zxAnPmLogManualReportStatus,
       "zxAnPmLogAutoReportMetric": zxAnPmLogAutoReportMetric,
       "zxAnPmLogAutoReportInterval": zxAnPmLogAutoReportInterval,
       "zxAnPmLogReportFtpHost": zxAnPmLogReportFtpHost,
       "zxAnPmLogReportFtpPath": zxAnPmLogReportFtpPath,
       "zxAnPmLogReportFtpUser": zxAnPmLogReportFtpUser,
       "zxAnPmLogReportFtpPassword": zxAnPmLogReportFtpPassword,
       "zxAnPmLogCtrlTable": zxAnPmLogCtrlTable,
       "zxAnPmLogCtrlEntry": zxAnPmLogCtrlEntry,
       "zxAnPmLogCtrlMetric": zxAnPmLogCtrlMetric,
       "zxAnPmLogCtrlMetricInstIndex": zxAnPmLogCtrlMetricInstIndex,
       "zxAnPmLoggingMetricAdminStatus": zxAnPmLoggingMetricAdminStatus,
       "zxAnPmLogCtrlRowStatus": zxAnPmLogCtrlRowStatus,
       "zxAnPerfFileMgmtObjects": zxAnPerfFileMgmtObjects,
       "zxAnPerfRetrievalControlObjects": zxAnPerfRetrievalControlObjects,
       "zxAnPerfRetrievalTimeGranularity": zxAnPerfRetrievalTimeGranularity,
       "zxAnPerfRetrievalStartTime": zxAnPerfRetrievalStartTime,
       "zxAnPerfRetrievalEndTime": zxAnPerfRetrievalEndTime,
       "zxAnPerfMgmtTrapObjects": zxAnPerfMgmtTrapObjects,
       "zxAnPmMetricOverWarning": zxAnPmMetricOverWarning,
       "zxAnPmMetricOverWarningRestore": zxAnPmMetricOverWarningRestore,
       "zxAnPmMetricOverAlarm": zxAnPmMetricOverAlarm,
       "zxAnPmMetricOverAlarmRestore": zxAnPmMetricOverAlarmRestore}
)
