# SNMP MIB module (RAISECOM-SYSLOG-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-SYSLOG-SERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:53 2025
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

(InetAddress,
 ModuleIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomSyslogService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



class LogFacility(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("kern", 1),
          ("user", 2),
          ("mail", 3),
          ("daemon", 4),
          ("auth", 5),
          ("syslog", 6),
          ("lpr", 7),
          ("news", 8),
          ("uucp", 9),
          ("cron", 10),
          ("security", 11),
          ("ftp", 12),
          ("ntp", 13),
          ("audit", 14),
          ("alert", 15),
          ("clock", 16),
          ("local0", 17),
          ("local1", 18),
          ("local2", 19),
          ("local3", 20),
          ("local4", 21),
          ("local5", 22),
          ("local6", 23),
          ("local7", 24))
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomSyslogMibObjects_ObjectIdentity = ObjectIdentity
raisecomSyslogMibObjects = _RaisecomSyslogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1)
)
_RaisecomLogBasic_ObjectIdentity = ObjectIdentity
raisecomLogBasic = _RaisecomLogBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1)
)
_RaisecomLogEnable_Type = EnableVar
_RaisecomLogEnable_Object = MibScalar
raisecomLogEnable = _RaisecomLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 1),
    _RaisecomLogEnable_Type()
)
raisecomLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogEnable.setStatus("current")


class _RaisecomLogRateLimit_Type(Integer32):
    """Custom type raisecomLogRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RaisecomLogRateLimit_Type.__name__ = "Integer32"
_RaisecomLogRateLimit_Object = MibScalar
raisecomLogRateLimit = _RaisecomLogRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 2),
    _RaisecomLogRateLimit_Type()
)
raisecomLogRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogRateLimit.setStatus("current")


class _RaisecomLogDropMessages_Type(Integer32):
    """Custom type raisecomLogDropMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaisecomLogDropMessages_Type.__name__ = "Integer32"
_RaisecomLogDropMessages_Object = MibScalar
raisecomLogDropMessages = _RaisecomLogDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 3),
    _RaisecomLogDropMessages_Type()
)
raisecomLogDropMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogDropMessages.setStatus("current")


class _RaisecomLogConsoleLogedMessages_Type(Integer32):
    """Custom type raisecomLogConsoleLogedMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaisecomLogConsoleLogedMessages_Type.__name__ = "Integer32"
_RaisecomLogConsoleLogedMessages_Object = MibScalar
raisecomLogConsoleLogedMessages = _RaisecomLogConsoleLogedMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 4),
    _RaisecomLogConsoleLogedMessages_Type()
)
raisecomLogConsoleLogedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogConsoleLogedMessages.setStatus("deprecated")


class _RaisecomLogMonitorMessages_Type(Integer32):
    """Custom type raisecomLogMonitorMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaisecomLogMonitorMessages_Type.__name__ = "Integer32"
_RaisecomLogMonitorMessages_Object = MibScalar
raisecomLogMonitorMessages = _RaisecomLogMonitorMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 5),
    _RaisecomLogMonitorMessages_Type()
)
raisecomLogMonitorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogMonitorMessages.setStatus("deprecated")


class _RaisecomLogTimeStamp_Type(Integer32):
    """Custom type raisecomLogTimeStamp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-timestamp", 1),
          ("date-timestamp", 2),
          ("up-timestamp", 3))
    )


_RaisecomLogTimeStamp_Type.__name__ = "Integer32"
_RaisecomLogTimeStamp_Object = MibScalar
raisecomLogTimeStamp = _RaisecomLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 6),
    _RaisecomLogTimeStamp_Type()
)
raisecomLogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogTimeStamp.setStatus("current")


class _RaisecomLogDebugTimeStamp_Type(Integer32):
    """Custom type raisecomLogDebugTimeStamp based on Integer32"""
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
        *(("no-timestamp", 1),
          ("date-timestamp", 2),
          ("up-timestamp", 3))
    )


_RaisecomLogDebugTimeStamp_Type.__name__ = "Integer32"
_RaisecomLogDebugTimeStamp_Object = MibScalar
raisecomLogDebugTimeStamp = _RaisecomLogDebugTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 7),
    _RaisecomLogDebugTimeStamp_Type()
)
raisecomLogDebugTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDebugTimeStamp.setStatus("current")
_RaisecomLogHistoryEnable_Type = EnableVar
_RaisecomLogHistoryEnable_Object = MibScalar
raisecomLogHistoryEnable = _RaisecomLogHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 8),
    _RaisecomLogHistoryEnable_Type()
)
raisecomLogHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogHistoryEnable.setStatus("current")


class _RaisecomLogHistorySize_Type(Integer32):
    """Custom type raisecomLogHistorySize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_RaisecomLogHistorySize_Type.__name__ = "Integer32"
