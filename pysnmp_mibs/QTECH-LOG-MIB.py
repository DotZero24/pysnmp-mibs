# SNMP MIB module (QTECH-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-LOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:22 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

qtechLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    qtechLogMIB.setRevisions(
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

_QtechLogMIBObjects_ObjectIdentity = ObjectIdentity
qtechLogMIBObjects = _QtechLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1)
)


class _QtechLogGlobalStatus_Type(EnabledStatus):
    """Custom type qtechLogGlobalStatus based on EnabledStatus"""
    defaultValue = 1


_QtechLogGlobalStatus_Type.__name__ = "EnabledStatus"
_QtechLogGlobalStatus_Object = MibScalar
qtechLogGlobalStatus = _QtechLogGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 1),
    _QtechLogGlobalStatus_Type()
)
qtechLogGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogGlobalStatus.setStatus("current")


class _QtechLogSendConsoleStatus_Type(EnabledStatus):
    """Custom type qtechLogSendConsoleStatus based on EnabledStatus"""
    defaultValue = 1


_QtechLogSendConsoleStatus_Type.__name__ = "EnabledStatus"
_QtechLogSendConsoleStatus_Object = MibScalar
qtechLogSendConsoleStatus = _QtechLogSendConsoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 2),
    _QtechLogSendConsoleStatus_Type()
)
qtechLogSendConsoleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendConsoleStatus.setStatus("current")


class _QtechLogSendConsoleMaxSeverity_Type(LogSeverity):
    """Custom type qtechLogSendConsoleMaxSeverity based on LogSeverity"""
    defaultValue = 7


_QtechLogSendConsoleMaxSeverity_Type.__name__ = "LogSeverity"
_QtechLogSendConsoleMaxSeverity_Object = MibScalar
qtechLogSendConsoleMaxSeverity = _QtechLogSendConsoleMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 3),
    _QtechLogSendConsoleMaxSeverity_Type()
)
qtechLogSendConsoleMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendConsoleMaxSeverity.setStatus("current")


class _QtechLogSendMonitorStatus_Type(EnabledStatus):
    """Custom type qtechLogSendMonitorStatus based on EnabledStatus"""
    defaultValue = 2


_QtechLogSendMonitorStatus_Type.__name__ = "EnabledStatus"
_QtechLogSendMonitorStatus_Object = MibScalar
qtechLogSendMonitorStatus = _QtechLogSendMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 4),
    _QtechLogSendMonitorStatus_Type()
)
qtechLogSendMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendMonitorStatus.setStatus("current")


class _QtechLogSendMonitorMaxSeverity_Type(LogSeverity):
    """Custom type qtechLogSendMonitorMaxSeverity based on LogSeverity"""
    defaultValue = 7


_QtechLogSendMonitorMaxSeverity_Type.__name__ = "LogSeverity"
_QtechLogSendMonitorMaxSeverity_Object = MibScalar
qtechLogSendMonitorMaxSeverity = _QtechLogSendMonitorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 5),
    _QtechLogSendMonitorMaxSeverity_Type()
)
qtechLogSendMonitorMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendMonitorMaxSeverity.setStatus("current")


class _QtechLogSaveFileName_Type(DisplayString):
    """Custom type qtechLogSaveFileName based on DisplayString"""
    defaultValue = OctetString("")


_QtechLogSaveFileName_Type.__name__ = "DisplayString"
_QtechLogSaveFileName_Object = MibScalar
qtechLogSaveFileName = _QtechLogSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 6),
    _QtechLogSaveFileName_Type()
)
qtechLogSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSaveFileName.setStatus("current")


class _QtechLogFileMaxSeverity_Type(LogSeverity):
    """Custom type qtechLogFileMaxSeverity based on LogSeverity"""
    defaultValue = 5


_QtechLogFileMaxSeverity_Type.__name__ = "LogSeverity"
_QtechLogFileMaxSeverity_Object = MibScalar
qtechLogFileMaxSeverity = _QtechLogFileMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 7),
    _QtechLogFileMaxSeverity_Type()
)
qtechLogFileMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogFileMaxSeverity.setStatus("current")


