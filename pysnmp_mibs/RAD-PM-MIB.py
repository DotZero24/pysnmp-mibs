# SNMP MIB module (RAD-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:55 2025
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

(AlarmEventSourceType,
 alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "AlarmEventSourceType",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

agnPerformanceManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PmEvents_ObjectIdentity = ObjectIdentity
pmEvents = _PmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 0)
)
_PmNumberOfIntervals_Type = Counter32
_PmNumberOfIntervals_Object = MibScalar
pmNumberOfIntervals = _PmNumberOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 1),
    _PmNumberOfIntervals_Type()
)
pmNumberOfIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNumberOfIntervals.setStatus("current")
_PmEntitiesEnableTable_Object = MibTable
pmEntitiesEnableTable = _PmEntitiesEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 2)
)
if mibBuilder.loadTexts:
    pmEntitiesEnableTable.setStatus("current")
_PmEntityEnableEntry_Object = MibTableRow
pmEntityEnableEntry = _PmEntityEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 2, 1)
)
pmEntityEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pmEntityEnableEntry.setStatus("current")


class _PmEntityActivity_Type(Integer32):
    """Custom type pmEntityActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PmEntityActivity_Type.__name__ = "Integer32"
_PmEntityActivity_Object = MibTableColumn
pmEntityActivity = _PmEntityActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 2, 1, 1),
    _PmEntityActivity_Type()
)
pmEntityActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEntityActivity.setStatus("current")


class _PmIntervalTimeDuration_Type(Unsigned32):
    """Custom type pmIntervalTimeDuration based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(900, 900),
    )


_PmIntervalTimeDuration_Type.__name__ = "Unsigned32"
_PmIntervalTimeDuration_Object = MibScalar
pmIntervalTimeDuration = _PmIntervalTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 3),
    _PmIntervalTimeDuration_Type()
)
pmIntervalTimeDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIntervalTimeDuration.setStatus("current")
_SystemPmStatusCmdTable_Object = MibTable
systemPmStatusCmdTable = _SystemPmStatusCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4)
)
if mibBuilder.loadTexts:
    systemPmStatusCmdTable.setStatus("current")
_SystemPmStatusCmdEntry_Object = MibTableRow
systemPmStatusCmdEntry = _SystemPmStatusCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4, 1)
)
systemPmStatusCmdEntry.setIndexNames(
    (0, "RAD-PM-MIB", "systemPmStatusCmdIndex"),
)
if mibBuilder.loadTexts:
    systemPmStatusCmdEntry.setStatus("current")
_SystemPmStatusCmdIndex_Type = Unsigned32
_SystemPmStatusCmdIndex_Object = MibTableColumn
systemPmStatusCmdIndex = _SystemPmStatusCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4, 1, 1),
    _SystemPmStatusCmdIndex_Type()
)
systemPmStatusCmdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemPmStatusCmdIndex.setStatus("current")


class _SystemPmStatusCmdActivation_Type(Integer32):
    """Custom type systemPmStatusCmdActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SystemPmStatusCmdActivation_Type.__name__ = "Integer32"
_SystemPmStatusCmdActivation_Object = MibTableColumn
systemPmStatusCmdActivation = _SystemPmStatusCmdActivation_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4, 1, 2),
    _SystemPmStatusCmdActivation_Type()
)
systemPmStatusCmdActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPmStatusCmdActivation.setStatus("current")


class _SystemPmStatusCmdStopReason_Type(Integer32):
    """Custom type systemPmStatusCmdStopReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("spaceOverflow", 2),
          ("timeDeltaOverfow", 3))
    )


_SystemPmStatusCmdStopReason_Type.__name__ = "Integer32"
_SystemPmStatusCmdStopReason_Object = MibTableColumn
systemPmStatusCmdStopReason = _SystemPmStatusCmdStopReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4, 1, 3),
    _SystemPmStatusCmdStopReason_Type()
)
systemPmStatusCmdStopReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPmStatusCmdStopReason.setStatus("current")
_SystemPmStatusCmdFreeSpace_Type = Unsigned32
_SystemPmStatusCmdFreeSpace_Object = MibTableColumn
systemPmStatusCmdFreeSpace = _SystemPmStatusCmdFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 4, 1, 4),
    _SystemPmStatusCmdFreeSpace_Type()
)
systemPmStatusCmdFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPmStatusCmdFreeSpace.setStatus("current")
_SystemPmIntervalConfigTable_Object = MibTable
systemPmIntervalConfigTable = _SystemPmIntervalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5)
)
if mibBuilder.loadTexts:
    systemPmIntervalConfigTable.setStatus("current")
