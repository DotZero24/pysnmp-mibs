# SNMP MIB module (FSSNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/FSSNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:50 2025
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

fsSntpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149)
)
if mibBuilder.loadTexts:
    fsSntpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSntp_ObjectIdentity = ObjectIdentity
fsSntp = _FsSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1)
)
_FsSntpScalars_ObjectIdentity = ObjectIdentity
fsSntpScalars = _FsSntpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1)
)


class _FsSntpGlobalTrace_Type(Integer32):
    """Custom type fsSntpGlobalTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSntpGlobalTrace_Type.__name__ = "Integer32"
_FsSntpGlobalTrace_Object = MibScalar
fsSntpGlobalTrace = _FsSntpGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 1),
    _FsSntpGlobalTrace_Type()
)
fsSntpGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGlobalTrace.setStatus("current")


class _FsSntpGlobalDebug_Type(Integer32):
    """Custom type fsSntpGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSntpGlobalDebug_Type.__name__ = "Integer32"
_FsSntpGlobalDebug_Object = MibScalar
fsSntpGlobalDebug = _FsSntpGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 2),
    _FsSntpGlobalDebug_Type()
)
fsSntpGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGlobalDebug.setStatus("current")


class _FsSntpAdminStatus_Type(Integer32):
    """Custom type fsSntpAdminStatus based on Integer32"""
    defaultValue = 0

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


_FsSntpAdminStatus_Type.__name__ = "Integer32"
_FsSntpAdminStatus_Object = MibScalar
fsSntpAdminStatus = _FsSntpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 3),
    _FsSntpAdminStatus_Type()
)
fsSntpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAdminStatus.setStatus("current")


class _FsSntpClientVersion_Type(Integer32):
    """Custom type fsSntpClientVersion based on Integer32"""
    defaultValue = 4

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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_FsSntpClientVersion_Type.__name__ = "Integer32"
_FsSntpClientVersion_Object = MibScalar
fsSntpClientVersion = _FsSntpClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 4),
    _FsSntpClientVersion_Type()
)
fsSntpClientVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpClientVersion.setStatus("current")


class _FsSntpClientAddressingMode_Type(Integer32):
    """Custom type fsSntpClientAddressingMode based on Integer32"""
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
        *(("unicast", 1),
          ("broadcast", 2),
          ("multicast", 3),
          ("manycast", 4))
    )


_FsSntpClientAddressingMode_Type.__name__ = "Integer32"
_FsSntpClientAddressingMode_Object = MibScalar
fsSntpClientAddressingMode = _FsSntpClientAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 5),
    _FsSntpClientAddressingMode_Type()
)
fsSntpClientAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpClientAddressingMode.setStatus("current")


class _FsSntpClientPort_Type(Integer32):
    """Custom type fsSntpClientPort based on Integer32"""
    defaultValue = 123

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(123, 123),
        ValueRangeConstraint(1025, 65535),
    )


_FsSntpClientPort_Type.__name__ = "Integer32"
_FsSntpClientPort_Object = MibScalar
fsSntpClientPort = _FsSntpClientPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 6),
    _FsSntpClientPort_Type()
)
fsSntpClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpClientPort.setStatus("current")


class _FsSntpTimeDisplayFormat_Type(Integer32):
    """Custom type fsSntpTimeDisplayFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hours", 1),
          ("ampm", 2))
    )


_FsSntpTimeDisplayFormat_Type.__name__ = "Integer32"
_FsSntpTimeDisplayFormat_Object = MibScalar
fsSntpTimeDisplayFormat = _FsSntpTimeDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 7),
    _FsSntpTimeDisplayFormat_Type()
)
fsSntpTimeDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpTimeDisplayFormat.setStatus("current")
_FsSntpAuthKeyId_Type = Integer32
_FsSntpAuthKeyId_Object = MibScalar
fsSntpAuthKeyId = _FsSntpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 8),
    _FsSntpAuthKeyId_Type()
)
fsSntpAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAuthKeyId.setStatus("current")


class _FsSntpAuthAlgorithm_Type(Integer32):
    """Custom type fsSntpAuthAlgorithm based on Integer32"""
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
        *(("none", 0),
          ("md5", 1),
          ("des", 2))
    )


_FsSntpAuthAlgorithm_Type.__name__ = "Integer32"
_FsSntpAuthAlgorithm_Object = MibScalar
fsSntpAuthAlgorithm = _FsSntpAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 9),
    _FsSntpAuthAlgorithm_Type()
)
fsSntpAuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAuthAlgorithm.setStatus("current")


class _FsSntpAuthKey_Type(OctetString):
    """Custom type fsSntpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsSntpAuthKey_Type.__name__ = "OctetString"
