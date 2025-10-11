# SNMP MIB module (DLINKSW-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKSW-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:12 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(SyslogFacility,
 SyslogSeverity) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogFacility",
    "SyslogSeverity")


# MODULE-IDENTITY

dlinkSwSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13)
)
if mibBuilder.loadTexts:
    dlinkSwSyslogMIB.setRevisions(
        ("2013-09-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
dSyslogMIBNotifications = _DSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 0)
)
_DSyslogMIBObjects_ObjectIdentity = ObjectIdentity
dSyslogMIBObjects = _DSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1)
)
_DSyslogGeneral_ObjectIdentity = ObjectIdentity
dSyslogGeneral = _DSyslogGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1)
)
_DSyslogSourceIfIndex_Type = InterfaceIndexOrZero
_DSyslogSourceIfIndex_Object = MibScalar
dSyslogSourceIfIndex = _DSyslogSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 1),
    _DSyslogSourceIfIndex_Type()
)
dSyslogSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogSourceIfIndex.setStatus("current")
_DSyslogDiscriminatorTable_Object = MibTable
dSyslogDiscriminatorTable = _DSyslogDiscriminatorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dSyslogDiscriminatorTable.setStatus("current")
_DSyslogDiscriminatorEntry_Object = MibTableRow
dSyslogDiscriminatorEntry = _DSyslogDiscriminatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1)
)
dSyslogDiscriminatorEntry.setIndexNames(
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogDiscriminatorName"),
)
if mibBuilder.loadTexts:
    dSyslogDiscriminatorEntry.setStatus("current")
_DSyslogDiscriminatorName_Type = DisplayString
_DSyslogDiscriminatorName_Object = MibTableColumn
dSyslogDiscriminatorName = _DSyslogDiscriminatorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 1),
    _DSyslogDiscriminatorName_Type()
)
dSyslogDiscriminatorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogDiscriminatorName.setStatus("current")
_DSyslogDiscriminatorRowstatus_Type = RowStatus
_DSyslogDiscriminatorRowstatus_Object = MibTableColumn
dSyslogDiscriminatorRowstatus = _DSyslogDiscriminatorRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 2),
    _DSyslogDiscriminatorRowstatus_Type()
)
dSyslogDiscriminatorRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogDiscriminatorRowstatus.setStatus("current")


class _DSyslogDisFacilityFilterMode_Type(Integer32):
    """Custom type dSyslogDisFacilityFilterMode based on Integer32"""
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
        *(("notSpecified", 1),
          ("drops", 2),
          ("includes", 3))
    )


_DSyslogDisFacilityFilterMode_Type.__name__ = "Integer32"
_DSyslogDisFacilityFilterMode_Object = MibTableColumn
dSyslogDisFacilityFilterMode = _DSyslogDisFacilityFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 3),
    _DSyslogDisFacilityFilterMode_Type()
)
dSyslogDisFacilityFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogDisFacilityFilterMode.setStatus("current")
_DSyslogDisFacilityFilterString_Type = DisplayString
_DSyslogDisFacilityFilterString_Object = MibTableColumn
dSyslogDisFacilityFilterString = _DSyslogDisFacilityFilterString_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 4),
    _DSyslogDisFacilityFilterString_Type()
)
dSyslogDisFacilityFilterString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogDisFacilityFilterString.setStatus("current")


class _DSyslogDisSeverityFilterMode_Type(Integer32):
    """Custom type dSyslogDisSeverityFilterMode based on Integer32"""
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
        *(("notSpecified", 1),
          ("drops", 2),
          ("includes", 3))
    )


_DSyslogDisSeverityFilterMode_Type.__name__ = "Integer32"
_DSyslogDisSeverityFilterMode_Object = MibTableColumn
dSyslogDisSeverityFilterMode = _DSyslogDisSeverityFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 5),
    _DSyslogDisSeverityFilterMode_Type()
)
dSyslogDisSeverityFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogDisSeverityFilterMode.setStatus("current")