_SystemPmIntervalConfigEntry_Object = MibTableRow
systemPmIntervalConfigEntry = _SystemPmIntervalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5, 1)
)
systemPmIntervalConfigEntry.setIndexNames(
    (0, "RAD-PM-MIB", "systemPmIntervalConfigIfIndexType"),
    (0, "RAD-PM-MIB", "systemPmIntervalConfigIfIndex"),
)
if mibBuilder.loadTexts:
    systemPmIntervalConfigEntry.setStatus("current")
_SystemPmIntervalConfigIfIndexType_Type = AlarmEventSourceType
_SystemPmIntervalConfigIfIndexType_Object = MibTableColumn
systemPmIntervalConfigIfIndexType = _SystemPmIntervalConfigIfIndexType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5, 1, 1),
    _SystemPmIntervalConfigIfIndexType_Type()
)
systemPmIntervalConfigIfIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemPmIntervalConfigIfIndexType.setStatus("current")
_SystemPmIntervalConfigIfIndex_Type = Unsigned32
_SystemPmIntervalConfigIfIndex_Object = MibTableColumn
systemPmIntervalConfigIfIndex = _SystemPmIntervalConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5, 1, 2),
    _SystemPmIntervalConfigIfIndex_Type()
)
systemPmIntervalConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemPmIntervalConfigIfIndex.setStatus("current")
_SystemPmIntervalConfigRowStatus_Type = RowStatus
_SystemPmIntervalConfigRowStatus_Object = MibTableColumn
systemPmIntervalConfigRowStatus = _SystemPmIntervalConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5, 1, 3),
    _SystemPmIntervalConfigRowStatus_Type()
)
systemPmIntervalConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemPmIntervalConfigRowStatus.setStatus("current")
_SystemPmIntervalConfigInterval_Type = Unsigned32
_SystemPmIntervalConfigInterval_Object = MibTableColumn
systemPmIntervalConfigInterval = _SystemPmIntervalConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 5, 1, 4),
    _SystemPmIntervalConfigInterval_Type()
)
systemPmIntervalConfigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemPmIntervalConfigInterval.setStatus("current")
_PmPortRateStatsTable_Object = MibTable
pmPortRateStatsTable = _PmPortRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7)
)
if mibBuilder.loadTexts:
    pmPortRateStatsTable.setStatus("current")
_PmPortRateStatsEntry_Object = MibTableRow
pmPortRateStatsEntry = _PmPortRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1)
)
pmPortRateStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pmPortRateStatsEntry.setStatus("current")
_PmPortRateStatsRowStatus_Type = RowStatus
_PmPortRateStatsRowStatus_Object = MibTableColumn
pmPortRateStatsRowStatus = _PmPortRateStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 1),
    _PmPortRateStatsRowStatus_Type()
)
pmPortRateStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPortRateStatsRowStatus.setStatus("current")


class _PmPortRateStatsMeasureCmd_Type(Integer32):
    """Custom type pmPortRateStatsMeasureCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PmPortRateStatsMeasureCmd_Type.__name__ = "Integer32"
_PmPortRateStatsMeasureCmd_Object = MibTableColumn
pmPortRateStatsMeasureCmd = _PmPortRateStatsMeasureCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 2),
    _PmPortRateStatsMeasureCmd_Type()
)
pmPortRateStatsMeasureCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPortRateStatsMeasureCmd.setStatus("current")


class _PmPortRateStatsDuration_Type(Unsigned32):
    """Custom type pmPortRateStatsDuration based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_PmPortRateStatsDuration_Type.__name__ = "Unsigned32"
_PmPortRateStatsDuration_Object = MibTableColumn
pmPortRateStatsDuration = _PmPortRateStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 3),
    _PmPortRateStatsDuration_Type()
)
pmPortRateStatsDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmPortRateStatsDuration.setStatus("current")
if mibBuilder.loadTexts:
    pmPortRateStatsDuration.setUnits("Seconds")
_PmPortRateStatsStartTime_Type = DateAndTime
_PmPortRateStatsStartTime_Object = MibTableColumn
pmPortRateStatsStartTime = _PmPortRateStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 4),
    _PmPortRateStatsStartTime_Type()
)
pmPortRateStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPortRateStatsStartTime.setStatus("current")