_FsSntpAuthKey_Object = MibScalar
fsSntpAuthKey = _FsSntpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 10),
    _FsSntpAuthKey_Type()
)
fsSntpAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAuthKey.setStatus("current")


class _FsSntpTimeZone_Type(DisplayString):
    """Custom type fsSntpTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsSntpTimeZone_Type.__name__ = "DisplayString"
_FsSntpTimeZone_Object = MibScalar
fsSntpTimeZone = _FsSntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 11),
    _FsSntpTimeZone_Type()
)
fsSntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpTimeZone.setStatus("current")


class _FsSntpDSTStartTime_Type(DisplayString):
    """Custom type fsSntpDSTStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_FsSntpDSTStartTime_Type.__name__ = "DisplayString"
_FsSntpDSTStartTime_Object = MibScalar
fsSntpDSTStartTime = _FsSntpDSTStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 12),
    _FsSntpDSTStartTime_Type()
)
fsSntpDSTStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpDSTStartTime.setStatus("current")


class _FsSntpDSTEndTime_Type(DisplayString):
    """Custom type fsSntpDSTEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_FsSntpDSTEndTime_Type.__name__ = "DisplayString"
_FsSntpDSTEndTime_Object = MibScalar
fsSntpDSTEndTime = _FsSntpDSTEndTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 13),
    _FsSntpDSTEndTime_Type()
)
fsSntpDSTEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpDSTEndTime.setStatus("current")
_FsSntpClientUptime_Type = Unsigned32
_FsSntpClientUptime_Object = MibScalar
fsSntpClientUptime = _FsSntpClientUptime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 14),
    _FsSntpClientUptime_Type()
)
fsSntpClientUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpClientUptime.setStatus("current")


class _FsSntpClientStatus_Type(Integer32):
    """Custom type fsSntpClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 1),
          ("notSynchronized", 2),
          ("noneConfigured", 3),
          ("syncToLocal", 4),
          ("syncToRemoteServer", 5),
          ("unknown", 99))
    )


_FsSntpClientStatus_Type.__name__ = "Integer32"
_FsSntpClientStatus_Object = MibScalar
fsSntpClientStatus = _FsSntpClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 15),
    _FsSntpClientStatus_Type()
)
fsSntpClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpClientStatus.setStatus("current")
_FsSntpServerReplyRxCount_Type = Counter32
_FsSntpServerReplyRxCount_Object = MibScalar
fsSntpServerReplyRxCount = _FsSntpServerReplyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 16),
    _FsSntpServerReplyRxCount_Type()
)
fsSntpServerReplyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpServerReplyRxCount.setStatus("current")
_FsSntpClientReqTxCount_Type = Counter32
_FsSntpClientReqTxCount_Object = MibScalar
fsSntpClientReqTxCount = _FsSntpClientReqTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 17),
    _FsSntpClientReqTxCount_Type()
)
fsSntpClientReqTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpClientReqTxCount.setStatus("current")
_FsSntpPktInDiscardCount_Type = Counter32
_FsSntpPktInDiscardCount_Object = MibScalar
fsSntpPktInDiscardCount = _FsSntpPktInDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 1, 18),
    _FsSntpPktInDiscardCount_Type()
)
fsSntpPktInDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPktInDiscardCount.setStatus("current")
_FsSntpUnicast_ObjectIdentity = ObjectIdentity
fsSntpUnicast = _FsSntpUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2)
)


