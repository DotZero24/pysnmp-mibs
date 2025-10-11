# SNMP MIB module (FS-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-LOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:51 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    fsLogMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LogSeverity(TextualConvention, Integer32):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )



class LogTimeStamp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("datetime", 2),
          ("uptime", 3))
    )



class LogSyslogFacility(TextualConvention, Integer32):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("system", 3),
          ("security", 4),
          ("syslogd", 5),
          ("lineprinter", 6),
          ("network", 7),
          ("uUCP", 8),
          ("clockdaemon", 9),
          ("authorization", 10),
          ("fTP", 11),
          ("nTP", 12),
          ("logaudit", 13),
          ("logalert", 14),
          ("clockdaemon2", 15),
          ("localuse0", 16),
          ("localuse1", 17),
          ("localuse2", 18),
          ("localuse3", 19),
          ("localuse4", 20),
          ("localuse5", 21),
          ("localuse6", 22),
          ("localuse7", 23))
    )



# MIB Managed Objects in the order of their OIDs

_FsLogMIBObjects_ObjectIdentity = ObjectIdentity
fsLogMIBObjects = _FsLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1)
)


class _FsLogGlobalStatus_Type(EnabledStatus):
    """Custom type fsLogGlobalStatus based on EnabledStatus"""
    defaultValue = 1


_FsLogGlobalStatus_Type.__name__ = "EnabledStatus"
_FsLogGlobalStatus_Object = MibScalar
fsLogGlobalStatus = _FsLogGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 1),
    _FsLogGlobalStatus_Type()
)
fsLogGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogGlobalStatus.setStatus("current")


class _FsLogSendConsoleStatus_Type(EnabledStatus):
    """Custom type fsLogSendConsoleStatus based on EnabledStatus"""
    defaultValue = 1


_FsLogSendConsoleStatus_Type.__name__ = "EnabledStatus"
_FsLogSendConsoleStatus_Object = MibScalar
fsLogSendConsoleStatus = _FsLogSendConsoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 2),
    _FsLogSendConsoleStatus_Type()
)
fsLogSendConsoleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendConsoleStatus.setStatus("current")


class _FsLogSendConsoleMaxSeverity_Type(LogSeverity):
    """Custom type fsLogSendConsoleMaxSeverity based on LogSeverity"""
    defaultValue = 7


_FsLogSendConsoleMaxSeverity_Type.__name__ = "LogSeverity"
_FsLogSendConsoleMaxSeverity_Object = MibScalar
fsLogSendConsoleMaxSeverity = _FsLogSendConsoleMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 3),
    _FsLogSendConsoleMaxSeverity_Type()
)
fsLogSendConsoleMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendConsoleMaxSeverity.setStatus("current")


class _FsLogSendMonitorStatus_Type(EnabledStatus):
    """Custom type fsLogSendMonitorStatus based on EnabledStatus"""
    defaultValue = 2


_FsLogSendMonitorStatus_Type.__name__ = "EnabledStatus"
_FsLogSendMonitorStatus_Object = MibScalar
fsLogSendMonitorStatus = _FsLogSendMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 4),
    _FsLogSendMonitorStatus_Type()
)
fsLogSendMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendMonitorStatus.setStatus("current")


class _FsLogSendMonitorMaxSeverity_Type(LogSeverity):
    """Custom type fsLogSendMonitorMaxSeverity based on LogSeverity"""
    defaultValue = 7


_FsLogSendMonitorMaxSeverity_Type.__name__ = "LogSeverity"
_FsLogSendMonitorMaxSeverity_Object = MibScalar
fsLogSendMonitorMaxSeverity = _FsLogSendMonitorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 5),
    _FsLogSendMonitorMaxSeverity_Type()
)
fsLogSendMonitorMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendMonitorMaxSeverity.setStatus("current")


class _FsLogSaveFileName_Type(DisplayString):
    """Custom type fsLogSaveFileName based on DisplayString"""
    defaultValue = OctetString("")


