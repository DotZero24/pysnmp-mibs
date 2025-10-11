# SNMP MIB module (SUPERMICRO-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:06 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

fsSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89)
)
if mibBuilder.loadTexts:
    fsSyslog.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSyslogGeneralGroup_ObjectIdentity = ObjectIdentity
fsSyslogGeneralGroup = _FsSyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1)
)


class _FsSyslogLogging_Type(Integer32):
    """Custom type fsSyslogLogging based on Integer32"""
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


_FsSyslogLogging_Type.__name__ = "Integer32"
_FsSyslogLogging_Object = MibScalar
fsSyslogLogging = _FsSyslogLogging_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 1),
    _FsSyslogLogging_Type()
)
fsSyslogLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogLogging.setStatus("current")


class _FsSyslogTimeStamp_Type(Integer32):
    """Custom type fsSyslogTimeStamp based on Integer32"""
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


_FsSyslogTimeStamp_Type.__name__ = "Integer32"
_FsSyslogTimeStamp_Object = MibScalar
fsSyslogTimeStamp = _FsSyslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 2),
    _FsSyslogTimeStamp_Type()
)
fsSyslogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogTimeStamp.setStatus("deprecated")


class _FsSyslogConsoleLog_Type(Integer32):
    """Custom type fsSyslogConsoleLog based on Integer32"""
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


_FsSyslogConsoleLog_Type.__name__ = "Integer32"
_FsSyslogConsoleLog_Object = MibScalar
fsSyslogConsoleLog = _FsSyslogConsoleLog_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 3),
    _FsSyslogConsoleLog_Type()
)
fsSyslogConsoleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogConsoleLog.setStatus("current")


class _FsSyslogSysBuffers_Type(Integer32):
    """Custom type fsSyslogSysBuffers based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsSyslogSysBuffers_Type.__name__ = "Integer32"
_FsSyslogSysBuffers_Object = MibScalar
fsSyslogSysBuffers = _FsSyslogSysBuffers_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 4),
    _FsSyslogSysBuffers_Type()
)
fsSyslogSysBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogSysBuffers.setStatus("current")


class _FsSyslogClearLog_Type(TruthValue):
    """Custom type fsSyslogClearLog based on TruthValue"""
    defaultValue = 2


_FsSyslogClearLog_Type.__name__ = "TruthValue"
_FsSyslogClearLog_Object = MibScalar
fsSyslogClearLog = _FsSyslogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 5),
    _FsSyslogClearLog_Type()
)
fsSyslogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogClearLog.setStatus("current")
_FsSyslogConfigTable_Object = MibTable
fsSyslogConfigTable = _FsSyslogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 6)
)
if mibBuilder.loadTexts:
    fsSyslogConfigTable.setStatus("current")
_FsSyslogConfigEntry_Object = MibTableRow
fsSyslogConfigEntry = _FsSyslogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 6, 1)
)
fsSyslogConfigEntry.setIndexNames(
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogConfigModule"),
)
if mibBuilder.loadTexts:
    fsSyslogConfigEntry.setStatus("current")


class _FsSyslogConfigModule_Type(Integer32):
    """Custom type fsSyslogConfigModule based on Integer32"""
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
        *(("web", 1),
          ("msr", 2),
          ("tftp", 3),
          ("cli", 4))
    )


_FsSyslogConfigModule_Type.__name__ = "Integer32"
_FsSyslogConfigModule_Object = MibTableColumn
fsSyslogConfigModule = _FsSyslogConfigModule_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 6, 1, 1),
    _FsSyslogConfigModule_Type()
)
fsSyslogConfigModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogConfigModule.setStatus("current")


class _FsSyslogConfigLogLevel_Type(Integer32):
    """Custom type fsSyslogConfigLogLevel based on Integer32"""
    defaultValue = 2

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


_FsSyslogConfigLogLevel_Type.__name__ = "Integer32"
_FsSyslogConfigLogLevel_Object = MibTableColumn
fsSyslogConfigLogLevel = _FsSyslogConfigLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 6, 1, 2),
    _FsSyslogConfigLogLevel_Type()
)
fsSyslogConfigLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogConfigLogLevel.setStatus("current")


class _FsSyslogFacility_Type(Integer32):
    """Custom type fsSyslogFacility based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_FsSyslogFacility_Type.__name__ = "Integer32"