class _FsSntpServerAutoDiscovery_Type(Integer32):
    """Custom type fsSntpServerAutoDiscovery based on Integer32"""
    defaultValue = 0

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


_FsSntpServerAutoDiscovery_Type.__name__ = "Integer32"
_FsSntpServerAutoDiscovery_Object = MibScalar
fsSntpServerAutoDiscovery = _FsSntpServerAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 1),
    _FsSntpServerAutoDiscovery_Type()
)
fsSntpServerAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpServerAutoDiscovery.setStatus("current")


class _FsSntpUnicastPollInterval_Type(Unsigned32):
    """Custom type fsSntpUnicastPollInterval based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16284),
    )


_FsSntpUnicastPollInterval_Type.__name__ = "Unsigned32"
_FsSntpUnicastPollInterval_Object = MibScalar
fsSntpUnicastPollInterval = _FsSntpUnicastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 2),
    _FsSntpUnicastPollInterval_Type()
)
fsSntpUnicastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpUnicastPollInterval.setUnits("seconds")


class _FsSntpUnicastPollTimeout_Type(Unsigned32):
    """Custom type fsSntpUnicastPollTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FsSntpUnicastPollTimeout_Type.__name__ = "Unsigned32"
_FsSntpUnicastPollTimeout_Object = MibScalar
fsSntpUnicastPollTimeout = _FsSntpUnicastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 3),
    _FsSntpUnicastPollTimeout_Type()
)
fsSntpUnicastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpUnicastPollTimeout.setUnits("seconds")


class _FsSntpUnicastPollRetry_Type(Unsigned32):
    """Custom type fsSntpUnicastPollRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsSntpUnicastPollRetry_Type.__name__ = "Unsigned32"
_FsSntpUnicastPollRetry_Object = MibScalar
fsSntpUnicastPollRetry = _FsSntpUnicastPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 4),
    _FsSntpUnicastPollRetry_Type()
)
fsSntpUnicastPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastPollRetry.setStatus("current")
_FsSntpUnicastServerTable_Object = MibTable
fsSntpUnicastServerTable = _FsSntpUnicastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsSntpUnicastServerTable.setStatus("current")
_FsSntpUnicastServerEntry_Object = MibTableRow
fsSntpUnicastServerEntry = _FsSntpUnicastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1)
)
fsSntpUnicastServerEntry.setIndexNames(
    (0, "FSSNTP-MIB", "fsSntpUnicastServerAddrType"),
    (0, "FSSNTP-MIB", "fsSntpUnicastServerAddr"),
)
if mibBuilder.loadTexts:
    fsSntpUnicastServerEntry.setStatus("current")
_FsSntpUnicastServerAddrType_Type = InetAddressType
_FsSntpUnicastServerAddrType_Object = MibTableColumn
fsSntpUnicastServerAddrType = _FsSntpUnicastServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 1),
    _FsSntpUnicastServerAddrType_Type()
)
fsSntpUnicastServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSntpUnicastServerAddrType.setStatus("current")
_FsSntpUnicastServerAddr_Type = InetAddress
_FsSntpUnicastServerAddr_Object = MibTableColumn
fsSntpUnicastServerAddr = _FsSntpUnicastServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 2),
    _FsSntpUnicastServerAddr_Type()
)
fsSntpUnicastServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSntpUnicastServerAddr.setStatus("current")


class _FsSntpUnicastServerVersion_Type(Integer32):
    """Custom type fsSntpUnicastServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3", 3),
          ("version4", 4))
    )


_FsSntpUnicastServerVersion_Type.__name__ = "Integer32"
_FsSntpUnicastServerVersion_Object = MibTableColumn
fsSntpUnicastServerVersion = _FsSntpUnicastServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 3),
    _FsSntpUnicastServerVersion_Type()
)
fsSntpUnicastServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastServerVersion.setStatus("current")


