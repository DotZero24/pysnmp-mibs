# SNMP MIB module (ZTE-AN-HIS-PERF-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-HIS-PERF-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:17 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnHisPerfMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168)
)
if mibBuilder.loadTexts:
    zxAnHisPerfMgmtMib.setRevisions(
        ("2011-11-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnHisPerfMgmtObjects_ObjectIdentity = ObjectIdentity
zxAnHisPerfMgmtObjects = _ZxAnHisPerfMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1)
)
_ZxAnHisPerfMgmtThreshAlmObjects_ObjectIdentity = ObjectIdentity
zxAnHisPerfMgmtThreshAlmObjects = _ZxAnHisPerfMgmtThreshAlmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1)
)


class _ZxAnHisPmMetricInstIndex_Type(DisplayString):
    """Custom type zxAnHisPmMetricInstIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnHisPmMetricInstIndex_Type.__name__ = "DisplayString"
_ZxAnHisPmMetricInstIndex_Object = MibScalar
zxAnHisPmMetricInstIndex = _ZxAnHisPmMetricInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 1),
    _ZxAnHisPmMetricInstIndex_Type()
)
zxAnHisPmMetricInstIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmMetricInstIndex.setStatus("current")
_ZxAnHisPmThresholdMetric_Type = ObjectIdentifier
_ZxAnHisPmThresholdMetric_Object = MibScalar
zxAnHisPmThresholdMetric = _ZxAnHisPmThresholdMetric_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 2),
    _ZxAnHisPmThresholdMetric_Type()
)
zxAnHisPmThresholdMetric.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmThresholdMetric.setStatus("current")
_ZxAnHisPmStatisticalValue_Type = Counter64
_ZxAnHisPmStatisticalValue_Object = MibScalar
zxAnHisPmStatisticalValue = _ZxAnHisPmStatisticalValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 3),
    _ZxAnHisPmStatisticalValue_Type()
)
zxAnHisPmStatisticalValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmStatisticalValue.setStatus("current")
_ZxAnHisPmRisingWarningThreshold_Type = Counter64
_ZxAnHisPmRisingWarningThreshold_Object = MibScalar
zxAnHisPmRisingWarningThreshold = _ZxAnHisPmRisingWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 4),
    _ZxAnHisPmRisingWarningThreshold_Type()
)
zxAnHisPmRisingWarningThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmRisingWarningThreshold.setStatus("current")
_ZxAnHisPmRisingAlarmThreshold_Type = Counter64
_ZxAnHisPmRisingAlarmThreshold_Object = MibScalar
zxAnHisPmRisingAlarmThreshold = _ZxAnHisPmRisingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 5),
    _ZxAnHisPmRisingAlarmThreshold_Type()
)
zxAnHisPmRisingAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmRisingAlarmThreshold.setStatus("current")
_ZxAnHisPmFallingWarningThreshold_Type = Counter64
_ZxAnHisPmFallingWarningThreshold_Object = MibScalar
zxAnHisPmFallingWarningThreshold = _ZxAnHisPmFallingWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 6),
    _ZxAnHisPmFallingWarningThreshold_Type()
)
zxAnHisPmFallingWarningThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmFallingWarningThreshold.setStatus("current")
_ZxAnHisPmFallingAlarmThreshold_Type = Counter64
_ZxAnHisPmFallingAlarmThreshold_Object = MibScalar
zxAnHisPmFallingAlarmThreshold = _ZxAnHisPmFallingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 1, 7),
    _ZxAnHisPmFallingAlarmThreshold_Type()
)
zxAnHisPmFallingAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnHisPmFallingAlarmThreshold.setStatus("current")
_ZxAnHisPerfMgmtGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnHisPerfMgmtGlobalObjects = _ZxAnHisPerfMgmtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 2)
)


class _ZxAnHisPerfMgmtSampleEnable_Type(Integer32):
    """Custom type zxAnHisPerfMgmtSampleEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnHisPerfMgmtSampleEnable_Type.__name__ = "Integer32"
_ZxAnHisPerfMgmtSampleEnable_Object = MibScalar
zxAnHisPerfMgmtSampleEnable = _ZxAnHisPerfMgmtSampleEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 2, 1),
    _ZxAnHisPerfMgmtSampleEnable_Type()
)
zxAnHisPerfMgmtSampleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnHisPerfMgmtSampleEnable.setStatus("current")


