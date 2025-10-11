# SNMP MIB module (G6-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-LOGGING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:05 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Logging_ObjectIdentity = ObjectIdentity
logging = _Logging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71)
)
_LoggingSendTestEvent_Type = DisplayString
_LoggingSendTestEvent_Object = MibScalar
loggingSendTestEvent = _LoggingSendTestEvent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 1),
    _LoggingSendTestEvent_Type()
)
loggingSendTestEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingSendTestEvent.setStatus("current")


class _LoggingLogFileStorage_Type(Integer32):
    """Custom type loggingLogFileStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ramDisk", 0),
          ("sdCard", 1))
    )


_LoggingLogFileStorage_Type.__name__ = "Integer32"
_LoggingLogFileStorage_Object = MibScalar
loggingLogFileStorage = _LoggingLogFileStorage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 2),
    _LoggingLogFileStorage_Type()
)
loggingLogFileStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingLogFileStorage.setStatus("current")
_TargetTable_Object = MibTable
targetTable = _TargetTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3)
)
if mibBuilder.loadTexts:
    targetTable.setStatus("current")
_TargetEntry_Object = MibTableRow
targetEntry = _TargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1)
)
targetEntry.setIndexNames(
    (0, "G6-LOGGING-MIB", "targetIndex"),
)
if mibBuilder.loadTexts:
    targetEntry.setStatus("current")


class _TargetIndex_Type(Integer32):
    """Custom type targetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TargetIndex_Type.__name__ = "Integer32"
_TargetIndex_Object = MibTableColumn
targetIndex = _TargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 1),
    _TargetIndex_Type()
)
targetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    targetIndex.setStatus("current")
_TargetAlias_Type = DisplayString
_TargetAlias_Object = MibTableColumn
targetAlias = _TargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 2),
    _TargetAlias_Type()
)
targetAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetAlias.setStatus("current")
_TargetHostAddress_Type = DisplayString
_TargetHostAddress_Object = MibTableColumn
targetHostAddress = _TargetHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 3),
    _TargetHostAddress_Type()
)
targetHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetHostAddress.setStatus("current")


class _TargetLogType_Type(Integer32):
    """Custom type targetLogType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("syslog", 1),
          ("snmpTrapV1", 2),
          ("snmpTrapV2c", 3),
          ("snmpTrapV3", 4),
          ("snmpInformV2c", 5),
          ("snmpInformV3", 6),
          ("displayInCli", 7),
          ("recentLogs", 8))
    )


_TargetLogType_Type.__name__ = "Integer32"
_TargetLogType_Object = MibTableColumn
targetLogType = _TargetLogType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 4),
    _TargetLogType_Type()
)
targetLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetLogType.setStatus("current")


class _TargetDetailLevel_Type(Integer32):
    """Custom type targetDetailLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concise", 0),
          ("verbose", 1),
          ("extended", 2))
    )


_TargetDetailLevel_Type.__name__ = "Integer32"
_TargetDetailLevel_Object = MibTableColumn
targetDetailLevel = _TargetDetailLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 5),
    _TargetDetailLevel_Type()
)
targetDetailLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetDetailLevel.setStatus("current")


class _TargetMessageFormat_Type(Integer32):
    """Custom type targetMessageFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("preferCustom", 1),
          ("customOnly", 2))
    )


_TargetMessageFormat_Type.__name__ = "Integer32"
_TargetMessageFormat_Object = MibTableColumn
targetMessageFormat = _TargetMessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 6),
    _TargetMessageFormat_Type()
)
targetMessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetMessageFormat.setStatus("current")


class _TargetTrapType_Type(Integer32):
    """Custom type targetTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("public", 0),
          ("preferPublic", 1),
          ("private", 2),
          ("both", 3))
    )