class _FsSntpUnicastServerPort_Type(Integer32):
    """Custom type fsSntpUnicastServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(123, 123),
        ValueRangeConstraint(1025, 65535),
    )


_FsSntpUnicastServerPort_Type.__name__ = "Integer32"
_FsSntpUnicastServerPort_Object = MibTableColumn
fsSntpUnicastServerPort = _FsSntpUnicastServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 4),
    _FsSntpUnicastServerPort_Type()
)
fsSntpUnicastServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastServerPort.setStatus("current")


class _FsSntpUnicastServerType_Type(Integer32):
    """Custom type fsSntpUnicastServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_FsSntpUnicastServerType_Type.__name__ = "Integer32"
_FsSntpUnicastServerType_Object = MibTableColumn
fsSntpUnicastServerType = _FsSntpUnicastServerType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 5),
    _FsSntpUnicastServerType_Type()
)
fsSntpUnicastServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastServerType.setStatus("current")
_FsSntpUnicastServerLastUpdateTime_Type = DisplayString
_FsSntpUnicastServerLastUpdateTime_Object = MibTableColumn
fsSntpUnicastServerLastUpdateTime = _FsSntpUnicastServerLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 6),
    _FsSntpUnicastServerLastUpdateTime_Type()
)
fsSntpUnicastServerLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpUnicastServerLastUpdateTime.setStatus("current")
_FsSntpUnicastServerTxRequests_Type = Counter32
_FsSntpUnicastServerTxRequests_Object = MibTableColumn
fsSntpUnicastServerTxRequests = _FsSntpUnicastServerTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 7),
    _FsSntpUnicastServerTxRequests_Type()
)
fsSntpUnicastServerTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpUnicastServerTxRequests.setStatus("current")
_FsSntpUnicastServerRowStatus_Type = RowStatus
_FsSntpUnicastServerRowStatus_Object = MibTableColumn
fsSntpUnicastServerRowStatus = _FsSntpUnicastServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 2, 5, 1, 8),
    _FsSntpUnicastServerRowStatus_Type()
)
fsSntpUnicastServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpUnicastServerRowStatus.setStatus("current")
_FsSntpBroadcast_ObjectIdentity = ObjectIdentity
fsSntpBroadcast = _FsSntpBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3)
)


class _FsSntpSendRequestInBcastMode_Type(Integer32):
    """Custom type fsSntpSendRequestInBcastMode based on Integer32"""
    defaultValue = 0

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


_FsSntpSendRequestInBcastMode_Type.__name__ = "Integer32"
_FsSntpSendRequestInBcastMode_Object = MibScalar
fsSntpSendRequestInBcastMode = _FsSntpSendRequestInBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3, 1),
    _FsSntpSendRequestInBcastMode_Type()
)
fsSntpSendRequestInBcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpSendRequestInBcastMode.setStatus("current")


class _FsSntpPollTimeoutInBcastMode_Type(Unsigned32):
    """Custom type fsSntpPollTimeoutInBcastMode based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FsSntpPollTimeoutInBcastMode_Type.__name__ = "Unsigned32"
_FsSntpPollTimeoutInBcastMode_Object = MibScalar
fsSntpPollTimeoutInBcastMode = _FsSntpPollTimeoutInBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3, 2),
    _FsSntpPollTimeoutInBcastMode_Type()
)
fsSntpPollTimeoutInBcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpPollTimeoutInBcastMode.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpPollTimeoutInBcastMode.setUnits("seconds")


class _FsSntpDelayTimeInBcastMode_Type(Unsigned32):
    """Custom type fsSntpDelayTimeInBcastMode based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 15000),
    )


