# SNMP MIB module (NEWTEC-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:58 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcSystemTime) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcSystemTime")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200)
)
if mibBuilder.loadTexts:
    ntcAlarm.setRevisions(
        ("2014-09-09 09:00",
         "2014-03-18 12:00",
         "2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAlmObjects_ObjectIdentity = ObjectIdentity
ntcAlmObjects = _NtcAlmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1)
)
if mibBuilder.loadTexts:
    ntcAlmObjects.setStatus("current")


class _NtcAlmReset_Type(Integer32):
    """Custom type ntcAlmReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_NtcAlmReset_Type.__name__ = "Integer32"
_NtcAlmReset_Object = MibScalar
ntcAlmReset = _NtcAlmReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 1),
    _NtcAlmReset_Type()
)
ntcAlmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAlmReset.setStatus("current")
_NtcAlmDefinitionTable_Object = MibTable
ntcAlmDefinitionTable = _NtcAlmDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 2)
)
if mibBuilder.loadTexts:
    ntcAlmDefinitionTable.setStatus("current")
_NtcAlmDefinitionEntry_Object = MibTableRow
ntcAlmDefinitionEntry = _NtcAlmDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 2, 1)
)
ntcAlmDefinitionEntry.setIndexNames(
    (0, "NEWTEC-ALARM-MIB", "ntcAlmDefinitionName"),
)
if mibBuilder.loadTexts:
    ntcAlmDefinitionEntry.setStatus("current")


class _NtcAlmDefinitionName_Type(DisplayString):
    """Custom type ntcAlmDefinitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NtcAlmDefinitionName_Type.__name__ = "DisplayString"
_NtcAlmDefinitionName_Object = MibTableColumn
ntcAlmDefinitionName = _NtcAlmDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 2, 1, 1),
    _NtcAlmDefinitionName_Type()
)
ntcAlmDefinitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAlmDefinitionName.setStatus("current")


class _NtcAlmDefinitionSeverity_Type(DisplayString):
    """Custom type ntcAlmDefinitionSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcAlmDefinitionSeverity_Type.__name__ = "DisplayString"
_NtcAlmDefinitionSeverity_Object = MibTableColumn
ntcAlmDefinitionSeverity = _NtcAlmDefinitionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 2, 1, 2),
    _NtcAlmDefinitionSeverity_Type()
)
ntcAlmDefinitionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmDefinitionSeverity.setStatus("current")
_NtcAlmDefinitionDescription_Type = DisplayString
_NtcAlmDefinitionDescription_Object = MibTableColumn
ntcAlmDefinitionDescription = _NtcAlmDefinitionDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 2, 1, 3),
    _NtcAlmDefinitionDescription_Type()
)
ntcAlmDefinitionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmDefinitionDescription.setStatus("current")
_NtcAlmActiveTable_Object = MibTable
ntcAlmActiveTable = _NtcAlmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3)
)
if mibBuilder.loadTexts:
    ntcAlmActiveTable.setStatus("current")
_NtcAlmActiveEntry_Object = MibTableRow
ntcAlmActiveEntry = _NtcAlmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1)
)
ntcAlmActiveEntry.setIndexNames(
    (0, "NEWTEC-ALARM-MIB", "ntcAlmActiveName"),
)
if mibBuilder.loadTexts:
    ntcAlmActiveEntry.setStatus("current")


class _NtcAlmActiveName_Type(DisplayString):
    """Custom type ntcAlmActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NtcAlmActiveName_Type.__name__ = "DisplayString"
_NtcAlmActiveName_Object = MibTableColumn
ntcAlmActiveName = _NtcAlmActiveName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 1),
    _NtcAlmActiveName_Type()
)
ntcAlmActiveName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAlmActiveName.setStatus("current")


class _NtcAlmActiveSeverity_Type(DisplayString):
    """Custom type ntcAlmActiveSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcAlmActiveSeverity_Type.__name__ = "DisplayString"
_NtcAlmActiveSeverity_Object = MibTableColumn
ntcAlmActiveSeverity = _NtcAlmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 2),
    _NtcAlmActiveSeverity_Type()
)
ntcAlmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveSeverity.setStatus("current")
_NtcAlmActiveTime_Type = NtcSystemTime
_NtcAlmActiveTime_Object = MibTableColumn
ntcAlmActiveTime = _NtcAlmActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 3),
    _NtcAlmActiveTime_Type()
)
ntcAlmActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveTime.setStatus("current")
_NtcAlmActiveCount_Type = Counter32
_NtcAlmActiveCount_Object = MibTableColumn
ntcAlmActiveCount = _NtcAlmActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 4),
    _NtcAlmActiveCount_Type()
)
ntcAlmActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveCount.setStatus("current")


class _NtcAlmActiveSource_Type(DisplayString):
    """Custom type ntcAlmActiveSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmActiveSource_Type.__name__ = "DisplayString"