_TargetTrapType_Type.__name__ = "Integer32"
_TargetTrapType_Object = MibTableColumn
targetTrapType = _TargetTrapType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 7),
    _TargetTrapType_Type()
)
targetTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetTrapType.setStatus("current")
_TargetTrapCommunity_Type = DisplayString
_TargetTrapCommunity_Object = MibTableColumn
targetTrapCommunity = _TargetTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 8),
    _TargetTrapCommunity_Type()
)
targetTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetTrapCommunity.setStatus("current")
_TargetSnmpV3Username_Type = DisplayString
_TargetSnmpV3Username_Object = MibTableColumn
targetSnmpV3Username = _TargetSnmpV3Username_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 9),
    _TargetSnmpV3Username_Type()
)
targetSnmpV3Username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetSnmpV3Username.setStatus("current")


class _TargetMinimumSeverity_Type(Integer32):
    """Custom type targetMinimumSeverity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("debug", 1),
          ("info", 2),
          ("notice", 3),
          ("warning", 4),
          ("error", 5),
          ("critical", 6),
          ("alert", 7),
          ("emergency", 8))
    )


_TargetMinimumSeverity_Type.__name__ = "Integer32"
_TargetMinimumSeverity_Object = MibTableColumn
targetMinimumSeverity = _TargetMinimumSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 10),
    _TargetMinimumSeverity_Type()
)
targetMinimumSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetMinimumSeverity.setStatus("current")


class _TargetRequiredRelevance_Type(Integer32):
    """Custom type targetRequiredRelevance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("negOnly", 1))
    )


_TargetRequiredRelevance_Type.__name__ = "Integer32"
_TargetRequiredRelevance_Object = MibTableColumn
targetRequiredRelevance = _TargetRequiredRelevance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 11),
    _TargetRequiredRelevance_Type()
)
targetRequiredRelevance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetRequiredRelevance.setStatus("current")


class _TargetRequiredSource_Type(Integer32):
    """Custom type targetRequiredSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("portOnly", 1),
          ("unitOnly", 2))
    )


_TargetRequiredSource_Type.__name__ = "Integer32"
_TargetRequiredSource_Object = MibTableColumn
targetRequiredSource = _TargetRequiredSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 12),
    _TargetRequiredSource_Type()
)
targetRequiredSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetRequiredSource.setStatus("current")


class _TargetLogConfigChanges_Type(Integer32):
    """Custom type targetLogConfigChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TargetLogConfigChanges_Type.__name__ = "Integer32"
_TargetLogConfigChanges_Object = MibTableColumn
targetLogConfigChanges = _TargetLogConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 13),
    _TargetLogConfigChanges_Type()
)
targetLogConfigChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetLogConfigChanges.setStatus("current")


class _TargetLogDebugEventsOnly_Type(Integer32):
    """Custom type targetLogDebugEventsOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TargetLogDebugEventsOnly_Type.__name__ = "Integer32"
_TargetLogDebugEventsOnly_Object = MibTableColumn
targetLogDebugEventsOnly = _TargetLogDebugEventsOnly_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 3, 1, 14),
    _TargetLogDebugEventsOnly_Type()
)
targetLogDebugEventsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetLogDebugEventsOnly.setStatus("current")
_HistoryConfigTable_Object = MibTable
historyConfigTable = _HistoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4)
)
if mibBuilder.loadTexts:
    historyConfigTable.setStatus("current")
_HistoryConfigEntry_Object = MibTableRow
historyConfigEntry = _HistoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1)
)
historyConfigEntry.setIndexNames(
    (0, "G6-LOGGING-MIB", "historyConfigIndex"),
)
if mibBuilder.loadTexts:
    historyConfigEntry.setStatus("current")


class _HistoryConfigIndex_Type(Integer32):
    """Custom type historyConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_HistoryConfigIndex_Type.__name__ = "Integer32"
