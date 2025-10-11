# SNMP MIB module (MY-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-LOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:54 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MyTrapType) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MyTrapType")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

myLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    myLogMIB.setRevisions(
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

_MyLogMIBObjects_ObjectIdentity = ObjectIdentity
myLogMIBObjects = _MyLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1)
)


class _MyLogGlobalStatus_Type(EnabledStatus):
    """Custom type myLogGlobalStatus based on EnabledStatus"""
    defaultValue = 1


_MyLogGlobalStatus_Type.__name__ = "EnabledStatus"
_MyLogGlobalStatus_Object = MibScalar
myLogGlobalStatus = _MyLogGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 1),
    _MyLogGlobalStatus_Type()
)
myLogGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogGlobalStatus.setStatus("current")


class _MyLogSendConsoleStatus_Type(EnabledStatus):
    """Custom type myLogSendConsoleStatus based on EnabledStatus"""
    defaultValue = 1


_MyLogSendConsoleStatus_Type.__name__ = "EnabledStatus"
_MyLogSendConsoleStatus_Object = MibScalar
myLogSendConsoleStatus = _MyLogSendConsoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 2),
    _MyLogSendConsoleStatus_Type()
)
myLogSendConsoleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendConsoleStatus.setStatus("current")


class _MyLogSendConsoleMaxSeverity_Type(LogSeverity):
    """Custom type myLogSendConsoleMaxSeverity based on LogSeverity"""
    defaultValue = 7


_MyLogSendConsoleMaxSeverity_Type.__name__ = "LogSeverity"
_MyLogSendConsoleMaxSeverity_Object = MibScalar
myLogSendConsoleMaxSeverity = _MyLogSendConsoleMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 3),
    _MyLogSendConsoleMaxSeverity_Type()
)
myLogSendConsoleMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendConsoleMaxSeverity.setStatus("current")


class _MyLogSendMonitorStatus_Type(EnabledStatus):
    """Custom type myLogSendMonitorStatus based on EnabledStatus"""
    defaultValue = 2


_MyLogSendMonitorStatus_Type.__name__ = "EnabledStatus"
_MyLogSendMonitorStatus_Object = MibScalar
myLogSendMonitorStatus = _MyLogSendMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 4),
    _MyLogSendMonitorStatus_Type()
)
myLogSendMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendMonitorStatus.setStatus("current")


class _MyLogSendMonitorMaxSeverity_Type(LogSeverity):
    """Custom type myLogSendMonitorMaxSeverity based on LogSeverity"""
    defaultValue = 7


_MyLogSendMonitorMaxSeverity_Type.__name__ = "LogSeverity"
_MyLogSendMonitorMaxSeverity_Object = MibScalar
myLogSendMonitorMaxSeverity = _MyLogSendMonitorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 5),
    _MyLogSendMonitorMaxSeverity_Type()
)
myLogSendMonitorMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendMonitorMaxSeverity.setStatus("current")


class _MyLogSaveFileName_Type(DisplayString):
    """Custom type myLogSaveFileName based on DisplayString"""
    defaultValue = OctetString("")


_MyLogSaveFileName_Type.__name__ = "DisplayString"
_MyLogSaveFileName_Object = MibScalar
myLogSaveFileName = _MyLogSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 6),
    _MyLogSaveFileName_Type()
)
myLogSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSaveFileName.setStatus("current")


class _MyLogFileMaxSeverity_Type(LogSeverity):
    """Custom type myLogFileMaxSeverity based on LogSeverity"""
    defaultValue = 5


_MyLogFileMaxSeverity_Type.__name__ = "LogSeverity"
_MyLogFileMaxSeverity_Object = MibScalar
myLogFileMaxSeverity = _MyLogFileMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 7),
    _MyLogFileMaxSeverity_Type()
)
myLogFileMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogFileMaxSeverity.setStatus("current")