_NtcAlmActiveSource_Object = MibTableColumn
ntcAlmActiveSource = _NtcAlmActiveSource_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 5),
    _NtcAlmActiveSource_Type()
)
ntcAlmActiveSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveSource.setStatus("current")
_NtcAlmActiveDescription_Type = DisplayString
_NtcAlmActiveDescription_Object = MibTableColumn
ntcAlmActiveDescription = _NtcAlmActiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 6),
    _NtcAlmActiveDescription_Type()
)
ntcAlmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveDescription.setStatus("current")


class _NtcAlmActiveProbableCause_Type(DisplayString):
    """Custom type ntcAlmActiveProbableCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmActiveProbableCause_Type.__name__ = "DisplayString"
_NtcAlmActiveProbableCause_Object = MibTableColumn
ntcAlmActiveProbableCause = _NtcAlmActiveProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 3, 1, 7),
    _NtcAlmActiveProbableCause_Type()
)
ntcAlmActiveProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmActiveProbableCause.setStatus("current")
_NtcAlmHistoryTable_Object = MibTable
ntcAlmHistoryTable = _NtcAlmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4)
)
if mibBuilder.loadTexts:
    ntcAlmHistoryTable.setStatus("current")
_NtcAlmHistoryEntry_Object = MibTableRow
ntcAlmHistoryEntry = _NtcAlmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1)
)
ntcAlmHistoryEntry.setIndexNames(
    (0, "NEWTEC-ALARM-MIB", "ntcAlmHistoryName"),
)
if mibBuilder.loadTexts:
    ntcAlmHistoryEntry.setStatus("current")


class _NtcAlmHistoryName_Type(DisplayString):
    """Custom type ntcAlmHistoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NtcAlmHistoryName_Type.__name__ = "DisplayString"
_NtcAlmHistoryName_Object = MibTableColumn
ntcAlmHistoryName = _NtcAlmHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 1),
    _NtcAlmHistoryName_Type()
)
ntcAlmHistoryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAlmHistoryName.setStatus("current")


class _NtcAlmHistorySeverity_Type(DisplayString):
    """Custom type ntcAlmHistorySeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcAlmHistorySeverity_Type.__name__ = "DisplayString"
_NtcAlmHistorySeverity_Object = MibTableColumn
ntcAlmHistorySeverity = _NtcAlmHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 2),
    _NtcAlmHistorySeverity_Type()
)
ntcAlmHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistorySeverity.setStatus("current")
_NtcAlmHistoryTime_Type = NtcSystemTime
_NtcAlmHistoryTime_Object = MibTableColumn
ntcAlmHistoryTime = _NtcAlmHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 3),
    _NtcAlmHistoryTime_Type()
)
ntcAlmHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistoryTime.setStatus("current")
_NtcAlmHistoryCount_Type = Counter32
_NtcAlmHistoryCount_Object = MibTableColumn
ntcAlmHistoryCount = _NtcAlmHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 4),
    _NtcAlmHistoryCount_Type()
)
ntcAlmHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistoryCount.setStatus("current")


class _NtcAlmHistorySource_Type(DisplayString):
    """Custom type ntcAlmHistorySource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmHistorySource_Type.__name__ = "DisplayString"
_NtcAlmHistorySource_Object = MibTableColumn
ntcAlmHistorySource = _NtcAlmHistorySource_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 5),
    _NtcAlmHistorySource_Type()
)
ntcAlmHistorySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistorySource.setStatus("current")
_NtcAlmHistoryDescription_Type = DisplayString
_NtcAlmHistoryDescription_Object = MibTableColumn
ntcAlmHistoryDescription = _NtcAlmHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 6),
    _NtcAlmHistoryDescription_Type()
)
ntcAlmHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistoryDescription.setStatus("current")