_FsSntpDelayTimeInBcastMode_Type.__name__ = "Unsigned32"
_FsSntpDelayTimeInBcastMode_Object = MibScalar
fsSntpDelayTimeInBcastMode = _FsSntpDelayTimeInBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3, 3),
    _FsSntpDelayTimeInBcastMode_Type()
)
fsSntpDelayTimeInBcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpDelayTimeInBcastMode.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpDelayTimeInBcastMode.setUnits("microseconds")
_FsSntpPrimaryServerAddrInBcastMode_Type = IpAddress
_FsSntpPrimaryServerAddrInBcastMode_Object = MibScalar
fsSntpPrimaryServerAddrInBcastMode = _FsSntpPrimaryServerAddrInBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3, 4),
    _FsSntpPrimaryServerAddrInBcastMode_Type()
)
fsSntpPrimaryServerAddrInBcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPrimaryServerAddrInBcastMode.setStatus("current")
_FsSntpSecondaryServerAddrInBcastMode_Type = IpAddress
_FsSntpSecondaryServerAddrInBcastMode_Object = MibScalar
fsSntpSecondaryServerAddrInBcastMode = _FsSntpSecondaryServerAddrInBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 3, 5),
    _FsSntpSecondaryServerAddrInBcastMode_Type()
)
fsSntpSecondaryServerAddrInBcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpSecondaryServerAddrInBcastMode.setStatus("current")
_FsSntpMulticast_ObjectIdentity = ObjectIdentity
fsSntpMulticast = _FsSntpMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4)
)


class _FsSntpSendRequestInMcastMode_Type(Integer32):
    """Custom type fsSntpSendRequestInMcastMode based on Integer32"""
    defaultValue = 0

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


_FsSntpSendRequestInMcastMode_Type.__name__ = "Integer32"
_FsSntpSendRequestInMcastMode_Object = MibScalar
fsSntpSendRequestInMcastMode = _FsSntpSendRequestInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 1),
    _FsSntpSendRequestInMcastMode_Type()
)
fsSntpSendRequestInMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpSendRequestInMcastMode.setStatus("current")


class _FsSntpPollTimeoutInMcastMode_Type(Unsigned32):
    """Custom type fsSntpPollTimeoutInMcastMode based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FsSntpPollTimeoutInMcastMode_Type.__name__ = "Unsigned32"
_FsSntpPollTimeoutInMcastMode_Object = MibScalar
fsSntpPollTimeoutInMcastMode = _FsSntpPollTimeoutInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 2),
    _FsSntpPollTimeoutInMcastMode_Type()
)
fsSntpPollTimeoutInMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpPollTimeoutInMcastMode.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpPollTimeoutInMcastMode.setUnits("seconds")


class _FsSntpDelayTimeInMcastMode_Type(Unsigned32):
    """Custom type fsSntpDelayTimeInMcastMode based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 15000),
    )