class _MyLogFileMaxSize_Type(Integer32):
    """Custom type myLogFileMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 2000000),
    )


_MyLogFileMaxSize_Type.__name__ = "Integer32"
_MyLogFileMaxSize_Object = MibScalar
myLogFileMaxSize = _MyLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 8),
    _MyLogFileMaxSize_Type()
)
myLogFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogFileMaxSize.setStatus("current")


class _MyLogSendBufferStatus_Type(EnabledStatus):
    """Custom type myLogSendBufferStatus based on EnabledStatus"""
    defaultValue = 1


_MyLogSendBufferStatus_Type.__name__ = "EnabledStatus"
_MyLogSendBufferStatus_Object = MibScalar
myLogSendBufferStatus = _MyLogSendBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 9),
    _MyLogSendBufferStatus_Type()
)
myLogSendBufferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendBufferStatus.setStatus("current")


class _MyLogSendBufferMaxSeverity_Type(LogSeverity):
    """Custom type myLogSendBufferMaxSeverity based on LogSeverity"""
    defaultValue = 7


_MyLogSendBufferMaxSeverity_Type.__name__ = "LogSeverity"
_MyLogSendBufferMaxSeverity_Object = MibScalar
myLogSendBufferMaxSeverity = _MyLogSendBufferMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 10),
    _MyLogSendBufferMaxSeverity_Type()
)
myLogSendBufferMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSendBufferMaxSeverity.setStatus("current")
_MyLogClearBuffer_Type = Integer32
_MyLogClearBuffer_Object = MibScalar
myLogClearBuffer = _MyLogClearBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 11),
    _MyLogClearBuffer_Type()
)
myLogClearBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogClearBuffer.setStatus("current")
_MyLogHisRecordMaxNum_Type = Integer32
_MyLogHisRecordMaxNum_Object = MibScalar
myLogHisRecordMaxNum = _MyLogHisRecordMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 12),
    _MyLogHisRecordMaxNum_Type()
)
myLogHisRecordMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisRecordMaxNum.setStatus("current")
_MyLogHisTable_Object = MibTable
myLogHisTable = _MyLogHisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    myLogHisTable.setStatus("current")
_MyLogHisEntry_Object = MibTableRow
myLogHisEntry = _MyLogHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1)
)
myLogHisEntry.setIndexNames(
    (0, "MY-LOG-MIB", "myLogHisIndex"),
)
if mibBuilder.loadTexts:
    myLogHisEntry.setStatus("current")
_MyLogHisIndex_Type = Integer32
_MyLogHisIndex_Object = MibTableColumn
myLogHisIndex = _MyLogHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 1),
    _MyLogHisIndex_Type()
)
myLogHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisIndex.setStatus("current")
_MyLogHisSeverity_Type = LogSeverity
_MyLogHisSeverity_Object = MibTableColumn
myLogHisSeverity = _MyLogHisSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 2),
    _MyLogHisSeverity_Type()
)
myLogHisSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisSeverity.setStatus("current")


class _MyLogHisMsgName_Type(DisplayString):
    """Custom type myLogHisMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MyLogHisMsgName_Type.__name__ = "DisplayString"
_MyLogHisMsgName_Object = MibTableColumn
myLogHisMsgName = _MyLogHisMsgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 3),
    _MyLogHisMsgName_Type()
)
myLogHisMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisMsgName.setStatus("current")


class _MyLogHisDescription_Type(DisplayString):
    """Custom type myLogHisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MyLogHisDescription_Type.__name__ = "DisplayString"
_MyLogHisDescription_Object = MibTableColumn
myLogHisDescription = _MyLogHisDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 4),
    _MyLogHisDescription_Type()
)
myLogHisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisDescription.setStatus("current")
_MyLogHisTime_Type = DateAndTime
_MyLogHisTime_Object = MibTableColumn
myLogHisTime = _MyLogHisTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 5),
    _MyLogHisTime_Type()
)
myLogHisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisTime.setStatus("current")
_MyLogHisStamps_Type = TimeStamp
_MyLogHisStamps_Object = MibTableColumn
myLogHisStamps = _MyLogHisStamps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 6),
    _MyLogHisStamps_Type()
)
myLogHisStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogHisStamps.setStatus("current")


class _MyLogSequenceGlobalStatus_Type(EnabledStatus):
    """Custom type myLogSequenceGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_MyLogSequenceGlobalStatus_Type.__name__ = "EnabledStatus"
_MyLogSequenceGlobalStatus_Object = MibScalar
myLogSequenceGlobalStatus = _MyLogSequenceGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 14),
    _MyLogSequenceGlobalStatus_Type()
)
myLogSequenceGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSequenceGlobalStatus.setStatus("current")


class _MyLogTimeStampGlobalStatus_Type(LogTimeStamp):
    """Custom type myLogTimeStampGlobalStatus based on LogTimeStamp"""
    defaultValue = 2


_MyLogTimeStampGlobalStatus_Type.__name__ = "LogTimeStamp"
_MyLogTimeStampGlobalStatus_Object = MibScalar
myLogTimeStampGlobalStatus = _MyLogTimeStampGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 15),
    _MyLogTimeStampGlobalStatus_Type()
)
myLogTimeStampGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogTimeStampGlobalStatus.setStatus("current")