class _DSyslogDisSeverityList_Type(Bits):
    """Custom type dSyslogDisSeverityList based on Bits"""
    namedValues = NamedValues(
        *(("emerg", 0),
          ("alert", 1),
          ("crit", 2),
          ("err", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )

_DSyslogDisSeverityList_Type.__name__ = "Bits"
_DSyslogDisSeverityList_Object = MibTableColumn
dSyslogDisSeverityList = _DSyslogDisSeverityList_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 2, 1, 6),
    _DSyslogDisSeverityList_Type()
)
dSyslogDisSeverityList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogDisSeverityList.setStatus("current")
_DSyslogLogOnEnabled_Type = TruthValue
_DSyslogLogOnEnabled_Object = MibScalar
dSyslogLogOnEnabled = _DSyslogLogOnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 3),
    _DSyslogLogOnEnabled_Type()
)
dSyslogLogOnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogOnEnabled.setStatus("current")
_DSyslogSourceIfType_Type = DisplayString
_DSyslogSourceIfType_Object = MibScalar
dSyslogSourceIfType = _DSyslogSourceIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 1, 4),
    _DSyslogSourceIfType_Type()
)
dSyslogSourceIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogSourceIfType.setStatus("current")
_DSyslogLogbuffer_ObjectIdentity = ObjectIdentity
dSyslogLogbuffer = _DSyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2)
)
if mibBuilder.loadTexts:
    dSyslogLogbuffer.setStatus("current")


class _DSyslogClearLogBuffer_Type(Integer32):
    """Custom type dSyslogClearLogBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DSyslogClearLogBuffer_Type.__name__ = "Integer32"
_DSyslogClearLogBuffer_Object = MibScalar
dSyslogClearLogBuffer = _DSyslogClearLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 1),
    _DSyslogClearLogBuffer_Type()
)
dSyslogClearLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogClearLogBuffer.setStatus("current")
_DSyslogLogBufferEnabled_Type = TruthValue
_DSyslogLogBufferEnabled_Object = MibScalar
dSyslogLogBufferEnabled = _DSyslogLogBufferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 2),
    _DSyslogLogBufferEnabled_Type()
)
dSyslogLogBufferEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogBufferEnabled.setStatus("current")
_DSyslogLogBufSeverity_Type = SyslogSeverity
_DSyslogLogBufSeverity_Object = MibScalar
dSyslogLogBufSeverity = _DSyslogLogBufSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 3),
    _DSyslogLogBufSeverity_Type()
)
dSyslogLogBufSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogBufSeverity.setStatus("current")
_DSyslogLogBufDiscriminator_Type = DisplayString
_DSyslogLogBufDiscriminator_Object = MibScalar
dSyslogLogBufDiscriminator = _DSyslogLogBufDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 4),
    _DSyslogLogBufDiscriminator_Type()
)
dSyslogLogBufDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogBufDiscriminator.setStatus("current")
_DSyslogLogBufWriteDelay_Type = Integer32
_DSyslogLogBufWriteDelay_Object = MibScalar
dSyslogLogBufWriteDelay = _DSyslogLogBufWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 5),
    _DSyslogLogBufWriteDelay_Type()
)
dSyslogLogBufWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogBufWriteDelay.setStatus("current")
if mibBuilder.loadTexts:
    dSyslogLogBufWriteDelay.setUnits("seconds")
_DSyslogClearAttackLogBufByUnit_Type = Integer32
_DSyslogClearAttackLogBufByUnit_Object = MibScalar
dSyslogClearAttackLogBufByUnit = _DSyslogClearAttackLogBufByUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 2, 6),
    _DSyslogClearAttackLogBufByUnit_Type()
)
dSyslogClearAttackLogBufByUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogClearAttackLogBufByUnit.setStatus("current")
_DSyslogLogConsole_ObjectIdentity = ObjectIdentity
dSyslogLogConsole = _DSyslogLogConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 3)
)
if mibBuilder.loadTexts:
    dSyslogLogConsole.setStatus("current")
_DSyslogLogConsoleEnabled_Type = TruthValue
_DSyslogLogConsoleEnabled_Object = MibScalar
dSyslogLogConsoleEnabled = _DSyslogLogConsoleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 3, 1),
    _DSyslogLogConsoleEnabled_Type()
)
dSyslogLogConsoleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogConsoleEnabled.setStatus("current")
_DSyslogLogConsoleSeverity_Type = SyslogSeverity
_DSyslogLogConsoleSeverity_Object = MibScalar
dSyslogLogConsoleSeverity = _DSyslogLogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 3, 2),
    _DSyslogLogConsoleSeverity_Type()
)
dSyslogLogConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogConsoleSeverity.setStatus("current")
_DSyslogLogConsoleDiscriminator_Type = DisplayString
_DSyslogLogConsoleDiscriminator_Object = MibScalar
dSyslogLogConsoleDiscriminator = _DSyslogLogConsoleDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 3, 3),
    _DSyslogLogConsoleDiscriminator_Type()
)
dSyslogLogConsoleDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogConsoleDiscriminator.setStatus("current")
_DSyslogLogSmtp_ObjectIdentity = ObjectIdentity
dSyslogLogSmtp = _DSyslogLogSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 4)
)
if mibBuilder.loadTexts:
    dSyslogLogSmtp.setStatus("current")
_DSyslogLogSmtpEnabled_Type = TruthValue
_DSyslogLogSmtpEnabled_Object = MibScalar
dSyslogLogSmtpEnabled = _DSyslogLogSmtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 4, 1),
    _DSyslogLogSmtpEnabled_Type()
)
dSyslogLogSmtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogSmtpEnabled.setStatus("current")
_DSyslogLogSmtpSeverity_Type = SyslogSeverity
_DSyslogLogSmtpSeverity_Object = MibScalar
dSyslogLogSmtpSeverity = _DSyslogLogSmtpSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 4, 2),
    _DSyslogLogSmtpSeverity_Type()
)
dSyslogLogSmtpSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogSmtpSeverity.setStatus("current")
_DSyslogLogSmtpDiscriminator_Type = DisplayString
_DSyslogLogSmtpDiscriminator_Object = MibScalar
dSyslogLogSmtpDiscriminator = _DSyslogLogSmtpDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 4, 3),
    _DSyslogLogSmtpDiscriminator_Type()
)
dSyslogLogSmtpDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSyslogLogSmtpDiscriminator.setStatus("current")
_DSyslogServerTable_Object = MibTable
dSyslogServerTable = _DSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5)
)
if mibBuilder.loadTexts:
    dSyslogServerTable.setStatus("current")
_DSyslogServerEntry_Object = MibTableRow
dSyslogServerEntry = _DSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1)
)
dSyslogServerEntry.setIndexNames(
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogServerAddressType"),
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogServerAddress"),
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogServerVrfName"),
)
if mibBuilder.loadTexts:
    dSyslogServerEntry.setStatus("current")
_DSyslogServerAddressType_Type = InetAddressType
_DSyslogServerAddressType_Object = MibTableColumn
dSyslogServerAddressType = _DSyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 1),
    _DSyslogServerAddressType_Type()
)
dSyslogServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogServerAddressType.setStatus("current")
_DSyslogServerAddress_Type = InetAddress
_DSyslogServerAddress_Object = MibTableColumn
dSyslogServerAddress = _DSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 2),
    _DSyslogServerAddress_Type()
)
dSyslogServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogServerAddress.setStatus("current")


class _DSyslogServerVrfName_Type(DisplayString):
    """Custom type dSyslogServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSyslogServerVrfName_Type.__name__ = "DisplayString"