class _PmPortRateStatsStatus_Type(Integer32):
    """Custom type pmPortRateStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("idle", 2),
          ("inProgress", 3),
          ("failed", 4),
          ("passed", 5))
    )


_PmPortRateStatsStatus_Type.__name__ = "Integer32"
_PmPortRateStatsStatus_Object = MibTableColumn
pmPortRateStatsStatus = _PmPortRateStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 5),
    _PmPortRateStatsStatus_Type()
)
pmPortRateStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPortRateStatsStatus.setStatus("current")
_PmPortRateStatsRxBytes_Type = Counter64
_PmPortRateStatsRxBytes_Object = MibTableColumn
pmPortRateStatsRxBytes = _PmPortRateStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 6),
    _PmPortRateStatsRxBytes_Type()
)
pmPortRateStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPortRateStatsRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmPortRateStatsRxBytes.setUnits("bytes")
_PmPortRateStatsTxBytes_Type = Counter64
_PmPortRateStatsTxBytes_Object = MibTableColumn
pmPortRateStatsTxBytes = _PmPortRateStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 7, 1, 7),
    _PmPortRateStatsTxBytes_Type()
)
pmPortRateStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPortRateStatsTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmPortRateStatsTxBytes.setUnits("bytes")
_PmFlowRateConfigTable_Object = MibTable
pmFlowRateConfigTable = _PmFlowRateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8)
)
if mibBuilder.loadTexts:
    pmFlowRateConfigTable.setStatus("current")
_PmFlowRateConfigEntry_Object = MibTableRow
pmFlowRateConfigEntry = _PmFlowRateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1)
)
pmFlowRateConfigEntry.setIndexNames(
    (0, "RAD-PM-MIB", "pmFlowRateConfigflowIdx1"),
    (0, "RAD-PM-MIB", "pmFlowRateConfigflowIdx2"),
)
if mibBuilder.loadTexts:
    pmFlowRateConfigEntry.setStatus("current")
_PmFlowRateConfigflowIdx1_Type = Unsigned32
_PmFlowRateConfigflowIdx1_Object = MibTableColumn
pmFlowRateConfigflowIdx1 = _PmFlowRateConfigflowIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 1),
    _PmFlowRateConfigflowIdx1_Type()
)
pmFlowRateConfigflowIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmFlowRateConfigflowIdx1.setStatus("current")
_PmFlowRateConfigflowIdx2_Type = Unsigned32
_PmFlowRateConfigflowIdx2_Object = MibTableColumn
pmFlowRateConfigflowIdx2 = _PmFlowRateConfigflowIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 2),
    _PmFlowRateConfigflowIdx2_Type()
)
pmFlowRateConfigflowIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmFlowRateConfigflowIdx2.setStatus("current")
_PmFlowRateConfigRowStatus_Type = RowStatus
_PmFlowRateConfigRowStatus_Object = MibTableColumn
pmFlowRateConfigRowStatus = _PmFlowRateConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 3),
    _PmFlowRateConfigRowStatus_Type()
)
pmFlowRateConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmFlowRateConfigRowStatus.setStatus("current")


class _PmFlowRateConfigMeasureCmd_Type(Integer32):
    """Custom type pmFlowRateConfigMeasureCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PmFlowRateConfigMeasureCmd_Type.__name__ = "Integer32"
_PmFlowRateConfigMeasureCmd_Object = MibTableColumn
pmFlowRateConfigMeasureCmd = _PmFlowRateConfigMeasureCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 4),
    _PmFlowRateConfigMeasureCmd_Type()
)
pmFlowRateConfigMeasureCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmFlowRateConfigMeasureCmd.setStatus("current")


class _PmFlowRateConfigDuration_Type(Unsigned32):
    """Custom type pmFlowRateConfigDuration based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_PmFlowRateConfigDuration_Type.__name__ = "Unsigned32"
_PmFlowRateConfigDuration_Object = MibTableColumn
pmFlowRateConfigDuration = _PmFlowRateConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 5),
    _PmFlowRateConfigDuration_Type()
)
pmFlowRateConfigDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmFlowRateConfigDuration.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateConfigDuration.setUnits("Seconds")
_PmFlowRateConfigStartTime_Type = DateAndTime
_PmFlowRateConfigStartTime_Object = MibTableColumn
pmFlowRateConfigStartTime = _PmFlowRateConfigStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 6),
    _PmFlowRateConfigStartTime_Type()
)
pmFlowRateConfigStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateConfigStartTime.setStatus("current")


class _PmFlowRateConfigStatus_Type(Integer32):
    """Custom type pmFlowRateConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("idle", 2),
          ("inProgress", 3),
          ("failed", 4),
          ("passed", 5))
    )