class _QtechLogFileMaxSize_Type(Integer32):
    """Custom type qtechLogFileMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 2000000),
    )


_QtechLogFileMaxSize_Type.__name__ = "Integer32"
_QtechLogFileMaxSize_Object = MibScalar
qtechLogFileMaxSize = _QtechLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 8),
    _QtechLogFileMaxSize_Type()
)
qtechLogFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogFileMaxSize.setStatus("current")


class _QtechLogSendBufferStatus_Type(EnabledStatus):
    """Custom type qtechLogSendBufferStatus based on EnabledStatus"""
    defaultValue = 1


_QtechLogSendBufferStatus_Type.__name__ = "EnabledStatus"
_QtechLogSendBufferStatus_Object = MibScalar
qtechLogSendBufferStatus = _QtechLogSendBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 9),
    _QtechLogSendBufferStatus_Type()
)
qtechLogSendBufferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendBufferStatus.setStatus("current")


class _QtechLogSendBufferMaxSeverity_Type(LogSeverity):
    """Custom type qtechLogSendBufferMaxSeverity based on LogSeverity"""
    defaultValue = 7


_QtechLogSendBufferMaxSeverity_Type.__name__ = "LogSeverity"
_QtechLogSendBufferMaxSeverity_Object = MibScalar
qtechLogSendBufferMaxSeverity = _QtechLogSendBufferMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 10),
    _QtechLogSendBufferMaxSeverity_Type()
)
qtechLogSendBufferMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSendBufferMaxSeverity.setStatus("current")
_QtechLogClearBuffer_Type = Integer32
_QtechLogClearBuffer_Object = MibScalar
qtechLogClearBuffer = _QtechLogClearBuffer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 11),
    _QtechLogClearBuffer_Type()
)
qtechLogClearBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogClearBuffer.setStatus("current")
_QtechLogHisRecordMaxNum_Type = Integer32
_QtechLogHisRecordMaxNum_Object = MibScalar
qtechLogHisRecordMaxNum = _QtechLogHisRecordMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 12),
    _QtechLogHisRecordMaxNum_Type()
)
qtechLogHisRecordMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisRecordMaxNum.setStatus("current")
_QtechLogHisTable_Object = MibTable
qtechLogHisTable = _QtechLogHisTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    qtechLogHisTable.setStatus("current")
_QtechLogHisEntry_Object = MibTableRow
qtechLogHisEntry = _QtechLogHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1)
)
qtechLogHisEntry.setIndexNames(
    (0, "QTECH-LOG-MIB", "qtechLogHisIndex"),
)
if mibBuilder.loadTexts:
    qtechLogHisEntry.setStatus("current")
_QtechLogHisIndex_Type = Integer32
_QtechLogHisIndex_Object = MibTableColumn
qtechLogHisIndex = _QtechLogHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 1),
    _QtechLogHisIndex_Type()
)
qtechLogHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisIndex.setStatus("current")
_QtechLogHisSeverity_Type = LogSeverity
_QtechLogHisSeverity_Object = MibTableColumn
qtechLogHisSeverity = _QtechLogHisSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 2),
    _QtechLogHisSeverity_Type()
)
qtechLogHisSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisSeverity.setStatus("current")


class _QtechLogHisMsgName_Type(DisplayString):
    """Custom type qtechLogHisMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_QtechLogHisMsgName_Type.__name__ = "DisplayString"
_QtechLogHisMsgName_Object = MibTableColumn
qtechLogHisMsgName = _QtechLogHisMsgName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 3),
    _QtechLogHisMsgName_Type()
)
qtechLogHisMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisMsgName.setStatus("current")