_DSyslogServerVrfName_Object = MibTableColumn
dSyslogServerVrfName = _DSyslogServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 3),
    _DSyslogServerVrfName_Type()
)
dSyslogServerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogServerVrfName.setStatus("current")
_DSyslogServerRowstatus_Type = RowStatus
_DSyslogServerRowstatus_Object = MibTableColumn
dSyslogServerRowstatus = _DSyslogServerRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 4),
    _DSyslogServerRowstatus_Type()
)
dSyslogServerRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogServerRowstatus.setStatus("current")


class _DSyslogServerPort_Type(Unsigned32):
    """Custom type dSyslogServerPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(1024, 65535),
    )


_DSyslogServerPort_Type.__name__ = "Unsigned32"
_DSyslogServerPort_Object = MibTableColumn
dSyslogServerPort = _DSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 5),
    _DSyslogServerPort_Type()
)
dSyslogServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogServerPort.setStatus("current")


class _DSyslogServerSeverity_Type(SyslogSeverity):
    """Custom type dSyslogServerSeverity based on SyslogSeverity"""
    defaultValue = 4


_DSyslogServerSeverity_Type.__name__ = "SyslogSeverity"
_DSyslogServerSeverity_Object = MibTableColumn
dSyslogServerSeverity = _DSyslogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 6),
    _DSyslogServerSeverity_Type()
)
dSyslogServerSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogServerSeverity.setStatus("current")


class _DSyslogServerFacility_Type(SyslogFacility):
    """Custom type dSyslogServerFacility based on SyslogFacility"""
    defaultValue = 23


_DSyslogServerFacility_Type.__name__ = "SyslogFacility"
_DSyslogServerFacility_Object = MibTableColumn
dSyslogServerFacility = _DSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 7),
    _DSyslogServerFacility_Type()
)
dSyslogServerFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogServerFacility.setStatus("current")
_DSyslogServerDiscriminator_Type = DisplayString
_DSyslogServerDiscriminator_Object = MibTableColumn
dSyslogServerDiscriminator = _DSyslogServerDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 5, 1, 8),
    _DSyslogServerDiscriminator_Type()
)
dSyslogServerDiscriminator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSyslogServerDiscriminator.setStatus("current")
_DSyslogBufferTableNum_Type = Unsigned32
_DSyslogBufferTableNum_Object = MibScalar
dSyslogBufferTableNum = _DSyslogBufferTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 6),
    _DSyslogBufferTableNum_Type()
)
dSyslogBufferTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogBufferTableNum.setStatus("current")
_DSyslogBufferTable_Object = MibTable
dSyslogBufferTable = _DSyslogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 7)
)
if mibBuilder.loadTexts:
    dSyslogBufferTable.setStatus("current")
_DSyslogBufferEntry_Object = MibTableRow
dSyslogBufferEntry = _DSyslogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 7, 1)
)
dSyslogBufferEntry.setIndexNames(
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogBufferIndex"),
)
if mibBuilder.loadTexts:
    dSyslogBufferEntry.setStatus("current")


class _DSyslogBufferIndex_Type(Unsigned32):
    """Custom type dSyslogBufferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_DSyslogBufferIndex_Type.__name__ = "Unsigned32"