_HistoryConfigIndex_Object = MibTableColumn
historyConfigIndex = _HistoryConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 1),
    _HistoryConfigIndex_Type()
)
historyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyConfigIndex.setStatus("current")
_HistoryConfigName_Type = DisplayString
_HistoryConfigName_Object = MibTableColumn
historyConfigName = _HistoryConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 2),
    _HistoryConfigName_Type()
)
historyConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyConfigName.setStatus("current")


class _HistoryConfigRecordMode_Type(Integer32):
    """Custom type historyConfigRecordMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HistoryConfigRecordMode_Type.__name__ = "Integer32"
_HistoryConfigRecordMode_Object = MibTableColumn
historyConfigRecordMode = _HistoryConfigRecordMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 3),
    _HistoryConfigRecordMode_Type()
)
historyConfigRecordMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyConfigRecordMode.setStatus("current")


class _HistoryConfigHistoryFileMode_Type(Integer32):
    """Custom type historyConfigHistoryFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("hourly", 1),
          ("daily", 2))
    )


_HistoryConfigHistoryFileMode_Type.__name__ = "Integer32"
_HistoryConfigHistoryFileMode_Object = MibTableColumn
historyConfigHistoryFileMode = _HistoryConfigHistoryFileMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 4),
    _HistoryConfigHistoryFileMode_Type()
)
historyConfigHistoryFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyConfigHistoryFileMode.setStatus("current")
_HistoryConfigDotstring_Type = DisplayString
_HistoryConfigDotstring_Object = MibTableColumn
historyConfigDotstring = _HistoryConfigDotstring_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 5),
    _HistoryConfigDotstring_Type()
)
historyConfigDotstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyConfigDotstring.setStatus("current")
_HistoryConfigRestart_Type = DisplayString
_HistoryConfigRestart_Object = MibTableColumn
historyConfigRestart = _HistoryConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 4, 1, 6),
    _HistoryConfigRestart_Type()
)
historyConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyConfigRestart.setStatus("current")
_StatisticsTable_Object = MibTable
statisticsTable = _StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100)
)
if mibBuilder.loadTexts:
    statisticsTable.setStatus("current")
_StatisticsEntry_Object = MibTableRow
statisticsEntry = _StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1)
)
statisticsEntry.setIndexNames(
    (0, "G6-LOGGING-MIB", "statisticsIndex"),
)
if mibBuilder.loadTexts:
    statisticsEntry.setStatus("current")