_RaisecomLogHistorySize_Object = MibScalar
raisecomLogHistorySize = _RaisecomLogHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 9),
    _RaisecomLogHistorySize_Type()
)
raisecomLogHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogHistorySize.setStatus("current")


class _RaisecomLogBufferSize_Type(Integer32):
    """Custom type raisecomLogBufferSize based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 256),
    )


_RaisecomLogBufferSize_Type.__name__ = "Integer32"
_RaisecomLogBufferSize_Object = MibScalar
raisecomLogBufferSize = _RaisecomLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 10),
    _RaisecomLogBufferSize_Type()
)
raisecomLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogBufferSize.setStatus("current")
_RaisecomLogSequenceNumEnable_Type = EnableVar
_RaisecomLogSequenceNumEnable_Object = MibScalar
raisecomLogSequenceNumEnable = _RaisecomLogSequenceNumEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 11),
    _RaisecomLogSequenceNumEnable_Type()
)
raisecomLogSequenceNumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogSequenceNumEnable.setStatus("current")


class _RaisecomDebugModuleLevel_Type(Integer32):
    """Custom type raisecomDebugModuleLevel based on Integer32"""
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
        *(("none", 1),
          ("high", 2),
          ("normal", 3),
          ("low", 4))
    )


_RaisecomDebugModuleLevel_Type.__name__ = "Integer32"
_RaisecomDebugModuleLevel_Object = MibScalar
raisecomDebugModuleLevel = _RaisecomDebugModuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 12),
    _RaisecomDebugModuleLevel_Type()
)
raisecomDebugModuleLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDebugModuleLevel.setStatus("current")


class _RaisecomLogDebugDropMessages_Type(Integer32):
    """Custom type raisecomLogDebugDropMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaisecomLogDebugDropMessages_Type.__name__ = "Integer32"
_RaisecomLogDebugDropMessages_Object = MibScalar
raisecomLogDebugDropMessages = _RaisecomLogDebugDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 13),
    _RaisecomLogDebugDropMessages_Type()
)
raisecomLogDebugDropMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogDebugDropMessages.setStatus("current")
_RaisecomLogBufferClear_Type = TruthValue
_RaisecomLogBufferClear_Object = MibScalar
raisecomLogBufferClear = _RaisecomLogBufferClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 14),
    _RaisecomLogBufferClear_Type()
)
raisecomLogBufferClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogBufferClear.setStatus("current")
_RaisecomLogConfig_Type = EnableVar
_RaisecomLogConfig_Object = MibScalar
raisecomLogConfig = _RaisecomLogConfig_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 15),
    _RaisecomLogConfig_Type()
)
raisecomLogConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogConfig.setStatus("current")


class _RaisecomLogConfigLevel_Type(SyslogSeverity):
    """Custom type raisecomLogConfigLevel based on SyslogSeverity"""
    defaultValue = 7


_RaisecomLogConfigLevel_Type.__name__ = "SyslogSeverity"
_RaisecomLogConfigLevel_Object = MibScalar
raisecomLogConfigLevel = _RaisecomLogConfigLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 16),
    _RaisecomLogConfigLevel_Type()
)
raisecomLogConfigLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogConfigLevel.setStatus("current")
_RaisecomLogDestinationTable_Object = MibTable
raisecomLogDestinationTable = _RaisecomLogDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    raisecomLogDestinationTable.setStatus("current")
_RaisecomLogDestinationEntry_Object = MibTableRow
raisecomLogDestinationEntry = _RaisecomLogDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1)
)
raisecomLogDestinationEntry.setIndexNames(
    (0, "RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogDestIndex"),
)
if mibBuilder.loadTexts:
    raisecomLogDestinationEntry.setStatus("current")


class _RaisecomLogDestIndex_Type(Integer32):
    """Custom type raisecomLogDestIndex based on Integer32"""
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
        *(("buffer", 1),
          ("console", 2),
          ("trap", 3),
          ("file", 4))
    )