class _NtcAlmHistoryProbableCause_Type(DisplayString):
    """Custom type ntcAlmHistoryProbableCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmHistoryProbableCause_Type.__name__ = "DisplayString"
_NtcAlmHistoryProbableCause_Object = MibTableColumn
ntcAlmHistoryProbableCause = _NtcAlmHistoryProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 4, 1, 7),
    _NtcAlmHistoryProbableCause_Type()
)
ntcAlmHistoryProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmHistoryProbableCause.setStatus("current")
_NtcAlmLogTable_Object = MibTable
ntcAlmLogTable = _NtcAlmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5)
)
if mibBuilder.loadTexts:
    ntcAlmLogTable.setStatus("current")
_NtcAlmLogEntry_Object = MibTableRow
ntcAlmLogEntry = _NtcAlmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1)
)
ntcAlmLogEntry.setIndexNames(
    (0, "NEWTEC-ALARM-MIB", "ntcAlmLogLogIndex"),
)
if mibBuilder.loadTexts:
    ntcAlmLogEntry.setStatus("current")
_NtcAlmLogLogIndex_Type = Unsigned32
_NtcAlmLogLogIndex_Object = MibTableColumn
ntcAlmLogLogIndex = _NtcAlmLogLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 1),
    _NtcAlmLogLogIndex_Type()
)
ntcAlmLogLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAlmLogLogIndex.setStatus("current")


class _NtcAlmLogName_Type(DisplayString):
    """Custom type ntcAlmLogName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NtcAlmLogName_Type.__name__ = "DisplayString"
_NtcAlmLogName_Object = MibTableColumn
ntcAlmLogName = _NtcAlmLogName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 2),
    _NtcAlmLogName_Type()
)
ntcAlmLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogName.setStatus("current")
_NtcAlmLogState_Type = NtcAlarmState
_NtcAlmLogState_Object = MibTableColumn
ntcAlmLogState = _NtcAlmLogState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 3),
    _NtcAlmLogState_Type()
)
ntcAlmLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogState.setStatus("current")


class _NtcAlmLogSeverity_Type(DisplayString):
    """Custom type ntcAlmLogSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcAlmLogSeverity_Type.__name__ = "DisplayString"
_NtcAlmLogSeverity_Object = MibTableColumn
ntcAlmLogSeverity = _NtcAlmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 4),
    _NtcAlmLogSeverity_Type()
)
ntcAlmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogSeverity.setStatus("current")
_NtcAlmLogTime_Type = NtcSystemTime
_NtcAlmLogTime_Object = MibTableColumn
ntcAlmLogTime = _NtcAlmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 5),
    _NtcAlmLogTime_Type()
)
ntcAlmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogTime.setStatus("current")
_NtcAlmLogCount_Type = Counter32
_NtcAlmLogCount_Object = MibTableColumn
ntcAlmLogCount = _NtcAlmLogCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 6),
    _NtcAlmLogCount_Type()
)
ntcAlmLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogCount.setStatus("current")


class _NtcAlmLogSource_Type(DisplayString):
    """Custom type ntcAlmLogSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmLogSource_Type.__name__ = "DisplayString"
_NtcAlmLogSource_Object = MibTableColumn
ntcAlmLogSource = _NtcAlmLogSource_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 7),
    _NtcAlmLogSource_Type()
)
ntcAlmLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogSource.setStatus("current")
_NtcAlmLogDescription_Type = DisplayString
_NtcAlmLogDescription_Object = MibTableColumn
ntcAlmLogDescription = _NtcAlmLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 8),
    _NtcAlmLogDescription_Type()
)
ntcAlmLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogDescription.setStatus("current")