class _QtechLogHisDescription_Type(DisplayString):
    """Custom type qtechLogHisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_QtechLogHisDescription_Type.__name__ = "DisplayString"
_QtechLogHisDescription_Object = MibTableColumn
qtechLogHisDescription = _QtechLogHisDescription_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 4),
    _QtechLogHisDescription_Type()
)
qtechLogHisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisDescription.setStatus("current")
_QtechLogHisTime_Type = DateAndTime
_QtechLogHisTime_Object = MibTableColumn
qtechLogHisTime = _QtechLogHisTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 5),
    _QtechLogHisTime_Type()
)
qtechLogHisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisTime.setStatus("current")
_QtechLogHisStamps_Type = TimeStamp
_QtechLogHisStamps_Object = MibTableColumn
qtechLogHisStamps = _QtechLogHisStamps_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 13, 1, 6),
    _QtechLogHisStamps_Type()
)
qtechLogHisStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogHisStamps.setStatus("current")


class _QtechLogSequenceGlobalStatus_Type(EnabledStatus):
    """Custom type qtechLogSequenceGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_QtechLogSequenceGlobalStatus_Type.__name__ = "EnabledStatus"
_QtechLogSequenceGlobalStatus_Object = MibScalar
qtechLogSequenceGlobalStatus = _QtechLogSequenceGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 14),
    _QtechLogSequenceGlobalStatus_Type()
)
qtechLogSequenceGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSequenceGlobalStatus.setStatus("current")


class _QtechLogTimeStampGlobalStatus_Type(LogTimeStamp):
    """Custom type qtechLogTimeStampGlobalStatus based on LogTimeStamp"""
    defaultValue = 2


_QtechLogTimeStampGlobalStatus_Type.__name__ = "LogTimeStamp"
_QtechLogTimeStampGlobalStatus_Object = MibScalar
qtechLogTimeStampGlobalStatus = _QtechLogTimeStampGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 15),
    _QtechLogTimeStampGlobalStatus_Type()
)
qtechLogTimeStampGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogTimeStampGlobalStatus.setStatus("current")