_RaisecomLogDestIndex_Type.__name__ = "Integer32"
_RaisecomLogDestIndex_Object = MibTableColumn
raisecomLogDestIndex = _RaisecomLogDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 1),
    _RaisecomLogDestIndex_Type()
)
raisecomLogDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomLogDestIndex.setStatus("current")
_RaisecomLogDestEnable_Type = EnableVar
_RaisecomLogDestEnable_Object = MibTableColumn
raisecomLogDestEnable = _RaisecomLogDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 2),
    _RaisecomLogDestEnable_Type()
)
raisecomLogDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDestEnable.setStatus("current")
_RaisecomLogDestServrity_Type = SyslogSeverity
_RaisecomLogDestServrity_Object = MibTableColumn
raisecomLogDestServrity = _RaisecomLogDestServrity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 3),
    _RaisecomLogDestServrity_Type()
)
raisecomLogDestServrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDestServrity.setStatus("current")


class _RaisecomLogDestDiscriminator_Type(Integer32):
    """Custom type raisecomLogDestDiscriminator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RaisecomLogDestDiscriminator_Type.__name__ = "Integer32"
_RaisecomLogDestDiscriminator_Object = MibTableColumn
raisecomLogDestDiscriminator = _RaisecomLogDestDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 4),
    _RaisecomLogDestDiscriminator_Type()
)
raisecomLogDestDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDestDiscriminator.setStatus("current")
_RaisecomLogDestLoggedMessages_Type = Integer32
_RaisecomLogDestLoggedMessages_Object = MibTableColumn
raisecomLogDestLoggedMessages = _RaisecomLogDestLoggedMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 5),
    _RaisecomLogDestLoggedMessages_Type()
)
raisecomLogDestLoggedMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDestLoggedMessages.setStatus("current")
_RaisecomLogDestDropMessages_Type = Integer32
_RaisecomLogDestDropMessages_Object = MibTableColumn
raisecomLogDestDropMessages = _RaisecomLogDestDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 17, 1, 6),
    _RaisecomLogDestDropMessages_Type()
)
raisecomLogDestDropMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDestDropMessages.setStatus("current")
_RaisecomLogDiscriminatorTable_Object = MibTable
raisecomLogDiscriminatorTable = _RaisecomLogDiscriminatorTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorTable.setStatus("current")
_RaisecomLogDiscriminatorEntry_Object = MibTableRow
raisecomLogDiscriminatorEntry = _RaisecomLogDiscriminatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1)
)
raisecomLogDiscriminatorEntry.setIndexNames(
    (0, "RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogDiscriminatorIndex"),
)
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorEntry.setStatus("current")


class _RaisecomLogDiscriminatorIndex_Type(Integer32):
    """Custom type raisecomLogDiscriminatorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RaisecomLogDiscriminatorIndex_Type.__name__ = "Integer32"
_RaisecomLogDiscriminatorIndex_Object = MibTableColumn
raisecomLogDiscriminatorIndex = _RaisecomLogDiscriminatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 1),
    _RaisecomLogDiscriminatorIndex_Type()
)
raisecomLogDiscriminatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorIndex.setStatus("current")


class _RaisecomLogDiscriminatorFacilityAct_Type(Integer32):
    """Custom type raisecomLogDiscriminatorFacilityAct based on Integer32"""
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
          ("drops", 2),
          ("includes", 3))
    )


_RaisecomLogDiscriminatorFacilityAct_Type.__name__ = "Integer32"
_RaisecomLogDiscriminatorFacilityAct_Object = MibTableColumn
raisecomLogDiscriminatorFacilityAct = _RaisecomLogDiscriminatorFacilityAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 2),
    _RaisecomLogDiscriminatorFacilityAct_Type()
)
raisecomLogDiscriminatorFacilityAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorFacilityAct.setStatus("current")