_FsSntpDelayTimeInMcastMode_Type.__name__ = "Unsigned32"
_FsSntpDelayTimeInMcastMode_Object = MibScalar
fsSntpDelayTimeInMcastMode = _FsSntpDelayTimeInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 3),
    _FsSntpDelayTimeInMcastMode_Type()
)
fsSntpDelayTimeInMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpDelayTimeInMcastMode.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpDelayTimeInMcastMode.setUnits("microseconds")
_FsSntpGrpAddrTypeInMcastMode_Type = InetAddressType
_FsSntpGrpAddrTypeInMcastMode_Object = MibScalar
fsSntpGrpAddrTypeInMcastMode = _FsSntpGrpAddrTypeInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 4),
    _FsSntpGrpAddrTypeInMcastMode_Type()
)
fsSntpGrpAddrTypeInMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGrpAddrTypeInMcastMode.setStatus("current")
_FsSntpGrpAddrInMcastMode_Type = InetAddress
_FsSntpGrpAddrInMcastMode_Object = MibScalar
fsSntpGrpAddrInMcastMode = _FsSntpGrpAddrInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 5),
    _FsSntpGrpAddrInMcastMode_Type()
)
fsSntpGrpAddrInMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGrpAddrInMcastMode.setStatus("current")
_FsSntpPrimaryServerAddrTypeInMcastMode_Type = InetAddressType
_FsSntpPrimaryServerAddrTypeInMcastMode_Object = MibScalar
fsSntpPrimaryServerAddrTypeInMcastMode = _FsSntpPrimaryServerAddrTypeInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 6),
    _FsSntpPrimaryServerAddrTypeInMcastMode_Type()
)
fsSntpPrimaryServerAddrTypeInMcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPrimaryServerAddrTypeInMcastMode.setStatus("current")
_FsSntpPrimaryServerAddrInMcastMode_Type = InetAddress
_FsSntpPrimaryServerAddrInMcastMode_Object = MibScalar
fsSntpPrimaryServerAddrInMcastMode = _FsSntpPrimaryServerAddrInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 7),
    _FsSntpPrimaryServerAddrInMcastMode_Type()
)
fsSntpPrimaryServerAddrInMcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPrimaryServerAddrInMcastMode.setStatus("current")
_FsSntpSecondaryServerAddrTypeInMcastMode_Type = InetAddressType
_FsSntpSecondaryServerAddrTypeInMcastMode_Object = MibScalar
fsSntpSecondaryServerAddrTypeInMcastMode = _FsSntpSecondaryServerAddrTypeInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 8),
    _FsSntpSecondaryServerAddrTypeInMcastMode_Type()
)
fsSntpSecondaryServerAddrTypeInMcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpSecondaryServerAddrTypeInMcastMode.setStatus("current")
_FsSntpSecondaryServerAddrInMcastMode_Type = InetAddress
_FsSntpSecondaryServerAddrInMcastMode_Object = MibScalar
fsSntpSecondaryServerAddrInMcastMode = _FsSntpSecondaryServerAddrInMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 4, 9),
    _FsSntpSecondaryServerAddrInMcastMode_Type()
)
fsSntpSecondaryServerAddrInMcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpSecondaryServerAddrInMcastMode.setStatus("current")
_FsSntpAnycast_ObjectIdentity = ObjectIdentity
fsSntpAnycast = _FsSntpAnycast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5)
)


class _FsSntpAnycastPollInterval_Type(Unsigned32):
    """Custom type fsSntpAnycastPollInterval based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 16284),
    )


_FsSntpAnycastPollInterval_Type.__name__ = "Unsigned32"
_FsSntpAnycastPollInterval_Object = MibScalar
fsSntpAnycastPollInterval = _FsSntpAnycastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 1),
    _FsSntpAnycastPollInterval_Type()
)
fsSntpAnycastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAnycastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpAnycastPollInterval.setUnits("seconds")


class _FsSntpAnycastPollTimeout_Type(Unsigned32):
    """Custom type fsSntpAnycastPollTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FsSntpAnycastPollTimeout_Type.__name__ = "Unsigned32"
_FsSntpAnycastPollTimeout_Object = MibScalar
fsSntpAnycastPollTimeout = _FsSntpAnycastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 2),
    _FsSntpAnycastPollTimeout_Type()
)
fsSntpAnycastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAnycastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fsSntpAnycastPollTimeout.setUnits("seconds")


class _FsSntpAnycastPollRetry_Type(Unsigned32):
    """Custom type fsSntpAnycastPollRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsSntpAnycastPollRetry_Type.__name__ = "Unsigned32"
_FsSntpAnycastPollRetry_Object = MibScalar
fsSntpAnycastPollRetry = _FsSntpAnycastPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 3),
    _FsSntpAnycastPollRetry_Type()
)
fsSntpAnycastPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpAnycastPollRetry.setStatus("current")


class _FsSntpServerTypeInAcastMode_Type(Integer32):
    """Custom type fsSntpServerTypeInAcastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2))
    )