class _StatisticsIndex_Type(Integer32):
    """Custom type statisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_StatisticsIndex_Type.__name__ = "Integer32"
_StatisticsIndex_Object = MibTableColumn
statisticsIndex = _StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 1),
    _StatisticsIndex_Type()
)
statisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statisticsIndex.setStatus("current")
_StatisticsNumberOfTargets_Type = Unsigned32
_StatisticsNumberOfTargets_Object = MibTableColumn
statisticsNumberOfTargets = _StatisticsNumberOfTargets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 2),
    _StatisticsNumberOfTargets_Type()
)
statisticsNumberOfTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsNumberOfTargets.setStatus("current")
_StatisticsLogfileCounter_Type = Unsigned32
_StatisticsLogfileCounter_Object = MibTableColumn
statisticsLogfileCounter = _StatisticsLogfileCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 3),
    _StatisticsLogfileCounter_Type()
)
statisticsLogfileCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLogfileCounter.setStatus("current")
_StatisticsSyslogCounter_Type = Unsigned32
_StatisticsSyslogCounter_Object = MibTableColumn
statisticsSyslogCounter = _StatisticsSyslogCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 4),
    _StatisticsSyslogCounter_Type()
)
statisticsSyslogCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsSyslogCounter.setStatus("current")
_StatisticsSyslogErrorCounter_Type = Unsigned32
_StatisticsSyslogErrorCounter_Object = MibTableColumn
statisticsSyslogErrorCounter = _StatisticsSyslogErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 5),
    _StatisticsSyslogErrorCounter_Type()
)
statisticsSyslogErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsSyslogErrorCounter.setStatus("current")
_StatisticsLastSyslogResponse_Type = DisplayString
_StatisticsLastSyslogResponse_Object = MibTableColumn
statisticsLastSyslogResponse = _StatisticsLastSyslogResponse_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 6),
    _StatisticsLastSyslogResponse_Type()
)
statisticsLastSyslogResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLastSyslogResponse.setStatus("current")
_StatisticsTrapCounter_Type = Unsigned32
_StatisticsTrapCounter_Object = MibTableColumn
statisticsTrapCounter = _StatisticsTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 7),
    _StatisticsTrapCounter_Type()
)
statisticsTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsTrapCounter.setStatus("current")
_StatisticsTrapErrorCounter_Type = Unsigned32
_StatisticsTrapErrorCounter_Object = MibTableColumn
statisticsTrapErrorCounter = _StatisticsTrapErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 8),
    _StatisticsTrapErrorCounter_Type()
)
statisticsTrapErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsTrapErrorCounter.setStatus("current")
_StatisticsActiveLogfileIndex_Type = Unsigned32
_StatisticsActiveLogfileIndex_Object = MibTableColumn
statisticsActiveLogfileIndex = _StatisticsActiveLogfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 9),
    _StatisticsActiveLogfileIndex_Type()
)
statisticsActiveLogfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsActiveLogfileIndex.setStatus("current")
_StatisticsLogfile1Size_Type = Unsigned32
_StatisticsLogfile1Size_Object = MibTableColumn
statisticsLogfile1Size = _StatisticsLogfile1Size_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 10),
    _StatisticsLogfile1Size_Type()
)
statisticsLogfile1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLogfile1Size.setStatus("current")
_StatisticsLogfile2Size_Type = Unsigned32
_StatisticsLogfile2Size_Object = MibTableColumn
statisticsLogfile2Size = _StatisticsLogfile2Size_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 100, 1, 11),
    _StatisticsLogfile2Size_Type()
)
statisticsLogfile2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLogfile2Size.setStatus("current")
_RecentLogsTable_Object = MibTable
recentLogsTable = _RecentLogsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101)
)
if mibBuilder.loadTexts:
    recentLogsTable.setStatus("current")
_RecentLogsEntry_Object = MibTableRow
recentLogsEntry = _RecentLogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1)
)
recentLogsEntry.setIndexNames(
    (0, "G6-LOGGING-MIB", "recentLogsIndex"),
)
if mibBuilder.loadTexts:
    recentLogsEntry.setStatus("current")


class _RecentLogsIndex_Type(Integer32):
    """Custom type recentLogsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_RecentLogsIndex_Type.__name__ = "Integer32"
_RecentLogsIndex_Object = MibTableColumn
recentLogsIndex = _RecentLogsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1, 1),
    _RecentLogsIndex_Type()
)
recentLogsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    recentLogsIndex.setStatus("current")
_RecentLogsTimeStamp_Type = Counter32
_RecentLogsTimeStamp_Object = MibTableColumn
recentLogsTimeStamp = _RecentLogsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1, 2),
    _RecentLogsTimeStamp_Type()
)
recentLogsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recentLogsTimeStamp.setStatus("current")