class _MyLogSyslogRelayGlobalStatus_Type(EnabledStatus):
    """Custom type myLogSyslogRelayGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_MyLogSyslogRelayGlobalStatus_Type.__name__ = "EnabledStatus"
_MyLogSyslogRelayGlobalStatus_Object = MibScalar
myLogSyslogRelayGlobalStatus = _MyLogSyslogRelayGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 16),
    _MyLogSyslogRelayGlobalStatus_Type()
)
myLogSyslogRelayGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogRelayGlobalStatus.setStatus("current")


class _MyLogSyslogFacility_Type(LogSyslogFacility):
    """Custom type myLogSyslogFacility based on LogSyslogFacility"""
    defaultValue = 23


_MyLogSyslogFacility_Type.__name__ = "LogSyslogFacility"
_MyLogSyslogFacility_Object = MibScalar
myLogSyslogFacility = _MyLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 17),
    _MyLogSyslogFacility_Type()
)
myLogSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogFacility.setStatus("current")


class _MyLogSyslogSeverity_Type(LogSeverity):
    """Custom type myLogSyslogSeverity based on LogSeverity"""
    defaultValue = 7


_MyLogSyslogSeverity_Type.__name__ = "LogSeverity"
_MyLogSyslogSeverity_Object = MibScalar
myLogSyslogSeverity = _MyLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 18),
    _MyLogSyslogSeverity_Type()
)
myLogSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogSeverity.setStatus("current")
_MyLogSyslogServerTable_Object = MibTable
myLogSyslogServerTable = _MyLogSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19)
)
if mibBuilder.loadTexts:
    myLogSyslogServerTable.setStatus("current")
_MyLogSyslogServerEntry_Object = MibTableRow
myLogSyslogServerEntry = _MyLogSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1)
)
myLogSyslogServerEntry.setIndexNames(
    (0, "MY-LOG-MIB", "myLogSyslogServerIpAddr"),
)
if mibBuilder.loadTexts:
    myLogSyslogServerEntry.setStatus("current")
_MyLogSyslogServerIpAddr_Type = IpAddress
_MyLogSyslogServerIpAddr_Object = MibTableColumn
myLogSyslogServerIpAddr = _MyLogSyslogServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1, 1),
    _MyLogSyslogServerIpAddr_Type()
)
myLogSyslogServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myLogSyslogServerIpAddr.setStatus("current")
_MyLogSyslogServerIpStatus_Type = ConfigStatus
_MyLogSyslogServerIpStatus_Object = MibTableColumn
myLogSyslogServerIpStatus = _MyLogSyslogServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1, 2),
    _MyLogSyslogServerIpStatus_Type()
)
myLogSyslogServerIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogServerIpStatus.setStatus("current")
_MyLogSyslogSendSrcIfindex_Type = IfIndex
_MyLogSyslogSendSrcIfindex_Object = MibScalar
myLogSyslogSendSrcIfindex = _MyLogSyslogSendSrcIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 20),
    _MyLogSyslogSendSrcIfindex_Type()
)
myLogSyslogSendSrcIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogSendSrcIfindex.setStatus("current")
_MyLogSyslogSendSrcIp_Type = IpAddress
_MyLogSyslogSendSrcIp_Object = MibScalar
myLogSyslogSendSrcIp = _MyLogSyslogSendSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 21),
    _MyLogSyslogSendSrcIp_Type()
)
myLogSyslogSendSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myLogSyslogSendSrcIp.setStatus("current")
_MyLogMIBConformance_ObjectIdentity = ObjectIdentity
myLogMIBConformance = _MyLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4)
)
_MyLogMIBCompliances_ObjectIdentity = ObjectIdentity
myLogMIBCompliances = _MyLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 1)
)
_MyLogMIBGroups_ObjectIdentity = ObjectIdentity
myLogMIBGroups = _MyLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2)
)

# Managed Objects groups

myLogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2, 1)
)
myLogMIBGroup.setObjects(
      *(("MY-LOG-MIB", "myLogGlobalStatus"),
        ("MY-LOG-MIB", "myLogSendConsoleStatus"),
        ("MY-LOG-MIB", "myLogSendConsoleMaxSeverity"),
        ("MY-LOG-MIB", "myLogSendMonitorStatus"),
        ("MY-LOG-MIB", "myLogSendMonitorMaxSeverity"),
        ("MY-LOG-MIB", "myLogSaveFileName"),
        ("MY-LOG-MIB", "myLogFileMaxSeverity"),
        ("MY-LOG-MIB", "myLogFileMaxSize"),
        ("MY-LOG-MIB", "myLogSendBufferStatus"),
        ("MY-LOG-MIB", "myLogSendBufferMaxSeverity"),
        ("MY-LOG-MIB", "myLogClearBuffer"),
        ("MY-LOG-MIB", "myLogHisRecordMaxNum"),
        ("MY-LOG-MIB", "myLogHisIndex"),
        ("MY-LOG-MIB", "myLogHisSeverity"),
        ("MY-LOG-MIB", "myLogHisMsgName"),
        ("MY-LOG-MIB", "myLogHisDescription"),
        ("MY-LOG-MIB", "myLogHisTime"),
        ("MY-LOG-MIB", "myLogSequenceGlobalStatus"),
        ("MY-LOG-MIB", "myLogTimeStampGlobalStatus"),
        ("MY-LOG-MIB", "myLogSyslogRelayGlobalStatus"),
        ("MY-LOG-MIB", "myLogSyslogFacility"),
        ("MY-LOG-MIB", "myLogSyslogSeverity"),
        ("MY-LOG-MIB", "myLogSyslogServerIpAddr"),
        ("MY-LOG-MIB", "myLogSyslogServerIpStatus"),
        ("MY-LOG-MIB", "myLogSyslogSendSrcIfindex"),
        ("MY-LOG-MIB", "myLogSyslogSendSrcIp"))
)
if mibBuilder.loadTexts:
    myLogMIBGroup.setStatus("current")

myLogHisStampsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2, 2)
)
myLogHisStampsMIBGroup.setObjects(
    ("MY-LOG-MIB", "myLogHisStamps")
)
if mibBuilder.loadTexts:
    myLogHisStampsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 1, 1)
)
myLogMIBCompliance.setObjects(
      *(("MY-LOG-MIB", "myLogMIBGroup"),
        ("MY-LOG-MIB", "myLogHisStampsMIBGroup"))
)
if mibBuilder.loadTexts:
    myLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-LOG-MIB",
    **{"LogSeverity": LogSeverity,
       "LogTimeStamp": LogTimeStamp,
       "LogSyslogFacility": LogSyslogFacility,
       "myLogMIB": myLogMIB,
       "myLogMIBObjects": myLogMIBObjects,
       "myLogGlobalStatus": myLogGlobalStatus,
       "myLogSendConsoleStatus": myLogSendConsoleStatus,
       "myLogSendConsoleMaxSeverity": myLogSendConsoleMaxSeverity,
       "myLogSendMonitorStatus": myLogSendMonitorStatus,
       "myLogSendMonitorMaxSeverity": myLogSendMonitorMaxSeverity,
       "myLogSaveFileName": myLogSaveFileName,
       "myLogFileMaxSeverity": myLogFileMaxSeverity,
       "myLogFileMaxSize": myLogFileMaxSize,
       "myLogSendBufferStatus": myLogSendBufferStatus,
       "myLogSendBufferMaxSeverity": myLogSendBufferMaxSeverity,
       "myLogClearBuffer": myLogClearBuffer,
       "myLogHisRecordMaxNum": myLogHisRecordMaxNum,
       "myLogHisTable": myLogHisTable,
       "myLogHisEntry": myLogHisEntry,
       "myLogHisIndex": myLogHisIndex,
       "myLogHisSeverity": myLogHisSeverity,
       "myLogHisMsgName": myLogHisMsgName,
       "myLogHisDescription": myLogHisDescription,
       "myLogHisTime": myLogHisTime,
       "myLogHisStamps": myLogHisStamps,
       "myLogSequenceGlobalStatus": myLogSequenceGlobalStatus,
       "myLogTimeStampGlobalStatus": myLogTimeStampGlobalStatus,
       "myLogSyslogRelayGlobalStatus": myLogSyslogRelayGlobalStatus,
       "myLogSyslogFacility": myLogSyslogFacility,
       "myLogSyslogSeverity": myLogSyslogSeverity,
       "myLogSyslogServerTable": myLogSyslogServerTable,
       "myLogSyslogServerEntry": myLogSyslogServerEntry,
       "myLogSyslogServerIpAddr": myLogSyslogServerIpAddr,
       "myLogSyslogServerIpStatus": myLogSyslogServerIpStatus,
       "myLogSyslogSendSrcIfindex": myLogSyslogSendSrcIfindex,
       "myLogSyslogSendSrcIp": myLogSyslogSendSrcIp,
       "myLogMIBConformance": myLogMIBConformance,
       "myLogMIBCompliances": myLogMIBCompliances,
       "myLogMIBCompliance": myLogMIBCompliance,
       "myLogMIBGroups": myLogMIBGroups,
       "myLogMIBGroup": myLogMIBGroup,
       "myLogHisStampsMIBGroup": myLogHisStampsMIBGroup}
)