class _ZxAnHisPerfMgmtAlarmEnable_Type(Integer32):
    """Custom type zxAnHisPerfMgmtAlarmEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnHisPerfMgmtAlarmEnable_Type.__name__ = "Integer32"
_ZxAnHisPerfMgmtAlarmEnable_Object = MibScalar
zxAnHisPerfMgmtAlarmEnable = _ZxAnHisPerfMgmtAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 2, 2),
    _ZxAnHisPerfMgmtAlarmEnable_Type()
)
zxAnHisPerfMgmtAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnHisPerfMgmtAlarmEnable.setStatus("current")


class _ZxAnHisPerfMgmtAutoUploadEnable_Type(Integer32):
    """Custom type zxAnHisPerfMgmtAutoUploadEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnHisPerfMgmtAutoUploadEnable_Type.__name__ = "Integer32"
_ZxAnHisPerfMgmtAutoUploadEnable_Object = MibScalar
zxAnHisPerfMgmtAutoUploadEnable = _ZxAnHisPerfMgmtAutoUploadEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 1, 2, 3),
    _ZxAnHisPerfMgmtAutoUploadEnable_Type()
)
zxAnHisPerfMgmtAutoUploadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnHisPerfMgmtAutoUploadEnable.setStatus("current")
_ZxAnHisPerfMgmtTrapObjects_ObjectIdentity = ObjectIdentity
zxAnHisPerfMgmtTrapObjects = _ZxAnHisPerfMgmtTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3)
)
_ZxAnHisPerfMgmtConformance_ObjectIdentity = ObjectIdentity
zxAnHisPerfMgmtConformance = _ZxAnHisPerfMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4)
)
_ZxAnHisPerfMIBCompliances_ObjectIdentity = ObjectIdentity
zxAnHisPerfMIBCompliances = _ZxAnHisPerfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4, 1)
)
_ZxAnHisPerfMIBGroups_ObjectIdentity = ObjectIdentity
zxAnHisPerfMIBGroups = _ZxAnHisPerfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4, 2)
)

# Managed Objects groups

zxAnHisPerfThreshAlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4, 2, 1)
)
zxAnHisPerfThreshAlmGroup.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingWarningThreshold"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingAlarmThreshold"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingWarningThreshold"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnHisPerfThreshAlmGroup.setStatus("current")

zxAnHisPerfGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4, 2, 2)
)
zxAnHisPerfGlobalGroup.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPerfMgmtSampleEnable"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPerfMgmtAlarmEnable"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPerfMgmtAutoUploadEnable"))
)
if mibBuilder.loadTexts:
    zxAnHisPerfGlobalGroup.setStatus("current")


# Notification objects

zxAnPm15minRisingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 1)
)
zxAnPm15minRisingWarning.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minRisingWarning.setStatus(
        "current"
    )

zxAnPm15minRisingWarningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 2)
)
zxAnPm15minRisingWarningRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minRisingWarningRestore.setStatus(
        "current"
    )

zxAnPm15minRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 3)
)
zxAnPm15minRisingAlarm.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minRisingAlarm.setStatus(
        "current"
    )

zxAnPm15minRisingAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 4)
)
zxAnPm15minRisingAlarmRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minRisingAlarmRestore.setStatus(
        "current"
    )

zxAnPm24hRisingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 5)
)
zxAnPm24hRisingWarning.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hRisingWarning.setStatus(
        "current"
    )

zxAnPm24hRisingWarningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 6)
)
zxAnPm24hRisingWarningRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hRisingWarningRestore.setStatus(
        "current"
    )

zxAnPm24hRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 7)
)
zxAnPm24hRisingAlarm.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hRisingAlarm.setStatus(
        "current"
    )

zxAnPm24hRisingAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 8)
)
zxAnPm24hRisingAlarmRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmRisingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hRisingAlarmRestore.setStatus(
        "current"
    )

zxAnPm15minFallingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 9)
)
zxAnPm15minFallingWarning.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minFallingWarning.setStatus(
        "current"
    )

zxAnPm15minFallingWarningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 10)
)
zxAnPm15minFallingWarningRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minFallingWarningRestore.setStatus(
        "current"
    )

zxAnPm15minFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 11)
)
zxAnPm15minFallingAlarm.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minFallingAlarm.setStatus(
        "current"
    )

zxAnPm15minFallingAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 12)
)
zxAnPm15minFallingAlarmRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm15minFallingAlarmRestore.setStatus(
        "current"
    )

zxAnPm24hFallingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 13)
)
zxAnPm24hFallingWarning.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hFallingWarning.setStatus(
        "current"
    )