_FsSyslogFacility_Object = MibScalar
fsSyslogFacility = _FsSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 7),
    _FsSyslogFacility_Type()
)
fsSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFacility.setStatus("current")


class _FsSyslogRole_Type(Integer32):
    """Custom type fsSyslogRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("relay", 2))
    )


_FsSyslogRole_Type.__name__ = "Integer32"
_FsSyslogRole_Object = MibScalar
fsSyslogRole = _FsSyslogRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 8),
    _FsSyslogRole_Type()
)
fsSyslogRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogRole.setStatus("current")


class _FsSyslogLogFile_Type(Integer32):
    """Custom type fsSyslogLogFile based on Integer32"""
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


_FsSyslogLogFile_Type.__name__ = "Integer32"
_FsSyslogLogFile_Object = MibScalar
fsSyslogLogFile = _FsSyslogLogFile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 9),
    _FsSyslogLogFile_Type()
)
fsSyslogLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogLogFile.setStatus("current")


class _FsSyslogMail_Type(Integer32):
    """Custom type fsSyslogMail based on Integer32"""
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


_FsSyslogMail_Type.__name__ = "Integer32"
_FsSyslogMail_Object = MibScalar
fsSyslogMail = _FsSyslogMail_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 10),
    _FsSyslogMail_Type()
)
fsSyslogMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogMail.setStatus("current")


class _FsSyslogProfile_Type(Integer32):
    """Custom type fsSyslogProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("cooked", 2))
    )


_FsSyslogProfile_Type.__name__ = "Integer32"
_FsSyslogProfile_Object = MibScalar
fsSyslogProfile = _FsSyslogProfile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 11),
    _FsSyslogProfile_Type()
)
fsSyslogProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogProfile.setStatus("current")


class _FsSyslogRelayPort_Type(Integer32):
    """Custom type fsSyslogRelayPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSyslogRelayPort_Type.__name__ = "Integer32"
_FsSyslogRelayPort_Object = MibScalar
fsSyslogRelayPort = _FsSyslogRelayPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 12),
    _FsSyslogRelayPort_Type()
)
fsSyslogRelayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogRelayPort.setStatus("current")


class _FsSyslogRelayTransType_Type(Integer32):
    """Custom type fsSyslogRelayTransType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_FsSyslogRelayTransType_Type.__name__ = "Integer32"
_FsSyslogRelayTransType_Object = MibScalar
fsSyslogRelayTransType = _FsSyslogRelayTransType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 13),
    _FsSyslogRelayTransType_Type()
)
fsSyslogRelayTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogRelayTransType.setStatus("current")


class _FsSyslogFileNameOne_Type(DisplayString):
    """Custom type fsSyslogFileNameOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSyslogFileNameOne_Type.__name__ = "DisplayString"
_FsSyslogFileNameOne_Object = MibScalar
fsSyslogFileNameOne = _FsSyslogFileNameOne_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 14),
    _FsSyslogFileNameOne_Type()
)
fsSyslogFileNameOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFileNameOne.setStatus("current")


class _FsSyslogFileNameTwo_Type(DisplayString):
    """Custom type fsSyslogFileNameTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSyslogFileNameTwo_Type.__name__ = "DisplayString"
_FsSyslogFileNameTwo_Object = MibScalar
fsSyslogFileNameTwo = _FsSyslogFileNameTwo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 15),
    _FsSyslogFileNameTwo_Type()
)
fsSyslogFileNameTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFileNameTwo.setStatus("current")


class _FsSyslogFileNameThree_Type(DisplayString):
    """Custom type fsSyslogFileNameThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSyslogFileNameThree_Type.__name__ = "DisplayString"
_FsSyslogFileNameThree_Object = MibScalar
fsSyslogFileNameThree = _FsSyslogFileNameThree_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 16),
    _FsSyslogFileNameThree_Type()
)
fsSyslogFileNameThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFileNameThree.setStatus("current")
_FsSyslogFileTable_Object = MibTable
fsSyslogFileTable = _FsSyslogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 17)
)
if mibBuilder.loadTexts:
    fsSyslogFileTable.setStatus("current")
_FsSyslogFileEntry_Object = MibTableRow
fsSyslogFileEntry = _FsSyslogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 17, 1)
)
fsSyslogFileEntry.setIndexNames(
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogFilePriority"),
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogFileName"),
)
if mibBuilder.loadTexts:
    fsSyslogFileEntry.setStatus("current")


class _FsSyslogFilePriority_Type(Integer32):
    """Custom type fsSyslogFilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 191),
    )