_FsLogSaveFileName_Type.__name__ = "DisplayString"
_FsLogSaveFileName_Object = MibScalar
fsLogSaveFileName = _FsLogSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 6),
    _FsLogSaveFileName_Type()
)
fsLogSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSaveFileName.setStatus("current")


class _FsLogFileMaxSeverity_Type(LogSeverity):
    """Custom type fsLogFileMaxSeverity based on LogSeverity"""
    defaultValue = 5


_FsLogFileMaxSeverity_Type.__name__ = "LogSeverity"
_FsLogFileMaxSeverity_Object = MibScalar
fsLogFileMaxSeverity = _FsLogFileMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 7),
    _FsLogFileMaxSeverity_Type()
)
fsLogFileMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogFileMaxSeverity.setStatus("current")


class _FsLogFileMaxSize_Type(Integer32):
    """Custom type fsLogFileMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 2000000),
    )


_FsLogFileMaxSize_Type.__name__ = "Integer32"
_FsLogFileMaxSize_Object = MibScalar
fsLogFileMaxSize = _FsLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 8),
    _FsLogFileMaxSize_Type()
)
fsLogFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogFileMaxSize.setStatus("current")


class _FsLogSendBufferStatus_Type(EnabledStatus):
    """Custom type fsLogSendBufferStatus based on EnabledStatus"""
    defaultValue = 1


_FsLogSendBufferStatus_Type.__name__ = "EnabledStatus"
_FsLogSendBufferStatus_Object = MibScalar
fsLogSendBufferStatus = _FsLogSendBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 9),
    _FsLogSendBufferStatus_Type()
)
fsLogSendBufferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendBufferStatus.setStatus("current")


class _FsLogSendBufferMaxSeverity_Type(LogSeverity):
    """Custom type fsLogSendBufferMaxSeverity based on LogSeverity"""
    defaultValue = 7


_FsLogSendBufferMaxSeverity_Type.__name__ = "LogSeverity"
_FsLogSendBufferMaxSeverity_Object = MibScalar
fsLogSendBufferMaxSeverity = _FsLogSendBufferMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 10),
    _FsLogSendBufferMaxSeverity_Type()
)
fsLogSendBufferMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSendBufferMaxSeverity.setStatus("current")
_FsLogClearBuffer_Type = Integer32
_FsLogClearBuffer_Object = MibScalar
fsLogClearBuffer = _FsLogClearBuffer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 11),
    _FsLogClearBuffer_Type()
)
fsLogClearBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogClearBuffer.setStatus("current")
_FsLogHisRecordMaxNum_Type = Integer32
_FsLogHisRecordMaxNum_Object = MibScalar
fsLogHisRecordMaxNum = _FsLogHisRecordMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 12),
    _FsLogHisRecordMaxNum_Type()
)
fsLogHisRecordMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisRecordMaxNum.setStatus("current")
_FsLogHisTable_Object = MibTable
fsLogHisTable = _FsLogHisTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    fsLogHisTable.setStatus("current")
_FsLogHisEntry_Object = MibTableRow
fsLogHisEntry = _FsLogHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1)
)
fsLogHisEntry.setIndexNames(
    (0, "FS-LOG-MIB", "fsLogHisIndex"),
)
if mibBuilder.loadTexts:
    fsLogHisEntry.setStatus("current")
_FsLogHisIndex_Type = Integer32
_FsLogHisIndex_Object = MibTableColumn
fsLogHisIndex = _FsLogHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 1),
    _FsLogHisIndex_Type()
)
fsLogHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisIndex.setStatus("current")
_FsLogHisSeverity_Type = LogSeverity
_FsLogHisSeverity_Object = MibTableColumn
fsLogHisSeverity = _FsLogHisSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 2),
    _FsLogHisSeverity_Type()
)
fsLogHisSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisSeverity.setStatus("current")


class _FsLogHisMsgName_Type(DisplayString):
    """Custom type fsLogHisMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_FsLogHisMsgName_Type.__name__ = "DisplayString"