class _RaisecomLogDiscriminatorFacilityStr_Type(OctetString):
    """Custom type raisecomLogDiscriminatorFacilityStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RaisecomLogDiscriminatorFacilityStr_Type.__name__ = "OctetString"
_RaisecomLogDiscriminatorFacilityStr_Object = MibTableColumn
raisecomLogDiscriminatorFacilityStr = _RaisecomLogDiscriminatorFacilityStr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 3),
    _RaisecomLogDiscriminatorFacilityStr_Type()
)
raisecomLogDiscriminatorFacilityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorFacilityStr.setStatus("current")


class _RaisecomLogDiscriminatorMnemonicsAct_Type(Integer32):
    """Custom type raisecomLogDiscriminatorMnemonicsAct based on Integer32"""
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
          ("drops", 2),
          ("includes", 3))
    )


_RaisecomLogDiscriminatorMnemonicsAct_Type.__name__ = "Integer32"
_RaisecomLogDiscriminatorMnemonicsAct_Object = MibTableColumn
raisecomLogDiscriminatorMnemonicsAct = _RaisecomLogDiscriminatorMnemonicsAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 4),
    _RaisecomLogDiscriminatorMnemonicsAct_Type()
)
raisecomLogDiscriminatorMnemonicsAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorMnemonicsAct.setStatus("current")


class _RaisecomLogDiscriminatorMnemonicsStr_Type(OctetString):
    """Custom type raisecomLogDiscriminatorMnemonicsStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RaisecomLogDiscriminatorMnemonicsStr_Type.__name__ = "OctetString"
_RaisecomLogDiscriminatorMnemonicsStr_Object = MibTableColumn
raisecomLogDiscriminatorMnemonicsStr = _RaisecomLogDiscriminatorMnemonicsStr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 5),
    _RaisecomLogDiscriminatorMnemonicsStr_Type()
)
raisecomLogDiscriminatorMnemonicsStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorMnemonicsStr.setStatus("current")


class _RaisecomLogDiscriminatorMsgbodyAct_Type(Integer32):
    """Custom type raisecomLogDiscriminatorMsgbodyAct based on Integer32"""
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
          ("drops", 2),
          ("includes", 3))
    )


_RaisecomLogDiscriminatorMsgbodyAct_Type.__name__ = "Integer32"
_RaisecomLogDiscriminatorMsgbodyAct_Object = MibTableColumn
raisecomLogDiscriminatorMsgbodyAct = _RaisecomLogDiscriminatorMsgbodyAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 6),
    _RaisecomLogDiscriminatorMsgbodyAct_Type()
)
raisecomLogDiscriminatorMsgbodyAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorMsgbodyAct.setStatus("current")


class _RaisecomLogDiscriminatorMsgbodyStr_Type(OctetString):
    """Custom type raisecomLogDiscriminatorMsgbodyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RaisecomLogDiscriminatorMsgbodyStr_Type.__name__ = "OctetString"
_RaisecomLogDiscriminatorMsgbodyStr_Object = MibTableColumn
raisecomLogDiscriminatorMsgbodyStr = _RaisecomLogDiscriminatorMsgbodyStr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 18, 1, 7),
    _RaisecomLogDiscriminatorMsgbodyStr_Type()
)
raisecomLogDiscriminatorMsgbodyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomLogDiscriminatorMsgbodyStr.setStatus("current")
_RaisecomLogHistoryTable_Object = MibTable
raisecomLogHistoryTable = _RaisecomLogHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    raisecomLogHistoryTable.setStatus("current")
_RaisecomLogHistoryEntry_Object = MibTableRow
raisecomLogHistoryEntry = _RaisecomLogHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1)
)
raisecomLogHistoryEntry.setIndexNames(
    (0, "RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistIndex"),
)
if mibBuilder.loadTexts:
    raisecomLogHistoryEntry.setStatus("current")
_RaisecomLogHistIndex_Type = Integer32
_RaisecomLogHistIndex_Object = MibTableColumn
raisecomLogHistIndex = _RaisecomLogHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 1),
    _RaisecomLogHistIndex_Type()
)
raisecomLogHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomLogHistIndex.setStatus("current")


class _RaisecomLogHistFacility_Type(OctetString):
    """Custom type raisecomLogHistFacility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RaisecomLogHistFacility_Type.__name__ = "OctetString"
_RaisecomLogHistFacility_Object = MibTableColumn
raisecomLogHistFacility = _RaisecomLogHistFacility_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 2),
    _RaisecomLogHistFacility_Type()
)
raisecomLogHistFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogHistFacility.setStatus("current")
_RaisecomLogHistSeverity_Type = SyslogSeverity
_RaisecomLogHistSeverity_Object = MibTableColumn
raisecomLogHistSeverity = _RaisecomLogHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 3),
    _RaisecomLogHistSeverity_Type()
)
raisecomLogHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogHistSeverity.setStatus("current")