_DSyslogBufferIndex_Object = MibTableColumn
dSyslogBufferIndex = _DSyslogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 7, 1, 1),
    _DSyslogBufferIndex_Type()
)
dSyslogBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogBufferIndex.setStatus("current")
_DSyslogBufferDateAndTime_Type = DateAndTime
_DSyslogBufferDateAndTime_Object = MibTableColumn
dSyslogBufferDateAndTime = _DSyslogBufferDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 7, 1, 2),
    _DSyslogBufferDateAndTime_Type()
)
dSyslogBufferDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogBufferDateAndTime.setStatus("current")
_DSyslogBufferDescription_Type = DisplayString
_DSyslogBufferDescription_Object = MibTableColumn
dSyslogBufferDescription = _DSyslogBufferDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 7, 1, 3),
    _DSyslogBufferDescription_Type()
)
dSyslogBufferDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogBufferDescription.setStatus("current")
_DSyslogAttackLogTableNum_Type = Unsigned32
_DSyslogAttackLogTableNum_Object = MibScalar
dSyslogAttackLogTableNum = _DSyslogAttackLogTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 8),
    _DSyslogAttackLogTableNum_Type()
)
dSyslogAttackLogTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogAttackLogTableNum.setStatus("current")
_DSyslogAttackLogTable_Object = MibTable
dSyslogAttackLogTable = _DSyslogAttackLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9)
)
if mibBuilder.loadTexts:
    dSyslogAttackLogTable.setStatus("current")
_DSyslogAttackLogEntry_Object = MibTableRow
dSyslogAttackLogEntry = _DSyslogAttackLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9, 1)
)
dSyslogAttackLogEntry.setIndexNames(
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogAttackLogUnitId"),
    (0, "DLINKSW-SYSLOG-MIB", "dSyslogAttackLogIndex"),
)
if mibBuilder.loadTexts:
    dSyslogAttackLogEntry.setStatus("current")


class _DSyslogAttackLogUnitId_Type(Unsigned32):
    """Custom type dSyslogAttackLogUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DSyslogAttackLogUnitId_Type.__name__ = "Unsigned32"
_DSyslogAttackLogUnitId_Object = MibTableColumn
dSyslogAttackLogUnitId = _DSyslogAttackLogUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9, 1, 1),
    _DSyslogAttackLogUnitId_Type()
)
dSyslogAttackLogUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogAttackLogUnitId.setStatus("current")


class _DSyslogAttackLogIndex_Type(Unsigned32):
    """Custom type dSyslogAttackLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_DSyslogAttackLogIndex_Type.__name__ = "Unsigned32"