class _RecentLogsSeverity_Type(Integer32):
    """Custom type recentLogsSeverity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("debug", 1),
          ("info", 2),
          ("notice", 3),
          ("warning", 4),
          ("error", 5),
          ("critical", 6),
          ("alert", 7),
          ("emergency", 8))
    )


_RecentLogsSeverity_Type.__name__ = "Integer32"
_RecentLogsSeverity_Object = MibTableColumn
recentLogsSeverity = _RecentLogsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1, 3),
    _RecentLogsSeverity_Type()
)
recentLogsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recentLogsSeverity.setStatus("current")
_RecentLogsSource_Type = DisplayString
_RecentLogsSource_Object = MibTableColumn
recentLogsSource = _RecentLogsSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1, 4),
    _RecentLogsSource_Type()
)
recentLogsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recentLogsSource.setStatus("current")
_RecentLogsMessage_Type = DisplayString
_RecentLogsMessage_Object = MibTableColumn
recentLogsMessage = _RecentLogsMessage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 101, 1, 5),
    _RecentLogsMessage_Type()
)
recentLogsMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recentLogsMessage.setStatus("current")
_HistoryRecordsTable_Object = MibTable
historyRecordsTable = _HistoryRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102)
)
if mibBuilder.loadTexts:
    historyRecordsTable.setStatus("current")
_HistoryRecordsEntry_Object = MibTableRow
historyRecordsEntry = _HistoryRecordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1)
)
historyRecordsEntry.setIndexNames(
    (0, "G6-LOGGING-MIB", "historyRecordsIndex"),
)
if mibBuilder.loadTexts:
    historyRecordsEntry.setStatus("current")


class _HistoryRecordsIndex_Type(Integer32):
    """Custom type historyRecordsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_HistoryRecordsIndex_Type.__name__ = "Integer32"
_HistoryRecordsIndex_Object = MibTableColumn
historyRecordsIndex = _HistoryRecordsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 1),
    _HistoryRecordsIndex_Type()
)
historyRecordsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyRecordsIndex.setStatus("current")
_HistoryRecordsName_Type = DisplayString
_HistoryRecordsName_Object = MibTableColumn
historyRecordsName = _HistoryRecordsName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 2),
    _HistoryRecordsName_Type()
)
historyRecordsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsName.setStatus("current")