_FsSyslogFilePriority_Type.__name__ = "Integer32"
_FsSyslogFilePriority_Object = MibTableColumn
fsSyslogFilePriority = _FsSyslogFilePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 17, 1, 1),
    _FsSyslogFilePriority_Type()
)
fsSyslogFilePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogFilePriority.setStatus("current")


class _FsSyslogFileName_Type(DisplayString):
    """Custom type fsSyslogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsSyslogFileName_Type.__name__ = "DisplayString"
_FsSyslogFileName_Object = MibTableColumn
fsSyslogFileName = _FsSyslogFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 17, 1, 2),
    _FsSyslogFileName_Type()
)
fsSyslogFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogFileName.setStatus("current")
_FsSyslogFileRowStatus_Type = RowStatus
_FsSyslogFileRowStatus_Object = MibTableColumn
fsSyslogFileRowStatus = _FsSyslogFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 17, 1, 3),
    _FsSyslogFileRowStatus_Type()
)
fsSyslogFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFileRowStatus.setStatus("current")


class _FsSyslogServerUpDownTrap_Type(Integer32):
    """Custom type fsSyslogServerUpDownTrap based on Integer32"""
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


_FsSyslogServerUpDownTrap_Type.__name__ = "Integer32"
_FsSyslogServerUpDownTrap_Object = MibScalar
fsSyslogServerUpDownTrap = _FsSyslogServerUpDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 1, 18),
    _FsSyslogServerUpDownTrap_Type()
)
fsSyslogServerUpDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogServerUpDownTrap.setStatus("current")
_FsSyslogLogs_ObjectIdentity = ObjectIdentity
fsSyslogLogs = _FsSyslogLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2)
)
_FsSyslogLogSrvAddr_Type = IpAddress
_FsSyslogLogSrvAddr_Object = MibScalar
fsSyslogLogSrvAddr = _FsSyslogLogSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 1),
    _FsSyslogLogSrvAddr_Type()
)
fsSyslogLogSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogLogSrvAddr.setStatus("deprecated")
_FsSyslogLogNoLogServer_Type = TruthValue
_FsSyslogLogNoLogServer_Object = MibScalar
fsSyslogLogNoLogServer = _FsSyslogLogNoLogServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 2),
    _FsSyslogLogNoLogServer_Type()
)
fsSyslogLogNoLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogLogNoLogServer.setStatus("deprecated")
_FsSyslogFwdTable_Object = MibTable
fsSyslogFwdTable = _FsSyslogFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3)
)
if mibBuilder.loadTexts:
    fsSyslogFwdTable.setStatus("current")
_FsSyslogFwdEntry_Object = MibTableRow
fsSyslogFwdEntry = _FsSyslogFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1)
)
fsSyslogFwdEntry.setIndexNames(
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogFwdPriority"),
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogFwdAddressType"),
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogFwdServerIP"),
)
if mibBuilder.loadTexts:
    fsSyslogFwdEntry.setStatus("current")


class _FsSyslogFwdPriority_Type(Integer32):
    """Custom type fsSyslogFwdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 191),
    )


_FsSyslogFwdPriority_Type.__name__ = "Integer32"
_FsSyslogFwdPriority_Object = MibTableColumn
fsSyslogFwdPriority = _FsSyslogFwdPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 1),
    _FsSyslogFwdPriority_Type()
)
fsSyslogFwdPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogFwdPriority.setStatus("current")
_FsSyslogFwdAddressType_Type = InetAddressType
_FsSyslogFwdAddressType_Object = MibTableColumn
fsSyslogFwdAddressType = _FsSyslogFwdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 2),
    _FsSyslogFwdAddressType_Type()
)
fsSyslogFwdAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogFwdAddressType.setStatus("current")


class _FsSyslogFwdServerIP_Type(InetAddress):
    """Custom type fsSyslogFwdServerIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsSyslogFwdServerIP_Type.__name__ = "InetAddress"
_FsSyslogFwdServerIP_Object = MibTableColumn
fsSyslogFwdServerIP = _FsSyslogFwdServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 3),
    _FsSyslogFwdServerIP_Type()
)
fsSyslogFwdServerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogFwdServerIP.setStatus("current")


class _FsSyslogFwdPort_Type(Integer32):
    """Custom type fsSyslogFwdPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSyslogFwdPort_Type.__name__ = "Integer32"