_FsSntpServerTypeInAcastMode_Type.__name__ = "Integer32"
_FsSntpServerTypeInAcastMode_Object = MibScalar
fsSntpServerTypeInAcastMode = _FsSntpServerTypeInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 4),
    _FsSntpServerTypeInAcastMode_Type()
)
fsSntpServerTypeInAcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpServerTypeInAcastMode.setStatus("current")
_FsSntpGrpAddrTypeInAcastMode_Type = InetAddressType
_FsSntpGrpAddrTypeInAcastMode_Object = MibScalar
fsSntpGrpAddrTypeInAcastMode = _FsSntpGrpAddrTypeInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 5),
    _FsSntpGrpAddrTypeInAcastMode_Type()
)
fsSntpGrpAddrTypeInAcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGrpAddrTypeInAcastMode.setStatus("current")
_FsSntpGrpAddrInAcastMode_Type = InetAddress
_FsSntpGrpAddrInAcastMode_Object = MibScalar
fsSntpGrpAddrInAcastMode = _FsSntpGrpAddrInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 6),
    _FsSntpGrpAddrInAcastMode_Type()
)
fsSntpGrpAddrInAcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSntpGrpAddrInAcastMode.setStatus("current")
_FsSntpPrimaryServerAddrTypeInAcastMode_Type = InetAddressType
_FsSntpPrimaryServerAddrTypeInAcastMode_Object = MibScalar
fsSntpPrimaryServerAddrTypeInAcastMode = _FsSntpPrimaryServerAddrTypeInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 7),
    _FsSntpPrimaryServerAddrTypeInAcastMode_Type()
)
fsSntpPrimaryServerAddrTypeInAcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPrimaryServerAddrTypeInAcastMode.setStatus("current")
_FsSntpPrimaryServerAddrInAcastMode_Type = InetAddress
_FsSntpPrimaryServerAddrInAcastMode_Object = MibScalar
fsSntpPrimaryServerAddrInAcastMode = _FsSntpPrimaryServerAddrInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 8),
    _FsSntpPrimaryServerAddrInAcastMode_Type()
)
fsSntpPrimaryServerAddrInAcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpPrimaryServerAddrInAcastMode.setStatus("current")
_FsSntpSecondaryServerAddrTypeInAcastMode_Type = InetAddressType
_FsSntpSecondaryServerAddrTypeInAcastMode_Object = MibScalar
fsSntpSecondaryServerAddrTypeInAcastMode = _FsSntpSecondaryServerAddrTypeInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 9),
    _FsSntpSecondaryServerAddrTypeInAcastMode_Type()
)
fsSntpSecondaryServerAddrTypeInAcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpSecondaryServerAddrTypeInAcastMode.setStatus("obsolete")
_FsSntpSecondaryServerAddrInAcastMode_Type = InetAddress
_FsSntpSecondaryServerAddrInAcastMode_Object = MibScalar
fsSntpSecondaryServerAddrInAcastMode = _FsSntpSecondaryServerAddrInAcastMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 149, 1, 5, 10),
    _FsSntpSecondaryServerAddrInAcastMode_Type()
)
fsSntpSecondaryServerAddrInAcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSntpSecondaryServerAddrInAcastMode.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSSNTP-MIB",
    **{"fsSntpMIB": fsSntpMIB,
       "fsSntp": fsSntp,
       "fsSntpScalars": fsSntpScalars,
       "fsSntpGlobalTrace": fsSntpGlobalTrace,
       "fsSntpGlobalDebug": fsSntpGlobalDebug,
       "fsSntpAdminStatus": fsSntpAdminStatus,
       "fsSntpClientVersion": fsSntpClientVersion,
       "fsSntpClientAddressingMode": fsSntpClientAddressingMode,
       "fsSntpClientPort": fsSntpClientPort,
       "fsSntpTimeDisplayFormat": fsSntpTimeDisplayFormat,
       "fsSntpAuthKeyId": fsSntpAuthKeyId,
       "fsSntpAuthAlgorithm": fsSntpAuthAlgorithm,
       "fsSntpAuthKey": fsSntpAuthKey,
       "fsSntpTimeZone": fsSntpTimeZone,
       "fsSntpDSTStartTime": fsSntpDSTStartTime,
       "fsSntpDSTEndTime": fsSntpDSTEndTime,
       "fsSntpClientUptime": fsSntpClientUptime,
       "fsSntpClientStatus": fsSntpClientStatus,
       "fsSntpServerReplyRxCount": fsSntpServerReplyRxCount,
       "fsSntpClientReqTxCount": fsSntpClientReqTxCount,
       "fsSntpPktInDiscardCount": fsSntpPktInDiscardCount,
       "fsSntpUnicast": fsSntpUnicast,
       "fsSntpServerAutoDiscovery": fsSntpServerAutoDiscovery,
       "fsSntpUnicastPollInterval": fsSntpUnicastPollInterval,
       "fsSntpUnicastPollTimeout": fsSntpUnicastPollTimeout,
       "fsSntpUnicastPollRetry": fsSntpUnicastPollRetry,
       "fsSntpUnicastServerTable": fsSntpUnicastServerTable,
       "fsSntpUnicastServerEntry": fsSntpUnicastServerEntry,
       "fsSntpUnicastServerAddrType": fsSntpUnicastServerAddrType,
       "fsSntpUnicastServerAddr": fsSntpUnicastServerAddr,
       "fsSntpUnicastServerVersion": fsSntpUnicastServerVersion,
       "fsSntpUnicastServerPort": fsSntpUnicastServerPort,
       "fsSntpUnicastServerType": fsSntpUnicastServerType,
       "fsSntpUnicastServerLastUpdateTime": fsSntpUnicastServerLastUpdateTime,
       "fsSntpUnicastServerTxRequests": fsSntpUnicastServerTxRequests,
       "fsSntpUnicastServerRowStatus": fsSntpUnicastServerRowStatus,
       "fsSntpBroadcast": fsSntpBroadcast,
       "fsSntpSendRequestInBcastMode": fsSntpSendRequestInBcastMode,
       "fsSntpPollTimeoutInBcastMode": fsSntpPollTimeoutInBcastMode,
       "fsSntpDelayTimeInBcastMode": fsSntpDelayTimeInBcastMode,
       "fsSntpPrimaryServerAddrInBcastMode": fsSntpPrimaryServerAddrInBcastMode,
       "fsSntpSecondaryServerAddrInBcastMode": fsSntpSecondaryServerAddrInBcastMode,
       "fsSntpMulticast": fsSntpMulticast,
       "fsSntpSendRequestInMcastMode": fsSntpSendRequestInMcastMode,
       "fsSntpPollTimeoutInMcastMode": fsSntpPollTimeoutInMcastMode,
       "fsSntpDelayTimeInMcastMode": fsSntpDelayTimeInMcastMode,
       "fsSntpGrpAddrTypeInMcastMode": fsSntpGrpAddrTypeInMcastMode,
       "fsSntpGrpAddrInMcastMode": fsSntpGrpAddrInMcastMode,
       "fsSntpPrimaryServerAddrTypeInMcastMode": fsSntpPrimaryServerAddrTypeInMcastMode,
       "fsSntpPrimaryServerAddrInMcastMode": fsSntpPrimaryServerAddrInMcastMode,
       "fsSntpSecondaryServerAddrTypeInMcastMode": fsSntpSecondaryServerAddrTypeInMcastMode,
       "fsSntpSecondaryServerAddrInMcastMode": fsSntpSecondaryServerAddrInMcastMode,
       "fsSntpAnycast": fsSntpAnycast,
       "fsSntpAnycastPollInterval": fsSntpAnycastPollInterval,
       "fsSntpAnycastPollTimeout": fsSntpAnycastPollTimeout,
       "fsSntpAnycastPollRetry": fsSntpAnycastPollRetry,
       "fsSntpServerTypeInAcastMode": fsSntpServerTypeInAcastMode,
       "fsSntpGrpAddrTypeInAcastMode": fsSntpGrpAddrTypeInAcastMode,
       "fsSntpGrpAddrInAcastMode": fsSntpGrpAddrInAcastMode,
       "fsSntpPrimaryServerAddrTypeInAcastMode": fsSntpPrimaryServerAddrTypeInAcastMode,
       "fsSntpPrimaryServerAddrInAcastMode": fsSntpPrimaryServerAddrInAcastMode,
       "fsSntpSecondaryServerAddrTypeInAcastMode": fsSntpSecondaryServerAddrTypeInAcastMode,
       "fsSntpSecondaryServerAddrInAcastMode": fsSntpSecondaryServerAddrInAcastMode}
)