class _QtechLogSyslogRelayGlobalStatus_Type(EnabledStatus):
    """Custom type qtechLogSyslogRelayGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_QtechLogSyslogRelayGlobalStatus_Type.__name__ = "EnabledStatus"
_QtechLogSyslogRelayGlobalStatus_Object = MibScalar
qtechLogSyslogRelayGlobalStatus = _QtechLogSyslogRelayGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 16),
    _QtechLogSyslogRelayGlobalStatus_Type()
)
qtechLogSyslogRelayGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogRelayGlobalStatus.setStatus("current")


class _QtechLogSyslogFacility_Type(LogSyslogFacility):
    """Custom type qtechLogSyslogFacility based on LogSyslogFacility"""
    defaultValue = 23


_QtechLogSyslogFacility_Type.__name__ = "LogSyslogFacility"
_QtechLogSyslogFacility_Object = MibScalar
qtechLogSyslogFacility = _QtechLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 17),
    _QtechLogSyslogFacility_Type()
)
qtechLogSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogFacility.setStatus("current")


class _QtechLogSyslogSeverity_Type(LogSeverity):
    """Custom type qtechLogSyslogSeverity based on LogSeverity"""
    defaultValue = 7


_QtechLogSyslogSeverity_Type.__name__ = "LogSeverity"
_QtechLogSyslogSeverity_Object = MibScalar
qtechLogSyslogSeverity = _QtechLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 18),
    _QtechLogSyslogSeverity_Type()
)
qtechLogSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogSeverity.setStatus("current")
_QtechLogSyslogServerTable_Object = MibTable
qtechLogSyslogServerTable = _QtechLogSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 19)
)
if mibBuilder.loadTexts:
    qtechLogSyslogServerTable.setStatus("current")
_QtechLogSyslogServerEntry_Object = MibTableRow
qtechLogSyslogServerEntry = _QtechLogSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 19, 1)
)
qtechLogSyslogServerEntry.setIndexNames(
    (0, "QTECH-LOG-MIB", "qtechLogSyslogServerIpAddr"),
)
if mibBuilder.loadTexts:
    qtechLogSyslogServerEntry.setStatus("current")
_QtechLogSyslogServerIpAddr_Type = IpAddress
_QtechLogSyslogServerIpAddr_Object = MibTableColumn
qtechLogSyslogServerIpAddr = _QtechLogSyslogServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 19, 1, 1),
    _QtechLogSyslogServerIpAddr_Type()
)
qtechLogSyslogServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLogSyslogServerIpAddr.setStatus("current")
_QtechLogSyslogServerIpStatus_Type = ConfigStatus
_QtechLogSyslogServerIpStatus_Object = MibTableColumn
qtechLogSyslogServerIpStatus = _QtechLogSyslogServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 19, 1, 2),
    _QtechLogSyslogServerIpStatus_Type()
)
qtechLogSyslogServerIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogServerIpStatus.setStatus("current")
_QtechLogSyslogSendSrcIfindex_Type = IfIndex
_QtechLogSyslogSendSrcIfindex_Object = MibScalar
qtechLogSyslogSendSrcIfindex = _QtechLogSyslogSendSrcIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 20),
    _QtechLogSyslogSendSrcIfindex_Type()
)
qtechLogSyslogSendSrcIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogSendSrcIfindex.setStatus("current")
_QtechLogSyslogSendSrcIp_Type = IpAddress
_QtechLogSyslogSendSrcIp_Object = MibScalar
qtechLogSyslogSendSrcIp = _QtechLogSyslogSendSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 1, 21),
    _QtechLogSyslogSendSrcIp_Type()
)
qtechLogSyslogSendSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLogSyslogSendSrcIp.setStatus("current")
_QtechLogMIBConformance_ObjectIdentity = ObjectIdentity
qtechLogMIBConformance = _QtechLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4)
)
_QtechLogMIBCompliances_ObjectIdentity = ObjectIdentity
qtechLogMIBCompliances = _QtechLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4, 1)
)
_QtechLogMIBGroups_ObjectIdentity = ObjectIdentity
qtechLogMIBGroups = _QtechLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4, 2)
)

# Managed Objects groups

qtechLogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4, 2, 1)
)
qtechLogMIBGroup.setObjects(
      *(("QTECH-LOG-MIB", "qtechLogGlobalStatus"),
        ("QTECH-LOG-MIB", "qtechLogSendConsoleStatus"),
        ("QTECH-LOG-MIB", "qtechLogSendConsoleMaxSeverity"),
        ("QTECH-LOG-MIB", "qtechLogSendMonitorStatus"),
        ("QTECH-LOG-MIB", "qtechLogSendMonitorMaxSeverity"),
        ("QTECH-LOG-MIB", "qtechLogSaveFileName"),
        ("QTECH-LOG-MIB", "qtechLogFileMaxSeverity"),
        ("QTECH-LOG-MIB", "qtechLogFileMaxSize"),
        ("QTECH-LOG-MIB", "qtechLogSendBufferStatus"),
        ("QTECH-LOG-MIB", "qtechLogSendBufferMaxSeverity"),
        ("QTECH-LOG-MIB", "qtechLogClearBuffer"),
        ("QTECH-LOG-MIB", "qtechLogHisRecordMaxNum"),
        ("QTECH-LOG-MIB", "qtechLogHisIndex"),
        ("QTECH-LOG-MIB", "qtechLogHisSeverity"),
        ("QTECH-LOG-MIB", "qtechLogHisMsgName"),
        ("QTECH-LOG-MIB", "qtechLogHisDescription"),
        ("QTECH-LOG-MIB", "qtechLogHisTime"),
        ("QTECH-LOG-MIB", "qtechLogSequenceGlobalStatus"),
        ("QTECH-LOG-MIB", "qtechLogTimeStampGlobalStatus"),
        ("QTECH-LOG-MIB", "qtechLogSyslogRelayGlobalStatus"),
        ("QTECH-LOG-MIB", "qtechLogSyslogFacility"),
        ("QTECH-LOG-MIB", "qtechLogSyslogSeverity"),
        ("QTECH-LOG-MIB", "qtechLogSyslogServerIpAddr"),
        ("QTECH-LOG-MIB", "qtechLogSyslogServerIpStatus"),
        ("QTECH-LOG-MIB", "qtechLogSyslogSendSrcIfindex"),
        ("QTECH-LOG-MIB", "qtechLogSyslogSendSrcIp"))
)
if mibBuilder.loadTexts:
    qtechLogMIBGroup.setStatus("current")

qtechLogHisStampsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4, 2, 2)
)
qtechLogHisStampsMIBGroup.setObjects(
    ("QTECH-LOG-MIB", "qtechLogHisStamps")
)
if mibBuilder.loadTexts:
    qtechLogHisStampsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 4, 4, 1, 1)
)
qtechLogMIBCompliance.setObjects(
      *(("QTECH-LOG-MIB", "qtechLogMIBGroup"),
        ("QTECH-LOG-MIB", "qtechLogHisStampsMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-LOG-MIB",
    **{"LogSeverity": LogSeverity,
       "LogTimeStamp": LogTimeStamp,
       "LogSyslogFacility": LogSyslogFacility,
       "qtechLogMIB": qtechLogMIB,
       "qtechLogMIBObjects": qtechLogMIBObjects,
       "qtechLogGlobalStatus": qtechLogGlobalStatus,
       "qtechLogSendConsoleStatus": qtechLogSendConsoleStatus,
       "qtechLogSendConsoleMaxSeverity": qtechLogSendConsoleMaxSeverity,
       "qtechLogSendMonitorStatus": qtechLogSendMonitorStatus,
       "qtechLogSendMonitorMaxSeverity": qtechLogSendMonitorMaxSeverity,
       "qtechLogSaveFileName": qtechLogSaveFileName,
       "qtechLogFileMaxSeverity": qtechLogFileMaxSeverity,
       "qtechLogFileMaxSize": qtechLogFileMaxSize,
       "qtechLogSendBufferStatus": qtechLogSendBufferStatus,
       "qtechLogSendBufferMaxSeverity": qtechLogSendBufferMaxSeverity,
       "qtechLogClearBuffer": qtechLogClearBuffer,
       "qtechLogHisRecordMaxNum": qtechLogHisRecordMaxNum,
       "qtechLogHisTable": qtechLogHisTable,
       "qtechLogHisEntry": qtechLogHisEntry,
       "qtechLogHisIndex": qtechLogHisIndex,
       "qtechLogHisSeverity": qtechLogHisSeverity,
       "qtechLogHisMsgName": qtechLogHisMsgName,
       "qtechLogHisDescription": qtechLogHisDescription,
       "qtechLogHisTime": qtechLogHisTime,
       "qtechLogHisStamps": qtechLogHisStamps,
       "qtechLogSequenceGlobalStatus": qtechLogSequenceGlobalStatus,
       "qtechLogTimeStampGlobalStatus": qtechLogTimeStampGlobalStatus,
       "qtechLogSyslogRelayGlobalStatus": qtechLogSyslogRelayGlobalStatus,
       "qtechLogSyslogFacility": qtechLogSyslogFacility,
       "qtechLogSyslogSeverity": qtechLogSyslogSeverity,
       "qtechLogSyslogServerTable": qtechLogSyslogServerTable,
       "qtechLogSyslogServerEntry": qtechLogSyslogServerEntry,
       "qtechLogSyslogServerIpAddr": qtechLogSyslogServerIpAddr,
       "qtechLogSyslogServerIpStatus": qtechLogSyslogServerIpStatus,
       "qtechLogSyslogSendSrcIfindex": qtechLogSyslogSendSrcIfindex,
       "qtechLogSyslogSendSrcIp": qtechLogSyslogSendSrcIp,
       "qtechLogMIBConformance": qtechLogMIBConformance,
       "qtechLogMIBCompliances": qtechLogMIBCompliances,
       "qtechLogMIBCompliance": qtechLogMIBCompliance,
       "qtechLogMIBGroups": qtechLogMIBGroups,
       "qtechLogMIBGroup": qtechLogMIBGroup,
       "qtechLogHisStampsMIBGroup": qtechLogHisStampsMIBGroup}
)