class _RaisecomLogHistMnemonics_Type(OctetString):
    """Custom type raisecomLogHistMnemonics based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RaisecomLogHistMnemonics_Type.__name__ = "OctetString"
_RaisecomLogHistMnemonics_Object = MibTableColumn
raisecomLogHistMnemonics = _RaisecomLogHistMnemonics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 4),
    _RaisecomLogHistMnemonics_Type()
)
raisecomLogHistMnemonics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogHistMnemonics.setStatus("current")


class _RaisecomLogHistMsgbody_Type(OctetString):
    """Custom type raisecomLogHistMsgbody based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RaisecomLogHistMsgbody_Type.__name__ = "OctetString"
_RaisecomLogHistMsgbody_Object = MibTableColumn
raisecomLogHistMsgbody = _RaisecomLogHistMsgbody_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 5),
    _RaisecomLogHistMsgbody_Type()
)
raisecomLogHistMsgbody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogHistMsgbody.setStatus("current")
_RaisecomLogHistTimestamp_Type = Integer32
_RaisecomLogHistTimestamp_Object = MibTableColumn
raisecomLogHistTimestamp = _RaisecomLogHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 1, 19, 1, 6),
    _RaisecomLogHistTimestamp_Type()
)
raisecomLogHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogHistTimestamp.setStatus("current")
_RaisecomLogServer_ObjectIdentity = ObjectIdentity
raisecomLogServer = _RaisecomLogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2)
)
_RaisecomLogMaxNumberOfLogServer_Type = Integer32
_RaisecomLogMaxNumberOfLogServer_Object = MibScalar
raisecomLogMaxNumberOfLogServer = _RaisecomLogMaxNumberOfLogServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 1),
    _RaisecomLogMaxNumberOfLogServer_Type()
)
raisecomLogMaxNumberOfLogServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogMaxNumberOfLogServer.setStatus("current")
_RaisecomLogServerNumber_Type = Integer32
_RaisecomLogServerNumber_Object = MibScalar
raisecomLogServerNumber = _RaisecomLogServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 2),
    _RaisecomLogServerNumber_Type()
)
raisecomLogServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogServerNumber.setStatus("current")
_RaisecomLogServerTable_Object = MibTable
raisecomLogServerTable = _RaisecomLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomLogServerTable.setStatus("current")
_RaisecomLogServerEntry_Object = MibTableRow
raisecomLogServerEntry = _RaisecomLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1)
)
raisecomLogServerEntry.setIndexNames(
    (0, "RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogServerIpAddress"),
)
if mibBuilder.loadTexts:
    raisecomLogServerEntry.setStatus("current")
_RaisecomLogServerIpAddress_Type = InetAddress
_RaisecomLogServerIpAddress_Object = MibTableColumn
raisecomLogServerIpAddress = _RaisecomLogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 1),
    _RaisecomLogServerIpAddress_Type()
)
raisecomLogServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomLogServerIpAddress.setStatus("current")