_PmFlowRateConfigStatus_Type.__name__ = "Integer32"
_PmFlowRateConfigStatus_Object = MibTableColumn
pmFlowRateConfigStatus = _PmFlowRateConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 8, 1, 7),
    _PmFlowRateConfigStatus_Type()
)
pmFlowRateConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateConfigStatus.setStatus("current")
_PmFlowRateStatsTable_Object = MibTable
pmFlowRateStatsTable = _PmFlowRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9)
)
if mibBuilder.loadTexts:
    pmFlowRateStatsTable.setStatus("current")
_PmFlowRateStatsEntry_Object = MibTableRow
pmFlowRateStatsEntry = _PmFlowRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1)
)
pmFlowRateStatsEntry.setIndexNames(
    (0, "RAD-PM-MIB", "pmFlowRateConfigflowIdx1"),
    (0, "RAD-PM-MIB", "pmFlowRateConfigflowIdx2"),
    (0, "RAD-PM-MIB", "pmFlowRateStatsCosIndex"),
)
if mibBuilder.loadTexts:
    pmFlowRateStatsEntry.setStatus("current")


class _PmFlowRateStatsCosIndex_Type(Unsigned32):
    """Custom type pmFlowRateStatsCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_PmFlowRateStatsCosIndex_Type.__name__ = "Unsigned32"
_PmFlowRateStatsCosIndex_Object = MibTableColumn
pmFlowRateStatsCosIndex = _PmFlowRateStatsCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 1),
    _PmFlowRateStatsCosIndex_Type()
)
pmFlowRateStatsCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmFlowRateStatsCosIndex.setStatus("current")
_PmFlowRateStatsRxBytes_Type = Counter64
_PmFlowRateStatsRxBytes_Object = MibTableColumn
pmFlowRateStatsRxBytes = _PmFlowRateStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 2),
    _PmFlowRateStatsRxBytes_Type()
)
pmFlowRateStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsRxBytes.setUnits("bytes")
_PmFlowRateStatsTxBytes_Type = Counter64
_PmFlowRateStatsTxBytes_Object = MibTableColumn
pmFlowRateStatsTxBytes = _PmFlowRateStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 3),
    _PmFlowRateStatsTxBytes_Type()
)
pmFlowRateStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsTxBytes.setUnits("bytes")
_PmFlowRateStatsGreenDropBytes_Type = Counter64
_PmFlowRateStatsGreenDropBytes_Object = MibTableColumn
pmFlowRateStatsGreenDropBytes = _PmFlowRateStatsGreenDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 4),
    _PmFlowRateStatsGreenDropBytes_Type()
)
pmFlowRateStatsGreenDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsGreenDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsGreenDropBytes.setUnits("bytes")
_PmFlowRateStatsYellowDropBytes_Type = Counter64
_PmFlowRateStatsYellowDropBytes_Object = MibTableColumn
pmFlowRateStatsYellowDropBytes = _PmFlowRateStatsYellowDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 5),
    _PmFlowRateStatsYellowDropBytes_Type()
)
pmFlowRateStatsYellowDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsYellowDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsYellowDropBytes.setUnits("bytes")
_PmFlowRateStatsRedDropBytes_Type = Counter64
_PmFlowRateStatsRedDropBytes_Object = MibTableColumn
pmFlowRateStatsRedDropBytes = _PmFlowRateStatsRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 6),
    _PmFlowRateStatsRedDropBytes_Type()
)
pmFlowRateStatsRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsRedDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsRedDropBytes.setUnits("bytes")
_PmFlowRateStatsTotalDropBytes_Type = Counter64
_PmFlowRateStatsTotalDropBytes_Object = MibTableColumn
pmFlowRateStatsTotalDropBytes = _PmFlowRateStatsTotalDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 9, 1, 7),
    _PmFlowRateStatsTotalDropBytes_Type()
)
pmFlowRateStatsTotalDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFlowRateStatsTotalDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    pmFlowRateStatsTotalDropBytes.setUnits("bytes")

# Managed Objects groups


# Notification objects

systemPmProcessDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 0, 1)
)
systemPmProcessDisabled.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-PM-MIB", "systemPmStatusCmdStopReason"))
)
if mibBuilder.loadTexts:
    systemPmProcessDisabled.setStatus(
        "current"
    )

systemPmSpaceOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 74, 0, 2)
)
systemPmSpaceOverflow.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-PM-MIB", "systemPmStatusCmdFreeSpace"))
)
if mibBuilder.loadTexts:
    systemPmSpaceOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-PM-MIB",
    **{"agnPerformanceManagement": agnPerformanceManagement,
       "pmEvents": pmEvents,
       "systemPmProcessDisabled": systemPmProcessDisabled,
       "systemPmSpaceOverflow": systemPmSpaceOverflow,
       "pmNumberOfIntervals": pmNumberOfIntervals,
       "pmEntitiesEnableTable": pmEntitiesEnableTable,
       "pmEntityEnableEntry": pmEntityEnableEntry,
       "pmEntityActivity": pmEntityActivity,
       "pmIntervalTimeDuration": pmIntervalTimeDuration,
       "systemPmStatusCmdTable": systemPmStatusCmdTable,
       "systemPmStatusCmdEntry": systemPmStatusCmdEntry,
       "systemPmStatusCmdIndex": systemPmStatusCmdIndex,
       "systemPmStatusCmdActivation": systemPmStatusCmdActivation,
       "systemPmStatusCmdStopReason": systemPmStatusCmdStopReason,
       "systemPmStatusCmdFreeSpace": systemPmStatusCmdFreeSpace,
       "systemPmIntervalConfigTable": systemPmIntervalConfigTable,
       "systemPmIntervalConfigEntry": systemPmIntervalConfigEntry,
       "systemPmIntervalConfigIfIndexType": systemPmIntervalConfigIfIndexType,
       "systemPmIntervalConfigIfIndex": systemPmIntervalConfigIfIndex,
       "systemPmIntervalConfigRowStatus": systemPmIntervalConfigRowStatus,
       "systemPmIntervalConfigInterval": systemPmIntervalConfigInterval,
       "pmPortRateStatsTable": pmPortRateStatsTable,
       "pmPortRateStatsEntry": pmPortRateStatsEntry,
       "pmPortRateStatsRowStatus": pmPortRateStatsRowStatus,
       "pmPortRateStatsMeasureCmd": pmPortRateStatsMeasureCmd,
       "pmPortRateStatsDuration": pmPortRateStatsDuration,
       "pmPortRateStatsStartTime": pmPortRateStatsStartTime,
       "pmPortRateStatsStatus": pmPortRateStatsStatus,
       "pmPortRateStatsRxBytes": pmPortRateStatsRxBytes,
       "pmPortRateStatsTxBytes": pmPortRateStatsTxBytes,
       "pmFlowRateConfigTable": pmFlowRateConfigTable,
       "pmFlowRateConfigEntry": pmFlowRateConfigEntry,
       "pmFlowRateConfigflowIdx1": pmFlowRateConfigflowIdx1,
       "pmFlowRateConfigflowIdx2": pmFlowRateConfigflowIdx2,
       "pmFlowRateConfigRowStatus": pmFlowRateConfigRowStatus,
       "pmFlowRateConfigMeasureCmd": pmFlowRateConfigMeasureCmd,
       "pmFlowRateConfigDuration": pmFlowRateConfigDuration,
       "pmFlowRateConfigStartTime": pmFlowRateConfigStartTime,
       "pmFlowRateConfigStatus": pmFlowRateConfigStatus,
       "pmFlowRateStatsTable": pmFlowRateStatsTable,
       "pmFlowRateStatsEntry": pmFlowRateStatsEntry,
       "pmFlowRateStatsCosIndex": pmFlowRateStatsCosIndex,
       "pmFlowRateStatsRxBytes": pmFlowRateStatsRxBytes,
       "pmFlowRateStatsTxBytes": pmFlowRateStatsTxBytes,
       "pmFlowRateStatsGreenDropBytes": pmFlowRateStatsGreenDropBytes,
       "pmFlowRateStatsYellowDropBytes": pmFlowRateStatsYellowDropBytes,
       "pmFlowRateStatsRedDropBytes": pmFlowRateStatsRedDropBytes,
       "pmFlowRateStatsTotalDropBytes": pmFlowRateStatsTotalDropBytes}
)