_FsSyslogFwdPort_Object = MibTableColumn
fsSyslogFwdPort = _FsSyslogFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 4),
    _FsSyslogFwdPort_Type()
)
fsSyslogFwdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFwdPort.setStatus("current")


class _FsSyslogFwdTransType_Type(Integer32):
    """Custom type fsSyslogFwdTransType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1),
          ("beep", 2))
    )


_FsSyslogFwdTransType_Type.__name__ = "Integer32"
_FsSyslogFwdTransType_Object = MibTableColumn
fsSyslogFwdTransType = _FsSyslogFwdTransType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 5),
    _FsSyslogFwdTransType_Type()
)
fsSyslogFwdTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFwdTransType.setStatus("current")
_FsSyslogFwdRowStatus_Type = RowStatus
_FsSyslogFwdRowStatus_Object = MibTableColumn
fsSyslogFwdRowStatus = _FsSyslogFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 2, 3, 1, 6),
    _FsSyslogFwdRowStatus_Type()
)
fsSyslogFwdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogFwdRowStatus.setStatus("current")
_FsSyslogSmtp_ObjectIdentity = ObjectIdentity
fsSyslogSmtp = _FsSyslogSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3)
)
_FsSyslogSmtpSrvAddr_Type = IpAddress
_FsSyslogSmtpSrvAddr_Object = MibScalar
fsSyslogSmtpSrvAddr = _FsSyslogSmtpSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 1),
    _FsSyslogSmtpSrvAddr_Type()
)
fsSyslogSmtpSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogSmtpSrvAddr.setStatus("deprecated")


class _FsSyslogSmtpRcvrMailId_Type(DisplayString):
    """Custom type fsSyslogSmtpRcvrMailId based on DisplayString"""
    defaultValue = OctetString("admin@email.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_FsSyslogSmtpRcvrMailId_Type.__name__ = "DisplayString"
_FsSyslogSmtpRcvrMailId_Object = MibScalar
fsSyslogSmtpRcvrMailId = _FsSyslogSmtpRcvrMailId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 2),
    _FsSyslogSmtpRcvrMailId_Type()
)
fsSyslogSmtpRcvrMailId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogSmtpRcvrMailId.setStatus("deprecated")


class _FsSyslogSmtpSenderMailId_Type(DisplayString):
    """Custom type fsSyslogSmtpSenderMailId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FsSyslogSmtpSenderMailId_Type.__name__ = "DisplayString"
_FsSyslogSmtpSenderMailId_Object = MibScalar
fsSyslogSmtpSenderMailId = _FsSyslogSmtpSenderMailId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 3),
    _FsSyslogSmtpSenderMailId_Type()
)
fsSyslogSmtpSenderMailId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogSmtpSenderMailId.setStatus("current")
_FsSyslogMailTable_Object = MibTable
fsSyslogMailTable = _FsSyslogMailTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4)
)
if mibBuilder.loadTexts:
    fsSyslogMailTable.setStatus("current")
_FsSyslogMailEntry_Object = MibTableRow
fsSyslogMailEntry = _FsSyslogMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1)
)
fsSyslogMailEntry.setIndexNames(
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogMailPriority"),
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogMailServAddType"),
    (0, "SUPERMICRO-SYSLOG-MIB", "fsSyslogMailServAdd"),
)
if mibBuilder.loadTexts:
    fsSyslogMailEntry.setStatus("current")


class _FsSyslogMailPriority_Type(Integer32):
    """Custom type fsSyslogMailPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 191),
    )


_FsSyslogMailPriority_Type.__name__ = "Integer32"
_FsSyslogMailPriority_Object = MibTableColumn
fsSyslogMailPriority = _FsSyslogMailPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 1),
    _FsSyslogMailPriority_Type()
)
fsSyslogMailPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogMailPriority.setStatus("current")
_FsSyslogMailServAddType_Type = InetAddressType
_FsSyslogMailServAddType_Object = MibTableColumn
fsSyslogMailServAddType = _FsSyslogMailServAddType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 2),
    _FsSyslogMailServAddType_Type()
)
fsSyslogMailServAddType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogMailServAddType.setStatus("current")


class _FsSyslogMailServAdd_Type(InetAddress):
    """Custom type fsSyslogMailServAdd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsSyslogMailServAdd_Type.__name__ = "InetAddress"