class _RaisecomLogServerPort_Type(Integer32):
    """Custom type raisecomLogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaisecomLogServerPort_Type.__name__ = "Integer32"
_RaisecomLogServerPort_Object = MibTableColumn
raisecomLogServerPort = _RaisecomLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 2),
    _RaisecomLogServerPort_Type()
)
raisecomLogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogServerPort.setStatus("current")
_RaisecomLogFacility_Type = LogFacility
_RaisecomLogFacility_Object = MibTableColumn
raisecomLogFacility = _RaisecomLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 3),
    _RaisecomLogFacility_Type()
)
raisecomLogFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomLogFacility.setStatus("current")
_RaisecomLogServerMaxSeverity_Type = SyslogSeverity
_RaisecomLogServerMaxSeverity_Object = MibTableColumn
raisecomLogServerMaxSeverity = _RaisecomLogServerMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 4),
    _RaisecomLogServerMaxSeverity_Type()
)
raisecomLogServerMaxSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomLogServerMaxSeverity.setStatus("current")
_RaisecomLogServerRowStatus_Type = RowStatus
_RaisecomLogServerRowStatus_Object = MibTableColumn
raisecomLogServerRowStatus = _RaisecomLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 5),
    _RaisecomLogServerRowStatus_Type()
)
raisecomLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomLogServerRowStatus.setStatus("current")
_RaisecomLogServerLoggedMessages_Type = Integer32
_RaisecomLogServerLoggedMessages_Object = MibTableColumn
raisecomLogServerLoggedMessages = _RaisecomLogServerLoggedMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 6),
    _RaisecomLogServerLoggedMessages_Type()
)
raisecomLogServerLoggedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogServerLoggedMessages.setStatus("current")
_RaisecomLogServerDropMessages_Type = Integer32
_RaisecomLogServerDropMessages_Object = MibTableColumn
raisecomLogServerDropMessages = _RaisecomLogServerDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 7),
    _RaisecomLogServerDropMessages_Type()
)
raisecomLogServerDropMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomLogServerDropMessages.setStatus("current")
_RaisecomLogServerDiscriminator_Type = Integer32
_RaisecomLogServerDiscriminator_Object = MibTableColumn
raisecomLogServerDiscriminator = _RaisecomLogServerDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 2, 3, 1, 8),
    _RaisecomLogServerDiscriminator_Type()
)
raisecomLogServerDiscriminator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomLogServerDiscriminator.setStatus("current")
_RaisecomDebug_ObjectIdentity = ObjectIdentity
raisecomDebug = _RaisecomDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3)
)
_RaisecomDebugTable_Object = MibTable
raisecomDebugTable = _RaisecomDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomDebugTable.setStatus("current")
_RaisecomDebugEntry_Object = MibTableRow
raisecomDebugEntry = _RaisecomDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1, 1)
)
raisecomDebugEntry.setIndexNames(
    (0, "RAISECOM-SYSLOG-SERVICE-MIB", "raisecomDebugIndex"),
)
if mibBuilder.loadTexts:
    raisecomDebugEntry.setStatus("current")
_RaisecomDebugIndex_Type = Integer32
_RaisecomDebugIndex_Object = MibTableColumn
raisecomDebugIndex = _RaisecomDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1, 1, 1),
    _RaisecomDebugIndex_Type()
)
raisecomDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomDebugIndex.setStatus("current")


class _RaisecomDebugModuleName_Type(OctetString):
    """Custom type raisecomDebugModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RaisecomDebugModuleName_Type.__name__ = "OctetString"
_RaisecomDebugModuleName_Object = MibTableColumn
raisecomDebugModuleName = _RaisecomDebugModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1, 1, 2),
    _RaisecomDebugModuleName_Type()
)
raisecomDebugModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDebugModuleName.setStatus("current")
_RaisecomDebugModuleEnable_Type = EnableVar
_RaisecomDebugModuleEnable_Object = MibTableColumn
raisecomDebugModuleEnable = _RaisecomDebugModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1, 1, 3),
    _RaisecomDebugModuleEnable_Type()
)
raisecomDebugModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDebugModuleEnable.setStatus("current")