_FsLogHisMsgName_Object = MibTableColumn
fsLogHisMsgName = _FsLogHisMsgName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 3),
    _FsLogHisMsgName_Type()
)
fsLogHisMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisMsgName.setStatus("current")


class _FsLogHisDescription_Type(DisplayString):
    """Custom type fsLogHisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_FsLogHisDescription_Type.__name__ = "DisplayString"
_FsLogHisDescription_Object = MibTableColumn
fsLogHisDescription = _FsLogHisDescription_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 4),
    _FsLogHisDescription_Type()
)
fsLogHisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisDescription.setStatus("current")
_FsLogHisTime_Type = DateAndTime
_FsLogHisTime_Object = MibTableColumn
fsLogHisTime = _FsLogHisTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 5),
    _FsLogHisTime_Type()
)
fsLogHisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisTime.setStatus("current")
_FsLogHisStamps_Type = TimeStamp
_FsLogHisStamps_Object = MibTableColumn
fsLogHisStamps = _FsLogHisStamps_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 13, 1, 6),
    _FsLogHisStamps_Type()
)
fsLogHisStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogHisStamps.setStatus("current")


class _FsLogSequenceGlobalStatus_Type(EnabledStatus):
    """Custom type fsLogSequenceGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_FsLogSequenceGlobalStatus_Type.__name__ = "EnabledStatus"
_FsLogSequenceGlobalStatus_Object = MibScalar
fsLogSequenceGlobalStatus = _FsLogSequenceGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 14),
    _FsLogSequenceGlobalStatus_Type()
)
fsLogSequenceGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSequenceGlobalStatus.setStatus("current")


class _FsLogTimeStampGlobalStatus_Type(LogTimeStamp):
    """Custom type fsLogTimeStampGlobalStatus based on LogTimeStamp"""
    defaultValue = 2


_FsLogTimeStampGlobalStatus_Type.__name__ = "LogTimeStamp"
_FsLogTimeStampGlobalStatus_Object = MibScalar
fsLogTimeStampGlobalStatus = _FsLogTimeStampGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 15),
    _FsLogTimeStampGlobalStatus_Type()
)
fsLogTimeStampGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogTimeStampGlobalStatus.setStatus("current")