_FsSyslogMailServAdd_Object = MibTableColumn
fsSyslogMailServAdd = _FsSyslogMailServAdd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 3),
    _FsSyslogMailServAdd_Type()
)
fsSyslogMailServAdd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSyslogMailServAdd.setStatus("current")


class _FsSyslogRxMailId_Type(DisplayString):
    """Custom type fsSyslogRxMailId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_FsSyslogRxMailId_Type.__name__ = "DisplayString"
_FsSyslogRxMailId_Object = MibTableColumn
fsSyslogRxMailId = _FsSyslogRxMailId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 4),
    _FsSyslogRxMailId_Type()
)
fsSyslogRxMailId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogRxMailId.setStatus("current")
_FsSyslogMailRowStatus_Type = RowStatus
_FsSyslogMailRowStatus_Object = MibTableColumn
fsSyslogMailRowStatus = _FsSyslogMailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 5),
    _FsSyslogMailRowStatus_Type()
)
fsSyslogMailRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogMailRowStatus.setStatus("current")


class _FsSyslogMailServUserName_Type(DisplayString):
    """Custom type fsSyslogMailServUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsSyslogMailServUserName_Type.__name__ = "DisplayString"
_FsSyslogMailServUserName_Object = MibTableColumn
fsSyslogMailServUserName = _FsSyslogMailServUserName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 6),
    _FsSyslogMailServUserName_Type()
)
fsSyslogMailServUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogMailServUserName.setStatus("current")


class _FsSyslogMailServPassword_Type(DisplayString):
    """Custom type fsSyslogMailServPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsSyslogMailServPassword_Type.__name__ = "DisplayString"
_FsSyslogMailServPassword_Object = MibTableColumn
fsSyslogMailServPassword = _FsSyslogMailServPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 4, 1, 7),
    _FsSyslogMailServPassword_Type()
)
fsSyslogMailServPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogMailServPassword.setStatus("current")


class _FsSyslogSmtpAuthMethod_Type(Integer32):
    """Custom type fsSyslogSmtpAuthMethod based on Integer32"""
    defaultValue = 1

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
        *(("noAuthenticate", 1),
          ("authLogin", 2),
          ("authPlain", 3),
          ("crammd5", 4),
          ("digestmd5", 5))
    )


_FsSyslogSmtpAuthMethod_Type.__name__ = "Integer32"
_FsSyslogSmtpAuthMethod_Object = MibScalar
fsSyslogSmtpAuthMethod = _FsSyslogSmtpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 3, 5),
    _FsSyslogSmtpAuthMethod_Type()
)
fsSyslogSmtpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSyslogSmtpAuthMethod.setStatus("current")
_FsSyslogSrvrUnreachableNotifications_ObjectIdentity = ObjectIdentity
fsSyslogSrvrUnreachableNotifications = _FsSyslogSrvrUnreachableNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4)
)
_SysLogTraps_ObjectIdentity = ObjectIdentity
sysLogTraps = _SysLogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4, 0)
)
_SysLogTrapObjects_ObjectIdentity = ObjectIdentity
sysLogTrapObjects = _SysLogTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4, 1)
)


class _SysLogSrvrUnreachEventTime_Type(DisplayString):
    """Custom type sysLogSrvrUnreachEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_SysLogSrvrUnreachEventTime_Type.__name__ = "DisplayString"
_SysLogSrvrUnreachEventTime_Object = MibScalar
sysLogSrvrUnreachEventTime = _SysLogSrvrUnreachEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4, 1, 1),
    _SysLogSrvrUnreachEventTime_Type()
)
sysLogSrvrUnreachEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysLogSrvrUnreachEventTime.setStatus("current")
_SysLogSrvrUnreachMessage_Type = DisplayString
_SysLogSrvrUnreachMessage_Object = MibScalar
sysLogSrvrUnreachMessage = _SysLogSrvrUnreachMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4, 1, 2),
    _SysLogSrvrUnreachMessage_Type()
)
sysLogSrvrUnreachMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysLogSrvrUnreachMessage.setStatus("current")

# Managed Objects groups


# Notification objects

sysLogSrvrUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 89, 4, 0, 1)
)
sysLogSrvrUnreachable.setObjects(
      *(("SUPERMICRO-SYSLOG-MIB", "sysLogSrvrUnreachEventTime"),
        ("SUPERMICRO-SYSLOG-MIB", "sysLogSrvrUnreachMessage"))
)
if mibBuilder.loadTexts:
    sysLogSrvrUnreachable.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-SYSLOG-MIB",
    **{"fsSyslog": fsSyslog,
       "fsSyslogGeneralGroup": fsSyslogGeneralGroup,
       "fsSyslogLogging": fsSyslogLogging,
       "fsSyslogTimeStamp": fsSyslogTimeStamp,
       "fsSyslogConsoleLog": fsSyslogConsoleLog,
       "fsSyslogSysBuffers": fsSyslogSysBuffers,
       "fsSyslogClearLog": fsSyslogClearLog,
       "fsSyslogConfigTable": fsSyslogConfigTable,
       "fsSyslogConfigEntry": fsSyslogConfigEntry,
       "fsSyslogConfigModule": fsSyslogConfigModule,
       "fsSyslogConfigLogLevel": fsSyslogConfigLogLevel,
       "fsSyslogFacility": fsSyslogFacility,
       "fsSyslogRole": fsSyslogRole,
       "fsSyslogLogFile": fsSyslogLogFile,
       "fsSyslogMail": fsSyslogMail,
       "fsSyslogProfile": fsSyslogProfile,
       "fsSyslogRelayPort": fsSyslogRelayPort,
       "fsSyslogRelayTransType": fsSyslogRelayTransType,
       "fsSyslogFileNameOne": fsSyslogFileNameOne,
       "fsSyslogFileNameTwo": fsSyslogFileNameTwo,
       "fsSyslogFileNameThree": fsSyslogFileNameThree,
       "fsSyslogFileTable": fsSyslogFileTable,
       "fsSyslogFileEntry": fsSyslogFileEntry,
       "fsSyslogFilePriority": fsSyslogFilePriority,
       "fsSyslogFileName": fsSyslogFileName,
       "fsSyslogFileRowStatus": fsSyslogFileRowStatus,
       "fsSyslogServerUpDownTrap": fsSyslogServerUpDownTrap,
       "fsSyslogLogs": fsSyslogLogs,
       "fsSyslogLogSrvAddr": fsSyslogLogSrvAddr,
       "fsSyslogLogNoLogServer": fsSyslogLogNoLogServer,
       "fsSyslogFwdTable": fsSyslogFwdTable,
       "fsSyslogFwdEntry": fsSyslogFwdEntry,
       "fsSyslogFwdPriority": fsSyslogFwdPriority,
       "fsSyslogFwdAddressType": fsSyslogFwdAddressType,
       "fsSyslogFwdServerIP": fsSyslogFwdServerIP,
       "fsSyslogFwdPort": fsSyslogFwdPort,
       "fsSyslogFwdTransType": fsSyslogFwdTransType,
       "fsSyslogFwdRowStatus": fsSyslogFwdRowStatus,
       "fsSyslogSmtp": fsSyslogSmtp,
       "fsSyslogSmtpSrvAddr": fsSyslogSmtpSrvAddr,
       "fsSyslogSmtpRcvrMailId": fsSyslogSmtpRcvrMailId,
       "fsSyslogSmtpSenderMailId": fsSyslogSmtpSenderMailId,
       "fsSyslogMailTable": fsSyslogMailTable,
       "fsSyslogMailEntry": fsSyslogMailEntry,
       "fsSyslogMailPriority": fsSyslogMailPriority,
       "fsSyslogMailServAddType": fsSyslogMailServAddType,
       "fsSyslogMailServAdd": fsSyslogMailServAdd,
       "fsSyslogRxMailId": fsSyslogRxMailId,
       "fsSyslogMailRowStatus": fsSyslogMailRowStatus,
       "fsSyslogMailServUserName": fsSyslogMailServUserName,
       "fsSyslogMailServPassword": fsSyslogMailServPassword,
       "fsSyslogSmtpAuthMethod": fsSyslogSmtpAuthMethod,
       "fsSyslogSrvrUnreachableNotifications": fsSyslogSrvrUnreachableNotifications,
       "sysLogTraps": sysLogTraps,
       "sysLogSrvrUnreachable": sysLogSrvrUnreachable,
       "sysLogTrapObjects": sysLogTrapObjects,
       "sysLogSrvrUnreachEventTime": sysLogSrvrUnreachEventTime,
       "sysLogSrvrUnreachMessage": sysLogSrvrUnreachMessage}
)