zxAnPm24hFallingWarningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 14)
)
zxAnPm24hFallingWarningRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingWarningThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hFallingWarningRestore.setStatus(
        "current"
    )

zxAnPm24hFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 15)
)
zxAnPm24hFallingAlarm.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hFallingAlarm.setStatus(
        "current"
    )

zxAnPm24hFallingAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 3, 16)
)
zxAnPm24hFallingAlarmRestore.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmMetricInstIndex"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmThresholdMetric"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmStatisticalValue"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPmFallingAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnPm24hFallingAlarmRestore.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnHisPerfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 168, 4, 1, 1)
)
zxAnHisPerfMIBCompliance.setObjects(
      *(("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPerfThreshAlmGroup"),
        ("ZTE-AN-HIS-PERF-MGMT-MIB", "zxAnHisPerfGlobalGroup"))
)
if mibBuilder.loadTexts:
    zxAnHisPerfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-HIS-PERF-MGMT-MIB",
    **{"zxAnHisPerfMgmtMib": zxAnHisPerfMgmtMib,
       "zxAnHisPerfMgmtObjects": zxAnHisPerfMgmtObjects,
       "zxAnHisPerfMgmtThreshAlmObjects": zxAnHisPerfMgmtThreshAlmObjects,
       "zxAnHisPmMetricInstIndex": zxAnHisPmMetricInstIndex,
       "zxAnHisPmThresholdMetric": zxAnHisPmThresholdMetric,
       "zxAnHisPmStatisticalValue": zxAnHisPmStatisticalValue,
       "zxAnHisPmRisingWarningThreshold": zxAnHisPmRisingWarningThreshold,
       "zxAnHisPmRisingAlarmThreshold": zxAnHisPmRisingAlarmThreshold,
       "zxAnHisPmFallingWarningThreshold": zxAnHisPmFallingWarningThreshold,
       "zxAnHisPmFallingAlarmThreshold": zxAnHisPmFallingAlarmThreshold,
       "zxAnHisPerfMgmtGlobalObjects": zxAnHisPerfMgmtGlobalObjects,
       "zxAnHisPerfMgmtSampleEnable": zxAnHisPerfMgmtSampleEnable,
       "zxAnHisPerfMgmtAlarmEnable": zxAnHisPerfMgmtAlarmEnable,
       "zxAnHisPerfMgmtAutoUploadEnable": zxAnHisPerfMgmtAutoUploadEnable,
       "zxAnHisPerfMgmtTrapObjects": zxAnHisPerfMgmtTrapObjects,
       "zxAnPm15minRisingWarning": zxAnPm15minRisingWarning,
       "zxAnPm15minRisingWarningRestore": zxAnPm15minRisingWarningRestore,
       "zxAnPm15minRisingAlarm": zxAnPm15minRisingAlarm,
       "zxAnPm15minRisingAlarmRestore": zxAnPm15minRisingAlarmRestore,
       "zxAnPm24hRisingWarning": zxAnPm24hRisingWarning,
       "zxAnPm24hRisingWarningRestore": zxAnPm24hRisingWarningRestore,
       "zxAnPm24hRisingAlarm": zxAnPm24hRisingAlarm,
       "zxAnPm24hRisingAlarmRestore": zxAnPm24hRisingAlarmRestore,
       "zxAnPm15minFallingWarning": zxAnPm15minFallingWarning,
       "zxAnPm15minFallingWarningRestore": zxAnPm15minFallingWarningRestore,
       "zxAnPm15minFallingAlarm": zxAnPm15minFallingAlarm,
       "zxAnPm15minFallingAlarmRestore": zxAnPm15minFallingAlarmRestore,
       "zxAnPm24hFallingWarning": zxAnPm24hFallingWarning,
       "zxAnPm24hFallingWarningRestore": zxAnPm24hFallingWarningRestore,
       "zxAnPm24hFallingAlarm": zxAnPm24hFallingAlarm,
       "zxAnPm24hFallingAlarmRestore": zxAnPm24hFallingAlarmRestore,
       "zxAnHisPerfMgmtConformance": zxAnHisPerfMgmtConformance,
       "zxAnHisPerfMIBCompliances": zxAnHisPerfMIBCompliances,
       "zxAnHisPerfMIBCompliance": zxAnHisPerfMIBCompliance,
       "zxAnHisPerfMIBGroups": zxAnHisPerfMIBGroups,
       "zxAnHisPerfThreshAlmGroup": zxAnHisPerfThreshAlmGroup,
       "zxAnHisPerfGlobalGroup": zxAnHisPerfGlobalGroup}
)