class _NtcAlmLogProbableCause_Type(DisplayString):
    """Custom type ntcAlmLogProbableCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtcAlmLogProbableCause_Type.__name__ = "DisplayString"
_NtcAlmLogProbableCause_Object = MibTableColumn
ntcAlmLogProbableCause = _NtcAlmLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 9),
    _NtcAlmLogProbableCause_Type()
)
ntcAlmLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogProbableCause.setStatus("current")
_NtcAlmLogSequenceNumber_Type = Counter32
_NtcAlmLogSequenceNumber_Object = MibTableColumn
ntcAlmLogSequenceNumber = _NtcAlmLogSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 1, 5, 1, 10),
    _NtcAlmLogSequenceNumber_Type()
)
ntcAlmLogSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlmLogSequenceNumber.setStatus("current")
_NtcAlmConformance_ObjectIdentity = ObjectIdentity
ntcAlmConformance = _NtcAlmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 2)
)
if mibBuilder.loadTexts:
    ntcAlmConformance.setStatus("current")
_NtcAlmConfCompliance_ObjectIdentity = ObjectIdentity
ntcAlmConfCompliance = _NtcAlmConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAlmConfCompliance.setStatus("current")
_NtcAlmConfGroup_ObjectIdentity = ObjectIdentity
ntcAlmConfGroup = _NtcAlmConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAlmConfGroup.setStatus("current")

# Managed Objects groups

ntcAlmConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 2, 2, 1)
)
ntcAlmConfGrpV1Standard.setObjects(
      *(("NEWTEC-ALARM-MIB", "ntcAlmReset"),
        ("NEWTEC-ALARM-MIB", "ntcAlmDefinitionSeverity"),
        ("NEWTEC-ALARM-MIB", "ntcAlmDefinitionDescription"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveSeverity"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveTime"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveCount"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveSource"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveDescription"),
        ("NEWTEC-ALARM-MIB", "ntcAlmActiveProbableCause"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistorySeverity"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistoryTime"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistoryCount"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistorySource"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistoryDescription"),
        ("NEWTEC-ALARM-MIB", "ntcAlmHistoryProbableCause"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogName"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogState"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogSeverity"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogTime"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogCount"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogSource"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogDescription"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogProbableCause"),
        ("NEWTEC-ALARM-MIB", "ntcAlmLogSequenceNumber"))
)
if mibBuilder.loadTexts:
    ntcAlmConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAlmConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 200, 2, 1, 1)
)
ntcAlmConfCompV1Standard.setObjects(
    ("NEWTEC-ALARM-MIB", "ntcAlmConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAlmConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ALARM-MIB",
    **{"ntcAlarm": ntcAlarm,
       "ntcAlmObjects": ntcAlmObjects,
       "ntcAlmReset": ntcAlmReset,
       "ntcAlmDefinitionTable": ntcAlmDefinitionTable,
       "ntcAlmDefinitionEntry": ntcAlmDefinitionEntry,
       "ntcAlmDefinitionName": ntcAlmDefinitionName,
       "ntcAlmDefinitionSeverity": ntcAlmDefinitionSeverity,
       "ntcAlmDefinitionDescription": ntcAlmDefinitionDescription,
       "ntcAlmActiveTable": ntcAlmActiveTable,
       "ntcAlmActiveEntry": ntcAlmActiveEntry,
       "ntcAlmActiveName": ntcAlmActiveName,
       "ntcAlmActiveSeverity": ntcAlmActiveSeverity,
       "ntcAlmActiveTime": ntcAlmActiveTime,
       "ntcAlmActiveCount": ntcAlmActiveCount,
       "ntcAlmActiveSource": ntcAlmActiveSource,
       "ntcAlmActiveDescription": ntcAlmActiveDescription,
       "ntcAlmActiveProbableCause": ntcAlmActiveProbableCause,
       "ntcAlmHistoryTable": ntcAlmHistoryTable,
       "ntcAlmHistoryEntry": ntcAlmHistoryEntry,
       "ntcAlmHistoryName": ntcAlmHistoryName,
       "ntcAlmHistorySeverity": ntcAlmHistorySeverity,
       "ntcAlmHistoryTime": ntcAlmHistoryTime,
       "ntcAlmHistoryCount": ntcAlmHistoryCount,
       "ntcAlmHistorySource": ntcAlmHistorySource,
       "ntcAlmHistoryDescription": ntcAlmHistoryDescription,
       "ntcAlmHistoryProbableCause": ntcAlmHistoryProbableCause,
       "ntcAlmLogTable": ntcAlmLogTable,
       "ntcAlmLogEntry": ntcAlmLogEntry,
       "ntcAlmLogLogIndex": ntcAlmLogLogIndex,
       "ntcAlmLogName": ntcAlmLogName,
       "ntcAlmLogState": ntcAlmLogState,
       "ntcAlmLogSeverity": ntcAlmLogSeverity,
       "ntcAlmLogTime": ntcAlmLogTime,
       "ntcAlmLogCount": ntcAlmLogCount,
       "ntcAlmLogSource": ntcAlmLogSource,
       "ntcAlmLogDescription": ntcAlmLogDescription,
       "ntcAlmLogProbableCause": ntcAlmLogProbableCause,
       "ntcAlmLogSequenceNumber": ntcAlmLogSequenceNumber,
       "ntcAlmConformance": ntcAlmConformance,
       "ntcAlmConfCompliance": ntcAlmConfCompliance,
       "ntcAlmConfCompV1Standard": ntcAlmConfCompV1Standard,
       "ntcAlmConfGroup": ntcAlmConfGroup,
       "ntcAlmConfGrpV1Standard": ntcAlmConfGrpV1Standard}
)