class _HistoryRecordsState_Type(Integer32):
    """Custom type historyRecordsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("invalid", 1),
          ("normal", 2),
          ("updating", 3))
    )


_HistoryRecordsState_Type.__name__ = "Integer32"
_HistoryRecordsState_Object = MibTableColumn
historyRecordsState = _HistoryRecordsState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 3),
    _HistoryRecordsState_Type()
)
historyRecordsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsState.setStatus("current")
_HistoryRecordsLastValue_Type = DisplayString
_HistoryRecordsLastValue_Object = MibTableColumn
historyRecordsLastValue = _HistoryRecordsLastValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 4),
    _HistoryRecordsLastValue_Type()
)
historyRecordsLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsLastValue.setStatus("current")
_HistoryRecordsAverageLastMinute_Type = DisplayString
_HistoryRecordsAverageLastMinute_Object = MibTableColumn
historyRecordsAverageLastMinute = _HistoryRecordsAverageLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 5),
    _HistoryRecordsAverageLastMinute_Type()
)
historyRecordsAverageLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsAverageLastMinute.setStatus("current")
_HistoryRecordsAverageLastHour_Type = DisplayString
_HistoryRecordsAverageLastHour_Object = MibTableColumn
historyRecordsAverageLastHour = _HistoryRecordsAverageLastHour_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 6),
    _HistoryRecordsAverageLastHour_Type()
)
historyRecordsAverageLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsAverageLastHour.setStatus("current")
_HistoryRecordsLastMinute_Type = DisplayString
_HistoryRecordsLastMinute_Object = MibTableColumn
historyRecordsLastMinute = _HistoryRecordsLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 7),
    _HistoryRecordsLastMinute_Type()
)
historyRecordsLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsLastMinute.setStatus("current")
_HistoryRecordsLastHour_Type = DisplayString
_HistoryRecordsLastHour_Object = MibTableColumn
historyRecordsLastHour = _HistoryRecordsLastHour_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 8),
    _HistoryRecordsLastHour_Type()
)
historyRecordsLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsLastHour.setStatus("current")
_HistoryRecordsLastDay_Type = DisplayString
_HistoryRecordsLastDay_Object = MibTableColumn
historyRecordsLastDay = _HistoryRecordsLastDay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 9),
    _HistoryRecordsLastDay_Type()
)
historyRecordsLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsLastDay.setStatus("current")
_HistoryRecordsLastUpdate_Type = Counter32
_HistoryRecordsLastUpdate_Object = MibTableColumn
historyRecordsLastUpdate = _HistoryRecordsLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 71, 102, 1, 10),
    _HistoryRecordsLastUpdate_Type()
)
historyRecordsLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyRecordsLastUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-LOGGING-MIB",
    **{"management": management,
       "logging": logging,
       "loggingSendTestEvent": loggingSendTestEvent,
       "loggingLogFileStorage": loggingLogFileStorage,
       "targetTable": targetTable,
       "targetEntry": targetEntry,
       "targetIndex": targetIndex,
       "targetAlias": targetAlias,
       "targetHostAddress": targetHostAddress,
       "targetLogType": targetLogType,
       "targetDetailLevel": targetDetailLevel,
       "targetMessageFormat": targetMessageFormat,
       "targetTrapType": targetTrapType,
       "targetTrapCommunity": targetTrapCommunity,
       "targetSnmpV3Username": targetSnmpV3Username,
       "targetMinimumSeverity": targetMinimumSeverity,
       "targetRequiredRelevance": targetRequiredRelevance,
       "targetRequiredSource": targetRequiredSource,
       "targetLogConfigChanges": targetLogConfigChanges,
       "targetLogDebugEventsOnly": targetLogDebugEventsOnly,
       "historyConfigTable": historyConfigTable,
       "historyConfigEntry": historyConfigEntry,
       "historyConfigIndex": historyConfigIndex,
       "historyConfigName": historyConfigName,
       "historyConfigRecordMode": historyConfigRecordMode,
       "historyConfigHistoryFileMode": historyConfigHistoryFileMode,
       "historyConfigDotstring": historyConfigDotstring,
       "historyConfigRestart": historyConfigRestart,
       "statisticsTable": statisticsTable,
       "statisticsEntry": statisticsEntry,
       "statisticsIndex": statisticsIndex,
       "statisticsNumberOfTargets": statisticsNumberOfTargets,
       "statisticsLogfileCounter": statisticsLogfileCounter,
       "statisticsSyslogCounter": statisticsSyslogCounter,
       "statisticsSyslogErrorCounter": statisticsSyslogErrorCounter,
       "statisticsLastSyslogResponse": statisticsLastSyslogResponse,
       "statisticsTrapCounter": statisticsTrapCounter,
       "statisticsTrapErrorCounter": statisticsTrapErrorCounter,
       "statisticsActiveLogfileIndex": statisticsActiveLogfileIndex,
       "statisticsLogfile1Size": statisticsLogfile1Size,
       "statisticsLogfile2Size": statisticsLogfile2Size,
       "recentLogsTable": recentLogsTable,
       "recentLogsEntry": recentLogsEntry,
       "recentLogsIndex": recentLogsIndex,
       "recentLogsTimeStamp": recentLogsTimeStamp,
       "recentLogsSeverity": recentLogsSeverity,
       "recentLogsSource": recentLogsSource,
       "recentLogsMessage": recentLogsMessage,
       "historyRecordsTable": historyRecordsTable,
       "historyRecordsEntry": historyRecordsEntry,
       "historyRecordsIndex": historyRecordsIndex,
       "historyRecordsName": historyRecordsName,
       "historyRecordsState": historyRecordsState,
       "historyRecordsLastValue": historyRecordsLastValue,
       "historyRecordsAverageLastMinute": historyRecordsAverageLastMinute,
       "historyRecordsAverageLastHour": historyRecordsAverageLastHour,
       "historyRecordsLastMinute": historyRecordsLastMinute,
       "historyRecordsLastHour": historyRecordsLastHour,
       "historyRecordsLastDay": historyRecordsLastDay,
       "historyRecordsLastUpdate": historyRecordsLastUpdate}
)