class _RaisecomDebugMsgName_Type(OctetString):
    """Custom type raisecomDebugMsgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RaisecomDebugMsgName_Type.__name__ = "OctetString"
_RaisecomDebugMsgName_Object = MibTableColumn
raisecomDebugMsgName = _RaisecomDebugMsgName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 3, 1, 1, 4),
    _RaisecomDebugMsgName_Type()
)
raisecomDebugMsgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDebugMsgName.setStatus("current")
_RaisecomLogTrapGroup_ObjectIdentity = ObjectIdentity
raisecomLogTrapGroup = _RaisecomLogTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 4)
)

# Managed Objects groups


# Notification objects

raisecomLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 4, 1, 4, 1)
)
raisecomLogTrap.setObjects(
      *(("RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistFacility"),
        ("RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistSeverity"),
        ("RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistMnemonics"),
        ("RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistMsgbody"),
        ("RAISECOM-SYSLOG-SERVICE-MIB", "raisecomLogHistTimestamp"))
)
if mibBuilder.loadTexts:
    raisecomLogTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-SYSLOG-SERVICE-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "LogFacility": LogFacility,
       "raisecomSyslogService": raisecomSyslogService,
       "raisecomSyslogMibObjects": raisecomSyslogMibObjects,
       "raisecomLogBasic": raisecomLogBasic,
       "raisecomLogEnable": raisecomLogEnable,
       "raisecomLogRateLimit": raisecomLogRateLimit,
       "raisecomLogDropMessages": raisecomLogDropMessages,
       "raisecomLogConsoleLogedMessages": raisecomLogConsoleLogedMessages,
       "raisecomLogMonitorMessages": raisecomLogMonitorMessages,
       "raisecomLogTimeStamp": raisecomLogTimeStamp,
       "raisecomLogDebugTimeStamp": raisecomLogDebugTimeStamp,
       "raisecomLogHistoryEnable": raisecomLogHistoryEnable,
       "raisecomLogHistorySize": raisecomLogHistorySize,
       "raisecomLogBufferSize": raisecomLogBufferSize,
       "raisecomLogSequenceNumEnable": raisecomLogSequenceNumEnable,
       "raisecomDebugModuleLevel": raisecomDebugModuleLevel,
       "raisecomLogDebugDropMessages": raisecomLogDebugDropMessages,
       "raisecomLogBufferClear": raisecomLogBufferClear,
       "raisecomLogConfig": raisecomLogConfig,
       "raisecomLogConfigLevel": raisecomLogConfigLevel,
       "raisecomLogDestinationTable": raisecomLogDestinationTable,
       "raisecomLogDestinationEntry": raisecomLogDestinationEntry,
       "raisecomLogDestIndex": raisecomLogDestIndex,
       "raisecomLogDestEnable": raisecomLogDestEnable,
       "raisecomLogDestServrity": raisecomLogDestServrity,
       "raisecomLogDestDiscriminator": raisecomLogDestDiscriminator,
       "raisecomLogDestLoggedMessages": raisecomLogDestLoggedMessages,
       "raisecomLogDestDropMessages": raisecomLogDestDropMessages,
       "raisecomLogDiscriminatorTable": raisecomLogDiscriminatorTable,
       "raisecomLogDiscriminatorEntry": raisecomLogDiscriminatorEntry,
       "raisecomLogDiscriminatorIndex": raisecomLogDiscriminatorIndex,
       "raisecomLogDiscriminatorFacilityAct": raisecomLogDiscriminatorFacilityAct,
       "raisecomLogDiscriminatorFacilityStr": raisecomLogDiscriminatorFacilityStr,
       "raisecomLogDiscriminatorMnemonicsAct": raisecomLogDiscriminatorMnemonicsAct,
       "raisecomLogDiscriminatorMnemonicsStr": raisecomLogDiscriminatorMnemonicsStr,
       "raisecomLogDiscriminatorMsgbodyAct": raisecomLogDiscriminatorMsgbodyAct,
       "raisecomLogDiscriminatorMsgbodyStr": raisecomLogDiscriminatorMsgbodyStr,
       "raisecomLogHistoryTable": raisecomLogHistoryTable,
       "raisecomLogHistoryEntry": raisecomLogHistoryEntry,
       "raisecomLogHistIndex": raisecomLogHistIndex,
       "raisecomLogHistFacility": raisecomLogHistFacility,
       "raisecomLogHistSeverity": raisecomLogHistSeverity,
       "raisecomLogHistMnemonics": raisecomLogHistMnemonics,
       "raisecomLogHistMsgbody": raisecomLogHistMsgbody,
       "raisecomLogHistTimestamp": raisecomLogHistTimestamp,
       "raisecomLogServer": raisecomLogServer,
       "raisecomLogMaxNumberOfLogServer": raisecomLogMaxNumberOfLogServer,
       "raisecomLogServerNumber": raisecomLogServerNumber,
       "raisecomLogServerTable": raisecomLogServerTable,
       "raisecomLogServerEntry": raisecomLogServerEntry,
       "raisecomLogServerIpAddress": raisecomLogServerIpAddress,
       "raisecomLogServerPort": raisecomLogServerPort,
       "raisecomLogFacility": raisecomLogFacility,
       "raisecomLogServerMaxSeverity": raisecomLogServerMaxSeverity,
       "raisecomLogServerRowStatus": raisecomLogServerRowStatus,
       "raisecomLogServerLoggedMessages": raisecomLogServerLoggedMessages,
       "raisecomLogServerDropMessages": raisecomLogServerDropMessages,
       "raisecomLogServerDiscriminator": raisecomLogServerDiscriminator,
       "raisecomDebug": raisecomDebug,
       "raisecomDebugTable": raisecomDebugTable,
       "raisecomDebugEntry": raisecomDebugEntry,
       "raisecomDebugIndex": raisecomDebugIndex,
       "raisecomDebugModuleName": raisecomDebugModuleName,
       "raisecomDebugModuleEnable": raisecomDebugModuleEnable,
       "raisecomDebugMsgName": raisecomDebugMsgName,
       "raisecomLogTrapGroup": raisecomLogTrapGroup,
       "raisecomLogTrap": raisecomLogTrap}
)