class _FsLogSyslogRelayGlobalStatus_Type(EnabledStatus):
    """Custom type fsLogSyslogRelayGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_FsLogSyslogRelayGlobalStatus_Type.__name__ = "EnabledStatus"
_FsLogSyslogRelayGlobalStatus_Object = MibScalar
fsLogSyslogRelayGlobalStatus = _FsLogSyslogRelayGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 16),
    _FsLogSyslogRelayGlobalStatus_Type()
)
fsLogSyslogRelayGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogRelayGlobalStatus.setStatus("current")


class _FsLogSyslogFacility_Type(LogSyslogFacility):
    """Custom type fsLogSyslogFacility based on LogSyslogFacility"""
    defaultValue = 23


_FsLogSyslogFacility_Type.__name__ = "LogSyslogFacility"
_FsLogSyslogFacility_Object = MibScalar
fsLogSyslogFacility = _FsLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 17),
    _FsLogSyslogFacility_Type()
)
fsLogSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogFacility.setStatus("current")


class _FsLogSyslogSeverity_Type(LogSeverity):
    """Custom type fsLogSyslogSeverity based on LogSeverity"""
    defaultValue = 7


_FsLogSyslogSeverity_Type.__name__ = "LogSeverity"
_FsLogSyslogSeverity_Object = MibScalar
fsLogSyslogSeverity = _FsLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 18),
    _FsLogSyslogSeverity_Type()
)
fsLogSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogSeverity.setStatus("current")
_FsLogSyslogServerTable_Object = MibTable
fsLogSyslogServerTable = _FsLogSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 19)
)
if mibBuilder.loadTexts:
    fsLogSyslogServerTable.setStatus("current")
_FsLogSyslogServerEntry_Object = MibTableRow
fsLogSyslogServerEntry = _FsLogSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 19, 1)
)
fsLogSyslogServerEntry.setIndexNames(
    (0, "FS-LOG-MIB", "fsLogSyslogServerIpAddr"),
)
if mibBuilder.loadTexts:
    fsLogSyslogServerEntry.setStatus("current")
_FsLogSyslogServerIpAddr_Type = IpAddress
_FsLogSyslogServerIpAddr_Object = MibTableColumn
fsLogSyslogServerIpAddr = _FsLogSyslogServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 19, 1, 1),
    _FsLogSyslogServerIpAddr_Type()
)
fsLogSyslogServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLogSyslogServerIpAddr.setStatus("current")
_FsLogSyslogServerIpStatus_Type = ConfigStatus
_FsLogSyslogServerIpStatus_Object = MibTableColumn
fsLogSyslogServerIpStatus = _FsLogSyslogServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 19, 1, 2),
    _FsLogSyslogServerIpStatus_Type()
)
fsLogSyslogServerIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogServerIpStatus.setStatus("current")
_FsLogSyslogSendSrcIfindex_Type = IfIndex
_FsLogSyslogSendSrcIfindex_Object = MibScalar
fsLogSyslogSendSrcIfindex = _FsLogSyslogSendSrcIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 20),
    _FsLogSyslogSendSrcIfindex_Type()
)
fsLogSyslogSendSrcIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogSendSrcIfindex.setStatus("current")
_FsLogSyslogSendSrcIp_Type = IpAddress
_FsLogSyslogSendSrcIp_Object = MibScalar
fsLogSyslogSendSrcIp = _FsLogSyslogSendSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 1, 21),
    _FsLogSyslogSendSrcIp_Type()
)
fsLogSyslogSendSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLogSyslogSendSrcIp.setStatus("current")
_FsLogMIBConformance_ObjectIdentity = ObjectIdentity
fsLogMIBConformance = _FsLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4)
)
_FsLogMIBCompliances_ObjectIdentity = ObjectIdentity
fsLogMIBCompliances = _FsLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4, 1)
)
_FsLogMIBGroups_ObjectIdentity = ObjectIdentity
fsLogMIBGroups = _FsLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4, 2)
)

# Managed Objects groups

fsLogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4, 2, 1)
)
fsLogMIBGroup.setObjects(
      *(("FS-LOG-MIB", "fsLogGlobalStatus"),
        ("FS-LOG-MIB", "fsLogSendConsoleStatus"),
        ("FS-LOG-MIB", "fsLogSendConsoleMaxSeverity"),
        ("FS-LOG-MIB", "fsLogSendMonitorStatus"),
        ("FS-LOG-MIB", "fsLogSendMonitorMaxSeverity"),
        ("FS-LOG-MIB", "fsLogSaveFileName"),
        ("FS-LOG-MIB", "fsLogFileMaxSeverity"),
        ("FS-LOG-MIB", "fsLogFileMaxSize"),
        ("FS-LOG-MIB", "fsLogSendBufferStatus"),
        ("FS-LOG-MIB", "fsLogSendBufferMaxSeverity"),
        ("FS-LOG-MIB", "fsLogClearBuffer"),
        ("FS-LOG-MIB", "fsLogHisRecordMaxNum"),
        ("FS-LOG-MIB", "fsLogHisIndex"),
        ("FS-LOG-MIB", "fsLogHisSeverity"),
        ("FS-LOG-MIB", "fsLogHisMsgName"),
        ("FS-LOG-MIB", "fsLogHisDescription"),
        ("FS-LOG-MIB", "fsLogHisTime"),
        ("FS-LOG-MIB", "fsLogSequenceGlobalStatus"),
        ("FS-LOG-MIB", "fsLogTimeStampGlobalStatus"),
        ("FS-LOG-MIB", "fsLogSyslogRelayGlobalStatus"),
        ("FS-LOG-MIB", "fsLogSyslogFacility"),
        ("FS-LOG-MIB", "fsLogSyslogSeverity"),
        ("FS-LOG-MIB", "fsLogSyslogServerIpAddr"),
        ("FS-LOG-MIB", "fsLogSyslogServerIpStatus"),
        ("FS-LOG-MIB", "fsLogSyslogSendSrcIfindex"),
        ("FS-LOG-MIB", "fsLogSyslogSendSrcIp"))
)
if mibBuilder.loadTexts:
    fsLogMIBGroup.setStatus("current")

fsLogHisStampsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4, 2, 2)
)
fsLogHisStampsMIBGroup.setObjects(
    ("FS-LOG-MIB", "fsLogHisStamps")
)
if mibBuilder.loadTexts:
    fsLogHisStampsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 4, 4, 1, 1)
)
fsLogMIBCompliance.setObjects(
      *(("FS-LOG-MIB", "fsLogMIBGroup"),
        ("FS-LOG-MIB", "fsLogHisStampsMIBGroup"))
)
if mibBuilder.loadTexts:
    fsLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-LOG-MIB",
    **{"LogSeverity": LogSeverity,
       "LogTimeStamp": LogTimeStamp,
       "LogSyslogFacility": LogSyslogFacility,
       "fsLogMIB": fsLogMIB,
       "fsLogMIBObjects": fsLogMIBObjects,
       "fsLogGlobalStatus": fsLogGlobalStatus,
       "fsLogSendConsoleStatus": fsLogSendConsoleStatus,
       "fsLogSendConsoleMaxSeverity": fsLogSendConsoleMaxSeverity,
       "fsLogSendMonitorStatus": fsLogSendMonitorStatus,
       "fsLogSendMonitorMaxSeverity": fsLogSendMonitorMaxSeverity,
       "fsLogSaveFileName": fsLogSaveFileName,
       "fsLogFileMaxSeverity": fsLogFileMaxSeverity,
       "fsLogFileMaxSize": fsLogFileMaxSize,
       "fsLogSendBufferStatus": fsLogSendBufferStatus,
       "fsLogSendBufferMaxSeverity": fsLogSendBufferMaxSeverity,
       "fsLogClearBuffer": fsLogClearBuffer,
       "fsLogHisRecordMaxNum": fsLogHisRecordMaxNum,
       "fsLogHisTable": fsLogHisTable,
       "fsLogHisEntry": fsLogHisEntry,
       "fsLogHisIndex": fsLogHisIndex,
       "fsLogHisSeverity": fsLogHisSeverity,
       "fsLogHisMsgName": fsLogHisMsgName,
       "fsLogHisDescription": fsLogHisDescription,
       "fsLogHisTime": fsLogHisTime,
       "fsLogHisStamps": fsLogHisStamps,
       "fsLogSequenceGlobalStatus": fsLogSequenceGlobalStatus,
       "fsLogTimeStampGlobalStatus": fsLogTimeStampGlobalStatus,
       "fsLogSyslogRelayGlobalStatus": fsLogSyslogRelayGlobalStatus,
       "fsLogSyslogFacility": fsLogSyslogFacility,
       "fsLogSyslogSeverity": fsLogSyslogSeverity,
       "fsLogSyslogServerTable": fsLogSyslogServerTable,
       "fsLogSyslogServerEntry": fsLogSyslogServerEntry,
       "fsLogSyslogServerIpAddr": fsLogSyslogServerIpAddr,
       "fsLogSyslogServerIpStatus": fsLogSyslogServerIpStatus,
       "fsLogSyslogSendSrcIfindex": fsLogSyslogSendSrcIfindex,
       "fsLogSyslogSendSrcIp": fsLogSyslogSendSrcIp,
       "fsLogMIBConformance": fsLogMIBConformance,
       "fsLogMIBCompliances": fsLogMIBCompliances,
       "fsLogMIBCompliance": fsLogMIBCompliance,
       "fsLogMIBGroups": fsLogMIBGroups,
       "fsLogMIBGroup": fsLogMIBGroup,
       "fsLogHisStampsMIBGroup": fsLogHisStampsMIBGroup}
)