_DSyslogAttackLogIndex_Object = MibTableColumn
dSyslogAttackLogIndex = _DSyslogAttackLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9, 1, 2),
    _DSyslogAttackLogIndex_Type()
)
dSyslogAttackLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSyslogAttackLogIndex.setStatus("current")
_DSyslogAttackLogDateAndTime_Type = DateAndTime
_DSyslogAttackLogDateAndTime_Object = MibTableColumn
dSyslogAttackLogDateAndTime = _DSyslogAttackLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9, 1, 3),
    _DSyslogAttackLogDateAndTime_Type()
)
dSyslogAttackLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogAttackLogDateAndTime.setStatus("current")
_DSyslogAttackLogDescription_Type = DisplayString
_DSyslogAttackLogDescription_Object = MibTableColumn
dSyslogAttackLogDescription = _DSyslogAttackLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 1, 9, 1, 4),
    _DSyslogAttackLogDescription_Type()
)
dSyslogAttackLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSyslogAttackLogDescription.setStatus("current")
_DSyslogMIBConformance_ObjectIdentity = ObjectIdentity
dSyslogMIBConformance = _DSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2)
)
_DSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
dSyslogMIBCompliances = _DSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1)
)
_DSyslogMIBGroups_ObjectIdentity = ObjectIdentity
dSyslogMIBGroups = _DSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2)
)

# Managed Objects groups

dSyslogGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 1)
)
dSyslogGeneralGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogClearLogBuffer"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogBufferEnabled"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogBufSeverity"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogBufDiscriminator"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogBufWriteDelay"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogBufferTableNum"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogBufferDateAndTime"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogBufferDescription"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogOnEnabled"))
)
if mibBuilder.loadTexts:
    dSyslogGeneralGroup.setStatus("current")

dSyslogDiscriminatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 2)
)
dSyslogDiscriminatorGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogDiscriminatorRowstatus"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogDisFacilityFilterMode"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogDisFacilityFilterString"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogDisSeverityFilterMode"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogDisSeverityList"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogBufDiscriminator"))
)
if mibBuilder.loadTexts:
    dSyslogDiscriminatorGroup.setStatus("current")

dSyslogLogConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 3)
)
dSyslogLogConsoleGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogLogConsoleEnabled"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogConsoleSeverity"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogConsoleDiscriminator"))
)
if mibBuilder.loadTexts:
    dSyslogLogConsoleGroup.setStatus("current")

dSyslogLogSmtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 4)
)
dSyslogLogSmtpGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogLogSmtpEnabled"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogSmtpSeverity"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogSmtpDiscriminator"))
)
if mibBuilder.loadTexts:
    dSyslogLogSmtpGroup.setStatus("current")

dSyslogLogServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 5)
)
dSyslogLogServerGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogSourceIfIndex"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogServerRowstatus"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogServerPort"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogServerSeverity"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogServerFacility"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogServerDiscriminator"))
)
if mibBuilder.loadTexts:
    dSyslogLogServerGroup.setStatus("current")

dSyslogAttackLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 2, 6)
)
dSyslogAttackLogGroup.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogClearAttackLogBufByUnit"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogAttackLogTableNum"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogAttackLogDateAndTime"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogAttackLogDescription"))
)
if mibBuilder.loadTexts:
    dSyslogAttackLogGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dSyslogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 13, 2, 1, 1)
)
dSyslogMIBCompliance.setObjects(
      *(("DLINKSW-SYSLOG-MIB", "dSyslogGeneralGroup"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogDiscriminatorGroup"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogConsoleGroup"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogSmtpGroup"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogLogServerGroup"),
        ("DLINKSW-SYSLOG-MIB", "dSyslogAttackLogGroup"))
)
if mibBuilder.loadTexts:
    dSyslogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SYSLOG-MIB",
    **{"dlinkSwSyslogMIB": dlinkSwSyslogMIB,
       "dSyslogMIBNotifications": dSyslogMIBNotifications,
       "dSyslogMIBObjects": dSyslogMIBObjects,
       "dSyslogGeneral": dSyslogGeneral,
       "dSyslogSourceIfIndex": dSyslogSourceIfIndex,
       "dSyslogDiscriminatorTable": dSyslogDiscriminatorTable,
       "dSyslogDiscriminatorEntry": dSyslogDiscriminatorEntry,
       "dSyslogDiscriminatorName": dSyslogDiscriminatorName,
       "dSyslogDiscriminatorRowstatus": dSyslogDiscriminatorRowstatus,
       "dSyslogDisFacilityFilterMode": dSyslogDisFacilityFilterMode,
       "dSyslogDisFacilityFilterString": dSyslogDisFacilityFilterString,
       "dSyslogDisSeverityFilterMode": dSyslogDisSeverityFilterMode,
       "dSyslogDisSeverityList": dSyslogDisSeverityList,
       "dSyslogLogOnEnabled": dSyslogLogOnEnabled,
       "dSyslogSourceIfType": dSyslogSourceIfType,
       "dSyslogLogbuffer": dSyslogLogbuffer,
       "dSyslogClearLogBuffer": dSyslogClearLogBuffer,
       "dSyslogLogBufferEnabled": dSyslogLogBufferEnabled,
       "dSyslogLogBufSeverity": dSyslogLogBufSeverity,
       "dSyslogLogBufDiscriminator": dSyslogLogBufDiscriminator,
       "dSyslogLogBufWriteDelay": dSyslogLogBufWriteDelay,
       "dSyslogClearAttackLogBufByUnit": dSyslogClearAttackLogBufByUnit,
       "dSyslogLogConsole": dSyslogLogConsole,
       "dSyslogLogConsoleEnabled": dSyslogLogConsoleEnabled,
       "dSyslogLogConsoleSeverity": dSyslogLogConsoleSeverity,
       "dSyslogLogConsoleDiscriminator": dSyslogLogConsoleDiscriminator,
       "dSyslogLogSmtp": dSyslogLogSmtp,
       "dSyslogLogSmtpEnabled": dSyslogLogSmtpEnabled,
       "dSyslogLogSmtpSeverity": dSyslogLogSmtpSeverity,
       "dSyslogLogSmtpDiscriminator": dSyslogLogSmtpDiscriminator,
       "dSyslogServerTable": dSyslogServerTable,
       "dSyslogServerEntry": dSyslogServerEntry,
       "dSyslogServerAddressType": dSyslogServerAddressType,
       "dSyslogServerAddress": dSyslogServerAddress,
       "dSyslogServerVrfName": dSyslogServerVrfName,
       "dSyslogServerRowstatus": dSyslogServerRowstatus,
       "dSyslogServerPort": dSyslogServerPort,
       "dSyslogServerSeverity": dSyslogServerSeverity,
       "dSyslogServerFacility": dSyslogServerFacility,
       "dSyslogServerDiscriminator": dSyslogServerDiscriminator,
       "dSyslogBufferTableNum": dSyslogBufferTableNum,
       "dSyslogBufferTable": dSyslogBufferTable,
       "dSyslogBufferEntry": dSyslogBufferEntry,
       "dSyslogBufferIndex": dSyslogBufferIndex,
       "dSyslogBufferDateAndTime": dSyslogBufferDateAndTime,
       "dSyslogBufferDescription": dSyslogBufferDescription,
       "dSyslogAttackLogTableNum": dSyslogAttackLogTableNum,
       "dSyslogAttackLogTable": dSyslogAttackLogTable,
       "dSyslogAttackLogEntry": dSyslogAttackLogEntry,
       "dSyslogAttackLogUnitId": dSyslogAttackLogUnitId,
       "dSyslogAttackLogIndex": dSyslogAttackLogIndex,
       "dSyslogAttackLogDateAndTime": dSyslogAttackLogDateAndTime,
       "dSyslogAttackLogDescription": dSyslogAttackLogDescription,
       "dSyslogMIBConformance": dSyslogMIBConformance,
       "dSyslogMIBCompliances": dSyslogMIBCompliances,
       "dSyslogMIBCompliance": dSyslogMIBCompliance,
       "dSyslogMIBGroups": dSyslogMIBGroups,
       "dSyslogGeneralGroup": dSyslogGeneralGroup,
       "dSyslogDiscriminatorGroup": dSyslogDiscriminatorGroup,
       "dSyslogLogConsoleGroup": dSyslogLogConsoleGroup,
       "dSyslogLogSmtpGroup": dSyslogLogSmtpGroup,
       "dSyslogLogServerGroup": dSyslogLogServerGroup,
       "dSyslogAttackLogGroup": dSyslogAttackLogGroup}
)
